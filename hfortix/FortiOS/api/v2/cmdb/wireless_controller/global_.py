"""
FortiOS CMDB - Cmdb Wireless Controller Global

Configuration endpoint for managing cmdb wireless controller global objects.

API Endpoints:
    GET    /cmdb/wireless-controller/global_
    PUT    /cmdb/wireless-controller/global_/{identifier}

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.wireless_controller.global_.get()
    >>>
    >>> # Get specific item (if supported)
    >>> item = fgt.api.cmdb.wireless_controller.global_.get(name="item_name")
    >>>
    >>> # Create new item (use POST)
    >>> result = fgt.api.cmdb.wireless_controller.global_.post(
    ...     name="new_item",
    ...     # ... additional parameters
    ... )
    >>>
    >>> # Update existing item (use PUT)
    >>> result = fgt.api.cmdb.wireless_controller.global_.put(
    ...     name="existing_item",
    ...     # ... parameters to update
    ... )
    >>>
    >>> # Delete item
    >>> result =
    fgt.api.cmdb.wireless_controller.global_.delete(name="item_name")

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


class Global:
    """
    Global Operations.

    Provides CRUD operations for FortiOS global configuration.

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
        Initialize Global endpoint.

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
        endpoint = "/wireless-controller/global"
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
        location: str | None = None,
        acd_process_count: int | None = None,
        wpad_process_count: int | None = None,
        image_download: str | None = None,
        rolling_wtp_upgrade: str | None = None,
        rolling_wtp_upgrade_threshold: str | None = None,
        max_retransmit: int | None = None,
        control_message_offload: str | None = None,
        data_ethernet_II: str | None = None,
        link_aggregation: str | None = None,
        mesh_eth_type: int | None = None,
        fiapp_eth_type: int | None = None,
        discovery_mc_addr: str | None = None,
        discovery_mc_addr6: str | None = None,
        max_clients: int | None = None,
        rogue_scan_mac_adjacency: int | None = None,
        ipsec_base_ip: str | None = None,
        wtp_share: str | None = None,
        tunnel_mode: str | None = None,
        nac_interval: int | None = None,
        ap_log_server: str | None = None,
        ap_log_server_ip: str | None = None,
        ap_log_server_port: int | None = None,
        max_sta_offline: int | None = None,
        max_sta_offline_ip2mac: int | None = None,
        max_sta_cap: int | None = None,
        max_sta_cap_wtp: int | None = None,
        max_rogue_ap: int | None = None,
        max_rogue_ap_wtp: int | None = None,
        max_rogue_sta: int | None = None,
        max_wids_entry: int | None = None,
        max_ble_device: int | None = None,
        dfs_lab_test: str | None = None,
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
            name: Name of the wireless controller. (optional)
            location: Description of the location of the wireless controller.
            (optional)
            acd_process_count: Configure the number cw_acd daemons for
            multi-core CPU support (default = 0). (optional)
            wpad_process_count: Wpad daemon process count for multi-core CPU
            support. (optional)
            image_download: Enable/disable WTP image download at join time.
            (optional)
            rolling_wtp_upgrade: Enable/disable rolling WTP upgrade (default =
            disable). (optional)
            rolling_wtp_upgrade_threshold: Minimum signal level/threshold in
            dBm required for the managed WTP to be included in rolling WTP
            upgrade (-95 to -20, default = -80). (optional)
            max_retransmit: Maximum number of tunnel packet retransmissions (0
            - 64, default = 3). (optional)
            control_message_offload: Configure CAPWAP control message data
            channel offload. (optional)
            data_ethernet_II: Configure the wireless controller to use Ethernet
            II or 802.3 frames with 802.3 data tunnel mode (default = enable).
            (optional)
            link_aggregation: Enable/disable calculating the CAPWAP transmit
            hash to load balance sessions to link aggregation nodes (default =
            disable). (optional)
            mesh_eth_type: Mesh Ethernet identifier included in backhaul
            packets (0 - 65535, default = 8755). (optional)
            fiapp_eth_type: Ethernet type for Fortinet Inter-Access Point
            Protocol (IAPP), or IEEE 802.11f, packets (0 - 65535, default =
            5252). (optional)
            discovery_mc_addr: Multicast IP address for AP discovery (default =
            244.0.1.140). (optional)
            discovery_mc_addr6: Multicast IPv6 address for AP discovery
            (default = FF02::18C). (optional)
            max_clients: Maximum number of clients that can connect
            simultaneously (default = 0, meaning no limitation). (optional)
            rogue_scan_mac_adjacency: Maximum numerical difference between an
            AP's Ethernet and wireless MAC values to match for rogue detection
            (0 - 31, default = 7). (optional)
            ipsec_base_ip: Base IP address for IPsec VPN tunnels between the
            access points and the wireless controller (default = 169.254.0.1).
            (optional)
            wtp_share: Enable/disable sharing of WTPs between VDOMs. (optional)
            tunnel_mode: Compatible/strict tunnel mode. (optional)
            nac_interval: Interval in seconds between two WiFi network access
            control (NAC) checks (10 - 600, default = 120). (optional)
            ap_log_server: Enable/disable configuring FortiGate to redirect
            wireless event log messages or FortiAPs to send UTM log messages to
            a syslog server (default = disable). (optional)
            ap_log_server_ip: IP address that FortiGate or FortiAPs send log
            messages to. (optional)
            ap_log_server_port: Port that FortiGate or FortiAPs send log
            messages to. (optional)
            max_sta_offline: Maximum number of station offline stored on the
            controller (default = 0). (optional)
            max_sta_offline_ip2mac: Maximum number of station offline ip2mac
            stored on the controller (default = 0). (optional)
            max_sta_cap: Maximum number of station cap stored on the controller
            (default = 0). (optional)
            max_sta_cap_wtp: Maximum number of station cap's wtp info stored on
            the controller (1 - 16, default = 8). (optional)
            max_rogue_ap: Maximum number of rogue APs stored on the controller
            (default = 0). (optional)
            max_rogue_ap_wtp: Maximum number of rogue AP's wtp info stored on
            the controller (1 - 16, default = 16). (optional)
            max_rogue_sta: Maximum number of rogue stations stored on the
            controller (default = 0). (optional)
            max_wids_entry: Maximum number of wids entries stored on the
            controller (default = 0). (optional)
            max_ble_device: Maximum number of BLE devices stored on the
            controller (default = 0). (optional)
            dfs_lab_test: Enable/disable DFS certificate lab test mode.
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
        endpoint = "/wireless-controller/global"
        if before is not None:
            data_payload["before"] = before
        if after is not None:
            data_payload["after"] = after
        if name is not None:
            data_payload["name"] = name
        if location is not None:
            data_payload["location"] = location
        if acd_process_count is not None:
            data_payload["acd-process-count"] = acd_process_count
        if wpad_process_count is not None:
            data_payload["wpad-process-count"] = wpad_process_count
        if image_download is not None:
            data_payload["image-download"] = image_download
        if rolling_wtp_upgrade is not None:
            data_payload["rolling-wtp-upgrade"] = rolling_wtp_upgrade
        if rolling_wtp_upgrade_threshold is not None:
            data_payload["rolling-wtp-upgrade-threshold"] = (
                rolling_wtp_upgrade_threshold
            )
        if max_retransmit is not None:
            data_payload["max-retransmit"] = max_retransmit
        if control_message_offload is not None:
            data_payload["control-message-offload"] = control_message_offload
        if data_ethernet_II is not None:
            data_payload["data-ethernet-II"] = data_ethernet_II
        if link_aggregation is not None:
            data_payload["link-aggregation"] = link_aggregation
        if mesh_eth_type is not None:
            data_payload["mesh-eth-type"] = mesh_eth_type
        if fiapp_eth_type is not None:
            data_payload["fiapp-eth-type"] = fiapp_eth_type
        if discovery_mc_addr is not None:
            data_payload["discovery-mc-addr"] = discovery_mc_addr
        if discovery_mc_addr6 is not None:
            data_payload["discovery-mc-addr6"] = discovery_mc_addr6
        if max_clients is not None:
            data_payload["max-clients"] = max_clients
        if rogue_scan_mac_adjacency is not None:
            data_payload["rogue-scan-mac-adjacency"] = rogue_scan_mac_adjacency
        if ipsec_base_ip is not None:
            data_payload["ipsec-base-ip"] = ipsec_base_ip
        if wtp_share is not None:
            data_payload["wtp-share"] = wtp_share
        if tunnel_mode is not None:
            data_payload["tunnel-mode"] = tunnel_mode
        if nac_interval is not None:
            data_payload["nac-interval"] = nac_interval
        if ap_log_server is not None:
            data_payload["ap-log-server"] = ap_log_server
        if ap_log_server_ip is not None:
            data_payload["ap-log-server-ip"] = ap_log_server_ip
        if ap_log_server_port is not None:
            data_payload["ap-log-server-port"] = ap_log_server_port
        if max_sta_offline is not None:
            data_payload["max-sta-offline"] = max_sta_offline
        if max_sta_offline_ip2mac is not None:
            data_payload["max-sta-offline-ip2mac"] = max_sta_offline_ip2mac
        if max_sta_cap is not None:
            data_payload["max-sta-cap"] = max_sta_cap
        if max_sta_cap_wtp is not None:
            data_payload["max-sta-cap-wtp"] = max_sta_cap_wtp
        if max_rogue_ap is not None:
            data_payload["max-rogue-ap"] = max_rogue_ap
        if max_rogue_ap_wtp is not None:
            data_payload["max-rogue-ap-wtp"] = max_rogue_ap_wtp
        if max_rogue_sta is not None:
            data_payload["max-rogue-sta"] = max_rogue_sta
        if max_wids_entry is not None:
            data_payload["max-wids-entry"] = max_wids_entry
        if max_ble_device is not None:
            data_payload["max-ble-device"] = max_ble_device
        if dfs_lab_test is not None:
            data_payload["dfs-lab-test"] = dfs_lab_test
        data_payload.update(kwargs)
        return self._client.put(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )
