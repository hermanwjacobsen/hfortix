"""
FortiOS CMDB - Cmdb System Device Upgrade

Configuration endpoint for managing cmdb system device upgrade objects.

API Endpoints:
    GET    /cmdb/system/device_upgrade
    POST   /cmdb/system/device_upgrade
    GET    /cmdb/system/device_upgrade
    PUT    /cmdb/system/device_upgrade/{identifier}
    DELETE /cmdb/system/device_upgrade/{identifier}

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.system.device_upgrade.get()
    >>>
    >>> # Get specific item (if supported)
    >>> item = fgt.api.cmdb.system.device_upgrade.get(name="item_name")
    >>>
    >>> # Create new item (use POST)
    >>> result = fgt.api.cmdb.system.device_upgrade.post(
    ...     name="new_item",
    ...     # ... additional parameters
    ... )
    >>>
    >>> # Update existing item (use PUT)
    >>> result = fgt.api.cmdb.system.device_upgrade.put(
    ...     name="existing_item",
    ...     # ... parameters to update
    ... )
    >>>
    >>> # Delete item
    >>> result = fgt.api.cmdb.system.device_upgrade.delete(name="item_name")

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


class DeviceUpgrade:
    """
    Deviceupgrade Operations.

    Provides CRUD operations for FortiOS deviceupgrade configuration.

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
        Initialize DeviceUpgrade endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

    def get(
        self,
        serial: str | None = None,
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
            serial: Object identifier (optional for list, required for
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
        if serial:
            endpoint = f"/system/device-upgrade/{serial}"
        else:
            endpoint = "/system/device-upgrade"
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
        serial: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        before: str | None = None,
        after: str | None = None,
        status: str | None = None,
        ha_reboot_controller: str | None = None,
        next_path_index: int | None = None,
        known_ha_members: list | None = None,
        initial_version: str | None = None,
        starter_admin: str | None = None,
        timing: str | None = None,
        maximum_minutes: int | None = None,
        time: str | None = None,
        setup_time: str | None = None,
        upgrade_path: str | None = None,
        device_type: str | None = None,
        allow_download: str | None = None,
        failure_reason: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update this specific resource.

        Args:
            payload_dict: Optional dictionary of all parameters (can be passed
            as first positional arg)
            serial: Object identifier (required)
            before: If *action=move*, use *before* to specify the ID of the
            resource that this resource will be moved before. (optional)
            after: If *action=move*, use *after* to specify the ID of the
            resource that this resource will be moved after. (optional)
            status: Current status of the upgrade. (optional)
            ha_reboot_controller: Serial number of the FortiGate unit that will
            control the reboot process for the federated upgrade of the HA
            cluster. (optional)
            next_path_index: The index of the next image to upgrade to.
            (optional)
            known_ha_members: Known members of the HA cluster. If a member is
            missing at upgrade time, the upgrade will be cancelled. (optional)
            initial_version: Firmware version when the upgrade was set up.
            (optional)
            starter_admin: Admin that started the upgrade. (optional)
            serial: Serial number of the node to include. (optional)
            timing: Run immediately or at a scheduled time. (optional)
            maximum_minutes: Maximum number of minutes to allow for immediate
            upgrade preparation. (optional)
            time: Scheduled upgrade execution time in UTC (hh:mm yyyy/mm/dd
            UTC). (optional)
            setup_time: Upgrade preparation start time in UTC (hh:mm yyyy/mm/dd
            UTC). (optional)
            upgrade_path: Fortinet OS image versions to upgrade through in
            major-minor-patch format, such as 7-0-4. (optional)
            device_type: Fortinet device type. (optional)
            allow_download: Enable/disable download firmware images. (optional)
            failure_reason: Upgrade failure reason. (optional)
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
        if not serial:
            raise ValueError("serial is required for put()")
        endpoint = f"/system/device-upgrade/{serial}"
        if before is not None:
            data_payload["before"] = before
        if after is not None:
            data_payload["after"] = after
        if status is not None:
            data_payload["status"] = status
        if ha_reboot_controller is not None:
            data_payload["ha-reboot-controller"] = ha_reboot_controller
        if next_path_index is not None:
            data_payload["next-path-index"] = next_path_index
        if known_ha_members is not None:
            data_payload["known-ha-members"] = known_ha_members
        if initial_version is not None:
            data_payload["initial-version"] = initial_version
        if starter_admin is not None:
            data_payload["starter-admin"] = starter_admin
        if serial is not None:
            data_payload["serial"] = serial
        if timing is not None:
            data_payload["timing"] = timing
        if maximum_minutes is not None:
            data_payload["maximum-minutes"] = maximum_minutes
        if time is not None:
            data_payload["time"] = time
        if setup_time is not None:
            data_payload["setup-time"] = setup_time
        if upgrade_path is not None:
            data_payload["upgrade-path"] = upgrade_path
        if device_type is not None:
            data_payload["device-type"] = device_type
        if allow_download is not None:
            data_payload["allow-download"] = allow_download
        if failure_reason is not None:
            data_payload["failure-reason"] = failure_reason
        data_payload.update(kwargs)
        return self._client.put(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )

    def delete(
        self,
        serial: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Delete this specific resource.

        Args:
            serial: Object identifier (required)
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
        if not serial:
            raise ValueError("serial is required for delete()")
        endpoint = f"/system/device-upgrade/{serial}"
        params.update(kwargs)
        return self._client.delete(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )

    def post(
        self,
        payload_dict: dict[str, Any] | None = None,
        nkey: str | None = None,
        status: str | None = None,
        ha_reboot_controller: str | None = None,
        next_path_index: int | None = None,
        known_ha_members: list | None = None,
        initial_version: str | None = None,
        starter_admin: str | None = None,
        serial: str | None = None,
        timing: str | None = None,
        maximum_minutes: int | None = None,
        time: str | None = None,
        setup_time: str | None = None,
        upgrade_path: str | None = None,
        device_type: str | None = None,
        allow_download: str | None = None,
        failure_reason: str | None = None,
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
            status: Current status of the upgrade. (optional)
            ha_reboot_controller: Serial number of the FortiGate unit that will
            control the reboot process for the federated upgrade of the HA
            cluster. (optional)
            next_path_index: The index of the next image to upgrade to.
            (optional)
            known_ha_members: Known members of the HA cluster. If a member is
            missing at upgrade time, the upgrade will be cancelled. (optional)
            initial_version: Firmware version when the upgrade was set up.
            (optional)
            starter_admin: Admin that started the upgrade. (optional)
            serial: Serial number of the node to include. (optional)
            timing: Run immediately or at a scheduled time. (optional)
            maximum_minutes: Maximum number of minutes to allow for immediate
            upgrade preparation. (optional)
            time: Scheduled upgrade execution time in UTC (hh:mm yyyy/mm/dd
            UTC). (optional)
            setup_time: Upgrade preparation start time in UTC (hh:mm yyyy/mm/dd
            UTC). (optional)
            upgrade_path: Fortinet OS image versions to upgrade through in
            major-minor-patch format, such as 7-0-4. (optional)
            device_type: Fortinet device type. (optional)
            allow_download: Enable/disable download firmware images. (optional)
            failure_reason: Upgrade failure reason. (optional)
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
        endpoint = "/system/device-upgrade"
        if nkey is not None:
            data_payload["nkey"] = nkey
        if status is not None:
            data_payload["status"] = status
        if ha_reboot_controller is not None:
            data_payload["ha-reboot-controller"] = ha_reboot_controller
        if next_path_index is not None:
            data_payload["next-path-index"] = next_path_index
        if known_ha_members is not None:
            data_payload["known-ha-members"] = known_ha_members
        if initial_version is not None:
            data_payload["initial-version"] = initial_version
        if starter_admin is not None:
            data_payload["starter-admin"] = starter_admin
        if serial is not None:
            data_payload["serial"] = serial
        if timing is not None:
            data_payload["timing"] = timing
        if maximum_minutes is not None:
            data_payload["maximum-minutes"] = maximum_minutes
        if time is not None:
            data_payload["time"] = time
        if setup_time is not None:
            data_payload["setup-time"] = setup_time
        if upgrade_path is not None:
            data_payload["upgrade-path"] = upgrade_path
        if device_type is not None:
            data_payload["device-type"] = device_type
        if allow_download is not None:
            data_payload["allow-download"] = allow_download
        if failure_reason is not None:
            data_payload["failure-reason"] = failure_reason
        data_payload.update(kwargs)
        return self._client.post(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )
