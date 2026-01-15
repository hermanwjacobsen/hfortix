"""Type stubs for IPS category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .custom import Custom
    from .decoder import Decoder
    from .global_ import Global
    from .rule import Rule
    from .rule_settings import RuleSettings
    from .sensor import Sensor
    from .settings import Settings
    from .view_map import ViewMap

__all__ = [
    "Custom",
    "Decoder",
    "Global",
    "Rule",
    "RuleSettings",
    "Sensor",
    "Settings",
    "ViewMap",
    "Ips",
]


class Ips:
    """IPS API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    custom: Custom
    decoder: Decoder
    global_: Global
    rule: Rule
    rule_settings: RuleSettings
    sensor: Sensor
    settings: Settings
    view_map: ViewMap

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize ips category with HTTP client."""
        ...
