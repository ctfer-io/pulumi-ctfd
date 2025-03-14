// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package ctfd

import (
	"context"
	"reflect"

	"github.com/ctfer-io/pulumi-ctfd/sdk/v2/go/ctfd/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func GetUsers(ctx *pulumi.Context, opts ...pulumi.InvokeOption) (*GetUsersResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv GetUsersResult
	err := ctx.Invoke("ctfd:index/getUsers:getUsers", nil, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of values returned by getUsers.
type GetUsersResult struct {
	// Affiliation to a team, company or agency.
	Affiliation string `pulumi:"affiliation"`
	// Is true if the user is banned from the CTF.
	Banned bool `pulumi:"banned"`
	// Country the user represent or is native from.
	Country string `pulumi:"country"`
	// Email of the user, may be used to verify the account.
	Email string `pulumi:"email"`
	// Is true if the user is hidden to the participants.
	Hidden bool `pulumi:"hidden"`
	// Identifier of the user.
	Id string `pulumi:"id"`
	// Language the user is fluent in.
	Language string `pulumi:"language"`
	// Name or pseudo of the user.
	Name string `pulumi:"name"`
	// Password of the user. Notice that during a CTF you may not want to update those to avoid defaulting user accesses.
	Password string `pulumi:"password"`
	// Generic type for RBAC purposes.
	Type string `pulumi:"type"`
	// Is true if the user has verified its account by email, or if set by an admin.
	Verified bool `pulumi:"verified"`
	// Website, blog, or anything similar (displayed to other participants).
	Website string `pulumi:"website"`
}

func GetUsersOutput(ctx *pulumi.Context, opts ...pulumi.InvokeOption) GetUsersResultOutput {
	return pulumi.ToOutput(0).ApplyT(func(int) (GetUsersResultOutput, error) {
		options := pulumi.InvokeOutputOptions{InvokeOptions: internal.PkgInvokeDefaultOpts(opts)}
		return ctx.InvokeOutput("ctfd:index/getUsers:getUsers", nil, GetUsersResultOutput{}, options).(GetUsersResultOutput), nil
	}).(GetUsersResultOutput)
}

// A collection of values returned by getUsers.
type GetUsersResultOutput struct{ *pulumi.OutputState }

func (GetUsersResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*GetUsersResult)(nil)).Elem()
}

func (o GetUsersResultOutput) ToGetUsersResultOutput() GetUsersResultOutput {
	return o
}

func (o GetUsersResultOutput) ToGetUsersResultOutputWithContext(ctx context.Context) GetUsersResultOutput {
	return o
}

// Affiliation to a team, company or agency.
func (o GetUsersResultOutput) Affiliation() pulumi.StringOutput {
	return o.ApplyT(func(v GetUsersResult) string { return v.Affiliation }).(pulumi.StringOutput)
}

// Is true if the user is banned from the CTF.
func (o GetUsersResultOutput) Banned() pulumi.BoolOutput {
	return o.ApplyT(func(v GetUsersResult) bool { return v.Banned }).(pulumi.BoolOutput)
}

// Country the user represent or is native from.
func (o GetUsersResultOutput) Country() pulumi.StringOutput {
	return o.ApplyT(func(v GetUsersResult) string { return v.Country }).(pulumi.StringOutput)
}

// Email of the user, may be used to verify the account.
func (o GetUsersResultOutput) Email() pulumi.StringOutput {
	return o.ApplyT(func(v GetUsersResult) string { return v.Email }).(pulumi.StringOutput)
}

// Is true if the user is hidden to the participants.
func (o GetUsersResultOutput) Hidden() pulumi.BoolOutput {
	return o.ApplyT(func(v GetUsersResult) bool { return v.Hidden }).(pulumi.BoolOutput)
}

// Identifier of the user.
func (o GetUsersResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v GetUsersResult) string { return v.Id }).(pulumi.StringOutput)
}

// Language the user is fluent in.
func (o GetUsersResultOutput) Language() pulumi.StringOutput {
	return o.ApplyT(func(v GetUsersResult) string { return v.Language }).(pulumi.StringOutput)
}

// Name or pseudo of the user.
func (o GetUsersResultOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v GetUsersResult) string { return v.Name }).(pulumi.StringOutput)
}

// Password of the user. Notice that during a CTF you may not want to update those to avoid defaulting user accesses.
func (o GetUsersResultOutput) Password() pulumi.StringOutput {
	return o.ApplyT(func(v GetUsersResult) string { return v.Password }).(pulumi.StringOutput)
}

// Generic type for RBAC purposes.
func (o GetUsersResultOutput) Type() pulumi.StringOutput {
	return o.ApplyT(func(v GetUsersResult) string { return v.Type }).(pulumi.StringOutput)
}

// Is true if the user has verified its account by email, or if set by an admin.
func (o GetUsersResultOutput) Verified() pulumi.BoolOutput {
	return o.ApplyT(func(v GetUsersResult) bool { return v.Verified }).(pulumi.BoolOutput)
}

// Website, blog, or anything similar (displayed to other participants).
func (o GetUsersResultOutput) Website() pulumi.StringOutput {
	return o.ApplyT(func(v GetUsersResult) string { return v.Website }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterOutputType(GetUsersResultOutput{})
}
