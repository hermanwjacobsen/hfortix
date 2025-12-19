"""
FortiOS CMDB - Web-proxy IsolatorServer

API Endpoints:
    GET    /web-proxy/isolator-server
    POST   /web-proxy/isolator-server
    GET    /web-proxy/isolator-server/{name}
    PUT    /web-proxy/isolator-server/{name}
    DELETE /web-proxy/isolator-server/{name}
"""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from ....http_client import HTTPClient


class IsolatorServer:
    """IsolatorServer operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize IsolatorServer endpoint.

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
            endpoint = f"/web-proxy/isolator-server/{name}"
        else:
            endpoint = "/web-proxy/isolator-server"
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
        addr_type: str | None = None,
        ip: str | None = None,
        ipv6: str | None = None,
        fqdn: str | None = None,
        port: int | None = None,
        interface_select_method: str | None = None,
        interface: str | None = None,
        vrf_select: int | None = None,
        comment: str | None = None,
        masquerade: str | None = None,
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
            addr_type: Address type of the forwarding proxy server: IP or FQDN. (optional)
            ip: Forward proxy server IP address. (optional)
            ipv6: Forward proxy server IPv6 address. (optional)
            fqdn: Forward server Fully Qualified Domain Name (FQDN). (optional)
            port: Port number that the forwarding server expects to receive HTTP sessions on (1 - 65535, default = 3128). (optional)
            interface_select_method: Specify how to select outgoing interface to reach server. (optional)
            interface: Specify outgoing interface to reach server. (optional)
            vrf_select: VRF ID used for connection to server. (optional)
            comment: Comment. (optional)
            masquerade: Enable/disable use of the IP address of the outgoing interface as the client IP address (default = enable) (optional)
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
        endpoint = f"/web-proxy/isolator-server/{name}"
        if before is not None:
            data_payload['before'] = before
        if after is not None:
            data_payload['after'] = after
        if name is not None:
            data_payload['name'] = name
        if addr_type is not None:
            data_payload['addr-type'] = addr_type
        if ip is not None:
            data_payload['ip'] = ip
        if ipv6 is not None:
            data_payload['ipv6'] = ipv6
        if fqdn is not None:
            data_payload['fqdn'] = fqdn
        if port is not None:
            data_payload['port'] = port
        if interface_select_method is not None:
            data_payload['interface-select-method'] = interface_select_method
        if interface is not None:
            data_payload['interface'] = interface
        if vrf_select is not None:
            data_payload['vrf-select'] = vrf_select
        if comment is not None:
            data_payload['comment'] = comment
        if masquerade is not None:
            data_payload['masquerade'] = masquerade
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
        endpoint = f"/web-proxy/isolator-server/{name}"
        params.update(kwargs)
        return self._client.delete("cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json)

    def post(
        self,
        payload_dict: dict[str, Any] | None = None,
        nkey: str | None = None,
        name: str | None = None,
        addr_type: str | None = None,
        ip: str | None = None,
        ipv6: str | None = None,
        fqdn: str | None = None,
        port: int | None = None,
        interface_select_method: str | None = None,
        interface: str | None = None,
        vrf_select: int | None = None,
        comment: str | None = None,
        masquerade: str | None = None,
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
            addr_type: Address type of the forwarding proxy server: IP or FQDN. (optional)
            ip: Forward proxy server IP address. (optional)
            ipv6: Forward proxy server IPv6 address. (optional)
            fqdn: Forward server Fully Qualified Domain Name (FQDN). (optional)
            port: Port number that the forwarding server expects to receive HTTP sessions on (1 - 65535, default = 3128). (optional)
            interface_select_method: Specify how to select outgoing interface to reach server. (optional)
            interface: Specify outgoing interface to reach server. (optional)
            vrf_select: VRF ID used for connection to server. (optional)
            comment: Comment. (optional)
            masquerade: Enable/disable use of the IP address of the outgoing interface as the client IP address (default = enable) (optional)
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
        endpoint = "/web-proxy/isolator-server"
        if nkey is not None:
            data_payload['nkey'] = nkey
        if name is not None:
            data_payload['name'] = name
        if addr_type is not None:
            data_payload['addr-type'] = addr_type
        if ip is not None:
            data_payload['ip'] = ip
        if ipv6 is not None:
            data_payload['ipv6'] = ipv6
        if fqdn is not None:
            data_payload['fqdn'] = fqdn
        if port is not None:
            data_payload['port'] = port
        if interface_select_method is not None:
            data_payload['interface-select-method'] = interface_select_method
        if interface is not None:
            data_payload['interface'] = interface
        if vrf_select is not None:
            data_payload['vrf-select'] = vrf_select
        if comment is not None:
            data_payload['comment'] = comment
        if masquerade is not None:
            data_payload['masquerade'] = masquerade
        data_payload.update(kwargs)
        return self._client.post("cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json)
