"""
FortiOS CMDB - System FtmPush

API Endpoints:
    GET    /system/ftm-push
    PUT    /system/ftm-push
"""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from ....http_client import HTTPClient


class FtmPush:
    """FtmPush operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize FtmPush endpoint.

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
        endpoint = "/system/ftm-push"
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
        proxy: str | None = None,
        interface: str | None = None,
        server: str | None = None,
        server_port: int | None = None,
        server_cert: str | None = None,
        server_ip: str | None = None,
        status: str | None = None,
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
            proxy: Enable/disable communication to the proxy server in FortiGuard configuration. (optional)
            interface: Interface of FortiToken Mobile push services server. (optional)
            server: IPv4 address or domain name of FortiToken Mobile push services server. (optional)
            server_port: Port to communicate with FortiToken Mobile push services server (1 - 65535, default = 4433). (optional)
            server_cert: Name of the server certificate to be used for SSL. (optional)
            server_ip: IPv4 address of FortiToken Mobile push services server (format: xxx.xxx.xxx.xxx). (optional)
            status: Enable/disable the use of FortiToken Mobile push services. (optional)
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
        endpoint = "/system/ftm-push"
        if before is not None:
            data_payload['before'] = before
        if after is not None:
            data_payload['after'] = after
        if proxy is not None:
            data_payload['proxy'] = proxy
        if interface is not None:
            data_payload['interface'] = interface
        if server is not None:
            data_payload['server'] = server
        if server_port is not None:
            data_payload['server-port'] = server_port
        if server_cert is not None:
            data_payload['server-cert'] = server_cert
        if server_ip is not None:
            data_payload['server-ip'] = server_ip
        if status is not None:
            data_payload['status'] = status
        data_payload.update(kwargs)
        return self._client.put("cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json)
