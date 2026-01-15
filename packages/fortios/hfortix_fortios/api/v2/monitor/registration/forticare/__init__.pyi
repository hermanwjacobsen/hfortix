"""Type stubs for FORTICARE category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .add_license import AddLicense
    from .check_connectivity import CheckConnectivity
    from .create import Create
    from .deregister_device import DeregisterDevice
    from .login import Login
    from .transfer import Transfer

__all__ = [
    "AddLicense",
    "CheckConnectivity",
    "Create",
    "DeregisterDevice",
    "Login",
    "Transfer",
    "Forticare",
]


class Forticare:
    """FORTICARE API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    add_license: AddLicense
    check_connectivity: CheckConnectivity
    create: Create
    deregister_device: DeregisterDevice
    login: Login
    transfer: Transfer

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize forticare category with HTTP client."""
        ...
