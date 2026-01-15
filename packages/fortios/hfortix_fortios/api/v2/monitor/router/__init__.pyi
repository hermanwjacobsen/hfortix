"""Type stubs for ROUTER category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .charts import Charts
    from .ipv4 import Ipv4
    from .ipv6 import Ipv6
    from .lookup_policy import LookupPolicy
    from .policy import Policy
    from .policy6 import Policy6
    from .statistics import Statistics
    from .bgp import Bgp
    from .lookup import Lookup
    from .ospf import Ospf
    from .sdwan import Sdwan

__all__ = [
    "Charts",
    "Ipv4",
    "Ipv6",
    "LookupPolicy",
    "Policy",
    "Policy6",
    "Statistics",
    "Router",
]


class Router:
    """ROUTER API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    bgp: Bgp
    lookup: Lookup
    ospf: Ospf
    sdwan: Sdwan
    charts: Charts
    ipv4: Ipv4
    ipv6: Ipv6
    lookup_policy: LookupPolicy
    policy: Policy
    policy6: Policy6
    statistics: Statistics

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize router category with HTTP client."""
        ...
