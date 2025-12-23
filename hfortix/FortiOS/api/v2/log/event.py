"""
FortiOS LOG - Log Event

Log retrieval endpoint for log event logs.

API Endpoints:
    GET    /log/event

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.log.event.get()
    >>>
    >>> # With filters and parameters
    >>> data = fgt.api.log.event.get(
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


# Event subtypes
class EventVPN:
    """
    Eventvpn Operations.

    Provides read-only access for FortiOS eventvpn data.

    Methods:
        get(): Retrieve monitoring/log data (read-only)

    Note:
        This is a read-only endpoint. Configuration changes are not supported.
    """

    def __init__(self, client: "IHTTPClient", storage: str = "disk") -> None:
        self._client = client
        self.raw = RawResource(client, "event/vpn", storage)
        self._resource = LogResource(client, "event/vpn", storage)

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
        Get VPN event logs.

        Supports dual approach:
        1. Individual parameters: get(rows=100, filter='user==admin')
        2. Payload dict: get(payload_dict={'rows': 100, 'filter':
        'user==admin'})

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


class EventUser:
    """User events - /disk/event/user"""

    def __init__(self, client: "IHTTPClient", storage: str = "disk") -> None:
        self._client = client
        self.raw = RawResource(client, "event/user", storage)
        self._resource = LogResource(client, "event/user", storage)

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
        Get user event logs.

        Supports dual approach:
        1. Individual parameters: get(rows=100, filter='user==admin')
        2. Payload dict: get(payload_dict={'rows': 100, 'filter':
        'user==admin'})

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


class EventRouter:
    """Router events - /disk/event/router"""

    def __init__(self, client: "IHTTPClient", storage: str = "disk") -> None:
        self._client = client
        self.raw = RawResource(client, "event/router", storage)
        self._resource = LogResource(client, "event/router", storage)

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
        Get router event logs.

        Supports dual approach:
        1. Individual parameters: get(rows=100, filter='msg=="route changed"')
        2. Payload dict: get(payload_dict={'rows': 100, 'filter': 'msg=="route
        changed"'})

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


class EventWireless:
    """Wireless events - /disk/event/wireless"""

    def __init__(self, client: "IHTTPClient", storage: str = "disk") -> None:
        self._client = client
        self.raw = RawResource(client, "event/wireless", storage)
        self._resource = LogResource(client, "event/wireless", storage)

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
        Get wireless event logs.

        Supports dual approach:
        1. Individual parameters: get(rows=100, filter='ssid=="Corporate"')
        2. Payload dict: get(payload_dict={'rows': 100, 'filter':
        'ssid=="Corporate"'})

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


class EventWAD:
    """WAD events - /disk/event/wad"""

    def __init__(self, client: "IHTTPClient", storage: str = "disk") -> None:
        self._client = client
        self.raw = RawResource(client, "event/wad", storage)
        self._resource = LogResource(client, "event/wad", storage)

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
        Get WAD event logs.

        Supports dual approach:
        1. Individual parameters: get(rows=100, filter='subtype=="auth"')
        2. Payload dict: get(payload_dict={'rows': 100, 'filter':
        'subtype=="auth"'})

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


class EventEndpoint:
    """Endpoint events - /disk/event/endpoint"""

    def __init__(self, client: "IHTTPClient", storage: str = "disk") -> None:
        self._client = client
        self.raw = RawResource(client, "event/endpoint", storage)
        self._resource = LogResource(client, "event/endpoint", storage)

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
        Get endpoint event logs.

        Supports dual approach:
        1. Individual parameters: get(rows=100, filter='hostname=="PC01"')
        2. Payload dict: get(payload_dict={'rows': 100, 'filter':
        'hostname=="PC01"'})

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


class EventHA:
    """HA events - /disk/event/ha"""

    def __init__(self, client: "IHTTPClient", storage: str = "disk") -> None:
        self._client = client
        self.raw = RawResource(client, "event/ha", storage)
        self._resource = LogResource(client, "event/ha", storage)

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
        Get HA event logs.

        Supports dual approach:
        1. Individual parameters: get(rows=100, filter='msg=="HA state
        changed"')
        2. Payload dict: get(payload_dict={'rows': 100, 'filter': 'msg=="HA
        state changed"'})

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


class EventComplianceCheck:
    """Compliance check events - /disk/event/compliance-check"""

    def __init__(self, client: "IHTTPClient", storage: str = "disk") -> None:
        self._client = client
        self.raw = RawResource(client, "event/compliance-check", storage)
        self._resource = LogResource(client, "event/compliance-check", storage)

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
        Get compliance check event logs.

        Supports dual approach:
        1. Individual parameters: get(rows=100, filter='result=="fail"')
        2. Payload dict: get(payload_dict={'rows': 100, 'filter':
        'result=="fail"'})

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


class EventSecurityRating:
    """Security rating events - /disk/event/security-rating"""

    def __init__(self, client: "IHTTPClient", storage: str = "disk") -> None:
        self._client = client
        self.raw = RawResource(client, "event/security-rating", storage)
        self._resource = LogResource(client, "event/security-rating", storage)

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
        Get security rating event logs.

        Supports dual approach:
        1. Individual parameters: get(rows=100, filter='rating<80')
        2. Payload dict: get(payload_dict={'rows': 100, 'filter': 'rating<80'})

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


class EventFortiextender:
    """Fortiextender events - /disk/event/fortiextender"""

    def __init__(self, client: "IHTTPClient", storage: str = "disk") -> None:
        self._client = client
        self.raw = RawResource(client, "event/fortiextender", storage)
        self._resource = LogResource(client, "event/fortiextender", storage)

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
        Get fortiextender event logs.

        Supports dual approach:
        1. Individual parameters: get(rows=100, filter='device=="FXT-001"')
        2. Payload dict: get(payload_dict={'rows': 100, 'filter':
        'device=="FXT-001"'})

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


class EventConnector:
    """Connector events - /disk/event/connector"""

    def __init__(self, client: "IHTTPClient", storage: str = "disk") -> None:
        self._client = client
        self.raw = RawResource(client, "event/connector", storage)
        self._resource = LogResource(client, "event/connector", storage)

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
        Get connector event logs.

        Supports dual approach:
        1. Individual parameters: get(rows=100, filter='status=="connected"')
        2. Payload dict: get(payload_dict={'rows': 100, 'filter':
        'status=="connected"'})

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


class EventSystem:
    """System events - /disk/event/system"""

    def __init__(self, client: "IHTTPClient", storage: str = "disk") -> None:
        self._client = client
        self.raw = RawResource(client, "event/system", storage)
        self._resource = LogResource(client, "event/system", storage)

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
        Get system event logs.

        Supports dual approach:
        1. Individual parameters: get(rows=100, filter='level=="alert"')
        2. Payload dict: get(payload_dict={'rows': 100, 'filter':
        'level=="alert"'})

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


class Event:
    """Event container - /disk/event/{subtype}"""

    def __init__(self, client: "IHTTPClient", storage: str = "disk") -> None:
        self._client = client
        self.vpn = EventVPN(client, storage)
        self.user = EventUser(client, storage)
        self.router = EventRouter(client, storage)
        self.wireless = EventWireless(client, storage)
        self.wad = EventWAD(client, storage)
        self.endpoint = EventEndpoint(client, storage)
        self.ha = EventHA(client, storage)
        self.compliance_check = EventComplianceCheck(client, storage)
        self.security_rating = EventSecurityRating(client, storage)
        self.fortiextender = EventFortiextender(client, storage)
        self.connector = EventConnector(client, storage)
        self.system = EventSystem(client, storage)


__all__ = [
    "EventVPN",
    "EventUser",
    "EventRouter",
    "EventWireless",
    "EventWAD",
    "EventEndpoint",
    "EventHA",
    "EventComplianceCheck",
    "EventSecurityRating",
    "EventFortiextender",
    "EventConnector",
    "EventSystem",
    "Event",
]
