"""Type stubs for INITIAL_CONFIG category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .template import Template
    from .vlans import Vlans

__all__ = [
    "Template",
    "Vlans",
    "InitialConfig",
]


class InitialConfig:
    """INITIAL_CONFIG API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    template: Template
    vlans: Vlans

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize initial_config category with HTTP client."""
        ...
