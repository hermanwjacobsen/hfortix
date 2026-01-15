"""Type stubs for PRIVATE_DATA_ENCRYPTION category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .set import Set

__all__ = [
    "Set",
    "PrivateDataEncryption",
]


class PrivateDataEncryption:
    """PRIVATE_DATA_ENCRYPTION API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    set: Set

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize private_data_encryption category with HTTP client."""
        ...
