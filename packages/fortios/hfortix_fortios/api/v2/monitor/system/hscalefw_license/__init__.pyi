"""Type stubs for HSCALEFW_LICENSE category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .upload import Upload

__all__ = [
    "Upload",
    "HscalefwLicense",
]


class HscalefwLicense:
    """HSCALEFW_LICENSE API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    upload: Upload

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize hscalefw_license category with HTTP client."""
        ...
