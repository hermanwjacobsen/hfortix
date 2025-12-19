"""
FortiOS Log - Disk Storage

Main orchestrator for disk log API endpoints.

API Endpoints:
    GET /disk/virus/archive                      - Get quarantined virus file metadata
    GET /disk/{type}/archive                     - Get archived items (ips, app-ctrl only)
    GET /disk/{type}/archive-download            - Download archived file (ips, app-ctrl only)
    GET /disk/{type}/raw                         - Get raw log data (all types)
    GET /disk/traffic/{subtype}/raw              - Get raw traffic logs by subtype
    GET /disk/event/{subtype}/raw                - Get raw event logs by subtype
    GET /disk/{type}                             - Get formatted log data for type
    GET /disk/traffic/{subtype}                  - Get formatted traffic logs by subtype
    GET /disk/event/{subtype}                    - Get formatted event logs by subtype
"""

from __future__ import annotations

from typing import TYPE_CHECKING

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


class Disk:
    """
    Disk log endpoint
    
    Examples:
        # IPS archive
        fgt.api.log.disk.ips.archive.get()
        fgt.api.log.disk.ips.archive.get(mkey=123)
        
        # IPS logs
        fgt.api.log.disk.ips.get(rows=100)
        fgt.api.log.disk.ips.raw.get(rows=100)
        
        # App Control
        fgt.api.log.disk.app_ctrl.archive.get()
        fgt.api.log.disk.app_ctrl.get(rows=50)
        
        # Virus
        fgt.api.log.disk.virus_archive.get()
        fgt.api.log.disk.virus.get(rows=100)
        
        # All log types
        fgt.api.log.disk.webfilter.get(rows=100)
        fgt.api.log.disk.waf.get(rows=100)
        fgt.api.log.disk.anomaly.get(rows=100)
        fgt.api.log.disk.emailfilter.get(rows=100)
        fgt.api.log.disk.dlp.get(rows=100)
        fgt.api.log.disk.voip.get(rows=100)
        fgt.api.log.disk.gtp.get(rows=100)
        fgt.api.log.disk.dns.get(rows=100)
        fgt.api.log.disk.ssh.get(rows=100)
        fgt.api.log.disk.ssl.get(rows=100)
        fgt.api.log.disk.cifs.get(rows=100)
        fgt.api.log.disk.file_filter.get(rows=100)
        
        # Traffic subtypes
        fgt.api.log.disk.traffic.forward.get(rows=100)
        fgt.api.log.disk.traffic.local.get(rows=100)
        fgt.api.log.disk.traffic.multicast.get(rows=100)
        fgt.api.log.disk.traffic.sniffer.get(rows=100)
        fgt.api.log.disk.traffic.fortiview.get(rows=100)
        fgt.api.log.disk.traffic.threat.get(rows=100)
        
        # Event subtypes
        fgt.api.log.disk.event.vpn.get(rows=50)
        fgt.api.log.disk.event.user.get(rows=50)
        fgt.api.log.disk.event.router.get(rows=50)
        fgt.api.log.disk.event.wireless.get(rows=50)
        fgt.api.log.disk.event.wad.get(rows=50)
        fgt.api.log.disk.event.endpoint.get(rows=50)
        fgt.api.log.disk.event.ha.get(rows=50)
        fgt.api.log.disk.event.compliance_check.get(rows=50)
        fgt.api.log.disk.event.security_rating.get(rows=50)
        fgt.api.log.disk.event.fortiextender.get(rows=50)
        fgt.api.log.disk.event.connector.get(rows=50)
        fgt.api.log.disk.event.system.get(rows=50)
    """

    def __init__(self, client: "HTTPClient") -> None:
        """Initialize Disk log endpoint."""
        self._client = client
        
        # Log types with archive support
        self.ips = IPS(client, "disk")
        self.app_ctrl = AppCtrl(client, "disk")
        
        # Virus (special archive endpoint)
        self.virus = Virus(client, "disk")
        self.virus_archive = VirusArchive(client, "disk")
        
        # All other log types
        self.webfilter = Webfilter(client, "disk")
        self.waf = WAF(client, "disk")
        self.anomaly = Anomaly(client, "disk")
        self.emailfilter = EmailFilter(client, "disk")
        self.dlp = DLP(client, "disk")
        self.voip = VoIP(client, "disk")
        self.gtp = GTP(client, "disk")
        self.dns = DNS(client, "disk")
        self.ssh = SSH(client, "disk")
        self.ssl = SSL(client, "disk")
        self.cifs = CIFS(client, "disk")
        self.file_filter = FileFilter(client, "disk")
        
        # Traffic subtypes
        self.traffic = Traffic(client, "disk")
        
        # Event subtypes
        self.event = Event(client, "disk")


__all__ = ["Disk"]
