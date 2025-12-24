"""
FortiOS CMDB - Cmdb System Speed Test Schedule

Configuration endpoint for managing cmdb system speed test schedule objects.

API Endpoints:
    GET    /cmdb/system/speed_test_schedule
    POST   /cmdb/system/speed_test_schedule
    GET    /cmdb/system/speed_test_schedule
    PUT    /cmdb/system/speed_test_schedule/{identifier}
    DELETE /cmdb/system/speed_test_schedule/{identifier}

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.system.speed_test_schedule.get()
    >>>
    >>> # Get specific item (if supported)
    >>> item = fgt.api.cmdb.system.speed_test_schedule.get(name="item_name")
    >>>
    >>> # Create new item (use POST)
    >>> result = fgt.api.cmdb.system.speed_test_schedule.post(
    ...     name="new_item",
    ...     # ... additional parameters
    ... )
    >>>
    >>> # Update existing item (use PUT)
    >>> result = fgt.api.cmdb.system.speed_test_schedule.put(
    ...     name="existing_item",
    ...     # ... parameters to update
    ... )
    >>>
    >>> # Delete item
    >>> result =
    fgt.api.cmdb.system.speed_test_schedule.delete(name="item_name")

Important:
    - Use **POST** to create new objects (404 error if already exists)
    - Use **PUT** to update existing objects (404 error if doesn't exist)
    - Use **GET** to retrieve configuration (no changes made)
    - Use **DELETE** to remove objects (404 error if doesn't exist)
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Coroutine, Union, cast

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client_interface import IHTTPClient


class SpeedTestSchedule:
    """
    Speedtestschedule Operations.

    Provides CRUD operations for FortiOS speedtestschedule configuration.

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
        Initialize SpeedTestSchedule endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

    def get(
        self,
        interface: str | None = None,
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
            interface: Object identifier (optional for list, required for
            specific)
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
        if interface:
            endpoint = f"/system/speed-test-schedule/{interface}"
        else:
            endpoint = "/system/speed-test-schedule"
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
        interface: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        before: str | None = None,
        after: str | None = None,
        status: str | None = None,
        diffserv: str | None = None,
        server_name: str | None = None,
        mode: str | None = None,
        schedules: list | None = None,
        dynamic_server: str | None = None,
        ctrl_port: int | None = None,
        server_port: int | None = None,
        update_shaper: str | None = None,
        update_inbandwidth: str | None = None,
        update_outbandwidth: str | None = None,
        update_interface_shaping: str | None = None,
        update_inbandwidth_maximum: int | None = None,
        update_inbandwidth_minimum: int | None = None,
        update_outbandwidth_maximum: int | None = None,
        update_outbandwidth_minimum: int | None = None,
        expected_inbandwidth_minimum: int | None = None,
        expected_inbandwidth_maximum: int | None = None,
        expected_outbandwidth_minimum: int | None = None,
        expected_outbandwidth_maximum: int | None = None,
        retries: int | None = None,
        retry_pause: int | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update this specific resource.

        Args:
            payload_dict: Optional dictionary of all parameters (can be passed
            as first positional arg)
            interface: Object identifier (required)
            before: If *action=move*, use *before* to specify the ID of the
            resource that this resource will be moved before. (optional)
            after: If *action=move*, use *after* to specify the ID of the
            resource that this resource will be moved after. (optional)
            interface: Interface name. (optional)
            status: Enable/disable scheduled speed test. (optional)
            diffserv: DSCP used for speed test. (optional)
            server_name: Speed test server name in system.speed-test-server
            list or leave it as empty to choose default server "FTNT_Auto".
            (optional)
            mode: Protocol Auto(default), TCP or UDP used for speed test.
            (optional)
            schedules: Schedules for the interface. (optional)
            dynamic_server: Enable/disable dynamic server option. (optional)
            ctrl_port: Port of the controller to get access token. (optional)
            server_port: Port of the server to run speed test. (optional)
            update_shaper: Set egress shaper based on the test result.
            (optional)
            update_inbandwidth: Enable/disable bypassing interface's inbound
            bandwidth setting. (optional)
            update_outbandwidth: Enable/disable bypassing interface's outbound
            bandwidth setting. (optional)
            update_interface_shaping: Enable/disable using the speedtest
            results as reference for interface shaping (overriding configured
            in/outbandwidth). (optional)
            update_inbandwidth_maximum: Maximum downloading bandwidth (kbps) to
            be used in a speed test. (optional)
            update_inbandwidth_minimum: Minimum downloading bandwidth (kbps) to
            be considered effective. (optional)
            update_outbandwidth_maximum: Maximum uploading bandwidth (kbps) to
            be used in a speed test. (optional)
            update_outbandwidth_minimum: Minimum uploading bandwidth (kbps) to
            be considered effective. (optional)
            expected_inbandwidth_minimum: Set the minimum inbandwidth threshold
            for applying speedtest results on shaping-profile. (optional)
            expected_inbandwidth_maximum: Set the maximum inbandwidth threshold
            for applying speedtest results on shaping-profile. (optional)
            expected_outbandwidth_minimum: Set the minimum outbandwidth
            threshold for applying speedtest results on shaping-profile.
            (optional)
            expected_outbandwidth_maximum: Set the maximum outbandwidth
            threshold for applying speedtest results on shaping-profile.
            (optional)
            retries: Maximum number of times the FortiGate unit will attempt to
            contact the same server before considering the speed test has
            failed (1 - 10, default = 5). (optional)
            retry_pause: Number of seconds the FortiGate pauses between
            successive speed tests before trying a different server (60 - 3600,
            default = 300). (optional)
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
        if not interface:
            raise ValueError("interface is required for put()")
        endpoint = f"/system/speed-test-schedule/{interface}"
        if before is not None:
            data_payload["before"] = before
        if after is not None:
            data_payload["after"] = after
        if interface is not None:
            data_payload["interface"] = interface
        if status is not None:
            data_payload["status"] = status
        if diffserv is not None:
            data_payload["diffserv"] = diffserv
        if server_name is not None:
            data_payload["server-name"] = server_name
        if mode is not None:
            data_payload["mode"] = mode
        if schedules is not None:
            data_payload["schedules"] = schedules
        if dynamic_server is not None:
            data_payload["dynamic-server"] = dynamic_server
        if ctrl_port is not None:
            data_payload["ctrl-port"] = ctrl_port
        if server_port is not None:
            data_payload["server-port"] = server_port
        if update_shaper is not None:
            data_payload["update-shaper"] = update_shaper
        if update_inbandwidth is not None:
            data_payload["update-inbandwidth"] = update_inbandwidth
        if update_outbandwidth is not None:
            data_payload["update-outbandwidth"] = update_outbandwidth
        if update_interface_shaping is not None:
            data_payload["update-interface-shaping"] = update_interface_shaping
        if update_inbandwidth_maximum is not None:
            data_payload["update-inbandwidth-maximum"] = (
                update_inbandwidth_maximum
            )
        if update_inbandwidth_minimum is not None:
            data_payload["update-inbandwidth-minimum"] = (
                update_inbandwidth_minimum
            )
        if update_outbandwidth_maximum is not None:
            data_payload["update-outbandwidth-maximum"] = (
                update_outbandwidth_maximum
            )
        if update_outbandwidth_minimum is not None:
            data_payload["update-outbandwidth-minimum"] = (
                update_outbandwidth_minimum
            )
        if expected_inbandwidth_minimum is not None:
            data_payload["expected-inbandwidth-minimum"] = (
                expected_inbandwidth_minimum
            )
        if expected_inbandwidth_maximum is not None:
            data_payload["expected-inbandwidth-maximum"] = (
                expected_inbandwidth_maximum
            )
        if expected_outbandwidth_minimum is not None:
            data_payload["expected-outbandwidth-minimum"] = (
                expected_outbandwidth_minimum
            )
        if expected_outbandwidth_maximum is not None:
            data_payload["expected-outbandwidth-maximum"] = (
                expected_outbandwidth_maximum
            )
        if retries is not None:
            data_payload["retries"] = retries
        if retry_pause is not None:
            data_payload["retry-pause"] = retry_pause
        data_payload.update(kwargs)
        return self._client.put(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )

    def delete(
        self,
        interface: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Delete this specific resource.

        Args:
            interface: Object identifier (required)
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
        if not interface:
            raise ValueError("interface is required for delete()")
        endpoint = f"/system/speed-test-schedule/{interface}"
        params.update(kwargs)
        return self._client.delete(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )

    def exists(
        self,
        interface: str,
        vdom: str | bool | None = None,
    ) -> Union[bool, Coroutine[Any, Any, bool]]:
        """
        Check if an object exists.

        Args:
            interface: Object identifier
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
        result = self.get(interface=interface, vdom=vdom)

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
        interface: str | None = None,
        status: str | None = None,
        diffserv: str | None = None,
        server_name: str | None = None,
        mode: str | None = None,
        schedules: list | None = None,
        dynamic_server: str | None = None,
        ctrl_port: int | None = None,
        server_port: int | None = None,
        update_shaper: str | None = None,
        update_inbandwidth: str | None = None,
        update_outbandwidth: str | None = None,
        update_interface_shaping: str | None = None,
        update_inbandwidth_maximum: int | None = None,
        update_inbandwidth_minimum: int | None = None,
        update_outbandwidth_maximum: int | None = None,
        update_outbandwidth_minimum: int | None = None,
        expected_inbandwidth_minimum: int | None = None,
        expected_inbandwidth_maximum: int | None = None,
        expected_outbandwidth_minimum: int | None = None,
        expected_outbandwidth_maximum: int | None = None,
        retries: int | None = None,
        retry_pause: int | None = None,
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
            interface: Interface name. (optional)
            status: Enable/disable scheduled speed test. (optional)
            diffserv: DSCP used for speed test. (optional)
            server_name: Speed test server name in system.speed-test-server
            list or leave it as empty to choose default server "FTNT_Auto".
            (optional)
            mode: Protocol Auto(default), TCP or UDP used for speed test.
            (optional)
            schedules: Schedules for the interface. (optional)
            dynamic_server: Enable/disable dynamic server option. (optional)
            ctrl_port: Port of the controller to get access token. (optional)
            server_port: Port of the server to run speed test. (optional)
            update_shaper: Set egress shaper based on the test result.
            (optional)
            update_inbandwidth: Enable/disable bypassing interface's inbound
            bandwidth setting. (optional)
            update_outbandwidth: Enable/disable bypassing interface's outbound
            bandwidth setting. (optional)
            update_interface_shaping: Enable/disable using the speedtest
            results as reference for interface shaping (overriding configured
            in/outbandwidth). (optional)
            update_inbandwidth_maximum: Maximum downloading bandwidth (kbps) to
            be used in a speed test. (optional)
            update_inbandwidth_minimum: Minimum downloading bandwidth (kbps) to
            be considered effective. (optional)
            update_outbandwidth_maximum: Maximum uploading bandwidth (kbps) to
            be used in a speed test. (optional)
            update_outbandwidth_minimum: Minimum uploading bandwidth (kbps) to
            be considered effective. (optional)
            expected_inbandwidth_minimum: Set the minimum inbandwidth threshold
            for applying speedtest results on shaping-profile. (optional)
            expected_inbandwidth_maximum: Set the maximum inbandwidth threshold
            for applying speedtest results on shaping-profile. (optional)
            expected_outbandwidth_minimum: Set the minimum outbandwidth
            threshold for applying speedtest results on shaping-profile.
            (optional)
            expected_outbandwidth_maximum: Set the maximum outbandwidth
            threshold for applying speedtest results on shaping-profile.
            (optional)
            retries: Maximum number of times the FortiGate unit will attempt to
            contact the same server before considering the speed test has
            failed (1 - 10, default = 5). (optional)
            retry_pause: Number of seconds the FortiGate pauses between
            successive speed tests before trying a different server (60 - 3600,
            default = 300). (optional)
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
        endpoint = "/system/speed-test-schedule"
        if nkey is not None:
            data_payload["nkey"] = nkey
        if interface is not None:
            data_payload["interface"] = interface
        if status is not None:
            data_payload["status"] = status
        if diffserv is not None:
            data_payload["diffserv"] = diffserv
        if server_name is not None:
            data_payload["server-name"] = server_name
        if mode is not None:
            data_payload["mode"] = mode
        if schedules is not None:
            data_payload["schedules"] = schedules
        if dynamic_server is not None:
            data_payload["dynamic-server"] = dynamic_server
        if ctrl_port is not None:
            data_payload["ctrl-port"] = ctrl_port
        if server_port is not None:
            data_payload["server-port"] = server_port
        if update_shaper is not None:
            data_payload["update-shaper"] = update_shaper
        if update_inbandwidth is not None:
            data_payload["update-inbandwidth"] = update_inbandwidth
        if update_outbandwidth is not None:
            data_payload["update-outbandwidth"] = update_outbandwidth
        if update_interface_shaping is not None:
            data_payload["update-interface-shaping"] = update_interface_shaping
        if update_inbandwidth_maximum is not None:
            data_payload["update-inbandwidth-maximum"] = (
                update_inbandwidth_maximum
            )
        if update_inbandwidth_minimum is not None:
            data_payload["update-inbandwidth-minimum"] = (
                update_inbandwidth_minimum
            )
        if update_outbandwidth_maximum is not None:
            data_payload["update-outbandwidth-maximum"] = (
                update_outbandwidth_maximum
            )
        if update_outbandwidth_minimum is not None:
            data_payload["update-outbandwidth-minimum"] = (
                update_outbandwidth_minimum
            )
        if expected_inbandwidth_minimum is not None:
            data_payload["expected-inbandwidth-minimum"] = (
                expected_inbandwidth_minimum
            )
        if expected_inbandwidth_maximum is not None:
            data_payload["expected-inbandwidth-maximum"] = (
                expected_inbandwidth_maximum
            )
        if expected_outbandwidth_minimum is not None:
            data_payload["expected-outbandwidth-minimum"] = (
                expected_outbandwidth_minimum
            )
        if expected_outbandwidth_maximum is not None:
            data_payload["expected-outbandwidth-maximum"] = (
                expected_outbandwidth_maximum
            )
        if retries is not None:
            data_payload["retries"] = retries
        if retry_pause is not None:
            data_payload["retry-pause"] = retry_pause
        data_payload.update(kwargs)
        return self._client.post(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )
