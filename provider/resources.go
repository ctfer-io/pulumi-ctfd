package ctfd

import (
	"fmt"
	"path"

	// Allow embedding bridge-metadata.json in the provider.
	_ "embed"

	"github.com/ctfer-io/pulumi-ctfd/provider/pkg/version"
	ctfd "github.com/ctfer-io/terraform-provider-ctfd/v2/provider"
	pf "github.com/pulumi/pulumi-terraform-bridge/v3/pkg/pf/tfbridge"
	"github.com/pulumi/pulumi-terraform-bridge/v3/pkg/tfbridge"
	"github.com/pulumi/pulumi-terraform-bridge/v3/pkg/tfbridge/tokens"
)

const (
	mainPkg = "ctfd"
	mainMod = "index" // the ctfd module
)

//go:embed cmd/pulumi-resource-ctfd/bridge-metadata.json
var metadata []byte

func Provider() tfbridge.ProviderInfo {
	prov := tfbridge.ProviderInfo{
		P:                       pf.ShimProvider(ctfd.New(version.Version)()),
		Version:                 version.Version,
		Name:                    "ctfd",
		DisplayName:             "CTFd",
		Publisher:               "CTFer.io",
		PluginDownloadURL:       "github://api.github.com/ctfer-io/",
		Description:             "The CTFd provider for Pulumi, to manage its resources as code.",
		Keywords:                []string{"pulumi", "ctfd", "category/cloud"},
		LogoURL:                 "https://raw.githubusercontent.com/ctfer-io/pulumi-ctfd/main/res/ctfd.png",
		License:                 "Apache-2.0",
		Homepage:                "https://ctfer.io",
		Repository:              "https://github.com/ctfer-io/pulumi-ctfd",
		GitHubOrg:               "ctfer-io",
		TFProviderModuleVersion: "v2",
		MetadataInfo:            tfbridge.NewProviderMetadata(metadata),
		Config:                  map[string]*tfbridge.SchemaInfo{},
		Resources: map[string]*tfbridge.ResourceInfo{
			"ctfd_challenge_standard": {
				Tok: tfbridge.MakeResource(mainPkg, mainMod, "ChallengeStandard"),
			},
			"ctfd_challenge_dynamic": {
				Tok: tfbridge.MakeResource(mainPkg, mainMod, "ChallengeDynamic"),
			},
			"ctfd_file": {
				Tok: tfbridge.MakeResource(mainPkg, mainMod, "File"),
			},
			"ctfd_flag": {
				Tok: tfbridge.MakeResource(mainPkg, mainMod, "Flag"),
			},
			"ctfd_hint": {
				Tok: tfbridge.MakeResource(mainPkg, mainMod, "Hint"),
			},
			"ctfd_team": {
				Tok: tfbridge.MakeResource(mainPkg, mainMod, "Team"),
			},
			"ctfd_user": {
				Tok: tfbridge.MakeResource(mainPkg, mainMod, "User"),
			},
		},
		DataSources: map[string]*tfbridge.DataSourceInfo{
			"ctfd_challenges_standard": {
				Tok: tfbridge.MakeDataSource(mainPkg, mainMod, "getChallengesStandard"),
			},
			"ctfd_challenges_dynamic": {
				Tok: tfbridge.MakeDataSource(mainPkg, mainMod, "getChallengesDynamic"),
			},
			"ctfd_teams": {
				Tok: tfbridge.MakeDataSource(mainPkg, mainMod, "getTeams"),
			},
			"ctfd_users": {
				Tok: tfbridge.MakeDataSource(mainPkg, mainMod, "getUsers"),
			},
		},
		JavaScript: &tfbridge.JavaScriptInfo{
			PackageName: "@ctfer-io/pulumi-ctfd",
			// List any npm dependencies and their versions
			Dependencies: map[string]string{
				"@pulumi/pulumi": "^3.0.0",
			},
			DevDependencies: map[string]string{
				"@types/node": "^10.0.0", // so we can access strongly typed node definitions.
				"@types/mime": "^2.0.0",
			},
		},
		Python: &tfbridge.PythonInfo{
			PackageName: fmt.Sprintf("ctfer-io_pulumi-%[1]s", mainPkg),
			// List any Python dependencies and their version ranges
			Requires: map[string]string{
				"pulumi": ">=3.0.0,<4.0.0",
			},
		},
		Golang: &tfbridge.GolangInfo{
			ImportBasePath: path.Join(
				fmt.Sprintf("github.com/ctfer-io/pulumi-%[1]s/sdk/", mainPkg),
				tfbridge.GetModuleMajorVersion(version.Version),
				"go",
				mainPkg,
			),
			GenerateResourceContainerTypes: true,
		},
		CSharp: &tfbridge.CSharpInfo{
			RootNamespace: "CTFerio",
			PackageReferences: map[string]string{
				"Pulumi": "3.*",
			},
		},
	}

	// These are new API's that you may opt to use to automatically compute resource
	// tokens, and apply auto aliasing for full backwards compatibility.  For more
	// information, please reference:
	// https://pkg.go.dev/github.com/pulumi/pulumi-terraform-bridge/v3/pkg/tfbridge#ProviderInfo.ComputeTokens
	prov.MustComputeTokens(tokens.SingleModule("ctfd_", mainMod,
		tokens.MakeStandard(mainPkg)))
	prov.MustApplyAutoAliases()
	prov.SetAutonaming(255, "-")

	return prov
}
