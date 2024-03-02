// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Ctfd.Inputs
{

    public sealed class ChallengeFileArgs : global::Pulumi.ResourceArgs
    {
        [Input("content")]
        private Input<string>? _content;

        /// <summary>
        /// Raw content of the file, perfectly fit the use-cases of a .txt document or anything with a simple binary content. You could provide it from the file-system using `file("${path.module}/...")`.
        /// </summary>
        public Input<string>? Content
        {
            get => _content;
            set
            {
                var emptySecret = Output.CreateSecret(0);
                _content = Output.Tuple<Input<string>?, int>(value, emptySecret).Apply(t => t.Item1);
            }
        }

        [Input("contentb64")]
        private Input<string>? _contentb64;

        /// <summary>
        /// Base 64 content of the file, perfectly fit the use-cases of complex binaries. You could provide it from the file-system using `filebase64("${path.module}/...")`.
        /// </summary>
        public Input<string>? Contentb64
        {
            get => _contentb64;
            set
            {
                var emptySecret = Output.CreateSecret(0);
                _contentb64 = Output.Tuple<Input<string>?, int>(value, emptySecret).Apply(t => t.Item1);
            }
        }

        /// <summary>
        /// Identifier of the file, used internally to handle the CTFd corresponding object.
        /// </summary>
        [Input("id")]
        public Input<string>? Id { get; set; }

        /// <summary>
        /// Location where the file is stored on the CTFd instance, for download purposes.
        /// </summary>
        [Input("location")]
        public Input<string>? Location { get; set; }

        /// <summary>
        /// Name of the file as displayed to end-users.
        /// </summary>
        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        /// <summary>
        /// The sha1 sum of the file.
        /// </summary>
        [Input("sha1sum")]
        public Input<string>? Sha1sum { get; set; }

        public ChallengeFileArgs()
        {
        }
        public static new ChallengeFileArgs Empty => new ChallengeFileArgs();
    }
}
