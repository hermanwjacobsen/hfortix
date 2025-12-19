"""
FortiOS CMDB - Firewall CentralSnatMap

API Endpoints:
    GET    /firewall/central-snat-map
    POST   /firewall/central-snat-map
    GET    /firewall/central-snat-map/{policyid}
    PUT    /firewall/central-snat-map/{policyid}
    DELETE /firewall/central-snat-map/{policyid}
"""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from ....http_client import HTTPClient


class CentralSnatMap:
    """CentralSnatMap operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize CentralSnatMap endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

    def get(
        self,
        policyid: str | None = None,
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
            policyid: Object identifier (optional for list, required for specific)
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
        if policyid:
            endpoint = f"/firewall/central-snat-map/{policyid}"
        else:
            endpoint = "/firewall/central-snat-map"
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
        policyid: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        before: str | None = None,
        after: str | None = None,
        uuid: str | None = None,
        status: str | None = None,
        type: str | None = None,
        srcintf: list | None = None,
        dstintf: list | None = None,
        orig_addr: list | None = None,
        orig_addr6: list | None = None,
        dst_addr: list | None = None,
        dst_addr6: list | None = None,
        protocol: int | None = None,
        orig_port: str | None = None,
        nat: str | None = None,
        nat46: str | None = None,
        nat64: str | None = None,
        nat_ippool: list | None = None,
        nat_ippool6: list | None = None,
        port_preserve: str | None = None,
        port_random: str | None = None,
        nat_port: str | None = None,
        dst_port: str | None = None,
        comments: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Update this specific resource.
        
        Args:
            payload_dict: Optional dictionary of all parameters (can be passed as first positional arg)
            policyid: Object identifier (required)
            before: If *action=move*, use *before* to specify the ID of the resource that this resource will be moved before. (optional)
            after: If *action=move*, use *after* to specify the ID of the resource that this resource will be moved after. (optional)
            policyid: Policy ID. (optional)
            uuid: Universally Unique Identifier (UUID; automatically assigned but can be manually reset). (optional)
            status: Enable/disable the active status of this policy. (optional)
            type: IPv4/IPv6 source NAT. (optional)
            srcintf: Source interface name from available interfaces. (optional)
            dstintf: Destination interface name from available interfaces. (optional)
            orig_addr: IPv4 Original address. (optional)
            orig_addr6: IPv6 Original address. (optional)
            dst_addr: IPv4 Destination address. (optional)
            dst_addr6: IPv6 Destination address. (optional)
            protocol: Integer value for the protocol type (0 - 255). (optional)
            orig_port: Original TCP port (1 to 65535, 0 means any port). (optional)
            nat: Enable/disable source NAT. (optional)
            nat46: Enable/disable NAT46. (optional)
            nat64: Enable/disable NAT64. (optional)
            nat_ippool: Name of the IP pools to be used to translate addresses from available IP Pools. (optional)
            nat_ippool6: IPv6 pools to be used for source NAT. (optional)
            port_preserve: Enable/disable preservation of the original source port from source NAT if it has not been used. (optional)
            port_random: Enable/disable random source port selection for source NAT. (optional)
            nat_port: Translated port or port range (1 to 65535, 0 means any port). (optional)
            dst_port: Destination port or port range (1 to 65535, 0 means any port). (optional)
            comments: Comment. (optional)
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
        if not policyid:
            raise ValueError("policyid is required for put()")
        endpoint = f"/firewall/central-snat-map/{policyid}"
        if before is not None:
            data_payload['before'] = before
        if after is not None:
            data_payload['after'] = after
        if policyid is not None:
            data_payload['policyid'] = policyid
        if uuid is not None:
            data_payload['uuid'] = uuid
        if status is not None:
            data_payload['status'] = status
        if type is not None:
            data_payload['type'] = type
        if srcintf is not None:
            data_payload['srcintf'] = srcintf
        if dstintf is not None:
            data_payload['dstintf'] = dstintf
        if orig_addr is not None:
            data_payload['orig-addr'] = orig_addr
        if orig_addr6 is not None:
            data_payload['orig-addr6'] = orig_addr6
        if dst_addr is not None:
            data_payload['dst-addr'] = dst_addr
        if dst_addr6 is not None:
            data_payload['dst-addr6'] = dst_addr6
        if protocol is not None:
            data_payload['protocol'] = protocol
        if orig_port is not None:
            data_payload['orig-port'] = orig_port
        if nat is not None:
            data_payload['nat'] = nat
        if nat46 is not None:
            data_payload['nat46'] = nat46
        if nat64 is not None:
            data_payload['nat64'] = nat64
        if nat_ippool is not None:
            data_payload['nat-ippool'] = nat_ippool
        if nat_ippool6 is not None:
            data_payload['nat-ippool6'] = nat_ippool6
        if port_preserve is not None:
            data_payload['port-preserve'] = port_preserve
        if port_random is not None:
            data_payload['port-random'] = port_random
        if nat_port is not None:
            data_payload['nat-port'] = nat_port
        if dst_port is not None:
            data_payload['dst-port'] = dst_port
        if comments is not None:
            data_payload['comments'] = comments
        data_payload.update(kwargs)
        return self._client.put("cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json)

    def delete(
        self,
        policyid: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Delete this specific resource.
        
        Args:
            policyid: Object identifier (required)
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
        if not policyid:
            raise ValueError("policyid is required for delete()")
        endpoint = f"/firewall/central-snat-map/{policyid}"
        params.update(kwargs)
        return self._client.delete("cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json)

    def post(
        self,
        payload_dict: dict[str, Any] | None = None,
        nkey: str | None = None,
        policyid: int | None = None,
        uuid: str | None = None,
        status: str | None = None,
        type: str | None = None,
        srcintf: list | None = None,
        dstintf: list | None = None,
        orig_addr: list | None = None,
        orig_addr6: list | None = None,
        dst_addr: list | None = None,
        dst_addr6: list | None = None,
        protocol: int | None = None,
        orig_port: str | None = None,
        nat: str | None = None,
        nat46: str | None = None,
        nat64: str | None = None,
        nat_ippool: list | None = None,
        nat_ippool6: list | None = None,
        port_preserve: str | None = None,
        port_random: str | None = None,
        nat_port: str | None = None,
        dst_port: str | None = None,
        comments: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Create object(s) in this table.
        
        Args:
            payload_dict: Optional dictionary of all parameters (can be passed as first positional arg)
            nkey: If *action=clone*, use *nkey* to specify the ID for the new resource to be created. (optional)
            policyid: Policy ID. (optional)
            uuid: Universally Unique Identifier (UUID; automatically assigned but can be manually reset). (optional)
            status: Enable/disable the active status of this policy. (optional)
            type: IPv4/IPv6 source NAT. (optional)
            srcintf: Source interface name from available interfaces. (optional)
            dstintf: Destination interface name from available interfaces. (optional)
            orig_addr: IPv4 Original address. (optional)
            orig_addr6: IPv6 Original address. (optional)
            dst_addr: IPv4 Destination address. (optional)
            dst_addr6: IPv6 Destination address. (optional)
            protocol: Integer value for the protocol type (0 - 255). (optional)
            orig_port: Original TCP port (1 to 65535, 0 means any port). (optional)
            nat: Enable/disable source NAT. (optional)
            nat46: Enable/disable NAT46. (optional)
            nat64: Enable/disable NAT64. (optional)
            nat_ippool: Name of the IP pools to be used to translate addresses from available IP Pools. (optional)
            nat_ippool6: IPv6 pools to be used for source NAT. (optional)
            port_preserve: Enable/disable preservation of the original source port from source NAT if it has not been used. (optional)
            port_random: Enable/disable random source port selection for source NAT. (optional)
            nat_port: Translated port or port range (1 to 65535, 0 means any port). (optional)
            dst_port: Destination port or port range (1 to 65535, 0 means any port). (optional)
            comments: Comment. (optional)
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
        endpoint = "/firewall/central-snat-map"
        if nkey is not None:
            data_payload['nkey'] = nkey
        if policyid is not None:
            data_payload['policyid'] = policyid
        if uuid is not None:
            data_payload['uuid'] = uuid
        if status is not None:
            data_payload['status'] = status
        if type is not None:
            data_payload['type'] = type
        if srcintf is not None:
            data_payload['srcintf'] = srcintf
        if dstintf is not None:
            data_payload['dstintf'] = dstintf
        if orig_addr is not None:
            data_payload['orig-addr'] = orig_addr
        if orig_addr6 is not None:
            data_payload['orig-addr6'] = orig_addr6
        if dst_addr is not None:
            data_payload['dst-addr'] = dst_addr
        if dst_addr6 is not None:
            data_payload['dst-addr6'] = dst_addr6
        if protocol is not None:
            data_payload['protocol'] = protocol
        if orig_port is not None:
            data_payload['orig-port'] = orig_port
        if nat is not None:
            data_payload['nat'] = nat
        if nat46 is not None:
            data_payload['nat46'] = nat46
        if nat64 is not None:
            data_payload['nat64'] = nat64
        if nat_ippool is not None:
            data_payload['nat-ippool'] = nat_ippool
        if nat_ippool6 is not None:
            data_payload['nat-ippool6'] = nat_ippool6
        if port_preserve is not None:
            data_payload['port-preserve'] = port_preserve
        if port_random is not None:
            data_payload['port-random'] = port_random
        if nat_port is not None:
            data_payload['nat-port'] = nat_port
        if dst_port is not None:
            data_payload['dst-port'] = dst_port
        if comments is not None:
            data_payload['comments'] = comments
        data_payload.update(kwargs)
        return self._client.post("cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json)
