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
from .. import _utilities

import types

__config__ = pulumi.Config('ctfd')


class _ExportableConfig(types.ModuleType):
    @property
    def api_key(self) -> Optional[str]:
        """
        User API key. Could use `CTFD_API_KEY` environment variable instead. Despite being the most convenient way to
        authenticate yourself, we do not recommend it as you will probably generate a long-live token without any rotation
        policy.
        """
        return __config__.get('apiKey')

    @property
    def nonce(self) -> Optional[str]:
        """
        User session nonce, comes with session. Could use `CTFD_NONCE` environment variable instead.
        """
        return __config__.get('nonce')

    @property
    def session(self) -> Optional[str]:
        """
        User session token, comes with nonce. Could use `CTFD_SESSION` environment variable instead.
        """
        return __config__.get('session')

    @property
    def url(self) -> Optional[str]:
        """
        CTFd base URL (e.g. `https://my-ctf.lan`). Could use `CTFD_URL` environment variable instead.
        """
        return __config__.get('url')

