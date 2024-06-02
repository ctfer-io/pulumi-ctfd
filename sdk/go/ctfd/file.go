// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package ctfd

import (
	"context"
	"reflect"

	"github.com/ctfer-io/pulumi-ctfd/sdk/go/ctfd/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// A CTFd file for a challenge.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
//
//	"encoding/base64"
//	"os"
//
//	"github.com/ctfer-io/pulumi-ctfd/sdk/go/ctfd"
//	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
//
// )
//
//	func filebase64OrPanic(path string) string {
//		if fileData, err := os.ReadFile(path); err == nil {
//			return base64.StdEncoding.EncodeToString(fileData[:])
//		} else {
//			panic(err.Error())
//		}
//	}
//
//	func main() {
//		pulumi.Run(func(ctx *pulumi.Context) error {
//			http, err := ctfd.NewChallenge(ctx, "http", &ctfd.ChallengeArgs{
//				Category:    pulumi.String("misc"),
//				Description: pulumi.String("..."),
//				Value:       pulumi.Int(500),
//				Decay:       pulumi.Int(100),
//				Minimum:     pulumi.Int(50),
//				State:       pulumi.String("visible"),
//				Function:    pulumi.String("logarithmic"),
//				Topics: pulumi.StringArray{
//					pulumi.String("Misc"),
//				},
//				Tags: pulumi.StringArray{
//					pulumi.String("misc"),
//					pulumi.String("basic"),
//				},
//			})
//			if err != nil {
//				return err
//			}
//			_, err = ctfd.NewFile(ctx, "httpFile", &ctfd.FileArgs{
//				ChallengeId: http.ID(),
//				Contentb64:  filebase64OrPanic(".../image.png"),
//			})
//			if err != nil {
//				return err
//			}
//			return nil
//		})
//	}
//
// ```
type File struct {
	pulumi.CustomResourceState

	// Challenge of the file.
	ChallengeId pulumi.StringPtrOutput `pulumi:"challengeId"`
	// Raw content of the file, perfectly fit the use-cases of a .txt document or anything with a simple binary content. You could provide it from the file-system using `file("${path.module}/...")`.
	Content pulumi.StringOutput `pulumi:"content"`
	// Base 64 content of the file, perfectly fit the use-cases of complex binaries. You could provide it from the file-system using `filebase64("${path.module}/...")`.
	Contentb64 pulumi.StringOutput `pulumi:"contentb64"`
	// Location where the file is stored on the CTFd instance, for download purposes.
	Location pulumi.StringOutput `pulumi:"location"`
	// Name of the file as displayed to end-users.
	Name pulumi.StringOutput `pulumi:"name"`
	// The sha1 sum of the file.
	Sha1sum pulumi.StringOutput `pulumi:"sha1sum"`
}

// NewFile registers a new resource with the given unique name, arguments, and options.
func NewFile(ctx *pulumi.Context,
	name string, args *FileArgs, opts ...pulumi.ResourceOption) (*File, error) {
	if args == nil {
		args = &FileArgs{}
	}

	if args.Content != nil {
		args.Content = pulumi.ToSecret(args.Content).(pulumi.StringPtrInput)
	}
	if args.Contentb64 != nil {
		args.Contentb64 = pulumi.ToSecret(args.Contentb64).(pulumi.StringPtrInput)
	}
	secrets := pulumi.AdditionalSecretOutputs([]string{
		"content",
		"contentb64",
	})
	opts = append(opts, secrets)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource File
	err := ctx.RegisterResource("ctfd:index/file:File", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetFile gets an existing File resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetFile(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *FileState, opts ...pulumi.ResourceOption) (*File, error) {
	var resource File
	err := ctx.ReadResource("ctfd:index/file:File", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering File resources.
type fileState struct {
	// Challenge of the file.
	ChallengeId *string `pulumi:"challengeId"`
	// Raw content of the file, perfectly fit the use-cases of a .txt document or anything with a simple binary content. You could provide it from the file-system using `file("${path.module}/...")`.
	Content *string `pulumi:"content"`
	// Base 64 content of the file, perfectly fit the use-cases of complex binaries. You could provide it from the file-system using `filebase64("${path.module}/...")`.
	Contentb64 *string `pulumi:"contentb64"`
	// Location where the file is stored on the CTFd instance, for download purposes.
	Location *string `pulumi:"location"`
	// Name of the file as displayed to end-users.
	Name *string `pulumi:"name"`
	// The sha1 sum of the file.
	Sha1sum *string `pulumi:"sha1sum"`
}

type FileState struct {
	// Challenge of the file.
	ChallengeId pulumi.StringPtrInput
	// Raw content of the file, perfectly fit the use-cases of a .txt document or anything with a simple binary content. You could provide it from the file-system using `file("${path.module}/...")`.
	Content pulumi.StringPtrInput
	// Base 64 content of the file, perfectly fit the use-cases of complex binaries. You could provide it from the file-system using `filebase64("${path.module}/...")`.
	Contentb64 pulumi.StringPtrInput
	// Location where the file is stored on the CTFd instance, for download purposes.
	Location pulumi.StringPtrInput
	// Name of the file as displayed to end-users.
	Name pulumi.StringPtrInput
	// The sha1 sum of the file.
	Sha1sum pulumi.StringPtrInput
}

func (FileState) ElementType() reflect.Type {
	return reflect.TypeOf((*fileState)(nil)).Elem()
}

type fileArgs struct {
	// Challenge of the file.
	ChallengeId *string `pulumi:"challengeId"`
	// Raw content of the file, perfectly fit the use-cases of a .txt document or anything with a simple binary content. You could provide it from the file-system using `file("${path.module}/...")`.
	Content *string `pulumi:"content"`
	// Base 64 content of the file, perfectly fit the use-cases of complex binaries. You could provide it from the file-system using `filebase64("${path.module}/...")`.
	Contentb64 *string `pulumi:"contentb64"`
	// Location where the file is stored on the CTFd instance, for download purposes.
	Location *string `pulumi:"location"`
	// Name of the file as displayed to end-users.
	Name *string `pulumi:"name"`
}

// The set of arguments for constructing a File resource.
type FileArgs struct {
	// Challenge of the file.
	ChallengeId pulumi.StringPtrInput
	// Raw content of the file, perfectly fit the use-cases of a .txt document or anything with a simple binary content. You could provide it from the file-system using `file("${path.module}/...")`.
	Content pulumi.StringPtrInput
	// Base 64 content of the file, perfectly fit the use-cases of complex binaries. You could provide it from the file-system using `filebase64("${path.module}/...")`.
	Contentb64 pulumi.StringPtrInput
	// Location where the file is stored on the CTFd instance, for download purposes.
	Location pulumi.StringPtrInput
	// Name of the file as displayed to end-users.
	Name pulumi.StringPtrInput
}

func (FileArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*fileArgs)(nil)).Elem()
}

type FileInput interface {
	pulumi.Input

	ToFileOutput() FileOutput
	ToFileOutputWithContext(ctx context.Context) FileOutput
}

func (*File) ElementType() reflect.Type {
	return reflect.TypeOf((**File)(nil)).Elem()
}

func (i *File) ToFileOutput() FileOutput {
	return i.ToFileOutputWithContext(context.Background())
}

func (i *File) ToFileOutputWithContext(ctx context.Context) FileOutput {
	return pulumi.ToOutputWithContext(ctx, i).(FileOutput)
}

// FileArrayInput is an input type that accepts FileArray and FileArrayOutput values.
// You can construct a concrete instance of `FileArrayInput` via:
//
//	FileArray{ FileArgs{...} }
type FileArrayInput interface {
	pulumi.Input

	ToFileArrayOutput() FileArrayOutput
	ToFileArrayOutputWithContext(context.Context) FileArrayOutput
}

type FileArray []FileInput

func (FileArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*File)(nil)).Elem()
}

func (i FileArray) ToFileArrayOutput() FileArrayOutput {
	return i.ToFileArrayOutputWithContext(context.Background())
}

func (i FileArray) ToFileArrayOutputWithContext(ctx context.Context) FileArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(FileArrayOutput)
}

