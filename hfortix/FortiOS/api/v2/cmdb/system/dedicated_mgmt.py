"""
FortiOS CMDB - System DedicatedMgmt

API Endpoints:
    GET    /system/dedicated-mgmt
    PUT    /system/dedicated-mgmt
"""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from ....http_client import HTTPClient


class DedicatedMgmt:
    """DedicatedMgmt operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize DedicatedMgmt endpoint.

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
        endpoint = "/system/dedicated-mgmt"
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
        interface: str | None = None,
        default_gateway: str | None = None,
        dhcp_server: str | None = None,
        dhcp_netmask: str | None = None,
        dhcp_start_ip: str | None = None,
        dhcp_end_ip: str | None = None,
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
            status: Enable/disable dedicated management. (optional)
            interface: Dedicated management interface. (optional)
            default_gateway: Default gateway for dedicated management interface. (optional)
            dhcp_server: Enable/disable DHCP server on management interface. (optional)
            dhcp_netmask: DHCP netmask. (optional)
            dhcp_start_ip: DHCP start IP for dedicated management. (optional)
            dhcp_end_ip: DHCP end IP for dedicated management. (optional)
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
        endpoint = "/system/dedicated-mgmt"
        if before is not None:
            data_payload['before'] = before
        if after is not None:
            data_payload['after'] = after
        if status is not None:
            data_payload['status'] = status
        if interface is not None:
            data_payload['interface'] = interface
        if default_gateway is not None:
            data_payload['default-gateway'] = default_gateway
        if dhcp_server is not None:
            data_payload['dhcp-server'] = dhcp_server
        if dhcp_netmask is not None:
            data_payload['dhcp-netmask'] = dhcp_netmask
        if dhcp_start_ip is not None:
            data_payload['dhcp-start-ip'] = dhcp_start_ip
        if dhcp_end_ip is not None:
            data_payload['dhcp-end-ip'] = dhcp_end_ip
        data_payload.update(kwargs)
        return self._client.put("cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json)
