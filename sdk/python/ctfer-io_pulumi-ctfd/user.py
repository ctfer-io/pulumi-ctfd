# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['UserArgs', 'User']

@pulumi.input_type
class UserArgs:
    def __init__(__self__, *,
                 email: pulumi.Input[str],
                 password: pulumi.Input[str],
                 affiliation: Optional[pulumi.Input[str]] = None,
                 banned: Optional[pulumi.Input[bool]] = None,
                 country: Optional[pulumi.Input[str]] = None,
                 hidden: Optional[pulumi.Input[bool]] = None,
                 language: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 verified: Optional[pulumi.Input[bool]] = None,
                 website: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a User resource.
        :param pulumi.Input[str] email: Email of the user, may be used to verify the account.
        :param pulumi.Input[str] password: Password of the user. Notice than during a CTF you may not want to update those to avoid defaulting user accesses.
        :param pulumi.Input[str] affiliation: Affiliation to a team, company or agency.
        :param pulumi.Input[bool] banned: Is true if the user is banned from the CTF.
        :param pulumi.Input[str] country: Country the user represent or is native from.
        :param pulumi.Input[bool] hidden: Is true if the user is hidden to the participants.
        :param pulumi.Input[str] language: Language the user is fluent in.
        :param pulumi.Input[str] name: Name or pseudo of the user.
        :param pulumi.Input[str] type: Generic type for RBAC purposes.
        :param pulumi.Input[bool] verified: Is true if the user has verified its account by email, or if set by an admin.
        :param pulumi.Input[str] website: Website, blog, or anything similar (displayed to other participants).
        """
        pulumi.set(__self__, "email", email)
        pulumi.set(__self__, "password", password)
        if affiliation is not None:
            pulumi.set(__self__, "affiliation", affiliation)
        if banned is not None:
            pulumi.set(__self__, "banned", banned)
        if country is not None:
            pulumi.set(__self__, "country", country)
        if hidden is not None:
            pulumi.set(__self__, "hidden", hidden)
        if language is not None:
            pulumi.set(__self__, "language", language)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if type is not None:
            pulumi.set(__self__, "type", type)
        if verified is not None:
            pulumi.set(__self__, "verified", verified)
        if website is not None:
            pulumi.set(__self__, "website", website)

    @property
    @pulumi.getter
    def email(self) -> pulumi.Input[str]:
        """
        Email of the user, may be used to verify the account.
        """
        return pulumi.get(self, "email")

    @email.setter
    def email(self, value: pulumi.Input[str]):
        pulumi.set(self, "email", value)

    @property
    @pulumi.getter
    def password(self) -> pulumi.Input[str]:
        """
        Password of the user. Notice than during a CTF you may not want to update those to avoid defaulting user accesses.
        """
        return pulumi.get(self, "password")

    @password.setter
    def password(self, value: pulumi.Input[str]):
        pulumi.set(self, "password", value)

    @property
    @pulumi.getter
    def affiliation(self) -> Optional[pulumi.Input[str]]:
        """
        Affiliation to a team, company or agency.
        """
        return pulumi.get(self, "affiliation")

    @affiliation.setter
    def affiliation(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "affiliation", value)

    @property
    @pulumi.getter
    def banned(self) -> Optional[pulumi.Input[bool]]:
        """
        Is true if the user is banned from the CTF.
        """
        return pulumi.get(self, "banned")

    @banned.setter
    def banned(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "banned", value)

    @property
    @pulumi.getter
    def country(self) -> Optional[pulumi.Input[str]]:
        """
        Country the user represent or is native from.
        """
        return pulumi.get(self, "country")

    @country.setter
    def country(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "country", value)

    @property
    @pulumi.getter
    def hidden(self) -> Optional[pulumi.Input[bool]]:
        """
        Is true if the user is hidden to the participants.
        """
        return pulumi.get(self, "hidden")

    @hidden.setter
    def hidden(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "hidden", value)

    @property
    @pulumi.getter
    def language(self) -> Optional[pulumi.Input[str]]:
        """
        Language the user is fluent in.
        """
        return pulumi.get(self, "language")

    @language.setter
    def language(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "language", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name or pseudo of the user.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        """
        Generic type for RBAC purposes.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter
    def verified(self) -> Optional[pulumi.Input[bool]]:
        """
        Is true if the user has verified its account by email, or if set by an admin.
        """
        return pulumi.get(self, "verified")

    @verified.setter
    def verified(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "verified", value)

    @property
    @pulumi.getter
    def website(self) -> Optional[pulumi.Input[str]]:
        """
        Website, blog, or anything similar (displayed to other participants).
        """
        return pulumi.get(self, "website")

    @website.setter
    def website(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "website", value)


@pulumi.input_type
class _UserState:
    def __init__(__self__, *,
                 affiliation: Optional[pulumi.Input[str]] = None,
                 banned: Optional[pulumi.Input[bool]] = None,
                 country: Optional[pulumi.Input[str]] = None,
                 email: Optional[pulumi.Input[str]] = None,
                 hidden: Optional[pulumi.Input[bool]] = None,
                 language: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 password: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 verified: Optional[pulumi.Input[bool]] = None,
                 website: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering User resources.
        :param pulumi.Input[str] affiliation: Affiliation to a team, company or agency.
        :param pulumi.Input[bool] banned: Is true if the user is banned from the CTF.
        :param pulumi.Input[str] country: Country the user represent or is native from.
        :param pulumi.Input[str] email: Email of the user, may be used to verify the account.
        :param pulumi.Input[bool] hidden: Is true if the user is hidden to the participants.
        :param pulumi.Input[str] language: Language the user is fluent in.
        :param pulumi.Input[str] name: Name or pseudo of the user.
        :param pulumi.Input[str] password: Password of the user. Notice than during a CTF you may not want to update those to avoid defaulting user accesses.
        :param pulumi.Input[str] type: Generic type for RBAC purposes.
        :param pulumi.Input[bool] verified: Is true if the user has verified its account by email, or if set by an admin.
        :param pulumi.Input[str] website: Website, blog, or anything similar (displayed to other participants).
        """
        if affiliation is not None:
            pulumi.set(__self__, "affiliation", affiliation)
        if banned is not None:
            pulumi.set(__self__, "banned", banned)
        if country is not None:
            pulumi.set(__self__, "country", country)
        if email is not None:
            pulumi.set(__self__, "email", email)
        if hidden is not None:
            pulumi.set(__self__, "hidden", hidden)
        if language is not None:
            pulumi.set(__self__, "language", language)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if password is not None:
            pulumi.set(__self__, "password", password)
        if type is not None:
            pulumi.set(__self__, "type", type)
        if verified is not None:
            pulumi.set(__self__, "verified", verified)
        if website is not None:
            pulumi.set(__self__, "website", website)

    @property
    @pulumi.getter
    def affiliation(self) -> Optional[pulumi.Input[str]]:
        """
        Affiliation to a team, company or agency.
        """
        return pulumi.get(self, "affiliation")

    @affiliation.setter
    def affiliation(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "affiliation", value)

    @property
    @pulumi.getter
    def banned(self) -> Optional[pulumi.Input[bool]]:
        """
        Is true if the user is banned from the CTF.
        """
        return pulumi.get(self, "banned")

    @banned.setter
    def banned(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "banned", value)

    @property
    @pulumi.getter
    def country(self) -> Optional[pulumi.Input[str]]:
        """
        Country the user represent or is native from.
        """
        return pulumi.get(self, "country")

    @country.setter
    def country(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "country", value)

    @property
    @pulumi.getter
    def email(self) -> Optional[pulumi.Input[str]]:
        """
        Email of the user, may be used to verify the account.
        """
        return pulumi.get(self, "email")

    @email.setter
    def email(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "email", value)

    @property
    @pulumi.getter
    def hidden(self) -> Optional[pulumi.Input[bool]]:
        """
        Is true if the user is hidden to the participants.
        """
        return pulumi.get(self, "hidden")

    @hidden.setter
    def hidden(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "hidden", value)

    @property
    @pulumi.getter
    def language(self) -> Optional[pulumi.Input[str]]:
        """
        Language the user is fluent in.
        """
        return pulumi.get(self, "language")

    @language.setter
    def language(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "language", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name or pseudo of the user.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def password(self) -> Optional[pulumi.Input[str]]:
        """
        Password of the user. Notice than during a CTF you may not want to update those to avoid defaulting user accesses.
        """
        return pulumi.get(self, "password")

    @password.setter
    def password(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "password", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        """
        Generic type for RBAC purposes.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter
    def verified(self) -> Optional[pulumi.Input[bool]]:
        """
        Is true if the user has verified its account by email, or if set by an admin.
        """
        return pulumi.get(self, "verified")

    @verified.setter
    def verified(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "verified", value)

    @property
    @pulumi.getter
    def website(self) -> Optional[pulumi.Input[str]]:
        """
        Website, blog, or anything similar (displayed to other participants).
        """
        return pulumi.get(self, "website")

    @website.setter
    def website(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "website", value)


class User(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 affiliation: Optional[pulumi.Input[str]] = None,
                 banned: Optional[pulumi.Input[bool]] = None,
                 country: Optional[pulumi.Input[str]] = None,
                 email: Optional[pulumi.Input[str]] = None,
                 hidden: Optional[pulumi.Input[bool]] = None,
                 language: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 password: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 verified: Optional[pulumi.Input[bool]] = None,
                 website: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        CTFd defines a User as someone who will either play or administrate the Capture The Flag event.

        ## Example Usage

        <!--Start PulumiCodeChooser -->
        ```python
        import pulumi
        import ctfer-io_pulumi-ctfd as ctfd

        ctfer = ctfd.User("ctfer",
            email="ctfer-io@protonmail.com",
            hidden=True,
            password="password",
            type="admin",
            verified=True)
        ```
        <!--End PulumiCodeChooser -->

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] affiliation: Affiliation to a team, company or agency.
        :param pulumi.Input[bool] banned: Is true if the user is banned from the CTF.
        :param pulumi.Input[str] country: Country the user represent or is native from.
        :param pulumi.Input[str] email: Email of the user, may be used to verify the account.
        :param pulumi.Input[bool] hidden: Is true if the user is hidden to the participants.
        :param pulumi.Input[str] language: Language the user is fluent in.
        :param pulumi.Input[str] name: Name or pseudo of the user.
        :param pulumi.Input[str] password: Password of the user. Notice than during a CTF you may not want to update those to avoid defaulting user accesses.
        :param pulumi.Input[str] type: Generic type for RBAC purposes.
        :param pulumi.Input[bool] verified: Is true if the user has verified its account by email, or if set by an admin.
        :param pulumi.Input[str] website: Website, blog, or anything similar (displayed to other participants).
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: UserArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        CTFd defines a User as someone who will either play or administrate the Capture The Flag event.

        ## Example Usage

        <!--Start PulumiCodeChooser -->
        ```python
        import pulumi
        import ctfer-io_pulumi-ctfd as ctfd

        ctfer = ctfd.User("ctfer",
            email="ctfer-io@protonmail.com",
            hidden=True,
            password="password",
            type="admin",
            verified=True)
        ```
        <!--End PulumiCodeChooser -->

        :param str resource_name: The name of the resource.
        :param UserArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(UserArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 affiliation: Optional[pulumi.Input[str]] = None,
                 banned: Optional[pulumi.Input[bool]] = None,
                 country: Optional[pulumi.Input[str]] = None,
                 email: Optional[pulumi.Input[str]] = None,
                 hidden: Optional[pulumi.Input[bool]] = None,
                 language: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 password: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 verified: Optional[pulumi.Input[bool]] = None,
                 website: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = UserArgs.__new__(UserArgs)

            __props__.__dict__["affiliation"] = affiliation
            __props__.__dict__["banned"] = banned
            __props__.__dict__["country"] = country
            if email is None and not opts.urn:
                raise TypeError("Missing required property 'email'")
            __props__.__dict__["email"] = None if email is None else pulumi.Output.secret(email)
            __props__.__dict__["hidden"] = hidden
            __props__.__dict__["language"] = language
            __props__.__dict__["name"] = name
            if password is None and not opts.urn:
                raise TypeError("Missing required property 'password'")
            __props__.__dict__["password"] = None if password is None else pulumi.Output.secret(password)
            __props__.__dict__["type"] = type
            __props__.__dict__["verified"] = verified
            __props__.__dict__["website"] = website
        secret_opts = pulumi.ResourceOptions(additional_secret_outputs=["email", "password"])
        opts = pulumi.ResourceOptions.merge(opts, secret_opts)
        super(User, __self__).__init__(
            'ctfd:index/user:User',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            affiliation: Optional[pulumi.Input[str]] = None,
            banned: Optional[pulumi.Input[bool]] = None,
            country: Optional[pulumi.Input[str]] = None,
            email: Optional[pulumi.Input[str]] = None,
            hidden: Optional[pulumi.Input[bool]] = None,
            language: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            password: Optional[pulumi.Input[str]] = None,
            type: Optional[pulumi.Input[str]] = None,
            verified: Optional[pulumi.Input[bool]] = None,
            website: Optional[pulumi.Input[str]] = None) -> 'User':
        """
        Get an existing User resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] affiliation: Affiliation to a team, company or agency.
        :param pulumi.Input[bool] banned: Is true if the user is banned from the CTF.
        :param pulumi.Input[str] country: Country the user represent or is native from.
        :param pulumi.Input[str] email: Email of the user, may be used to verify the account.
        :param pulumi.Input[bool] hidden: Is true if the user is hidden to the participants.
        :param pulumi.Input[str] language: Language the user is fluent in.
        :param pulumi.Input[str] name: Name or pseudo of the user.
        :param pulumi.Input[str] password: Password of the user. Notice than during a CTF you may not want to update those to avoid defaulting user accesses.
        :param pulumi.Input[str] type: Generic type for RBAC purposes.
        :param pulumi.Input[bool] verified: Is true if the user has verified its account by email, or if set by an admin.
        :param pulumi.Input[str] website: Website, blog, or anything similar (displayed to other participants).
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _UserState.__new__(_UserState)

        __props__.__dict__["affiliation"] = affiliation
        __props__.__dict__["banned"] = banned
        __props__.__dict__["country"] = country
        __props__.__dict__["email"] = email
        __props__.__dict__["hidden"] = hidden
        __props__.__dict__["language"] = language
        __props__.__dict__["name"] = name
        __props__.__dict__["password"] = password
        __props__.__dict__["type"] = type
        __props__.__dict__["verified"] = verified
        __props__.__dict__["website"] = website
        return User(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def affiliation(self) -> pulumi.Output[Optional[str]]:
        """
        Affiliation to a team, company or agency.
        """
        return pulumi.get(self, "affiliation")

    @property
    @pulumi.getter
    def banned(self) -> pulumi.Output[bool]:
        """
        Is true if the user is banned from the CTF.
        """
        return pulumi.get(self, "banned")

    @property
    @pulumi.getter
    def country(self) -> pulumi.Output[Optional[str]]:
        """
        Country the user represent or is native from.
        """
        return pulumi.get(self, "country")

    @property
    @pulumi.getter
    def email(self) -> pulumi.Output[str]:
        """
        Email of the user, may be used to verify the account.
        """
        return pulumi.get(self, "email")

    @property
    @pulumi.getter
    def hidden(self) -> pulumi.Output[bool]:
        """
        Is true if the user is hidden to the participants.
        """
        return pulumi.get(self, "hidden")

    @property
    @pulumi.getter
    def language(self) -> pulumi.Output[Optional[str]]:
        """
        Language the user is fluent in.
        """
        return pulumi.get(self, "language")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name or pseudo of the user.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def password(self) -> pulumi.Output[str]:
        """
        Password of the user. Notice than during a CTF you may not want to update those to avoid defaulting user accesses.
        """
        return pulumi.get(self, "password")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Generic type for RBAC purposes.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def verified(self) -> pulumi.Output[bool]:
        """
        Is true if the user has verified its account by email, or if set by an admin.
        """
        return pulumi.get(self, "verified")

    @property
    @pulumi.getter
    def website(self) -> pulumi.Output[Optional[str]]:
        """
        Website, blog, or anything similar (displayed to other participants).
        """
        return pulumi.get(self, "website")

