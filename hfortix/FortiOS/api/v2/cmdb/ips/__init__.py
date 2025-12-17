"""
FortiOS IPS API

Intrusion Prevention System (IPS) configuration for threat protection.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ...http_client import HTTPClient


class Ips:
    """IPS API endpoints"""

    def __init__(self, client: "HTTPClient") -> None:
        self._client = client

        from .custom import Custom
        from .decoder import Decoder
        from .global_ import Global
        from .rule import Rule
        from .rule_settings import RuleSettings
        from .sensor import Sensor
        from .settings import Settings
        from .view_map import ViewMap

        self.custom = Custom(client)
        self.decoder = Decoder(client)
        self.global_ = Global(client)
        self.rule = Rule(client)
        self.rule_settings = RuleSettings(client)
        self.sensor = Sensor(client)
        self.settings = Settings(client)
        self.view_map = ViewMap(client)
