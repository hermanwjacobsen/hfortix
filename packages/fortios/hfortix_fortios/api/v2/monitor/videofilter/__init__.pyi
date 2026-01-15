"""Type stubs for VIDEOFILTER category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .fortiguard_categories import FortiguardCategories

__all__ = [
    "FortiguardCategories",
    "Videofilter",
]


class Videofilter:
    """VIDEOFILTER API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    fortiguard_categories: FortiguardCategories

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize videofilter category with HTTP client."""
        ...
