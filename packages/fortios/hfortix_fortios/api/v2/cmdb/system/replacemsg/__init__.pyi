"""Type stubs for REPLACEMSG category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .admin import Admin
    from .alertmail import Alertmail
    from .auth import Auth
    from .automation import Automation
    from .fortiguard_wf import FortiguardWf
    from .http import Http
    from .mail import Mail
    from .nac_quar import NacQuar
    from .spam import Spam
    from .sslvpn import Sslvpn
    from .traffic_quota import TrafficQuota
    from .utm import Utm

__all__ = [
    "Admin",
    "Alertmail",
    "Auth",
    "Automation",
    "FortiguardWf",
    "Http",
    "Mail",
    "NacQuar",
    "Spam",
    "Sslvpn",
    "TrafficQuota",
    "Utm",
    "Replacemsg",
]


class Replacemsg:
    """REPLACEMSG API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    admin: Admin
    alertmail: Alertmail
    auth: Auth
    automation: Automation
    fortiguard_wf: FortiguardWf
    http: Http
    mail: Mail
    nac_quar: NacQuar
    spam: Spam
    sslvpn: Sslvpn
    traffic_quota: TrafficQuota
    utm: Utm

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize replacemsg category with HTTP client."""
        ...
