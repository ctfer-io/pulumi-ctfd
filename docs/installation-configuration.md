---
title: CTFd Installation & Configuration
meta_desc: Provides an overview on how to setup the CTFd Provider for Pulumi.
layout: package
---

## Installation

The CTFd provider is available as a package in all Pulumi languages:
- JavaScript/TypeScript: [`@ctfer-io/pulumi-ctfd`](https://www.npmjs.com/package/@ctfer-io/pulumi-ctfd)
- Python: [`pulumi-ctfd`](https://pypi.org/project/pulumi-ctfd/)
- Golang: [`github.com/ctfer-io/pulumi-ctfd/sdk/go/ctfd`](https://github.com/ctfer-io/pulumi-ctfd)
- .NET: [`Pulumi.Ctfd`](https://www.nuget.org/packages/Pulumi.Ctfd)

## Configuration

Pulumi relies on the CTFd REST JSON API to authenticate requests from the host machine to CTFd. Your credentials are never sent to pulumi.com.
The Pulumi CTFd Provider needs to be configured with CTFd credentials before it can be used to manage resources.

Your can either configure it using:
1. [environment variables](#environment-variables)
2. [provider configuration](/#provider)

### Environment variables

Using the following you can configure the CTFd. For description of each variable, refer to the [provider configuration](#provider-configuration).

```bash
export CTFD_URL="https://my-ctf.lan"
export CTFD_API_KEY="ctfd_xxx"
# additional configuration
```

We recommend using an API key rather than a nonce/session combo for security purposes: the API key is natively supported thus enable better logging, authentication & authorization.
Moreover, it is possible to rotate the keys and revoke them on the fly using the API, while a session/nonce is not build in this way.
