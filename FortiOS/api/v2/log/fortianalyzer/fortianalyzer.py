"""
FortiOS Log API - FortiAnalyzer

Retrieve logs from FortiAnalyzer (when FortiGate is configured to send logs to FortiAnalyzer).

API Endpoints:
    GET /fortianalyzer/virus/archive                     - Get quarantined virus file metadata
    GET /fortianalyzer/{type}/archive                    - Get archived packet captures (ips, app-ctrl)
    GET /fortianalyzer/{type}/archive-download           - Download archived packet capture files
    GET /fortianalyzer/{type}/raw                        - Get raw log data (plain text format)
    GET /fortianalyzer/traffic/{subtype}/raw             - Get raw traffic logs
    GET /fortianalyzer/event/{subtype}/raw               - Get raw event logs
    GET /fortianalyzer/{type}                            - Get formatted log data (JSON)
    GET /fortianalyzer/traffic/{subtype}                 - Get formatted traffic logs (JSON)
    GET /fortianalyzer/event/{subtype}                   - Get formatted event logs (JSON)
"""
from typing import TYPE_CHECKING, Any, Optional, Union

if TYPE_CHECKING:
    from ....client import FortiOS


class FortiAnalyzer:
    """FortiAnalyzer log endpoint"""

    def __init__(self, client: 'FortiOS') -> None:
        """
        Initialize FortiAnalyzer log handler

        Args:
            client: FortiOS client instance
        """
        self._client = client

    def virus_archive(self, mkey: Optional[int] = None, **kwargs: Any) -> dict[str, Any]:
        """
        Get quarantined virus file metadata from FortiAnalyzer.

        Args:
            mkey (int, optional): The checksum from the virus log
            **kwargs: Additional parameters to pass to the API

        Returns:
            dict: API response with virus archive metadata

        Examples:
            >>> # Get virus archive metadata
            >>> result = fgt.log.fortianalyzer.virus_archive(mkey=12345)

            >>> # List all virus archives
            >>> result = fgt.log.fortianalyzer.virus_archive()
        """
        endpoint = 'fortianalyzer/virus/archive'

        params = {}
        if mkey is not None:
            params['mkey'] = mkey
        params.update(kwargs)

        return self._client.get('log', endpoint, params=params if params else None)

    def archive(self, log_type: str, mkey: Optional[int] = None, **kwargs: Any) -> dict[str, Any]:
        """
        Get archived packet captures for IPS or Application Control from FortiAnalyzer.

        Args:
            log_type (str): Type of archive - 'ips' or 'app-ctrl'
            mkey (int, optional): Archive identifier
            **kwargs: Additional parameters to pass to the API

        Returns:
            dict: API response with packet capture archive list

        Examples:
            >>> # Get all IPS packet capture archives
            >>> result = fgt.log.fortianalyzer.archive(log_type='ips')

            >>> # Get specific archive by ID
            >>> result = fgt.log.fortianalyzer.archive(log_type='app-ctrl', mkey=123)
        """
        endpoint = f'fortianalyzer/{log_type}/archive'

        params = {}
        if mkey is not None:
            params['mkey'] = mkey
        params.update(kwargs)

        return self._client.get('log', endpoint, params=params if params else None)

    def archive_download(self, log_type: str, mkey: Optional[int] = None, **kwargs: Any) -> dict[str, Any]:
        """
        Download an archived packet capture file from FortiAnalyzer.

        Args:
            log_type (str): Type of archive - 'ips' or 'app-ctrl'
            mkey (int, optional): Archive identifier
            **kwargs: Additional parameters to pass to the API

        Returns:
            bytes: Binary packet capture file data

        Examples:
            >>> # Download IPS packet capture archive
            >>> pcap_data = fgt.log.fortianalyzer.archive_download(log_type='ips', mkey=123)
            >>> with open('capture.pcap', 'wb') as f:
            ...     f.write(pcap_data)

            >>> # Download app-ctrl packet capture
            >>> pcap_data = fgt.log.fortianalyzer.archive_download(log_type='app-ctrl', mkey=456)
        """
        endpoint = f'fortianalyzer/{log_type}/archive-download'

        params = {}
        if mkey is not None:
            params['mkey'] = mkey
        params.update(kwargs)

        return self._client.get_binary('log', endpoint, params=params if params else None)

    def raw(
        self,
        log_type: str,
        rows: Optional[int] = None,
        session_id: Optional[int] = None,
        serial_no: Optional[str] = None,
        is_ha_member: Optional[bool] = None,
        filter: Optional[str] = None,
        keep_session_alive: Optional[bool] = None,
        **kwargs: Any
    ) -> dict[str, Any]:
        """
        Get raw log data from FortiAnalyzer in plain text format.

        Returns logs in FortiOS native log format (not JSON).

        Args:
            log_type (str): Type of log to retrieve
                Valid values: 'virus', 'webfilter', 'waf', 'ips', 'anomaly',
                'app-ctrl', 'emailfilter', 'dlp', 'voip', 'gtp', 'dns', 'ssh',
                'ssl', 'cifs', 'file-filter'
            rows (int, optional): Number of rows to return
            session_id (int, optional): Session ID to continue getting data
            serial_no (str, optional): Retrieve log from specified device
            is_ha_member (str, optional): Is the specified device an HA member
            filter (str or list, optional): Filter expression(s)
            keep_session_alive (str, optional): Keep log session alive for manual abort
            **kwargs: Additional parameters to pass to the API

        Returns:
            bytes: Raw log data in plain text format

        Examples:
            >>> # Get raw IPS logs
            >>> raw_logs = fgt.log.fortianalyzer.raw(log_type='ips', rows=100)

            >>> # Get raw webfilter logs with filter
            >>> raw_logs = fgt.log.fortianalyzer.raw(
            ...     log_type='webfilter',
            ...     rows=50,
            ...     filter='hostname==example.com'
            ... )
        """
        endpoint = f'fortianalyzer/{log_type}/raw'

        params = {}
        param_map = {
            'rows': rows,
            'session_id': session_id,
            'serial_no': serial_no,
            'is_ha_member': is_ha_member,
            'filter': filter,
            'keep_session_alive': keep_session_alive,
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
        is_ha_member: Optional[bool] = None,
        filter: Optional[str] = None,
        keep_session_alive: Optional[bool] = None,
        **kwargs: Any
    ) -> dict[str, Any]:
        """
        Get raw traffic logs from FortiAnalyzer in plain text format.

        Args:
            subtype (str): Traffic log subtype
                Valid values: 'forward', 'local', 'multicast', 'sniffer', 'fortiview', 'threat'
            rows (int, optional): Number of rows to return
            session_id (int, optional): Session ID to continue getting data
            serial_no (str, optional): Retrieve log from specified device
            is_ha_member (str, optional): Is the specified device an HA member
            filter (str or list, optional): Filter expression(s)
            keep_session_alive (str, optional): Keep log session alive
            **kwargs: Additional parameters to pass to the API

        Returns:
            bytes: Raw traffic logs in plain text format

        Examples:
            >>> # Get raw forward traffic logs
            >>> raw_logs = fgt.log.fortianalyzer.traffic_raw(subtype='forward', rows=100)

            >>> # Get raw local traffic with filter
            >>> raw_logs = fgt.log.fortianalyzer.traffic_raw(
            ...     subtype='local',
            ...     rows=50,
            ...     filter='srcip==192.168.1.100'
            ... )
        """
        endpoint = f'fortianalyzer/traffic/{subtype}/raw'

        params = {}
        param_map = {
            'rows': rows,
            'session_id': session_id,
            'serial_no': serial_no,
            'is_ha_member': is_ha_member,
            'filter': filter,
            'keep_session_alive': keep_session_alive,
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
        is_ha_member: Optional[bool] = None,
        filter: Optional[str] = None,
        keep_session_alive: Optional[bool] = None,
        **kwargs: Any
    ) -> dict[str, Any]:
        """
        Get raw event logs from FortiAnalyzer in plain text format.

        Args:
            subtype (str): Event log subtype
                Valid values: 'vpn', 'user', 'router', 'wireless', 'wad', 'endpoint',
                'ha', 'compliance-check', 'security-rating', 'fortiextender',
                'connector', 'system'
            rows (int, optional): Number of rows to return
            session_id (int, optional): Session ID to continue getting data
            serial_no (str, optional): Retrieve log from specified device
            is_ha_member (str, optional): Is the specified device an HA member
            filter (str or list, optional): Filter expression(s)
            keep_session_alive (str, optional): Keep log session alive
            **kwargs: Additional parameters to pass to the API

        Returns:
            bytes: Raw event logs in plain text format

        Examples:
            >>> # Get raw system event logs
            >>> raw_logs = fgt.log.fortianalyzer.event_raw(subtype='system', rows=100)

            >>> # Get raw VPN event logs with filter
            >>> raw_logs = fgt.log.fortianalyzer.event_raw(
            ...     subtype='vpn',
            ...     rows=50,
            ...     filter='user==vpnuser1'
            ... )
        """
        endpoint = f'fortianalyzer/event/{subtype}/raw'

        params = {}
        param_map = {
            'rows': rows,
            'session_id': session_id,
            'serial_no': serial_no,
            'is_ha_member': is_ha_member,
            'filter': filter,
            'keep_session_alive': keep_session_alive,
        }

        for key, value in param_map.items():
            if value is not None:
                params[key] = value
        params.update(kwargs)

        return self._client.get('log', endpoint, params=params if params else None)

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
        Get log data from FortiAnalyzer for the specified type (formatted, not raw).

        Retrieves formatted log entries with time range and filtering support.

        Args:
            log_type (str): Type of log to retrieve
                Valid values: 'virus', 'webfilter', 'waf', 'ips', 'anomaly',
                'app-ctrl', 'emailfilter', 'dlp', 'voip', 'gtp', 'dns', 'ssh',
                'ssl', 'cifs', 'file-filter'
            rows (int, optional): Number of rows to return
            start (int, optional): Start time (Unix timestamp)
            end (int, optional): End time (Unix timestamp)
            filter (str or list, optional): Filter expression(s)
            **kwargs: Additional parameters to pass to the API

        Returns:
            dict: API response containing formatted log entries

        Examples:
            >>> # Get IPS logs
            >>> result = fgt.log.fortianalyzer.get(log_type='ips', rows=100)

            >>> # Get webfilter logs with time range
            >>> import time
            >>> end_time = int(time.time())
            >>> start_time = end_time - 3600  # Last hour
            >>> result = fgt.log.fortianalyzer.get(
            ...     log_type='webfilter',
            ...     rows=50,
            ...     start=start_time,
            ...     end=end_time
            ... )

            >>> # Get app-ctrl logs with filter
            >>> result = fgt.log.fortianalyzer.get(
            ...     log_type='app-ctrl',
            ...     rows=100,
            ...     filter='app==Facebook'
            ... )
        """
        endpoint = f'fortianalyzer/{log_type}'

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
        Get formatted traffic logs from FortiAnalyzer (JSON format).

        Args:
            subtype (str): Traffic log subtype
                Valid values: 'forward', 'local', 'multicast', 'sniffer', 'fortiview', 'threat'
            rows (int, optional): Number of rows to return
            start (int, optional): Start time (Unix timestamp)
            end (int, optional): End time (Unix timestamp)
            filter (str or list, optional): Filter expression(s)
            **kwargs: Additional parameters to pass to the API

        Returns:
            dict: API response with formatted traffic logs

        Examples:
            >>> # Get forward traffic logs
            >>> result = fgt.log.fortianalyzer.traffic(subtype='forward', rows=100)

            >>> # Get forward traffic for specific source IP
            >>> result = fgt.log.fortianalyzer.traffic(
            ...     subtype='forward',
            ...     rows=50,
            ...     filter='srcip==192.168.1.100'
            ... )

            >>> # Get threat traffic logs with time range
            >>> import time
            >>> end_time = int(time.time())
            >>> start_time = end_time - 3600
            >>> result = fgt.log.fortianalyzer.traffic(
            ...     subtype='threat',
            ...     rows=100,
            ...     start=start_time,
            ...     end=end_time
            ... )
        """
        endpoint = f'fortianalyzer/traffic/{subtype}'

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
        Get formatted event logs from FortiAnalyzer (JSON format).

        Args:
            subtype (str): Event log subtype
                Valid values: 'vpn', 'user', 'router', 'wireless', 'wad', 'endpoint',
                'ha', 'compliance-check', 'security-rating', 'fortiextender',
                'connector', 'system'
            rows (int, optional): Number of rows to return
            start (int, optional): Start time (Unix timestamp)
            end (int, optional): End time (Unix timestamp)
            filter (str or list, optional): Filter expression(s)
            **kwargs: Additional parameters to pass to the API

        Returns:
            dict: API response with formatted event logs

        Examples:
            >>> # Get system event logs
            >>> result = fgt.log.fortianalyzer.event(subtype='system', rows=100)

            >>> # Get VPN event logs with filter
            >>> result = fgt.log.fortianalyzer.event(
            ...     subtype='vpn',
            ...     rows=50,
            ...     filter='user==vpnuser1'
            ... )

            >>> # Get user event logs with time range
            >>> import time
            >>> end_time = int(time.time())
            >>> start_time = end_time - 3600
            >>> result = fgt.log.fortianalyzer.event(
            ...     subtype='user',
            ...     rows=100,
            ...     start=start_time,
            ...     end=end_time
            ... )
        """
        endpoint = f'fortianalyzer/event/{subtype}'

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
