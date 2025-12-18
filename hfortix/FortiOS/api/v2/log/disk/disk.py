"""
FortiOS Log - Disk Storage

Provides access to log data stored on disk, including archived items and raw log retrieval.

API Endpoints:
    GET /disk/virus/archive                      - Get quarantined virus file metadata
    GET /disk/{type}/archive                     - Get archived items (ips, app-ctrl)
    GET /disk/{type}/archive-download            - Download archived file
    GET /disk/{type}/raw                         - Get raw log data (virus, webfilter, waf, ips, etc.)
    GET /disk/traffic/{subtype}/raw              - Get raw traffic logs by subtype
    GET /disk/event/{subtype}/raw                - Get raw event logs by subtype
    GET /disk/{type}                             - Get log data for type
    GET /disk/traffic/{subtype}                  - Get traffic logs by subtype
    GET /disk/event/{subtype}                    - Get event logs by subtype
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional

if TYPE_CHECKING:
    from ....http_client import HTTPClient


# Archive resources
class ArchiveResource:
    """Base archive resource"""

    def __init__(self, client: "HTTPClient", log_type: str, storage: str) -> None:
        self._client = client
        self._log_type = log_type
        self._storage = storage

    def get(self, mkey: Optional[int] = None, raw_json: bool = False, **kwargs: Any) -> dict[str, Any]:
        """Get archived items."""
        endpoint = f"{self._storage}/{self._log_type}/archive"
        params = {}
        if mkey is not None:
            params["mkey"] = mkey
        params.update(kwargs)
        return self._client.get("log", endpoint, params=params if params else None, raw_json=raw_json)


class ArchiveDownloadResource:
    """Base archive download resource"""

    def __init__(self, client: "HTTPClient", log_type: str, storage: str) -> None:
        self._client = client
        self._log_type = log_type
        self._storage = storage

    def get(self, mkey: Optional[int] = None, **kwargs: Any) -> bytes:
        """Download archived file."""
        endpoint = f"{self._storage}/{self._log_type}/archive-download"
        params = {}
        if mkey is not None:
            params["mkey"] = mkey
        params.update(kwargs)
        return self._client.get_binary("log", endpoint, params=params if params else None)


# Raw log resources
class RawResource:
    """Base raw log resource"""

    def __init__(self, client: "HTTPClient", log_type: str, storage: str) -> None:
        self._client = client
        self._log_type = log_type
        self._storage = storage

    def get(self, rows: Optional[int] = None, session_id: Optional[int] = None,
            serial_no: Optional[str] = None, is_ha_member: Optional[bool] = None,
            filter: Optional[str] = None, keep_session_alive: Optional[bool] = None,
            raw_json: bool = False, **kwargs: Any) -> dict[str, Any]:
        """Get raw logs."""
        endpoint = f"{self._storage}/{self._log_type}/raw"
        params = {}
        if rows is not None:
            params["rows"] = rows
        if session_id is not None:
            params["session_id"] = session_id
        if serial_no is not None:
            params["serial_no"] = serial_no
        if is_ha_member is not None:
            params["is_ha_member"] = is_ha_member
        if filter is not None:
            params["filter"] = filter
        if keep_session_alive is not None:
            params["keep_session_alive"] = keep_session_alive
        params.update(kwargs)
        return self._client.get("log", endpoint, params=params if params else None, raw_json=raw_json)


# Formatted log resources
class LogResource:
    """Base formatted log resource"""

    def __init__(self, client: "HTTPClient", log_type: str, storage: str) -> None:
        self._client = client
        self._log_type = log_type
        self._storage = storage

    def get(self, rows: Optional[int] = None, start: Optional[int] = None, end: Optional[int] = None,
            filter: Optional[str] = None, raw_json: bool = False, **kwargs: Any) -> dict[str, Any]:
        """Get formatted logs."""
        endpoint = f"{self._storage}/{self._log_type}"
        params = {}
        if rows is not None:
            params["rows"] = rows
        if start is not None:
            params["start"] = start
        if end is not None:
            params["end"] = end
        if filter is not None:
            params["filter"] = filter
        params.update(kwargs)
        return self._client.get("log", endpoint, params=params if params else None, raw_json=raw_json)


# Log type containers
class IPS:
    """IPS log type - /disk/ips"""

    def __init__(self, client: "HTTPClient", storage: str = "disk") -> None:
        self._client = client
        self.archive = ArchiveResource(client, "ips", storage)
        self.archive_download = ArchiveDownloadResource(client, "ips", storage)
        self.raw = RawResource(client, "ips", storage)
        self._resource = LogResource(client, "ips", storage)

    def get(self, **kwargs: Any) -> dict[str, Any]:
        """Get IPS logs."""
        return self._resource.get(**kwargs)


class AppCtrl:
    """App Control log type - /disk/app-ctrl"""

    def __init__(self, client: "HTTPClient", storage: str = "disk") -> None:
        self._client = client
        self.archive = ArchiveResource(client, "app-ctrl", storage)
        self.archive_download = ArchiveDownloadResource(client, "app-ctrl", storage)
        self.raw = RawResource(client, "app-ctrl", storage)
        self._resource = LogResource(client, "app-ctrl", storage)

    def get(self, **kwargs: Any) -> dict[str, Any]:
        """Get App Control logs."""
        return self._resource.get(**kwargs)


class Virus:
    """Virus log type - /disk/virus"""

    def __init__(self, client: "HTTPClient", storage: str = "disk") -> None:
        self._client = client
        self.raw = RawResource(client, "virus", storage)
        self._resource = LogResource(client, "virus", storage)

    def get(self, **kwargs: Any) -> dict[str, Any]:
        """Get virus logs."""
        return self._resource.get(**kwargs)


class VirusArchive:
    """Special virus archive endpoint - /disk/virus/archive"""

    def __init__(self, client: "HTTPClient", storage: str = "disk") -> None:
        self._client = client
        self._storage = storage

    def get(self, mkey: Optional[int] = None, raw_json: bool = False, **kwargs: Any) -> dict[str, Any]:
        """Get quarantined virus file metadata."""
        endpoint = f"{self._storage}/virus/archive"
        params = {}
        if mkey is not None:
            params["mkey"] = mkey
        params.update(kwargs)
        return self._client.get("log", endpoint, params=params if params else None, raw_json=raw_json)


# Traffic subtypes
class TrafficForward:
    """Forward traffic - /disk/traffic/forward"""

    def __init__(self, client: "HTTPClient", storage: str = "disk") -> None:
        self._client = client
        self.raw = RawResource(client, "traffic/forward", storage)
        self._resource = LogResource(client, "traffic/forward", storage)

    def get(self, **kwargs: Any) -> dict[str, Any]:
        """Get forward traffic logs."""
        return self._resource.get(**kwargs)


class Traffic:
    """Traffic container - /disk/traffic/{subtype}"""

    def __init__(self, client: "HTTPClient", storage: str = "disk") -> None:
        self._client = client
        self.forward = TrafficForward(client, storage)


# Event subtypes
class EventSystem:
    """System events - /disk/event/system"""

    def __init__(self, client: "HTTPClient", storage: str = "disk") -> None:
        self._client = client
        self.raw = RawResource(client, "event/system", storage)
        self._resource = LogResource(client, "event/system", storage)

    def get(self, **kwargs: Any) -> dict[str, Any]:
        """Get system event logs."""
        return self._resource.get(**kwargs)


class Event:
    """Event container - /disk/event/{subtype}"""

    def __init__(self, client: "HTTPClient", storage: str = "disk") -> None:
        self._client = client
        self.system = EventSystem(client, storage)


class Disk:
    """
    Disk log endpoint
    
    Examples:
        # IPS archive
        fgt.log.disk.ips.archive.get()
        fgt.log.disk.ips.archive.get(mkey=123)
        
        # IPS logs
        fgt.log.disk.ips.get(rows=100)
        fgt.log.disk.ips.raw.get(rows=100)
        
        # App Control
        fgt.log.disk.app_ctrl.archive.get()
        fgt.log.disk.app_ctrl.get(rows=50)
        
        # Virus
        fgt.log.disk.virus_archive.get()
        fgt.log.disk.virus.get(rows=100)
        
        # Traffic
        fgt.log.disk.traffic.forward.get(rows=100)
        fgt.log.disk.traffic.forward.raw.get(rows=100)
        
        # Events
        fgt.log.disk.event.system.get(rows=50)
        fgt.log.disk.event.system.raw.get(rows=50)
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
        
        # Traffic subtypes
        self.traffic = Traffic(client, "disk")
        
        # Event subtypes
        self.event = Event(client, "disk")

