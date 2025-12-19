"""
FortiOS Monitor - Web Ui
Web UI customization monitoring
"""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ....http_client import HTTPClient

__all__ = ["WebUi"]

from .custom_language import CustomLanguage
from .language import Language, ImportLanguage


class WebUi:
    """WebUi Monitor category class"""

    def __init__(self, client: "HTTPClient") -> None:
        """
        Initialize WebUi Monitor category

        Args:
            client: HTTPClient instance
        """
        self._client = client

        # Initialize endpoints
        self.custom_language = CustomLanguage(client)
        self.language = Language(client)

    def __dir__(self):
        """Control autocomplete to show only public attributes"""
        return ["custom_language", "language"]
