"""
FortiOS CMDB DLP API
Data Loss Prevention configuration endpoints
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ....http_client import HTTPClient

from .data_type import DataType
from .dictionary import Dictionary
from .exact_data_match import ExactDataMatch
from .filepattern import Filepattern
from .label import Label
from .profile import Profile
from .sensor import Sensor
from .settings import Settings

__all__ = ["DLP"]


class DLP:
    """
    DLP API helper class
    Provides access to Data Loss Prevention configuration endpoints
    """

    def __init__(self, client: "HTTPClient") -> None:
        """
        Initialize DLP helper

        Args:
            client: HTTPClient instance
        """
        self._client = client
        self.data_type = DataType(client)
        self.dictionary = Dictionary(client)
        self.exact_data_match = ExactDataMatch(client)
        self.filepattern = Filepattern(client)
        self.label = Label(client)
        self.profile = Profile(client)
        self.sensor = Sensor(client)
        self.settings = Settings(client)

    def __dir__(self):
        """Control autocomplete to show only public attributes"""
        return [
            "data_type",
            "dictionary",
            "exact_data_match",
            "filepattern",
            "label",
            "profile",
            "sensor",
            "settings",
        ]
