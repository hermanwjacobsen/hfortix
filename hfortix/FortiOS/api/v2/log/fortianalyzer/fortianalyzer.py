"""
FortiOS Log - FortiAnalyzer Storage

Main orchestrator for FortiAnalyzer log API endpoints.
Retrieves logs from FortiAnalyzer (when FortiGate is configured to send logs to FortiAnalyzer).

API Endpoints:
    GET /fortianalyzer/virus/archive                     - Get quarantined virus file metadata
    GET /fortianalyzer/{type}/archive                    - Get archived items (ips, app-ctrl only)
    GET /fortianalyzer/{type}/archive-download           - Download archived file (ips, app-ctrl only)
    GET /fortianalyzer/{type}/raw                        - Get raw log data (all types)
    GET /fortianalyzer/traffic/{subtype}/raw             - Get raw traffic logs by subtype
    GET /fortianalyzer/event/{subtype}/raw               - Get raw event logs by subtype
    GET /fortianalyzer/{type}                            - Get formatted log data for type
    GET /fortianalyzer/traffic/{subtype}                 - Get formatted traffic logs by subtype
    GET /fortianalyzer/event/{subtype}                   - Get formatted event logs by subtype
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
    FortiAnalyzer log endpoint
    
    Retrieves logs from FortiAnalyzer when FortiGate is configured to send logs to FortiAnalyzer.
    Uses the same structure as disk logs but with "fortianalyzer" storage.
    
    Examples:
        # IPS archive
        fgt.api.log.fortianalyzer.ips.archive.get()
        fgt.api.log.fortianalyzer.ips.archive.get(mkey=123)
        
        # IPS logs
        fgt.api.log.fortianalyzer.ips.get(rows=100)
        fgt.api.log.fortianalyzer.ips.raw.get(rows=100)
        
        # App Control
        fgt.api.log.fortianalyzer.app_ctrl.archive.get()
        fgt.api.log.fortianalyzer.app_ctrl.get(rows=50)
        
        # Virus
        fgt.api.log.fortianalyzer.virus_archive.get()
        fgt.api.log.fortianalyzer.virus.get(rows=100)
        
        # All log types
        fgt.api.log.fortianalyzer.webfilter.get(rows=100)
        fgt.api.log.fortianalyzer.waf.get(rows=100)
        fgt.api.log.fortianalyzer.anomaly.get(rows=100)
        fgt.api.log.fortianalyzer.emailfilter.get(rows=100)
        fgt.api.log.fortianalyzer.dlp.get(rows=100)
        fgt.api.log.fortianalyzer.voip.get(rows=100)
        fgt.api.log.fortianalyzer.gtp.get(rows=100)
        fgt.api.log.fortianalyzer.dns.get(rows=100)
        fgt.api.log.fortianalyzer.ssh.get(rows=100)
        fgt.api.log.fortianalyzer.ssl.get(rows=100)
        fgt.api.log.fortianalyzer.cifs.get(rows=100)
        fgt.api.log.fortianalyzer.file_filter.get(rows=100)
        
        # Traffic subtypes
        fgt.api.log.fortianalyzer.traffic.forward.get(rows=100)
        fgt.api.log.fortianalyzer.traffic.local.get(rows=100)
        fgt.api.log.fortianalyzer.traffic.multicast.get(rows=100)
        fgt.api.log.fortianalyzer.traffic.sniffer.get(rows=100)
        fgt.api.log.fortianalyzer.traffic.fortiview.get(rows=100)
        fgt.api.log.fortianalyzer.traffic.threat.get(rows=100)
        
        # Event subtypes
        fgt.api.log.fortianalyzer.event.vpn.get(rows=50)
        fgt.api.log.fortianalyzer.event.user.get(rows=50)
        fgt.api.log.fortianalyzer.event.router.get(rows=50)
        fgt.api.log.fortianalyzer.event.wireless.get(rows=50)
        fgt.api.log.fortianalyzer.event.wad.get(rows=50)
        fgt.api.log.fortianalyzer.event.endpoint.get(rows=50)
        fgt.api.log.fortianalyzer.event.ha.get(rows=50)
        fgt.api.log.fortianalyzer.event.compliance_check.get(rows=50)
        fgt.api.log.fortianalyzer.event.security_rating.get(rows=50)
        fgt.api.log.fortianalyzer.event.fortiextender.get(rows=50)
        fgt.api.log.fortianalyzer.event.connector.get(rows=50)
        fgt.api.log.fortianalyzer.event.system.get(rows=50)
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
