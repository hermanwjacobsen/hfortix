"""
FortiOS CMDB - Cmdb Firewall Policy

Configuration endpoint for managing cmdb firewall policy objects.

API Endpoints:
    GET    /cmdb/firewall/policy
    POST   /cmdb/firewall/policy
    GET    /cmdb/firewall/policy
    PUT    /cmdb/firewall/policy/{identifier}
    DELETE /cmdb/firewall/policy/{identifier}

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.firewall.policy.get()
    >>>
    >>> # Get specific item (if supported)
    >>> item = fgt.api.cmdb.firewall.policy.get(name="item_name")
    >>>
    >>> # Create new item (use POST)
    >>> result = fgt.api.cmdb.firewall.policy.post(
    ...     name="new_item",
    ...     # ... additional parameters
    ... )
    >>>
    >>> # Update existing item (use PUT)
    >>> result = fgt.api.cmdb.firewall.policy.put(
    ...     name="existing_item",
    ...     # ... parameters to update
    ... )
    >>>
    >>> # Delete item
    >>> result = fgt.api.cmdb.firewall.policy.delete(name="item_name")

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

# Import from central API helpers
from ...._helpers import build_cmdb_payload


class Policy:
    """
    Policy Operations.

    Provides CRUD operations for FortiOS policy configuration.

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
        Initialize Policy endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

    def get(
        self,
        policyid: str | None = None,
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
            policyid: Object identifier (optional for list, required for
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
        if policyid:
            endpoint = f"/firewall/policy/{policyid}"
        else:
            endpoint = "/firewall/policy"
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
        policyid: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        before: str | None = None,
        after: str | None = None,
        status: str | None = None,
        name: str | None = None,
        uuid: str | None = None,
        srcintf: list | None = None,
        dstintf: list | None = None,
        nat64: str | None = None,
        nat46: str | None = None,
        ztna_status: str | None = None,
        ztna_device_ownership: str | None = None,
        srcaddr: list | None = None,
        dstaddr: list | None = None,
        srcaddr6: list | None = None,
        dstaddr6: list | None = None,
        ztna_ems_tag: list | None = None,
        ztna_ems_tag_secondary: list | None = None,
        ztna_tags_match_logic: str | None = None,
        ztna_geo_tag: list | None = None,
        internet_service: str | None = None,
        internet_service_name: list | None = None,
        internet_service_group: list | None = None,
        internet_service_custom: list | None = None,
        network_service_dynamic: list | None = None,
        internet_service_custom_group: list | None = None,
        internet_service_src: str | None = None,
        internet_service_src_name: list | None = None,
        internet_service_src_group: list | None = None,
        internet_service_src_custom: list | None = None,
        network_service_src_dynamic: list | None = None,
        internet_service_src_custom_group: list | None = None,
        reputation_minimum: int | None = None,
        reputation_direction: str | None = None,
        src_vendor_mac: list | None = None,
        internet_service6: str | None = None,
        internet_service6_name: list | None = None,
        internet_service6_group: list | None = None,
        internet_service6_custom: list | None = None,
        internet_service6_custom_group: list | None = None,
        internet_service6_src: str | None = None,
        internet_service6_src_name: list | None = None,
        internet_service6_src_group: list | None = None,
        internet_service6_src_custom: list | None = None,
        internet_service6_src_custom_group: list | None = None,
        reputation_minimum6: int | None = None,
        reputation_direction6: str | None = None,
        rtp_nat: str | None = None,
        rtp_addr: list | None = None,
        send_deny_packet: str | None = None,
        firewall_session_dirty: str | None = None,
        schedule: str | None = None,
        schedule_timeout: str | None = None,
        policy_expiry: str | None = None,
        policy_expiry_date: str | None = None,
        policy_expiry_date_utc: str | None = None,
        service: list | None = None,
        tos_mask: str | None = None,
        tos: str | None = None,
        tos_negate: str | None = None,
        anti_replay: str | None = None,
        tcp_session_without_syn: str | None = None,
        geoip_anycast: str | None = None,
        geoip_match: str | None = None,
        dynamic_shaping: str | None = None,
        passive_wan_health_measurement: str | None = None,
        app_monitor: str | None = None,
        utm_status: str | None = None,
        inspection_mode: str | None = None,
        http_policy_redirect: str | None = None,
        ssh_policy_redirect: str | None = None,
        ztna_policy_redirect: str | None = None,
        webproxy_profile: str | None = None,
        profile_type: str | None = None,
        profile_group: str | None = None,
        profile_protocol_options: str | None = None,
        ssl_ssh_profile: str | None = None,
        av_profile: str | None = None,
        webfilter_profile: str | None = None,
        dnsfilter_profile: str | None = None,
        emailfilter_profile: str | None = None,
        dlp_profile: str | None = None,
        file_filter_profile: str | None = None,
        ips_sensor: str | None = None,
        application_list: str | None = None,
        voip_profile: str | None = None,
        ips_voip_filter: str | None = None,
        sctp_filter_profile: str | None = None,
        diameter_filter_profile: str | None = None,
        virtual_patch_profile: str | None = None,
        icap_profile: str | None = None,
        videofilter_profile: str | None = None,
        waf_profile: str | None = None,
        ssh_filter_profile: str | None = None,
        casb_profile: str | None = None,
        logtraffic: str | None = None,
        logtraffic_start: str | None = None,
        log_http_transaction: str | None = None,
        capture_packet: str | None = None,
        auto_asic_offload: str | None = None,
        np_acceleration: str | None = None,
        webproxy_forward_server: str | None = None,
        traffic_shaper: str | None = None,
        traffic_shaper_reverse: str | None = None,
        per_ip_shaper: str | None = None,
        nat: str | None = None,
        pcp_outbound: str | None = None,
        pcp_inbound: str | None = None,
        pcp_poolname: list | None = None,
        permit_any_host: str | None = None,
        permit_stun_host: str | None = None,
        fixedport: str | None = None,
        port_preserve: str | None = None,
        port_random: str | None = None,
        ippool: str | None = None,
        poolname: list | None = None,
        poolname6: list | None = None,
        session_ttl: str | None = None,
        vlan_cos_fwd: int | None = None,
        vlan_cos_rev: int | None = None,
        inbound: str | None = None,
        outbound: str | None = None,
        natinbound: str | None = None,
        natoutbound: str | None = None,
        fec: str | None = None,
        wccp: str | None = None,
        ntlm: str | None = None,
        ntlm_guest: str | None = None,
        ntlm_enabled_browsers: list | None = None,
        fsso_agent_for_ntlm: str | None = None,
        groups: list | None = None,
        users: list | None = None,
        fsso_groups: list | None = None,
        auth_path: str | None = None,
        disclaimer: str | None = None,
        email_collect: str | None = None,
        vpntunnel: str | None = None,
        natip: str | None = None,
        match_vip: str | None = None,
        match_vip_only: str | None = None,
        diffserv_copy: str | None = None,
        diffserv_forward: str | None = None,
        diffserv_reverse: str | None = None,
        diffservcode_forward: str | None = None,
        diffservcode_rev: str | None = None,
        tcp_mss_sender: int | None = None,
        tcp_mss_receiver: int | None = None,
        comments: str | None = None,
        auth_cert: str | None = None,
        auth_redirect_addr: str | None = None,
        redirect_url: str | None = None,
        identity_based_route: str | None = None,
        block_notification: str | None = None,
        custom_log_fields: list | None = None,
        replacemsg_override_group: str | None = None,
        srcaddr_negate: str | None = None,
        srcaddr6_negate: str | None = None,
        dstaddr_negate: str | None = None,
        dstaddr6_negate: str | None = None,
        ztna_ems_tag_negate: str | None = None,
        service_negate: str | None = None,
        internet_service_negate: str | None = None,
        internet_service_src_negate: str | None = None,
        internet_service6_negate: str | None = None,
        internet_service6_src_negate: str | None = None,
        timeout_send_rst: str | None = None,
        captive_portal_exempt: str | None = None,
        decrypted_traffic_mirror: str | None = None,
        dsri: str | None = None,
        radius_mac_auth_bypass: str | None = None,
        radius_ip_auth_bypass: str | None = None,
        delay_tcp_npu_session: str | None = None,
        vlan_filter: str | None = None,
        sgt_check: str | None = None,
        sgt: list | None = None,
        internet_service_fortiguard: list | None = None,
        internet_service_src_fortiguard: list | None = None,
        internet_service6_fortiguard: list | None = None,
        internet_service6_src_fortiguard: list | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update this specific resource.

        Args:
            payload_dict: Optional dictionary of all parameters (can be passed
            as first positional arg)
            policyid: Object identifier (required)
            before: If *action=move*, use *before* to specify the ID of the
            resource that this resource will be moved before. (optional)
            after: If *action=move*, use *after* to specify the ID of the
            resource that this resource will be moved after. (optional)
            policyid: Policy ID (0 - 4294967294). (optional)
            status: Enable or disable this policy. (optional)
            name: Policy name. (optional)
            uuid: Universally Unique Identifier (UUID; automatically assigned
            but can be manually reset). (optional)
            srcintf: Incoming (ingress) interface. (optional)
            dstintf: Outgoing (egress) interface. (optional)
            nat64: Enable/disable NAT64. (optional)
            nat46: Enable/disable NAT46. (optional)
            ztna_status: Enable/disable zero trust access. (optional)
            ztna_device_ownership: Enable/disable zero trust device ownership.
            (optional)
            srcaddr: Source IPv4 address and address group names. (optional)
            dstaddr: Destination IPv4 address and address group names.
            (optional)
            srcaddr6: Source IPv6 address name and address group names.
            (optional)
            dstaddr6: Destination IPv6 address name and address group names.
            (optional)
            ztna_ems_tag: Source ztna-ems-tag names. (optional)
            ztna_ems_tag_secondary: Source ztna-ems-tag-secondary names.
            (optional)
            ztna_tags_match_logic: ZTNA tag matching logic. (optional)
            ztna_geo_tag: Source ztna-geo-tag names. (optional)
            internet_service: Enable/disable use of Internet Services for this
            policy. If enabled, destination address and service are not used.
            (optional)
            internet_service_name: Internet Service name. (optional)
            internet_service_group: Internet Service group name. (optional)
            internet_service_custom: Custom Internet Service name. (optional)
            network_service_dynamic: Dynamic Network Service name. (optional)
            internet_service_custom_group: Custom Internet Service group name.
            (optional)
            internet_service_src: Enable/disable use of Internet Services in
            source for this policy. If enabled, source address is not used.
            (optional)
            internet_service_src_name: Internet Service source name. (optional)
            internet_service_src_group: Internet Service source group name.
            (optional)
            internet_service_src_custom: Custom Internet Service source name.
            (optional)
            network_service_src_dynamic: Dynamic Network Service source name.
            (optional)
            internet_service_src_custom_group: Custom Internet Service source
            group name. (optional)
            reputation_minimum: Minimum Reputation to take action. (optional)
            reputation_direction: Direction of the initial traffic for
            reputation to take effect. (optional)
            src_vendor_mac: Vendor MAC source ID. (optional)
            internet_service6: Enable/disable use of IPv6 Internet Services for
            this policy. If enabled, destination address and service are not
            used. (optional)
            internet_service6_name: IPv6 Internet Service name. (optional)
            internet_service6_group: Internet Service group name. (optional)
            internet_service6_custom: Custom IPv6 Internet Service name.
            (optional)
            internet_service6_custom_group: Custom Internet Service6 group
            name. (optional)
            internet_service6_src: Enable/disable use of IPv6 Internet Services
            in source for this policy. If enabled, source address is not used.
            (optional)
            internet_service6_src_name: IPv6 Internet Service source name.
            (optional)
            internet_service6_src_group: Internet Service6 source group name.
            (optional)
            internet_service6_src_custom: Custom IPv6 Internet Service source
            name. (optional)
            internet_service6_src_custom_group: Custom Internet Service6 source
            group name. (optional)
            reputation_minimum6: IPv6 Minimum Reputation to take action.
            (optional)
            reputation_direction6: Direction of the initial traffic for IPv6
            reputation to take effect. (optional)
            rtp_nat: Enable Real Time Protocol (RTP) NAT. (optional)
            rtp_addr: Address names if this is an RTP NAT policy. (optional)
            send_deny_packet: Enable to send a reply when a session is denied
            or blocked by a firewall policy. (optional)
            firewall_session_dirty: How to handle sessions if the configuration
            of this firewall policy changes. (optional)
            schedule: Schedule name. (optional)
            schedule_timeout: Enable to force current sessions to end when the
            schedule object times out. Disable allows them to end from
            inactivity. (optional)
            policy_expiry: Enable/disable policy expiry. (optional)
            policy_expiry_date: Policy expiry date (YYYY-MM-DD HH:MM:SS).
            (optional)
            policy_expiry_date_utc: Policy expiry date and time, in epoch
            format. (optional)
            service: Service and service group names. (optional)
            tos_mask: Non-zero bit positions are used for comparison while zero
            bit positions are ignored. (optional)
            tos: ToS (Type of Service) value used for comparison. (optional)
            tos_negate: Enable negated TOS match. (optional)
            anti_replay: Enable/disable anti-replay check. (optional)
            tcp_session_without_syn: Enable/disable creation of TCP session
            without SYN flag. (optional)
            geoip_anycast: Enable/disable recognition of anycast IP addresses
            using the geography IP database. (optional)
            geoip_match: Match geography address based either on its physical
            location or registered location. (optional)
            dynamic_shaping: Enable/disable dynamic RADIUS defined traffic
            shaping. (optional)
            passive_wan_health_measurement: Enable/disable passive WAN health
            measurement. When enabled, auto-asic-offload is disabled.
            (optional)
            app_monitor: Enable/disable application TCP metrics in session
            logs.When enabled, auto-asic-offload is disabled. (optional)
            utm_status: Enable to add one or more security profiles (AV, IPS,
            etc.) to the firewall policy. (optional)
            inspection_mode: Policy inspection mode (Flow/proxy). Default is
            Flow mode. (optional)
            http_policy_redirect: Redirect HTTP(S) traffic to matching
            transparent web proxy policy. (optional)
            ssh_policy_redirect: Redirect SSH traffic to matching transparent
            proxy policy. (optional)
            ztna_policy_redirect: Redirect ZTNA traffic to matching
            Access-Proxy proxy-policy. (optional)
            webproxy_profile: Webproxy profile name. (optional)
            profile_type: Determine whether the firewall policy allows security
            profile groups or single profiles only. (optional)
            profile_group: Name of profile group. (optional)
            profile_protocol_options: Name of an existing Protocol options
            profile. (optional)
            ssl_ssh_profile: Name of an existing SSL SSH profile. (optional)
            av_profile: Name of an existing Antivirus profile. (optional)
            webfilter_profile: Name of an existing Web filter profile.
            (optional)
            dnsfilter_profile: Name of an existing DNS filter profile.
            (optional)
            emailfilter_profile: Name of an existing email filter profile.
            (optional)
            dlp_profile: Name of an existing DLP profile. (optional)
            file_filter_profile: Name of an existing file-filter profile.
            (optional)
            ips_sensor: Name of an existing IPS sensor. (optional)
            application_list: Name of an existing Application list. (optional)
            voip_profile: Name of an existing VoIP (voipd) profile. (optional)
            ips_voip_filter: Name of an existing VoIP (ips) profile. (optional)
            sctp_filter_profile: Name of an existing SCTP filter profile.
            (optional)
            diameter_filter_profile: Name of an existing Diameter filter
            profile. (optional)
            virtual_patch_profile: Name of an existing virtual-patch profile.
            (optional)
            icap_profile: Name of an existing ICAP profile. (optional)
            videofilter_profile: Name of an existing VideoFilter profile.
            (optional)
            waf_profile: Name of an existing Web application firewall profile.
            (optional)
            ssh_filter_profile: Name of an existing SSH filter profile.
            (optional)
            casb_profile: Name of an existing CASB profile. (optional)
            logtraffic: Enable or disable logging. Log all sessions or security
            profile sessions. (optional)
            logtraffic_start: Record logs when a session starts. (optional)
            log_http_transaction: Enable/disable HTTP transaction log.
            (optional)
            capture_packet: Enable/disable capture packets. (optional)
            auto_asic_offload: Enable/disable policy traffic ASIC offloading.
            (optional)
            np_acceleration: Enable/disable UTM Network Processor acceleration.
            (optional)
            webproxy_forward_server: Webproxy forward server name. (optional)
            traffic_shaper: Traffic shaper. (optional)
            traffic_shaper_reverse: Reverse traffic shaper. (optional)
            per_ip_shaper: Per-IP traffic shaper. (optional)
            nat: Enable/disable source NAT. (optional)
            pcp_outbound: Enable/disable PCP outbound SNAT. (optional)
            pcp_inbound: Enable/disable PCP inbound DNAT. (optional)
            pcp_poolname: PCP pool names. (optional)
            permit_any_host: Enable/disable fullcone NAT. Accept UDP packets
            from any host. (optional)
            permit_stun_host: Accept UDP packets from any Session Traversal
            Utilities for NAT (STUN) host. (optional)
            fixedport: Enable to prevent source NAT from changing a session's
            source port. (optional)
            port_preserve: Enable/disable preservation of the original source
            port from source NAT if it has not been used. (optional)
            port_random: Enable/disable random source port selection for source
            NAT. (optional)
            ippool: Enable to use IP Pools for source NAT. (optional)
            poolname: IP Pool names. (optional)
            poolname6: IPv6 pool names. (optional)
            session_ttl: TTL in seconds for sessions accepted by this policy (0
            means use the system default session TTL). (optional)
            vlan_cos_fwd: VLAN forward direction user priority: 255
            passthrough, 0 lowest, 7 highest. (optional)
            vlan_cos_rev: VLAN reverse direction user priority: 255
            passthrough, 0 lowest, 7 highest. (optional)
            inbound: Policy-based IPsec VPN: only traffic from the remote
            network can initiate a VPN. (optional)
            outbound: Policy-based IPsec VPN: only traffic from the internal
            network can initiate a VPN. (optional)
            natinbound: Policy-based IPsec VPN: apply destination NAT to
            inbound traffic. (optional)
            natoutbound: Policy-based IPsec VPN: apply source NAT to outbound
            traffic. (optional)
            fec: Enable/disable Forward Error Correction on traffic matching
            this policy on a FEC device. (optional)
            wccp: Enable/disable forwarding traffic matching this policy to a
            configured WCCP server. (optional)
            ntlm: Enable/disable NTLM authentication. (optional)
            ntlm_guest: Enable/disable NTLM guest user access. (optional)
            ntlm_enabled_browsers: HTTP-User-Agent value of supported browsers.
            (optional)
            fsso_agent_for_ntlm: FSSO agent to use for NTLM authentication.
            (optional)
            groups: Names of user groups that can authenticate with this
            policy. (optional)
            users: Names of individual users that can authenticate with this
            policy. (optional)
            fsso_groups: Names of FSSO groups. (optional)
            auth_path: Enable/disable authentication-based routing. (optional)
            disclaimer: Enable/disable user authentication disclaimer.
            (optional)
            email_collect: Enable/disable email collection. (optional)
            vpntunnel: Policy-based IPsec VPN: name of the IPsec VPN Phase 1.
            (optional)
            natip: Policy-based IPsec VPN: source NAT IP address for outgoing
            traffic. (optional)
            match_vip: Enable to match packets that have had their destination
            addresses changed by a VIP. (optional)
            match_vip_only: Enable/disable matching of only those packets that
            have had their destination addresses changed by a VIP. (optional)
            diffserv_copy: Enable to copy packet's DiffServ values from
            session's original direction to its reply direction. (optional)
            diffserv_forward: Enable to change packet's DiffServ values to the
            specified diffservcode-forward value. (optional)
            diffserv_reverse: Enable to change packet's reverse (reply)
            DiffServ values to the specified diffservcode-rev value. (optional)
            diffservcode_forward: Change packet's DiffServ to this value.
            (optional)
            diffservcode_rev: Change packet's reverse (reply) DiffServ to this
            value. (optional)
            tcp_mss_sender: Sender TCP maximum segment size (MSS). (optional)
            tcp_mss_receiver: Receiver TCP maximum segment size (MSS).
            (optional)
            comments: Comment. (optional)
            auth_cert: HTTPS server certificate for policy authentication.
            (optional)
            auth_redirect_addr: HTTP-to-HTTPS redirect address for firewall
            authentication. (optional)
            redirect_url: URL users are directed to after seeing and accepting
            the disclaimer or authenticating. (optional)
            identity_based_route: Name of identity-based routing rule.
            (optional)
            block_notification: Enable/disable block notification. (optional)
            custom_log_fields: Custom fields to append to log messages for this
            policy. (optional)
            replacemsg_override_group: Override the default replacement message
            group for this policy. (optional)
            srcaddr_negate: When enabled srcaddr specifies what the source
            address must NOT be. (optional)
            srcaddr6_negate: When enabled srcaddr6 specifies what the source
            address must NOT be. (optional)
            dstaddr_negate: When enabled dstaddr specifies what the destination
            address must NOT be. (optional)
            dstaddr6_negate: When enabled dstaddr6 specifies what the
            destination address must NOT be. (optional)
            ztna_ems_tag_negate: When enabled ztna-ems-tag specifies what the
            tags must NOT be. (optional)
            service_negate: When enabled service specifies what the service
            must NOT be. (optional)
            internet_service_negate: When enabled internet-service specifies
            what the service must NOT be. (optional)
            internet_service_src_negate: When enabled internet-service-src
            specifies what the service must NOT be. (optional)
            internet_service6_negate: When enabled internet-service6 specifies
            what the service must NOT be. (optional)
            internet_service6_src_negate: When enabled internet-service6-src
            specifies what the service must NOT be. (optional)
            timeout_send_rst: Enable/disable sending RST packets when TCP
            sessions expire. (optional)
            captive_portal_exempt: Enable to exempt some users from the captive
            portal. (optional)
            decrypted_traffic_mirror: Decrypted traffic mirror. (optional)
            dsri: Enable DSRI to ignore HTTP server responses. (optional)
            radius_mac_auth_bypass: Enable MAC authentication bypass. The
            bypassed MAC address must be received from RADIUS server.
            (optional)
            radius_ip_auth_bypass: Enable IP authentication bypass. The
            bypassed IP address must be received from RADIUS server. (optional)
            delay_tcp_npu_session: Enable TCP NPU session delay to guarantee
            packet order of 3-way handshake. (optional)
            vlan_filter: VLAN ranges to allow (optional)
            sgt_check: Enable/disable security group tags (SGT) check.
            (optional)
            sgt: Security group tags. (optional)
            internet_service_fortiguard: FortiGuard Internet Service name.
            (optional)
            internet_service_src_fortiguard: FortiGuard Internet Service source
            name. (optional)
            internet_service6_fortiguard: FortiGuard IPv6 Internet Service
            name. (optional)
            internet_service6_src_fortiguard: FortiGuard IPv6 Internet Service
            source name. (optional)
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
        # Start with payload_dict or empty
        data_payload = payload_dict.copy() if payload_dict else {}

        # Build endpoint path
        if not policyid:
            raise ValueError("policyid is required for put()")
        endpoint = f"/firewall/policy/{policyid}"

        # Build payload from all parameters using helper function
        policy_params = build_cmdb_payload(
            before=before,
            after=after,
            policyid=policyid,
            status=status,
            name=name,
            uuid=uuid,
            srcintf=srcintf,
            dstintf=dstintf,
            nat64=nat64,
            nat46=nat46,
            ztna_status=ztna_status,
            ztna_device_ownership=ztna_device_ownership,
            srcaddr=srcaddr,
            dstaddr=dstaddr,
            srcaddr6=srcaddr6,
            dstaddr6=dstaddr6,
            ztna_ems_tag=ztna_ems_tag,
            ztna_ems_tag_secondary=ztna_ems_tag_secondary,
            ztna_tags_match_logic=ztna_tags_match_logic,
            ztna_geo_tag=ztna_geo_tag,
            internet_service=internet_service,
            internet_service_name=internet_service_name,
            internet_service_group=internet_service_group,
            internet_service_custom=internet_service_custom,
            network_service_dynamic=network_service_dynamic,
            internet_service_custom_group=internet_service_custom_group,
            internet_service_src=internet_service_src,
            internet_service_src_name=internet_service_src_name,
            internet_service_src_group=internet_service_src_group,
            internet_service_src_custom=internet_service_src_custom,
            network_service_src_dynamic=network_service_src_dynamic,
            internet_service_src_custom_group=internet_service_src_custom_group,
            reputation_minimum=reputation_minimum,
            reputation_direction=reputation_direction,
            src_vendor_mac=src_vendor_mac,
            internet_service6=internet_service6,
            internet_service6_name=internet_service6_name,
            internet_service6_group=internet_service6_group,
            internet_service6_custom=internet_service6_custom,
            internet_service6_custom_group=internet_service6_custom_group,
            internet_service6_src=internet_service6_src,
            internet_service6_src_name=internet_service6_src_name,
            internet_service6_src_group=internet_service6_src_group,
            internet_service6_src_custom=internet_service6_src_custom,
            internet_service6_src_custom_group=internet_service6_src_custom_group,
            reputation_minimum6=reputation_minimum6,
            reputation_direction6=reputation_direction6,
            rtp_nat=rtp_nat,
            rtp_addr=rtp_addr,
            send_deny_packet=send_deny_packet,
            firewall_session_dirty=firewall_session_dirty,
            schedule=schedule,
            schedule_timeout=schedule_timeout,
            policy_expiry=policy_expiry,
            policy_expiry_date=policy_expiry_date,
            policy_expiry_date_utc=policy_expiry_date_utc,
            service=service,
            tos_mask=tos_mask,
            tos=tos,
            tos_negate=tos_negate,
            anti_replay=anti_replay,
            tcp_session_without_syn=tcp_session_without_syn,
            geoip_anycast=geoip_anycast,
            geoip_match=geoip_match,
            dynamic_shaping=dynamic_shaping,
            passive_wan_health_measurement=passive_wan_health_measurement,
            app_monitor=app_monitor,
            utm_status=utm_status,
            inspection_mode=inspection_mode,
            http_policy_redirect=http_policy_redirect,
            ssh_policy_redirect=ssh_policy_redirect,
            ztna_policy_redirect=ztna_policy_redirect,
            webproxy_profile=webproxy_profile,
            profile_type=profile_type,
            profile_group=profile_group,
            profile_protocol_options=profile_protocol_options,
            ssl_ssh_profile=ssl_ssh_profile,
            av_profile=av_profile,
            webfilter_profile=webfilter_profile,
            dnsfilter_profile=dnsfilter_profile,
            emailfilter_profile=emailfilter_profile,
            dlp_profile=dlp_profile,
            file_filter_profile=file_filter_profile,
            ips_sensor=ips_sensor,
            application_list=application_list,
            voip_profile=voip_profile,
            ips_voip_filter=ips_voip_filter,
            sctp_filter_profile=sctp_filter_profile,
            diameter_filter_profile=diameter_filter_profile,
            virtual_patch_profile=virtual_patch_profile,
            icap_profile=icap_profile,
            videofilter_profile=videofilter_profile,
            waf_profile=waf_profile,
            ssh_filter_profile=ssh_filter_profile,
            casb_profile=casb_profile,
            logtraffic=logtraffic,
            logtraffic_start=logtraffic_start,
            log_http_transaction=log_http_transaction,
            capture_packet=capture_packet,
            auto_asic_offload=auto_asic_offload,
            np_acceleration=np_acceleration,
            webproxy_forward_server=webproxy_forward_server,
            traffic_shaper=traffic_shaper,
            traffic_shaper_reverse=traffic_shaper_reverse,
            per_ip_shaper=per_ip_shaper,
            nat=nat,
            pcp_outbound=pcp_outbound,
            pcp_inbound=pcp_inbound,
            pcp_poolname=pcp_poolname,
            permit_any_host=permit_any_host,
            permit_stun_host=permit_stun_host,
            fixedport=fixedport,
            port_preserve=port_preserve,
            port_random=port_random,
            ippool=ippool,
            poolname=poolname,
            poolname6=poolname6,
            session_ttl=session_ttl,
            vlan_cos_fwd=vlan_cos_fwd,
            vlan_cos_rev=vlan_cos_rev,
            inbound=inbound,
            outbound=outbound,
            natinbound=natinbound,
            natoutbound=natoutbound,
            fec=fec,
            wccp=wccp,
            ntlm=ntlm,
            ntlm_guest=ntlm_guest,
            ntlm_enabled_browsers=ntlm_enabled_browsers,
            fsso_agent_for_ntlm=fsso_agent_for_ntlm,
            groups=groups,
            users=users,
            fsso_groups=fsso_groups,
            auth_path=auth_path,
            disclaimer=disclaimer,
            email_collect=email_collect,
            vpntunnel=vpntunnel,
            natip=natip,
            match_vip=match_vip,
            match_vip_only=match_vip_only,
            diffserv_copy=diffserv_copy,
            diffserv_forward=diffserv_forward,
            diffserv_reverse=diffserv_reverse,
            diffservcode_forward=diffservcode_forward,
            diffservcode_rev=diffservcode_rev,
            tcp_mss_sender=tcp_mss_sender,
            tcp_mss_receiver=tcp_mss_receiver,
            comments=comments,
            auth_cert=auth_cert,
            auth_redirect_addr=auth_redirect_addr,
            redirect_url=redirect_url,
            identity_based_route=identity_based_route,
            block_notification=block_notification,
            custom_log_fields=custom_log_fields,
            replacemsg_override_group=replacemsg_override_group,
            srcaddr_negate=srcaddr_negate,
            srcaddr6_negate=srcaddr6_negate,
            dstaddr_negate=dstaddr_negate,
            dstaddr6_negate=dstaddr6_negate,
            ztna_ems_tag_negate=ztna_ems_tag_negate,
            service_negate=service_negate,
            internet_service_negate=internet_service_negate,
            internet_service_src_negate=internet_service_src_negate,
            internet_service6_negate=internet_service6_negate,
            internet_service6_src_negate=internet_service6_src_negate,
            timeout_send_rst=timeout_send_rst,
            captive_portal_exempt=captive_portal_exempt,
            decrypted_traffic_mirror=decrypted_traffic_mirror,
            dsri=dsri,
            radius_mac_auth_bypass=radius_mac_auth_bypass,
            radius_ip_auth_bypass=radius_ip_auth_bypass,
            delay_tcp_npu_session=delay_tcp_npu_session,
            vlan_filter=vlan_filter,
            sgt_check=sgt_check,
            sgt=sgt,
            internet_service_fortiguard=internet_service_fortiguard,
            internet_service_src_fortiguard=internet_service_src_fortiguard,
            internet_service6_fortiguard=internet_service6_fortiguard,
            internet_service6_src_fortiguard=internet_service6_src_fortiguard,
        )

        # Merge with data_payload and kwargs
        data_payload.update(policy_params)
        data_payload.update(kwargs)

        return self._client.put(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )

    def delete(
        self,
        policyid: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Delete this specific resource.

        Args:
            policyid: Object identifier (required)
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
        if not policyid:
            raise ValueError("policyid is required for delete()")
        endpoint = f"/firewall/policy/{policyid}"
        params.update(kwargs)
        return self._client.delete(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )

    def exists(
        self,
        policyid: str,
        vdom: str | bool | None = None,
    ) -> Union[bool, Coroutine[Any, Any, bool]]:
        """
        Check if an object exists.

        Args:
            policyid: Object identifier
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
        result = self.get(policyid=policyid, vdom=vdom)

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
        policyid: int | None = None,
        status: str | None = None,
        name: str | None = None,
        uuid: str | None = None,
        srcintf: list | None = None,
        dstintf: list | None = None,
        nat64: str | None = None,
        nat46: str | None = None,
        ztna_status: str | None = None,
        ztna_device_ownership: str | None = None,
        srcaddr: list | None = None,
        dstaddr: list | None = None,
        srcaddr6: list | None = None,
        dstaddr6: list | None = None,
        ztna_ems_tag: list | None = None,
        ztna_ems_tag_secondary: list | None = None,
        ztna_tags_match_logic: str | None = None,
        ztna_geo_tag: list | None = None,
        internet_service: str | None = None,
        internet_service_name: list | None = None,
        internet_service_group: list | None = None,
        internet_service_custom: list | None = None,
        network_service_dynamic: list | None = None,
        internet_service_custom_group: list | None = None,
        internet_service_src: str | None = None,
        internet_service_src_name: list | None = None,
        internet_service_src_group: list | None = None,
        internet_service_src_custom: list | None = None,
        network_service_src_dynamic: list | None = None,
        internet_service_src_custom_group: list | None = None,
        reputation_minimum: int | None = None,
        reputation_direction: str | None = None,
        src_vendor_mac: list | None = None,
        internet_service6: str | None = None,
        internet_service6_name: list | None = None,
        internet_service6_group: list | None = None,
        internet_service6_custom: list | None = None,
        internet_service6_custom_group: list | None = None,
        internet_service6_src: str | None = None,
        internet_service6_src_name: list | None = None,
        internet_service6_src_group: list | None = None,
        internet_service6_src_custom: list | None = None,
        internet_service6_src_custom_group: list | None = None,
        reputation_minimum6: int | None = None,
        reputation_direction6: str | None = None,
        rtp_nat: str | None = None,
        rtp_addr: list | None = None,
        send_deny_packet: str | None = None,
        firewall_session_dirty: str | None = None,
        schedule: str | None = None,
        schedule_timeout: str | None = None,
        policy_expiry: str | None = None,
        policy_expiry_date: str | None = None,
        policy_expiry_date_utc: str | None = None,
        service: list | None = None,
        tos_mask: str | None = None,
        tos: str | None = None,
        tos_negate: str | None = None,
        anti_replay: str | None = None,
        tcp_session_without_syn: str | None = None,
        geoip_anycast: str | None = None,
        geoip_match: str | None = None,
        dynamic_shaping: str | None = None,
        passive_wan_health_measurement: str | None = None,
        app_monitor: str | None = None,
        utm_status: str | None = None,
        inspection_mode: str | None = None,
        http_policy_redirect: str | None = None,
        ssh_policy_redirect: str | None = None,
        ztna_policy_redirect: str | None = None,
        webproxy_profile: str | None = None,
        profile_type: str | None = None,
        profile_group: str | None = None,
        profile_protocol_options: str | None = None,
        ssl_ssh_profile: str | None = None,
        av_profile: str | None = None,
        webfilter_profile: str | None = None,
        dnsfilter_profile: str | None = None,
        emailfilter_profile: str | None = None,
        dlp_profile: str | None = None,
        file_filter_profile: str | None = None,
        ips_sensor: str | None = None,
        application_list: str | None = None,
        voip_profile: str | None = None,
        ips_voip_filter: str | None = None,
        sctp_filter_profile: str | None = None,
        diameter_filter_profile: str | None = None,
        virtual_patch_profile: str | None = None,
        icap_profile: str | None = None,
        videofilter_profile: str | None = None,
        waf_profile: str | None = None,
        ssh_filter_profile: str | None = None,
        casb_profile: str | None = None,
        logtraffic: str | None = None,
        logtraffic_start: str | None = None,
        log_http_transaction: str | None = None,
        capture_packet: str | None = None,
        auto_asic_offload: str | None = None,
        np_acceleration: str | None = None,
        webproxy_forward_server: str | None = None,
        traffic_shaper: str | None = None,
        traffic_shaper_reverse: str | None = None,
        per_ip_shaper: str | None = None,
        nat: str | None = None,
        pcp_outbound: str | None = None,
        pcp_inbound: str | None = None,
        pcp_poolname: list | None = None,
        permit_any_host: str | None = None,
        permit_stun_host: str | None = None,
        fixedport: str | None = None,
        port_preserve: str | None = None,
        port_random: str | None = None,
        ippool: str | None = None,
        poolname: list | None = None,
        poolname6: list | None = None,
        session_ttl: str | None = None,
        vlan_cos_fwd: int | None = None,
        vlan_cos_rev: int | None = None,
        inbound: str | None = None,
        outbound: str | None = None,
        natinbound: str | None = None,
        natoutbound: str | None = None,
        fec: str | None = None,
        wccp: str | None = None,
        ntlm: str | None = None,
        ntlm_guest: str | None = None,
        ntlm_enabled_browsers: list | None = None,
        fsso_agent_for_ntlm: str | None = None,
        groups: list | None = None,
        users: list | None = None,
        fsso_groups: list | None = None,
        auth_path: str | None = None,
        disclaimer: str | None = None,
        email_collect: str | None = None,
        vpntunnel: str | None = None,
        natip: str | None = None,
        match_vip: str | None = None,
        match_vip_only: str | None = None,
        diffserv_copy: str | None = None,
        diffserv_forward: str | None = None,
        diffserv_reverse: str | None = None,
        diffservcode_forward: str | None = None,
        diffservcode_rev: str | None = None,
        tcp_mss_sender: int | None = None,
        tcp_mss_receiver: int | None = None,
        comments: str | None = None,
        auth_cert: str | None = None,
        auth_redirect_addr: str | None = None,
        redirect_url: str | None = None,
        identity_based_route: str | None = None,
        block_notification: str | None = None,
        custom_log_fields: list | None = None,
        replacemsg_override_group: str | None = None,
        srcaddr_negate: str | None = None,
        srcaddr6_negate: str | None = None,
        dstaddr_negate: str | None = None,
        dstaddr6_negate: str | None = None,
        ztna_ems_tag_negate: str | None = None,
        service_negate: str | None = None,
        internet_service_negate: str | None = None,
        internet_service_src_negate: str | None = None,
        internet_service6_negate: str | None = None,
        internet_service6_src_negate: str | None = None,
        timeout_send_rst: str | None = None,
        captive_portal_exempt: str | None = None,
        decrypted_traffic_mirror: str | None = None,
        dsri: str | None = None,
        radius_mac_auth_bypass: str | None = None,
        radius_ip_auth_bypass: str | None = None,
        delay_tcp_npu_session: str | None = None,
        vlan_filter: str | None = None,
        sgt_check: str | None = None,
        sgt: list | None = None,
        internet_service_fortiguard: list | None = None,
        internet_service_src_fortiguard: list | None = None,
        internet_service6_fortiguard: list | None = None,
        internet_service6_src_fortiguard: list | None = None,
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
            policyid: Policy ID (0 - 4294967294). (optional)
            status: Enable or disable this policy. (optional)
            name: Policy name. (optional)
            uuid: Universally Unique Identifier (UUID; automatically assigned
            but can be manually reset). (optional)
            srcintf: Incoming (ingress) interface. (optional)
            dstintf: Outgoing (egress) interface. (optional)
            nat64: Enable/disable NAT64. (optional)
            nat46: Enable/disable NAT46. (optional)
            ztna_status: Enable/disable zero trust access. (optional)
            ztna_device_ownership: Enable/disable zero trust device ownership.
            (optional)
            srcaddr: Source IPv4 address and address group names. (optional)
            dstaddr: Destination IPv4 address and address group names.
            (optional)
            srcaddr6: Source IPv6 address name and address group names.
            (optional)
            dstaddr6: Destination IPv6 address name and address group names.
            (optional)
            ztna_ems_tag: Source ztna-ems-tag names. (optional)
            ztna_ems_tag_secondary: Source ztna-ems-tag-secondary names.
            (optional)
            ztna_tags_match_logic: ZTNA tag matching logic. (optional)
            ztna_geo_tag: Source ztna-geo-tag names. (optional)
            internet_service: Enable/disable use of Internet Services for this
            policy. If enabled, destination address and service are not used.
            (optional)
            internet_service_name: Internet Service name. (optional)
            internet_service_group: Internet Service group name. (optional)
            internet_service_custom: Custom Internet Service name. (optional)
            network_service_dynamic: Dynamic Network Service name. (optional)
            internet_service_custom_group: Custom Internet Service group name.
            (optional)
            internet_service_src: Enable/disable use of Internet Services in
            source for this policy. If enabled, source address is not used.
            (optional)
            internet_service_src_name: Internet Service source name. (optional)
            internet_service_src_group: Internet Service source group name.
            (optional)
            internet_service_src_custom: Custom Internet Service source name.
            (optional)
            network_service_src_dynamic: Dynamic Network Service source name.
            (optional)
            internet_service_src_custom_group: Custom Internet Service source
            group name. (optional)
            reputation_minimum: Minimum Reputation to take action. (optional)
            reputation_direction: Direction of the initial traffic for
            reputation to take effect. (optional)
            src_vendor_mac: Vendor MAC source ID. (optional)
            internet_service6: Enable/disable use of IPv6 Internet Services for
            this policy. If enabled, destination address and service are not
            used. (optional)
            internet_service6_name: IPv6 Internet Service name. (optional)
            internet_service6_group: Internet Service group name. (optional)
            internet_service6_custom: Custom IPv6 Internet Service name.
            (optional)
            internet_service6_custom_group: Custom Internet Service6 group
            name. (optional)
            internet_service6_src: Enable/disable use of IPv6 Internet Services
            in source for this policy. If enabled, source address is not used.
            (optional)
            internet_service6_src_name: IPv6 Internet Service source name.
            (optional)
            internet_service6_src_group: Internet Service6 source group name.
            (optional)
            internet_service6_src_custom: Custom IPv6 Internet Service source
            name. (optional)
            internet_service6_src_custom_group: Custom Internet Service6 source
            group name. (optional)
            reputation_minimum6: IPv6 Minimum Reputation to take action.
            (optional)
            reputation_direction6: Direction of the initial traffic for IPv6
            reputation to take effect. (optional)
            rtp_nat: Enable Real Time Protocol (RTP) NAT. (optional)
            rtp_addr: Address names if this is an RTP NAT policy. (optional)
            send_deny_packet: Enable to send a reply when a session is denied
            or blocked by a firewall policy. (optional)
            firewall_session_dirty: How to handle sessions if the configuration
            of this firewall policy changes. (optional)
            schedule: Schedule name. (optional)
            schedule_timeout: Enable to force current sessions to end when the
            schedule object times out. Disable allows them to end from
            inactivity. (optional)
            policy_expiry: Enable/disable policy expiry. (optional)
            policy_expiry_date: Policy expiry date (YYYY-MM-DD HH:MM:SS).
            (optional)
            policy_expiry_date_utc: Policy expiry date and time, in epoch
            format. (optional)
            service: Service and service group names. (optional)
            tos_mask: Non-zero bit positions are used for comparison while zero
            bit positions are ignored. (optional)
            tos: ToS (Type of Service) value used for comparison. (optional)
            tos_negate: Enable negated TOS match. (optional)
            anti_replay: Enable/disable anti-replay check. (optional)
            tcp_session_without_syn: Enable/disable creation of TCP session
            without SYN flag. (optional)
            geoip_anycast: Enable/disable recognition of anycast IP addresses
            using the geography IP database. (optional)
            geoip_match: Match geography address based either on its physical
            location or registered location. (optional)
            dynamic_shaping: Enable/disable dynamic RADIUS defined traffic
            shaping. (optional)
            passive_wan_health_measurement: Enable/disable passive WAN health
            measurement. When enabled, auto-asic-offload is disabled.
            (optional)
            app_monitor: Enable/disable application TCP metrics in session
            logs.When enabled, auto-asic-offload is disabled. (optional)
            utm_status: Enable to add one or more security profiles (AV, IPS,
            etc.) to the firewall policy. (optional)
            inspection_mode: Policy inspection mode (Flow/proxy). Default is
            Flow mode. (optional)
            http_policy_redirect: Redirect HTTP(S) traffic to matching
            transparent web proxy policy. (optional)
            ssh_policy_redirect: Redirect SSH traffic to matching transparent
            proxy policy. (optional)
            ztna_policy_redirect: Redirect ZTNA traffic to matching
            Access-Proxy proxy-policy. (optional)
            webproxy_profile: Webproxy profile name. (optional)
            profile_type: Determine whether the firewall policy allows security
            profile groups or single profiles only. (optional)
            profile_group: Name of profile group. (optional)
            profile_protocol_options: Name of an existing Protocol options
            profile. (optional)
            ssl_ssh_profile: Name of an existing SSL SSH profile. (optional)
            av_profile: Name of an existing Antivirus profile. (optional)
            webfilter_profile: Name of an existing Web filter profile.
            (optional)
            dnsfilter_profile: Name of an existing DNS filter profile.
            (optional)
            emailfilter_profile: Name of an existing email filter profile.
            (optional)
            dlp_profile: Name of an existing DLP profile. (optional)
            file_filter_profile: Name of an existing file-filter profile.
            (optional)
            ips_sensor: Name of an existing IPS sensor. (optional)
            application_list: Name of an existing Application list. (optional)
            voip_profile: Name of an existing VoIP (voipd) profile. (optional)
            ips_voip_filter: Name of an existing VoIP (ips) profile. (optional)
            sctp_filter_profile: Name of an existing SCTP filter profile.
            (optional)
            diameter_filter_profile: Name of an existing Diameter filter
            profile. (optional)
            virtual_patch_profile: Name of an existing virtual-patch profile.
            (optional)
            icap_profile: Name of an existing ICAP profile. (optional)
            videofilter_profile: Name of an existing VideoFilter profile.
            (optional)
            waf_profile: Name of an existing Web application firewall profile.
            (optional)
            ssh_filter_profile: Name of an existing SSH filter profile.
            (optional)
            casb_profile: Name of an existing CASB profile. (optional)
            logtraffic: Enable or disable logging. Log all sessions or security
            profile sessions. (optional)
            logtraffic_start: Record logs when a session starts. (optional)
            log_http_transaction: Enable/disable HTTP transaction log.
            (optional)
            capture_packet: Enable/disable capture packets. (optional)
            auto_asic_offload: Enable/disable policy traffic ASIC offloading.
            (optional)
            np_acceleration: Enable/disable UTM Network Processor acceleration.
            (optional)
            webproxy_forward_server: Webproxy forward server name. (optional)
            traffic_shaper: Traffic shaper. (optional)
            traffic_shaper_reverse: Reverse traffic shaper. (optional)
            per_ip_shaper: Per-IP traffic shaper. (optional)
            nat: Enable/disable source NAT. (optional)
            pcp_outbound: Enable/disable PCP outbound SNAT. (optional)
            pcp_inbound: Enable/disable PCP inbound DNAT. (optional)
            pcp_poolname: PCP pool names. (optional)
            permit_any_host: Enable/disable fullcone NAT. Accept UDP packets
            from any host. (optional)
            permit_stun_host: Accept UDP packets from any Session Traversal
            Utilities for NAT (STUN) host. (optional)
            fixedport: Enable to prevent source NAT from changing a session's
            source port. (optional)
            port_preserve: Enable/disable preservation of the original source
            port from source NAT if it has not been used. (optional)
            port_random: Enable/disable random source port selection for source
            NAT. (optional)
            ippool: Enable to use IP Pools for source NAT. (optional)
            poolname: IP Pool names. (optional)
            poolname6: IPv6 pool names. (optional)
            session_ttl: TTL in seconds for sessions accepted by this policy (0
            means use the system default session TTL). (optional)
            vlan_cos_fwd: VLAN forward direction user priority: 255
            passthrough, 0 lowest, 7 highest. (optional)
            vlan_cos_rev: VLAN reverse direction user priority: 255
            passthrough, 0 lowest, 7 highest. (optional)
            inbound: Policy-based IPsec VPN: only traffic from the remote
            network can initiate a VPN. (optional)
            outbound: Policy-based IPsec VPN: only traffic from the internal
            network can initiate a VPN. (optional)
            natinbound: Policy-based IPsec VPN: apply destination NAT to
            inbound traffic. (optional)
            natoutbound: Policy-based IPsec VPN: apply source NAT to outbound
            traffic. (optional)
            fec: Enable/disable Forward Error Correction on traffic matching
            this policy on a FEC device. (optional)
            wccp: Enable/disable forwarding traffic matching this policy to a
            configured WCCP server. (optional)
            ntlm: Enable/disable NTLM authentication. (optional)
            ntlm_guest: Enable/disable NTLM guest user access. (optional)
            ntlm_enabled_browsers: HTTP-User-Agent value of supported browsers.
            (optional)
            fsso_agent_for_ntlm: FSSO agent to use for NTLM authentication.
            (optional)
            groups: Names of user groups that can authenticate with this
            policy. (optional)
            users: Names of individual users that can authenticate with this
            policy. (optional)
            fsso_groups: Names of FSSO groups. (optional)
            auth_path: Enable/disable authentication-based routing. (optional)
            disclaimer: Enable/disable user authentication disclaimer.
            (optional)
            email_collect: Enable/disable email collection. (optional)
            vpntunnel: Policy-based IPsec VPN: name of the IPsec VPN Phase 1.
            (optional)
            natip: Policy-based IPsec VPN: source NAT IP address for outgoing
            traffic. (optional)
            match_vip: Enable to match packets that have had their destination
            addresses changed by a VIP. (optional)
            match_vip_only: Enable/disable matching of only those packets that
            have had their destination addresses changed by a VIP. (optional)
            diffserv_copy: Enable to copy packet's DiffServ values from
            session's original direction to its reply direction. (optional)
            diffserv_forward: Enable to change packet's DiffServ values to the
            specified diffservcode-forward value. (optional)
            diffserv_reverse: Enable to change packet's reverse (reply)
            DiffServ values to the specified diffservcode-rev value. (optional)
            diffservcode_forward: Change packet's DiffServ to this value.
            (optional)
            diffservcode_rev: Change packet's reverse (reply) DiffServ to this
            value. (optional)
            tcp_mss_sender: Sender TCP maximum segment size (MSS). (optional)
            tcp_mss_receiver: Receiver TCP maximum segment size (MSS).
            (optional)
            comments: Comment. (optional)
            auth_cert: HTTPS server certificate for policy authentication.
            (optional)
            auth_redirect_addr: HTTP-to-HTTPS redirect address for firewall
            authentication. (optional)
            redirect_url: URL users are directed to after seeing and accepting
            the disclaimer or authenticating. (optional)
            identity_based_route: Name of identity-based routing rule.
            (optional)
            block_notification: Enable/disable block notification. (optional)
            custom_log_fields: Custom fields to append to log messages for this
            policy. (optional)
            replacemsg_override_group: Override the default replacement message
            group for this policy. (optional)
            srcaddr_negate: When enabled srcaddr specifies what the source
            address must NOT be. (optional)
            srcaddr6_negate: When enabled srcaddr6 specifies what the source
            address must NOT be. (optional)
            dstaddr_negate: When enabled dstaddr specifies what the destination
            address must NOT be. (optional)
            dstaddr6_negate: When enabled dstaddr6 specifies what the
            destination address must NOT be. (optional)
            ztna_ems_tag_negate: When enabled ztna-ems-tag specifies what the
            tags must NOT be. (optional)
            service_negate: When enabled service specifies what the service
            must NOT be. (optional)
            internet_service_negate: When enabled internet-service specifies
            what the service must NOT be. (optional)
            internet_service_src_negate: When enabled internet-service-src
            specifies what the service must NOT be. (optional)
            internet_service6_negate: When enabled internet-service6 specifies
            what the service must NOT be. (optional)
            internet_service6_src_negate: When enabled internet-service6-src
            specifies what the service must NOT be. (optional)
            timeout_send_rst: Enable/disable sending RST packets when TCP
            sessions expire. (optional)
            captive_portal_exempt: Enable to exempt some users from the captive
            portal. (optional)
            decrypted_traffic_mirror: Decrypted traffic mirror. (optional)
            dsri: Enable DSRI to ignore HTTP server responses. (optional)
            radius_mac_auth_bypass: Enable MAC authentication bypass. The
            bypassed MAC address must be received from RADIUS server.
            (optional)
            radius_ip_auth_bypass: Enable IP authentication bypass. The
            bypassed IP address must be received from RADIUS server. (optional)
            delay_tcp_npu_session: Enable TCP NPU session delay to guarantee
            packet order of 3-way handshake. (optional)
            vlan_filter: VLAN ranges to allow (optional)
            sgt_check: Enable/disable security group tags (SGT) check.
            (optional)
            sgt: Security group tags. (optional)
            internet_service_fortiguard: FortiGuard Internet Service name.
            (optional)
            internet_service_src_fortiguard: FortiGuard Internet Service source
            name. (optional)
            internet_service6_fortiguard: FortiGuard IPv6 Internet Service
            name. (optional)
            internet_service6_src_fortiguard: FortiGuard IPv6 Internet Service
            source name. (optional)
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
        # Start with payload_dict or empty
        data_payload = payload_dict.copy() if payload_dict else {}
        endpoint = "/firewall/policy"

        # Build payload from all parameters using helper function
        policy_params = build_cmdb_payload(
            nkey=nkey,
            policyid=policyid,
            status=status,
            name=name,
            uuid=uuid,
            srcintf=srcintf,
            dstintf=dstintf,
            nat64=nat64,
            nat46=nat46,
            ztna_status=ztna_status,
            ztna_device_ownership=ztna_device_ownership,
            srcaddr=srcaddr,
            dstaddr=dstaddr,
            srcaddr6=srcaddr6,
            dstaddr6=dstaddr6,
            ztna_ems_tag=ztna_ems_tag,
            ztna_ems_tag_secondary=ztna_ems_tag_secondary,
            ztna_tags_match_logic=ztna_tags_match_logic,
            ztna_geo_tag=ztna_geo_tag,
            internet_service=internet_service,
            internet_service_name=internet_service_name,
            internet_service_group=internet_service_group,
            internet_service_custom=internet_service_custom,
            network_service_dynamic=network_service_dynamic,
            internet_service_custom_group=internet_service_custom_group,
            internet_service_src=internet_service_src,
            internet_service_src_name=internet_service_src_name,
            internet_service_src_group=internet_service_src_group,
            internet_service_src_custom=internet_service_src_custom,
            network_service_src_dynamic=network_service_src_dynamic,
            internet_service_src_custom_group=internet_service_src_custom_group,
            reputation_minimum=reputation_minimum,
            reputation_direction=reputation_direction,
            src_vendor_mac=src_vendor_mac,
            internet_service6=internet_service6,
            internet_service6_name=internet_service6_name,
            internet_service6_group=internet_service6_group,
            internet_service6_custom=internet_service6_custom,
            internet_service6_custom_group=internet_service6_custom_group,
            internet_service6_src=internet_service6_src,
            internet_service6_src_name=internet_service6_src_name,
            internet_service6_src_group=internet_service6_src_group,
            internet_service6_src_custom=internet_service6_src_custom,
            internet_service6_src_custom_group=internet_service6_src_custom_group,
            reputation_minimum6=reputation_minimum6,
            reputation_direction6=reputation_direction6,
            rtp_nat=rtp_nat,
            rtp_addr=rtp_addr,
            send_deny_packet=send_deny_packet,
            firewall_session_dirty=firewall_session_dirty,
            schedule=schedule,
            schedule_timeout=schedule_timeout,
            policy_expiry=policy_expiry,
            policy_expiry_date=policy_expiry_date,
            policy_expiry_date_utc=policy_expiry_date_utc,
            service=service,
            tos_mask=tos_mask,
            tos=tos,
            tos_negate=tos_negate,
            anti_replay=anti_replay,
            tcp_session_without_syn=tcp_session_without_syn,
            geoip_anycast=geoip_anycast,
            geoip_match=geoip_match,
            dynamic_shaping=dynamic_shaping,
            passive_wan_health_measurement=passive_wan_health_measurement,
            app_monitor=app_monitor,
            utm_status=utm_status,
            inspection_mode=inspection_mode,
            http_policy_redirect=http_policy_redirect,
            ssh_policy_redirect=ssh_policy_redirect,
            ztna_policy_redirect=ztna_policy_redirect,
            webproxy_profile=webproxy_profile,
            profile_type=profile_type,
            profile_group=profile_group,
            profile_protocol_options=profile_protocol_options,
            ssl_ssh_profile=ssl_ssh_profile,
            av_profile=av_profile,
            webfilter_profile=webfilter_profile,
            dnsfilter_profile=dnsfilter_profile,
            emailfilter_profile=emailfilter_profile,
            dlp_profile=dlp_profile,
            file_filter_profile=file_filter_profile,
            ips_sensor=ips_sensor,
            application_list=application_list,
            voip_profile=voip_profile,
            ips_voip_filter=ips_voip_filter,
            sctp_filter_profile=sctp_filter_profile,
            diameter_filter_profile=diameter_filter_profile,
            virtual_patch_profile=virtual_patch_profile,
            icap_profile=icap_profile,
            videofilter_profile=videofilter_profile,
            waf_profile=waf_profile,
            ssh_filter_profile=ssh_filter_profile,
            casb_profile=casb_profile,
            logtraffic=logtraffic,
            logtraffic_start=logtraffic_start,
            log_http_transaction=log_http_transaction,
            capture_packet=capture_packet,
            auto_asic_offload=auto_asic_offload,
            np_acceleration=np_acceleration,
            webproxy_forward_server=webproxy_forward_server,
            traffic_shaper=traffic_shaper,
            traffic_shaper_reverse=traffic_shaper_reverse,
            per_ip_shaper=per_ip_shaper,
            nat=nat,
            pcp_outbound=pcp_outbound,
            pcp_inbound=pcp_inbound,
            pcp_poolname=pcp_poolname,
            permit_any_host=permit_any_host,
            permit_stun_host=permit_stun_host,
            fixedport=fixedport,
            port_preserve=port_preserve,
            port_random=port_random,
            ippool=ippool,
            poolname=poolname,
            poolname6=poolname6,
            session_ttl=session_ttl,
            vlan_cos_fwd=vlan_cos_fwd,
            vlan_cos_rev=vlan_cos_rev,
            inbound=inbound,
            outbound=outbound,
            natinbound=natinbound,
            natoutbound=natoutbound,
            fec=fec,
            wccp=wccp,
            ntlm=ntlm,
            ntlm_guest=ntlm_guest,
            ntlm_enabled_browsers=ntlm_enabled_browsers,
            fsso_agent_for_ntlm=fsso_agent_for_ntlm,
            groups=groups,
            users=users,
            fsso_groups=fsso_groups,
            auth_path=auth_path,
            disclaimer=disclaimer,
            email_collect=email_collect,
            vpntunnel=vpntunnel,
            natip=natip,
            match_vip=match_vip,
            match_vip_only=match_vip_only,
            diffserv_copy=diffserv_copy,
            diffserv_forward=diffserv_forward,
            diffserv_reverse=diffserv_reverse,
            diffservcode_forward=diffservcode_forward,
            diffservcode_rev=diffservcode_rev,
            tcp_mss_sender=tcp_mss_sender,
            tcp_mss_receiver=tcp_mss_receiver,
            comments=comments,
            auth_cert=auth_cert,
            auth_redirect_addr=auth_redirect_addr,
            redirect_url=redirect_url,
            identity_based_route=identity_based_route,
            block_notification=block_notification,
            custom_log_fields=custom_log_fields,
            replacemsg_override_group=replacemsg_override_group,
            srcaddr_negate=srcaddr_negate,
            srcaddr6_negate=srcaddr6_negate,
            dstaddr_negate=dstaddr_negate,
            dstaddr6_negate=dstaddr6_negate,
            ztna_ems_tag_negate=ztna_ems_tag_negate,
            service_negate=service_negate,
            internet_service_negate=internet_service_negate,
            internet_service_src_negate=internet_service_src_negate,
            internet_service6_negate=internet_service6_negate,
            internet_service6_src_negate=internet_service6_src_negate,
            timeout_send_rst=timeout_send_rst,
            captive_portal_exempt=captive_portal_exempt,
            decrypted_traffic_mirror=decrypted_traffic_mirror,
            dsri=dsri,
            radius_mac_auth_bypass=radius_mac_auth_bypass,
            radius_ip_auth_bypass=radius_ip_auth_bypass,
            delay_tcp_npu_session=delay_tcp_npu_session,
            vlan_filter=vlan_filter,
            sgt_check=sgt_check,
            sgt=sgt,
            internet_service_fortiguard=internet_service_fortiguard,
            internet_service_src_fortiguard=internet_service_src_fortiguard,
            internet_service6_fortiguard=internet_service6_fortiguard,
            internet_service6_src_fortiguard=internet_service6_src_fortiguard,
        )

        # Merge with data_payload and kwargs
        data_payload.update(policy_params)
        data_payload.update(kwargs)

        return self._client.post(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )
