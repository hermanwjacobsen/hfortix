"""
FortiOS CMDB - Cmdb Wireless Controller Setting

Configuration endpoint for managing cmdb wireless controller setting objects.

API Endpoints:
    GET    /cmdb/wireless-controller/setting
    PUT    /cmdb/wireless-controller/setting/{identifier}

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.wireless_controller.setting.get()
    >>>
    >>> # Get specific item (if supported)
    >>> item = fgt.api.cmdb.wireless_controller.setting.get(name="item_name")
    >>>
    >>> # Create new item (use POST)
    >>> result = fgt.api.cmdb.wireless_controller.setting.post(
    ...     name="new_item",
    ...     # ... additional parameters
    ... )
    >>>
    >>> # Update existing item (use PUT)
    >>> result = fgt.api.cmdb.wireless_controller.setting.put(
    ...     name="existing_item",
    ...     # ... parameters to update
    ... )
    >>>
    >>> # Delete item
    >>> result =
    fgt.api.cmdb.wireless_controller.setting.delete(name="item_name")

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


class Setting:
    """
    Setting Operations.

    Provides CRUD operations for FortiOS setting configuration.

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
        Initialize Setting endpoint.

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
        endpoint = "/wireless-controller/setting"
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
        account_id: str | None = None,
        country: str | None = None,
        duplicate_ssid: str | None = None,
        fapc_compatibility: str | None = None,
        wfa_compatibility: str | None = None,
        phishing_ssid_detect: str | None = None,
        fake_ssid_action: str | None = None,
        offending_ssid: list | None = None,
        device_weight: int | None = None,
        device_holdoff: int | None = None,
        device_idle: int | None = None,
        firmware_provision_on_authorization: str | None = None,
        rolling_wtp_upgrade: str | None = None,
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
            before: If *action=move*, use *before* to specify the ID of the
            resource that this resource will be moved before. (optional)
            after: If *action=move*, use *after* to specify the ID of the
            resource that this resource will be moved after. (optional)
            account_id: FortiCloud customer account ID. (optional)
            country: Country or region in which the FortiGate is located. The
            country determines the 802.11 bands and channels that are
            available. (optional)
            duplicate_ssid: Enable/disable allowing Virtual Access Points
            (VAPs) to use the same SSID name in the same VDOM. (optional)
            fapc_compatibility: Enable/disable FAP-C series compatibility.
            (optional)
            wfa_compatibility: Enable/disable WFA compatibility. (optional)
            phishing_ssid_detect: Enable/disable phishing SSID detection.
            (optional)
            fake_ssid_action: Actions taken for detected fake SSID. (optional)
            offending_ssid: Configure offending SSID. (optional)
            device_weight: Upper limit of confidence of device for
            identification (0 - 255, default = 1, 0 = disable). (optional)
            device_holdoff: Lower limit of creation time of device for
            identification in minutes (0 - 60, default = 5). (optional)
            device_idle: Upper limit of idle time of device for identification
            in minutes (0 - 14400, default = 1440). (optional)
            firmware_provision_on_authorization: Enable/disable automatic
            provisioning of latest firmware on authorization. (optional)
            rolling_wtp_upgrade: Enable/disable rolling WTP upgrade (default =
            disable). (optional)
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
        endpoint = "/wireless-controller/setting"
        if before is not None:
            data_payload["before"] = before
        if after is not None:
            data_payload["after"] = after
        if account_id is not None:
            data_payload["account-id"] = account_id
        if country is not None:
            data_payload["country"] = country
        if duplicate_ssid is not None:
            data_payload["duplicate-ssid"] = duplicate_ssid
        if fapc_compatibility is not None:
            data_payload["fapc-compatibility"] = fapc_compatibility
        if wfa_compatibility is not None:
            data_payload["wfa-compatibility"] = wfa_compatibility
        if phishing_ssid_detect is not None:
            data_payload["phishing-ssid-detect"] = phishing_ssid_detect
        if fake_ssid_action is not None:
            data_payload["fake-ssid-action"] = fake_ssid_action
        if offending_ssid is not None:
            data_payload["offending-ssid"] = offending_ssid
        if device_weight is not None:
            data_payload["device-weight"] = device_weight
        if device_holdoff is not None:
            data_payload["device-holdof"] = device_holdoff
        if device_idle is not None:
            data_payload["device-idle"] = device_idle
        if firmware_provision_on_authorization is not None:
            data_payload["firmware-provision-on-authorization"] = (
                firmware_provision_on_authorization
            )
        if rolling_wtp_upgrade is not None:
            data_payload["rolling-wtp-upgrade"] = rolling_wtp_upgrade
        if darrp_optimize is not None:
            data_payload["darrp-optimize"] = darrp_optimize
        if darrp_optimize_schedules is not None:
            data_payload["darrp-optimize-schedules"] = darrp_optimize_schedules
        data_payload.update(kwargs)
        return self._client.put(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )
