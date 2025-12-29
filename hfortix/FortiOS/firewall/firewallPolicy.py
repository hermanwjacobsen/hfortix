"""
Firewall Policy Convenience Wrapper

Provides simplified syntax for firewall policy operations.
Instead of: fgt.api.cmdb.firewall.policy.post(data)
Use: fgt.firewall.policy.create(name='MyPolicy', srcintf=['port1'], ...)
"""

import logging
import sys
from typing import (  # noqa: F401
    TYPE_CHECKING,
    Any,
    Coroutine,
    Dict,
    List,
    Literal,
    Optional,
    Union,
    cast,
)

# Import shared helpers from the API layer
from ..api._helpers import build_cmdb_payload_normalized

# Import shared firewall helpers
from ._helpers import validate_address_pairs, validate_policy_id

if TYPE_CHECKING:
    from ..fortios import FortiOS


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
        self._logger = logging.getLogger("hfortix.firewall.policy")

    def _handle_error(
        self,
        operation: Any,
        error_mode: Optional[Literal["raise", "return", "print"]] = None,
        error_format: Optional[
            Literal["detailed", "simple", "code_only"]
        ] = None,  # noqa: E501
    ) -> Any:
        """
        Execute operation with configurable error handling.

        Args:
            operation: Callable that performs the API operation
            error_mode: Override default error mode ("raise", "return", "print")
            error_format: Override default error format ("detailed", "simple", "code_only")  # noqa: E501

        Returns:
            Operation result or error dict depending on error_mode
        """
        # Use instance defaults if not overridden
        mode = error_mode if error_mode is not None else self._fgt.error_mode
        fmt = (
            error_format
            if error_format is not None
            else self._fgt.error_format
        )  # noqa: E501

        try:
            # Execute the operation
            return operation()
        except Exception as e:
            # Handle based on error mode
            if mode == "raise":
                # Re-raise the exception (default behavior)
                raise
            elif mode == "return":
                # Return error as dict
                error_dict: Dict[str, Any] = {
                    "status": "error",
                    "error": str(e),
                }

                # Add details based on format
                if fmt == "detailed":
                    # Full exception details
                    error_dict["exception_type"] = type(e).__name__
                    if hasattr(e, "http_status"):
                        error_dict["http_status"] = getattr(e, "http_status")
                    if hasattr(e, "error_code"):
                        error_dict["error_code"] = getattr(e, "error_code")
                    if hasattr(e, "endpoint"):
                        error_dict["endpoint"] = getattr(e, "endpoint")
                    if hasattr(e, "method"):
                        error_dict["method"] = getattr(e, "method")
                elif fmt == "simple":
                    # Just type and message
                    error_dict["exception_type"] = type(e).__name__
                    if hasattr(e, "error_code"):
                        error_dict["error_code"] = getattr(e, "error_code")
                elif fmt == "code_only":
                    # Just the error code
                    if hasattr(e, "error_code"):
                        error_dict["error_code"] = getattr(e, "error_code")
                    else:
                        error_dict["error_code"] = -1  # Unknown error

                return error_dict
            elif mode == "print":
                # Print error and return None
                if fmt == "detailed":
                    print(
                        f"ERROR: {type(e).__name__}: {str(e)}", file=sys.stderr
                    )
                elif fmt == "simple":
                    print(f"ERROR: {str(e)}", file=sys.stderr)
                elif fmt == "code_only":
                    if hasattr(e, "error_code"):
                        error_code = getattr(e, "error_code")
                        print(f"ERROR CODE: {error_code}", file=sys.stderr)
                    else:
                        print("ERROR CODE: -1", file=sys.stderr)
                return None
            else:
                # Shouldn't happen, but raise if invalid mode
                raise ValueError(f"Invalid error_mode: {mode}")

    def create(
        self,
        # Core required parameters
        name: str,
        srcintf: Union[str, List[str]],
        dstintf: Union[str, List[str]],
        service: Union[str, List[str]],
        # Source/Destination addresses (at least one of each pair required)
        srcaddr: Optional[Union[str, List[str]]] = None,
        dstaddr: Optional[Union[str, List[str]]] = None,
        # Core optional parameters
        action: Optional[str] = None,
        schedule: str = "always",
        status: Optional[str] = None,
        # IPv6 addresses (alternative to srcaddr/dstaddr)
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
        internet_service_src_custom_group: Optional[
            Union[str, List[str]]
        ] = None,
        network_service_src_dynamic: Optional[Union[str, List[str]]] = None,
        internet_service_src_fortiguard: Optional[
            Union[str, List[str]]
        ] = None,
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
        internet_service6_src_custom_group: Optional[
            Union[str, List[str]]
        ] = None,
        internet_service6_src_fortiguard: Optional[
            Union[str, List[str]]
        ] = None,
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
        raw_json: Optional[bool] = None,
        # Catch-all for any additional fields
        data: Optional[Dict[str, Any]] = None,
        # Error handling configuration
        error_mode: Optional[Literal["raise", "return", "print"]] = None,
        error_format: Optional[
            Literal["detailed", "simple", "code_only"]
        ] = None,  # noqa: E501
    ) -> Union[Dict[str, Any], "Coroutine[Any, Any, Dict[str, Any]]"]:
        """
        Create a new firewall policy with all available FortiOS parameters.

        Args:
            # Core required parameters
            name: Policy name (required)
            srcintf: Source interface(s) - string or list (required)
            dstintf: Destination interface(s) - string or list (required)
            service: Service(s) - string or list (required)

            # Address pairs (at least one complete pair required)
            # IPv4 pair - must provide BOTH srcaddr AND dstaddr together
            srcaddr: Source IPv4 address(es) - string or list
                (required with dstaddr)
            dstaddr: Destination IPv4 address(es) - string or list
                (required with srcaddr)

            # IPv6 pair - must provide BOTH srcaddr6 AND dstaddr6 together
            srcaddr6: Source IPv6 address(es) - string or list
                (required with dstaddr6)
            dstaddr6: Destination IPv6 address(es) - string or list
                (required with srcaddr6)

            # Note: You must provide at least one complete pair
            # (IPv4 OR IPv6 OR both)

            # Core optional parameters
            action: Policy action ('accept', 'deny', 'ipsec')
            schedule: Schedule name (default: "always")
            status: Enable/disable policy ('enable', 'disable')

            # Internet Services (IPv4) - Destination
            internet_service: Enable/disable Internet Services ('enable',
            'disable')
            internet_service_name: Internet Service name(s) - string or list
            internet_service_group: Internet Service group(s) - string or list
            internet_service_custom: Custom Internet Service(s) - string or
            list
            internet_service_custom_group: Custom Internet Service group(s) -
            string or list
            network_service_dynamic: Dynamic network service(s) - string or
            list
            internet_service_fortiguard: FortiGuard Internet Service(s) -
            string or list
            internet_service_negate: Negate Internet Service match ('enable',
            'disable')

            # Internet Services (IPv4) - Source
            internet_service_src: Enable/disable source Internet Services
            ('enable', 'disable')
            internet_service_src_name: Source Internet Service name(s) - string
            or list
            internet_service_src_group: Source Internet Service group(s) -
            string or list
            internet_service_src_custom: Source Custom Internet Service(s) -
            string or list
            internet_service_src_custom_group: Source Custom Internet Service
            group(s) - string or list
            network_service_src_dynamic: Source dynamic network service(s) -
            string or list
            internet_service_src_fortiguard: Source FortiGuard Internet
            Service(s) - string or list
            internet_service_src_negate: Negate source Internet Service match
            ('enable', 'disable')

            # Internet Services (IPv6) - Destination
            internet_service6: Enable/disable IPv6 Internet Services ('enable',
            'disable')
            internet_service6_name: IPv6 Internet Service name(s) - string or
            list
            internet_service6_group: IPv6 Internet Service group(s) - string or
            list
            internet_service6_custom: IPv6 Custom Internet Service(s) - string
            or list
            internet_service6_custom_group: IPv6 Custom Internet Service
            group(s) - string or list
            internet_service6_fortiguard: IPv6 FortiGuard Internet Service(s) -
            string or list
            internet_service6_negate: Negate IPv6 Internet Service match
            ('enable', 'disable')

            # Internet Services (IPv6) - Source
            internet_service6_src: Enable/disable source IPv6 Internet Services
            ('enable', 'disable')
            internet_service6_src_name: Source IPv6 Internet Service name(s) -
            string or list
            internet_service6_src_group: Source IPv6 Internet Service group(s)
            - string or list
            internet_service6_src_custom: Source IPv6 Custom Internet
            Service(s) - string or list
            internet_service6_src_custom_group: Source IPv6 Custom Internet
            Service group(s) - string or list
            internet_service6_src_fortiguard: Source IPv6 FortiGuard Internet
            Service(s) - string or list
            internet_service6_src_negate: Negate source IPv6 Internet Service
            match ('enable', 'disable')

            # Reputation
            reputation_minimum: Minimum reputation score (0-100)
            reputation_direction: Reputation direction ('source',
            'destination')
            reputation_minimum6: Minimum IPv6 reputation score (0-100)
            reputation_direction6: IPv6 reputation direction ('source',
            'destination')

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
            ztna_ems_tag_negate: Negate ZTNA EMS tag match ('enable',
            'disable')
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
            passive_wan_health_measurement: Passive WAN health measurement
            ('enable', 'disable')
            app_monitor: Application monitor ('enable', 'disable')
            captive_portal_exempt: Captive portal exempt ('enable', 'disable')
            decrypted_traffic_mirror: Decrypted traffic mirror name
            dynamic_shaping: Enable dynamic shaping ('enable', 'disable')
            fec: Enable Forward Error Correction ('enable', 'disable')

            # Session Control
            send_deny_packet: Send deny packet ('enable', 'disable')
            firewall_session_dirty: Firewall session dirty ('check-all',
            'check-new')
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
            tcp_session_without_syn: TCP session without SYN ('enable',
            'disable')
            anti_replay: Enable anti-replay ('enable', 'disable')
            tos: Type of Service (ToS) value
            tos_mask: ToS mask
            tos_negate: Negate ToS match ('enable', 'disable')

            # Geo-IP
            geoip_anycast: Geo-IP anycast ('enable', 'disable')
            geoip_match: Geo-IP match ('physical-location',
            'registered-location')

            # Security Groups
            sgt_check: Security Group Tag check ('enable', 'disable')
            sgt: Security Group Tag(s) - string or list

            # Performance
            auto_asic_offload: Auto ASIC offload ('enable', 'disable')
            np_acceleration: Network processor acceleration ('enable',
            'disable')
            delay_tcp_npu_session: Delay TCP NPU session ('enable', 'disable')

            # VIP Matching
            match_vip: Match VIP ('enable', 'disable')
            match_vip_only: Match VIP only ('enable', 'disable')

            # RADIUS Bypass
            radius_mac_auth_bypass: RADIUS MAC auth bypass ('enable',
            'disable')
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
            dstaddr_negate: Negate destination address match ('enable',
            'disable')
            srcaddr6_negate: Negate source IPv6 address match ('enable',
            'disable')
            dstaddr6_negate: Negate destination IPv6 address match ('enable',
            'disable')
            service_negate: Negate service match ('enable', 'disable')

            # Comments
            comments: Policy comments

            # API Parameters
            vdom: Virtual domain name
            datasource: Include datasource in response
            with_meta: Include metadata in response
            data: Additional fields as dictionary (merged with explicit
            parameters)

            # Error Handling (can override FortiOS instance defaults)
            error_mode: How to handle errors for this call only
                - "raise": Raise exception (stops program unless caught)
                - "return": Return error dict (program continues)
                - "log": Log error and return None (program continues)
                If not specified, uses the FortiOS instance default
            error_format: Error message detail level for this call only
                - "detailed": Full context with endpoint, hints, parameters
                - "simple": Just error message and code
                - "code_only": Just the error code number
                If not specified, uses the FortiOS instance default

        Returns:
            API response dictionary (on success)
            Error dictionary (if error_mode="return" and error occurs)
            None (if error_mode="log" and error occurs)

        Raises:
            Various APIError exceptions (if error_mode="raise" and
                error occurs)

        Example:
            >>> # Simple IPv4 policy (schedule defaults to "always")
            >>> result = fgt.firewall.policy.create(
            ...     name='Allow-Web-Traffic',
            ...     srcintf='port1',
            ...     dstintf='port2',
            ...     srcaddr='internal-net',
            ...     dstaddr='all',
            ...     service=['HTTP', 'HTTPS'],
            ...     action='accept'
            ... )

            >>> # IPv6 policy
            >>> result = fgt.firewall.policy.create(
            ...     name='Allow-IPv6-Web',
            ...     srcintf='port1',
            ...     dstintf='port2',
            ...     srcaddr6='internal-net-v6',
            ...     dstaddr6='all',
            ...     service=['HTTP', 'HTTPS'],
            ...     action='accept'
            ... )

            >>> # Dual-stack policy (both IPv4 and IPv6)
            >>> result = fgt.firewall.policy.create(
            ...     name='Allow-DualStack-Web',
            ...     srcintf='port1',
            ...     dstintf='port2',
            ...     srcaddr='internal-net',
            ...     srcaddr6='internal-net-v6',
            ...     dstaddr='all',
            ...     dstaddr6='all',
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
            ...     schedule='business-hours',  # Override default
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
        # Validate address pairs using shared helper
        validate_address_pairs(srcaddr, dstaddr, srcaddr6, dstaddr6)

        # Use the shared builder function to construct the policy payload
        policy_data = build_cmdb_payload_normalized(
            name=name,
            srcintf=srcintf,
            dstintf=dstintf,
            srcaddr=srcaddr,
            dstaddr=dstaddr,
            action=action,
            schedule=schedule,
            service=service,
            status=status,
            srcaddr6=srcaddr6,
            dstaddr6=dstaddr6,
            internet_service=internet_service,
            internet_service_name=internet_service_name,
            internet_service_group=internet_service_group,
            internet_service_custom=internet_service_custom,
            internet_service_custom_group=internet_service_custom_group,
            network_service_dynamic=network_service_dynamic,
            internet_service_fortiguard=internet_service_fortiguard,
            internet_service_negate=internet_service_negate,
            internet_service_src=internet_service_src,
            internet_service_src_name=internet_service_src_name,
            internet_service_src_group=internet_service_src_group,
            internet_service_src_custom=internet_service_src_custom,
            internet_service_src_custom_group=internet_service_src_custom_group,  # noqa: E501
            network_service_src_dynamic=network_service_src_dynamic,
            internet_service_src_fortiguard=internet_service_src_fortiguard,
            internet_service_src_negate=internet_service_src_negate,
            internet_service6=internet_service6,
            internet_service6_name=internet_service6_name,
            internet_service6_group=internet_service6_group,
            internet_service6_custom=internet_service6_custom,
            internet_service6_custom_group=internet_service6_custom_group,
            internet_service6_fortiguard=internet_service6_fortiguard,
            internet_service6_negate=internet_service6_negate,
            internet_service6_src=internet_service6_src,
            internet_service6_src_name=internet_service6_src_name,
            internet_service6_src_group=internet_service6_src_group,
            internet_service6_src_custom=internet_service6_src_custom,
            internet_service6_src_custom_group=internet_service6_src_custom_group,  # noqa: E501
            internet_service6_src_fortiguard=internet_service6_src_fortiguard,
            internet_service6_src_negate=internet_service6_src_negate,
            reputation_minimum=reputation_minimum,
            reputation_direction=reputation_direction,
            reputation_minimum6=reputation_minimum6,
            reputation_direction6=reputation_direction6,
            rtp_nat=rtp_nat,
            rtp_addr=rtp_addr,
            ztna_status=ztna_status,
            ztna_device_ownership=ztna_device_ownership,
            ztna_ems_tag=ztna_ems_tag,
            ztna_ems_tag_secondary=ztna_ems_tag_secondary,
            ztna_tags_match_logic=ztna_tags_match_logic,
            ztna_geo_tag=ztna_geo_tag,
            ztna_ems_tag_negate=ztna_ems_tag_negate,
            ztna_policy_redirect=ztna_policy_redirect,
            src_vendor_mac=src_vendor_mac,
            inspection_mode=inspection_mode,
            utm_status=utm_status,
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
            http_policy_redirect=http_policy_redirect,
            ssh_policy_redirect=ssh_policy_redirect,
            webproxy_profile=webproxy_profile,
            webproxy_forward_server=webproxy_forward_server,
            nat=nat,
            nat64=nat64,
            nat46=nat46,
            ippool=ippool,
            poolname=poolname,
            poolname6=poolname6,
            natip=natip,
            fixedport=fixedport,
            permit_any_host=permit_any_host,
            permit_stun_host=permit_stun_host,
            port_preserve=port_preserve,
            port_random=port_random,
            pcp_outbound=pcp_outbound,
            pcp_inbound=pcp_inbound,
            pcp_poolname=pcp_poolname,
            vpntunnel=vpntunnel,
            inbound=inbound,
            outbound=outbound,
            natinbound=natinbound,
            natoutbound=natoutbound,
            users=users,
            groups=groups,
            fsso_groups=fsso_groups,
            fsso_agent_for_ntlm=fsso_agent_for_ntlm,
            ntlm=ntlm,
            ntlm_guest=ntlm_guest,
            ntlm_enabled_browsers=ntlm_enabled_browsers,
            auth_path=auth_path,
            auth_cert=auth_cert,
            auth_redirect_addr=auth_redirect_addr,
            disclaimer=disclaimer,
            email_collect=email_collect,
            traffic_shaper=traffic_shaper,
            traffic_shaper_reverse=traffic_shaper_reverse,
            per_ip_shaper=per_ip_shaper,
            logtraffic=logtraffic,
            logtraffic_start=logtraffic_start,
            log_http_transaction=log_http_transaction,
            capture_packet=capture_packet,
            custom_log_fields=custom_log_fields,
            wccp=wccp,
            passive_wan_health_measurement=passive_wan_health_measurement,
            app_monitor=app_monitor,
            captive_portal_exempt=captive_portal_exempt,
            decrypted_traffic_mirror=decrypted_traffic_mirror,
            dynamic_shaping=dynamic_shaping,
            fec=fec,
            send_deny_packet=send_deny_packet,
            firewall_session_dirty=firewall_session_dirty,
            schedule_timeout=schedule_timeout,
            policy_expiry=policy_expiry,
            policy_expiry_date=policy_expiry_date,
            policy_expiry_date_utc=policy_expiry_date_utc,
            session_ttl=session_ttl,
            timeout_send_rst=timeout_send_rst,
            vlan_cos_fwd=vlan_cos_fwd,
            vlan_cos_rev=vlan_cos_rev,
            vlan_filter=vlan_filter,
            diffserv_copy=diffserv_copy,
            diffserv_forward=diffserv_forward,
            diffserv_reverse=diffserv_reverse,
            diffservcode_forward=diffservcode_forward,
            diffservcode_rev=diffservcode_rev,
            tcp_mss_sender=tcp_mss_sender,
            tcp_mss_receiver=tcp_mss_receiver,
            tcp_session_without_syn=tcp_session_without_syn,
            anti_replay=anti_replay,
            tos=tos,
            tos_mask=tos_mask,
            tos_negate=tos_negate,
            geoip_anycast=geoip_anycast,
            geoip_match=geoip_match,
            sgt_check=sgt_check,
            sgt=sgt,
            auto_asic_offload=auto_asic_offload,
            np_acceleration=np_acceleration,
            delay_tcp_npu_session=delay_tcp_npu_session,
            match_vip=match_vip,
            match_vip_only=match_vip_only,
            radius_mac_auth_bypass=radius_mac_auth_bypass,
            radius_ip_auth_bypass=radius_ip_auth_bypass,
            dsri=dsri,
            identity_based_route=identity_based_route,
            redirect_url=redirect_url,
            block_notification=block_notification,
            replacemsg_override_group=replacemsg_override_group,
            srcaddr_negate=srcaddr_negate,
            dstaddr_negate=dstaddr_negate,
            srcaddr6_negate=srcaddr6_negate,
            dstaddr6_negate=dstaddr6_negate,
            service_negate=service_negate,
            comments=comments,
        )

        # Merge with additional data if provided
        if data:
            policy_data.update(data)

        # Build API parameters
        api_params: dict[str, Any] = {}
        if vdom:
            api_params["vdom"] = vdom
        if datasource is not None:
            api_params["datasource"] = datasource
        if with_meta is not None:
            api_params["with_meta"] = with_meta
        if raw_json is not None:
            api_params["raw_json"] = raw_json

        # Execute with error handling
        return self._handle_error(
            lambda: self._api.post(payload_dict=policy_data, **api_params),
            error_mode=error_mode,
            error_format=error_format,
        )

    def get(
        self,
        policy_id: Optional[Union[str, int]] = None,
        vdom: Optional[str] = None,
        filter: Optional[str] = None,
        raw_json: Optional[bool] = None,
        **kwargs,
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
        api_params: dict[str, Any] = {}
        if policy_id is not None:
            api_params["policyid"] = str(policy_id)
        if vdom:
            api_params["vdom"] = vdom
        if filter:
            api_params["filter"] = filter
        if raw_json is not None:
            api_params["raw_json"] = raw_json
        # Merge any additional kwargs
        api_params.update(kwargs)

        return cast(
            Union[Dict[str, Any], List[Dict[str, Any]]],
            self._api.get(**api_params),
        )

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
        internet_service_src_custom_group: Optional[
            Union[str, List[str]]
        ] = None,
        network_service_src_dynamic: Optional[Union[str, List[str]]] = None,
        internet_service_src_fortiguard: Optional[
            Union[str, List[str]]
        ] = None,
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
        internet_service6_src_custom_group: Optional[
            Union[str, List[str]]
        ] = None,
        internet_service6_src_fortiguard: Optional[
            Union[str, List[str]]
        ] = None,
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
        raw_json: Optional[bool] = None,
        # Catch-all for any additional fields
        data: Optional[Dict[str, Any]] = None,
    ) -> Union[Dict[str, Any], "Coroutine[Any, Any, Dict[str, Any]]"]:
        """
        Update an existing firewall policy.
        Update an existing firewall policy (partial update - only specify
        fields to change).
        All parameters same as create() but optional. See create() docstring
        for full parameter documentation.

        Args:
            policy_id: Policy ID to update (required)
            (All other parameters are optional - see create() method for
            details)

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
        # Validate policy_id
        validate_policy_id(policy_id, "update")

        # Use the shared builder function to construct the policy payload
        policy_data = build_cmdb_payload_normalized(
            name=name,
            srcintf=srcintf,
            dstintf=dstintf,
            srcaddr=srcaddr,
            dstaddr=dstaddr,
            action=action,
            schedule=schedule,
            service=service,
            status=status,
            srcaddr6=srcaddr6,
            dstaddr6=dstaddr6,
            internet_service=internet_service,
            internet_service_name=internet_service_name,
            internet_service_group=internet_service_group,
            internet_service_custom=internet_service_custom,
            internet_service_custom_group=internet_service_custom_group,
            network_service_dynamic=network_service_dynamic,
            internet_service_fortiguard=internet_service_fortiguard,
            internet_service_negate=internet_service_negate,
            internet_service_src=internet_service_src,
            internet_service_src_name=internet_service_src_name,
            internet_service_src_group=internet_service_src_group,
            internet_service_src_custom=internet_service_src_custom,
            internet_service_src_custom_group=internet_service_src_custom_group,  # noqa: E501
            network_service_src_dynamic=network_service_src_dynamic,
            internet_service_src_fortiguard=internet_service_src_fortiguard,
            internet_service_src_negate=internet_service_src_negate,
            internet_service6=internet_service6,
            internet_service6_name=internet_service6_name,
            internet_service6_group=internet_service6_group,
            internet_service6_custom=internet_service6_custom,
            internet_service6_custom_group=internet_service6_custom_group,
            internet_service6_fortiguard=internet_service6_fortiguard,
            internet_service6_negate=internet_service6_negate,
            internet_service6_src=internet_service6_src,
            internet_service6_src_name=internet_service6_src_name,
            internet_service6_src_group=internet_service6_src_group,
            internet_service6_src_custom=internet_service6_src_custom,
            internet_service6_src_custom_group=internet_service6_src_custom_group,  # noqa: E501
            internet_service6_src_fortiguard=internet_service6_src_fortiguard,
            internet_service6_src_negate=internet_service6_src_negate,
            reputation_minimum=reputation_minimum,
            reputation_direction=reputation_direction,
            reputation_minimum6=reputation_minimum6,
            reputation_direction6=reputation_direction6,
            rtp_nat=rtp_nat,
            rtp_addr=rtp_addr,
            ztna_status=ztna_status,
            ztna_device_ownership=ztna_device_ownership,
            ztna_ems_tag=ztna_ems_tag,
            ztna_ems_tag_secondary=ztna_ems_tag_secondary,
            ztna_tags_match_logic=ztna_tags_match_logic,
            ztna_geo_tag=ztna_geo_tag,
            ztna_ems_tag_negate=ztna_ems_tag_negate,
            ztna_policy_redirect=ztna_policy_redirect,
            src_vendor_mac=src_vendor_mac,
            inspection_mode=inspection_mode,
            utm_status=utm_status,
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
            http_policy_redirect=http_policy_redirect,
            ssh_policy_redirect=ssh_policy_redirect,
            webproxy_profile=webproxy_profile,
            webproxy_forward_server=webproxy_forward_server,
            nat=nat,
            nat64=nat64,
            nat46=nat46,
            ippool=ippool,
            poolname=poolname,
            poolname6=poolname6,
            natip=natip,
            fixedport=fixedport,
            permit_any_host=permit_any_host,
            permit_stun_host=permit_stun_host,
            port_preserve=port_preserve,
            port_random=port_random,
            pcp_outbound=pcp_outbound,
            pcp_inbound=pcp_inbound,
            pcp_poolname=pcp_poolname,
            vpntunnel=vpntunnel,
            inbound=inbound,
            outbound=outbound,
            natinbound=natinbound,
            natoutbound=natoutbound,
            users=users,
            groups=groups,
            fsso_groups=fsso_groups,
            fsso_agent_for_ntlm=fsso_agent_for_ntlm,
            ntlm=ntlm,
            ntlm_guest=ntlm_guest,
            ntlm_enabled_browsers=ntlm_enabled_browsers,
            auth_path=auth_path,
            auth_cert=auth_cert,
            auth_redirect_addr=auth_redirect_addr,
            disclaimer=disclaimer,
            email_collect=email_collect,
            traffic_shaper=traffic_shaper,
            traffic_shaper_reverse=traffic_shaper_reverse,
            per_ip_shaper=per_ip_shaper,
            logtraffic=logtraffic,
            logtraffic_start=logtraffic_start,
            log_http_transaction=log_http_transaction,
            capture_packet=capture_packet,
            custom_log_fields=custom_log_fields,
            wccp=wccp,
            passive_wan_health_measurement=passive_wan_health_measurement,
            app_monitor=app_monitor,
            captive_portal_exempt=captive_portal_exempt,
            decrypted_traffic_mirror=decrypted_traffic_mirror,
            dynamic_shaping=dynamic_shaping,
            fec=fec,
            send_deny_packet=send_deny_packet,
            firewall_session_dirty=firewall_session_dirty,
            schedule_timeout=schedule_timeout,
            policy_expiry=policy_expiry,
            policy_expiry_date=policy_expiry_date,
            policy_expiry_date_utc=policy_expiry_date_utc,
            session_ttl=session_ttl,
            timeout_send_rst=timeout_send_rst,
            vlan_cos_fwd=vlan_cos_fwd,
            vlan_cos_rev=vlan_cos_rev,
            vlan_filter=vlan_filter,
            diffserv_copy=diffserv_copy,
            diffserv_forward=diffserv_forward,
            diffserv_reverse=diffserv_reverse,
            diffservcode_forward=diffservcode_forward,
            diffservcode_rev=diffservcode_rev,
            tcp_mss_sender=tcp_mss_sender,
            tcp_mss_receiver=tcp_mss_receiver,
            tcp_session_without_syn=tcp_session_without_syn,
            anti_replay=anti_replay,
            tos=tos,
            tos_mask=tos_mask,
            tos_negate=tos_negate,
            geoip_anycast=geoip_anycast,
            geoip_match=geoip_match,
            sgt_check=sgt_check,
            sgt=sgt,
            auto_asic_offload=auto_asic_offload,
            np_acceleration=np_acceleration,
            delay_tcp_npu_session=delay_tcp_npu_session,
            match_vip=match_vip,
            match_vip_only=match_vip_only,
            radius_mac_auth_bypass=radius_mac_auth_bypass,
            radius_ip_auth_bypass=radius_ip_auth_bypass,
            dsri=dsri,
            identity_based_route=identity_based_route,
            redirect_url=redirect_url,
            block_notification=block_notification,
            replacemsg_override_group=replacemsg_override_group,
            srcaddr_negate=srcaddr_negate,
            dstaddr_negate=dstaddr_negate,
            srcaddr6_negate=srcaddr6_negate,
            dstaddr6_negate=dstaddr6_negate,
            service_negate=service_negate,
            comments=comments,
        )

        # Merge with additional data if provided
        if data:
            policy_data.update(data)

        # Build API parameters
        api_params: dict[str, Any] = {}
        if vdom:
            api_params["vdom"] = vdom
        if datasource is not None:
            api_params["datasource"] = datasource
        if with_meta is not None:
            api_params["with_meta"] = with_meta
        if raw_json is not None:
            api_params["raw_json"] = raw_json

        return self._api.put(
            policyid=str(policy_id),
            payload_dict=policy_data,
            **api_params,
        )

    def delete(
        self,
        policy_id: Union[str, int],
        vdom: Optional[str] = None,
        raw_json: Optional[bool] = None,
    ) -> Union[Dict[str, Any], "Coroutine[Any, Any, Dict[str, Any]]"]:
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
        # Validate policy_id
        validate_policy_id(policy_id, "delete")

        api_params: dict[str, Any] = {}
        if vdom:
            api_params["vdom"] = vdom
        if raw_json is not None:
            api_params["raw_json"] = raw_json

        return self._api.delete(policyid=str(policy_id), **api_params)

    def exists(
        self,
        policy_id: Optional[Union[str, int]] = None,
        name: Optional[str] = None,
        vdom: Optional[str] = None,
    ) -> Union[bool, Coroutine[Any, Any, bool]]:
        """
        Check if a firewall policy exists by ID or name.

        Args:
            policy_id: Policy ID to check (optional if name is provided)
            name: Policy name to check (optional if policy_id is provided)
            vdom: Virtual domain name (optional)

        Returns:
            True if policy exists, False otherwise

        Raises:
            ValueError: If neither policy_id nor name is provided

        Examples:
            >>> # Check by policy ID
            >>> if fgt.firewall.policy.exists(policy_id=1):
            ...     print("Policy exists")

            >>> # Check by policy name
            >>> if fgt.firewall.policy.exists(
            ...     name="Allow-Web-Traffic"
            ... ):
            ...     print("Policy exists")
        """
        # Validate that at least one identifier is provided
        if not policy_id and not name:
            raise ValueError("Either policy_id or name must be provided")

        # If name is provided, use get_by_name
        # (less efficient but more flexible)
        if name:
            try:
                policy = self.get_by_name(name=name, vdom=vdom)
                return policy is not None and policy != {}
            except Exception:
                return False

        # Original logic for policy_id (more efficient direct API call)
        validate_policy_id(policy_id, "exists")
        try:
            return self._api.exists(policyid=str(policy_id), vdom=vdom)
        except Exception:
            return False

    def move(
        self,
        policy_id: Union[str, int],
        position: str,
        reference_id: Optional[Union[str, int]] = None,
        vdom: Optional[str] = None,
        raw_json: Optional[bool] = None,
    ) -> Dict[str, Any]:
        """
        Move a firewall policy to a different position.

        Args:
            policy_id: Policy ID to move
            position: Position ('before', 'after', 'top', or 'bottom')
            reference_id: Reference policy ID (required for 'before'/'after',
            ignored for 'top'/'bottom')
            vdom: Virtual domain name (optional)

        Returns:
            API response dictionary

        Examples:
            >>> # Move policy 5 before policy 3
            >>> result = fgt.firewall.policy.move(policy_id=5,
            position='before', reference_id=3)

            >>> # Move policy 10 to the top
            >>> result = fgt.firewall.policy.move(policy_id=10, position='top')

            >>> # Move policy 15 to the bottom
            >>> result = fgt.firewall.policy.move(policy_id=15,
            position='bottom')
        """
        # Validate policy_id
        validate_policy_id(policy_id, "move")

        # Build move-specific parameters
        move_kwargs: Dict[str, Any] = {"action": "move"}

        # Add the position parameter
        if position in ("before", "after"):
            if reference_id is None:
                raise ValueError(
                    f"reference_id is required when position is '{position}'"
                )
            move_kwargs[position] = str(reference_id)
        elif position == "top":
            # To move to top, we need to find the first policy and use 'before'
            policies_raw = self.get(vdom=vdom)
            # Ensure we have a list of policy dicts
            if isinstance(policies_raw, dict):
                policies: list[dict[str, Any]] = policies_raw.get(
                    "results", []
                )
            else:
                policies = policies_raw
            if not policies:
                raise ValueError("Cannot move to top: no policies found")
            # Get the first policy ID (policies are returned in order)
            # Exclude the policy being moved from consideration
            for policy in policies:
                first_policy_id = policy["policyid"]
                if str(first_policy_id) != str(policy_id):
                    break
            else:
                # All policies are the same ID? Already at top if only one
                # policy
                return {
                    "status": "success",
                    "message": "Policy already at top",
                }
            # Don't move if already at the top
            if str(policies[0]["policyid"]) == str(policy_id):
                return {
                    "status": "success",
                    "message": "Policy already at top",
                }
            move_kwargs["before"] = str(first_policy_id)
        elif position == "bottom":
            # To move to bottom, we need to find the last policy and use
            # 'after'
            policies_raw = self.get(vdom=vdom)
            # Ensure we have a list of policy dicts
            if isinstance(policies_raw, dict):
                policies_bottom: list[dict[str, Any]] = policies_raw.get(
                    "results", []
                )
            else:
                policies_bottom = policies_raw
            if not policies_bottom:
                raise ValueError("Cannot move to bottom: no policies found")
            # Get the last policy ID, excluding the policy being moved
            for policy in reversed(policies_bottom):
                last_policy_id = policy["policyid"]
                if str(last_policy_id) != str(policy_id):
                    break
            else:
                # All policies are the same ID? Already at bottom if only one
                # policy
                return {
                    "status": "success",
                    "message": "Policy already at bottom",
                }
            # Don't move if already at the bottom
            if str(policies_bottom[-1]["policyid"]) == str(policy_id):
                return {
                    "status": "success",
                    "message": "Policy already at bottom",
                }
            move_kwargs["after"] = str(last_policy_id)
        else:
            raise ValueError(
                f"Invalid position: {position}. Must be 'before', 'after', 'top', or 'bottom'"  # noqa: E501
            )

        # Call the API using the HTTP client directly with params
        # We need to use the HTTP client directly because move uses query
        # params,
        # not data payload
        endpoint = f"firewall/policy/{policy_id}"

        # Build the call parameters
        call_params: dict[str, Any] = {
            "data": {},
            "params": move_kwargs,
        }
        if vdom:
            call_params["vdom"] = vdom
        if raw_json is not None:
            call_params["raw_json"] = raw_json

        # Type ignore: client can be sync or async, runtime returns
        # Dict[str, Any]
        return self._fgt._client.put(  # type: ignore[return-value]
            "cmdb", endpoint, **call_params
        )

    def clone(
        self,
        policy_id: Union[str, int],
        new_name: Optional[str] = None,
        status: Optional[str] = None,
        vdom: Optional[str] = None,
        additional_changes: Optional[Dict[str, Any]] = None,
    ) -> Union[Dict[str, Any], "Coroutine[Any, Any, Dict[str, Any]]"]:
        """
        Clone an existing firewall policy.

        Args:
            policy_id: Policy ID to clone
            new_name: Name for the cloned policy (optional, will auto-generate
            if not provided)
            status: Status for cloned policy - 'enable' or 'disable' (optional,
            defaults to original)
            vdom: Virtual domain name (optional)
            additional_changes: Additional field changes as dictionary
            (optional)

        Returns:
            API response dictionary

        Examples:
            >>> # Clone policy 1 with a new name
            >>> result = fgt.firewall.policy.clone(policy_id=1,
            new_name='Cloned-Policy')

            >>> # Clone and disable
            >>> result = fgt.firewall.policy.clone(policy_id=1,
            new_name='Test-Policy', status='disable')

            >>> # Clone with additional changes
            >>> result = fgt.firewall.policy.clone(
            ...     policy_id=1,
            ...     new_name='Modified-Clone',
            ...     status='disable',
            ...     additional_changes={'comments': 'Testing clone feature'}
            ... )
        """
        # Validate policy_id
        validate_policy_id(policy_id, "clone")

        # Get the original policy
        original_response = self.get(policy_id=policy_id, vdom=vdom)

        # Handle response format
        if (
            isinstance(original_response, dict)
            and "results" in original_response
        ):
            original = (
                original_response["results"][0]
                if original_response["results"]
                else {}
            )
        elif isinstance(original_response, list):
            original = original_response[0] if original_response else {}
        else:
            original = original_response

        # Remove fields that shouldn't be copied
        clone_data = {
            k: v
            for k, v in original.items()
            if k not in ("policyid", "uuid", "q_origin_key")
        }

        # Apply name change
        if new_name:
            clone_data["name"] = new_name
        else:
            # Auto-generate name if not provided
            original_name = clone_data.get("name", "Policy")
            clone_data["name"] = f"{original_name}-Clone"

        # Apply status change
        if status:
            clone_data["status"] = status

        # Apply additional changes
        if additional_changes:
            clone_data.update(additional_changes)

        # Use the underlying API post method directly with the cloned data
        api_params: dict[str, Any] = {}
        if vdom:
            api_params["vdom"] = vdom

        return self._api.post(data=clone_data, **api_params)

    def rename(
        self,
        policy_id: Union[str, int],
        new_name: str,
        vdom: Optional[str] = None,
    ) -> Union[Dict[str, Any], "Coroutine[Any, Any, Dict[str, Any]]"]:
        """
        Rename a firewall policy.

        Args:
            policy_id: Policy ID to rename
            new_name: New name for the policy
            vdom: Virtual domain name (optional)

        Returns:
            API response dictionary

        Example:
            >>> result = fgt.firewall.policy.rename(
            ...     policy_id=1,
            ...     new_name='Updated-Policy-Name'
            ... )
        """
        # Validate policy_id
        validate_policy_id(policy_id, "rename")

        # Simply update the name field
        return self.update(policy_id=policy_id, name=new_name, vdom=vdom)

    def enable(
        self,
        policy_id: Union[str, int],
        vdom: Optional[str] = None,
    ) -> Union[Dict[str, Any], "Coroutine[Any, Any, Dict[str, Any]]"]:
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
        # Validate policy_id
        validate_policy_id(policy_id, "enable")

        return self.update(policy_id=policy_id, status="enable", vdom=vdom)

    def disable(
        self,
        policy_id: Union[str, int],
        vdom: Optional[str] = None,
    ) -> Union[Dict[str, Any], "Coroutine[Any, Any, Dict[str, Any]]"]:
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
        # Validate policy_id
        validate_policy_id(policy_id, "disable")

        return self.update(policy_id=policy_id, status="disable", vdom=vdom)

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
        policies = self.get(filter=f"name=={name}", vdom=vdom)

        # Handle both dict and list responses
        if isinstance(policies, dict):
            results = policies.get("results", [])
        else:
            results = policies

        return results[0] if results else None
