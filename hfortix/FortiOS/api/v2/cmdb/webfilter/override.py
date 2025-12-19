"""
FortiOS CMDB - Webfilter Override

API Endpoints:
    GET    /webfilter/override
    POST   /webfilter/override
    GET    /webfilter/override/{id}
    PUT    /webfilter/override/{id}
    DELETE /webfilter/override/{id}
"""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from ....http_client import HTTPClient


class Override:
    """Override operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize Override endpoint.

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
            endpoint = f"/webfilter/override/{id}"
        else:
            endpoint = "/webfilter/override"
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
        status: str | None = None,
        ip: str | None = None,
        user: str | None = None,
        user_group: str | None = None,
        old_profile: str | None = None,
        new_profile: str | None = None,
        ip6: str | None = None,
        expires: str | None = None,
        initiator: str | None = None,
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
            id: Override rule ID. (optional)
            status: Enable/disable override rule. (optional)
            ip: IPv4 address which the override applies. (optional)
            user: Name of the user which the override applies. (optional)
            user_group: Specify the user group for which the override applies. (optional)
            old_profile: Name of the web filter profile which the override applies. (optional)
            new_profile: Name of the new web filter profile used by the override. (optional)
            ip6: IPv6 address which the override applies. (optional)
            expires: Override expiration date and time, from 5 minutes to 365 from now (format: yyyy/mm/dd hh:mm:ss). (optional)
            initiator: Initiating user of override (read-only setting). (optional)
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
        endpoint = f"/webfilter/override/{id}"
        if before is not None:
            data_payload['before'] = before
        if after is not None:
            data_payload['after'] = after
        if id is not None:
            data_payload['id'] = id
        if status is not None:
            data_payload['status'] = status
        if ip is not None:
            data_payload['ip'] = ip
        if user is not None:
            data_payload['user'] = user
        if user_group is not None:
            data_payload['user-group'] = user_group
        if old_profile is not None:
            data_payload['old-profile'] = old_profile
        if new_profile is not None:
            data_payload['new-profile'] = new_profile
        if ip6 is not None:
            data_payload['ip6'] = ip6
        if expires is not None:
            data_payload['expires'] = expires
        if initiator is not None:
            data_payload['initiator'] = initiator
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
        endpoint = f"/webfilter/override/{id}"
        params.update(kwargs)
        return self._client.delete("cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json)

    def post(
        self,
        payload_dict: dict[str, Any] | None = None,
        nkey: str | None = None,
        id: int | None = None,
        status: str | None = None,
        ip: str | None = None,
        user: str | None = None,
        user_group: str | None = None,
        old_profile: str | None = None,
        new_profile: str | None = None,
        ip6: str | None = None,
        expires: str | None = None,
        initiator: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Create object(s) in this table.
        
        Args:
            payload_dict: Optional dictionary of all parameters (can be passed as first positional arg)
            nkey: If *action=clone*, use *nkey* to specify the ID for the new resource to be created. (optional)
            id: Override rule ID. (optional)
            status: Enable/disable override rule. (optional)
            ip: IPv4 address which the override applies. (optional)
            user: Name of the user which the override applies. (optional)
            user_group: Specify the user group for which the override applies. (optional)
            old_profile: Name of the web filter profile which the override applies. (optional)
            new_profile: Name of the new web filter profile used by the override. (optional)
            ip6: IPv6 address which the override applies. (optional)
            expires: Override expiration date and time, from 5 minutes to 365 from now (format: yyyy/mm/dd hh:mm:ss). (optional)
            initiator: Initiating user of override (read-only setting). (optional)
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
        endpoint = "/webfilter/override"
        if nkey is not None:
            data_payload['nkey'] = nkey
        if id is not None:
            data_payload['id'] = id
        if status is not None:
            data_payload['status'] = status
        if ip is not None:
            data_payload['ip'] = ip
        if user is not None:
            data_payload['user'] = user
        if user_group is not None:
            data_payload['user-group'] = user_group
        if old_profile is not None:
            data_payload['old-profile'] = old_profile
        if new_profile is not None:
            data_payload['new-profile'] = new_profile
        if ip6 is not None:
            data_payload['ip6'] = ip6
        if expires is not None:
            data_payload['expires'] = expires
        if initiator is not None:
            data_payload['initiator'] = initiator
        data_payload.update(kwargs)
        return self._client.post("cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json)
