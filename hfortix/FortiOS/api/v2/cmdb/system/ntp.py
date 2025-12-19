"""
FortiOS CMDB - System Ntp

API Endpoints:
    GET    /system/ntp
    PUT    /system/ntp
"""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from ....http_client import HTTPClient


class Ntp:
    """Ntp operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize Ntp endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

    def get(
        self,
        payload_dict: dict[str, Any] | None = None,
        exclude_default_values: bool | None = None,
        stat_items: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Select all entries in a CLI table.
        
        Args:
            exclude_default_values: Exclude properties/objects with default value (optional)
            stat_items: Items to count occurrence in entire response (multiple items should be separated by '|'). (optional)
            vdom: Virtual domain name, or False to skip. Handled by HTTPClient.
            raw_json: If True, return full API response with metadata. If False, return only results.
            **kwargs: Additional query parameters (filter, sort, start, count, format, etc.)
        
        Common Query Parameters (via **kwargs):
            filter: Filter results (e.g., filter='name==value')
            sort: Sort results (e.g., sort='name,asc')
            start: Starting entry index for paging
            count: Maximum number of entries to return
            format: Fields to return (e.g., format='name|type')
            See FortiOS REST API documentation for full list of query parameters
        
        Returns:
            Dictionary containing API response
        """
        params = payload_dict.copy() if payload_dict else {}
        endpoint = "/system/ntp"
        if exclude_default_values is not None:
            params['exclude-default-values'] = exclude_default_values
        if stat_items is not None:
            params['stat-items'] = stat_items
        params.update(kwargs)
        return self._client.get("cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json)

    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        before: str | None = None,
        after: str | None = None,
        ntpsync: str | None = None,
        type: str | None = None,
        syncinterval: int | None = None,
        ntpserver: list | None = None,
        source_ip: str | None = None,
        source_ip6: str | None = None,
        server_mode: str | None = None,
        authentication: str | None = None,
        key_type: str | None = None,
        key_id: int | None = None,
        interface: list | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Update this specific resource.
        
        Args:
            payload_dict: Optional dictionary of all parameters (can be passed as first positional arg)
            before: If *action=move*, use *before* to specify the ID of the resource that this resource will be moved before. (optional)
            after: If *action=move*, use *after* to specify the ID of the resource that this resource will be moved after. (optional)
            ntpsync: Enable/disable setting the FortiGate system time by synchronizing with an NTP Server. (optional)
            type: Use the FortiGuard NTP server or any other available NTP Server. (optional)
            syncinterval: NTP synchronization interval (1 - 1440 min). (optional)
            ntpserver: Configure the FortiGate to connect to any available third-party NTP server. (optional)
            source_ip: Source IP address for communication to the NTP server. (optional)
            source_ip6: Source IPv6 address for communication to the NTP server. (optional)
            server_mode: Enable/disable FortiGate NTP Server Mode. Your FortiGate becomes an NTP server for other devices on your network. The FortiGate relays NTP requests to its configured NTP server. (optional)
            authentication: Enable/disable authentication. (optional)
            key_type: Key type for authentication (MD5, SHA1, SHA256). (optional)
            key_id: Key ID for authentication. (optional)
            interface: FortiGate interface(s) with NTP server mode enabled. Devices on your network can contact these interfaces for NTP services. (optional)
            vdom: Virtual domain name, or False to skip. Handled by HTTPClient.
            raw_json: If True, return full API response with metadata. If False, return only results.
            **kwargs: Additional query parameters (filter, sort, start, count, format, etc.)
        
        Common Query Parameters (via **kwargs):
            filter: Filter results (e.g., filter='name==value')
            sort: Sort results (e.g., sort='name,asc')
            start: Starting entry index for paging
            count: Maximum number of entries to return
            format: Fields to return (e.g., format='name|type')
            See FortiOS REST API documentation for full list of query parameters
        
        Returns:
            Dictionary containing API response
        """
        data_payload = payload_dict.copy() if payload_dict else {}
        params = {}
        endpoint = "/system/ntp"
        if before is not None:
            data_payload['before'] = before
        if after is not None:
            data_payload['after'] = after
        if ntpsync is not None:
            data_payload['ntpsync'] = ntpsync
        if type is not None:
            data_payload['type'] = type
        if syncinterval is not None:
            data_payload['syncinterval'] = syncinterval
        if ntpserver is not None:
            data_payload['ntpserver'] = ntpserver
        if source_ip is not None:
            data_payload['source-ip'] = source_ip
        if source_ip6 is not None:
            data_payload['source-ip6'] = source_ip6
        if server_mode is not None:
            data_payload['server-mode'] = server_mode
        if authentication is not None:
            data_payload['authentication'] = authentication
        if key_type is not None:
            data_payload['key-type'] = key_type
        if key_id is not None:
            data_payload['key-id'] = key_id
        if interface is not None:
            data_payload['interface'] = interface
        data_payload.update(kwargs)
        return self._client.put("cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json)
