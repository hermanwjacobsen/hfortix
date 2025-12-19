"""
FortiOS CMDB - Firewall InternetService

API Endpoints:
    GET    /firewall/internet-service
    POST   /firewall/internet-service
    GET    /firewall/internet-service/{id}
    PUT    /firewall/internet-service/{id}
    DELETE /firewall/internet-service/{id}
"""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from ....http_client import HTTPClient


class InternetService:
    """InternetService operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize InternetService endpoint.

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
            endpoint = f"/firewall/internet-service/{id}"
        else:
            endpoint = "/firewall/internet-service"
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
        name: str | None = None,
        icon_id: int | None = None,
        direction: str | None = None,
        database: str | None = None,
        ip_range_number: int | None = None,
        extra_ip_range_number: int | None = None,
        ip_number: int | None = None,
        ip6_range_number: int | None = None,
        extra_ip6_range_number: int | None = None,
        singularity: int | None = None,
        obsolete: int | None = None,
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
            id: Internet Service ID. (optional)
            name: Internet Service name. (optional)
            icon_id: Icon ID of Internet Service. (optional)
            direction: How this service may be used in a firewall policy (source, destination or both). (optional)
            database: Database name this Internet Service belongs to. (optional)
            ip_range_number: Number of IPv4 ranges. (optional)
            extra_ip_range_number: Extra number of IPv4 ranges. (optional)
            ip_number: Total number of IPv4 addresses. (optional)
            ip6_range_number: Number of IPv6 ranges. (optional)
            extra_ip6_range_number: Extra number of IPv6 ranges. (optional)
            singularity: Singular level of the Internet Service. (optional)
            obsolete: Indicates whether the Internet Service can be used. (optional)
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
        endpoint = f"/firewall/internet-service/{id}"
        if before is not None:
            data_payload['before'] = before
        if after is not None:
            data_payload['after'] = after
        if id is not None:
            data_payload['id'] = id
        if name is not None:
            data_payload['name'] = name
        if icon_id is not None:
            data_payload['icon-id'] = icon_id
        if direction is not None:
            data_payload['direction'] = direction
        if database is not None:
            data_payload['database'] = database
        if ip_range_number is not None:
            data_payload['ip-range-number'] = ip_range_number
        if extra_ip_range_number is not None:
            data_payload['extra-ip-range-number'] = extra_ip_range_number
        if ip_number is not None:
            data_payload['ip-number'] = ip_number
        if ip6_range_number is not None:
            data_payload['ip6-range-number'] = ip6_range_number
        if extra_ip6_range_number is not None:
            data_payload['extra-ip6-range-number'] = extra_ip6_range_number
        if singularity is not None:
            data_payload['singularity'] = singularity
        if obsolete is not None:
            data_payload['obsolete'] = obsolete
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
        endpoint = f"/firewall/internet-service/{id}"
        params.update(kwargs)
        return self._client.delete("cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json)

    def post(
        self,
        payload_dict: dict[str, Any] | None = None,
        nkey: str | None = None,
        id: int | None = None,
        name: str | None = None,
        icon_id: int | None = None,
        direction: str | None = None,
        database: str | None = None,
        ip_range_number: int | None = None,
        extra_ip_range_number: int | None = None,
        ip_number: int | None = None,
        ip6_range_number: int | None = None,
        extra_ip6_range_number: int | None = None,
        singularity: int | None = None,
        obsolete: int | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Create object(s) in this table.
        
        Args:
            payload_dict: Optional dictionary of all parameters (can be passed as first positional arg)
            nkey: If *action=clone*, use *nkey* to specify the ID for the new resource to be created. (optional)
            id: Internet Service ID. (optional)
            name: Internet Service name. (optional)
            icon_id: Icon ID of Internet Service. (optional)
            direction: How this service may be used in a firewall policy (source, destination or both). (optional)
            database: Database name this Internet Service belongs to. (optional)
            ip_range_number: Number of IPv4 ranges. (optional)
            extra_ip_range_number: Extra number of IPv4 ranges. (optional)
            ip_number: Total number of IPv4 addresses. (optional)
            ip6_range_number: Number of IPv6 ranges. (optional)
            extra_ip6_range_number: Extra number of IPv6 ranges. (optional)
            singularity: Singular level of the Internet Service. (optional)
            obsolete: Indicates whether the Internet Service can be used. (optional)
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
        endpoint = "/firewall/internet-service"
        if nkey is not None:
            data_payload['nkey'] = nkey
        if id is not None:
            data_payload['id'] = id
        if name is not None:
            data_payload['name'] = name
        if icon_id is not None:
            data_payload['icon-id'] = icon_id
        if direction is not None:
            data_payload['direction'] = direction
        if database is not None:
            data_payload['database'] = database
        if ip_range_number is not None:
            data_payload['ip-range-number'] = ip_range_number
        if extra_ip_range_number is not None:
            data_payload['extra-ip-range-number'] = extra_ip_range_number
        if ip_number is not None:
            data_payload['ip-number'] = ip_number
        if ip6_range_number is not None:
            data_payload['ip6-range-number'] = ip6_range_number
        if extra_ip6_range_number is not None:
            data_payload['extra-ip6-range-number'] = extra_ip6_range_number
        if singularity is not None:
            data_payload['singularity'] = singularity
        if obsolete is not None:
            data_payload['obsolete'] = obsolete
        data_payload.update(kwargs)
        return self._client.post("cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json)
