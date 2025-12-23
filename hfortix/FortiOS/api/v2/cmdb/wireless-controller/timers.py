"""
FortiOS CMDB - Cmdb Wireless Controller Timers

Configuration endpoint for managing cmdb wireless controller timers objects.

API Endpoints:
    GET    /cmdb/wireless-controller/timers
    PUT    /cmdb/wireless-controller/timers/{identifier}

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.wireless_controller.timers.get()
    >>>
    >>> # Get specific item (if supported)
    >>> item = fgt.api.cmdb.wireless_controller.timers.get(name="item_name")
    >>>
    >>> # Create new item (use POST)
    >>> result = fgt.api.cmdb.wireless_controller.timers.post(
    ...     name="new_item",
    ...     # ... additional parameters
    ... )
    >>>
    >>> # Update existing item (use PUT)
    >>> result = fgt.api.cmdb.wireless_controller.timers.put(
    ...     name="existing_item",
    ...     # ... parameters to update
    ... )
    >>>
    >>> # Delete item
    >>> result =
    fgt.api.cmdb.wireless_controller.timers.delete(name="item_name")

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


class Timers:
    """
    Timers Operations.

    Provides CRUD operations for FortiOS timers configuration.

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
        Initialize Timers endpoint.

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
        endpoint = "/wireless-controller/timers"
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
        echo_interval: int | None = None,
        nat_session_keep_alive: int | None = None,
        discovery_interval: int | None = None,
        client_idle_timeout: int | None = None,
        client_idle_rehome_timeout: int | None = None,
        auth_timeout: int | None = None,
        rogue_ap_log: int | None = None,
        fake_ap_log: int | None = None,
        sta_offline_cleanup: int | None = None,
        sta_offline_ip2mac_cleanup: int | None = None,
        sta_cap_cleanup: int | None = None,
        rogue_ap_cleanup: int | None = None,
        rogue_sta_cleanup: int | None = None,
        wids_entry_cleanup: int | None = None,
        ble_device_cleanup: int | None = None,
        sta_stats_interval: int | None = None,
        vap_stats_interval: int | None = None,
        radio_stats_interval: int | None = None,
        sta_capability_interval: int | None = None,
        sta_locate_timer: int | None = None,
        ipsec_intf_cleanup: int | None = None,
        ble_scan_report_intv: int | None = None,
        drma_interval: int | None = None,
        ap_reboot_wait_interval1: int | None = None,
        ap_reboot_wait_time: str | None = None,
        ap_reboot_wait_interval2: int | None = None,
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
            echo_interval: Time between echo requests sent by the managed WTP,
            AP, or FortiAP (1 - 255 sec, default = 30). (optional)
            nat_session_keep_alive: Maximal time in seconds between control
            requests sent by the managed WTP, AP, or FortiAP (0 - 255 sec,
            default = 0). (optional)
            discovery_interval: Time between discovery requests (2 - 180 sec,
            default = 5). (optional)
            client_idle_timeout: Time after which a client is considered idle
            and times out (20 - 3600 sec, default = 300, 0 for no timeout).
            (optional)
            client_idle_rehome_timeout: Time after which a client is considered
            idle and disconnected from the home controller (2 - 3600 sec,
            default = 20, 0 for no timeout). (optional)
            auth_timeout: Time after which a client is considered failed in
            RADIUS authentication and times out (5 - 30 sec, default = 5).
            (optional)
            rogue_ap_log: Time between logging rogue AP messages if periodic
            rogue AP logging is configured (0 - 1440 min, default = 0).
            (optional)
            fake_ap_log: Time between recording logs about fake APs if periodic
            fake AP logging is configured (1 - 1440 min, default = 1).
            (optional)
            sta_offline_cleanup: Time period in seconds to keep station offline
            data after it is gone (default = 300). (optional)
            sta_offline_ip2mac_cleanup: Time period in seconds to keep station
            offline Ip2mac data after it is gone (default = 300). (optional)
            sta_cap_cleanup: Time period in minutes to keep station capability
            data after it is gone (default = 0). (optional)
            rogue_ap_cleanup: Time period in minutes to keep rogue AP after it
            is gone (default = 0). (optional)
            rogue_sta_cleanup: Time period in minutes to keep rogue station
            after it is gone (default = 0). (optional)
            wids_entry_cleanup: Time period in minutes to keep wids entry after
            it is gone (default = 0). (optional)
            ble_device_cleanup: Time period in minutes to keep BLE device after
            it is gone (default = 60). (optional)
            sta_stats_interval: Time between running client (station) reports
            (1 - 255 sec, default = 10). (optional)
            vap_stats_interval: Time between running Virtual Access Point (VAP)
            reports (1 - 255 sec, default = 15). (optional)
            radio_stats_interval: Time between running radio reports (1 - 255
            sec, default = 15). (optional)
            sta_capability_interval: Time between running station capability
            reports (1 - 255 sec, default = 30). (optional)
            sta_locate_timer: Time between running client presence flushes to
            remove clients that are listed but no longer present (0 - 86400
            sec, default = 1800). (optional)
            ipsec_intf_cleanup: Time period to keep IPsec VPN interfaces up
            after WTP sessions are disconnected (30 - 3600 sec, default = 120).
            (optional)
            ble_scan_report_intv: Time between running Bluetooth Low Energy
            (BLE) reports (10 - 3600 sec, default = 30). (optional)
            drma_interval: Dynamic radio mode assignment (DRMA) schedule
            interval in minutes (1 - 1440, default = 60). (optional)
            ap_reboot_wait_interval1: Time in minutes to wait before AP reboots
            when there is no controller detected (5 - 65535, default = 0, 0 for
            no reboot). (optional)
            ap_reboot_wait_time: Time to reboot the AP when there is no
            controller detected and standalone SSIDs are pushed to the AP in
            the previous session, format hh:mm. (optional)
            ap_reboot_wait_interval2: Time in minutes to wait before AP reboots
            when there is no controller detected and standalone SSIDs are
            pushed to the AP in the previous session (5 - 65535, default = 0, 0
            for no reboot). (optional)
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
        endpoint = "/wireless-controller/timers"
        if before is not None:
            data_payload["before"] = before
        if after is not None:
            data_payload["after"] = after
        if echo_interval is not None:
            data_payload["echo-interval"] = echo_interval
        if nat_session_keep_alive is not None:
            data_payload["nat-session-keep-alive"] = nat_session_keep_alive
        if discovery_interval is not None:
            data_payload["discovery-interval"] = discovery_interval
        if client_idle_timeout is not None:
            data_payload["client-idle-timeout"] = client_idle_timeout
        if client_idle_rehome_timeout is not None:
            data_payload["client-idle-rehome-timeout"] = (
                client_idle_rehome_timeout
            )
        if auth_timeout is not None:
            data_payload["auth-timeout"] = auth_timeout
        if rogue_ap_log is not None:
            data_payload["rogue-ap-log"] = rogue_ap_log
        if fake_ap_log is not None:
            data_payload["fake-ap-log"] = fake_ap_log
        if sta_offline_cleanup is not None:
            data_payload["sta-offline-cleanup"] = sta_offline_cleanup
        if sta_offline_ip2mac_cleanup is not None:
            data_payload["sta-offline-ip2mac-cleanup"] = (
                sta_offline_ip2mac_cleanup
            )
        if sta_cap_cleanup is not None:
            data_payload["sta-cap-cleanup"] = sta_cap_cleanup
        if rogue_ap_cleanup is not None:
            data_payload["rogue-ap-cleanup"] = rogue_ap_cleanup
        if rogue_sta_cleanup is not None:
            data_payload["rogue-sta-cleanup"] = rogue_sta_cleanup
        if wids_entry_cleanup is not None:
            data_payload["wids-entry-cleanup"] = wids_entry_cleanup
        if ble_device_cleanup is not None:
            data_payload["ble-device-cleanup"] = ble_device_cleanup
        if sta_stats_interval is not None:
            data_payload["sta-stats-interval"] = sta_stats_interval
        if vap_stats_interval is not None:
            data_payload["vap-stats-interval"] = vap_stats_interval
        if radio_stats_interval is not None:
            data_payload["radio-stats-interval"] = radio_stats_interval
        if sta_capability_interval is not None:
            data_payload["sta-capability-interval"] = sta_capability_interval
        if sta_locate_timer is not None:
            data_payload["sta-locate-timer"] = sta_locate_timer
        if ipsec_intf_cleanup is not None:
            data_payload["ipsec-intf-cleanup"] = ipsec_intf_cleanup
        if ble_scan_report_intv is not None:
            data_payload["ble-scan-report-intv"] = ble_scan_report_intv
        if drma_interval is not None:
            data_payload["drma-interval"] = drma_interval
        if ap_reboot_wait_interval1 is not None:
            data_payload["ap-reboot-wait-interval1"] = ap_reboot_wait_interval1
        if ap_reboot_wait_time is not None:
            data_payload["ap-reboot-wait-time"] = ap_reboot_wait_time
        if ap_reboot_wait_interval2 is not None:
            data_payload["ap-reboot-wait-interval2"] = ap_reboot_wait_interval2
        data_payload.update(kwargs)
        return self._client.put(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )
