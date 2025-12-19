"""
FortiOS CMDB - Firewall SslServer

API Endpoints:
    GET    /firewall/ssl-server
    POST   /firewall/ssl-server
    GET    /firewall/ssl-server/{name}
    PUT    /firewall/ssl-server/{name}
    DELETE /firewall/ssl-server/{name}
"""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from ....http_client import HTTPClient


class SslServer:
    """SslServer operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize SslServer endpoint.

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
            endpoint = f"/firewall/ssl-server/{name}"
        else:
            endpoint = "/firewall/ssl-server"
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
        ip: str | None = None,
        port: int | None = None,
        ssl_mode: str | None = None,
        add_header_x_forwarded_proto: str | None = None,
        mapped_port: int | None = None,
        ssl_cert: list | None = None,
        ssl_dh_bits: str | None = None,
        ssl_algorithm: str | None = None,
        ssl_client_renegotiation: str | None = None,
        ssl_min_version: str | None = None,
        ssl_max_version: str | None = None,
        ssl_send_empty_frags: str | None = None,
        url_rewrite: str | None = None,
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
            name: Server name. (optional)
            ip: IPv4 address of the SSL server. (optional)
            port: Server service port (1 - 65535, default = 443). (optional)
            ssl_mode: SSL/TLS mode for encryption and decryption of traffic. (optional)
            add_header_x_forwarded_proto: Enable/disable adding an X-Forwarded-Proto header to forwarded requests. (optional)
            mapped_port: Mapped server service port (1 - 65535, default = 80). (optional)
            ssl_cert: List of certificate names to use for SSL connections to this server. (default = "Fortinet_SSL"). (optional)
            ssl_dh_bits: Bit-size of Diffie-Hellman (DH) prime used in DHE-RSA negotiation (default = 2048). (optional)
            ssl_algorithm: Relative strength of encryption algorithms accepted in negotiation. (optional)
            ssl_client_renegotiation: Allow or block client renegotiation by server. (optional)
            ssl_min_version: Lowest SSL/TLS version to negotiate. (optional)
            ssl_max_version: Highest SSL/TLS version to negotiate. (optional)
            ssl_send_empty_frags: Enable/disable sending empty fragments to avoid attack on CBC IV. (optional)
            url_rewrite: Enable/disable rewriting the URL. (optional)
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
        endpoint = f"/firewall/ssl-server/{name}"
        if before is not None:
            data_payload['before'] = before
        if after is not None:
            data_payload['after'] = after
        if name is not None:
            data_payload['name'] = name
        if ip is not None:
            data_payload['ip'] = ip
        if port is not None:
            data_payload['port'] = port
        if ssl_mode is not None:
            data_payload['ssl-mode'] = ssl_mode
        if add_header_x_forwarded_proto is not None:
            data_payload['add-header-x-forwarded-proto'] = add_header_x_forwarded_proto
        if mapped_port is not None:
            data_payload['mapped-port'] = mapped_port
        if ssl_cert is not None:
            data_payload['ssl-cert'] = ssl_cert
        if ssl_dh_bits is not None:
            data_payload['ssl-dh-bits'] = ssl_dh_bits
        if ssl_algorithm is not None:
            data_payload['ssl-algorithm'] = ssl_algorithm
        if ssl_client_renegotiation is not None:
            data_payload['ssl-client-renegotiation'] = ssl_client_renegotiation
        if ssl_min_version is not None:
            data_payload['ssl-min-version'] = ssl_min_version
        if ssl_max_version is not None:
            data_payload['ssl-max-version'] = ssl_max_version
        if ssl_send_empty_frags is not None:
            data_payload['ssl-send-empty-frags'] = ssl_send_empty_frags
        if url_rewrite is not None:
            data_payload['url-rewrite'] = url_rewrite
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
        endpoint = f"/firewall/ssl-server/{name}"
        params.update(kwargs)
        return self._client.delete("cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json)

    def post(
        self,
        payload_dict: dict[str, Any] | None = None,
        nkey: str | None = None,
        name: str | None = None,
        ip: str | None = None,
        port: int | None = None,
        ssl_mode: str | None = None,
        add_header_x_forwarded_proto: str | None = None,
        mapped_port: int | None = None,
        ssl_cert: list | None = None,
        ssl_dh_bits: str | None = None,
        ssl_algorithm: str | None = None,
        ssl_client_renegotiation: str | None = None,
        ssl_min_version: str | None = None,
        ssl_max_version: str | None = None,
        ssl_send_empty_frags: str | None = None,
        url_rewrite: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Create object(s) in this table.
        
        Args:
            payload_dict: Optional dictionary of all parameters (can be passed as first positional arg)
            nkey: If *action=clone*, use *nkey* to specify the ID for the new resource to be created. (optional)
            name: Server name. (optional)
            ip: IPv4 address of the SSL server. (optional)
            port: Server service port (1 - 65535, default = 443). (optional)
            ssl_mode: SSL/TLS mode for encryption and decryption of traffic. (optional)
            add_header_x_forwarded_proto: Enable/disable adding an X-Forwarded-Proto header to forwarded requests. (optional)
            mapped_port: Mapped server service port (1 - 65535, default = 80). (optional)
            ssl_cert: List of certificate names to use for SSL connections to this server. (default = "Fortinet_SSL"). (optional)
            ssl_dh_bits: Bit-size of Diffie-Hellman (DH) prime used in DHE-RSA negotiation (default = 2048). (optional)
            ssl_algorithm: Relative strength of encryption algorithms accepted in negotiation. (optional)
            ssl_client_renegotiation: Allow or block client renegotiation by server. (optional)
            ssl_min_version: Lowest SSL/TLS version to negotiate. (optional)
            ssl_max_version: Highest SSL/TLS version to negotiate. (optional)
            ssl_send_empty_frags: Enable/disable sending empty fragments to avoid attack on CBC IV. (optional)
            url_rewrite: Enable/disable rewriting the URL. (optional)
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
        endpoint = "/firewall/ssl-server"
        if nkey is not None:
            data_payload['nkey'] = nkey
        if name is not None:
            data_payload['name'] = name
        if ip is not None:
            data_payload['ip'] = ip
        if port is not None:
            data_payload['port'] = port
        if ssl_mode is not None:
            data_payload['ssl-mode'] = ssl_mode
        if add_header_x_forwarded_proto is not None:
            data_payload['add-header-x-forwarded-proto'] = add_header_x_forwarded_proto
        if mapped_port is not None:
            data_payload['mapped-port'] = mapped_port
        if ssl_cert is not None:
            data_payload['ssl-cert'] = ssl_cert
        if ssl_dh_bits is not None:
            data_payload['ssl-dh-bits'] = ssl_dh_bits
        if ssl_algorithm is not None:
            data_payload['ssl-algorithm'] = ssl_algorithm
        if ssl_client_renegotiation is not None:
            data_payload['ssl-client-renegotiation'] = ssl_client_renegotiation
        if ssl_min_version is not None:
            data_payload['ssl-min-version'] = ssl_min_version
        if ssl_max_version is not None:
            data_payload['ssl-max-version'] = ssl_max_version
        if ssl_send_empty_frags is not None:
            data_payload['ssl-send-empty-frags'] = ssl_send_empty_frags
        if url_rewrite is not None:
            data_payload['url-rewrite'] = url_rewrite
        data_payload.update(kwargs)
        return self._client.post("cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json)
