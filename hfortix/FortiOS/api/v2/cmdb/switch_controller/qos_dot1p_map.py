"""
FortiOS CMDB - Cmdb Switch Controller Qos Dot1p Map

Configuration endpoint for managing cmdb switch controller qos dot1p map
objects.

API Endpoints:
    GET    /cmdb/switch-controller/qos_dot1p_map
    POST   /cmdb/switch-controller/qos_dot1p_map
    GET    /cmdb/switch-controller/qos_dot1p_map
    PUT    /cmdb/switch-controller/qos_dot1p_map/{identifier}
    DELETE /cmdb/switch-controller/qos_dot1p_map/{identifier}

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.switch_controller.qos_dot1p_map.get()
    >>>
    >>> # Get specific item (if supported)
    >>> item =
    fgt.api.cmdb.switch_controller.qos_dot1p_map.get(name="item_name")
    >>>
    >>> # Create new item (use POST)
    >>> result = fgt.api.cmdb.switch_controller.qos_dot1p_map.post(
    ...     name="new_item",
    ...     # ... additional parameters
    ... )
    >>>
    >>> # Update existing item (use PUT)
    >>> result = fgt.api.cmdb.switch_controller.qos_dot1p_map.put(
    ...     name="existing_item",
    ...     # ... parameters to update
    ... )
    >>>
    >>> # Delete item
    >>> result =
    fgt.api.cmdb.switch_controller.qos_dot1p_map.delete(name="item_name")

Important:
    - Use **POST** to create new objects (404 error if already exists)
    - Use **PUT** to update existing objects (404 error if doesn't exist)
    - Use **GET** to retrieve configuration (no changes made)
    - Use **DELETE** to remove objects (404 error if doesn't exist)
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Union, cast

if TYPE_CHECKING:
    from collections.abc import Coroutine

    from hfortix.FortiOS.http_client_interface import IHTTPClient


class QosDot1pMap:
    """
    Qosdot1Pmap Operations.

    Provides CRUD operations for FortiOS qosdot1pmap configuration.

    Methods:
        get(): Retrieve configuration objects
        post(): Create new configuration objects
        put(): Update existing configuration objects
        delete(): Remove configuration objects

    Important:
        - POST creates new objects (404 if name already exists)
        - PUT updates existing objects (404 if name doesn't exist)
        - GET retrieves objects without making changes
        - DELETE removes objects (404 if name doesn't exist)
    """

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize QosDot1pMap endpoint.

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
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Select a specific entry from a CLI table.

        Args:
            name: Object identifier (optional for list, required for specific)
            attr: Attribute name that references other table (optional)
            skip_to_datasource: Skip to provided table's Nth entry. E.g
            {datasource: 'firewall.address', pos: 10, global_entry: false}
            (optional)
            acs: If true, returned result are in ascending order. (optional)
            search: If present, the objects will be filtered by the search
            value. (optional)
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

        # Build endpoint path
        if name:
            endpoint = f"/switch-controller.qos/dot1p-map/{name}"
        else:
            endpoint = "/switch-controller.qos/dot1p-map"
        if attr is not None:
            params["attr"] = attr
        if skip_to_datasource is not None:
            params["skip_to_datasource"] = skip_to_datasource
        if acs is not None:
            params["acs"] = acs
        if search is not None:
            params["search"] = search
        params.update(kwargs)
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )

    def put(
        self,
        name: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        before: str | None = None,
        after: str | None = None,
        description: str | None = None,
        egress_pri_tagging: str | None = None,
        priority_0: str | None = None,
        priority_1: str | None = None,
        priority_2: str | None = None,
        priority_3: str | None = None,
        priority_4: str | None = None,
        priority_5: str | None = None,
        priority_6: str | None = None,
        priority_7: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update this specific resource.

        Args:
            payload_dict: Optional dictionary of all parameters (can be passed
            as first positional arg)
            name: Object identifier (required)
            before: If *action=move*, use *before* to specify the ID of the
            resource that this resource will be moved before. (optional)
            after: If *action=move*, use *after* to specify the ID of the
            resource that this resource will be moved after. (optional)
            name: Dot1p map name. (optional)
            description: Description of the 802.1p name. (optional)
            egress_pri_tagging: Enable/disable egress priority-tag frame.
            (optional)
            priority_0: COS queue mapped to dot1p priority number. (optional)
            priority_1: COS queue mapped to dot1p priority number. (optional)
            priority_2: COS queue mapped to dot1p priority number. (optional)
            priority_3: COS queue mapped to dot1p priority number. (optional)
            priority_4: COS queue mapped to dot1p priority number. (optional)
            priority_5: COS queue mapped to dot1p priority number. (optional)
            priority_6: COS queue mapped to dot1p priority number. (optional)
            priority_7: COS queue mapped to dot1p priority number. (optional)
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

        # Build endpoint path
        if not name:
            raise ValueError("name is required for put()")
        endpoint = f"/switch-controller.qos/dot1p-map/{name}"
        if before is not None:
            data_payload["before"] = before
        if after is not None:
            data_payload["after"] = after
        if name is not None:
            data_payload["name"] = name
        if description is not None:
            data_payload["description"] = description
        if egress_pri_tagging is not None:
            data_payload["egress-pri-tagging"] = egress_pri_tagging
        if priority_0 is not None:
            data_payload["priority-0"] = priority_0
        if priority_1 is not None:
            data_payload["priority-1"] = priority_1
        if priority_2 is not None:
            data_payload["priority-2"] = priority_2
        if priority_3 is not None:
            data_payload["priority-3"] = priority_3
        if priority_4 is not None:
            data_payload["priority-4"] = priority_4
        if priority_5 is not None:
            data_payload["priority-5"] = priority_5
        if priority_6 is not None:
            data_payload["priority-6"] = priority_6
        if priority_7 is not None:
            data_payload["priority-7"] = priority_7
        data_payload.update(kwargs)
        return self._client.put(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )

    def delete(
        self,
        name: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Delete this specific resource.

        Args:
            name: Object identifier (required)
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

        # Build endpoint path
        if not name:
            raise ValueError("name is required for delete()")
        endpoint = f"/switch-controller.qos/dot1p-map/{name}"
        params.update(kwargs)
        return self._client.delete(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )

    def exists(
        self,
        name: str,
        vdom: str | bool | None = None,
    ) -> Union[bool, Coroutine[Any, Any, bool]]:
        """
        Check if an object exists.

        Args:
            name: Object identifier
            vdom: Virtual domain name, or False to skip. Handled by HTTPClient.

        Returns:
            True if object exists, False otherwise

        Example:
            >>> if fgt.api.cmdb.firewall.address.exists("server1"):
            ...     print("Address exists")
        """
        import inspect

        from hfortix.FortiOS.exceptions_forti import ResourceNotFoundError

        # Call get() - returns dict (sync) or coroutine (async)
        result = self.get(name=name, vdom=vdom)

        # Check if async mode
        if inspect.iscoroutine(result):

            async def _async():
                try:
                    # Runtime check confirms result is a coroutine, cast for
                    # mypy
                    await cast(Coroutine[Any, Any, dict[str, Any]], result)
                    return True
                except ResourceNotFoundError:
                    return False

            # Type ignore justified: mypy can't verify Union return type
            # narrowing

            return _async()
        # Sync mode - get() already executed, no exception means it exists
        return True

    def post(
        self,
        payload_dict: dict[str, Any] | None = None,
        nkey: str | None = None,
        name: str | None = None,
        description: str | None = None,
        egress_pri_tagging: str | None = None,
        priority_0: str | None = None,
        priority_1: str | None = None,
        priority_2: str | None = None,
        priority_3: str | None = None,
        priority_4: str | None = None,
        priority_5: str | None = None,
        priority_6: str | None = None,
        priority_7: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Create object(s) in this table.

        Args:
            payload_dict: Optional dictionary of all parameters (can be passed
            as first positional arg)
            nkey: If *action=clone*, use *nkey* to specify the ID for the new
            resource to be created. (optional)
            name: Dot1p map name. (optional)
            description: Description of the 802.1p name. (optional)
            egress_pri_tagging: Enable/disable egress priority-tag frame.
            (optional)
            priority_0: COS queue mapped to dot1p priority number. (optional)
            priority_1: COS queue mapped to dot1p priority number. (optional)
            priority_2: COS queue mapped to dot1p priority number. (optional)
            priority_3: COS queue mapped to dot1p priority number. (optional)
            priority_4: COS queue mapped to dot1p priority number. (optional)
            priority_5: COS queue mapped to dot1p priority number. (optional)
            priority_6: COS queue mapped to dot1p priority number. (optional)
            priority_7: COS queue mapped to dot1p priority number. (optional)
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
        endpoint = "/switch-controller.qos/dot1p-map"
        if nkey is not None:
            data_payload["nkey"] = nkey
        if name is not None:
            data_payload["name"] = name
        if description is not None:
            data_payload["description"] = description
        if egress_pri_tagging is not None:
            data_payload["egress-pri-tagging"] = egress_pri_tagging
        if priority_0 is not None:
            data_payload["priority-0"] = priority_0
        if priority_1 is not None:
            data_payload["priority-1"] = priority_1
        if priority_2 is not None:
            data_payload["priority-2"] = priority_2
        if priority_3 is not None:
            data_payload["priority-3"] = priority_3
        if priority_4 is not None:
            data_payload["priority-4"] = priority_4
        if priority_5 is not None:
            data_payload["priority-5"] = priority_5
        if priority_6 is not None:
            data_payload["priority-6"] = priority_6
        if priority_7 is not None:
            data_payload["priority-7"] = priority_7
        data_payload.update(kwargs)
        return self._client.post(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )
