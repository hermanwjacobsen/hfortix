"""Type stubs for DNSFILTER category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .domain_filter import DomainFilter
    from .profile import Profile

__all__ = [
    "DomainFilter",
    "Profile",
    "Dnsfilter",
]


class Dnsfilter:
    """DNSFILTER API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    domain_filter: DomainFilter
    profile: Profile

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize dnsfilter category with HTTP client."""
        ...
