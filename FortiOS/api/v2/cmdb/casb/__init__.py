"""
FortiOS CMDB - CASB (Cloud Access Security Broker)
Configure CASB security policies and rules
"""
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ....client import FortiOS

from .attribute_match import AttributeMatch
from .profile import Profile
from .saas_application import SaasApplication
from .user_activity import UserActivity


class Casb:
    """CASB category class"""

    def __init__(self, client: 'FortiOS') -> None:
        """
        Initialize CASB category

        Args:
            client: FortiOS client instance
        """
        self._client = client

        # Initialize endpoints
        self.attribute_match = AttributeMatch(client)
        self.profile = Profile(client)
        self.saas_application = SaasApplication(client)
        self.user_activity = UserActivity(client)
