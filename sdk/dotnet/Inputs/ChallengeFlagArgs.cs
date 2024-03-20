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

    public sealed class ChallengeFlagArgs : global::Pulumi.ResourceArgs
    {
        [Input("content", required: true)]
        private Input<string>? _content;

        /// <summary>
        /// The actual flag to match. Consider using the convention `MYCTF{value}` with `MYCTF` being the shortcode of your event's name and `value` depending on each challenge.
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

        /// <summary>
        /// The flag sensitivity information, either case*sensitive or case*insensitive
        /// </summary>
        [Input("data")]
        public Input<string>? Data { get; set; }

        /// <summary>
        /// Identifier of the flag, used internally to handle the CTFd corresponding object.
        /// </summary>
        [Input("id")]
        public Input<string>? Id { get; set; }

        /// <summary>
        /// The type of the flag, could be either static or regex
        /// </summary>
        [Input("type")]
        public Input<string>? Type { get; set; }

        public ChallengeFlagArgs()
        {
        }
        public static new ChallengeFlagArgs Empty => new ChallengeFlagArgs();
    }
}
