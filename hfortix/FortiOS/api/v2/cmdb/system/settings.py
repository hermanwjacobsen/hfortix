"""
FortiOS CMDB - Cmdb System Settings

Configuration endpoint for managing cmdb system settings objects.

API Endpoints:
    GET    /cmdb/system/settings
    PUT    /cmdb/system/settings/{identifier}

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.system.settings.get()
    >>>
    >>> # Get specific item (if supported)
    >>> item = fgt.api.cmdb.system.settings.get(name="item_name")
    >>>
    >>> # Create new item (use POST)
    >>> result = fgt.api.cmdb.system.settings.post(
    ...     name="new_item",
    ...     # ... additional parameters
    ... )
    >>>
    >>> # Update existing item (use PUT)
    >>> result = fgt.api.cmdb.system.settings.put(
    ...     name="existing_item",
    ...     # ... parameters to update
    ... )
    >>>
    >>> # Delete item
    >>> result = fgt.api.cmdb.system.settings.delete(name="item_name")

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


class Settings:
    """
    Settings Operations.

    Provides CRUD operations for FortiOS settings configuration.

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
        Initialize Settings endpoint.

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
        endpoint = "/system/settings"
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
        comments: str | None = None,
        vdom_type: str | None = None,
        lan_extension_controller_addr: str | None = None,
        lan_extension_controller_port: int | None = None,
        opmode: str | None = None,
        ngfw_mode: str | None = None,
        http_external_dest: str | None = None,
        firewall_session_dirty: str | None = None,
        manageip: str | None = None,
        gateway: str | None = None,
        ip: str | None = None,
        manageip6: str | None = None,
        gateway6: str | None = None,
        ip6: str | None = None,
        device: str | None = None,
        bfd: str | None = None,
        bfd_desired_min_tx: int | None = None,
        bfd_required_min_rx: int | None = None,
        bfd_detect_mult: int | None = None,
        bfd_dont_enforce_src_port: str | None = None,
        utf8_spam_tagging: str | None = None,
        wccp_cache_engine: str | None = None,
        vpn_stats_log: str | None = None,
        vpn_stats_period: int | None = None,
        v4_ecmp_mode: str | None = None,
        mac_ttl: int | None = None,
        fw_session_hairpin: str | None = None,
        prp_trailer_action: str | None = None,
        snat_hairpin_traffic: str | None = None,
        dhcp_proxy: str | None = None,
        dhcp_proxy_interface_select_method: str | None = None,
        dhcp_proxy_interface: str | None = None,
        dhcp_proxy_vrf_select: int | None = None,
        dhcp_server_ip: str | None = None,
        dhcp6_server_ip: str | None = None,
        central_nat: str | None = None,
        gui_default_policy_columns: list | None = None,
        lldp_reception: str | None = None,
        lldp_transmission: str | None = None,
        link_down_access: str | None = None,
        nat46_generate_ipv6_fragment_header: str | None = None,
        nat46_force_ipv4_packet_forwarding: str | None = None,
        nat64_force_ipv6_packet_forwarding: str | None = None,
        detect_unknown_esp: str | None = None,
        intree_ses_best_route: str | None = None,
        auxiliary_session: str | None = None,
        asymroute: str | None = None,
        asymroute_icmp: str | None = None,
        tcp_session_without_syn: str | None = None,
        ses_denied_traffic: str | None = None,
        ses_denied_multicast_traffic: str | None = None,
        strict_src_check: str | None = None,
        allow_linkdown_path: str | None = None,
        asymroute6: str | None = None,
        asymroute6_icmp: str | None = None,
        sctp_session_without_init: str | None = None,
        sip_expectation: str | None = None,
        sip_nat_trace: str | None = None,
        h323_direct_model: str | None = None,
        status: str | None = None,
        sip_tcp_port: int | None = None,
        sip_udp_port: int | None = None,
        sip_ssl_port: int | None = None,
        sccp_port: int | None = None,
        multicast_forward: str | None = None,
        multicast_ttl_notchange: str | None = None,
        multicast_skip_policy: str | None = None,
        allow_subnet_overlap: str | None = None,
        deny_tcp_with_icmp: str | None = None,
        ecmp_max_paths: int | None = None,
        discovered_device_timeout: int | None = None,
        email_portal_check_dns: str | None = None,
        default_voip_alg_mode: str | None = None,
        gui_icap: str | None = None,
        gui_implicit_policy: str | None = None,
        gui_dns_database: str | None = None,
        gui_load_balance: str | None = None,
        gui_multicast_policy: str | None = None,
        gui_dos_policy: str | None = None,
        gui_object_colors: str | None = None,
        gui_route_tag_address_creation: str | None = None,
        gui_voip_profile: str | None = None,
        gui_ap_profile: str | None = None,
        gui_security_profile_group: str | None = None,
        gui_local_in_policy: str | None = None,
        gui_explicit_proxy: str | None = None,
        gui_dynamic_routing: str | None = None,
        gui_policy_based_ipsec: str | None = None,
        gui_threat_weight: str | None = None,
        gui_spamfilter: str | None = None,
        gui_file_filter: str | None = None,
        gui_application_control: str | None = None,
        gui_ips: str | None = None,
        gui_dhcp_advanced: str | None = None,
        gui_vpn: str | None = None,
        gui_wireless_controller: str | None = None,
        gui_advanced_wireless_features: str | None = None,
        gui_switch_controller: str | None = None,
        gui_fortiap_split_tunneling: str | None = None,
        gui_webfilter_advanced: str | None = None,
        gui_traffic_shaping: str | None = None,
        gui_wan_load_balancing: str | None = None,
        gui_antivirus: str | None = None,
        gui_webfilter: str | None = None,
        gui_videofilter: str | None = None,
        gui_dnsfilter: str | None = None,
        gui_waf_profile: str | None = None,
        gui_dlp_profile: str | None = None,
        gui_dlp_advanced: str | None = None,
        gui_virtual_patch_profile: str | None = None,
        gui_casb: str | None = None,
        gui_fortiextender_controller: str | None = None,
        gui_advanced_policy: str | None = None,
        gui_allow_unnamed_policy: str | None = None,
        gui_email_collection: str | None = None,
        gui_multiple_interface_policy: str | None = None,
        gui_policy_disclaimer: str | None = None,
        gui_ztna: str | None = None,
        gui_ot: str | None = None,
        gui_dynamic_device_os_id: str | None = None,
        location_id: str | None = None,
        ike_session_resume: str | None = None,
        ike_quick_crash_detect: str | None = None,
        ike_dn_format: str | None = None,
        ike_port: int | None = None,
        ike_tcp_port: int | None = None,
        ike_policy_route: str | None = None,
        ike_detailed_event_logs: str | None = None,
        block_land_attack: str | None = None,
        default_app_port_as_service: str | None = None,
        fqdn_session_check: str | None = None,
        ext_resource_session_check: str | None = None,
        dyn_addr_session_check: str | None = None,
        default_policy_expiry_days: int | None = None,
        gui_enforce_change_summary: str | None = None,
        internet_service_database_cache: str | None = None,
        internet_service_app_ctrl_size: int | None = None,
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
            comments: VDOM comments. (optional)
            vdom_type: Vdom type (traffic, lan-extension or admin). (optional)
            lan_extension_controller_addr: Controller IP address or FQDN to
            connect. (optional)
            lan_extension_controller_port: Controller port to connect.
            (optional)
            opmode: Firewall operation mode (NAT or Transparent). (optional)
            ngfw_mode: Next Generation Firewall (NGFW) mode. (optional)
            http_external_dest: Offload HTTP traffic to FortiWeb or FortiCache.
            (optional)
            firewall_session_dirty: Select how to manage sessions affected by
            firewall policy configuration changes. (optional)
            manageip: Transparent mode IPv4 management IP address and netmask.
            (optional)
            gateway: Transparent mode IPv4 default gateway IP address.
            (optional)
            ip: IP address and netmask. (optional)
            manageip6: Transparent mode IPv6 management IP address and netmask.
            (optional)
            gateway6: Transparent mode IPv6 default gateway IP address.
            (optional)
            ip6: IPv6 address prefix for NAT mode. (optional)
            device: Interface to use for management access for NAT mode.
            (optional)
            bfd: Enable/disable Bi-directional Forwarding Detection (BFD) on
            all interfaces. (optional)
            bfd_desired_min_tx: BFD desired minimal transmit interval (1 -
            100000 ms, default = 250). (optional)
            bfd_required_min_rx: BFD required minimal receive interval (1 -
            100000 ms, default = 250). (optional)
            bfd_detect_mult: BFD detection multiplier (1 - 50, default = 3).
            (optional)
            bfd_dont_enforce_src_port: Enable to not enforce verifying the
            source port of BFD Packets. (optional)
            utf8_spam_tagging: Enable/disable converting antispam tags to UTF-8
            for better non-ASCII character support. (optional)
            wccp_cache_engine: Enable/disable WCCP cache engine. (optional)
            vpn_stats_log: Enable/disable periodic VPN log statistics for one
            or more types of VPN. Separate names with a space. (optional)
            vpn_stats_period: Period to send VPN log statistics (0 or 60 -
            86400 sec). (optional)
            v4_ecmp_mode: IPv4 Equal-cost multi-path (ECMP) routing and load
            balancing mode. (optional)
            mac_ttl: Duration of MAC addresses in Transparent mode (300 -
            8640000 sec, default = 300). (optional)
            fw_session_hairpin: Enable/disable checking for a matching policy
            each time hairpin traffic goes through the FortiGate. (optional)
            prp_trailer_action: Enable/disable action to take on PRP trailer.
            (optional)
            snat_hairpin_traffic: Enable/disable source NAT (SNAT) for VIP
            hairpin traffic. (optional)
            dhcp_proxy: Enable/disable the DHCP Proxy. (optional)
            dhcp_proxy_interface_select_method: Specify how to select outgoing
            interface to reach server. (optional)
            dhcp_proxy_interface: Specify outgoing interface to reach server.
            (optional)
            dhcp_proxy_vrf_select: VRF ID used for connection to server.
            (optional)
            dhcp_server_ip: DHCP Server IPv4 address. (optional)
            dhcp6_server_ip: DHCPv6 server IPv6 address. (optional)
            central_nat: Enable/disable central NAT. (optional)
            gui_default_policy_columns: Default columns to display for policy
            lists on GUI. (optional)
            lldp_reception: Enable/disable Link Layer Discovery Protocol (LLDP)
            reception for this VDOM or apply global settings to this VDOM.
            (optional)
            lldp_transmission: Enable/disable Link Layer Discovery Protocol
            (LLDP) transmission for this VDOM or apply global settings to this
            VDOM. (optional)
            link_down_access: Enable/disable link down access traffic.
            (optional)
            nat46_generate_ipv6_fragment_header: Enable/disable NAT46 IPv6
            fragment header generation. (optional)
            nat46_force_ipv4_packet_forwarding: Enable/disable mandatory IPv4
            packet forwarding in NAT46. (optional)
            nat64_force_ipv6_packet_forwarding: Enable/disable mandatory IPv6
            packet forwarding in NAT64. (optional)
            detect_unknown_esp: Enable/disable detection of unknown ESP packets
            (default = enable). (optional)
            intree_ses_best_route: Force the intree session to always use the
            best route. (optional)
            auxiliary_session: Enable/disable auxiliary session. (optional)
            asymroute: Enable/disable IPv4 asymmetric routing. (optional)
            asymroute_icmp: Enable/disable ICMP asymmetric routing. (optional)
            tcp_session_without_syn: Enable/disable allowing TCP session
            without SYN flags. (optional)
            ses_denied_traffic: Enable/disable including denied session in the
            session table. (optional)
            ses_denied_multicast_traffic: Enable/disable including denied
            multicast session in the session table. (optional)
            strict_src_check: Enable/disable strict source verification.
            (optional)
            allow_linkdown_path: Enable/disable link down path. (optional)
            asymroute6: Enable/disable asymmetric IPv6 routing. (optional)
            asymroute6_icmp: Enable/disable asymmetric ICMPv6 routing.
            (optional)
            sctp_session_without_init: Enable/disable SCTP session creation
            without SCTP INIT. (optional)
            sip_expectation: Enable/disable the SIP kernel session helper to
            create an expectation for port 5060. (optional)
            sip_nat_trace: Enable/disable recording the original SIP source IP
            address when NAT is used. (optional)
            h323_direct_model: Enable/disable H323 direct model. (optional)
            status: Enable/disable this VDOM. (optional)
            sip_tcp_port: TCP port the SIP proxy monitors for SIP traffic (0 -
            65535, default = 5060). (optional)
            sip_udp_port: UDP port the SIP proxy monitors for SIP traffic (0 -
            65535, default = 5060). (optional)
            sip_ssl_port: TCP port the SIP proxy monitors for SIP SSL/TLS
            traffic (0 - 65535, default = 5061). (optional)
            sccp_port: TCP port the SCCP proxy monitors for SCCP traffic (0 -
            65535, default = 2000). (optional)
            multicast_forward: Enable/disable multicast forwarding. (optional)
            multicast_ttl_notchange: Enable/disable preventing the FortiGate
            from changing the TTL for forwarded multicast packets. (optional)
            multicast_skip_policy: Enable/disable allowing multicast traffic
            through the FortiGate without a policy check. (optional)
            allow_subnet_overlap: Enable/disable allowing interface subnets to
            use overlapping IP addresses. (optional)
            deny_tcp_with_icmp: Enable/disable denying TCP by sending an ICMP
            communication prohibited packet. (optional)
            ecmp_max_paths: Maximum number of Equal Cost Multi-Path (ECMP)
            next-hops. Set to 1 to disable ECMP routing (1 - 255, default =
            255). (optional)
            discovered_device_timeout: Timeout for discovered devices (1 - 365
            days, default = 28). (optional)
            email_portal_check_dns: Enable/disable using DNS to validate email
            addresses collected by a captive portal. (optional)
            default_voip_alg_mode: Configure how the FortiGate handles VoIP
            traffic when a policy that accepts the traffic doesn't include a
            VoIP profile. (optional)
            gui_icap: Enable/disable ICAP on the GUI. (optional)
            gui_implicit_policy: Enable/disable implicit firewall policies on
            the GUI. (optional)
            gui_dns_database: Enable/disable DNS database settings on the GUI.
            (optional)
            gui_load_balance: Enable/disable server load balancing on the GUI.
            (optional)
            gui_multicast_policy: Enable/disable multicast firewall policies on
            the GUI. (optional)
            gui_dos_policy: Enable/disable DoS policies on the GUI. (optional)
            gui_object_colors: Enable/disable object colors on the GUI.
            (optional)
            gui_route_tag_address_creation: Enable/disable route-tag addresses
            on the GUI. (optional)
            gui_voip_profile: Enable/disable VoIP profiles on the GUI.
            (optional)
            gui_ap_profile: Enable/disable FortiAP profiles on the GUI.
            (optional)
            gui_security_profile_group: Enable/disable Security Profile Groups
            on the GUI. (optional)
            gui_local_in_policy: Enable/disable Local-In policies on the GUI.
            (optional)
            gui_explicit_proxy: Enable/disable the explicit proxy on the GUI.
            (optional)
            gui_dynamic_routing: Enable/disable dynamic routing on the GUI.
            (optional)
            gui_policy_based_ipsec: Enable/disable policy-based IPsec VPN on
            the GUI. (optional)
            gui_threat_weight: Enable/disable threat weight on the GUI.
            (optional)
            gui_spamfilter: Enable/disable Antispam on the GUI. (optional)
            gui_file_filter: Enable/disable File-filter on the GUI. (optional)
            gui_application_control: Enable/disable application control on the
            GUI. (optional)
            gui_ips: Enable/disable IPS on the GUI. (optional)
            gui_dhcp_advanced: Enable/disable advanced DHCP options on the GUI.
            (optional)
            gui_vpn: Enable/disable IPsec VPN settings pages on the GUI.
            (optional)
            gui_wireless_controller: Enable/disable the wireless controller on
            the GUI. (optional)
            gui_advanced_wireless_features: Enable/disable advanced wireless
            features in GUI. (optional)
            gui_switch_controller: Enable/disable the switch controller on the
            GUI. (optional)
            gui_fortiap_split_tunneling: Enable/disable FortiAP split tunneling
            on the GUI. (optional)
            gui_webfilter_advanced: Enable/disable advanced web filtering on
            the GUI. (optional)
            gui_traffic_shaping: Enable/disable traffic shaping on the GUI.
            (optional)
            gui_wan_load_balancing: Enable/disable SD-WAN on the GUI.
            (optional)
            gui_antivirus: Enable/disable AntiVirus on the GUI. (optional)
            gui_webfilter: Enable/disable Web filtering on the GUI. (optional)
            gui_videofilter: Enable/disable Video filtering on the GUI.
            (optional)
            gui_dnsfilter: Enable/disable DNS Filtering on the GUI. (optional)
            gui_waf_profile: Enable/disable Web Application Firewall on the
            GUI. (optional)
            gui_dlp_profile: Enable/disable Data Loss Prevention on the GUI.
            (optional)
            gui_dlp_advanced: Enable/disable Show advanced DLP expressions on
            the GUI. (optional)
            gui_virtual_patch_profile: Enable/disable Virtual Patching on the
            GUI. (optional)
            gui_casb: Enable/disable Inline-CASB on the GUI. (optional)
            gui_fortiextender_controller: Enable/disable FortiExtender on the
            GUI. (optional)
            gui_advanced_policy: Enable/disable advanced policy configuration
            on the GUI. (optional)
            gui_allow_unnamed_policy: Enable/disable the requirement for policy
            naming on the GUI. (optional)
            gui_email_collection: Enable/disable email collection on the GUI.
            (optional)
            gui_multiple_interface_policy: Enable/disable adding multiple
            interfaces to a policy on the GUI. (optional)
            gui_policy_disclaimer: Enable/disable policy disclaimer on the GUI.
            (optional)
            gui_ztna: Enable/disable Zero Trust Network Access features on the
            GUI. (optional)
            gui_ot: Enable/disable Operational technology features on the GUI.
            (optional)
            gui_dynamic_device_os_id: Enable/disable Create dynamic addresses
            to manage known devices. (optional)
            location_id: Local location ID in the form of an IPv4 address.
            (optional)
            ike_session_resume: Enable/disable IKEv2 session resumption (RFC
            5723). (optional)
            ike_quick_crash_detect: Enable/disable IKE quick crash detection
            (RFC 6290). (optional)
            ike_dn_format: Configure IKE ASN.1 Distinguished Name format
            conventions. (optional)
            ike_port: UDP port for IKE/IPsec traffic (default 500). (optional)
            ike_tcp_port: TCP port for IKE/IPsec traffic (default 443).
            (optional)
            ike_policy_route: Enable/disable IKE Policy Based Routing (PBR).
            (optional)
            ike_detailed_event_logs: Enable/disable detail log for IKE events.
            (optional)
            block_land_attack: Enable/disable blocking of land attacks.
            (optional)
            default_app_port_as_service: Enable/disable policy service
            enforcement based on application default ports. (optional)
            fqdn_session_check: Enable/disable dirty session check caused by
            FQDN updates. (optional)
            ext_resource_session_check: Enable/disable dirty session check
            caused by external resource updates. (optional)
            dyn_addr_session_check: Enable/disable dirty session check caused
            by dynamic address updates. (optional)
            default_policy_expiry_days: Default policy expiry in days (0 - 365
            days, default = 30). (optional)
            gui_enforce_change_summary: Enforce change summaries for select
            tables in the GUI. (optional)
            internet_service_database_cache: Enable/disable Internet Service
            database caching. (optional)
            internet_service_app_ctrl_size: Maximum number of tuple entries
            (protocol, port, IP address, application ID) stored by the
            FortiGate unit (0 - 4294967295, default = 32768). A smaller value
            limits the FortiGate unit from learning about internet
            applications. (optional)
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
        endpoint = "/system/settings"
        if before is not None:
            data_payload["before"] = before
        if after is not None:
            data_payload["after"] = after
        if comments is not None:
            data_payload["comments"] = comments
        if vdom_type is not None:
            data_payload["vdom-type"] = vdom_type
        if lan_extension_controller_addr is not None:
            data_payload["lan-extension-controller-addr"] = (
                lan_extension_controller_addr
            )
        if lan_extension_controller_port is not None:
            data_payload["lan-extension-controller-port"] = (
                lan_extension_controller_port
            )
        if opmode is not None:
            data_payload["opmode"] = opmode
        if ngfw_mode is not None:
            data_payload["ngfw-mode"] = ngfw_mode
        if http_external_dest is not None:
            data_payload["http-external-dest"] = http_external_dest
        if firewall_session_dirty is not None:
            data_payload["firewall-session-dirty"] = firewall_session_dirty
        if manageip is not None:
            data_payload["manageip"] = manageip
        if gateway is not None:
            data_payload["gateway"] = gateway
        if ip is not None:
            data_payload["ip"] = ip
        if manageip6 is not None:
            data_payload["manageip6"] = manageip6
        if gateway6 is not None:
            data_payload["gateway6"] = gateway6
        if ip6 is not None:
            data_payload["ip6"] = ip6
        if device is not None:
            data_payload["device"] = device
        if bfd is not None:
            data_payload["bfd"] = bfd
        if bfd_desired_min_tx is not None:
            data_payload["bfd-desired-min-tx"] = bfd_desired_min_tx
        if bfd_required_min_rx is not None:
            data_payload["bfd-required-min-rx"] = bfd_required_min_rx
        if bfd_detect_mult is not None:
            data_payload["bfd-detect-mult"] = bfd_detect_mult
        if bfd_dont_enforce_src_port is not None:
            data_payload["bfd-dont-enforce-src-port"] = (
                bfd_dont_enforce_src_port
            )
        if utf8_spam_tagging is not None:
            data_payload["utf8-spam-tagging"] = utf8_spam_tagging
        if wccp_cache_engine is not None:
            data_payload["wccp-cache-engine"] = wccp_cache_engine
        if vpn_stats_log is not None:
            data_payload["vpn-stats-log"] = vpn_stats_log
        if vpn_stats_period is not None:
            data_payload["vpn-stats-period"] = vpn_stats_period
        if v4_ecmp_mode is not None:
            data_payload["v4-ecmp-mode"] = v4_ecmp_mode
        if mac_ttl is not None:
            data_payload["mac-ttl"] = mac_ttl
        if fw_session_hairpin is not None:
            data_payload["fw-session-hairpin"] = fw_session_hairpin
        if prp_trailer_action is not None:
            data_payload["prp-trailer-action"] = prp_trailer_action
        if snat_hairpin_traffic is not None:
            data_payload["snat-hairpin-traffic"] = snat_hairpin_traffic
        if dhcp_proxy is not None:
            data_payload["dhcp-proxy"] = dhcp_proxy
        if dhcp_proxy_interface_select_method is not None:
            data_payload["dhcp-proxy-interface-select-method"] = (
                dhcp_proxy_interface_select_method
            )
        if dhcp_proxy_interface is not None:
            data_payload["dhcp-proxy-interface"] = dhcp_proxy_interface
        if dhcp_proxy_vrf_select is not None:
            data_payload["dhcp-proxy-vrf-select"] = dhcp_proxy_vrf_select
        if dhcp_server_ip is not None:
            data_payload["dhcp-server-ip"] = dhcp_server_ip
        if dhcp6_server_ip is not None:
            data_payload["dhcp6-server-ip"] = dhcp6_server_ip
        if central_nat is not None:
            data_payload["central-nat"] = central_nat
        if gui_default_policy_columns is not None:
            data_payload["gui-default-policy-columns"] = (
                gui_default_policy_columns
            )
        if lldp_reception is not None:
            data_payload["lldp-reception"] = lldp_reception
        if lldp_transmission is not None:
            data_payload["lldp-transmission"] = lldp_transmission
        if link_down_access is not None:
            data_payload["link-down-access"] = link_down_access
        if nat46_generate_ipv6_fragment_header is not None:
            data_payload["nat46-generate-ipv6-fragment-header"] = (
                nat46_generate_ipv6_fragment_header
            )
        if nat46_force_ipv4_packet_forwarding is not None:
            data_payload["nat46-force-ipv4-packet-forwarding"] = (
                nat46_force_ipv4_packet_forwarding
            )
        if nat64_force_ipv6_packet_forwarding is not None:
            data_payload["nat64-force-ipv6-packet-forwarding"] = (
                nat64_force_ipv6_packet_forwarding
            )
        if detect_unknown_esp is not None:
            data_payload["detect-unknown-esp"] = detect_unknown_esp
        if intree_ses_best_route is not None:
            data_payload["intree-ses-best-route"] = intree_ses_best_route
        if auxiliary_session is not None:
            data_payload["auxiliary-session"] = auxiliary_session
        if asymroute is not None:
            data_payload["asymroute"] = asymroute
        if asymroute_icmp is not None:
            data_payload["asymroute-icmp"] = asymroute_icmp
        if tcp_session_without_syn is not None:
            data_payload["tcp-session-without-syn"] = tcp_session_without_syn
        if ses_denied_traffic is not None:
            data_payload["ses-denied-traffic"] = ses_denied_traffic
        if ses_denied_multicast_traffic is not None:
            data_payload["ses-denied-multicast-traffic"] = (
                ses_denied_multicast_traffic
            )
        if strict_src_check is not None:
            data_payload["strict-src-check"] = strict_src_check
        if allow_linkdown_path is not None:
            data_payload["allow-linkdown-path"] = allow_linkdown_path
        if asymroute6 is not None:
            data_payload["asymroute6"] = asymroute6
        if asymroute6_icmp is not None:
            data_payload["asymroute6-icmp"] = asymroute6_icmp
        if sctp_session_without_init is not None:
            data_payload["sctp-session-without-init"] = (
                sctp_session_without_init
            )
        if sip_expectation is not None:
            data_payload["sip-expectation"] = sip_expectation
        if sip_nat_trace is not None:
            data_payload["sip-nat-trace"] = sip_nat_trace
        if h323_direct_model is not None:
            data_payload["h323-direct-model"] = h323_direct_model
        if status is not None:
            data_payload["status"] = status
        if sip_tcp_port is not None:
            data_payload["sip-tcp-port"] = sip_tcp_port
        if sip_udp_port is not None:
            data_payload["sip-udp-port"] = sip_udp_port
        if sip_ssl_port is not None:
            data_payload["sip-ssl-port"] = sip_ssl_port
        if sccp_port is not None:
            data_payload["sccp-port"] = sccp_port
        if multicast_forward is not None:
            data_payload["multicast-forward"] = multicast_forward
        if multicast_ttl_notchange is not None:
            data_payload["multicast-ttl-notchange"] = multicast_ttl_notchange
        if multicast_skip_policy is not None:
            data_payload["multicast-skip-policy"] = multicast_skip_policy
        if allow_subnet_overlap is not None:
            data_payload["allow-subnet-overlap"] = allow_subnet_overlap
        if deny_tcp_with_icmp is not None:
            data_payload["deny-tcp-with-icmp"] = deny_tcp_with_icmp
        if ecmp_max_paths is not None:
            data_payload["ecmp-max-paths"] = ecmp_max_paths
        if discovered_device_timeout is not None:
            data_payload["discovered-device-timeout"] = (
                discovered_device_timeout
            )
        if email_portal_check_dns is not None:
            data_payload["email-portal-check-dns"] = email_portal_check_dns
        if default_voip_alg_mode is not None:
            data_payload["default-voip-alg-mode"] = default_voip_alg_mode
        if gui_icap is not None:
            data_payload["gui-icap"] = gui_icap
        if gui_implicit_policy is not None:
            data_payload["gui-implicit-policy"] = gui_implicit_policy
        if gui_dns_database is not None:
            data_payload["gui-dns-database"] = gui_dns_database
        if gui_load_balance is not None:
            data_payload["gui-load-balance"] = gui_load_balance
        if gui_multicast_policy is not None:
            data_payload["gui-multicast-policy"] = gui_multicast_policy
        if gui_dos_policy is not None:
            data_payload["gui-dos-policy"] = gui_dos_policy
        if gui_object_colors is not None:
            data_payload["gui-object-colors"] = gui_object_colors
        if gui_route_tag_address_creation is not None:
            data_payload["gui-route-tag-address-creation"] = (
                gui_route_tag_address_creation
            )
        if gui_voip_profile is not None:
            data_payload["gui-voip-profile"] = gui_voip_profile
        if gui_ap_profile is not None:
            data_payload["gui-ap-profile"] = gui_ap_profile
        if gui_security_profile_group is not None:
            data_payload["gui-security-profile-group"] = (
                gui_security_profile_group
            )
        if gui_local_in_policy is not None:
            data_payload["gui-local-in-policy"] = gui_local_in_policy
        if gui_explicit_proxy is not None:
            data_payload["gui-explicit-proxy"] = gui_explicit_proxy
        if gui_dynamic_routing is not None:
            data_payload["gui-dynamic-routing"] = gui_dynamic_routing
        if gui_policy_based_ipsec is not None:
            data_payload["gui-policy-based-ipsec"] = gui_policy_based_ipsec
        if gui_threat_weight is not None:
            data_payload["gui-threat-weight"] = gui_threat_weight
        if gui_spamfilter is not None:
            data_payload["gui-spamfilter"] = gui_spamfilter
        if gui_file_filter is not None:
            data_payload["gui-file-filter"] = gui_file_filter
        if gui_application_control is not None:
            data_payload["gui-application-control"] = gui_application_control
        if gui_ips is not None:
            data_payload["gui-ips"] = gui_ips
        if gui_dhcp_advanced is not None:
            data_payload["gui-dhcp-advanced"] = gui_dhcp_advanced
        if gui_vpn is not None:
            data_payload["gui-vpn"] = gui_vpn
        if gui_wireless_controller is not None:
            data_payload["gui-wireless-controller"] = gui_wireless_controller
        if gui_advanced_wireless_features is not None:
            data_payload["gui-advanced-wireless-features"] = (
                gui_advanced_wireless_features
            )
        if gui_switch_controller is not None:
            data_payload["gui-switch-controller"] = gui_switch_controller
        if gui_fortiap_split_tunneling is not None:
            data_payload["gui-fortiap-split-tunneling"] = (
                gui_fortiap_split_tunneling
            )
        if gui_webfilter_advanced is not None:
            data_payload["gui-webfilter-advanced"] = gui_webfilter_advanced
        if gui_traffic_shaping is not None:
            data_payload["gui-traffic-shaping"] = gui_traffic_shaping
        if gui_wan_load_balancing is not None:
            data_payload["gui-wan-load-balancing"] = gui_wan_load_balancing
        if gui_antivirus is not None:
            data_payload["gui-antivirus"] = gui_antivirus
        if gui_webfilter is not None:
            data_payload["gui-webfilter"] = gui_webfilter
        if gui_videofilter is not None:
            data_payload["gui-videofilter"] = gui_videofilter
        if gui_dnsfilter is not None:
            data_payload["gui-dnsfilter"] = gui_dnsfilter
        if gui_waf_profile is not None:
            data_payload["gui-waf-profile"] = gui_waf_profile
        if gui_dlp_profile is not None:
            data_payload["gui-dlp-profile"] = gui_dlp_profile
        if gui_dlp_advanced is not None:
            data_payload["gui-dlp-advanced"] = gui_dlp_advanced
        if gui_virtual_patch_profile is not None:
            data_payload["gui-virtual-patch-profile"] = (
                gui_virtual_patch_profile
            )
        if gui_casb is not None:
            data_payload["gui-casb"] = gui_casb
        if gui_fortiextender_controller is not None:
            data_payload["gui-fortiextender-controller"] = (
                gui_fortiextender_controller
            )
        if gui_advanced_policy is not None:
            data_payload["gui-advanced-policy"] = gui_advanced_policy
        if gui_allow_unnamed_policy is not None:
            data_payload["gui-allow-unnamed-policy"] = gui_allow_unnamed_policy
        if gui_email_collection is not None:
            data_payload["gui-email-collection"] = gui_email_collection
        if gui_multiple_interface_policy is not None:
            data_payload["gui-multiple-interface-policy"] = (
                gui_multiple_interface_policy
            )
        if gui_policy_disclaimer is not None:
            data_payload["gui-policy-disclaimer"] = gui_policy_disclaimer
        if gui_ztna is not None:
            data_payload["gui-ztna"] = gui_ztna
        if gui_ot is not None:
            data_payload["gui-ot"] = gui_ot
        if gui_dynamic_device_os_id is not None:
            data_payload["gui-dynamic-device-os-id"] = gui_dynamic_device_os_id
        if location_id is not None:
            data_payload["location-id"] = location_id
        if ike_session_resume is not None:
            data_payload["ike-session-resume"] = ike_session_resume
        if ike_quick_crash_detect is not None:
            data_payload["ike-quick-crash-detect"] = ike_quick_crash_detect
        if ike_dn_format is not None:
            data_payload["ike-dn-format"] = ike_dn_format
        if ike_port is not None:
            data_payload["ike-port"] = ike_port
        if ike_tcp_port is not None:
            data_payload["ike-tcp-port"] = ike_tcp_port
        if ike_policy_route is not None:
            data_payload["ike-policy-route"] = ike_policy_route
        if ike_detailed_event_logs is not None:
            data_payload["ike-detailed-event-logs"] = ike_detailed_event_logs
        if block_land_attack is not None:
            data_payload["block-land-attack"] = block_land_attack
        if default_app_port_as_service is not None:
            data_payload["default-app-port-as-service"] = (
                default_app_port_as_service
            )
        if fqdn_session_check is not None:
            data_payload["fqdn-session-check"] = fqdn_session_check
        if ext_resource_session_check is not None:
            data_payload["ext-resource-session-check"] = (
                ext_resource_session_check
            )
        if dyn_addr_session_check is not None:
            data_payload["dyn-addr-session-check"] = dyn_addr_session_check
        if default_policy_expiry_days is not None:
            data_payload["default-policy-expiry-days"] = (
                default_policy_expiry_days
            )
        if gui_enforce_change_summary is not None:
            data_payload["gui-enforce-change-summary"] = (
                gui_enforce_change_summary
            )
        if internet_service_database_cache is not None:
            data_payload["internet-service-database-cache"] = (
                internet_service_database_cache
            )
        if internet_service_app_ctrl_size is not None:
            data_payload["internet-service-app-ctrl-size"] = (
                internet_service_app_ctrl_size
            )
        data_payload.update(kwargs)
        return self._client.put(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )
