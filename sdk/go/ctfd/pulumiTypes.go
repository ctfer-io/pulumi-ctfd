// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package ctfd

import (
	"context"
	"reflect"

	"github.com/ctfer-io/pulumi-ctfd/sdk/go/ctfd/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

var _ = internal.GetEnvOrDefault

type ChallengeRequirements struct {
	// Behavior if not unlocked, either hidden or anonymized.
	Behavior *string `pulumi:"behavior"`
	// List of the challenges ID.
	Prerequisites []string `pulumi:"prerequisites"`
}

// ChallengeRequirementsInput is an input type that accepts ChallengeRequirementsArgs and ChallengeRequirementsOutput values.
// You can construct a concrete instance of `ChallengeRequirementsInput` via:
//
//	ChallengeRequirementsArgs{...}
type ChallengeRequirementsInput interface {
	pulumi.Input

	ToChallengeRequirementsOutput() ChallengeRequirementsOutput
	ToChallengeRequirementsOutputWithContext(context.Context) ChallengeRequirementsOutput
}

type ChallengeRequirementsArgs struct {
	// Behavior if not unlocked, either hidden or anonymized.
	Behavior pulumi.StringPtrInput `pulumi:"behavior"`
	// List of the challenges ID.
	Prerequisites pulumi.StringArrayInput `pulumi:"prerequisites"`
}

func (ChallengeRequirementsArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*ChallengeRequirements)(nil)).Elem()
}

func (i ChallengeRequirementsArgs) ToChallengeRequirementsOutput() ChallengeRequirementsOutput {
	return i.ToChallengeRequirementsOutputWithContext(context.Background())
}

func (i ChallengeRequirementsArgs) ToChallengeRequirementsOutputWithContext(ctx context.Context) ChallengeRequirementsOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ChallengeRequirementsOutput)
}

func (i ChallengeRequirementsArgs) ToChallengeRequirementsPtrOutput() ChallengeRequirementsPtrOutput {
	return i.ToChallengeRequirementsPtrOutputWithContext(context.Background())
}

func (i ChallengeRequirementsArgs) ToChallengeRequirementsPtrOutputWithContext(ctx context.Context) ChallengeRequirementsPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ChallengeRequirementsOutput).ToChallengeRequirementsPtrOutputWithContext(ctx)
}

// ChallengeRequirementsPtrInput is an input type that accepts ChallengeRequirementsArgs, ChallengeRequirementsPtr and ChallengeRequirementsPtrOutput values.
// You can construct a concrete instance of `ChallengeRequirementsPtrInput` via:
//
//	        ChallengeRequirementsArgs{...}
//
//	or:
//
//	        nil
type ChallengeRequirementsPtrInput interface {
	pulumi.Input

	ToChallengeRequirementsPtrOutput() ChallengeRequirementsPtrOutput
	ToChallengeRequirementsPtrOutputWithContext(context.Context) ChallengeRequirementsPtrOutput
}

type challengeRequirementsPtrType ChallengeRequirementsArgs

func ChallengeRequirementsPtr(v *ChallengeRequirementsArgs) ChallengeRequirementsPtrInput {
	return (*challengeRequirementsPtrType)(v)
}

func (*challengeRequirementsPtrType) ElementType() reflect.Type {
	return reflect.TypeOf((**ChallengeRequirements)(nil)).Elem()
}

func (i *challengeRequirementsPtrType) ToChallengeRequirementsPtrOutput() ChallengeRequirementsPtrOutput {
	return i.ToChallengeRequirementsPtrOutputWithContext(context.Background())
}

func (i *challengeRequirementsPtrType) ToChallengeRequirementsPtrOutputWithContext(ctx context.Context) ChallengeRequirementsPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ChallengeRequirementsPtrOutput)
}

type ChallengeRequirementsOutput struct{ *pulumi.OutputState }

func (ChallengeRequirementsOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*ChallengeRequirements)(nil)).Elem()
}

func (o ChallengeRequirementsOutput) ToChallengeRequirementsOutput() ChallengeRequirementsOutput {
	return o
}

func (o ChallengeRequirementsOutput) ToChallengeRequirementsOutputWithContext(ctx context.Context) ChallengeRequirementsOutput {
	return o
}

func (o ChallengeRequirementsOutput) ToChallengeRequirementsPtrOutput() ChallengeRequirementsPtrOutput {
	return o.ToChallengeRequirementsPtrOutputWithContext(context.Background())
}

