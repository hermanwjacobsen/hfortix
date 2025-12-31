"""FortiOS CMDB - Ips category"""

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
]


class Ips:
    """
    Ips category wrapper.

    This class provides access to all ips CMDB endpoints.
    """

    def __init__(self, client):
        """
        Initialize Ips with all endpoint classes.

        Args:
            client: HTTPClient instance
        """
        self.custom = Custom(client)
        self.decoder = Decoder(client)
        self.global_ = Global(client)
        self.rule = Rule(client)
        self.rule_settings = RuleSettings(client)
        self.sensor = Sensor(client)
        self.settings = Settings(client)
        self.view_map = ViewMap(client)
