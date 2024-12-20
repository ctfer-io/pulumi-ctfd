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
    'GetTeamsResult',
    'AwaitableGetTeamsResult',
    'get_teams',
    'get_teams_output',
]

@pulumi.output_type
class GetTeamsResult:
    """
    A collection of values returned by getTeams.
    """
    def __init__(__self__, affiliation=None, banned=None, captain=None, country=None, email=None, hidden=None, id=None, members=None, name=None, password=None, website=None):
        if affiliation and not isinstance(affiliation, str):
            raise TypeError("Expected argument 'affiliation' to be a str")
        pulumi.set(__self__, "affiliation", affiliation)
        if banned and not isinstance(banned, bool):
            raise TypeError("Expected argument 'banned' to be a bool")
        pulumi.set(__self__, "banned", banned)
        if captain and not isinstance(captain, str):
            raise TypeError("Expected argument 'captain' to be a str")
        pulumi.set(__self__, "captain", captain)
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
        if members and not isinstance(members, list):
            raise TypeError("Expected argument 'members' to be a list")
        pulumi.set(__self__, "members", members)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if password and not isinstance(password, str):
            raise TypeError("Expected argument 'password' to be a str")
        pulumi.set(__self__, "password", password)
        if website and not isinstance(website, str):
            raise TypeError("Expected argument 'website' to be a str")
        pulumi.set(__self__, "website", website)

    @property
    @pulumi.getter
    def affiliation(self) -> str:
        """
        Affiliation to a company or agency.
        """
        return pulumi.get(self, "affiliation")

    @property
    @pulumi.getter
    def banned(self) -> bool:
        """
        Is true if the team is banned from the CTF.
        """
        return pulumi.get(self, "banned")

    @property
    @pulumi.getter
    def captain(self) -> str:
        """
        Member who is captain of the team. Must be part of the members too. Note it could cause a fatal error in case of resource import with an inconsistent CTFd configuration i.e. if a team has no captain yet (should not be possible).
        """
        return pulumi.get(self, "captain")

    @property
    @pulumi.getter
    def country(self) -> str:
        """
        Country the team represent or is hail from.
        """
        return pulumi.get(self, "country")

    @property
    @pulumi.getter
    def email(self) -> str:
        """
        Email of the team.
        """
        return pulumi.get(self, "email")

    @property
    @pulumi.getter
    def hidden(self) -> bool:
        """
        Is true if the team is hidden to the participants.
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
    def members(self) -> Sequence[str]:
        """
        List of members (User), defined by their IDs.
        """
        return pulumi.get(self, "members")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Name of the team.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def password(self) -> str:
        """
        Password of the team. Notice that during a CTF you may not want to update those to avoid defaulting team accesses.
        """
        return pulumi.get(self, "password")

    @property
    @pulumi.getter
    def website(self) -> str:
        """
        Website, blog, or anything similar (displayed to other participants).
        """
        return pulumi.get(self, "website")


class AwaitableGetTeamsResult(GetTeamsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetTeamsResult(
            affiliation=self.affiliation,
            banned=self.banned,
            captain=self.captain,
            country=self.country,
            email=self.email,
            hidden=self.hidden,
            id=self.id,
            members=self.members,
            name=self.name,
            password=self.password,
            website=self.website)


def get_teams(opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetTeamsResult:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('ctfd:index/getTeams:getTeams', __args__, opts=opts, typ=GetTeamsResult).value

    return AwaitableGetTeamsResult(
        affiliation=pulumi.get(__ret__, 'affiliation'),
        banned=pulumi.get(__ret__, 'banned'),
        captain=pulumi.get(__ret__, 'captain'),
        country=pulumi.get(__ret__, 'country'),
        email=pulumi.get(__ret__, 'email'),
        hidden=pulumi.get(__ret__, 'hidden'),
        id=pulumi.get(__ret__, 'id'),
        members=pulumi.get(__ret__, 'members'),
        name=pulumi.get(__ret__, 'name'),
        password=pulumi.get(__ret__, 'password'),
        website=pulumi.get(__ret__, 'website'))
def get_teams_output(opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetTeamsResult]:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('ctfd:index/getTeams:getTeams', __args__, opts=opts, typ=GetTeamsResult)
    return __ret__.apply(lambda __response__: GetTeamsResult(
        affiliation=pulumi.get(__response__, 'affiliation'),
        banned=pulumi.get(__response__, 'banned'),
        captain=pulumi.get(__response__, 'captain'),
        country=pulumi.get(__response__, 'country'),
        email=pulumi.get(__response__, 'email'),
        hidden=pulumi.get(__response__, 'hidden'),
        id=pulumi.get(__response__, 'id'),
        members=pulumi.get(__response__, 'members'),
        name=pulumi.get(__response__, 'name'),
        password=pulumi.get(__response__, 'password'),
        website=pulumi.get(__response__, 'website')))
