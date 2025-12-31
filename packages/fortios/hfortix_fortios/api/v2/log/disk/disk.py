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
    >>> from hfortix_fortios import FortiOS
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


class Disk:
    """
    Disk Operations.

    Provides read-only access for FortiOS disk data.

    Methods:
        get(): Retrieve monitoring/log data (read-only)

    Note:
        This is a read-only endpoint. Configuration changes are not supported.
    """

    def __init__(self, client: "IHTTPClient") -> None:
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
