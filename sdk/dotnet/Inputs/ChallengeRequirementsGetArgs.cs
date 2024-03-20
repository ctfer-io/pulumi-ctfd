// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace CTFerio.Ctfd.Inputs
{

    public sealed class ChallengeRequirementsGetArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Behavior if not unlocked, either hidden or anonymized.
        /// </summary>
        [Input("behavior")]
        public Input<string>? Behavior { get; set; }

        [Input("prerequisites")]
        private InputList<string>? _prerequisites;

        /// <summary>
        /// List of the challenges ID.
        /// </summary>
        public InputList<string> Prerequisites
        {
            get => _prerequisites ?? (_prerequisites = new InputList<string>());
            set => _prerequisites = value;
        }

        public ChallengeRequirementsGetArgs()
        {
        }
        public static new ChallengeRequirementsGetArgs Empty => new ChallengeRequirementsGetArgs();
    }
}
