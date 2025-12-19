"""
FortiOS LOG - Log Fortianalyzer Fortianalyzer

Log retrieval endpoint for log fortianalyzer fortianalyzer logs.

API Endpoints:
    GET    /log/fortianalyzer/fortianalyzer
    GET    /log/fortianalyzer/fortianalyzer
    GET    /log/fortianalyzer/fortianalyzer
    GET    /log/fortianalyzer/fortianalyzer
    GET    /log/fortianalyzer/fortianalyzer
    GET    /log/fortianalyzer/fortianalyzer
    GET    /log/fortianalyzer/fortianalyzer
    GET    /log/fortianalyzer/fortianalyzer
    GET    /log/fortianalyzer/fortianalyzer

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>> 
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.log.fortianalyzer.fortianalyzer.get()
    >>> 
    >>> # With filters and parameters
    >>> data = fgt.api.log.fortianalyzer.fortianalyzer.get(
    ...     count=100,
    ...     start=0
    ... )

Note:
    This is a read-only endpoint. Only GET operations are supported.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

# Import all the shared log types - they work for FortiAnalyzer too!
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


class FortiAnalyzer:
    """
    Fortianalyzer Operations.
    
    Provides read-only access for FortiOS fortianalyzer data.

    Methods:
        get(): Retrieve monitoring/log data (read-only)
    
    Note:
        This is a read-only endpoint. Configuration changes are not supported.
    """

    def __init__(self, client: "HTTPClient") -> None:
        """Initialize FortiAnalyzer log endpoint."""
        self._client = client
        
        # Log types with archive support (pass "fortianalyzer" as storage)
        self.ips = IPS(client, "fortianalyzer")
        self.app_ctrl = AppCtrl(client, "fortianalyzer")
        
        # Virus (special archive endpoint)
        self.virus = Virus(client, "fortianalyzer")
        self.virus_archive = VirusArchive(client, "fortianalyzer")
        
        # All other log types
        self.webfilter = Webfilter(client, "fortianalyzer")
        self.waf = WAF(client, "fortianalyzer")
        self.anomaly = Anomaly(client, "fortianalyzer")
        self.emailfilter = EmailFilter(client, "fortianalyzer")
        self.dlp = DLP(client, "fortianalyzer")
        self.voip = VoIP(client, "fortianalyzer")
        self.gtp = GTP(client, "fortianalyzer")
        self.dns = DNS(client, "fortianalyzer")
        self.ssh = SSH(client, "fortianalyzer")
        self.ssl = SSL(client, "fortianalyzer")
        self.cifs = CIFS(client, "fortianalyzer")
        self.file_filter = FileFilter(client, "fortianalyzer")
        
        # Traffic subtypes
        self.traffic = Traffic(client, "fortianalyzer")
        
        # Event subtypes
        self.event = Event(client, "fortianalyzer")


__all__ = ["FortiAnalyzer"]
