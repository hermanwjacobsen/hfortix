"""Type stubs for SYSLOGD4 category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .filter import Filter
    from .override_filter import OverrideFilter
    from .override_setting import OverrideSetting
    from .setting import Setting

__all__ = [
    "Filter",
    "OverrideFilter",
    "OverrideSetting",
    "Setting",
    "Syslogd4",
]


class Syslogd4:
    """SYSLOGD4 API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    filter: Filter
    override_filter: OverrideFilter
    override_setting: OverrideSetting
    setting: Setting

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize syslogd4 category with HTTP client."""
        ...
