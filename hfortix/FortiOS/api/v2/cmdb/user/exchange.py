"""
FortiOS CMDB - User Exchange

API Endpoints:
    GET    /user/exchange
    POST   /user/exchange
    GET    /user/exchange/{name}
    PUT    /user/exchange/{name}
    DELETE /user/exchange/{name}
"""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from ....http_client import HTTPClient


class Exchange:
    """Exchange operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize Exchange endpoint.

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
            endpoint = f"/user/exchange/{name}"
        else:
            endpoint = "/user/exchange"
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
        server_name: str | None = None,
        domain_name: str | None = None,
        username: str | None = None,
        password: str | None = None,
        ip: str | None = None,
        connect_protocol: str | None = None,
        validate_server_certificate: str | None = None,
        auth_type: str | None = None,
        auth_level: str | None = None,
        http_auth_type: str | None = None,
        ssl_min_proto_version: str | None = None,
        auto_discover_kdc: str | None = None,
        kdc_ip: list | None = None,
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
            name: MS Exchange server entry name. (optional)
            server_name: MS Exchange server hostname. (optional)
            domain_name: MS Exchange server fully qualified domain name. (optional)
            username: User name used to sign in to the server. Must have proper permissions for service. (optional)
            password: Password for the specified username. (optional)
            ip: Server IPv4 address. (optional)
            connect_protocol: Connection protocol used to connect to MS Exchange service. (optional)
            validate_server_certificate: Enable/disable exchange server certificate validation. (optional)
            auth_type: Authentication security type used for the RPC protocol layer. (optional)
            auth_level: Authentication security level used for the RPC protocol layer. (optional)
            http_auth_type: Authentication security type used for the HTTP transport. (optional)
            ssl_min_proto_version: Minimum SSL/TLS protocol version for HTTPS transport (default is to follow system global setting). (optional)
            auto_discover_kdc: Enable/disable automatic discovery of KDC IP addresses. (optional)
            kdc_ip: KDC IPv4 addresses for Kerberos authentication. (optional)
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
        endpoint = f"/user/exchange/{name}"
        if before is not None:
            data_payload['before'] = before
        if after is not None:
            data_payload['after'] = after
        if name is not None:
            data_payload['name'] = name
        if server_name is not None:
            data_payload['server-name'] = server_name
        if domain_name is not None:
            data_payload['domain-name'] = domain_name
        if username is not None:
            data_payload['username'] = username
        if password is not None:
            data_payload['password'] = password
        if ip is not None:
            data_payload['ip'] = ip
        if connect_protocol is not None:
            data_payload['connect-protocol'] = connect_protocol
        if validate_server_certificate is not None:
            data_payload['validate-server-certificate'] = validate_server_certificate
        if auth_type is not None:
            data_payload['auth-type'] = auth_type
        if auth_level is not None:
            data_payload['auth-level'] = auth_level
        if http_auth_type is not None:
            data_payload['http-auth-type'] = http_auth_type
        if ssl_min_proto_version is not None:
            data_payload['ssl-min-proto-version'] = ssl_min_proto_version
        if auto_discover_kdc is not None:
            data_payload['auto-discover-kdc'] = auto_discover_kdc
        if kdc_ip is not None:
            data_payload['kdc-ip'] = kdc_ip
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
        endpoint = f"/user/exchange/{name}"
        params.update(kwargs)
        return self._client.delete("cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json)

    def post(
        self,
        payload_dict: dict[str, Any] | None = None,
        nkey: str | None = None,
        name: str | None = None,
        server_name: str | None = None,
        domain_name: str | None = None,
        username: str | None = None,
        password: str | None = None,
        ip: str | None = None,
        connect_protocol: str | None = None,
        validate_server_certificate: str | None = None,
        auth_type: str | None = None,
        auth_level: str | None = None,
        http_auth_type: str | None = None,
        ssl_min_proto_version: str | None = None,
        auto_discover_kdc: str | None = None,
        kdc_ip: list | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Create object(s) in this table.
        
        Args:
            payload_dict: Optional dictionary of all parameters (can be passed as first positional arg)
            nkey: If *action=clone*, use *nkey* to specify the ID for the new resource to be created. (optional)
            name: MS Exchange server entry name. (optional)
            server_name: MS Exchange server hostname. (optional)
            domain_name: MS Exchange server fully qualified domain name. (optional)
            username: User name used to sign in to the server. Must have proper permissions for service. (optional)
            password: Password for the specified username. (optional)
            ip: Server IPv4 address. (optional)
            connect_protocol: Connection protocol used to connect to MS Exchange service. (optional)
            validate_server_certificate: Enable/disable exchange server certificate validation. (optional)
            auth_type: Authentication security type used for the RPC protocol layer. (optional)
            auth_level: Authentication security level used for the RPC protocol layer. (optional)
            http_auth_type: Authentication security type used for the HTTP transport. (optional)
            ssl_min_proto_version: Minimum SSL/TLS protocol version for HTTPS transport (default is to follow system global setting). (optional)
            auto_discover_kdc: Enable/disable automatic discovery of KDC IP addresses. (optional)
            kdc_ip: KDC IPv4 addresses for Kerberos authentication. (optional)
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
        endpoint = "/user/exchange"
        if nkey is not None:
            data_payload['nkey'] = nkey
        if name is not None:
            data_payload['name'] = name
        if server_name is not None:
            data_payload['server-name'] = server_name
        if domain_name is not None:
            data_payload['domain-name'] = domain_name
        if username is not None:
            data_payload['username'] = username
        if password is not None:
            data_payload['password'] = password
        if ip is not None:
            data_payload['ip'] = ip
        if connect_protocol is not None:
            data_payload['connect-protocol'] = connect_protocol
        if validate_server_certificate is not None:
            data_payload['validate-server-certificate'] = validate_server_certificate
        if auth_type is not None:
            data_payload['auth-type'] = auth_type
        if auth_level is not None:
            data_payload['auth-level'] = auth_level
        if http_auth_type is not None:
            data_payload['http-auth-type'] = http_auth_type
        if ssl_min_proto_version is not None:
            data_payload['ssl-min-proto-version'] = ssl_min_proto_version
        if auto_discover_kdc is not None:
            data_payload['auto-discover-kdc'] = auto_discover_kdc
        if kdc_ip is not None:
            data_payload['kdc-ip'] = kdc_ip
        data_payload.update(kwargs)
        return self._client.post("cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json)
