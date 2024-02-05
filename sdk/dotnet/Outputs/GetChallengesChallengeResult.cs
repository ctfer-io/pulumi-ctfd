// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Ctfd.Outputs
{

    [OutputType]
    public sealed class GetChallengesChallengeResult
    {
        /// <summary>
        /// Category of the challenge that CTFd groups by on the web UI.
        /// </summary>
        public readonly string Category;
        /// <summary>
        /// Connection Information to connect to the challenge instance, useful for pwn or web pentest.
        /// </summary>
        public readonly string ConnectionInfo;
        public readonly int Decay;
        /// <summary>
        /// Description of the challenge, consider using multiline descriptions for better style.
        /// </summary>
        public readonly string Description;
        /// <summary>
        /// List of files given to players to flag the challenge.
        /// </summary>
        public readonly ImmutableArray<Outputs.GetChallengesChallengeFileResult> Files;
        /// <summary>
        /// List of challenge flags that solves it.
        /// </summary>
        public readonly ImmutableArray<Outputs.GetChallengesChallengeFlagResult> Flags;
        /// <summary>
        /// Decay function to define how the challenge value evolve through solves, either linear or logarithmic.
        /// </summary>
        public readonly string Function;
        /// <summary>
        /// List of hints about the challenge displayed to the end-user.
        /// </summary>
        public readonly ImmutableArray<Outputs.GetChallengesChallengeHintResult> Hints;
        /// <summary>
        /// Identifier of the challenge.
        /// </summary>
        public readonly string Id;
        public readonly int Initial;
        /// <summary>
        /// Maximum amount of attempts before being unable to flag the challenge.
        /// </summary>
        public readonly int MaxAttempts;
        public readonly int Minimum;
        /// <summary>
        /// Name of the challenge, displayed as it.
        /// </summary>
        public readonly string Name;
        /// <summary>
        /// List of required challenges that needs to get flagged before this one being accessible. Useful for skill-trees-like strategy CTF.
        /// </summary>
        public readonly Outputs.GetChallengesChallengeRequirementsResult Requirements;
        /// <summary>
        /// State of the challenge, either hidden or visible.
        /// </summary>
        public readonly string State;
        /// <summary>
        /// List of challenge tags that will be displayed to the end-user. You could use them to give some quick insights of what a challenge involves.
        /// </summary>
        public readonly ImmutableArray<string> Tags;
        /// <summary>
        /// List of challenge topics that are displayed to the administrators for maintenance and planification.
        /// </summary>
        public readonly ImmutableArray<string> Topics;
        /// <summary>
        /// Type of the challenge defining its layout, either standard or dynamic.
        /// </summary>
        public readonly string Type;
        public readonly int Value;

        [OutputConstructor]
        private GetChallengesChallengeResult(
            string category,

            string connectionInfo,

            int decay,

            string description,

            ImmutableArray<Outputs.GetChallengesChallengeFileResult> files,

            ImmutableArray<Outputs.GetChallengesChallengeFlagResult> flags,

            string function,

            ImmutableArray<Outputs.GetChallengesChallengeHintResult> hints,

            string id,

            int initial,

            int maxAttempts,

            int minimum,

            string name,

            Outputs.GetChallengesChallengeRequirementsResult requirements,

            string state,

            ImmutableArray<string> tags,

            ImmutableArray<string> topics,

            string type,

            int value)
        {
            Category = category;
            ConnectionInfo = connectionInfo;
            Decay = decay;
            Description = description;
            Files = files;
            Flags = flags;
            Function = function;
            Hints = hints;
            Id = id;
            Initial = initial;
            MaxAttempts = maxAttempts;
            Minimum = minimum;
            Name = name;
            Requirements = requirements;
            State = state;
            Tags = tags;
            Topics = topics;
            Type = type;
            Value = value;
        }
    }
}
