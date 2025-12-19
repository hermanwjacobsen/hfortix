"""
FortiOS Monitor - Firmware
Firmware upgrade monitoring and operations
"""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ....http_client import HTTPClient

__all__ = ["Firmware"]

from .extension_device import ExtensionDevice


class Firmware:
    """Firmware Monitor category class"""

    def __init__(self, client: "HTTPClient") -> None:
        """
        Initialize Firmware Monitor category

        Args:
            client: HTTPClient instance
        """
        self._client = client

        # Initialize endpoints
        self.extension_device = ExtensionDevice(client)

    def __dir__(self):
        """Control autocomplete to show only public attributes"""
        return [
            "extension_device"
        ]
