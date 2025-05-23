// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

// Export members:
export { BracketArgs, BracketState } from "./bracket";
export type Bracket = import("./bracket").Bracket;
export const Bracket: typeof import("./bracket").Bracket = null as any;
utilities.lazyLoad(exports, ["Bracket"], () => require("./bracket"));

export { ChallengeDynamicArgs, ChallengeDynamicState } from "./challengeDynamic";
export type ChallengeDynamic = import("./challengeDynamic").ChallengeDynamic;
export const ChallengeDynamic: typeof import("./challengeDynamic").ChallengeDynamic = null as any;
utilities.lazyLoad(exports, ["ChallengeDynamic"], () => require("./challengeDynamic"));

export { ChallengeStandardArgs, ChallengeStandardState } from "./challengeStandard";
export type ChallengeStandard = import("./challengeStandard").ChallengeStandard;
export const ChallengeStandard: typeof import("./challengeStandard").ChallengeStandard = null as any;
utilities.lazyLoad(exports, ["ChallengeStandard"], () => require("./challengeStandard"));

export { FileArgs, FileState } from "./file";
export type File = import("./file").File;
export const File: typeof import("./file").File = null as any;
utilities.lazyLoad(exports, ["File"], () => require("./file"));

export { FlagArgs, FlagState } from "./flag";
export type Flag = import("./flag").Flag;
export const Flag: typeof import("./flag").Flag = null as any;
utilities.lazyLoad(exports, ["Flag"], () => require("./flag"));

export { GetBracketsResult } from "./getBrackets";
export const getBrackets: typeof import("./getBrackets").getBrackets = null as any;
export const getBracketsOutput: typeof import("./getBrackets").getBracketsOutput = null as any;
utilities.lazyLoad(exports, ["getBrackets","getBracketsOutput"], () => require("./getBrackets"));

export { GetChallengesDynamicResult } from "./getChallengesDynamic";
export const getChallengesDynamic: typeof import("./getChallengesDynamic").getChallengesDynamic = null as any;
export const getChallengesDynamicOutput: typeof import("./getChallengesDynamic").getChallengesDynamicOutput = null as any;
utilities.lazyLoad(exports, ["getChallengesDynamic","getChallengesDynamicOutput"], () => require("./getChallengesDynamic"));

export { GetChallengesStandardResult } from "./getChallengesStandard";
export const getChallengesStandard: typeof import("./getChallengesStandard").getChallengesStandard = null as any;
export const getChallengesStandardOutput: typeof import("./getChallengesStandard").getChallengesStandardOutput = null as any;
utilities.lazyLoad(exports, ["getChallengesStandard","getChallengesStandardOutput"], () => require("./getChallengesStandard"));

export { GetTeamsResult } from "./getTeams";
export const getTeams: typeof import("./getTeams").getTeams = null as any;
export const getTeamsOutput: typeof import("./getTeams").getTeamsOutput = null as any;
utilities.lazyLoad(exports, ["getTeams","getTeamsOutput"], () => require("./getTeams"));

export { GetUsersResult } from "./getUsers";
export const getUsers: typeof import("./getUsers").getUsers = null as any;
export const getUsersOutput: typeof import("./getUsers").getUsersOutput = null as any;
utilities.lazyLoad(exports, ["getUsers","getUsersOutput"], () => require("./getUsers"));

export { HintArgs, HintState } from "./hint";
export type Hint = import("./hint").Hint;
export const Hint: typeof import("./hint").Hint = null as any;
utilities.lazyLoad(exports, ["Hint"], () => require("./hint"));

export { ProviderArgs } from "./provider";
export type Provider = import("./provider").Provider;
export const Provider: typeof import("./provider").Provider = null as any;
utilities.lazyLoad(exports, ["Provider"], () => require("./provider"));

export { TeamArgs, TeamState } from "./team";
export type Team = import("./team").Team;
export const Team: typeof import("./team").Team = null as any;
utilities.lazyLoad(exports, ["Team"], () => require("./team"));

export { UserArgs, UserState } from "./user";
export type User = import("./user").User;
export const User: typeof import("./user").User = null as any;
utilities.lazyLoad(exports, ["User"], () => require("./user"));


// Export sub-modules:
import * as config from "./config";
import * as types from "./types";

export {
    config,
    types,
};

const _module = {
    version: utilities.getVersion(),
    construct: (name: string, type: string, urn: string): pulumi.Resource => {
        switch (type) {
            case "ctfd:index/bracket:Bracket":
                return new Bracket(name, <any>undefined, { urn })
            case "ctfd:index/challengeDynamic:ChallengeDynamic":
                return new ChallengeDynamic(name, <any>undefined, { urn })
            case "ctfd:index/challengeStandard:ChallengeStandard":
                return new ChallengeStandard(name, <any>undefined, { urn })
            case "ctfd:index/file:File":
                return new File(name, <any>undefined, { urn })
            case "ctfd:index/flag:Flag":
                return new Flag(name, <any>undefined, { urn })
            case "ctfd:index/hint:Hint":
                return new Hint(name, <any>undefined, { urn })
            case "ctfd:index/team:Team":
                return new Team(name, <any>undefined, { urn })
            case "ctfd:index/user:User":
                return new User(name, <any>undefined, { urn })
            default:
                throw new Error(`unknown resource type ${type}`);
        }
    },
};
pulumi.runtime.registerResourceModule("ctfd", "index/bracket", _module)
pulumi.runtime.registerResourceModule("ctfd", "index/challengeDynamic", _module)
pulumi.runtime.registerResourceModule("ctfd", "index/challengeStandard", _module)
pulumi.runtime.registerResourceModule("ctfd", "index/file", _module)
pulumi.runtime.registerResourceModule("ctfd", "index/flag", _module)
pulumi.runtime.registerResourceModule("ctfd", "index/hint", _module)
pulumi.runtime.registerResourceModule("ctfd", "index/team", _module)
pulumi.runtime.registerResourceModule("ctfd", "index/user", _module)
pulumi.runtime.registerResourcePackage("ctfd", {
    version: utilities.getVersion(),
    constructProvider: (name: string, type: string, urn: string): pulumi.ProviderResource => {
        if (type !== "pulumi:providers:ctfd") {
            throw new Error(`unknown provider type ${type}`);
        }
        return new Provider(name, <any>undefined, { urn });
    },
});
