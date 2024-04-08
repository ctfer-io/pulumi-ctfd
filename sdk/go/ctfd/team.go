// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package ctfd

import (
	"context"
	"reflect"

	"errors"
	"github.com/ctfer-io/pulumi-ctfd/sdk/go/ctfd/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// CTFd defines a Team as a group of Users who will attend the Capture The Flag event.
//
// ## Example Usage
//
// <!--Start PulumiCodeChooser -->
// ```go
// package main
//
// import (
//
//	"github.com/ctfer-io/pulumi-ctfd/sdk/go/ctfd"
//	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
//
// )
//
//	func main() {
//		pulumi.Run(func(ctx *pulumi.Context) error {
//			ctfer, err := ctfd.NewUser(ctx, "ctfer", &ctfd.UserArgs{
//				Email:    pulumi.String("ctfer-io@protonmail.com"),
//				Password: pulumi.String("password"),
//			})
//			if err != nil {
//				return err
//			}
//			_, err = ctfd.NewTeam(ctx, "cybercombattants", &ctfd.TeamArgs{
//				Email:    pulumi.String("lucastesson@protonmail.com"),
//				Password: pulumi.String("password"),
//				Members: pulumi.StringArray{
//					ctfer.ID(),
//				},
//				Captain: ctfer.ID(),
//			})
//			if err != nil {
//				return err
//			}
//			return nil
//		})
//	}
//
// ```
// <!--End PulumiCodeChooser -->
type Team struct {
	pulumi.CustomResourceState

	// Affiliation to a company or agency.
	Affiliation pulumi.StringPtrOutput `pulumi:"affiliation"`
	// Is true if the team is banned from the CTF.
	Banned pulumi.BoolOutput `pulumi:"banned"`
	// Member who is captain of the team. Must be part of the members too. Note it could cause a fatal error in case of resource import with an inconsistent CTFd configuration i.e. if a team has no captain yet (should not be possible).
	Captain pulumi.StringOutput `pulumi:"captain"`
	// Country the team represent or is hail from.
	Country pulumi.StringPtrOutput `pulumi:"country"`
	// Email of the team.
	Email pulumi.StringOutput `pulumi:"email"`
	// Is true if the team is hidden to the participants.
	Hidden pulumi.BoolOutput `pulumi:"hidden"`
	// List of members (User), defined by their IDs.
	Members pulumi.StringArrayOutput `pulumi:"members"`
	// Name of the team.
	Name pulumi.StringOutput `pulumi:"name"`
	// Password of the team. Notice that during a CTF you may not want to update those to avoid defaulting team accesses.
	Password pulumi.StringOutput `pulumi:"password"`
	// Website, blog, or anything similar (displayed to other participants).
	Website pulumi.StringPtrOutput `pulumi:"website"`
}

// NewTeam registers a new resource with the given unique name, arguments, and options.
func NewTeam(ctx *pulumi.Context,
	name string, args *TeamArgs, opts ...pulumi.ResourceOption) (*Team, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Captain == nil {
		return nil, errors.New("invalid value for required argument 'Captain'")
	}
	if args.Email == nil {
		return nil, errors.New("invalid value for required argument 'Email'")
	}
	if args.Members == nil {
		return nil, errors.New("invalid value for required argument 'Members'")
	}
	if args.Password == nil {
		return nil, errors.New("invalid value for required argument 'Password'")
	}
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource Team
	err := ctx.RegisterResource("ctfd:index/team:Team", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetTeam gets an existing Team resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetTeam(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *TeamState, opts ...pulumi.ResourceOption) (*Team, error) {
	var resource Team
	err := ctx.ReadResource("ctfd:index/team:Team", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Team resources.
type teamState struct {
	// Affiliation to a company or agency.
	Affiliation *string `pulumi:"affiliation"`
	// Is true if the team is banned from the CTF.
	Banned *bool `pulumi:"banned"`
	// Member who is captain of the team. Must be part of the members too. Note it could cause a fatal error in case of resource import with an inconsistent CTFd configuration i.e. if a team has no captain yet (should not be possible).
	Captain *string `pulumi:"captain"`
	// Country the team represent or is hail from.
	Country *string `pulumi:"country"`
	// Email of the team.
	Email *string `pulumi:"email"`
	// Is true if the team is hidden to the participants.
	Hidden *bool `pulumi:"hidden"`
	// List of members (User), defined by their IDs.
	Members []string `pulumi:"members"`
	// Name of the team.
	Name *string `pulumi:"name"`
	// Password of the team. Notice that during a CTF you may not want to update those to avoid defaulting team accesses.
	Password *string `pulumi:"password"`
	// Website, blog, or anything similar (displayed to other participants).
	Website *string `pulumi:"website"`
}

type TeamState struct {
	// Affiliation to a company or agency.
	Affiliation pulumi.StringPtrInput
	// Is true if the team is banned from the CTF.
	Banned pulumi.BoolPtrInput
	// Member who is captain of the team. Must be part of the members too. Note it could cause a fatal error in case of resource import with an inconsistent CTFd configuration i.e. if a team has no captain yet (should not be possible).
	Captain pulumi.StringPtrInput
	// Country the team represent or is hail from.
	Country pulumi.StringPtrInput
	// Email of the team.
	Email pulumi.StringPtrInput
	// Is true if the team is hidden to the participants.
	Hidden pulumi.BoolPtrInput
	// List of members (User), defined by their IDs.
	Members pulumi.StringArrayInput
	// Name of the team.
	Name pulumi.StringPtrInput
	// Password of the team. Notice that during a CTF you may not want to update those to avoid defaulting team accesses.
	Password pulumi.StringPtrInput
	// Website, blog, or anything similar (displayed to other participants).
	Website pulumi.StringPtrInput
}

func (TeamState) ElementType() reflect.Type {
	return reflect.TypeOf((*teamState)(nil)).Elem()
}

type teamArgs struct {
	// Affiliation to a company or agency.
	Affiliation *string `pulumi:"affiliation"`
	// Is true if the team is banned from the CTF.
	Banned *bool `pulumi:"banned"`
	// Member who is captain of the team. Must be part of the members too. Note it could cause a fatal error in case of resource import with an inconsistent CTFd configuration i.e. if a team has no captain yet (should not be possible).
	Captain string `pulumi:"captain"`
	// Country the team represent or is hail from.
	Country *string `pulumi:"country"`
	// Email of the team.
	Email string `pulumi:"email"`
	// Is true if the team is hidden to the participants.
	Hidden *bool `pulumi:"hidden"`
	// List of members (User), defined by their IDs.
	Members []string `pulumi:"members"`
	// Name of the team.
	Name *string `pulumi:"name"`
	// Password of the team. Notice that during a CTF you may not want to update those to avoid defaulting team accesses.
	Password string `pulumi:"password"`
	// Website, blog, or anything similar (displayed to other participants).
	Website *string `pulumi:"website"`
}

// The set of arguments for constructing a Team resource.
type TeamArgs struct {
	// Affiliation to a company or agency.
	Affiliation pulumi.StringPtrInput
	// Is true if the team is banned from the CTF.
	Banned pulumi.BoolPtrInput
	// Member who is captain of the team. Must be part of the members too. Note it could cause a fatal error in case of resource import with an inconsistent CTFd configuration i.e. if a team has no captain yet (should not be possible).
	Captain pulumi.StringInput
	// Country the team represent or is hail from.
	Country pulumi.StringPtrInput
	// Email of the team.
	Email pulumi.StringInput
	// Is true if the team is hidden to the participants.
	Hidden pulumi.BoolPtrInput
	// List of members (User), defined by their IDs.
	Members pulumi.StringArrayInput
	// Name of the team.
	Name pulumi.StringPtrInput
	// Password of the team. Notice that during a CTF you may not want to update those to avoid defaulting team accesses.
	Password pulumi.StringInput
	// Website, blog, or anything similar (displayed to other participants).
	Website pulumi.StringPtrInput
}

func (TeamArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*teamArgs)(nil)).Elem()
}

type TeamInput interface {
	pulumi.Input

	ToTeamOutput() TeamOutput
	ToTeamOutputWithContext(ctx context.Context) TeamOutput
}

func (*Team) ElementType() reflect.Type {
	return reflect.TypeOf((**Team)(nil)).Elem()
}

func (i *Team) ToTeamOutput() TeamOutput {
	return i.ToTeamOutputWithContext(context.Background())
}

func (i *Team) ToTeamOutputWithContext(ctx context.Context) TeamOutput {
	return pulumi.ToOutputWithContext(ctx, i).(TeamOutput)
}

// TeamArrayInput is an input type that accepts TeamArray and TeamArrayOutput values.
// You can construct a concrete instance of `TeamArrayInput` via:
//
//	TeamArray{ TeamArgs{...} }
type TeamArrayInput interface {
	pulumi.Input

	ToTeamArrayOutput() TeamArrayOutput
	ToTeamArrayOutputWithContext(context.Context) TeamArrayOutput
}

type TeamArray []TeamInput

func (TeamArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Team)(nil)).Elem()
}

func (i TeamArray) ToTeamArrayOutput() TeamArrayOutput {
	return i.ToTeamArrayOutputWithContext(context.Background())
}

func (i TeamArray) ToTeamArrayOutputWithContext(ctx context.Context) TeamArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(TeamArrayOutput)
}

