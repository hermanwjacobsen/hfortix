"""FortiOS CMDB - Antivirus category"""

from .exempt_list import ExemptList
from .profile import Profile
from .quarantine import Quarantine
from .settings import Settings

__all__ = ["ExemptList", "Profile", "Quarantine", "Settings"]


class Antivirus:
    """
    Antivirus category wrapper.

    This class provides access to all antivirus CMDB endpoints.
    """

    def __init__(self, client):
        """
        Initialize Antivirus with all endpoint classes.

        Args:
            client: HTTPClient instance
        """
        self.exempt_list = ExemptList(client)
        self.profile = Profile(client)
        self.quarantine = Quarantine(client)
        self.settings = Settings(client)
