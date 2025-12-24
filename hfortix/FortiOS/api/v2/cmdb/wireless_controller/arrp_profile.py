"""
FortiOS CMDB - Cmdb Wireless Controller Arrp Profile

Configuration endpoint for managing cmdb wireless controller arrp profile
objects.

API Endpoints:
    GET    /cmdb/wireless-controller/arrp_profile
    POST   /cmdb/wireless-controller/arrp_profile
    GET    /cmdb/wireless-controller/arrp_profile
    PUT    /cmdb/wireless-controller/arrp_profile/{identifier}
    DELETE /cmdb/wireless-controller/arrp_profile/{identifier}

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.wireless_controller.arrp_profile.get()
    >>>
    >>> # Get specific item (if supported)
    >>> item =
    fgt.api.cmdb.wireless_controller.arrp_profile.get(name="item_name")
    >>>
    >>> # Create new item (use POST)
    >>> result = fgt.api.cmdb.wireless_controller.arrp_profile.post(
    ...     name="new_item",
    ...     # ... additional parameters
    ... )
    >>>
    >>> # Update existing item (use PUT)
    >>> result = fgt.api.cmdb.wireless_controller.arrp_profile.put(
    ...     name="existing_item",
    ...     # ... parameters to update
    ... )
    >>>
    >>> # Delete item
    >>> result =
    fgt.api.cmdb.wireless_controller.arrp_profile.delete(name="item_name")

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


class ArrpProfile:
    """
    Arrpprofile Operations.

    Provides CRUD operations for FortiOS arrpprofile configuration.

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
        Initialize ArrpProfile endpoint.

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
            endpoint = f"/wireless-controller/arrp-profile/{name}"
        else:
            endpoint = "/wireless-controller/arrp-profile"
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
        comment: str | None = None,
        selection_period: int | None = None,
        monitor_period: int | None = None,
        weight_managed_ap: int | None = None,
        weight_rogue_ap: int | None = None,
        weight_noise_floor: int | None = None,
        weight_channel_load: int | None = None,
        weight_spectral_rssi: int | None = None,
        weight_weather_channel: int | None = None,
        weight_dfs_channel: int | None = None,
        threshold_ap: int | None = None,
        threshold_noise_floor: str | None = None,
        threshold_channel_load: int | None = None,
        threshold_spectral_rssi: str | None = None,
        threshold_tx_retries: int | None = None,
        threshold_rx_errors: int | None = None,
        include_weather_channel: str | None = None,
        include_dfs_channel: str | None = None,
        override_darrp_optimize: str | None = None,
        darrp_optimize: int | None = None,
        darrp_optimize_schedules: list | None = None,
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
            name: WiFi ARRP profile name. (optional)
            comment: Comment. (optional)
            selection_period: Period in seconds to measure average channel
            load, noise floor, spectral RSSI (default = 3600). (optional)
            monitor_period: Period in seconds to measure average transmit
            retries and receive errors (default = 300). (optional)
            weight_managed_ap: Weight in DARRP channel score calculation for
            managed APs (0 - 2000, default = 50). (optional)
            weight_rogue_ap: Weight in DARRP channel score calculation for
            rogue APs (0 - 2000, default = 10). (optional)
            weight_noise_floor: Weight in DARRP channel score calculation for
            noise floor (0 - 2000, default = 40). (optional)
            weight_channel_load: Weight in DARRP channel score calculation for
            channel load (0 - 2000, default = 20). (optional)
            weight_spectral_rssi: Weight in DARRP channel score calculation for
            spectral RSSI (0 - 2000, default = 40). (optional)
            weight_weather_channel: Weight in DARRP channel score calculation
            for weather channel (0 - 2000, default = 0). (optional)
            weight_dfs_channel: Weight in DARRP channel score calculation for
            DFS channel (0 - 2000, default = 0). (optional)
            threshold_ap: Threshold to reject channel in DARRP channel
            selection phase 1 due to surrounding APs (0 - 500, default = 250).
            (optional)
            threshold_noise_floor: Threshold in dBm to reject channel in DARRP
            channel selection phase 1 due to noise floor (-95 to -20, default =
            -85). (optional)
            threshold_channel_load: Threshold in percentage to reject channel
            in DARRP channel selection phase 1 due to channel load (0 - 100,
            default = 60). (optional)
            threshold_spectral_rssi: Threshold in dBm to reject channel in
            DARRP channel selection phase 1 due to spectral RSSI (-95 to -20,
            default = -65). (optional)
            threshold_tx_retries: Threshold in percentage for transmit retries
            to trigger channel reselection in DARRP monitor stage (0 - 1000,
            default = 300). (optional)
            threshold_rx_errors: Threshold in percentage for receive errors to
            trigger channel reselection in DARRP monitor stage (0 - 100,
            default = 50). (optional)
            include_weather_channel: Enable/disable use of weather channel in
            DARRP channel selection phase 1 (default = enable). (optional)
            include_dfs_channel: Enable/disable use of DFS channel in DARRP
            channel selection phase 1 (default = enable). (optional)
            override_darrp_optimize: Enable to override setting darrp-optimize
            and darrp-optimize-schedules (default = disable). (optional)
            darrp_optimize: Time for running Distributed Automatic Radio
            Resource Provisioning (DARRP) optimizations (0 - 86400 sec, default
            = 86400, 0 = disable). (optional)
            darrp_optimize_schedules: Firewall schedules for DARRP running
            time. DARRP will run periodically based on darrp-optimize within
            the schedules. Separate multiple schedule names with a space.
            (optional)
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
        endpoint = f"/wireless-controller/arrp-profile/{name}"
        if before is not None:
            data_payload["before"] = before
        if after is not None:
            data_payload["after"] = after
        if name is not None:
            data_payload["name"] = name
        if comment is not None:
            data_payload["comment"] = comment
        if selection_period is not None:
            data_payload["selection-period"] = selection_period
        if monitor_period is not None:
            data_payload["monitor-period"] = monitor_period
        if weight_managed_ap is not None:
            data_payload["weight-managed-ap"] = weight_managed_ap
        if weight_rogue_ap is not None:
            data_payload["weight-rogue-ap"] = weight_rogue_ap
        if weight_noise_floor is not None:
            data_payload["weight-noise-floor"] = weight_noise_floor
        if weight_channel_load is not None:
            data_payload["weight-channel-load"] = weight_channel_load
        if weight_spectral_rssi is not None:
            data_payload["weight-spectral-rssi"] = weight_spectral_rssi
        if weight_weather_channel is not None:
            data_payload["weight-weather-channel"] = weight_weather_channel
        if weight_dfs_channel is not None:
            data_payload["weight-dfs-channel"] = weight_dfs_channel
        if threshold_ap is not None:
            data_payload["threshold-ap"] = threshold_ap
        if threshold_noise_floor is not None:
            data_payload["threshold-noise-floor"] = threshold_noise_floor
        if threshold_channel_load is not None:
            data_payload["threshold-channel-load"] = threshold_channel_load
        if threshold_spectral_rssi is not None:
            data_payload["threshold-spectral-rssi"] = threshold_spectral_rssi
        if threshold_tx_retries is not None:
            data_payload["threshold-tx-retries"] = threshold_tx_retries
        if threshold_rx_errors is not None:
            data_payload["threshold-rx-errors"] = threshold_rx_errors
        if include_weather_channel is not None:
            data_payload["include-weather-channel"] = include_weather_channel
        if include_dfs_channel is not None:
            data_payload["include-dfs-channel"] = include_dfs_channel
        if override_darrp_optimize is not None:
            data_payload["override-darrp-optimize"] = override_darrp_optimize
        if darrp_optimize is not None:
            data_payload["darrp-optimize"] = darrp_optimize
        if darrp_optimize_schedules is not None:
            data_payload["darrp-optimize-schedules"] = darrp_optimize_schedules
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
        endpoint = f"/wireless-controller/arrp-profile/{name}"
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
        comment: str | None = None,
        selection_period: int | None = None,
        monitor_period: int | None = None,
        weight_managed_ap: int | None = None,
        weight_rogue_ap: int | None = None,
        weight_noise_floor: int | None = None,
        weight_channel_load: int | None = None,
        weight_spectral_rssi: int | None = None,
        weight_weather_channel: int | None = None,
        weight_dfs_channel: int | None = None,
        threshold_ap: int | None = None,
        threshold_noise_floor: str | None = None,
        threshold_channel_load: int | None = None,
        threshold_spectral_rssi: str | None = None,
        threshold_tx_retries: int | None = None,
        threshold_rx_errors: int | None = None,
        include_weather_channel: str | None = None,
        include_dfs_channel: str | None = None,
        override_darrp_optimize: str | None = None,
        darrp_optimize: int | None = None,
        darrp_optimize_schedules: list | None = None,
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
            name: WiFi ARRP profile name. (optional)
            comment: Comment. (optional)
            selection_period: Period in seconds to measure average channel
            load, noise floor, spectral RSSI (default = 3600). (optional)
            monitor_period: Period in seconds to measure average transmit
            retries and receive errors (default = 300). (optional)
            weight_managed_ap: Weight in DARRP channel score calculation for
            managed APs (0 - 2000, default = 50). (optional)
            weight_rogue_ap: Weight in DARRP channel score calculation for
            rogue APs (0 - 2000, default = 10). (optional)
            weight_noise_floor: Weight in DARRP channel score calculation for
            noise floor (0 - 2000, default = 40). (optional)
            weight_channel_load: Weight in DARRP channel score calculation for
            channel load (0 - 2000, default = 20). (optional)
            weight_spectral_rssi: Weight in DARRP channel score calculation for
            spectral RSSI (0 - 2000, default = 40). (optional)
            weight_weather_channel: Weight in DARRP channel score calculation
            for weather channel (0 - 2000, default = 0). (optional)
            weight_dfs_channel: Weight in DARRP channel score calculation for
            DFS channel (0 - 2000, default = 0). (optional)
            threshold_ap: Threshold to reject channel in DARRP channel
            selection phase 1 due to surrounding APs (0 - 500, default = 250).
            (optional)
            threshold_noise_floor: Threshold in dBm to reject channel in DARRP
            channel selection phase 1 due to noise floor (-95 to -20, default =
            -85). (optional)
            threshold_channel_load: Threshold in percentage to reject channel
            in DARRP channel selection phase 1 due to channel load (0 - 100,
            default = 60). (optional)
            threshold_spectral_rssi: Threshold in dBm to reject channel in
            DARRP channel selection phase 1 due to spectral RSSI (-95 to -20,
            default = -65). (optional)
            threshold_tx_retries: Threshold in percentage for transmit retries
            to trigger channel reselection in DARRP monitor stage (0 - 1000,
            default = 300). (optional)
            threshold_rx_errors: Threshold in percentage for receive errors to
            trigger channel reselection in DARRP monitor stage (0 - 100,
            default = 50). (optional)
            include_weather_channel: Enable/disable use of weather channel in
            DARRP channel selection phase 1 (default = enable). (optional)
            include_dfs_channel: Enable/disable use of DFS channel in DARRP
            channel selection phase 1 (default = enable). (optional)
            override_darrp_optimize: Enable to override setting darrp-optimize
            and darrp-optimize-schedules (default = disable). (optional)
            darrp_optimize: Time for running Distributed Automatic Radio
            Resource Provisioning (DARRP) optimizations (0 - 86400 sec, default
            = 86400, 0 = disable). (optional)
            darrp_optimize_schedules: Firewall schedules for DARRP running
            time. DARRP will run periodically based on darrp-optimize within
            the schedules. Separate multiple schedule names with a space.
            (optional)
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
        endpoint = "/wireless-controller/arrp-profile"
        if nkey is not None:
            data_payload["nkey"] = nkey
        if name is not None:
            data_payload["name"] = name
        if comment is not None:
            data_payload["comment"] = comment
        if selection_period is not None:
            data_payload["selection-period"] = selection_period
        if monitor_period is not None:
            data_payload["monitor-period"] = monitor_period
        if weight_managed_ap is not None:
            data_payload["weight-managed-ap"] = weight_managed_ap
        if weight_rogue_ap is not None:
            data_payload["weight-rogue-ap"] = weight_rogue_ap
        if weight_noise_floor is not None:
            data_payload["weight-noise-floor"] = weight_noise_floor
        if weight_channel_load is not None:
            data_payload["weight-channel-load"] = weight_channel_load
        if weight_spectral_rssi is not None:
            data_payload["weight-spectral-rssi"] = weight_spectral_rssi
        if weight_weather_channel is not None:
            data_payload["weight-weather-channel"] = weight_weather_channel
        if weight_dfs_channel is not None:
            data_payload["weight-dfs-channel"] = weight_dfs_channel
        if threshold_ap is not None:
            data_payload["threshold-ap"] = threshold_ap
        if threshold_noise_floor is not None:
            data_payload["threshold-noise-floor"] = threshold_noise_floor
        if threshold_channel_load is not None:
            data_payload["threshold-channel-load"] = threshold_channel_load
        if threshold_spectral_rssi is not None:
            data_payload["threshold-spectral-rssi"] = threshold_spectral_rssi
        if threshold_tx_retries is not None:
            data_payload["threshold-tx-retries"] = threshold_tx_retries
        if threshold_rx_errors is not None:
            data_payload["threshold-rx-errors"] = threshold_rx_errors
        if include_weather_channel is not None:
            data_payload["include-weather-channel"] = include_weather_channel
        if include_dfs_channel is not None:
            data_payload["include-dfs-channel"] = include_dfs_channel
        if override_darrp_optimize is not None:
            data_payload["override-darrp-optimize"] = override_darrp_optimize
        if darrp_optimize is not None:
            data_payload["darrp-optimize"] = darrp_optimize
        if darrp_optimize_schedules is not None:
            data_payload["darrp-optimize-schedules"] = darrp_optimize_schedules
        data_payload.update(kwargs)
        return self._client.post(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )
