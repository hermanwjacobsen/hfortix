"""
FortiOS CMDB - Firewall MulticastPolicy6

API Endpoints:
    GET    /firewall/multicast-policy6
    POST   /firewall/multicast-policy6
    GET    /firewall/multicast-policy6/{id}
    PUT    /firewall/multicast-policy6/{id}
    DELETE /firewall/multicast-policy6/{id}
"""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from ....http_client import HTTPClient


class MulticastPolicy6:
    """MulticastPolicy6 operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize MulticastPolicy6 endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

    def get(
        self,
        id: str | None = None,
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
            id: Object identifier (optional for list, required for specific)
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
        if id:
            endpoint = f"/firewall/multicast-policy6/{id}"
        else:
            endpoint = "/firewall/multicast-policy6"
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
        id: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        before: str | None = None,
        after: str | None = None,
        uuid: str | None = None,
        status: str | None = None,
        name: str | None = None,
        srcintf: str | None = None,
        dstintf: str | None = None,
        srcaddr: list | None = None,
        dstaddr: list | None = None,
        protocol: int | None = None,
        start_port: int | None = None,
        end_port: int | None = None,
        utm_status: str | None = None,
        ips_sensor: str | None = None,
        logtraffic: str | None = None,
        auto_asic_offload: str | None = None,
        comments: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Update this specific resource.
        
        Args:
            payload_dict: Optional dictionary of all parameters (can be passed as first positional arg)
            id: Object identifier (required)
            before: If *action=move*, use *before* to specify the ID of the resource that this resource will be moved before. (optional)
            after: If *action=move*, use *after* to specify the ID of the resource that this resource will be moved after. (optional)
            id: Policy ID (0 - 4294967294). (optional)
            uuid: Universally Unique Identifier (UUID; automatically assigned but can be manually reset). (optional)
            status: Enable/disable this policy. (optional)
            name: Policy name. (optional)
            srcintf: IPv6 source interface name. (optional)
            dstintf: IPv6 destination interface name. (optional)
            srcaddr: IPv6 source address name. (optional)
            dstaddr: IPv6 destination address name. (optional)
            protocol: Integer value for the protocol type as defined by IANA (0 - 255, default = 0). (optional)
            start_port: Integer value for starting TCP/UDP/SCTP destination port in range (1 - 65535, default = 1). (optional)
            end_port: Integer value for ending TCP/UDP/SCTP destination port in range (1 - 65535, default = 65535). (optional)
            utm_status: Enable to add an IPS security profile to the policy. (optional)
            ips_sensor: Name of an existing IPS sensor. (optional)
            logtraffic: Enable or disable logging. Log all sessions or security profile sessions. (optional)
            auto_asic_offload: Enable/disable offloading policy traffic for hardware acceleration. (optional)
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
        if not id:
            raise ValueError("id is required for put()")
        endpoint = f"/firewall/multicast-policy6/{id}"
        if before is not None:
            data_payload['before'] = before
        if after is not None:
            data_payload['after'] = after
        if id is not None:
            data_payload['id'] = id
        if uuid is not None:
            data_payload['uuid'] = uuid
        if status is not None:
            data_payload['status'] = status
        if name is not None:
            data_payload['name'] = name
        if srcintf is not None:
            data_payload['srcintf'] = srcintf
        if dstintf is not None:
            data_payload['dstintf'] = dstintf
        if srcaddr is not None:
            data_payload['srcaddr'] = srcaddr
        if dstaddr is not None:
            data_payload['dstaddr'] = dstaddr
        if protocol is not None:
            data_payload['protocol'] = protocol
        if start_port is not None:
            data_payload['start-port'] = start_port
        if end_port is not None:
            data_payload['end-port'] = end_port
        if utm_status is not None:
            data_payload['utm-status'] = utm_status
        if ips_sensor is not None:
            data_payload['ips-sensor'] = ips_sensor
        if logtraffic is not None:
            data_payload['logtraffic'] = logtraffic
        if auto_asic_offload is not None:
            data_payload['auto-asic-offload'] = auto_asic_offload
        if comments is not None:
            data_payload['comments'] = comments
        data_payload.update(kwargs)
        return self._client.put("cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json)

    def delete(
        self,
        id: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Delete this specific resource.
        
        Args:
            id: Object identifier (required)
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
        if not id:
            raise ValueError("id is required for delete()")
        endpoint = f"/firewall/multicast-policy6/{id}"
        params.update(kwargs)
        return self._client.delete("cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json)

    def post(
        self,
        payload_dict: dict[str, Any] | None = None,
        nkey: str | None = None,
        id: int | None = None,
        uuid: str | None = None,
        status: str | None = None,
        name: str | None = None,
        srcintf: str | None = None,
        dstintf: str | None = None,
        srcaddr: list | None = None,
        dstaddr: list | None = None,
        protocol: int | None = None,
        start_port: int | None = None,
        end_port: int | None = None,
        utm_status: str | None = None,
        ips_sensor: str | None = None,
        logtraffic: str | None = None,
        auto_asic_offload: str | None = None,
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
            id: Policy ID (0 - 4294967294). (optional)
            uuid: Universally Unique Identifier (UUID; automatically assigned but can be manually reset). (optional)
            status: Enable/disable this policy. (optional)
            name: Policy name. (optional)
            srcintf: IPv6 source interface name. (optional)
            dstintf: IPv6 destination interface name. (optional)
            srcaddr: IPv6 source address name. (optional)
            dstaddr: IPv6 destination address name. (optional)
            protocol: Integer value for the protocol type as defined by IANA (0 - 255, default = 0). (optional)
            start_port: Integer value for starting TCP/UDP/SCTP destination port in range (1 - 65535, default = 1). (optional)
            end_port: Integer value for ending TCP/UDP/SCTP destination port in range (1 - 65535, default = 65535). (optional)
            utm_status: Enable to add an IPS security profile to the policy. (optional)
            ips_sensor: Name of an existing IPS sensor. (optional)
            logtraffic: Enable or disable logging. Log all sessions or security profile sessions. (optional)
            auto_asic_offload: Enable/disable offloading policy traffic for hardware acceleration. (optional)
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
        endpoint = "/firewall/multicast-policy6"
        if nkey is not None:
            data_payload['nkey'] = nkey
        if id is not None:
            data_payload['id'] = id
        if uuid is not None:
            data_payload['uuid'] = uuid
        if status is not None:
            data_payload['status'] = status
        if name is not None:
            data_payload['name'] = name
        if srcintf is not None:
            data_payload['srcintf'] = srcintf
        if dstintf is not None:
            data_payload['dstintf'] = dstintf
        if srcaddr is not None:
            data_payload['srcaddr'] = srcaddr
        if dstaddr is not None:
            data_payload['dstaddr'] = dstaddr
        if protocol is not None:
            data_payload['protocol'] = protocol
        if start_port is not None:
            data_payload['start-port'] = start_port
        if end_port is not None:
            data_payload['end-port'] = end_port
        if utm_status is not None:
            data_payload['utm-status'] = utm_status
        if ips_sensor is not None:
            data_payload['ips-sensor'] = ips_sensor
        if logtraffic is not None:
            data_payload['logtraffic'] = logtraffic
        if auto_asic_offload is not None:
            data_payload['auto-asic-offload'] = auto_asic_offload
        if comments is not None:
            data_payload['comments'] = comments
        data_payload.update(kwargs)
        return self._client.post("cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json)
