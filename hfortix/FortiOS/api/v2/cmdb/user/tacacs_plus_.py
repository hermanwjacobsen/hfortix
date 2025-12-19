"""
FortiOS CMDB - User TacacsPlus

API Endpoints:
    GET    /user/tacacs+
    POST   /user/tacacs+
    GET    /user/tacacs+/{name}
    PUT    /user/tacacs+/{name}
    DELETE /user/tacacs+/{name}
"""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from ....http_client import HTTPClient


class TacacsPlus:
    """TacacsPlus operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize TacacsPlus endpoint.

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
            endpoint = f"/user/tacacs+/{name}"
        else:
            endpoint = "/user/tacacs+"
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
        server: str | None = None,
        secondary_server: str | None = None,
        tertiary_server: str | None = None,
        port: int | None = None,
        secondary_key: str | None = None,
        tertiary_key: str | None = None,
        status_ttl: int | None = None,
        authen_type: str | None = None,
        authorization: str | None = None,
        source_ip: str | None = None,
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
            name: Object identifier (required)
            before: If *action=move*, use *before* to specify the ID of the resource that this resource will be moved before. (optional)
            after: If *action=move*, use *after* to specify the ID of the resource that this resource will be moved after. (optional)
            name: TACACS+ server entry name. (optional)
            server: Primary TACACS+ server CN domain name or IP address. (optional)
            secondary_server: Secondary TACACS+ server CN domain name or IP address. (optional)
            tertiary_server: Tertiary TACACS+ server CN domain name or IP address. (optional)
            port: Port number of the TACACS+ server. (optional)
            secondary_key: Key to access the secondary server. (optional)
            tertiary_key: Key to access the tertiary server. (optional)
            status_ttl: Time for which server reachability is cached so that when a server is unreachable, it will not be retried for at least this period of time (0 = cache disabled, default = 300). (optional)
            authen_type: Allowed authentication protocols/methods. (optional)
            authorization: Enable/disable TACACS+ authorization. (optional)
            source_ip: Source IP address for communications to TACACS+ server. (optional)
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
        
        # Build endpoint path
        if not name:
            raise ValueError("name is required for put()")
        endpoint = f"/user/tacacs+/{name}"
        if before is not None:
            data_payload['before'] = before
        if after is not None:
            data_payload['after'] = after
        if name is not None:
            data_payload['name'] = name
        if server is not None:
            data_payload['server'] = server
        if secondary_server is not None:
            data_payload['secondary-server'] = secondary_server
        if tertiary_server is not None:
            data_payload['tertiary-server'] = tertiary_server
        if port is not None:
            data_payload['port'] = port
        if secondary_key is not None:
            data_payload['secondary-key'] = secondary_key
        if tertiary_key is not None:
            data_payload['tertiary-key'] = tertiary_key
        if status_ttl is not None:
            data_payload['status-ttl'] = status_ttl
        if authen_type is not None:
            data_payload['authen-type'] = authen_type
        if authorization is not None:
            data_payload['authorization'] = authorization
        if source_ip is not None:
            data_payload['source-ip'] = source_ip
        if interface_select_method is not None:
            data_payload['interface-select-method'] = interface_select_method
        if interface is not None:
            data_payload['interface'] = interface
        if vrf_select is not None:
            data_payload['vrf-select'] = vrf_select
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
        endpoint = f"/user/tacacs+/{name}"
        params.update(kwargs)
        return self._client.delete("cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json)

    def post(
        self,
        payload_dict: dict[str, Any] | None = None,
        nkey: str | None = None,
        name: str | None = None,
        server: str | None = None,
        secondary_server: str | None = None,
        tertiary_server: str | None = None,
        port: int | None = None,
        secondary_key: str | None = None,
        tertiary_key: str | None = None,
        status_ttl: int | None = None,
        authen_type: str | None = None,
        authorization: str | None = None,
        source_ip: str | None = None,
        interface_select_method: str | None = None,
        interface: str | None = None,
        vrf_select: int | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Create object(s) in this table.
        
        Args:
            payload_dict: Optional dictionary of all parameters (can be passed as first positional arg)
            nkey: If *action=clone*, use *nkey* to specify the ID for the new resource to be created. (optional)
            name: TACACS+ server entry name. (optional)
            server: Primary TACACS+ server CN domain name or IP address. (optional)
            secondary_server: Secondary TACACS+ server CN domain name or IP address. (optional)
            tertiary_server: Tertiary TACACS+ server CN domain name or IP address. (optional)
            port: Port number of the TACACS+ server. (optional)
            secondary_key: Key to access the secondary server. (optional)
            tertiary_key: Key to access the tertiary server. (optional)
            status_ttl: Time for which server reachability is cached so that when a server is unreachable, it will not be retried for at least this period of time (0 = cache disabled, default = 300). (optional)
            authen_type: Allowed authentication protocols/methods. (optional)
            authorization: Enable/disable TACACS+ authorization. (optional)
            source_ip: Source IP address for communications to TACACS+ server. (optional)
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
        endpoint = "/user/tacacs+"
        if nkey is not None:
            data_payload['nkey'] = nkey
        if name is not None:
            data_payload['name'] = name
        if server is not None:
            data_payload['server'] = server
        if secondary_server is not None:
            data_payload['secondary-server'] = secondary_server
        if tertiary_server is not None:
            data_payload['tertiary-server'] = tertiary_server
        if port is not None:
            data_payload['port'] = port
        if secondary_key is not None:
            data_payload['secondary-key'] = secondary_key
        if tertiary_key is not None:
            data_payload['tertiary-key'] = tertiary_key
        if status_ttl is not None:
            data_payload['status-ttl'] = status_ttl
        if authen_type is not None:
            data_payload['authen-type'] = authen_type
        if authorization is not None:
            data_payload['authorization'] = authorization
        if source_ip is not None:
            data_payload['source-ip'] = source_ip
        if interface_select_method is not None:
            data_payload['interface-select-method'] = interface_select_method
        if interface is not None:
            data_payload['interface'] = interface
        if vrf_select is not None:
            data_payload['vrf-select'] = vrf_select
        data_payload.update(kwargs)
        return self._client.post("cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json)
