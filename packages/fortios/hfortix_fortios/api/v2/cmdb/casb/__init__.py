"""FortiOS CMDB - Casb category"""

from .attribute_match import AttributeMatch
from .profile import Profile
from .saas_application import SaasApplication
from .user_activity import UserActivity

__all__ = ["AttributeMatch", "Profile", "SaasApplication", "UserActivity"]


class Casb:
    """
    Casb category wrapper.

    This class provides access to all casb CMDB endpoints.
    """

    def __init__(self, client):
        """
        Initialize Casb with all endpoint classes.

        Args:
            client: HTTPClient instance
        """
        self.attribute_match = AttributeMatch(client)
        self.profile = Profile(client)
        self.saas_application = SaasApplication(client)
        self.user_activity = UserActivity(client)
