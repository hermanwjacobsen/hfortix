"""
FortiOS CMDB - Firewall Addrgrp6

API Endpoints:
    GET    /firewall/addrgrp6
    POST   /firewall/addrgrp6
    GET    /firewall/addrgrp6/{name}
    PUT    /firewall/addrgrp6/{name}
    DELETE /firewall/addrgrp6/{name}
"""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from ....http_client import HTTPClient


class Addrgrp6:
    """Addrgrp6 operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize Addrgrp6 endpoint.

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
            endpoint = f"/firewall/addrgrp6/{name}"
        else:
            endpoint = "/firewall/addrgrp6"
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
        uuid: str | None = None,
        color: int | None = None,
        comment: str | None = None,
        member: list | None = None,
        exclude: str | None = None,
        exclude_member: list | None = None,
        tagging: list | None = None,
        fabric_object: str | None = None,
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
            name: IPv6 address group name. (optional)
            uuid: Universally Unique Identifier (UUID; automatically assigned but can be manually reset). (optional)
            color: Integer value to determine the color of the icon in the GUI (1 - 32, default = 0, which sets the value to 1). (optional)
            comment: Comment. (optional)
            member: Address objects contained within the group. (optional)
            exclude: Enable/disable address6 exclusion. (optional)
            exclude_member: Address6 exclusion member. (optional)
            tagging: Config object tagging. (optional)
            fabric_object: Security Fabric global object setting. (optional)
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
        endpoint = f"/firewall/addrgrp6/{name}"
        if before is not None:
            data_payload['before'] = before
        if after is not None:
            data_payload['after'] = after
        if name is not None:
            data_payload['name'] = name
        if uuid is not None:
            data_payload['uuid'] = uuid
        if color is not None:
            data_payload['color'] = color
        if comment is not None:
            data_payload['comment'] = comment
        if member is not None:
            data_payload['member'] = member
        if exclude is not None:
            data_payload['exclude'] = exclude
        if exclude_member is not None:
            data_payload['exclude-member'] = exclude_member
        if tagging is not None:
            data_payload['tagging'] = tagging
        if fabric_object is not None:
            data_payload['fabric-object'] = fabric_object
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
        endpoint = f"/firewall/addrgrp6/{name}"
        params.update(kwargs)
        return self._client.delete("cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json)

    def post(
        self,
        payload_dict: dict[str, Any] | None = None,
        nkey: str | None = None,
        name: str | None = None,
        uuid: str | None = None,
        color: int | None = None,
        comment: str | None = None,
        member: list | None = None,
        exclude: str | None = None,
        exclude_member: list | None = None,
        tagging: list | None = None,
        fabric_object: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Create object(s) in this table.
        
        Args:
            payload_dict: Optional dictionary of all parameters (can be passed as first positional arg)
            nkey: If *action=clone*, use *nkey* to specify the ID for the new resource to be created. (optional)
            name: IPv6 address group name. (optional)
            uuid: Universally Unique Identifier (UUID; automatically assigned but can be manually reset). (optional)
            color: Integer value to determine the color of the icon in the GUI (1 - 32, default = 0, which sets the value to 1). (optional)
            comment: Comment. (optional)
            member: Address objects contained within the group. (optional)
            exclude: Enable/disable address6 exclusion. (optional)
            exclude_member: Address6 exclusion member. (optional)
            tagging: Config object tagging. (optional)
            fabric_object: Security Fabric global object setting. (optional)
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
        endpoint = "/firewall/addrgrp6"
        if nkey is not None:
            data_payload['nkey'] = nkey
        if name is not None:
            data_payload['name'] = name
        if uuid is not None:
            data_payload['uuid'] = uuid
        if color is not None:
            data_payload['color'] = color
        if comment is not None:
            data_payload['comment'] = comment
        if member is not None:
            data_payload['member'] = member
        if exclude is not None:
            data_payload['exclude'] = exclude
        if exclude_member is not None:
            data_payload['exclude-member'] = exclude_member
        if tagging is not None:
            data_payload['tagging'] = tagging
        if fabric_object is not None:
            data_payload['fabric-object'] = fabric_object
        data_payload.update(kwargs)
        return self._client.post("cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json)
