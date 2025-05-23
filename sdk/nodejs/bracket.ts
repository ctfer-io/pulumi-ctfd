// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * A bracket for users or teams to compete in parallel.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as ctfd from "@ctfer-io/pulumi-ctfd";
 *
 * const juniors = new ctfd.Bracket("juniors", {
 *     description: "Bracket for 14-25 years old players.",
 *     type: "users",
 * });
 * const player1 = new ctfd.User("player1", {
 *     email: "player1@ctfer.io",
 *     password: "password",
 *     bracketId: juniors.id,
 * });
 * ```
 */
export class Bracket extends pulumi.CustomResource {
    /**
     * Get an existing Bracket resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: BracketState, opts?: pulumi.CustomResourceOptions): Bracket {
        return new Bracket(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'ctfd:index/bracket:Bracket';

    /**
     * Returns true if the given object is an instance of Bracket.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Bracket {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Bracket.__pulumiType;
    }

    /**
     * Description that explains the goal of this bracket.
     */
    public readonly description!: pulumi.Output<string | undefined>;
    /**
     * Name displayed to end-users (e.g. "Students", "Interns", "Engineers").
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * Type of the bracket, either "users" or "teams".
     */
    public readonly type!: pulumi.Output<string>;

    /**
     * Create a Bracket resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: BracketArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: BracketArgs | BracketState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as BracketState | undefined;
            resourceInputs["description"] = state ? state.description : undefined;
            resourceInputs["name"] = state ? state.name : undefined;
            resourceInputs["type"] = state ? state.type : undefined;
        } else {
            const args = argsOrState as BracketArgs | undefined;
            resourceInputs["description"] = args ? args.description : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["type"] = args ? args.type : undefined;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(Bracket.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Bracket resources.
 */
export interface BracketState {
    /**
     * Description that explains the goal of this bracket.
     */
    description?: pulumi.Input<string>;
    /**
     * Name displayed to end-users (e.g. "Students", "Interns", "Engineers").
     */
    name?: pulumi.Input<string>;
    /**
     * Type of the bracket, either "users" or "teams".
     */
    type?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a Bracket resource.
 */
export interface BracketArgs {
    /**
     * Description that explains the goal of this bracket.
     */
    description?: pulumi.Input<string>;
    /**
     * Name displayed to end-users (e.g. "Students", "Interns", "Engineers").
     */
    name?: pulumi.Input<string>;
    /**
     * Type of the bracket, either "users" or "teams".
     */
    type?: pulumi.Input<string>;
}
