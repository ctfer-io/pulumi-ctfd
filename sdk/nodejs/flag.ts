// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * A flag to solve the challenge.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as ctfd from "@ctfer-io/pulumi-ctfd";
 *
 * const http = new ctfd.ChallengeDynamic("http", {
 *     category: "misc",
 *     description: "...",
 *     value: 500,
 *     decay: 100,
 *     minimum: 50,
 *     state: "visible",
 *     "function": "logarithmic",
 *     topics: ["Misc"],
 *     tags: [
 *         "misc",
 *         "basic",
 *     ],
 * });
 * const httpFlag = new ctfd.Flag("httpFlag", {
 *     challengeId: http.id,
 *     content: "CTF{some_flag}",
 * });
 * ```
 */
export class Flag extends pulumi.CustomResource {
    /**
     * Get an existing Flag resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: FlagState, opts?: pulumi.CustomResourceOptions): Flag {
        return new Flag(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'ctfd:index/flag:Flag';

    /**
     * Returns true if the given object is an instance of Flag.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Flag {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Flag.__pulumiType;
    }

    /**
     * Challenge of the flag.
     */
    public readonly challengeId!: pulumi.Output<string>;
    /**
     * The actual flag to match. Consider using the convention `MYCTF{value}` with `MYCTF` being the shortcode of your event's name and `value` depending on each challenge.
     */
    public readonly content!: pulumi.Output<string>;
    /**
     * The flag sensitivity information, either case*sensitive or case*insensitive
     */
    public readonly data!: pulumi.Output<string>;
    /**
     * The type of the flag, could be either static or regex
     */
    public readonly type!: pulumi.Output<string>;

    /**
     * Create a Flag resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: FlagArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: FlagArgs | FlagState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as FlagState | undefined;
            resourceInputs["challengeId"] = state ? state.challengeId : undefined;
            resourceInputs["content"] = state ? state.content : undefined;
            resourceInputs["data"] = state ? state.data : undefined;
            resourceInputs["type"] = state ? state.type : undefined;
        } else {
            const args = argsOrState as FlagArgs | undefined;
            if ((!args || args.challengeId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'challengeId'");
            }
            if ((!args || args.content === undefined) && !opts.urn) {
                throw new Error("Missing required property 'content'");
            }
            resourceInputs["challengeId"] = args ? args.challengeId : undefined;
            resourceInputs["content"] = args?.content ? pulumi.secret(args.content) : undefined;
            resourceInputs["data"] = args ? args.data : undefined;
            resourceInputs["type"] = args ? args.type : undefined;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const secretOpts = { additionalSecretOutputs: ["content"] };
        opts = pulumi.mergeOptions(opts, secretOpts);
        super(Flag.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Flag resources.
 */
export interface FlagState {
    /**
     * Challenge of the flag.
     */
    challengeId?: pulumi.Input<string>;
    /**
     * The actual flag to match. Consider using the convention `MYCTF{value}` with `MYCTF` being the shortcode of your event's name and `value` depending on each challenge.
     */
    content?: pulumi.Input<string>;
    /**
     * The flag sensitivity information, either case*sensitive or case*insensitive
     */
    data?: pulumi.Input<string>;
    /**
     * The type of the flag, could be either static or regex
     */
    type?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a Flag resource.
 */
export interface FlagArgs {
    /**
     * Challenge of the flag.
     */
    challengeId: pulumi.Input<string>;
    /**
     * The actual flag to match. Consider using the convention `MYCTF{value}` with `MYCTF` being the shortcode of your event's name and `value` depending on each challenge.
     */
    content: pulumi.Input<string>;
    /**
     * The flag sensitivity information, either case*sensitive or case*insensitive
     */
    data?: pulumi.Input<string>;
    /**
     * The type of the flag, could be either static or regex
     */
    type?: pulumi.Input<string>;
}
