"""
FortiOS LOG - Log Traffic

Log retrieval endpoint for log traffic logs.

API Endpoints:
    GET    /log/traffic

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.log.traffic.get()
    >>>
    >>> # With filters and parameters
    >>> data = fgt.api.log.traffic.get(
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


# Traffic subtypes
class TrafficForward:
    """
    Trafficforward Operations.

    Provides read-only access for FortiOS trafficforward data.

    Methods:
        get(): Retrieve monitoring/log data (read-only)

    Note:
        This is a read-only endpoint. Configuration changes are not supported.
    """

    def __init__(self, client: "IHTTPClient", storage: str = "disk") -> None:
        self._client = client
        self.raw = RawResource(client, "traffic/forward", storage)
        self._resource = LogResource(client, "traffic/forward", storage)

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
        Get forward traffic logs.

        Supports dual approach:
        1. Individual parameters: get(rows=100, filter='srcip==192.168.1.1')
        2. Payload dict: get(payload_dict={'rows': 100, 'filter':
        'srcip==192.168.1.1'})

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


class TrafficLocal:
    """Local traffic - /disk/traffic/local"""

    def __init__(self, client: "IHTTPClient", storage: str = "disk") -> None:
        self._client = client
        self.raw = RawResource(client, "traffic/local", storage)
        self._resource = LogResource(client, "traffic/local", storage)

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
        Get local traffic logs.

        Supports dual approach:
        1. Individual parameters: get(rows=100, filter='srcip==192.168.1.1')
        2. Payload dict: get(payload_dict={'rows': 100, 'filter':
        'srcip==192.168.1.1'})

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


class TrafficMulticast:
    """Multicast traffic - /disk/traffic/multicast"""

    def __init__(self, client: "IHTTPClient", storage: str = "disk") -> None:
        self._client = client
        self.raw = RawResource(client, "traffic/multicast", storage)
        self._resource = LogResource(client, "traffic/multicast", storage)

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
        Get multicast traffic logs.

        Supports dual approach:
        1. Individual parameters: get(rows=100, filter='srcip==192.168.1.1')
        2. Payload dict: get(payload_dict={'rows': 100, 'filter':
        'srcip==192.168.1.1'})

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


class TrafficSniffer:
    """Sniffer traffic - /disk/traffic/sniffer"""

    def __init__(self, client: "IHTTPClient", storage: str = "disk") -> None:
        self._client = client
        self.raw = RawResource(client, "traffic/sniffer", storage)
        self._resource = LogResource(client, "traffic/sniffer", storage)

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
        Get sniffer traffic logs.

        Supports dual approach:
        1. Individual parameters: get(rows=100, filter='srcip==192.168.1.1')
        2. Payload dict: get(payload_dict={'rows': 100, 'filter':
        'srcip==192.168.1.1'})

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


class TrafficFortiview:
    """Fortiview traffic - /disk/traffic/fortiview"""

    def __init__(self, client: "IHTTPClient", storage: str = "disk") -> None:
        self._client = client
        self.raw = RawResource(client, "traffic/fortiview", storage)
        self._resource = LogResource(client, "traffic/fortiview", storage)

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
        Get fortiview traffic logs.

        Supports dual approach:
        1. Individual parameters: get(rows=100, filter='srcip==192.168.1.1')
        2. Payload dict: get(payload_dict={'rows': 100, 'filter':
        'srcip==192.168.1.1'})

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


class TrafficThreat:
    """Threat traffic - /disk/traffic/threat"""

    def __init__(self, client: "IHTTPClient", storage: str = "disk") -> None:
        self._client = client
        self.raw = RawResource(client, "traffic/threat", storage)
        self._resource = LogResource(client, "traffic/threat", storage)

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
        Get threat traffic logs.

        Supports dual approach:
        1. Individual parameters: get(rows=100, filter='srcip==192.168.1.1')
        2. Payload dict: get(payload_dict={'rows': 100, 'filter':
        'srcip==192.168.1.1'})

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


class Traffic:
    """Traffic container - /disk/traffic/{subtype}"""

    def __init__(self, client: "IHTTPClient", storage: str = "disk") -> None:
        self._client = client
        self.forward = TrafficForward(client, storage)
        self.local = TrafficLocal(client, storage)
        self.multicast = TrafficMulticast(client, storage)
        self.sniffer = TrafficSniffer(client, storage)
        self.fortiview = TrafficFortiview(client, storage)
        self.threat = TrafficThreat(client, storage)


__all__ = [
    "TrafficForward",
    "TrafficLocal",
    "TrafficMulticast",
    "TrafficSniffer",
    "TrafficFortiview",
    "TrafficThreat",
    "Traffic",
]
