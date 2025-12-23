"""
FortiOS LOG - Log Virus

Log retrieval endpoint for log virus logs.

API Endpoints:
    GET    /log/virus

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.log.virus.get()
    >>>
    >>> # With filters and parameters
    >>> data = fgt.api.log.virus.get(
    ...     count=100,
    ...     start=0
    ... )

Note:
    This is a read-only endpoint. Only GET operations are supported.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional, Union

from .base import LogResource, RawResource

if TYPE_CHECKING:
    from collections.abc import Coroutine

    from hfortix.FortiOS.http_client_interface import IHTTPClient


class Virus:
    """
    Virus Operations.

    Provides read-only access for FortiOS virus data.

    Methods:
        get(): Retrieve monitoring/log data (read-only)

    Note:
        This is a read-only endpoint. Configuration changes are not supported.
    """

    def __init__(self, client: "IHTTPClient", storage: str = "disk") -> None:
        self._client = client
        self._storage = storage
        self.raw = RawResource(client, "virus", storage)
        self._resource = LogResource(client, "virus", storage)

    def get(
        self,
        rows: Optional[int] = None,
        session_id: Optional[int] = None,
        serial_no: Optional[str] = None,
        is_ha_member: Optional[Union[str, bool]] = None,
        filter: Optional[Union[str, list[str]]] = None,
        extra: Optional[str] = None,
        payload_dict: Optional[dict[str, Any]] = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Get virus logs (formatted).

        Supports dual approach:
        1. Individual parameters: get(rows=100, filter='virus=="Trojan"')
        2. Payload dict: get(payload_dict={'rows': 100, 'filter':
        'virus=="Trojan"'})

        Args:
            rows: Maximum number of log entries to return
            session_id: Session ID for pagination
            serial_no: FortiGate serial number (for HA members)
            is_ha_member: Whether this is an HA member query
            filter: Log filter expression (string or list)
            extra: Additional options (e.g., 'reverse_lookup')
            payload_dict: Alternative to individual parameters - pass all
            params as dict
            raw_json: Return raw JSON response without parsing
            **kwargs: Additional parameters to pass to the API

        Returns:
            Dictionary containing log entries and metadata
        """
        if payload_dict:
            params = payload_dict.copy()
        else:
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
            if extra is not None:
                params["extra"] = extra

        params.update(kwargs)
        return self._resource.get(
            rows=params.get("rows"),
            session_id=params.get("session_id"),
            serial_no=params.get("serial_no"),
            is_ha_member=params.get("is_ha_member"),
            filter=params.get("filter"),
            extra=params.get("extra"),
            raw_json=raw_json,
            **{
                k: v
                for k, v in params.items()
                if k
                not in [
                    "rows",
                    "session_id",
                    "serial_no",
                    "is_ha_member",
                    "filter",
                    "extra",
                ]
            },
        )


class VirusArchive:
    """Special virus archive endpoint - /disk/virus/archive

    Returns metadata about quarantined virus files
    """

    def __init__(self, client: "IHTTPClient", storage: str = "disk") -> None:
        self._client = client
        self._storage = storage

    def get(
        self,
        mkey: Optional[int] = None,
        payload_dict: Optional[dict[str, Any]] = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Get quarantined virus file metadata.

        Args:
            mkey: The checksum column from the virus log
            payload_dict: Dictionary containing all parameters
            raw_json: Return raw JSON response
            **kwargs: Additional parameters

        Returns:
            Virus quarantine archive metadata including:
            - status: Quarantine status
            - checksum: File checksum
            - filename: Initial name of the file
            - timestamp: Time when the file was scanned
            - service: Service which requested the quarantine
            - duplicates: Number of duplicate file submissions
            - ttl: Time until this quarantine entry expires

        Example:
            # Get all quarantined viruses
            result = fgt.api.log.disk.virus_archive.get()

            # Get specific virus by checksum
            result = fgt.api.log.disk.virus_archive.get(mkey=12345678)

            # Using payload_dict
            result = fgt.api.log.disk.virus_archive.get(payload_dict={'mkey':
            12345678})
        """
        endpoint = f"{self._storage}/virus/archive"

        if payload_dict:
            params = payload_dict.copy()
        else:
            params = {}
            if mkey is not None:
                params["mkey"] = mkey

        params.update(kwargs)
        return self._client.get(
            "log",
            endpoint,
            params=params if params else None,
            raw_json=raw_json,
        )


__all__ = ["Virus", "VirusArchive"]
