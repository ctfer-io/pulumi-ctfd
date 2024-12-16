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

__all__ = [
    'GetUsersResult',
    'AwaitableGetUsersResult',
    'get_users',
    'get_users_output',
]

@pulumi.output_type
class GetUsersResult:
    """
    A collection of values returned by getUsers.
    """
    def __init__(__self__, affiliation=None, banned=None, country=None, email=None, hidden=None, id=None, language=None, name=None, password=None, type=None, verified=None, website=None):
        if affiliation and not isinstance(affiliation, str):
            raise TypeError("Expected argument 'affiliation' to be a str")
        pulumi.set(__self__, "affiliation", affiliation)
        if banned and not isinstance(banned, bool):
            raise TypeError("Expected argument 'banned' to be a bool")
        pulumi.set(__self__, "banned", banned)
        if country and not isinstance(country, str):
            raise TypeError("Expected argument 'country' to be a str")
        pulumi.set(__self__, "country", country)
        if email and not isinstance(email, str):
            raise TypeError("Expected argument 'email' to be a str")
        pulumi.set(__self__, "email", email)
        if hidden and not isinstance(hidden, bool):
            raise TypeError("Expected argument 'hidden' to be a bool")
        pulumi.set(__self__, "hidden", hidden)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if language and not isinstance(language, str):
            raise TypeError("Expected argument 'language' to be a str")
        pulumi.set(__self__, "language", language)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if password and not isinstance(password, str):
            raise TypeError("Expected argument 'password' to be a str")
        pulumi.set(__self__, "password", password)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if verified and not isinstance(verified, bool):
            raise TypeError("Expected argument 'verified' to be a bool")
        pulumi.set(__self__, "verified", verified)
        if website and not isinstance(website, str):
            raise TypeError("Expected argument 'website' to be a str")
        pulumi.set(__self__, "website", website)

    @property
    @pulumi.getter
    def affiliation(self) -> str:
        """
        Affiliation to a team, company or agency.
        """
        return pulumi.get(self, "affiliation")

    @property
    @pulumi.getter
    def banned(self) -> bool:
        """
        Is true if the user is banned from the CTF.
        """
        return pulumi.get(self, "banned")

    @property
    @pulumi.getter
    def country(self) -> str:
        """
        Country the user represent or is native from.
        """
        return pulumi.get(self, "country")

    @property
    @pulumi.getter
    def email(self) -> str:
        """
        Email of the user, may be used to verify the account.
        """
        return pulumi.get(self, "email")

    @property
    @pulumi.getter
    def hidden(self) -> bool:
        """
        Is true if the user is hidden to the participants.
        """
        return pulumi.get(self, "hidden")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Identifier of the user.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def language(self) -> str:
        """
        Language the user is fluent in.
        """
        return pulumi.get(self, "language")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Name or pseudo of the user.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def password(self) -> str:
        """
        Password of the user. Notice that during a CTF you may not want to update those to avoid defaulting user accesses.
        """
        return pulumi.get(self, "password")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Generic type for RBAC purposes.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def verified(self) -> bool:
        """
        Is true if the user has verified its account by email, or if set by an admin.
        """
        return pulumi.get(self, "verified")

    @property
    @pulumi.getter
    def website(self) -> str:
        """
        Website, blog, or anything similar (displayed to other participants).
        """
        return pulumi.get(self, "website")


class AwaitableGetUsersResult(GetUsersResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetUsersResult(
            affiliation=self.affiliation,
            banned=self.banned,
            country=self.country,
            email=self.email,
            hidden=self.hidden,
            id=self.id,
            language=self.language,
            name=self.name,
            password=self.password,
            type=self.type,
            verified=self.verified,
            website=self.website)


def get_users(opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetUsersResult:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('ctfd:index/getUsers:getUsers', __args__, opts=opts, typ=GetUsersResult).value

    return AwaitableGetUsersResult(
        affiliation=pulumi.get(__ret__, 'affiliation'),
        banned=pulumi.get(__ret__, 'banned'),
        country=pulumi.get(__ret__, 'country'),
        email=pulumi.get(__ret__, 'email'),
        hidden=pulumi.get(__ret__, 'hidden'),
        id=pulumi.get(__ret__, 'id'),
        language=pulumi.get(__ret__, 'language'),
        name=pulumi.get(__ret__, 'name'),
        password=pulumi.get(__ret__, 'password'),
        type=pulumi.get(__ret__, 'type'),
        verified=pulumi.get(__ret__, 'verified'),
        website=pulumi.get(__ret__, 'website'))
def get_users_output(opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetUsersResult]:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('ctfd:index/getUsers:getUsers', __args__, opts=opts, typ=GetUsersResult)
    return __ret__.apply(lambda __response__: GetUsersResult(
        affiliation=pulumi.get(__response__, 'affiliation'),
        banned=pulumi.get(__response__, 'banned'),
        country=pulumi.get(__response__, 'country'),
        email=pulumi.get(__response__, 'email'),
        hidden=pulumi.get(__response__, 'hidden'),
        id=pulumi.get(__response__, 'id'),
        language=pulumi.get(__response__, 'language'),
        name=pulumi.get(__response__, 'name'),
        password=pulumi.get(__response__, 'password'),
        type=pulumi.get(__response__, 'type'),
        verified=pulumi.get(__response__, 'verified'),
        website=pulumi.get(__response__, 'website')))
