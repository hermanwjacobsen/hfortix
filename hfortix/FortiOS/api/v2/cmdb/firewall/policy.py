"""
FortiOS CMDB - Firewall Policy

API Endpoints:
    GET    /firewall/policy
    POST   /firewall/policy
    GET    /firewall/policy/{policyid}
    PUT    /firewall/policy/{policyid}
    DELETE /firewall/policy/{policyid}
"""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from ....http_client import HTTPClient


class Policy:
    """Policy operations."""

    def __init__(self, client: 'HTTPClient'):
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
    ) -> dict[str, Any]:
        """
        Select a specific entry from a CLI table.
        
        Args:
            policyid: Object identifier (optional for list, required for specific)
            attr: Attribute name that references other table (optional)
            skip_to_datasource: Skip to provided table's Nth entry. E.g {datasource: 'firewall.address', pos: 10, global_entry: false} (optional)
            acs: If true, returned result are in ascending order. (optional)
            search: If present, the objects will be filtered by the search value. (optional)
            vdom: Virtual domain name, or False to skip. Handled by HTTPClient.
            raw_json: If True, return full API response with metadata. If False, return only results.
            **kwargs: Additional query parameters (filter, sort, start, count, format, etc.)
        
        Common Query Parameters (via **kwargs):
            filter: Filter results (e.g., filter='name==value')
            sort: Sort results (e.g., sort='name,asc')
            start: Starting entry index for paging
            count: Maximum number of entries to return
            format: Fields to return (e.g., format='name|type')
            See FortiOS REST API documentation for full list of query parameters
        
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
            params['attr'] = attr
        if skip_to_datasource is not None:
            params['skip_to_datasource'] = skip_to_datasource
        if acs is not None:
            params['acs'] = acs
        if search is not None:
            params['search'] = search
        params.update(kwargs)
        return self._client.get("cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json)

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
    ) -> dict[str, Any]:
        """
        Update this specific resource.
        
        Args:
            payload_dict: Optional dictionary of all parameters (can be passed as first positional arg)
            policyid: Object identifier (required)
            before: If *action=move*, use *before* to specify the ID of the resource that this resource will be moved before. (optional)
            after: If *action=move*, use *after* to specify the ID of the resource that this resource will be moved after. (optional)
            policyid: Policy ID (0 - 4294967294). (optional)
            status: Enable or disable this policy. (optional)
            name: Policy name. (optional)
            uuid: Universally Unique Identifier (UUID; automatically assigned but can be manually reset). (optional)
            srcintf: Incoming (ingress) interface. (optional)
            dstintf: Outgoing (egress) interface. (optional)
            nat64: Enable/disable NAT64. (optional)
            nat46: Enable/disable NAT46. (optional)
            ztna_status: Enable/disable zero trust access. (optional)
            ztna_device_ownership: Enable/disable zero trust device ownership. (optional)
            srcaddr: Source IPv4 address and address group names. (optional)
            dstaddr: Destination IPv4 address and address group names. (optional)
            srcaddr6: Source IPv6 address name and address group names. (optional)
            dstaddr6: Destination IPv6 address name and address group names. (optional)
            ztna_ems_tag: Source ztna-ems-tag names. (optional)
            ztna_ems_tag_secondary: Source ztna-ems-tag-secondary names. (optional)
            ztna_tags_match_logic: ZTNA tag matching logic. (optional)
            ztna_geo_tag: Source ztna-geo-tag names. (optional)
            internet_service: Enable/disable use of Internet Services for this policy. If enabled, destination address and service are not used. (optional)
            internet_service_name: Internet Service name. (optional)
            internet_service_group: Internet Service group name. (optional)
            internet_service_custom: Custom Internet Service name. (optional)
            network_service_dynamic: Dynamic Network Service name. (optional)
            internet_service_custom_group: Custom Internet Service group name. (optional)
            internet_service_src: Enable/disable use of Internet Services in source for this policy. If enabled, source address is not used. (optional)
            internet_service_src_name: Internet Service source name. (optional)
            internet_service_src_group: Internet Service source group name. (optional)
            internet_service_src_custom: Custom Internet Service source name. (optional)
            network_service_src_dynamic: Dynamic Network Service source name. (optional)
            internet_service_src_custom_group: Custom Internet Service source group name. (optional)
            reputation_minimum: Minimum Reputation to take action. (optional)
            reputation_direction: Direction of the initial traffic for reputation to take effect. (optional)
            src_vendor_mac: Vendor MAC source ID. (optional)
            internet_service6: Enable/disable use of IPv6 Internet Services for this policy. If enabled, destination address and service are not used. (optional)
            internet_service6_name: IPv6 Internet Service name. (optional)
            internet_service6_group: Internet Service group name. (optional)
            internet_service6_custom: Custom IPv6 Internet Service name. (optional)
            internet_service6_custom_group: Custom Internet Service6 group name. (optional)
            internet_service6_src: Enable/disable use of IPv6 Internet Services in source for this policy. If enabled, source address is not used. (optional)
            internet_service6_src_name: IPv6 Internet Service source name. (optional)
            internet_service6_src_group: Internet Service6 source group name. (optional)
            internet_service6_src_custom: Custom IPv6 Internet Service source name. (optional)
            internet_service6_src_custom_group: Custom Internet Service6 source group name. (optional)
            reputation_minimum6: IPv6 Minimum Reputation to take action. (optional)
            reputation_direction6: Direction of the initial traffic for IPv6 reputation to take effect. (optional)
            rtp_nat: Enable Real Time Protocol (RTP) NAT. (optional)
            rtp_addr: Address names if this is an RTP NAT policy. (optional)
            send_deny_packet: Enable to send a reply when a session is denied or blocked by a firewall policy. (optional)
            firewall_session_dirty: How to handle sessions if the configuration of this firewall policy changes. (optional)
            schedule: Schedule name. (optional)
            schedule_timeout: Enable to force current sessions to end when the schedule object times out. Disable allows them to end from inactivity. (optional)
            policy_expiry: Enable/disable policy expiry. (optional)
            policy_expiry_date: Policy expiry date (YYYY-MM-DD HH:MM:SS). (optional)
            policy_expiry_date_utc: Policy expiry date and time, in epoch format. (optional)
            service: Service and service group names. (optional)
            tos_mask: Non-zero bit positions are used for comparison while zero bit positions are ignored. (optional)
            tos: ToS (Type of Service) value used for comparison. (optional)
            tos_negate: Enable negated TOS match. (optional)
            anti_replay: Enable/disable anti-replay check. (optional)
            tcp_session_without_syn: Enable/disable creation of TCP session without SYN flag. (optional)
            geoip_anycast: Enable/disable recognition of anycast IP addresses using the geography IP database. (optional)
            geoip_match: Match geography address based either on its physical location or registered location. (optional)
            dynamic_shaping: Enable/disable dynamic RADIUS defined traffic shaping. (optional)
            passive_wan_health_measurement: Enable/disable passive WAN health measurement. When enabled, auto-asic-offload is disabled. (optional)
            app_monitor: Enable/disable application TCP metrics in session logs.When enabled, auto-asic-offload is disabled. (optional)
            utm_status: Enable to add one or more security profiles (AV, IPS, etc.) to the firewall policy. (optional)
            inspection_mode: Policy inspection mode (Flow/proxy). Default is Flow mode. (optional)
            http_policy_redirect: Redirect HTTP(S) traffic to matching transparent web proxy policy. (optional)
            ssh_policy_redirect: Redirect SSH traffic to matching transparent proxy policy. (optional)
            ztna_policy_redirect: Redirect ZTNA traffic to matching Access-Proxy proxy-policy. (optional)
            webproxy_profile: Webproxy profile name. (optional)
            profile_type: Determine whether the firewall policy allows security profile groups or single profiles only. (optional)
            profile_group: Name of profile group. (optional)
            profile_protocol_options: Name of an existing Protocol options profile. (optional)
            ssl_ssh_profile: Name of an existing SSL SSH profile. (optional)
            av_profile: Name of an existing Antivirus profile. (optional)
            webfilter_profile: Name of an existing Web filter profile. (optional)
            dnsfilter_profile: Name of an existing DNS filter profile. (optional)
            emailfilter_profile: Name of an existing email filter profile. (optional)
            dlp_profile: Name of an existing DLP profile. (optional)
            file_filter_profile: Name of an existing file-filter profile. (optional)
            ips_sensor: Name of an existing IPS sensor. (optional)
            application_list: Name of an existing Application list. (optional)
            voip_profile: Name of an existing VoIP (voipd) profile. (optional)
            ips_voip_filter: Name of an existing VoIP (ips) profile. (optional)
            sctp_filter_profile: Name of an existing SCTP filter profile. (optional)
            diameter_filter_profile: Name of an existing Diameter filter profile. (optional)
            virtual_patch_profile: Name of an existing virtual-patch profile. (optional)
            icap_profile: Name of an existing ICAP profile. (optional)
            videofilter_profile: Name of an existing VideoFilter profile. (optional)
            waf_profile: Name of an existing Web application firewall profile. (optional)
            ssh_filter_profile: Name of an existing SSH filter profile. (optional)
            casb_profile: Name of an existing CASB profile. (optional)
            logtraffic: Enable or disable logging. Log all sessions or security profile sessions. (optional)
            logtraffic_start: Record logs when a session starts. (optional)
            log_http_transaction: Enable/disable HTTP transaction log. (optional)
            capture_packet: Enable/disable capture packets. (optional)
            auto_asic_offload: Enable/disable policy traffic ASIC offloading. (optional)
            np_acceleration: Enable/disable UTM Network Processor acceleration. (optional)
            webproxy_forward_server: Webproxy forward server name. (optional)
            traffic_shaper: Traffic shaper. (optional)
            traffic_shaper_reverse: Reverse traffic shaper. (optional)
            per_ip_shaper: Per-IP traffic shaper. (optional)
            nat: Enable/disable source NAT. (optional)
            pcp_outbound: Enable/disable PCP outbound SNAT. (optional)
            pcp_inbound: Enable/disable PCP inbound DNAT. (optional)
            pcp_poolname: PCP pool names. (optional)
            permit_any_host: Enable/disable fullcone NAT. Accept UDP packets from any host. (optional)
            permit_stun_host: Accept UDP packets from any Session Traversal Utilities for NAT (STUN) host. (optional)
            fixedport: Enable to prevent source NAT from changing a session's source port. (optional)
            port_preserve: Enable/disable preservation of the original source port from source NAT if it has not been used. (optional)
            port_random: Enable/disable random source port selection for source NAT. (optional)
            ippool: Enable to use IP Pools for source NAT. (optional)
            poolname: IP Pool names. (optional)
            poolname6: IPv6 pool names. (optional)
            session_ttl: TTL in seconds for sessions accepted by this policy (0 means use the system default session TTL). (optional)
            vlan_cos_fwd: VLAN forward direction user priority: 255 passthrough, 0 lowest, 7 highest. (optional)
            vlan_cos_rev: VLAN reverse direction user priority: 255 passthrough, 0 lowest, 7 highest. (optional)
            inbound: Policy-based IPsec VPN: only traffic from the remote network can initiate a VPN. (optional)
            outbound: Policy-based IPsec VPN: only traffic from the internal network can initiate a VPN. (optional)
            natinbound: Policy-based IPsec VPN: apply destination NAT to inbound traffic. (optional)
            natoutbound: Policy-based IPsec VPN: apply source NAT to outbound traffic. (optional)
            fec: Enable/disable Forward Error Correction on traffic matching this policy on a FEC device. (optional)
            wccp: Enable/disable forwarding traffic matching this policy to a configured WCCP server. (optional)
            ntlm: Enable/disable NTLM authentication. (optional)
            ntlm_guest: Enable/disable NTLM guest user access. (optional)
            ntlm_enabled_browsers: HTTP-User-Agent value of supported browsers. (optional)
            fsso_agent_for_ntlm: FSSO agent to use for NTLM authentication. (optional)
            groups: Names of user groups that can authenticate with this policy. (optional)
            users: Names of individual users that can authenticate with this policy. (optional)
            fsso_groups: Names of FSSO groups. (optional)
            auth_path: Enable/disable authentication-based routing. (optional)
            disclaimer: Enable/disable user authentication disclaimer. (optional)
            email_collect: Enable/disable email collection. (optional)
            vpntunnel: Policy-based IPsec VPN: name of the IPsec VPN Phase 1. (optional)
            natip: Policy-based IPsec VPN: source NAT IP address for outgoing traffic. (optional)
            match_vip: Enable to match packets that have had their destination addresses changed by a VIP. (optional)
            match_vip_only: Enable/disable matching of only those packets that have had their destination addresses changed by a VIP. (optional)
            diffserv_copy: Enable to copy packet's DiffServ values from session's original direction to its reply direction. (optional)
            diffserv_forward: Enable to change packet's DiffServ values to the specified diffservcode-forward value. (optional)
            diffserv_reverse: Enable to change packet's reverse (reply) DiffServ values to the specified diffservcode-rev value. (optional)
            diffservcode_forward: Change packet's DiffServ to this value. (optional)
            diffservcode_rev: Change packet's reverse (reply) DiffServ to this value. (optional)
            tcp_mss_sender: Sender TCP maximum segment size (MSS). (optional)
            tcp_mss_receiver: Receiver TCP maximum segment size (MSS). (optional)
            comments: Comment. (optional)
            auth_cert: HTTPS server certificate for policy authentication. (optional)
            auth_redirect_addr: HTTP-to-HTTPS redirect address for firewall authentication. (optional)
            redirect_url: URL users are directed to after seeing and accepting the disclaimer or authenticating. (optional)
            identity_based_route: Name of identity-based routing rule. (optional)
            block_notification: Enable/disable block notification. (optional)
            custom_log_fields: Custom fields to append to log messages for this policy. (optional)
            replacemsg_override_group: Override the default replacement message group for this policy. (optional)
            srcaddr_negate: When enabled srcaddr specifies what the source address must NOT be. (optional)
            srcaddr6_negate: When enabled srcaddr6 specifies what the source address must NOT be. (optional)
            dstaddr_negate: When enabled dstaddr specifies what the destination address must NOT be. (optional)
            dstaddr6_negate: When enabled dstaddr6 specifies what the destination address must NOT be. (optional)
            ztna_ems_tag_negate: When enabled ztna-ems-tag specifies what the tags must NOT be. (optional)
            service_negate: When enabled service specifies what the service must NOT be. (optional)
            internet_service_negate: When enabled internet-service specifies what the service must NOT be. (optional)
            internet_service_src_negate: When enabled internet-service-src specifies what the service must NOT be. (optional)
            internet_service6_negate: When enabled internet-service6 specifies what the service must NOT be. (optional)
            internet_service6_src_negate: When enabled internet-service6-src specifies what the service must NOT be. (optional)
            timeout_send_rst: Enable/disable sending RST packets when TCP sessions expire. (optional)
            captive_portal_exempt: Enable to exempt some users from the captive portal. (optional)
            decrypted_traffic_mirror: Decrypted traffic mirror. (optional)
            dsri: Enable DSRI to ignore HTTP server responses. (optional)
            radius_mac_auth_bypass: Enable MAC authentication bypass. The bypassed MAC address must be received from RADIUS server. (optional)
            radius_ip_auth_bypass: Enable IP authentication bypass. The bypassed IP address must be received from RADIUS server. (optional)
            delay_tcp_npu_session: Enable TCP NPU session delay to guarantee packet order of 3-way handshake. (optional)
            vlan_filter: VLAN ranges to allow (optional)
            sgt_check: Enable/disable security group tags (SGT) check. (optional)
            sgt: Security group tags. (optional)
            internet_service_fortiguard: FortiGuard Internet Service name. (optional)
            internet_service_src_fortiguard: FortiGuard Internet Service source name. (optional)
            internet_service6_fortiguard: FortiGuard IPv6 Internet Service name. (optional)
            internet_service6_src_fortiguard: FortiGuard IPv6 Internet Service source name. (optional)
            vdom: Virtual domain name, or False to skip. Handled by HTTPClient.
            raw_json: If True, return full API response with metadata. If False, return only results.
            **kwargs: Additional query parameters (filter, sort, start, count, format, etc.)
        
        Common Query Parameters (via **kwargs):
            filter: Filter results (e.g., filter='name==value')
            sort: Sort results (e.g., sort='name,asc')
            start: Starting entry index for paging
            count: Maximum number of entries to return
            format: Fields to return (e.g., format='name|type')
            See FortiOS REST API documentation for full list of query parameters
        
        Returns:
            Dictionary containing API response
        """
        data_payload = payload_dict.copy() if payload_dict else {}
        params = {}
        
        # Build endpoint path
        if not policyid:
            raise ValueError("policyid is required for put()")
        endpoint = f"/firewall/policy/{policyid}"
        if before is not None:
            data_payload['before'] = before
        if after is not None:
            data_payload['after'] = after
        if policyid is not None:
            data_payload['policyid'] = policyid
        if status is not None:
            data_payload['status'] = status
        if name is not None:
            data_payload['name'] = name
        if uuid is not None:
            data_payload['uuid'] = uuid
        if srcintf is not None:
            data_payload['srcintf'] = srcintf
        if dstintf is not None:
            data_payload['dstintf'] = dstintf
        if nat64 is not None:
            data_payload['nat64'] = nat64
        if nat46 is not None:
            data_payload['nat46'] = nat46
        if ztna_status is not None:
            data_payload['ztna-status'] = ztna_status
        if ztna_device_ownership is not None:
            data_payload['ztna-device-ownership'] = ztna_device_ownership
        if srcaddr is not None:
            data_payload['srcaddr'] = srcaddr
        if dstaddr is not None:
            data_payload['dstaddr'] = dstaddr
        if srcaddr6 is not None:
            data_payload['srcaddr6'] = srcaddr6
        if dstaddr6 is not None:
            data_payload['dstaddr6'] = dstaddr6
        if ztna_ems_tag is not None:
            data_payload['ztna-ems-tag'] = ztna_ems_tag
        if ztna_ems_tag_secondary is not None:
            data_payload['ztna-ems-tag-secondary'] = ztna_ems_tag_secondary
        if ztna_tags_match_logic is not None:
            data_payload['ztna-tags-match-logic'] = ztna_tags_match_logic
        if ztna_geo_tag is not None:
            data_payload['ztna-geo-tag'] = ztna_geo_tag
        if internet_service is not None:
            data_payload['internet-service'] = internet_service
        if internet_service_name is not None:
            data_payload['internet-service-name'] = internet_service_name
        if internet_service_group is not None:
            data_payload['internet-service-group'] = internet_service_group
        if internet_service_custom is not None:
            data_payload['internet-service-custom'] = internet_service_custom
        if network_service_dynamic is not None:
            data_payload['network-service-dynamic'] = network_service_dynamic
        if internet_service_custom_group is not None:
            data_payload['internet-service-custom-group'] = internet_service_custom_group
        if internet_service_src is not None:
            data_payload['internet-service-src'] = internet_service_src
        if internet_service_src_name is not None:
            data_payload['internet-service-src-name'] = internet_service_src_name
        if internet_service_src_group is not None:
            data_payload['internet-service-src-group'] = internet_service_src_group
        if internet_service_src_custom is not None:
            data_payload['internet-service-src-custom'] = internet_service_src_custom
        if network_service_src_dynamic is not None:
            data_payload['network-service-src-dynamic'] = network_service_src_dynamic
        if internet_service_src_custom_group is not None:
            data_payload['internet-service-src-custom-group'] = internet_service_src_custom_group
        if reputation_minimum is not None:
            data_payload['reputation-minimum'] = reputation_minimum
        if reputation_direction is not None:
            data_payload['reputation-direction'] = reputation_direction
        if src_vendor_mac is not None:
            data_payload['src-vendor-mac'] = src_vendor_mac
        if internet_service6 is not None:
            data_payload['internet-service6'] = internet_service6
        if internet_service6_name is not None:
            data_payload['internet-service6-name'] = internet_service6_name
        if internet_service6_group is not None:
            data_payload['internet-service6-group'] = internet_service6_group
        if internet_service6_custom is not None:
            data_payload['internet-service6-custom'] = internet_service6_custom
        if internet_service6_custom_group is not None:
            data_payload['internet-service6-custom-group'] = internet_service6_custom_group
        if internet_service6_src is not None:
            data_payload['internet-service6-src'] = internet_service6_src
        if internet_service6_src_name is not None:
            data_payload['internet-service6-src-name'] = internet_service6_src_name
        if internet_service6_src_group is not None:
            data_payload['internet-service6-src-group'] = internet_service6_src_group
        if internet_service6_src_custom is not None:
            data_payload['internet-service6-src-custom'] = internet_service6_src_custom
        if internet_service6_src_custom_group is not None:
            data_payload['internet-service6-src-custom-group'] = internet_service6_src_custom_group
        if reputation_minimum6 is not None:
            data_payload['reputation-minimum6'] = reputation_minimum6
        if reputation_direction6 is not None:
            data_payload['reputation-direction6'] = reputation_direction6
        if rtp_nat is not None:
            data_payload['rtp-nat'] = rtp_nat
        if rtp_addr is not None:
            data_payload['rtp-addr'] = rtp_addr
        if send_deny_packet is not None:
            data_payload['send-deny-packet'] = send_deny_packet
        if firewall_session_dirty is not None:
            data_payload['firewall-session-dirty'] = firewall_session_dirty
        if schedule is not None:
            data_payload['schedule'] = schedule
        if schedule_timeout is not None:
            data_payload['schedule-timeout'] = schedule_timeout
        if policy_expiry is not None:
            data_payload['policy-expiry'] = policy_expiry
        if policy_expiry_date is not None:
            data_payload['policy-expiry-date'] = policy_expiry_date
        if policy_expiry_date_utc is not None:
            data_payload['policy-expiry-date-utc'] = policy_expiry_date_utc
        if service is not None:
            data_payload['service'] = service
        if tos_mask is not None:
            data_payload['tos-mask'] = tos_mask
        if tos is not None:
            data_payload['tos'] = tos
        if tos_negate is not None:
            data_payload['tos-negate'] = tos_negate
        if anti_replay is not None:
            data_payload['anti-replay'] = anti_replay
        if tcp_session_without_syn is not None:
            data_payload['tcp-session-without-syn'] = tcp_session_without_syn
        if geoip_anycast is not None:
            data_payload['geoip-anycast'] = geoip_anycast
        if geoip_match is not None:
            data_payload['geoip-match'] = geoip_match
        if dynamic_shaping is not None:
            data_payload['dynamic-shaping'] = dynamic_shaping
        if passive_wan_health_measurement is not None:
            data_payload['passive-wan-health-measurement'] = passive_wan_health_measurement
        if app_monitor is not None:
            data_payload['app-monitor'] = app_monitor
        if utm_status is not None:
            data_payload['utm-status'] = utm_status
        if inspection_mode is not None:
            data_payload['inspection-mode'] = inspection_mode
        if http_policy_redirect is not None:
            data_payload['http-policy-redirect'] = http_policy_redirect
        if ssh_policy_redirect is not None:
            data_payload['ssh-policy-redirect'] = ssh_policy_redirect
        if ztna_policy_redirect is not None:
            data_payload['ztna-policy-redirect'] = ztna_policy_redirect
        if webproxy_profile is not None:
            data_payload['webproxy-profile'] = webproxy_profile
        if profile_type is not None:
            data_payload['profile-type'] = profile_type
        if profile_group is not None:
            data_payload['profile-group'] = profile_group
        if profile_protocol_options is not None:
            data_payload['profile-protocol-options'] = profile_protocol_options
        if ssl_ssh_profile is not None:
            data_payload['ssl-ssh-profile'] = ssl_ssh_profile
        if av_profile is not None:
            data_payload['av-profile'] = av_profile
        if webfilter_profile is not None:
            data_payload['webfilter-profile'] = webfilter_profile
        if dnsfilter_profile is not None:
            data_payload['dnsfilter-profile'] = dnsfilter_profile
        if emailfilter_profile is not None:
            data_payload['emailfilter-profile'] = emailfilter_profile
        if dlp_profile is not None:
            data_payload['dlp-profile'] = dlp_profile
        if file_filter_profile is not None:
            data_payload['file-filter-profile'] = file_filter_profile
        if ips_sensor is not None:
            data_payload['ips-sensor'] = ips_sensor
        if application_list is not None:
            data_payload['application-list'] = application_list
        if voip_profile is not None:
            data_payload['voip-profile'] = voip_profile
        if ips_voip_filter is not None:
            data_payload['ips-voip-filter'] = ips_voip_filter
        if sctp_filter_profile is not None:
            data_payload['sctp-filter-profile'] = sctp_filter_profile
        if diameter_filter_profile is not None:
            data_payload['diameter-filter-profile'] = diameter_filter_profile
        if virtual_patch_profile is not None:
            data_payload['virtual-patch-profile'] = virtual_patch_profile
        if icap_profile is not None:
            data_payload['icap-profile'] = icap_profile
        if videofilter_profile is not None:
            data_payload['videofilter-profile'] = videofilter_profile
        if waf_profile is not None:
            data_payload['waf-profile'] = waf_profile
        if ssh_filter_profile is not None:
            data_payload['ssh-filter-profile'] = ssh_filter_profile
        if casb_profile is not None:
            data_payload['casb-profile'] = casb_profile
        if logtraffic is not None:
            data_payload['logtraffic'] = logtraffic
        if logtraffic_start is not None:
            data_payload['logtraffic-start'] = logtraffic_start
        if log_http_transaction is not None:
            data_payload['log-http-transaction'] = log_http_transaction
        if capture_packet is not None:
            data_payload['capture-packet'] = capture_packet
        if auto_asic_offload is not None:
            data_payload['auto-asic-offload'] = auto_asic_offload
        if np_acceleration is not None:
            data_payload['np-acceleration'] = np_acceleration
        if webproxy_forward_server is not None:
            data_payload['webproxy-forward-server'] = webproxy_forward_server
        if traffic_shaper is not None:
            data_payload['traffic-shaper'] = traffic_shaper
        if traffic_shaper_reverse is not None:
            data_payload['traffic-shaper-reverse'] = traffic_shaper_reverse
        if per_ip_shaper is not None:
            data_payload['per-ip-shaper'] = per_ip_shaper
        if nat is not None:
            data_payload['nat'] = nat
        if pcp_outbound is not None:
            data_payload['pcp-outbound'] = pcp_outbound
        if pcp_inbound is not None:
            data_payload['pcp-inbound'] = pcp_inbound
        if pcp_poolname is not None:
            data_payload['pcp-poolname'] = pcp_poolname
        if permit_any_host is not None:
            data_payload['permit-any-host'] = permit_any_host
        if permit_stun_host is not None:
            data_payload['permit-stun-host'] = permit_stun_host
        if fixedport is not None:
            data_payload['fixedport'] = fixedport
        if port_preserve is not None:
            data_payload['port-preserve'] = port_preserve
        if port_random is not None:
            data_payload['port-random'] = port_random
        if ippool is not None:
            data_payload['ippool'] = ippool
        if poolname is not None:
            data_payload['poolname'] = poolname
        if poolname6 is not None:
            data_payload['poolname6'] = poolname6
        if session_ttl is not None:
            data_payload['session-ttl'] = session_ttl
        if vlan_cos_fwd is not None:
            data_payload['vlan-cos-fwd'] = vlan_cos_fwd
        if vlan_cos_rev is not None:
            data_payload['vlan-cos-rev'] = vlan_cos_rev
        if inbound is not None:
            data_payload['inbound'] = inbound
        if outbound is not None:
            data_payload['outbound'] = outbound
        if natinbound is not None:
            data_payload['natinbound'] = natinbound
        if natoutbound is not None:
            data_payload['natoutbound'] = natoutbound
        if fec is not None:
            data_payload['fec'] = fec
        if wccp is not None:
            data_payload['wccp'] = wccp
        if ntlm is not None:
            data_payload['ntlm'] = ntlm
        if ntlm_guest is not None:
            data_payload['ntlm-guest'] = ntlm_guest
        if ntlm_enabled_browsers is not None:
            data_payload['ntlm-enabled-browsers'] = ntlm_enabled_browsers
        if fsso_agent_for_ntlm is not None:
            data_payload['fsso-agent-for-ntlm'] = fsso_agent_for_ntlm
        if groups is not None:
            data_payload['groups'] = groups
        if users is not None:
            data_payload['users'] = users
        if fsso_groups is not None:
            data_payload['fsso-groups'] = fsso_groups
        if auth_path is not None:
            data_payload['auth-path'] = auth_path
        if disclaimer is not None:
            data_payload['disclaimer'] = disclaimer
        if email_collect is not None:
            data_payload['email-collect'] = email_collect
        if vpntunnel is not None:
            data_payload['vpntunnel'] = vpntunnel
        if natip is not None:
            data_payload['natip'] = natip
        if match_vip is not None:
            data_payload['match-vip'] = match_vip
        if match_vip_only is not None:
            data_payload['match-vip-only'] = match_vip_only
        if diffserv_copy is not None:
            data_payload['diffserv-copy'] = diffserv_copy
        if diffserv_forward is not None:
            data_payload['diffserv-forward'] = diffserv_forward
        if diffserv_reverse is not None:
            data_payload['diffserv-reverse'] = diffserv_reverse
        if diffservcode_forward is not None:
            data_payload['diffservcode-forward'] = diffservcode_forward
        if diffservcode_rev is not None:
            data_payload['diffservcode-rev'] = diffservcode_rev
        if tcp_mss_sender is not None:
            data_payload['tcp-mss-sender'] = tcp_mss_sender
        if tcp_mss_receiver is not None:
            data_payload['tcp-mss-receiver'] = tcp_mss_receiver
        if comments is not None:
            data_payload['comments'] = comments
        if auth_cert is not None:
            data_payload['auth-cert'] = auth_cert
        if auth_redirect_addr is not None:
            data_payload['auth-redirect-addr'] = auth_redirect_addr
        if redirect_url is not None:
            data_payload['redirect-url'] = redirect_url
        if identity_based_route is not None:
            data_payload['identity-based-route'] = identity_based_route
        if block_notification is not None:
            data_payload['block-notification'] = block_notification
        if custom_log_fields is not None:
            data_payload['custom-log-fields'] = custom_log_fields
        if replacemsg_override_group is not None:
            data_payload['replacemsg-override-group'] = replacemsg_override_group
        if srcaddr_negate is not None:
            data_payload['srcaddr-negate'] = srcaddr_negate
        if srcaddr6_negate is not None:
            data_payload['srcaddr6-negate'] = srcaddr6_negate
        if dstaddr_negate is not None:
            data_payload['dstaddr-negate'] = dstaddr_negate
        if dstaddr6_negate is not None:
            data_payload['dstaddr6-negate'] = dstaddr6_negate
        if ztna_ems_tag_negate is not None:
            data_payload['ztna-ems-tag-negate'] = ztna_ems_tag_negate
        if service_negate is not None:
            data_payload['service-negate'] = service_negate
        if internet_service_negate is not None:
            data_payload['internet-service-negate'] = internet_service_negate
        if internet_service_src_negate is not None:
            data_payload['internet-service-src-negate'] = internet_service_src_negate
        if internet_service6_negate is not None:
            data_payload['internet-service6-negate'] = internet_service6_negate
        if internet_service6_src_negate is not None:
            data_payload['internet-service6-src-negate'] = internet_service6_src_negate
        if timeout_send_rst is not None:
            data_payload['timeout-send-rst'] = timeout_send_rst
        if captive_portal_exempt is not None:
            data_payload['captive-portal-exempt'] = captive_portal_exempt
        if decrypted_traffic_mirror is not None:
            data_payload['decrypted-traffic-mirror'] = decrypted_traffic_mirror
        if dsri is not None:
            data_payload['dsri'] = dsri
        if radius_mac_auth_bypass is not None:
            data_payload['radius-mac-auth-bypass'] = radius_mac_auth_bypass
        if radius_ip_auth_bypass is not None:
            data_payload['radius-ip-auth-bypass'] = radius_ip_auth_bypass
        if delay_tcp_npu_session is not None:
            data_payload['delay-tcp-npu-session'] = delay_tcp_npu_session
        if vlan_filter is not None:
            data_payload['vlan-filter'] = vlan_filter
        if sgt_check is not None:
            data_payload['sgt-check'] = sgt_check
        if sgt is not None:
            data_payload['sgt'] = sgt
        if internet_service_fortiguard is not None:
            data_payload['internet-service-fortiguard'] = internet_service_fortiguard
        if internet_service_src_fortiguard is not None:
            data_payload['internet-service-src-fortiguard'] = internet_service_src_fortiguard
        if internet_service6_fortiguard is not None:
            data_payload['internet-service6-fortiguard'] = internet_service6_fortiguard
        if internet_service6_src_fortiguard is not None:
            data_payload['internet-service6-src-fortiguard'] = internet_service6_src_fortiguard
        data_payload.update(kwargs)
        return self._client.put("cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json)

    def delete(
        self,
        policyid: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Delete this specific resource.
        
        Args:
            policyid: Object identifier (required)
            vdom: Virtual domain name, or False to skip. Handled by HTTPClient.
            raw_json: If True, return full API response with metadata. If False, return only results.
            **kwargs: Additional query parameters (filter, sort, start, count, format, etc.)
        
        Common Query Parameters (via **kwargs):
            filter: Filter results (e.g., filter='name==value')
            sort: Sort results (e.g., sort='name,asc')
            start: Starting entry index for paging
            count: Maximum number of entries to return
            format: Fields to return (e.g., format='name|type')
            See FortiOS REST API documentation for full list of query parameters
        
        Returns:
            Dictionary containing API response
        """
        params = payload_dict.copy() if payload_dict else {}
        
        # Build endpoint path
        if not policyid:
            raise ValueError("policyid is required for delete()")
        endpoint = f"/firewall/policy/{policyid}"
        params.update(kwargs)
        return self._client.delete("cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json)

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
    ) -> dict[str, Any]:
        """
        Create object(s) in this table.
        
        Args:
            payload_dict: Optional dictionary of all parameters (can be passed as first positional arg)
            nkey: If *action=clone*, use *nkey* to specify the ID for the new resource to be created. (optional)
            policyid: Policy ID (0 - 4294967294). (optional)
            status: Enable or disable this policy. (optional)
            name: Policy name. (optional)
            uuid: Universally Unique Identifier (UUID; automatically assigned but can be manually reset). (optional)
            srcintf: Incoming (ingress) interface. (optional)
            dstintf: Outgoing (egress) interface. (optional)
            nat64: Enable/disable NAT64. (optional)
            nat46: Enable/disable NAT46. (optional)
            ztna_status: Enable/disable zero trust access. (optional)
            ztna_device_ownership: Enable/disable zero trust device ownership. (optional)
            srcaddr: Source IPv4 address and address group names. (optional)
            dstaddr: Destination IPv4 address and address group names. (optional)
            srcaddr6: Source IPv6 address name and address group names. (optional)
            dstaddr6: Destination IPv6 address name and address group names. (optional)
            ztna_ems_tag: Source ztna-ems-tag names. (optional)
            ztna_ems_tag_secondary: Source ztna-ems-tag-secondary names. (optional)
            ztna_tags_match_logic: ZTNA tag matching logic. (optional)
            ztna_geo_tag: Source ztna-geo-tag names. (optional)
            internet_service: Enable/disable use of Internet Services for this policy. If enabled, destination address and service are not used. (optional)
            internet_service_name: Internet Service name. (optional)
            internet_service_group: Internet Service group name. (optional)
            internet_service_custom: Custom Internet Service name. (optional)
            network_service_dynamic: Dynamic Network Service name. (optional)
            internet_service_custom_group: Custom Internet Service group name. (optional)
            internet_service_src: Enable/disable use of Internet Services in source for this policy. If enabled, source address is not used. (optional)
            internet_service_src_name: Internet Service source name. (optional)
            internet_service_src_group: Internet Service source group name. (optional)
            internet_service_src_custom: Custom Internet Service source name. (optional)
            network_service_src_dynamic: Dynamic Network Service source name. (optional)
            internet_service_src_custom_group: Custom Internet Service source group name. (optional)
            reputation_minimum: Minimum Reputation to take action. (optional)
            reputation_direction: Direction of the initial traffic for reputation to take effect. (optional)
            src_vendor_mac: Vendor MAC source ID. (optional)
            internet_service6: Enable/disable use of IPv6 Internet Services for this policy. If enabled, destination address and service are not used. (optional)
            internet_service6_name: IPv6 Internet Service name. (optional)
            internet_service6_group: Internet Service group name. (optional)
            internet_service6_custom: Custom IPv6 Internet Service name. (optional)
            internet_service6_custom_group: Custom Internet Service6 group name. (optional)
            internet_service6_src: Enable/disable use of IPv6 Internet Services in source for this policy. If enabled, source address is not used. (optional)
            internet_service6_src_name: IPv6 Internet Service source name. (optional)
            internet_service6_src_group: Internet Service6 source group name. (optional)
            internet_service6_src_custom: Custom IPv6 Internet Service source name. (optional)
            internet_service6_src_custom_group: Custom Internet Service6 source group name. (optional)
            reputation_minimum6: IPv6 Minimum Reputation to take action. (optional)
            reputation_direction6: Direction of the initial traffic for IPv6 reputation to take effect. (optional)
            rtp_nat: Enable Real Time Protocol (RTP) NAT. (optional)
            rtp_addr: Address names if this is an RTP NAT policy. (optional)
            send_deny_packet: Enable to send a reply when a session is denied or blocked by a firewall policy. (optional)
            firewall_session_dirty: How to handle sessions if the configuration of this firewall policy changes. (optional)
            schedule: Schedule name. (optional)
            schedule_timeout: Enable to force current sessions to end when the schedule object times out. Disable allows them to end from inactivity. (optional)
            policy_expiry: Enable/disable policy expiry. (optional)
            policy_expiry_date: Policy expiry date (YYYY-MM-DD HH:MM:SS). (optional)
            policy_expiry_date_utc: Policy expiry date and time, in epoch format. (optional)
            service: Service and service group names. (optional)
            tos_mask: Non-zero bit positions are used for comparison while zero bit positions are ignored. (optional)
            tos: ToS (Type of Service) value used for comparison. (optional)
            tos_negate: Enable negated TOS match. (optional)
            anti_replay: Enable/disable anti-replay check. (optional)
            tcp_session_without_syn: Enable/disable creation of TCP session without SYN flag. (optional)
            geoip_anycast: Enable/disable recognition of anycast IP addresses using the geography IP database. (optional)
            geoip_match: Match geography address based either on its physical location or registered location. (optional)
            dynamic_shaping: Enable/disable dynamic RADIUS defined traffic shaping. (optional)
            passive_wan_health_measurement: Enable/disable passive WAN health measurement. When enabled, auto-asic-offload is disabled. (optional)
            app_monitor: Enable/disable application TCP metrics in session logs.When enabled, auto-asic-offload is disabled. (optional)
            utm_status: Enable to add one or more security profiles (AV, IPS, etc.) to the firewall policy. (optional)
            inspection_mode: Policy inspection mode (Flow/proxy). Default is Flow mode. (optional)
            http_policy_redirect: Redirect HTTP(S) traffic to matching transparent web proxy policy. (optional)
            ssh_policy_redirect: Redirect SSH traffic to matching transparent proxy policy. (optional)
            ztna_policy_redirect: Redirect ZTNA traffic to matching Access-Proxy proxy-policy. (optional)
            webproxy_profile: Webproxy profile name. (optional)
            profile_type: Determine whether the firewall policy allows security profile groups or single profiles only. (optional)
            profile_group: Name of profile group. (optional)
            profile_protocol_options: Name of an existing Protocol options profile. (optional)
            ssl_ssh_profile: Name of an existing SSL SSH profile. (optional)
            av_profile: Name of an existing Antivirus profile. (optional)
            webfilter_profile: Name of an existing Web filter profile. (optional)
            dnsfilter_profile: Name of an existing DNS filter profile. (optional)
            emailfilter_profile: Name of an existing email filter profile. (optional)
            dlp_profile: Name of an existing DLP profile. (optional)
            file_filter_profile: Name of an existing file-filter profile. (optional)
            ips_sensor: Name of an existing IPS sensor. (optional)
            application_list: Name of an existing Application list. (optional)
            voip_profile: Name of an existing VoIP (voipd) profile. (optional)
            ips_voip_filter: Name of an existing VoIP (ips) profile. (optional)
            sctp_filter_profile: Name of an existing SCTP filter profile. (optional)
            diameter_filter_profile: Name of an existing Diameter filter profile. (optional)
            virtual_patch_profile: Name of an existing virtual-patch profile. (optional)
            icap_profile: Name of an existing ICAP profile. (optional)
            videofilter_profile: Name of an existing VideoFilter profile. (optional)
            waf_profile: Name of an existing Web application firewall profile. (optional)
            ssh_filter_profile: Name of an existing SSH filter profile. (optional)
            casb_profile: Name of an existing CASB profile. (optional)
            logtraffic: Enable or disable logging. Log all sessions or security profile sessions. (optional)
            logtraffic_start: Record logs when a session starts. (optional)
            log_http_transaction: Enable/disable HTTP transaction log. (optional)
            capture_packet: Enable/disable capture packets. (optional)
            auto_asic_offload: Enable/disable policy traffic ASIC offloading. (optional)
            np_acceleration: Enable/disable UTM Network Processor acceleration. (optional)
            webproxy_forward_server: Webproxy forward server name. (optional)
            traffic_shaper: Traffic shaper. (optional)
            traffic_shaper_reverse: Reverse traffic shaper. (optional)
            per_ip_shaper: Per-IP traffic shaper. (optional)
            nat: Enable/disable source NAT. (optional)
            pcp_outbound: Enable/disable PCP outbound SNAT. (optional)
            pcp_inbound: Enable/disable PCP inbound DNAT. (optional)
            pcp_poolname: PCP pool names. (optional)
            permit_any_host: Enable/disable fullcone NAT. Accept UDP packets from any host. (optional)
            permit_stun_host: Accept UDP packets from any Session Traversal Utilities for NAT (STUN) host. (optional)
            fixedport: Enable to prevent source NAT from changing a session's source port. (optional)
            port_preserve: Enable/disable preservation of the original source port from source NAT if it has not been used. (optional)
            port_random: Enable/disable random source port selection for source NAT. (optional)
            ippool: Enable to use IP Pools for source NAT. (optional)
            poolname: IP Pool names. (optional)
            poolname6: IPv6 pool names. (optional)
            session_ttl: TTL in seconds for sessions accepted by this policy (0 means use the system default session TTL). (optional)
            vlan_cos_fwd: VLAN forward direction user priority: 255 passthrough, 0 lowest, 7 highest. (optional)
            vlan_cos_rev: VLAN reverse direction user priority: 255 passthrough, 0 lowest, 7 highest. (optional)
            inbound: Policy-based IPsec VPN: only traffic from the remote network can initiate a VPN. (optional)
            outbound: Policy-based IPsec VPN: only traffic from the internal network can initiate a VPN. (optional)
            natinbound: Policy-based IPsec VPN: apply destination NAT to inbound traffic. (optional)
            natoutbound: Policy-based IPsec VPN: apply source NAT to outbound traffic. (optional)
            fec: Enable/disable Forward Error Correction on traffic matching this policy on a FEC device. (optional)
            wccp: Enable/disable forwarding traffic matching this policy to a configured WCCP server. (optional)
            ntlm: Enable/disable NTLM authentication. (optional)
            ntlm_guest: Enable/disable NTLM guest user access. (optional)
            ntlm_enabled_browsers: HTTP-User-Agent value of supported browsers. (optional)
            fsso_agent_for_ntlm: FSSO agent to use for NTLM authentication. (optional)
            groups: Names of user groups that can authenticate with this policy. (optional)
            users: Names of individual users that can authenticate with this policy. (optional)
            fsso_groups: Names of FSSO groups. (optional)
            auth_path: Enable/disable authentication-based routing. (optional)
            disclaimer: Enable/disable user authentication disclaimer. (optional)
            email_collect: Enable/disable email collection. (optional)
            vpntunnel: Policy-based IPsec VPN: name of the IPsec VPN Phase 1. (optional)
            natip: Policy-based IPsec VPN: source NAT IP address for outgoing traffic. (optional)
            match_vip: Enable to match packets that have had their destination addresses changed by a VIP. (optional)
            match_vip_only: Enable/disable matching of only those packets that have had their destination addresses changed by a VIP. (optional)
            diffserv_copy: Enable to copy packet's DiffServ values from session's original direction to its reply direction. (optional)
            diffserv_forward: Enable to change packet's DiffServ values to the specified diffservcode-forward value. (optional)
            diffserv_reverse: Enable to change packet's reverse (reply) DiffServ values to the specified diffservcode-rev value. (optional)
            diffservcode_forward: Change packet's DiffServ to this value. (optional)
            diffservcode_rev: Change packet's reverse (reply) DiffServ to this value. (optional)
            tcp_mss_sender: Sender TCP maximum segment size (MSS). (optional)
            tcp_mss_receiver: Receiver TCP maximum segment size (MSS). (optional)
            comments: Comment. (optional)
            auth_cert: HTTPS server certificate for policy authentication. (optional)
            auth_redirect_addr: HTTP-to-HTTPS redirect address for firewall authentication. (optional)
            redirect_url: URL users are directed to after seeing and accepting the disclaimer or authenticating. (optional)
            identity_based_route: Name of identity-based routing rule. (optional)
            block_notification: Enable/disable block notification. (optional)
            custom_log_fields: Custom fields to append to log messages for this policy. (optional)
            replacemsg_override_group: Override the default replacement message group for this policy. (optional)
            srcaddr_negate: When enabled srcaddr specifies what the source address must NOT be. (optional)
            srcaddr6_negate: When enabled srcaddr6 specifies what the source address must NOT be. (optional)
            dstaddr_negate: When enabled dstaddr specifies what the destination address must NOT be. (optional)
            dstaddr6_negate: When enabled dstaddr6 specifies what the destination address must NOT be. (optional)
            ztna_ems_tag_negate: When enabled ztna-ems-tag specifies what the tags must NOT be. (optional)
            service_negate: When enabled service specifies what the service must NOT be. (optional)
            internet_service_negate: When enabled internet-service specifies what the service must NOT be. (optional)
            internet_service_src_negate: When enabled internet-service-src specifies what the service must NOT be. (optional)
            internet_service6_negate: When enabled internet-service6 specifies what the service must NOT be. (optional)
            internet_service6_src_negate: When enabled internet-service6-src specifies what the service must NOT be. (optional)
            timeout_send_rst: Enable/disable sending RST packets when TCP sessions expire. (optional)
            captive_portal_exempt: Enable to exempt some users from the captive portal. (optional)
            decrypted_traffic_mirror: Decrypted traffic mirror. (optional)
            dsri: Enable DSRI to ignore HTTP server responses. (optional)
            radius_mac_auth_bypass: Enable MAC authentication bypass. The bypassed MAC address must be received from RADIUS server. (optional)
            radius_ip_auth_bypass: Enable IP authentication bypass. The bypassed IP address must be received from RADIUS server. (optional)
            delay_tcp_npu_session: Enable TCP NPU session delay to guarantee packet order of 3-way handshake. (optional)
            vlan_filter: VLAN ranges to allow (optional)
            sgt_check: Enable/disable security group tags (SGT) check. (optional)
            sgt: Security group tags. (optional)
            internet_service_fortiguard: FortiGuard Internet Service name. (optional)
            internet_service_src_fortiguard: FortiGuard Internet Service source name. (optional)
            internet_service6_fortiguard: FortiGuard IPv6 Internet Service name. (optional)
            internet_service6_src_fortiguard: FortiGuard IPv6 Internet Service source name. (optional)
            vdom: Virtual domain name, or False to skip. Handled by HTTPClient.
            raw_json: If True, return full API response with metadata. If False, return only results.
            **kwargs: Additional query parameters (filter, sort, start, count, format, etc.)
        
        Common Query Parameters (via **kwargs):
            filter: Filter results (e.g., filter='name==value')
            sort: Sort results (e.g., sort='name,asc')
            start: Starting entry index for paging
            count: Maximum number of entries to return
            format: Fields to return (e.g., format='name|type')
            See FortiOS REST API documentation for full list of query parameters
        
        Returns:
            Dictionary containing API response
        """
        data_payload = payload_dict.copy() if payload_dict else {}
        params = {}
        endpoint = "/firewall/policy"
        if nkey is not None:
            data_payload['nkey'] = nkey
        if policyid is not None:
            data_payload['policyid'] = policyid
        if status is not None:
            data_payload['status'] = status
        if name is not None:
            data_payload['name'] = name
        if uuid is not None:
            data_payload['uuid'] = uuid
        if srcintf is not None:
            data_payload['srcintf'] = srcintf
        if dstintf is not None:
            data_payload['dstintf'] = dstintf
        if nat64 is not None:
            data_payload['nat64'] = nat64
        if nat46 is not None:
            data_payload['nat46'] = nat46
        if ztna_status is not None:
            data_payload['ztna-status'] = ztna_status
        if ztna_device_ownership is not None:
            data_payload['ztna-device-ownership'] = ztna_device_ownership
        if srcaddr is not None:
            data_payload['srcaddr'] = srcaddr
        if dstaddr is not None:
            data_payload['dstaddr'] = dstaddr
        if srcaddr6 is not None:
            data_payload['srcaddr6'] = srcaddr6
        if dstaddr6 is not None:
            data_payload['dstaddr6'] = dstaddr6
        if ztna_ems_tag is not None:
            data_payload['ztna-ems-tag'] = ztna_ems_tag
        if ztna_ems_tag_secondary is not None:
            data_payload['ztna-ems-tag-secondary'] = ztna_ems_tag_secondary
        if ztna_tags_match_logic is not None:
            data_payload['ztna-tags-match-logic'] = ztna_tags_match_logic
        if ztna_geo_tag is not None:
            data_payload['ztna-geo-tag'] = ztna_geo_tag
        if internet_service is not None:
            data_payload['internet-service'] = internet_service
        if internet_service_name is not None:
            data_payload['internet-service-name'] = internet_service_name
        if internet_service_group is not None:
            data_payload['internet-service-group'] = internet_service_group
        if internet_service_custom is not None:
            data_payload['internet-service-custom'] = internet_service_custom
        if network_service_dynamic is not None:
            data_payload['network-service-dynamic'] = network_service_dynamic
        if internet_service_custom_group is not None:
            data_payload['internet-service-custom-group'] = internet_service_custom_group
        if internet_service_src is not None:
            data_payload['internet-service-src'] = internet_service_src
        if internet_service_src_name is not None:
            data_payload['internet-service-src-name'] = internet_service_src_name
        if internet_service_src_group is not None:
            data_payload['internet-service-src-group'] = internet_service_src_group
        if internet_service_src_custom is not None:
            data_payload['internet-service-src-custom'] = internet_service_src_custom
        if network_service_src_dynamic is not None:
            data_payload['network-service-src-dynamic'] = network_service_src_dynamic
        if internet_service_src_custom_group is not None:
            data_payload['internet-service-src-custom-group'] = internet_service_src_custom_group
        if reputation_minimum is not None:
            data_payload['reputation-minimum'] = reputation_minimum
        if reputation_direction is not None:
            data_payload['reputation-direction'] = reputation_direction
        if src_vendor_mac is not None:
            data_payload['src-vendor-mac'] = src_vendor_mac
        if internet_service6 is not None:
            data_payload['internet-service6'] = internet_service6
        if internet_service6_name is not None:
            data_payload['internet-service6-name'] = internet_service6_name
        if internet_service6_group is not None:
            data_payload['internet-service6-group'] = internet_service6_group
        if internet_service6_custom is not None:
            data_payload['internet-service6-custom'] = internet_service6_custom
        if internet_service6_custom_group is not None:
            data_payload['internet-service6-custom-group'] = internet_service6_custom_group
        if internet_service6_src is not None:
            data_payload['internet-service6-src'] = internet_service6_src
        if internet_service6_src_name is not None:
            data_payload['internet-service6-src-name'] = internet_service6_src_name
        if internet_service6_src_group is not None:
            data_payload['internet-service6-src-group'] = internet_service6_src_group
        if internet_service6_src_custom is not None:
            data_payload['internet-service6-src-custom'] = internet_service6_src_custom
        if internet_service6_src_custom_group is not None:
            data_payload['internet-service6-src-custom-group'] = internet_service6_src_custom_group
        if reputation_minimum6 is not None:
            data_payload['reputation-minimum6'] = reputation_minimum6
        if reputation_direction6 is not None:
            data_payload['reputation-direction6'] = reputation_direction6
        if rtp_nat is not None:
            data_payload['rtp-nat'] = rtp_nat
        if rtp_addr is not None:
            data_payload['rtp-addr'] = rtp_addr
        if send_deny_packet is not None:
            data_payload['send-deny-packet'] = send_deny_packet
        if firewall_session_dirty is not None:
            data_payload['firewall-session-dirty'] = firewall_session_dirty
        if schedule is not None:
            data_payload['schedule'] = schedule
        if schedule_timeout is not None:
            data_payload['schedule-timeout'] = schedule_timeout
        if policy_expiry is not None:
            data_payload['policy-expiry'] = policy_expiry
        if policy_expiry_date is not None:
            data_payload['policy-expiry-date'] = policy_expiry_date
        if policy_expiry_date_utc is not None:
            data_payload['policy-expiry-date-utc'] = policy_expiry_date_utc
        if service is not None:
            data_payload['service'] = service
        if tos_mask is not None:
            data_payload['tos-mask'] = tos_mask
        if tos is not None:
            data_payload['tos'] = tos
        if tos_negate is not None:
            data_payload['tos-negate'] = tos_negate
        if anti_replay is not None:
            data_payload['anti-replay'] = anti_replay
        if tcp_session_without_syn is not None:
            data_payload['tcp-session-without-syn'] = tcp_session_without_syn
        if geoip_anycast is not None:
            data_payload['geoip-anycast'] = geoip_anycast
        if geoip_match is not None:
            data_payload['geoip-match'] = geoip_match
        if dynamic_shaping is not None:
            data_payload['dynamic-shaping'] = dynamic_shaping
        if passive_wan_health_measurement is not None:
            data_payload['passive-wan-health-measurement'] = passive_wan_health_measurement
        if app_monitor is not None:
            data_payload['app-monitor'] = app_monitor
        if utm_status is not None:
            data_payload['utm-status'] = utm_status
        if inspection_mode is not None:
            data_payload['inspection-mode'] = inspection_mode
        if http_policy_redirect is not None:
            data_payload['http-policy-redirect'] = http_policy_redirect
        if ssh_policy_redirect is not None:
            data_payload['ssh-policy-redirect'] = ssh_policy_redirect
        if ztna_policy_redirect is not None:
            data_payload['ztna-policy-redirect'] = ztna_policy_redirect
        if webproxy_profile is not None:
            data_payload['webproxy-profile'] = webproxy_profile
        if profile_type is not None:
            data_payload['profile-type'] = profile_type
        if profile_group is not None:
            data_payload['profile-group'] = profile_group
        if profile_protocol_options is not None:
            data_payload['profile-protocol-options'] = profile_protocol_options
        if ssl_ssh_profile is not None:
            data_payload['ssl-ssh-profile'] = ssl_ssh_profile
        if av_profile is not None:
            data_payload['av-profile'] = av_profile
        if webfilter_profile is not None:
            data_payload['webfilter-profile'] = webfilter_profile
        if dnsfilter_profile is not None:
            data_payload['dnsfilter-profile'] = dnsfilter_profile
        if emailfilter_profile is not None:
            data_payload['emailfilter-profile'] = emailfilter_profile
        if dlp_profile is not None:
            data_payload['dlp-profile'] = dlp_profile
        if file_filter_profile is not None:
            data_payload['file-filter-profile'] = file_filter_profile
        if ips_sensor is not None:
            data_payload['ips-sensor'] = ips_sensor
        if application_list is not None:
            data_payload['application-list'] = application_list
        if voip_profile is not None:
            data_payload['voip-profile'] = voip_profile
        if ips_voip_filter is not None:
            data_payload['ips-voip-filter'] = ips_voip_filter
        if sctp_filter_profile is not None:
            data_payload['sctp-filter-profile'] = sctp_filter_profile
        if diameter_filter_profile is not None:
            data_payload['diameter-filter-profile'] = diameter_filter_profile
        if virtual_patch_profile is not None:
            data_payload['virtual-patch-profile'] = virtual_patch_profile
        if icap_profile is not None:
            data_payload['icap-profile'] = icap_profile
        if videofilter_profile is not None:
            data_payload['videofilter-profile'] = videofilter_profile
        if waf_profile is not None:
            data_payload['waf-profile'] = waf_profile
        if ssh_filter_profile is not None:
            data_payload['ssh-filter-profile'] = ssh_filter_profile
        if casb_profile is not None:
            data_payload['casb-profile'] = casb_profile
        if logtraffic is not None:
            data_payload['logtraffic'] = logtraffic
        if logtraffic_start is not None:
            data_payload['logtraffic-start'] = logtraffic_start
        if log_http_transaction is not None:
            data_payload['log-http-transaction'] = log_http_transaction
        if capture_packet is not None:
            data_payload['capture-packet'] = capture_packet
        if auto_asic_offload is not None:
            data_payload['auto-asic-offload'] = auto_asic_offload
        if np_acceleration is not None:
            data_payload['np-acceleration'] = np_acceleration
        if webproxy_forward_server is not None:
            data_payload['webproxy-forward-server'] = webproxy_forward_server
        if traffic_shaper is not None:
            data_payload['traffic-shaper'] = traffic_shaper
        if traffic_shaper_reverse is not None:
            data_payload['traffic-shaper-reverse'] = traffic_shaper_reverse
        if per_ip_shaper is not None:
            data_payload['per-ip-shaper'] = per_ip_shaper
        if nat is not None:
            data_payload['nat'] = nat
        if pcp_outbound is not None:
            data_payload['pcp-outbound'] = pcp_outbound
        if pcp_inbound is not None:
            data_payload['pcp-inbound'] = pcp_inbound
        if pcp_poolname is not None:
            data_payload['pcp-poolname'] = pcp_poolname
        if permit_any_host is not None:
            data_payload['permit-any-host'] = permit_any_host
        if permit_stun_host is not None:
            data_payload['permit-stun-host'] = permit_stun_host
        if fixedport is not None:
            data_payload['fixedport'] = fixedport
        if port_preserve is not None:
            data_payload['port-preserve'] = port_preserve
        if port_random is not None:
            data_payload['port-random'] = port_random
        if ippool is not None:
            data_payload['ippool'] = ippool
        if poolname is not None:
            data_payload['poolname'] = poolname
        if poolname6 is not None:
            data_payload['poolname6'] = poolname6
        if session_ttl is not None:
            data_payload['session-ttl'] = session_ttl
        if vlan_cos_fwd is not None:
            data_payload['vlan-cos-fwd'] = vlan_cos_fwd
        if vlan_cos_rev is not None:
            data_payload['vlan-cos-rev'] = vlan_cos_rev
        if inbound is not None:
            data_payload['inbound'] = inbound
        if outbound is not None:
            data_payload['outbound'] = outbound
        if natinbound is not None:
            data_payload['natinbound'] = natinbound
        if natoutbound is not None:
            data_payload['natoutbound'] = natoutbound
        if fec is not None:
            data_payload['fec'] = fec
        if wccp is not None:
            data_payload['wccp'] = wccp
        if ntlm is not None:
            data_payload['ntlm'] = ntlm
        if ntlm_guest is not None:
            data_payload['ntlm-guest'] = ntlm_guest
        if ntlm_enabled_browsers is not None:
            data_payload['ntlm-enabled-browsers'] = ntlm_enabled_browsers
        if fsso_agent_for_ntlm is not None:
            data_payload['fsso-agent-for-ntlm'] = fsso_agent_for_ntlm
        if groups is not None:
            data_payload['groups'] = groups
        if users is not None:
            data_payload['users'] = users
        if fsso_groups is not None:
            data_payload['fsso-groups'] = fsso_groups
        if auth_path is not None:
            data_payload['auth-path'] = auth_path
        if disclaimer is not None:
            data_payload['disclaimer'] = disclaimer
        if email_collect is not None:
            data_payload['email-collect'] = email_collect
        if vpntunnel is not None:
            data_payload['vpntunnel'] = vpntunnel
        if natip is not None:
            data_payload['natip'] = natip
        if match_vip is not None:
            data_payload['match-vip'] = match_vip
        if match_vip_only is not None:
            data_payload['match-vip-only'] = match_vip_only
        if diffserv_copy is not None:
            data_payload['diffserv-copy'] = diffserv_copy
        if diffserv_forward is not None:
            data_payload['diffserv-forward'] = diffserv_forward
        if diffserv_reverse is not None:
            data_payload['diffserv-reverse'] = diffserv_reverse
        if diffservcode_forward is not None:
            data_payload['diffservcode-forward'] = diffservcode_forward
        if diffservcode_rev is not None:
            data_payload['diffservcode-rev'] = diffservcode_rev
        if tcp_mss_sender is not None:
            data_payload['tcp-mss-sender'] = tcp_mss_sender
        if tcp_mss_receiver is not None:
            data_payload['tcp-mss-receiver'] = tcp_mss_receiver
        if comments is not None:
            data_payload['comments'] = comments
        if auth_cert is not None:
            data_payload['auth-cert'] = auth_cert
        if auth_redirect_addr is not None:
            data_payload['auth-redirect-addr'] = auth_redirect_addr
        if redirect_url is not None:
            data_payload['redirect-url'] = redirect_url
        if identity_based_route is not None:
            data_payload['identity-based-route'] = identity_based_route
        if block_notification is not None:
            data_payload['block-notification'] = block_notification
        if custom_log_fields is not None:
            data_payload['custom-log-fields'] = custom_log_fields
        if replacemsg_override_group is not None:
            data_payload['replacemsg-override-group'] = replacemsg_override_group
        if srcaddr_negate is not None:
            data_payload['srcaddr-negate'] = srcaddr_negate
        if srcaddr6_negate is not None:
            data_payload['srcaddr6-negate'] = srcaddr6_negate
        if dstaddr_negate is not None:
            data_payload['dstaddr-negate'] = dstaddr_negate
        if dstaddr6_negate is not None:
            data_payload['dstaddr6-negate'] = dstaddr6_negate
        if ztna_ems_tag_negate is not None:
            data_payload['ztna-ems-tag-negate'] = ztna_ems_tag_negate
        if service_negate is not None:
            data_payload['service-negate'] = service_negate
        if internet_service_negate is not None:
            data_payload['internet-service-negate'] = internet_service_negate
        if internet_service_src_negate is not None:
            data_payload['internet-service-src-negate'] = internet_service_src_negate
        if internet_service6_negate is not None:
            data_payload['internet-service6-negate'] = internet_service6_negate
        if internet_service6_src_negate is not None:
            data_payload['internet-service6-src-negate'] = internet_service6_src_negate
        if timeout_send_rst is not None:
            data_payload['timeout-send-rst'] = timeout_send_rst
        if captive_portal_exempt is not None:
            data_payload['captive-portal-exempt'] = captive_portal_exempt
        if decrypted_traffic_mirror is not None:
            data_payload['decrypted-traffic-mirror'] = decrypted_traffic_mirror
        if dsri is not None:
            data_payload['dsri'] = dsri
        if radius_mac_auth_bypass is not None:
            data_payload['radius-mac-auth-bypass'] = radius_mac_auth_bypass
        if radius_ip_auth_bypass is not None:
            data_payload['radius-ip-auth-bypass'] = radius_ip_auth_bypass
        if delay_tcp_npu_session is not None:
            data_payload['delay-tcp-npu-session'] = delay_tcp_npu_session
        if vlan_filter is not None:
            data_payload['vlan-filter'] = vlan_filter
        if sgt_check is not None:
            data_payload['sgt-check'] = sgt_check
        if sgt is not None:
            data_payload['sgt'] = sgt
        if internet_service_fortiguard is not None:
            data_payload['internet-service-fortiguard'] = internet_service_fortiguard
        if internet_service_src_fortiguard is not None:
            data_payload['internet-service-src-fortiguard'] = internet_service_src_fortiguard
        if internet_service6_fortiguard is not None:
            data_payload['internet-service6-fortiguard'] = internet_service6_fortiguard
        if internet_service6_src_fortiguard is not None:
            data_payload['internet-service6-src-fortiguard'] = internet_service6_src_fortiguard
        data_payload.update(kwargs)
        return self._client.post("cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json)
