"""
FortiOS Authentication API
Authentication configuration endpoints
"""
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ....client import FortiOS


class Authentication:
    """
    Authentication API helper class
    Provides access to authentication configuration endpoints
    """

    def __init__(self, client: 'FortiOS') -> None:
        """
        Initialize Authentication helper

        Args:
            client: FortiOS client instance
        """
        self._client = client

        # Initialize endpoint classes
        from .rule import Rule
        from .scheme import Scheme
        from .setting import Setting

        self.rule = Rule(client)
        self.scheme = Scheme(client)
        self.setting = Setting(client)
