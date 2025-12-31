"""FortiOS CMDB - Application category"""

from .custom import Custom
from .group import Group
from .list import List
from .name import Name
from .rule_settings import RuleSettings

__all__ = ["Custom", "Group", "List", "Name", "RuleSettings"]


class Application:
    """
    Application category wrapper.

    This class provides access to all application CMDB endpoints.
    """

    def __init__(self, client):
        """
        Initialize Application with all endpoint classes.

        Args:
            client: HTTPClient instance
        """
        self.custom = Custom(client)
        self.group = Group(client)
        self.list = List(client)
        self.name = Name(client)
        self.rule_settings = RuleSettings(client)
