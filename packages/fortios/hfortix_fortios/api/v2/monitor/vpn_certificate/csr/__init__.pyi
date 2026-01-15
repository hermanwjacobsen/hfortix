"""Type stubs for CSR category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .generate import Generate

__all__ = [
    "Generate",
    "Csr",
]


class Csr:
    """CSR API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    generate: Generate

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize csr category with HTTP client."""
        ...
