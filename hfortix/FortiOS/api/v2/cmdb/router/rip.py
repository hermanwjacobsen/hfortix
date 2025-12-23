"""
FortiOS CMDB - Cmdb Router Rip

Configuration endpoint for managing cmdb router rip objects.

API Endpoints:
    GET    /cmdb/router/rip
    PUT    /cmdb/router/rip/{identifier}

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.router.rip.get()
    >>>
    >>> # Get specific item (if supported)
    >>> item = fgt.api.cmdb.router.rip.get(name="item_name")
    >>>
    >>> # Create new item (use POST)
    >>> result = fgt.api.cmdb.router.rip.post(
    ...     name="new_item",
    ...     # ... additional parameters
    ... )
    >>>
    >>> # Update existing item (use PUT)
    >>> result = fgt.api.cmdb.router.rip.put(
    ...     name="existing_item",
    ...     # ... parameters to update
    ... )
    >>>
    >>> # Delete item
    >>> result = fgt.api.cmdb.router.rip.delete(name="item_name")

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


class Rip:
    """
    Rip Operations.

    Provides CRUD operations for FortiOS rip configuration.

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
        Initialize Rip endpoint.

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
        endpoint = "/router/rip"
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
        default_information_originate: str | None = None,
        default_metric: int | None = None,
        max_out_metric: int | None = None,
        distance: list | None = None,
        distribute_list: list | None = None,
        neighbor: list | None = None,
        network: list | None = None,
        offset_list: list | None = None,
        passive_interface: list | None = None,
        redistribute: list | None = None,
        update_timer: int | None = None,
        timeout_timer: int | None = None,
        garbage_timer: int | None = None,
        version: str | None = None,
        interface: list | None = None,
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
            default_information_originate: Enable/disable generation of default
            route. (optional)
            default_metric: Default metric. (optional)
            max_out_metric: Maximum metric allowed to output(0 means 'not
            set'). (optional)
            distance: Distance. (optional)
            distribute_list: Distribute list. (optional)
            neighbor: Neighbor. (optional)
            network: Network. (optional)
            offset_list: Offset list. (optional)
            passive_interface: Passive interface configuration. (optional)
            redistribute: Redistribute configuration. (optional)
            update_timer: Update timer in seconds. (optional)
            timeout_timer: Timeout timer in seconds. (optional)
            garbage_timer: Garbage timer in seconds. (optional)
            version: RIP version. (optional)
            interface: RIP interface configuration. (optional)
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
        endpoint = "/router/rip"
        if before is not None:
            data_payload["before"] = before
        if after is not None:
            data_payload["after"] = after
        if default_information_originate is not None:
            data_payload["default-information-originate"] = (
                default_information_originate
            )
        if default_metric is not None:
            data_payload["default-metric"] = default_metric
        if max_out_metric is not None:
            data_payload["max-out-metric"] = max_out_metric
        if distance is not None:
            data_payload["distance"] = distance
        if distribute_list is not None:
            data_payload["distribute-list"] = distribute_list
        if neighbor is not None:
            data_payload["neighbor"] = neighbor
        if network is not None:
            data_payload["network"] = network
        if offset_list is not None:
            data_payload["offset-list"] = offset_list
        if passive_interface is not None:
            data_payload["passive-interface"] = passive_interface
        if redistribute is not None:
            data_payload["redistribute"] = redistribute
        if update_timer is not None:
            data_payload["update-timer"] = update_timer
        if timeout_timer is not None:
            data_payload["timeout-timer"] = timeout_timer
        if garbage_timer is not None:
            data_payload["garbage-timer"] = garbage_timer
        if version is not None:
            data_payload["version"] = version
        if interface is not None:
            data_payload["interface"] = interface
        data_payload.update(kwargs)
        return self._client.put(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )
