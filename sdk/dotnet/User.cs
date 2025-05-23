// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace CTFerio.Ctfd
{
    /// <summary>
    /// CTFd defines a User as someone who will either play or administrate the Capture The Flag event.
    /// 
    /// ## Example Usage
    /// 
    /// ```csharp
    /// using System.Collections.Generic;
    /// using System.Linq;
    /// using Pulumi;
    /// using Ctfd = CTFerio.Ctfd;
    /// 
    /// return await Deployment.RunAsync(() =&gt; 
    /// {
    ///     var ctfer = new Ctfd.User("ctfer", new()
    ///     {
    ///         Email = "ctfer-io@protonmail.com",
    ///         Hidden = true,
    ///         Password = "password",
    ///         Type = "admin",
    ///         Verified = true,
    ///     });
    /// 
    /// });
    /// ```
    /// </summary>
    [CtfdResourceType("ctfd:index/user:User")]
    public partial class User : global::Pulumi.CustomResource
    {
        /// <summary>
        /// Affiliation to a team, company or agency.
        /// </summary>
        [Output("affiliation")]
        public Output<string?> Affiliation { get; private set; } = null!;

        /// <summary>
        /// Is true if the user is banned from the CTF.
        /// </summary>
        [Output("banned")]
        public Output<bool> Banned { get; private set; } = null!;

        /// <summary>
        /// The bracket id the user plays in.
        /// </summary>
        [Output("bracketId")]
        public Output<string?> BracketId { get; private set; } = null!;

        /// <summary>
        /// Country the user represent or is native from.
        /// </summary>
        [Output("country")]
        public Output<string?> Country { get; private set; } = null!;

        /// <summary>
        /// Email of the user, may be used to verify the account.
        /// </summary>
        [Output("email")]
        public Output<string> Email { get; private set; } = null!;

        /// <summary>
        /// Is true if the user is hidden to the participants.
        /// </summary>
        [Output("hidden")]
        public Output<bool> Hidden { get; private set; } = null!;

        /// <summary>
        /// Language the user is fluent in.
        /// </summary>
        [Output("language")]
        public Output<string?> Language { get; private set; } = null!;

        /// <summary>
        /// Name or pseudo of the user.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// Password of the user. Notice than during a CTF you may not want to update those to avoid defaulting user accesses.
        /// </summary>
        [Output("password")]
        public Output<string> Password { get; private set; } = null!;

        /// <summary>
        /// Generic type for RBAC purposes.
        /// </summary>
        [Output("type")]
        public Output<string> Type { get; private set; } = null!;

        /// <summary>
        /// Is true if the user has verified its account by email, or if set by an admin.
        /// </summary>
        [Output("verified")]
        public Output<bool> Verified { get; private set; } = null!;

        /// <summary>
        /// Website, blog, or anything similar (displayed to other participants).
        /// </summary>
        [Output("website")]
        public Output<string?> Website { get; private set; } = null!;


        /// <summary>
        /// Create a User resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public User(string name, UserArgs args, CustomResourceOptions? options = null)
            : base("ctfd:index/user:User", name, args ?? new UserArgs(), MakeResourceOptions(options, ""))
        {
        }

        private User(string name, Input<string> id, UserState? state = null, CustomResourceOptions? options = null)
            : base("ctfd:index/user:User", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                PluginDownloadURL = "github://api.github.com/ctfer-io/",
                AdditionalSecretOutputs =
                {
                    "email",
                    "password",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing User resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static User Get(string name, Input<string> id, UserState? state = null, CustomResourceOptions? options = null)
        {
            return new User(name, id, state, options);
        }
    }

    public sealed class UserArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Affiliation to a team, company or agency.
        /// </summary>
        [Input("affiliation")]
        public Input<string>? Affiliation { get; set; }

        /// <summary>
        /// Is true if the user is banned from the CTF.
        /// </summary>
        [Input("banned")]
        public Input<bool>? Banned { get; set; }

        /// <summary>
        /// The bracket id the user plays in.
        /// </summary>
        [Input("bracketId")]
        public Input<string>? BracketId { get; set; }

        /// <summary>
        /// Country the user represent or is native from.
        /// </summary>
        [Input("country")]
        public Input<string>? Country { get; set; }

        [Input("email", required: true)]
        private Input<string>? _email;

        /// <summary>
        /// Email of the user, may be used to verify the account.
        /// </summary>
        public Input<string>? Email
        {
            get => _email;
            set
            {
                var emptySecret = Output.CreateSecret(0);
                _email = Output.Tuple<Input<string>?, int>(value, emptySecret).Apply(t => t.Item1);
            }
        }

        /// <summary>
        /// Is true if the user is hidden to the participants.
        /// </summary>
        [Input("hidden")]
        public Input<bool>? Hidden { get; set; }

        /// <summary>
        /// Language the user is fluent in.
        /// </summary>
        [Input("language")]
        public Input<string>? Language { get; set; }

        /// <summary>
        /// Name or pseudo of the user.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("password", required: true)]
        private Input<string>? _password;

        /// <summary>
        /// Password of the user. Notice than during a CTF you may not want to update those to avoid defaulting user accesses.
        /// </summary>
        public Input<string>? Password
        {
            get => _password;
            set
            {
                var emptySecret = Output.CreateSecret(0);
                _password = Output.Tuple<Input<string>?, int>(value, emptySecret).Apply(t => t.Item1);
            }
        }

        /// <summary>
        /// Generic type for RBAC purposes.
        /// </summary>
        [Input("type")]
        public Input<string>? Type { get; set; }

        /// <summary>
        /// Is true if the user has verified its account by email, or if set by an admin.
        /// </summary>
        [Input("verified")]
        public Input<bool>? Verified { get; set; }

        /// <summary>
        /// Website, blog, or anything similar (displayed to other participants).
        /// </summary>
        [Input("website")]
        public Input<string>? Website { get; set; }

        public UserArgs()
        {
        }
        public static new UserArgs Empty => new UserArgs();
    }

    public sealed class UserState : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Affiliation to a team, company or agency.
        /// </summary>
        [Input("affiliation")]
        public Input<string>? Affiliation { get; set; }

        /// <summary>
        /// Is true if the user is banned from the CTF.
        /// </summary>
        [Input("banned")]
        public Input<bool>? Banned { get; set; }

        /// <summary>
        /// The bracket id the user plays in.
        /// </summary>
        [Input("bracketId")]
        public Input<string>? BracketId { get; set; }

        /// <summary>
        /// Country the user represent or is native from.
        /// </summary>
        [Input("country")]
        public Input<string>? Country { get; set; }

        [Input("email")]
        private Input<string>? _email;

        /// <summary>
        /// Email of the user, may be used to verify the account.
        /// </summary>
        public Input<string>? Email
        {
            get => _email;
            set
            {
                var emptySecret = Output.CreateSecret(0);
                _email = Output.Tuple<Input<string>?, int>(value, emptySecret).Apply(t => t.Item1);
            }
        }

        /// <summary>
        /// Is true if the user is hidden to the participants.
        /// </summary>
        [Input("hidden")]
        public Input<bool>? Hidden { get; set; }

        /// <summary>
        /// Language the user is fluent in.
        /// </summary>
        [Input("language")]
        public Input<string>? Language { get; set; }

        /// <summary>
        /// Name or pseudo of the user.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("password")]
        private Input<string>? _password;

        /// <summary>
        /// Password of the user. Notice than during a CTF you may not want to update those to avoid defaulting user accesses.
        /// </summary>
        public Input<string>? Password
        {
            get => _password;
            set
            {
                var emptySecret = Output.CreateSecret(0);
                _password = Output.Tuple<Input<string>?, int>(value, emptySecret).Apply(t => t.Item1);
            }
        }

        /// <summary>
        /// Generic type for RBAC purposes.
        /// </summary>
        [Input("type")]
        public Input<string>? Type { get; set; }

        /// <summary>
        /// Is true if the user has verified its account by email, or if set by an admin.
        /// </summary>
        [Input("verified")]
        public Input<bool>? Verified { get; set; }

        /// <summary>
        /// Website, blog, or anything similar (displayed to other participants).
        /// </summary>
        [Input("website")]
        public Input<string>? Website { get; set; }

        public UserState()
        {
        }
        public static new UserState Empty => new UserState();
    }
}
