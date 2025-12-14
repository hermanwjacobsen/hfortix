"""
FortiOS Application API
Application control configuration endpoints
"""
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ....client import FortiOS


class Application:
    """
    Application API helper class
    Provides access to application control configuration endpoints
    """

    def __init__(self, client: 'FortiOS') -> None:
        """
        Initialize Application helper

        Args:
            client: FortiOS client instance
        """
        self._client = client

        # Initialize endpoint classes
        from .custom import Custom
        from .group import Group
        from .list import List
        from .name import Name

        self.custom = Custom(client)
        self.group = Group(client)
        self.list = List(client)
        self.name = Name(client)
