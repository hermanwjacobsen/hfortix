"""
FortiOS CMDB - Vpn IpsecManualkey

API Endpoints:
    GET    /vpn.ipsec/manualkey
    POST   /vpn.ipsec/manualkey
    GET    /vpn.ipsec/manualkey/{name}
    PUT    /vpn.ipsec/manualkey/{name}
    DELETE /vpn.ipsec/manualkey/{name}
"""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from ....http_client import HTTPClient


class IpsecManualkey:
    """IpsecManualkey operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize IpsecManualkey endpoint.

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
            endpoint = f"/vpn.ipsec/manualkey/{name}"
        else:
            endpoint = "/vpn.ipsec/manualkey"
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
        interface: str | None = None,
        remote_gw: str | None = None,
        local_gw: str | None = None,
        authentication: str | None = None,
        encryption: str | None = None,
        authkey: str | None = None,
        enckey: str | None = None,
        localspi: str | None = None,
        remotespi: str | None = None,
        npu_offload: str | None = None,
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
            name: IPsec tunnel name. (optional)
            interface: Name of the physical, aggregate, or VLAN interface. (optional)
            remote_gw: Peer gateway. (optional)
            local_gw: Local gateway. (optional)
            authentication: Authentication algorithm. Must be the same for both ends of the tunnel. (optional)
            encryption: Encryption algorithm. Must be the same for both ends of the tunnel. (optional)
            authkey: Hexadecimal authentication key in 16-digit (8-byte) segments separated by hyphens. (optional)
            enckey: Hexadecimal encryption key in 16-digit (8-byte) segments separated by hyphens. (optional)
            localspi: Local SPI, a hexadecimal 8-digit (4-byte) tag. Discerns between two traffic streams with different encryption rules. (optional)
            remotespi: Remote SPI, a hexadecimal 8-digit (4-byte) tag. Discerns between two traffic streams with different encryption rules. (optional)
            npu_offload: Enable/disable NPU offloading. (optional)
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
        endpoint = f"/vpn.ipsec/manualkey/{name}"
        if before is not None:
            data_payload['before'] = before
        if after is not None:
            data_payload['after'] = after
        if name is not None:
            data_payload['name'] = name
        if interface is not None:
            data_payload['interface'] = interface
        if remote_gw is not None:
            data_payload['remote-gw'] = remote_gw
        if local_gw is not None:
            data_payload['local-gw'] = local_gw
        if authentication is not None:
            data_payload['authentication'] = authentication
        if encryption is not None:
            data_payload['encryption'] = encryption
        if authkey is not None:
            data_payload['authkey'] = authkey
        if enckey is not None:
            data_payload['enckey'] = enckey
        if localspi is not None:
            data_payload['localspi'] = localspi
        if remotespi is not None:
            data_payload['remotespi'] = remotespi
        if npu_offload is not None:
            data_payload['npu-offload'] = npu_offload
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
        endpoint = f"/vpn.ipsec/manualkey/{name}"
        params.update(kwargs)
        return self._client.delete("cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json)

    def post(
        self,
        payload_dict: dict[str, Any] | None = None,
        nkey: str | None = None,
        name: str | None = None,
        interface: str | None = None,
        remote_gw: str | None = None,
        local_gw: str | None = None,
        authentication: str | None = None,
        encryption: str | None = None,
        authkey: str | None = None,
        enckey: str | None = None,
        localspi: str | None = None,
        remotespi: str | None = None,
        npu_offload: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Create object(s) in this table.
        
        Args:
            payload_dict: Optional dictionary of all parameters (can be passed as first positional arg)
            nkey: If *action=clone*, use *nkey* to specify the ID for the new resource to be created. (optional)
            name: IPsec tunnel name. (optional)
            interface: Name of the physical, aggregate, or VLAN interface. (optional)
            remote_gw: Peer gateway. (optional)
            local_gw: Local gateway. (optional)
            authentication: Authentication algorithm. Must be the same for both ends of the tunnel. (optional)
            encryption: Encryption algorithm. Must be the same for both ends of the tunnel. (optional)
            authkey: Hexadecimal authentication key in 16-digit (8-byte) segments separated by hyphens. (optional)
            enckey: Hexadecimal encryption key in 16-digit (8-byte) segments separated by hyphens. (optional)
            localspi: Local SPI, a hexadecimal 8-digit (4-byte) tag. Discerns between two traffic streams with different encryption rules. (optional)
            remotespi: Remote SPI, a hexadecimal 8-digit (4-byte) tag. Discerns between two traffic streams with different encryption rules. (optional)
            npu_offload: Enable/disable NPU offloading. (optional)
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
        endpoint = "/vpn.ipsec/manualkey"
        if nkey is not None:
            data_payload['nkey'] = nkey
        if name is not None:
            data_payload['name'] = name
        if interface is not None:
            data_payload['interface'] = interface
        if remote_gw is not None:
            data_payload['remote-gw'] = remote_gw
        if local_gw is not None:
            data_payload['local-gw'] = local_gw
        if authentication is not None:
            data_payload['authentication'] = authentication
        if encryption is not None:
            data_payload['encryption'] = encryption
        if authkey is not None:
            data_payload['authkey'] = authkey
        if enckey is not None:
            data_payload['enckey'] = enckey
        if localspi is not None:
            data_payload['localspi'] = localspi
        if remotespi is not None:
            data_payload['remotespi'] = remotespi
        if npu_offload is not None:
            data_payload['npu-offload'] = npu_offload
        data_payload.update(kwargs)
        return self._client.post("cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json)
