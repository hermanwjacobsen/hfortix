"""
FortiOS CMDB - System EmailServer

API Endpoints:
    GET    /system/email-server
    PUT    /system/email-server
"""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from ....http_client import HTTPClient


class EmailServer:
    """EmailServer operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize EmailServer endpoint.

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
        endpoint = "/system/email-server"
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
        type: str | None = None,
        server: str | None = None,
        port: int | None = None,
        source_ip: str | None = None,
        source_ip6: str | None = None,
        authenticate: str | None = None,
        validate_server: str | None = None,
        username: str | None = None,
        password: str | None = None,
        security: str | None = None,
        ssl_min_proto_version: str | None = None,
        interface_select_method: str | None = None,
        interface: str | None = None,
        vrf_select: int | None = None,
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
            type: Use FortiGuard Message service or custom email server. (optional)
            server: SMTP server IP address or hostname. (optional)
            port: SMTP server port. (optional)
            source_ip: SMTP server IPv4 source IP. (optional)
            source_ip6: SMTP server IPv6 source IP. (optional)
            authenticate: Enable/disable authentication. (optional)
            validate_server: Enable/disable validation of server certificate. (optional)
            username: SMTP server user name for authentication. (optional)
            password: SMTP server user password for authentication. (optional)
            security: Connection security used by the email server. (optional)
            ssl_min_proto_version: Minimum supported protocol version for SSL/TLS connections (default is to follow system global setting). (optional)
            interface_select_method: Specify how to select outgoing interface to reach server. (optional)
            interface: Specify outgoing interface to reach server. (optional)
            vrf_select: VRF ID used for connection to server. (optional)
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
        endpoint = "/system/email-server"
        if before is not None:
            data_payload['before'] = before
        if after is not None:
            data_payload['after'] = after
        if type is not None:
            data_payload['type'] = type
        if server is not None:
            data_payload['server'] = server
        if port is not None:
            data_payload['port'] = port
        if source_ip is not None:
            data_payload['source-ip'] = source_ip
        if source_ip6 is not None:
            data_payload['source-ip6'] = source_ip6
        if authenticate is not None:
            data_payload['authenticate'] = authenticate
        if validate_server is not None:
            data_payload['validate-server'] = validate_server
        if username is not None:
            data_payload['username'] = username
        if password is not None:
            data_payload['password'] = password
        if security is not None:
            data_payload['security'] = security
        if ssl_min_proto_version is not None:
            data_payload['ssl-min-proto-version'] = ssl_min_proto_version
        if interface_select_method is not None:
            data_payload['interface-select-method'] = interface_select_method
        if interface is not None:
            data_payload['interface'] = interface
        if vrf_select is not None:
            data_payload['vrf-select'] = vrf_select
        data_payload.update(kwargs)
        return self._client.put("cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json)