// FileMapInput is an input type that accepts FileMap and FileMapOutput values.
// You can construct a concrete instance of `FileMapInput` via:
//
//	FileMap{ "key": FileArgs{...} }
type FileMapInput interface {
	pulumi.Input

	ToFileMapOutput() FileMapOutput
	ToFileMapOutputWithContext(context.Context) FileMapOutput
}

type FileMap map[string]FileInput

func (FileMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*File)(nil)).Elem()
}

func (i FileMap) ToFileMapOutput() FileMapOutput {
	return i.ToFileMapOutputWithContext(context.Background())
}

func (i FileMap) ToFileMapOutputWithContext(ctx context.Context) FileMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(FileMapOutput)
}

type FileOutput struct{ *pulumi.OutputState }

func (FileOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**File)(nil)).Elem()
}

func (o FileOutput) ToFileOutput() FileOutput {
	return o
}

func (o FileOutput) ToFileOutputWithContext(ctx context.Context) FileOutput {
	return o
}

// Challenge of the file.
func (o FileOutput) ChallengeId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *File) pulumi.StringPtrOutput { return v.ChallengeId }).(pulumi.StringPtrOutput)
}

// Raw content of the file, perfectly fit the use-cases of a .txt document or anything with a simple binary content. You could provide it from the file-system using `file("${path.module}/...")`.
func (o FileOutput) Content() pulumi.StringOutput {
	return o.ApplyT(func(v *File) pulumi.StringOutput { return v.Content }).(pulumi.StringOutput)
}