// TeamMapInput is an input type that accepts TeamMap and TeamMapOutput values.
// You can construct a concrete instance of `TeamMapInput` via:
//
//	TeamMap{ "key": TeamArgs{...} }
type TeamMapInput interface {
	pulumi.Input

	ToTeamMapOutput() TeamMapOutput
	ToTeamMapOutputWithContext(context.Context) TeamMapOutput
}

type TeamMap map[string]TeamInput

func (TeamMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Team)(nil)).Elem()
}

func (i TeamMap) ToTeamMapOutput() TeamMapOutput {
	return i.ToTeamMapOutputWithContext(context.Background())
}

func (i TeamMap) ToTeamMapOutputWithContext(ctx context.Context) TeamMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(TeamMapOutput)
}

type TeamOutput struct{ *pulumi.OutputState }

func (TeamOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Team)(nil)).Elem()
}

func (o TeamOutput) ToTeamOutput() TeamOutput {
	return o
}

func (o TeamOutput) ToTeamOutputWithContext(ctx context.Context) TeamOutput {
	return o
}

// Affiliation to a company or agency.
func (o TeamOutput) Affiliation() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Team) pulumi.StringPtrOutput { return v.Affiliation }).(pulumi.StringPtrOutput)
}

// Is true if the team is banned from the CTF.
func (o TeamOutput) Banned() pulumi.BoolOutput {
	return o.ApplyT(func(v *Team) pulumi.BoolOutput { return v.Banned }).(pulumi.BoolOutput)
}

