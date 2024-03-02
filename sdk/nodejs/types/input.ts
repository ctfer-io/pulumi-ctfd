// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";

export interface ChallengeFile {
    /**
     * Raw content of the file, perfectly fit the use-cases of a .txt document or anything with a simple binary content. You could provide it from the file-system using `file("${path.module}/...")`.
     */
    content?: pulumi.Input<string>;
    /**
     * Base 64 content of the file, perfectly fit the use-cases of complex binaries. You could provide it from the file-system using `filebase64("${path.module}/...")`.
     */
    contentb64?: pulumi.Input<string>;
    /**
     * Identifier of the file, used internally to handle the CTFd corresponding object.
     */
    id?: pulumi.Input<string>;
    /**
     * Location where the file is stored on the CTFd instance, for download purposes.
     */
    location?: pulumi.Input<string>;
    /**
     * Name of the file as displayed to end-users.
     */
    name: pulumi.Input<string>;
    /**
     * The sha1 sum of the file.
     */
    sha1sum?: pulumi.Input<string>;
}

export interface ChallengeFlag {
    /**
     * The actual flag to match. Consider using the convention `MYCTF{value}` with `MYCTF` being the shortcode of your event's name and `value` depending on each challenge.
     */
    content: pulumi.Input<string>;
    /**
     * The flag sensitivity information, either case*sensitive or case*insensitive
     */
    data?: pulumi.Input<string>;
    /**
     * Identifier of the flag, used internally to handle the CTFd corresponding object.
     */
    id?: pulumi.Input<string>;
    /**
     * The type of the flag, could be either static or regex
     */
    type?: pulumi.Input<string>;
}

export interface ChallengeHint {
    /**
     * Content of the hint as displayed to the end-user.
     */
    content: pulumi.Input<string>;
    /**
     * Cost of the hint, and if any specified, the end-user will consume its own (or team) points to get it.
     */
    cost?: pulumi.Input<number>;
    /**
     * Identifier of the hint, used internally to handle the CTFd corresponding object.
     */
    id?: pulumi.Input<string>;
    /**
     * Other hints required to be consumed before getting this one. Useful for cost-increasing hint strategies with more and more help.
     */
    requirements?: pulumi.Input<pulumi.Input<string>[]>;
}

export interface ChallengeRequirements {
    /**
     * Behavior if not unlocked, either hidden or anonymized.
     */
    behavior?: pulumi.Input<string>;
    /**
     * List of the challenges ID.
     */
    prerequisites?: pulumi.Input<pulumi.Input<string>[]>;
}