func (o ChallengeRequirementsOutput) ToChallengeRequirementsPtrOutputWithContext(ctx context.Context) ChallengeRequirementsPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, v ChallengeRequirements) *ChallengeRequirements {
		return &v
	}).(ChallengeRequirementsPtrOutput)
}

// Behavior if not unlocked, either hidden or anonymized.
func (o ChallengeRequirementsOutput) Behavior() pulumi.StringPtrOutput {
	return o.ApplyT(func(v ChallengeRequirements) *string { return v.Behavior }).(pulumi.StringPtrOutput)
}

// List of the challenges ID.
func (o ChallengeRequirementsOutput) Prerequisites() pulumi.StringArrayOutput {
	return o.ApplyT(func(v ChallengeRequirements) []string { return v.Prerequisites }).(pulumi.StringArrayOutput)
}

type ChallengeRequirementsPtrOutput struct{ *pulumi.OutputState }

func (ChallengeRequirementsPtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**ChallengeRequirements)(nil)).Elem()
}

func (o ChallengeRequirementsPtrOutput) ToChallengeRequirementsPtrOutput() ChallengeRequirementsPtrOutput {
	return o
}

func (o ChallengeRequirementsPtrOutput) ToChallengeRequirementsPtrOutputWithContext(ctx context.Context) ChallengeRequirementsPtrOutput {
	return o
}

func (o ChallengeRequirementsPtrOutput) Elem() ChallengeRequirementsOutput {
	return o.ApplyT(func(v *ChallengeRequirements) ChallengeRequirements {
		if v != nil {
			return *v
		}
		var ret ChallengeRequirements
		return ret
	}).(ChallengeRequirementsOutput)
}

// Behavior if not unlocked, either hidden or anonymized.
func (o ChallengeRequirementsPtrOutput) Behavior() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *ChallengeRequirements) *string {
		if v == nil {
			return nil
		}
		return v.Behavior
	}).(pulumi.StringPtrOutput)
}

// List of the challenges ID.
func (o ChallengeRequirementsPtrOutput) Prerequisites() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *ChallengeRequirements) []string {
		if v == nil {
			return nil
		}
		return v.Prerequisites
	}).(pulumi.StringArrayOutput)
}

type GetChallengesChallenge struct {
	// Category of the challenge that CTFd groups by on the web UI.
	Category string `pulumi:"category"`
	// Connection Information to connect to the challenge instance, useful for pwn or web pentest.
	ConnectionInfo string `pulumi:"connectionInfo"`
	Decay          int    `pulumi:"decay"`
	// Description of the challenge, consider using multiline descriptions for better style.
	Description string `pulumi:"description"`
	// Decay function to define how the challenge value evolve through solves, either linear or logarithmic.
	Function string `pulumi:"function"`
	// Identifier of the challenge.
	Id string `pulumi:"id"`
	// Maximum amount of attempts before being unable to flag the challenge.
	MaxAttempts int `pulumi:"maxAttempts"`
	Minimum     int `pulumi:"minimum"`
	// Name of the challenge, displayed as it.
	Name string `pulumi:"name"`
	// Suggestion for the end-user as next challenge to work on.
	Next int `pulumi:"next"`
	// List of required challenges that needs to get flagged before this one being accessible. Useful for skill-trees-like strategy CTF.
	Requirements GetChallengesChallengeRequirements `pulumi:"requirements"`
	// State of the challenge, either hidden or visible.
	State string `pulumi:"state"`
	// List of challenge tags that will be displayed to the end-user. You could use them to give some quick insights of what a challenge involves.
	Tags []string `pulumi:"tags"`
	// List of challenge topics that are displayed to the administrators for maintenance and planification.
	Topics []string `pulumi:"topics"`
	// Type of the challenge defining its layout, either standard or dynamic.
	Type  string `pulumi:"type"`
	Value int    `pulumi:"value"`
}

// GetChallengesChallengeInput is an input type that accepts GetChallengesChallengeArgs and GetChallengesChallengeOutput values.
// You can construct a concrete instance of `GetChallengesChallengeInput` via:
//
//	GetChallengesChallengeArgs{...}
type GetChallengesChallengeInput interface {
	pulumi.Input

	ToGetChallengesChallengeOutput() GetChallengesChallengeOutput
	ToGetChallengesChallengeOutputWithContext(context.Context) GetChallengesChallengeOutput
}

