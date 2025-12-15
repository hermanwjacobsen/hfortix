"""
FortiOS CMDB DNS Filter API
DNS filtering configuration endpoints
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ....http_client import HTTPClient

from .domain_filter import DomainFilter
from .profile import Profile

__all__ = ['DNSFilter']


class DNSFilter:
    """
    DNS Filter API helper class
    Provides access to DNS filtering configuration endpoints
    """
    
    def __init__(self, client: 'HTTPClient') -> None:
        """
        Initialize DNSFilter helper
        
        Args:
            client: HTTPClient instance
        """
        self._client = client
        self.domain_filter = DomainFilter(client)
        self.profile = Profile(client)
    
    def __dir__(self):
        """Control autocomplete to show only public attributes"""
        return ['domain_filter', 'profile']
