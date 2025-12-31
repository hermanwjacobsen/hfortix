"""
FortiOS LOG - Log Forticloud Forticloud

Log retrieval endpoint for log forticloud forticloud logs.

API Endpoints:
    GET    /log/forticloud/forticloud
    GET    /log/forticloud/forticloud
    GET    /log/forticloud/forticloud
    GET    /log/forticloud/forticloud
    GET    /log/forticloud/forticloud
    GET    /log/forticloud/forticloud
    GET    /log/forticloud/forticloud
    GET    /log/forticloud/forticloud
    GET    /log/forticloud/forticloud

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.log.forticloud.forticloud.get()
    >>>
    >>> # With filters and parameters
    >>> data = fgt.api.log.forticloud.forticloud.get(
    ...     count=100,
    ...     start=0
    ... )

Note:
    This is a read-only endpoint. Only GET operations are supported.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

# Import all the shared log types - they work for FortiCloud too!
from hfortix_fortios.api.v2.log.anomaly import Anomaly
from hfortix_fortios.api.v2.log.app_ctrl import AppCtrl
from hfortix_fortios.api.v2.log.cifs import CIFS
from hfortix_fortios.api.v2.log.dlp import DLP
from hfortix_fortios.api.v2.log.dns import DNS
from hfortix_fortios.api.v2.log.emailfilter import EmailFilter
from hfortix_fortios.api.v2.log.event import Event
from hfortix_fortios.api.v2.log.file_filter import FileFilter
from hfortix_fortios.api.v2.log.gtp import GTP
from hfortix_fortios.api.v2.log.ips import IPS
from hfortix_fortios.api.v2.log.ssh import SSH
from hfortix_fortios.api.v2.log.ssl import SSL
from hfortix_fortios.api.v2.log.traffic import Traffic
from hfortix_fortios.api.v2.log.virus import Virus, VirusArchive
from hfortix_fortios.api.v2.log.voip import VoIP
from hfortix_fortios.api.v2.log.waf import WAF
from hfortix_fortios.api.v2.log.webfilter import Webfilter

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient


class FortiCloud:
    """
    Forticloud Operations.

    Provides read-only access for FortiOS forticloud data.

    Methods:
        get(): Retrieve monitoring/log data (read-only)

    Note:
        This is a read-only endpoint. Configuration changes are not supported.
    """

    def __init__(self, client: "IHTTPClient") -> None:
        """
        Initialize FortiCloud log endpoint

        Args:
            client: HTTP client for API requests
        """
        # Individual log types
        self.virus = Virus(client, "forticloud")
        self.webfilter = Webfilter(client, "forticloud")
        self.waf = WAF(client, "forticloud")
        self.ips = IPS(client, "forticloud")
        self.anomaly = Anomaly(client, "forticloud")
        self.app_ctrl = AppCtrl(client, "forticloud")
        self.emailfilter = EmailFilter(client, "forticloud")
        self.dlp = DLP(client, "forticloud")
        self.voip = VoIP(client, "forticloud")
        self.gtp = GTP(client, "forticloud")
        self.dns = DNS(client, "forticloud")
        self.ssh = SSH(client, "forticloud")
        self.ssl = SSL(client, "forticloud")
        self.cifs = CIFS(client, "forticloud")
        self.file_filter = FileFilter(client, "forticloud")

        # Virus archive (special case)
        self.virus_archive = VirusArchive(client, "forticloud")

        # Traffic subtypes
        self.traffic = Traffic(client, "forticloud")

        # Event subtypes
        self.event = Event(client, "forticloud")

    def __repr__(self) -> str:
        return "<FortiCloud Log API>"
