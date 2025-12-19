"""
FortiOS Log - FortiCloud Storage

Main orchestrator for forticloud log API endpoints.

API Endpoints:
    GET /forticloud/virus/archive                - Get quarantined virus file metadata
    GET /forticloud/{type}/archive               - Get archived items (ips, app-ctrl only)
    GET /forticloud/{type}/archive-download      - Download archived file (ips, app-ctrl only)
    GET /forticloud/{type}/raw                   - Get raw log data (all types)
    GET /forticloud/traffic/{subtype}/raw        - Get raw traffic logs by subtype
    GET /forticloud/event/{subtype}/raw          - Get raw event logs by subtype
    GET /forticloud/{type}                       - Get formatted log data for type
    GET /forticloud/traffic/{subtype}            - Get formatted traffic logs by subtype
    GET /forticloud/event/{subtype}              - Get formatted event logs by subtype
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
    FortiCloud log endpoint
    
    Examples:
        # IPS archive
        fgt.api.log.forticloud.ips.archive.get()
        
        # IPS logs
        fgt.api.log.forticloud.ips.get(rows=100, filter='srcip==192.168.1.1')
        fgt.api.log.forticloud.ips.raw()
        
        # Virus archive
        fgt.api.log.forticloud.virus_archive.get(mkey='checksum123')
        
        # Traffic logs
        fgt.api.log.forticloud.traffic.forward.get(rows=50)
        fgt.api.log.forticloud.traffic.forward.raw()
        
        # Event logs  
        fgt.api.log.forticloud.event.system.get(rows=25)
        fgt.api.log.forticloud.event.system.raw()
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
