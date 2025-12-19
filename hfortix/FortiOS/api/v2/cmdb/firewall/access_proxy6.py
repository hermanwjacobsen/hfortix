"""
FortiOS CMDB - Firewall AccessProxy6

API Endpoints:
    GET    /firewall/access-proxy6
    POST   /firewall/access-proxy6
    GET    /firewall/access-proxy6/{name}
    PUT    /firewall/access-proxy6/{name}
    DELETE /firewall/access-proxy6/{name}
"""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from ....http_client import HTTPClient


class AccessProxy6:
    """AccessProxy6 operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize AccessProxy6 endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

    def get(
        self,
        name: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        attr: str | None = None,
        skip_to_datasource: dict | None = None,
        acs: int | None = None,
        search: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Select a specific entry from a CLI table.
        
        Args:
            name: Object identifier (optional for list, required for specific)
            attr: Attribute name that references other table (optional)
            skip_to_datasource: Skip to provided table's Nth entry. E.g {datasource: 'firewall.address', pos: 10, global_entry: false} (optional)
            acs: If true, returned result are in ascending order. (optional)
            search: If present, the objects will be filtered by the search value. (optional)
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
        
        # Build endpoint path
        if name:
            endpoint = f"/firewall/access-proxy6/{name}"
        else:
            endpoint = "/firewall/access-proxy6"
        if attr is not None:
            params['attr'] = attr
        if skip_to_datasource is not None:
            params['skip_to_datasource'] = skip_to_datasource
        if acs is not None:
            params['acs'] = acs
        if search is not None:
            params['search'] = search
        params.update(kwargs)
        return self._client.get("cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json)

    def put(
        self,
        name: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        before: str | None = None,
        after: str | None = None,
        vip: str | None = None,
        auth_portal: str | None = None,
        auth_virtual_host: str | None = None,
        log_blocked_traffic: str | None = None,
        add_vhost_domain_to_dnsdb: str | None = None,
        svr_pool_multiplex: str | None = None,
        svr_pool_ttl: int | None = None,
        svr_pool_server_max_request: int | None = None,
        svr_pool_server_max_concurrent_request: int | None = None,
        decrypted_traffic_mirror: str | None = None,
        api_gateway: list | None = None,
        api_gateway6: list | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Update this specific resource.
        
        Args:
            payload_dict: Optional dictionary of all parameters (can be passed as first positional arg)
            name: Object identifier (required)
            before: If *action=move*, use *before* to specify the ID of the resource that this resource will be moved before. (optional)
            after: If *action=move*, use *after* to specify the ID of the resource that this resource will be moved after. (optional)
            name: Access Proxy name. (optional)
            vip: Virtual IP name. (optional)
            auth_portal: Enable/disable authentication portal. (optional)
            auth_virtual_host: Virtual host for authentication portal. (optional)
            log_blocked_traffic: Enable/disable logging of blocked traffic. (optional)
            add_vhost_domain_to_dnsdb: Enable/disable adding vhost/domain to dnsdb for ztna dox tunnel. (optional)
            svr_pool_multiplex: Enable/disable server pool multiplexing (default = disable). Share connected server in HTTP, HTTPS, and web-portal api-gateway. (optional)
            svr_pool_ttl: Time-to-live in the server pool for idle connections to servers. (optional)
            svr_pool_server_max_request: Maximum number of requests that servers in server pool handle before disconnecting (default = unlimited). (optional)
            svr_pool_server_max_concurrent_request: Maximum number of concurrent requests that servers in server pool could handle (default = unlimited). (optional)
            decrypted_traffic_mirror: Decrypted traffic mirror. (optional)
            api_gateway: Set IPv4 API Gateway. (optional)
            api_gateway6: Set IPv6 API Gateway. (optional)
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
        
        # Build endpoint path
        if not name:
            raise ValueError("name is required for put()")
        endpoint = f"/firewall/access-proxy6/{name}"
        if before is not None:
            data_payload['before'] = before
        if after is not None:
            data_payload['after'] = after
        if name is not None:
            data_payload['name'] = name
        if vip is not None:
            data_payload['vip'] = vip
        if auth_portal is not None:
            data_payload['auth-portal'] = auth_portal
        if auth_virtual_host is not None:
            data_payload['auth-virtual-host'] = auth_virtual_host
        if log_blocked_traffic is not None:
            data_payload['log-blocked-traffic'] = log_blocked_traffic
        if add_vhost_domain_to_dnsdb is not None:
            data_payload['add-vhost-domain-to-dnsdb'] = add_vhost_domain_to_dnsdb
        if svr_pool_multiplex is not None:
            data_payload['svr-pool-multiplex'] = svr_pool_multiplex
        if svr_pool_ttl is not None:
            data_payload['svr-pool-ttl'] = svr_pool_ttl
        if svr_pool_server_max_request is not None:
            data_payload['svr-pool-server-max-request'] = svr_pool_server_max_request
        if svr_pool_server_max_concurrent_request is not None:
            data_payload['svr-pool-server-max-concurrent-request'] = svr_pool_server_max_concurrent_request
        if decrypted_traffic_mirror is not None:
            data_payload['decrypted-traffic-mirror'] = decrypted_traffic_mirror
        if api_gateway is not None:
            data_payload['api-gateway'] = api_gateway
        if api_gateway6 is not None:
            data_payload['api-gateway6'] = api_gateway6
        data_payload.update(kwargs)
        return self._client.put("cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json)

    def delete(
        self,
        name: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Delete this specific resource.
        
        Args:
            name: Object identifier (required)
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
        
        # Build endpoint path
        if not name:
            raise ValueError("name is required for delete()")
        endpoint = f"/firewall/access-proxy6/{name}"
        params.update(kwargs)
        return self._client.delete("cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json)

    def post(
        self,
        payload_dict: dict[str, Any] | None = None,
        nkey: str | None = None,
        name: str | None = None,
        vip: str | None = None,
        auth_portal: str | None = None,
        auth_virtual_host: str | None = None,
        log_blocked_traffic: str | None = None,
        add_vhost_domain_to_dnsdb: str | None = None,
        svr_pool_multiplex: str | None = None,
        svr_pool_ttl: int | None = None,
        svr_pool_server_max_request: int | None = None,
        svr_pool_server_max_concurrent_request: int | None = None,
        decrypted_traffic_mirror: str | None = None,
        api_gateway: list | None = None,
        api_gateway6: list | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Create object(s) in this table.
        
        Args:
            payload_dict: Optional dictionary of all parameters (can be passed as first positional arg)
            nkey: If *action=clone*, use *nkey* to specify the ID for the new resource to be created. (optional)
            name: Access Proxy name. (optional)
            vip: Virtual IP name. (optional)
            auth_portal: Enable/disable authentication portal. (optional)
            auth_virtual_host: Virtual host for authentication portal. (optional)
            log_blocked_traffic: Enable/disable logging of blocked traffic. (optional)
            add_vhost_domain_to_dnsdb: Enable/disable adding vhost/domain to dnsdb for ztna dox tunnel. (optional)
            svr_pool_multiplex: Enable/disable server pool multiplexing (default = disable). Share connected server in HTTP, HTTPS, and web-portal api-gateway. (optional)
            svr_pool_ttl: Time-to-live in the server pool for idle connections to servers. (optional)
            svr_pool_server_max_request: Maximum number of requests that servers in server pool handle before disconnecting (default = unlimited). (optional)
            svr_pool_server_max_concurrent_request: Maximum number of concurrent requests that servers in server pool could handle (default = unlimited). (optional)
            decrypted_traffic_mirror: Decrypted traffic mirror. (optional)
            api_gateway: Set IPv4 API Gateway. (optional)
            api_gateway6: Set IPv6 API Gateway. (optional)
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
        endpoint = "/firewall/access-proxy6"
        if nkey is not None:
            data_payload['nkey'] = nkey
        if name is not None:
            data_payload['name'] = name
        if vip is not None:
            data_payload['vip'] = vip
        if auth_portal is not None:
            data_payload['auth-portal'] = auth_portal
        if auth_virtual_host is not None:
            data_payload['auth-virtual-host'] = auth_virtual_host
        if log_blocked_traffic is not None:
            data_payload['log-blocked-traffic'] = log_blocked_traffic
        if add_vhost_domain_to_dnsdb is not None:
            data_payload['add-vhost-domain-to-dnsdb'] = add_vhost_domain_to_dnsdb
        if svr_pool_multiplex is not None:
            data_payload['svr-pool-multiplex'] = svr_pool_multiplex
        if svr_pool_ttl is not None:
            data_payload['svr-pool-ttl'] = svr_pool_ttl
        if svr_pool_server_max_request is not None:
            data_payload['svr-pool-server-max-request'] = svr_pool_server_max_request
        if svr_pool_server_max_concurrent_request is not None:
            data_payload['svr-pool-server-max-concurrent-request'] = svr_pool_server_max_concurrent_request
        if decrypted_traffic_mirror is not None:
            data_payload['decrypted-traffic-mirror'] = decrypted_traffic_mirror
        if api_gateway is not None:
            data_payload['api-gateway'] = api_gateway
        if api_gateway6 is not None:
            data_payload['api-gateway6'] = api_gateway6
        data_payload.update(kwargs)
        return self._client.post("cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json)
