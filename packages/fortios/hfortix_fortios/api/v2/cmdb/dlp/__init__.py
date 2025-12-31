"""FortiOS CMDB - Dlp category"""

from .data_type import DataType
from .dictionary import Dictionary
from .exact_data_match import ExactDataMatch
from .filepattern import Filepattern
from .label import Label
from .profile import Profile
from .sensor import Sensor
from .settings import Settings

__all__ = [
    "DataType",
    "Dictionary",
    "ExactDataMatch",
    "Filepattern",
    "Label",
    "Profile",
    "Sensor",
    "Settings",
]


class Dlp:
    """
    Dlp category wrapper.

    This class provides access to all dlp CMDB endpoints.
    """

    def __init__(self, client):
        """
        Initialize Dlp with all endpoint classes.

        Args:
            client: HTTPClient instance
        """
        self.data_type = DataType(client)
        self.dictionary = Dictionary(client)
        self.exact_data_match = ExactDataMatch(client)
        self.filepattern = Filepattern(client)
        self.label = Label(client)
        self.profile = Profile(client)
        self.sensor = Sensor(client)
        self.settings = Settings(client)
