"""
FortiOS CMDB - Switch-controller TrafficPolicy

API Endpoints:
    GET    /switch-controller/traffic-policy
    POST   /switch-controller/traffic-policy
    GET    /switch-controller/traffic-policy/{name}
    PUT    /switch-controller/traffic-policy/{name}
    DELETE /switch-controller/traffic-policy/{name}
"""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from ....http_client import HTTPClient


class TrafficPolicy:
    """TrafficPolicy operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize TrafficPolicy endpoint.

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
            endpoint = f"/switch-controller/traffic-policy/{name}"
        else:
            endpoint = "/switch-controller/traffic-policy"
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
        policer_status: str | None = None,
        guaranteed_bandwidth: int | None = None,
        guaranteed_burst: int | None = None,
        maximum_burst: int | None = None,
        type: str | None = None,
        cos_queue: int | None = None,
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
            name: Traffic policy name. (optional)
            description: Description of the traffic policy. (optional)
            policer_status: Enable/disable policer config on the traffic policy. (optional)
            guaranteed_bandwidth: Guaranteed bandwidth in kbps (max value = 524287000). (optional)
            guaranteed_burst: Guaranteed burst size in bytes (max value = 4294967295). (optional)
            maximum_burst: Maximum burst size in bytes (max value = 4294967295). (optional)
            type: Configure type of policy(ingress/egress). (optional)
            cos_queue: COS queue(0 - 7), or unset to disable. (optional)
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
        endpoint = f"/switch-controller/traffic-policy/{name}"
        if before is not None:
            data_payload['before'] = before
        if after is not None:
            data_payload['after'] = after
        if name is not None:
            data_payload['name'] = name
        if description is not None:
            data_payload['description'] = description
        if policer_status is not None:
            data_payload['policer-status'] = policer_status
        if guaranteed_bandwidth is not None:
            data_payload['guaranteed-bandwidth'] = guaranteed_bandwidth
        if guaranteed_burst is not None:
            data_payload['guaranteed-burst'] = guaranteed_burst
        if maximum_burst is not None:
            data_payload['maximum-burst'] = maximum_burst
        if type is not None:
            data_payload['type'] = type
        if cos_queue is not None:
            data_payload['cos-queue'] = cos_queue
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
        endpoint = f"/switch-controller/traffic-policy/{name}"
        params.update(kwargs)
        return self._client.delete("cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json)

    def post(
        self,
        payload_dict: dict[str, Any] | None = None,
        nkey: str | None = None,
        name: str | None = None,
        description: str | None = None,
        policer_status: str | None = None,
        guaranteed_bandwidth: int | None = None,
        guaranteed_burst: int | None = None,
        maximum_burst: int | None = None,
        type: str | None = None,
        cos_queue: int | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Create object(s) in this table.
        
        Args:
            payload_dict: Optional dictionary of all parameters (can be passed as first positional arg)
            nkey: If *action=clone*, use *nkey* to specify the ID for the new resource to be created. (optional)
            name: Traffic policy name. (optional)
            description: Description of the traffic policy. (optional)
            policer_status: Enable/disable policer config on the traffic policy. (optional)
            guaranteed_bandwidth: Guaranteed bandwidth in kbps (max value = 524287000). (optional)
            guaranteed_burst: Guaranteed burst size in bytes (max value = 4294967295). (optional)
            maximum_burst: Maximum burst size in bytes (max value = 4294967295). (optional)
            type: Configure type of policy(ingress/egress). (optional)
            cos_queue: COS queue(0 - 7), or unset to disable. (optional)
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
        endpoint = "/switch-controller/traffic-policy"
        if nkey is not None:
            data_payload['nkey'] = nkey
        if name is not None:
            data_payload['name'] = name
        if description is not None:
            data_payload['description'] = description
        if policer_status is not None:
            data_payload['policer-status'] = policer_status
        if guaranteed_bandwidth is not None:
            data_payload['guaranteed-bandwidth'] = guaranteed_bandwidth
        if guaranteed_burst is not None:
            data_payload['guaranteed-burst'] = guaranteed_burst
        if maximum_burst is not None:
            data_payload['maximum-burst'] = maximum_burst
        if type is not None:
            data_payload['type'] = type
        if cos_queue is not None:
            data_payload['cos-queue'] = cos_queue
        data_payload.update(kwargs)
        return self._client.post("cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json)
