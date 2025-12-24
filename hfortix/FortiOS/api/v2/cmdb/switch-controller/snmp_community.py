"""
FortiOS CMDB - Cmdb Switch Controller Snmp Community

Configuration endpoint for managing cmdb switch controller snmp community
objects.

API Endpoints:
    GET    /cmdb/switch-controller/snmp_community
    POST   /cmdb/switch-controller/snmp_community
    GET    /cmdb/switch-controller/snmp_community
    PUT    /cmdb/switch-controller/snmp_community/{identifier}
    DELETE /cmdb/switch-controller/snmp_community/{identifier}

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.switch_controller.snmp_community.get()
    >>>
    >>> # Get specific item (if supported)
    >>> item =
    fgt.api.cmdb.switch_controller.snmp_community.get(name="item_name")
    >>>
    >>> # Create new item (use POST)
    >>> result = fgt.api.cmdb.switch_controller.snmp_community.post(
    ...     name="new_item",
    ...     # ... additional parameters
    ... )
    >>>
    >>> # Update existing item (use PUT)
    >>> result = fgt.api.cmdb.switch_controller.snmp_community.put(
    ...     name="existing_item",
    ...     # ... parameters to update
    ... )
    >>>
    >>> # Delete item
    >>> result =
    fgt.api.cmdb.switch_controller.snmp_community.delete(name="item_name")

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


class SnmpCommunity:
    """
    Snmpcommunity Operations.

    Provides CRUD operations for FortiOS snmpcommunity configuration.

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
        Initialize SnmpCommunity endpoint.

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
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Select a specific entry from a CLI table.

        Args:
            id: Object identifier (optional for list, required for specific)
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
        if id:
            endpoint = f"/switch-controller/snmp-community/{id}"
        else:
            endpoint = "/switch-controller/snmp-community"
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
        id: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        before: str | None = None,
        after: str | None = None,
        name: str | None = None,
        status: str | None = None,
        hosts: list | None = None,
        query_v1_status: str | None = None,
        query_v1_port: int | None = None,
        query_v2c_status: str | None = None,
        query_v2c_port: int | None = None,
        trap_v1_status: str | None = None,
        trap_v1_lport: int | None = None,
        trap_v1_rport: int | None = None,
        trap_v2c_status: str | None = None,
        trap_v2c_lport: int | None = None,
        trap_v2c_rport: int | None = None,
        events: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update this specific resource.

        Args:
            payload_dict: Optional dictionary of all parameters (can be passed
            as first positional arg)
            id: Object identifier (required)
            before: If *action=move*, use *before* to specify the ID of the
            resource that this resource will be moved before. (optional)
            after: If *action=move*, use *after* to specify the ID of the
            resource that this resource will be moved after. (optional)
            id: SNMP community ID. (optional)
            name: SNMP community name. (optional)
            status: Enable/disable this SNMP community. (optional)
            hosts: Configure IPv4 SNMP managers (hosts). (optional)
            query_v1_status: Enable/disable SNMP v1 queries. (optional)
            query_v1_port: SNMP v1 query port (default = 161). (optional)
            query_v2c_status: Enable/disable SNMP v2c queries. (optional)
            query_v2c_port: SNMP v2c query port (default = 161). (optional)
            trap_v1_status: Enable/disable SNMP v1 traps. (optional)
            trap_v1_lport: SNMP v2c trap local port (default = 162). (optional)
            trap_v1_rport: SNMP v2c trap remote port (default = 162).
            (optional)
            trap_v2c_status: Enable/disable SNMP v2c traps. (optional)
            trap_v2c_lport: SNMP v2c trap local port (default = 162).
            (optional)
            trap_v2c_rport: SNMP v2c trap remote port (default = 162).
            (optional)
            events: SNMP notifications (traps) to send. (optional)
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
        if not id:
            raise ValueError("id is required for put()")
        endpoint = f"/switch-controller/snmp-community/{id}"
        if before is not None:
            data_payload["before"] = before
        if after is not None:
            data_payload["after"] = after
        if id is not None:
            data_payload["id"] = id
        if name is not None:
            data_payload["name"] = name
        if status is not None:
            data_payload["status"] = status
        if hosts is not None:
            data_payload["hosts"] = hosts
        if query_v1_status is not None:
            data_payload["query-v1-status"] = query_v1_status
        if query_v1_port is not None:
            data_payload["query-v1-port"] = query_v1_port
        if query_v2c_status is not None:
            data_payload["query-v2c-status"] = query_v2c_status
        if query_v2c_port is not None:
            data_payload["query-v2c-port"] = query_v2c_port
        if trap_v1_status is not None:
            data_payload["trap-v1-status"] = trap_v1_status
        if trap_v1_lport is not None:
            data_payload["trap-v1-lport"] = trap_v1_lport
        if trap_v1_rport is not None:
            data_payload["trap-v1-rport"] = trap_v1_rport
        if trap_v2c_status is not None:
            data_payload["trap-v2c-status"] = trap_v2c_status
        if trap_v2c_lport is not None:
            data_payload["trap-v2c-lport"] = trap_v2c_lport
        if trap_v2c_rport is not None:
            data_payload["trap-v2c-rport"] = trap_v2c_rport
        if events is not None:
            data_payload["events"] = events
        data_payload.update(kwargs)
        return self._client.put(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )

    def delete(
        self,
        id: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Delete this specific resource.

        Args:
            id: Object identifier (required)
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
        if not id:
            raise ValueError("id is required for delete()")
        endpoint = f"/switch-controller/snmp-community/{id}"
        params.update(kwargs)
        return self._client.delete(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )

    def exists(
        self,
        id: str,
        vdom: str | bool | None = None,
    ) -> Union[bool, Coroutine[Any, Any, bool]]:
        """
        Check if an object exists.

        Args:
            id: Object identifier
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
        result = self.get(id=id, vdom=vdom)

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
        id: int | None = None,
        name: str | None = None,
        status: str | None = None,
        hosts: list | None = None,
        query_v1_status: str | None = None,
        query_v1_port: int | None = None,
        query_v2c_status: str | None = None,
        query_v2c_port: int | None = None,
        trap_v1_status: str | None = None,
        trap_v1_lport: int | None = None,
        trap_v1_rport: int | None = None,
        trap_v2c_status: str | None = None,
        trap_v2c_lport: int | None = None,
        trap_v2c_rport: int | None = None,
        events: str | None = None,
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
            id: SNMP community ID. (optional)
            name: SNMP community name. (optional)
            status: Enable/disable this SNMP community. (optional)
            hosts: Configure IPv4 SNMP managers (hosts). (optional)
            query_v1_status: Enable/disable SNMP v1 queries. (optional)
            query_v1_port: SNMP v1 query port (default = 161). (optional)
            query_v2c_status: Enable/disable SNMP v2c queries. (optional)
            query_v2c_port: SNMP v2c query port (default = 161). (optional)
            trap_v1_status: Enable/disable SNMP v1 traps. (optional)
            trap_v1_lport: SNMP v2c trap local port (default = 162). (optional)
            trap_v1_rport: SNMP v2c trap remote port (default = 162).
            (optional)
            trap_v2c_status: Enable/disable SNMP v2c traps. (optional)
            trap_v2c_lport: SNMP v2c trap local port (default = 162).
            (optional)
            trap_v2c_rport: SNMP v2c trap remote port (default = 162).
            (optional)
            events: SNMP notifications (traps) to send. (optional)
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
        endpoint = "/switch-controller/snmp-community"
        if nkey is not None:
            data_payload["nkey"] = nkey
        if id is not None:
            data_payload["id"] = id
        if name is not None:
            data_payload["name"] = name
        if status is not None:
            data_payload["status"] = status
        if hosts is not None:
            data_payload["hosts"] = hosts
        if query_v1_status is not None:
            data_payload["query-v1-status"] = query_v1_status
        if query_v1_port is not None:
            data_payload["query-v1-port"] = query_v1_port
        if query_v2c_status is not None:
            data_payload["query-v2c-status"] = query_v2c_status
        if query_v2c_port is not None:
            data_payload["query-v2c-port"] = query_v2c_port
        if trap_v1_status is not None:
            data_payload["trap-v1-status"] = trap_v1_status
        if trap_v1_lport is not None:
            data_payload["trap-v1-lport"] = trap_v1_lport
        if trap_v1_rport is not None:
            data_payload["trap-v1-rport"] = trap_v1_rport
        if trap_v2c_status is not None:
            data_payload["trap-v2c-status"] = trap_v2c_status
        if trap_v2c_lport is not None:
            data_payload["trap-v2c-lport"] = trap_v2c_lport
        if trap_v2c_rport is not None:
            data_payload["trap-v2c-rport"] = trap_v2c_rport
        if events is not None:
            data_payload["events"] = events
        data_payload.update(kwargs)
        return self._client.post(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )
