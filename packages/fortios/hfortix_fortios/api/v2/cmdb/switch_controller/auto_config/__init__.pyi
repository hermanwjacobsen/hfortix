"""Type stubs for AUTO_CONFIG category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .custom import Custom
    from .default import Default
    from .policy import Policy

__all__ = [
    "Custom",
    "Default",
    "Policy",
    "AutoConfig",
]


class AutoConfig:
    """AUTO_CONFIG API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    custom: Custom
    default: Default
    policy: Policy

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize auto_config category with HTTP client."""
        ...
