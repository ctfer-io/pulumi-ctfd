// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

export function getChallenges(opts?: pulumi.InvokeOptions): Promise<GetChallengesResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("ctfd:index/getChallenges:getChallenges", {
    }, opts);
}

/**
 * A collection of values returned by getChallenges.
 */
export interface GetChallengesResult {
    readonly challenges: outputs.GetChallengesChallenge[];
    /**
     * The ID of this resource.
     */
    readonly id: string;
}
export function getChallengesOutput(opts?: pulumi.InvokeOptions): pulumi.Output<GetChallengesResult> {
    return pulumi.output(getChallenges(opts))
}
