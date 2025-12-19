"""
FortiOS CMDB - Firewall DosPolicy6

API Endpoints:
    GET    /firewall/DoS-policy6
    POST   /firewall/DoS-policy6
    GET    /firewall/DoS-policy6/{policyid}
    PUT    /firewall/DoS-policy6/{policyid}
    DELETE /firewall/DoS-policy6/{policyid}
"""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from ....http_client import HTTPClient


class DosPolicy6:
    """DosPolicy6 operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize DosPolicy6 endpoint.

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
            endpoint = f"/firewall/DoS-policy6/{policyid}"
        else:
            endpoint = "/firewall/DoS-policy6"
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
        status: str | None = None,
        name: str | None = None,
        comments: str | None = None,
        interface: str | None = None,
        srcaddr: list | None = None,
        dstaddr: list | None = None,
        service: list | None = None,
        anomaly: list | None = None,
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
            status: Enable/disable this policy. (optional)
            name: Policy name. (optional)
            comments: Comment. (optional)
            interface: Incoming interface name from available interfaces. (optional)
            srcaddr: Source address name from available addresses. (optional)
            dstaddr: Destination address name from available addresses. (optional)
            service: Service object from available options. (optional)
            anomaly: Anomaly name. (optional)
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
        endpoint = f"/firewall/DoS-policy6/{policyid}"
        if before is not None:
            data_payload['before'] = before
        if after is not None:
            data_payload['after'] = after
        if policyid is not None:
            data_payload['policyid'] = policyid
        if status is not None:
            data_payload['status'] = status
        if name is not None:
            data_payload['name'] = name
        if comments is not None:
            data_payload['comments'] = comments
        if interface is not None:
            data_payload['interface'] = interface
        if srcaddr is not None:
            data_payload['srcaddr'] = srcaddr
        if dstaddr is not None:
            data_payload['dstaddr'] = dstaddr
        if service is not None:
            data_payload['service'] = service
        if anomaly is not None:
            data_payload['anomaly'] = anomaly
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
        endpoint = f"/firewall/DoS-policy6/{policyid}"
        params.update(kwargs)
        return self._client.delete("cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json)

    def post(
        self,
        payload_dict: dict[str, Any] | None = None,
        nkey: str | None = None,
        policyid: int | None = None,
        status: str | None = None,
        name: str | None = None,
        comments: str | None = None,
        interface: str | None = None,
        srcaddr: list | None = None,
        dstaddr: list | None = None,
        service: list | None = None,
        anomaly: list | None = None,
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
            status: Enable/disable this policy. (optional)
            name: Policy name. (optional)
            comments: Comment. (optional)
            interface: Incoming interface name from available interfaces. (optional)
            srcaddr: Source address name from available addresses. (optional)
            dstaddr: Destination address name from available addresses. (optional)
            service: Service object from available options. (optional)
            anomaly: Anomaly name. (optional)
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
        endpoint = "/firewall/DoS-policy6"
        if nkey is not None:
            data_payload['nkey'] = nkey
        if policyid is not None:
            data_payload['policyid'] = policyid
        if status is not None:
            data_payload['status'] = status
        if name is not None:
            data_payload['name'] = name
        if comments is not None:
            data_payload['comments'] = comments
        if interface is not None:
            data_payload['interface'] = interface
        if srcaddr is not None:
            data_payload['srcaddr'] = srcaddr
        if dstaddr is not None:
            data_payload['dstaddr'] = dstaddr
        if service is not None:
            data_payload['service'] = service
        if anomaly is not None:
            data_payload['anomaly'] = anomaly
        data_payload.update(kwargs)
        return self._client.post("cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json)
