"""
Firewall Policy Convenience Wrapper

Provides simplified syntax for firewall policy operations.
Instead of: fgt.api.cmdb.firewall.policy.post(data)
Use: fgt.firewall.policy.create(name='MyPolicy', srcintf=['port1'], ...)
"""

from typing import TYPE_CHECKING, Any, Dict, List, Optional, Union

if TYPE_CHECKING:
    from ..fortios import FortiOS


def _normalize_to_name_list(value: Union[str, List[str], Dict[str, str], List[Dict[str, str]], None]) -> List[Dict[str, str]]:
    """
    Normalize various input formats to FortiOS API format: [{'name': 'value'}, ...]
    
    Args:
        value: Can be:
            - String: 'port1' → [{'name': 'port1'}]
            - List of strings: ['port1', 'port2'] → [{'name': 'port1'}, {'name': 'port2'}]
            - Dict: {'name': 'port1'} → [{'name': 'port1'}]
            - List of dicts: [{'name': 'port1'}, {'name': 'port2'}] → unchanged
            - None: []
    
    Returns:
        List of dicts in FortiOS format
    """
    if value is None:
        return []
    
    # Already a list
    if isinstance(value, list):
        if not value:
            return []
        # If first item is a dict, assume whole list is dicts
        if isinstance(value[0], dict):
            # Filter out empty dicts that sometimes appear in API responses
            return [item for item in value if isinstance(item, dict) and item and 'name' in item]  # type: ignore
        # List of strings
        return [{'name': str(item)} for item in value]
    
    # Single dict
    if isinstance(value, dict):
        return [value] if value and 'name' in value else []
    
    # Single string
    return [{'name': str(value)}]


