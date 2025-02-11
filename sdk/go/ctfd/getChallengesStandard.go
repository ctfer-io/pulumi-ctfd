// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package ctfd

import (
	"context"
	"reflect"

	"github.com/ctfer-io/pulumi-ctfd/sdk/v2/go/ctfd/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func GetChallengesStandard(ctx *pulumi.Context, opts ...pulumi.InvokeOption) (*GetChallengesStandardResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv GetChallengesStandardResult
	err := ctx.Invoke("ctfd:index/getChallengesStandard:getChallengesStandard", nil, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of values returned by getChallengesStandard.
type GetChallengesStandardResult struct {
	Challenges []GetChallengesStandardChallenge `pulumi:"challenges"`
	// The ID of this resource.
	Id string `pulumi:"id"`
}

func GetChallengesStandardOutput(ctx *pulumi.Context, opts ...pulumi.InvokeOption) GetChallengesStandardResultOutput {
	return pulumi.ToOutput(0).ApplyT(func(int) (GetChallengesStandardResultOutput, error) {
		options := pulumi.InvokeOutputOptions{InvokeOptions: internal.PkgInvokeDefaultOpts(opts)}
		return ctx.InvokeOutput("ctfd:index/getChallengesStandard:getChallengesStandard", nil, GetChallengesStandardResultOutput{}, options).(GetChallengesStandardResultOutput), nil
	}).(GetChallengesStandardResultOutput)
}

// A collection of values returned by getChallengesStandard.
type GetChallengesStandardResultOutput struct{ *pulumi.OutputState }

func (GetChallengesStandardResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*GetChallengesStandardResult)(nil)).Elem()
}

func (o GetChallengesStandardResultOutput) ToGetChallengesStandardResultOutput() GetChallengesStandardResultOutput {
	return o
}

func (o GetChallengesStandardResultOutput) ToGetChallengesStandardResultOutputWithContext(ctx context.Context) GetChallengesStandardResultOutput {
	return o
}

func (o GetChallengesStandardResultOutput) Challenges() GetChallengesStandardChallengeArrayOutput {
	return o.ApplyT(func(v GetChallengesStandardResult) []GetChallengesStandardChallenge { return v.Challenges }).(GetChallengesStandardChallengeArrayOutput)
}

// The ID of this resource.
func (o GetChallengesStandardResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v GetChallengesStandardResult) string { return v.Id }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterOutputType(GetChallengesStandardResultOutput{})
}
