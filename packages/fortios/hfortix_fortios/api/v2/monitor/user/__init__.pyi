"""Type stubs for USER category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .collected_email import CollectedEmail
    from .banned import Banned
    from .device import Device
    from .firewall import Firewall
    from .fortitoken import Fortitoken
    from .fortitoken_cloud import FortitokenCloud
    from .fsso import Fsso
    from .guest import Guest
    from .info import Info
    from .local import Local
    from .password_policy_conform import PasswordPolicyConform
    from .proxy import Proxy
    from .query import Query
    from .radius import Radius
    from .scim import Scim
    from .tacacs_plus import TacacsPlus

__all__ = [
    "CollectedEmail",
    "User",
]


class User:
    """USER API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    banned: Banned
    device: Device
    firewall: Firewall
    fortitoken: Fortitoken
    fortitoken_cloud: FortitokenCloud
    fsso: Fsso
    guest: Guest
    info: Info
    local: Local
    password_policy_conform: PasswordPolicyConform
    proxy: Proxy
    query: Query
    radius: Radius
    scim: Scim
    tacacs_plus: TacacsPlus
    collected_email: CollectedEmail

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize user category with HTTP client."""
        ...
