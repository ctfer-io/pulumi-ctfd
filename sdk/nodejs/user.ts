// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * CTFd defines a User as someone who will either play or administrate the Capture The Flag event.
 *
 * ## Import
 *
 * User can be imported by the CTFd ID (check URLs)
 *
 * ```sh
 * $ pulumi import ctfd:index/user:User ctfer 1
 * ```
 */
export class User extends pulumi.CustomResource {
    /**
     * Get an existing User resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: UserState, opts?: pulumi.CustomResourceOptions): User {
        return new User(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'ctfd:index/user:User';

    /**
     * Returns true if the given object is an instance of User.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is User {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === User.__pulumiType;
    }

    /**
     * Affiliation to a team, company or agency.
     */
    public readonly affiliation!: pulumi.Output<string | undefined>;
    /**
     * Is true if the user is banned from the CTF.
     */
    public readonly banned!: pulumi.Output<boolean>;
    /**
     * Country the user represent or is native from.
     */
    public readonly country!: pulumi.Output<string | undefined>;
    /**
     * Email of the user, may be used to verify the account.
     */
    public readonly email!: pulumi.Output<string>;
    /**
     * Is true if the user is hidden to the participants.
     */
    public readonly hidden!: pulumi.Output<boolean>;
    /**
     * Language the user is fluent in.
     */
    public readonly language!: pulumi.Output<string | undefined>;
    /**
     * Name or pseudo of the user.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * Password of the user. Notice than during a CTF you may not want to update those to avoid defaulting user accesses.
     */
    public readonly password!: pulumi.Output<string>;
    /**
     * Generic type for RBAC purposes.
     */
    public readonly type!: pulumi.Output<string>;
    /**
     * Is true if the user has verified its account by email, or if set by an admin.
     */
    public readonly verified!: pulumi.Output<boolean>;
    /**
     * Website, blog, or anything similar (displayed to other participants).
     */
    public readonly website!: pulumi.Output<string | undefined>;

    /**
     * Create a User resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: UserArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: UserArgs | UserState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as UserState | undefined;
            resourceInputs["affiliation"] = state ? state.affiliation : undefined;
            resourceInputs["banned"] = state ? state.banned : undefined;
            resourceInputs["country"] = state ? state.country : undefined;
            resourceInputs["email"] = state ? state.email : undefined;
            resourceInputs["hidden"] = state ? state.hidden : undefined;
            resourceInputs["language"] = state ? state.language : undefined;
            resourceInputs["name"] = state ? state.name : undefined;
            resourceInputs["password"] = state ? state.password : undefined;
            resourceInputs["type"] = state ? state.type : undefined;
            resourceInputs["verified"] = state ? state.verified : undefined;
            resourceInputs["website"] = state ? state.website : undefined;
        } else {
            const args = argsOrState as UserArgs | undefined;
            if ((!args || args.email === undefined) && !opts.urn) {
                throw new Error("Missing required property 'email'");
            }
            if ((!args || args.password === undefined) && !opts.urn) {
                throw new Error("Missing required property 'password'");
            }
            resourceInputs["affiliation"] = args ? args.affiliation : undefined;
            resourceInputs["banned"] = args ? args.banned : undefined;
            resourceInputs["country"] = args ? args.country : undefined;
            resourceInputs["email"] = args?.email ? pulumi.secret(args.email) : undefined;
            resourceInputs["hidden"] = args ? args.hidden : undefined;
            resourceInputs["language"] = args ? args.language : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["password"] = args?.password ? pulumi.secret(args.password) : undefined;
            resourceInputs["type"] = args ? args.type : undefined;
            resourceInputs["verified"] = args ? args.verified : undefined;
            resourceInputs["website"] = args ? args.website : undefined;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const secretOpts = { additionalSecretOutputs: ["email", "password"] };
        opts = pulumi.mergeOptions(opts, secretOpts);
        super(User.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering User resources.
 */
export interface UserState {
    /**
     * Affiliation to a team, company or agency.
     */
    affiliation?: pulumi.Input<string>;
    /**
     * Is true if the user is banned from the CTF.
     */
    banned?: pulumi.Input<boolean>;
    /**
     * Country the user represent or is native from.
     */
    country?: pulumi.Input<string>;
    /**
     * Email of the user, may be used to verify the account.
     */
    email?: pulumi.Input<string>;
    /**
     * Is true if the user is hidden to the participants.
     */
    hidden?: pulumi.Input<boolean>;
    /**
     * Language the user is fluent in.
     */
    language?: pulumi.Input<string>;
    /**
     * Name or pseudo of the user.
     */
    name?: pulumi.Input<string>;
    /**
     * Password of the user. Notice than during a CTF you may not want to update those to avoid defaulting user accesses.
     */
    password?: pulumi.Input<string>;
    /**
     * Generic type for RBAC purposes.
     */
    type?: pulumi.Input<string>;
    /**
     * Is true if the user has verified its account by email, or if set by an admin.
     */
    verified?: pulumi.Input<boolean>;
    /**
     * Website, blog, or anything similar (displayed to other participants).
     */
    website?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a User resource.
 */
export interface UserArgs {
    /**
     * Affiliation to a team, company or agency.
     */
    affiliation?: pulumi.Input<string>;
    /**
     * Is true if the user is banned from the CTF.
     */
    banned?: pulumi.Input<boolean>;
    /**
     * Country the user represent or is native from.
     */
    country?: pulumi.Input<string>;
    /**
     * Email of the user, may be used to verify the account.
     */
    email: pulumi.Input<string>;
    /**
     * Is true if the user is hidden to the participants.
     */
    hidden?: pulumi.Input<boolean>;
    /**
     * Language the user is fluent in.
     */
    language?: pulumi.Input<string>;
    /**
     * Name or pseudo of the user.
     */
    name?: pulumi.Input<string>;
    /**
     * Password of the user. Notice than during a CTF you may not want to update those to avoid defaulting user accesses.
     */
    password: pulumi.Input<string>;
    /**
     * Generic type for RBAC purposes.
     */
    type?: pulumi.Input<string>;
    /**
     * Is true if the user has verified its account by email, or if set by an admin.
     */
    verified?: pulumi.Input<boolean>;
    /**
     * Website, blog, or anything similar (displayed to other participants).
     */
    website?: pulumi.Input<string>;
}