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
    /// CTFd defines a Team as a group of Users who will attend the Capture The Flag event.
    /// 
    /// ## Example Usage
    /// 
    /// &lt;!--Start PulumiCodeChooser --&gt;
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
    ///         Password = "password",
    ///     });
    /// 
    ///     var cybercombattants = new Ctfd.Team("cybercombattants", new()
    ///     {
    ///         Email = "lucastesson@protonmail.com",
    ///         Password = "password",
    ///         Members = new[]
    ///         {
    ///             ctfer.Id,
    ///         },
    ///         Captain = ctfer.Id,
    ///     });
    /// 
    /// });
    /// ```
    /// &lt;!--End PulumiCodeChooser --&gt;
    /// 
    /// ## Import
    /// 
    /// User can be imported by the CTFd ID (check URLs)
    /// 
    /// ```sh
    /// $ pulumi import ctfd:index/team:Team cybercombattants 1
    /// ```
    /// </summary>
    [CtfdResourceType("ctfd:index/team:Team")]
    public partial class Team : global::Pulumi.CustomResource
    {
        /// <summary>
        /// Affiliation to a company or agency.
        /// </summary>
        [Output("affiliation")]
        public Output<string?> Affiliation { get; private set; } = null!;

        /// <summary>
        /// Is true if the team is banned from the CTF.
        /// </summary>
        [Output("banned")]
        public Output<bool> Banned { get; private set; } = null!;

        /// <summary>
        /// Member who is captain of the team. Must be part of the members too.
        /// </summary>
        [Output("captain")]
        public Output<string> Captain { get; private set; } = null!;

        /// <summary>
        /// Country the team represent or is hail from.
        /// </summary>
        [Output("country")]
        public Output<string?> Country { get; private set; } = null!;

        /// <summary>
        /// Email of the team.
        /// </summary>
        [Output("email")]
        public Output<string> Email { get; private set; } = null!;

        /// <summary>
        /// Is true if the team is hidden to the participants.
        /// </summary>
        [Output("hidden")]
        public Output<bool> Hidden { get; private set; } = null!;

        /// <summary>
        /// List of members (User), defined by their IDs.
        /// </summary>
        [Output("members")]
        public Output<ImmutableArray<string>> Members { get; private set; } = null!;

        /// <summary>
        /// Name of the team.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// Password of the team. Notice that during a CTF you may not want to update those to avoid defaulting team accesses.
        /// </summary>
        [Output("password")]
        public Output<string> Password { get; private set; } = null!;

        /// <summary>
        /// Website, blog, or anything similar (displayed to other participants).
        /// </summary>
        [Output("website")]
        public Output<string?> Website { get; private set; } = null!;


        /// <summary>
        /// Create a Team resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Team(string name, TeamArgs args, CustomResourceOptions? options = null)
            : base("ctfd:index/team:Team", name, args ?? new TeamArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Team(string name, Input<string> id, TeamState? state = null, CustomResourceOptions? options = null)
            : base("ctfd:index/team:Team", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                PluginDownloadURL = "github://api.github.com/ctfer-io/",
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing Team resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Team Get(string name, Input<string> id, TeamState? state = null, CustomResourceOptions? options = null)
        {
            return new Team(name, id, state, options);
        }
    }

    public sealed class TeamArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Affiliation to a company or agency.
        /// </summary>
        [Input("affiliation")]
        public Input<string>? Affiliation { get; set; }

        /// <summary>
        /// Is true if the team is banned from the CTF.
        /// </summary>
        [Input("banned")]
        public Input<bool>? Banned { get; set; }

        /// <summary>
        /// Member who is captain of the team. Must be part of the members too.
        /// </summary>
        [Input("captain", required: true)]
        public Input<string> Captain { get; set; } = null!;

        /// <summary>
        /// Country the team represent or is hail from.
        /// </summary>
        [Input("country")]
        public Input<string>? Country { get; set; }

        /// <summary>
        /// Email of the team.
        /// </summary>
        [Input("email", required: true)]
        public Input<string> Email { get; set; } = null!;

        /// <summary>
        /// Is true if the team is hidden to the participants.
        /// </summary>
        [Input("hidden")]
        public Input<bool>? Hidden { get; set; }

        [Input("members", required: true)]
        private InputList<string>? _members;

        /// <summary>
        /// List of members (User), defined by their IDs.
        /// </summary>
        public InputList<string> Members
        {
            get => _members ?? (_members = new InputList<string>());
            set => _members = value;
        }

        /// <summary>
        /// Name of the team.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// Password of the team. Notice that during a CTF you may not want to update those to avoid defaulting team accesses.
        /// </summary>
        [Input("password", required: true)]
        public Input<string> Password { get; set; } = null!;

        /// <summary>
        /// Website, blog, or anything similar (displayed to other participants).
        /// </summary>
        [Input("website")]
        public Input<string>? Website { get; set; }

        public TeamArgs()
        {
        }
        public static new TeamArgs Empty => new TeamArgs();
    }

    public sealed class TeamState : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Affiliation to a company or agency.
        /// </summary>
        [Input("affiliation")]
        public Input<string>? Affiliation { get; set; }

        /// <summary>
        /// Is true if the team is banned from the CTF.
        /// </summary>
        [Input("banned")]
        public Input<bool>? Banned { get; set; }

        /// <summary>
        /// Member who is captain of the team. Must be part of the members too.
        /// </summary>
        [Input("captain")]
        public Input<string>? Captain { get; set; }

        /// <summary>
        /// Country the team represent or is hail from.
        /// </summary>
        [Input("country")]
        public Input<string>? Country { get; set; }

        /// <summary>
        /// Email of the team.
        /// </summary>
        [Input("email")]
        public Input<string>? Email { get; set; }

        /// <summary>
        /// Is true if the team is hidden to the participants.
        /// </summary>
        [Input("hidden")]
        public Input<bool>? Hidden { get; set; }

        [Input("members")]
        private InputList<string>? _members;

        /// <summary>
        /// List of members (User), defined by their IDs.
        /// </summary>
        public InputList<string> Members
        {
            get => _members ?? (_members = new InputList<string>());
            set => _members = value;
        }

        /// <summary>
        /// Name of the team.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// Password of the team. Notice that during a CTF you may not want to update those to avoid defaulting team accesses.
        /// </summary>
        [Input("password")]
        public Input<string>? Password { get; set; }

        /// <summary>
        /// Website, blog, or anything similar (displayed to other participants).
        /// </summary>
        [Input("website")]
        public Input<string>? Website { get; set; }

        public TeamState()
        {
        }
        public static new TeamState Empty => new TeamState();
    }
}
