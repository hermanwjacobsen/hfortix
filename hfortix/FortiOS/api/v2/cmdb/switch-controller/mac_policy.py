"""
FortiOS CMDB - Switch-controller MacPolicy

API Endpoints:
    GET    /switch-controller/mac-policy
    POST   /switch-controller/mac-policy
    GET    /switch-controller/mac-policy/{name}
    PUT    /switch-controller/mac-policy/{name}
    DELETE /switch-controller/mac-policy/{name}
"""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from ....http_client import HTTPClient


class MacPolicy:
    """MacPolicy operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize MacPolicy endpoint.

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
            endpoint = f"/switch-controller/mac-policy/{name}"
        else:
            endpoint = "/switch-controller/mac-policy"
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
        description: str | None = None,
        fortilink: str | None = None,
        vlan: str | None = None,
        traffic_policy: str | None = None,
        bounce_port_link: str | None = None,
        bounce_port_duration: int | None = None,
        poe_reset: str | None = None,
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
            name: MAC policy name. (optional)
            description: Description for the MAC policy. (optional)
            fortilink: FortiLink interface for which this MAC policy belongs to. (optional)
            vlan: Ingress traffic VLAN assignment for the MAC address matching this MAC policy. (optional)
            traffic_policy: Traffic policy to be applied when using this MAC policy. (optional)
            bounce_port_link: Enable/disable bouncing (administratively bring the link down, up) of a switch port where this mac-policy is applied. (optional)
            bounce_port_duration: Bounce duration in seconds of a switch port where this mac-policy is applied. (optional)
            poe_reset: Enable/disable POE reset of a switch port where this mac-policy is applied. (optional)
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
        endpoint = f"/switch-controller/mac-policy/{name}"
        if before is not None:
            data_payload['before'] = before
        if after is not None:
            data_payload['after'] = after
        if name is not None:
            data_payload['name'] = name
        if description is not None:
            data_payload['description'] = description
        if fortilink is not None:
            data_payload['fortilink'] = fortilink
        if vlan is not None:
            data_payload['vlan'] = vlan
        if traffic_policy is not None:
            data_payload['traffic-policy'] = traffic_policy
        if bounce_port_link is not None:
            data_payload['bounce-port-link'] = bounce_port_link
        if bounce_port_duration is not None:
            data_payload['bounce-port-duration'] = bounce_port_duration
        if poe_reset is not None:
            data_payload['poe-reset'] = poe_reset
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
        endpoint = f"/switch-controller/mac-policy/{name}"
        params.update(kwargs)
        return self._client.delete("cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json)

    def post(
        self,
        payload_dict: dict[str, Any] | None = None,
        nkey: str | None = None,
        name: str | None = None,
        description: str | None = None,
        fortilink: str | None = None,
        vlan: str | None = None,
        traffic_policy: str | None = None,
        bounce_port_link: str | None = None,
        bounce_port_duration: int | None = None,
        poe_reset: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Create object(s) in this table.
        
        Args:
            payload_dict: Optional dictionary of all parameters (can be passed as first positional arg)
            nkey: If *action=clone*, use *nkey* to specify the ID for the new resource to be created. (optional)
            name: MAC policy name. (optional)
            description: Description for the MAC policy. (optional)
            fortilink: FortiLink interface for which this MAC policy belongs to. (optional)
            vlan: Ingress traffic VLAN assignment for the MAC address matching this MAC policy. (optional)
            traffic_policy: Traffic policy to be applied when using this MAC policy. (optional)
            bounce_port_link: Enable/disable bouncing (administratively bring the link down, up) of a switch port where this mac-policy is applied. (optional)
            bounce_port_duration: Bounce duration in seconds of a switch port where this mac-policy is applied. (optional)
            poe_reset: Enable/disable POE reset of a switch port where this mac-policy is applied. (optional)
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
        endpoint = "/switch-controller/mac-policy"
        if nkey is not None:
            data_payload['nkey'] = nkey
        if name is not None:
            data_payload['name'] = name
        if description is not None:
            data_payload['description'] = description
        if fortilink is not None:
            data_payload['fortilink'] = fortilink
        if vlan is not None:
            data_payload['vlan'] = vlan
        if traffic_policy is not None:
            data_payload['traffic-policy'] = traffic_policy
        if bounce_port_link is not None:
            data_payload['bounce-port-link'] = bounce_port_link
        if bounce_port_duration is not None:
            data_payload['bounce-port-duration'] = bounce_port_duration
        if poe_reset is not None:
            data_payload['poe-reset'] = poe_reset
        data_payload.update(kwargs)
        return self._client.post("cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json)
