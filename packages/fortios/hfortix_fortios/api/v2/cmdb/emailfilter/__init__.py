"""FortiOS CMDB - Emailfilter category"""

from .block_allow_list import BlockAllowList
from .bword import Bword
from .dnsbl import Dnsbl
from .fortishield import Fortishield
from .iptrust import Iptrust
from .mheader import Mheader
from .options import Options
from .profile import Profile

__all__ = [
    "BlockAllowList",
    "Bword",
    "Dnsbl",
    "Fortishield",
    "Iptrust",
    "Mheader",
    "Options",
    "Profile",
]


class Emailfilter:
    """
    Emailfilter category wrapper.

    This class provides access to all emailfilter CMDB endpoints.
    """

    def __init__(self, client):
        """
        Initialize Emailfilter with all endpoint classes.

        Args:
            client: HTTPClient instance
        """
        self.block_allow_list = BlockAllowList(client)
        self.bword = Bword(client)
        self.dnsbl = Dnsbl(client)
        self.fortishield = Fortishield(client)
        self.iptrust = Iptrust(client)
        self.mheader = Mheader(client)
        self.options = Options(client)
        self.profile = Profile(client)
