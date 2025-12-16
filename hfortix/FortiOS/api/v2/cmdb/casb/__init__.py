"""
FortiOS CMDB - CASB (Cloud Access Security Broker)
Configure CASB security policies and rules
"""
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ....http_client import HTTPClient

__all__ = ['Casb']

from .attribute_match import AttributeMatch
from .profile import Profile
from .saas_application import SaasApplication
from .user_activity import UserActivity


class Casb:
    """CASB category class"""

    def __init__(self, client: 'HTTPClient') -> None:
        """
        Initialize CASB category

        Args:
            client: HTTPClient instance
        """
        self._client = client

        # Initialize endpoints
        self.attribute_match = AttributeMatch(client)
        self.profile = Profile(client)
        self.saas_application = SaasApplication(client)
        self.user_activity = UserActivity(client)
    
    def __dir__(self):
        """Control autocomplete to show only public attributes"""
        return ['attribute_match', 'profile', 'saas_application', 'user_activity']
