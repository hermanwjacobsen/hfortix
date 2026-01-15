"""Type stubs for hfortix_fortios.api module."""

from __future__ import annotations

from hfortix_core.http.interface import IHTTPClient

from .utils import Utils
from .v2.cmdb import CMDB
from .v2.log import Log
from .v2.monitor import Monitor
from .v2.service import Service

__all__ = ["API", "CMDB", "Log", "Monitor", "Service"]


class API:
    """FortiOS REST API v2 Interface.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    cmdb: CMDB
    monitor: Monitor
    log: Log
    service: Service
    utils: Utils
    
    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None: ...
