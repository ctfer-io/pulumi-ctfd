# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import sys
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
if sys.version_info >= (3, 11):
    from typing import NotRequired, TypedDict, TypeAlias
else:
    from typing_extensions import NotRequired, TypedDict, TypeAlias
from . import _utilities

__all__ = ['FlagArgs', 'Flag']

@pulumi.input_type
class FlagArgs:
    def __init__(__self__, *,
                 challenge_id: pulumi.Input[str],
                 content: pulumi.Input[str],
                 data: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Flag resource.
        :param pulumi.Input[str] challenge_id: Challenge of the flag.
        :param pulumi.Input[str] content: The actual flag to match. Consider using the convention `MYCTF{value}` with `MYCTF` being the shortcode of your event's name and `value` depending on each challenge.
        :param pulumi.Input[str] data: The flag sensitivity information, either case*sensitive or case*insensitive
        :param pulumi.Input[str] type: The type of the flag, could be either static or regex
        """
        pulumi.set(__self__, "challenge_id", challenge_id)
        pulumi.set(__self__, "content", content)
        if data is not None:
            pulumi.set(__self__, "data", data)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="challengeId")
    def challenge_id(self) -> pulumi.Input[str]:
        """
        Challenge of the flag.
        """
        return pulumi.get(self, "challenge_id")

    @challenge_id.setter
    def challenge_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "challenge_id", value)

    @property
    @pulumi.getter
    def content(self) -> pulumi.Input[str]:
        """
        The actual flag to match. Consider using the convention `MYCTF{value}` with `MYCTF` being the shortcode of your event's name and `value` depending on each challenge.
        """
        return pulumi.get(self, "content")

    @content.setter
    def content(self, value: pulumi.Input[str]):
        pulumi.set(self, "content", value)

    @property
    @pulumi.getter
    def data(self) -> Optional[pulumi.Input[str]]:
        """
        The flag sensitivity information, either case*sensitive or case*insensitive
        """
        return pulumi.get(self, "data")

    @data.setter
    def data(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "data", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        """
        The type of the flag, could be either static or regex
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)


@pulumi.input_type
class _FlagState:
    def __init__(__self__, *,
                 challenge_id: Optional[pulumi.Input[str]] = None,
                 content: Optional[pulumi.Input[str]] = None,
                 data: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Flag resources.
        :param pulumi.Input[str] challenge_id: Challenge of the flag.
        :param pulumi.Input[str] content: The actual flag to match. Consider using the convention `MYCTF{value}` with `MYCTF` being the shortcode of your event's name and `value` depending on each challenge.
        :param pulumi.Input[str] data: The flag sensitivity information, either case*sensitive or case*insensitive
        :param pulumi.Input[str] type: The type of the flag, could be either static or regex
        """
        if challenge_id is not None:
            pulumi.set(__self__, "challenge_id", challenge_id)
        if content is not None:
            pulumi.set(__self__, "content", content)
        if data is not None:
            pulumi.set(__self__, "data", data)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="challengeId")
    def challenge_id(self) -> Optional[pulumi.Input[str]]:
        """
        Challenge of the flag.
        """
        return pulumi.get(self, "challenge_id")

    @challenge_id.setter
    def challenge_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "challenge_id", value)

    @property
    @pulumi.getter
    def content(self) -> Optional[pulumi.Input[str]]:
        """
        The actual flag to match. Consider using the convention `MYCTF{value}` with `MYCTF` being the shortcode of your event's name and `value` depending on each challenge.
        """
        return pulumi.get(self, "content")

    @content.setter
    def content(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "content", value)

    @property
    @pulumi.getter
    def data(self) -> Optional[pulumi.Input[str]]:
        """
        The flag sensitivity information, either case*sensitive or case*insensitive
        """
        return pulumi.get(self, "data")

    @data.setter
    def data(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "data", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        """
        The type of the flag, could be either static or regex
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)


