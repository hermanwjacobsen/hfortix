"""
FortiOS CMDB - Firewall ShaperPerIpShaper

API Endpoints:
    GET    /firewall.shaper/per-ip-shaper
    POST   /firewall.shaper/per-ip-shaper
    GET    /firewall.shaper/per-ip-shaper/{name}
    PUT    /firewall.shaper/per-ip-shaper/{name}
    DELETE /firewall.shaper/per-ip-shaper/{name}
"""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from ....http_client import HTTPClient


class ShaperPerIpShaper:
    """ShaperPerIpShaper operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize ShaperPerIpShaper endpoint.

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
            endpoint = f"/firewall.shaper/per-ip-shaper/{name}"
        else:
            endpoint = "/firewall.shaper/per-ip-shaper"
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
        max_bandwidth: int | None = None,
        bandwidth_unit: str | None = None,
        max_concurrent_session: int | None = None,
        max_concurrent_tcp_session: int | None = None,
        max_concurrent_udp_session: int | None = None,
        diffserv_forward: str | None = None,
        diffserv_reverse: str | None = None,
        diffservcode_forward: str | None = None,
        diffservcode_rev: str | None = None,
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
            name: Traffic shaper name. (optional)
            max_bandwidth: Upper bandwidth limit enforced by this shaper (0 - 80000000). 0 means no limit. Units depend on the bandwidth-unit setting. (optional)
            bandwidth_unit: Unit of measurement for maximum bandwidth for this shaper (Kbps, Mbps or Gbps). (optional)
            max_concurrent_session: Maximum number of concurrent sessions allowed by this shaper (0 - 2097000). 0 means no limit. (optional)
            max_concurrent_tcp_session: Maximum number of concurrent TCP sessions allowed by this shaper (0 - 2097000). 0 means no limit. (optional)
            max_concurrent_udp_session: Maximum number of concurrent UDP sessions allowed by this shaper (0 - 2097000). 0 means no limit. (optional)
            diffserv_forward: Enable/disable changing the Forward (original) DiffServ setting applied to traffic accepted by this shaper. (optional)
            diffserv_reverse: Enable/disable changing the Reverse (reply) DiffServ setting applied to traffic accepted by this shaper. (optional)
            diffservcode_forward: Forward (original) DiffServ setting to be applied to traffic accepted by this shaper. (optional)
            diffservcode_rev: Reverse (reply) DiffServ setting to be applied to traffic accepted by this shaper. (optional)
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
        endpoint = f"/firewall.shaper/per-ip-shaper/{name}"
        if before is not None:
            data_payload['before'] = before
        if after is not None:
            data_payload['after'] = after
        if name is not None:
            data_payload['name'] = name
        if max_bandwidth is not None:
            data_payload['max-bandwidth'] = max_bandwidth
        if bandwidth_unit is not None:
            data_payload['bandwidth-unit'] = bandwidth_unit
        if max_concurrent_session is not None:
            data_payload['max-concurrent-session'] = max_concurrent_session
        if max_concurrent_tcp_session is not None:
            data_payload['max-concurrent-tcp-session'] = max_concurrent_tcp_session
        if max_concurrent_udp_session is not None:
            data_payload['max-concurrent-udp-session'] = max_concurrent_udp_session
        if diffserv_forward is not None:
            data_payload['diffserv-forward'] = diffserv_forward
        if diffserv_reverse is not None:
            data_payload['diffserv-reverse'] = diffserv_reverse
        if diffservcode_forward is not None:
            data_payload['diffservcode-forward'] = diffservcode_forward
        if diffservcode_rev is not None:
            data_payload['diffservcode-rev'] = diffservcode_rev
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
        endpoint = f"/firewall.shaper/per-ip-shaper/{name}"
        params.update(kwargs)
        return self._client.delete("cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json)

    def post(
        self,
        payload_dict: dict[str, Any] | None = None,
        nkey: str | None = None,
        name: str | None = None,
        max_bandwidth: int | None = None,
        bandwidth_unit: str | None = None,
        max_concurrent_session: int | None = None,
        max_concurrent_tcp_session: int | None = None,
        max_concurrent_udp_session: int | None = None,
        diffserv_forward: str | None = None,
        diffserv_reverse: str | None = None,
        diffservcode_forward: str | None = None,
        diffservcode_rev: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Create object(s) in this table.
        
        Args:
            payload_dict: Optional dictionary of all parameters (can be passed as first positional arg)
            nkey: If *action=clone*, use *nkey* to specify the ID for the new resource to be created. (optional)
            name: Traffic shaper name. (optional)
            max_bandwidth: Upper bandwidth limit enforced by this shaper (0 - 80000000). 0 means no limit. Units depend on the bandwidth-unit setting. (optional)
            bandwidth_unit: Unit of measurement for maximum bandwidth for this shaper (Kbps, Mbps or Gbps). (optional)
            max_concurrent_session: Maximum number of concurrent sessions allowed by this shaper (0 - 2097000). 0 means no limit. (optional)
            max_concurrent_tcp_session: Maximum number of concurrent TCP sessions allowed by this shaper (0 - 2097000). 0 means no limit. (optional)
            max_concurrent_udp_session: Maximum number of concurrent UDP sessions allowed by this shaper (0 - 2097000). 0 means no limit. (optional)
            diffserv_forward: Enable/disable changing the Forward (original) DiffServ setting applied to traffic accepted by this shaper. (optional)
            diffserv_reverse: Enable/disable changing the Reverse (reply) DiffServ setting applied to traffic accepted by this shaper. (optional)
            diffservcode_forward: Forward (original) DiffServ setting to be applied to traffic accepted by this shaper. (optional)
            diffservcode_rev: Reverse (reply) DiffServ setting to be applied to traffic accepted by this shaper. (optional)
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
        endpoint = "/firewall.shaper/per-ip-shaper"
        if nkey is not None:
            data_payload['nkey'] = nkey
        if name is not None:
            data_payload['name'] = name
        if max_bandwidth is not None:
            data_payload['max-bandwidth'] = max_bandwidth
        if bandwidth_unit is not None:
            data_payload['bandwidth-unit'] = bandwidth_unit
        if max_concurrent_session is not None:
            data_payload['max-concurrent-session'] = max_concurrent_session
        if max_concurrent_tcp_session is not None:
            data_payload['max-concurrent-tcp-session'] = max_concurrent_tcp_session
        if max_concurrent_udp_session is not None:
            data_payload['max-concurrent-udp-session'] = max_concurrent_udp_session
        if diffserv_forward is not None:
            data_payload['diffserv-forward'] = diffserv_forward
        if diffserv_reverse is not None:
            data_payload['diffserv-reverse'] = diffserv_reverse
        if diffservcode_forward is not None:
            data_payload['diffservcode-forward'] = diffservcode_forward
        if diffservcode_rev is not None:
            data_payload['diffservcode-rev'] = diffservcode_rev
        data_payload.update(kwargs)
        return self._client.post("cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json)
