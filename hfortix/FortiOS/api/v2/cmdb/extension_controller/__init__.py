"""
FortiOS Extension Controller API
Extension controller configuration endpoints for FortiExtender and FortiGate connectors
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ....http_client import HTTPClient

__all__ = ["ExtensionController"]


class ExtensionController:
    """
    Extension Controller API helper class
    Provides access to extension controller configuration endpoints
    """

    def __init__(self, client: "HTTPClient") -> None:
        """
        Initialize ExtensionController helper

        Args:
            client: HTTPClient instance
        """
        self._client = client

        # Initialize endpoint classes
        from .dataplan import Dataplan
        from .extender import Extender
        from .extender_profile import ExtenderProfile
        from .extender_vap import ExtenderVap
        from .fortigate import Fortigate
        from .fortigate_profile import FortigateProfile

        self.dataplan = Dataplan(client)
        self.extender = Extender(client)
        self.extender_profile = ExtenderProfile(client)
        self.extender_vap = ExtenderVap(client)
        self.fortigate = Fortigate(client)
        self.fortigate_profile = FortigateProfile(client)

    def __dir__(self):
        """Control autocomplete to show only public attributes"""
        return [
            "dataplan",
            "extender",
            "extender_profile",
            "extender_vap",
            "fortigate",
            "fortigate_profile",
        ]