class Flag(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 challenge_id: Optional[pulumi.Input[str]] = None,
                 content: Optional[pulumi.Input[str]] = None,
                 data: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        A flag to solve the challenge.

        ## Example Usage

        ```python
        import pulumi
        import ctfer-io_pulumi-ctfd as ctfd

        http = ctfd.ChallengeDynamic("http",
            category="misc",
            description="...",
            value=500,
            decay=100,
            minimum=50,
            state="visible",
            function="logarithmic",
            topics=["Misc"],
            tags=[
                "misc",
                "basic",
            ])
        http_flag = ctfd.Flag("httpFlag",
            challenge_id=http.id,
            content="CTF{some_flag}")
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] challenge_id: Challenge of the flag.
        :param pulumi.Input[str] content: The actual flag to match. Consider using the convention `MYCTF{value}` with `MYCTF` being the shortcode of your event's name and `value` depending on each challenge.
        :param pulumi.Input[str] data: The flag sensitivity information, either case*sensitive or case*insensitive
        :param pulumi.Input[str] type: The type of the flag, could be either static or regex
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: FlagArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        A flag to solve the challenge.

        ## Example Usage

        ```python
        import pulumi
        import ctfer-io_pulumi-ctfd as ctfd

        http = ctfd.ChallengeDynamic("http",
            category="misc",
            description="...",
            value=500,
            decay=100,
            minimum=50,
            state="visible",
            function="logarithmic",
            topics=["Misc"],
            tags=[
                "misc",
                "basic",
            ])
        http_flag = ctfd.Flag("httpFlag",
            challenge_id=http.id,
            content="CTF{some_flag}")
        ```

        :param str resource_name: The name of the resource.
        :param FlagArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(FlagArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 challenge_id: Optional[pulumi.Input[str]] = None,
                 content: Optional[pulumi.Input[str]] = None,
                 data: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = FlagArgs.__new__(FlagArgs)

            if challenge_id is None and not opts.urn:
                raise TypeError("Missing required property 'challenge_id'")
            __props__.__dict__["challenge_id"] = challenge_id
            if content is None and not opts.urn:
                raise TypeError("Missing required property 'content'")
            __props__.__dict__["content"] = None if content is None else pulumi.Output.secret(content)
            __props__.__dict__["data"] = data
            __props__.__dict__["type"] = type
        secret_opts = pulumi.ResourceOptions(additional_secret_outputs=["content"])
        opts = pulumi.ResourceOptions.merge(opts, secret_opts)
        super(Flag, __self__).__init__(
            'ctfd:index/flag:Flag',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            challenge_id: Optional[pulumi.Input[str]] = None,
            content: Optional[pulumi.Input[str]] = None,
            data: Optional[pulumi.Input[str]] = None,
            type: Optional[pulumi.Input[str]] = None) -> 'Flag':
        """
        Get an existing Flag resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] challenge_id: Challenge of the flag.
        :param pulumi.Input[str] content: The actual flag to match. Consider using the convention `MYCTF{value}` with `MYCTF` being the shortcode of your event's name and `value` depending on each challenge.
        :param pulumi.Input[str] data: The flag sensitivity information, either case*sensitive or case*insensitive
        :param pulumi.Input[str] type: The type of the flag, could be either static or regex
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _FlagState.__new__(_FlagState)

        __props__.__dict__["challenge_id"] = challenge_id
        __props__.__dict__["content"] = content
        __props__.__dict__["data"] = data
        __props__.__dict__["type"] = type
        return Flag(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="challengeId")
    def challenge_id(self) -> pulumi.Output[str]:
        """
        Challenge of the flag.
        """
        return pulumi.get(self, "challenge_id")

    @property
    @pulumi.getter
    def content(self) -> pulumi.Output[str]:
        """
        The actual flag to match. Consider using the convention `MYCTF{value}` with `MYCTF` being the shortcode of your event's name and `value` depending on each challenge.
        """
        return pulumi.get(self, "content")

    @property
    @pulumi.getter
    def data(self) -> pulumi.Output[str]:
        """
        The flag sensitivity information, either case*sensitive or case*insensitive
        """
        return pulumi.get(self, "data")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the flag, could be either static or regex
        """
        return pulumi.get(self, "type")

