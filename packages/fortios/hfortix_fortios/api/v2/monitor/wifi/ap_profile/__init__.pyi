"""Type stubs for AP_PROFILE category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .create_default import CreateDefault

__all__ = [
    "CreateDefault",
    "ApProfile",
]


class ApProfile:
    """AP_PROFILE API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    create_default: CreateDefault

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize ap_profile category with HTTP client."""
        ...
