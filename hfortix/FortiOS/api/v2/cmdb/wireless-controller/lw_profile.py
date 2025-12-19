"""
FortiOS CMDB - Wireless-controller LwProfile

API Endpoints:
    GET    /wireless-controller/lw-profile
    POST   /wireless-controller/lw-profile
    GET    /wireless-controller/lw-profile/{name}
    PUT    /wireless-controller/lw-profile/{name}
    DELETE /wireless-controller/lw-profile/{name}
"""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from ....http_client import HTTPClient


class LwProfile:
    """LwProfile operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize LwProfile endpoint.

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
            endpoint = f"/wireless-controller/lw-profile/{name}"
        else:
            endpoint = "/wireless-controller/lw-profile"
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
        comment: str | None = None,
        lw_protocol: str | None = None,
        cups_server: str | None = None,
        cups_server_port: int | None = None,
        cups_api_key: str | None = None,
        tc_server: str | None = None,
        tc_server_port: int | None = None,
        tc_api_key: str | None = None,
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
            name: LoRaWAN profile name. (optional)
            comment: Comment. (optional)
            lw_protocol: Configure LoRaWAN protocol (default = basics-station) (optional)
            cups_server: CUPS (Configuration and Update Server) domain name or IP address of LoRaWAN device. (optional)
            cups_server_port: CUPS Port value of LoRaWAN device. (optional)
            cups_api_key: CUPS API key of LoRaWAN device. (optional)
            tc_server: TC (Traffic Controller) domain name or IP address of LoRaWAN device. (optional)
            tc_server_port: TC Port value of LoRaWAN device. (optional)
            tc_api_key: TC API key of LoRaWAN device. (optional)
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
        endpoint = f"/wireless-controller/lw-profile/{name}"
        if before is not None:
            data_payload['before'] = before
        if after is not None:
            data_payload['after'] = after
        if name is not None:
            data_payload['name'] = name
        if comment is not None:
            data_payload['comment'] = comment
        if lw_protocol is not None:
            data_payload['lw-protocol'] = lw_protocol
        if cups_server is not None:
            data_payload['cups-server'] = cups_server
        if cups_server_port is not None:
            data_payload['cups-server-port'] = cups_server_port
        if cups_api_key is not None:
            data_payload['cups-api-key'] = cups_api_key
        if tc_server is not None:
            data_payload['tc-server'] = tc_server
        if tc_server_port is not None:
            data_payload['tc-server-port'] = tc_server_port
        if tc_api_key is not None:
            data_payload['tc-api-key'] = tc_api_key
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
        endpoint = f"/wireless-controller/lw-profile/{name}"
        params.update(kwargs)
        return self._client.delete("cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json)

    def post(
        self,
        payload_dict: dict[str, Any] | None = None,
        nkey: str | None = None,
        name: str | None = None,
        comment: str | None = None,
        lw_protocol: str | None = None,
        cups_server: str | None = None,
        cups_server_port: int | None = None,
        cups_api_key: str | None = None,
        tc_server: str | None = None,
        tc_server_port: int | None = None,
        tc_api_key: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Create object(s) in this table.
        
        Args:
            payload_dict: Optional dictionary of all parameters (can be passed as first positional arg)
            nkey: If *action=clone*, use *nkey* to specify the ID for the new resource to be created. (optional)
            name: LoRaWAN profile name. (optional)
            comment: Comment. (optional)
            lw_protocol: Configure LoRaWAN protocol (default = basics-station) (optional)
            cups_server: CUPS (Configuration and Update Server) domain name or IP address of LoRaWAN device. (optional)
            cups_server_port: CUPS Port value of LoRaWAN device. (optional)
            cups_api_key: CUPS API key of LoRaWAN device. (optional)
            tc_server: TC (Traffic Controller) domain name or IP address of LoRaWAN device. (optional)
            tc_server_port: TC Port value of LoRaWAN device. (optional)
            tc_api_key: TC API key of LoRaWAN device. (optional)
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
        endpoint = "/wireless-controller/lw-profile"
        if nkey is not None:
            data_payload['nkey'] = nkey
        if name is not None:
            data_payload['name'] = name
        if comment is not None:
            data_payload['comment'] = comment
        if lw_protocol is not None:
            data_payload['lw-protocol'] = lw_protocol
        if cups_server is not None:
            data_payload['cups-server'] = cups_server
        if cups_server_port is not None:
            data_payload['cups-server-port'] = cups_server_port
        if cups_api_key is not None:
            data_payload['cups-api-key'] = cups_api_key
        if tc_server is not None:
            data_payload['tc-server'] = tc_server
        if tc_server_port is not None:
            data_payload['tc-server-port'] = tc_server_port
        if tc_api_key is not None:
            data_payload['tc-api-key'] = tc_api_key
        data_payload.update(kwargs)
        return self._client.post("cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json)
