"""
FortiOS CMDB - Cmdb Wireless Controller Vap

Configuration endpoint for managing cmdb wireless controller vap objects.

API Endpoints:
    GET    /cmdb/wireless-controller/vap
    POST   /cmdb/wireless-controller/vap
    GET    /cmdb/wireless-controller/vap
    PUT    /cmdb/wireless-controller/vap/{identifier}
    DELETE /cmdb/wireless-controller/vap/{identifier}

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.wireless_controller.vap.get()
    >>>
    >>> # Get specific item (if supported)
    >>> item = fgt.api.cmdb.wireless_controller.vap.get(name="item_name")
    >>>
    >>> # Create new item (use POST)
    >>> result = fgt.api.cmdb.wireless_controller.vap.post(
    ...     name="new_item",
    ...     # ... additional parameters
    ... )
    >>>
    >>> # Update existing item (use PUT)
    >>> result = fgt.api.cmdb.wireless_controller.vap.put(
    ...     name="existing_item",
    ...     # ... parameters to update
    ... )
    >>>
    >>> # Delete item
    >>> result = fgt.api.cmdb.wireless_controller.vap.delete(name="item_name")

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


class Vap:
    """
    Vap Operations.

    Provides CRUD operations for FortiOS vap configuration.

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
        Initialize Vap endpoint.

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
            endpoint = f"/wireless-controller/vap/{name}"
        else:
            endpoint = "/wireless-controller/vap"
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
        pre_auth: str | None = None,
        external_pre_auth: str | None = None,
        mesh_backhaul: str | None = None,
        atf_weight: int | None = None,
        max_clients: int | None = None,
        max_clients_ap: int | None = None,
        ssid: str | None = None,
        broadcast_ssid: str | None = None,
        security: str | None = None,
        pmf: str | None = None,
        pmf_assoc_comeback_timeout: int | None = None,
        pmf_sa_query_retry_timeout: int | None = None,
        beacon_protection: str | None = None,
        okc: str | None = None,
        mbo: str | None = None,
        gas_comeback_delay: int | None = None,
        gas_fragmentation_limit: int | None = None,
        mbo_cell_data_conn_pref: str | None = None,
        _80211k: str | None = None,
        _80211v: str | None = None,
        neighbor_report_dual_band: str | None = None,
        fast_bss_transition: str | None = None,
        ft_mobility_domain: int | None = None,
        ft_r0_key_lifetime: int | None = None,
        ft_over_ds: str | None = None,
        sae_groups: str | None = None,
        owe_groups: str | None = None,
        owe_transition: str | None = None,
        owe_transition_ssid: str | None = None,
        additional_akms: str | None = None,
        eapol_key_retries: str | None = None,
        tkip_counter_measure: str | None = None,
        external_web: str | None = None,
        external_web_format: str | None = None,
        external_logout: str | None = None,
        mac_username_delimiter: str | None = None,
        mac_password_delimiter: str | None = None,
        mac_calling_station_delimiter: str | None = None,
        mac_called_station_delimiter: str | None = None,
        mac_case: str | None = None,
        called_station_id_type: str | None = None,
        mac_auth_bypass: str | None = None,
        radius_mac_auth: str | None = None,
        radius_mac_auth_server: str | None = None,
        radius_mac_auth_block_interval: int | None = None,
        radius_mac_mpsk_auth: str | None = None,
        radius_mac_mpsk_timeout: int | None = None,
        radius_mac_auth_usergroups: list | None = None,
        auth: str | None = None,
        encrypt: str | None = None,
        keyindex: int | None = None,
        passphrase: str | None = None,
        sae_password: str | None = None,
        sae_h2e_only: str | None = None,
        sae_hnp_only: str | None = None,
        sae_pk: str | None = None,
        sae_private_key: str | None = None,
        akm24_only: str | None = None,
        radius_server: str | None = None,
        nas_filter_rule: str | None = None,
        domain_name_stripping: str | None = None,
        mlo: str | None = None,
        local_standalone: str | None = None,
        local_standalone_nat: str | None = None,
        ip: str | None = None,
        dhcp_lease_time: int | None = None,
        local_standalone_dns: str | None = None,
        local_standalone_dns_ip: str | None = None,
        local_lan_partition: str | None = None,
        local_bridging: str | None = None,
        local_lan: str | None = None,
        local_authentication: str | None = None,
        usergroup: list | None = None,
        captive_portal: str | None = None,
        captive_network_assistant_bypass: str | None = None,
        portal_message_override_group: str | None = None,
        portal_message_overrides: list | None = None,
        portal_type: str | None = None,
        selected_usergroups: list | None = None,
        security_exempt_list: str | None = None,
        security_redirect_url: str | None = None,
        auth_cert: str | None = None,
        auth_portal_addr: str | None = None,
        intra_vap_privacy: str | None = None,
        schedule: list | None = None,
        ldpc: str | None = None,
        high_efficiency: str | None = None,
        target_wake_time: str | None = None,
        port_macauth: str | None = None,
        port_macauth_timeout: int | None = None,
        port_macauth_reauth_timeout: int | None = None,
        bss_color_partial: str | None = None,
        mpsk_profile: str | None = None,
        split_tunneling: str | None = None,
        nac: str | None = None,
        nac_profile: str | None = None,
        vlanid: int | None = None,
        vlan_auto: str | None = None,
        dynamic_vlan: str | None = None,
        captive_portal_fw_accounting: str | None = None,
        captive_portal_ac_name: str | None = None,
        captive_portal_auth_timeout: int | None = None,
        multicast_rate: str | None = None,
        multicast_enhance: str | None = None,
        igmp_snooping: str | None = None,
        dhcp_address_enforcement: str | None = None,
        broadcast_suppression: str | None = None,
        ipv6_rules: str | None = None,
        me_disable_thresh: int | None = None,
        mu_mimo: str | None = None,
        probe_resp_suppression: str | None = None,
        probe_resp_threshold: str | None = None,
        radio_sensitivity: str | None = None,
        quarantine: str | None = None,
        radio_5g_threshold: str | None = None,
        radio_2g_threshold: str | None = None,
        vlan_name: list | None = None,
        vlan_pooling: str | None = None,
        vlan_pool: list | None = None,
        dhcp_option43_insertion: str | None = None,
        dhcp_option82_insertion: str | None = None,
        dhcp_option82_circuit_id_insertion: str | None = None,
        dhcp_option82_remote_id_insertion: str | None = None,
        ptk_rekey: str | None = None,
        ptk_rekey_intv: int | None = None,
        gtk_rekey: str | None = None,
        gtk_rekey_intv: int | None = None,
        eap_reauth: str | None = None,
        eap_reauth_intv: int | None = None,
        roaming_acct_interim_update: str | None = None,
        qos_profile: str | None = None,
        hotspot20_profile: str | None = None,
        access_control_list: str | None = None,
        primary_wag_profile: str | None = None,
        secondary_wag_profile: str | None = None,
        tunnel_echo_interval: int | None = None,
        tunnel_fallback_interval: int | None = None,
        rates_11a: str | None = None,
        rates_11bg: str | None = None,
        rates_11n_ss12: str | None = None,
        rates_11n_ss34: str | None = None,
        rates_11ac_mcs_map: str | None = None,
        rates_11ax_mcs_map: str | None = None,
        rates_11be_mcs_map: str | None = None,
        rates_11be_mcs_map_160: str | None = None,
        rates_11be_mcs_map_320: str | None = None,
        utm_profile: str | None = None,
        utm_status: str | None = None,
        utm_log: str | None = None,
        ips_sensor: str | None = None,
        application_list: str | None = None,
        antivirus_profile: str | None = None,
        webfilter_profile: str | None = None,
        scan_botnet_connections: str | None = None,
        address_group: str | None = None,
        address_group_policy: str | None = None,
        sticky_client_remove: str | None = None,
        sticky_client_threshold_5g: str | None = None,
        sticky_client_threshold_2g: str | None = None,
        sticky_client_threshold_6g: str | None = None,
        bstm_rssi_disassoc_timer: int | None = None,
        bstm_load_balancing_disassoc_timer: int | None = None,
        bstm_disassociation_imminent: str | None = None,
        beacon_advertising: str | None = None,
        osen: str | None = None,
        application_detection_engine: str | None = None,
        application_dscp_marking: str | None = None,
        application_report_intv: int | None = None,
        l3_roaming: str | None = None,
        l3_roaming_mode: str | None = None,
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
            name: Virtual AP name. (optional)
            pre_auth: Enable/disable pre-authentication, where supported by
            clients (default = enable). (optional)
            external_pre_auth: Enable/disable pre-authentication with external
            APs not managed by the FortiGate (default = disable). (optional)
            mesh_backhaul: Enable/disable using this VAP as a WiFi mesh
            backhaul (default = disable). This entry is only available when
            security is set to a WPA type or open. (optional)
            atf_weight: Airtime weight in percentage (default = 20). (optional)
            max_clients: Maximum number of clients that can connect
            simultaneously to the VAP (default = 0, meaning no limitation).
            (optional)
            max_clients_ap: Maximum number of clients that can connect
            simultaneously to the VAP per AP radio (default = 0, meaning no
            limitation). (optional)
            ssid: IEEE 802.11 service set identifier (SSID) for the wireless
            interface. Users who wish to use the wireless network must
            configure their computers to access this SSID name. (optional)
            broadcast_ssid: Enable/disable broadcasting the SSID (default =
            enable). (optional)
            security: Security mode for the wireless interface (default =
            wpa2-only-personal). (optional)
            pmf: Protected Management Frames (PMF) support (default = disable).
            (optional)
            pmf_assoc_comeback_timeout: Protected Management Frames (PMF)
            comeback maximum timeout (1-20 sec). (optional)
            pmf_sa_query_retry_timeout: Protected Management Frames (PMF) SA
            query retry timeout interval (1 - 5 100s of msec). (optional)
            beacon_protection: Enable/disable beacon protection support
            (default = disable). (optional)
            okc: Enable/disable Opportunistic Key Caching (OKC) (default =
            enable). (optional)
            mbo: Enable/disable Multiband Operation (default = disable).
            (optional)
            gas_comeback_delay: GAS comeback delay (0 or 100 - 10000
            milliseconds, default = 500). (optional)
            gas_fragmentation_limit: GAS fragmentation limit (512 - 4096,
            default = 1024). (optional)
            mbo_cell_data_conn_pref: MBO cell data connection preference (0, 1,
            or 255, default = 1). (optional)
            _80211k: Enable/disable 802.11k assisted roaming (default =
            enable). (optional)
            _80211v: Enable/disable 802.11v assisted roaming (default =
            enable). (optional)
            neighbor_report_dual_band: Enable/disable dual-band neighbor report
            (default = disable). (optional)
            fast_bss_transition: Enable/disable 802.11r Fast BSS Transition
            (FT) (default = disable). (optional)
            ft_mobility_domain: Mobility domain identifier in FT (1 - 65535,
            default = 1000). (optional)
            ft_r0_key_lifetime: Lifetime of the PMK-R0 key in FT, 1-65535
            minutes. (optional)
            ft_over_ds: Enable/disable FT over the Distribution System (DS).
            (optional)
            sae_groups: SAE-Groups. (optional)
            owe_groups: OWE-Groups. (optional)
            owe_transition: Enable/disable OWE transition mode support.
            (optional)
            owe_transition_ssid: OWE transition mode peer SSID. (optional)
            additional_akms: Additional AKMs. (optional)
            eapol_key_retries: Enable/disable retransmission of EAPOL-Key
            frames (message 3/4 and group message 1/2) (default = enable).
            (optional)
            tkip_counter_measure: Enable/disable TKIP counter measure.
            (optional)
            external_web: URL of external authentication web server. (optional)
            external_web_format: URL query parameter detection (default =
            auto-detect). (optional)
            external_logout: URL of external authentication logout server.
            (optional)
            mac_username_delimiter: MAC authentication username delimiter
            (default = hyphen). (optional)
            mac_password_delimiter: MAC authentication password delimiter
            (default = hyphen). (optional)
            mac_calling_station_delimiter: MAC calling station delimiter
            (default = hyphen). (optional)
            mac_called_station_delimiter: MAC called station delimiter (default
            = hyphen). (optional)
            mac_case: MAC case (default = uppercase). (optional)
            called_station_id_type: The format type of RADIUS attribute
            Called-Station-Id (default = mac). (optional)
            mac_auth_bypass: Enable/disable MAC authentication bypass.
            (optional)
            radius_mac_auth: Enable/disable RADIUS-based MAC authentication of
            clients (default = disable). (optional)
            radius_mac_auth_server: RADIUS-based MAC authentication server.
            (optional)
            radius_mac_auth_block_interval: Don't send RADIUS MAC auth request
            again if the client has been rejected within specific interval (0
            or 30 - 864000 seconds, default = 0, 0 to disable blocking).
            (optional)
            radius_mac_mpsk_auth: Enable/disable RADIUS-based MAC
            authentication of clients for MPSK authentication (default =
            disable). (optional)
            radius_mac_mpsk_timeout: RADIUS MAC MPSK cache timeout interval (0
            or 300 - 864000, default = 86400, 0 to disable caching). (optional)
            radius_mac_auth_usergroups: Selective user groups that are
            permitted for RADIUS mac authentication. (optional)
            auth: Authentication protocol. (optional)
            encrypt: Encryption protocol to use (only available when security
            is set to a WPA type). (optional)
            keyindex: WEP key index (1 - 4). (optional)
            passphrase: WPA pre-shared key (PSK) to be used to authenticate
            WiFi users. (optional)
            sae_password: WPA3 SAE password to be used to authenticate WiFi
            users. (optional)
            sae_h2e_only: Use hash-to-element-only mechanism for PWE derivation
            (default = disable). (optional)
            sae_hnp_only: Use hunting-and-pecking-only mechanism for PWE
            derivation (default = disable). (optional)
            sae_pk: Enable/disable WPA3 SAE-PK (default = disable). (optional)
            sae_private_key: Private key used for WPA3 SAE-PK authentication.
            (optional)
            akm24_only: WPA3 SAE using group-dependent hash only (default =
            disable). (optional)
            radius_server: RADIUS server to be used to authenticate WiFi users.
            (optional)
            nas_filter_rule: Enable/disable NAS filter rule support (default =
            disable). (optional)
            domain_name_stripping: Enable/disable stripping domain name from
            identity (default = disable). (optional)
            mlo: Enable/disable WiFi7 Multi-Link-Operation (default = disable).
            (optional)
            local_standalone: Enable/disable AP local standalone (default =
            disable). (optional)
            local_standalone_nat: Enable/disable AP local standalone NAT mode.
            (optional)
            ip: IP address and subnet mask for the local standalone NAT subnet.
            (optional)
            dhcp_lease_time: DHCP lease time in seconds for NAT IP address.
            (optional)
            local_standalone_dns: Enable/disable AP local standalone DNS.
            (optional)
            local_standalone_dns_ip: IPv4 addresses for the local standalone
            DNS. (optional)
            local_lan_partition: Enable/disable segregating client traffic to
            local LAN side (default = disable). (optional)
            local_bridging: Enable/disable bridging of wireless and Ethernet
            interfaces on the FortiAP (default = disable). (optional)
            local_lan: Allow/deny traffic destined for a Class A, B, or C
            private IP address (default = allow). (optional)
            local_authentication: Enable/disable AP local authentication.
            (optional)
            usergroup: Firewall user group to be used to authenticate WiFi
            users. (optional)
            captive_portal: Enable/disable captive portal. (optional)
            captive_network_assistant_bypass: Enable/disable Captive Network
            Assistant bypass. (optional)
            portal_message_override_group: Replacement message group for this
            VAP (only available when security is set to a captive portal type).
            (optional)
            portal_message_overrides: Individual message overrides. (optional)
            portal_type: Captive portal functionality. Configure how the
            captive portal authenticates users and whether it includes a
            disclaimer. (optional)
            selected_usergroups: Selective user groups that are permitted to
            authenticate. (optional)
            security_exempt_list: Optional security exempt list for captive
            portal authentication. (optional)
            security_redirect_url: Optional URL for redirecting users after
            they pass captive portal authentication. (optional)
            auth_cert: HTTPS server certificate. (optional)
            auth_portal_addr: Address of captive portal. (optional)
            intra_vap_privacy: Enable/disable blocking communication between
            clients on the same SSID (called intra-SSID privacy) (default =
            disable). (optional)
            schedule: Firewall schedules for enabling this VAP on the FortiAP.
            This VAP will be enabled when at least one of the schedules is
            valid. Separate multiple schedule names with a space. (optional)
            ldpc: VAP low-density parity-check (LDPC) coding configuration.
            (optional)
            high_efficiency: Enable/disable 802.11ax high efficiency (default =
            enable). (optional)
            target_wake_time: Enable/disable 802.11ax target wake time (default
            = enable). (optional)
            port_macauth: Enable/disable LAN port MAC authentication (default =
            disable). (optional)
            port_macauth_timeout: LAN port MAC authentication idle timeout
            value (default = 600 sec). (optional)
            port_macauth_reauth_timeout: LAN port MAC authentication
            re-authentication timeout value (default = 7200 sec). (optional)
            bss_color_partial: Enable/disable 802.11ax partial BSS color
            (default = enable). (optional)
            mpsk_profile: MPSK profile name. (optional)
            split_tunneling: Enable/disable split tunneling (default =
            disable). (optional)
            nac: Enable/disable network access control. (optional)
            nac_profile: NAC profile name. (optional)
            vlanid: Optional VLAN ID. (optional)
            vlan_auto: Enable/disable automatic management of SSID VLAN
            interface. (optional)
            dynamic_vlan: Enable/disable dynamic VLAN assignment. (optional)
            captive_portal_fw_accounting: Enable/disable RADIUS accounting for
            captive portal firewall authentication session. (optional)
            captive_portal_ac_name: Local-bridging captive portal ac-name.
            (optional)
            captive_portal_auth_timeout: Hard timeout - AP will always clear
            the session after timeout regardless of traffic (0 - 864000 sec,
            default = 0). (optional)
            multicast_rate: Multicast rate (0, 6000, 12000, or 24000 kbps,
            default = 0). (optional)
            multicast_enhance: Enable/disable converting multicast to unicast
            to improve performance (default = disable). (optional)
            igmp_snooping: Enable/disable IGMP snooping. (optional)
            dhcp_address_enforcement: Enable/disable DHCP address enforcement
            (default = disable). (optional)
            broadcast_suppression: Optional suppression of broadcast messages.
            For example, you can keep DHCP messages, ARP broadcasts, and so on
            off of the wireless network. (optional)
            ipv6_rules: Optional rules of IPv6 packets. For example, you can
            keep RA, RS and so on off of the wireless network. (optional)
            me_disable_thresh: Disable multicast enhancement when this many
            clients are receiving multicast traffic. (optional)
            mu_mimo: Enable/disable Multi-user MIMO (default = enable).
            (optional)
            probe_resp_suppression: Enable/disable probe response suppression
            (to ignore weak signals) (default = disable). (optional)
            probe_resp_threshold: Minimum signal level/threshold in dBm
            required for the AP response to probe requests (-95 to -20, default
            = -80). (optional)
            radio_sensitivity: Enable/disable software radio sensitivity (to
            ignore weak signals) (default = disable). (optional)
            quarantine: Enable/disable station quarantine (default = disable).
            (optional)
            radio_5g_threshold: Minimum signal level/threshold in dBm required
            for the AP response to receive a packet in 5G band(-95 to -20,
            default = -76). (optional)
            radio_2g_threshold: Minimum signal level/threshold in dBm required
            for the AP response to receive a packet in 2.4G band (-95 to -20,
            default = -79). (optional)
            vlan_name: Table for mapping VLAN name to VLAN ID. (optional)
            vlan_pooling: Enable/disable VLAN pooling, to allow grouping of
            multiple wireless controller VLANs into VLAN pools (default =
            disable). When set to wtp-group, VLAN pooling occurs with VLAN
            assignment by wtp-group. (optional)
            vlan_pool: VLAN pool. (optional)
            dhcp_option43_insertion: Enable/disable insertion of DHCP option 43
            (default = enable). (optional)
            dhcp_option82_insertion: Enable/disable DHCP option 82 insert
            (default = disable). (optional)
            dhcp_option82_circuit_id_insertion: Enable/disable DHCP option 82
            circuit-id insert (default = disable). (optional)
            dhcp_option82_remote_id_insertion: Enable/disable DHCP option 82
            remote-id insert (default = disable). (optional)
            ptk_rekey: Enable/disable PTK rekey for WPA-Enterprise security.
            (optional)
            ptk_rekey_intv: PTK rekey interval (600 - 864000 sec, default =
            86400). (optional)
            gtk_rekey: Enable/disable GTK rekey for WPA security. (optional)
            gtk_rekey_intv: GTK rekey interval (600 - 864000 sec, default =
            86400). (optional)
            eap_reauth: Enable/disable EAP re-authentication for WPA-Enterprise
            security. (optional)
            eap_reauth_intv: EAP re-authentication interval (1800 - 864000 sec,
            default = 86400). (optional)
            roaming_acct_interim_update: Enable/disable using accounting
            interim update instead of accounting start/stop on roaming for
            WPA-Enterprise security. (optional)
            qos_profile: Quality of service profile name. (optional)
            hotspot20_profile: Hotspot 2.0 profile name. (optional)
            access_control_list: Profile name for access-control-list.
            (optional)
            primary_wag_profile: Primary wireless access gateway profile name.
            (optional)
            secondary_wag_profile: Secondary wireless access gateway profile
            name. (optional)
            tunnel_echo_interval: The time interval to send echo to both
            primary and secondary tunnel peers (1 - 65535 sec, default = 300).
            (optional)
            tunnel_fallback_interval: The time interval for secondary tunnel to
            fall back to primary tunnel (0 - 65535 sec, default = 7200).
            (optional)
            rates_11a: Allowed data rates for 802.11a. (optional)
            rates_11bg: Allowed data rates for 802.11b/g. (optional)
            rates_11n_ss12: Allowed data rates for 802.11n with 1 or 2 spatial
            streams. (optional)
            rates_11n_ss34: Allowed data rates for 802.11n with 3 or 4 spatial
            streams. (optional)
            rates_11ac_mcs_map: Comma separated list of max supported VHT MCS
            for spatial streams 1 through 8. (optional)
            rates_11ax_mcs_map: Comma separated list of max supported HE MCS
            for spatial streams 1 through 8. (optional)
            rates_11be_mcs_map: Comma separated list of max nss that supports
            EHT-MCS 0-9, 10-11, 12-13 for 20MHz/40MHz/80MHz bandwidth.
            (optional)
            rates_11be_mcs_map_160: Comma separated list of max nss that
            supports EHT-MCS 0-9, 10-11, 12-13 for 160MHz bandwidth. (optional)
            rates_11be_mcs_map_320: Comma separated list of max nss that
            supports EHT-MCS 0-9, 10-11, 12-13 for 320MHz bandwidth. (optional)
            utm_profile: UTM profile name. (optional)
            utm_status: Enable to add one or more security profiles (AV, IPS,
            etc.) to the VAP. (optional)
            utm_log: Enable/disable UTM logging. (optional)
            ips_sensor: IPS sensor name. (optional)
            application_list: Application control list name. (optional)
            antivirus_profile: AntiVirus profile name. (optional)
            webfilter_profile: WebFilter profile name. (optional)
            scan_botnet_connections: Block or monitor connections to Botnet
            servers or disable Botnet scanning. (optional)
            address_group: Firewall Address Group Name. (optional)
            address_group_policy: Configure MAC address filtering policy for
            MAC addresses that are in the address-group. (optional)
            sticky_client_remove: Enable/disable sticky client remove to
            maintain good signal level clients in SSID (default = disable).
            (optional)
            sticky_client_threshold_5g: Minimum signal level/threshold in dBm
            required for the 5G client to be serviced by the AP (-95 to -20,
            default = -76). (optional)
            sticky_client_threshold_2g: Minimum signal level/threshold in dBm
            required for the 2G client to be serviced by the AP (-95 to -20,
            default = -79). (optional)
            sticky_client_threshold_6g: Minimum signal level/threshold in dBm
            required for the 6G client to be serviced by the AP (-95 to -20,
            default = -76). (optional)
            bstm_rssi_disassoc_timer: Time interval for client to voluntarily
            leave AP before forcing a disassociation due to low RSSI (0 to
            2000, default = 200). (optional)
            bstm_load_balancing_disassoc_timer: Time interval for client to
            voluntarily leave AP before forcing a disassociation due to AP
            load-balancing (0 to 30, default = 10). (optional)
            bstm_disassociation_imminent: Enable/disable forcing of
            disassociation after the BSTM request timer has been reached
            (default = enable). (optional)
            beacon_advertising: Fortinet beacon advertising IE data (default =
            empty). (optional)
            osen: Enable/disable OSEN as part of key management (default =
            disable). (optional)
            application_detection_engine: Enable/disable application detection
            engine (default = disable). (optional)
            application_dscp_marking: Enable/disable application attribute
            based DSCP marking (default = disable). (optional)
            application_report_intv: Application report interval (30 - 864000
            sec, default = 120). (optional)
            l3_roaming: Enable/disable layer 3 roaming (default = disable).
            (optional)
            l3_roaming_mode: Select the way that layer 3 roaming traffic is
            passed (default = direct). (optional)
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
        endpoint = f"/wireless-controller/vap/{name}"
        if before is not None:
            data_payload["before"] = before
        if after is not None:
            data_payload["after"] = after
        if name is not None:
            data_payload["name"] = name
        if pre_auth is not None:
            data_payload["pre-auth"] = pre_auth
        if external_pre_auth is not None:
            data_payload["external-pre-auth"] = external_pre_auth
        if mesh_backhaul is not None:
            data_payload["mesh-backhaul"] = mesh_backhaul
        if atf_weight is not None:
            data_payload["atf-weight"] = atf_weight
        if max_clients is not None:
            data_payload["max-clients"] = max_clients
        if max_clients_ap is not None:
            data_payload["max-clients-ap"] = max_clients_ap
        if ssid is not None:
            data_payload["ssid"] = ssid
        if broadcast_ssid is not None:
            data_payload["broadcast-ssid"] = broadcast_ssid
        if security is not None:
            data_payload["security"] = security
        if pmf is not None:
            data_payload["pm"] = pmf
        if pmf_assoc_comeback_timeout is not None:
            data_payload["pmf-assoc-comeback-timeout"] = (
                pmf_assoc_comeback_timeout
            )
        if pmf_sa_query_retry_timeout is not None:
            data_payload["pmf-sa-query-retry-timeout"] = (
                pmf_sa_query_retry_timeout
            )
        if beacon_protection is not None:
            data_payload["beacon-protection"] = beacon_protection
        if okc is not None:
            data_payload["okc"] = okc
        if mbo is not None:
            data_payload["mbo"] = mbo
        if gas_comeback_delay is not None:
            data_payload["gas-comeback-delay"] = gas_comeback_delay
        if gas_fragmentation_limit is not None:
            data_payload["gas-fragmentation-limit"] = gas_fragmentation_limit
        if mbo_cell_data_conn_pref is not None:
            data_payload["mbo-cell-data-conn-pre"] = mbo_cell_data_conn_pref
        if _80211k is not None:
            data_payload["80211k"] = _80211k
        if _80211v is not None:
            data_payload["80211v"] = _80211v
        if neighbor_report_dual_band is not None:
            data_payload["neighbor-report-dual-band"] = (
                neighbor_report_dual_band
            )
        if fast_bss_transition is not None:
            data_payload["fast-bss-transition"] = fast_bss_transition
        if ft_mobility_domain is not None:
            data_payload["ft-mobility-domain"] = ft_mobility_domain
        if ft_r0_key_lifetime is not None:
            data_payload["ft-r0-key-lifetime"] = ft_r0_key_lifetime
        if ft_over_ds is not None:
            data_payload["ft-over-ds"] = ft_over_ds
        if sae_groups is not None:
            data_payload["sae-groups"] = sae_groups
        if owe_groups is not None:
            data_payload["owe-groups"] = owe_groups
        if owe_transition is not None:
            data_payload["owe-transition"] = owe_transition
        if owe_transition_ssid is not None:
            data_payload["owe-transition-ssid"] = owe_transition_ssid
        if additional_akms is not None:
            data_payload["additional-akms"] = additional_akms
        if eapol_key_retries is not None:
            data_payload["eapol-key-retries"] = eapol_key_retries
        if tkip_counter_measure is not None:
            data_payload["tkip-counter-measure"] = tkip_counter_measure
        if external_web is not None:
            data_payload["external-web"] = external_web
        if external_web_format is not None:
            data_payload["external-web-format"] = external_web_format
        if external_logout is not None:
            data_payload["external-logout"] = external_logout
        if mac_username_delimiter is not None:
            data_payload["mac-username-delimiter"] = mac_username_delimiter
        if mac_password_delimiter is not None:
            data_payload["mac-password-delimiter"] = mac_password_delimiter
        if mac_calling_station_delimiter is not None:
            data_payload["mac-calling-station-delimiter"] = (
                mac_calling_station_delimiter
            )
        if mac_called_station_delimiter is not None:
            data_payload["mac-called-station-delimiter"] = (
                mac_called_station_delimiter
            )
        if mac_case is not None:
            data_payload["mac-case"] = mac_case
        if called_station_id_type is not None:
            data_payload["called-station-id-type"] = called_station_id_type
        if mac_auth_bypass is not None:
            data_payload["mac-auth-bypass"] = mac_auth_bypass
        if radius_mac_auth is not None:
            data_payload["radius-mac-auth"] = radius_mac_auth
        if radius_mac_auth_server is not None:
            data_payload["radius-mac-auth-server"] = radius_mac_auth_server
        if radius_mac_auth_block_interval is not None:
            data_payload["radius-mac-auth-block-interval"] = (
                radius_mac_auth_block_interval
            )
        if radius_mac_mpsk_auth is not None:
            data_payload["radius-mac-mpsk-auth"] = radius_mac_mpsk_auth
        if radius_mac_mpsk_timeout is not None:
            data_payload["radius-mac-mpsk-timeout"] = radius_mac_mpsk_timeout
        if radius_mac_auth_usergroups is not None:
            data_payload["radius-mac-auth-usergroups"] = (
                radius_mac_auth_usergroups
            )
        if auth is not None:
            data_payload["auth"] = auth
        if encrypt is not None:
            data_payload["encrypt"] = encrypt
        if keyindex is not None:
            data_payload["keyindex"] = keyindex
        if passphrase is not None:
            data_payload["passphrase"] = passphrase
        if sae_password is not None:
            data_payload["sae-password"] = sae_password
        if sae_h2e_only is not None:
            data_payload["sae-h2e-only"] = sae_h2e_only
        if sae_hnp_only is not None:
            data_payload["sae-hnp-only"] = sae_hnp_only
        if sae_pk is not None:
            data_payload["sae-pk"] = sae_pk
        if sae_private_key is not None:
            data_payload["sae-private-key"] = sae_private_key
        if akm24_only is not None:
            data_payload["akm24-only"] = akm24_only
        if radius_server is not None:
            data_payload["radius-server"] = radius_server
        if nas_filter_rule is not None:
            data_payload["nas-filter-rule"] = nas_filter_rule
        if domain_name_stripping is not None:
            data_payload["domain-name-stripping"] = domain_name_stripping
        if mlo is not None:
            data_payload["mlo"] = mlo
        if local_standalone is not None:
            data_payload["local-standalone"] = local_standalone
        if local_standalone_nat is not None:
            data_payload["local-standalone-nat"] = local_standalone_nat
        if ip is not None:
            data_payload["ip"] = ip
        if dhcp_lease_time is not None:
            data_payload["dhcp-lease-time"] = dhcp_lease_time
        if local_standalone_dns is not None:
            data_payload["local-standalone-dns"] = local_standalone_dns
        if local_standalone_dns_ip is not None:
            data_payload["local-standalone-dns-ip"] = local_standalone_dns_ip
        if local_lan_partition is not None:
            data_payload["local-lan-partition"] = local_lan_partition
        if local_bridging is not None:
            data_payload["local-bridging"] = local_bridging
        if local_lan is not None:
            data_payload["local-lan"] = local_lan
        if local_authentication is not None:
            data_payload["local-authentication"] = local_authentication
        if usergroup is not None:
            data_payload["usergroup"] = usergroup
        if captive_portal is not None:
            data_payload["captive-portal"] = captive_portal
        if captive_network_assistant_bypass is not None:
            data_payload["captive-network-assistant-bypass"] = (
                captive_network_assistant_bypass
            )
        if portal_message_override_group is not None:
            data_payload["portal-message-override-group"] = (
                portal_message_override_group
            )
        if portal_message_overrides is not None:
            data_payload["portal-message-overrides"] = portal_message_overrides
        if portal_type is not None:
            data_payload["portal-type"] = portal_type
        if selected_usergroups is not None:
            data_payload["selected-usergroups"] = selected_usergroups
        if security_exempt_list is not None:
            data_payload["security-exempt-list"] = security_exempt_list
        if security_redirect_url is not None:
            data_payload["security-redirect-url"] = security_redirect_url
        if auth_cert is not None:
            data_payload["auth-cert"] = auth_cert
        if auth_portal_addr is not None:
            data_payload["auth-portal-addr"] = auth_portal_addr
        if intra_vap_privacy is not None:
            data_payload["intra-vap-privacy"] = intra_vap_privacy
        if schedule is not None:
            data_payload["schedule"] = schedule
        if ldpc is not None:
            data_payload["ldpc"] = ldpc
        if high_efficiency is not None:
            data_payload["high-efficiency"] = high_efficiency
        if target_wake_time is not None:
            data_payload["target-wake-time"] = target_wake_time
        if port_macauth is not None:
            data_payload["port-macauth"] = port_macauth
        if port_macauth_timeout is not None:
            data_payload["port-macauth-timeout"] = port_macauth_timeout
        if port_macauth_reauth_timeout is not None:
            data_payload["port-macauth-reauth-timeout"] = (
                port_macauth_reauth_timeout
            )
        if bss_color_partial is not None:
            data_payload["bss-color-partial"] = bss_color_partial
        if mpsk_profile is not None:
            data_payload["mpsk-profile"] = mpsk_profile
        if split_tunneling is not None:
            data_payload["split-tunneling"] = split_tunneling
        if nac is not None:
            data_payload["nac"] = nac
        if nac_profile is not None:
            data_payload["nac-profile"] = nac_profile
        if vlanid is not None:
            data_payload["vlanid"] = vlanid
        if vlan_auto is not None:
            data_payload["vlan-auto"] = vlan_auto
        if dynamic_vlan is not None:
            data_payload["dynamic-vlan"] = dynamic_vlan
        if captive_portal_fw_accounting is not None:
            data_payload["captive-portal-fw-accounting"] = (
                captive_portal_fw_accounting
            )
        if captive_portal_ac_name is not None:
            data_payload["captive-portal-ac-name"] = captive_portal_ac_name
        if captive_portal_auth_timeout is not None:
            data_payload["captive-portal-auth-timeout"] = (
                captive_portal_auth_timeout
            )
        if multicast_rate is not None:
            data_payload["multicast-rate"] = multicast_rate
        if multicast_enhance is not None:
            data_payload["multicast-enhance"] = multicast_enhance
        if igmp_snooping is not None:
            data_payload["igmp-snooping"] = igmp_snooping
        if dhcp_address_enforcement is not None:
            data_payload["dhcp-address-enforcement"] = dhcp_address_enforcement
        if broadcast_suppression is not None:
            data_payload["broadcast-suppression"] = broadcast_suppression
        if ipv6_rules is not None:
            data_payload["ipv6-rules"] = ipv6_rules
        if me_disable_thresh is not None:
            data_payload["me-disable-thresh"] = me_disable_thresh
        if mu_mimo is not None:
            data_payload["mu-mimo"] = mu_mimo
        if probe_resp_suppression is not None:
            data_payload["probe-resp-suppression"] = probe_resp_suppression
        if probe_resp_threshold is not None:
            data_payload["probe-resp-threshold"] = probe_resp_threshold
        if radio_sensitivity is not None:
            data_payload["radio-sensitivity"] = radio_sensitivity
        if quarantine is not None:
            data_payload["quarantine"] = quarantine
        if radio_5g_threshold is not None:
            data_payload["radio-5g-threshold"] = radio_5g_threshold
        if radio_2g_threshold is not None:
            data_payload["radio-2g-threshold"] = radio_2g_threshold
        if vlan_name is not None:
            data_payload["vlan-name"] = vlan_name
        if vlan_pooling is not None:
            data_payload["vlan-pooling"] = vlan_pooling
        if vlan_pool is not None:
            data_payload["vlan-pool"] = vlan_pool
        if dhcp_option43_insertion is not None:
            data_payload["dhcp-option43-insertion"] = dhcp_option43_insertion
        if dhcp_option82_insertion is not None:
            data_payload["dhcp-option82-insertion"] = dhcp_option82_insertion
        if dhcp_option82_circuit_id_insertion is not None:
            data_payload["dhcp-option82-circuit-id-insertion"] = (
                dhcp_option82_circuit_id_insertion
            )
        if dhcp_option82_remote_id_insertion is not None:
            data_payload["dhcp-option82-remote-id-insertion"] = (
                dhcp_option82_remote_id_insertion
            )
        if ptk_rekey is not None:
            data_payload["ptk-rekey"] = ptk_rekey
        if ptk_rekey_intv is not None:
            data_payload["ptk-rekey-intv"] = ptk_rekey_intv
        if gtk_rekey is not None:
            data_payload["gtk-rekey"] = gtk_rekey
        if gtk_rekey_intv is not None:
            data_payload["gtk-rekey-intv"] = gtk_rekey_intv
        if eap_reauth is not None:
            data_payload["eap-reauth"] = eap_reauth
        if eap_reauth_intv is not None:
            data_payload["eap-reauth-intv"] = eap_reauth_intv
        if roaming_acct_interim_update is not None:
            data_payload["roaming-acct-interim-update"] = (
                roaming_acct_interim_update
            )
        if qos_profile is not None:
            data_payload["qos-profile"] = qos_profile
        if hotspot20_profile is not None:
            data_payload["hotspot20-profile"] = hotspot20_profile
        if access_control_list is not None:
            data_payload["access-control-list"] = access_control_list
        if primary_wag_profile is not None:
            data_payload["primary-wag-profile"] = primary_wag_profile
        if secondary_wag_profile is not None:
            data_payload["secondary-wag-profile"] = secondary_wag_profile
        if tunnel_echo_interval is not None:
            data_payload["tunnel-echo-interval"] = tunnel_echo_interval
        if tunnel_fallback_interval is not None:
            data_payload["tunnel-fallback-interval"] = tunnel_fallback_interval
        if rates_11a is not None:
            data_payload["rates-11a"] = rates_11a
        if rates_11bg is not None:
            data_payload["rates-11bg"] = rates_11bg
        if rates_11n_ss12 is not None:
            data_payload["rates-11n-ss12"] = rates_11n_ss12
        if rates_11n_ss34 is not None:
            data_payload["rates-11n-ss34"] = rates_11n_ss34
        if rates_11ac_mcs_map is not None:
            data_payload["rates-11ac-mcs-map"] = rates_11ac_mcs_map
        if rates_11ax_mcs_map is not None:
            data_payload["rates-11ax-mcs-map"] = rates_11ax_mcs_map
        if rates_11be_mcs_map is not None:
            data_payload["rates-11be-mcs-map"] = rates_11be_mcs_map
        if rates_11be_mcs_map_160 is not None:
            data_payload["rates-11be-mcs-map-160"] = rates_11be_mcs_map_160
        if rates_11be_mcs_map_320 is not None:
            data_payload["rates-11be-mcs-map-320"] = rates_11be_mcs_map_320
        if utm_profile is not None:
            data_payload["utm-profile"] = utm_profile
        if utm_status is not None:
            data_payload["utm-status"] = utm_status
        if utm_log is not None:
            data_payload["utm-log"] = utm_log
        if ips_sensor is not None:
            data_payload["ips-sensor"] = ips_sensor
        if application_list is not None:
            data_payload["application-list"] = application_list
        if antivirus_profile is not None:
            data_payload["antivirus-profile"] = antivirus_profile
        if webfilter_profile is not None:
            data_payload["webfilter-profile"] = webfilter_profile
        if scan_botnet_connections is not None:
            data_payload["scan-botnet-connections"] = scan_botnet_connections
        if address_group is not None:
            data_payload["address-group"] = address_group
        if address_group_policy is not None:
            data_payload["address-group-policy"] = address_group_policy
        if sticky_client_remove is not None:
            data_payload["sticky-client-remove"] = sticky_client_remove
        if sticky_client_threshold_5g is not None:
            data_payload["sticky-client-threshold-5g"] = (
                sticky_client_threshold_5g
            )
        if sticky_client_threshold_2g is not None:
            data_payload["sticky-client-threshold-2g"] = (
                sticky_client_threshold_2g
            )
        if sticky_client_threshold_6g is not None:
            data_payload["sticky-client-threshold-6g"] = (
                sticky_client_threshold_6g
            )
        if bstm_rssi_disassoc_timer is not None:
            data_payload["bstm-rssi-disassoc-timer"] = bstm_rssi_disassoc_timer
        if bstm_load_balancing_disassoc_timer is not None:
            data_payload["bstm-load-balancing-disassoc-timer"] = (
                bstm_load_balancing_disassoc_timer
            )
        if bstm_disassociation_imminent is not None:
            data_payload["bstm-disassociation-imminent"] = (
                bstm_disassociation_imminent
            )
        if beacon_advertising is not None:
            data_payload["beacon-advertising"] = beacon_advertising
        if osen is not None:
            data_payload["osen"] = osen
        if application_detection_engine is not None:
            data_payload["application-detection-engine"] = (
                application_detection_engine
            )
        if application_dscp_marking is not None:
            data_payload["application-dscp-marking"] = application_dscp_marking
        if application_report_intv is not None:
            data_payload["application-report-intv"] = application_report_intv
        if l3_roaming is not None:
            data_payload["l3-roaming"] = l3_roaming
        if l3_roaming_mode is not None:
            data_payload["l3-roaming-mode"] = l3_roaming_mode
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
        endpoint = f"/wireless-controller/vap/{name}"
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
        pre_auth: str | None = None,
        external_pre_auth: str | None = None,
        mesh_backhaul: str | None = None,
        atf_weight: int | None = None,
        max_clients: int | None = None,
        max_clients_ap: int | None = None,
        ssid: str | None = None,
        broadcast_ssid: str | None = None,
        security: str | None = None,
        pmf: str | None = None,
        pmf_assoc_comeback_timeout: int | None = None,
        pmf_sa_query_retry_timeout: int | None = None,
        beacon_protection: str | None = None,
        okc: str | None = None,
        mbo: str | None = None,
        gas_comeback_delay: int | None = None,
        gas_fragmentation_limit: int | None = None,
        mbo_cell_data_conn_pref: str | None = None,
        _80211k: str | None = None,
        _80211v: str | None = None,
        neighbor_report_dual_band: str | None = None,
        fast_bss_transition: str | None = None,
        ft_mobility_domain: int | None = None,
        ft_r0_key_lifetime: int | None = None,
        ft_over_ds: str | None = None,
        sae_groups: str | None = None,
        owe_groups: str | None = None,
        owe_transition: str | None = None,
        owe_transition_ssid: str | None = None,
        additional_akms: str | None = None,
        eapol_key_retries: str | None = None,
        tkip_counter_measure: str | None = None,
        external_web: str | None = None,
        external_web_format: str | None = None,
        external_logout: str | None = None,
        mac_username_delimiter: str | None = None,
        mac_password_delimiter: str | None = None,
        mac_calling_station_delimiter: str | None = None,
        mac_called_station_delimiter: str | None = None,
        mac_case: str | None = None,
        called_station_id_type: str | None = None,
        mac_auth_bypass: str | None = None,
        radius_mac_auth: str | None = None,
        radius_mac_auth_server: str | None = None,
        radius_mac_auth_block_interval: int | None = None,
        radius_mac_mpsk_auth: str | None = None,
        radius_mac_mpsk_timeout: int | None = None,
        radius_mac_auth_usergroups: list | None = None,
        auth: str | None = None,
        encrypt: str | None = None,
        keyindex: int | None = None,
        passphrase: str | None = None,
        sae_password: str | None = None,
        sae_h2e_only: str | None = None,
        sae_hnp_only: str | None = None,
        sae_pk: str | None = None,
        sae_private_key: str | None = None,
        akm24_only: str | None = None,
        radius_server: str | None = None,
        nas_filter_rule: str | None = None,
        domain_name_stripping: str | None = None,
        mlo: str | None = None,
        local_standalone: str | None = None,
        local_standalone_nat: str | None = None,
        ip: str | None = None,
        dhcp_lease_time: int | None = None,
        local_standalone_dns: str | None = None,
        local_standalone_dns_ip: str | None = None,
        local_lan_partition: str | None = None,
        local_bridging: str | None = None,
        local_lan: str | None = None,
        local_authentication: str | None = None,
        usergroup: list | None = None,
        captive_portal: str | None = None,
        captive_network_assistant_bypass: str | None = None,
        portal_message_override_group: str | None = None,
        portal_message_overrides: list | None = None,
        portal_type: str | None = None,
        selected_usergroups: list | None = None,
        security_exempt_list: str | None = None,
        security_redirect_url: str | None = None,
        auth_cert: str | None = None,
        auth_portal_addr: str | None = None,
        intra_vap_privacy: str | None = None,
        schedule: list | None = None,
        ldpc: str | None = None,
        high_efficiency: str | None = None,
        target_wake_time: str | None = None,
        port_macauth: str | None = None,
        port_macauth_timeout: int | None = None,
        port_macauth_reauth_timeout: int | None = None,
        bss_color_partial: str | None = None,
        mpsk_profile: str | None = None,
        split_tunneling: str | None = None,
        nac: str | None = None,
        nac_profile: str | None = None,
        vlanid: int | None = None,
        vlan_auto: str | None = None,
        dynamic_vlan: str | None = None,
        captive_portal_fw_accounting: str | None = None,
        captive_portal_ac_name: str | None = None,
        captive_portal_auth_timeout: int | None = None,
        multicast_rate: str | None = None,
        multicast_enhance: str | None = None,
        igmp_snooping: str | None = None,
        dhcp_address_enforcement: str | None = None,
        broadcast_suppression: str | None = None,
        ipv6_rules: str | None = None,
        me_disable_thresh: int | None = None,
        mu_mimo: str | None = None,
        probe_resp_suppression: str | None = None,
        probe_resp_threshold: str | None = None,
        radio_sensitivity: str | None = None,
        quarantine: str | None = None,
        radio_5g_threshold: str | None = None,
        radio_2g_threshold: str | None = None,
        vlan_name: list | None = None,
        vlan_pooling: str | None = None,
        vlan_pool: list | None = None,
        dhcp_option43_insertion: str | None = None,
        dhcp_option82_insertion: str | None = None,
        dhcp_option82_circuit_id_insertion: str | None = None,
        dhcp_option82_remote_id_insertion: str | None = None,
        ptk_rekey: str | None = None,
        ptk_rekey_intv: int | None = None,
        gtk_rekey: str | None = None,
        gtk_rekey_intv: int | None = None,
        eap_reauth: str | None = None,
        eap_reauth_intv: int | None = None,
        roaming_acct_interim_update: str | None = None,
        qos_profile: str | None = None,
        hotspot20_profile: str | None = None,
        access_control_list: str | None = None,
        primary_wag_profile: str | None = None,
        secondary_wag_profile: str | None = None,
        tunnel_echo_interval: int | None = None,
        tunnel_fallback_interval: int | None = None,
        rates_11a: str | None = None,
        rates_11bg: str | None = None,
        rates_11n_ss12: str | None = None,
        rates_11n_ss34: str | None = None,
        rates_11ac_mcs_map: str | None = None,
        rates_11ax_mcs_map: str | None = None,
        rates_11be_mcs_map: str | None = None,
        rates_11be_mcs_map_160: str | None = None,
        rates_11be_mcs_map_320: str | None = None,
        utm_profile: str | None = None,
        utm_status: str | None = None,
        utm_log: str | None = None,
        ips_sensor: str | None = None,
        application_list: str | None = None,
        antivirus_profile: str | None = None,
        webfilter_profile: str | None = None,
        scan_botnet_connections: str | None = None,
        address_group: str | None = None,
        address_group_policy: str | None = None,
        sticky_client_remove: str | None = None,
        sticky_client_threshold_5g: str | None = None,
        sticky_client_threshold_2g: str | None = None,
        sticky_client_threshold_6g: str | None = None,
        bstm_rssi_disassoc_timer: int | None = None,
        bstm_load_balancing_disassoc_timer: int | None = None,
        bstm_disassociation_imminent: str | None = None,
        beacon_advertising: str | None = None,
        osen: str | None = None,
        application_detection_engine: str | None = None,
        application_dscp_marking: str | None = None,
        application_report_intv: int | None = None,
        l3_roaming: str | None = None,
        l3_roaming_mode: str | None = None,
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
            name: Virtual AP name. (optional)
            pre_auth: Enable/disable pre-authentication, where supported by
            clients (default = enable). (optional)
            external_pre_auth: Enable/disable pre-authentication with external
            APs not managed by the FortiGate (default = disable). (optional)
            mesh_backhaul: Enable/disable using this VAP as a WiFi mesh
            backhaul (default = disable). This entry is only available when
            security is set to a WPA type or open. (optional)
            atf_weight: Airtime weight in percentage (default = 20). (optional)
            max_clients: Maximum number of clients that can connect
            simultaneously to the VAP (default = 0, meaning no limitation).
            (optional)
            max_clients_ap: Maximum number of clients that can connect
            simultaneously to the VAP per AP radio (default = 0, meaning no
            limitation). (optional)
            ssid: IEEE 802.11 service set identifier (SSID) for the wireless
            interface. Users who wish to use the wireless network must
            configure their computers to access this SSID name. (optional)
            broadcast_ssid: Enable/disable broadcasting the SSID (default =
            enable). (optional)
            security: Security mode for the wireless interface (default =
            wpa2-only-personal). (optional)
            pmf: Protected Management Frames (PMF) support (default = disable).
            (optional)
            pmf_assoc_comeback_timeout: Protected Management Frames (PMF)
            comeback maximum timeout (1-20 sec). (optional)
            pmf_sa_query_retry_timeout: Protected Management Frames (PMF) SA
            query retry timeout interval (1 - 5 100s of msec). (optional)
            beacon_protection: Enable/disable beacon protection support
            (default = disable). (optional)
            okc: Enable/disable Opportunistic Key Caching (OKC) (default =
            enable). (optional)
            mbo: Enable/disable Multiband Operation (default = disable).
            (optional)
            gas_comeback_delay: GAS comeback delay (0 or 100 - 10000
            milliseconds, default = 500). (optional)
            gas_fragmentation_limit: GAS fragmentation limit (512 - 4096,
            default = 1024). (optional)
            mbo_cell_data_conn_pref: MBO cell data connection preference (0, 1,
            or 255, default = 1). (optional)
            _80211k: Enable/disable 802.11k assisted roaming (default =
            enable). (optional)
            _80211v: Enable/disable 802.11v assisted roaming (default =
            enable). (optional)
            neighbor_report_dual_band: Enable/disable dual-band neighbor report
            (default = disable). (optional)
            fast_bss_transition: Enable/disable 802.11r Fast BSS Transition
            (FT) (default = disable). (optional)
            ft_mobility_domain: Mobility domain identifier in FT (1 - 65535,
            default = 1000). (optional)
            ft_r0_key_lifetime: Lifetime of the PMK-R0 key in FT, 1-65535
            minutes. (optional)
            ft_over_ds: Enable/disable FT over the Distribution System (DS).
            (optional)
            sae_groups: SAE-Groups. (optional)
            owe_groups: OWE-Groups. (optional)
            owe_transition: Enable/disable OWE transition mode support.
            (optional)
            owe_transition_ssid: OWE transition mode peer SSID. (optional)
            additional_akms: Additional AKMs. (optional)
            eapol_key_retries: Enable/disable retransmission of EAPOL-Key
            frames (message 3/4 and group message 1/2) (default = enable).
            (optional)
            tkip_counter_measure: Enable/disable TKIP counter measure.
            (optional)
            external_web: URL of external authentication web server. (optional)
            external_web_format: URL query parameter detection (default =
            auto-detect). (optional)
            external_logout: URL of external authentication logout server.
            (optional)
            mac_username_delimiter: MAC authentication username delimiter
            (default = hyphen). (optional)
            mac_password_delimiter: MAC authentication password delimiter
            (default = hyphen). (optional)
            mac_calling_station_delimiter: MAC calling station delimiter
            (default = hyphen). (optional)
            mac_called_station_delimiter: MAC called station delimiter (default
            = hyphen). (optional)
            mac_case: MAC case (default = uppercase). (optional)
            called_station_id_type: The format type of RADIUS attribute
            Called-Station-Id (default = mac). (optional)
            mac_auth_bypass: Enable/disable MAC authentication bypass.
            (optional)
            radius_mac_auth: Enable/disable RADIUS-based MAC authentication of
            clients (default = disable). (optional)
            radius_mac_auth_server: RADIUS-based MAC authentication server.
            (optional)
            radius_mac_auth_block_interval: Don't send RADIUS MAC auth request
            again if the client has been rejected within specific interval (0
            or 30 - 864000 seconds, default = 0, 0 to disable blocking).
            (optional)
            radius_mac_mpsk_auth: Enable/disable RADIUS-based MAC
            authentication of clients for MPSK authentication (default =
            disable). (optional)
            radius_mac_mpsk_timeout: RADIUS MAC MPSK cache timeout interval (0
            or 300 - 864000, default = 86400, 0 to disable caching). (optional)
            radius_mac_auth_usergroups: Selective user groups that are
            permitted for RADIUS mac authentication. (optional)
            auth: Authentication protocol. (optional)
            encrypt: Encryption protocol to use (only available when security
            is set to a WPA type). (optional)
            keyindex: WEP key index (1 - 4). (optional)
            passphrase: WPA pre-shared key (PSK) to be used to authenticate
            WiFi users. (optional)
            sae_password: WPA3 SAE password to be used to authenticate WiFi
            users. (optional)
            sae_h2e_only: Use hash-to-element-only mechanism for PWE derivation
            (default = disable). (optional)
            sae_hnp_only: Use hunting-and-pecking-only mechanism for PWE
            derivation (default = disable). (optional)
            sae_pk: Enable/disable WPA3 SAE-PK (default = disable). (optional)
            sae_private_key: Private key used for WPA3 SAE-PK authentication.
            (optional)
            akm24_only: WPA3 SAE using group-dependent hash only (default =
            disable). (optional)
            radius_server: RADIUS server to be used to authenticate WiFi users.
            (optional)
            nas_filter_rule: Enable/disable NAS filter rule support (default =
            disable). (optional)
            domain_name_stripping: Enable/disable stripping domain name from
            identity (default = disable). (optional)
            mlo: Enable/disable WiFi7 Multi-Link-Operation (default = disable).
            (optional)
            local_standalone: Enable/disable AP local standalone (default =
            disable). (optional)
            local_standalone_nat: Enable/disable AP local standalone NAT mode.
            (optional)
            ip: IP address and subnet mask for the local standalone NAT subnet.
            (optional)
            dhcp_lease_time: DHCP lease time in seconds for NAT IP address.
            (optional)
            local_standalone_dns: Enable/disable AP local standalone DNS.
            (optional)
            local_standalone_dns_ip: IPv4 addresses for the local standalone
            DNS. (optional)
            local_lan_partition: Enable/disable segregating client traffic to
            local LAN side (default = disable). (optional)
            local_bridging: Enable/disable bridging of wireless and Ethernet
            interfaces on the FortiAP (default = disable). (optional)
            local_lan: Allow/deny traffic destined for a Class A, B, or C
            private IP address (default = allow). (optional)
            local_authentication: Enable/disable AP local authentication.
            (optional)
            usergroup: Firewall user group to be used to authenticate WiFi
            users. (optional)
            captive_portal: Enable/disable captive portal. (optional)
            captive_network_assistant_bypass: Enable/disable Captive Network
            Assistant bypass. (optional)
            portal_message_override_group: Replacement message group for this
            VAP (only available when security is set to a captive portal type).
            (optional)
            portal_message_overrides: Individual message overrides. (optional)
            portal_type: Captive portal functionality. Configure how the
            captive portal authenticates users and whether it includes a
            disclaimer. (optional)
            selected_usergroups: Selective user groups that are permitted to
            authenticate. (optional)
            security_exempt_list: Optional security exempt list for captive
            portal authentication. (optional)
            security_redirect_url: Optional URL for redirecting users after
            they pass captive portal authentication. (optional)
            auth_cert: HTTPS server certificate. (optional)
            auth_portal_addr: Address of captive portal. (optional)
            intra_vap_privacy: Enable/disable blocking communication between
            clients on the same SSID (called intra-SSID privacy) (default =
            disable). (optional)
            schedule: Firewall schedules for enabling this VAP on the FortiAP.
            This VAP will be enabled when at least one of the schedules is
            valid. Separate multiple schedule names with a space. (optional)
            ldpc: VAP low-density parity-check (LDPC) coding configuration.
            (optional)
            high_efficiency: Enable/disable 802.11ax high efficiency (default =
            enable). (optional)
            target_wake_time: Enable/disable 802.11ax target wake time (default
            = enable). (optional)
            port_macauth: Enable/disable LAN port MAC authentication (default =
            disable). (optional)
            port_macauth_timeout: LAN port MAC authentication idle timeout
            value (default = 600 sec). (optional)
            port_macauth_reauth_timeout: LAN port MAC authentication
            re-authentication timeout value (default = 7200 sec). (optional)
            bss_color_partial: Enable/disable 802.11ax partial BSS color
            (default = enable). (optional)
            mpsk_profile: MPSK profile name. (optional)
            split_tunneling: Enable/disable split tunneling (default =
            disable). (optional)
            nac: Enable/disable network access control. (optional)
            nac_profile: NAC profile name. (optional)
            vlanid: Optional VLAN ID. (optional)
            vlan_auto: Enable/disable automatic management of SSID VLAN
            interface. (optional)
            dynamic_vlan: Enable/disable dynamic VLAN assignment. (optional)
            captive_portal_fw_accounting: Enable/disable RADIUS accounting for
            captive portal firewall authentication session. (optional)
            captive_portal_ac_name: Local-bridging captive portal ac-name.
            (optional)
            captive_portal_auth_timeout: Hard timeout - AP will always clear
            the session after timeout regardless of traffic (0 - 864000 sec,
            default = 0). (optional)
            multicast_rate: Multicast rate (0, 6000, 12000, or 24000 kbps,
            default = 0). (optional)
            multicast_enhance: Enable/disable converting multicast to unicast
            to improve performance (default = disable). (optional)
            igmp_snooping: Enable/disable IGMP snooping. (optional)
            dhcp_address_enforcement: Enable/disable DHCP address enforcement
            (default = disable). (optional)
            broadcast_suppression: Optional suppression of broadcast messages.
            For example, you can keep DHCP messages, ARP broadcasts, and so on
            off of the wireless network. (optional)
            ipv6_rules: Optional rules of IPv6 packets. For example, you can
            keep RA, RS and so on off of the wireless network. (optional)
            me_disable_thresh: Disable multicast enhancement when this many
            clients are receiving multicast traffic. (optional)
            mu_mimo: Enable/disable Multi-user MIMO (default = enable).
            (optional)
            probe_resp_suppression: Enable/disable probe response suppression
            (to ignore weak signals) (default = disable). (optional)
            probe_resp_threshold: Minimum signal level/threshold in dBm
            required for the AP response to probe requests (-95 to -20, default
            = -80). (optional)
            radio_sensitivity: Enable/disable software radio sensitivity (to
            ignore weak signals) (default = disable). (optional)
            quarantine: Enable/disable station quarantine (default = disable).
            (optional)
            radio_5g_threshold: Minimum signal level/threshold in dBm required
            for the AP response to receive a packet in 5G band(-95 to -20,
            default = -76). (optional)
            radio_2g_threshold: Minimum signal level/threshold in dBm required
            for the AP response to receive a packet in 2.4G band (-95 to -20,
            default = -79). (optional)
            vlan_name: Table for mapping VLAN name to VLAN ID. (optional)
            vlan_pooling: Enable/disable VLAN pooling, to allow grouping of
            multiple wireless controller VLANs into VLAN pools (default =
            disable). When set to wtp-group, VLAN pooling occurs with VLAN
            assignment by wtp-group. (optional)
            vlan_pool: VLAN pool. (optional)
            dhcp_option43_insertion: Enable/disable insertion of DHCP option 43
            (default = enable). (optional)
            dhcp_option82_insertion: Enable/disable DHCP option 82 insert
            (default = disable). (optional)
            dhcp_option82_circuit_id_insertion: Enable/disable DHCP option 82
            circuit-id insert (default = disable). (optional)
            dhcp_option82_remote_id_insertion: Enable/disable DHCP option 82
            remote-id insert (default = disable). (optional)
            ptk_rekey: Enable/disable PTK rekey for WPA-Enterprise security.
            (optional)
            ptk_rekey_intv: PTK rekey interval (600 - 864000 sec, default =
            86400). (optional)
            gtk_rekey: Enable/disable GTK rekey for WPA security. (optional)
            gtk_rekey_intv: GTK rekey interval (600 - 864000 sec, default =
            86400). (optional)
            eap_reauth: Enable/disable EAP re-authentication for WPA-Enterprise
            security. (optional)
            eap_reauth_intv: EAP re-authentication interval (1800 - 864000 sec,
            default = 86400). (optional)
            roaming_acct_interim_update: Enable/disable using accounting
            interim update instead of accounting start/stop on roaming for
            WPA-Enterprise security. (optional)
            qos_profile: Quality of service profile name. (optional)
            hotspot20_profile: Hotspot 2.0 profile name. (optional)
            access_control_list: Profile name for access-control-list.
            (optional)
            primary_wag_profile: Primary wireless access gateway profile name.
            (optional)
            secondary_wag_profile: Secondary wireless access gateway profile
            name. (optional)
            tunnel_echo_interval: The time interval to send echo to both
            primary and secondary tunnel peers (1 - 65535 sec, default = 300).
            (optional)
            tunnel_fallback_interval: The time interval for secondary tunnel to
            fall back to primary tunnel (0 - 65535 sec, default = 7200).
            (optional)
            rates_11a: Allowed data rates for 802.11a. (optional)
            rates_11bg: Allowed data rates for 802.11b/g. (optional)
            rates_11n_ss12: Allowed data rates for 802.11n with 1 or 2 spatial
            streams. (optional)
            rates_11n_ss34: Allowed data rates for 802.11n with 3 or 4 spatial
            streams. (optional)
            rates_11ac_mcs_map: Comma separated list of max supported VHT MCS
            for spatial streams 1 through 8. (optional)
            rates_11ax_mcs_map: Comma separated list of max supported HE MCS
            for spatial streams 1 through 8. (optional)
            rates_11be_mcs_map: Comma separated list of max nss that supports
            EHT-MCS 0-9, 10-11, 12-13 for 20MHz/40MHz/80MHz bandwidth.
            (optional)
            rates_11be_mcs_map_160: Comma separated list of max nss that
            supports EHT-MCS 0-9, 10-11, 12-13 for 160MHz bandwidth. (optional)
            rates_11be_mcs_map_320: Comma separated list of max nss that
            supports EHT-MCS 0-9, 10-11, 12-13 for 320MHz bandwidth. (optional)
            utm_profile: UTM profile name. (optional)
            utm_status: Enable to add one or more security profiles (AV, IPS,
            etc.) to the VAP. (optional)
            utm_log: Enable/disable UTM logging. (optional)
            ips_sensor: IPS sensor name. (optional)
            application_list: Application control list name. (optional)
            antivirus_profile: AntiVirus profile name. (optional)
            webfilter_profile: WebFilter profile name. (optional)
            scan_botnet_connections: Block or monitor connections to Botnet
            servers or disable Botnet scanning. (optional)
            address_group: Firewall Address Group Name. (optional)
            address_group_policy: Configure MAC address filtering policy for
            MAC addresses that are in the address-group. (optional)
            sticky_client_remove: Enable/disable sticky client remove to
            maintain good signal level clients in SSID (default = disable).
            (optional)
            sticky_client_threshold_5g: Minimum signal level/threshold in dBm
            required for the 5G client to be serviced by the AP (-95 to -20,
            default = -76). (optional)
            sticky_client_threshold_2g: Minimum signal level/threshold in dBm
            required for the 2G client to be serviced by the AP (-95 to -20,
            default = -79). (optional)
            sticky_client_threshold_6g: Minimum signal level/threshold in dBm
            required for the 6G client to be serviced by the AP (-95 to -20,
            default = -76). (optional)
            bstm_rssi_disassoc_timer: Time interval for client to voluntarily
            leave AP before forcing a disassociation due to low RSSI (0 to
            2000, default = 200). (optional)
            bstm_load_balancing_disassoc_timer: Time interval for client to
            voluntarily leave AP before forcing a disassociation due to AP
            load-balancing (0 to 30, default = 10). (optional)
            bstm_disassociation_imminent: Enable/disable forcing of
            disassociation after the BSTM request timer has been reached
            (default = enable). (optional)
            beacon_advertising: Fortinet beacon advertising IE data (default =
            empty). (optional)
            osen: Enable/disable OSEN as part of key management (default =
            disable). (optional)
            application_detection_engine: Enable/disable application detection
            engine (default = disable). (optional)
            application_dscp_marking: Enable/disable application attribute
            based DSCP marking (default = disable). (optional)
            application_report_intv: Application report interval (30 - 864000
            sec, default = 120). (optional)
            l3_roaming: Enable/disable layer 3 roaming (default = disable).
            (optional)
            l3_roaming_mode: Select the way that layer 3 roaming traffic is
            passed (default = direct). (optional)
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
        endpoint = "/wireless-controller/vap"
        if nkey is not None:
            data_payload["nkey"] = nkey
        if name is not None:
            data_payload["name"] = name
        if pre_auth is not None:
            data_payload["pre-auth"] = pre_auth
        if external_pre_auth is not None:
            data_payload["external-pre-auth"] = external_pre_auth
        if mesh_backhaul is not None:
            data_payload["mesh-backhaul"] = mesh_backhaul
        if atf_weight is not None:
            data_payload["atf-weight"] = atf_weight
        if max_clients is not None:
            data_payload["max-clients"] = max_clients
        if max_clients_ap is not None:
            data_payload["max-clients-ap"] = max_clients_ap
        if ssid is not None:
            data_payload["ssid"] = ssid
        if broadcast_ssid is not None:
            data_payload["broadcast-ssid"] = broadcast_ssid
        if security is not None:
            data_payload["security"] = security
        if pmf is not None:
            data_payload["pm"] = pmf
        if pmf_assoc_comeback_timeout is not None:
            data_payload["pmf-assoc-comeback-timeout"] = (
                pmf_assoc_comeback_timeout
            )
        if pmf_sa_query_retry_timeout is not None:
            data_payload["pmf-sa-query-retry-timeout"] = (
                pmf_sa_query_retry_timeout
            )
        if beacon_protection is not None:
            data_payload["beacon-protection"] = beacon_protection
        if okc is not None:
            data_payload["okc"] = okc
        if mbo is not None:
            data_payload["mbo"] = mbo
        if gas_comeback_delay is not None:
            data_payload["gas-comeback-delay"] = gas_comeback_delay
        if gas_fragmentation_limit is not None:
            data_payload["gas-fragmentation-limit"] = gas_fragmentation_limit
        if mbo_cell_data_conn_pref is not None:
            data_payload["mbo-cell-data-conn-pre"] = mbo_cell_data_conn_pref
        if _80211k is not None:
            data_payload["80211k"] = _80211k
        if _80211v is not None:
            data_payload["80211v"] = _80211v
        if neighbor_report_dual_band is not None:
            data_payload["neighbor-report-dual-band"] = (
                neighbor_report_dual_band
            )
        if fast_bss_transition is not None:
            data_payload["fast-bss-transition"] = fast_bss_transition
        if ft_mobility_domain is not None:
            data_payload["ft-mobility-domain"] = ft_mobility_domain
        if ft_r0_key_lifetime is not None:
            data_payload["ft-r0-key-lifetime"] = ft_r0_key_lifetime
        if ft_over_ds is not None:
            data_payload["ft-over-ds"] = ft_over_ds
        if sae_groups is not None:
            data_payload["sae-groups"] = sae_groups
        if owe_groups is not None:
            data_payload["owe-groups"] = owe_groups
        if owe_transition is not None:
            data_payload["owe-transition"] = owe_transition
        if owe_transition_ssid is not None:
            data_payload["owe-transition-ssid"] = owe_transition_ssid
        if additional_akms is not None:
            data_payload["additional-akms"] = additional_akms
        if eapol_key_retries is not None:
            data_payload["eapol-key-retries"] = eapol_key_retries
        if tkip_counter_measure is not None:
            data_payload["tkip-counter-measure"] = tkip_counter_measure
        if external_web is not None:
            data_payload["external-web"] = external_web
        if external_web_format is not None:
            data_payload["external-web-format"] = external_web_format
        if external_logout is not None:
            data_payload["external-logout"] = external_logout
        if mac_username_delimiter is not None:
            data_payload["mac-username-delimiter"] = mac_username_delimiter
        if mac_password_delimiter is not None:
            data_payload["mac-password-delimiter"] = mac_password_delimiter
        if mac_calling_station_delimiter is not None:
            data_payload["mac-calling-station-delimiter"] = (
                mac_calling_station_delimiter
            )
        if mac_called_station_delimiter is not None:
            data_payload["mac-called-station-delimiter"] = (
                mac_called_station_delimiter
            )
        if mac_case is not None:
            data_payload["mac-case"] = mac_case
        if called_station_id_type is not None:
            data_payload["called-station-id-type"] = called_station_id_type
        if mac_auth_bypass is not None:
            data_payload["mac-auth-bypass"] = mac_auth_bypass
        if radius_mac_auth is not None:
            data_payload["radius-mac-auth"] = radius_mac_auth
        if radius_mac_auth_server is not None:
            data_payload["radius-mac-auth-server"] = radius_mac_auth_server
        if radius_mac_auth_block_interval is not None:
            data_payload["radius-mac-auth-block-interval"] = (
                radius_mac_auth_block_interval
            )
        if radius_mac_mpsk_auth is not None:
            data_payload["radius-mac-mpsk-auth"] = radius_mac_mpsk_auth
        if radius_mac_mpsk_timeout is not None:
            data_payload["radius-mac-mpsk-timeout"] = radius_mac_mpsk_timeout
        if radius_mac_auth_usergroups is not None:
            data_payload["radius-mac-auth-usergroups"] = (
                radius_mac_auth_usergroups
            )
        if auth is not None:
            data_payload["auth"] = auth
        if encrypt is not None:
            data_payload["encrypt"] = encrypt
        if keyindex is not None:
            data_payload["keyindex"] = keyindex
        if passphrase is not None:
            data_payload["passphrase"] = passphrase
        if sae_password is not None:
            data_payload["sae-password"] = sae_password
        if sae_h2e_only is not None:
            data_payload["sae-h2e-only"] = sae_h2e_only
        if sae_hnp_only is not None:
            data_payload["sae-hnp-only"] = sae_hnp_only
        if sae_pk is not None:
            data_payload["sae-pk"] = sae_pk
        if sae_private_key is not None:
            data_payload["sae-private-key"] = sae_private_key
        if akm24_only is not None:
            data_payload["akm24-only"] = akm24_only
        if radius_server is not None:
            data_payload["radius-server"] = radius_server
        if nas_filter_rule is not None:
            data_payload["nas-filter-rule"] = nas_filter_rule
        if domain_name_stripping is not None:
            data_payload["domain-name-stripping"] = domain_name_stripping
        if mlo is not None:
            data_payload["mlo"] = mlo
        if local_standalone is not None:
            data_payload["local-standalone"] = local_standalone
        if local_standalone_nat is not None:
            data_payload["local-standalone-nat"] = local_standalone_nat
        if ip is not None:
            data_payload["ip"] = ip
        if dhcp_lease_time is not None:
            data_payload["dhcp-lease-time"] = dhcp_lease_time
        if local_standalone_dns is not None:
            data_payload["local-standalone-dns"] = local_standalone_dns
        if local_standalone_dns_ip is not None:
            data_payload["local-standalone-dns-ip"] = local_standalone_dns_ip
        if local_lan_partition is not None:
            data_payload["local-lan-partition"] = local_lan_partition
        if local_bridging is not None:
            data_payload["local-bridging"] = local_bridging
        if local_lan is not None:
            data_payload["local-lan"] = local_lan
        if local_authentication is not None:
            data_payload["local-authentication"] = local_authentication
        if usergroup is not None:
            data_payload["usergroup"] = usergroup
        if captive_portal is not None:
            data_payload["captive-portal"] = captive_portal
        if captive_network_assistant_bypass is not None:
            data_payload["captive-network-assistant-bypass"] = (
                captive_network_assistant_bypass
            )
        if portal_message_override_group is not None:
            data_payload["portal-message-override-group"] = (
                portal_message_override_group
            )
        if portal_message_overrides is not None:
            data_payload["portal-message-overrides"] = portal_message_overrides
        if portal_type is not None:
            data_payload["portal-type"] = portal_type
        if selected_usergroups is not None:
            data_payload["selected-usergroups"] = selected_usergroups
        if security_exempt_list is not None:
            data_payload["security-exempt-list"] = security_exempt_list
        if security_redirect_url is not None:
            data_payload["security-redirect-url"] = security_redirect_url
        if auth_cert is not None:
            data_payload["auth-cert"] = auth_cert
        if auth_portal_addr is not None:
            data_payload["auth-portal-addr"] = auth_portal_addr
        if intra_vap_privacy is not None:
            data_payload["intra-vap-privacy"] = intra_vap_privacy
        if schedule is not None:
            data_payload["schedule"] = schedule
        if ldpc is not None:
            data_payload["ldpc"] = ldpc
        if high_efficiency is not None:
            data_payload["high-efficiency"] = high_efficiency
        if target_wake_time is not None:
            data_payload["target-wake-time"] = target_wake_time
        if port_macauth is not None:
            data_payload["port-macauth"] = port_macauth
        if port_macauth_timeout is not None:
            data_payload["port-macauth-timeout"] = port_macauth_timeout
        if port_macauth_reauth_timeout is not None:
            data_payload["port-macauth-reauth-timeout"] = (
                port_macauth_reauth_timeout
            )
        if bss_color_partial is not None:
            data_payload["bss-color-partial"] = bss_color_partial
        if mpsk_profile is not None:
            data_payload["mpsk-profile"] = mpsk_profile
        if split_tunneling is not None:
            data_payload["split-tunneling"] = split_tunneling
        if nac is not None:
            data_payload["nac"] = nac
        if nac_profile is not None:
            data_payload["nac-profile"] = nac_profile
        if vlanid is not None:
            data_payload["vlanid"] = vlanid
        if vlan_auto is not None:
            data_payload["vlan-auto"] = vlan_auto
        if dynamic_vlan is not None:
            data_payload["dynamic-vlan"] = dynamic_vlan
        if captive_portal_fw_accounting is not None:
            data_payload["captive-portal-fw-accounting"] = (
                captive_portal_fw_accounting
            )
        if captive_portal_ac_name is not None:
            data_payload["captive-portal-ac-name"] = captive_portal_ac_name
        if captive_portal_auth_timeout is not None:
            data_payload["captive-portal-auth-timeout"] = (
                captive_portal_auth_timeout
            )
        if multicast_rate is not None:
            data_payload["multicast-rate"] = multicast_rate
        if multicast_enhance is not None:
            data_payload["multicast-enhance"] = multicast_enhance
        if igmp_snooping is not None:
            data_payload["igmp-snooping"] = igmp_snooping
        if dhcp_address_enforcement is not None:
            data_payload["dhcp-address-enforcement"] = dhcp_address_enforcement
        if broadcast_suppression is not None:
            data_payload["broadcast-suppression"] = broadcast_suppression
        if ipv6_rules is not None:
            data_payload["ipv6-rules"] = ipv6_rules
        if me_disable_thresh is not None:
            data_payload["me-disable-thresh"] = me_disable_thresh
        if mu_mimo is not None:
            data_payload["mu-mimo"] = mu_mimo
        if probe_resp_suppression is not None:
            data_payload["probe-resp-suppression"] = probe_resp_suppression
        if probe_resp_threshold is not None:
            data_payload["probe-resp-threshold"] = probe_resp_threshold
        if radio_sensitivity is not None:
            data_payload["radio-sensitivity"] = radio_sensitivity
        if quarantine is not None:
            data_payload["quarantine"] = quarantine
        if radio_5g_threshold is not None:
            data_payload["radio-5g-threshold"] = radio_5g_threshold
        if radio_2g_threshold is not None:
            data_payload["radio-2g-threshold"] = radio_2g_threshold
        if vlan_name is not None:
            data_payload["vlan-name"] = vlan_name
        if vlan_pooling is not None:
            data_payload["vlan-pooling"] = vlan_pooling
        if vlan_pool is not None:
            data_payload["vlan-pool"] = vlan_pool
        if dhcp_option43_insertion is not None:
            data_payload["dhcp-option43-insertion"] = dhcp_option43_insertion
        if dhcp_option82_insertion is not None:
            data_payload["dhcp-option82-insertion"] = dhcp_option82_insertion
        if dhcp_option82_circuit_id_insertion is not None:
            data_payload["dhcp-option82-circuit-id-insertion"] = (
                dhcp_option82_circuit_id_insertion
            )
        if dhcp_option82_remote_id_insertion is not None:
            data_payload["dhcp-option82-remote-id-insertion"] = (
                dhcp_option82_remote_id_insertion
            )
        if ptk_rekey is not None:
            data_payload["ptk-rekey"] = ptk_rekey
        if ptk_rekey_intv is not None:
            data_payload["ptk-rekey-intv"] = ptk_rekey_intv
        if gtk_rekey is not None:
            data_payload["gtk-rekey"] = gtk_rekey
        if gtk_rekey_intv is not None:
            data_payload["gtk-rekey-intv"] = gtk_rekey_intv
        if eap_reauth is not None:
            data_payload["eap-reauth"] = eap_reauth
        if eap_reauth_intv is not None:
            data_payload["eap-reauth-intv"] = eap_reauth_intv
        if roaming_acct_interim_update is not None:
            data_payload["roaming-acct-interim-update"] = (
                roaming_acct_interim_update
            )
        if qos_profile is not None:
            data_payload["qos-profile"] = qos_profile
        if hotspot20_profile is not None:
            data_payload["hotspot20-profile"] = hotspot20_profile
        if access_control_list is not None:
            data_payload["access-control-list"] = access_control_list
        if primary_wag_profile is not None:
            data_payload["primary-wag-profile"] = primary_wag_profile
        if secondary_wag_profile is not None:
            data_payload["secondary-wag-profile"] = secondary_wag_profile
        if tunnel_echo_interval is not None:
            data_payload["tunnel-echo-interval"] = tunnel_echo_interval
        if tunnel_fallback_interval is not None:
            data_payload["tunnel-fallback-interval"] = tunnel_fallback_interval
        if rates_11a is not None:
            data_payload["rates-11a"] = rates_11a
        if rates_11bg is not None:
            data_payload["rates-11bg"] = rates_11bg
        if rates_11n_ss12 is not None:
            data_payload["rates-11n-ss12"] = rates_11n_ss12
        if rates_11n_ss34 is not None:
            data_payload["rates-11n-ss34"] = rates_11n_ss34
        if rates_11ac_mcs_map is not None:
            data_payload["rates-11ac-mcs-map"] = rates_11ac_mcs_map
        if rates_11ax_mcs_map is not None:
            data_payload["rates-11ax-mcs-map"] = rates_11ax_mcs_map
        if rates_11be_mcs_map is not None:
            data_payload["rates-11be-mcs-map"] = rates_11be_mcs_map
        if rates_11be_mcs_map_160 is not None:
            data_payload["rates-11be-mcs-map-160"] = rates_11be_mcs_map_160
        if rates_11be_mcs_map_320 is not None:
            data_payload["rates-11be-mcs-map-320"] = rates_11be_mcs_map_320
        if utm_profile is not None:
            data_payload["utm-profile"] = utm_profile
        if utm_status is not None:
            data_payload["utm-status"] = utm_status
        if utm_log is not None:
            data_payload["utm-log"] = utm_log
        if ips_sensor is not None:
            data_payload["ips-sensor"] = ips_sensor
        if application_list is not None:
            data_payload["application-list"] = application_list
        if antivirus_profile is not None:
            data_payload["antivirus-profile"] = antivirus_profile
        if webfilter_profile is not None:
            data_payload["webfilter-profile"] = webfilter_profile
        if scan_botnet_connections is not None:
            data_payload["scan-botnet-connections"] = scan_botnet_connections
        if address_group is not None:
            data_payload["address-group"] = address_group
        if address_group_policy is not None:
            data_payload["address-group-policy"] = address_group_policy
        if sticky_client_remove is not None:
            data_payload["sticky-client-remove"] = sticky_client_remove
        if sticky_client_threshold_5g is not None:
            data_payload["sticky-client-threshold-5g"] = (
                sticky_client_threshold_5g
            )
        if sticky_client_threshold_2g is not None:
            data_payload["sticky-client-threshold-2g"] = (
                sticky_client_threshold_2g
            )
        if sticky_client_threshold_6g is not None:
            data_payload["sticky-client-threshold-6g"] = (
                sticky_client_threshold_6g
            )
        if bstm_rssi_disassoc_timer is not None:
            data_payload["bstm-rssi-disassoc-timer"] = bstm_rssi_disassoc_timer
        if bstm_load_balancing_disassoc_timer is not None:
            data_payload["bstm-load-balancing-disassoc-timer"] = (
                bstm_load_balancing_disassoc_timer
            )
        if bstm_disassociation_imminent is not None:
            data_payload["bstm-disassociation-imminent"] = (
                bstm_disassociation_imminent
            )
        if beacon_advertising is not None:
            data_payload["beacon-advertising"] = beacon_advertising
        if osen is not None:
            data_payload["osen"] = osen
        if application_detection_engine is not None:
            data_payload["application-detection-engine"] = (
                application_detection_engine
            )
        if application_dscp_marking is not None:
            data_payload["application-dscp-marking"] = application_dscp_marking
        if application_report_intv is not None:
            data_payload["application-report-intv"] = application_report_intv
        if l3_roaming is not None:
            data_payload["l3-roaming"] = l3_roaming
        if l3_roaming_mode is not None:
            data_payload["l3-roaming-mode"] = l3_roaming_mode
        data_payload.update(kwargs)
        return self._client.post(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )
