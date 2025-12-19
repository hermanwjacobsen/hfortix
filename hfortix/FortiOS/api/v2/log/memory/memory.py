"""
FortiOS Log - Memory Storage

Main orchestrator for memory log API endpoints.

API Endpoints:
    GET /memory/virus/archive                    - Get quarantined virus file metadata
    GET /memory/{type}/archive                   - Get archived items (ips, app-ctrl only)
    GET /memory/{type}/archive-download          - Download archived file (ips, app-ctrl only)
    GET /memory/{type}/raw                       - Get raw log data (all types)
    GET /memory/traffic/{subtype}/raw            - Get raw traffic logs by subtype
    GET /memory/event/{subtype}/raw              - Get raw event logs by subtype
    GET /memory/{type}                           - Get formatted log data for type
    GET /memory/traffic/{subtype}                - Get formatted traffic logs by subtype
    GET /memory/event/{subtype}                  - Get formatted event logs by subtype
"""

from __future__ import annotations

from typing import TYPE_CHECKING

# Import all the shared log types - they work for Memory too!
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


class Memory:
    """
    Memory log endpoint
    
    Examples:
        # IPS archive
        fgt.api.log.memory.ips.archive.get()
        
        # IPS logs
        fgt.api.log.memory.ips.get(rows=100, filter='srcip==192.168.1.1')
        fgt.api.log.memory.ips.raw()
        
        # Virus archive
        fgt.api.log.memory.virus_archive.get(mkey='checksum123')
        
        # Traffic logs
        fgt.api.log.memory.traffic.forward.get(rows=50)
        fgt.api.log.memory.traffic.forward.raw()
        
        # Event logs  
        fgt.api.log.memory.event.system.get(rows=25)
        fgt.api.log.memory.event.system.raw()
    """

    def __init__(self, client: "HTTPClient") -> None:
        """
        Initialize Memory log endpoint
        
        Args:
            client: HTTP client for API requests
        """
        # Individual log types
        self.virus = Virus(client, "memory")
        self.webfilter = Webfilter(client, "memory")
        self.waf = WAF(client, "memory")
        self.ips = IPS(client, "memory")
        self.anomaly = Anomaly(client, "memory")
        self.app_ctrl = AppCtrl(client, "memory")
        self.emailfilter = EmailFilter(client, "memory")
        self.dlp = DLP(client, "memory")
        self.voip = VoIP(client, "memory")
        self.gtp = GTP(client, "memory")
        self.dns = DNS(client, "memory")
        self.ssh = SSH(client, "memory")
        self.ssl = SSL(client, "memory")
        self.cifs = CIFS(client, "memory")
        self.file_filter = FileFilter(client, "memory")

        # Virus archive (special case)
        self.virus_archive = VirusArchive(client, "memory")

        # Traffic subtypes
        self.traffic = Traffic(client, "memory")

        # Event subtypes
        self.event = Event(client, "memory")

    def __repr__(self) -> str:
        return "<Memory Log API>"
