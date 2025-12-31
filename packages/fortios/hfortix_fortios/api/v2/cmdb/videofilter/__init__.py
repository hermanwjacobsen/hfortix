"""FortiOS CMDB - Videofilter category"""

from .keyword import Keyword
from .profile import Profile
from .youtube_key import YoutubeKey

__all__ = ["Keyword", "Profile", "YoutubeKey"]


class Videofilter:
    """
    Videofilter category wrapper.

    This class provides access to all videofilter CMDB endpoints.
    """

    def __init__(self, client):
        """
        Initialize Videofilter with all endpoint classes.

        Args:
            client: HTTPClient instance
        """
        self.keyword = Keyword(client)
        self.profile = Profile(client)
        self.youtube_key = YoutubeKey(client)
