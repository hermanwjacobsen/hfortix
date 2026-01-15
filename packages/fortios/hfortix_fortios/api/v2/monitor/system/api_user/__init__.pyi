"""Type stubs for API_USER category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .generate_key import GenerateKey

__all__ = [
    "GenerateKey",
    "ApiUser",
]


class ApiUser:
    """API_USER API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    generate_key: GenerateKey

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize api_user category with HTTP client."""
        ...
