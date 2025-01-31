// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace CTFerio.Ctfd.Outputs
{

    [OutputType]
    public sealed class ChallengeStandardRequirements
    {
        /// <summary>
        /// Behavior if not unlocked, either hidden or anonymized.
        /// </summary>
        public readonly string? Behavior;
        /// <summary>
        /// List of the challenges ID.
        /// </summary>
        public readonly ImmutableArray<string> Prerequisites;

        [OutputConstructor]
        private ChallengeStandardRequirements(
            string? behavior,

            ImmutableArray<string> prerequisites)
        {
            Behavior = behavior;
            Prerequisites = prerequisites;
        }
    }
}
