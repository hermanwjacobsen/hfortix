"""
FortiOS CMDB - Automation API

This module provides access to FortiOS automation configuration endpoints.
"""
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ....http_client import HTTPClient

__all__ = ['Automation']

from .setting import Setting


class Automation:
    """Automation configuration endpoints"""

    def __init__(self, client: 'HTTPClient') -> None:
        """
        Initialize Automation API

        Args:
            client: HTTPClient instance
        """
        self._client = client

        # Initialize endpoint classes
        self.setting = Setting(client)
    
    def __dir__(self):
        """Control autocomplete to show only public attributes"""
        return ['setting']