// Base 64 content of the file, perfectly fit the use-cases of complex binaries. You could provide it from the file-system using `filebase64("${path.module}/...")`.
func (o FileOutput) Contentb64() pulumi.StringOutput {
	return o.ApplyT(func(v *File) pulumi.StringOutput { return v.Contentb64 }).(pulumi.StringOutput)
}

// Location where the file is stored on the CTFd instance, for download purposes.
func (o FileOutput) Location() pulumi.StringOutput {
	return o.ApplyT(func(v *File) pulumi.StringOutput { return v.Location }).(pulumi.StringOutput)
}

// Name of the file as displayed to end-users.
func (o FileOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *File) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

// The sha1 sum of the file.
func (o FileOutput) Sha1sum() pulumi.StringOutput {
	return o.ApplyT(func(v *File) pulumi.StringOutput { return v.Sha1sum }).(pulumi.StringOutput)
}

type FileArrayOutput struct{ *pulumi.OutputState }

func (FileArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*File)(nil)).Elem()
}

func (o FileArrayOutput) ToFileArrayOutput() FileArrayOutput {
	return o
}

func (o FileArrayOutput) ToFileArrayOutputWithContext(ctx context.Context) FileArrayOutput {
	return o
}

func (o FileArrayOutput) Index(i pulumi.IntInput) FileOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *File {
		return vs[0].([]*File)[vs[1].(int)]
	}).(FileOutput)
}

type FileMapOutput struct{ *pulumi.OutputState }

func (FileMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*File)(nil)).Elem()
}

func (o FileMapOutput) ToFileMapOutput() FileMapOutput {
	return o
}

func (o FileMapOutput) ToFileMapOutputWithContext(ctx context.Context) FileMapOutput {
	return o
}

func (o FileMapOutput) MapIndex(k pulumi.StringInput) FileOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *File {
		return vs[0].(map[string]*File)[vs[1].(string)]
	}).(FileOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*FileInput)(nil)).Elem(), &File{})
	pulumi.RegisterInputType(reflect.TypeOf((*FileArrayInput)(nil)).Elem(), FileArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*FileMapInput)(nil)).Elem(), FileMap{})
	pulumi.RegisterOutputType(FileOutput{})
	pulumi.RegisterOutputType(FileArrayOutput{})
	pulumi.RegisterOutputType(FileMapOutput{})
}
