"""
FortiOS Ethernet OAM API
Ethernet Operations, Administration and Maintenance endpoints
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ....http_client import HTTPClient

__all__ = ['EthernetOAM']


class EthernetOAM:
    """
    Ethernet OAM API helper class
    Provides access to ethernet OAM configuration endpoints
    """

    def __init__(self, client: 'HTTPClient') -> None:
        """
        Initialize EthernetOAM helper

        Args:
            client: HTTPClient instance
        """
        self._client = client

        # Initialize endpoint classes
        from .cfm import Cfm

        self.cfm = Cfm(client)
    
    def __dir__(self):
        """Control autocomplete to show only public attributes"""
        return ['cfm']
