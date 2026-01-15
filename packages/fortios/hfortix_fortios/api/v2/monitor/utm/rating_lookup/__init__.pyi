"""Type stubs for RATING_LOOKUP category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .select import Select

__all__ = [
    "Select",
    "RatingLookup",
]


class RatingLookup:
    """RATING_LOOKUP API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    select: Select

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize rating_lookup category with HTTP client."""
        ...
