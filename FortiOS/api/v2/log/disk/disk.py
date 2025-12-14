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
from typing import TYPE_CHECKING, Any, Optional

if TYPE_CHECKING:
    from ....client import FortiOS


class Disk:
    """Disk log endpoint"""

    def __init__(self, client: 'FortiOS') -> None:
        """
        Initialize Disk log endpoint.

        Args:
            client: FortiOS client instance
        """
        self._client = client

    def virus_archive(self, mkey: Optional[int] = None, **kwargs: Any) -> dict[str, Any]:
        """
        Get quarantined virus file metadata.

        Returns metadata describing quarantined virus files including status,
        checksum, filename, timestamp, and time to live.

        Args:
            mkey (int, optional): Checksum column from the virus log
            **kwargs: Additional parameters to pass to the API

        Returns:
            dict: API response containing:
                - status: Quarantine status (Infected, Machine Learning, Intercepted)
                - status_description: Description of the archived virus
                - checksum: File checksum
                - filename: Original file name
                - timestamp: Scan time (milliseconds since Unix Epoch)
                - service: Service that requested quarantine
                - duplicates: Number of duplicate submissions
                - ttl: Time to live or "FOREVER"

        Examples:
            # Get all quarantined virus metadata
            result = fgt.log.disk.virus_archive()

            # Get specific virus by checksum
            result = fgt.log.disk.virus_archive(mkey=12345)
        """
        endpoint = 'disk/virus/archive'
        params = {}

        if mkey is not None:
            params['mkey'] = mkey

        params.update(kwargs)

        return self._client.get('log', endpoint, params=params if params else None)

    def archive(self, log_type: str, mkey: Optional[int] = None, **kwargs: Any) -> dict[str, Any]:
        """
        Get archived items (packet captures from IPS or Application Control).

        Returns a list of archived packet capture details including source/destination
        IP addresses, ports, protocol, and packet data.

        Args:
            log_type (str): Type of log archive
                Valid values: 'ips', 'app-ctrl'
            mkey (int, optional): Archive identifier
            **kwargs: Additional parameters to pass to the API

        Returns:
            dict: API response containing array of:
                - src: Source IP address
                - dst: Destination IP address
                - proto: Protocol (tcp, udp, icmp, etc.)
                - src_port: Source port
                - dst_port: Destination port
                - len: Size in bytes of captured data
                - data: Array of bytes representing packet content

        Examples:
            # Get all IPS archives
            result = fgt.log.disk.archive(log_type='ips')

            # Get specific app-ctrl archive
            result = fgt.log.disk.archive(log_type='app-ctrl', mkey=123)
        """
        endpoint = f'disk/{log_type}/archive'
        params = {}

        if mkey is not None:
            params['mkey'] = mkey

        params.update(kwargs)

        return self._client.get('log', endpoint, params=params if params else None)

    def archive_download(self, log_type: str, mkey: Optional[int] = None, **kwargs: Any) -> dict[str, Any]:
        """
        Download an archived file (binary data).

        Downloads archived packet capture files. Returns binary data, not JSON.

        Args:
            log_type (str): Type of log archive
                Valid values: 'ips', 'app-ctrl'
            mkey (int, optional): Archive identifier
            **kwargs: Additional parameters to pass to the API

        Returns:
            bytes: Raw binary data of the archived file

        Examples:
            # Download IPS archive
            pcap_data = fgt.log.disk.archive_download(log_type='ips', mkey=123)

            # Save to file
            with open('capture.pcap', 'wb') as f:
                f.write(pcap_data)
        """
        endpoint = f'disk/{log_type}/archive-download'
        params = {}

        if mkey is not None:
            params['mkey'] = mkey

        params.update(kwargs)

        # This returns binary data, similar to sniffer download
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
        Get raw log data for the specified log type.

        Retrieves raw log entries with filtering and pagination support.

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
                Operators: ==, !=, =@, !@, <=, <, >=, >
                Logical OR: comma (,)
                Logical AND: ampersand (&)
            keep_session_alive (str, optional): Keep log session alive
            **kwargs: Additional parameters to pass to the API

        Returns:
            dict: API response containing raw log entries

        Examples:
            # Get virus logs
            result = fgt.log.disk.raw(log_type='virus', rows=100)

            # Get IPS logs with filter
            result = fgt.log.disk.raw(
                log_type='ips',
                rows=50,
                filter='severity>=high'
            )

            # Continue session
            result = fgt.log.disk.raw(
                log_type='webfilter',
                session_id=12345,
                keep_session_alive='true'
            )
        """
        endpoint = f'disk/{log_type}/raw'
        params = {}

        if rows is not None:
            params['rows'] = rows
        if session_id is not None:
            params['session_id'] = session_id
        if serial_no is not None:
            params['serial_no'] = serial_no
        if is_ha_member is not None:
            params['is_ha_member'] = is_ha_member
        if filter is not None:
            params['filter'] = filter
        if keep_session_alive is not None:
            params['keep_session_alive'] = keep_session_alive

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
        Get raw traffic logs by subtype.

        Retrieves raw traffic log entries for specific subtypes (forward, local, etc.).

        Args:
            subtype (str): Traffic log subtype
                Valid values: 'forward', 'local', 'multicast', 'sniffer'
            rows (int, optional): Number of rows to return
            session_id (int, optional): Session ID to continue getting data
            serial_no (str, optional): Retrieve log from specified device
            is_ha_member (str, optional): Is the specified device an HA member
            filter (str or list, optional): Filter expression(s)
            keep_session_alive (str, optional): Keep log session alive
            **kwargs: Additional parameters to pass to the API

        Returns:
            dict: API response containing raw traffic log entries

        Examples:
            # Get forward traffic logs
            result = fgt.log.disk.traffic_raw(subtype='forward', rows=100)

            # Get local traffic with filter
            result = fgt.log.disk.traffic_raw(
                subtype='local',
                rows=50,
                filter='srcip==192.168.1.100'
            )
        """
        endpoint = f'disk/traffic/{subtype}/raw'
        params = {}

        if rows is not None:
            params['rows'] = rows
        if session_id is not None:
            params['session_id'] = session_id
        if serial_no is not None:
            params['serial_no'] = serial_no
        if is_ha_member is not None:
            params['is_ha_member'] = is_ha_member
        if filter is not None:
            params['filter'] = filter
        if keep_session_alive is not None:
            params['keep_session_alive'] = keep_session_alive

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
        Get raw event logs by subtype.

        Retrieves raw event log entries for specific subtypes (system, user, etc.).

        Args:
            subtype (str): Event log subtype
                Valid values: 'system', 'user', 'router', 'wireless',
                'wad', 'endpoint', 'ha', 'security-rating', 'fortiextender'
            rows (int, optional): Number of rows to return
            session_id (int, optional): Session ID to continue getting data
            serial_no (str, optional): Retrieve log from specified device
            is_ha_member (str, optional): Is the specified device an HA member
            filter (str or list, optional): Filter expression(s)
            keep_session_alive (str, optional): Keep log session alive
            **kwargs: Additional parameters to pass to the API

        Returns:
            dict: API response containing raw event log entries

        Examples:
            # Get system event logs
            result = fgt.log.disk.event_raw(subtype='system', rows=100)

            # Get user events with filter
            result = fgt.log.disk.event_raw(
                subtype='user',
                rows=50,
                filter='action==login'
            )
        """
        endpoint = f'disk/event/{subtype}/raw'
        params = {}

        if rows is not None:
            params['rows'] = rows
        if session_id is not None:
            params['session_id'] = session_id
        if serial_no is not None:
            params['serial_no'] = serial_no
        if is_ha_member is not None:
            params['is_ha_member'] = is_ha_member
        if filter is not None:
            params['filter'] = filter
        if keep_session_alive is not None:
            params['keep_session_alive'] = keep_session_alive

        params.update(kwargs)

        return self._client.get('log', endpoint, params=params if params else None)

    def get(
        self,
        log_type: str,
        rows: Optional[int] = None,
        start: Optional[int] = None,
        end: Optional[int] = None,
        filter: Optional[str] = None,
        **kwargs: Any
    ) -> dict[str, Any]:
        """
        Get log data for the specified type (formatted, not raw).

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
            # Get virus logs
            result = fgt.log.disk.get(log_type='virus', rows=100)

            # Get IPS logs with time range
            import time
            end_time = int(time.time())
            start_time = end_time - 3600  # Last hour
            result = fgt.log.disk.get(
                log_type='ips',
                start=start_time,
                end=end_time,
                rows=50
            )
        """
        endpoint = f'disk/{log_type}'
        params = {}

        if rows is not None:
            params['rows'] = rows
        if start is not None:
            params['start'] = start
        if end is not None:
            params['end'] = end
        if filter is not None:
            params['filter'] = filter

        params.update(kwargs)

        return self._client.get('log', endpoint, params=params if params else None)

    def traffic(
        self,
        subtype: str,
        rows: Optional[int] = None,
        start: Optional[int] = None,
        end: Optional[int] = None,
        filter: Optional[str] = None,
        **kwargs: Any
    ) -> dict[str, Any]:
        """
        Get traffic logs by subtype (formatted, not raw).

        Retrieves formatted traffic log entries with time range and filtering support.

        Args:
            subtype (str): Traffic log subtype
                Valid values: 'forward', 'local', 'multicast', 'sniffer'
            rows (int, optional): Number of rows to return
            start (int, optional): Start time (Unix timestamp)
            end (int, optional): End time (Unix timestamp)
            filter (str or list, optional): Filter expression(s)
            **kwargs: Additional parameters to pass to the API

        Returns:
            dict: API response containing formatted traffic log entries

        Examples:
            # Get forward traffic logs
            result = fgt.log.disk.traffic(subtype='forward', rows=100)

            # Get local traffic with time range
            import time
            end_time = int(time.time())
            start_time = end_time - 1800  # Last 30 minutes
            result = fgt.log.disk.traffic(
                subtype='local',
                start=start_time,
                end=end_time
            )
        """
        endpoint = f'disk/traffic/{subtype}'
        params = {}

        if rows is not None:
            params['rows'] = rows
        if start is not None:
            params['start'] = start
        if end is not None:
            params['end'] = end
        if filter is not None:
            params['filter'] = filter

        params.update(kwargs)

        return self._client.get('log', endpoint, params=params if params else None)

    def event(
        self,
        subtype: str,
        rows: Optional[int] = None,
        start: Optional[int] = None,
        end: Optional[int] = None,
        filter: Optional[str] = None,
        **kwargs: Any
    ) -> dict[str, Any]:
        """
        Get event logs by subtype (formatted, not raw).

        Retrieves formatted event log entries with time range and filtering support.

        Args:
            subtype (str): Event log subtype
                Valid values: 'system', 'user', 'router', 'wireless',
                'wad', 'endpoint', 'ha', 'security-rating', 'fortiextender'
            rows (int, optional): Number of rows to return
            start (int, optional): Start time (Unix timestamp)
            end (int, optional): End time (Unix timestamp)
            filter (str or list, optional): Filter expression(s)
            **kwargs: Additional parameters to pass to the API

        Returns:
            dict: API response containing formatted event log entries

        Examples:
            # Get system event logs
            result = fgt.log.disk.event(subtype='system', rows=100)

            # Get HA events with time range and filter
            import time
            end_time = int(time.time())
            start_time = end_time - 3600  # Last hour
            result = fgt.log.disk.event(
                subtype='ha',
                start=start_time,
                end=end_time,
                filter='level==warning'
            )
        """
        endpoint = f'disk/event/{subtype}'
        params = {}

        if rows is not None:
            params['rows'] = rows
        if start is not None:
            params['start'] = start
        if end is not None:
            params['end'] = end
        if filter is not None:
            params['filter'] = filter

        params.update(kwargs)

        return self._client.get('log', endpoint, params=params if params else None)
