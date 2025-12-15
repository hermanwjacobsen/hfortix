"""
FortiOS Memory Log API

This module provides methods to retrieve logs from memory storage.
"""
from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional, Union

if TYPE_CHECKING:
    from ....http_client import HTTPClient


class Memory:
    """
    Memory Log API for FortiOS.

    Provides methods to retrieve and manage logs stored in memory.
    """

    def __init__(self, client: 'HTTPClient') -> None:
        """Initialize Memory log API with FortiOS client."""
        self._client = client

    # Archive Operations

    def virus_archive(self, mkey: Optional[int] = None, **kwargs: Any) -> dict[str, Any]:
        """
        Return a description of the quarantined virus file.

        Args:
            mkey (str, optional): Checksum of the virus archive
            **kwargs: Additional parameters to pass

        Returns:
            dict: Virus archive metadata or list of all archives

        Example:
            >>> # List all virus archives
            >>> archives = fgt.log.memory.virus_archive()

            >>> # Get specific archive by checksum
            >>> archive = fgt.log.memory.virus_archive(mkey='abc123...')
        """
        endpoint = 'memory/virus/archive'
        if mkey is not None:
            endpoint += f'/{mkey}'
        return self._client.get('log', endpoint, params=kwargs if kwargs else None)

    def archive(self, log_type: str, mkey: Optional[int] = None, **kwargs: Any) -> dict[str, Any]:
        """
        Return a list of archived items for the desired type.

        Args:
            log_type (str): Type of archive ('app-ctrl', 'ips')
            mkey (str, optional): ID of specific archive entry
            **kwargs: Additional parameters to pass

        Returns:
            dict: Archive list or specific archive details

        Example:
            >>> # List all IPS archives
            >>> archives = fgt.log.memory.archive('ips')

            >>> # Get specific app-ctrl archive
            >>> archive = fgt.log.memory.archive('app-ctrl', mkey='12345')
        """
        endpoint = f'memory/{log_type}/archive'
        if mkey is not None:
            endpoint += f'/{mkey}'
        return self._client.get('log', endpoint, params=kwargs if kwargs else None)

    def archive_download(self, log_type: str, mkey: Optional[int] = None, **kwargs: Any) -> dict[str, Any]:
        """
        Download an archived file.

        Args:
            log_type (str): Type of archive ('virus', 'app-ctrl', 'ips')
            mkey (str, optional): ID of the archive to download
            **kwargs: Additional parameters to pass

        Returns:
            bytes: Binary file content

        Example:
            >>> # Download virus archive
            >>> file_data = fgt.log.memory.archive_download('virus', mkey='abc123...')
            >>> with open('virus.bin', 'wb') as f:
            ...     f.write(file_data)

            >>> # Download IPS archive
            >>> file_data = fgt.log.memory.archive_download('ips', mkey='12345')
        """
        endpoint = f'memory/{log_type}/archive-download'
        if mkey is not None:
            endpoint += f'/{mkey}'
        return self._client.get_binary('log', endpoint, params=kwargs if kwargs else None)

    # Raw Log Retrieval

    def raw(
        self,
        log_type: str,
        rows: Optional[int] = None,
        session_id: Optional[int] = None,
        serial_no: Optional[str] = None,
        start: Optional[int] = None,
        end: Optional[int] = None,
        **kwargs: Any
    ) -> dict[str, Any]:
        """
        Retrieve raw log data for the given log type.

        Args:
            log_type (str): Type of log to retrieve
                Valid values: 'virus', 'webfilter', 'waf', 'ips', 'anomaly',
                'app-ctrl', 'emailfilter', 'dlp', 'voip', 'gtp', 'dns', 'ssh',
                'ssl', 'cifs', 'file-filter'
            rows (int, optional): Number of rows to return
            session_id (int, optional): Session ID for log streaming
            serial_no (str, optional): Serial number of FortiGate
            start (int, optional): Start time (Unix timestamp)
            end (int, optional): End time (Unix timestamp)
            **kwargs: Additional parameters to pass

        Returns:
            dict: Raw log data

        Example:
            >>> # Get last 100 virus logs
            >>> logs = fgt.log.memory.raw('virus', rows=100)

            >>> # Get IPS logs with time range
            >>> import time
            >>> end_time = int(time.time())
            >>> start_time = end_time - 3600
            >>> logs = fgt.log.memory.raw(
            ...     log_type='ips',
            ...     rows=50,
            ...     start=start_time,
            ...     end=end_time
            ... )
        """
        endpoint = f'memory/{log_type}/raw'

        params = {}
        param_map = {
            'rows': rows,
            'session_id': session_id,
            'serial_no': serial_no,
            'start': start,
            'end': end,
        }

        for key, value in param_map.items():
            if value is not None:
                params[key] = value
        params.update(kwargs)

        return self._client.get('log', endpoint, params=params if params else None)

    def traffic_raw(
        self,
        subtype: str,
        rows: Optional[int] = None,
        session_id: Optional[int] = None,
        serial_no: Optional[str] = None,
        start: Optional[int] = None,
        end: Optional[int] = None,
        **kwargs: Any
    ) -> dict[str, Any]:
        """
        Retrieve raw traffic log data for the given subtype.

        Args:
            subtype (str): Traffic log subtype
                Valid values: 'forward', 'local', 'multicast', 'sniffer'
            rows (int, optional): Number of rows to return
            session_id (int, optional): Session ID for log streaming
            serial_no (str, optional): Serial number of FortiGate
            start (int, optional): Start time (Unix timestamp)
            end (int, optional): End time (Unix timestamp)
            **kwargs: Additional parameters to pass

        Returns:
            dict: Raw traffic log data

        Example:
            >>> # Get last 100 forward traffic logs
            >>> logs = fgt.log.memory.traffic_raw('forward', rows=100)

            >>> # Get sniffer logs with time range
            >>> import time
            >>> end_time = int(time.time())
            >>> start_time = end_time - 1800  # Last 30 minutes
            >>> logs = fgt.log.memory.traffic_raw(
            ...     subtype='sniffer',
            ...     rows=50,
            ...     start=start_time,
            ...     end=end_time
            ... )
        """
        endpoint = f'memory/traffic/{subtype}/raw'

        params = {}
        param_map = {
            'rows': rows,
            'session_id': session_id,
            'serial_no': serial_no,
            'start': start,
            'end': end,
        }

        for key, value in param_map.items():
            if value is not None:
                params[key] = value
        params.update(kwargs)

        return self._client.get('log', endpoint, params=params if params else None)

    def event_raw(
        self,
        subtype: str,
        rows: Optional[int] = None,
        session_id: Optional[int] = None,
        serial_no: Optional[str] = None,
        start: Optional[int] = None,
        end: Optional[int] = None,
        **kwargs: Any
    ) -> dict[str, Any]:
        """
        Retrieve raw event log data for the given subtype.

        Args:
            subtype (str): Event log subtype
                Valid values: 'vpn', 'user', 'router', 'wireless', 'wad', 'endpoint',
                'ha', 'compliance-check', 'security-rating', 'fortiextender',
                'connector', 'system'
            rows (int, optional): Number of rows to return
            session_id (int, optional): Session ID for log streaming
            serial_no (str, optional): Serial number of FortiGate
            start (int, optional): Start time (Unix timestamp)
            end (int, optional): End time (Unix timestamp)
            **kwargs: Additional parameters to pass

        Returns:
            dict: Raw event log data

        Example:
            >>> # Get last 50 system event logs
            >>> logs = fgt.log.memory.event_raw('system', rows=50)

            >>> # Get VPN logs with time range
            >>> import time
            >>> end_time = int(time.time())
            >>> start_time = end_time - 3600  # Last hour
            >>> logs = fgt.log.memory.event_raw(
            ...     subtype='vpn',
            ...     rows=100,
            ...     start=start_time,
            ...     end=end_time
            ... )
        """
        endpoint = f'memory/event/{subtype}/raw'

        params = {}
        param_map = {
            'rows': rows,
            'session_id': session_id,
            'serial_no': serial_no,
            'start': start,
            'end': end,
        }

        for key, value in param_map.items():
            if value is not None:
                params[key] = value
        params.update(kwargs)

        return self._client.get('log', endpoint, params=params if params else None)

    # Formatted Log Retrieval

    def get(
        self,
        log_type: str,
        rows: Optional[int] = None,
        start: Optional[int] = None,
        end: Optional[int] = None,
        filter: Optional[str] = None,
        vdom: str = 'root',
        **kwargs: Any
    ) -> dict[str, Any]:
        """
        Retrieve formatted log data for the given log type.

        Args:
            log_type (str): Type of log to retrieve
                Valid values: 'virus', 'webfilter', 'waf', 'ips', 'anomaly',
                'app-ctrl', 'emailfilter', 'dlp', 'voip', 'gtp', 'dns', 'ssh',
                'ssl', 'cifs', 'file-filter'
            rows (int, optional): Number of rows to return
            start (int, optional): Start time (Unix timestamp)
            end (int, optional): End time (Unix timestamp)
            filter (str, optional): Filter expression
            vdom (str, optional): Virtual domain name (default: 'root')
            **kwargs: Additional parameters to pass

        Returns:
            dict: Formatted log entries

        Example:
            >>> # Get virus logs
            >>> logs = fgt.log.memory.get('virus', rows=100)

            >>> # Get IPS logs with time range and filter
            >>> import time
            >>> end_time = int(time.time())
            >>> start_time = end_time - 3600
            >>> logs = fgt.log.memory.get(
            ...     log_type='ips',
            ...     rows=100,
            ...     start=start_time,
            ...     end=end_time,
            ...     filter='severity==critical'
            ... )

            >>> # Get app-ctrl logs with filter
            >>> result = fgt.log.memory.get(
            ...     log_type='app-ctrl',
            ...     rows=100,
            ...     filter='app==Facebook'
            ... )
        """
        endpoint = f'memory/{log_type}'

        params = {}
        param_map = {
            'rows': rows,
            'start': start,
            'end': end,
            'filter': filter,
        }

        for key, value in param_map.items():
            if value is not None:
                params[key] = value
        params.update(kwargs)

        return self._client.get('log', endpoint, params=params if params else None)

    def traffic(
        self,
        subtype: str,
        rows: Optional[int] = None,
        start: Optional[int] = None,
        end: Optional[int] = None,
        filter: Optional[str] = None,
        vdom: str = 'root',
        **kwargs: Any
    ) -> dict[str, Any]:
        """
        Get formatted traffic logs from memory (JSON format).

        Args:
            subtype (str): Traffic log subtype
                Valid values: 'forward', 'local', 'multicast', 'sniffer'
            rows (int, optional): Number of rows to return
            start (int, optional): Start time (Unix timestamp)
            end (int, optional): End time (Unix timestamp)
            filter (str, optional): Filter expression
            vdom (str, optional): Virtual domain name (default: 'root')
            **kwargs: Additional parameters to pass

        Returns:
            dict: Memory traffic log entries

        Example:
            >>> # Get forward traffic logs
            >>> logs = fgt.log.memory.traffic('forward', rows=100)

            >>> # Get local traffic logs with filter
            >>> logs = fgt.log.memory.traffic(
            ...     subtype='local',
            ...     rows=50,
            ...     filter='dstport==443'
            ... )

            >>> # Get threat traffic logs with time range
            >>> import time
            >>> end_time = int(time.time())
            >>> start_time = end_time - 3600
            >>> result = fgt.log.memory.traffic(
            ...     subtype='forward',
            ...     rows=100,
            ...     start=start_time,
            ...     end=end_time
            ... )
        """
        endpoint = f'memory/traffic/{subtype}'

        params = {}
        param_map = {
            'rows': rows,
            'start': start,
            'end': end,
            'filter': filter,
        }

        for key, value in param_map.items():
            if value is not None:
                params[key] = value
        params.update(kwargs)

        return self._client.get('log', endpoint, params=params if params else None)

    def event(
        self,
        subtype: str,
        rows: Optional[int] = None,
        start: Optional[int] = None,
        end: Optional[int] = None,
        filter: Optional[str] = None,
        vdom: str = 'root',
        **kwargs: Any
    ) -> dict[str, Any]:
        """
        Get formatted event logs from memory (JSON format).

        Args:
            subtype (str): Event log subtype
                Valid values: 'vpn', 'user', 'router', 'wireless', 'wad', 'endpoint',
                'ha', 'compliance-check', 'security-rating', 'fortiextender',
                'connector', 'system'
            rows (int, optional): Number of rows to return
            start (int, optional): Start time (Unix timestamp)
            end (int, optional): End time (Unix timestamp)
            filter (str, optional): Filter expression
            vdom (str, optional): Virtual domain name (default: 'root')
            **kwargs: Additional parameters to pass

        Returns:
            dict: Memory event log entries

        Example:
            >>> # Get system event logs
            >>> logs = fgt.log.memory.event('system', rows=100)

            >>> # Get VPN event logs with filter
            >>> logs = fgt.log.memory.event(
            ...     subtype='vpn',
            ...     rows=50,
            ...     filter='status==down'
            ... )

            >>> # Get user event logs with time range
            >>> import time
            >>> end_time = int(time.time())
            >>> start_time = end_time - 3600  # Last hour
            >>> result = fgt.log.memory.event(
            ...     subtype='user',
            ...     rows=100,
            ...     start=start_time,
            ...     end=end_time
            ... )
        """
        endpoint = f'memory/event/{subtype}'

        params = {}
        param_map = {
            'rows': rows,
            'start': start,
            'end': end,
            'filter': filter,
        }

        for key, value in param_map.items():
            if value is not None:
                params[key] = value
        params.update(kwargs)

        return self._client.get('log', endpoint, params=params if params else None, vdom=vdom)
