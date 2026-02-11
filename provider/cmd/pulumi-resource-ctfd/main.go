// Copyright 2016-2018, Pulumi Corporation.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

//go:generate go run ./generate.go

package main

import (
	"context"
	_ "embed"
	"log"
	"os"
	"os/signal"
	"syscall"

	ctfd "github.com/ctfer-io/pulumi-ctfd/provider/v2"
	"github.com/ctfer-io/pulumi-ctfd/provider/v2/pkg/version"
	"github.com/pulumi/pulumi-terraform-bridge/v3/pkg/pf/tfbridge"
	"go.opentelemetry.io/contrib/exporters/autoexport"
	"go.opentelemetry.io/otel"
	"go.opentelemetry.io/otel/attribute"
	"go.opentelemetry.io/otel/propagation"
	"go.opentelemetry.io/otel/sdk/resource"
	sdktrace "go.opentelemetry.io/otel/sdk/trace"
	semconv "go.opentelemetry.io/otel/semconv/v1.39.0"
	"go.opentelemetry.io/otel/trace"
	"go.uber.org/multierr"
)

//go:embed schema-embed.json
var pulumiSchema []byte

func main() {
	ctx := context.Background()

	out, err := SetupOTelSDK(ctx, version.Version)
	if err != nil {
		log.Fatal(err)
	}

	// Set up signal handler to catch termination
	sigChan := make(chan os.Signal, 1)
	signal.Notify(sigChan, syscall.SIGTERM, syscall.SIGINT)

	// Cleanup function
	cleanup := func() {
		if err := out.Shutdown(context.WithoutCancel(ctx)); err != nil {
			log.Printf("Error shutting down tracer provider: %s", err)
		}
	}

	// Handle signals in a goroutine
	go func() {
		<-sigChan
		cleanup()
		os.Exit(0)
	}()

	// Also cleanup on normal exit
	defer cleanup()

	// Create startup span
	tracer := otel.Tracer(serviceName)
	ctx, span := tracer.Start(ctx, "startup")
	span.SetAttributes(attribute.String("provider.version", version.Version))
	defer span.End()

	tfbridge.Main(ctx, "ctfd", ctfd.Provider(ctx, out.TracerProvider), tfbridge.ProviderMetadata{
		PackageSchema: pulumiSchema,
	})
}

const (
	serviceName = "pulumi-ctfd"
)

type OTelSetup struct {
	Shutdown       func(context.Context) error
	TracerProvider trace.TracerProvider
}

func SetupOTelSDK(ctx context.Context, version string) (out OTelSetup, err error) {
	var shutdownFuncs []func(context.Context) error

	// shutdown calls cleanup functions registered via shutdownFuncs.
	// The errors from the calls are joined.
	// Each registered cleanup will be invoked once.
	out.Shutdown = func(ctx context.Context) error {
		var err error
		for _, fn := range shutdownFuncs {
			err = multierr.Append(err, fn(ctx))
		}
		shutdownFuncs = nil
		return err
	}

	// handleErr calls shutdown for cleanup and makes sure that all errors are returned.
	handleErr := func(inErr error) {
		err = multierr.Append(inErr, out.Shutdown(ctx))
	}

	// Set up propagator
	prop := propagation.NewCompositeTextMapPropagator(
		propagation.TraceContext{},
		propagation.Baggage{},
	)
	otel.SetTextMapPropagator(prop)

	// Ensure default SDK resources and the required service name are set
	r, err := resource.Merge(
		resource.Environment(),
		resource.NewWithAttributes(
			semconv.SchemaURL,
			semconv.ServiceName(serviceName), // override service name
			semconv.ServiceVersion(version),  // override service version
		),
	)
	if err != nil {
		return
	}

	// Set up trace provider
	exp, err := autoexport.NewSpanExporter(ctx)
	if err != nil {
		handleErr(err)
		return
	}
	shutdownFuncs = append(shutdownFuncs, exp.Shutdown)

	out.TracerProvider = sdktrace.NewTracerProvider(
		// We need to have the burden of a simple span processor as the process might be short-lived
		// because a batch processor can not give enough time to export data...
		sdktrace.WithSpanProcessor(sdktrace.NewSimpleSpanProcessor(exp)),
		sdktrace.WithResource(r),
	)

	return
}
