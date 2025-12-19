"""
FortiOS CMDB - System Vxlan

API Endpoints:
    GET    /system/vxlan
    POST   /system/vxlan
    GET    /system/vxlan/{name}
    PUT    /system/vxlan/{name}
    DELETE /system/vxlan/{name}
"""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from ....http_client import HTTPClient


class Vxlan:
    """Vxlan operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize Vxlan endpoint.

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
            endpoint = f"/system/vxlan/{name}"
        else:
            endpoint = "/system/vxlan"
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
        vni: int | None = None,
        ip_version: str | None = None,
        remote_ip: list | None = None,
        local_ip: str | None = None,
        remote_ip6: list | None = None,
        local_ip6: str | None = None,
        dstport: int | None = None,
        multicast_ttl: int | None = None,
        evpn_id: int | None = None,
        learn_from_traffic: str | None = None,
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
            name: VXLAN device or interface name. Must be a unique interface name. (optional)
            interface: Outgoing interface for VXLAN encapsulated traffic. (optional)
            vni: VXLAN network ID. (optional)
            ip_version: IP version to use for the VXLAN interface and so for communication over the VXLAN. IPv4 or IPv6 unicast or multicast. (optional)
            remote_ip: IPv4 address of the VXLAN interface on the device at the remote end of the VXLAN. (optional)
            local_ip: IPv4 address to use as the source address for egress VXLAN packets. (optional)
            remote_ip6: IPv6 IP address of the VXLAN interface on the device at the remote end of the VXLAN. (optional)
            local_ip6: IPv6 address to use as the source address for egress VXLAN packets. (optional)
            dstport: VXLAN destination port (1 - 65535, default = 4789). (optional)
            multicast_ttl: VXLAN multicast TTL (1-255, default = 0). (optional)
            evpn_id: EVPN instance. (optional)
            learn_from_traffic: Enable/disable VXLAN MAC learning from traffic. (optional)
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
        endpoint = f"/system/vxlan/{name}"
        if before is not None:
            data_payload['before'] = before
        if after is not None:
            data_payload['after'] = after
        if name is not None:
            data_payload['name'] = name
        if interface is not None:
            data_payload['interface'] = interface
        if vni is not None:
            data_payload['vni'] = vni
        if ip_version is not None:
            data_payload['ip-version'] = ip_version
        if remote_ip is not None:
            data_payload['remote-ip'] = remote_ip
        if local_ip is not None:
            data_payload['local-ip'] = local_ip
        if remote_ip6 is not None:
            data_payload['remote-ip6'] = remote_ip6
        if local_ip6 is not None:
            data_payload['local-ip6'] = local_ip6
        if dstport is not None:
            data_payload['dstport'] = dstport
        if multicast_ttl is not None:
            data_payload['multicast-ttl'] = multicast_ttl
        if evpn_id is not None:
            data_payload['evpn-id'] = evpn_id
        if learn_from_traffic is not None:
            data_payload['learn-from-traffic'] = learn_from_traffic
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
        endpoint = f"/system/vxlan/{name}"
        params.update(kwargs)
        return self._client.delete("cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json)

    def post(
        self,
        payload_dict: dict[str, Any] | None = None,
        nkey: str | None = None,
        name: str | None = None,
        interface: str | None = None,
        vni: int | None = None,
        ip_version: str | None = None,
        remote_ip: list | None = None,
        local_ip: str | None = None,
        remote_ip6: list | None = None,
        local_ip6: str | None = None,
        dstport: int | None = None,
        multicast_ttl: int | None = None,
        evpn_id: int | None = None,
        learn_from_traffic: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Create object(s) in this table.
        
        Args:
            payload_dict: Optional dictionary of all parameters (can be passed as first positional arg)
            nkey: If *action=clone*, use *nkey* to specify the ID for the new resource to be created. (optional)
            name: VXLAN device or interface name. Must be a unique interface name. (optional)
            interface: Outgoing interface for VXLAN encapsulated traffic. (optional)
            vni: VXLAN network ID. (optional)
            ip_version: IP version to use for the VXLAN interface and so for communication over the VXLAN. IPv4 or IPv6 unicast or multicast. (optional)
            remote_ip: IPv4 address of the VXLAN interface on the device at the remote end of the VXLAN. (optional)
            local_ip: IPv4 address to use as the source address for egress VXLAN packets. (optional)
            remote_ip6: IPv6 IP address of the VXLAN interface on the device at the remote end of the VXLAN. (optional)
            local_ip6: IPv6 address to use as the source address for egress VXLAN packets. (optional)
            dstport: VXLAN destination port (1 - 65535, default = 4789). (optional)
            multicast_ttl: VXLAN multicast TTL (1-255, default = 0). (optional)
            evpn_id: EVPN instance. (optional)
            learn_from_traffic: Enable/disable VXLAN MAC learning from traffic. (optional)
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
        endpoint = "/system/vxlan"
        if nkey is not None:
            data_payload['nkey'] = nkey
        if name is not None:
            data_payload['name'] = name
        if interface is not None:
            data_payload['interface'] = interface
        if vni is not None:
            data_payload['vni'] = vni
        if ip_version is not None:
            data_payload['ip-version'] = ip_version
        if remote_ip is not None:
            data_payload['remote-ip'] = remote_ip
        if local_ip is not None:
            data_payload['local-ip'] = local_ip
        if remote_ip6 is not None:
            data_payload['remote-ip6'] = remote_ip6
        if local_ip6 is not None:
            data_payload['local-ip6'] = local_ip6
        if dstport is not None:
            data_payload['dstport'] = dstport
        if multicast_ttl is not None:
            data_payload['multicast-ttl'] = multicast_ttl
        if evpn_id is not None:
            data_payload['evpn-id'] = evpn_id
        if learn_from_traffic is not None:
            data_payload['learn-from-traffic'] = learn_from_traffic
        data_payload.update(kwargs)
        return self._client.post("cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json)
