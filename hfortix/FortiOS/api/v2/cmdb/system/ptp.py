"""
FortiOS CMDB - System Ptp

API Endpoints:
    GET    /system/ptp
    PUT    /system/ptp
"""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from ....http_client import HTTPClient


class Ptp:
    """Ptp operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize Ptp endpoint.

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
        endpoint = "/system/ptp"
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
        status: str | None = None,
        mode: str | None = None,
        delay_mechanism: str | None = None,
        request_interval: int | None = None,
        interface: str | None = None,
        server_mode: str | None = None,
        server_interface: list | None = None,
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
            status: Enable/disable setting the FortiGate system time by synchronizing with an PTP Server. (optional)
            mode: Multicast transmission or hybrid transmission. (optional)
            delay_mechanism: End to end delay detection or peer to peer delay detection. (optional)
            request_interval: The delay request value is the logarithmic mean interval in seconds between the delay request messages sent by the slave to the master. (optional)
            interface: PTP client will reply through this interface. (optional)
            server_mode: Enable/disable FortiGate PTP server mode. Your FortiGate becomes an PTP server for other devices on your network. (optional)
            server_interface: FortiGate interface(s) with PTP server mode enabled. Devices on your network can contact these interfaces for PTP services. (optional)
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
        endpoint = "/system/ptp"
        if before is not None:
            data_payload['before'] = before
        if after is not None:
            data_payload['after'] = after
        if status is not None:
            data_payload['status'] = status
        if mode is not None:
            data_payload['mode'] = mode
        if delay_mechanism is not None:
            data_payload['delay-mechanism'] = delay_mechanism
        if request_interval is not None:
            data_payload['request-interval'] = request_interval
        if interface is not None:
            data_payload['interface'] = interface
        if server_mode is not None:
            data_payload['server-mode'] = server_mode
        if server_interface is not None:
            data_payload['server-interface'] = server_interface
        data_payload.update(kwargs)
        return self._client.put("cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json)
