"""Type stubs for FORTICLOUD category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .device_status import DeviceStatus
    from .disclaimer import Disclaimer
    from .domains import Domains
    from .login import Login
    from .logout import Logout
    from .migrate import Migrate
    from .register_device import RegisterDevice

__all__ = [
    "DeviceStatus",
    "Disclaimer",
    "Domains",
    "Login",
    "Logout",
    "Migrate",
    "RegisterDevice",
    "Forticloud",
]


class Forticloud:
    """FORTICLOUD API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    device_status: DeviceStatus
    disclaimer: Disclaimer
    domains: Domains
    login: Login
    logout: Logout
    migrate: Migrate
    register_device: RegisterDevice

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize forticloud category with HTTP client."""
        ...
