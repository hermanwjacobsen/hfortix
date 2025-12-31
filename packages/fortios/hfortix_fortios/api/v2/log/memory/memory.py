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
    >>> from hfortix_fortios import FortiOS
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


class Memory:
    """
    Memory Operations.

    Provides read-only access for FortiOS memory data.

    Methods:
        get(): Retrieve monitoring/log data (read-only)

    Note:
        This is a read-only endpoint. Configuration changes are not supported.
    """

    def __init__(self, client: "IHTTPClient") -> None:
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
