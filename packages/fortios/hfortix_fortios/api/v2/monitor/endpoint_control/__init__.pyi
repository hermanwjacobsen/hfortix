"""Type stubs for ENDPOINT_CONTROL category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .record_list import RecordList
    from .summary import Summary
    from .avatar import Avatar
    from .ems import Ems
    from .installer import Installer

__all__ = [
    "RecordList",
    "Summary",
    "EndpointControl",
]


class EndpointControl:
    """ENDPOINT_CONTROL API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    avatar: Avatar
    ems: Ems
    installer: Installer
    record_list: RecordList
    summary: Summary

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize endpoint_control category with HTTP client."""
        ...