// Member who is captain of the team. Must be part of the members too. Note it could cause a fatal error in case of resource import with an inconsistent CTFd configuration i.e. if a team has no captain yet (should not be possible).
func (o TeamOutput) Captain() pulumi.StringOutput {
	return o.ApplyT(func(v *Team) pulumi.StringOutput { return v.Captain }).(pulumi.StringOutput)
}

// Country the team represent or is hail from.
func (o TeamOutput) Country() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Team) pulumi.StringPtrOutput { return v.Country }).(pulumi.StringPtrOutput)
}

// Email of the team.
func (o TeamOutput) Email() pulumi.StringOutput {
	return o.ApplyT(func(v *Team) pulumi.StringOutput { return v.Email }).(pulumi.StringOutput)
}

// Is true if the team is hidden to the participants.
func (o TeamOutput) Hidden() pulumi.BoolOutput {
	return o.ApplyT(func(v *Team) pulumi.BoolOutput { return v.Hidden }).(pulumi.BoolOutput)
}

// List of members (User), defined by their IDs.
func (o TeamOutput) Members() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *Team) pulumi.StringArrayOutput { return v.Members }).(pulumi.StringArrayOutput)
}

// Name of the team.
func (o TeamOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *Team) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

// Password of the team. Notice that during a CTF you may not want to update those to avoid defaulting team accesses.
func (o TeamOutput) Password() pulumi.StringOutput {
	return o.ApplyT(func(v *Team) pulumi.StringOutput { return v.Password }).(pulumi.StringOutput)
}

// Website, blog, or anything similar (displayed to other participants).
func (o TeamOutput) Website() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Team) pulumi.StringPtrOutput { return v.Website }).(pulumi.StringPtrOutput)
}

type TeamArrayOutput struct{ *pulumi.OutputState }

func (TeamArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Team)(nil)).Elem()
}

func (o TeamArrayOutput) ToTeamArrayOutput() TeamArrayOutput {
	return o
}

func (o TeamArrayOutput) ToTeamArrayOutputWithContext(ctx context.Context) TeamArrayOutput {
	return o
}

func (o TeamArrayOutput) Index(i pulumi.IntInput) TeamOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *Team {
		return vs[0].([]*Team)[vs[1].(int)]
	}).(TeamOutput)
}

type TeamMapOutput struct{ *pulumi.OutputState }

func (TeamMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Team)(nil)).Elem()
}

func (o TeamMapOutput) ToTeamMapOutput() TeamMapOutput {
	return o
}

func (o TeamMapOutput) ToTeamMapOutputWithContext(ctx context.Context) TeamMapOutput {
	return o
}

func (o TeamMapOutput) MapIndex(k pulumi.StringInput) TeamOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *Team {
		return vs[0].(map[string]*Team)[vs[1].(string)]
	}).(TeamOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*TeamInput)(nil)).Elem(), &Team{})
	pulumi.RegisterInputType(reflect.TypeOf((*TeamArrayInput)(nil)).Elem(), TeamArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*TeamMapInput)(nil)).Elem(), TeamMap{})
	pulumi.RegisterOutputType(TeamOutput{})
	pulumi.RegisterOutputType(TeamArrayOutput{})
	pulumi.RegisterOutputType(TeamMapOutput{})
}
