"""
FortiOS Endpoint Control API
Endpoint control configuration endpoints
"""
from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ....client import FortiOS


class EndpointControl:
    """
    Endpoint Control API helper class
    Provides access to endpoint control configuration endpoints
    """

    def __init__(self, client: 'FortiOS') -> None:
        """
        Initialize EndpointControl helper

        Args:
            client: FortiOS client instance
        """
        self._client = client

        # Initialize endpoint classes
        from .fctems import Fctems
        from .fctems_override import FctemsOverride
        from .settings import Settings

        self.fctems = Fctems(client)
        self.fctems_override = FctemsOverride(client)
        self.settings = Settings(client)
