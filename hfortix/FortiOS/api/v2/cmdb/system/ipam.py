"""
FortiOS CMDB - Cmdb System Ipam

Configuration endpoint for managing cmdb system ipam objects.

API Endpoints:
    GET    /cmdb/system/ipam
    PUT    /cmdb/system/ipam/{identifier}

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.system.ipam.get()
    >>>
    >>> # Get specific item (if supported)
    >>> item = fgt.api.cmdb.system.ipam.get(name="item_name")
    >>>
    >>> # Create new item (use POST)
    >>> result = fgt.api.cmdb.system.ipam.post(
    ...     name="new_item",
    ...     # ... additional parameters
    ... )
    >>>
    >>> # Update existing item (use PUT)
    >>> result = fgt.api.cmdb.system.ipam.put(
    ...     name="existing_item",
    ...     # ... parameters to update
    ... )
    >>>
    >>> # Delete item
    >>> result = fgt.api.cmdb.system.ipam.delete(name="item_name")

Important:
    - Use **POST** to create new objects (404 error if already exists)
    - Use **PUT** to update existing objects (404 error if doesn't exist)
    - Use **GET** to retrieve configuration (no changes made)
    - Use **DELETE** to remove objects (404 error if doesn't exist)
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Union

if TYPE_CHECKING:
    from collections.abc import Coroutine

    from hfortix.FortiOS.http_client_interface import IHTTPClient


class Ipam:
    """
    Ipam Operations.

    Provides CRUD operations for FortiOS ipam configuration.

    Methods:
        get(): Retrieve configuration objects
        put(): Update existing configuration objects

    Important:
        - POST creates new objects (404 if name already exists)
        - PUT updates existing objects (404 if name doesn't exist)
        - GET retrieves objects without making changes
        - DELETE removes objects (404 if name doesn't exist)
    """

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Ipam endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

    def get(
        self,
        payload_dict: dict[str, Any] | None = None,
        exclude_default_values: bool | None = None,
        stat_items: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Select all entries in a CLI table.

        Args:
            exclude_default_values: Exclude properties/objects with default
            value (optional)
            stat_items: Items to count occurrence in entire response (multiple
            items should be separated by '|'). (optional)
            vdom: Virtual domain name, or False to skip. Handled by HTTPClient.
            raw_json: If True, return full API response with metadata. If
            False, return only results.
            **kwargs: Additional query parameters (filter, sort, start, count,
            format, etc.)

        Common Query Parameters (via **kwargs):
            filter: Filter results (e.g., filter='name==value')
            sort: Sort results (e.g., sort='name,asc')
            start: Starting entry index for paging
            count: Maximum number of entries to return
            format: Fields to return (e.g., format='name|type')
            See FortiOS REST API documentation for full list of query
            parameters

        Returns:
            Dictionary containing API response
        """
        params = payload_dict.copy() if payload_dict else {}
        endpoint = "/system/ipam"
        if exclude_default_values is not None:
            params["exclude-default-values"] = exclude_default_values
        if stat_items is not None:
            params["stat-items"] = stat_items
        params.update(kwargs)
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )

    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        before: str | None = None,
        after: str | None = None,
        status: str | None = None,
        server_type: str | None = None,
        automatic_conflict_resolution: str | None = None,
        require_subnet_size_match: str | None = None,
        manage_lan_addresses: str | None = None,
        manage_lan_extension_addresses: str | None = None,
        manage_ssid_addresses: str | None = None,
        pools: list | None = None,
        rules: list | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update this specific resource.

        Args:
            payload_dict: Optional dictionary of all parameters (can be passed
            as first positional arg)
            before: If *action=move*, use *before* to specify the ID of the
            resource that this resource will be moved before. (optional)
            after: If *action=move*, use *after* to specify the ID of the
            resource that this resource will be moved after. (optional)
            status: Enable/disable IP address management services. (optional)
            server_type: Configure the type of IPAM server to use. (optional)
            automatic_conflict_resolution: Enable/disable automatic conflict
            resolution. (optional)
            require_subnet_size_match: Enable/disable reassignment of subnets
            to make requested and actual sizes match. (optional)
            manage_lan_addresses: Enable/disable default management of LAN
            interface addresses. (optional)
            manage_lan_extension_addresses: Enable/disable default management
            of FortiExtender LAN extension interface addresses. (optional)
            manage_ssid_addresses: Enable/disable default management of FortiAP
            SSID addresses. (optional)
            pools: Configure IPAM pools. (optional)
            rules: Configure IPAM allocation rules. (optional)
            vdom: Virtual domain name, or False to skip. Handled by HTTPClient.
            raw_json: If True, return full API response with metadata. If
            False, return only results.
            **kwargs: Additional query parameters (filter, sort, start, count,
            format, etc.)

        Common Query Parameters (via **kwargs):
            filter: Filter results (e.g., filter='name==value')
            sort: Sort results (e.g., sort='name,asc')
            start: Starting entry index for paging
            count: Maximum number of entries to return
            format: Fields to return (e.g., format='name|type')
            See FortiOS REST API documentation for full list of query
            parameters

        Returns:
            Dictionary containing API response
        """
        data_payload = payload_dict.copy() if payload_dict else {}
        endpoint = "/system/ipam"
        if before is not None:
            data_payload["before"] = before
        if after is not None:
            data_payload["after"] = after
        if status is not None:
            data_payload["status"] = status
        if server_type is not None:
            data_payload["server-type"] = server_type
        if automatic_conflict_resolution is not None:
            data_payload["automatic-conflict-resolution"] = (
                automatic_conflict_resolution
            )
        if require_subnet_size_match is not None:
            data_payload["require-subnet-size-match"] = (
                require_subnet_size_match
            )
        if manage_lan_addresses is not None:
            data_payload["manage-lan-addresses"] = manage_lan_addresses
        if manage_lan_extension_addresses is not None:
            data_payload["manage-lan-extension-addresses"] = (
                manage_lan_extension_addresses
            )
        if manage_ssid_addresses is not None:
            data_payload["manage-ssid-addresses"] = manage_ssid_addresses
        if pools is not None:
            data_payload["pools"] = pools
        if rules is not None:
            data_payload["rules"] = rules
        data_payload.update(kwargs)
        return self._client.put(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )
