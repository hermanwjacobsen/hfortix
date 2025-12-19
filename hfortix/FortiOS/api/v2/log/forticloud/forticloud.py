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
    >>> from hfortix.FortiOS import FortiOS
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
from ..anomaly import Anomaly
from ..app_ctrl import AppCtrl
from ..cifs import CIFS
from ..dlp import DLP
from ..dns import DNS
from ..emailfilter import EmailFilter
from ..event import Event
from ..file_filter import FileFilter
from ..gtp import GTP
from ..ips import IPS
from ..ssh import SSH
from ..ssl import SSL
from ..traffic import Traffic
from ..virus import Virus, VirusArchive
from ..voip import VoIP
from ..waf import WAF
from ..webfilter import Webfilter

if TYPE_CHECKING:
    from ....http_client import HTTPClient


class FortiCloud:
    """
    Forticloud Operations.
    
    Provides read-only access for FortiOS forticloud data.

    Methods:
        get(): Retrieve monitoring/log data (read-only)
    
    Note:
        This is a read-only endpoint. Configuration changes are not supported.
    """

    def __init__(self, client: "HTTPClient") -> None:
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
