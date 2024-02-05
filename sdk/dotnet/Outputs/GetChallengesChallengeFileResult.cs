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
    public sealed class GetChallengesChallengeFileResult
    {
        public readonly string Content;
        public readonly string Contentb64;
        public readonly string Id;
        public readonly string Location;
        public readonly string Name;

        [OutputConstructor]
        private GetChallengesChallengeFileResult(
            string content,

            string contentb64,

            string id,

            string location,

            string name)
        {
            Content = content;
            Contentb64 = contentb64;
            Id = id;
            Location = location;
            Name = name;
        }
    }
}