type GetChallengesChallengeArgs struct {
	// Category of the challenge that CTFd groups by on the web UI.
	Category pulumi.StringInput `pulumi:"category"`
	// Connection Information to connect to the challenge instance, useful for pwn or web pentest.
	ConnectionInfo pulumi.StringInput `pulumi:"connectionInfo"`
	Decay          pulumi.IntInput    `pulumi:"decay"`
	// Description of the challenge, consider using multiline descriptions for better style.
	Description pulumi.StringInput `pulumi:"description"`
	// Decay function to define how the challenge value evolve through solves, either linear or logarithmic.
	Function pulumi.StringInput `pulumi:"function"`
	// Identifier of the challenge.
	Id pulumi.StringInput `pulumi:"id"`
	// Maximum amount of attempts before being unable to flag the challenge.
	MaxAttempts pulumi.IntInput `pulumi:"maxAttempts"`
	Minimum     pulumi.IntInput `pulumi:"minimum"`
	// Name of the challenge, displayed as it.
	Name pulumi.StringInput `pulumi:"name"`
	// Suggestion for the end-user as next challenge to work on.
	Next pulumi.IntInput `pulumi:"next"`
	// List of required challenges that needs to get flagged before this one being accessible. Useful for skill-trees-like strategy CTF.
	Requirements GetChallengesChallengeRequirementsInput `pulumi:"requirements"`
	// State of the challenge, either hidden or visible.
	State pulumi.StringInput `pulumi:"state"`
	// List of challenge tags that will be displayed to the end-user. You could use them to give some quick insights of what a challenge involves.
	Tags pulumi.StringArrayInput `pulumi:"tags"`
	// List of challenge topics that are displayed to the administrators for maintenance and planification.
	Topics pulumi.StringArrayInput `pulumi:"topics"`
	// Type of the challenge defining its layout, either standard or dynamic.
	Type  pulumi.StringInput `pulumi:"type"`
	Value pulumi.IntInput    `pulumi:"value"`
}

func (GetChallengesChallengeArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*GetChallengesChallenge)(nil)).Elem()
}

func (i GetChallengesChallengeArgs) ToGetChallengesChallengeOutput() GetChallengesChallengeOutput {
	return i.ToGetChallengesChallengeOutputWithContext(context.Background())
}

func (i GetChallengesChallengeArgs) ToGetChallengesChallengeOutputWithContext(ctx context.Context) GetChallengesChallengeOutput {
	return pulumi.ToOutputWithContext(ctx, i).(GetChallengesChallengeOutput)
}

// GetChallengesChallengeArrayInput is an input type that accepts GetChallengesChallengeArray and GetChallengesChallengeArrayOutput values.
// You can construct a concrete instance of `GetChallengesChallengeArrayInput` via:
//
//	GetChallengesChallengeArray{ GetChallengesChallengeArgs{...} }
type GetChallengesChallengeArrayInput interface {
	pulumi.Input

	ToGetChallengesChallengeArrayOutput() GetChallengesChallengeArrayOutput
	ToGetChallengesChallengeArrayOutputWithContext(context.Context) GetChallengesChallengeArrayOutput
}

type GetChallengesChallengeArray []GetChallengesChallengeInput

func (GetChallengesChallengeArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]GetChallengesChallenge)(nil)).Elem()
}

func (i GetChallengesChallengeArray) ToGetChallengesChallengeArrayOutput() GetChallengesChallengeArrayOutput {
	return i.ToGetChallengesChallengeArrayOutputWithContext(context.Background())
}

func (i GetChallengesChallengeArray) ToGetChallengesChallengeArrayOutputWithContext(ctx context.Context) GetChallengesChallengeArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(GetChallengesChallengeArrayOutput)
}

type GetChallengesChallengeOutput struct{ *pulumi.OutputState }

func (GetChallengesChallengeOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*GetChallengesChallenge)(nil)).Elem()
}

func (o GetChallengesChallengeOutput) ToGetChallengesChallengeOutput() GetChallengesChallengeOutput {
	return o
}

func (o GetChallengesChallengeOutput) ToGetChallengesChallengeOutputWithContext(ctx context.Context) GetChallengesChallengeOutput {
	return o
}

// Category of the challenge that CTFd groups by on the web UI.
func (o GetChallengesChallengeOutput) Category() pulumi.StringOutput {
	return o.ApplyT(func(v GetChallengesChallenge) string { return v.Category }).(pulumi.StringOutput)
}

