<div align="center">
    <h1><img src="res/ctfd.png">Pulumi CTFd Provider</h1>
    <p><b>Let's code your CTF(d)</b><p>
    <a href="https://pkg.go.dev/github.com/ctfer-io/pulumi-ctfd"><img src="https://shields.io/badge/-reference-blue?logo=go&style=for-the-badge" alt="reference"></a>
    <a href=""><img src="https://img.shields.io/github/license/ctfer-io/pulumi-ctfd?style=for-the-badge" alt="License"></a>
	<br>
	<a href="https://github.com/ctfer-io/pulumi-ctfd/actions/workflows/codeql-analysis.yaml"><img src="https://img.shields.io/github/actions/workflow/status/ctfer-io/pulumi-ctfd/codeql-analysis.yaml?style=for-the-badge&label=CodeQL" alt="CodeQL"></a>
    <a href="https://securityscorecards.dev/viewer/?uri=github.com/ctfer-io/pulumi-ctfd"><img src="https://img.shields.io/ossf-scorecard/github.com/ctfer-io/pulumi-ctfd?label=openssf%20scorecard&style=for-the-badge" alt="OpenSSF Scoreboard"></a>
</div>

## Context

[CTFd](https://ctfd.io) is an open-source CTFd platform famous for its simplicity and extensibility.
It has been used for various Capture The Flag (CTF) events, originally for the [CSAW](https://www.csaw.io/ctf), later by others such the [BreizhCTF](https://www.breizhctf.com/).

One of [CTFer](https://ctfer.io) approach is seeing the CTFd resources as simply as objects with CRUD operations (e.g. challenges).
From this simplification arise a possibility: managing them as Terraform resources, which we did with the [Terraform Provider for CTFd](https://github.com/ctfer-io/terraform-provider-ctfd).
Nevertheless, due to the limitations of Terraform and the necessity to bring reproducibility to Capture The Flag events, as stated by multiple organizers, we had to go further and give it an additional predicate: managing them as code through programming language.

[Pulumi](https://www.pulumi.com/docs/get-started) is an Infrastructure-as-Code (IaC) and Free Open-Source Software (FOSS) tool that is a first-class opportunity for this.

To sum it up, you can manage a Capture The Flag event based upon CTFd in multiple programming languages.

## SDK

To install the provider, refer to [this documentation](/docs/installation-configuration.md).

For more information on how to use the SDK in your favorite language, refer to [this documentation](/docs/_index.md).
