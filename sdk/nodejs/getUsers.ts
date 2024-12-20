// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

export function getUsers(opts?: pulumi.InvokeOptions): Promise<GetUsersResult> {
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("ctfd:index/getUsers:getUsers", {
    }, opts);
}

/**
 * A collection of values returned by getUsers.
 */
export interface GetUsersResult {
    /**
     * Affiliation to a team, company or agency.
     */
    readonly affiliation: string;
    /**
     * Is true if the user is banned from the CTF.
     */
    readonly banned: boolean;
    /**
     * Country the user represent or is native from.
     */
    readonly country: string;
    /**
     * Email of the user, may be used to verify the account.
     */
    readonly email: string;
    /**
     * Is true if the user is hidden to the participants.
     */
    readonly hidden: boolean;
    /**
     * Identifier of the user.
     */
    readonly id: string;
    /**
     * Language the user is fluent in.
     */
    readonly language: string;
    /**
     * Name or pseudo of the user.
     */
    readonly name: string;
    /**
     * Password of the user. Notice that during a CTF you may not want to update those to avoid defaulting user accesses.
     */
    readonly password: string;
    /**
     * Generic type for RBAC purposes.
     */
    readonly type: string;
    /**
     * Is true if the user has verified its account by email, or if set by an admin.
     */
    readonly verified: boolean;
    /**
     * Website, blog, or anything similar (displayed to other participants).
     */
    readonly website: string;
}
export function getUsersOutput(opts?: pulumi.InvokeOutputOptions): pulumi.Output<GetUsersResult> {
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invokeOutput("ctfd:index/getUsers:getUsers", {
    }, opts);
}