// Connection Information to connect to the challenge instance, useful for pwn or web pentest.
func (o GetChallengesChallengeOutput) ConnectionInfo() pulumi.StringOutput {
	return o.ApplyT(func(v GetChallengesChallenge) string { return v.ConnectionInfo }).(pulumi.StringOutput)
}

func (o GetChallengesChallengeOutput) Decay() pulumi.IntOutput {
	return o.ApplyT(func(v GetChallengesChallenge) int { return v.Decay }).(pulumi.IntOutput)
}

// Description of the challenge, consider using multiline descriptions for better style.
func (o GetChallengesChallengeOutput) Description() pulumi.StringOutput {
	return o.ApplyT(func(v GetChallengesChallenge) string { return v.Description }).(pulumi.StringOutput)
}

// Decay function to define how the challenge value evolve through solves, either linear or logarithmic.
func (o GetChallengesChallengeOutput) Function() pulumi.StringOutput {
	return o.ApplyT(func(v GetChallengesChallenge) string { return v.Function }).(pulumi.StringOutput)
}

// Identifier of the challenge.
func (o GetChallengesChallengeOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v GetChallengesChallenge) string { return v.Id }).(pulumi.StringOutput)
}

// Maximum amount of attempts before being unable to flag the challenge.
func (o GetChallengesChallengeOutput) MaxAttempts() pulumi.IntOutput {
	return o.ApplyT(func(v GetChallengesChallenge) int { return v.MaxAttempts }).(pulumi.IntOutput)
}

func (o GetChallengesChallengeOutput) Minimum() pulumi.IntOutput {
	return o.ApplyT(func(v GetChallengesChallenge) int { return v.Minimum }).(pulumi.IntOutput)
}

// Name of the challenge, displayed as it.
func (o GetChallengesChallengeOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v GetChallengesChallenge) string { return v.Name }).(pulumi.StringOutput)
}

// Suggestion for the end-user as next challenge to work on.
func (o GetChallengesChallengeOutput) Next() pulumi.IntOutput {
	return o.ApplyT(func(v GetChallengesChallenge) int { return v.Next }).(pulumi.IntOutput)
}

// List of required challenges that needs to get flagged before this one being accessible. Useful for skill-trees-like strategy CTF.
func (o GetChallengesChallengeOutput) Requirements() GetChallengesChallengeRequirementsOutput {
	return o.ApplyT(func(v GetChallengesChallenge) GetChallengesChallengeRequirements { return v.Requirements }).(GetChallengesChallengeRequirementsOutput)
}

// State of the challenge, either hidden or visible.
func (o GetChallengesChallengeOutput) State() pulumi.StringOutput {
	return o.ApplyT(func(v GetChallengesChallenge) string { return v.State }).(pulumi.StringOutput)
}

// List of challenge tags that will be displayed to the end-user. You could use them to give some quick insights of what a challenge involves.
func (o GetChallengesChallengeOutput) Tags() pulumi.StringArrayOutput {
	return o.ApplyT(func(v GetChallengesChallenge) []string { return v.Tags }).(pulumi.StringArrayOutput)
}

// List of challenge topics that are displayed to the administrators for maintenance and planification.
func (o GetChallengesChallengeOutput) Topics() pulumi.StringArrayOutput {
	return o.ApplyT(func(v GetChallengesChallenge) []string { return v.Topics }).(pulumi.StringArrayOutput)
}

// Type of the challenge defining its layout, either standard or dynamic.
func (o GetChallengesChallengeOutput) Type() pulumi.StringOutput {
	return o.ApplyT(func(v GetChallengesChallenge) string { return v.Type }).(pulumi.StringOutput)
}

func (o GetChallengesChallengeOutput) Value() pulumi.IntOutput {
	return o.ApplyT(func(v GetChallengesChallenge) int { return v.Value }).(pulumi.IntOutput)
}

type GetChallengesChallengeArrayOutput struct{ *pulumi.OutputState }

func (GetChallengesChallengeArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]GetChallengesChallenge)(nil)).Elem()
}

func (o GetChallengesChallengeArrayOutput) ToGetChallengesChallengeArrayOutput() GetChallengesChallengeArrayOutput {
	return o
}

func (o GetChallengesChallengeArrayOutput) ToGetChallengesChallengeArrayOutputWithContext(ctx context.Context) GetChallengesChallengeArrayOutput {
	return o
}

