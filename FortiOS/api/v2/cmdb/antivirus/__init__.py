"""
FortiOS Antivirus API
Antivirus configuration endpoints
"""
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ....http_client import HTTPClient

__all__ = ['Antivirus']


class Antivirus:
    """
    Antivirus API helper class
    Provides access to antivirus configuration endpoints
    """

    def __init__(self, client: 'HTTPClient') -> None:
        """
        Initialize Antivirus helper

        Args:
            client: HTTPClient instance
        """
        self._client = client

        # Initialize endpoint classes
        # Note: exempt-list.py has a dash, so we import it differently
        import importlib
        exempt_list_module = importlib.import_module('.exempt-list', package='FortiOS.api.v2.cmdb.antivirus')
        ExemptList = exempt_list_module.ExemptList
        self.exempt_list = ExemptList(client)

        # Import profile, quarantine, and settings normally
        from .profile import Profile
        from .quarantine import Quarantine
        from .settings import Settings

        self.profile = Profile(client)
        self.quarantine = Quarantine(client)
        self.settings = Settings(client)
    
    def __dir__(self):
        """Control autocomplete to show only public attributes"""
        return ['exempt_list', 'profile', 'quarantine', 'settings']
