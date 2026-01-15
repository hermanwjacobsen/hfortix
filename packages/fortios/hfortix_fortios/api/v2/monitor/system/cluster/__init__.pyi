"""Type stubs for CLUSTER category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .state import State

__all__ = [
    "State",
    "Cluster",
]


class Cluster:
    """CLUSTER API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    state: State

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize cluster category with HTTP client."""
        ...
