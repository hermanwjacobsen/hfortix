"""
FortiOS CMDB - CASB (Cloud Access Security Broker)
Configure CASB security policies and rules
"""

from .attribute_match import AttributeMatch
from .saas_application import SaasApplication


class Casb:
    """CASB category class"""
    
    def __init__(self, client):
        """
        Initialize CASB category
        
        Args:
            client: FortiOS client instance
        """
        self._client = client
        
        # Initialize endpoints
        self.attribute_match = AttributeMatch(client)
        self.saas_application = SaasApplication(client)