class FirewallPolicy:
    """Convenience wrapper for firewall policy operations."""
    
    def __init__(self, fortios_instance: "FortiOS"):
        """
        Initialize the FirewallPolicy wrapper.
        
        Args:
            fortios_instance: The parent FortiOS instance
        """
        self._fgt = fortios_instance
        self._api = fortios_instance.api.cmdb.firewall.policy
    
    def create(
        self,
        # Core required parameters
        name: str,
        srcintf: Union[str, List[str]],
        dstintf: Union[str, List[str]],
        srcaddr: Union[str, List[str]],
        dstaddr: Union[str, List[str]],
        # Core optional parameters (no defaults per API spec)
        action: Optional[str] = None,
        schedule: Optional[str] = None,
        service: Optional[Union[str, List[str]]] = None,
        status: Optional[str] = None,
        # IPv6 addresses
        srcaddr6: Optional[Union[str, List[str]]] = None,
        dstaddr6: Optional[Union[str, List[str]]] = None,
        # Internet Services (IPv4) - destination
        internet_service: Optional[str] = None,
        internet_service_name: Optional[Union[str, List[str]]] = None,
        internet_service_group: Optional[Union[str, List[str]]] = None,
        internet_service_custom: Optional[Union[str, List[str]]] = None,
        internet_service_custom_group: Optional[Union[str, List[str]]] = None,
        network_service_dynamic: Optional[Union[str, List[str]]] = None,
        internet_service_fortiguard: Optional[Union[str, List[str]]] = None,
        internet_service_negate: Optional[str] = None,
        # Internet Services (IPv4) - source
        internet_service_src: Optional[str] = None,
        internet_service_src_name: Optional[Union[str, List[str]]] = None,
        internet_service_src_group: Optional[Union[str, List[str]]] = None,
        internet_service_src_custom: Optional[Union[str, List[str]]] = None,
        internet_service_src_custom_group: Optional[Union[str, List[str]]] = None,
        network_service_src_dynamic: Optional[Union[str, List[str]]] = None,
        internet_service_src_fortiguard: Optional[Union[str, List[str]]] = None,
        internet_service_src_negate: Optional[str] = None,
        # Internet Services (IPv6) - destination
        internet_service6: Optional[str] = None,
        internet_service6_name: Optional[Union[str, List[str]]] = None,
        internet_service6_group: Optional[Union[str, List[str]]] = None,
        internet_service6_custom: Optional[Union[str, List[str]]] = None,
        internet_service6_custom_group: Optional[Union[str, List[str]]] = None,
        internet_service6_fortiguard: Optional[Union[str, List[str]]] = None,
        internet_service6_negate: Optional[str] = None,
        # Internet Services (IPv6) - source
        internet_service6_src: Optional[str] = None,
        internet_service6_src_name: Optional[Union[str, List[str]]] = None,
        internet_service6_src_group: Optional[Union[str, List[str]]] = None,
        internet_service6_src_custom: Optional[Union[str, List[str]]] = None,
        internet_service6_src_custom_group: Optional[Union[str, List[str]]] = None,
        internet_service6_src_fortiguard: Optional[Union[str, List[str]]] = None,
        internet_service6_src_negate: Optional[str] = None,
        # Reputation
        reputation_minimum: Optional[int] = None,
        reputation_direction: Optional[str] = None,
        reputation_minimum6: Optional[int] = None,
        reputation_direction6: Optional[str] = None,
        # RTP
        rtp_nat: Optional[str] = None,
        rtp_addr: Optional[Union[str, List[str]]] = None,
        # ZTNA
        ztna_status: Optional[str] = None,
        ztna_device_ownership: Optional[str] = None,
        ztna_ems_tag: Optional[Union[str, List[str]]] = None,
        ztna_ems_tag_secondary: Optional[Union[str, List[str]]] = None,
        ztna_tags_match_logic: Optional[str] = None,
        ztna_geo_tag: Optional[Union[str, List[str]]] = None,
        ztna_ems_tag_negate: Optional[str] = None,
        ztna_policy_redirect: Optional[str] = None,
        # Vendor MAC
        src_vendor_mac: Optional[Union[str, List[str]]] = None,
        # Inspection & UTM
        inspection_mode: Optional[str] = None,
        utm_status: Optional[str] = None,
        profile_type: Optional[str] = None,
        profile_group: Optional[str] = None,
        profile_protocol_options: Optional[str] = None,
        # SSL/SSH & Security Profiles
        ssl_ssh_profile: Optional[str] = None,
        av_profile: Optional[str] = None,
        webfilter_profile: Optional[str] = None,
        dnsfilter_profile: Optional[str] = None,
        emailfilter_profile: Optional[str] = None,
        dlp_profile: Optional[str] = None,
        file_filter_profile: Optional[str] = None,
        ips_sensor: Optional[str] = None,
        application_list: Optional[str] = None,
        voip_profile: Optional[str] = None,
        ips_voip_filter: Optional[str] = None,
        sctp_filter_profile: Optional[str] = None,
        diameter_filter_profile: Optional[str] = None,
        virtual_patch_profile: Optional[str] = None,
        icap_profile: Optional[str] = None,
        videofilter_profile: Optional[str] = None,
        waf_profile: Optional[str] = None,
        ssh_filter_profile: Optional[str] = None,
        casb_profile: Optional[str] = None,
        # Proxy
        http_policy_redirect: Optional[str] = None,
        ssh_policy_redirect: Optional[str] = None,
        webproxy_profile: Optional[str] = None,
        webproxy_forward_server: Optional[str] = None,
        # NAT
        nat: Optional[str] = None,
        nat64: Optional[str] = None,
        nat46: Optional[str] = None,
        ippool: Optional[str] = None,
        poolname: Optional[Union[str, List[str]]] = None,
        poolname6: Optional[Union[str, List[str]]] = None,
        natip: Optional[str] = None,
        fixedport: Optional[str] = None,
        permit_any_host: Optional[str] = None,
        permit_stun_host: Optional[str] = None,
        port_preserve: Optional[str] = None,
        port_random: Optional[str] = None,
        # PCP
        pcp_outbound: Optional[str] = None,
        pcp_inbound: Optional[str] = None,
        pcp_poolname: Optional[Union[str, List[str]]] = None,
        # VPN
        vpntunnel: Optional[str] = None,
        inbound: Optional[str] = None,
        outbound: Optional[str] = None,
        natinbound: Optional[str] = None,
        natoutbound: Optional[str] = None,
        # Users & Authentication
        users: Optional[Union[str, List[str]]] = None,
        groups: Optional[Union[str, List[str]]] = None,
        fsso_groups: Optional[Union[str, List[str]]] = None,
        fsso_agent_for_ntlm: Optional[str] = None,
        ntlm: Optional[str] = None,
        ntlm_guest: Optional[str] = None,
        ntlm_enabled_browsers: Optional[Union[str, List[str]]] = None,
        auth_path: Optional[str] = None,
        auth_cert: Optional[str] = None,
        auth_redirect_addr: Optional[str] = None,
        disclaimer: Optional[str] = None,
        email_collect: Optional[str] = None,
        # Traffic Shaping
        traffic_shaper: Optional[str] = None,
        traffic_shaper_reverse: Optional[str] = None,
        per_ip_shaper: Optional[str] = None,
        # Logging
        logtraffic: Optional[str] = None,
        logtraffic_start: Optional[str] = None,
        log_http_transaction: Optional[str] = None,
        capture_packet: Optional[str] = None,
        custom_log_fields: Optional[Union[str, List[str]]] = None,
        # Advanced features
        wccp: Optional[str] = None,
        passive_wan_health_measurement: Optional[str] = None,
        app_monitor: Optional[str] = None,
        captive_portal_exempt: Optional[str] = None,
        decrypted_traffic_mirror: Optional[str] = None,
        dynamic_shaping: Optional[str] = None,
        fec: Optional[str] = None,
        # Session control
        send_deny_packet: Optional[str] = None,
        firewall_session_dirty: Optional[str] = None,
        schedule_timeout: Optional[str] = None,
        policy_expiry: Optional[str] = None,
        policy_expiry_date: Optional[str] = None,
        policy_expiry_date_utc: Optional[str] = None,
        session_ttl: Optional[str] = None,
        timeout_send_rst: Optional[str] = None,
        # QoS & VLAN
        vlan_cos_fwd: Optional[int] = None,
        vlan_cos_rev: Optional[int] = None,
        vlan_filter: Optional[str] = None,
        diffserv_copy: Optional[str] = None,
        diffserv_forward: Optional[str] = None,
        diffserv_reverse: Optional[str] = None,
        diffservcode_forward: Optional[str] = None,
        diffservcode_rev: Optional[str] = None,
        # TCP/IP
        tcp_mss_sender: Optional[int] = None,
        tcp_mss_receiver: Optional[int] = None,
        tcp_session_without_syn: Optional[str] = None,
        anti_replay: Optional[str] = None,
        tos: Optional[str] = None,
        tos_mask: Optional[str] = None,
        tos_negate: Optional[str] = None,
        # Geo-IP
        geoip_anycast: Optional[str] = None,
        geoip_match: Optional[str] = None,
        # Security Groups
        sgt_check: Optional[str] = None,
        sgt: Optional[Union[str, List[str]]] = None,
        # Performance
        auto_asic_offload: Optional[str] = None,
        np_acceleration: Optional[str] = None,
        delay_tcp_npu_session: Optional[str] = None,
        # VIP matching
        match_vip: Optional[str] = None,
        match_vip_only: Optional[str] = None,
        # RADIUS bypass
        radius_mac_auth_bypass: Optional[str] = None,
        radius_ip_auth_bypass: Optional[str] = None,
        dsri: Optional[str] = None,
        # Identity routing
        identity_based_route: Optional[str] = None,
        # Redirect & Messages
        redirect_url: Optional[str] = None,
        block_notification: Optional[str] = None,
        replacemsg_override_group: Optional[str] = None,
        # Negation options
        srcaddr_negate: Optional[str] = None,
        dstaddr_negate: Optional[str] = None,
        srcaddr6_negate: Optional[str] = None,
        dstaddr6_negate: Optional[str] = None,
        service_negate: Optional[str] = None,
        # Comments
        comments: Optional[str] = None,
        # API parameters
        vdom: Optional[str] = None,
        datasource: Optional[bool] = None,
        with_meta: Optional[bool] = None,
        # Catch-all for any additional fields
        data: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """
        Create a new firewall policy with all available FortiOS parameters.
        
        Args:
            # Core required parameters
            name: Policy name
            srcintf: Source interface(s) - string or list
            dstintf: Destination interface(s) - string or list
            srcaddr: Source address(es) - string or list
            dstaddr: Destination address(es) - string or list
            
            # Core optional parameters (no defaults - FortiOS uses its own defaults)
            action: Policy action ('accept', 'deny', 'ipsec')
            schedule: Schedule name
            service: Service(s) - string or list
            status: Enable/disable policy ('enable', 'disable')
            
            # IPv6 Addresses
            srcaddr6: Source IPv6 address(es) - string or list
            dstaddr6: Destination IPv6 address(es) - string or list
            
            # Internet Services (IPv4) - Destination
            internet_service: Enable/disable Internet Services ('enable', 'disable')
            internet_service_name: Internet Service name(s) - string or list
            internet_service_group: Internet Service group(s) - string or list
            internet_service_custom: Custom Internet Service(s) - string or list
            internet_service_custom_group: Custom Internet Service group(s) - string or list
            network_service_dynamic: Dynamic network service(s) - string or list
            internet_service_fortiguard: FortiGuard Internet Service(s) - string or list
            internet_service_negate: Negate Internet Service match ('enable', 'disable')
            
            # Internet Services (IPv4) - Source
            internet_service_src: Enable/disable source Internet Services ('enable', 'disable')
            internet_service_src_name: Source Internet Service name(s) - string or list
            internet_service_src_group: Source Internet Service group(s) - string or list
            internet_service_src_custom: Source Custom Internet Service(s) - string or list
            internet_service_src_custom_group: Source Custom Internet Service group(s) - string or list
            network_service_src_dynamic: Source dynamic network service(s) - string or list
            internet_service_src_fortiguard: Source FortiGuard Internet Service(s) - string or list
            internet_service_src_negate: Negate source Internet Service match ('enable', 'disable')
            
            # Internet Services (IPv6) - Destination
            internet_service6: Enable/disable IPv6 Internet Services ('enable', 'disable')
            internet_service6_name: IPv6 Internet Service name(s) - string or list
            internet_service6_group: IPv6 Internet Service group(s) - string or list
            internet_service6_custom: IPv6 Custom Internet Service(s) - string or list
            internet_service6_custom_group: IPv6 Custom Internet Service group(s) - string or list
            internet_service6_fortiguard: IPv6 FortiGuard Internet Service(s) - string or list
            internet_service6_negate: Negate IPv6 Internet Service match ('enable', 'disable')
            
            # Internet Services (IPv6) - Source
            internet_service6_src: Enable/disable source IPv6 Internet Services ('enable', 'disable')
            internet_service6_src_name: Source IPv6 Internet Service name(s) - string or list
            internet_service6_src_group: Source IPv6 Internet Service group(s) - string or list
            internet_service6_src_custom: Source IPv6 Custom Internet Service(s) - string or list
            internet_service6_src_custom_group: Source IPv6 Custom Internet Service group(s) - string or list
            internet_service6_src_fortiguard: Source IPv6 FortiGuard Internet Service(s) - string or list
            internet_service6_src_negate: Negate source IPv6 Internet Service match ('enable', 'disable')
            
            # Reputation
            reputation_minimum: Minimum reputation score (0-100)
            reputation_direction: Reputation direction ('source', 'destination')
            reputation_minimum6: Minimum IPv6 reputation score (0-100)
            reputation_direction6: IPv6 reputation direction ('source', 'destination')
            
            # RTP
            rtp_nat: Enable RTP NAT ('enable', 'disable')
            rtp_addr: RTP address(es) - string or list
            
            # ZTNA
            ztna_status: ZTNA status ('enable', 'disable')
            ztna_device_ownership: ZTNA device ownership ('enable', 'disable')
            ztna_ems_tag: ZTNA EMS tag(s) - string or list
            ztna_ems_tag_secondary: ZTNA EMS secondary tag(s) - string or list
            ztna_tags_match_logic: ZTNA tags match logic ('or', 'and')
            ztna_geo_tag: ZTNA geo tag(s) - string or list
            ztna_ems_tag_negate: Negate ZTNA EMS tag match ('enable', 'disable')
            ztna_policy_redirect: ZTNA policy redirect ('enable', 'disable')
            
            # Vendor MAC
            src_vendor_mac: Source vendor MAC address(es) - string or list
            
            # Inspection & UTM
            inspection_mode: Inspection mode ('proxy', 'flow')
            utm_status: UTM status ('enable', 'disable')
            profile_type: Profile type ('single', 'group')
            profile_group: Profile group name
            profile_protocol_options: Protocol options profile name
            
            # SSL/SSH & Security Profiles
            ssl_ssh_profile: SSL/SSH inspection profile name
            av_profile: Antivirus profile name
            webfilter_profile: Web filter profile name
            dnsfilter_profile: DNS filter profile name
            emailfilter_profile: Email filter profile name
            dlp_profile: DLP profile name
            file_filter_profile: File filter profile name
            ips_sensor: IPS sensor name
            application_list: Application control list name
            voip_profile: VoIP profile name
            ips_voip_filter: IPS VoIP filter name
            sctp_filter_profile: SCTP filter profile name
            diameter_filter_profile: Diameter filter profile name
            virtual_patch_profile: Virtual patch profile name
            icap_profile: ICAP profile name
            videofilter_profile: Video filter profile name
            waf_profile: Web application firewall profile name
            ssh_filter_profile: SSH filter profile name
            casb_profile: CASB profile name
            
            # Proxy
            http_policy_redirect: HTTP policy redirect ('enable', 'disable')
            ssh_policy_redirect: SSH policy redirect ('enable', 'disable')
            webproxy_profile: Web proxy profile name
            webproxy_forward_server: Web proxy forward server name
            
            # NAT
            nat: Enable NAT ('enable', 'disable')
            nat64: Enable NAT64 ('enable', 'disable')
            nat46: Enable NAT46 ('enable', 'disable')
            ippool: Enable IP pool ('enable', 'disable')
            poolname: IP pool name(s) - string or list
            poolname6: IPv6 pool name(s) - string or list
            natip: NAT IP address range
            fixedport: Enable fixed port ('enable', 'disable')
            permit_any_host: Permit any host ('enable', 'disable')
            permit_stun_host: Permit STUN host ('enable', 'disable')
            port_preserve: Enable port preserve ('enable', 'disable')
            port_random: Enable port random ('enable', 'disable')
            
            # PCP (Port Control Protocol)
            pcp_outbound: Enable PCP outbound ('enable', 'disable')
            pcp_inbound: Enable PCP inbound ('enable', 'disable')
            pcp_poolname: PCP pool name(s) - string or list
            
            # VPN
            vpntunnel: VPN tunnel name
            inbound: VPN inbound ('enable', 'disable')
            outbound: VPN outbound ('enable', 'disable')
            natinbound: VPN NAT inbound ('enable', 'disable')
            natoutbound: VPN NAT outbound ('enable', 'disable')
            
            # Users & Authentication
            users: User name(s) - string or list
            groups: Group name(s) - string or list
            fsso_groups: FSSO group(s) - string or list
            fsso_agent_for_ntlm: FSSO agent for NTLM
            ntlm: Enable NTLM ('enable', 'disable')
            ntlm_guest: Enable NTLM guest ('enable', 'disable')
            ntlm_enabled_browsers: NTLM enabled browser(s) - string or list
            auth_path: Authentication path ('enable', 'disable')
            auth_cert: Authentication certificate
            auth_redirect_addr: Authentication redirect address
            disclaimer: Disclaimer ('enable', 'disable')
            email_collect: Enable email collection ('enable', 'disable')
            
            # Traffic Shaping
            traffic_shaper: Traffic shaper name
            traffic_shaper_reverse: Reverse traffic shaper name
            per_ip_shaper: Per-IP shaper name
            
            # Logging
            logtraffic: Log traffic ('all', 'utm', 'disable')
            logtraffic_start: Log traffic start ('enable', 'disable')
            log_http_transaction: Log HTTP transaction ('enable', 'disable')
            capture_packet: Capture packet ('enable', 'disable')
            custom_log_fields: Custom log field(s) - string or list
            
            # Advanced Features
            wccp: Enable WCCP ('enable', 'disable')
            passive_wan_health_measurement: Passive WAN health measurement ('enable', 'disable')
            app_monitor: Application monitor ('enable', 'disable')
            captive_portal_exempt: Captive portal exempt ('enable', 'disable')
            decrypted_traffic_mirror: Decrypted traffic mirror name
            dynamic_shaping: Enable dynamic shaping ('enable', 'disable')
            fec: Enable Forward Error Correction ('enable', 'disable')
            
            # Session Control
            send_deny_packet: Send deny packet ('enable', 'disable')
            firewall_session_dirty: Firewall session dirty ('check-all', 'check-new')
            schedule_timeout: Schedule timeout ('enable', 'disable')
            policy_expiry: Policy expiry ('enable', 'disable')
            policy_expiry_date: Policy expiry date
            policy_expiry_date_utc: Policy expiry date UTC
            session_ttl: Session TTL (in seconds)
            timeout_send_rst: Timeout send RST ('enable', 'disable')
            
            # QoS & VLAN
            vlan_cos_fwd: VLAN CoS for forward direction (0-7)
            vlan_cos_rev: VLAN CoS for reverse direction (0-7)
            vlan_filter: VLAN filter
            diffserv_copy: Enable DiffServ copy ('enable', 'disable')
            diffserv_forward: DiffServ forward ('enable', 'disable')
            diffserv_reverse: DiffServ reverse ('enable', 'disable')
            diffservcode_forward: DiffServ code forward
            diffservcode_rev: DiffServ code reverse
            
            # TCP/IP
            tcp_mss_sender: TCP MSS sender (0-65535)
            tcp_mss_receiver: TCP MSS receiver (0-65535)
            tcp_session_without_syn: TCP session without SYN ('enable', 'disable')
            anti_replay: Enable anti-replay ('enable', 'disable')
            tos: Type of Service (ToS) value
            tos_mask: ToS mask
            tos_negate: Negate ToS match ('enable', 'disable')
            
            # Geo-IP
            geoip_anycast: Geo-IP anycast ('enable', 'disable')
            geoip_match: Geo-IP match ('physical-location', 'registered-location')
            
            # Security Groups
            sgt_check: Security Group Tag check ('enable', 'disable')
            sgt: Security Group Tag(s) - string or list
            
            # Performance
            auto_asic_offload: Auto ASIC offload ('enable', 'disable')
            np_acceleration: Network processor acceleration ('enable', 'disable')
            delay_tcp_npu_session: Delay TCP NPU session ('enable', 'disable')
            
            # VIP Matching
            match_vip: Match VIP ('enable', 'disable')
            match_vip_only: Match VIP only ('enable', 'disable')
            
            # RADIUS Bypass
            radius_mac_auth_bypass: RADIUS MAC auth bypass ('enable', 'disable')
            radius_ip_auth_bypass: RADIUS IP auth bypass ('enable', 'disable')
            dsri: Disable Server Response Inspection ('enable', 'disable')
            
            # Identity Routing
            identity_based_route: Identity-based route name
            
            # Redirects & Messages
            redirect_url: Redirect URL
            block_notification: Block notification ('enable', 'disable')
            replacemsg_override_group: Replace message override group name
            
            # Negation Options
            srcaddr_negate: Negate source address match ('enable', 'disable')
            dstaddr_negate: Negate destination address match ('enable', 'disable')
            srcaddr6_negate: Negate source IPv6 address match ('enable', 'disable')
            dstaddr6_negate: Negate destination IPv6 address match ('enable', 'disable')
            service_negate: Negate service match ('enable', 'disable')
            
            # Comments
            comments: Policy comments
            
            # API Parameters
            vdom: Virtual domain name
            datasource: Include datasource in response
            with_meta: Include metadata in response
            data: Additional fields as dictionary (merged with explicit parameters)
            
        Returns:
            API response dictionary
            
        Example:
            >>> # Simple policy
            >>> result = fgt.firewall.policy.create(
            ...     name='Allow-Web-Traffic',
            ...     srcintf='port1',
            ...     dstintf='port2',
            ...     srcaddr='internal-net',
            ...     dstaddr='all',
            ...     service=['HTTP', 'HTTPS'],
            ...     action='accept'
            ... )
            
            >>> # Advanced policy with security profiles
            >>> result = fgt.firewall.policy.create(
            ...     name='Secure-Web-Access',
            ...     srcintf=['port1', 'port3'],
            ...     dstintf='wan1',
            ...     srcaddr=['internal-net', 'guest-net'],
            ...     dstaddr='all',
            ...     service=['HTTP', 'HTTPS'],
            ...     action='accept',
            ...     inspection_mode='proxy',
            ...     ssl_ssh_profile='deep-inspection',
            ...     av_profile='default',
            ...     webfilter_profile='default',
            ...     ips_sensor='default',
            ...     application_list='default',
            ...     nat='enable',
            ...     logtraffic='all'
            ... )
        """
        # Build the policy data dictionary
        policy_data: Dict[str, Any] = {
            'name': name,
            'srcintf': _normalize_to_name_list(srcintf),
            'dstintf': _normalize_to_name_list(dstintf),
            'srcaddr': _normalize_to_name_list(srcaddr),
            'dstaddr': _normalize_to_name_list(dstaddr),
        }
        
        # Add core optional fields if provided
        if action is not None:
            policy_data['action'] = action
        if schedule is not None:
            policy_data['schedule'] = schedule
        if status is not None:
            policy_data['status'] = status
        
        # Add service if provided (no default - FortiOS will use its own default)
        if service is not None:
            policy_data['service'] = _normalize_to_name_list(service)
        
        # Add optional string fields (simple enable/disable or profile names)
        optional_string_fields = {
            # Inspection & UTM
            'inspection-mode': inspection_mode,
            'utm-status': utm_status,
            'profile-type': profile_type,
            'profile-group': profile_group,
            'profile-protocol-options': profile_protocol_options,
            # Security Profiles
            'ssl-ssh-profile': ssl_ssh_profile,
            'av-profile': av_profile,
            'webfilter-profile': webfilter_profile,
            'dnsfilter-profile': dnsfilter_profile,
            'emailfilter-profile': emailfilter_profile,
            'dlp-profile': dlp_profile,
            'file-filter-profile': file_filter_profile,
            'ips-sensor': ips_sensor,
            'application-list': application_list,
            'voip-profile': voip_profile,
            'ips-voip-filter': ips_voip_filter,
            'sctp-filter-profile': sctp_filter_profile,
            'diameter-filter-profile': diameter_filter_profile,
            'virtual-patch-profile': virtual_patch_profile,
            'icap-profile': icap_profile,
            'videofilter-profile': videofilter_profile,
            'waf-profile': waf_profile,
            'ssh-filter-profile': ssh_filter_profile,
            'casb-profile': casb_profile,
            # Proxy
            'http-policy-redirect': http_policy_redirect,
            'ssh-policy-redirect': ssh_policy_redirect,
            'webproxy-profile': webproxy_profile,
            'webproxy-forward-server': webproxy_forward_server,
            # NAT
            'nat': nat,
            'nat64': nat64,
            'nat46': nat46,
            'ippool': ippool,
            'natip': natip,
            'fixedport': fixedport,
            'permit-any-host': permit_any_host,
            'permit-stun-host': permit_stun_host,
            'port-preserve': port_preserve,
            'port-random': port_random,
            # PCP
            'pcp-outbound': pcp_outbound,
            'pcp-inbound': pcp_inbound,
            # VPN
            'vpntunnel': vpntunnel,
            'inbound': inbound,
            'outbound': outbound,
            'natinbound': natinbound,
            'natoutbound': natoutbound,
            # ZTNA
            'ztna-status': ztna_status,
            'ztna-device-ownership': ztna_device_ownership,
            'ztna-tags-match-logic': ztna_tags_match_logic,
            'ztna-ems-tag-negate': ztna_ems_tag_negate,
            'ztna-policy-redirect': ztna_policy_redirect,
            # Internet Services
            'internet-service': internet_service,
            'internet-service-negate': internet_service_negate,
            'internet-service-src': internet_service_src,
            'internet-service-src-negate': internet_service_src_negate,
            'internet-service6': internet_service6,
            'internet-service6-negate': internet_service6_negate,
            'internet-service6-src': internet_service6_src,
            'internet-service6-src-negate': internet_service6_src_negate,
            # RTP
            'rtp-nat': rtp_nat,
            # Authentication
            'fsso-agent-for-ntlm': fsso_agent_for_ntlm,
            'ntlm': ntlm,
            'ntlm-guest': ntlm_guest,
            'auth-path': auth_path,
            'auth-cert': auth_cert,
            'auth-redirect-addr': auth_redirect_addr,
            'disclaimer': disclaimer,
            'email-collect': email_collect,
            # Traffic Shaping
            'traffic-shaper': traffic_shaper,
            'traffic-shaper-reverse': traffic_shaper_reverse,
            'per-ip-shaper': per_ip_shaper,
            # Logging
            'logtraffic': logtraffic,
            'logtraffic-start': logtraffic_start,
            'log-http-transaction': log_http_transaction,
            'capture-packet': capture_packet,
            # Advanced
            'wccp': wccp,
            'passive-wan-health-measurement': passive_wan_health_measurement,
            'app-monitor': app_monitor,
            'captive-portal-exempt': captive_portal_exempt,
            'decrypted-traffic-mirror': decrypted_traffic_mirror,
            'dynamic-shaping': dynamic_shaping,
            'fec': fec,
            # Session control
            'send-deny-packet': send_deny_packet,
            'firewall-session-dirty': firewall_session_dirty,
            'schedule-timeout': schedule_timeout,
            'policy-expiry': policy_expiry,
            'policy-expiry-date': policy_expiry_date,
            'policy-expiry-date-utc': policy_expiry_date_utc,
            'session-ttl': session_ttl,
            'timeout-send-rst': timeout_send_rst,
            # VLAN & QoS
            'vlan-filter': vlan_filter,
            'diffserv-copy': diffserv_copy,
            'diffserv-forward': diffserv_forward,
            'diffserv-reverse': diffserv_reverse,
            'diffservcode-forward': diffservcode_forward,
            'diffservcode-rev': diffservcode_rev,
            # TCP/IP
            'tcp-session-without-syn': tcp_session_without_syn,
            'anti-replay': anti_replay,
            'tos': tos,
            'tos-mask': tos_mask,
            'tos-negate': tos_negate,
            # Geo-IP
            'geoip-anycast': geoip_anycast,
            'geoip-match': geoip_match,
            # Security Groups
            'sgt-check': sgt_check,
            # Performance
            'auto-asic-offload': auto_asic_offload,
            'np-acceleration': np_acceleration,
            'delay-tcp-npu-session': delay_tcp_npu_session,
            # VIP
            'match-vip': match_vip,
            'match-vip-only': match_vip_only,
            # RADIUS
            'radius-mac-auth-bypass': radius_mac_auth_bypass,
            'radius-ip-auth-bypass': radius_ip_auth_bypass,
            'dsri': dsri,
            # Identity routing
            'identity-based-route': identity_based_route,
            # Redirects & Messages
            'redirect-url': redirect_url,
            'block-notification': block_notification,
            'replacemsg-override-group': replacemsg_override_group,
            # Negation
            'srcaddr-negate': srcaddr_negate,
            'dstaddr-negate': dstaddr_negate,
            'srcaddr6-negate': srcaddr6_negate,
            'dstaddr6-negate': dstaddr6_negate,
            'service-negate': service_negate,
            # Comments
            'comments': comments,
        }
        
        for key, value in optional_string_fields.items():
            if value is not None:
                policy_data[key] = value
        
        # Add optional integer fields
        optional_int_fields = {
            'reputation-minimum': reputation_minimum,
            'reputation-minimum6': reputation_minimum6,
            'vlan-cos-fwd': vlan_cos_fwd,
            'vlan-cos-rev': vlan_cos_rev,
            'tcp-mss-sender': tcp_mss_sender,
            'tcp-mss-receiver': tcp_mss_receiver,
        }
        
        for key, value in optional_int_fields.items():
            if value is not None:
                policy_data[key] = value
        
        # Add reputation direction fields (special handling for direction)
        if reputation_direction is not None:
            policy_data['reputation-direction'] = reputation_direction
        if reputation_direction6 is not None:
            policy_data['reputation-direction6'] = reputation_direction6
        
        # Add list fields using the helper function for normalization
        list_fields = {
            'srcaddr6': srcaddr6,
            'dstaddr6': dstaddr6,
            'internet-service-name': internet_service_name,
            'internet-service-group': internet_service_group,
            'internet-service-custom': internet_service_custom,
            'internet-service-custom-group': internet_service_custom_group,
            'network-service-dynamic': network_service_dynamic,
            'internet-service-fortiguard': internet_service_fortiguard,
            'internet-service-src-name': internet_service_src_name,
            'internet-service-src-group': internet_service_src_group,
            'internet-service-src-custom': internet_service_src_custom,
            'internet-service-src-custom-group': internet_service_src_custom_group,
            'network-service-src-dynamic': network_service_src_dynamic,
            'internet-service-src-fortiguard': internet_service_src_fortiguard,
            'internet-service6-name': internet_service6_name,
            'internet-service6-group': internet_service6_group,
            'internet-service6-custom': internet_service6_custom,
            'internet-service6-custom-group': internet_service6_custom_group,
            'internet-service6-fortiguard': internet_service6_fortiguard,
            'internet-service6-src-name': internet_service6_src_name,
            'internet-service6-src-group': internet_service6_src_group,
            'internet-service6-src-custom': internet_service6_src_custom,
            'internet-service6-src-custom-group': internet_service6_src_custom_group,
            'internet-service6-src-fortiguard': internet_service6_src_fortiguard,
            'rtp-addr': rtp_addr,
            'ztna-ems-tag': ztna_ems_tag,
            'ztna-ems-tag-secondary': ztna_ems_tag_secondary,
            'ztna-geo-tag': ztna_geo_tag,
            'src-vendor-mac': src_vendor_mac,
            'poolname': poolname,
            'poolname6': poolname6,
            'pcp-poolname': pcp_poolname,
            'users': users,
            'groups': groups,
            'fsso-groups': fsso_groups,
            'ntlm-enabled-browsers': ntlm_enabled_browsers,
            'custom-log-fields': custom_log_fields,
            'sgt': sgt,
        }
        
        for key, value in list_fields.items():
            if value is not None:
                policy_data[key] = _normalize_to_name_list(value)
        
        # Merge with additional data if provided
        if data:
            policy_data.update(data)
        
        # Build API parameters
        api_params = {}
        if vdom:
            api_params['vdom'] = vdom
        if datasource is not None:
            api_params['datasource'] = datasource
        if with_meta is not None:
            api_params['with_meta'] = with_meta
        
        return self._api.post(data=policy_data, **api_params)
    
    def get(
        self, 
        policy_id: Optional[Union[str, int]] = None,
        vdom: Optional[str] = None,
        filter: Optional[str] = None,
        **kwargs
    ) -> Union[Dict[str, Any], List[Dict[str, Any]]]:
        """
        Get firewall policy/policies.
        
        Args:
            policy_id: Policy ID (optional, retrieves all if not specified)
            vdom: Virtual domain name (optional)
            filter: Filter string (optional)
            **kwargs: Additional parameters passed to the API
            
        Returns:
            Policy data (single policy if policy_id provided, list otherwise)
            
        Examples:
            >>> # Get all policies
            >>> policies = fgt.firewall.policy.get()
            
            >>> # Get specific policy by ID
            >>> policy = fgt.firewall.policy.get(policy_id=1)
            
            >>> # Get policies with filter
            >>> policies = fgt.firewall.policy.get(filter='name==Allow-HTTP')
        """
        return self._api.get(mkey=policy_id, vdom=vdom, filter=filter, **kwargs)
    
    def update(
        self,
        policy_id: Union[str, int],
        # All optional fields for update (partial update)
        name: Optional[str] = None,
        srcintf: Optional[Union[str, List[str]]] = None,
        dstintf: Optional[Union[str, List[str]]] = None,
        srcaddr: Optional[Union[str, List[str]]] = None,
        dstaddr: Optional[Union[str, List[str]]] = None,
        action: Optional[str] = None,
        schedule: Optional[str] = None,
        service: Optional[Union[str, List[str]]] = None,
        status: Optional[str] = None,
        # IPv6 addresses
        srcaddr6: Optional[Union[str, List[str]]] = None,
        dstaddr6: Optional[Union[str, List[str]]] = None,
        # Internet Services (IPv4) - destination
        internet_service: Optional[str] = None,
        internet_service_name: Optional[Union[str, List[str]]] = None,
        internet_service_group: Optional[Union[str, List[str]]] = None,
        internet_service_custom: Optional[Union[str, List[str]]] = None,
        internet_service_custom_group: Optional[Union[str, List[str]]] = None,
        network_service_dynamic: Optional[Union[str, List[str]]] = None,
        internet_service_fortiguard: Optional[Union[str, List[str]]] = None,
        internet_service_negate: Optional[str] = None,
        # Internet Services (IPv4) - source
        internet_service_src: Optional[str] = None,
        internet_service_src_name: Optional[Union[str, List[str]]] = None,
        internet_service_src_group: Optional[Union[str, List[str]]] = None,
        internet_service_src_custom: Optional[Union[str, List[str]]] = None,
        internet_service_src_custom_group: Optional[Union[str, List[str]]] = None,
        network_service_src_dynamic: Optional[Union[str, List[str]]] = None,
        internet_service_src_fortiguard: Optional[Union[str, List[str]]] = None,
        internet_service_src_negate: Optional[str] = None,
        # Internet Services (IPv6) - destination
        internet_service6: Optional[str] = None,
        internet_service6_name: Optional[Union[str, List[str]]] = None,
        internet_service6_group: Optional[Union[str, List[str]]] = None,
        internet_service6_custom: Optional[Union[str, List[str]]] = None,
        internet_service6_custom_group: Optional[Union[str, List[str]]] = None,
        internet_service6_fortiguard: Optional[Union[str, List[str]]] = None,
        internet_service6_negate: Optional[str] = None,
        # Internet Services (IPv6) - source
        internet_service6_src: Optional[str] = None,
        internet_service6_src_name: Optional[Union[str, List[str]]] = None,
        internet_service6_src_group: Optional[Union[str, List[str]]] = None,
        internet_service6_src_custom: Optional[Union[str, List[str]]] = None,
        internet_service6_src_custom_group: Optional[Union[str, List[str]]] = None,
        internet_service6_src_fortiguard: Optional[Union[str, List[str]]] = None,
        internet_service6_src_negate: Optional[str] = None,
        # Reputation
        reputation_minimum: Optional[int] = None,
        reputation_direction: Optional[str] = None,
        reputation_minimum6: Optional[int] = None,
        reputation_direction6: Optional[str] = None,
        # RTP
        rtp_nat: Optional[str] = None,
        rtp_addr: Optional[Union[str, List[str]]] = None,
        # ZTNA
        ztna_status: Optional[str] = None,
        ztna_device_ownership: Optional[str] = None,
        ztna_ems_tag: Optional[Union[str, List[str]]] = None,
        ztna_ems_tag_secondary: Optional[Union[str, List[str]]] = None,
        ztna_tags_match_logic: Optional[str] = None,
        ztna_geo_tag: Optional[Union[str, List[str]]] = None,
        ztna_ems_tag_negate: Optional[str] = None,
        ztna_policy_redirect: Optional[str] = None,
        # Vendor MAC
        src_vendor_mac: Optional[Union[str, List[str]]] = None,
        # Inspection & UTM
        inspection_mode: Optional[str] = None,
        utm_status: Optional[str] = None,
        profile_type: Optional[str] = None,
        profile_group: Optional[str] = None,
        profile_protocol_options: Optional[str] = None,
        # SSL/SSH & Security Profiles
        ssl_ssh_profile: Optional[str] = None,
        av_profile: Optional[str] = None,
        webfilter_profile: Optional[str] = None,
        dnsfilter_profile: Optional[str] = None,
        emailfilter_profile: Optional[str] = None,
        dlp_profile: Optional[str] = None,
        file_filter_profile: Optional[str] = None,
        ips_sensor: Optional[str] = None,
        application_list: Optional[str] = None,
        voip_profile: Optional[str] = None,
        ips_voip_filter: Optional[str] = None,
        sctp_filter_profile: Optional[str] = None,
        diameter_filter_profile: Optional[str] = None,
        virtual_patch_profile: Optional[str] = None,
        icap_profile: Optional[str] = None,
        videofilter_profile: Optional[str] = None,
        waf_profile: Optional[str] = None,
        ssh_filter_profile: Optional[str] = None,
        casb_profile: Optional[str] = None,
        # Proxy
        http_policy_redirect: Optional[str] = None,
        ssh_policy_redirect: Optional[str] = None,
        webproxy_profile: Optional[str] = None,
        webproxy_forward_server: Optional[str] = None,
        # NAT
        nat: Optional[str] = None,
        nat64: Optional[str] = None,
        nat46: Optional[str] = None,
        ippool: Optional[str] = None,
        poolname: Optional[Union[str, List[str]]] = None,
        poolname6: Optional[Union[str, List[str]]] = None,
        natip: Optional[str] = None,
        fixedport: Optional[str] = None,
        permit_any_host: Optional[str] = None,
        permit_stun_host: Optional[str] = None,
        port_preserve: Optional[str] = None,
        port_random: Optional[str] = None,
        # PCP
        pcp_outbound: Optional[str] = None,
        pcp_inbound: Optional[str] = None,
        pcp_poolname: Optional[Union[str, List[str]]] = None,
        # VPN
        vpntunnel: Optional[str] = None,
        inbound: Optional[str] = None,
        outbound: Optional[str] = None,
        natinbound: Optional[str] = None,
        natoutbound: Optional[str] = None,
        # Users & Authentication
        users: Optional[Union[str, List[str]]] = None,
        groups: Optional[Union[str, List[str]]] = None,
        fsso_groups: Optional[Union[str, List[str]]] = None,
        fsso_agent_for_ntlm: Optional[str] = None,
        ntlm: Optional[str] = None,
        ntlm_guest: Optional[str] = None,
        ntlm_enabled_browsers: Optional[Union[str, List[str]]] = None,
        auth_path: Optional[str] = None,
        auth_cert: Optional[str] = None,
        auth_redirect_addr: Optional[str] = None,
        disclaimer: Optional[str] = None,
        email_collect: Optional[str] = None,
        # Traffic Shaping
        traffic_shaper: Optional[str] = None,
        traffic_shaper_reverse: Optional[str] = None,
        per_ip_shaper: Optional[str] = None,
        # Logging
        logtraffic: Optional[str] = None,
        logtraffic_start: Optional[str] = None,
        log_http_transaction: Optional[str] = None,
        capture_packet: Optional[str] = None,
        custom_log_fields: Optional[Union[str, List[str]]] = None,
        # Advanced features
        wccp: Optional[str] = None,
        passive_wan_health_measurement: Optional[str] = None,
        app_monitor: Optional[str] = None,
        captive_portal_exempt: Optional[str] = None,
        decrypted_traffic_mirror: Optional[str] = None,
        dynamic_shaping: Optional[str] = None,
        fec: Optional[str] = None,
        # Session control
        send_deny_packet: Optional[str] = None,
        firewall_session_dirty: Optional[str] = None,
        schedule_timeout: Optional[str] = None,
        policy_expiry: Optional[str] = None,
        policy_expiry_date: Optional[str] = None,
        policy_expiry_date_utc: Optional[str] = None,
        session_ttl: Optional[str] = None,
        timeout_send_rst: Optional[str] = None,
        # QoS & VLAN
        vlan_cos_fwd: Optional[int] = None,
        vlan_cos_rev: Optional[int] = None,
        vlan_filter: Optional[str] = None,
        diffserv_copy: Optional[str] = None,
        diffserv_forward: Optional[str] = None,
        diffserv_reverse: Optional[str] = None,
        diffservcode_forward: Optional[str] = None,
        diffservcode_rev: Optional[str] = None,
        # TCP/IP
        tcp_mss_sender: Optional[int] = None,
        tcp_mss_receiver: Optional[int] = None,
        tcp_session_without_syn: Optional[str] = None,
        anti_replay: Optional[str] = None,
        tos: Optional[str] = None,
        tos_mask: Optional[str] = None,
        tos_negate: Optional[str] = None,
        # Geo-IP
        geoip_anycast: Optional[str] = None,
        geoip_match: Optional[str] = None,
        # Security Groups
        sgt_check: Optional[str] = None,
        sgt: Optional[Union[str, List[str]]] = None,
        # Performance
        auto_asic_offload: Optional[str] = None,
        np_acceleration: Optional[str] = None,
        delay_tcp_npu_session: Optional[str] = None,
        # VIP matching
        match_vip: Optional[str] = None,
        match_vip_only: Optional[str] = None,
        # RADIUS bypass
        radius_mac_auth_bypass: Optional[str] = None,
        radius_ip_auth_bypass: Optional[str] = None,
        dsri: Optional[str] = None,
        # Identity routing
        identity_based_route: Optional[str] = None,
        # Redirect & Messages
        redirect_url: Optional[str] = None,
        block_notification: Optional[str] = None,
        replacemsg_override_group: Optional[str] = None,
        # Negation options
        srcaddr_negate: Optional[str] = None,
        dstaddr_negate: Optional[str] = None,
        srcaddr6_negate: Optional[str] = None,
        dstaddr6_negate: Optional[str] = None,
        service_negate: Optional[str] = None,
        # Comments
        comments: Optional[str] = None,
        # API parameters
        vdom: Optional[str] = None,
        datasource: Optional[bool] = None,
        with_meta: Optional[bool] = None,
        # Catch-all for any additional fields
        data: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """
        Update an existing firewall policy (partial update - only specify fields to change).
        All parameters same as create() but optional. See create() docstring for full parameter documentation.
        
        Args:
            policy_id: Policy ID to update (required)
            (All other parameters are optional - see create() method for details)
            
        Returns:
            API response dictionary
            
        Example:
            >>> # Enable deep inspection on existing policy
            >>> result = fgt.firewall.policy.update(
            ...     policy_id=2,
            ...     inspection_mode='proxy',
            ...     ssl_ssh_profile='deep-inspection',
            ...     passive_wan_health_measurement='enable'
            ... )
            
            >>> # Change source and destination addresses
            >>> result = fgt.firewall.policy.update(
            ...     policy_id=5,
            ...     srcaddr=['internal-net', 'dmz-net'],
            ...     dstaddr='all'
            ... )
        """
        # Build the update data dictionary (only include non-None values)
        policy_data: Dict[str, Any] = {}
        
        # Core fields
        if name is not None:
            policy_data['name'] = name
        if srcintf is not None:
            policy_data['srcintf'] = _normalize_to_name_list(srcintf)
        if dstintf is not None:
            policy_data['dstintf'] = _normalize_to_name_list(dstintf)
        if srcaddr is not None:
            policy_data['srcaddr'] = _normalize_to_name_list(srcaddr)
        if dstaddr is not None:
            policy_data['dstaddr'] = _normalize_to_name_list(dstaddr)
        if action is not None:
            policy_data['action'] = action
        if schedule is not None:
            policy_data['schedule'] = schedule
        if service is not None:
            policy_data['service'] = _normalize_to_name_list(service)
        if status is not None:
            policy_data['status'] = status
        
        # Add optional string fields
        optional_string_fields = {
            # Inspection & UTM
            'inspection-mode': inspection_mode,
            'utm-status': utm_status,
            'profile-type': profile_type,
            'profile-group': profile_group,
            'profile-protocol-options': profile_protocol_options,
            # Security Profiles
            'ssl-ssh-profile': ssl_ssh_profile,
            'av-profile': av_profile,
            'webfilter-profile': webfilter_profile,
            'dnsfilter-profile': dnsfilter_profile,
            'emailfilter-profile': emailfilter_profile,
            'dlp-profile': dlp_profile,
            'file-filter-profile': file_filter_profile,
            'ips-sensor': ips_sensor,
            'application-list': application_list,
            'voip-profile': voip_profile,
            'ips-voip-filter': ips_voip_filter,
            'sctp-filter-profile': sctp_filter_profile,
            'diameter-filter-profile': diameter_filter_profile,
            'virtual-patch-profile': virtual_patch_profile,
            'icap-profile': icap_profile,
            'videofilter-profile': videofilter_profile,
            'waf-profile': waf_profile,
            'ssh-filter-profile': ssh_filter_profile,
            'casb-profile': casb_profile,
            # Proxy
            'http-policy-redirect': http_policy_redirect,
            'ssh-policy-redirect': ssh_policy_redirect,
            'webproxy-profile': webproxy_profile,
            'webproxy-forward-server': webproxy_forward_server,
            # NAT
            'nat': nat,
            'nat64': nat64,
            'nat46': nat46,
            'ippool': ippool,
            'natip': natip,
            'fixedport': fixedport,
            'permit-any-host': permit_any_host,
            'permit-stun-host': permit_stun_host,
            'port-preserve': port_preserve,
            'port-random': port_random,
            # PCP
            'pcp-outbound': pcp_outbound,
            'pcp-inbound': pcp_inbound,
            # VPN
            'vpntunnel': vpntunnel,
            'inbound': inbound,
            'outbound': outbound,
            'natinbound': natinbound,
            'natoutbound': natoutbound,
            # ZTNA
            'ztna-status': ztna_status,
            'ztna-device-ownership': ztna_device_ownership,
            'ztna-tags-match-logic': ztna_tags_match_logic,
            'ztna-ems-tag-negate': ztna_ems_tag_negate,
            'ztna-policy-redirect': ztna_policy_redirect,
            # Internet Services
            'internet-service': internet_service,
            'internet-service-negate': internet_service_negate,
            'internet-service-src': internet_service_src,
            'internet-service-src-negate': internet_service_src_negate,
            'internet-service6': internet_service6,
            'internet-service6-negate': internet_service6_negate,
            'internet-service6-src': internet_service6_src,
            'internet-service6-src-negate': internet_service6_src_negate,
            # RTP
            'rtp-nat': rtp_nat,
            # Authentication
            'fsso-agent-for-ntlm': fsso_agent_for_ntlm,
            'ntlm': ntlm,
            'ntlm-guest': ntlm_guest,
            'auth-path': auth_path,
            'auth-cert': auth_cert,
            'auth-redirect-addr': auth_redirect_addr,
            'disclaimer': disclaimer,
            'email-collect': email_collect,
            # Traffic Shaping
            'traffic-shaper': traffic_shaper,
            'traffic-shaper-reverse': traffic_shaper_reverse,
            'per-ip-shaper': per_ip_shaper,
            # Logging
            'logtraffic': logtraffic,
            'logtraffic-start': logtraffic_start,
            'log-http-transaction': log_http_transaction,
            'capture-packet': capture_packet,
            # Advanced
            'wccp': wccp,
            'passive-wan-health-measurement': passive_wan_health_measurement,
            'app-monitor': app_monitor,
            'captive-portal-exempt': captive_portal_exempt,
            'decrypted-traffic-mirror': decrypted_traffic_mirror,
            'dynamic-shaping': dynamic_shaping,
            'fec': fec,
            # Session control
            'send-deny-packet': send_deny_packet,
            'firewall-session-dirty': firewall_session_dirty,
            'schedule-timeout': schedule_timeout,
            'policy-expiry': policy_expiry,
            'policy-expiry-date': policy_expiry_date,
            'policy-expiry-date-utc': policy_expiry_date_utc,
            'session-ttl': session_ttl,
            'timeout-send-rst': timeout_send_rst,
            # VLAN & QoS
            'vlan-filter': vlan_filter,
            'diffserv-copy': diffserv_copy,
            'diffserv-forward': diffserv_forward,
            'diffserv-reverse': diffserv_reverse,
            'diffservcode-forward': diffservcode_forward,
            'diffservcode-rev': diffservcode_rev,
            # TCP/IP
            'tcp-session-without-syn': tcp_session_without_syn,
            'anti-replay': anti_replay,
            'tos': tos,
            'tos-mask': tos_mask,
            'tos-negate': tos_negate,
            # Geo-IP
            'geoip-anycast': geoip_anycast,
            'geoip-match': geoip_match,
            # Security Groups
            'sgt-check': sgt_check,
            # Performance
            'auto-asic-offload': auto_asic_offload,
            'np-acceleration': np_acceleration,
            'delay-tcp-npu-session': delay_tcp_npu_session,
            # VIP
            'match-vip': match_vip,
            'match-vip-only': match_vip_only,
            # RADIUS
            'radius-mac-auth-bypass': radius_mac_auth_bypass,
            'radius-ip-auth-bypass': radius_ip_auth_bypass,
            'dsri': dsri,
            # Identity routing
            'identity-based-route': identity_based_route,
            # Redirects & Messages
            'redirect-url': redirect_url,
            'block-notification': block_notification,
            'replacemsg-override-group': replacemsg_override_group,
            # Negation
            'srcaddr-negate': srcaddr_negate,
            'dstaddr-negate': dstaddr_negate,
            'srcaddr6-negate': srcaddr6_negate,
            'dstaddr6-negate': dstaddr6_negate,
            'service-negate': service_negate,
            # Comments
            'comments': comments,
        }
        
        for key, value in optional_string_fields.items():
            if value is not None:
                policy_data[key] = value
        
        # Add optional integer fields
        optional_int_fields = {
            'reputation-minimum': reputation_minimum,
            'reputation-minimum6': reputation_minimum6,
            'vlan-cos-fwd': vlan_cos_fwd,
            'vlan-cos-rev': vlan_cos_rev,
            'tcp-mss-sender': tcp_mss_sender,
            'tcp-mss-receiver': tcp_mss_receiver,
        }
        
        for key, value in optional_int_fields.items():
            if value is not None:
                policy_data[key] = value
        
        # Add reputation direction fields
        if reputation_direction is not None:
            policy_data['reputation-direction'] = reputation_direction
        if reputation_direction6 is not None:
            policy_data['reputation-direction6'] = reputation_direction6
        
        # Add list fields using the helper function for normalization
        list_fields = {
            'srcaddr6': srcaddr6,
            'dstaddr6': dstaddr6,
            'internet-service-name': internet_service_name,
            'internet-service-group': internet_service_group,
            'internet-service-custom': internet_service_custom,
            'internet-service-custom-group': internet_service_custom_group,
            'network-service-dynamic': network_service_dynamic,
            'internet-service-fortiguard': internet_service_fortiguard,
            'internet-service-src-name': internet_service_src_name,
            'internet-service-src-group': internet_service_src_group,
            'internet-service-src-custom': internet_service_src_custom,
            'internet-service-src-custom-group': internet_service_src_custom_group,
            'network-service-src-dynamic': network_service_src_dynamic,
            'internet-service-src-fortiguard': internet_service_src_fortiguard,
            'internet-service6-name': internet_service6_name,
            'internet-service6-group': internet_service6_group,
            'internet-service6-custom': internet_service6_custom,
            'internet-service6-custom-group': internet_service6_custom_group,
            'internet-service6-fortiguard': internet_service6_fortiguard,
            'internet-service6-src-name': internet_service6_src_name,
            'internet-service6-src-group': internet_service6_src_group,
            'internet-service6-src-custom': internet_service6_src_custom,
            'internet-service6-src-custom-group': internet_service6_src_custom_group,
            'internet-service6-src-fortiguard': internet_service6_src_fortiguard,
            'rtp-addr': rtp_addr,
            'ztna-ems-tag': ztna_ems_tag,
            'ztna-ems-tag-secondary': ztna_ems_tag_secondary,
            'ztna-geo-tag': ztna_geo_tag,
            'src-vendor-mac': src_vendor_mac,
            'poolname': poolname,
            'poolname6': poolname6,
            'pcp-poolname': pcp_poolname,
            'users': users,
            'groups': groups,
            'fsso-groups': fsso_groups,
            'ntlm-enabled-browsers': ntlm_enabled_browsers,
            'custom-log-fields': custom_log_fields,
            'sgt': sgt,
        }
        
        for key, value in list_fields.items():
            if value is not None:
                policy_data[key] = _normalize_to_name_list(value)
        
        # Merge with additional data if provided
        if data:
            policy_data.update(data)
        
        # Build API parameters
        api_params = {}
        if vdom:
            api_params['vdom'] = vdom
        if datasource is not None:
            api_params['datasource'] = datasource
        if with_meta is not None:
            api_params['with_meta'] = with_meta
        
        return self._api.put(mkey=str(policy_id), data=policy_data, **api_params)
    
    def delete(
        self, 
        policy_id: Union[str, int],
        vdom: Optional[str] = None,
    ) -> Dict[str, Any]:
        """
        Delete a firewall policy.
        
        Args:
            policy_id: Policy ID to delete
            vdom: Virtual domain name (optional)
            
        Returns:
            API response dictionary
            
        Example:
            >>> result = fgt.firewall.policy.delete(policy_id=1)
        """
        api_params = {}
        if vdom:
            api_params['vdom'] = vdom
        return self._api.delete(mkey=str(policy_id), **api_params)
    
    def exists(
        self, 
        policy_id: Union[str, int],
        vdom: Optional[str] = None,
    ) -> bool:
        """
        Check if a firewall policy exists.
        
        Args:
            policy_id: Policy ID to check
            vdom: Virtual domain name (optional)
            
        Returns:
            True if policy exists, False otherwise
            
        Example:
            >>> if fgt.firewall.policy.exists(policy_id=1):
            ...     print("Policy exists")
        """
        return self._api.exists(str(policy_id), vdom=vdom)
    
    def move(
        self,
        policy_id: Union[str, int],
        position: str,
        reference_id: Optional[Union[str, int]] = None,
        vdom: Optional[str] = None,
    ) -> Dict[str, Any]:
        """
        Move a firewall policy to a different position.
        
        Args:
            policy_id: Policy ID to move
            position: Position ('before', 'after', 'top', or 'bottom')
            reference_id: Reference policy ID (required for 'before'/'after', ignored for 'top'/'bottom')
            vdom: Virtual domain name (optional)
            
        Returns:
            API response dictionary
            
        Examples:
            >>> # Move policy 5 before policy 3
            >>> result = fgt.firewall.policy.move(policy_id=5, position='before', reference_id=3)
            
            >>> # Move policy 10 to the top
            >>> result = fgt.firewall.policy.move(policy_id=10, position='top')
            
            >>> # Move policy 15 to the bottom
            >>> result = fgt.firewall.policy.move(policy_id=15, position='bottom')
        """
        # Build move-specific parameters
        move_kwargs: Dict[str, Any] = {'action': 'move'}
        if vdom:
            move_kwargs['vdom'] = vdom
        
        # Add the position parameter
        if position in ('before', 'after'):
            if reference_id is None:
                raise ValueError(f"reference_id is required when position is '{position}'")
            move_kwargs[position] = str(reference_id)
        elif position == 'top':
            # Move to position 0 (top)
            move_kwargs['before'] = '1'
        elif position == 'bottom':
            # For bottom, we don't specify before/after, just the action
            pass
        else:
            raise ValueError(f"Invalid position: {position}. Must be 'before', 'after', 'top', or 'bottom'")
        
        # Call the API using the put method
        return self._api.put(
            mkey=str(policy_id),
            data={},  # Move doesn't require data
            **move_kwargs
        )
    
    def clone(
        self,
        policy_id: Union[str, int],
        new_name: Optional[str] = None,
        status: Optional[str] = None,
        vdom: Optional[str] = None,
        additional_changes: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """
        Clone an existing firewall policy.
        
        Args:
            policy_id: Policy ID to clone
            new_name: Name for the cloned policy (optional, will auto-generate if not provided)
            status: Status for cloned policy - 'enable' or 'disable' (optional, defaults to original)
            vdom: Virtual domain name (optional)
            additional_changes: Additional field changes as dictionary (optional)
            
        Returns:
            API response dictionary
            
        Examples:
            >>> # Clone policy 1 with a new name
            >>> result = fgt.firewall.policy.clone(policy_id=1, new_name='Cloned-Policy')
            
            >>> # Clone and disable
            >>> result = fgt.firewall.policy.clone(policy_id=1, new_name='Test-Policy', status='disable')
            
            >>> # Clone with additional changes
            >>> result = fgt.firewall.policy.clone(
            ...     policy_id=1,
            ...     new_name='Modified-Clone',
            ...     status='disable',
            ...     additional_changes={'comments': 'Testing clone feature'}
            ... )
        """
        # Get the original policy
        original_response = self.get(policy_id=policy_id, vdom=vdom)
        
        # Handle response format
        if isinstance(original_response, dict) and 'results' in original_response:
            original = original_response['results'][0] if original_response['results'] else {}
        elif isinstance(original_response, list):
            original = original_response[0] if original_response else {}
        else:
            original = original_response
        
        # Remove fields that shouldn't be copied
        clone_data = {k: v for k, v in original.items() 
                     if k not in ('policyid', 'uuid', 'q_origin_key')}
        
        # Apply name change
        if new_name:
            clone_data['name'] = new_name
        else:
            # Auto-generate name if not provided
            original_name = clone_data.get('name', 'Policy')
            clone_data['name'] = f"{original_name}-Clone"
        
        # Apply status change
        if status:
            clone_data['status'] = status
        
        # Apply additional changes
        if additional_changes:
            clone_data.update(additional_changes)
        
        # Use the underlying API post method directly with the cloned data
        api_params = {}
        if vdom:
            api_params['vdom'] = vdom
        return self._api.post(data=clone_data, **api_params)
    
    def enable(
        self,
        policy_id: Union[str, int],
        vdom: Optional[str] = None,
    ) -> Dict[str, Any]:
        """
        Enable a firewall policy.
        
        Args:
            policy_id: Policy ID to enable
            vdom: Virtual domain name (optional)
            
        Returns:
            API response dictionary
            
        Example:
            >>> result = fgt.firewall.policy.enable(policy_id=1)
        """
        return self.update(policy_id=policy_id, status='enable', vdom=vdom)
    
    def disable(
        self,
        policy_id: Union[str, int],
        vdom: Optional[str] = None,
    ) -> Dict[str, Any]:
        """
        Disable a firewall policy.
        
        Args:
            policy_id: Policy ID to disable
            vdom: Virtual domain name (optional)
            
        Returns:
            API response dictionary
            
        Example:
            >>> result = fgt.firewall.policy.disable(policy_id=1)
        """
        return self.update(policy_id=policy_id, status='disable', vdom=vdom)
    
    def get_by_name(
        self,
        name: str,
        vdom: Optional[str] = None,
    ) -> Optional[Dict[str, Any]]:
        """
        Get a firewall policy by name.
        
        Args:
            name: Policy name to search for
            vdom: Virtual domain name (optional)
            
        Returns:
            Policy data if found, None otherwise
            
        Example:
            >>> policy = fgt.firewall.policy.get_by_name('Allow-HTTP')
        """
        policies = self.get(filter=f'name=={name}', vdom=vdom)
        
        # Handle both dict and list responses
        if isinstance(policies, dict):
            results = policies.get('results', [])
        else:
            results = policies
        
        return results[0] if results else None
