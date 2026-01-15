"""Type stubs for WEBFILTER category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .fortiguard_categories import FortiguardCategories
    from .trusted_urls import TrustedUrls
    from .category_quota import CategoryQuota
    from .malicious_urls import MaliciousUrls
    from .override import Override

__all__ = [
    "FortiguardCategories",
    "TrustedUrls",
    "Webfilter",
]


class Webfilter:
    """WEBFILTER API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    category_quota: CategoryQuota
    malicious_urls: MaliciousUrls
    override: Override
    fortiguard_categories: FortiguardCategories
    trusted_urls: TrustedUrls

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize webfilter category with HTTP client."""
        ...
