"""FortiOS CMDB - Webfilter category"""

from .content import Content
from .content_header import ContentHeader
from .fortiguard import Fortiguard
from .ftgd_local_cat import FtgdLocalCat
from .ftgd_local_rating import FtgdLocalRating
from .ftgd_local_risk import FtgdLocalRisk
from .ftgd_risk_level import FtgdRiskLevel
from .ips_urlfilter_cache_setting import IpsUrlfilterCacheSetting
from .ips_urlfilter_setting import IpsUrlfilterSetting
from .ips_urlfilter_setting6 import IpsUrlfilterSetting6
from .override import Override
from .profile import Profile
from .search_engine import SearchEngine
from .urlfilter import Urlfilter

__all__ = [
    "Content",
    "ContentHeader",
    "Fortiguard",
    "FtgdLocalCat",
    "FtgdLocalRating",
    "FtgdLocalRisk",
    "FtgdRiskLevel",
    "IpsUrlfilterCacheSetting",
    "IpsUrlfilterSetting",
    "IpsUrlfilterSetting6",
    "Override",
    "Profile",
    "SearchEngine",
    "Urlfilter",
]


class Webfilter:
    """
    Webfilter category wrapper.

    This class provides access to all webfilter CMDB endpoints.
    """

    def __init__(self, client):
        """
        Initialize Webfilter with all endpoint classes.

        Args:
            client: HTTPClient instance
        """
        self.content = Content(client)
        self.content_header = ContentHeader(client)
        self.fortiguard = Fortiguard(client)
        self.ftgd_local_cat = FtgdLocalCat(client)
        self.ftgd_local_rating = FtgdLocalRating(client)
        self.ftgd_local_risk = FtgdLocalRisk(client)
        self.ftgd_risk_level = FtgdRiskLevel(client)
        self.ips_urlfilter_cache_setting = IpsUrlfilterCacheSetting(client)
        self.ips_urlfilter_setting = IpsUrlfilterSetting(client)
        self.ips_urlfilter_setting6 = IpsUrlfilterSetting6(client)
        self.override = Override(client)
        self.profile = Profile(client)
        self.search_engine = SearchEngine(client)
        self.urlfilter = Urlfilter(client)
