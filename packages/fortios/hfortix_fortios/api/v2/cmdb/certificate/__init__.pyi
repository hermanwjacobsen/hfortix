"""Type stubs for CERTIFICATE category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .ca import Ca
    from .crl import Crl
    from .hsm_local import HsmLocal
    from .local import Local
    from .remote import Remote

__all__ = [
    "Ca",
    "Crl",
    "HsmLocal",
    "Local",
    "Remote",
    "Certificate",
]


class Certificate:
    """CERTIFICATE API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    ca: Ca
    crl: Crl
    hsm_local: HsmLocal
    local: Local
    remote: Remote

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize certificate category with HTTP client."""
        ...
