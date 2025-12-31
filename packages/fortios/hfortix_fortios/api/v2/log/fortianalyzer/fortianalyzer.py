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
    >>> from hfortix_fortios import FortiOS
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


class FortiAnalyzer:
    """
    Fortianalyzer Operations.

    Provides read-only access for FortiOS fortianalyzer data.

    Methods:
        get(): Retrieve monitoring/log data (read-only)

    Note:
        This is a read-only endpoint. Configuration changes are not supported.
    """

    def __init__(self, client: "IHTTPClient") -> None:
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
