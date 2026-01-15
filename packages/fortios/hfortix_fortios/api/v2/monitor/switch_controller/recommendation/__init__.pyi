"""Type stubs for RECOMMENDATION category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .pse_config import PseConfig

__all__ = [
    "PseConfig",
    "Recommendation",
]


class Recommendation:
    """RECOMMENDATION API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    pse_config: PseConfig

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize recommendation category with HTTP client."""
        ...
