"""
FortiOS CMDB DLP API
"""

from __future__ import annotations
from .data_type import DataType
from .dictionary import Dictionary
from .exact_data_match import ExactDataMatch
from .filepattern import Filepattern
from .label import Label
from .profile import Profile
from .sensor import Sensor
from .settings import Settings


class DLP:
    """DLP configuration endpoints"""
    
    def __init__(self, client):
        self._client = client
        self.data_type = DataType(client)
        self.dictionary = Dictionary(client)
        self.exact_data_match = ExactDataMatch(client)
        self.filepattern = Filepattern(client)
        self.label = Label(client)
        self.profile = Profile(client)
        self.sensor = Sensor(client)
        self.settings = Settings(client)
