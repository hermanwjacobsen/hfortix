"""
FortiOS CMDB - Cmdb System Interface

Configuration endpoint for managing cmdb system interface objects.

API Endpoints:
    GET    /cmdb/system/interface
    POST   /cmdb/system/interface
    GET    /cmdb/system/interface
    PUT    /cmdb/system/interface/{identifier}
    DELETE /cmdb/system/interface/{identifier}

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.system.interface.get()
    >>>
    >>> # Get specific item (if supported)
    >>> item = fgt.api.cmdb.system.interface.get(name="item_name")
    >>>
    >>> # Create new item (use POST)
    >>> result = fgt.api.cmdb.system.interface.post(
    ...     name="new_item",
    ...     # ... additional parameters
    ... )
    >>>
    >>> # Update existing item (use PUT)
    >>> result = fgt.api.cmdb.system.interface.put(
    ...     name="existing_item",
    ...     # ... parameters to update
    ... )
    >>>
    >>> # Delete item
    >>> result = fgt.api.cmdb.system.interface.delete(name="item_name")

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


class Interface:
    """
    Interface Operations.

    Provides CRUD operations for FortiOS interface configuration.

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
        Initialize Interface endpoint.

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
            endpoint = f"/system/interface/{name}"
        else:
            endpoint = "/system/interface"
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
        vrf: int | None = None,
        cli_conn_status: int | None = None,
        fortilink: str | None = None,
        switch_controller_source_ip: str | None = None,
        mode: str | None = None,
        client_options: list | None = None,
        distance: int | None = None,
        priority: int | None = None,
        dhcp_relay_interface_select_method: str | None = None,
        dhcp_relay_interface: str | None = None,
        dhcp_relay_vrf_select: int | None = None,
        dhcp_broadcast_flag: str | None = None,
        dhcp_relay_service: str | None = None,
        dhcp_relay_ip: str | None = None,
        dhcp_relay_source_ip: str | None = None,
        dhcp_relay_circuit_id: str | None = None,
        dhcp_relay_link_selection: str | None = None,
        dhcp_relay_request_all_server: str | None = None,
        dhcp_relay_allow_no_end_option: str | None = None,
        dhcp_relay_type: str | None = None,
        dhcp_smart_relay: str | None = None,
        dhcp_relay_agent_option: str | None = None,
        dhcp_classless_route_addition: str | None = None,
        management_ip: str | None = None,
        ip: str | None = None,
        allowaccess: str | None = None,
        gwdetect: str | None = None,
        ping_serv_status: int | None = None,
        detectserver: str | None = None,
        detectprotocol: str | None = None,
        ha_priority: int | None = None,
        fail_detect: str | None = None,
        fail_detect_option: str | None = None,
        fail_alert_method: str | None = None,
        fail_action_on_extender: str | None = None,
        fail_alert_interfaces: list | None = None,
        dhcp_client_identifier: str | None = None,
        dhcp_renew_time: int | None = None,
        ipunnumbered: str | None = None,
        username: str | None = None,
        pppoe_egress_cos: str | None = None,
        pppoe_unnumbered_negotiate: str | None = None,
        password: str | None = None,
        idle_timeout: int | None = None,
        multilink: str | None = None,
        mrru: int | None = None,
        detected_peer_mtu: int | None = None,
        disc_retry_timeout: int | None = None,
        padt_retry_timeout: int | None = None,
        service_name: str | None = None,
        ac_name: str | None = None,
        lcp_echo_interval: int | None = None,
        lcp_max_echo_fails: int | None = None,
        defaultgw: str | None = None,
        dns_server_override: str | None = None,
        dns_server_protocol: str | None = None,
        auth_type: str | None = None,
        pptp_client: str | None = None,
        pptp_user: str | None = None,
        pptp_password: str | None = None,
        pptp_server_ip: str | None = None,
        pptp_auth_type: str | None = None,
        pptp_timeout: int | None = None,
        arpforward: str | None = None,
        ndiscforward: str | None = None,
        broadcast_forward: str | None = None,
        bfd: str | None = None,
        bfd_desired_min_tx: int | None = None,
        bfd_detect_mult: int | None = None,
        bfd_required_min_rx: int | None = None,
        l2forward: str | None = None,
        icmp_send_redirect: str | None = None,
        icmp_accept_redirect: str | None = None,
        reachable_time: int | None = None,
        vlanforward: str | None = None,
        stpforward: str | None = None,
        stpforward_mode: str | None = None,
        ips_sniffer_mode: str | None = None,
        ident_accept: str | None = None,
        ipmac: str | None = None,
        subst: str | None = None,
        macaddr: str | None = None,
        virtual_mac: str | None = None,
        substitute_dst_mac: str | None = None,
        speed: str | None = None,
        status: str | None = None,
        netbios_forward: str | None = None,
        wins_ip: str | None = None,
        type: str | None = None,
        dedicated_to: str | None = None,
        trust_ip_1: str | None = None,
        trust_ip_2: str | None = None,
        trust_ip_3: str | None = None,
        trust_ip6_1: str | None = None,
        trust_ip6_2: str | None = None,
        trust_ip6_3: str | None = None,
        wccp: str | None = None,
        netflow_sampler: str | None = None,
        netflow_sample_rate: int | None = None,
        netflow_sampler_id: int | None = None,
        sflow_sampler: str | None = None,
        drop_fragment: str | None = None,
        src_check: str | None = None,
        sample_rate: int | None = None,
        polling_interval: int | None = None,
        sample_direction: str | None = None,
        explicit_web_proxy: str | None = None,
        explicit_ftp_proxy: str | None = None,
        proxy_captive_portal: str | None = None,
        tcp_mss: int | None = None,
        inbandwidth: int | None = None,
        outbandwidth: int | None = None,
        egress_shaping_profile: str | None = None,
        ingress_shaping_profile: str | None = None,
        spillover_threshold: int | None = None,
        ingress_spillover_threshold: int | None = None,
        weight: int | None = None,
        interface: str | None = None,
        external: str | None = None,
        mtu_override: str | None = None,
        mtu: int | None = None,
        vlan_protocol: str | None = None,
        vlanid: int | None = None,
        trunk: str | None = None,
        forward_domain: int | None = None,
        remote_ip: str | None = None,
        member: list | None = None,
        lacp_mode: str | None = None,
        lacp_ha_secondary: str | None = None,
        system_id_type: str | None = None,
        system_id: str | None = None,
        lacp_speed: str | None = None,
        min_links: int | None = None,
        min_links_down: str | None = None,
        algorithm: str | None = None,
        link_up_delay: int | None = None,
        aggregate_type: str | None = None,
        priority_override: str | None = None,
        aggregate: str | None = None,
        redundant_interface: str | None = None,
        devindex: int | None = None,
        vindex: int | None = None,
        switch: str | None = None,
        description: str | None = None,
        alias: str | None = None,
        l2tp_client: str | None = None,
        l2tp_client_settings: list | None = None,
        security_mode: str | None = None,
        security_mac_auth_bypass: str | None = None,
        security_ip_auth_bypass: str | None = None,
        security_8021x_mode: str | None = None,
        security_8021x_master: str | None = None,
        security_8021x_dynamic_vlan_id: int | None = None,
        security_8021x_member_mode: str | None = None,
        security_external_web: str | None = None,
        security_external_logout: str | None = None,
        replacemsg_override_group: str | None = None,
        security_redirect_url: str | None = None,
        auth_cert: str | None = None,
        auth_portal_addr: str | None = None,
        security_exempt_list: str | None = None,
        security_groups: list | None = None,
        ike_saml_server: str | None = None,
        stp: str | None = None,
        stp_ha_secondary: str | None = None,
        stp_edge: str | None = None,
        device_identification: str | None = None,
        exclude_signatures: str | None = None,
        device_user_identification: str | None = None,
        lldp_reception: str | None = None,
        lldp_transmission: str | None = None,
        lldp_network_policy: str | None = None,
        estimated_upstream_bandwidth: int | None = None,
        estimated_downstream_bandwidth: int | None = None,
        measured_upstream_bandwidth: int | None = None,
        measured_downstream_bandwidth: int | None = None,
        bandwidth_measure_time: int | None = None,
        monitor_bandwidth: str | None = None,
        vrrp_virtual_mac: str | None = None,
        vrrp: list | None = None,
        phy_setting: list | None = None,
        role: str | None = None,
        snmp_index: int | None = None,
        secondary_IP: str | None = None,
        secondaryip: list | None = None,
        preserve_session_route: str | None = None,
        auto_auth_extension_device: str | None = None,
        ap_discover: str | None = None,
        fortilink_neighbor_detect: str | None = None,
        ip_managed_by_fortiipam: str | None = None,
        managed_subnetwork_size: str | None = None,
        fortilink_split_interface: str | None = None,
        internal: int | None = None,
        fortilink_backup_link: int | None = None,
        switch_controller_access_vlan: str | None = None,
        switch_controller_traffic_policy: str | None = None,
        switch_controller_rspan_mode: str | None = None,
        switch_controller_netflow_collect: str | None = None,
        switch_controller_mgmt_vlan: int | None = None,
        switch_controller_igmp_snooping: str | None = None,
        switch_controller_igmp_snooping_proxy: str | None = None,
        switch_controller_igmp_snooping_fast_leave: str | None = None,
        switch_controller_dhcp_snooping: str | None = None,
        switch_controller_dhcp_snooping_verify_mac: str | None = None,
        switch_controller_dhcp_snooping_option82: str | None = None,
        dhcp_snooping_server_list: list | None = None,
        switch_controller_arp_inspection: str | None = None,
        switch_controller_learning_limit: int | None = None,
        switch_controller_nac: str | None = None,
        switch_controller_dynamic: str | None = None,
        switch_controller_feature: str | None = None,
        switch_controller_iot_scanning: str | None = None,
        switch_controller_offload: str | None = None,
        switch_controller_offload_ip: str | None = None,
        switch_controller_offload_gw: str | None = None,
        swc_vlan: int | None = None,
        swc_first_create: int | None = None,
        color: int | None = None,
        tagging: list | None = None,
        eap_supplicant: str | None = None,
        eap_method: str | None = None,
        eap_identity: str | None = None,
        eap_password: str | None = None,
        eap_ca_cert: str | None = None,
        eap_user_cert: str | None = None,
        default_purdue_level: str | None = None,
        ipv6: list | None = None,
        physical: str | None = None,
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
            name: Name. (optional)
            vrf: Virtual Routing Forwarding ID. (optional)
            cli_conn_status: CLI connection status. (optional)
            fortilink: Enable FortiLink to dedicate this interface to manage
            other Fortinet devices. (optional)
            switch_controller_source_ip: Source IP address used in FortiLink
            over L3 connections. (optional)
            mode: Addressing mode (static, DHCP, PPPoE). (optional)
            client_options: DHCP client options. (optional)
            distance: Distance for routes learned through PPPoE or DHCP, lower
            distance indicates preferred route. (optional)
            priority: Priority of learned routes. (optional)
            dhcp_relay_interface_select_method: Specify how to select outgoing
            interface to reach server. (optional)
            dhcp_relay_interface: Specify outgoing interface to reach server.
            (optional)
            dhcp_relay_vrf_select: VRF ID used for connection to server.
            (optional)
            dhcp_broadcast_flag: Enable/disable setting of the broadcast flag
            in messages sent by the DHCP client (default = enable). (optional)
            dhcp_relay_service: Enable/disable allowing this interface to act
            as a DHCP relay. (optional)
            dhcp_relay_ip: DHCP relay IP address. (optional)
            dhcp_relay_source_ip: IP address used by the DHCP relay as its
            source IP. (optional)
            dhcp_relay_circuit_id: DHCP relay circuit ID. (optional)
            dhcp_relay_link_selection: DHCP relay link selection. (optional)
            dhcp_relay_request_all_server: Enable/disable sending of DHCP
            requests to all servers. (optional)
            dhcp_relay_allow_no_end_option: Enable/disable relaying DHCP
            messages with no end option. (optional)
            dhcp_relay_type: DHCP relay type (regular or IPsec). (optional)
            dhcp_smart_relay: Enable/disable DHCP smart relay. (optional)
            dhcp_relay_agent_option: Enable/disable DHCP relay agent option.
            (optional)
            dhcp_classless_route_addition: Enable/disable addition of classless
            static routes retrieved from DHCP server. (optional)
            management_ip: High Availability in-band management IP address of
            this interface. (optional)
            ip: Interface IPv4 address and subnet mask, syntax: X.X.X.X/24.
            (optional)
            allowaccess: Permitted types of management access to this
            interface. (optional)
            gwdetect: Enable/disable detect gateway alive for first. (optional)
            ping_serv_status: PING server status. (optional)
            detectserver: Gateway's ping server for this IP. (optional)
            detectprotocol: Protocols used to detect the server. (optional)
            ha_priority: HA election priority for the PING server. (optional)
            fail_detect: Enable/disable fail detection features for this
            interface. (optional)
            fail_detect_option: Options for detecting that this interface has
            failed. (optional)
            fail_alert_method: Select link-failed-signal or link-down method to
            alert about a failed link. (optional)
            fail_action_on_extender: Action on FortiExtender when interface
            fail. (optional)
            fail_alert_interfaces: Names of the FortiGate interfaces to which
            the link failure alert is sent. (optional)
            dhcp_client_identifier: DHCP client identifier. (optional)
            dhcp_renew_time: DHCP renew time in seconds (300-604800), 0 means
            use the renew time provided by the server. (optional)
            ipunnumbered: Unnumbered IP used for PPPoE interfaces for which no
            unique local address is provided. (optional)
            username: Username of the PPPoE account, provided by your ISP.
            (optional)
            pppoe_egress_cos: CoS in VLAN tag for outgoing PPPoE/PPP packets.
            (optional)
            pppoe_unnumbered_negotiate: Enable/disable PPPoE unnumbered
            negotiation. (optional)
            password: PPPoE account's password. (optional)
            idle_timeout: PPPoE auto disconnect after idle timeout seconds, 0
            means no timeout. (optional)
            multilink: Enable/disable PPP multilink support. (optional)
            mrru: PPP MRRU (296 - 65535, default = 1500). (optional)
            detected_peer_mtu: MTU of detected peer (0 - 4294967295).
            (optional)
            disc_retry_timeout: Time in seconds to wait before retrying to
            start a PPPoE discovery, 0 means no timeout. (optional)
            padt_retry_timeout: PPPoE Active Discovery Terminate (PADT) used to
            terminate sessions after an idle time. (optional)
            service_name: PPPoE service name. (optional)
            ac_name: PPPoE server name. (optional)
            lcp_echo_interval: Time in seconds between PPPoE Link Control
            Protocol (LCP) echo requests. (optional)
            lcp_max_echo_fails: Maximum missed LCP echo messages before
            disconnect. (optional)
            defaultgw: Enable to get the gateway IP from the DHCP or PPPoE
            server. (optional)
            dns_server_override: Enable/disable use DNS acquired by DHCP or
            PPPoE. (optional)
            dns_server_protocol: DNS transport protocols. (optional)
            auth_type: PPP authentication type to use. (optional)
            pptp_client: Enable/disable PPTP client. (optional)
            pptp_user: PPTP user name. (optional)
            pptp_password: PPTP password. (optional)
            pptp_server_ip: PPTP server IP address. (optional)
            pptp_auth_type: PPTP authentication type. (optional)
            pptp_timeout: Idle timer in minutes (0 for disabled). (optional)
            arpforward: Enable/disable ARP forwarding. (optional)
            ndiscforward: Enable/disable NDISC forwarding. (optional)
            broadcast_forward: Enable/disable broadcast forwarding. (optional)
            bfd: Bidirectional Forwarding Detection (BFD) settings. (optional)
            bfd_desired_min_tx: BFD desired minimal transmit interval.
            (optional)
            bfd_detect_mult: BFD detection multiplier. (optional)
            bfd_required_min_rx: BFD required minimal receive interval.
            (optional)
            l2forward: Enable/disable l2 forwarding. (optional)
            icmp_send_redirect: Enable/disable sending of ICMP redirects.
            (optional)
            icmp_accept_redirect: Enable/disable ICMP accept redirect.
            (optional)
            reachable_time: IPv4 reachable time in milliseconds (30000 -
            3600000, default = 30000). (optional)
            vlanforward: Enable/disable traffic forwarding between VLANs on
            this interface. (optional)
            stpforward: Enable/disable STP forwarding. (optional)
            stpforward_mode: Configure STP forwarding mode. (optional)
            ips_sniffer_mode: Enable/disable the use of this interface as a
            one-armed sniffer. (optional)
            ident_accept: Enable/disable authentication for this interface.
            (optional)
            ipmac: Enable/disable IP/MAC binding. (optional)
            subst: Enable to always send packets from this interface to a
            destination MAC address. (optional)
            macaddr: Change the interface's MAC address. (optional)
            virtual_mac: Change the interface's virtual MAC address. (optional)
            substitute_dst_mac: Destination MAC address that all packets are
            sent to from this interface. (optional)
            speed: Interface speed. The default setting and the options
            available depend on the interface hardware. (optional)
            status: Bring the interface up or shut the interface down.
            (optional)
            netbios_forward: Enable/disable NETBIOS forwarding. (optional)
            wins_ip: WINS server IP. (optional)
            type: Interface type. (optional)
            dedicated_to: Configure interface for single purpose. (optional)
            trust_ip_1: Trusted host for dedicated management traffic
            (0.0.0.0/24 for all hosts). (optional)
            trust_ip_2: Trusted host for dedicated management traffic
            (0.0.0.0/24 for all hosts). (optional)
            trust_ip_3: Trusted host for dedicated management traffic
            (0.0.0.0/24 for all hosts). (optional)
            trust_ip6_1: Trusted IPv6 host for dedicated management traffic
            (::/0 for all hosts). (optional)
            trust_ip6_2: Trusted IPv6 host for dedicated management traffic
            (::/0 for all hosts). (optional)
            trust_ip6_3: Trusted IPv6 host for dedicated management traffic
            (::/0 for all hosts). (optional)
            wccp: Enable/disable WCCP on this interface. Used for encapsulated
            WCCP communication between WCCP clients and servers. (optional)
            netflow_sampler: Enable/disable NetFlow on this interface and set
            the data that NetFlow collects (rx, tx, or both). (optional)
            netflow_sample_rate: NetFlow sample rate. Sample one packet every
            configured number of packets (optional)
            netflow_sampler_id: Netflow sampler ID. (optional)
            sflow_sampler: Enable/disable sFlow on this interface. (optional)
            drop_fragment: Enable/disable drop fragment packets. (optional)
            src_check: Enable/disable source IP check. (optional)
            sample_rate: sFlow sample rate (10 - 99999). (optional)
            polling_interval: sFlow polling interval in seconds (1 - 255).
            (optional)
            sample_direction: Data that NetFlow collects (rx, tx, or both).
            (optional)
            explicit_web_proxy: Enable/disable the explicit web proxy on this
            interface. (optional)
            explicit_ftp_proxy: Enable/disable the explicit FTP proxy on this
            interface. (optional)
            proxy_captive_portal: Enable/disable proxy captive portal on this
            interface. (optional)
            tcp_mss: TCP maximum segment size. 0 means do not change segment
            size. (optional)
            inbandwidth: Bandwidth limit for incoming traffic (0 - 80000000
            kbps), 0 means unlimited. (optional)
            outbandwidth: Bandwidth limit for outgoing traffic (0 - 80000000
            kbps). (optional)
            egress_shaping_profile: Outgoing traffic shaping profile.
            (optional)
            ingress_shaping_profile: Incoming traffic shaping profile.
            (optional)
            spillover_threshold: Egress Spillover threshold (0 - 16776000
            kbps), 0 means unlimited. (optional)
            ingress_spillover_threshold: Ingress Spillover threshold (0 -
            16776000 kbps), 0 means unlimited. (optional)
            weight: Default weight for static routes (if route has no weight
            configured). (optional)
            interface: Interface name. (optional)
            external: Enable/disable identifying the interface as an external
            interface (which usually means it's connected to the Internet).
            (optional)
            mtu_override: Enable to set a custom MTU for this interface.
            (optional)
            mtu: MTU value for this interface. (optional)
            vlan_protocol: Ethernet protocol of VLAN. (optional)
            vlanid: VLAN ID (1 - 4094). (optional)
            trunk: Enable/disable VLAN trunk. (optional)
            forward_domain: Transparent mode forward domain. (optional)
            remote_ip: Remote IP address of tunnel. (optional)
            member: Physical interfaces that belong to the aggregate or
            redundant interface. (optional)
            lacp_mode: LACP mode. (optional)
            lacp_ha_secondary: LACP HA secondary member. (optional)
            system_id_type: Method in which system ID is generated. (optional)
            system_id: Define a system ID for the aggregate interface.
            (optional)
            lacp_speed: How often the interface sends LACP messages. (optional)
            min_links: Minimum number of aggregated ports that must be up.
            (optional)
            min_links_down: Action to take when less than the configured
            minimum number of links are active. (optional)
            algorithm: Frame distribution algorithm. (optional)
            link_up_delay: Number of milliseconds to wait before considering a
            link is up. (optional)
            aggregate_type: Type of aggregation. (optional)
            priority_override: Enable/disable fail back to higher priority port
            once recovered. (optional)
            aggregate: Aggregate interface. (optional)
            redundant_interface: Redundant interface. (optional)
            devindex: Device Index. (optional)
            vindex: Switch control interface VLAN ID. (optional)
            switch: Contained in switch. (optional)
            description: Description. (optional)
            alias: Alias will be displayed with the interface name to make it
            easier to distinguish. (optional)
            l2tp_client: Enable/disable this interface as a Layer 2 Tunnelling
            Protocol (L2TP) client. (optional)
            l2tp_client_settings: L2TP client settings. (optional)
            security_mode: Turn on captive portal authentication for this
            interface. (optional)
            security_mac_auth_bypass: Enable/disable MAC authentication bypass.
            (optional)
            security_ip_auth_bypass: Enable/disable IP authentication bypass.
            (optional)
            security_8021x_mode: 802.1X mode. (optional)
            security_8021x_master: 802.1X master virtual-switch. (optional)
            security_8021x_dynamic_vlan_id: VLAN ID for virtual switch.
            (optional)
            security_8021x_member_mode: 802.1X member mode. (optional)
            security_external_web: URL of external authentication web server.
            (optional)
            security_external_logout: URL of external authentication logout
            server. (optional)
            replacemsg_override_group: Replacement message override group.
            (optional)
            security_redirect_url: URL redirection after
            disclaimer/authentication. (optional)
            auth_cert: HTTPS server certificate. (optional)
            auth_portal_addr: Address of captive portal. (optional)
            security_exempt_list: Name of security-exempt-list. (optional)
            security_groups: User groups that can authenticate with the captive
            portal. (optional)
            ike_saml_server: Configure IKE authentication SAML server.
            (optional)
            stp: Enable/disable STP. (optional)
            stp_ha_secondary: Control STP behavior on HA secondary. (optional)
            stp_edge: Enable/disable as STP edge port. (optional)
            device_identification: Enable/disable passively gathering of device
            identity information about the devices on the network connected to
            this interface. (optional)
            exclude_signatures: Exclude IOT or OT application signatures.
            (optional)
            device_user_identification: Enable/disable passive gathering of
            user identity information about users on this interface. (optional)
            lldp_reception: Enable/disable Link Layer Discovery Protocol (LLDP)
            reception. (optional)
            lldp_transmission: Enable/disable Link Layer Discovery Protocol
            (LLDP) transmission. (optional)
            lldp_network_policy: LLDP-MED network policy profile. (optional)
            estimated_upstream_bandwidth: Estimated maximum upstream bandwidth
            (kbps). Used to estimate link utilization. (optional)
            estimated_downstream_bandwidth: Estimated maximum downstream
            bandwidth (kbps). Used to estimate link utilization. (optional)
            measured_upstream_bandwidth: Measured upstream bandwidth (kbps).
            (optional)
            measured_downstream_bandwidth: Measured downstream bandwidth
            (kbps). (optional)
            bandwidth_measure_time: Bandwidth measure time. (optional)
            monitor_bandwidth: Enable monitoring bandwidth on this interface.
            (optional)
            vrrp_virtual_mac: Enable/disable use of virtual MAC for VRRP.
            (optional)
            vrrp: VRRP configuration. (optional)
            phy_setting: PHY settings (optional)
            role: Interface role. (optional)
            snmp_index: Permanent SNMP Index of the interface. (optional)
            secondary_IP: Enable/disable adding a secondary IP to this
            interface. (optional)
            secondaryip: Second IP address of interface. (optional)
            preserve_session_route: Enable/disable preservation of session
            route when dirty. (optional)
            auto_auth_extension_device: Enable/disable automatic authorization
            of dedicated Fortinet extension device on this interface.
            (optional)
            ap_discover: Enable/disable automatic registration of unknown
            FortiAP devices. (optional)
            fortilink_neighbor_detect: Protocol for FortiGate neighbor
            discovery. (optional)
            ip_managed_by_fortiipam: Enable/disable automatic IP address
            assignment of this interface by FortiIPAM. (optional)
            managed_subnetwork_size: Number of IP addresses to be allocated by
            FortiIPAM and used by this FortiGate unit's DHCP server settings.
            (optional)
            fortilink_split_interface: Enable/disable FortiLink split interface
            to connect member link to different FortiSwitch in stack for uplink
            redundancy. (optional)
            internal: Implicitly created. (optional)
            fortilink_backup_link: FortiLink split interface backup link.
            (optional)
            switch_controller_access_vlan: Block FortiSwitch port-to-port
            traffic. (optional)
            switch_controller_traffic_policy: Switch controller traffic policy
            for the VLAN. (optional)
            switch_controller_rspan_mode: Stop Layer2 MAC learning and
            interception of BPDUs and other packets on this interface.
            (optional)
            switch_controller_netflow_collect: NetFlow collection and
            processing. (optional)
            switch_controller_mgmt_vlan: VLAN to use for FortiLink management
            purposes. (optional)
            switch_controller_igmp_snooping: Switch controller IGMP snooping.
            (optional)
            switch_controller_igmp_snooping_proxy: Switch controller IGMP
            snooping proxy. (optional)
            switch_controller_igmp_snooping_fast_leave: Switch controller IGMP
            snooping fast-leave. (optional)
            switch_controller_dhcp_snooping: Switch controller DHCP snooping.
            (optional)
            switch_controller_dhcp_snooping_verify_mac: Switch controller DHCP
            snooping verify MAC. (optional)
            switch_controller_dhcp_snooping_option82: Switch controller DHCP
            snooping option82. (optional)
            dhcp_snooping_server_list: Configure DHCP server access list.
            (optional)
            switch_controller_arp_inspection: Enable/disable/Monitor
            FortiSwitch ARP inspection. (optional)
            switch_controller_learning_limit: Limit the number of dynamic MAC
            addresses on this VLAN (1 - 128, 0 = no limit, default). (optional)
            switch_controller_nac: Integrated FortiLink settings for managed
            FortiSwitch. (optional)
            switch_controller_dynamic: Integrated FortiLink settings for
            managed FortiSwitch. (optional)
            switch_controller_feature: Interface's purpose when assigning
            traffic (read only). (optional)
            switch_controller_iot_scanning: Enable/disable managed FortiSwitch
            IoT scanning. (optional)
            switch_controller_offload: Enable/disable managed FortiSwitch
            routing offload. (optional)
            switch_controller_offload_ip: IP for routing offload on
            FortiSwitch. (optional)
            switch_controller_offload_gw: Enable/disable managed FortiSwitch
            routing offload gateway. (optional)
            swc_vlan: Creation status for switch-controller VLANs. (optional)
            swc_first_create: Initial create for switch-controller VLANs.
            (optional)
            color: Color of icon on the GUI. (optional)
            tagging: Config object tagging. (optional)
            eap_supplicant: Enable/disable EAP-Supplicant. (optional)
            eap_method: EAP method. (optional)
            eap_identity: EAP identity. (optional)
            eap_password: EAP password. (optional)
            eap_ca_cert: EAP CA certificate name. (optional)
            eap_user_cert: EAP user certificate name. (optional)
            default_purdue_level: default purdue level of device detected on
            this interface. (optional)
            ipv6: IPv6 of interface. (optional)
            physical: Print physical interface information. (optional)
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
        endpoint = f"/system/interface/{name}"
        if before is not None:
            data_payload["before"] = before
        if after is not None:
            data_payload["after"] = after
        if name is not None:
            data_payload["name"] = name
        if vrf is not None:
            data_payload["vr"] = vrf
        if cli_conn_status is not None:
            data_payload["cli-conn-status"] = cli_conn_status
        if fortilink is not None:
            data_payload["fortilink"] = fortilink
        if switch_controller_source_ip is not None:
            data_payload["switch-controller-source-ip"] = (
                switch_controller_source_ip
            )
        if mode is not None:
            data_payload["mode"] = mode
        if client_options is not None:
            data_payload["client-options"] = client_options
        if distance is not None:
            data_payload["distance"] = distance
        if priority is not None:
            data_payload["priority"] = priority
        if dhcp_relay_interface_select_method is not None:
            data_payload["dhcp-relay-interface-select-method"] = (
                dhcp_relay_interface_select_method
            )
        if dhcp_relay_interface is not None:
            data_payload["dhcp-relay-interface"] = dhcp_relay_interface
        if dhcp_relay_vrf_select is not None:
            data_payload["dhcp-relay-vrf-select"] = dhcp_relay_vrf_select
        if dhcp_broadcast_flag is not None:
            data_payload["dhcp-broadcast-flag"] = dhcp_broadcast_flag
        if dhcp_relay_service is not None:
            data_payload["dhcp-relay-service"] = dhcp_relay_service
        if dhcp_relay_ip is not None:
            data_payload["dhcp-relay-ip"] = dhcp_relay_ip
        if dhcp_relay_source_ip is not None:
            data_payload["dhcp-relay-source-ip"] = dhcp_relay_source_ip
        if dhcp_relay_circuit_id is not None:
            data_payload["dhcp-relay-circuit-id"] = dhcp_relay_circuit_id
        if dhcp_relay_link_selection is not None:
            data_payload["dhcp-relay-link-selection"] = (
                dhcp_relay_link_selection
            )
        if dhcp_relay_request_all_server is not None:
            data_payload["dhcp-relay-request-all-server"] = (
                dhcp_relay_request_all_server
            )
        if dhcp_relay_allow_no_end_option is not None:
            data_payload["dhcp-relay-allow-no-end-option"] = (
                dhcp_relay_allow_no_end_option
            )
        if dhcp_relay_type is not None:
            data_payload["dhcp-relay-type"] = dhcp_relay_type
        if dhcp_smart_relay is not None:
            data_payload["dhcp-smart-relay"] = dhcp_smart_relay
        if dhcp_relay_agent_option is not None:
            data_payload["dhcp-relay-agent-option"] = dhcp_relay_agent_option
        if dhcp_classless_route_addition is not None:
            data_payload["dhcp-classless-route-addition"] = (
                dhcp_classless_route_addition
            )
        if management_ip is not None:
            data_payload["management-ip"] = management_ip
        if ip is not None:
            data_payload["ip"] = ip
        if allowaccess is not None:
            data_payload["allowaccess"] = allowaccess
        if gwdetect is not None:
            data_payload["gwdetect"] = gwdetect
        if ping_serv_status is not None:
            data_payload["ping-serv-status"] = ping_serv_status
        if detectserver is not None:
            data_payload["detectserver"] = detectserver
        if detectprotocol is not None:
            data_payload["detectprotocol"] = detectprotocol
        if ha_priority is not None:
            data_payload["ha-priority"] = ha_priority
        if fail_detect is not None:
            data_payload["fail-detect"] = fail_detect
        if fail_detect_option is not None:
            data_payload["fail-detect-option"] = fail_detect_option
        if fail_alert_method is not None:
            data_payload["fail-alert-method"] = fail_alert_method
        if fail_action_on_extender is not None:
            data_payload["fail-action-on-extender"] = fail_action_on_extender
        if fail_alert_interfaces is not None:
            data_payload["fail-alert-interfaces"] = fail_alert_interfaces
        if dhcp_client_identifier is not None:
            data_payload["dhcp-client-identifier"] = dhcp_client_identifier
        if dhcp_renew_time is not None:
            data_payload["dhcp-renew-time"] = dhcp_renew_time
        if ipunnumbered is not None:
            data_payload["ipunnumbered"] = ipunnumbered
        if username is not None:
            data_payload["username"] = username
        if pppoe_egress_cos is not None:
            data_payload["pppoe-egress-cos"] = pppoe_egress_cos
        if pppoe_unnumbered_negotiate is not None:
            data_payload["pppoe-unnumbered-negotiate"] = (
                pppoe_unnumbered_negotiate
            )
        if password is not None:
            data_payload["password"] = password
        if idle_timeout is not None:
            data_payload["idle-timeout"] = idle_timeout
        if multilink is not None:
            data_payload["multilink"] = multilink
        if mrru is not None:
            data_payload["mrru"] = mrru
        if detected_peer_mtu is not None:
            data_payload["detected-peer-mtu"] = detected_peer_mtu
        if disc_retry_timeout is not None:
            data_payload["disc-retry-timeout"] = disc_retry_timeout
        if padt_retry_timeout is not None:
            data_payload["padt-retry-timeout"] = padt_retry_timeout
        if service_name is not None:
            data_payload["service-name"] = service_name
        if ac_name is not None:
            data_payload["ac-name"] = ac_name
        if lcp_echo_interval is not None:
            data_payload["lcp-echo-interval"] = lcp_echo_interval
        if lcp_max_echo_fails is not None:
            data_payload["lcp-max-echo-fails"] = lcp_max_echo_fails
        if defaultgw is not None:
            data_payload["defaultgw"] = defaultgw
        if dns_server_override is not None:
            data_payload["dns-server-override"] = dns_server_override
        if dns_server_protocol is not None:
            data_payload["dns-server-protocol"] = dns_server_protocol
        if auth_type is not None:
            data_payload["auth-type"] = auth_type
        if pptp_client is not None:
            data_payload["pptp-client"] = pptp_client
        if pptp_user is not None:
            data_payload["pptp-user"] = pptp_user
        if pptp_password is not None:
            data_payload["pptp-password"] = pptp_password
        if pptp_server_ip is not None:
            data_payload["pptp-server-ip"] = pptp_server_ip
        if pptp_auth_type is not None:
            data_payload["pptp-auth-type"] = pptp_auth_type
        if pptp_timeout is not None:
            data_payload["pptp-timeout"] = pptp_timeout
        if arpforward is not None:
            data_payload["arpforward"] = arpforward
        if ndiscforward is not None:
            data_payload["ndiscforward"] = ndiscforward
        if broadcast_forward is not None:
            data_payload["broadcast-forward"] = broadcast_forward
        if bfd is not None:
            data_payload["bfd"] = bfd
        if bfd_desired_min_tx is not None:
            data_payload["bfd-desired-min-tx"] = bfd_desired_min_tx
        if bfd_detect_mult is not None:
            data_payload["bfd-detect-mult"] = bfd_detect_mult
        if bfd_required_min_rx is not None:
            data_payload["bfd-required-min-rx"] = bfd_required_min_rx
        if l2forward is not None:
            data_payload["l2forward"] = l2forward
        if icmp_send_redirect is not None:
            data_payload["icmp-send-redirect"] = icmp_send_redirect
        if icmp_accept_redirect is not None:
            data_payload["icmp-accept-redirect"] = icmp_accept_redirect
        if reachable_time is not None:
            data_payload["reachable-time"] = reachable_time
        if vlanforward is not None:
            data_payload["vlanforward"] = vlanforward
        if stpforward is not None:
            data_payload["stpforward"] = stpforward
        if stpforward_mode is not None:
            data_payload["stpforward-mode"] = stpforward_mode
        if ips_sniffer_mode is not None:
            data_payload["ips-sniffer-mode"] = ips_sniffer_mode
        if ident_accept is not None:
            data_payload["ident-accept"] = ident_accept
        if ipmac is not None:
            data_payload["ipmac"] = ipmac
        if subst is not None:
            data_payload["subst"] = subst
        if macaddr is not None:
            data_payload["macaddr"] = macaddr
        if virtual_mac is not None:
            data_payload["virtual-mac"] = virtual_mac
        if substitute_dst_mac is not None:
            data_payload["substitute-dst-mac"] = substitute_dst_mac
        if speed is not None:
            data_payload["speed"] = speed
        if status is not None:
            data_payload["status"] = status
        if netbios_forward is not None:
            data_payload["netbios-forward"] = netbios_forward
        if wins_ip is not None:
            data_payload["wins-ip"] = wins_ip
        if type is not None:
            data_payload["type"] = type
        if dedicated_to is not None:
            data_payload["dedicated-to"] = dedicated_to
        if trust_ip_1 is not None:
            data_payload["trust-ip-1"] = trust_ip_1
        if trust_ip_2 is not None:
            data_payload["trust-ip-2"] = trust_ip_2
        if trust_ip_3 is not None:
            data_payload["trust-ip-3"] = trust_ip_3
        if trust_ip6_1 is not None:
            data_payload["trust-ip6-1"] = trust_ip6_1
        if trust_ip6_2 is not None:
            data_payload["trust-ip6-2"] = trust_ip6_2
        if trust_ip6_3 is not None:
            data_payload["trust-ip6-3"] = trust_ip6_3
        if wccp is not None:
            data_payload["wccp"] = wccp
        if netflow_sampler is not None:
            data_payload["netflow-sampler"] = netflow_sampler
        if netflow_sample_rate is not None:
            data_payload["netflow-sample-rate"] = netflow_sample_rate
        if netflow_sampler_id is not None:
            data_payload["netflow-sampler-id"] = netflow_sampler_id
        if sflow_sampler is not None:
            data_payload["sflow-sampler"] = sflow_sampler
        if drop_fragment is not None:
            data_payload["drop-fragment"] = drop_fragment
        if src_check is not None:
            data_payload["src-check"] = src_check
        if sample_rate is not None:
            data_payload["sample-rate"] = sample_rate
        if polling_interval is not None:
            data_payload["polling-interval"] = polling_interval
        if sample_direction is not None:
            data_payload["sample-direction"] = sample_direction
        if explicit_web_proxy is not None:
            data_payload["explicit-web-proxy"] = explicit_web_proxy
        if explicit_ftp_proxy is not None:
            data_payload["explicit-ftp-proxy"] = explicit_ftp_proxy
        if proxy_captive_portal is not None:
            data_payload["proxy-captive-portal"] = proxy_captive_portal
        if tcp_mss is not None:
            data_payload["tcp-mss"] = tcp_mss
        if inbandwidth is not None:
            data_payload["inbandwidth"] = inbandwidth
        if outbandwidth is not None:
            data_payload["outbandwidth"] = outbandwidth
        if egress_shaping_profile is not None:
            data_payload["egress-shaping-profile"] = egress_shaping_profile
        if ingress_shaping_profile is not None:
            data_payload["ingress-shaping-profile"] = ingress_shaping_profile
        if spillover_threshold is not None:
            data_payload["spillover-threshold"] = spillover_threshold
        if ingress_spillover_threshold is not None:
            data_payload["ingress-spillover-threshold"] = (
                ingress_spillover_threshold
            )
        if weight is not None:
            data_payload["weight"] = weight
        if interface is not None:
            data_payload["interface"] = interface
        if external is not None:
            data_payload["external"] = external
        if mtu_override is not None:
            data_payload["mtu-override"] = mtu_override
        if mtu is not None:
            data_payload["mtu"] = mtu
        if vlan_protocol is not None:
            data_payload["vlan-protocol"] = vlan_protocol
        if vlanid is not None:
            data_payload["vlanid"] = vlanid
        if trunk is not None:
            data_payload["trunk"] = trunk
        if forward_domain is not None:
            data_payload["forward-domain"] = forward_domain
        if remote_ip is not None:
            data_payload["remote-ip"] = remote_ip
        if member is not None:
            data_payload["member"] = member
        if lacp_mode is not None:
            data_payload["lacp-mode"] = lacp_mode
        if lacp_ha_secondary is not None:
            data_payload["lacp-ha-secondary"] = lacp_ha_secondary
        if system_id_type is not None:
            data_payload["system-id-type"] = system_id_type
        if system_id is not None:
            data_payload["system-id"] = system_id
        if lacp_speed is not None:
            data_payload["lacp-speed"] = lacp_speed
        if min_links is not None:
            data_payload["min-links"] = min_links
        if min_links_down is not None:
            data_payload["min-links-down"] = min_links_down
        if algorithm is not None:
            data_payload["algorithm"] = algorithm
        if link_up_delay is not None:
            data_payload["link-up-delay"] = link_up_delay
        if aggregate_type is not None:
            data_payload["aggregate-type"] = aggregate_type
        if priority_override is not None:
            data_payload["priority-override"] = priority_override
        if aggregate is not None:
            data_payload["aggregate"] = aggregate
        if redundant_interface is not None:
            data_payload["redundant-interface"] = redundant_interface
        if devindex is not None:
            data_payload["devindex"] = devindex
        if vindex is not None:
            data_payload["vindex"] = vindex
        if switch is not None:
            data_payload["switch"] = switch
        if description is not None:
            data_payload["description"] = description
        if alias is not None:
            data_payload["alias"] = alias
        if l2tp_client is not None:
            data_payload["l2tp-client"] = l2tp_client
        if l2tp_client_settings is not None:
            data_payload["l2tp-client-settings"] = l2tp_client_settings
        if security_mode is not None:
            data_payload["security-mode"] = security_mode
        if security_mac_auth_bypass is not None:
            data_payload["security-mac-auth-bypass"] = security_mac_auth_bypass
        if security_ip_auth_bypass is not None:
            data_payload["security-ip-auth-bypass"] = security_ip_auth_bypass
        if security_8021x_mode is not None:
            data_payload["security-8021x-mode"] = security_8021x_mode
        if security_8021x_master is not None:
            data_payload["security-8021x-master"] = security_8021x_master
        if security_8021x_dynamic_vlan_id is not None:
            data_payload["security-8021x-dynamic-vlan-id"] = (
                security_8021x_dynamic_vlan_id
            )
        if security_8021x_member_mode is not None:
            data_payload["security-8021x-member-mode"] = (
                security_8021x_member_mode
            )
        if security_external_web is not None:
            data_payload["security-external-web"] = security_external_web
        if security_external_logout is not None:
            data_payload["security-external-logout"] = security_external_logout
        if replacemsg_override_group is not None:
            data_payload["replacemsg-override-group"] = (
                replacemsg_override_group
            )
        if security_redirect_url is not None:
            data_payload["security-redirect-url"] = security_redirect_url
        if auth_cert is not None:
            data_payload["auth-cert"] = auth_cert
        if auth_portal_addr is not None:
            data_payload["auth-portal-addr"] = auth_portal_addr
        if security_exempt_list is not None:
            data_payload["security-exempt-list"] = security_exempt_list
        if security_groups is not None:
            data_payload["security-groups"] = security_groups
        if ike_saml_server is not None:
            data_payload["ike-saml-server"] = ike_saml_server
        if stp is not None:
            data_payload["stp"] = stp
        if stp_ha_secondary is not None:
            data_payload["stp-ha-secondary"] = stp_ha_secondary
        if stp_edge is not None:
            data_payload["stp-edge"] = stp_edge
        if device_identification is not None:
            data_payload["device-identification"] = device_identification
        if exclude_signatures is not None:
            data_payload["exclude-signatures"] = exclude_signatures
        if device_user_identification is not None:
            data_payload["device-user-identification"] = (
                device_user_identification
            )
        if lldp_reception is not None:
            data_payload["lldp-reception"] = lldp_reception
        if lldp_transmission is not None:
            data_payload["lldp-transmission"] = lldp_transmission
        if lldp_network_policy is not None:
            data_payload["lldp-network-policy"] = lldp_network_policy
        if estimated_upstream_bandwidth is not None:
            data_payload["estimated-upstream-bandwidth"] = (
                estimated_upstream_bandwidth
            )
        if estimated_downstream_bandwidth is not None:
            data_payload["estimated-downstream-bandwidth"] = (
                estimated_downstream_bandwidth
            )
        if measured_upstream_bandwidth is not None:
            data_payload["measured-upstream-bandwidth"] = (
                measured_upstream_bandwidth
            )
        if measured_downstream_bandwidth is not None:
            data_payload["measured-downstream-bandwidth"] = (
                measured_downstream_bandwidth
            )
        if bandwidth_measure_time is not None:
            data_payload["bandwidth-measure-time"] = bandwidth_measure_time
        if monitor_bandwidth is not None:
            data_payload["monitor-bandwidth"] = monitor_bandwidth
        if vrrp_virtual_mac is not None:
            data_payload["vrrp-virtual-mac"] = vrrp_virtual_mac
        if vrrp is not None:
            data_payload["vrrp"] = vrrp
        if phy_setting is not None:
            data_payload["phy-setting"] = phy_setting
        if role is not None:
            data_payload["role"] = role
        if snmp_index is not None:
            data_payload["snmp-index"] = snmp_index
        if secondary_IP is not None:
            data_payload["secondary-IP"] = secondary_IP
        if secondaryip is not None:
            data_payload["secondaryip"] = secondaryip
        if preserve_session_route is not None:
            data_payload["preserve-session-route"] = preserve_session_route
        if auto_auth_extension_device is not None:
            data_payload["auto-auth-extension-device"] = (
                auto_auth_extension_device
            )
        if ap_discover is not None:
            data_payload["ap-discover"] = ap_discover
        if fortilink_neighbor_detect is not None:
            data_payload["fortilink-neighbor-detect"] = (
                fortilink_neighbor_detect
            )
        if ip_managed_by_fortiipam is not None:
            data_payload["ip-managed-by-fortiipam"] = ip_managed_by_fortiipam
        if managed_subnetwork_size is not None:
            data_payload["managed-subnetwork-size"] = managed_subnetwork_size
        if fortilink_split_interface is not None:
            data_payload["fortilink-split-interface"] = (
                fortilink_split_interface
            )
        if internal is not None:
            data_payload["internal"] = internal
        if fortilink_backup_link is not None:
            data_payload["fortilink-backup-link"] = fortilink_backup_link
        if switch_controller_access_vlan is not None:
            data_payload["switch-controller-access-vlan"] = (
                switch_controller_access_vlan
            )
        if switch_controller_traffic_policy is not None:
            data_payload["switch-controller-traffic-policy"] = (
                switch_controller_traffic_policy
            )
        if switch_controller_rspan_mode is not None:
            data_payload["switch-controller-rspan-mode"] = (
                switch_controller_rspan_mode
            )
        if switch_controller_netflow_collect is not None:
            data_payload["switch-controller-netflow-collect"] = (
                switch_controller_netflow_collect
            )
        if switch_controller_mgmt_vlan is not None:
            data_payload["switch-controller-mgmt-vlan"] = (
                switch_controller_mgmt_vlan
            )
        if switch_controller_igmp_snooping is not None:
            data_payload["switch-controller-igmp-snooping"] = (
                switch_controller_igmp_snooping
            )
        if switch_controller_igmp_snooping_proxy is not None:
            data_payload["switch-controller-igmp-snooping-proxy"] = (
                switch_controller_igmp_snooping_proxy
            )
        if switch_controller_igmp_snooping_fast_leave is not None:
            data_payload["switch-controller-igmp-snooping-fast-leave"] = (
                switch_controller_igmp_snooping_fast_leave
            )
        if switch_controller_dhcp_snooping is not None:
            data_payload["switch-controller-dhcp-snooping"] = (
                switch_controller_dhcp_snooping
            )
        if switch_controller_dhcp_snooping_verify_mac is not None:
            data_payload["switch-controller-dhcp-snooping-verify-mac"] = (
                switch_controller_dhcp_snooping_verify_mac
            )
        if switch_controller_dhcp_snooping_option82 is not None:
            data_payload["switch-controller-dhcp-snooping-option82"] = (
                switch_controller_dhcp_snooping_option82
            )
        if dhcp_snooping_server_list is not None:
            data_payload["dhcp-snooping-server-list"] = (
                dhcp_snooping_server_list
            )
        if switch_controller_arp_inspection is not None:
            data_payload["switch-controller-arp-inspection"] = (
                switch_controller_arp_inspection
            )
        if switch_controller_learning_limit is not None:
            data_payload["switch-controller-learning-limit"] = (
                switch_controller_learning_limit
            )
        if switch_controller_nac is not None:
            data_payload["switch-controller-nac"] = switch_controller_nac
        if switch_controller_dynamic is not None:
            data_payload["switch-controller-dynamic"] = (
                switch_controller_dynamic
            )
        if switch_controller_feature is not None:
            data_payload["switch-controller-feature"] = (
                switch_controller_feature
            )
        if switch_controller_iot_scanning is not None:
            data_payload["switch-controller-iot-scanning"] = (
                switch_controller_iot_scanning
            )
        if switch_controller_offload is not None:
            data_payload["switch-controller-offload"] = (
                switch_controller_offload
            )
        if switch_controller_offload_ip is not None:
            data_payload["switch-controller-offload-ip"] = (
                switch_controller_offload_ip
            )
        if switch_controller_offload_gw is not None:
            data_payload["switch-controller-offload-gw"] = (
                switch_controller_offload_gw
            )
        if swc_vlan is not None:
            data_payload["swc-vlan"] = swc_vlan
        if swc_first_create is not None:
            data_payload["swc-first-create"] = swc_first_create
        if color is not None:
            data_payload["color"] = color
        if tagging is not None:
            data_payload["tagging"] = tagging
        if eap_supplicant is not None:
            data_payload["eap-supplicant"] = eap_supplicant
        if eap_method is not None:
            data_payload["eap-method"] = eap_method
        if eap_identity is not None:
            data_payload["eap-identity"] = eap_identity
        if eap_password is not None:
            data_payload["eap-password"] = eap_password
        if eap_ca_cert is not None:
            data_payload["eap-ca-cert"] = eap_ca_cert
        if eap_user_cert is not None:
            data_payload["eap-user-cert"] = eap_user_cert
        if default_purdue_level is not None:
            data_payload["default-purdue-level"] = default_purdue_level
        if ipv6 is not None:
            data_payload["ipv6"] = ipv6
        if physical is not None:
            data_payload["physical"] = physical
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
        endpoint = f"/system/interface/{name}"
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
        vrf: int | None = None,
        cli_conn_status: int | None = None,
        fortilink: str | None = None,
        switch_controller_source_ip: str | None = None,
        mode: str | None = None,
        client_options: list | None = None,
        distance: int | None = None,
        priority: int | None = None,
        dhcp_relay_interface_select_method: str | None = None,
        dhcp_relay_interface: str | None = None,
        dhcp_relay_vrf_select: int | None = None,
        dhcp_broadcast_flag: str | None = None,
        dhcp_relay_service: str | None = None,
        dhcp_relay_ip: str | None = None,
        dhcp_relay_source_ip: str | None = None,
        dhcp_relay_circuit_id: str | None = None,
        dhcp_relay_link_selection: str | None = None,
        dhcp_relay_request_all_server: str | None = None,
        dhcp_relay_allow_no_end_option: str | None = None,
        dhcp_relay_type: str | None = None,
        dhcp_smart_relay: str | None = None,
        dhcp_relay_agent_option: str | None = None,
        dhcp_classless_route_addition: str | None = None,
        management_ip: str | None = None,
        ip: str | None = None,
        allowaccess: str | None = None,
        gwdetect: str | None = None,
        ping_serv_status: int | None = None,
        detectserver: str | None = None,
        detectprotocol: str | None = None,
        ha_priority: int | None = None,
        fail_detect: str | None = None,
        fail_detect_option: str | None = None,
        fail_alert_method: str | None = None,
        fail_action_on_extender: str | None = None,
        fail_alert_interfaces: list | None = None,
        dhcp_client_identifier: str | None = None,
        dhcp_renew_time: int | None = None,
        ipunnumbered: str | None = None,
        username: str | None = None,
        pppoe_egress_cos: str | None = None,
        pppoe_unnumbered_negotiate: str | None = None,
        password: str | None = None,
        idle_timeout: int | None = None,
        multilink: str | None = None,
        mrru: int | None = None,
        detected_peer_mtu: int | None = None,
        disc_retry_timeout: int | None = None,
        padt_retry_timeout: int | None = None,
        service_name: str | None = None,
        ac_name: str | None = None,
        lcp_echo_interval: int | None = None,
        lcp_max_echo_fails: int | None = None,
        defaultgw: str | None = None,
        dns_server_override: str | None = None,
        dns_server_protocol: str | None = None,
        auth_type: str | None = None,
        pptp_client: str | None = None,
        pptp_user: str | None = None,
        pptp_password: str | None = None,
        pptp_server_ip: str | None = None,
        pptp_auth_type: str | None = None,
        pptp_timeout: int | None = None,
        arpforward: str | None = None,
        ndiscforward: str | None = None,
        broadcast_forward: str | None = None,
        bfd: str | None = None,
        bfd_desired_min_tx: int | None = None,
        bfd_detect_mult: int | None = None,
        bfd_required_min_rx: int | None = None,
        l2forward: str | None = None,
        icmp_send_redirect: str | None = None,
        icmp_accept_redirect: str | None = None,
        reachable_time: int | None = None,
        vlanforward: str | None = None,
        stpforward: str | None = None,
        stpforward_mode: str | None = None,
        ips_sniffer_mode: str | None = None,
        ident_accept: str | None = None,
        ipmac: str | None = None,
        subst: str | None = None,
        macaddr: str | None = None,
        virtual_mac: str | None = None,
        substitute_dst_mac: str | None = None,
        speed: str | None = None,
        status: str | None = None,
        netbios_forward: str | None = None,
        wins_ip: str | None = None,
        type: str | None = None,
        dedicated_to: str | None = None,
        trust_ip_1: str | None = None,
        trust_ip_2: str | None = None,
        trust_ip_3: str | None = None,
        trust_ip6_1: str | None = None,
        trust_ip6_2: str | None = None,
        trust_ip6_3: str | None = None,
        wccp: str | None = None,
        netflow_sampler: str | None = None,
        netflow_sample_rate: int | None = None,
        netflow_sampler_id: int | None = None,
        sflow_sampler: str | None = None,
        drop_fragment: str | None = None,
        src_check: str | None = None,
        sample_rate: int | None = None,
        polling_interval: int | None = None,
        sample_direction: str | None = None,
        explicit_web_proxy: str | None = None,
        explicit_ftp_proxy: str | None = None,
        proxy_captive_portal: str | None = None,
        tcp_mss: int | None = None,
        inbandwidth: int | None = None,
        outbandwidth: int | None = None,
        egress_shaping_profile: str | None = None,
        ingress_shaping_profile: str | None = None,
        spillover_threshold: int | None = None,
        ingress_spillover_threshold: int | None = None,
        weight: int | None = None,
        interface: str | None = None,
        external: str | None = None,
        mtu_override: str | None = None,
        mtu: int | None = None,
        vlan_protocol: str | None = None,
        vlanid: int | None = None,
        trunk: str | None = None,
        forward_domain: int | None = None,
        remote_ip: str | None = None,
        member: list | None = None,
        lacp_mode: str | None = None,
        lacp_ha_secondary: str | None = None,
        system_id_type: str | None = None,
        system_id: str | None = None,
        lacp_speed: str | None = None,
        min_links: int | None = None,
        min_links_down: str | None = None,
        algorithm: str | None = None,
        link_up_delay: int | None = None,
        aggregate_type: str | None = None,
        priority_override: str | None = None,
        aggregate: str | None = None,
        redundant_interface: str | None = None,
        devindex: int | None = None,
        vindex: int | None = None,
        switch: str | None = None,
        description: str | None = None,
        alias: str | None = None,
        l2tp_client: str | None = None,
        l2tp_client_settings: list | None = None,
        security_mode: str | None = None,
        security_mac_auth_bypass: str | None = None,
        security_ip_auth_bypass: str | None = None,
        security_8021x_mode: str | None = None,
        security_8021x_master: str | None = None,
        security_8021x_dynamic_vlan_id: int | None = None,
        security_8021x_member_mode: str | None = None,
        security_external_web: str | None = None,
        security_external_logout: str | None = None,
        replacemsg_override_group: str | None = None,
        security_redirect_url: str | None = None,
        auth_cert: str | None = None,
        auth_portal_addr: str | None = None,
        security_exempt_list: str | None = None,
        security_groups: list | None = None,
        ike_saml_server: str | None = None,
        stp: str | None = None,
        stp_ha_secondary: str | None = None,
        stp_edge: str | None = None,
        device_identification: str | None = None,
        exclude_signatures: str | None = None,
        device_user_identification: str | None = None,
        lldp_reception: str | None = None,
        lldp_transmission: str | None = None,
        lldp_network_policy: str | None = None,
        estimated_upstream_bandwidth: int | None = None,
        estimated_downstream_bandwidth: int | None = None,
        measured_upstream_bandwidth: int | None = None,
        measured_downstream_bandwidth: int | None = None,
        bandwidth_measure_time: int | None = None,
        monitor_bandwidth: str | None = None,
        vrrp_virtual_mac: str | None = None,
        vrrp: list | None = None,
        phy_setting: list | None = None,
        role: str | None = None,
        snmp_index: int | None = None,
        secondary_IP: str | None = None,
        secondaryip: list | None = None,
        preserve_session_route: str | None = None,
        auto_auth_extension_device: str | None = None,
        ap_discover: str | None = None,
        fortilink_neighbor_detect: str | None = None,
        ip_managed_by_fortiipam: str | None = None,
        managed_subnetwork_size: str | None = None,
        fortilink_split_interface: str | None = None,
        internal: int | None = None,
        fortilink_backup_link: int | None = None,
        switch_controller_access_vlan: str | None = None,
        switch_controller_traffic_policy: str | None = None,
        switch_controller_rspan_mode: str | None = None,
        switch_controller_netflow_collect: str | None = None,
        switch_controller_mgmt_vlan: int | None = None,
        switch_controller_igmp_snooping: str | None = None,
        switch_controller_igmp_snooping_proxy: str | None = None,
        switch_controller_igmp_snooping_fast_leave: str | None = None,
        switch_controller_dhcp_snooping: str | None = None,
        switch_controller_dhcp_snooping_verify_mac: str | None = None,
        switch_controller_dhcp_snooping_option82: str | None = None,
        dhcp_snooping_server_list: list | None = None,
        switch_controller_arp_inspection: str | None = None,
        switch_controller_learning_limit: int | None = None,
        switch_controller_nac: str | None = None,
        switch_controller_dynamic: str | None = None,
        switch_controller_feature: str | None = None,
        switch_controller_iot_scanning: str | None = None,
        switch_controller_offload: str | None = None,
        switch_controller_offload_ip: str | None = None,
        switch_controller_offload_gw: str | None = None,
        swc_vlan: int | None = None,
        swc_first_create: int | None = None,
        color: int | None = None,
        tagging: list | None = None,
        eap_supplicant: str | None = None,
        eap_method: str | None = None,
        eap_identity: str | None = None,
        eap_password: str | None = None,
        eap_ca_cert: str | None = None,
        eap_user_cert: str | None = None,
        default_purdue_level: str | None = None,
        ipv6: list | None = None,
        physical: str | None = None,
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
            name: Name. (optional)
            vrf: Virtual Routing Forwarding ID. (optional)
            cli_conn_status: CLI connection status. (optional)
            fortilink: Enable FortiLink to dedicate this interface to manage
            other Fortinet devices. (optional)
            switch_controller_source_ip: Source IP address used in FortiLink
            over L3 connections. (optional)
            mode: Addressing mode (static, DHCP, PPPoE). (optional)
            client_options: DHCP client options. (optional)
            distance: Distance for routes learned through PPPoE or DHCP, lower
            distance indicates preferred route. (optional)
            priority: Priority of learned routes. (optional)
            dhcp_relay_interface_select_method: Specify how to select outgoing
            interface to reach server. (optional)
            dhcp_relay_interface: Specify outgoing interface to reach server.
            (optional)
            dhcp_relay_vrf_select: VRF ID used for connection to server.
            (optional)
            dhcp_broadcast_flag: Enable/disable setting of the broadcast flag
            in messages sent by the DHCP client (default = enable). (optional)
            dhcp_relay_service: Enable/disable allowing this interface to act
            as a DHCP relay. (optional)
            dhcp_relay_ip: DHCP relay IP address. (optional)
            dhcp_relay_source_ip: IP address used by the DHCP relay as its
            source IP. (optional)
            dhcp_relay_circuit_id: DHCP relay circuit ID. (optional)
            dhcp_relay_link_selection: DHCP relay link selection. (optional)
            dhcp_relay_request_all_server: Enable/disable sending of DHCP
            requests to all servers. (optional)
            dhcp_relay_allow_no_end_option: Enable/disable relaying DHCP
            messages with no end option. (optional)
            dhcp_relay_type: DHCP relay type (regular or IPsec). (optional)
            dhcp_smart_relay: Enable/disable DHCP smart relay. (optional)
            dhcp_relay_agent_option: Enable/disable DHCP relay agent option.
            (optional)
            dhcp_classless_route_addition: Enable/disable addition of classless
            static routes retrieved from DHCP server. (optional)
            management_ip: High Availability in-band management IP address of
            this interface. (optional)
            ip: Interface IPv4 address and subnet mask, syntax: X.X.X.X/24.
            (optional)
            allowaccess: Permitted types of management access to this
            interface. (optional)
            gwdetect: Enable/disable detect gateway alive for first. (optional)
            ping_serv_status: PING server status. (optional)
            detectserver: Gateway's ping server for this IP. (optional)
            detectprotocol: Protocols used to detect the server. (optional)
            ha_priority: HA election priority for the PING server. (optional)
            fail_detect: Enable/disable fail detection features for this
            interface. (optional)
            fail_detect_option: Options for detecting that this interface has
            failed. (optional)
            fail_alert_method: Select link-failed-signal or link-down method to
            alert about a failed link. (optional)
            fail_action_on_extender: Action on FortiExtender when interface
            fail. (optional)
            fail_alert_interfaces: Names of the FortiGate interfaces to which
            the link failure alert is sent. (optional)
            dhcp_client_identifier: DHCP client identifier. (optional)
            dhcp_renew_time: DHCP renew time in seconds (300-604800), 0 means
            use the renew time provided by the server. (optional)
            ipunnumbered: Unnumbered IP used for PPPoE interfaces for which no
            unique local address is provided. (optional)
            username: Username of the PPPoE account, provided by your ISP.
            (optional)
            pppoe_egress_cos: CoS in VLAN tag for outgoing PPPoE/PPP packets.
            (optional)
            pppoe_unnumbered_negotiate: Enable/disable PPPoE unnumbered
            negotiation. (optional)
            password: PPPoE account's password. (optional)
            idle_timeout: PPPoE auto disconnect after idle timeout seconds, 0
            means no timeout. (optional)
            multilink: Enable/disable PPP multilink support. (optional)
            mrru: PPP MRRU (296 - 65535, default = 1500). (optional)
            detected_peer_mtu: MTU of detected peer (0 - 4294967295).
            (optional)
            disc_retry_timeout: Time in seconds to wait before retrying to
            start a PPPoE discovery, 0 means no timeout. (optional)
            padt_retry_timeout: PPPoE Active Discovery Terminate (PADT) used to
            terminate sessions after an idle time. (optional)
            service_name: PPPoE service name. (optional)
            ac_name: PPPoE server name. (optional)
            lcp_echo_interval: Time in seconds between PPPoE Link Control
            Protocol (LCP) echo requests. (optional)
            lcp_max_echo_fails: Maximum missed LCP echo messages before
            disconnect. (optional)
            defaultgw: Enable to get the gateway IP from the DHCP or PPPoE
            server. (optional)
            dns_server_override: Enable/disable use DNS acquired by DHCP or
            PPPoE. (optional)
            dns_server_protocol: DNS transport protocols. (optional)
            auth_type: PPP authentication type to use. (optional)
            pptp_client: Enable/disable PPTP client. (optional)
            pptp_user: PPTP user name. (optional)
            pptp_password: PPTP password. (optional)
            pptp_server_ip: PPTP server IP address. (optional)
            pptp_auth_type: PPTP authentication type. (optional)
            pptp_timeout: Idle timer in minutes (0 for disabled). (optional)
            arpforward: Enable/disable ARP forwarding. (optional)
            ndiscforward: Enable/disable NDISC forwarding. (optional)
            broadcast_forward: Enable/disable broadcast forwarding. (optional)
            bfd: Bidirectional Forwarding Detection (BFD) settings. (optional)
            bfd_desired_min_tx: BFD desired minimal transmit interval.
            (optional)
            bfd_detect_mult: BFD detection multiplier. (optional)
            bfd_required_min_rx: BFD required minimal receive interval.
            (optional)
            l2forward: Enable/disable l2 forwarding. (optional)
            icmp_send_redirect: Enable/disable sending of ICMP redirects.
            (optional)
            icmp_accept_redirect: Enable/disable ICMP accept redirect.
            (optional)
            reachable_time: IPv4 reachable time in milliseconds (30000 -
            3600000, default = 30000). (optional)
            vlanforward: Enable/disable traffic forwarding between VLANs on
            this interface. (optional)
            stpforward: Enable/disable STP forwarding. (optional)
            stpforward_mode: Configure STP forwarding mode. (optional)
            ips_sniffer_mode: Enable/disable the use of this interface as a
            one-armed sniffer. (optional)
            ident_accept: Enable/disable authentication for this interface.
            (optional)
            ipmac: Enable/disable IP/MAC binding. (optional)
            subst: Enable to always send packets from this interface to a
            destination MAC address. (optional)
            macaddr: Change the interface's MAC address. (optional)
            virtual_mac: Change the interface's virtual MAC address. (optional)
            substitute_dst_mac: Destination MAC address that all packets are
            sent to from this interface. (optional)
            speed: Interface speed. The default setting and the options
            available depend on the interface hardware. (optional)
            status: Bring the interface up or shut the interface down.
            (optional)
            netbios_forward: Enable/disable NETBIOS forwarding. (optional)
            wins_ip: WINS server IP. (optional)
            type: Interface type. (optional)
            dedicated_to: Configure interface for single purpose. (optional)
            trust_ip_1: Trusted host for dedicated management traffic
            (0.0.0.0/24 for all hosts). (optional)
            trust_ip_2: Trusted host for dedicated management traffic
            (0.0.0.0/24 for all hosts). (optional)
            trust_ip_3: Trusted host for dedicated management traffic
            (0.0.0.0/24 for all hosts). (optional)
            trust_ip6_1: Trusted IPv6 host for dedicated management traffic
            (::/0 for all hosts). (optional)
            trust_ip6_2: Trusted IPv6 host for dedicated management traffic
            (::/0 for all hosts). (optional)
            trust_ip6_3: Trusted IPv6 host for dedicated management traffic
            (::/0 for all hosts). (optional)
            wccp: Enable/disable WCCP on this interface. Used for encapsulated
            WCCP communication between WCCP clients and servers. (optional)
            netflow_sampler: Enable/disable NetFlow on this interface and set
            the data that NetFlow collects (rx, tx, or both). (optional)
            netflow_sample_rate: NetFlow sample rate. Sample one packet every
            configured number of packets (optional)
            netflow_sampler_id: Netflow sampler ID. (optional)
            sflow_sampler: Enable/disable sFlow on this interface. (optional)
            drop_fragment: Enable/disable drop fragment packets. (optional)
            src_check: Enable/disable source IP check. (optional)
            sample_rate: sFlow sample rate (10 - 99999). (optional)
            polling_interval: sFlow polling interval in seconds (1 - 255).
            (optional)
            sample_direction: Data that NetFlow collects (rx, tx, or both).
            (optional)
            explicit_web_proxy: Enable/disable the explicit web proxy on this
            interface. (optional)
            explicit_ftp_proxy: Enable/disable the explicit FTP proxy on this
            interface. (optional)
            proxy_captive_portal: Enable/disable proxy captive portal on this
            interface. (optional)
            tcp_mss: TCP maximum segment size. 0 means do not change segment
            size. (optional)
            inbandwidth: Bandwidth limit for incoming traffic (0 - 80000000
            kbps), 0 means unlimited. (optional)
            outbandwidth: Bandwidth limit for outgoing traffic (0 - 80000000
            kbps). (optional)
            egress_shaping_profile: Outgoing traffic shaping profile.
            (optional)
            ingress_shaping_profile: Incoming traffic shaping profile.
            (optional)
            spillover_threshold: Egress Spillover threshold (0 - 16776000
            kbps), 0 means unlimited. (optional)
            ingress_spillover_threshold: Ingress Spillover threshold (0 -
            16776000 kbps), 0 means unlimited. (optional)
            weight: Default weight for static routes (if route has no weight
            configured). (optional)
            interface: Interface name. (optional)
            external: Enable/disable identifying the interface as an external
            interface (which usually means it's connected to the Internet).
            (optional)
            mtu_override: Enable to set a custom MTU for this interface.
            (optional)
            mtu: MTU value for this interface. (optional)
            vlan_protocol: Ethernet protocol of VLAN. (optional)
            vlanid: VLAN ID (1 - 4094). (optional)
            trunk: Enable/disable VLAN trunk. (optional)
            forward_domain: Transparent mode forward domain. (optional)
            remote_ip: Remote IP address of tunnel. (optional)
            member: Physical interfaces that belong to the aggregate or
            redundant interface. (optional)
            lacp_mode: LACP mode. (optional)
            lacp_ha_secondary: LACP HA secondary member. (optional)
            system_id_type: Method in which system ID is generated. (optional)
            system_id: Define a system ID for the aggregate interface.
            (optional)
            lacp_speed: How often the interface sends LACP messages. (optional)
            min_links: Minimum number of aggregated ports that must be up.
            (optional)
            min_links_down: Action to take when less than the configured
            minimum number of links are active. (optional)
            algorithm: Frame distribution algorithm. (optional)
            link_up_delay: Number of milliseconds to wait before considering a
            link is up. (optional)
            aggregate_type: Type of aggregation. (optional)
            priority_override: Enable/disable fail back to higher priority port
            once recovered. (optional)
            aggregate: Aggregate interface. (optional)
            redundant_interface: Redundant interface. (optional)
            devindex: Device Index. (optional)
            vindex: Switch control interface VLAN ID. (optional)
            switch: Contained in switch. (optional)
            description: Description. (optional)
            alias: Alias will be displayed with the interface name to make it
            easier to distinguish. (optional)
            l2tp_client: Enable/disable this interface as a Layer 2 Tunnelling
            Protocol (L2TP) client. (optional)
            l2tp_client_settings: L2TP client settings. (optional)
            security_mode: Turn on captive portal authentication for this
            interface. (optional)
            security_mac_auth_bypass: Enable/disable MAC authentication bypass.
            (optional)
            security_ip_auth_bypass: Enable/disable IP authentication bypass.
            (optional)
            security_8021x_mode: 802.1X mode. (optional)
            security_8021x_master: 802.1X master virtual-switch. (optional)
            security_8021x_dynamic_vlan_id: VLAN ID for virtual switch.
            (optional)
            security_8021x_member_mode: 802.1X member mode. (optional)
            security_external_web: URL of external authentication web server.
            (optional)
            security_external_logout: URL of external authentication logout
            server. (optional)
            replacemsg_override_group: Replacement message override group.
            (optional)
            security_redirect_url: URL redirection after
            disclaimer/authentication. (optional)
            auth_cert: HTTPS server certificate. (optional)
            auth_portal_addr: Address of captive portal. (optional)
            security_exempt_list: Name of security-exempt-list. (optional)
            security_groups: User groups that can authenticate with the captive
            portal. (optional)
            ike_saml_server: Configure IKE authentication SAML server.
            (optional)
            stp: Enable/disable STP. (optional)
            stp_ha_secondary: Control STP behavior on HA secondary. (optional)
            stp_edge: Enable/disable as STP edge port. (optional)
            device_identification: Enable/disable passively gathering of device
            identity information about the devices on the network connected to
            this interface. (optional)
            exclude_signatures: Exclude IOT or OT application signatures.
            (optional)
            device_user_identification: Enable/disable passive gathering of
            user identity information about users on this interface. (optional)
            lldp_reception: Enable/disable Link Layer Discovery Protocol (LLDP)
            reception. (optional)
            lldp_transmission: Enable/disable Link Layer Discovery Protocol
            (LLDP) transmission. (optional)
            lldp_network_policy: LLDP-MED network policy profile. (optional)
            estimated_upstream_bandwidth: Estimated maximum upstream bandwidth
            (kbps). Used to estimate link utilization. (optional)
            estimated_downstream_bandwidth: Estimated maximum downstream
            bandwidth (kbps). Used to estimate link utilization. (optional)
            measured_upstream_bandwidth: Measured upstream bandwidth (kbps).
            (optional)
            measured_downstream_bandwidth: Measured downstream bandwidth
            (kbps). (optional)
            bandwidth_measure_time: Bandwidth measure time. (optional)
            monitor_bandwidth: Enable monitoring bandwidth on this interface.
            (optional)
            vrrp_virtual_mac: Enable/disable use of virtual MAC for VRRP.
            (optional)
            vrrp: VRRP configuration. (optional)
            phy_setting: PHY settings (optional)
            role: Interface role. (optional)
            snmp_index: Permanent SNMP Index of the interface. (optional)
            secondary_IP: Enable/disable adding a secondary IP to this
            interface. (optional)
            secondaryip: Second IP address of interface. (optional)
            preserve_session_route: Enable/disable preservation of session
            route when dirty. (optional)
            auto_auth_extension_device: Enable/disable automatic authorization
            of dedicated Fortinet extension device on this interface.
            (optional)
            ap_discover: Enable/disable automatic registration of unknown
            FortiAP devices. (optional)
            fortilink_neighbor_detect: Protocol for FortiGate neighbor
            discovery. (optional)
            ip_managed_by_fortiipam: Enable/disable automatic IP address
            assignment of this interface by FortiIPAM. (optional)
            managed_subnetwork_size: Number of IP addresses to be allocated by
            FortiIPAM and used by this FortiGate unit's DHCP server settings.
            (optional)
            fortilink_split_interface: Enable/disable FortiLink split interface
            to connect member link to different FortiSwitch in stack for uplink
            redundancy. (optional)
            internal: Implicitly created. (optional)
            fortilink_backup_link: FortiLink split interface backup link.
            (optional)
            switch_controller_access_vlan: Block FortiSwitch port-to-port
            traffic. (optional)
            switch_controller_traffic_policy: Switch controller traffic policy
            for the VLAN. (optional)
            switch_controller_rspan_mode: Stop Layer2 MAC learning and
            interception of BPDUs and other packets on this interface.
            (optional)
            switch_controller_netflow_collect: NetFlow collection and
            processing. (optional)
            switch_controller_mgmt_vlan: VLAN to use for FortiLink management
            purposes. (optional)
            switch_controller_igmp_snooping: Switch controller IGMP snooping.
            (optional)
            switch_controller_igmp_snooping_proxy: Switch controller IGMP
            snooping proxy. (optional)
            switch_controller_igmp_snooping_fast_leave: Switch controller IGMP
            snooping fast-leave. (optional)
            switch_controller_dhcp_snooping: Switch controller DHCP snooping.
            (optional)
            switch_controller_dhcp_snooping_verify_mac: Switch controller DHCP
            snooping verify MAC. (optional)
            switch_controller_dhcp_snooping_option82: Switch controller DHCP
            snooping option82. (optional)
            dhcp_snooping_server_list: Configure DHCP server access list.
            (optional)
            switch_controller_arp_inspection: Enable/disable/Monitor
            FortiSwitch ARP inspection. (optional)
            switch_controller_learning_limit: Limit the number of dynamic MAC
            addresses on this VLAN (1 - 128, 0 = no limit, default). (optional)
            switch_controller_nac: Integrated FortiLink settings for managed
            FortiSwitch. (optional)
            switch_controller_dynamic: Integrated FortiLink settings for
            managed FortiSwitch. (optional)
            switch_controller_feature: Interface's purpose when assigning
            traffic (read only). (optional)
            switch_controller_iot_scanning: Enable/disable managed FortiSwitch
            IoT scanning. (optional)
            switch_controller_offload: Enable/disable managed FortiSwitch
            routing offload. (optional)
            switch_controller_offload_ip: IP for routing offload on
            FortiSwitch. (optional)
            switch_controller_offload_gw: Enable/disable managed FortiSwitch
            routing offload gateway. (optional)
            swc_vlan: Creation status for switch-controller VLANs. (optional)
            swc_first_create: Initial create for switch-controller VLANs.
            (optional)
            color: Color of icon on the GUI. (optional)
            tagging: Config object tagging. (optional)
            eap_supplicant: Enable/disable EAP-Supplicant. (optional)
            eap_method: EAP method. (optional)
            eap_identity: EAP identity. (optional)
            eap_password: EAP password. (optional)
            eap_ca_cert: EAP CA certificate name. (optional)
            eap_user_cert: EAP user certificate name. (optional)
            default_purdue_level: default purdue level of device detected on
            this interface. (optional)
            ipv6: IPv6 of interface. (optional)
            physical: Print physical interface information. (optional)
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
        endpoint = "/system/interface"
        if nkey is not None:
            data_payload["nkey"] = nkey
        if name is not None:
            data_payload["name"] = name
        if vrf is not None:
            data_payload["vr"] = vrf
        if cli_conn_status is not None:
            data_payload["cli-conn-status"] = cli_conn_status
        if fortilink is not None:
            data_payload["fortilink"] = fortilink
        if switch_controller_source_ip is not None:
            data_payload["switch-controller-source-ip"] = (
                switch_controller_source_ip
            )
        if mode is not None:
            data_payload["mode"] = mode
        if client_options is not None:
            data_payload["client-options"] = client_options
        if distance is not None:
            data_payload["distance"] = distance
        if priority is not None:
            data_payload["priority"] = priority
        if dhcp_relay_interface_select_method is not None:
            data_payload["dhcp-relay-interface-select-method"] = (
                dhcp_relay_interface_select_method
            )
        if dhcp_relay_interface is not None:
            data_payload["dhcp-relay-interface"] = dhcp_relay_interface
        if dhcp_relay_vrf_select is not None:
            data_payload["dhcp-relay-vrf-select"] = dhcp_relay_vrf_select
        if dhcp_broadcast_flag is not None:
            data_payload["dhcp-broadcast-flag"] = dhcp_broadcast_flag
        if dhcp_relay_service is not None:
            data_payload["dhcp-relay-service"] = dhcp_relay_service
        if dhcp_relay_ip is not None:
            data_payload["dhcp-relay-ip"] = dhcp_relay_ip
        if dhcp_relay_source_ip is not None:
            data_payload["dhcp-relay-source-ip"] = dhcp_relay_source_ip
        if dhcp_relay_circuit_id is not None:
            data_payload["dhcp-relay-circuit-id"] = dhcp_relay_circuit_id
        if dhcp_relay_link_selection is not None:
            data_payload["dhcp-relay-link-selection"] = (
                dhcp_relay_link_selection
            )
        if dhcp_relay_request_all_server is not None:
            data_payload["dhcp-relay-request-all-server"] = (
                dhcp_relay_request_all_server
            )
        if dhcp_relay_allow_no_end_option is not None:
            data_payload["dhcp-relay-allow-no-end-option"] = (
                dhcp_relay_allow_no_end_option
            )
        if dhcp_relay_type is not None:
            data_payload["dhcp-relay-type"] = dhcp_relay_type
        if dhcp_smart_relay is not None:
            data_payload["dhcp-smart-relay"] = dhcp_smart_relay
        if dhcp_relay_agent_option is not None:
            data_payload["dhcp-relay-agent-option"] = dhcp_relay_agent_option
        if dhcp_classless_route_addition is not None:
            data_payload["dhcp-classless-route-addition"] = (
                dhcp_classless_route_addition
            )
        if management_ip is not None:
            data_payload["management-ip"] = management_ip
        if ip is not None:
            data_payload["ip"] = ip
        if allowaccess is not None:
            data_payload["allowaccess"] = allowaccess
        if gwdetect is not None:
            data_payload["gwdetect"] = gwdetect
        if ping_serv_status is not None:
            data_payload["ping-serv-status"] = ping_serv_status
        if detectserver is not None:
            data_payload["detectserver"] = detectserver
        if detectprotocol is not None:
            data_payload["detectprotocol"] = detectprotocol
        if ha_priority is not None:
            data_payload["ha-priority"] = ha_priority
        if fail_detect is not None:
            data_payload["fail-detect"] = fail_detect
        if fail_detect_option is not None:
            data_payload["fail-detect-option"] = fail_detect_option
        if fail_alert_method is not None:
            data_payload["fail-alert-method"] = fail_alert_method
        if fail_action_on_extender is not None:
            data_payload["fail-action-on-extender"] = fail_action_on_extender
        if fail_alert_interfaces is not None:
            data_payload["fail-alert-interfaces"] = fail_alert_interfaces
        if dhcp_client_identifier is not None:
            data_payload["dhcp-client-identifier"] = dhcp_client_identifier
        if dhcp_renew_time is not None:
            data_payload["dhcp-renew-time"] = dhcp_renew_time
        if ipunnumbered is not None:
            data_payload["ipunnumbered"] = ipunnumbered
        if username is not None:
            data_payload["username"] = username
        if pppoe_egress_cos is not None:
            data_payload["pppoe-egress-cos"] = pppoe_egress_cos
        if pppoe_unnumbered_negotiate is not None:
            data_payload["pppoe-unnumbered-negotiate"] = (
                pppoe_unnumbered_negotiate
            )
        if password is not None:
            data_payload["password"] = password
        if idle_timeout is not None:
            data_payload["idle-timeout"] = idle_timeout
        if multilink is not None:
            data_payload["multilink"] = multilink
        if mrru is not None:
            data_payload["mrru"] = mrru
        if detected_peer_mtu is not None:
            data_payload["detected-peer-mtu"] = detected_peer_mtu
        if disc_retry_timeout is not None:
            data_payload["disc-retry-timeout"] = disc_retry_timeout
        if padt_retry_timeout is not None:
            data_payload["padt-retry-timeout"] = padt_retry_timeout
        if service_name is not None:
            data_payload["service-name"] = service_name
        if ac_name is not None:
            data_payload["ac-name"] = ac_name
        if lcp_echo_interval is not None:
            data_payload["lcp-echo-interval"] = lcp_echo_interval
        if lcp_max_echo_fails is not None:
            data_payload["lcp-max-echo-fails"] = lcp_max_echo_fails
        if defaultgw is not None:
            data_payload["defaultgw"] = defaultgw
        if dns_server_override is not None:
            data_payload["dns-server-override"] = dns_server_override
        if dns_server_protocol is not None:
            data_payload["dns-server-protocol"] = dns_server_protocol
        if auth_type is not None:
            data_payload["auth-type"] = auth_type
        if pptp_client is not None:
            data_payload["pptp-client"] = pptp_client
        if pptp_user is not None:
            data_payload["pptp-user"] = pptp_user
        if pptp_password is not None:
            data_payload["pptp-password"] = pptp_password
        if pptp_server_ip is not None:
            data_payload["pptp-server-ip"] = pptp_server_ip
        if pptp_auth_type is not None:
            data_payload["pptp-auth-type"] = pptp_auth_type
        if pptp_timeout is not None:
            data_payload["pptp-timeout"] = pptp_timeout
        if arpforward is not None:
            data_payload["arpforward"] = arpforward
        if ndiscforward is not None:
            data_payload["ndiscforward"] = ndiscforward
        if broadcast_forward is not None:
            data_payload["broadcast-forward"] = broadcast_forward
        if bfd is not None:
            data_payload["bfd"] = bfd
        if bfd_desired_min_tx is not None:
            data_payload["bfd-desired-min-tx"] = bfd_desired_min_tx
        if bfd_detect_mult is not None:
            data_payload["bfd-detect-mult"] = bfd_detect_mult
        if bfd_required_min_rx is not None:
            data_payload["bfd-required-min-rx"] = bfd_required_min_rx
        if l2forward is not None:
            data_payload["l2forward"] = l2forward
        if icmp_send_redirect is not None:
            data_payload["icmp-send-redirect"] = icmp_send_redirect
        if icmp_accept_redirect is not None:
            data_payload["icmp-accept-redirect"] = icmp_accept_redirect
        if reachable_time is not None:
            data_payload["reachable-time"] = reachable_time
        if vlanforward is not None:
            data_payload["vlanforward"] = vlanforward
        if stpforward is not None:
            data_payload["stpforward"] = stpforward
        if stpforward_mode is not None:
            data_payload["stpforward-mode"] = stpforward_mode
        if ips_sniffer_mode is not None:
            data_payload["ips-sniffer-mode"] = ips_sniffer_mode
        if ident_accept is not None:
            data_payload["ident-accept"] = ident_accept
        if ipmac is not None:
            data_payload["ipmac"] = ipmac
        if subst is not None:
            data_payload["subst"] = subst
        if macaddr is not None:
            data_payload["macaddr"] = macaddr
        if virtual_mac is not None:
            data_payload["virtual-mac"] = virtual_mac
        if substitute_dst_mac is not None:
            data_payload["substitute-dst-mac"] = substitute_dst_mac
        if speed is not None:
            data_payload["speed"] = speed
        if status is not None:
            data_payload["status"] = status
        if netbios_forward is not None:
            data_payload["netbios-forward"] = netbios_forward
        if wins_ip is not None:
            data_payload["wins-ip"] = wins_ip
        if type is not None:
            data_payload["type"] = type
        if dedicated_to is not None:
            data_payload["dedicated-to"] = dedicated_to
        if trust_ip_1 is not None:
            data_payload["trust-ip-1"] = trust_ip_1
        if trust_ip_2 is not None:
            data_payload["trust-ip-2"] = trust_ip_2
        if trust_ip_3 is not None:
            data_payload["trust-ip-3"] = trust_ip_3
        if trust_ip6_1 is not None:
            data_payload["trust-ip6-1"] = trust_ip6_1
        if trust_ip6_2 is not None:
            data_payload["trust-ip6-2"] = trust_ip6_2
        if trust_ip6_3 is not None:
            data_payload["trust-ip6-3"] = trust_ip6_3
        if wccp is not None:
            data_payload["wccp"] = wccp
        if netflow_sampler is not None:
            data_payload["netflow-sampler"] = netflow_sampler
        if netflow_sample_rate is not None:
            data_payload["netflow-sample-rate"] = netflow_sample_rate
        if netflow_sampler_id is not None:
            data_payload["netflow-sampler-id"] = netflow_sampler_id
        if sflow_sampler is not None:
            data_payload["sflow-sampler"] = sflow_sampler
        if drop_fragment is not None:
            data_payload["drop-fragment"] = drop_fragment
        if src_check is not None:
            data_payload["src-check"] = src_check
        if sample_rate is not None:
            data_payload["sample-rate"] = sample_rate
        if polling_interval is not None:
            data_payload["polling-interval"] = polling_interval
        if sample_direction is not None:
            data_payload["sample-direction"] = sample_direction
        if explicit_web_proxy is not None:
            data_payload["explicit-web-proxy"] = explicit_web_proxy
        if explicit_ftp_proxy is not None:
            data_payload["explicit-ftp-proxy"] = explicit_ftp_proxy
        if proxy_captive_portal is not None:
            data_payload["proxy-captive-portal"] = proxy_captive_portal
        if tcp_mss is not None:
            data_payload["tcp-mss"] = tcp_mss
        if inbandwidth is not None:
            data_payload["inbandwidth"] = inbandwidth
        if outbandwidth is not None:
            data_payload["outbandwidth"] = outbandwidth
        if egress_shaping_profile is not None:
            data_payload["egress-shaping-profile"] = egress_shaping_profile
        if ingress_shaping_profile is not None:
            data_payload["ingress-shaping-profile"] = ingress_shaping_profile
        if spillover_threshold is not None:
            data_payload["spillover-threshold"] = spillover_threshold
        if ingress_spillover_threshold is not None:
            data_payload["ingress-spillover-threshold"] = (
                ingress_spillover_threshold
            )
        if weight is not None:
            data_payload["weight"] = weight
        if interface is not None:
            data_payload["interface"] = interface
        if external is not None:
            data_payload["external"] = external
        if mtu_override is not None:
            data_payload["mtu-override"] = mtu_override
        if mtu is not None:
            data_payload["mtu"] = mtu
        if vlan_protocol is not None:
            data_payload["vlan-protocol"] = vlan_protocol
        if vlanid is not None:
            data_payload["vlanid"] = vlanid
        if trunk is not None:
            data_payload["trunk"] = trunk
        if forward_domain is not None:
            data_payload["forward-domain"] = forward_domain
        if remote_ip is not None:
            data_payload["remote-ip"] = remote_ip
        if member is not None:
            data_payload["member"] = member
        if lacp_mode is not None:
            data_payload["lacp-mode"] = lacp_mode
        if lacp_ha_secondary is not None:
            data_payload["lacp-ha-secondary"] = lacp_ha_secondary
        if system_id_type is not None:
            data_payload["system-id-type"] = system_id_type
        if system_id is not None:
            data_payload["system-id"] = system_id
        if lacp_speed is not None:
            data_payload["lacp-speed"] = lacp_speed
        if min_links is not None:
            data_payload["min-links"] = min_links
        if min_links_down is not None:
            data_payload["min-links-down"] = min_links_down
        if algorithm is not None:
            data_payload["algorithm"] = algorithm
        if link_up_delay is not None:
            data_payload["link-up-delay"] = link_up_delay
        if aggregate_type is not None:
            data_payload["aggregate-type"] = aggregate_type
        if priority_override is not None:
            data_payload["priority-override"] = priority_override
        if aggregate is not None:
            data_payload["aggregate"] = aggregate
        if redundant_interface is not None:
            data_payload["redundant-interface"] = redundant_interface
        if devindex is not None:
            data_payload["devindex"] = devindex
        if vindex is not None:
            data_payload["vindex"] = vindex
        if switch is not None:
            data_payload["switch"] = switch
        if description is not None:
            data_payload["description"] = description
        if alias is not None:
            data_payload["alias"] = alias
        if l2tp_client is not None:
            data_payload["l2tp-client"] = l2tp_client
        if l2tp_client_settings is not None:
            data_payload["l2tp-client-settings"] = l2tp_client_settings
        if security_mode is not None:
            data_payload["security-mode"] = security_mode
        if security_mac_auth_bypass is not None:
            data_payload["security-mac-auth-bypass"] = security_mac_auth_bypass
        if security_ip_auth_bypass is not None:
            data_payload["security-ip-auth-bypass"] = security_ip_auth_bypass
        if security_8021x_mode is not None:
            data_payload["security-8021x-mode"] = security_8021x_mode
        if security_8021x_master is not None:
            data_payload["security-8021x-master"] = security_8021x_master
        if security_8021x_dynamic_vlan_id is not None:
            data_payload["security-8021x-dynamic-vlan-id"] = (
                security_8021x_dynamic_vlan_id
            )
        if security_8021x_member_mode is not None:
            data_payload["security-8021x-member-mode"] = (
                security_8021x_member_mode
            )
        if security_external_web is not None:
            data_payload["security-external-web"] = security_external_web
        if security_external_logout is not None:
            data_payload["security-external-logout"] = security_external_logout
        if replacemsg_override_group is not None:
            data_payload["replacemsg-override-group"] = (
                replacemsg_override_group
            )
        if security_redirect_url is not None:
            data_payload["security-redirect-url"] = security_redirect_url
        if auth_cert is not None:
            data_payload["auth-cert"] = auth_cert
        if auth_portal_addr is not None:
            data_payload["auth-portal-addr"] = auth_portal_addr
        if security_exempt_list is not None:
            data_payload["security-exempt-list"] = security_exempt_list
        if security_groups is not None:
            data_payload["security-groups"] = security_groups
        if ike_saml_server is not None:
            data_payload["ike-saml-server"] = ike_saml_server
        if stp is not None:
            data_payload["stp"] = stp
        if stp_ha_secondary is not None:
            data_payload["stp-ha-secondary"] = stp_ha_secondary
        if stp_edge is not None:
            data_payload["stp-edge"] = stp_edge
        if device_identification is not None:
            data_payload["device-identification"] = device_identification
        if exclude_signatures is not None:
            data_payload["exclude-signatures"] = exclude_signatures
        if device_user_identification is not None:
            data_payload["device-user-identification"] = (
                device_user_identification
            )
        if lldp_reception is not None:
            data_payload["lldp-reception"] = lldp_reception
        if lldp_transmission is not None:
            data_payload["lldp-transmission"] = lldp_transmission
        if lldp_network_policy is not None:
            data_payload["lldp-network-policy"] = lldp_network_policy
        if estimated_upstream_bandwidth is not None:
            data_payload["estimated-upstream-bandwidth"] = (
                estimated_upstream_bandwidth
            )
        if estimated_downstream_bandwidth is not None:
            data_payload["estimated-downstream-bandwidth"] = (
                estimated_downstream_bandwidth
            )
        if measured_upstream_bandwidth is not None:
            data_payload["measured-upstream-bandwidth"] = (
                measured_upstream_bandwidth
            )
        if measured_downstream_bandwidth is not None:
            data_payload["measured-downstream-bandwidth"] = (
                measured_downstream_bandwidth
            )
        if bandwidth_measure_time is not None:
            data_payload["bandwidth-measure-time"] = bandwidth_measure_time
        if monitor_bandwidth is not None:
            data_payload["monitor-bandwidth"] = monitor_bandwidth
        if vrrp_virtual_mac is not None:
            data_payload["vrrp-virtual-mac"] = vrrp_virtual_mac
        if vrrp is not None:
            data_payload["vrrp"] = vrrp
        if phy_setting is not None:
            data_payload["phy-setting"] = phy_setting
        if role is not None:
            data_payload["role"] = role
        if snmp_index is not None:
            data_payload["snmp-index"] = snmp_index
        if secondary_IP is not None:
            data_payload["secondary-IP"] = secondary_IP
        if secondaryip is not None:
            data_payload["secondaryip"] = secondaryip
        if preserve_session_route is not None:
            data_payload["preserve-session-route"] = preserve_session_route
        if auto_auth_extension_device is not None:
            data_payload["auto-auth-extension-device"] = (
                auto_auth_extension_device
            )
        if ap_discover is not None:
            data_payload["ap-discover"] = ap_discover
        if fortilink_neighbor_detect is not None:
            data_payload["fortilink-neighbor-detect"] = (
                fortilink_neighbor_detect
            )
        if ip_managed_by_fortiipam is not None:
            data_payload["ip-managed-by-fortiipam"] = ip_managed_by_fortiipam
        if managed_subnetwork_size is not None:
            data_payload["managed-subnetwork-size"] = managed_subnetwork_size
        if fortilink_split_interface is not None:
            data_payload["fortilink-split-interface"] = (
                fortilink_split_interface
            )
        if internal is not None:
            data_payload["internal"] = internal
        if fortilink_backup_link is not None:
            data_payload["fortilink-backup-link"] = fortilink_backup_link
        if switch_controller_access_vlan is not None:
            data_payload["switch-controller-access-vlan"] = (
                switch_controller_access_vlan
            )
        if switch_controller_traffic_policy is not None:
            data_payload["switch-controller-traffic-policy"] = (
                switch_controller_traffic_policy
            )
        if switch_controller_rspan_mode is not None:
            data_payload["switch-controller-rspan-mode"] = (
                switch_controller_rspan_mode
            )
        if switch_controller_netflow_collect is not None:
            data_payload["switch-controller-netflow-collect"] = (
                switch_controller_netflow_collect
            )
        if switch_controller_mgmt_vlan is not None:
            data_payload["switch-controller-mgmt-vlan"] = (
                switch_controller_mgmt_vlan
            )
        if switch_controller_igmp_snooping is not None:
            data_payload["switch-controller-igmp-snooping"] = (
                switch_controller_igmp_snooping
            )
        if switch_controller_igmp_snooping_proxy is not None:
            data_payload["switch-controller-igmp-snooping-proxy"] = (
                switch_controller_igmp_snooping_proxy
            )
        if switch_controller_igmp_snooping_fast_leave is not None:
            data_payload["switch-controller-igmp-snooping-fast-leave"] = (
                switch_controller_igmp_snooping_fast_leave
            )
        if switch_controller_dhcp_snooping is not None:
            data_payload["switch-controller-dhcp-snooping"] = (
                switch_controller_dhcp_snooping
            )
        if switch_controller_dhcp_snooping_verify_mac is not None:
            data_payload["switch-controller-dhcp-snooping-verify-mac"] = (
                switch_controller_dhcp_snooping_verify_mac
            )
        if switch_controller_dhcp_snooping_option82 is not None:
            data_payload["switch-controller-dhcp-snooping-option82"] = (
                switch_controller_dhcp_snooping_option82
            )
        if dhcp_snooping_server_list is not None:
            data_payload["dhcp-snooping-server-list"] = (
                dhcp_snooping_server_list
            )
        if switch_controller_arp_inspection is not None:
            data_payload["switch-controller-arp-inspection"] = (
                switch_controller_arp_inspection
            )
        if switch_controller_learning_limit is not None:
            data_payload["switch-controller-learning-limit"] = (
                switch_controller_learning_limit
            )
        if switch_controller_nac is not None:
            data_payload["switch-controller-nac"] = switch_controller_nac
        if switch_controller_dynamic is not None:
            data_payload["switch-controller-dynamic"] = (
                switch_controller_dynamic
            )
        if switch_controller_feature is not None:
            data_payload["switch-controller-feature"] = (
                switch_controller_feature
            )
        if switch_controller_iot_scanning is not None:
            data_payload["switch-controller-iot-scanning"] = (
                switch_controller_iot_scanning
            )
        if switch_controller_offload is not None:
            data_payload["switch-controller-offload"] = (
                switch_controller_offload
            )
        if switch_controller_offload_ip is not None:
            data_payload["switch-controller-offload-ip"] = (
                switch_controller_offload_ip
            )
        if switch_controller_offload_gw is not None:
            data_payload["switch-controller-offload-gw"] = (
                switch_controller_offload_gw
            )
        if swc_vlan is not None:
            data_payload["swc-vlan"] = swc_vlan
        if swc_first_create is not None:
            data_payload["swc-first-create"] = swc_first_create
        if color is not None:
            data_payload["color"] = color
        if tagging is not None:
            data_payload["tagging"] = tagging
        if eap_supplicant is not None:
            data_payload["eap-supplicant"] = eap_supplicant
        if eap_method is not None:
            data_payload["eap-method"] = eap_method
        if eap_identity is not None:
            data_payload["eap-identity"] = eap_identity
        if eap_password is not None:
            data_payload["eap-password"] = eap_password
        if eap_ca_cert is not None:
            data_payload["eap-ca-cert"] = eap_ca_cert
        if eap_user_cert is not None:
            data_payload["eap-user-cert"] = eap_user_cert
        if default_purdue_level is not None:
            data_payload["default-purdue-level"] = default_purdue_level
        if ipv6 is not None:
            data_payload["ipv6"] = ipv6
        if physical is not None:
            data_payload["physical"] = physical
        data_payload.update(kwargs)
        return self._client.post(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )
