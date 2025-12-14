"""
FortiOS CMDB DNS Filter API
"""

from __future__ import annotations
from .domain_filter import DomainFilter
from .profile import Profile


class DNSFilter:
    """DNS Filter configuration endpoints"""
    
    def __init__(self, client):
        self._client = client
        self.domain_filter = DomainFilter(client)
        self.profile = Profile(client)
