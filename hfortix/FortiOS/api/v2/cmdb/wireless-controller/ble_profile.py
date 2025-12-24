"""
FortiOS CMDB - Cmdb Wireless Controller Ble Profile

Configuration endpoint for managing cmdb wireless controller ble profile
objects.

API Endpoints:
    GET    /cmdb/wireless-controller/ble_profile
    POST   /cmdb/wireless-controller/ble_profile
    GET    /cmdb/wireless-controller/ble_profile
    PUT    /cmdb/wireless-controller/ble_profile/{identifier}
    DELETE /cmdb/wireless-controller/ble_profile/{identifier}

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.wireless_controller.ble_profile.get()
    >>>
    >>> # Get specific item (if supported)
    >>> item =
    fgt.api.cmdb.wireless_controller.ble_profile.get(name="item_name")
    >>>
    >>> # Create new item (use POST)
    >>> result = fgt.api.cmdb.wireless_controller.ble_profile.post(
    ...     name="new_item",
    ...     # ... additional parameters
    ... )
    >>>
    >>> # Update existing item (use PUT)
    >>> result = fgt.api.cmdb.wireless_controller.ble_profile.put(
    ...     name="existing_item",
    ...     # ... parameters to update
    ... )
    >>>
    >>> # Delete item
    >>> result =
    fgt.api.cmdb.wireless_controller.ble_profile.delete(name="item_name")

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


class BleProfile:
    """
    Bleprofile Operations.

    Provides CRUD operations for FortiOS bleprofile configuration.

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
        Initialize BleProfile endpoint.

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
            endpoint = f"/wireless-controller/ble-profile/{name}"
        else:
            endpoint = "/wireless-controller/ble-profile"
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
        advertising: str | None = None,
        ibeacon_uuid: str | None = None,
        major_id: int | None = None,
        minor_id: int | None = None,
        eddystone_namespace: str | None = None,
        eddystone_instance: str | None = None,
        eddystone_url: str | None = None,
        txpower: str | None = None,
        beacon_interval: int | None = None,
        ble_scanning: str | None = None,
        scan_type: str | None = None,
        scan_threshold: str | None = None,
        scan_period: int | None = None,
        scan_time: int | None = None,
        scan_interval: int | None = None,
        scan_window: int | None = None,
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
            name: Bluetooth Low Energy profile name. (optional)
            comment: Comment. (optional)
            advertising: Advertising type. (optional)
            ibeacon_uuid: Universally Unique Identifier (UUID; automatically
            assigned but can be manually reset). (optional)
            major_id: Major ID. (optional)
            minor_id: Minor ID. (optional)
            eddystone_namespace: Eddystone namespace ID. (optional)
            eddystone_instance: Eddystone instance ID. (optional)
            eddystone_url: Eddystone URL. (optional)
            txpower: Transmit power level (default = 0). (optional)
            beacon_interval: Beacon interval (default = 100 msec). (optional)
            ble_scanning: Enable/disable Bluetooth Low Energy (BLE) scanning.
            (optional)
            scan_type: Scan Type (default = active). (optional)
            scan_threshold: Minimum signal level/threshold in dBm required for
            the AP to report detected BLE device (-95 to -20, default = -90).
            (optional)
            scan_period: Scan Period (default = 4000 msec). (optional)
            scan_time: Scan Time (default = 1000 msec). (optional)
            scan_interval: Scan Interval (default = 50 msec). (optional)
            scan_window: Scan Windows (default = 50 msec). (optional)
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
        endpoint = f"/wireless-controller/ble-profile/{name}"
        if before is not None:
            data_payload["before"] = before
        if after is not None:
            data_payload["after"] = after
        if name is not None:
            data_payload["name"] = name
        if comment is not None:
            data_payload["comment"] = comment
        if advertising is not None:
            data_payload["advertising"] = advertising
        if ibeacon_uuid is not None:
            data_payload["ibeacon-uuid"] = ibeacon_uuid
        if major_id is not None:
            data_payload["major-id"] = major_id
        if minor_id is not None:
            data_payload["minor-id"] = minor_id
        if eddystone_namespace is not None:
            data_payload["eddystone-namespace"] = eddystone_namespace
        if eddystone_instance is not None:
            data_payload["eddystone-instance"] = eddystone_instance
        if eddystone_url is not None:
            data_payload["eddystone-url"] = eddystone_url
        if txpower is not None:
            data_payload["txpower"] = txpower
        if beacon_interval is not None:
            data_payload["beacon-interval"] = beacon_interval
        if ble_scanning is not None:
            data_payload["ble-scanning"] = ble_scanning
        if scan_type is not None:
            data_payload["scan-type"] = scan_type
        if scan_threshold is not None:
            data_payload["scan-threshold"] = scan_threshold
        if scan_period is not None:
            data_payload["scan-period"] = scan_period
        if scan_time is not None:
            data_payload["scan-time"] = scan_time
        if scan_interval is not None:
            data_payload["scan-interval"] = scan_interval
        if scan_window is not None:
            data_payload["scan-window"] = scan_window
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
        endpoint = f"/wireless-controller/ble-profile/{name}"
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
        advertising: str | None = None,
        ibeacon_uuid: str | None = None,
        major_id: int | None = None,
        minor_id: int | None = None,
        eddystone_namespace: str | None = None,
        eddystone_instance: str | None = None,
        eddystone_url: str | None = None,
        txpower: str | None = None,
        beacon_interval: int | None = None,
        ble_scanning: str | None = None,
        scan_type: str | None = None,
        scan_threshold: str | None = None,
        scan_period: int | None = None,
        scan_time: int | None = None,
        scan_interval: int | None = None,
        scan_window: int | None = None,
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
            name: Bluetooth Low Energy profile name. (optional)
            comment: Comment. (optional)
            advertising: Advertising type. (optional)
            ibeacon_uuid: Universally Unique Identifier (UUID; automatically
            assigned but can be manually reset). (optional)
            major_id: Major ID. (optional)
            minor_id: Minor ID. (optional)
            eddystone_namespace: Eddystone namespace ID. (optional)
            eddystone_instance: Eddystone instance ID. (optional)
            eddystone_url: Eddystone URL. (optional)
            txpower: Transmit power level (default = 0). (optional)
            beacon_interval: Beacon interval (default = 100 msec). (optional)
            ble_scanning: Enable/disable Bluetooth Low Energy (BLE) scanning.
            (optional)
            scan_type: Scan Type (default = active). (optional)
            scan_threshold: Minimum signal level/threshold in dBm required for
            the AP to report detected BLE device (-95 to -20, default = -90).
            (optional)
            scan_period: Scan Period (default = 4000 msec). (optional)
            scan_time: Scan Time (default = 1000 msec). (optional)
            scan_interval: Scan Interval (default = 50 msec). (optional)
            scan_window: Scan Windows (default = 50 msec). (optional)
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
        endpoint = "/wireless-controller/ble-profile"
        if nkey is not None:
            data_payload["nkey"] = nkey
        if name is not None:
            data_payload["name"] = name
        if comment is not None:
            data_payload["comment"] = comment
        if advertising is not None:
            data_payload["advertising"] = advertising
        if ibeacon_uuid is not None:
            data_payload["ibeacon-uuid"] = ibeacon_uuid
        if major_id is not None:
            data_payload["major-id"] = major_id
        if minor_id is not None:
            data_payload["minor-id"] = minor_id
        if eddystone_namespace is not None:
            data_payload["eddystone-namespace"] = eddystone_namespace
        if eddystone_instance is not None:
            data_payload["eddystone-instance"] = eddystone_instance
        if eddystone_url is not None:
            data_payload["eddystone-url"] = eddystone_url
        if txpower is not None:
            data_payload["txpower"] = txpower
        if beacon_interval is not None:
            data_payload["beacon-interval"] = beacon_interval
        if ble_scanning is not None:
            data_payload["ble-scanning"] = ble_scanning
        if scan_type is not None:
            data_payload["scan-type"] = scan_type
        if scan_threshold is not None:
            data_payload["scan-threshold"] = scan_threshold
        if scan_period is not None:
            data_payload["scan-period"] = scan_period
        if scan_time is not None:
            data_payload["scan-time"] = scan_time
        if scan_interval is not None:
            data_payload["scan-interval"] = scan_interval
        if scan_window is not None:
            data_payload["scan-window"] = scan_window
        data_payload.update(kwargs)
        return self._client.post(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )
