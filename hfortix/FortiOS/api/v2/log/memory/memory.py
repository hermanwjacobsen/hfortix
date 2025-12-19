"""
FortiOS LOG - Log Memory Memory

Log retrieval endpoint for log memory memory logs.

API Endpoints:
    GET    /log/memory/memory
    GET    /log/memory/memory
    GET    /log/memory/memory
    GET    /log/memory/memory
    GET    /log/memory/memory
    GET    /log/memory/memory
    GET    /log/memory/memory
    GET    /log/memory/memory
    GET    /log/memory/memory

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>> 
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.log.memory.memory.get()
    >>> 
    >>> # With filters and parameters
    >>> data = fgt.api.log.memory.memory.get(
    ...     count=100,
    ...     start=0
    ... )

Note:
    This is a read-only endpoint. Only GET operations are supported.
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
    Memory Operations.
    
    Provides read-only access for FortiOS memory data.

    Methods:
        get(): Retrieve monitoring/log data (read-only)
    
    Note:
        This is a read-only endpoint. Configuration changes are not supported.
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
