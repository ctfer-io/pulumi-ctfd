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
    public sealed class ChallengeFile
    {
        /// <summary>
        /// Raw content of the file, perfectly fit the use-cases of a .txt document or anything with a simple binary content. You could provide it from the file-system using `file("${path.module}/...")`.
        /// </summary>
        public readonly string? Content;
        /// <summary>
        /// Base 64 content of the file, perfectly fit the use-cases of complex binaries. You could provide it from the file-system using `filebase64("${path.module}/...")`.
        /// </summary>
        public readonly string? Contentb64;
        /// <summary>
        /// Identifier of the file, used internally to handle the CTFd corresponding object.
        /// </summary>
        public readonly string? Id;
        /// <summary>
        /// Location where the file is stored on the CTFd instance, for download purposes.
        /// </summary>
        public readonly string? Location;
        /// <summary>
        /// Name of the file as displayed to end-users.
        /// </summary>
        public readonly string Name;

        [OutputConstructor]
        private ChallengeFile(
            string? content,

            string? contentb64,

            string? id,

            string? location,

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
