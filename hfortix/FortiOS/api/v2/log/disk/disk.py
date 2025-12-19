"""
FortiOS LOG - Log Disk Disk

Log retrieval endpoint for log disk disk logs.

API Endpoints:
    GET    /log/disk/disk
    GET    /log/disk/disk
    GET    /log/disk/disk
    GET    /log/disk/disk
    GET    /log/disk/disk
    GET    /log/disk/disk
    GET    /log/disk/disk
    GET    /log/disk/disk
    GET    /log/disk/disk

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>> 
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.log.disk.disk.get()
    >>> 
    >>> # With filters and parameters
    >>> data = fgt.api.log.disk.disk.get(
    ...     count=100,
    ...     start=0
    ... )

Note:
    This is a read-only endpoint. Only GET operations are supported.
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
    Disk Operations.
    
    Provides read-only access for FortiOS disk data.

    Methods:
        get(): Retrieve monitoring/log data (read-only)
    
    Note:
        This is a read-only endpoint. Configuration changes are not supported.
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
