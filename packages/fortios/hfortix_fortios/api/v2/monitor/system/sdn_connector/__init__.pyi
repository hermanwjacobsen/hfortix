"""Type stubs for SDN_CONNECTOR category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .nsx_security_tags import NsxSecurityTags
    from .status import Status
    from .update import Update
    from .validate_gcp_key import ValidateGcpKey

__all__ = [
    "NsxSecurityTags",
    "Status",
    "Update",
    "ValidateGcpKey",
    "SdnConnector",
]


class SdnConnector:
    """SDN_CONNECTOR API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    nsx_security_tags: NsxSecurityTags
    status: Status
    update: Update
    validate_gcp_key: ValidateGcpKey

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize sdn_connector category with HTTP client."""
        ...
