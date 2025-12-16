"""
FortiOS Authentication API
Authentication configuration endpoints
"""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ....http_client import HTTPClient

__all__ = ["Authentication"]


class Authentication:
    """
    Authentication API helper class
    Provides access to authentication configuration endpoints
    """

    def __init__(self, client: "HTTPClient") -> None:
        """
        Initialize Authentication helper

        Args:
            client: HTTPClient instance
        """
        self._client = client

        # Initialize endpoint classes
        from .rule import Rule
        from .scheme import Scheme
        from .setting import Setting

        self.rule = Rule(client)
        self.scheme = Scheme(client)
        self.setting = Setting(client)

    def __dir__(self):
        """Control autocomplete to show only public attributes"""
        return ["rule", "scheme", "setting"]
