"""Type stubs for IPS category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .anomaly import Anomaly
    from .hold_signatures import HoldSignatures
    from .metadata import Metadata
    from .rate_based import RateBased
    from .session import Session

__all__ = [
    "Anomaly",
    "HoldSignatures",
    "Metadata",
    "RateBased",
    "Ips",
]


class Ips:
    """IPS API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    session: Session
    anomaly: Anomaly
    hold_signatures: HoldSignatures
    metadata: Metadata
    rate_based: RateBased

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize ips category with HTTP client."""
        ...
