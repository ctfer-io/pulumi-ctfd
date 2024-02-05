# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['ProviderArgs', 'Provider']

@pulumi.input_type
class ProviderArgs:
    def __init__(__self__, *,
                 api_key: Optional[pulumi.Input[str]] = None,
                 nonce: Optional[pulumi.Input[str]] = None,
                 session: Optional[pulumi.Input[str]] = None,
                 url: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Provider resource.
        :param pulumi.Input[str] api_key: User API key. Could use `CTFD_API_KEY` environment variable instead. Despite being the most convenient way to
               authenticate yourself, we do not recommend it as you will probably generate a long-live token without any rotation
               policy.
        :param pulumi.Input[str] nonce: User session nonce, comes with session. Could use `CTFD_NONCE` environment variable instead.
        :param pulumi.Input[str] session: User session token, comes with nonce. Could use `CTFD_SESSION` environment variable instead.
        :param pulumi.Input[str] url: CTFd base URL (e.g. `https://my-ctf.lan`). Could use `CTFD_URL` environment variable instead.
        """
        if api_key is not None:
            pulumi.set(__self__, "api_key", api_key)
        if nonce is not None:
            pulumi.set(__self__, "nonce", nonce)
        if session is not None:
            pulumi.set(__self__, "session", session)
        if url is not None:
            pulumi.set(__self__, "url", url)

    @property
    @pulumi.getter(name="apiKey")
    def api_key(self) -> Optional[pulumi.Input[str]]:
        """
        User API key. Could use `CTFD_API_KEY` environment variable instead. Despite being the most convenient way to
        authenticate yourself, we do not recommend it as you will probably generate a long-live token without any rotation
        policy.
        """
        return pulumi.get(self, "api_key")

    @api_key.setter
    def api_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "api_key", value)

    @property
    @pulumi.getter
    def nonce(self) -> Optional[pulumi.Input[str]]:
        """
        User session nonce, comes with session. Could use `CTFD_NONCE` environment variable instead.
        """
        return pulumi.get(self, "nonce")

    @nonce.setter
    def nonce(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "nonce", value)

    @property
    @pulumi.getter
    def session(self) -> Optional[pulumi.Input[str]]:
        """
        User session token, comes with nonce. Could use `CTFD_SESSION` environment variable instead.
        """
        return pulumi.get(self, "session")

    @session.setter
    def session(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "session", value)

    @property
    @pulumi.getter
    def url(self) -> Optional[pulumi.Input[str]]:
        """
        CTFd base URL (e.g. `https://my-ctf.lan`). Could use `CTFD_URL` environment variable instead.
        """
        return pulumi.get(self, "url")

    @url.setter
    def url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "url", value)


class Provider(pulumi.ProviderResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 api_key: Optional[pulumi.Input[str]] = None,
                 nonce: Optional[pulumi.Input[str]] = None,
                 session: Optional[pulumi.Input[str]] = None,
                 url: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        The provider type for the ctfd package. By default, resources use package-wide configuration
        settings, however an explicit `Provider` instance may be created and passed during resource
        construction to achieve fine-grained programmatic control over provider settings. See the
        [documentation](https://www.pulumi.com/docs/reference/programming-model/#providers) for more information.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] api_key: User API key. Could use `CTFD_API_KEY` environment variable instead. Despite being the most convenient way to
               authenticate yourself, we do not recommend it as you will probably generate a long-live token without any rotation
               policy.
        :param pulumi.Input[str] nonce: User session nonce, comes with session. Could use `CTFD_NONCE` environment variable instead.
        :param pulumi.Input[str] session: User session token, comes with nonce. Could use `CTFD_SESSION` environment variable instead.
        :param pulumi.Input[str] url: CTFd base URL (e.g. `https://my-ctf.lan`). Could use `CTFD_URL` environment variable instead.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[ProviderArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The provider type for the ctfd package. By default, resources use package-wide configuration
        settings, however an explicit `Provider` instance may be created and passed during resource
        construction to achieve fine-grained programmatic control over provider settings. See the
        [documentation](https://www.pulumi.com/docs/reference/programming-model/#providers) for more information.

        :param str resource_name: The name of the resource.
        :param ProviderArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ProviderArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 api_key: Optional[pulumi.Input[str]] = None,
                 nonce: Optional[pulumi.Input[str]] = None,
                 session: Optional[pulumi.Input[str]] = None,
                 url: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ProviderArgs.__new__(ProviderArgs)

            __props__.__dict__["api_key"] = None if api_key is None else pulumi.Output.secret(api_key)
            __props__.__dict__["nonce"] = None if nonce is None else pulumi.Output.secret(nonce)
            __props__.__dict__["session"] = None if session is None else pulumi.Output.secret(session)
            __props__.__dict__["url"] = url
        secret_opts = pulumi.ResourceOptions(additional_secret_outputs=["apiKey", "nonce", "session"])
        opts = pulumi.ResourceOptions.merge(opts, secret_opts)
        super(Provider, __self__).__init__(
            'ctfd',
            resource_name,
            __props__,
            opts)

    @property
    @pulumi.getter(name="apiKey")
    def api_key(self) -> pulumi.Output[Optional[str]]:
        """
        User API key. Could use `CTFD_API_KEY` environment variable instead. Despite being the most convenient way to
        authenticate yourself, we do not recommend it as you will probably generate a long-live token without any rotation
        policy.
        """
        return pulumi.get(self, "api_key")

    @property
    @pulumi.getter
    def nonce(self) -> pulumi.Output[Optional[str]]:
        """
        User session nonce, comes with session. Could use `CTFD_NONCE` environment variable instead.
        """
        return pulumi.get(self, "nonce")

    @property
    @pulumi.getter
    def session(self) -> pulumi.Output[Optional[str]]:
        """
        User session token, comes with nonce. Could use `CTFD_SESSION` environment variable instead.
        """
        return pulumi.get(self, "session")

    @property
    @pulumi.getter
    def url(self) -> pulumi.Output[Optional[str]]:
        """
        CTFd base URL (e.g. `https://my-ctf.lan`). Could use `CTFD_URL` environment variable instead.
        """
        return pulumi.get(self, "url")