func (o GetChallengesChallengeArrayOutput) Index(i pulumi.IntInput) GetChallengesChallengeOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) GetChallengesChallenge {
		return vs[0].([]GetChallengesChallenge)[vs[1].(int)]
	}).(GetChallengesChallengeOutput)
}

type GetChallengesChallengeRequirements struct {
	// Behavior if not unlocked, either hidden or anonymized.
	Behavior string `pulumi:"behavior"`
	// List of the challenges ID.
	Prerequisites []string `pulumi:"prerequisites"`
}

// GetChallengesChallengeRequirementsInput is an input type that accepts GetChallengesChallengeRequirementsArgs and GetChallengesChallengeRequirementsOutput values.
// You can construct a concrete instance of `GetChallengesChallengeRequirementsInput` via:
//
//	GetChallengesChallengeRequirementsArgs{...}
type GetChallengesChallengeRequirementsInput interface {
	pulumi.Input

	ToGetChallengesChallengeRequirementsOutput() GetChallengesChallengeRequirementsOutput
	ToGetChallengesChallengeRequirementsOutputWithContext(context.Context) GetChallengesChallengeRequirementsOutput
}

type GetChallengesChallengeRequirementsArgs struct {
	// Behavior if not unlocked, either hidden or anonymized.
	Behavior pulumi.StringInput `pulumi:"behavior"`
	// List of the challenges ID.
	Prerequisites pulumi.StringArrayInput `pulumi:"prerequisites"`
}

func (GetChallengesChallengeRequirementsArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*GetChallengesChallengeRequirements)(nil)).Elem()
}

func (i GetChallengesChallengeRequirementsArgs) ToGetChallengesChallengeRequirementsOutput() GetChallengesChallengeRequirementsOutput {
	return i.ToGetChallengesChallengeRequirementsOutputWithContext(context.Background())
}

func (i GetChallengesChallengeRequirementsArgs) ToGetChallengesChallengeRequirementsOutputWithContext(ctx context.Context) GetChallengesChallengeRequirementsOutput {
	return pulumi.ToOutputWithContext(ctx, i).(GetChallengesChallengeRequirementsOutput)
}

type GetChallengesChallengeRequirementsOutput struct{ *pulumi.OutputState }

func (GetChallengesChallengeRequirementsOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*GetChallengesChallengeRequirements)(nil)).Elem()
}

func (o GetChallengesChallengeRequirementsOutput) ToGetChallengesChallengeRequirementsOutput() GetChallengesChallengeRequirementsOutput {
	return o
}

func (o GetChallengesChallengeRequirementsOutput) ToGetChallengesChallengeRequirementsOutputWithContext(ctx context.Context) GetChallengesChallengeRequirementsOutput {
	return o
}

// Behavior if not unlocked, either hidden or anonymized.
func (o GetChallengesChallengeRequirementsOutput) Behavior() pulumi.StringOutput {
	return o.ApplyT(func(v GetChallengesChallengeRequirements) string { return v.Behavior }).(pulumi.StringOutput)
}

// List of the challenges ID.
func (o GetChallengesChallengeRequirementsOutput) Prerequisites() pulumi.StringArrayOutput {
	return o.ApplyT(func(v GetChallengesChallengeRequirements) []string { return v.Prerequisites }).(pulumi.StringArrayOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*ChallengeRequirementsInput)(nil)).Elem(), ChallengeRequirementsArgs{})
	pulumi.RegisterInputType(reflect.TypeOf((*ChallengeRequirementsPtrInput)(nil)).Elem(), ChallengeRequirementsArgs{})
	pulumi.RegisterInputType(reflect.TypeOf((*GetChallengesChallengeInput)(nil)).Elem(), GetChallengesChallengeArgs{})
	pulumi.RegisterInputType(reflect.TypeOf((*GetChallengesChallengeArrayInput)(nil)).Elem(), GetChallengesChallengeArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*GetChallengesChallengeRequirementsInput)(nil)).Elem(), GetChallengesChallengeRequirementsArgs{})
	pulumi.RegisterOutputType(ChallengeRequirementsOutput{})
	pulumi.RegisterOutputType(ChallengeRequirementsPtrOutput{})
	pulumi.RegisterOutputType(GetChallengesChallengeOutput{})
	pulumi.RegisterOutputType(GetChallengesChallengeArrayOutput{})
	pulumi.RegisterOutputType(GetChallengesChallengeRequirementsOutput{})
}
