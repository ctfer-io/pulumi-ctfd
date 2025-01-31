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

__all__ = ['FileArgs', 'File']

@pulumi.input_type
class FileArgs:
    def __init__(__self__, *,
                 challenge_id: Optional[pulumi.Input[str]] = None,
                 contentb64: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a File resource.
        :param pulumi.Input[str] challenge_id: Challenge of the file.
        :param pulumi.Input[str] contentb64: Base 64 content of the file, perfectly fit the use-cases of complex binaries. You could provide it from the file-system using `filebase64("${path.module}/...")`.
        :param pulumi.Input[str] location: Location where the file is stored on the CTFd instance, for download purposes.
        :param pulumi.Input[str] name: Name of the file as displayed to end-users.
        """
        if challenge_id is not None:
            pulumi.set(__self__, "challenge_id", challenge_id)
        if contentb64 is not None:
            pulumi.set(__self__, "contentb64", contentb64)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="challengeId")
    def challenge_id(self) -> Optional[pulumi.Input[str]]:
        """
        Challenge of the file.
        """
        return pulumi.get(self, "challenge_id")

    @challenge_id.setter
    def challenge_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "challenge_id", value)

    @property
    @pulumi.getter
    def contentb64(self) -> Optional[pulumi.Input[str]]:
        """
        Base 64 content of the file, perfectly fit the use-cases of complex binaries. You could provide it from the file-system using `filebase64("${path.module}/...")`.
        """
        return pulumi.get(self, "contentb64")

    @contentb64.setter
    def contentb64(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "contentb64", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        Location where the file is stored on the CTFd instance, for download purposes.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the file as displayed to end-users.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _FileState:
    def __init__(__self__, *,
                 challenge_id: Optional[pulumi.Input[str]] = None,
                 contentb64: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 sha1sum: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering File resources.
        :param pulumi.Input[str] challenge_id: Challenge of the file.
        :param pulumi.Input[str] contentb64: Base 64 content of the file, perfectly fit the use-cases of complex binaries. You could provide it from the file-system using `filebase64("${path.module}/...")`.
        :param pulumi.Input[str] location: Location where the file is stored on the CTFd instance, for download purposes.
        :param pulumi.Input[str] name: Name of the file as displayed to end-users.
        :param pulumi.Input[str] sha1sum: The sha1 sum of the file.
        """
        if challenge_id is not None:
            pulumi.set(__self__, "challenge_id", challenge_id)
        if contentb64 is not None:
            pulumi.set(__self__, "contentb64", contentb64)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if sha1sum is not None:
            pulumi.set(__self__, "sha1sum", sha1sum)

    @property
    @pulumi.getter(name="challengeId")
    def challenge_id(self) -> Optional[pulumi.Input[str]]:
        """
        Challenge of the file.
        """
        return pulumi.get(self, "challenge_id")

    @challenge_id.setter
    def challenge_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "challenge_id", value)

    @property
    @pulumi.getter
    def contentb64(self) -> Optional[pulumi.Input[str]]:
        """
        Base 64 content of the file, perfectly fit the use-cases of complex binaries. You could provide it from the file-system using `filebase64("${path.module}/...")`.
        """
        return pulumi.get(self, "contentb64")

    @contentb64.setter
    def contentb64(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "contentb64", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        Location where the file is stored on the CTFd instance, for download purposes.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the file as displayed to end-users.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def sha1sum(self) -> Optional[pulumi.Input[str]]:
        """
        The sha1 sum of the file.
        """
        return pulumi.get(self, "sha1sum")

    @sha1sum.setter
    def sha1sum(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "sha1sum", value)


class File(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 challenge_id: Optional[pulumi.Input[str]] = None,
                 contentb64: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        A CTFd file for a challenge.

        ## Example Usage

        ```python
        import pulumi
        import base64
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
        http_file = ctfd.File("httpFile",
            challenge_id=http.id,
            contentb64=(lambda path: base64.b64encode(open(path).read().encode()).decode())(".../image.png"))
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] challenge_id: Challenge of the file.
        :param pulumi.Input[str] contentb64: Base 64 content of the file, perfectly fit the use-cases of complex binaries. You could provide it from the file-system using `filebase64("${path.module}/...")`.
        :param pulumi.Input[str] location: Location where the file is stored on the CTFd instance, for download purposes.
        :param pulumi.Input[str] name: Name of the file as displayed to end-users.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[FileArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        A CTFd file for a challenge.

        ## Example Usage

        ```python
        import pulumi
        import base64
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
        http_file = ctfd.File("httpFile",
            challenge_id=http.id,
            contentb64=(lambda path: base64.b64encode(open(path).read().encode()).decode())(".../image.png"))
        ```

        :param str resource_name: The name of the resource.
        :param FileArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(FileArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 challenge_id: Optional[pulumi.Input[str]] = None,
                 contentb64: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = FileArgs.__new__(FileArgs)

            __props__.__dict__["challenge_id"] = challenge_id
            __props__.__dict__["contentb64"] = None if contentb64 is None else pulumi.Output.secret(contentb64)
            __props__.__dict__["location"] = location
            __props__.__dict__["name"] = name
            __props__.__dict__["sha1sum"] = None
        secret_opts = pulumi.ResourceOptions(additional_secret_outputs=["contentb64"])
        opts = pulumi.ResourceOptions.merge(opts, secret_opts)
        super(File, __self__).__init__(
            'ctfd:index/file:File',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            challenge_id: Optional[pulumi.Input[str]] = None,
            contentb64: Optional[pulumi.Input[str]] = None,
            location: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            sha1sum: Optional[pulumi.Input[str]] = None) -> 'File':
        """
        Get an existing File resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] challenge_id: Challenge of the file.
        :param pulumi.Input[str] contentb64: Base 64 content of the file, perfectly fit the use-cases of complex binaries. You could provide it from the file-system using `filebase64("${path.module}/...")`.
        :param pulumi.Input[str] location: Location where the file is stored on the CTFd instance, for download purposes.
        :param pulumi.Input[str] name: Name of the file as displayed to end-users.
        :param pulumi.Input[str] sha1sum: The sha1 sum of the file.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _FileState.__new__(_FileState)

        __props__.__dict__["challenge_id"] = challenge_id
        __props__.__dict__["contentb64"] = contentb64
        __props__.__dict__["location"] = location
        __props__.__dict__["name"] = name
        __props__.__dict__["sha1sum"] = sha1sum
        return File(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="challengeId")
    def challenge_id(self) -> pulumi.Output[Optional[str]]:
        """
        Challenge of the file.
        """
        return pulumi.get(self, "challenge_id")

    @property
    @pulumi.getter
    def contentb64(self) -> pulumi.Output[str]:
        """
        Base 64 content of the file, perfectly fit the use-cases of complex binaries. You could provide it from the file-system using `filebase64("${path.module}/...")`.
        """
        return pulumi.get(self, "contentb64")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        Location where the file is stored on the CTFd instance, for download purposes.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the file as displayed to end-users.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def sha1sum(self) -> pulumi.Output[str]:
        """
        The sha1 sum of the file.
        """
        return pulumi.get(self, "sha1sum")

