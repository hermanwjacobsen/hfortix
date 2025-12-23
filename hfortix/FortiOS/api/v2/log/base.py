"""
FortiOS LOG - Log Base

Log retrieval endpoint for log base logs.

API Endpoints:
    GET    /log/base

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.log.base.get()
    >>>
    >>> # With filters and parameters
    >>> data = fgt.api.log.base.get(
    ...     count=100,
    ...     start=0
    ... )

Note:
    This is a read-only endpoint. Only GET operations are supported.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional, Union

if TYPE_CHECKING:
    from collections.abc import Coroutine

    from hfortix.FortiOS.http_client_interface import IHTTPClient


class ArchiveResource:
    """
    Archiveresource Operations.

    Provides read-only access for FortiOS archiveresource data.

    Methods:
        get(, Coroutine): Retrieve monitoring/log data (read-only)

    Note:
        This is a read-only endpoint. Configuration changes are not supported.
    """

    def __init__(
        self, client: "IHTTPClient", log_type: str, storage: str
    ) -> None:
        self._client = client
        self._log_type = log_type
        self._storage = storage

    def get(
        self,
        mkey: Optional[int] = None,
        payload_dict: Optional[dict[str, Any]] = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Get archived packet capture items.

        Args:
            mkey: Archive identifier
            payload_dict: Dictionary containing all parameters (alternative to
            individual params)
            raw_json: Return raw JSON response
            **kwargs: Additional parameters

        Returns:
            List of archived packet captures or specific archive details

        Example:
            # Using individual parameters
            result = fgt.api.log.disk.ips.archive.get(mkey=123)

            # Using payload_dict
            result = fgt.api.log.disk.ips.archive.get(payload_dict={'mkey':
            123})
        """
        endpoint = f"{self._storage}/{self._log_type}/archive"

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


class ArchiveDownloadResource:
    """Archive download resource (IPS and App-Ctrl only)"""

    def __init__(
        self, client: "IHTTPClient", log_type: str, storage: str
    ) -> None:
        self._client = client
        self._log_type = log_type
        self._storage = storage

    def get(
        self,
        mkey: Optional[int] = None,
        payload_dict: Optional[dict[str, Any]] = None,
        **kwargs: Any,
    ) -> Union[bytes, Coroutine[Any, Any, bytes]]:
        """
        Download archived packet capture file.

        Args:
            mkey: Archive identifier
            payload_dict: Dictionary containing all parameters
            **kwargs: Additional parameters

        Returns:
            Binary content of the archived file

        Example:
            data = fgt.api.log.disk.ips.archive_download.get(mkey=123)
        """
        endpoint = f"{self._storage}/{self._log_type}/archive-download"

        if payload_dict:
            params = payload_dict.copy()
        else:
            params = {}
            if mkey is not None:
                params["mkey"] = mkey

        params.update(kwargs)
        return self._client.get_binary(
            "log", endpoint, params=params if params else None
        )


class RawResource:
    """Raw log resource - supports all log types"""

    def __init__(
        self, client: "IHTTPClient", log_type: str, storage: str
    ) -> None:
        self._client = client
        self._log_type = log_type
        self._storage = storage

    def get(
        self,
        rows: Optional[int] = None,
        session_id: Optional[int] = None,
        serial_no: Optional[str] = None,
        is_ha_member: Optional[Union[str, bool]] = None,
        filter: Optional[Union[str, list[str]]] = None,
        keep_session_alive: Optional[Union[str, bool]] = None,
        payload_dict: Optional[dict[str, Any]] = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[str, Any, Coroutine[Any, Any, Union[str, Any]]]:
        """
        Get raw log data (returns plain text).

        Args:
            rows: Number of rows to return
            session_id: Session ID to continue getting data for that request
            serial_no: Retrieve log from the specified device
            is_ha_member: Is the specified device an HA member
            filter: Filtering key/value pairs (supports operators: ==, !=, =@,
            !@, <=, <, >=, >)
            keep_session_alive: Keep the log session alive (must be manually
            aborted)
            payload_dict: Dictionary containing all parameters (alternative to
            individual params)
            raw_json: If True, return the raw httpx Response object instead of
            text
            **kwargs: Additional parameters

        Returns:
            Plain text log data (FortiOS log format) or raw Response if
            raw_json=True

        Example:
            # Using individual parameters
            logs = fgt.api.log.disk.virus.raw.get(rows=100,
            filter="srcip==192.168.1.1")

            # Using payload_dict
            logs = fgt.api.log.disk.virus.raw.get(payload_dict={'rows': 100,
            'filter': 'srcip==192.168.1.1'})

            # Get raw Response object
            response = fgt.api.log.disk.virus.raw.get(rows=10, raw_json=True)
            text = response.text
        """
        endpoint = f"{self._storage}/{self._log_type}/raw"

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
            if keep_session_alive is not None:
                params["keep_session_alive"] = keep_session_alive

        params.update(kwargs)

        # Raw endpoints return plain text, not JSON - use get_binary and decode
        binary_data = self._client.get_binary(
            "log", endpoint, params=params if params else None
        )

        # Check if async mode
        import inspect

        if inspect.iscoroutine(binary_data):

            async def _async():
                from typing import cast

                data = await cast(Coroutine[Any, Any, bytes], binary_data)
                if raw_json:
                    return {
                        "text": data.decode("utf-8"),
                        "content": data,
                    }
                else:
                    return data.decode("utf-8")

            return _async()

        # Sync mode - binary_data is bytes
        if raw_json:
            # If raw_json is requested, we need to return the response object
            # This is a limitation - we already got binary data
            # For now, return the text in a dict that mimics a response
            from typing import cast

            data = cast(bytes, binary_data)
            return {
                "text": data.decode("utf-8"),
                "content": data,
            }
        else:
            from typing import cast

            data = cast(bytes, binary_data)
            return data.decode("utf-8")


class LogResource:
    """Formatted log resource"""

    def __init__(
        self, client: "IHTTPClient", log_type: str, storage: str
    ) -> None:
        self._client = client
        self._log_type = log_type
        self._storage = storage

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
        Get formatted log data.

        Args:
            rows: Number of rows to return
            session_id: Session ID to continue getting data for that request
            serial_no: Retrieve log from the specified device
            is_ha_member: Is the specified device an HA member
            filter: Filtering key/value pairs (supports operators: ==, !=, =@,
            !@, <=, <, >=, >)
            extra: Extra data flags (e.g., 'reverse_lookup', 'country_id')
            payload_dict: Dictionary containing all parameters (alternative to
            individual params)
            raw_json: Return raw JSON response
            **kwargs: Additional parameters

        Returns:
            Formatted log data

        Example:
            # Using individual parameters
            logs = fgt.api.log.disk.virus.get(rows=50, extra='reverse_lookup')

            # Using payload_dict
            logs = fgt.api.log.disk.virus.get(payload_dict={'rows': 50,
            'extra': 'reverse_lookup'})
        """
        endpoint = f"{self._storage}/{self._log_type}"

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
        return self._client.get(
            "log",
            endpoint,
            params=params if params else None,
            raw_json=raw_json,
        )


__all__ = [
    "ArchiveResource",
    "ArchiveDownloadResource",
    "RawResource",
    "LogResource",
]
