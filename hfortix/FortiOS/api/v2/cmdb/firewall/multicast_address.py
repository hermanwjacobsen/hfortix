"""
FortiOS CMDB - Firewall MulticastAddress

API Endpoints:
    GET    /firewall/multicast-address
    POST   /firewall/multicast-address
    GET    /firewall/multicast-address/{name}
    PUT    /firewall/multicast-address/{name}
    DELETE /firewall/multicast-address/{name}
"""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from ....http_client import HTTPClient


class MulticastAddress:
    """MulticastAddress operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize MulticastAddress endpoint.

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
            endpoint = f"/firewall/multicast-address/{name}"
        else:
            endpoint = "/firewall/multicast-address"
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
        type: str | None = None,
        subnet: str | None = None,
        start_ip: str | None = None,
        end_ip: str | None = None,
        comment: str | None = None,
        associated_interface: str | None = None,
        color: int | None = None,
        tagging: list | None = None,
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
            name: Multicast address name. (optional)
            type: Type of address object: multicast IP address range or broadcast IP/mask to be treated as a multicast address. (optional)
            subnet: Broadcast address and subnet. (optional)
            start_ip: First IPv4 address (inclusive) in the range for the address. (optional)
            end_ip: Final IPv4 address (inclusive) in the range for the address. (optional)
            comment: Comment. (optional)
            associated_interface: Interface associated with the address object. When setting up a policy, only addresses associated with this interface are available. (optional)
            color: Integer value to determine the color of the icon in the GUI (1 - 32, default = 0, which sets value to 1). (optional)
            tagging: Config object tagging. (optional)
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
        endpoint = f"/firewall/multicast-address/{name}"
        if before is not None:
            data_payload['before'] = before
        if after is not None:
            data_payload['after'] = after
        if name is not None:
            data_payload['name'] = name
        if type is not None:
            data_payload['type'] = type
        if subnet is not None:
            data_payload['subnet'] = subnet
        if start_ip is not None:
            data_payload['start-ip'] = start_ip
        if end_ip is not None:
            data_payload['end-ip'] = end_ip
        if comment is not None:
            data_payload['comment'] = comment
        if associated_interface is not None:
            data_payload['associated-interface'] = associated_interface
        if color is not None:
            data_payload['color'] = color
        if tagging is not None:
            data_payload['tagging'] = tagging
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
        endpoint = f"/firewall/multicast-address/{name}"
        params.update(kwargs)
        return self._client.delete("cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json)

    def post(
        self,
        payload_dict: dict[str, Any] | None = None,
        nkey: str | None = None,
        name: str | None = None,
        type: str | None = None,
        subnet: str | None = None,
        start_ip: str | None = None,
        end_ip: str | None = None,
        comment: str | None = None,
        associated_interface: str | None = None,
        color: int | None = None,
        tagging: list | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Create object(s) in this table.
        
        Args:
            payload_dict: Optional dictionary of all parameters (can be passed as first positional arg)
            nkey: If *action=clone*, use *nkey* to specify the ID for the new resource to be created. (optional)
            name: Multicast address name. (optional)
            type: Type of address object: multicast IP address range or broadcast IP/mask to be treated as a multicast address. (optional)
            subnet: Broadcast address and subnet. (optional)
            start_ip: First IPv4 address (inclusive) in the range for the address. (optional)
            end_ip: Final IPv4 address (inclusive) in the range for the address. (optional)
            comment: Comment. (optional)
            associated_interface: Interface associated with the address object. When setting up a policy, only addresses associated with this interface are available. (optional)
            color: Integer value to determine the color of the icon in the GUI (1 - 32, default = 0, which sets value to 1). (optional)
            tagging: Config object tagging. (optional)
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
        endpoint = "/firewall/multicast-address"
        if nkey is not None:
            data_payload['nkey'] = nkey
        if name is not None:
            data_payload['name'] = name
        if type is not None:
            data_payload['type'] = type
        if subnet is not None:
            data_payload['subnet'] = subnet
        if start_ip is not None:
            data_payload['start-ip'] = start_ip
        if end_ip is not None:
            data_payload['end-ip'] = end_ip
        if comment is not None:
            data_payload['comment'] = comment
        if associated_interface is not None:
            data_payload['associated-interface'] = associated_interface
        if color is not None:
            data_payload['color'] = color
        if tagging is not None:
            data_payload['tagging'] = tagging
        data_payload.update(kwargs)
        return self._client.post("cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json)
