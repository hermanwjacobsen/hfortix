"""Type stubs for QOS category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .dot1p_map import Dot1pMap
    from .ip_dscp_map import IpDscpMap
    from .qos_policy import QosPolicy
    from .queue_policy import QueuePolicy

__all__ = [
    "Dot1pMap",
    "IpDscpMap",
    "QosPolicy",
    "QueuePolicy",
    "Qos",
]


class Qos:
    """QOS API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    dot1p_map: Dot1pMap
    ip_dscp_map: IpDscpMap
    qos_policy: QosPolicy
    queue_policy: QueuePolicy

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize qos category with HTTP client."""
        ...
