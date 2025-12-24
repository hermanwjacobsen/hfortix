"""
FortiOS CMDB - Cmdb Wireless Controller Wids Profile

Configuration endpoint for managing cmdb wireless controller wids profile
objects.

API Endpoints:
    GET    /cmdb/wireless-controller/wids_profile
    POST   /cmdb/wireless-controller/wids_profile
    GET    /cmdb/wireless-controller/wids_profile
    PUT    /cmdb/wireless-controller/wids_profile/{identifier}
    DELETE /cmdb/wireless-controller/wids_profile/{identifier}

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.wireless_controller.wids_profile.get()
    >>>
    >>> # Get specific item (if supported)
    >>> item =
    fgt.api.cmdb.wireless_controller.wids_profile.get(name="item_name")
    >>>
    >>> # Create new item (use POST)
    >>> result = fgt.api.cmdb.wireless_controller.wids_profile.post(
    ...     name="new_item",
    ...     # ... additional parameters
    ... )
    >>>
    >>> # Update existing item (use PUT)
    >>> result = fgt.api.cmdb.wireless_controller.wids_profile.put(
    ...     name="existing_item",
    ...     # ... parameters to update
    ... )
    >>>
    >>> # Delete item
    >>> result =
    fgt.api.cmdb.wireless_controller.wids_profile.delete(name="item_name")

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


class WidsProfile:
    """
    Widsprofile Operations.

    Provides CRUD operations for FortiOS widsprofile configuration.

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
        Initialize WidsProfile endpoint.

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
            endpoint = f"/wireless-controller/wids-profile/{name}"
        else:
            endpoint = "/wireless-controller/wids-profile"
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
        sensor_mode: str | None = None,
        ap_scan: str | None = None,
        ap_scan_channel_list_2G_5G: list | None = None,
        ap_scan_channel_list_6G: list | None = None,
        ap_bgscan_period: int | None = None,
        ap_bgscan_intv: int | None = None,
        ap_bgscan_duration: int | None = None,
        ap_bgscan_idle: int | None = None,
        ap_bgscan_report_intv: int | None = None,
        ap_bgscan_disable_schedules: list | None = None,
        ap_fgscan_report_intv: int | None = None,
        ap_scan_passive: str | None = None,
        ap_scan_threshold: str | None = None,
        ap_auto_suppress: str | None = None,
        wireless_bridge: str | None = None,
        deauth_broadcast: str | None = None,
        null_ssid_probe_resp: str | None = None,
        long_duration_attack: str | None = None,
        long_duration_thresh: int | None = None,
        invalid_mac_oui: str | None = None,
        weak_wep_iv: str | None = None,
        auth_frame_flood: str | None = None,
        auth_flood_time: int | None = None,
        auth_flood_thresh: int | None = None,
        assoc_frame_flood: str | None = None,
        assoc_flood_time: int | None = None,
        assoc_flood_thresh: int | None = None,
        reassoc_flood: str | None = None,
        reassoc_flood_time: int | None = None,
        reassoc_flood_thresh: int | None = None,
        probe_flood: str | None = None,
        probe_flood_time: int | None = None,
        probe_flood_thresh: int | None = None,
        bcn_flood: str | None = None,
        bcn_flood_time: int | None = None,
        bcn_flood_thresh: int | None = None,
        rts_flood: str | None = None,
        rts_flood_time: int | None = None,
        rts_flood_thresh: int | None = None,
        cts_flood: str | None = None,
        cts_flood_time: int | None = None,
        cts_flood_thresh: int | None = None,
        client_flood: str | None = None,
        client_flood_time: int | None = None,
        client_flood_thresh: int | None = None,
        block_ack_flood: str | None = None,
        block_ack_flood_time: int | None = None,
        block_ack_flood_thresh: int | None = None,
        pspoll_flood: str | None = None,
        pspoll_flood_time: int | None = None,
        pspoll_flood_thresh: int | None = None,
        netstumbler: str | None = None,
        netstumbler_time: int | None = None,
        netstumbler_thresh: int | None = None,
        wellenreiter: str | None = None,
        wellenreiter_time: int | None = None,
        wellenreiter_thresh: int | None = None,
        spoofed_deauth: str | None = None,
        asleap_attack: str | None = None,
        eapol_start_flood: str | None = None,
        eapol_start_thresh: int | None = None,
        eapol_start_intv: int | None = None,
        eapol_logoff_flood: str | None = None,
        eapol_logoff_thresh: int | None = None,
        eapol_logoff_intv: int | None = None,
        eapol_succ_flood: str | None = None,
        eapol_succ_thresh: int | None = None,
        eapol_succ_intv: int | None = None,
        eapol_fail_flood: str | None = None,
        eapol_fail_thresh: int | None = None,
        eapol_fail_intv: int | None = None,
        eapol_pre_succ_flood: str | None = None,
        eapol_pre_succ_thresh: int | None = None,
        eapol_pre_succ_intv: int | None = None,
        eapol_pre_fail_flood: str | None = None,
        eapol_pre_fail_thresh: int | None = None,
        eapol_pre_fail_intv: int | None = None,
        deauth_unknown_src_thresh: int | None = None,
        windows_bridge: str | None = None,
        disassoc_broadcast: str | None = None,
        ap_spoofing: str | None = None,
        chan_based_mitm: str | None = None,
        adhoc_valid_ssid: str | None = None,
        adhoc_network: str | None = None,
        eapol_key_overflow: str | None = None,
        ap_impersonation: str | None = None,
        invalid_addr_combination: str | None = None,
        beacon_wrong_channel: str | None = None,
        ht_greenfield: str | None = None,
        overflow_ie: str | None = None,
        malformed_ht_ie: str | None = None,
        malformed_auth: str | None = None,
        malformed_association: str | None = None,
        ht_40mhz_intolerance: str | None = None,
        valid_ssid_misuse: str | None = None,
        valid_client_misassociation: str | None = None,
        hotspotter_attack: str | None = None,
        pwsave_dos_attack: str | None = None,
        omerta_attack: str | None = None,
        disconnect_station: str | None = None,
        unencrypted_valid: str | None = None,
        fata_jack: str | None = None,
        risky_encryption: str | None = None,
        fuzzed_beacon: str | None = None,
        fuzzed_probe_request: str | None = None,
        fuzzed_probe_response: str | None = None,
        air_jack: str | None = None,
        wpa_ft_attack: str | None = None,
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
            name: WIDS profile name. (optional)
            comment: Comment. (optional)
            sensor_mode: Scan nearby WiFi stations (default = disable).
            (optional)
            ap_scan: Enable/disable rogue AP detection. (optional)
            ap_scan_channel_list_2G_5G: Selected ap scan channel list for 2.4G
            and 5G bands. (optional)
            ap_scan_channel_list_6G: Selected ap scan channel list for 6G band.
            (optional)
            ap_bgscan_period: Period between background scans (10 - 3600 sec,
            default = 600). (optional)
            ap_bgscan_intv: Period between successive channel scans (1 - 600
            sec, default = 3). (optional)
            ap_bgscan_duration: Listen time on scanning a channel (10 - 1000
            msec, default = 30). (optional)
            ap_bgscan_idle: Wait time for channel inactivity before scanning
            this channel (0 - 1000 msec, default = 20). (optional)
            ap_bgscan_report_intv: Period between background scan reports (15 -
            600 sec, default = 30). (optional)
            ap_bgscan_disable_schedules: Firewall schedules for turning off
            FortiAP radio background scan. Background scan will be disabled
            when at least one of the schedules is valid. Separate multiple
            schedule names with a space. (optional)
            ap_fgscan_report_intv: Period between foreground scan reports (15 -
            600 sec, default = 15). (optional)
            ap_scan_passive: Enable/disable passive scanning. Enable means do
            not send probe request on any channels (default = disable).
            (optional)
            ap_scan_threshold: Minimum signal level/threshold in dBm required
            for the AP to report detected rogue AP (-95 to -20, default = -90).
            (optional)
            ap_auto_suppress: Enable/disable on-wire rogue AP auto-suppression
            (default = disable). (optional)
            wireless_bridge: Enable/disable wireless bridge detection (default
            = disable). (optional)
            deauth_broadcast: Enable/disable broadcasting de-authentication
            detection (default = disable). (optional)
            null_ssid_probe_resp: Enable/disable null SSID probe response
            detection (default = disable). (optional)
            long_duration_attack: Enable/disable long duration attack detection
            based on user configured threshold (default = disable). (optional)
            long_duration_thresh: Threshold value for long duration attack
            detection (1000 - 32767 usec, default = 8200). (optional)
            invalid_mac_oui: Enable/disable invalid MAC OUI detection.
            (optional)
            weak_wep_iv: Enable/disable weak WEP IV (Initialization Vector)
            detection (default = disable). (optional)
            auth_frame_flood: Enable/disable authentication frame flooding
            detection (default = disable). (optional)
            auth_flood_time: Number of seconds after which a station is
            considered not connected. (optional)
            auth_flood_thresh: The threshold value for authentication frame
            flooding. (optional)
            assoc_frame_flood: Enable/disable association frame flooding
            detection (default = disable). (optional)
            assoc_flood_time: Number of seconds after which a station is
            considered not connected. (optional)
            assoc_flood_thresh: The threshold value for association frame
            flooding. (optional)
            reassoc_flood: Enable/disable reassociation flood detection
            (default = disable). (optional)
            reassoc_flood_time: Detection Window Period. (optional)
            reassoc_flood_thresh: The threshold value for reassociation flood.
            (optional)
            probe_flood: Enable/disable probe flood detection (default =
            disable). (optional)
            probe_flood_time: Detection Window Period. (optional)
            probe_flood_thresh: The threshold value for probe flood. (optional)
            bcn_flood: Enable/disable bcn flood detection (default = disable).
            (optional)
            bcn_flood_time: Detection Window Period. (optional)
            bcn_flood_thresh: The threshold value for bcn flood. (optional)
            rts_flood: Enable/disable rts flood detection (default = disable).
            (optional)
            rts_flood_time: Detection Window Period. (optional)
            rts_flood_thresh: The threshold value for rts flood. (optional)
            cts_flood: Enable/disable cts flood detection (default = disable).
            (optional)
            cts_flood_time: Detection Window Period. (optional)
            cts_flood_thresh: The threshold value for cts flood. (optional)
            client_flood: Enable/disable client flood detection (default =
            disable). (optional)
            client_flood_time: Detection Window Period. (optional)
            client_flood_thresh: The threshold value for client flood.
            (optional)
            block_ack_flood: Enable/disable block_ack flood detection (default
            = disable). (optional)
            block_ack_flood_time: Detection Window Period. (optional)
            block_ack_flood_thresh: The threshold value for block_ack flood.
            (optional)
            pspoll_flood: Enable/disable pspoll flood detection (default =
            disable). (optional)
            pspoll_flood_time: Detection Window Period. (optional)
            pspoll_flood_thresh: The threshold value for pspoll flood.
            (optional)
            netstumbler: Enable/disable netstumbler detection (default =
            disable). (optional)
            netstumbler_time: Detection Window Period. (optional)
            netstumbler_thresh: The threshold value for netstumbler. (optional)
            wellenreiter: Enable/disable wellenreiter detection (default =
            disable). (optional)
            wellenreiter_time: Detection Window Period. (optional)
            wellenreiter_thresh: The threshold value for wellenreiter.
            (optional)
            spoofed_deauth: Enable/disable spoofed de-authentication attack
            detection (default = disable). (optional)
            asleap_attack: Enable/disable asleap attack detection (default =
            disable). (optional)
            eapol_start_flood: Enable/disable EAPOL-Start flooding (to AP)
            detection (default = disable). (optional)
            eapol_start_thresh: The threshold value for EAPOL-Start flooding in
            specified interval. (optional)
            eapol_start_intv: The detection interval for EAPOL-Start flooding
            (1 - 3600 sec). (optional)
            eapol_logoff_flood: Enable/disable EAPOL-Logoff flooding (to AP)
            detection (default = disable). (optional)
            eapol_logoff_thresh: The threshold value for EAPOL-Logoff flooding
            in specified interval. (optional)
            eapol_logoff_intv: The detection interval for EAPOL-Logoff flooding
            (1 - 3600 sec). (optional)
            eapol_succ_flood: Enable/disable EAPOL-Success flooding (to AP)
            detection (default = disable). (optional)
            eapol_succ_thresh: The threshold value for EAPOL-Success flooding
            in specified interval. (optional)
            eapol_succ_intv: The detection interval for EAPOL-Success flooding
            (1 - 3600 sec). (optional)
            eapol_fail_flood: Enable/disable EAPOL-Failure flooding (to AP)
            detection (default = disable). (optional)
            eapol_fail_thresh: The threshold value for EAPOL-Failure flooding
            in specified interval. (optional)
            eapol_fail_intv: The detection interval for EAPOL-Failure flooding
            (1 - 3600 sec). (optional)
            eapol_pre_succ_flood: Enable/disable premature EAPOL-Success
            flooding (to STA) detection (default = disable). (optional)
            eapol_pre_succ_thresh: The threshold value for premature
            EAPOL-Success flooding in specified interval. (optional)
            eapol_pre_succ_intv: The detection interval for premature
            EAPOL-Success flooding (1 - 3600 sec). (optional)
            eapol_pre_fail_flood: Enable/disable premature EAPOL-Failure
            flooding (to STA) detection (default = disable). (optional)
            eapol_pre_fail_thresh: The threshold value for premature
            EAPOL-Failure flooding in specified interval. (optional)
            eapol_pre_fail_intv: The detection interval for premature
            EAPOL-Failure flooding (1 - 3600 sec). (optional)
            deauth_unknown_src_thresh: Threshold value per second to deauth
            unknown src for DoS attack (0: no limit). (optional)
            windows_bridge: Enable/disable windows bridge detection (default =
            disable). (optional)
            disassoc_broadcast: Enable/disable broadcast dis-association
            detection (default = disable). (optional)
            ap_spoofing: Enable/disable AP spoofing detection (default =
            disable). (optional)
            chan_based_mitm: Enable/disable channel based mitm detection
            (default = disable). (optional)
            adhoc_valid_ssid: Enable/disable adhoc using valid SSID detection
            (default = disable). (optional)
            adhoc_network: Enable/disable adhoc network detection (default =
            disable). (optional)
            eapol_key_overflow: Enable/disable overflow EAPOL key detection
            (default = disable). (optional)
            ap_impersonation: Enable/disable AP impersonation detection
            (default = disable). (optional)
            invalid_addr_combination: Enable/disable invalid address
            combination detection (default = disable). (optional)
            beacon_wrong_channel: Enable/disable beacon wrong channel detection
            (default = disable). (optional)
            ht_greenfield: Enable/disable HT greenfield detection (default =
            disable). (optional)
            overflow_ie: Enable/disable overflow IE detection (default =
            disable). (optional)
            malformed_ht_ie: Enable/disable malformed HT IE detection (default
            = disable). (optional)
            malformed_auth: Enable/disable malformed auth frame detection
            (default = disable). (optional)
            malformed_association: Enable/disable malformed association request
            detection (default = disable). (optional)
            ht_40mhz_intolerance: Enable/disable HT 40 MHz intolerance
            detection (default = disable). (optional)
            valid_ssid_misuse: Enable/disable valid SSID misuse detection
            (default = disable). (optional)
            valid_client_misassociation: Enable/disable valid client
            misassociation detection (default = disable). (optional)
            hotspotter_attack: Enable/disable hotspotter attack detection
            (default = disable). (optional)
            pwsave_dos_attack: Enable/disable power save DOS attack detection
            (default = disable). (optional)
            omerta_attack: Enable/disable omerta attack detection (default =
            disable). (optional)
            disconnect_station: Enable/disable disconnect station detection
            (default = disable). (optional)
            unencrypted_valid: Enable/disable unencrypted valid detection
            (default = disable). (optional)
            fata_jack: Enable/disable FATA-Jack detection (default = disable).
            (optional)
            risky_encryption: Enable/disable Risky Encryption detection
            (default = disable). (optional)
            fuzzed_beacon: Enable/disable fuzzed beacon detection (default =
            disable). (optional)
            fuzzed_probe_request: Enable/disable fuzzed probe request detection
            (default = disable). (optional)
            fuzzed_probe_response: Enable/disable fuzzed probe response
            detection (default = disable). (optional)
            air_jack: Enable/disable AirJack detection (default = disable).
            (optional)
            wpa_ft_attack: Enable/disable WPA FT attack detection (default =
            disable). (optional)
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
        endpoint = f"/wireless-controller/wids-profile/{name}"
        if before is not None:
            data_payload["before"] = before
        if after is not None:
            data_payload["after"] = after
        if name is not None:
            data_payload["name"] = name
        if comment is not None:
            data_payload["comment"] = comment
        if sensor_mode is not None:
            data_payload["sensor-mode"] = sensor_mode
        if ap_scan is not None:
            data_payload["ap-scan"] = ap_scan
        if ap_scan_channel_list_2G_5G is not None:
            data_payload["ap-scan-channel-list-2G-5G"] = (
                ap_scan_channel_list_2G_5G
            )
        if ap_scan_channel_list_6G is not None:
            data_payload["ap-scan-channel-list-6G"] = ap_scan_channel_list_6G
        if ap_bgscan_period is not None:
            data_payload["ap-bgscan-period"] = ap_bgscan_period
        if ap_bgscan_intv is not None:
            data_payload["ap-bgscan-intv"] = ap_bgscan_intv
        if ap_bgscan_duration is not None:
            data_payload["ap-bgscan-duration"] = ap_bgscan_duration
        if ap_bgscan_idle is not None:
            data_payload["ap-bgscan-idle"] = ap_bgscan_idle
        if ap_bgscan_report_intv is not None:
            data_payload["ap-bgscan-report-intv"] = ap_bgscan_report_intv
        if ap_bgscan_disable_schedules is not None:
            data_payload["ap-bgscan-disable-schedules"] = (
                ap_bgscan_disable_schedules
            )
        if ap_fgscan_report_intv is not None:
            data_payload["ap-fgscan-report-intv"] = ap_fgscan_report_intv
        if ap_scan_passive is not None:
            data_payload["ap-scan-passive"] = ap_scan_passive
        if ap_scan_threshold is not None:
            data_payload["ap-scan-threshold"] = ap_scan_threshold
        if ap_auto_suppress is not None:
            data_payload["ap-auto-suppress"] = ap_auto_suppress
        if wireless_bridge is not None:
            data_payload["wireless-bridge"] = wireless_bridge
        if deauth_broadcast is not None:
            data_payload["deauth-broadcast"] = deauth_broadcast
        if null_ssid_probe_resp is not None:
            data_payload["null-ssid-probe-resp"] = null_ssid_probe_resp
        if long_duration_attack is not None:
            data_payload["long-duration-attack"] = long_duration_attack
        if long_duration_thresh is not None:
            data_payload["long-duration-thresh"] = long_duration_thresh
        if invalid_mac_oui is not None:
            data_payload["invalid-mac-oui"] = invalid_mac_oui
        if weak_wep_iv is not None:
            data_payload["weak-wep-iv"] = weak_wep_iv
        if auth_frame_flood is not None:
            data_payload["auth-frame-flood"] = auth_frame_flood
        if auth_flood_time is not None:
            data_payload["auth-flood-time"] = auth_flood_time
        if auth_flood_thresh is not None:
            data_payload["auth-flood-thresh"] = auth_flood_thresh
        if assoc_frame_flood is not None:
            data_payload["assoc-frame-flood"] = assoc_frame_flood
        if assoc_flood_time is not None:
            data_payload["assoc-flood-time"] = assoc_flood_time
        if assoc_flood_thresh is not None:
            data_payload["assoc-flood-thresh"] = assoc_flood_thresh
        if reassoc_flood is not None:
            data_payload["reassoc-flood"] = reassoc_flood
        if reassoc_flood_time is not None:
            data_payload["reassoc-flood-time"] = reassoc_flood_time
        if reassoc_flood_thresh is not None:
            data_payload["reassoc-flood-thresh"] = reassoc_flood_thresh
        if probe_flood is not None:
            data_payload["probe-flood"] = probe_flood
        if probe_flood_time is not None:
            data_payload["probe-flood-time"] = probe_flood_time
        if probe_flood_thresh is not None:
            data_payload["probe-flood-thresh"] = probe_flood_thresh
        if bcn_flood is not None:
            data_payload["bcn-flood"] = bcn_flood
        if bcn_flood_time is not None:
            data_payload["bcn-flood-time"] = bcn_flood_time
        if bcn_flood_thresh is not None:
            data_payload["bcn-flood-thresh"] = bcn_flood_thresh
        if rts_flood is not None:
            data_payload["rts-flood"] = rts_flood
        if rts_flood_time is not None:
            data_payload["rts-flood-time"] = rts_flood_time
        if rts_flood_thresh is not None:
            data_payload["rts-flood-thresh"] = rts_flood_thresh
        if cts_flood is not None:
            data_payload["cts-flood"] = cts_flood
        if cts_flood_time is not None:
            data_payload["cts-flood-time"] = cts_flood_time
        if cts_flood_thresh is not None:
            data_payload["cts-flood-thresh"] = cts_flood_thresh
        if client_flood is not None:
            data_payload["client-flood"] = client_flood
        if client_flood_time is not None:
            data_payload["client-flood-time"] = client_flood_time
        if client_flood_thresh is not None:
            data_payload["client-flood-thresh"] = client_flood_thresh
        if block_ack_flood is not None:
            data_payload["block_ack-flood"] = block_ack_flood
        if block_ack_flood_time is not None:
            data_payload["block_ack-flood-time"] = block_ack_flood_time
        if block_ack_flood_thresh is not None:
            data_payload["block_ack-flood-thresh"] = block_ack_flood_thresh
        if pspoll_flood is not None:
            data_payload["pspoll-flood"] = pspoll_flood
        if pspoll_flood_time is not None:
            data_payload["pspoll-flood-time"] = pspoll_flood_time
        if pspoll_flood_thresh is not None:
            data_payload["pspoll-flood-thresh"] = pspoll_flood_thresh
        if netstumbler is not None:
            data_payload["netstumbler"] = netstumbler
        if netstumbler_time is not None:
            data_payload["netstumbler-time"] = netstumbler_time
        if netstumbler_thresh is not None:
            data_payload["netstumbler-thresh"] = netstumbler_thresh
        if wellenreiter is not None:
            data_payload["wellenreiter"] = wellenreiter
        if wellenreiter_time is not None:
            data_payload["wellenreiter-time"] = wellenreiter_time
        if wellenreiter_thresh is not None:
            data_payload["wellenreiter-thresh"] = wellenreiter_thresh
        if spoofed_deauth is not None:
            data_payload["spoofed-deauth"] = spoofed_deauth
        if asleap_attack is not None:
            data_payload["asleap-attack"] = asleap_attack
        if eapol_start_flood is not None:
            data_payload["eapol-start-flood"] = eapol_start_flood
        if eapol_start_thresh is not None:
            data_payload["eapol-start-thresh"] = eapol_start_thresh
        if eapol_start_intv is not None:
            data_payload["eapol-start-intv"] = eapol_start_intv
        if eapol_logoff_flood is not None:
            data_payload["eapol-logoff-flood"] = eapol_logoff_flood
        if eapol_logoff_thresh is not None:
            data_payload["eapol-logoff-thresh"] = eapol_logoff_thresh
        if eapol_logoff_intv is not None:
            data_payload["eapol-logoff-intv"] = eapol_logoff_intv
        if eapol_succ_flood is not None:
            data_payload["eapol-succ-flood"] = eapol_succ_flood
        if eapol_succ_thresh is not None:
            data_payload["eapol-succ-thresh"] = eapol_succ_thresh
        if eapol_succ_intv is not None:
            data_payload["eapol-succ-intv"] = eapol_succ_intv
        if eapol_fail_flood is not None:
            data_payload["eapol-fail-flood"] = eapol_fail_flood
        if eapol_fail_thresh is not None:
            data_payload["eapol-fail-thresh"] = eapol_fail_thresh
        if eapol_fail_intv is not None:
            data_payload["eapol-fail-intv"] = eapol_fail_intv
        if eapol_pre_succ_flood is not None:
            data_payload["eapol-pre-succ-flood"] = eapol_pre_succ_flood
        if eapol_pre_succ_thresh is not None:
            data_payload["eapol-pre-succ-thresh"] = eapol_pre_succ_thresh
        if eapol_pre_succ_intv is not None:
            data_payload["eapol-pre-succ-intv"] = eapol_pre_succ_intv
        if eapol_pre_fail_flood is not None:
            data_payload["eapol-pre-fail-flood"] = eapol_pre_fail_flood
        if eapol_pre_fail_thresh is not None:
            data_payload["eapol-pre-fail-thresh"] = eapol_pre_fail_thresh
        if eapol_pre_fail_intv is not None:
            data_payload["eapol-pre-fail-intv"] = eapol_pre_fail_intv
        if deauth_unknown_src_thresh is not None:
            data_payload["deauth-unknown-src-thresh"] = (
                deauth_unknown_src_thresh
            )
        if windows_bridge is not None:
            data_payload["windows-bridge"] = windows_bridge
        if disassoc_broadcast is not None:
            data_payload["disassoc-broadcast"] = disassoc_broadcast
        if ap_spoofing is not None:
            data_payload["ap-spoofing"] = ap_spoofing
        if chan_based_mitm is not None:
            data_payload["chan-based-mitm"] = chan_based_mitm
        if adhoc_valid_ssid is not None:
            data_payload["adhoc-valid-ssid"] = adhoc_valid_ssid
        if adhoc_network is not None:
            data_payload["adhoc-network"] = adhoc_network
        if eapol_key_overflow is not None:
            data_payload["eapol-key-overflow"] = eapol_key_overflow
        if ap_impersonation is not None:
            data_payload["ap-impersonation"] = ap_impersonation
        if invalid_addr_combination is not None:
            data_payload["invalid-addr-combination"] = invalid_addr_combination
        if beacon_wrong_channel is not None:
            data_payload["beacon-wrong-channel"] = beacon_wrong_channel
        if ht_greenfield is not None:
            data_payload["ht-greenfield"] = ht_greenfield
        if overflow_ie is not None:
            data_payload["overflow-ie"] = overflow_ie
        if malformed_ht_ie is not None:
            data_payload["malformed-ht-ie"] = malformed_ht_ie
        if malformed_auth is not None:
            data_payload["malformed-auth"] = malformed_auth
        if malformed_association is not None:
            data_payload["malformed-association"] = malformed_association
        if ht_40mhz_intolerance is not None:
            data_payload["ht-40mhz-intolerance"] = ht_40mhz_intolerance
        if valid_ssid_misuse is not None:
            data_payload["valid-ssid-misuse"] = valid_ssid_misuse
        if valid_client_misassociation is not None:
            data_payload["valid-client-misassociation"] = (
                valid_client_misassociation
            )
        if hotspotter_attack is not None:
            data_payload["hotspotter-attack"] = hotspotter_attack
        if pwsave_dos_attack is not None:
            data_payload["pwsave-dos-attack"] = pwsave_dos_attack
        if omerta_attack is not None:
            data_payload["omerta-attack"] = omerta_attack
        if disconnect_station is not None:
            data_payload["disconnect-station"] = disconnect_station
        if unencrypted_valid is not None:
            data_payload["unencrypted-valid"] = unencrypted_valid
        if fata_jack is not None:
            data_payload["fata-jack"] = fata_jack
        if risky_encryption is not None:
            data_payload["risky-encryption"] = risky_encryption
        if fuzzed_beacon is not None:
            data_payload["fuzzed-beacon"] = fuzzed_beacon
        if fuzzed_probe_request is not None:
            data_payload["fuzzed-probe-request"] = fuzzed_probe_request
        if fuzzed_probe_response is not None:
            data_payload["fuzzed-probe-response"] = fuzzed_probe_response
        if air_jack is not None:
            data_payload["air-jack"] = air_jack
        if wpa_ft_attack is not None:
            data_payload["wpa-ft-attack"] = wpa_ft_attack
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
        endpoint = f"/wireless-controller/wids-profile/{name}"
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
        sensor_mode: str | None = None,
        ap_scan: str | None = None,
        ap_scan_channel_list_2G_5G: list | None = None,
        ap_scan_channel_list_6G: list | None = None,
        ap_bgscan_period: int | None = None,
        ap_bgscan_intv: int | None = None,
        ap_bgscan_duration: int | None = None,
        ap_bgscan_idle: int | None = None,
        ap_bgscan_report_intv: int | None = None,
        ap_bgscan_disable_schedules: list | None = None,
        ap_fgscan_report_intv: int | None = None,
        ap_scan_passive: str | None = None,
        ap_scan_threshold: str | None = None,
        ap_auto_suppress: str | None = None,
        wireless_bridge: str | None = None,
        deauth_broadcast: str | None = None,
        null_ssid_probe_resp: str | None = None,
        long_duration_attack: str | None = None,
        long_duration_thresh: int | None = None,
        invalid_mac_oui: str | None = None,
        weak_wep_iv: str | None = None,
        auth_frame_flood: str | None = None,
        auth_flood_time: int | None = None,
        auth_flood_thresh: int | None = None,
        assoc_frame_flood: str | None = None,
        assoc_flood_time: int | None = None,
        assoc_flood_thresh: int | None = None,
        reassoc_flood: str | None = None,
        reassoc_flood_time: int | None = None,
        reassoc_flood_thresh: int | None = None,
        probe_flood: str | None = None,
        probe_flood_time: int | None = None,
        probe_flood_thresh: int | None = None,
        bcn_flood: str | None = None,
        bcn_flood_time: int | None = None,
        bcn_flood_thresh: int | None = None,
        rts_flood: str | None = None,
        rts_flood_time: int | None = None,
        rts_flood_thresh: int | None = None,
        cts_flood: str | None = None,
        cts_flood_time: int | None = None,
        cts_flood_thresh: int | None = None,
        client_flood: str | None = None,
        client_flood_time: int | None = None,
        client_flood_thresh: int | None = None,
        block_ack_flood: str | None = None,
        block_ack_flood_time: int | None = None,
        block_ack_flood_thresh: int | None = None,
        pspoll_flood: str | None = None,
        pspoll_flood_time: int | None = None,
        pspoll_flood_thresh: int | None = None,
        netstumbler: str | None = None,
        netstumbler_time: int | None = None,
        netstumbler_thresh: int | None = None,
        wellenreiter: str | None = None,
        wellenreiter_time: int | None = None,
        wellenreiter_thresh: int | None = None,
        spoofed_deauth: str | None = None,
        asleap_attack: str | None = None,
        eapol_start_flood: str | None = None,
        eapol_start_thresh: int | None = None,
        eapol_start_intv: int | None = None,
        eapol_logoff_flood: str | None = None,
        eapol_logoff_thresh: int | None = None,
        eapol_logoff_intv: int | None = None,
        eapol_succ_flood: str | None = None,
        eapol_succ_thresh: int | None = None,
        eapol_succ_intv: int | None = None,
        eapol_fail_flood: str | None = None,
        eapol_fail_thresh: int | None = None,
        eapol_fail_intv: int | None = None,
        eapol_pre_succ_flood: str | None = None,
        eapol_pre_succ_thresh: int | None = None,
        eapol_pre_succ_intv: int | None = None,
        eapol_pre_fail_flood: str | None = None,
        eapol_pre_fail_thresh: int | None = None,
        eapol_pre_fail_intv: int | None = None,
        deauth_unknown_src_thresh: int | None = None,
        windows_bridge: str | None = None,
        disassoc_broadcast: str | None = None,
        ap_spoofing: str | None = None,
        chan_based_mitm: str | None = None,
        adhoc_valid_ssid: str | None = None,
        adhoc_network: str | None = None,
        eapol_key_overflow: str | None = None,
        ap_impersonation: str | None = None,
        invalid_addr_combination: str | None = None,
        beacon_wrong_channel: str | None = None,
        ht_greenfield: str | None = None,
        overflow_ie: str | None = None,
        malformed_ht_ie: str | None = None,
        malformed_auth: str | None = None,
        malformed_association: str | None = None,
        ht_40mhz_intolerance: str | None = None,
        valid_ssid_misuse: str | None = None,
        valid_client_misassociation: str | None = None,
        hotspotter_attack: str | None = None,
        pwsave_dos_attack: str | None = None,
        omerta_attack: str | None = None,
        disconnect_station: str | None = None,
        unencrypted_valid: str | None = None,
        fata_jack: str | None = None,
        risky_encryption: str | None = None,
        fuzzed_beacon: str | None = None,
        fuzzed_probe_request: str | None = None,
        fuzzed_probe_response: str | None = None,
        air_jack: str | None = None,
        wpa_ft_attack: str | None = None,
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
            name: WIDS profile name. (optional)
            comment: Comment. (optional)
            sensor_mode: Scan nearby WiFi stations (default = disable).
            (optional)
            ap_scan: Enable/disable rogue AP detection. (optional)
            ap_scan_channel_list_2G_5G: Selected ap scan channel list for 2.4G
            and 5G bands. (optional)
            ap_scan_channel_list_6G: Selected ap scan channel list for 6G band.
            (optional)
            ap_bgscan_period: Period between background scans (10 - 3600 sec,
            default = 600). (optional)
            ap_bgscan_intv: Period between successive channel scans (1 - 600
            sec, default = 3). (optional)
            ap_bgscan_duration: Listen time on scanning a channel (10 - 1000
            msec, default = 30). (optional)
            ap_bgscan_idle: Wait time for channel inactivity before scanning
            this channel (0 - 1000 msec, default = 20). (optional)
            ap_bgscan_report_intv: Period between background scan reports (15 -
            600 sec, default = 30). (optional)
            ap_bgscan_disable_schedules: Firewall schedules for turning off
            FortiAP radio background scan. Background scan will be disabled
            when at least one of the schedules is valid. Separate multiple
            schedule names with a space. (optional)
            ap_fgscan_report_intv: Period between foreground scan reports (15 -
            600 sec, default = 15). (optional)
            ap_scan_passive: Enable/disable passive scanning. Enable means do
            not send probe request on any channels (default = disable).
            (optional)
            ap_scan_threshold: Minimum signal level/threshold in dBm required
            for the AP to report detected rogue AP (-95 to -20, default = -90).
            (optional)
            ap_auto_suppress: Enable/disable on-wire rogue AP auto-suppression
            (default = disable). (optional)
            wireless_bridge: Enable/disable wireless bridge detection (default
            = disable). (optional)
            deauth_broadcast: Enable/disable broadcasting de-authentication
            detection (default = disable). (optional)
            null_ssid_probe_resp: Enable/disable null SSID probe response
            detection (default = disable). (optional)
            long_duration_attack: Enable/disable long duration attack detection
            based on user configured threshold (default = disable). (optional)
            long_duration_thresh: Threshold value for long duration attack
            detection (1000 - 32767 usec, default = 8200). (optional)
            invalid_mac_oui: Enable/disable invalid MAC OUI detection.
            (optional)
            weak_wep_iv: Enable/disable weak WEP IV (Initialization Vector)
            detection (default = disable). (optional)
            auth_frame_flood: Enable/disable authentication frame flooding
            detection (default = disable). (optional)
            auth_flood_time: Number of seconds after which a station is
            considered not connected. (optional)
            auth_flood_thresh: The threshold value for authentication frame
            flooding. (optional)
            assoc_frame_flood: Enable/disable association frame flooding
            detection (default = disable). (optional)
            assoc_flood_time: Number of seconds after which a station is
            considered not connected. (optional)
            assoc_flood_thresh: The threshold value for association frame
            flooding. (optional)
            reassoc_flood: Enable/disable reassociation flood detection
            (default = disable). (optional)
            reassoc_flood_time: Detection Window Period. (optional)
            reassoc_flood_thresh: The threshold value for reassociation flood.
            (optional)
            probe_flood: Enable/disable probe flood detection (default =
            disable). (optional)
            probe_flood_time: Detection Window Period. (optional)
            probe_flood_thresh: The threshold value for probe flood. (optional)
            bcn_flood: Enable/disable bcn flood detection (default = disable).
            (optional)
            bcn_flood_time: Detection Window Period. (optional)
            bcn_flood_thresh: The threshold value for bcn flood. (optional)
            rts_flood: Enable/disable rts flood detection (default = disable).
            (optional)
            rts_flood_time: Detection Window Period. (optional)
            rts_flood_thresh: The threshold value for rts flood. (optional)
            cts_flood: Enable/disable cts flood detection (default = disable).
            (optional)
            cts_flood_time: Detection Window Period. (optional)
            cts_flood_thresh: The threshold value for cts flood. (optional)
            client_flood: Enable/disable client flood detection (default =
            disable). (optional)
            client_flood_time: Detection Window Period. (optional)
            client_flood_thresh: The threshold value for client flood.
            (optional)
            block_ack_flood: Enable/disable block_ack flood detection (default
            = disable). (optional)
            block_ack_flood_time: Detection Window Period. (optional)
            block_ack_flood_thresh: The threshold value for block_ack flood.
            (optional)
            pspoll_flood: Enable/disable pspoll flood detection (default =
            disable). (optional)
            pspoll_flood_time: Detection Window Period. (optional)
            pspoll_flood_thresh: The threshold value for pspoll flood.
            (optional)
            netstumbler: Enable/disable netstumbler detection (default =
            disable). (optional)
            netstumbler_time: Detection Window Period. (optional)
            netstumbler_thresh: The threshold value for netstumbler. (optional)
            wellenreiter: Enable/disable wellenreiter detection (default =
            disable). (optional)
            wellenreiter_time: Detection Window Period. (optional)
            wellenreiter_thresh: The threshold value for wellenreiter.
            (optional)
            spoofed_deauth: Enable/disable spoofed de-authentication attack
            detection (default = disable). (optional)
            asleap_attack: Enable/disable asleap attack detection (default =
            disable). (optional)
            eapol_start_flood: Enable/disable EAPOL-Start flooding (to AP)
            detection (default = disable). (optional)
            eapol_start_thresh: The threshold value for EAPOL-Start flooding in
            specified interval. (optional)
            eapol_start_intv: The detection interval for EAPOL-Start flooding
            (1 - 3600 sec). (optional)
            eapol_logoff_flood: Enable/disable EAPOL-Logoff flooding (to AP)
            detection (default = disable). (optional)
            eapol_logoff_thresh: The threshold value for EAPOL-Logoff flooding
            in specified interval. (optional)
            eapol_logoff_intv: The detection interval for EAPOL-Logoff flooding
            (1 - 3600 sec). (optional)
            eapol_succ_flood: Enable/disable EAPOL-Success flooding (to AP)
            detection (default = disable). (optional)
            eapol_succ_thresh: The threshold value for EAPOL-Success flooding
            in specified interval. (optional)
            eapol_succ_intv: The detection interval for EAPOL-Success flooding
            (1 - 3600 sec). (optional)
            eapol_fail_flood: Enable/disable EAPOL-Failure flooding (to AP)
            detection (default = disable). (optional)
            eapol_fail_thresh: The threshold value for EAPOL-Failure flooding
            in specified interval. (optional)
            eapol_fail_intv: The detection interval for EAPOL-Failure flooding
            (1 - 3600 sec). (optional)
            eapol_pre_succ_flood: Enable/disable premature EAPOL-Success
            flooding (to STA) detection (default = disable). (optional)
            eapol_pre_succ_thresh: The threshold value for premature
            EAPOL-Success flooding in specified interval. (optional)
            eapol_pre_succ_intv: The detection interval for premature
            EAPOL-Success flooding (1 - 3600 sec). (optional)
            eapol_pre_fail_flood: Enable/disable premature EAPOL-Failure
            flooding (to STA) detection (default = disable). (optional)
            eapol_pre_fail_thresh: The threshold value for premature
            EAPOL-Failure flooding in specified interval. (optional)
            eapol_pre_fail_intv: The detection interval for premature
            EAPOL-Failure flooding (1 - 3600 sec). (optional)
            deauth_unknown_src_thresh: Threshold value per second to deauth
            unknown src for DoS attack (0: no limit). (optional)
            windows_bridge: Enable/disable windows bridge detection (default =
            disable). (optional)
            disassoc_broadcast: Enable/disable broadcast dis-association
            detection (default = disable). (optional)
            ap_spoofing: Enable/disable AP spoofing detection (default =
            disable). (optional)
            chan_based_mitm: Enable/disable channel based mitm detection
            (default = disable). (optional)
            adhoc_valid_ssid: Enable/disable adhoc using valid SSID detection
            (default = disable). (optional)
            adhoc_network: Enable/disable adhoc network detection (default =
            disable). (optional)
            eapol_key_overflow: Enable/disable overflow EAPOL key detection
            (default = disable). (optional)
            ap_impersonation: Enable/disable AP impersonation detection
            (default = disable). (optional)
            invalid_addr_combination: Enable/disable invalid address
            combination detection (default = disable). (optional)
            beacon_wrong_channel: Enable/disable beacon wrong channel detection
            (default = disable). (optional)
            ht_greenfield: Enable/disable HT greenfield detection (default =
            disable). (optional)
            overflow_ie: Enable/disable overflow IE detection (default =
            disable). (optional)
            malformed_ht_ie: Enable/disable malformed HT IE detection (default
            = disable). (optional)
            malformed_auth: Enable/disable malformed auth frame detection
            (default = disable). (optional)
            malformed_association: Enable/disable malformed association request
            detection (default = disable). (optional)
            ht_40mhz_intolerance: Enable/disable HT 40 MHz intolerance
            detection (default = disable). (optional)
            valid_ssid_misuse: Enable/disable valid SSID misuse detection
            (default = disable). (optional)
            valid_client_misassociation: Enable/disable valid client
            misassociation detection (default = disable). (optional)
            hotspotter_attack: Enable/disable hotspotter attack detection
            (default = disable). (optional)
            pwsave_dos_attack: Enable/disable power save DOS attack detection
            (default = disable). (optional)
            omerta_attack: Enable/disable omerta attack detection (default =
            disable). (optional)
            disconnect_station: Enable/disable disconnect station detection
            (default = disable). (optional)
            unencrypted_valid: Enable/disable unencrypted valid detection
            (default = disable). (optional)
            fata_jack: Enable/disable FATA-Jack detection (default = disable).
            (optional)
            risky_encryption: Enable/disable Risky Encryption detection
            (default = disable). (optional)
            fuzzed_beacon: Enable/disable fuzzed beacon detection (default =
            disable). (optional)
            fuzzed_probe_request: Enable/disable fuzzed probe request detection
            (default = disable). (optional)
            fuzzed_probe_response: Enable/disable fuzzed probe response
            detection (default = disable). (optional)
            air_jack: Enable/disable AirJack detection (default = disable).
            (optional)
            wpa_ft_attack: Enable/disable WPA FT attack detection (default =
            disable). (optional)
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
        endpoint = "/wireless-controller/wids-profile"
        if nkey is not None:
            data_payload["nkey"] = nkey
        if name is not None:
            data_payload["name"] = name
        if comment is not None:
            data_payload["comment"] = comment
        if sensor_mode is not None:
            data_payload["sensor-mode"] = sensor_mode
        if ap_scan is not None:
            data_payload["ap-scan"] = ap_scan
        if ap_scan_channel_list_2G_5G is not None:
            data_payload["ap-scan-channel-list-2G-5G"] = (
                ap_scan_channel_list_2G_5G
            )
        if ap_scan_channel_list_6G is not None:
            data_payload["ap-scan-channel-list-6G"] = ap_scan_channel_list_6G
        if ap_bgscan_period is not None:
            data_payload["ap-bgscan-period"] = ap_bgscan_period
        if ap_bgscan_intv is not None:
            data_payload["ap-bgscan-intv"] = ap_bgscan_intv
        if ap_bgscan_duration is not None:
            data_payload["ap-bgscan-duration"] = ap_bgscan_duration
        if ap_bgscan_idle is not None:
            data_payload["ap-bgscan-idle"] = ap_bgscan_idle
        if ap_bgscan_report_intv is not None:
            data_payload["ap-bgscan-report-intv"] = ap_bgscan_report_intv
        if ap_bgscan_disable_schedules is not None:
            data_payload["ap-bgscan-disable-schedules"] = (
                ap_bgscan_disable_schedules
            )
        if ap_fgscan_report_intv is not None:
            data_payload["ap-fgscan-report-intv"] = ap_fgscan_report_intv
        if ap_scan_passive is not None:
            data_payload["ap-scan-passive"] = ap_scan_passive
        if ap_scan_threshold is not None:
            data_payload["ap-scan-threshold"] = ap_scan_threshold
        if ap_auto_suppress is not None:
            data_payload["ap-auto-suppress"] = ap_auto_suppress
        if wireless_bridge is not None:
            data_payload["wireless-bridge"] = wireless_bridge
        if deauth_broadcast is not None:
            data_payload["deauth-broadcast"] = deauth_broadcast
        if null_ssid_probe_resp is not None:
            data_payload["null-ssid-probe-resp"] = null_ssid_probe_resp
        if long_duration_attack is not None:
            data_payload["long-duration-attack"] = long_duration_attack
        if long_duration_thresh is not None:
            data_payload["long-duration-thresh"] = long_duration_thresh
        if invalid_mac_oui is not None:
            data_payload["invalid-mac-oui"] = invalid_mac_oui
        if weak_wep_iv is not None:
            data_payload["weak-wep-iv"] = weak_wep_iv
        if auth_frame_flood is not None:
            data_payload["auth-frame-flood"] = auth_frame_flood
        if auth_flood_time is not None:
            data_payload["auth-flood-time"] = auth_flood_time
        if auth_flood_thresh is not None:
            data_payload["auth-flood-thresh"] = auth_flood_thresh
        if assoc_frame_flood is not None:
            data_payload["assoc-frame-flood"] = assoc_frame_flood
        if assoc_flood_time is not None:
            data_payload["assoc-flood-time"] = assoc_flood_time
        if assoc_flood_thresh is not None:
            data_payload["assoc-flood-thresh"] = assoc_flood_thresh
        if reassoc_flood is not None:
            data_payload["reassoc-flood"] = reassoc_flood
        if reassoc_flood_time is not None:
            data_payload["reassoc-flood-time"] = reassoc_flood_time
        if reassoc_flood_thresh is not None:
            data_payload["reassoc-flood-thresh"] = reassoc_flood_thresh
        if probe_flood is not None:
            data_payload["probe-flood"] = probe_flood
        if probe_flood_time is not None:
            data_payload["probe-flood-time"] = probe_flood_time
        if probe_flood_thresh is not None:
            data_payload["probe-flood-thresh"] = probe_flood_thresh
        if bcn_flood is not None:
            data_payload["bcn-flood"] = bcn_flood
        if bcn_flood_time is not None:
            data_payload["bcn-flood-time"] = bcn_flood_time
        if bcn_flood_thresh is not None:
            data_payload["bcn-flood-thresh"] = bcn_flood_thresh
        if rts_flood is not None:
            data_payload["rts-flood"] = rts_flood
        if rts_flood_time is not None:
            data_payload["rts-flood-time"] = rts_flood_time
        if rts_flood_thresh is not None:
            data_payload["rts-flood-thresh"] = rts_flood_thresh
        if cts_flood is not None:
            data_payload["cts-flood"] = cts_flood
        if cts_flood_time is not None:
            data_payload["cts-flood-time"] = cts_flood_time
        if cts_flood_thresh is not None:
            data_payload["cts-flood-thresh"] = cts_flood_thresh
        if client_flood is not None:
            data_payload["client-flood"] = client_flood
        if client_flood_time is not None:
            data_payload["client-flood-time"] = client_flood_time
        if client_flood_thresh is not None:
            data_payload["client-flood-thresh"] = client_flood_thresh
        if block_ack_flood is not None:
            data_payload["block_ack-flood"] = block_ack_flood
        if block_ack_flood_time is not None:
            data_payload["block_ack-flood-time"] = block_ack_flood_time
        if block_ack_flood_thresh is not None:
            data_payload["block_ack-flood-thresh"] = block_ack_flood_thresh
        if pspoll_flood is not None:
            data_payload["pspoll-flood"] = pspoll_flood
        if pspoll_flood_time is not None:
            data_payload["pspoll-flood-time"] = pspoll_flood_time
        if pspoll_flood_thresh is not None:
            data_payload["pspoll-flood-thresh"] = pspoll_flood_thresh
        if netstumbler is not None:
            data_payload["netstumbler"] = netstumbler
        if netstumbler_time is not None:
            data_payload["netstumbler-time"] = netstumbler_time
        if netstumbler_thresh is not None:
            data_payload["netstumbler-thresh"] = netstumbler_thresh
        if wellenreiter is not None:
            data_payload["wellenreiter"] = wellenreiter
        if wellenreiter_time is not None:
            data_payload["wellenreiter-time"] = wellenreiter_time
        if wellenreiter_thresh is not None:
            data_payload["wellenreiter-thresh"] = wellenreiter_thresh
        if spoofed_deauth is not None:
            data_payload["spoofed-deauth"] = spoofed_deauth
        if asleap_attack is not None:
            data_payload["asleap-attack"] = asleap_attack
        if eapol_start_flood is not None:
            data_payload["eapol-start-flood"] = eapol_start_flood
        if eapol_start_thresh is not None:
            data_payload["eapol-start-thresh"] = eapol_start_thresh
        if eapol_start_intv is not None:
            data_payload["eapol-start-intv"] = eapol_start_intv
        if eapol_logoff_flood is not None:
            data_payload["eapol-logoff-flood"] = eapol_logoff_flood
        if eapol_logoff_thresh is not None:
            data_payload["eapol-logoff-thresh"] = eapol_logoff_thresh
        if eapol_logoff_intv is not None:
            data_payload["eapol-logoff-intv"] = eapol_logoff_intv
        if eapol_succ_flood is not None:
            data_payload["eapol-succ-flood"] = eapol_succ_flood
        if eapol_succ_thresh is not None:
            data_payload["eapol-succ-thresh"] = eapol_succ_thresh
        if eapol_succ_intv is not None:
            data_payload["eapol-succ-intv"] = eapol_succ_intv
        if eapol_fail_flood is not None:
            data_payload["eapol-fail-flood"] = eapol_fail_flood
        if eapol_fail_thresh is not None:
            data_payload["eapol-fail-thresh"] = eapol_fail_thresh
        if eapol_fail_intv is not None:
            data_payload["eapol-fail-intv"] = eapol_fail_intv
        if eapol_pre_succ_flood is not None:
            data_payload["eapol-pre-succ-flood"] = eapol_pre_succ_flood
        if eapol_pre_succ_thresh is not None:
            data_payload["eapol-pre-succ-thresh"] = eapol_pre_succ_thresh
        if eapol_pre_succ_intv is not None:
            data_payload["eapol-pre-succ-intv"] = eapol_pre_succ_intv
        if eapol_pre_fail_flood is not None:
            data_payload["eapol-pre-fail-flood"] = eapol_pre_fail_flood
        if eapol_pre_fail_thresh is not None:
            data_payload["eapol-pre-fail-thresh"] = eapol_pre_fail_thresh
        if eapol_pre_fail_intv is not None:
            data_payload["eapol-pre-fail-intv"] = eapol_pre_fail_intv
        if deauth_unknown_src_thresh is not None:
            data_payload["deauth-unknown-src-thresh"] = (
                deauth_unknown_src_thresh
            )
        if windows_bridge is not None:
            data_payload["windows-bridge"] = windows_bridge
        if disassoc_broadcast is not None:
            data_payload["disassoc-broadcast"] = disassoc_broadcast
        if ap_spoofing is not None:
            data_payload["ap-spoofing"] = ap_spoofing
        if chan_based_mitm is not None:
            data_payload["chan-based-mitm"] = chan_based_mitm
        if adhoc_valid_ssid is not None:
            data_payload["adhoc-valid-ssid"] = adhoc_valid_ssid
        if adhoc_network is not None:
            data_payload["adhoc-network"] = adhoc_network
        if eapol_key_overflow is not None:
            data_payload["eapol-key-overflow"] = eapol_key_overflow
        if ap_impersonation is not None:
            data_payload["ap-impersonation"] = ap_impersonation
        if invalid_addr_combination is not None:
            data_payload["invalid-addr-combination"] = invalid_addr_combination
        if beacon_wrong_channel is not None:
            data_payload["beacon-wrong-channel"] = beacon_wrong_channel
        if ht_greenfield is not None:
            data_payload["ht-greenfield"] = ht_greenfield
        if overflow_ie is not None:
            data_payload["overflow-ie"] = overflow_ie
        if malformed_ht_ie is not None:
            data_payload["malformed-ht-ie"] = malformed_ht_ie
        if malformed_auth is not None:
            data_payload["malformed-auth"] = malformed_auth
        if malformed_association is not None:
            data_payload["malformed-association"] = malformed_association
        if ht_40mhz_intolerance is not None:
            data_payload["ht-40mhz-intolerance"] = ht_40mhz_intolerance
        if valid_ssid_misuse is not None:
            data_payload["valid-ssid-misuse"] = valid_ssid_misuse
        if valid_client_misassociation is not None:
            data_payload["valid-client-misassociation"] = (
                valid_client_misassociation
            )
        if hotspotter_attack is not None:
            data_payload["hotspotter-attack"] = hotspotter_attack
        if pwsave_dos_attack is not None:
            data_payload["pwsave-dos-attack"] = pwsave_dos_attack
        if omerta_attack is not None:
            data_payload["omerta-attack"] = omerta_attack
        if disconnect_station is not None:
            data_payload["disconnect-station"] = disconnect_station
        if unencrypted_valid is not None:
            data_payload["unencrypted-valid"] = unencrypted_valid
        if fata_jack is not None:
            data_payload["fata-jack"] = fata_jack
        if risky_encryption is not None:
            data_payload["risky-encryption"] = risky_encryption
        if fuzzed_beacon is not None:
            data_payload["fuzzed-beacon"] = fuzzed_beacon
        if fuzzed_probe_request is not None:
            data_payload["fuzzed-probe-request"] = fuzzed_probe_request
        if fuzzed_probe_response is not None:
            data_payload["fuzzed-probe-response"] = fuzzed_probe_response
        if air_jack is not None:
            data_payload["air-jack"] = air_jack
        if wpa_ft_attack is not None:
            data_payload["wpa-ft-attack"] = wpa_ft_attack
        data_payload.update(kwargs)
        return self._client.post(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )
