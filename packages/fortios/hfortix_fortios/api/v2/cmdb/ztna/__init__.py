"""FortiOS CMDB - Ztna category"""

from .reverse_connector import ReverseConnector
from .traffic_forward_proxy import TrafficForwardProxy
from .web_portal import WebPortal
from .web_portal_bookmark import WebPortalBookmark
from .web_proxy import WebProxy

__all__ = [
    "ReverseConnector",
    "TrafficForwardProxy",
    "WebPortal",
    "WebPortalBookmark",
    "WebProxy",
]


class Ztna:
    """
    Ztna category wrapper.

    This class provides access to all ztna CMDB endpoints.
    """

    def __init__(self, client):
        """
        Initialize Ztna with all endpoint classes.

        Args:
            client: HTTPClient instance
        """
        self.reverse_connector = ReverseConnector(client)
        self.traffic_forward_proxy = TrafficForwardProxy(client)
        self.web_portal = WebPortal(client)
        self.web_portal_bookmark = WebPortalBookmark(client)
        self.web_proxy = WebProxy(client)
