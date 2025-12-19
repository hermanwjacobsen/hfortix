"""
FortiOS CMDB - Router Static6

API Endpoints:
    GET    /router/static6
    POST   /router/static6
    GET    /router/static6/{seq-num}
    PUT    /router/static6/{seq-num}
    DELETE /router/static6/{seq-num}
"""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from ....http_client import HTTPClient


class Static6:
    """Static6 operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize Static6 endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

    def get(
        self,
        seq_num: str | None = None,
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
            seq_num: Object identifier (optional for list, required for specific)
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
        if seq_num:
            endpoint = f"/router/static6/{seq_num}"
        else:
            endpoint = "/router/static6"
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
        seq_num: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        before: str | None = None,
        after: str | None = None,
        status: str | None = None,
        dst: str | None = None,
        gateway: str | None = None,
        device: str | None = None,
        devindex: int | None = None,
        distance: int | None = None,
        weight: int | None = None,
        priority: int | None = None,
        comment: str | None = None,
        blackhole: str | None = None,
        dynamic_gateway: str | None = None,
        sdwan_zone: list | None = None,
        dstaddr: str | None = None,
        link_monitor_exempt: str | None = None,
        vrf: int | None = None,
        bfd: str | None = None,
        tag: int | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Update this specific resource.
        
        Args:
            payload_dict: Optional dictionary of all parameters (can be passed as first positional arg)
            seq_num: Object identifier (required)
            before: If *action=move*, use *before* to specify the ID of the resource that this resource will be moved before. (optional)
            after: If *action=move*, use *after* to specify the ID of the resource that this resource will be moved after. (optional)
            seq_num: Sequence number. (optional)
            status: Enable/disable this static route. (optional)
            dst: Destination IPv6 prefix. (optional)
            gateway: IPv6 address of the gateway. (optional)
            device: Gateway out interface or tunnel. (optional)
            devindex: Device index (0 - 4294967295). (optional)
            distance: Administrative distance (1 - 255). (optional)
            weight: Administrative weight (0 - 255). (optional)
            priority: Administrative priority (1 - 65535). (optional)
            comment: Optional comments. (optional)
            blackhole: Enable/disable black hole. (optional)
            dynamic_gateway: Enable use of dynamic gateway retrieved from Router Advertisement (RA). (optional)
            sdwan_zone: Choose SD-WAN Zone. (optional)
            dstaddr: Name of firewall address or address group. (optional)
            link_monitor_exempt: Enable/disable withdrawal of this static route when link monitor or health check is down. (optional)
            vrf: Virtual Routing Forwarding ID. (optional)
            bfd: Enable/disable Bidirectional Forwarding Detection (BFD). (optional)
            tag: Route tag. (optional)
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
        if not seq_num:
            raise ValueError("seq_num is required for put()")
        endpoint = f"/router/static6/{seq_num}"
        if before is not None:
            data_payload['before'] = before
        if after is not None:
            data_payload['after'] = after
        if seq_num is not None:
            data_payload['seq-num'] = seq_num
        if status is not None:
            data_payload['status'] = status
        if dst is not None:
            data_payload['dst'] = dst
        if gateway is not None:
            data_payload['gateway'] = gateway
        if device is not None:
            data_payload['device'] = device
        if devindex is not None:
            data_payload['devindex'] = devindex
        if distance is not None:
            data_payload['distance'] = distance
        if weight is not None:
            data_payload['weight'] = weight
        if priority is not None:
            data_payload['priority'] = priority
        if comment is not None:
            data_payload['comment'] = comment
        if blackhole is not None:
            data_payload['blackhole'] = blackhole
        if dynamic_gateway is not None:
            data_payload['dynamic-gateway'] = dynamic_gateway
        if sdwan_zone is not None:
            data_payload['sdwan-zone'] = sdwan_zone
        if dstaddr is not None:
            data_payload['dstaddr'] = dstaddr
        if link_monitor_exempt is not None:
            data_payload['link-monitor-exempt'] = link_monitor_exempt
        if vrf is not None:
            data_payload['vrf'] = vrf
        if bfd is not None:
            data_payload['bfd'] = bfd
        if tag is not None:
            data_payload['tag'] = tag
        data_payload.update(kwargs)
        return self._client.put("cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json)

    def delete(
        self,
        seq_num: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Delete this specific resource.
        
        Args:
            seq_num: Object identifier (required)
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
        if not seq_num:
            raise ValueError("seq_num is required for delete()")
        endpoint = f"/router/static6/{seq_num}"
        params.update(kwargs)
        return self._client.delete("cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json)

    def post(
        self,
        payload_dict: dict[str, Any] | None = None,
        nkey: str | None = None,
        seq_num: int | None = None,
        status: str | None = None,
        dst: str | None = None,
        gateway: str | None = None,
        device: str | None = None,
        devindex: int | None = None,
        distance: int | None = None,
        weight: int | None = None,
        priority: int | None = None,
        comment: str | None = None,
        blackhole: str | None = None,
        dynamic_gateway: str | None = None,
        sdwan_zone: list | None = None,
        dstaddr: str | None = None,
        link_monitor_exempt: str | None = None,
        vrf: int | None = None,
        bfd: str | None = None,
        tag: int | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Create object(s) in this table.
        
        Args:
            payload_dict: Optional dictionary of all parameters (can be passed as first positional arg)
            nkey: If *action=clone*, use *nkey* to specify the ID for the new resource to be created. (optional)
            seq_num: Sequence number. (optional)
            status: Enable/disable this static route. (optional)
            dst: Destination IPv6 prefix. (optional)
            gateway: IPv6 address of the gateway. (optional)
            device: Gateway out interface or tunnel. (optional)
            devindex: Device index (0 - 4294967295). (optional)
            distance: Administrative distance (1 - 255). (optional)
            weight: Administrative weight (0 - 255). (optional)
            priority: Administrative priority (1 - 65535). (optional)
            comment: Optional comments. (optional)
            blackhole: Enable/disable black hole. (optional)
            dynamic_gateway: Enable use of dynamic gateway retrieved from Router Advertisement (RA). (optional)
            sdwan_zone: Choose SD-WAN Zone. (optional)
            dstaddr: Name of firewall address or address group. (optional)
            link_monitor_exempt: Enable/disable withdrawal of this static route when link monitor or health check is down. (optional)
            vrf: Virtual Routing Forwarding ID. (optional)
            bfd: Enable/disable Bidirectional Forwarding Detection (BFD). (optional)
            tag: Route tag. (optional)
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
        endpoint = "/router/static6"
        if nkey is not None:
            data_payload['nkey'] = nkey
        if seq_num is not None:
            data_payload['seq-num'] = seq_num
        if status is not None:
            data_payload['status'] = status
        if dst is not None:
            data_payload['dst'] = dst
        if gateway is not None:
            data_payload['gateway'] = gateway
        if device is not None:
            data_payload['device'] = device
        if devindex is not None:
            data_payload['devindex'] = devindex
        if distance is not None:
            data_payload['distance'] = distance
        if weight is not None:
            data_payload['weight'] = weight
        if priority is not None:
            data_payload['priority'] = priority
        if comment is not None:
            data_payload['comment'] = comment
        if blackhole is not None:
            data_payload['blackhole'] = blackhole
        if dynamic_gateway is not None:
            data_payload['dynamic-gateway'] = dynamic_gateway
        if sdwan_zone is not None:
            data_payload['sdwan-zone'] = sdwan_zone
        if dstaddr is not None:
            data_payload['dstaddr'] = dstaddr
        if link_monitor_exempt is not None:
            data_payload['link-monitor-exempt'] = link_monitor_exempt
        if vrf is not None:
            data_payload['vrf'] = vrf
        if bfd is not None:
            data_payload['bfd'] = bfd
        if tag is not None:
            data_payload['tag'] = tag
        data_payload.update(kwargs)
        return self._client.post("cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json)
