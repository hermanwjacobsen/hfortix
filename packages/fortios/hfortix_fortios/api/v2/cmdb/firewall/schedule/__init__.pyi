"""Type stubs for SCHEDULE category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .group import Group
    from .onetime import Onetime
    from .recurring import Recurring

__all__ = [
    "Group",
    "Onetime",
    "Recurring",
    "Schedule",
]


class Schedule:
    """SCHEDULE API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    group: Group
    onetime: Onetime
    recurring: Recurring

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize schedule category with HTTP client."""
        ...
