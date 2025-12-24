"""
FortiOS CMDB - Cmdb Switch Controller Stp Settings

Configuration endpoint for managing cmdb switch controller stp settings
objects.

API Endpoints:
    GET    /cmdb/switch-controller/stp_settings
    PUT    /cmdb/switch-controller/stp_settings/{identifier}

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.switch_controller.stp_settings.get()
    >>>
    >>> # Get specific item (if supported)
    >>> item =
    fgt.api.cmdb.switch_controller.stp_settings.get(name="item_name")
    >>>
    >>> # Create new item (use POST)
    >>> result = fgt.api.cmdb.switch_controller.stp_settings.post(
    ...     name="new_item",
    ...     # ... additional parameters
    ... )
    >>>
    >>> # Update existing item (use PUT)
    >>> result = fgt.api.cmdb.switch_controller.stp_settings.put(
    ...     name="existing_item",
    ...     # ... parameters to update
    ... )
    >>>
    >>> # Delete item
    >>> result =
    fgt.api.cmdb.switch_controller.stp_settings.delete(name="item_name")

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


class StpSettings:
    """
    Stpsettings Operations.

    Provides CRUD operations for FortiOS stpsettings configuration.

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
        Initialize StpSettings endpoint.

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
        endpoint = "/switch-controller/stp-settings"
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
        name: str | None = None,
        revision: int | None = None,
        hello_time: int | None = None,
        forward_time: int | None = None,
        max_age: int | None = None,
        max_hops: int | None = None,
        pending_timer: int | None = None,
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
            name: Name of global STP settings configuration. (optional)
            revision: STP revision number (0 - 65535). (optional)
            hello_time: Period of time between successive STP frame Bridge
            Protocol Data Units (BPDUs) sent on a port (1 - 10 sec, default =
            2). (optional)
            forward_time: Period of time a port is in listening and learning
            state (4 - 30 sec, default = 15). (optional)
            max_age: Maximum time before a bridge port expires its
            configuration BPDU information (6 - 40 sec, default = 20).
            (optional)
            max_hops: Maximum number of hops between the root bridge and the
            furthest bridge (1- 40, default = 20). (optional)
            pending_timer: Pending time (1 - 15 sec, default = 4). (optional)
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
        endpoint = "/switch-controller/stp-settings"
        if before is not None:
            data_payload["before"] = before
        if after is not None:
            data_payload["after"] = after
        if name is not None:
            data_payload["name"] = name
        if revision is not None:
            data_payload["revision"] = revision
        if hello_time is not None:
            data_payload["hello-time"] = hello_time
        if forward_time is not None:
            data_payload["forward-time"] = forward_time
        if max_age is not None:
            data_payload["max-age"] = max_age
        if max_hops is not None:
            data_payload["max-hops"] = max_hops
        if pending_timer is not None:
            data_payload["pending-timer"] = pending_timer
        data_payload.update(kwargs)
        return self._client.put(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )
