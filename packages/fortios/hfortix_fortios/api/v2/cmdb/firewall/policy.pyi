from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject
from hfortix_core.types import MutationResponse, RawAPIResponse

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class PolicyPayload(TypedDict, total=False):
    """
    Type hints for firewall/policy payload fields.
    
    Configure IPv4/IPv6 policies.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.antivirus.profile.ProfileEndpoint` (via: av-profile)
        - :class:`~.application.list.ListEndpoint` (via: application-list)
        - :class:`~.casb.profile.ProfileEndpoint` (via: casb-profile)
        - :class:`~.diameter-filter.profile.ProfileEndpoint` (via: diameter-filter-profile)
        - :class:`~.dlp.profile.ProfileEndpoint` (via: dlp-profile)
        - :class:`~.dnsfilter.profile.ProfileEndpoint` (via: dnsfilter-profile)
        - :class:`~.emailfilter.profile.ProfileEndpoint` (via: emailfilter-profile)
        - :class:`~.file-filter.profile.ProfileEndpoint` (via: file-filter-profile)
        - :class:`~.firewall.decrypted-traffic-mirror.DecryptedTrafficMirrorEndpoint` (via: decrypted-traffic-mirror)
        - :class:`~.firewall.identity-based-route.IdentityBasedRouteEndpoint` (via: identity-based-route)
        - ... and 28 more dependencies

    **Usage:**
        payload: PolicyPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    policyid: int  # Policy ID (0 - 4294967294). | Default: 0 | Min: 0 | Max: 4294967294
    status: Literal["enable", "disable"]  # Enable or disable this policy. | Default: enable
    name: str  # Policy name. | MaxLen: 35
    uuid: str  # Universally Unique Identifier | Default: 00000000-0000-0000-0000-000000000000
    srcintf: list[dict[str, Any]]  # Incoming (ingress) interface.
    dstintf: list[dict[str, Any]]  # Outgoing (egress) interface.
    action: Literal["accept", "deny", "ipsec"]  # Policy action (accept/deny/ipsec). | Default: deny
    nat64: Literal["enable", "disable"]  # Enable/disable NAT64. | Default: disable
    nat46: Literal["enable", "disable"]  # Enable/disable NAT46. | Default: disable
    ztna_status: Literal["enable", "disable"]  # Enable/disable zero trust access. | Default: disable
    ztna_device_ownership: Literal["enable", "disable"]  # Enable/disable zero trust device ownership. | Default: disable
    srcaddr: list[dict[str, Any]]  # Source IPv4 address and address group names.
    dstaddr: list[dict[str, Any]]  # Destination IPv4 address and address group names.
    srcaddr6: list[dict[str, Any]]  # Source IPv6 address name and address group names.
    dstaddr6: list[dict[str, Any]]  # Destination IPv6 address name and address group na
    ztna_ems_tag: list[dict[str, Any]]  # Source ztna-ems-tag names.
    ztna_ems_tag_secondary: list[dict[str, Any]]  # Source ztna-ems-tag-secondary names.
    ztna_tags_match_logic: Literal["or", "and"]  # ZTNA tag matching logic. | Default: or
    ztna_geo_tag: list[dict[str, Any]]  # Source ztna-geo-tag names.
    internet_service: Literal["enable", "disable"]  # Enable/disable use of Internet Services for this p | Default: disable
    internet_service_name: list[dict[str, Any]]  # Internet Service name.
    internet_service_group: list[dict[str, Any]]  # Internet Service group name.
    internet_service_custom: list[dict[str, Any]]  # Custom Internet Service name.
    network_service_dynamic: list[dict[str, Any]]  # Dynamic Network Service name.
    internet_service_custom_group: list[dict[str, Any]]  # Custom Internet Service group name.
    internet_service_src: Literal["enable", "disable"]  # Enable/disable use of Internet Services in source | Default: disable
    internet_service_src_name: list[dict[str, Any]]  # Internet Service source name.
    internet_service_src_group: list[dict[str, Any]]  # Internet Service source group name.
    internet_service_src_custom: list[dict[str, Any]]  # Custom Internet Service source name.
    network_service_src_dynamic: list[dict[str, Any]]  # Dynamic Network Service source name.
    internet_service_src_custom_group: list[dict[str, Any]]  # Custom Internet Service source group name.
    reputation_minimum: int  # Minimum Reputation to take action. | Default: 0 | Min: 0 | Max: 4294967295
    reputation_direction: Literal["source", "destination"]  # Direction of the initial traffic for reputation to | Default: destination
    src_vendor_mac: list[dict[str, Any]]  # Vendor MAC source ID.
    internet_service6: Literal["enable", "disable"]  # Enable/disable use of IPv6 Internet Services for t | Default: disable
    internet_service6_name: list[dict[str, Any]]  # IPv6 Internet Service name.
    internet_service6_group: list[dict[str, Any]]  # Internet Service group name.
    internet_service6_custom: list[dict[str, Any]]  # Custom IPv6 Internet Service name.
    internet_service6_custom_group: list[dict[str, Any]]  # Custom Internet Service6 group name.
    internet_service6_src: Literal["enable", "disable"]  # Enable/disable use of IPv6 Internet Services in so | Default: disable
    internet_service6_src_name: list[dict[str, Any]]  # IPv6 Internet Service source name.
    internet_service6_src_group: list[dict[str, Any]]  # Internet Service6 source group name.
    internet_service6_src_custom: list[dict[str, Any]]  # Custom IPv6 Internet Service source name.
    internet_service6_src_custom_group: list[dict[str, Any]]  # Custom Internet Service6 source group name.
    reputation_minimum6: int  # IPv6 Minimum Reputation to take action. | Default: 0 | Min: 0 | Max: 4294967295
    reputation_direction6: Literal["source", "destination"]  # Direction of the initial traffic for IPv6 reputati | Default: destination
    rtp_nat: Literal["disable", "enable"]  # Enable Real Time Protocol (RTP) NAT. | Default: disable
    rtp_addr: list[dict[str, Any]]  # Address names if this is an RTP NAT policy.
    send_deny_packet: Literal["disable", "enable"]  # Enable to send a reply when a session is denied or | Default: disable
    firewall_session_dirty: Literal["check-all", "check-new"]  # How to handle sessions if the configuration of thi | Default: check-all
    schedule: str  # Schedule name. | MaxLen: 35
    schedule_timeout: Literal["enable", "disable"]  # Enable to force current sessions to end when the s | Default: disable
    policy_expiry: Literal["enable", "disable"]  # Enable/disable policy expiry. | Default: disable
    policy_expiry_date: str  # Policy expiry date (YYYY-MM-DD HH:MM:SS). | Default: 0000-00-00 00:00:00
    policy_expiry_date_utc: str  # Policy expiry date and time, in epoch format.
    service: list[dict[str, Any]]  # Service and service group names.
    tos_mask: str  # Non-zero bit positions are used for comparison whi
    tos: str  # ToS (Type of Service) value used for comparison.
    tos_negate: Literal["enable", "disable"]  # Enable negated TOS match. | Default: disable
    anti_replay: Literal["enable", "disable"]  # Enable/disable anti-replay check. | Default: enable
    tcp_session_without_syn: Literal["all", "data-only", "disable"]  # Enable/disable creation of TCP session without SYN | Default: disable
    geoip_anycast: Literal["enable", "disable"]  # Enable/disable recognition of anycast IP addresses | Default: disable
    geoip_match: Literal["physical-location", "registered-location"]  # Match geography address based either on its physic | Default: physical-location
    dynamic_shaping: Literal["enable", "disable"]  # Enable/disable dynamic RADIUS defined traffic shap | Default: disable
    passive_wan_health_measurement: Literal["enable", "disable"]  # Enable/disable passive WAN health measurement. Whe | Default: disable
    app_monitor: Literal["enable", "disable"]  # Enable/disable application TCP metrics in session | Default: disable
    utm_status: Literal["enable", "disable"]  # Enable to add one or more security profiles | Default: disable
    inspection_mode: Literal["proxy", "flow"]  # Policy inspection mode (Flow/proxy). Default is Fl | Default: flow
    http_policy_redirect: Literal["enable", "disable", "legacy"]  # Redirect HTTP(S) traffic to matching transparent w | Default: disable
    ssh_policy_redirect: Literal["enable", "disable"]  # Redirect SSH traffic to matching transparent proxy | Default: disable
    ztna_policy_redirect: Literal["enable", "disable"]  # Redirect ZTNA traffic to matching Access-Proxy pro | Default: disable
    webproxy_profile: str  # Webproxy profile name. | MaxLen: 63
    profile_type: Literal["single", "group"]  # Determine whether the firewall policy allows secur | Default: single
    profile_group: str  # Name of profile group. | MaxLen: 47
    profile_protocol_options: str  # Name of an existing Protocol options profile. | Default: default | MaxLen: 47
    ssl_ssh_profile: str  # Name of an existing SSL SSH profile. | Default: no-inspection | MaxLen: 47
    av_profile: str  # Name of an existing Antivirus profile. | MaxLen: 47
    webfilter_profile: str  # Name of an existing Web filter profile. | MaxLen: 47
    dnsfilter_profile: str  # Name of an existing DNS filter profile. | MaxLen: 47
    emailfilter_profile: str  # Name of an existing email filter profile. | MaxLen: 47
    dlp_profile: str  # Name of an existing DLP profile. | MaxLen: 47
    file_filter_profile: str  # Name of an existing file-filter profile. | MaxLen: 47
    ips_sensor: str  # Name of an existing IPS sensor. | MaxLen: 47
    application_list: str  # Name of an existing Application list. | MaxLen: 47
    voip_profile: str  # Name of an existing VoIP (voipd) profile. | MaxLen: 47
    ips_voip_filter: str  # Name of an existing VoIP (ips) profile. | MaxLen: 47
    sctp_filter_profile: str  # Name of an existing SCTP filter profile. | MaxLen: 47
    diameter_filter_profile: str  # Name of an existing Diameter filter profile. | MaxLen: 47
    virtual_patch_profile: str  # Name of an existing virtual-patch profile. | MaxLen: 47
    icap_profile: str  # Name of an existing ICAP profile. | MaxLen: 47
    videofilter_profile: str  # Name of an existing VideoFilter profile. | MaxLen: 47
    waf_profile: str  # Name of an existing Web application firewall profi | MaxLen: 47
    ssh_filter_profile: str  # Name of an existing SSH filter profile. | MaxLen: 47
    casb_profile: str  # Name of an existing CASB profile. | MaxLen: 47
    logtraffic: Literal["all", "utm", "disable"]  # Enable or disable logging. Log all sessions or sec | Default: utm
    logtraffic_start: Literal["enable", "disable"]  # Record logs when a session starts. | Default: disable
    log_http_transaction: Literal["enable", "disable"]  # Enable/disable HTTP transaction log. | Default: disable
    capture_packet: Literal["enable", "disable"]  # Enable/disable capture packets. | Default: disable
    auto_asic_offload: Literal["enable", "disable"]  # Enable/disable policy traffic ASIC offloading. | Default: enable
    wanopt: Literal["enable", "disable"]  # Enable/disable WAN optimization. | Default: disable
    wanopt_detection: Literal["active", "passive", "off"]  # WAN optimization auto-detection mode. | Default: active
    wanopt_passive_opt: Literal["default", "transparent", "non-transparent"]  # WAN optimization passive mode options. This option | Default: default
    wanopt_profile: str  # WAN optimization profile. | MaxLen: 35
    wanopt_peer: str  # WAN optimization peer. | MaxLen: 35
    webcache: Literal["enable", "disable"]  # Enable/disable web cache. | Default: disable
    webcache_https: Literal["disable", "enable"]  # Enable/disable web cache for HTTPS. | Default: disable
    webproxy_forward_server: str  # Webproxy forward server name. | MaxLen: 63
    traffic_shaper: str  # Traffic shaper. | MaxLen: 35
    traffic_shaper_reverse: str  # Reverse traffic shaper. | MaxLen: 35
    per_ip_shaper: str  # Per-IP traffic shaper. | MaxLen: 35
    nat: Literal["enable", "disable"]  # Enable/disable source NAT. | Default: disable
    pcp_outbound: Literal["enable", "disable"]  # Enable/disable PCP outbound SNAT. | Default: disable
    pcp_inbound: Literal["enable", "disable"]  # Enable/disable PCP inbound DNAT. | Default: disable
    pcp_poolname: list[dict[str, Any]]  # PCP pool names.
    permit_any_host: Literal["enable", "disable"]  # Enable/disable fullcone NAT. Accept UDP packets fr | Default: disable
    permit_stun_host: Literal["enable", "disable"]  # Accept UDP packets from any Session Traversal Util | Default: disable
    fixedport: Literal["enable", "disable"]  # Enable to prevent source NAT from changing a sessi | Default: disable
    port_preserve: Literal["enable", "disable"]  # Enable/disable preservation of the original source | Default: enable
    port_random: Literal["enable", "disable"]  # Enable/disable random source port selection for so | Default: disable
    ippool: Literal["enable", "disable"]  # Enable to use IP Pools for source NAT. | Default: disable
    poolname: list[dict[str, Any]]  # IP Pool names.
    poolname6: list[dict[str, Any]]  # IPv6 pool names.
    session_ttl: str  # TTL in seconds for sessions accepted by this polic
    vlan_cos_fwd: int  # VLAN forward direction user priority: 255 passthro | Default: 255 | Min: 0 | Max: 7
    vlan_cos_rev: int  # VLAN reverse direction user priority: 255 passthro | Default: 255 | Min: 0 | Max: 7
    inbound: Literal["enable", "disable"]  # Policy-based IPsec VPN: only traffic from the remo | Default: disable
    outbound: Literal["enable", "disable"]  # Policy-based IPsec VPN: only traffic from the inte | Default: enable
    natinbound: Literal["enable", "disable"]  # Policy-based IPsec VPN: apply destination NAT to i | Default: disable
    natoutbound: Literal["enable", "disable"]  # Policy-based IPsec VPN: apply source NAT to outbou | Default: disable
    fec: Literal["enable", "disable"]  # Enable/disable Forward Error Correction on traffic | Default: disable
    wccp: Literal["enable", "disable"]  # Enable/disable forwarding traffic matching this po | Default: disable
    ntlm: Literal["enable", "disable"]  # Enable/disable NTLM authentication. | Default: disable
    ntlm_guest: Literal["enable", "disable"]  # Enable/disable NTLM guest user access. | Default: disable
    ntlm_enabled_browsers: list[dict[str, Any]]  # HTTP-User-Agent value of supported browsers.
    fsso_agent_for_ntlm: str  # FSSO agent to use for NTLM authentication. | MaxLen: 35
    groups: list[dict[str, Any]]  # Names of user groups that can authenticate with th
    users: list[dict[str, Any]]  # Names of individual users that can authenticate wi
    fsso_groups: list[dict[str, Any]]  # Names of FSSO groups.
    auth_path: Literal["enable", "disable"]  # Enable/disable authentication-based routing. | Default: disable
    disclaimer: Literal["enable", "disable"]  # Enable/disable user authentication disclaimer. | Default: disable
    email_collect: Literal["enable", "disable"]  # Enable/disable email collection. | Default: disable
    vpntunnel: str  # Policy-based IPsec VPN: name of the IPsec VPN Phas | MaxLen: 35
    natip: str  # Policy-based IPsec VPN: source NAT IP address for | Default: 0.0.0.0 0.0.0.0
    match_vip: Literal["enable", "disable"]  # Enable to match packets that have had their destin | Default: enable
    match_vip_only: Literal["enable", "disable"]  # Enable/disable matching of only those packets that | Default: disable
    diffserv_copy: Literal["enable", "disable"]  # Enable to copy packet's DiffServ values from sessi | Default: disable
    diffserv_forward: Literal["enable", "disable"]  # Enable to change packet's DiffServ values to the s | Default: disable
    diffserv_reverse: Literal["enable", "disable"]  # Enable to change packet's reverse (reply) DiffServ | Default: disable
    diffservcode_forward: str  # Change packet's DiffServ to this value.
    diffservcode_rev: str  # Change packet's reverse (reply) DiffServ to this v
    tcp_mss_sender: int  # Sender TCP maximum segment size (MSS). | Default: 0 | Min: 0 | Max: 65535
    tcp_mss_receiver: int  # Receiver TCP maximum segment size (MSS). | Default: 0 | Min: 0 | Max: 65535
    comments: str  # Comment. | MaxLen: 1023
    auth_cert: str  # HTTPS server certificate for policy authentication | MaxLen: 35
    auth_redirect_addr: str  # HTTP-to-HTTPS redirect address for firewall authen | MaxLen: 63
    redirect_url: str  # URL users are directed to after seeing and accepti | MaxLen: 1023
    identity_based_route: str  # Name of identity-based routing rule. | MaxLen: 35
    block_notification: Literal["enable", "disable"]  # Enable/disable block notification. | Default: disable
    custom_log_fields: list[dict[str, Any]]  # Custom fields to append to log messages for this p
    replacemsg_override_group: str  # Override the default replacement message group for | MaxLen: 35
    srcaddr_negate: Literal["enable", "disable"]  # When enabled srcaddr specifies what the source add | Default: disable
    srcaddr6_negate: Literal["enable", "disable"]  # When enabled srcaddr6 specifies what the source ad | Default: disable
    dstaddr_negate: Literal["enable", "disable"]  # When enabled dstaddr specifies what the destinatio | Default: disable
    dstaddr6_negate: Literal["enable", "disable"]  # When enabled dstaddr6 specifies what the destinati | Default: disable
    ztna_ems_tag_negate: Literal["enable", "disable"]  # When enabled ztna-ems-tag specifies what the tags | Default: disable
    service_negate: Literal["enable", "disable"]  # When enabled service specifies what the service mu | Default: disable
    internet_service_negate: Literal["enable", "disable"]  # When enabled internet-service specifies what the s | Default: disable
    internet_service_src_negate: Literal["enable", "disable"]  # When enabled internet-service-src specifies what t | Default: disable
    internet_service6_negate: Literal["enable", "disable"]  # When enabled internet-service6 specifies what the | Default: disable
    internet_service6_src_negate: Literal["enable", "disable"]  # When enabled internet-service6-src specifies what | Default: disable
    timeout_send_rst: Literal["enable", "disable"]  # Enable/disable sending RST packets when TCP sessio | Default: disable
    captive_portal_exempt: Literal["enable", "disable"]  # Enable to exempt some users from the captive porta | Default: disable
    decrypted_traffic_mirror: str  # Decrypted traffic mirror. | MaxLen: 35
    dsri: Literal["enable", "disable"]  # Enable DSRI to ignore HTTP server responses. | Default: disable
    radius_mac_auth_bypass: Literal["enable", "disable"]  # Enable MAC authentication bypass. The bypassed MAC | Default: disable
    radius_ip_auth_bypass: Literal["enable", "disable"]  # Enable IP authentication bypass. The bypassed IP a | Default: disable
    delay_tcp_npu_session: Literal["enable", "disable"]  # Enable TCP NPU session delay to guarantee packet o | Default: disable
    vlan_filter: str  # VLAN ranges to allow
    sgt_check: Literal["enable", "disable"]  # Enable/disable security group tags (SGT) check. | Default: disable
    sgt: list[dict[str, Any]]  # Security group tags.
    internet_service_fortiguard: list[dict[str, Any]]  # FortiGuard Internet Service name.
    internet_service_src_fortiguard: list[dict[str, Any]]  # FortiGuard Internet Service source name.
    internet_service6_fortiguard: list[dict[str, Any]]  # FortiGuard IPv6 Internet Service name.
    internet_service6_src_fortiguard: list[dict[str, Any]]  # FortiGuard IPv6 Internet Service source name.

# Nested TypedDicts for table field children (dict mode)

class PolicySrcintfItem(TypedDict):
    """Type hints for srcintf table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # Interface name. | MaxLen: 79


class PolicyDstintfItem(TypedDict):
    """Type hints for dstintf table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # Interface name. | MaxLen: 79


class PolicySrcaddrItem(TypedDict):
    """Type hints for srcaddr table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # Address name. | MaxLen: 79


class PolicyDstaddrItem(TypedDict):
    """Type hints for dstaddr table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # Address name. | MaxLen: 79


class PolicySrcaddr6Item(TypedDict):
    """Type hints for srcaddr6 table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # Address name. | MaxLen: 79


class PolicyDstaddr6Item(TypedDict):
    """Type hints for dstaddr6 table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # Address name. | MaxLen: 79


class PolicyZtnaemstagItem(TypedDict):
    """Type hints for ztna-ems-tag table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # Address name. | MaxLen: 79


class PolicyZtnaemstagsecondaryItem(TypedDict):
    """Type hints for ztna-ems-tag-secondary table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # Address name. | MaxLen: 79


class PolicyZtnageotagItem(TypedDict):
    """Type hints for ztna-geo-tag table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # Address name. | MaxLen: 79


class PolicyInternetservicenameItem(TypedDict):
    """Type hints for internet-service-name table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # Internet Service name. | MaxLen: 79


class PolicyInternetservicegroupItem(TypedDict):
    """Type hints for internet-service-group table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # Internet Service group name. | MaxLen: 79


class PolicyInternetservicecustomItem(TypedDict):
    """Type hints for internet-service-custom table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # Custom Internet Service name. | MaxLen: 79


class PolicyNetworkservicedynamicItem(TypedDict):
    """Type hints for network-service-dynamic table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # Dynamic Network Service name. | MaxLen: 79


class PolicyInternetservicecustomgroupItem(TypedDict):
    """Type hints for internet-service-custom-group table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # Custom Internet Service group name. | MaxLen: 79


class PolicyInternetservicesrcnameItem(TypedDict):
    """Type hints for internet-service-src-name table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # Internet Service name. | MaxLen: 79


class PolicyInternetservicesrcgroupItem(TypedDict):
    """Type hints for internet-service-src-group table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # Internet Service group name. | MaxLen: 79


class PolicyInternetservicesrccustomItem(TypedDict):
    """Type hints for internet-service-src-custom table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # Custom Internet Service name. | MaxLen: 79


class PolicyNetworkservicesrcdynamicItem(TypedDict):
    """Type hints for network-service-src-dynamic table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # Dynamic Network Service name. | MaxLen: 79


class PolicyInternetservicesrccustomgroupItem(TypedDict):
    """Type hints for internet-service-src-custom-group table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # Custom Internet Service group name. | MaxLen: 79


class PolicySrcvendormacItem(TypedDict):
    """Type hints for src-vendor-mac table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    id: int  # Vendor MAC ID. | Default: 0 | Min: 0 | Max: 4294967295


class PolicyInternetservice6nameItem(TypedDict):
    """Type hints for internet-service6-name table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # IPv6 Internet Service name. | MaxLen: 79


class PolicyInternetservice6groupItem(TypedDict):
    """Type hints for internet-service6-group table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # Internet Service group name. | MaxLen: 79


class PolicyInternetservice6customItem(TypedDict):
    """Type hints for internet-service6-custom table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # Custom Internet Service name. | MaxLen: 79


class PolicyInternetservice6customgroupItem(TypedDict):
    """Type hints for internet-service6-custom-group table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # Custom Internet Service6 group name. | MaxLen: 79


class PolicyInternetservice6srcnameItem(TypedDict):
    """Type hints for internet-service6-src-name table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # Internet Service name. | MaxLen: 79


class PolicyInternetservice6srcgroupItem(TypedDict):
    """Type hints for internet-service6-src-group table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # Internet Service group name. | MaxLen: 79


class PolicyInternetservice6srccustomItem(TypedDict):
    """Type hints for internet-service6-src-custom table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # Custom Internet Service name. | MaxLen: 79


class PolicyInternetservice6srccustomgroupItem(TypedDict):
    """Type hints for internet-service6-src-custom-group table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # Custom Internet Service6 group name. | MaxLen: 79


class PolicyRtpaddrItem(TypedDict):
    """Type hints for rtp-addr table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # Address name. | MaxLen: 79


class PolicyServiceItem(TypedDict):
    """Type hints for service table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # Service and service group names. | MaxLen: 79


class PolicyPcppoolnameItem(TypedDict):
    """Type hints for pcp-poolname table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # PCP pool name. | MaxLen: 79


class PolicyPoolnameItem(TypedDict):
    """Type hints for poolname table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # IP pool name. | MaxLen: 79


class PolicyPoolname6Item(TypedDict):
    """Type hints for poolname6 table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # IPv6 pool name. | MaxLen: 79


class PolicyNtlmenabledbrowsersItem(TypedDict):
    """Type hints for ntlm-enabled-browsers table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    user_agent_string: str  # User agent string. | MaxLen: 79


class PolicyGroupsItem(TypedDict):
    """Type hints for groups table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # Group name. | MaxLen: 79


class PolicyUsersItem(TypedDict):
    """Type hints for users table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # Names of individual users that can authenticate wi | MaxLen: 79


class PolicyFssogroupsItem(TypedDict):
    """Type hints for fsso-groups table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # Names of FSSO groups. | MaxLen: 511


class PolicyCustomlogfieldsItem(TypedDict):
    """Type hints for custom-log-fields table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    field_id: str  # Custom log field. | MaxLen: 35


class PolicySgtItem(TypedDict):
    """Type hints for sgt table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    id: int  # Security group tag (1 - 65535). | Default: 0 | Min: 1 | Max: 65535


class PolicyInternetservicefortiguardItem(TypedDict):
    """Type hints for internet-service-fortiguard table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # FortiGuard Internet Service name. | MaxLen: 79


class PolicyInternetservicesrcfortiguardItem(TypedDict):
    """Type hints for internet-service-src-fortiguard table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # FortiGuard Internet Service name. | MaxLen: 79


class PolicyInternetservice6fortiguardItem(TypedDict):
    """Type hints for internet-service6-fortiguard table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # FortiGuard Internet Service name. | MaxLen: 79


class PolicyInternetservice6srcfortiguardItem(TypedDict):
    """Type hints for internet-service6-src-fortiguard table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # FortiGuard Internet Service name. | MaxLen: 79


# Nested classes for table field children (object mode)

@final
class PolicySrcintfObject:
    """Typed object for srcintf table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Interface name. | MaxLen: 79
    name: str
    
    # Methods from FortiObject
    @property
    def dict(self) -> dict[str, Any]:
        """Convert to dictionary."""
        ...
    @property
    def json(self) -> dict[str, Any]:
        """Convert to dictionary (alias for .dict)."""
        ...
    @property
    def raw(self) -> dict[str, Any]:
        """Get raw API response data."""
        ...
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> FortiObject: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


@final
class PolicyDstintfObject:
    """Typed object for dstintf table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Interface name. | MaxLen: 79
    name: str
    
    # Methods from FortiObject
    @property
    def dict(self) -> dict[str, Any]:
        """Convert to dictionary."""
        ...
    @property
    def json(self) -> dict[str, Any]:
        """Convert to dictionary (alias for .dict)."""
        ...
    @property
    def raw(self) -> dict[str, Any]:
        """Get raw API response data."""
        ...
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> FortiObject: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


@final
class PolicySrcaddrObject:
    """Typed object for srcaddr table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Address name. | MaxLen: 79
    name: str
    
    # Methods from FortiObject
    @property
    def dict(self) -> dict[str, Any]:
        """Convert to dictionary."""
        ...
    @property
    def json(self) -> dict[str, Any]:
        """Convert to dictionary (alias for .dict)."""
        ...
    @property
    def raw(self) -> dict[str, Any]:
        """Get raw API response data."""
        ...
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> FortiObject: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


@final
class PolicyDstaddrObject:
    """Typed object for dstaddr table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Address name. | MaxLen: 79
    name: str
    
    # Methods from FortiObject
    @property
    def dict(self) -> dict[str, Any]:
        """Convert to dictionary."""
        ...
    @property
    def json(self) -> dict[str, Any]:
        """Convert to dictionary (alias for .dict)."""
        ...
    @property
    def raw(self) -> dict[str, Any]:
        """Get raw API response data."""
        ...
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> FortiObject: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


@final
class PolicySrcaddr6Object:
    """Typed object for srcaddr6 table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Address name. | MaxLen: 79
    name: str
    
    # Methods from FortiObject
    @property
    def dict(self) -> dict[str, Any]:
        """Convert to dictionary."""
        ...
    @property
    def json(self) -> dict[str, Any]:
        """Convert to dictionary (alias for .dict)."""
        ...
    @property
    def raw(self) -> dict[str, Any]:
        """Get raw API response data."""
        ...
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> FortiObject: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


@final
class PolicyDstaddr6Object:
    """Typed object for dstaddr6 table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Address name. | MaxLen: 79
    name: str
    
    # Methods from FortiObject
    @property
    def dict(self) -> dict[str, Any]:
        """Convert to dictionary."""
        ...
    @property
    def json(self) -> dict[str, Any]:
        """Convert to dictionary (alias for .dict)."""
        ...
    @property
    def raw(self) -> dict[str, Any]:
        """Get raw API response data."""
        ...
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> FortiObject: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


@final
class PolicyZtnaemstagObject:
    """Typed object for ztna-ems-tag table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Address name. | MaxLen: 79
    name: str
    
    # Methods from FortiObject
    @property
    def dict(self) -> dict[str, Any]:
        """Convert to dictionary."""
        ...
    @property
    def json(self) -> dict[str, Any]:
        """Convert to dictionary (alias for .dict)."""
        ...
    @property
    def raw(self) -> dict[str, Any]:
        """Get raw API response data."""
        ...
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> FortiObject: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


@final
class PolicyZtnaemstagsecondaryObject:
    """Typed object for ztna-ems-tag-secondary table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Address name. | MaxLen: 79
    name: str
    
    # Methods from FortiObject
    @property
    def dict(self) -> dict[str, Any]:
        """Convert to dictionary."""
        ...
    @property
    def json(self) -> dict[str, Any]:
        """Convert to dictionary (alias for .dict)."""
        ...
    @property
    def raw(self) -> dict[str, Any]:
        """Get raw API response data."""
        ...
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> FortiObject: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


@final
class PolicyZtnageotagObject:
    """Typed object for ztna-geo-tag table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Address name. | MaxLen: 79
    name: str
    
    # Methods from FortiObject
    @property
    def dict(self) -> dict[str, Any]:
        """Convert to dictionary."""
        ...
    @property
    def json(self) -> dict[str, Any]:
        """Convert to dictionary (alias for .dict)."""
        ...
    @property
    def raw(self) -> dict[str, Any]:
        """Get raw API response data."""
        ...
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> FortiObject: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


@final
class PolicyInternetservicenameObject:
    """Typed object for internet-service-name table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Internet Service name. | MaxLen: 79
    name: str
    
    # Methods from FortiObject
    @property
    def dict(self) -> dict[str, Any]:
        """Convert to dictionary."""
        ...
    @property
    def json(self) -> dict[str, Any]:
        """Convert to dictionary (alias for .dict)."""
        ...
    @property
    def raw(self) -> dict[str, Any]:
        """Get raw API response data."""
        ...
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> FortiObject: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


@final
class PolicyInternetservicegroupObject:
    """Typed object for internet-service-group table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Internet Service group name. | MaxLen: 79
    name: str
    
    # Methods from FortiObject
    @property
    def dict(self) -> dict[str, Any]:
        """Convert to dictionary."""
        ...
    @property
    def json(self) -> dict[str, Any]:
        """Convert to dictionary (alias for .dict)."""
        ...
    @property
    def raw(self) -> dict[str, Any]:
        """Get raw API response data."""
        ...
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> FortiObject: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


@final
class PolicyInternetservicecustomObject:
    """Typed object for internet-service-custom table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Custom Internet Service name. | MaxLen: 79
    name: str
    
    # Methods from FortiObject
    @property
    def dict(self) -> dict[str, Any]:
        """Convert to dictionary."""
        ...
    @property
    def json(self) -> dict[str, Any]:
        """Convert to dictionary (alias for .dict)."""
        ...
    @property
    def raw(self) -> dict[str, Any]:
        """Get raw API response data."""
        ...
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> FortiObject: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


@final
class PolicyNetworkservicedynamicObject:
    """Typed object for network-service-dynamic table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Dynamic Network Service name. | MaxLen: 79
    name: str
    
    # Methods from FortiObject
    @property
    def dict(self) -> dict[str, Any]:
        """Convert to dictionary."""
        ...
    @property
    def json(self) -> dict[str, Any]:
        """Convert to dictionary (alias for .dict)."""
        ...
    @property
    def raw(self) -> dict[str, Any]:
        """Get raw API response data."""
        ...
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> FortiObject: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


@final
class PolicyInternetservicecustomgroupObject:
    """Typed object for internet-service-custom-group table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Custom Internet Service group name. | MaxLen: 79
    name: str
    
    # Methods from FortiObject
    @property
    def dict(self) -> dict[str, Any]:
        """Convert to dictionary."""
        ...
    @property
    def json(self) -> dict[str, Any]:
        """Convert to dictionary (alias for .dict)."""
        ...
    @property
    def raw(self) -> dict[str, Any]:
        """Get raw API response data."""
        ...
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> FortiObject: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


@final
class PolicyInternetservicesrcnameObject:
    """Typed object for internet-service-src-name table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Internet Service name. | MaxLen: 79
    name: str
    
    # Methods from FortiObject
    @property
    def dict(self) -> dict[str, Any]:
        """Convert to dictionary."""
        ...
    @property
    def json(self) -> dict[str, Any]:
        """Convert to dictionary (alias for .dict)."""
        ...
    @property
    def raw(self) -> dict[str, Any]:
        """Get raw API response data."""
        ...
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> FortiObject: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


@final
class PolicyInternetservicesrcgroupObject:
    """Typed object for internet-service-src-group table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Internet Service group name. | MaxLen: 79
    name: str
    
    # Methods from FortiObject
    @property
    def dict(self) -> dict[str, Any]:
        """Convert to dictionary."""
        ...
    @property
    def json(self) -> dict[str, Any]:
        """Convert to dictionary (alias for .dict)."""
        ...
    @property
    def raw(self) -> dict[str, Any]:
        """Get raw API response data."""
        ...
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> FortiObject: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


@final
class PolicyInternetservicesrccustomObject:
    """Typed object for internet-service-src-custom table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Custom Internet Service name. | MaxLen: 79
    name: str
    
    # Methods from FortiObject
    @property
    def dict(self) -> dict[str, Any]:
        """Convert to dictionary."""
        ...
    @property
    def json(self) -> dict[str, Any]:
        """Convert to dictionary (alias for .dict)."""
        ...
    @property
    def raw(self) -> dict[str, Any]:
        """Get raw API response data."""
        ...
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> FortiObject: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


@final
class PolicyNetworkservicesrcdynamicObject:
    """Typed object for network-service-src-dynamic table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Dynamic Network Service name. | MaxLen: 79
    name: str
    
    # Methods from FortiObject
    @property
    def dict(self) -> dict[str, Any]:
        """Convert to dictionary."""
        ...
    @property
    def json(self) -> dict[str, Any]:
        """Convert to dictionary (alias for .dict)."""
        ...
    @property
    def raw(self) -> dict[str, Any]:
        """Get raw API response data."""
        ...
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> FortiObject: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


@final
class PolicyInternetservicesrccustomgroupObject:
    """Typed object for internet-service-src-custom-group table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Custom Internet Service group name. | MaxLen: 79
    name: str
    
    # Methods from FortiObject
    @property
    def dict(self) -> dict[str, Any]:
        """Convert to dictionary."""
        ...
    @property
    def json(self) -> dict[str, Any]:
        """Convert to dictionary (alias for .dict)."""
        ...
    @property
    def raw(self) -> dict[str, Any]:
        """Get raw API response data."""
        ...
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> FortiObject: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


@final
class PolicySrcvendormacObject:
    """Typed object for src-vendor-mac table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Vendor MAC ID. | Default: 0 | Min: 0 | Max: 4294967295
    id: int
    
    # Methods from FortiObject
    @property
    def dict(self) -> dict[str, Any]:
        """Convert to dictionary."""
        ...
    @property
    def json(self) -> dict[str, Any]:
        """Convert to dictionary (alias for .dict)."""
        ...
    @property
    def raw(self) -> dict[str, Any]:
        """Get raw API response data."""
        ...
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> FortiObject: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


@final
class PolicyInternetservice6nameObject:
    """Typed object for internet-service6-name table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # IPv6 Internet Service name. | MaxLen: 79
    name: str
    
    # Methods from FortiObject
    @property
    def dict(self) -> dict[str, Any]:
        """Convert to dictionary."""
        ...
    @property
    def json(self) -> dict[str, Any]:
        """Convert to dictionary (alias for .dict)."""
        ...
    @property
    def raw(self) -> dict[str, Any]:
        """Get raw API response data."""
        ...
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> FortiObject: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


@final
class PolicyInternetservice6groupObject:
    """Typed object for internet-service6-group table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Internet Service group name. | MaxLen: 79
    name: str
    
    # Methods from FortiObject
    @property
    def dict(self) -> dict[str, Any]:
        """Convert to dictionary."""
        ...
    @property
    def json(self) -> dict[str, Any]:
        """Convert to dictionary (alias for .dict)."""
        ...
    @property
    def raw(self) -> dict[str, Any]:
        """Get raw API response data."""
        ...
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> FortiObject: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


@final
class PolicyInternetservice6customObject:
    """Typed object for internet-service6-custom table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Custom Internet Service name. | MaxLen: 79
    name: str
    
    # Methods from FortiObject
    @property
    def dict(self) -> dict[str, Any]:
        """Convert to dictionary."""
        ...
    @property
    def json(self) -> dict[str, Any]:
        """Convert to dictionary (alias for .dict)."""
        ...
    @property
    def raw(self) -> dict[str, Any]:
        """Get raw API response data."""
        ...
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> FortiObject: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


@final
class PolicyInternetservice6customgroupObject:
    """Typed object for internet-service6-custom-group table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Custom Internet Service6 group name. | MaxLen: 79
    name: str
    
    # Methods from FortiObject
    @property
    def dict(self) -> dict[str, Any]:
        """Convert to dictionary."""
        ...
    @property
    def json(self) -> dict[str, Any]:
        """Convert to dictionary (alias for .dict)."""
        ...
    @property
    def raw(self) -> dict[str, Any]:
        """Get raw API response data."""
        ...
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> FortiObject: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


@final
class PolicyInternetservice6srcnameObject:
    """Typed object for internet-service6-src-name table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Internet Service name. | MaxLen: 79
    name: str
    
    # Methods from FortiObject
    @property
    def dict(self) -> dict[str, Any]:
        """Convert to dictionary."""
        ...
    @property
    def json(self) -> dict[str, Any]:
        """Convert to dictionary (alias for .dict)."""
        ...
    @property
    def raw(self) -> dict[str, Any]:
        """Get raw API response data."""
        ...
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> FortiObject: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


@final
class PolicyInternetservice6srcgroupObject:
    """Typed object for internet-service6-src-group table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Internet Service group name. | MaxLen: 79
    name: str
    
    # Methods from FortiObject
    @property
    def dict(self) -> dict[str, Any]:
        """Convert to dictionary."""
        ...
    @property
    def json(self) -> dict[str, Any]:
        """Convert to dictionary (alias for .dict)."""
        ...
    @property
    def raw(self) -> dict[str, Any]:
        """Get raw API response data."""
        ...
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> FortiObject: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


@final
class PolicyInternetservice6srccustomObject:
    """Typed object for internet-service6-src-custom table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Custom Internet Service name. | MaxLen: 79
    name: str
    
    # Methods from FortiObject
    @property
    def dict(self) -> dict[str, Any]:
        """Convert to dictionary."""
        ...
    @property
    def json(self) -> dict[str, Any]:
        """Convert to dictionary (alias for .dict)."""
        ...
    @property
    def raw(self) -> dict[str, Any]:
        """Get raw API response data."""
        ...
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> FortiObject: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


@final
class PolicyInternetservice6srccustomgroupObject:
    """Typed object for internet-service6-src-custom-group table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Custom Internet Service6 group name. | MaxLen: 79
    name: str
    
    # Methods from FortiObject
    @property
    def dict(self) -> dict[str, Any]:
        """Convert to dictionary."""
        ...
    @property
    def json(self) -> dict[str, Any]:
        """Convert to dictionary (alias for .dict)."""
        ...
    @property
    def raw(self) -> dict[str, Any]:
        """Get raw API response data."""
        ...
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> FortiObject: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


@final
class PolicyRtpaddrObject:
    """Typed object for rtp-addr table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Address name. | MaxLen: 79
    name: str
    
    # Methods from FortiObject
    @property
    def dict(self) -> dict[str, Any]:
        """Convert to dictionary."""
        ...
    @property
    def json(self) -> dict[str, Any]:
        """Convert to dictionary (alias for .dict)."""
        ...
    @property
    def raw(self) -> dict[str, Any]:
        """Get raw API response data."""
        ...
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> FortiObject: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


@final
class PolicyServiceObject:
    """Typed object for service table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Service and service group names. | MaxLen: 79
    name: str
    
    # Methods from FortiObject
    @property
    def dict(self) -> dict[str, Any]:
        """Convert to dictionary."""
        ...
    @property
    def json(self) -> dict[str, Any]:
        """Convert to dictionary (alias for .dict)."""
        ...
    @property
    def raw(self) -> dict[str, Any]:
        """Get raw API response data."""
        ...
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> FortiObject: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


@final
class PolicyPcppoolnameObject:
    """Typed object for pcp-poolname table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # PCP pool name. | MaxLen: 79
    name: str
    
    # Methods from FortiObject
    @property
    def dict(self) -> dict[str, Any]:
        """Convert to dictionary."""
        ...
    @property
    def json(self) -> dict[str, Any]:
        """Convert to dictionary (alias for .dict)."""
        ...
    @property
    def raw(self) -> dict[str, Any]:
        """Get raw API response data."""
        ...
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> FortiObject: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


@final
class PolicyPoolnameObject:
    """Typed object for poolname table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # IP pool name. | MaxLen: 79
    name: str
    
    # Methods from FortiObject
    @property
    def dict(self) -> dict[str, Any]:
        """Convert to dictionary."""
        ...
    @property
    def json(self) -> dict[str, Any]:
        """Convert to dictionary (alias for .dict)."""
        ...
    @property
    def raw(self) -> dict[str, Any]:
        """Get raw API response data."""
        ...
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> FortiObject: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


@final
class PolicyPoolname6Object:
    """Typed object for poolname6 table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # IPv6 pool name. | MaxLen: 79
    name: str
    
    # Methods from FortiObject
    @property
    def dict(self) -> dict[str, Any]:
        """Convert to dictionary."""
        ...
    @property
    def json(self) -> dict[str, Any]:
        """Convert to dictionary (alias for .dict)."""
        ...
    @property
    def raw(self) -> dict[str, Any]:
        """Get raw API response data."""
        ...
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> FortiObject: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


@final
class PolicyNtlmenabledbrowsersObject:
    """Typed object for ntlm-enabled-browsers table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # User agent string. | MaxLen: 79
    user_agent_string: str
    
    # Methods from FortiObject
    @property
    def dict(self) -> dict[str, Any]:
        """Convert to dictionary."""
        ...
    @property
    def json(self) -> dict[str, Any]:
        """Convert to dictionary (alias for .dict)."""
        ...
    @property
    def raw(self) -> dict[str, Any]:
        """Get raw API response data."""
        ...
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> FortiObject: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


@final
class PolicyGroupsObject:
    """Typed object for groups table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Group name. | MaxLen: 79
    name: str
    
    # Methods from FortiObject
    @property
    def dict(self) -> dict[str, Any]:
        """Convert to dictionary."""
        ...
    @property
    def json(self) -> dict[str, Any]:
        """Convert to dictionary (alias for .dict)."""
        ...
    @property
    def raw(self) -> dict[str, Any]:
        """Get raw API response data."""
        ...
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> FortiObject: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


@final
class PolicyUsersObject:
    """Typed object for users table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Names of individual users that can authenticate with this po | MaxLen: 79
    name: str
    
    # Methods from FortiObject
    @property
    def dict(self) -> dict[str, Any]:
        """Convert to dictionary."""
        ...
    @property
    def json(self) -> dict[str, Any]:
        """Convert to dictionary (alias for .dict)."""
        ...
    @property
    def raw(self) -> dict[str, Any]:
        """Get raw API response data."""
        ...
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> FortiObject: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


@final
class PolicyFssogroupsObject:
    """Typed object for fsso-groups table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Names of FSSO groups. | MaxLen: 511
    name: str
    
    # Methods from FortiObject
    @property
    def dict(self) -> dict[str, Any]:
        """Convert to dictionary."""
        ...
    @property
    def json(self) -> dict[str, Any]:
        """Convert to dictionary (alias for .dict)."""
        ...
    @property
    def raw(self) -> dict[str, Any]:
        """Get raw API response data."""
        ...
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> FortiObject: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


@final
class PolicyCustomlogfieldsObject:
    """Typed object for custom-log-fields table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Custom log field. | MaxLen: 35
    field_id: str
    
    # Methods from FortiObject
    @property
    def dict(self) -> dict[str, Any]:
        """Convert to dictionary."""
        ...
    @property
    def json(self) -> dict[str, Any]:
        """Convert to dictionary (alias for .dict)."""
        ...
    @property
    def raw(self) -> dict[str, Any]:
        """Get raw API response data."""
        ...
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> FortiObject: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


@final
class PolicySgtObject:
    """Typed object for sgt table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Security group tag (1 - 65535). | Default: 0 | Min: 1 | Max: 65535
    id: int
    
    # Methods from FortiObject
    @property
    def dict(self) -> dict[str, Any]:
        """Convert to dictionary."""
        ...
    @property
    def json(self) -> dict[str, Any]:
        """Convert to dictionary (alias for .dict)."""
        ...
    @property
    def raw(self) -> dict[str, Any]:
        """Get raw API response data."""
        ...
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> FortiObject: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


@final
class PolicyInternetservicefortiguardObject:
    """Typed object for internet-service-fortiguard table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # FortiGuard Internet Service name. | MaxLen: 79
    name: str
    
    # Methods from FortiObject
    @property
    def dict(self) -> dict[str, Any]:
        """Convert to dictionary."""
        ...
    @property
    def json(self) -> dict[str, Any]:
        """Convert to dictionary (alias for .dict)."""
        ...
    @property
    def raw(self) -> dict[str, Any]:
        """Get raw API response data."""
        ...
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> FortiObject: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


@final
class PolicyInternetservicesrcfortiguardObject:
    """Typed object for internet-service-src-fortiguard table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # FortiGuard Internet Service name. | MaxLen: 79
    name: str
    
    # Methods from FortiObject
    @property
    def dict(self) -> dict[str, Any]:
        """Convert to dictionary."""
        ...
    @property
    def json(self) -> dict[str, Any]:
        """Convert to dictionary (alias for .dict)."""
        ...
    @property
    def raw(self) -> dict[str, Any]:
        """Get raw API response data."""
        ...
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> FortiObject: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


@final
class PolicyInternetservice6fortiguardObject:
    """Typed object for internet-service6-fortiguard table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # FortiGuard Internet Service name. | MaxLen: 79
    name: str
    
    # Methods from FortiObject
    @property
    def dict(self) -> dict[str, Any]:
        """Convert to dictionary."""
        ...
    @property
    def json(self) -> dict[str, Any]:
        """Convert to dictionary (alias for .dict)."""
        ...
    @property
    def raw(self) -> dict[str, Any]:
        """Get raw API response data."""
        ...
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> FortiObject: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


@final
class PolicyInternetservice6srcfortiguardObject:
    """Typed object for internet-service6-src-fortiguard table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # FortiGuard Internet Service name. | MaxLen: 79
    name: str
    
    # Methods from FortiObject
    @property
    def dict(self) -> dict[str, Any]:
        """Convert to dictionary."""
        ...
    @property
    def json(self) -> dict[str, Any]:
        """Convert to dictionary (alias for .dict)."""
        ...
    @property
    def raw(self) -> dict[str, Any]:
        """Get raw API response data."""
        ...
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> FortiObject: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...



# Response TypedDict for GET returns (all fields present in API response)
class PolicyResponse(TypedDict):
    """
    Type hints for firewall/policy API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    policyid: int  # Policy ID (0 - 4294967294). | Default: 0 | Min: 0 | Max: 4294967294
    status: Literal["enable", "disable"]  # Enable or disable this policy. | Default: enable
    name: str  # Policy name. | MaxLen: 35
    uuid: str  # Universally Unique Identifier | Default: 00000000-0000-0000-0000-000000000000
    srcintf: list[PolicySrcintfItem]  # Incoming (ingress) interface.
    dstintf: list[PolicyDstintfItem]  # Outgoing (egress) interface.
    action: Literal["accept", "deny", "ipsec"]  # Policy action (accept/deny/ipsec). | Default: deny
    nat64: Literal["enable", "disable"]  # Enable/disable NAT64. | Default: disable
    nat46: Literal["enable", "disable"]  # Enable/disable NAT46. | Default: disable
    ztna_status: Literal["enable", "disable"]  # Enable/disable zero trust access. | Default: disable
    ztna_device_ownership: Literal["enable", "disable"]  # Enable/disable zero trust device ownership. | Default: disable
    srcaddr: list[PolicySrcaddrItem]  # Source IPv4 address and address group names.
    dstaddr: list[PolicyDstaddrItem]  # Destination IPv4 address and address group names.
    srcaddr6: list[PolicySrcaddr6Item]  # Source IPv6 address name and address group names.
    dstaddr6: list[PolicyDstaddr6Item]  # Destination IPv6 address name and address group na
    ztna_ems_tag: list[PolicyZtnaemstagItem]  # Source ztna-ems-tag names.
    ztna_ems_tag_secondary: list[PolicyZtnaemstagsecondaryItem]  # Source ztna-ems-tag-secondary names.
    ztna_tags_match_logic: Literal["or", "and"]  # ZTNA tag matching logic. | Default: or
    ztna_geo_tag: list[PolicyZtnageotagItem]  # Source ztna-geo-tag names.
    internet_service: Literal["enable", "disable"]  # Enable/disable use of Internet Services for this p | Default: disable
    internet_service_name: list[PolicyInternetservicenameItem]  # Internet Service name.
    internet_service_group: list[PolicyInternetservicegroupItem]  # Internet Service group name.
    internet_service_custom: list[PolicyInternetservicecustomItem]  # Custom Internet Service name.
    network_service_dynamic: list[PolicyNetworkservicedynamicItem]  # Dynamic Network Service name.
    internet_service_custom_group: list[PolicyInternetservicecustomgroupItem]  # Custom Internet Service group name.
    internet_service_src: Literal["enable", "disable"]  # Enable/disable use of Internet Services in source | Default: disable
    internet_service_src_name: list[PolicyInternetservicesrcnameItem]  # Internet Service source name.
    internet_service_src_group: list[PolicyInternetservicesrcgroupItem]  # Internet Service source group name.
    internet_service_src_custom: list[PolicyInternetservicesrccustomItem]  # Custom Internet Service source name.
    network_service_src_dynamic: list[PolicyNetworkservicesrcdynamicItem]  # Dynamic Network Service source name.
    internet_service_src_custom_group: list[PolicyInternetservicesrccustomgroupItem]  # Custom Internet Service source group name.
    reputation_minimum: int  # Minimum Reputation to take action. | Default: 0 | Min: 0 | Max: 4294967295
    reputation_direction: Literal["source", "destination"]  # Direction of the initial traffic for reputation to | Default: destination
    src_vendor_mac: list[PolicySrcvendormacItem]  # Vendor MAC source ID.
    internet_service6: Literal["enable", "disable"]  # Enable/disable use of IPv6 Internet Services for t | Default: disable
    internet_service6_name: list[PolicyInternetservice6nameItem]  # IPv6 Internet Service name.
    internet_service6_group: list[PolicyInternetservice6groupItem]  # Internet Service group name.
    internet_service6_custom: list[PolicyInternetservice6customItem]  # Custom IPv6 Internet Service name.
    internet_service6_custom_group: list[PolicyInternetservice6customgroupItem]  # Custom Internet Service6 group name.
    internet_service6_src: Literal["enable", "disable"]  # Enable/disable use of IPv6 Internet Services in so | Default: disable
    internet_service6_src_name: list[PolicyInternetservice6srcnameItem]  # IPv6 Internet Service source name.
    internet_service6_src_group: list[PolicyInternetservice6srcgroupItem]  # Internet Service6 source group name.
    internet_service6_src_custom: list[PolicyInternetservice6srccustomItem]  # Custom IPv6 Internet Service source name.
    internet_service6_src_custom_group: list[PolicyInternetservice6srccustomgroupItem]  # Custom Internet Service6 source group name.
    reputation_minimum6: int  # IPv6 Minimum Reputation to take action. | Default: 0 | Min: 0 | Max: 4294967295
    reputation_direction6: Literal["source", "destination"]  # Direction of the initial traffic for IPv6 reputati | Default: destination
    rtp_nat: Literal["disable", "enable"]  # Enable Real Time Protocol (RTP) NAT. | Default: disable
    rtp_addr: list[PolicyRtpaddrItem]  # Address names if this is an RTP NAT policy.
    send_deny_packet: Literal["disable", "enable"]  # Enable to send a reply when a session is denied or | Default: disable
    firewall_session_dirty: Literal["check-all", "check-new"]  # How to handle sessions if the configuration of thi | Default: check-all
    schedule: str  # Schedule name. | MaxLen: 35
    schedule_timeout: Literal["enable", "disable"]  # Enable to force current sessions to end when the s | Default: disable
    policy_expiry: Literal["enable", "disable"]  # Enable/disable policy expiry. | Default: disable
    policy_expiry_date: str  # Policy expiry date (YYYY-MM-DD HH:MM:SS). | Default: 0000-00-00 00:00:00
    policy_expiry_date_utc: str  # Policy expiry date and time, in epoch format.
    service: list[PolicyServiceItem]  # Service and service group names.
    tos_mask: str  # Non-zero bit positions are used for comparison whi
    tos: str  # ToS (Type of Service) value used for comparison.
    tos_negate: Literal["enable", "disable"]  # Enable negated TOS match. | Default: disable
    anti_replay: Literal["enable", "disable"]  # Enable/disable anti-replay check. | Default: enable
    tcp_session_without_syn: Literal["all", "data-only", "disable"]  # Enable/disable creation of TCP session without SYN | Default: disable
    geoip_anycast: Literal["enable", "disable"]  # Enable/disable recognition of anycast IP addresses | Default: disable
    geoip_match: Literal["physical-location", "registered-location"]  # Match geography address based either on its physic | Default: physical-location
    dynamic_shaping: Literal["enable", "disable"]  # Enable/disable dynamic RADIUS defined traffic shap | Default: disable
    passive_wan_health_measurement: Literal["enable", "disable"]  # Enable/disable passive WAN health measurement. Whe | Default: disable
    app_monitor: Literal["enable", "disable"]  # Enable/disable application TCP metrics in session | Default: disable
    utm_status: Literal["enable", "disable"]  # Enable to add one or more security profiles | Default: disable
    inspection_mode: Literal["proxy", "flow"]  # Policy inspection mode (Flow/proxy). Default is Fl | Default: flow
    http_policy_redirect: Literal["enable", "disable", "legacy"]  # Redirect HTTP(S) traffic to matching transparent w | Default: disable
    ssh_policy_redirect: Literal["enable", "disable"]  # Redirect SSH traffic to matching transparent proxy | Default: disable
    ztna_policy_redirect: Literal["enable", "disable"]  # Redirect ZTNA traffic to matching Access-Proxy pro | Default: disable
    webproxy_profile: str  # Webproxy profile name. | MaxLen: 63
    profile_type: Literal["single", "group"]  # Determine whether the firewall policy allows secur | Default: single
    profile_group: str  # Name of profile group. | MaxLen: 47
    profile_protocol_options: str  # Name of an existing Protocol options profile. | Default: default | MaxLen: 47
    ssl_ssh_profile: str  # Name of an existing SSL SSH profile. | Default: no-inspection | MaxLen: 47
    av_profile: str  # Name of an existing Antivirus profile. | MaxLen: 47
    webfilter_profile: str  # Name of an existing Web filter profile. | MaxLen: 47
    dnsfilter_profile: str  # Name of an existing DNS filter profile. | MaxLen: 47
    emailfilter_profile: str  # Name of an existing email filter profile. | MaxLen: 47
    dlp_profile: str  # Name of an existing DLP profile. | MaxLen: 47
    file_filter_profile: str  # Name of an existing file-filter profile. | MaxLen: 47
    ips_sensor: str  # Name of an existing IPS sensor. | MaxLen: 47
    application_list: str  # Name of an existing Application list. | MaxLen: 47
    voip_profile: str  # Name of an existing VoIP (voipd) profile. | MaxLen: 47
    ips_voip_filter: str  # Name of an existing VoIP (ips) profile. | MaxLen: 47
    sctp_filter_profile: str  # Name of an existing SCTP filter profile. | MaxLen: 47
    diameter_filter_profile: str  # Name of an existing Diameter filter profile. | MaxLen: 47
    virtual_patch_profile: str  # Name of an existing virtual-patch profile. | MaxLen: 47
    icap_profile: str  # Name of an existing ICAP profile. | MaxLen: 47
    videofilter_profile: str  # Name of an existing VideoFilter profile. | MaxLen: 47
    waf_profile: str  # Name of an existing Web application firewall profi | MaxLen: 47
    ssh_filter_profile: str  # Name of an existing SSH filter profile. | MaxLen: 47
    casb_profile: str  # Name of an existing CASB profile. | MaxLen: 47
    logtraffic: Literal["all", "utm", "disable"]  # Enable or disable logging. Log all sessions or sec | Default: utm
    logtraffic_start: Literal["enable", "disable"]  # Record logs when a session starts. | Default: disable
    log_http_transaction: Literal["enable", "disable"]  # Enable/disable HTTP transaction log. | Default: disable
    capture_packet: Literal["enable", "disable"]  # Enable/disable capture packets. | Default: disable
    auto_asic_offload: Literal["enable", "disable"]  # Enable/disable policy traffic ASIC offloading. | Default: enable
    wanopt: Literal["enable", "disable"]  # Enable/disable WAN optimization. | Default: disable
    wanopt_detection: Literal["active", "passive", "off"]  # WAN optimization auto-detection mode. | Default: active
    wanopt_passive_opt: Literal["default", "transparent", "non-transparent"]  # WAN optimization passive mode options. This option | Default: default
    wanopt_profile: str  # WAN optimization profile. | MaxLen: 35
    wanopt_peer: str  # WAN optimization peer. | MaxLen: 35
    webcache: Literal["enable", "disable"]  # Enable/disable web cache. | Default: disable
    webcache_https: Literal["disable", "enable"]  # Enable/disable web cache for HTTPS. | Default: disable
    webproxy_forward_server: str  # Webproxy forward server name. | MaxLen: 63
    traffic_shaper: str  # Traffic shaper. | MaxLen: 35
    traffic_shaper_reverse: str  # Reverse traffic shaper. | MaxLen: 35
    per_ip_shaper: str  # Per-IP traffic shaper. | MaxLen: 35
    nat: Literal["enable", "disable"]  # Enable/disable source NAT. | Default: disable
    pcp_outbound: Literal["enable", "disable"]  # Enable/disable PCP outbound SNAT. | Default: disable
    pcp_inbound: Literal["enable", "disable"]  # Enable/disable PCP inbound DNAT. | Default: disable
    pcp_poolname: list[PolicyPcppoolnameItem]  # PCP pool names.
    permit_any_host: Literal["enable", "disable"]  # Enable/disable fullcone NAT. Accept UDP packets fr | Default: disable
    permit_stun_host: Literal["enable", "disable"]  # Accept UDP packets from any Session Traversal Util | Default: disable
    fixedport: Literal["enable", "disable"]  # Enable to prevent source NAT from changing a sessi | Default: disable
    port_preserve: Literal["enable", "disable"]  # Enable/disable preservation of the original source | Default: enable
    port_random: Literal["enable", "disable"]  # Enable/disable random source port selection for so | Default: disable
    ippool: Literal["enable", "disable"]  # Enable to use IP Pools for source NAT. | Default: disable
    poolname: list[PolicyPoolnameItem]  # IP Pool names.
    poolname6: list[PolicyPoolname6Item]  # IPv6 pool names.
    session_ttl: str  # TTL in seconds for sessions accepted by this polic
    vlan_cos_fwd: int  # VLAN forward direction user priority: 255 passthro | Default: 255 | Min: 0 | Max: 7
    vlan_cos_rev: int  # VLAN reverse direction user priority: 255 passthro | Default: 255 | Min: 0 | Max: 7
    inbound: Literal["enable", "disable"]  # Policy-based IPsec VPN: only traffic from the remo | Default: disable
    outbound: Literal["enable", "disable"]  # Policy-based IPsec VPN: only traffic from the inte | Default: enable
    natinbound: Literal["enable", "disable"]  # Policy-based IPsec VPN: apply destination NAT to i | Default: disable
    natoutbound: Literal["enable", "disable"]  # Policy-based IPsec VPN: apply source NAT to outbou | Default: disable
    fec: Literal["enable", "disable"]  # Enable/disable Forward Error Correction on traffic | Default: disable
    wccp: Literal["enable", "disable"]  # Enable/disable forwarding traffic matching this po | Default: disable
    ntlm: Literal["enable", "disable"]  # Enable/disable NTLM authentication. | Default: disable
    ntlm_guest: Literal["enable", "disable"]  # Enable/disable NTLM guest user access. | Default: disable
    ntlm_enabled_browsers: list[PolicyNtlmenabledbrowsersItem]  # HTTP-User-Agent value of supported browsers.
    fsso_agent_for_ntlm: str  # FSSO agent to use for NTLM authentication. | MaxLen: 35
    groups: list[PolicyGroupsItem]  # Names of user groups that can authenticate with th
    users: list[PolicyUsersItem]  # Names of individual users that can authenticate wi
    fsso_groups: list[PolicyFssogroupsItem]  # Names of FSSO groups.
    auth_path: Literal["enable", "disable"]  # Enable/disable authentication-based routing. | Default: disable
    disclaimer: Literal["enable", "disable"]  # Enable/disable user authentication disclaimer. | Default: disable
    email_collect: Literal["enable", "disable"]  # Enable/disable email collection. | Default: disable
    vpntunnel: str  # Policy-based IPsec VPN: name of the IPsec VPN Phas | MaxLen: 35
    natip: str  # Policy-based IPsec VPN: source NAT IP address for | Default: 0.0.0.0 0.0.0.0
    match_vip: Literal["enable", "disable"]  # Enable to match packets that have had their destin | Default: enable
    match_vip_only: Literal["enable", "disable"]  # Enable/disable matching of only those packets that | Default: disable
    diffserv_copy: Literal["enable", "disable"]  # Enable to copy packet's DiffServ values from sessi | Default: disable
    diffserv_forward: Literal["enable", "disable"]  # Enable to change packet's DiffServ values to the s | Default: disable
    diffserv_reverse: Literal["enable", "disable"]  # Enable to change packet's reverse (reply) DiffServ | Default: disable
    diffservcode_forward: str  # Change packet's DiffServ to this value.
    diffservcode_rev: str  # Change packet's reverse (reply) DiffServ to this v
    tcp_mss_sender: int  # Sender TCP maximum segment size (MSS). | Default: 0 | Min: 0 | Max: 65535
    tcp_mss_receiver: int  # Receiver TCP maximum segment size (MSS). | Default: 0 | Min: 0 | Max: 65535
    comments: str  # Comment. | MaxLen: 1023
    auth_cert: str  # HTTPS server certificate for policy authentication | MaxLen: 35
    auth_redirect_addr: str  # HTTP-to-HTTPS redirect address for firewall authen | MaxLen: 63
    redirect_url: str  # URL users are directed to after seeing and accepti | MaxLen: 1023
    identity_based_route: str  # Name of identity-based routing rule. | MaxLen: 35
    block_notification: Literal["enable", "disable"]  # Enable/disable block notification. | Default: disable
    custom_log_fields: list[PolicyCustomlogfieldsItem]  # Custom fields to append to log messages for this p
    replacemsg_override_group: str  # Override the default replacement message group for | MaxLen: 35
    srcaddr_negate: Literal["enable", "disable"]  # When enabled srcaddr specifies what the source add | Default: disable
    srcaddr6_negate: Literal["enable", "disable"]  # When enabled srcaddr6 specifies what the source ad | Default: disable
    dstaddr_negate: Literal["enable", "disable"]  # When enabled dstaddr specifies what the destinatio | Default: disable
    dstaddr6_negate: Literal["enable", "disable"]  # When enabled dstaddr6 specifies what the destinati | Default: disable
    ztna_ems_tag_negate: Literal["enable", "disable"]  # When enabled ztna-ems-tag specifies what the tags | Default: disable
    service_negate: Literal["enable", "disable"]  # When enabled service specifies what the service mu | Default: disable
    internet_service_negate: Literal["enable", "disable"]  # When enabled internet-service specifies what the s | Default: disable
    internet_service_src_negate: Literal["enable", "disable"]  # When enabled internet-service-src specifies what t | Default: disable
    internet_service6_negate: Literal["enable", "disable"]  # When enabled internet-service6 specifies what the | Default: disable
    internet_service6_src_negate: Literal["enable", "disable"]  # When enabled internet-service6-src specifies what | Default: disable
    timeout_send_rst: Literal["enable", "disable"]  # Enable/disable sending RST packets when TCP sessio | Default: disable
    captive_portal_exempt: Literal["enable", "disable"]  # Enable to exempt some users from the captive porta | Default: disable
    decrypted_traffic_mirror: str  # Decrypted traffic mirror. | MaxLen: 35
    dsri: Literal["enable", "disable"]  # Enable DSRI to ignore HTTP server responses. | Default: disable
    radius_mac_auth_bypass: Literal["enable", "disable"]  # Enable MAC authentication bypass. The bypassed MAC | Default: disable
    radius_ip_auth_bypass: Literal["enable", "disable"]  # Enable IP authentication bypass. The bypassed IP a | Default: disable
    delay_tcp_npu_session: Literal["enable", "disable"]  # Enable TCP NPU session delay to guarantee packet o | Default: disable
    vlan_filter: str  # VLAN ranges to allow
    sgt_check: Literal["enable", "disable"]  # Enable/disable security group tags (SGT) check. | Default: disable
    sgt: list[PolicySgtItem]  # Security group tags.
    internet_service_fortiguard: list[PolicyInternetservicefortiguardItem]  # FortiGuard Internet Service name.
    internet_service_src_fortiguard: list[PolicyInternetservicesrcfortiguardItem]  # FortiGuard Internet Service source name.
    internet_service6_fortiguard: list[PolicyInternetservice6fortiguardItem]  # FortiGuard IPv6 Internet Service name.
    internet_service6_src_fortiguard: list[PolicyInternetservice6srcfortiguardItem]  # FortiGuard IPv6 Internet Service source name.


@final
class PolicyObject:
    """Typed FortiObject for firewall/policy with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Policy ID (0 - 4294967294). | Default: 0 | Min: 0 | Max: 4294967294
    policyid: int
    # Enable or disable this policy. | Default: enable
    status: Literal["enable", "disable"]
    # Policy name. | MaxLen: 35
    name: str
    # Universally Unique Identifier | Default: 00000000-0000-0000-0000-000000000000
    uuid: str
    # Incoming (ingress) interface.
    srcintf: list[PolicySrcintfObject]
    # Outgoing (egress) interface.
    dstintf: list[PolicyDstintfObject]
    # Policy action (accept/deny/ipsec). | Default: deny
    action: Literal["accept", "deny", "ipsec"]
    # Enable/disable NAT64. | Default: disable
    nat64: Literal["enable", "disable"]
    # Enable/disable NAT46. | Default: disable
    nat46: Literal["enable", "disable"]
    # Enable/disable zero trust access. | Default: disable
    ztna_status: Literal["enable", "disable"]
    # Enable/disable zero trust device ownership. | Default: disable
    ztna_device_ownership: Literal["enable", "disable"]
    # Source IPv4 address and address group names.
    srcaddr: list[PolicySrcaddrObject]
    # Destination IPv4 address and address group names.
    dstaddr: list[PolicyDstaddrObject]
    # Source IPv6 address name and address group names.
    srcaddr6: list[PolicySrcaddr6Object]
    # Destination IPv6 address name and address group names.
    dstaddr6: list[PolicyDstaddr6Object]
    # Source ztna-ems-tag names.
    ztna_ems_tag: list[PolicyZtnaemstagObject]
    # Source ztna-ems-tag-secondary names.
    ztna_ems_tag_secondary: list[PolicyZtnaemstagsecondaryObject]
    # ZTNA tag matching logic. | Default: or
    ztna_tags_match_logic: Literal["or", "and"]
    # Source ztna-geo-tag names.
    ztna_geo_tag: list[PolicyZtnageotagObject]
    # Enable/disable use of Internet Services for this policy. If | Default: disable
    internet_service: Literal["enable", "disable"]
    # Internet Service name.
    internet_service_name: list[PolicyInternetservicenameObject]
    # Internet Service group name.
    internet_service_group: list[PolicyInternetservicegroupObject]
    # Custom Internet Service name.
    internet_service_custom: list[PolicyInternetservicecustomObject]
    # Dynamic Network Service name.
    network_service_dynamic: list[PolicyNetworkservicedynamicObject]
    # Custom Internet Service group name.
    internet_service_custom_group: list[PolicyInternetservicecustomgroupObject]
    # Enable/disable use of Internet Services in source for this p | Default: disable
    internet_service_src: Literal["enable", "disable"]
    # Internet Service source name.
    internet_service_src_name: list[PolicyInternetservicesrcnameObject]
    # Internet Service source group name.
    internet_service_src_group: list[PolicyInternetservicesrcgroupObject]
    # Custom Internet Service source name.
    internet_service_src_custom: list[PolicyInternetservicesrccustomObject]
    # Dynamic Network Service source name.
    network_service_src_dynamic: list[PolicyNetworkservicesrcdynamicObject]
    # Custom Internet Service source group name.
    internet_service_src_custom_group: list[PolicyInternetservicesrccustomgroupObject]
    # Minimum Reputation to take action. | Default: 0 | Min: 0 | Max: 4294967295
    reputation_minimum: int
    # Direction of the initial traffic for reputation to take effe | Default: destination
    reputation_direction: Literal["source", "destination"]
    # Vendor MAC source ID.
    src_vendor_mac: list[PolicySrcvendormacObject]
    # Enable/disable use of IPv6 Internet Services for this policy | Default: disable
    internet_service6: Literal["enable", "disable"]
    # IPv6 Internet Service name.
    internet_service6_name: list[PolicyInternetservice6nameObject]
    # Internet Service group name.
    internet_service6_group: list[PolicyInternetservice6groupObject]
    # Custom IPv6 Internet Service name.
    internet_service6_custom: list[PolicyInternetservice6customObject]
    # Custom Internet Service6 group name.
    internet_service6_custom_group: list[PolicyInternetservice6customgroupObject]
    # Enable/disable use of IPv6 Internet Services in source for t | Default: disable
    internet_service6_src: Literal["enable", "disable"]
    # IPv6 Internet Service source name.
    internet_service6_src_name: list[PolicyInternetservice6srcnameObject]
    # Internet Service6 source group name.
    internet_service6_src_group: list[PolicyInternetservice6srcgroupObject]
    # Custom IPv6 Internet Service source name.
    internet_service6_src_custom: list[PolicyInternetservice6srccustomObject]
    # Custom Internet Service6 source group name.
    internet_service6_src_custom_group: list[PolicyInternetservice6srccustomgroupObject]
    # IPv6 Minimum Reputation to take action. | Default: 0 | Min: 0 | Max: 4294967295
    reputation_minimum6: int
    # Direction of the initial traffic for IPv6 reputation to take | Default: destination
    reputation_direction6: Literal["source", "destination"]
    # Enable Real Time Protocol (RTP) NAT. | Default: disable
    rtp_nat: Literal["disable", "enable"]
    # Address names if this is an RTP NAT policy.
    rtp_addr: list[PolicyRtpaddrObject]
    # Enable to send a reply when a session is denied or blocked b | Default: disable
    send_deny_packet: Literal["disable", "enable"]
    # How to handle sessions if the configuration of this firewall | Default: check-all
    firewall_session_dirty: Literal["check-all", "check-new"]
    # Schedule name. | MaxLen: 35
    schedule: str
    # Enable to force current sessions to end when the schedule ob | Default: disable
    schedule_timeout: Literal["enable", "disable"]
    # Enable/disable policy expiry. | Default: disable
    policy_expiry: Literal["enable", "disable"]
    # Policy expiry date (YYYY-MM-DD HH:MM:SS). | Default: 0000-00-00 00:00:00
    policy_expiry_date: str
    # Policy expiry date and time, in epoch format.
    policy_expiry_date_utc: str
    # Service and service group names.
    service: list[PolicyServiceObject]
    # Non-zero bit positions are used for comparison while zero bi
    tos_mask: str
    # ToS (Type of Service) value used for comparison.
    tos: str
    # Enable negated TOS match. | Default: disable
    tos_negate: Literal["enable", "disable"]
    # Enable/disable anti-replay check. | Default: enable
    anti_replay: Literal["enable", "disable"]
    # Enable/disable creation of TCP session without SYN flag. | Default: disable
    tcp_session_without_syn: Literal["all", "data-only", "disable"]
    # Enable/disable recognition of anycast IP addresses using the | Default: disable
    geoip_anycast: Literal["enable", "disable"]
    # Match geography address based either on its physical locatio | Default: physical-location
    geoip_match: Literal["physical-location", "registered-location"]
    # Enable/disable dynamic RADIUS defined traffic shaping. | Default: disable
    dynamic_shaping: Literal["enable", "disable"]
    # Enable/disable passive WAN health measurement. When enabled, | Default: disable
    passive_wan_health_measurement: Literal["enable", "disable"]
    # Enable/disable application TCP metrics in session logs.When | Default: disable
    app_monitor: Literal["enable", "disable"]
    # Enable to add one or more security profiles (AV, IPS, etc.) | Default: disable
    utm_status: Literal["enable", "disable"]
    # Policy inspection mode (Flow/proxy). Default is Flow mode. | Default: flow
    inspection_mode: Literal["proxy", "flow"]
    # Redirect HTTP(S) traffic to matching transparent web proxy p | Default: disable
    http_policy_redirect: Literal["enable", "disable", "legacy"]
    # Redirect SSH traffic to matching transparent proxy policy. | Default: disable
    ssh_policy_redirect: Literal["enable", "disable"]
    # Redirect ZTNA traffic to matching Access-Proxy proxy-policy. | Default: disable
    ztna_policy_redirect: Literal["enable", "disable"]
    # Webproxy profile name. | MaxLen: 63
    webproxy_profile: str
    # Determine whether the firewall policy allows security profil | Default: single
    profile_type: Literal["single", "group"]
    # Name of profile group. | MaxLen: 47
    profile_group: str
    # Name of an existing Protocol options profile. | Default: default | MaxLen: 47
    profile_protocol_options: str
    # Name of an existing SSL SSH profile. | Default: no-inspection | MaxLen: 47
    ssl_ssh_profile: str
    # Name of an existing Antivirus profile. | MaxLen: 47
    av_profile: str
    # Name of an existing Web filter profile. | MaxLen: 47
    webfilter_profile: str
    # Name of an existing DNS filter profile. | MaxLen: 47
    dnsfilter_profile: str
    # Name of an existing email filter profile. | MaxLen: 47
    emailfilter_profile: str
    # Name of an existing DLP profile. | MaxLen: 47
    dlp_profile: str
    # Name of an existing file-filter profile. | MaxLen: 47
    file_filter_profile: str
    # Name of an existing IPS sensor. | MaxLen: 47
    ips_sensor: str
    # Name of an existing Application list. | MaxLen: 47
    application_list: str
    # Name of an existing VoIP (voipd) profile. | MaxLen: 47
    voip_profile: str
    # Name of an existing VoIP (ips) profile. | MaxLen: 47
    ips_voip_filter: str
    # Name of an existing SCTP filter profile. | MaxLen: 47
    sctp_filter_profile: str
    # Name of an existing Diameter filter profile. | MaxLen: 47
    diameter_filter_profile: str
    # Name of an existing virtual-patch profile. | MaxLen: 47
    virtual_patch_profile: str
    # Name of an existing ICAP profile. | MaxLen: 47
    icap_profile: str
    # Name of an existing VideoFilter profile. | MaxLen: 47
    videofilter_profile: str
    # Name of an existing Web application firewall profile. | MaxLen: 47
    waf_profile: str
    # Name of an existing SSH filter profile. | MaxLen: 47
    ssh_filter_profile: str
    # Name of an existing CASB profile. | MaxLen: 47
    casb_profile: str
    # Enable or disable logging. Log all sessions or security prof | Default: utm
    logtraffic: Literal["all", "utm", "disable"]
    # Record logs when a session starts. | Default: disable
    logtraffic_start: Literal["enable", "disable"]
    # Enable/disable HTTP transaction log. | Default: disable
    log_http_transaction: Literal["enable", "disable"]
    # Enable/disable capture packets. | Default: disable
    capture_packet: Literal["enable", "disable"]
    # Enable/disable policy traffic ASIC offloading. | Default: enable
    auto_asic_offload: Literal["enable", "disable"]
    # Enable/disable WAN optimization. | Default: disable
    wanopt: Literal["enable", "disable"]
    # WAN optimization auto-detection mode. | Default: active
    wanopt_detection: Literal["active", "passive", "off"]
    # WAN optimization passive mode options. This option decides w | Default: default
    wanopt_passive_opt: Literal["default", "transparent", "non-transparent"]
    # WAN optimization profile. | MaxLen: 35
    wanopt_profile: str
    # WAN optimization peer. | MaxLen: 35
    wanopt_peer: str
    # Enable/disable web cache. | Default: disable
    webcache: Literal["enable", "disable"]
    # Enable/disable web cache for HTTPS. | Default: disable
    webcache_https: Literal["disable", "enable"]
    # Webproxy forward server name. | MaxLen: 63
    webproxy_forward_server: str
    # Traffic shaper. | MaxLen: 35
    traffic_shaper: str
    # Reverse traffic shaper. | MaxLen: 35
    traffic_shaper_reverse: str
    # Per-IP traffic shaper. | MaxLen: 35
    per_ip_shaper: str
    # Enable/disable source NAT. | Default: disable
    nat: Literal["enable", "disable"]
    # Enable/disable PCP outbound SNAT. | Default: disable
    pcp_outbound: Literal["enable", "disable"]
    # Enable/disable PCP inbound DNAT. | Default: disable
    pcp_inbound: Literal["enable", "disable"]
    # PCP pool names.
    pcp_poolname: list[PolicyPcppoolnameObject]
    # Enable/disable fullcone NAT. Accept UDP packets from any hos | Default: disable
    permit_any_host: Literal["enable", "disable"]
    # Accept UDP packets from any Session Traversal Utilities for | Default: disable
    permit_stun_host: Literal["enable", "disable"]
    # Enable to prevent source NAT from changing a session's sourc | Default: disable
    fixedport: Literal["enable", "disable"]
    # Enable/disable preservation of the original source port from | Default: enable
    port_preserve: Literal["enable", "disable"]
    # Enable/disable random source port selection for source NAT. | Default: disable
    port_random: Literal["enable", "disable"]
    # Enable to use IP Pools for source NAT. | Default: disable
    ippool: Literal["enable", "disable"]
    # IP Pool names.
    poolname: list[PolicyPoolnameObject]
    # IPv6 pool names.
    poolname6: list[PolicyPoolname6Object]
    # TTL in seconds for sessions accepted by this policy
    session_ttl: str
    # VLAN forward direction user priority: 255 passthrough, 0 low | Default: 255 | Min: 0 | Max: 7
    vlan_cos_fwd: int
    # VLAN reverse direction user priority: 255 passthrough, 0 low | Default: 255 | Min: 0 | Max: 7
    vlan_cos_rev: int
    # Policy-based IPsec VPN: only traffic from the remote network | Default: disable
    inbound: Literal["enable", "disable"]
    # Policy-based IPsec VPN: only traffic from the internal netwo | Default: enable
    outbound: Literal["enable", "disable"]
    # Policy-based IPsec VPN: apply destination NAT to inbound tra | Default: disable
    natinbound: Literal["enable", "disable"]
    # Policy-based IPsec VPN: apply source NAT to outbound traffic | Default: disable
    natoutbound: Literal["enable", "disable"]
    # Enable/disable Forward Error Correction on traffic matching | Default: disable
    fec: Literal["enable", "disable"]
    # Enable/disable forwarding traffic matching this policy to a | Default: disable
    wccp: Literal["enable", "disable"]
    # Enable/disable NTLM authentication. | Default: disable
    ntlm: Literal["enable", "disable"]
    # Enable/disable NTLM guest user access. | Default: disable
    ntlm_guest: Literal["enable", "disable"]
    # HTTP-User-Agent value of supported browsers.
    ntlm_enabled_browsers: list[PolicyNtlmenabledbrowsersObject]
    # FSSO agent to use for NTLM authentication. | MaxLen: 35
    fsso_agent_for_ntlm: str
    # Names of user groups that can authenticate with this policy.
    groups: list[PolicyGroupsObject]
    # Names of individual users that can authenticate with this po
    users: list[PolicyUsersObject]
    # Names of FSSO groups.
    fsso_groups: list[PolicyFssogroupsObject]
    # Enable/disable authentication-based routing. | Default: disable
    auth_path: Literal["enable", "disable"]
    # Enable/disable user authentication disclaimer. | Default: disable
    disclaimer: Literal["enable", "disable"]
    # Enable/disable email collection. | Default: disable
    email_collect: Literal["enable", "disable"]
    # Policy-based IPsec VPN: name of the IPsec VPN Phase 1. | MaxLen: 35
    vpntunnel: str
    # Policy-based IPsec VPN: source NAT IP address for outgoing t | Default: 0.0.0.0 0.0.0.0
    natip: str
    # Enable to match packets that have had their destination addr | Default: enable
    match_vip: Literal["enable", "disable"]
    # Enable/disable matching of only those packets that have had | Default: disable
    match_vip_only: Literal["enable", "disable"]
    # Enable to copy packet's DiffServ values from session's origi | Default: disable
    diffserv_copy: Literal["enable", "disable"]
    # Enable to change packet's DiffServ values to the specified d | Default: disable
    diffserv_forward: Literal["enable", "disable"]
    # Enable to change packet's reverse (reply) DiffServ values to | Default: disable
    diffserv_reverse: Literal["enable", "disable"]
    # Change packet's DiffServ to this value.
    diffservcode_forward: str
    # Change packet's reverse (reply) DiffServ to this value.
    diffservcode_rev: str
    # Sender TCP maximum segment size (MSS). | Default: 0 | Min: 0 | Max: 65535
    tcp_mss_sender: int
    # Receiver TCP maximum segment size (MSS). | Default: 0 | Min: 0 | Max: 65535
    tcp_mss_receiver: int
    # Comment. | MaxLen: 1023
    comments: str
    # HTTPS server certificate for policy authentication. | MaxLen: 35
    auth_cert: str
    # HTTP-to-HTTPS redirect address for firewall authentication. | MaxLen: 63
    auth_redirect_addr: str
    # URL users are directed to after seeing and accepting the dis | MaxLen: 1023
    redirect_url: str
    # Name of identity-based routing rule. | MaxLen: 35
    identity_based_route: str
    # Enable/disable block notification. | Default: disable
    block_notification: Literal["enable", "disable"]
    # Custom fields to append to log messages for this policy.
    custom_log_fields: list[PolicyCustomlogfieldsObject]
    # Override the default replacement message group for this poli | MaxLen: 35
    replacemsg_override_group: str
    # When enabled srcaddr specifies what the source address must | Default: disable
    srcaddr_negate: Literal["enable", "disable"]
    # When enabled srcaddr6 specifies what the source address must | Default: disable
    srcaddr6_negate: Literal["enable", "disable"]
    # When enabled dstaddr specifies what the destination address | Default: disable
    dstaddr_negate: Literal["enable", "disable"]
    # When enabled dstaddr6 specifies what the destination address | Default: disable
    dstaddr6_negate: Literal["enable", "disable"]
    # When enabled ztna-ems-tag specifies what the tags must NOT b | Default: disable
    ztna_ems_tag_negate: Literal["enable", "disable"]
    # When enabled service specifies what the service must NOT be. | Default: disable
    service_negate: Literal["enable", "disable"]
    # When enabled internet-service specifies what the service mus | Default: disable
    internet_service_negate: Literal["enable", "disable"]
    # When enabled internet-service-src specifies what the service | Default: disable
    internet_service_src_negate: Literal["enable", "disable"]
    # When enabled internet-service6 specifies what the service mu | Default: disable
    internet_service6_negate: Literal["enable", "disable"]
    # When enabled internet-service6-src specifies what the servic | Default: disable
    internet_service6_src_negate: Literal["enable", "disable"]
    # Enable/disable sending RST packets when TCP sessions expire. | Default: disable
    timeout_send_rst: Literal["enable", "disable"]
    # Enable to exempt some users from the captive portal. | Default: disable
    captive_portal_exempt: Literal["enable", "disable"]
    # Decrypted traffic mirror. | MaxLen: 35
    decrypted_traffic_mirror: str
    # Enable DSRI to ignore HTTP server responses. | Default: disable
    dsri: Literal["enable", "disable"]
    # Enable MAC authentication bypass. The bypassed MAC address m | Default: disable
    radius_mac_auth_bypass: Literal["enable", "disable"]
    # Enable IP authentication bypass. The bypassed IP address mus | Default: disable
    radius_ip_auth_bypass: Literal["enable", "disable"]
    # Enable TCP NPU session delay to guarantee packet order of 3- | Default: disable
    delay_tcp_npu_session: Literal["enable", "disable"]
    # VLAN ranges to allow
    vlan_filter: str
    # Enable/disable security group tags (SGT) check. | Default: disable
    sgt_check: Literal["enable", "disable"]
    # Security group tags.
    sgt: list[PolicySgtObject]
    # FortiGuard Internet Service name.
    internet_service_fortiguard: list[PolicyInternetservicefortiguardObject]
    # FortiGuard Internet Service source name.
    internet_service_src_fortiguard: list[PolicyInternetservicesrcfortiguardObject]
    # FortiGuard IPv6 Internet Service name.
    internet_service6_fortiguard: list[PolicyInternetservice6fortiguardObject]
    # FortiGuard IPv6 Internet Service source name.
    internet_service6_src_fortiguard: list[PolicyInternetservice6srcfortiguardObject]
    
    # Common API response fields
    status: str
    http_status: int | None
    vdom: str | None
    
    # Methods from FortiObject
    @property
    def dict(self) -> dict[str, Any]:
        """Convert to dictionary."""
        ...
    @property
    def json(self) -> dict[str, Any]:
        """Convert to dictionary (alias for .dict)."""
        ...
    @property
    def raw(self) -> dict[str, Any]:
        """Get raw API response data."""
        ...
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> PolicyPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Policy:
    """
    Configure IPv4/IPv6 policies.
    
    Path: firewall/policy
    Category: cmdb
    Primary Key: policyid
    """
    
    # ================================================================
    # GET OVERLOADS - Always returns FortiObject
    # Pylance matches overloads top-to-bottom, so these must come first!
    # ================================================================
    
    # With mkey as positional arg -> returns FortiObject
    @overload
    def get(
        self,
        policyid: int,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> PolicyObject: ...
    
    # With mkey as keyword arg -> returns FortiObject
    @overload
    def get(
        self,
        *,
        policyid: int,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> PolicyObject: ...
    
    # Without mkey -> returns list of FortiObjects
    @overload
    def get(
        self,
        policyid: None = None,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> list[PolicyObject]: ...
    
    # ================================================================
    # (removed - all GET now returns FortiObject)
    # ================================================================
    
    # With mkey as positional arg -> returns single object
    @overload
    def get(
        self,
        policyid: int,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        *,
        **kwargs: Any,
    ) -> PolicyObject: ...
    
    # With mkey as keyword arg -> returns single object
    @overload
    def get(
        self,
        *,
        policyid: int,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> PolicyObject: ...
    
    # With no mkey -> returns list of objects
    @overload
    def get(
        self,
        *,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> list[PolicyObject]: ...
    
    # raw_json=True returns the full API envelope
    @overload
    def get(
        self,
        policyid: int | None = ...,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> RawAPIResponse: ...
    
    # Dict mode with mkey provided as positional arg (single dict)
    @overload
    def get(
        self,
        policyid: int,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> PolicyObject: ...
    
    # Dict mode with mkey provided as keyword arg (single dict)
    @overload
    def get(
        self,
        *,
        policyid: int,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> PolicyObject: ...
    
    # Dict mode - list of dicts (no mkey/name provided) - keyword-only signature
    @overload
    def get(
        self,
        *,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> list[PolicyObject]: ...
    
    # Fallback overload for all other cases
    @overload
    def get(
        self,
        policyid: int | None = ...,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], list[dict[str, Any]], FortiObject, list[FortiObject]]: ...
    
    def get(
        self,
        policyid: int | None = ...,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> PolicyObject | list[PolicyObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: PolicyPayload | None = ...,
        policyid: int | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        srcintf: str | list[str] | list[dict[str, Any]] | None = ...,
        dstintf: str | list[str] | list[dict[str, Any]] | None = ...,
        action: Literal["accept", "deny", "ipsec"] | None = ...,
        nat64: Literal["enable", "disable"] | None = ...,
        nat46: Literal["enable", "disable"] | None = ...,
        ztna_status: Literal["enable", "disable"] | None = ...,
        ztna_device_ownership: Literal["enable", "disable"] | None = ...,
        srcaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        ztna_ems_tag: str | list[str] | list[dict[str, Any]] | None = ...,
        ztna_ems_tag_secondary: str | list[str] | list[dict[str, Any]] | None = ...,
        ztna_tags_match_logic: Literal["or", "and"] | None = ...,
        ztna_geo_tag: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service: Literal["enable", "disable"] | None = ...,
        internet_service_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        network_service_dynamic: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src: Literal["enable", "disable"] | None = ...,
        internet_service_src_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        network_service_src_dynamic: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        reputation_minimum: int | None = ...,
        reputation_direction: Literal["source", "destination"] | None = ...,
        src_vendor_mac: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6: Literal["enable", "disable"] | None = ...,
        internet_service6_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src: Literal["enable", "disable"] | None = ...,
        internet_service6_src_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        reputation_minimum6: int | None = ...,
        reputation_direction6: Literal["source", "destination"] | None = ...,
        rtp_nat: Literal["disable", "enable"] | None = ...,
        rtp_addr: str | list[str] | list[dict[str, Any]] | None = ...,
        send_deny_packet: Literal["disable", "enable"] | None = ...,
        firewall_session_dirty: Literal["check-all", "check-new"] | None = ...,
        schedule: str | None = ...,
        schedule_timeout: Literal["enable", "disable"] | None = ...,
        policy_expiry: Literal["enable", "disable"] | None = ...,
        policy_expiry_date: str | None = ...,
        policy_expiry_date_utc: str | None = ...,
        service: str | list[str] | list[dict[str, Any]] | None = ...,
        tos_mask: str | None = ...,
        tos: str | None = ...,
        tos_negate: Literal["enable", "disable"] | None = ...,
        anti_replay: Literal["enable", "disable"] | None = ...,
        tcp_session_without_syn: Literal["all", "data-only", "disable"] | None = ...,
        geoip_anycast: Literal["enable", "disable"] | None = ...,
        geoip_match: Literal["physical-location", "registered-location"] | None = ...,
        dynamic_shaping: Literal["enable", "disable"] | None = ...,
        passive_wan_health_measurement: Literal["enable", "disable"] | None = ...,
        app_monitor: Literal["enable", "disable"] | None = ...,
        utm_status: Literal["enable", "disable"] | None = ...,
        inspection_mode: Literal["proxy", "flow"] | None = ...,
        http_policy_redirect: Literal["enable", "disable", "legacy"] | None = ...,
        ssh_policy_redirect: Literal["enable", "disable"] | None = ...,
        ztna_policy_redirect: Literal["enable", "disable"] | None = ...,
        webproxy_profile: str | None = ...,
        profile_type: Literal["single", "group"] | None = ...,
        profile_group: str | None = ...,
        profile_protocol_options: str | None = ...,
        ssl_ssh_profile: str | None = ...,
        av_profile: str | None = ...,
        webfilter_profile: str | None = ...,
        dnsfilter_profile: str | None = ...,
        emailfilter_profile: str | None = ...,
        dlp_profile: str | None = ...,
        file_filter_profile: str | None = ...,
        ips_sensor: str | None = ...,
        application_list: str | None = ...,
        voip_profile: str | None = ...,
        ips_voip_filter: str | None = ...,
        sctp_filter_profile: str | None = ...,
        diameter_filter_profile: str | None = ...,
        virtual_patch_profile: str | None = ...,
        icap_profile: str | None = ...,
        videofilter_profile: str | None = ...,
        waf_profile: str | None = ...,
        ssh_filter_profile: str | None = ...,
        casb_profile: str | None = ...,
        logtraffic: Literal["all", "utm", "disable"] | None = ...,
        logtraffic_start: Literal["enable", "disable"] | None = ...,
        log_http_transaction: Literal["enable", "disable"] | None = ...,
        capture_packet: Literal["enable", "disable"] | None = ...,
        auto_asic_offload: Literal["enable", "disable"] | None = ...,
        wanopt: Literal["enable", "disable"] | None = ...,
        wanopt_detection: Literal["active", "passive", "off"] | None = ...,
        wanopt_passive_opt: Literal["default", "transparent", "non-transparent"] | None = ...,
        wanopt_profile: str | None = ...,
        wanopt_peer: str | None = ...,
        webcache: Literal["enable", "disable"] | None = ...,
        webcache_https: Literal["disable", "enable"] | None = ...,
        webproxy_forward_server: str | None = ...,
        traffic_shaper: str | None = ...,
        traffic_shaper_reverse: str | None = ...,
        per_ip_shaper: str | None = ...,
        nat: Literal["enable", "disable"] | None = ...,
        pcp_outbound: Literal["enable", "disable"] | None = ...,
        pcp_inbound: Literal["enable", "disable"] | None = ...,
        pcp_poolname: str | list[str] | list[dict[str, Any]] | None = ...,
        permit_any_host: Literal["enable", "disable"] | None = ...,
        permit_stun_host: Literal["enable", "disable"] | None = ...,
        fixedport: Literal["enable", "disable"] | None = ...,
        port_preserve: Literal["enable", "disable"] | None = ...,
        port_random: Literal["enable", "disable"] | None = ...,
        ippool: Literal["enable", "disable"] | None = ...,
        poolname: str | list[str] | list[dict[str, Any]] | None = ...,
        poolname6: str | list[str] | list[dict[str, Any]] | None = ...,
        session_ttl: str | None = ...,
        vlan_cos_fwd: int | None = ...,
        vlan_cos_rev: int | None = ...,
        inbound: Literal["enable", "disable"] | None = ...,
        outbound: Literal["enable", "disable"] | None = ...,
        natinbound: Literal["enable", "disable"] | None = ...,
        natoutbound: Literal["enable", "disable"] | None = ...,
        fec: Literal["enable", "disable"] | None = ...,
        wccp: Literal["enable", "disable"] | None = ...,
        ntlm: Literal["enable", "disable"] | None = ...,
        ntlm_guest: Literal["enable", "disable"] | None = ...,
        ntlm_enabled_browsers: str | list[str] | list[dict[str, Any]] | None = ...,
        fsso_agent_for_ntlm: str | None = ...,
        groups: str | list[str] | list[dict[str, Any]] | None = ...,
        users: str | list[str] | list[dict[str, Any]] | None = ...,
        fsso_groups: str | list[str] | list[dict[str, Any]] | None = ...,
        auth_path: Literal["enable", "disable"] | None = ...,
        disclaimer: Literal["enable", "disable"] | None = ...,
        email_collect: Literal["enable", "disable"] | None = ...,
        vpntunnel: str | None = ...,
        natip: str | None = ...,
        match_vip: Literal["enable", "disable"] | None = ...,
        match_vip_only: Literal["enable", "disable"] | None = ...,
        diffserv_copy: Literal["enable", "disable"] | None = ...,
        diffserv_forward: Literal["enable", "disable"] | None = ...,
        diffserv_reverse: Literal["enable", "disable"] | None = ...,
        diffservcode_forward: str | None = ...,
        diffservcode_rev: str | None = ...,
        tcp_mss_sender: int | None = ...,
        tcp_mss_receiver: int | None = ...,
        comments: str | None = ...,
        auth_cert: str | None = ...,
        auth_redirect_addr: str | None = ...,
        redirect_url: str | None = ...,
        identity_based_route: str | None = ...,
        block_notification: Literal["enable", "disable"] | None = ...,
        custom_log_fields: str | list[str] | list[dict[str, Any]] | None = ...,
        replacemsg_override_group: str | None = ...,
        srcaddr_negate: Literal["enable", "disable"] | None = ...,
        srcaddr6_negate: Literal["enable", "disable"] | None = ...,
        dstaddr_negate: Literal["enable", "disable"] | None = ...,
        dstaddr6_negate: Literal["enable", "disable"] | None = ...,
        ztna_ems_tag_negate: Literal["enable", "disable"] | None = ...,
        service_negate: Literal["enable", "disable"] | None = ...,
        internet_service_negate: Literal["enable", "disable"] | None = ...,
        internet_service_src_negate: Literal["enable", "disable"] | None = ...,
        internet_service6_negate: Literal["enable", "disable"] | None = ...,
        internet_service6_src_negate: Literal["enable", "disable"] | None = ...,
        timeout_send_rst: Literal["enable", "disable"] | None = ...,
        captive_portal_exempt: Literal["enable", "disable"] | None = ...,
        decrypted_traffic_mirror: str | None = ...,
        dsri: Literal["enable", "disable"] | None = ...,
        radius_mac_auth_bypass: Literal["enable", "disable"] | None = ...,
        radius_ip_auth_bypass: Literal["enable", "disable"] | None = ...,
        delay_tcp_npu_session: Literal["enable", "disable"] | None = ...,
        vlan_filter: str | None = ...,
        sgt_check: Literal["enable", "disable"] | None = ...,
        sgt: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> PolicyObject: ...
    
    @overload
    def post(
        self,
        payload_dict: PolicyPayload | None = ...,
        policyid: int | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        srcintf: str | list[str] | list[dict[str, Any]] | None = ...,
        dstintf: str | list[str] | list[dict[str, Any]] | None = ...,
        action: Literal["accept", "deny", "ipsec"] | None = ...,
        nat64: Literal["enable", "disable"] | None = ...,
        nat46: Literal["enable", "disable"] | None = ...,
        ztna_status: Literal["enable", "disable"] | None = ...,
        ztna_device_ownership: Literal["enable", "disable"] | None = ...,
        srcaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        ztna_ems_tag: str | list[str] | list[dict[str, Any]] | None = ...,
        ztna_ems_tag_secondary: str | list[str] | list[dict[str, Any]] | None = ...,
        ztna_tags_match_logic: Literal["or", "and"] | None = ...,
        ztna_geo_tag: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service: Literal["enable", "disable"] | None = ...,
        internet_service_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        network_service_dynamic: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src: Literal["enable", "disable"] | None = ...,
        internet_service_src_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        network_service_src_dynamic: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        reputation_minimum: int | None = ...,
        reputation_direction: Literal["source", "destination"] | None = ...,
        src_vendor_mac: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6: Literal["enable", "disable"] | None = ...,
        internet_service6_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src: Literal["enable", "disable"] | None = ...,
        internet_service6_src_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        reputation_minimum6: int | None = ...,
        reputation_direction6: Literal["source", "destination"] | None = ...,
        rtp_nat: Literal["disable", "enable"] | None = ...,
        rtp_addr: str | list[str] | list[dict[str, Any]] | None = ...,
        send_deny_packet: Literal["disable", "enable"] | None = ...,
        firewall_session_dirty: Literal["check-all", "check-new"] | None = ...,
        schedule: str | None = ...,
        schedule_timeout: Literal["enable", "disable"] | None = ...,
        policy_expiry: Literal["enable", "disable"] | None = ...,
        policy_expiry_date: str | None = ...,
        policy_expiry_date_utc: str | None = ...,
        service: str | list[str] | list[dict[str, Any]] | None = ...,
        tos_mask: str | None = ...,
        tos: str | None = ...,
        tos_negate: Literal["enable", "disable"] | None = ...,
        anti_replay: Literal["enable", "disable"] | None = ...,
        tcp_session_without_syn: Literal["all", "data-only", "disable"] | None = ...,
        geoip_anycast: Literal["enable", "disable"] | None = ...,
        geoip_match: Literal["physical-location", "registered-location"] | None = ...,
        dynamic_shaping: Literal["enable", "disable"] | None = ...,
        passive_wan_health_measurement: Literal["enable", "disable"] | None = ...,
        app_monitor: Literal["enable", "disable"] | None = ...,
        utm_status: Literal["enable", "disable"] | None = ...,
        inspection_mode: Literal["proxy", "flow"] | None = ...,
        http_policy_redirect: Literal["enable", "disable", "legacy"] | None = ...,
        ssh_policy_redirect: Literal["enable", "disable"] | None = ...,
        ztna_policy_redirect: Literal["enable", "disable"] | None = ...,
        webproxy_profile: str | None = ...,
        profile_type: Literal["single", "group"] | None = ...,
        profile_group: str | None = ...,
        profile_protocol_options: str | None = ...,
        ssl_ssh_profile: str | None = ...,
        av_profile: str | None = ...,
        webfilter_profile: str | None = ...,
        dnsfilter_profile: str | None = ...,
        emailfilter_profile: str | None = ...,
        dlp_profile: str | None = ...,
        file_filter_profile: str | None = ...,
        ips_sensor: str | None = ...,
        application_list: str | None = ...,
        voip_profile: str | None = ...,
        ips_voip_filter: str | None = ...,
        sctp_filter_profile: str | None = ...,
        diameter_filter_profile: str | None = ...,
        virtual_patch_profile: str | None = ...,
        icap_profile: str | None = ...,
        videofilter_profile: str | None = ...,
        waf_profile: str | None = ...,
        ssh_filter_profile: str | None = ...,
        casb_profile: str | None = ...,
        logtraffic: Literal["all", "utm", "disable"] | None = ...,
        logtraffic_start: Literal["enable", "disable"] | None = ...,
        log_http_transaction: Literal["enable", "disable"] | None = ...,
        capture_packet: Literal["enable", "disable"] | None = ...,
        auto_asic_offload: Literal["enable", "disable"] | None = ...,
        wanopt: Literal["enable", "disable"] | None = ...,
        wanopt_detection: Literal["active", "passive", "off"] | None = ...,
        wanopt_passive_opt: Literal["default", "transparent", "non-transparent"] | None = ...,
        wanopt_profile: str | None = ...,
        wanopt_peer: str | None = ...,
        webcache: Literal["enable", "disable"] | None = ...,
        webcache_https: Literal["disable", "enable"] | None = ...,
        webproxy_forward_server: str | None = ...,
        traffic_shaper: str | None = ...,
        traffic_shaper_reverse: str | None = ...,
        per_ip_shaper: str | None = ...,
        nat: Literal["enable", "disable"] | None = ...,
        pcp_outbound: Literal["enable", "disable"] | None = ...,
        pcp_inbound: Literal["enable", "disable"] | None = ...,
        pcp_poolname: str | list[str] | list[dict[str, Any]] | None = ...,
        permit_any_host: Literal["enable", "disable"] | None = ...,
        permit_stun_host: Literal["enable", "disable"] | None = ...,
        fixedport: Literal["enable", "disable"] | None = ...,
        port_preserve: Literal["enable", "disable"] | None = ...,
        port_random: Literal["enable", "disable"] | None = ...,
        ippool: Literal["enable", "disable"] | None = ...,
        poolname: str | list[str] | list[dict[str, Any]] | None = ...,
        poolname6: str | list[str] | list[dict[str, Any]] | None = ...,
        session_ttl: str | None = ...,
        vlan_cos_fwd: int | None = ...,
        vlan_cos_rev: int | None = ...,
        inbound: Literal["enable", "disable"] | None = ...,
        outbound: Literal["enable", "disable"] | None = ...,
        natinbound: Literal["enable", "disable"] | None = ...,
        natoutbound: Literal["enable", "disable"] | None = ...,
        fec: Literal["enable", "disable"] | None = ...,
        wccp: Literal["enable", "disable"] | None = ...,
        ntlm: Literal["enable", "disable"] | None = ...,
        ntlm_guest: Literal["enable", "disable"] | None = ...,
        ntlm_enabled_browsers: str | list[str] | list[dict[str, Any]] | None = ...,
        fsso_agent_for_ntlm: str | None = ...,
        groups: str | list[str] | list[dict[str, Any]] | None = ...,
        users: str | list[str] | list[dict[str, Any]] | None = ...,
        fsso_groups: str | list[str] | list[dict[str, Any]] | None = ...,
        auth_path: Literal["enable", "disable"] | None = ...,
        disclaimer: Literal["enable", "disable"] | None = ...,
        email_collect: Literal["enable", "disable"] | None = ...,
        vpntunnel: str | None = ...,
        natip: str | None = ...,
        match_vip: Literal["enable", "disable"] | None = ...,
        match_vip_only: Literal["enable", "disable"] | None = ...,
        diffserv_copy: Literal["enable", "disable"] | None = ...,
        diffserv_forward: Literal["enable", "disable"] | None = ...,
        diffserv_reverse: Literal["enable", "disable"] | None = ...,
        diffservcode_forward: str | None = ...,
        diffservcode_rev: str | None = ...,
        tcp_mss_sender: int | None = ...,
        tcp_mss_receiver: int | None = ...,
        comments: str | None = ...,
        auth_cert: str | None = ...,
        auth_redirect_addr: str | None = ...,
        redirect_url: str | None = ...,
        identity_based_route: str | None = ...,
        block_notification: Literal["enable", "disable"] | None = ...,
        custom_log_fields: str | list[str] | list[dict[str, Any]] | None = ...,
        replacemsg_override_group: str | None = ...,
        srcaddr_negate: Literal["enable", "disable"] | None = ...,
        srcaddr6_negate: Literal["enable", "disable"] | None = ...,
        dstaddr_negate: Literal["enable", "disable"] | None = ...,
        dstaddr6_negate: Literal["enable", "disable"] | None = ...,
        ztna_ems_tag_negate: Literal["enable", "disable"] | None = ...,
        service_negate: Literal["enable", "disable"] | None = ...,
        internet_service_negate: Literal["enable", "disable"] | None = ...,
        internet_service_src_negate: Literal["enable", "disable"] | None = ...,
        internet_service6_negate: Literal["enable", "disable"] | None = ...,
        internet_service6_src_negate: Literal["enable", "disable"] | None = ...,
        timeout_send_rst: Literal["enable", "disable"] | None = ...,
        captive_portal_exempt: Literal["enable", "disable"] | None = ...,
        decrypted_traffic_mirror: str | None = ...,
        dsri: Literal["enable", "disable"] | None = ...,
        radius_mac_auth_bypass: Literal["enable", "disable"] | None = ...,
        radius_ip_auth_bypass: Literal["enable", "disable"] | None = ...,
        delay_tcp_npu_session: Literal["enable", "disable"] | None = ...,
        vlan_filter: str | None = ...,
        sgt_check: Literal["enable", "disable"] | None = ...,
        sgt: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    # raw_json=True returns the full API envelope
    @overload
    def post(
        self,
        payload_dict: PolicyPayload | None = ...,
        policyid: int | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        srcintf: str | list[str] | list[dict[str, Any]] | None = ...,
        dstintf: str | list[str] | list[dict[str, Any]] | None = ...,
        action: Literal["accept", "deny", "ipsec"] | None = ...,
        nat64: Literal["enable", "disable"] | None = ...,
        nat46: Literal["enable", "disable"] | None = ...,
        ztna_status: Literal["enable", "disable"] | None = ...,
        ztna_device_ownership: Literal["enable", "disable"] | None = ...,
        srcaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        ztna_ems_tag: str | list[str] | list[dict[str, Any]] | None = ...,
        ztna_ems_tag_secondary: str | list[str] | list[dict[str, Any]] | None = ...,
        ztna_tags_match_logic: Literal["or", "and"] | None = ...,
        ztna_geo_tag: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service: Literal["enable", "disable"] | None = ...,
        internet_service_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        network_service_dynamic: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src: Literal["enable", "disable"] | None = ...,
        internet_service_src_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        network_service_src_dynamic: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        reputation_minimum: int | None = ...,
        reputation_direction: Literal["source", "destination"] | None = ...,
        src_vendor_mac: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6: Literal["enable", "disable"] | None = ...,
        internet_service6_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src: Literal["enable", "disable"] | None = ...,
        internet_service6_src_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        reputation_minimum6: int | None = ...,
        reputation_direction6: Literal["source", "destination"] | None = ...,
        rtp_nat: Literal["disable", "enable"] | None = ...,
        rtp_addr: str | list[str] | list[dict[str, Any]] | None = ...,
        send_deny_packet: Literal["disable", "enable"] | None = ...,
        firewall_session_dirty: Literal["check-all", "check-new"] | None = ...,
        schedule: str | None = ...,
        schedule_timeout: Literal["enable", "disable"] | None = ...,
        policy_expiry: Literal["enable", "disable"] | None = ...,
        policy_expiry_date: str | None = ...,
        policy_expiry_date_utc: str | None = ...,
        service: str | list[str] | list[dict[str, Any]] | None = ...,
        tos_mask: str | None = ...,
        tos: str | None = ...,
        tos_negate: Literal["enable", "disable"] | None = ...,
        anti_replay: Literal["enable", "disable"] | None = ...,
        tcp_session_without_syn: Literal["all", "data-only", "disable"] | None = ...,
        geoip_anycast: Literal["enable", "disable"] | None = ...,
        geoip_match: Literal["physical-location", "registered-location"] | None = ...,
        dynamic_shaping: Literal["enable", "disable"] | None = ...,
        passive_wan_health_measurement: Literal["enable", "disable"] | None = ...,
        app_monitor: Literal["enable", "disable"] | None = ...,
        utm_status: Literal["enable", "disable"] | None = ...,
        inspection_mode: Literal["proxy", "flow"] | None = ...,
        http_policy_redirect: Literal["enable", "disable", "legacy"] | None = ...,
        ssh_policy_redirect: Literal["enable", "disable"] | None = ...,
        ztna_policy_redirect: Literal["enable", "disable"] | None = ...,
        webproxy_profile: str | None = ...,
        profile_type: Literal["single", "group"] | None = ...,
        profile_group: str | None = ...,
        profile_protocol_options: str | None = ...,
        ssl_ssh_profile: str | None = ...,
        av_profile: str | None = ...,
        webfilter_profile: str | None = ...,
        dnsfilter_profile: str | None = ...,
        emailfilter_profile: str | None = ...,
        dlp_profile: str | None = ...,
        file_filter_profile: str | None = ...,
        ips_sensor: str | None = ...,
        application_list: str | None = ...,
        voip_profile: str | None = ...,
        ips_voip_filter: str | None = ...,
        sctp_filter_profile: str | None = ...,
        diameter_filter_profile: str | None = ...,
        virtual_patch_profile: str | None = ...,
        icap_profile: str | None = ...,
        videofilter_profile: str | None = ...,
        waf_profile: str | None = ...,
        ssh_filter_profile: str | None = ...,
        casb_profile: str | None = ...,
        logtraffic: Literal["all", "utm", "disable"] | None = ...,
        logtraffic_start: Literal["enable", "disable"] | None = ...,
        log_http_transaction: Literal["enable", "disable"] | None = ...,
        capture_packet: Literal["enable", "disable"] | None = ...,
        auto_asic_offload: Literal["enable", "disable"] | None = ...,
        wanopt: Literal["enable", "disable"] | None = ...,
        wanopt_detection: Literal["active", "passive", "off"] | None = ...,
        wanopt_passive_opt: Literal["default", "transparent", "non-transparent"] | None = ...,
        wanopt_profile: str | None = ...,
        wanopt_peer: str | None = ...,
        webcache: Literal["enable", "disable"] | None = ...,
        webcache_https: Literal["disable", "enable"] | None = ...,
        webproxy_forward_server: str | None = ...,
        traffic_shaper: str | None = ...,
        traffic_shaper_reverse: str | None = ...,
        per_ip_shaper: str | None = ...,
        nat: Literal["enable", "disable"] | None = ...,
        pcp_outbound: Literal["enable", "disable"] | None = ...,
        pcp_inbound: Literal["enable", "disable"] | None = ...,
        pcp_poolname: str | list[str] | list[dict[str, Any]] | None = ...,
        permit_any_host: Literal["enable", "disable"] | None = ...,
        permit_stun_host: Literal["enable", "disable"] | None = ...,
        fixedport: Literal["enable", "disable"] | None = ...,
        port_preserve: Literal["enable", "disable"] | None = ...,
        port_random: Literal["enable", "disable"] | None = ...,
        ippool: Literal["enable", "disable"] | None = ...,
        poolname: str | list[str] | list[dict[str, Any]] | None = ...,
        poolname6: str | list[str] | list[dict[str, Any]] | None = ...,
        session_ttl: str | None = ...,
        vlan_cos_fwd: int | None = ...,
        vlan_cos_rev: int | None = ...,
        inbound: Literal["enable", "disable"] | None = ...,
        outbound: Literal["enable", "disable"] | None = ...,
        natinbound: Literal["enable", "disable"] | None = ...,
        natoutbound: Literal["enable", "disable"] | None = ...,
        fec: Literal["enable", "disable"] | None = ...,
        wccp: Literal["enable", "disable"] | None = ...,
        ntlm: Literal["enable", "disable"] | None = ...,
        ntlm_guest: Literal["enable", "disable"] | None = ...,
        ntlm_enabled_browsers: str | list[str] | list[dict[str, Any]] | None = ...,
        fsso_agent_for_ntlm: str | None = ...,
        groups: str | list[str] | list[dict[str, Any]] | None = ...,
        users: str | list[str] | list[dict[str, Any]] | None = ...,
        fsso_groups: str | list[str] | list[dict[str, Any]] | None = ...,
        auth_path: Literal["enable", "disable"] | None = ...,
        disclaimer: Literal["enable", "disable"] | None = ...,
        email_collect: Literal["enable", "disable"] | None = ...,
        vpntunnel: str | None = ...,
        natip: str | None = ...,
        match_vip: Literal["enable", "disable"] | None = ...,
        match_vip_only: Literal["enable", "disable"] | None = ...,
        diffserv_copy: Literal["enable", "disable"] | None = ...,
        diffserv_forward: Literal["enable", "disable"] | None = ...,
        diffserv_reverse: Literal["enable", "disable"] | None = ...,
        diffservcode_forward: str | None = ...,
        diffservcode_rev: str | None = ...,
        tcp_mss_sender: int | None = ...,
        tcp_mss_receiver: int | None = ...,
        comments: str | None = ...,
        auth_cert: str | None = ...,
        auth_redirect_addr: str | None = ...,
        redirect_url: str | None = ...,
        identity_based_route: str | None = ...,
        block_notification: Literal["enable", "disable"] | None = ...,
        custom_log_fields: str | list[str] | list[dict[str, Any]] | None = ...,
        replacemsg_override_group: str | None = ...,
        srcaddr_negate: Literal["enable", "disable"] | None = ...,
        srcaddr6_negate: Literal["enable", "disable"] | None = ...,
        dstaddr_negate: Literal["enable", "disable"] | None = ...,
        dstaddr6_negate: Literal["enable", "disable"] | None = ...,
        ztna_ems_tag_negate: Literal["enable", "disable"] | None = ...,
        service_negate: Literal["enable", "disable"] | None = ...,
        internet_service_negate: Literal["enable", "disable"] | None = ...,
        internet_service_src_negate: Literal["enable", "disable"] | None = ...,
        internet_service6_negate: Literal["enable", "disable"] | None = ...,
        internet_service6_src_negate: Literal["enable", "disable"] | None = ...,
        timeout_send_rst: Literal["enable", "disable"] | None = ...,
        captive_portal_exempt: Literal["enable", "disable"] | None = ...,
        decrypted_traffic_mirror: str | None = ...,
        dsri: Literal["enable", "disable"] | None = ...,
        radius_mac_auth_bypass: Literal["enable", "disable"] | None = ...,
        radius_ip_auth_bypass: Literal["enable", "disable"] | None = ...,
        delay_tcp_npu_session: Literal["enable", "disable"] | None = ...,
        vlan_filter: str | None = ...,
        sgt_check: Literal["enable", "disable"] | None = ...,
        sgt: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> RawAPIResponse: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: PolicyPayload | None = ...,
        policyid: int | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        srcintf: str | list[str] | list[dict[str, Any]] | None = ...,
        dstintf: str | list[str] | list[dict[str, Any]] | None = ...,
        action: Literal["accept", "deny", "ipsec"] | None = ...,
        nat64: Literal["enable", "disable"] | None = ...,
        nat46: Literal["enable", "disable"] | None = ...,
        ztna_status: Literal["enable", "disable"] | None = ...,
        ztna_device_ownership: Literal["enable", "disable"] | None = ...,
        srcaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        ztna_ems_tag: str | list[str] | list[dict[str, Any]] | None = ...,
        ztna_ems_tag_secondary: str | list[str] | list[dict[str, Any]] | None = ...,
        ztna_tags_match_logic: Literal["or", "and"] | None = ...,
        ztna_geo_tag: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service: Literal["enable", "disable"] | None = ...,
        internet_service_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        network_service_dynamic: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src: Literal["enable", "disable"] | None = ...,
        internet_service_src_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        network_service_src_dynamic: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        reputation_minimum: int | None = ...,
        reputation_direction: Literal["source", "destination"] | None = ...,
        src_vendor_mac: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6: Literal["enable", "disable"] | None = ...,
        internet_service6_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src: Literal["enable", "disable"] | None = ...,
        internet_service6_src_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        reputation_minimum6: int | None = ...,
        reputation_direction6: Literal["source", "destination"] | None = ...,
        rtp_nat: Literal["disable", "enable"] | None = ...,
        rtp_addr: str | list[str] | list[dict[str, Any]] | None = ...,
        send_deny_packet: Literal["disable", "enable"] | None = ...,
        firewall_session_dirty: Literal["check-all", "check-new"] | None = ...,
        schedule: str | None = ...,
        schedule_timeout: Literal["enable", "disable"] | None = ...,
        policy_expiry: Literal["enable", "disable"] | None = ...,
        policy_expiry_date: str | None = ...,
        policy_expiry_date_utc: str | None = ...,
        service: str | list[str] | list[dict[str, Any]] | None = ...,
        tos_mask: str | None = ...,
        tos: str | None = ...,
        tos_negate: Literal["enable", "disable"] | None = ...,
        anti_replay: Literal["enable", "disable"] | None = ...,
        tcp_session_without_syn: Literal["all", "data-only", "disable"] | None = ...,
        geoip_anycast: Literal["enable", "disable"] | None = ...,
        geoip_match: Literal["physical-location", "registered-location"] | None = ...,
        dynamic_shaping: Literal["enable", "disable"] | None = ...,
        passive_wan_health_measurement: Literal["enable", "disable"] | None = ...,
        app_monitor: Literal["enable", "disable"] | None = ...,
        utm_status: Literal["enable", "disable"] | None = ...,
        inspection_mode: Literal["proxy", "flow"] | None = ...,
        http_policy_redirect: Literal["enable", "disable", "legacy"] | None = ...,
        ssh_policy_redirect: Literal["enable", "disable"] | None = ...,
        ztna_policy_redirect: Literal["enable", "disable"] | None = ...,
        webproxy_profile: str | None = ...,
        profile_type: Literal["single", "group"] | None = ...,
        profile_group: str | None = ...,
        profile_protocol_options: str | None = ...,
        ssl_ssh_profile: str | None = ...,
        av_profile: str | None = ...,
        webfilter_profile: str | None = ...,
        dnsfilter_profile: str | None = ...,
        emailfilter_profile: str | None = ...,
        dlp_profile: str | None = ...,
        file_filter_profile: str | None = ...,
        ips_sensor: str | None = ...,
        application_list: str | None = ...,
        voip_profile: str | None = ...,
        ips_voip_filter: str | None = ...,
        sctp_filter_profile: str | None = ...,
        diameter_filter_profile: str | None = ...,
        virtual_patch_profile: str | None = ...,
        icap_profile: str | None = ...,
        videofilter_profile: str | None = ...,
        waf_profile: str | None = ...,
        ssh_filter_profile: str | None = ...,
        casb_profile: str | None = ...,
        logtraffic: Literal["all", "utm", "disable"] | None = ...,
        logtraffic_start: Literal["enable", "disable"] | None = ...,
        log_http_transaction: Literal["enable", "disable"] | None = ...,
        capture_packet: Literal["enable", "disable"] | None = ...,
        auto_asic_offload: Literal["enable", "disable"] | None = ...,
        wanopt: Literal["enable", "disable"] | None = ...,
        wanopt_detection: Literal["active", "passive", "off"] | None = ...,
        wanopt_passive_opt: Literal["default", "transparent", "non-transparent"] | None = ...,
        wanopt_profile: str | None = ...,
        wanopt_peer: str | None = ...,
        webcache: Literal["enable", "disable"] | None = ...,
        webcache_https: Literal["disable", "enable"] | None = ...,
        webproxy_forward_server: str | None = ...,
        traffic_shaper: str | None = ...,
        traffic_shaper_reverse: str | None = ...,
        per_ip_shaper: str | None = ...,
        nat: Literal["enable", "disable"] | None = ...,
        pcp_outbound: Literal["enable", "disable"] | None = ...,
        pcp_inbound: Literal["enable", "disable"] | None = ...,
        pcp_poolname: str | list[str] | list[dict[str, Any]] | None = ...,
        permit_any_host: Literal["enable", "disable"] | None = ...,
        permit_stun_host: Literal["enable", "disable"] | None = ...,
        fixedport: Literal["enable", "disable"] | None = ...,
        port_preserve: Literal["enable", "disable"] | None = ...,
        port_random: Literal["enable", "disable"] | None = ...,
        ippool: Literal["enable", "disable"] | None = ...,
        poolname: str | list[str] | list[dict[str, Any]] | None = ...,
        poolname6: str | list[str] | list[dict[str, Any]] | None = ...,
        session_ttl: str | None = ...,
        vlan_cos_fwd: int | None = ...,
        vlan_cos_rev: int | None = ...,
        inbound: Literal["enable", "disable"] | None = ...,
        outbound: Literal["enable", "disable"] | None = ...,
        natinbound: Literal["enable", "disable"] | None = ...,
        natoutbound: Literal["enable", "disable"] | None = ...,
        fec: Literal["enable", "disable"] | None = ...,
        wccp: Literal["enable", "disable"] | None = ...,
        ntlm: Literal["enable", "disable"] | None = ...,
        ntlm_guest: Literal["enable", "disable"] | None = ...,
        ntlm_enabled_browsers: str | list[str] | list[dict[str, Any]] | None = ...,
        fsso_agent_for_ntlm: str | None = ...,
        groups: str | list[str] | list[dict[str, Any]] | None = ...,
        users: str | list[str] | list[dict[str, Any]] | None = ...,
        fsso_groups: str | list[str] | list[dict[str, Any]] | None = ...,
        auth_path: Literal["enable", "disable"] | None = ...,
        disclaimer: Literal["enable", "disable"] | None = ...,
        email_collect: Literal["enable", "disable"] | None = ...,
        vpntunnel: str | None = ...,
        natip: str | None = ...,
        match_vip: Literal["enable", "disable"] | None = ...,
        match_vip_only: Literal["enable", "disable"] | None = ...,
        diffserv_copy: Literal["enable", "disable"] | None = ...,
        diffserv_forward: Literal["enable", "disable"] | None = ...,
        diffserv_reverse: Literal["enable", "disable"] | None = ...,
        diffservcode_forward: str | None = ...,
        diffservcode_rev: str | None = ...,
        tcp_mss_sender: int | None = ...,
        tcp_mss_receiver: int | None = ...,
        comments: str | None = ...,
        auth_cert: str | None = ...,
        auth_redirect_addr: str | None = ...,
        redirect_url: str | None = ...,
        identity_based_route: str | None = ...,
        block_notification: Literal["enable", "disable"] | None = ...,
        custom_log_fields: str | list[str] | list[dict[str, Any]] | None = ...,
        replacemsg_override_group: str | None = ...,
        srcaddr_negate: Literal["enable", "disable"] | None = ...,
        srcaddr6_negate: Literal["enable", "disable"] | None = ...,
        dstaddr_negate: Literal["enable", "disable"] | None = ...,
        dstaddr6_negate: Literal["enable", "disable"] | None = ...,
        ztna_ems_tag_negate: Literal["enable", "disable"] | None = ...,
        service_negate: Literal["enable", "disable"] | None = ...,
        internet_service_negate: Literal["enable", "disable"] | None = ...,
        internet_service_src_negate: Literal["enable", "disable"] | None = ...,
        internet_service6_negate: Literal["enable", "disable"] | None = ...,
        internet_service6_src_negate: Literal["enable", "disable"] | None = ...,
        timeout_send_rst: Literal["enable", "disable"] | None = ...,
        captive_portal_exempt: Literal["enable", "disable"] | None = ...,
        decrypted_traffic_mirror: str | None = ...,
        dsri: Literal["enable", "disable"] | None = ...,
        radius_mac_auth_bypass: Literal["enable", "disable"] | None = ...,
        radius_ip_auth_bypass: Literal["enable", "disable"] | None = ...,
        delay_tcp_npu_session: Literal["enable", "disable"] | None = ...,
        vlan_filter: str | None = ...,
        sgt_check: Literal["enable", "disable"] | None = ...,
        sgt: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    def post(
        self,
        payload_dict: PolicyPayload | None = ...,
        policyid: int | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        srcintf: str | list[str] | list[dict[str, Any]] | None = ...,
        dstintf: str | list[str] | list[dict[str, Any]] | None = ...,
        action: Literal["accept", "deny", "ipsec"] | None = ...,
        nat64: Literal["enable", "disable"] | None = ...,
        nat46: Literal["enable", "disable"] | None = ...,
        ztna_status: Literal["enable", "disable"] | None = ...,
        ztna_device_ownership: Literal["enable", "disable"] | None = ...,
        srcaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        ztna_ems_tag: str | list[str] | list[dict[str, Any]] | None = ...,
        ztna_ems_tag_secondary: str | list[str] | list[dict[str, Any]] | None = ...,
        ztna_tags_match_logic: Literal["or", "and"] | None = ...,
        ztna_geo_tag: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service: Literal["enable", "disable"] | None = ...,
        internet_service_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        network_service_dynamic: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src: Literal["enable", "disable"] | None = ...,
        internet_service_src_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        network_service_src_dynamic: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        reputation_minimum: int | None = ...,
        reputation_direction: Literal["source", "destination"] | None = ...,
        src_vendor_mac: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6: Literal["enable", "disable"] | None = ...,
        internet_service6_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src: Literal["enable", "disable"] | None = ...,
        internet_service6_src_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        reputation_minimum6: int | None = ...,
        reputation_direction6: Literal["source", "destination"] | None = ...,
        rtp_nat: Literal["disable", "enable"] | None = ...,
        rtp_addr: str | list[str] | list[dict[str, Any]] | None = ...,
        send_deny_packet: Literal["disable", "enable"] | None = ...,
        firewall_session_dirty: Literal["check-all", "check-new"] | None = ...,
        schedule: str | None = ...,
        schedule_timeout: Literal["enable", "disable"] | None = ...,
        policy_expiry: Literal["enable", "disable"] | None = ...,
        policy_expiry_date: str | None = ...,
        policy_expiry_date_utc: str | None = ...,
        service: str | list[str] | list[dict[str, Any]] | None = ...,
        tos_mask: str | None = ...,
        tos: str | None = ...,
        tos_negate: Literal["enable", "disable"] | None = ...,
        anti_replay: Literal["enable", "disable"] | None = ...,
        tcp_session_without_syn: Literal["all", "data-only", "disable"] | None = ...,
        geoip_anycast: Literal["enable", "disable"] | None = ...,
        geoip_match: Literal["physical-location", "registered-location"] | None = ...,
        dynamic_shaping: Literal["enable", "disable"] | None = ...,
        passive_wan_health_measurement: Literal["enable", "disable"] | None = ...,
        app_monitor: Literal["enable", "disable"] | None = ...,
        utm_status: Literal["enable", "disable"] | None = ...,
        inspection_mode: Literal["proxy", "flow"] | None = ...,
        http_policy_redirect: Literal["enable", "disable", "legacy"] | None = ...,
        ssh_policy_redirect: Literal["enable", "disable"] | None = ...,
        ztna_policy_redirect: Literal["enable", "disable"] | None = ...,
        webproxy_profile: str | None = ...,
        profile_type: Literal["single", "group"] | None = ...,
        profile_group: str | None = ...,
        profile_protocol_options: str | None = ...,
        ssl_ssh_profile: str | None = ...,
        av_profile: str | None = ...,
        webfilter_profile: str | None = ...,
        dnsfilter_profile: str | None = ...,
        emailfilter_profile: str | None = ...,
        dlp_profile: str | None = ...,
        file_filter_profile: str | None = ...,
        ips_sensor: str | None = ...,
        application_list: str | None = ...,
        voip_profile: str | None = ...,
        ips_voip_filter: str | None = ...,
        sctp_filter_profile: str | None = ...,
        diameter_filter_profile: str | None = ...,
        virtual_patch_profile: str | None = ...,
        icap_profile: str | None = ...,
        videofilter_profile: str | None = ...,
        waf_profile: str | None = ...,
        ssh_filter_profile: str | None = ...,
        casb_profile: str | None = ...,
        logtraffic: Literal["all", "utm", "disable"] | None = ...,
        logtraffic_start: Literal["enable", "disable"] | None = ...,
        log_http_transaction: Literal["enable", "disable"] | None = ...,
        capture_packet: Literal["enable", "disable"] | None = ...,
        auto_asic_offload: Literal["enable", "disable"] | None = ...,
        wanopt: Literal["enable", "disable"] | None = ...,
        wanopt_detection: Literal["active", "passive", "off"] | None = ...,
        wanopt_passive_opt: Literal["default", "transparent", "non-transparent"] | None = ...,
        wanopt_profile: str | None = ...,
        wanopt_peer: str | None = ...,
        webcache: Literal["enable", "disable"] | None = ...,
        webcache_https: Literal["disable", "enable"] | None = ...,
        webproxy_forward_server: str | None = ...,
        traffic_shaper: str | None = ...,
        traffic_shaper_reverse: str | None = ...,
        per_ip_shaper: str | None = ...,
        nat: Literal["enable", "disable"] | None = ...,
        pcp_outbound: Literal["enable", "disable"] | None = ...,
        pcp_inbound: Literal["enable", "disable"] | None = ...,
        pcp_poolname: str | list[str] | list[dict[str, Any]] | None = ...,
        permit_any_host: Literal["enable", "disable"] | None = ...,
        permit_stun_host: Literal["enable", "disable"] | None = ...,
        fixedport: Literal["enable", "disable"] | None = ...,
        port_preserve: Literal["enable", "disable"] | None = ...,
        port_random: Literal["enable", "disable"] | None = ...,
        ippool: Literal["enable", "disable"] | None = ...,
        poolname: str | list[str] | list[dict[str, Any]] | None = ...,
        poolname6: str | list[str] | list[dict[str, Any]] | None = ...,
        session_ttl: str | None = ...,
        vlan_cos_fwd: int | None = ...,
        vlan_cos_rev: int | None = ...,
        inbound: Literal["enable", "disable"] | None = ...,
        outbound: Literal["enable", "disable"] | None = ...,
        natinbound: Literal["enable", "disable"] | None = ...,
        natoutbound: Literal["enable", "disable"] | None = ...,
        fec: Literal["enable", "disable"] | None = ...,
        wccp: Literal["enable", "disable"] | None = ...,
        ntlm: Literal["enable", "disable"] | None = ...,
        ntlm_guest: Literal["enable", "disable"] | None = ...,
        ntlm_enabled_browsers: str | list[str] | list[dict[str, Any]] | None = ...,
        fsso_agent_for_ntlm: str | None = ...,
        groups: str | list[str] | list[dict[str, Any]] | None = ...,
        users: str | list[str] | list[dict[str, Any]] | None = ...,
        fsso_groups: str | list[str] | list[dict[str, Any]] | None = ...,
        auth_path: Literal["enable", "disable"] | None = ...,
        disclaimer: Literal["enable", "disable"] | None = ...,
        email_collect: Literal["enable", "disable"] | None = ...,
        vpntunnel: str | None = ...,
        natip: str | None = ...,
        match_vip: Literal["enable", "disable"] | None = ...,
        match_vip_only: Literal["enable", "disable"] | None = ...,
        diffserv_copy: Literal["enable", "disable"] | None = ...,
        diffserv_forward: Literal["enable", "disable"] | None = ...,
        diffserv_reverse: Literal["enable", "disable"] | None = ...,
        diffservcode_forward: str | None = ...,
        diffservcode_rev: str | None = ...,
        tcp_mss_sender: int | None = ...,
        tcp_mss_receiver: int | None = ...,
        comments: str | None = ...,
        auth_cert: str | None = ...,
        auth_redirect_addr: str | None = ...,
        redirect_url: str | None = ...,
        identity_based_route: str | None = ...,
        block_notification: Literal["enable", "disable"] | None = ...,
        custom_log_fields: str | list[str] | list[dict[str, Any]] | None = ...,
        replacemsg_override_group: str | None = ...,
        srcaddr_negate: Literal["enable", "disable"] | None = ...,
        srcaddr6_negate: Literal["enable", "disable"] | None = ...,
        dstaddr_negate: Literal["enable", "disable"] | None = ...,
        dstaddr6_negate: Literal["enable", "disable"] | None = ...,
        ztna_ems_tag_negate: Literal["enable", "disable"] | None = ...,
        service_negate: Literal["enable", "disable"] | None = ...,
        internet_service_negate: Literal["enable", "disable"] | None = ...,
        internet_service_src_negate: Literal["enable", "disable"] | None = ...,
        internet_service6_negate: Literal["enable", "disable"] | None = ...,
        internet_service6_src_negate: Literal["enable", "disable"] | None = ...,
        timeout_send_rst: Literal["enable", "disable"] | None = ...,
        captive_portal_exempt: Literal["enable", "disable"] | None = ...,
        decrypted_traffic_mirror: str | None = ...,
        dsri: Literal["enable", "disable"] | None = ...,
        radius_mac_auth_bypass: Literal["enable", "disable"] | None = ...,
        radius_ip_auth_bypass: Literal["enable", "disable"] | None = ...,
        delay_tcp_npu_session: Literal["enable", "disable"] | None = ...,
        vlan_filter: str | None = ...,
        sgt_check: Literal["enable", "disable"] | None = ...,
        sgt: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: PolicyPayload | None = ...,
        policyid: int | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        srcintf: str | list[str] | list[dict[str, Any]] | None = ...,
        dstintf: str | list[str] | list[dict[str, Any]] | None = ...,
        action: Literal["accept", "deny", "ipsec"] | None = ...,
        nat64: Literal["enable", "disable"] | None = ...,
        nat46: Literal["enable", "disable"] | None = ...,
        ztna_status: Literal["enable", "disable"] | None = ...,
        ztna_device_ownership: Literal["enable", "disable"] | None = ...,
        srcaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        ztna_ems_tag: str | list[str] | list[dict[str, Any]] | None = ...,
        ztna_ems_tag_secondary: str | list[str] | list[dict[str, Any]] | None = ...,
        ztna_tags_match_logic: Literal["or", "and"] | None = ...,
        ztna_geo_tag: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service: Literal["enable", "disable"] | None = ...,
        internet_service_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        network_service_dynamic: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src: Literal["enable", "disable"] | None = ...,
        internet_service_src_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        network_service_src_dynamic: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        reputation_minimum: int | None = ...,
        reputation_direction: Literal["source", "destination"] | None = ...,
        src_vendor_mac: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6: Literal["enable", "disable"] | None = ...,
        internet_service6_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src: Literal["enable", "disable"] | None = ...,
        internet_service6_src_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        reputation_minimum6: int | None = ...,
        reputation_direction6: Literal["source", "destination"] | None = ...,
        rtp_nat: Literal["disable", "enable"] | None = ...,
        rtp_addr: str | list[str] | list[dict[str, Any]] | None = ...,
        send_deny_packet: Literal["disable", "enable"] | None = ...,
        firewall_session_dirty: Literal["check-all", "check-new"] | None = ...,
        schedule: str | None = ...,
        schedule_timeout: Literal["enable", "disable"] | None = ...,
        policy_expiry: Literal["enable", "disable"] | None = ...,
        policy_expiry_date: str | None = ...,
        policy_expiry_date_utc: str | None = ...,
        service: str | list[str] | list[dict[str, Any]] | None = ...,
        tos_mask: str | None = ...,
        tos: str | None = ...,
        tos_negate: Literal["enable", "disable"] | None = ...,
        anti_replay: Literal["enable", "disable"] | None = ...,
        tcp_session_without_syn: Literal["all", "data-only", "disable"] | None = ...,
        geoip_anycast: Literal["enable", "disable"] | None = ...,
        geoip_match: Literal["physical-location", "registered-location"] | None = ...,
        dynamic_shaping: Literal["enable", "disable"] | None = ...,
        passive_wan_health_measurement: Literal["enable", "disable"] | None = ...,
        app_monitor: Literal["enable", "disable"] | None = ...,
        utm_status: Literal["enable", "disable"] | None = ...,
        inspection_mode: Literal["proxy", "flow"] | None = ...,
        http_policy_redirect: Literal["enable", "disable", "legacy"] | None = ...,
        ssh_policy_redirect: Literal["enable", "disable"] | None = ...,
        ztna_policy_redirect: Literal["enable", "disable"] | None = ...,
        webproxy_profile: str | None = ...,
        profile_type: Literal["single", "group"] | None = ...,
        profile_group: str | None = ...,
        profile_protocol_options: str | None = ...,
        ssl_ssh_profile: str | None = ...,
        av_profile: str | None = ...,
        webfilter_profile: str | None = ...,
        dnsfilter_profile: str | None = ...,
        emailfilter_profile: str | None = ...,
        dlp_profile: str | None = ...,
        file_filter_profile: str | None = ...,
        ips_sensor: str | None = ...,
        application_list: str | None = ...,
        voip_profile: str | None = ...,
        ips_voip_filter: str | None = ...,
        sctp_filter_profile: str | None = ...,
        diameter_filter_profile: str | None = ...,
        virtual_patch_profile: str | None = ...,
        icap_profile: str | None = ...,
        videofilter_profile: str | None = ...,
        waf_profile: str | None = ...,
        ssh_filter_profile: str | None = ...,
        casb_profile: str | None = ...,
        logtraffic: Literal["all", "utm", "disable"] | None = ...,
        logtraffic_start: Literal["enable", "disable"] | None = ...,
        log_http_transaction: Literal["enable", "disable"] | None = ...,
        capture_packet: Literal["enable", "disable"] | None = ...,
        auto_asic_offload: Literal["enable", "disable"] | None = ...,
        wanopt: Literal["enable", "disable"] | None = ...,
        wanopt_detection: Literal["active", "passive", "off"] | None = ...,
        wanopt_passive_opt: Literal["default", "transparent", "non-transparent"] | None = ...,
        wanopt_profile: str | None = ...,
        wanopt_peer: str | None = ...,
        webcache: Literal["enable", "disable"] | None = ...,
        webcache_https: Literal["disable", "enable"] | None = ...,
        webproxy_forward_server: str | None = ...,
        traffic_shaper: str | None = ...,
        traffic_shaper_reverse: str | None = ...,
        per_ip_shaper: str | None = ...,
        nat: Literal["enable", "disable"] | None = ...,
        pcp_outbound: Literal["enable", "disable"] | None = ...,
        pcp_inbound: Literal["enable", "disable"] | None = ...,
        pcp_poolname: str | list[str] | list[dict[str, Any]] | None = ...,
        permit_any_host: Literal["enable", "disable"] | None = ...,
        permit_stun_host: Literal["enable", "disable"] | None = ...,
        fixedport: Literal["enable", "disable"] | None = ...,
        port_preserve: Literal["enable", "disable"] | None = ...,
        port_random: Literal["enable", "disable"] | None = ...,
        ippool: Literal["enable", "disable"] | None = ...,
        poolname: str | list[str] | list[dict[str, Any]] | None = ...,
        poolname6: str | list[str] | list[dict[str, Any]] | None = ...,
        session_ttl: str | None = ...,
        vlan_cos_fwd: int | None = ...,
        vlan_cos_rev: int | None = ...,
        inbound: Literal["enable", "disable"] | None = ...,
        outbound: Literal["enable", "disable"] | None = ...,
        natinbound: Literal["enable", "disable"] | None = ...,
        natoutbound: Literal["enable", "disable"] | None = ...,
        fec: Literal["enable", "disable"] | None = ...,
        wccp: Literal["enable", "disable"] | None = ...,
        ntlm: Literal["enable", "disable"] | None = ...,
        ntlm_guest: Literal["enable", "disable"] | None = ...,
        ntlm_enabled_browsers: str | list[str] | list[dict[str, Any]] | None = ...,
        fsso_agent_for_ntlm: str | None = ...,
        groups: str | list[str] | list[dict[str, Any]] | None = ...,
        users: str | list[str] | list[dict[str, Any]] | None = ...,
        fsso_groups: str | list[str] | list[dict[str, Any]] | None = ...,
        auth_path: Literal["enable", "disable"] | None = ...,
        disclaimer: Literal["enable", "disable"] | None = ...,
        email_collect: Literal["enable", "disable"] | None = ...,
        vpntunnel: str | None = ...,
        natip: str | None = ...,
        match_vip: Literal["enable", "disable"] | None = ...,
        match_vip_only: Literal["enable", "disable"] | None = ...,
        diffserv_copy: Literal["enable", "disable"] | None = ...,
        diffserv_forward: Literal["enable", "disable"] | None = ...,
        diffserv_reverse: Literal["enable", "disable"] | None = ...,
        diffservcode_forward: str | None = ...,
        diffservcode_rev: str | None = ...,
        tcp_mss_sender: int | None = ...,
        tcp_mss_receiver: int | None = ...,
        comments: str | None = ...,
        auth_cert: str | None = ...,
        auth_redirect_addr: str | None = ...,
        redirect_url: str | None = ...,
        identity_based_route: str | None = ...,
        block_notification: Literal["enable", "disable"] | None = ...,
        custom_log_fields: str | list[str] | list[dict[str, Any]] | None = ...,
        replacemsg_override_group: str | None = ...,
        srcaddr_negate: Literal["enable", "disable"] | None = ...,
        srcaddr6_negate: Literal["enable", "disable"] | None = ...,
        dstaddr_negate: Literal["enable", "disable"] | None = ...,
        dstaddr6_negate: Literal["enable", "disable"] | None = ...,
        ztna_ems_tag_negate: Literal["enable", "disable"] | None = ...,
        service_negate: Literal["enable", "disable"] | None = ...,
        internet_service_negate: Literal["enable", "disable"] | None = ...,
        internet_service_src_negate: Literal["enable", "disable"] | None = ...,
        internet_service6_negate: Literal["enable", "disable"] | None = ...,
        internet_service6_src_negate: Literal["enable", "disable"] | None = ...,
        timeout_send_rst: Literal["enable", "disable"] | None = ...,
        captive_portal_exempt: Literal["enable", "disable"] | None = ...,
        decrypted_traffic_mirror: str | None = ...,
        dsri: Literal["enable", "disable"] | None = ...,
        radius_mac_auth_bypass: Literal["enable", "disable"] | None = ...,
        radius_ip_auth_bypass: Literal["enable", "disable"] | None = ...,
        delay_tcp_npu_session: Literal["enable", "disable"] | None = ...,
        vlan_filter: str | None = ...,
        sgt_check: Literal["enable", "disable"] | None = ...,
        sgt: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> PolicyObject: ...
    
    @overload
    def put(
        self,
        payload_dict: PolicyPayload | None = ...,
        policyid: int | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        srcintf: str | list[str] | list[dict[str, Any]] | None = ...,
        dstintf: str | list[str] | list[dict[str, Any]] | None = ...,
        action: Literal["accept", "deny", "ipsec"] | None = ...,
        nat64: Literal["enable", "disable"] | None = ...,
        nat46: Literal["enable", "disable"] | None = ...,
        ztna_status: Literal["enable", "disable"] | None = ...,
        ztna_device_ownership: Literal["enable", "disable"] | None = ...,
        srcaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        ztna_ems_tag: str | list[str] | list[dict[str, Any]] | None = ...,
        ztna_ems_tag_secondary: str | list[str] | list[dict[str, Any]] | None = ...,
        ztna_tags_match_logic: Literal["or", "and"] | None = ...,
        ztna_geo_tag: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service: Literal["enable", "disable"] | None = ...,
        internet_service_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        network_service_dynamic: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src: Literal["enable", "disable"] | None = ...,
        internet_service_src_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        network_service_src_dynamic: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        reputation_minimum: int | None = ...,
        reputation_direction: Literal["source", "destination"] | None = ...,
        src_vendor_mac: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6: Literal["enable", "disable"] | None = ...,
        internet_service6_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src: Literal["enable", "disable"] | None = ...,
        internet_service6_src_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        reputation_minimum6: int | None = ...,
        reputation_direction6: Literal["source", "destination"] | None = ...,
        rtp_nat: Literal["disable", "enable"] | None = ...,
        rtp_addr: str | list[str] | list[dict[str, Any]] | None = ...,
        send_deny_packet: Literal["disable", "enable"] | None = ...,
        firewall_session_dirty: Literal["check-all", "check-new"] | None = ...,
        schedule: str | None = ...,
        schedule_timeout: Literal["enable", "disable"] | None = ...,
        policy_expiry: Literal["enable", "disable"] | None = ...,
        policy_expiry_date: str | None = ...,
        policy_expiry_date_utc: str | None = ...,
        service: str | list[str] | list[dict[str, Any]] | None = ...,
        tos_mask: str | None = ...,
        tos: str | None = ...,
        tos_negate: Literal["enable", "disable"] | None = ...,
        anti_replay: Literal["enable", "disable"] | None = ...,
        tcp_session_without_syn: Literal["all", "data-only", "disable"] | None = ...,
        geoip_anycast: Literal["enable", "disable"] | None = ...,
        geoip_match: Literal["physical-location", "registered-location"] | None = ...,
        dynamic_shaping: Literal["enable", "disable"] | None = ...,
        passive_wan_health_measurement: Literal["enable", "disable"] | None = ...,
        app_monitor: Literal["enable", "disable"] | None = ...,
        utm_status: Literal["enable", "disable"] | None = ...,
        inspection_mode: Literal["proxy", "flow"] | None = ...,
        http_policy_redirect: Literal["enable", "disable", "legacy"] | None = ...,
        ssh_policy_redirect: Literal["enable", "disable"] | None = ...,
        ztna_policy_redirect: Literal["enable", "disable"] | None = ...,
        webproxy_profile: str | None = ...,
        profile_type: Literal["single", "group"] | None = ...,
        profile_group: str | None = ...,
        profile_protocol_options: str | None = ...,
        ssl_ssh_profile: str | None = ...,
        av_profile: str | None = ...,
        webfilter_profile: str | None = ...,
        dnsfilter_profile: str | None = ...,
        emailfilter_profile: str | None = ...,
        dlp_profile: str | None = ...,
        file_filter_profile: str | None = ...,
        ips_sensor: str | None = ...,
        application_list: str | None = ...,
        voip_profile: str | None = ...,
        ips_voip_filter: str | None = ...,
        sctp_filter_profile: str | None = ...,
        diameter_filter_profile: str | None = ...,
        virtual_patch_profile: str | None = ...,
        icap_profile: str | None = ...,
        videofilter_profile: str | None = ...,
        waf_profile: str | None = ...,
        ssh_filter_profile: str | None = ...,
        casb_profile: str | None = ...,
        logtraffic: Literal["all", "utm", "disable"] | None = ...,
        logtraffic_start: Literal["enable", "disable"] | None = ...,
        log_http_transaction: Literal["enable", "disable"] | None = ...,
        capture_packet: Literal["enable", "disable"] | None = ...,
        auto_asic_offload: Literal["enable", "disable"] | None = ...,
        wanopt: Literal["enable", "disable"] | None = ...,
        wanopt_detection: Literal["active", "passive", "off"] | None = ...,
        wanopt_passive_opt: Literal["default", "transparent", "non-transparent"] | None = ...,
        wanopt_profile: str | None = ...,
        wanopt_peer: str | None = ...,
        webcache: Literal["enable", "disable"] | None = ...,
        webcache_https: Literal["disable", "enable"] | None = ...,
        webproxy_forward_server: str | None = ...,
        traffic_shaper: str | None = ...,
        traffic_shaper_reverse: str | None = ...,
        per_ip_shaper: str | None = ...,
        nat: Literal["enable", "disable"] | None = ...,
        pcp_outbound: Literal["enable", "disable"] | None = ...,
        pcp_inbound: Literal["enable", "disable"] | None = ...,
        pcp_poolname: str | list[str] | list[dict[str, Any]] | None = ...,
        permit_any_host: Literal["enable", "disable"] | None = ...,
        permit_stun_host: Literal["enable", "disable"] | None = ...,
        fixedport: Literal["enable", "disable"] | None = ...,
        port_preserve: Literal["enable", "disable"] | None = ...,
        port_random: Literal["enable", "disable"] | None = ...,
        ippool: Literal["enable", "disable"] | None = ...,
        poolname: str | list[str] | list[dict[str, Any]] | None = ...,
        poolname6: str | list[str] | list[dict[str, Any]] | None = ...,
        session_ttl: str | None = ...,
        vlan_cos_fwd: int | None = ...,
        vlan_cos_rev: int | None = ...,
        inbound: Literal["enable", "disable"] | None = ...,
        outbound: Literal["enable", "disable"] | None = ...,
        natinbound: Literal["enable", "disable"] | None = ...,
        natoutbound: Literal["enable", "disable"] | None = ...,
        fec: Literal["enable", "disable"] | None = ...,
        wccp: Literal["enable", "disable"] | None = ...,
        ntlm: Literal["enable", "disable"] | None = ...,
        ntlm_guest: Literal["enable", "disable"] | None = ...,
        ntlm_enabled_browsers: str | list[str] | list[dict[str, Any]] | None = ...,
        fsso_agent_for_ntlm: str | None = ...,
        groups: str | list[str] | list[dict[str, Any]] | None = ...,
        users: str | list[str] | list[dict[str, Any]] | None = ...,
        fsso_groups: str | list[str] | list[dict[str, Any]] | None = ...,
        auth_path: Literal["enable", "disable"] | None = ...,
        disclaimer: Literal["enable", "disable"] | None = ...,
        email_collect: Literal["enable", "disable"] | None = ...,
        vpntunnel: str | None = ...,
        natip: str | None = ...,
        match_vip: Literal["enable", "disable"] | None = ...,
        match_vip_only: Literal["enable", "disable"] | None = ...,
        diffserv_copy: Literal["enable", "disable"] | None = ...,
        diffserv_forward: Literal["enable", "disable"] | None = ...,
        diffserv_reverse: Literal["enable", "disable"] | None = ...,
        diffservcode_forward: str | None = ...,
        diffservcode_rev: str | None = ...,
        tcp_mss_sender: int | None = ...,
        tcp_mss_receiver: int | None = ...,
        comments: str | None = ...,
        auth_cert: str | None = ...,
        auth_redirect_addr: str | None = ...,
        redirect_url: str | None = ...,
        identity_based_route: str | None = ...,
        block_notification: Literal["enable", "disable"] | None = ...,
        custom_log_fields: str | list[str] | list[dict[str, Any]] | None = ...,
        replacemsg_override_group: str | None = ...,
        srcaddr_negate: Literal["enable", "disable"] | None = ...,
        srcaddr6_negate: Literal["enable", "disable"] | None = ...,
        dstaddr_negate: Literal["enable", "disable"] | None = ...,
        dstaddr6_negate: Literal["enable", "disable"] | None = ...,
        ztna_ems_tag_negate: Literal["enable", "disable"] | None = ...,
        service_negate: Literal["enable", "disable"] | None = ...,
        internet_service_negate: Literal["enable", "disable"] | None = ...,
        internet_service_src_negate: Literal["enable", "disable"] | None = ...,
        internet_service6_negate: Literal["enable", "disable"] | None = ...,
        internet_service6_src_negate: Literal["enable", "disable"] | None = ...,
        timeout_send_rst: Literal["enable", "disable"] | None = ...,
        captive_portal_exempt: Literal["enable", "disable"] | None = ...,
        decrypted_traffic_mirror: str | None = ...,
        dsri: Literal["enable", "disable"] | None = ...,
        radius_mac_auth_bypass: Literal["enable", "disable"] | None = ...,
        radius_ip_auth_bypass: Literal["enable", "disable"] | None = ...,
        delay_tcp_npu_session: Literal["enable", "disable"] | None = ...,
        vlan_filter: str | None = ...,
        sgt_check: Literal["enable", "disable"] | None = ...,
        sgt: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    # raw_json=True returns the full API envelope
    @overload
    def put(
        self,
        payload_dict: PolicyPayload | None = ...,
        policyid: int | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        srcintf: str | list[str] | list[dict[str, Any]] | None = ...,
        dstintf: str | list[str] | list[dict[str, Any]] | None = ...,
        action: Literal["accept", "deny", "ipsec"] | None = ...,
        nat64: Literal["enable", "disable"] | None = ...,
        nat46: Literal["enable", "disable"] | None = ...,
        ztna_status: Literal["enable", "disable"] | None = ...,
        ztna_device_ownership: Literal["enable", "disable"] | None = ...,
        srcaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        ztna_ems_tag: str | list[str] | list[dict[str, Any]] | None = ...,
        ztna_ems_tag_secondary: str | list[str] | list[dict[str, Any]] | None = ...,
        ztna_tags_match_logic: Literal["or", "and"] | None = ...,
        ztna_geo_tag: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service: Literal["enable", "disable"] | None = ...,
        internet_service_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        network_service_dynamic: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src: Literal["enable", "disable"] | None = ...,
        internet_service_src_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        network_service_src_dynamic: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        reputation_minimum: int | None = ...,
        reputation_direction: Literal["source", "destination"] | None = ...,
        src_vendor_mac: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6: Literal["enable", "disable"] | None = ...,
        internet_service6_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src: Literal["enable", "disable"] | None = ...,
        internet_service6_src_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        reputation_minimum6: int | None = ...,
        reputation_direction6: Literal["source", "destination"] | None = ...,
        rtp_nat: Literal["disable", "enable"] | None = ...,
        rtp_addr: str | list[str] | list[dict[str, Any]] | None = ...,
        send_deny_packet: Literal["disable", "enable"] | None = ...,
        firewall_session_dirty: Literal["check-all", "check-new"] | None = ...,
        schedule: str | None = ...,
        schedule_timeout: Literal["enable", "disable"] | None = ...,
        policy_expiry: Literal["enable", "disable"] | None = ...,
        policy_expiry_date: str | None = ...,
        policy_expiry_date_utc: str | None = ...,
        service: str | list[str] | list[dict[str, Any]] | None = ...,
        tos_mask: str | None = ...,
        tos: str | None = ...,
        tos_negate: Literal["enable", "disable"] | None = ...,
        anti_replay: Literal["enable", "disable"] | None = ...,
        tcp_session_without_syn: Literal["all", "data-only", "disable"] | None = ...,
        geoip_anycast: Literal["enable", "disable"] | None = ...,
        geoip_match: Literal["physical-location", "registered-location"] | None = ...,
        dynamic_shaping: Literal["enable", "disable"] | None = ...,
        passive_wan_health_measurement: Literal["enable", "disable"] | None = ...,
        app_monitor: Literal["enable", "disable"] | None = ...,
        utm_status: Literal["enable", "disable"] | None = ...,
        inspection_mode: Literal["proxy", "flow"] | None = ...,
        http_policy_redirect: Literal["enable", "disable", "legacy"] | None = ...,
        ssh_policy_redirect: Literal["enable", "disable"] | None = ...,
        ztna_policy_redirect: Literal["enable", "disable"] | None = ...,
        webproxy_profile: str | None = ...,
        profile_type: Literal["single", "group"] | None = ...,
        profile_group: str | None = ...,
        profile_protocol_options: str | None = ...,
        ssl_ssh_profile: str | None = ...,
        av_profile: str | None = ...,
        webfilter_profile: str | None = ...,
        dnsfilter_profile: str | None = ...,
        emailfilter_profile: str | None = ...,
        dlp_profile: str | None = ...,
        file_filter_profile: str | None = ...,
        ips_sensor: str | None = ...,
        application_list: str | None = ...,
        voip_profile: str | None = ...,
        ips_voip_filter: str | None = ...,
        sctp_filter_profile: str | None = ...,
        diameter_filter_profile: str | None = ...,
        virtual_patch_profile: str | None = ...,
        icap_profile: str | None = ...,
        videofilter_profile: str | None = ...,
        waf_profile: str | None = ...,
        ssh_filter_profile: str | None = ...,
        casb_profile: str | None = ...,
        logtraffic: Literal["all", "utm", "disable"] | None = ...,
        logtraffic_start: Literal["enable", "disable"] | None = ...,
        log_http_transaction: Literal["enable", "disable"] | None = ...,
        capture_packet: Literal["enable", "disable"] | None = ...,
        auto_asic_offload: Literal["enable", "disable"] | None = ...,
        wanopt: Literal["enable", "disable"] | None = ...,
        wanopt_detection: Literal["active", "passive", "off"] | None = ...,
        wanopt_passive_opt: Literal["default", "transparent", "non-transparent"] | None = ...,
        wanopt_profile: str | None = ...,
        wanopt_peer: str | None = ...,
        webcache: Literal["enable", "disable"] | None = ...,
        webcache_https: Literal["disable", "enable"] | None = ...,
        webproxy_forward_server: str | None = ...,
        traffic_shaper: str | None = ...,
        traffic_shaper_reverse: str | None = ...,
        per_ip_shaper: str | None = ...,
        nat: Literal["enable", "disable"] | None = ...,
        pcp_outbound: Literal["enable", "disable"] | None = ...,
        pcp_inbound: Literal["enable", "disable"] | None = ...,
        pcp_poolname: str | list[str] | list[dict[str, Any]] | None = ...,
        permit_any_host: Literal["enable", "disable"] | None = ...,
        permit_stun_host: Literal["enable", "disable"] | None = ...,
        fixedport: Literal["enable", "disable"] | None = ...,
        port_preserve: Literal["enable", "disable"] | None = ...,
        port_random: Literal["enable", "disable"] | None = ...,
        ippool: Literal["enable", "disable"] | None = ...,
        poolname: str | list[str] | list[dict[str, Any]] | None = ...,
        poolname6: str | list[str] | list[dict[str, Any]] | None = ...,
        session_ttl: str | None = ...,
        vlan_cos_fwd: int | None = ...,
        vlan_cos_rev: int | None = ...,
        inbound: Literal["enable", "disable"] | None = ...,
        outbound: Literal["enable", "disable"] | None = ...,
        natinbound: Literal["enable", "disable"] | None = ...,
        natoutbound: Literal["enable", "disable"] | None = ...,
        fec: Literal["enable", "disable"] | None = ...,
        wccp: Literal["enable", "disable"] | None = ...,
        ntlm: Literal["enable", "disable"] | None = ...,
        ntlm_guest: Literal["enable", "disable"] | None = ...,
        ntlm_enabled_browsers: str | list[str] | list[dict[str, Any]] | None = ...,
        fsso_agent_for_ntlm: str | None = ...,
        groups: str | list[str] | list[dict[str, Any]] | None = ...,
        users: str | list[str] | list[dict[str, Any]] | None = ...,
        fsso_groups: str | list[str] | list[dict[str, Any]] | None = ...,
        auth_path: Literal["enable", "disable"] | None = ...,
        disclaimer: Literal["enable", "disable"] | None = ...,
        email_collect: Literal["enable", "disable"] | None = ...,
        vpntunnel: str | None = ...,
        natip: str | None = ...,
        match_vip: Literal["enable", "disable"] | None = ...,
        match_vip_only: Literal["enable", "disable"] | None = ...,
        diffserv_copy: Literal["enable", "disable"] | None = ...,
        diffserv_forward: Literal["enable", "disable"] | None = ...,
        diffserv_reverse: Literal["enable", "disable"] | None = ...,
        diffservcode_forward: str | None = ...,
        diffservcode_rev: str | None = ...,
        tcp_mss_sender: int | None = ...,
        tcp_mss_receiver: int | None = ...,
        comments: str | None = ...,
        auth_cert: str | None = ...,
        auth_redirect_addr: str | None = ...,
        redirect_url: str | None = ...,
        identity_based_route: str | None = ...,
        block_notification: Literal["enable", "disable"] | None = ...,
        custom_log_fields: str | list[str] | list[dict[str, Any]] | None = ...,
        replacemsg_override_group: str | None = ...,
        srcaddr_negate: Literal["enable", "disable"] | None = ...,
        srcaddr6_negate: Literal["enable", "disable"] | None = ...,
        dstaddr_negate: Literal["enable", "disable"] | None = ...,
        dstaddr6_negate: Literal["enable", "disable"] | None = ...,
        ztna_ems_tag_negate: Literal["enable", "disable"] | None = ...,
        service_negate: Literal["enable", "disable"] | None = ...,
        internet_service_negate: Literal["enable", "disable"] | None = ...,
        internet_service_src_negate: Literal["enable", "disable"] | None = ...,
        internet_service6_negate: Literal["enable", "disable"] | None = ...,
        internet_service6_src_negate: Literal["enable", "disable"] | None = ...,
        timeout_send_rst: Literal["enable", "disable"] | None = ...,
        captive_portal_exempt: Literal["enable", "disable"] | None = ...,
        decrypted_traffic_mirror: str | None = ...,
        dsri: Literal["enable", "disable"] | None = ...,
        radius_mac_auth_bypass: Literal["enable", "disable"] | None = ...,
        radius_ip_auth_bypass: Literal["enable", "disable"] | None = ...,
        delay_tcp_npu_session: Literal["enable", "disable"] | None = ...,
        vlan_filter: str | None = ...,
        sgt_check: Literal["enable", "disable"] | None = ...,
        sgt: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> RawAPIResponse: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: PolicyPayload | None = ...,
        policyid: int | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        srcintf: str | list[str] | list[dict[str, Any]] | None = ...,
        dstintf: str | list[str] | list[dict[str, Any]] | None = ...,
        action: Literal["accept", "deny", "ipsec"] | None = ...,
        nat64: Literal["enable", "disable"] | None = ...,
        nat46: Literal["enable", "disable"] | None = ...,
        ztna_status: Literal["enable", "disable"] | None = ...,
        ztna_device_ownership: Literal["enable", "disable"] | None = ...,
        srcaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        ztna_ems_tag: str | list[str] | list[dict[str, Any]] | None = ...,
        ztna_ems_tag_secondary: str | list[str] | list[dict[str, Any]] | None = ...,
        ztna_tags_match_logic: Literal["or", "and"] | None = ...,
        ztna_geo_tag: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service: Literal["enable", "disable"] | None = ...,
        internet_service_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        network_service_dynamic: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src: Literal["enable", "disable"] | None = ...,
        internet_service_src_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        network_service_src_dynamic: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        reputation_minimum: int | None = ...,
        reputation_direction: Literal["source", "destination"] | None = ...,
        src_vendor_mac: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6: Literal["enable", "disable"] | None = ...,
        internet_service6_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src: Literal["enable", "disable"] | None = ...,
        internet_service6_src_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        reputation_minimum6: int | None = ...,
        reputation_direction6: Literal["source", "destination"] | None = ...,
        rtp_nat: Literal["disable", "enable"] | None = ...,
        rtp_addr: str | list[str] | list[dict[str, Any]] | None = ...,
        send_deny_packet: Literal["disable", "enable"] | None = ...,
        firewall_session_dirty: Literal["check-all", "check-new"] | None = ...,
        schedule: str | None = ...,
        schedule_timeout: Literal["enable", "disable"] | None = ...,
        policy_expiry: Literal["enable", "disable"] | None = ...,
        policy_expiry_date: str | None = ...,
        policy_expiry_date_utc: str | None = ...,
        service: str | list[str] | list[dict[str, Any]] | None = ...,
        tos_mask: str | None = ...,
        tos: str | None = ...,
        tos_negate: Literal["enable", "disable"] | None = ...,
        anti_replay: Literal["enable", "disable"] | None = ...,
        tcp_session_without_syn: Literal["all", "data-only", "disable"] | None = ...,
        geoip_anycast: Literal["enable", "disable"] | None = ...,
        geoip_match: Literal["physical-location", "registered-location"] | None = ...,
        dynamic_shaping: Literal["enable", "disable"] | None = ...,
        passive_wan_health_measurement: Literal["enable", "disable"] | None = ...,
        app_monitor: Literal["enable", "disable"] | None = ...,
        utm_status: Literal["enable", "disable"] | None = ...,
        inspection_mode: Literal["proxy", "flow"] | None = ...,
        http_policy_redirect: Literal["enable", "disable", "legacy"] | None = ...,
        ssh_policy_redirect: Literal["enable", "disable"] | None = ...,
        ztna_policy_redirect: Literal["enable", "disable"] | None = ...,
        webproxy_profile: str | None = ...,
        profile_type: Literal["single", "group"] | None = ...,
        profile_group: str | None = ...,
        profile_protocol_options: str | None = ...,
        ssl_ssh_profile: str | None = ...,
        av_profile: str | None = ...,
        webfilter_profile: str | None = ...,
        dnsfilter_profile: str | None = ...,
        emailfilter_profile: str | None = ...,
        dlp_profile: str | None = ...,
        file_filter_profile: str | None = ...,
        ips_sensor: str | None = ...,
        application_list: str | None = ...,
        voip_profile: str | None = ...,
        ips_voip_filter: str | None = ...,
        sctp_filter_profile: str | None = ...,
        diameter_filter_profile: str | None = ...,
        virtual_patch_profile: str | None = ...,
        icap_profile: str | None = ...,
        videofilter_profile: str | None = ...,
        waf_profile: str | None = ...,
        ssh_filter_profile: str | None = ...,
        casb_profile: str | None = ...,
        logtraffic: Literal["all", "utm", "disable"] | None = ...,
        logtraffic_start: Literal["enable", "disable"] | None = ...,
        log_http_transaction: Literal["enable", "disable"] | None = ...,
        capture_packet: Literal["enable", "disable"] | None = ...,
        auto_asic_offload: Literal["enable", "disable"] | None = ...,
        wanopt: Literal["enable", "disable"] | None = ...,
        wanopt_detection: Literal["active", "passive", "off"] | None = ...,
        wanopt_passive_opt: Literal["default", "transparent", "non-transparent"] | None = ...,
        wanopt_profile: str | None = ...,
        wanopt_peer: str | None = ...,
        webcache: Literal["enable", "disable"] | None = ...,
        webcache_https: Literal["disable", "enable"] | None = ...,
        webproxy_forward_server: str | None = ...,
        traffic_shaper: str | None = ...,
        traffic_shaper_reverse: str | None = ...,
        per_ip_shaper: str | None = ...,
        nat: Literal["enable", "disable"] | None = ...,
        pcp_outbound: Literal["enable", "disable"] | None = ...,
        pcp_inbound: Literal["enable", "disable"] | None = ...,
        pcp_poolname: str | list[str] | list[dict[str, Any]] | None = ...,
        permit_any_host: Literal["enable", "disable"] | None = ...,
        permit_stun_host: Literal["enable", "disable"] | None = ...,
        fixedport: Literal["enable", "disable"] | None = ...,
        port_preserve: Literal["enable", "disable"] | None = ...,
        port_random: Literal["enable", "disable"] | None = ...,
        ippool: Literal["enable", "disable"] | None = ...,
        poolname: str | list[str] | list[dict[str, Any]] | None = ...,
        poolname6: str | list[str] | list[dict[str, Any]] | None = ...,
        session_ttl: str | None = ...,
        vlan_cos_fwd: int | None = ...,
        vlan_cos_rev: int | None = ...,
        inbound: Literal["enable", "disable"] | None = ...,
        outbound: Literal["enable", "disable"] | None = ...,
        natinbound: Literal["enable", "disable"] | None = ...,
        natoutbound: Literal["enable", "disable"] | None = ...,
        fec: Literal["enable", "disable"] | None = ...,
        wccp: Literal["enable", "disable"] | None = ...,
        ntlm: Literal["enable", "disable"] | None = ...,
        ntlm_guest: Literal["enable", "disable"] | None = ...,
        ntlm_enabled_browsers: str | list[str] | list[dict[str, Any]] | None = ...,
        fsso_agent_for_ntlm: str | None = ...,
        groups: str | list[str] | list[dict[str, Any]] | None = ...,
        users: str | list[str] | list[dict[str, Any]] | None = ...,
        fsso_groups: str | list[str] | list[dict[str, Any]] | None = ...,
        auth_path: Literal["enable", "disable"] | None = ...,
        disclaimer: Literal["enable", "disable"] | None = ...,
        email_collect: Literal["enable", "disable"] | None = ...,
        vpntunnel: str | None = ...,
        natip: str | None = ...,
        match_vip: Literal["enable", "disable"] | None = ...,
        match_vip_only: Literal["enable", "disable"] | None = ...,
        diffserv_copy: Literal["enable", "disable"] | None = ...,
        diffserv_forward: Literal["enable", "disable"] | None = ...,
        diffserv_reverse: Literal["enable", "disable"] | None = ...,
        diffservcode_forward: str | None = ...,
        diffservcode_rev: str | None = ...,
        tcp_mss_sender: int | None = ...,
        tcp_mss_receiver: int | None = ...,
        comments: str | None = ...,
        auth_cert: str | None = ...,
        auth_redirect_addr: str | None = ...,
        redirect_url: str | None = ...,
        identity_based_route: str | None = ...,
        block_notification: Literal["enable", "disable"] | None = ...,
        custom_log_fields: str | list[str] | list[dict[str, Any]] | None = ...,
        replacemsg_override_group: str | None = ...,
        srcaddr_negate: Literal["enable", "disable"] | None = ...,
        srcaddr6_negate: Literal["enable", "disable"] | None = ...,
        dstaddr_negate: Literal["enable", "disable"] | None = ...,
        dstaddr6_negate: Literal["enable", "disable"] | None = ...,
        ztna_ems_tag_negate: Literal["enable", "disable"] | None = ...,
        service_negate: Literal["enable", "disable"] | None = ...,
        internet_service_negate: Literal["enable", "disable"] | None = ...,
        internet_service_src_negate: Literal["enable", "disable"] | None = ...,
        internet_service6_negate: Literal["enable", "disable"] | None = ...,
        internet_service6_src_negate: Literal["enable", "disable"] | None = ...,
        timeout_send_rst: Literal["enable", "disable"] | None = ...,
        captive_portal_exempt: Literal["enable", "disable"] | None = ...,
        decrypted_traffic_mirror: str | None = ...,
        dsri: Literal["enable", "disable"] | None = ...,
        radius_mac_auth_bypass: Literal["enable", "disable"] | None = ...,
        radius_ip_auth_bypass: Literal["enable", "disable"] | None = ...,
        delay_tcp_npu_session: Literal["enable", "disable"] | None = ...,
        vlan_filter: str | None = ...,
        sgt_check: Literal["enable", "disable"] | None = ...,
        sgt: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    def put(
        self,
        payload_dict: PolicyPayload | None = ...,
        policyid: int | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        srcintf: str | list[str] | list[dict[str, Any]] | None = ...,
        dstintf: str | list[str] | list[dict[str, Any]] | None = ...,
        action: Literal["accept", "deny", "ipsec"] | None = ...,
        nat64: Literal["enable", "disable"] | None = ...,
        nat46: Literal["enable", "disable"] | None = ...,
        ztna_status: Literal["enable", "disable"] | None = ...,
        ztna_device_ownership: Literal["enable", "disable"] | None = ...,
        srcaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        ztna_ems_tag: str | list[str] | list[dict[str, Any]] | None = ...,
        ztna_ems_tag_secondary: str | list[str] | list[dict[str, Any]] | None = ...,
        ztna_tags_match_logic: Literal["or", "and"] | None = ...,
        ztna_geo_tag: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service: Literal["enable", "disable"] | None = ...,
        internet_service_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        network_service_dynamic: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src: Literal["enable", "disable"] | None = ...,
        internet_service_src_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        network_service_src_dynamic: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        reputation_minimum: int | None = ...,
        reputation_direction: Literal["source", "destination"] | None = ...,
        src_vendor_mac: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6: Literal["enable", "disable"] | None = ...,
        internet_service6_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src: Literal["enable", "disable"] | None = ...,
        internet_service6_src_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        reputation_minimum6: int | None = ...,
        reputation_direction6: Literal["source", "destination"] | None = ...,
        rtp_nat: Literal["disable", "enable"] | None = ...,
        rtp_addr: str | list[str] | list[dict[str, Any]] | None = ...,
        send_deny_packet: Literal["disable", "enable"] | None = ...,
        firewall_session_dirty: Literal["check-all", "check-new"] | None = ...,
        schedule: str | None = ...,
        schedule_timeout: Literal["enable", "disable"] | None = ...,
        policy_expiry: Literal["enable", "disable"] | None = ...,
        policy_expiry_date: str | None = ...,
        policy_expiry_date_utc: str | None = ...,
        service: str | list[str] | list[dict[str, Any]] | None = ...,
        tos_mask: str | None = ...,
        tos: str | None = ...,
        tos_negate: Literal["enable", "disable"] | None = ...,
        anti_replay: Literal["enable", "disable"] | None = ...,
        tcp_session_without_syn: Literal["all", "data-only", "disable"] | None = ...,
        geoip_anycast: Literal["enable", "disable"] | None = ...,
        geoip_match: Literal["physical-location", "registered-location"] | None = ...,
        dynamic_shaping: Literal["enable", "disable"] | None = ...,
        passive_wan_health_measurement: Literal["enable", "disable"] | None = ...,
        app_monitor: Literal["enable", "disable"] | None = ...,
        utm_status: Literal["enable", "disable"] | None = ...,
        inspection_mode: Literal["proxy", "flow"] | None = ...,
        http_policy_redirect: Literal["enable", "disable", "legacy"] | None = ...,
        ssh_policy_redirect: Literal["enable", "disable"] | None = ...,
        ztna_policy_redirect: Literal["enable", "disable"] | None = ...,
        webproxy_profile: str | None = ...,
        profile_type: Literal["single", "group"] | None = ...,
        profile_group: str | None = ...,
        profile_protocol_options: str | None = ...,
        ssl_ssh_profile: str | None = ...,
        av_profile: str | None = ...,
        webfilter_profile: str | None = ...,
        dnsfilter_profile: str | None = ...,
        emailfilter_profile: str | None = ...,
        dlp_profile: str | None = ...,
        file_filter_profile: str | None = ...,
        ips_sensor: str | None = ...,
        application_list: str | None = ...,
        voip_profile: str | None = ...,
        ips_voip_filter: str | None = ...,
        sctp_filter_profile: str | None = ...,
        diameter_filter_profile: str | None = ...,
        virtual_patch_profile: str | None = ...,
        icap_profile: str | None = ...,
        videofilter_profile: str | None = ...,
        waf_profile: str | None = ...,
        ssh_filter_profile: str | None = ...,
        casb_profile: str | None = ...,
        logtraffic: Literal["all", "utm", "disable"] | None = ...,
        logtraffic_start: Literal["enable", "disable"] | None = ...,
        log_http_transaction: Literal["enable", "disable"] | None = ...,
        capture_packet: Literal["enable", "disable"] | None = ...,
        auto_asic_offload: Literal["enable", "disable"] | None = ...,
        wanopt: Literal["enable", "disable"] | None = ...,
        wanopt_detection: Literal["active", "passive", "off"] | None = ...,
        wanopt_passive_opt: Literal["default", "transparent", "non-transparent"] | None = ...,
        wanopt_profile: str | None = ...,
        wanopt_peer: str | None = ...,
        webcache: Literal["enable", "disable"] | None = ...,
        webcache_https: Literal["disable", "enable"] | None = ...,
        webproxy_forward_server: str | None = ...,
        traffic_shaper: str | None = ...,
        traffic_shaper_reverse: str | None = ...,
        per_ip_shaper: str | None = ...,
        nat: Literal["enable", "disable"] | None = ...,
        pcp_outbound: Literal["enable", "disable"] | None = ...,
        pcp_inbound: Literal["enable", "disable"] | None = ...,
        pcp_poolname: str | list[str] | list[dict[str, Any]] | None = ...,
        permit_any_host: Literal["enable", "disable"] | None = ...,
        permit_stun_host: Literal["enable", "disable"] | None = ...,
        fixedport: Literal["enable", "disable"] | None = ...,
        port_preserve: Literal["enable", "disable"] | None = ...,
        port_random: Literal["enable", "disable"] | None = ...,
        ippool: Literal["enable", "disable"] | None = ...,
        poolname: str | list[str] | list[dict[str, Any]] | None = ...,
        poolname6: str | list[str] | list[dict[str, Any]] | None = ...,
        session_ttl: str | None = ...,
        vlan_cos_fwd: int | None = ...,
        vlan_cos_rev: int | None = ...,
        inbound: Literal["enable", "disable"] | None = ...,
        outbound: Literal["enable", "disable"] | None = ...,
        natinbound: Literal["enable", "disable"] | None = ...,
        natoutbound: Literal["enable", "disable"] | None = ...,
        fec: Literal["enable", "disable"] | None = ...,
        wccp: Literal["enable", "disable"] | None = ...,
        ntlm: Literal["enable", "disable"] | None = ...,
        ntlm_guest: Literal["enable", "disable"] | None = ...,
        ntlm_enabled_browsers: str | list[str] | list[dict[str, Any]] | None = ...,
        fsso_agent_for_ntlm: str | None = ...,
        groups: str | list[str] | list[dict[str, Any]] | None = ...,
        users: str | list[str] | list[dict[str, Any]] | None = ...,
        fsso_groups: str | list[str] | list[dict[str, Any]] | None = ...,
        auth_path: Literal["enable", "disable"] | None = ...,
        disclaimer: Literal["enable", "disable"] | None = ...,
        email_collect: Literal["enable", "disable"] | None = ...,
        vpntunnel: str | None = ...,
        natip: str | None = ...,
        match_vip: Literal["enable", "disable"] | None = ...,
        match_vip_only: Literal["enable", "disable"] | None = ...,
        diffserv_copy: Literal["enable", "disable"] | None = ...,
        diffserv_forward: Literal["enable", "disable"] | None = ...,
        diffserv_reverse: Literal["enable", "disable"] | None = ...,
        diffservcode_forward: str | None = ...,
        diffservcode_rev: str | None = ...,
        tcp_mss_sender: int | None = ...,
        tcp_mss_receiver: int | None = ...,
        comments: str | None = ...,
        auth_cert: str | None = ...,
        auth_redirect_addr: str | None = ...,
        redirect_url: str | None = ...,
        identity_based_route: str | None = ...,
        block_notification: Literal["enable", "disable"] | None = ...,
        custom_log_fields: str | list[str] | list[dict[str, Any]] | None = ...,
        replacemsg_override_group: str | None = ...,
        srcaddr_negate: Literal["enable", "disable"] | None = ...,
        srcaddr6_negate: Literal["enable", "disable"] | None = ...,
        dstaddr_negate: Literal["enable", "disable"] | None = ...,
        dstaddr6_negate: Literal["enable", "disable"] | None = ...,
        ztna_ems_tag_negate: Literal["enable", "disable"] | None = ...,
        service_negate: Literal["enable", "disable"] | None = ...,
        internet_service_negate: Literal["enable", "disable"] | None = ...,
        internet_service_src_negate: Literal["enable", "disable"] | None = ...,
        internet_service6_negate: Literal["enable", "disable"] | None = ...,
        internet_service6_src_negate: Literal["enable", "disable"] | None = ...,
        timeout_send_rst: Literal["enable", "disable"] | None = ...,
        captive_portal_exempt: Literal["enable", "disable"] | None = ...,
        decrypted_traffic_mirror: str | None = ...,
        dsri: Literal["enable", "disable"] | None = ...,
        radius_mac_auth_bypass: Literal["enable", "disable"] | None = ...,
        radius_ip_auth_bypass: Literal["enable", "disable"] | None = ...,
        delay_tcp_npu_session: Literal["enable", "disable"] | None = ...,
        vlan_filter: str | None = ...,
        sgt_check: Literal["enable", "disable"] | None = ...,
        sgt: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        policyid: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> PolicyObject: ...
    
    @overload
    def delete(
        self,
        policyid: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    # raw_json=True returns the full API envelope
    @overload
    def delete(
        self,
        policyid: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> RawAPIResponse: ...
    
    # Default overload
    @overload
    def delete(
        self,
        policyid: int | None = ...,
        vdom: str | bool | None = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    def delete(
        self,
        policyid: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    def exists(
        self,
        policyid: int,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: PolicyPayload | None = ...,
        policyid: int | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        srcintf: str | list[str] | list[dict[str, Any]] | None = ...,
        dstintf: str | list[str] | list[dict[str, Any]] | None = ...,
        action: Literal["accept", "deny", "ipsec"] | None = ...,
        nat64: Literal["enable", "disable"] | None = ...,
        nat46: Literal["enable", "disable"] | None = ...,
        ztna_status: Literal["enable", "disable"] | None = ...,
        ztna_device_ownership: Literal["enable", "disable"] | None = ...,
        srcaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        ztna_ems_tag: str | list[str] | list[dict[str, Any]] | None = ...,
        ztna_ems_tag_secondary: str | list[str] | list[dict[str, Any]] | None = ...,
        ztna_tags_match_logic: Literal["or", "and"] | None = ...,
        ztna_geo_tag: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service: Literal["enable", "disable"] | None = ...,
        internet_service_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        network_service_dynamic: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src: Literal["enable", "disable"] | None = ...,
        internet_service_src_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        network_service_src_dynamic: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        reputation_minimum: int | None = ...,
        reputation_direction: Literal["source", "destination"] | None = ...,
        src_vendor_mac: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6: Literal["enable", "disable"] | None = ...,
        internet_service6_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src: Literal["enable", "disable"] | None = ...,
        internet_service6_src_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        reputation_minimum6: int | None = ...,
        reputation_direction6: Literal["source", "destination"] | None = ...,
        rtp_nat: Literal["disable", "enable"] | None = ...,
        rtp_addr: str | list[str] | list[dict[str, Any]] | None = ...,
        send_deny_packet: Literal["disable", "enable"] | None = ...,
        firewall_session_dirty: Literal["check-all", "check-new"] | None = ...,
        schedule: str | None = ...,
        schedule_timeout: Literal["enable", "disable"] | None = ...,
        policy_expiry: Literal["enable", "disable"] | None = ...,
        policy_expiry_date: str | None = ...,
        policy_expiry_date_utc: str | None = ...,
        service: str | list[str] | list[dict[str, Any]] | None = ...,
        tos_mask: str | None = ...,
        tos: str | None = ...,
        tos_negate: Literal["enable", "disable"] | None = ...,
        anti_replay: Literal["enable", "disable"] | None = ...,
        tcp_session_without_syn: Literal["all", "data-only", "disable"] | None = ...,
        geoip_anycast: Literal["enable", "disable"] | None = ...,
        geoip_match: Literal["physical-location", "registered-location"] | None = ...,
        dynamic_shaping: Literal["enable", "disable"] | None = ...,
        passive_wan_health_measurement: Literal["enable", "disable"] | None = ...,
        app_monitor: Literal["enable", "disable"] | None = ...,
        utm_status: Literal["enable", "disable"] | None = ...,
        inspection_mode: Literal["proxy", "flow"] | None = ...,
        http_policy_redirect: Literal["enable", "disable", "legacy"] | None = ...,
        ssh_policy_redirect: Literal["enable", "disable"] | None = ...,
        ztna_policy_redirect: Literal["enable", "disable"] | None = ...,
        webproxy_profile: str | None = ...,
        profile_type: Literal["single", "group"] | None = ...,
        profile_group: str | None = ...,
        profile_protocol_options: str | None = ...,
        ssl_ssh_profile: str | None = ...,
        av_profile: str | None = ...,
        webfilter_profile: str | None = ...,
        dnsfilter_profile: str | None = ...,
        emailfilter_profile: str | None = ...,
        dlp_profile: str | None = ...,
        file_filter_profile: str | None = ...,
        ips_sensor: str | None = ...,
        application_list: str | None = ...,
        voip_profile: str | None = ...,
        ips_voip_filter: str | None = ...,
        sctp_filter_profile: str | None = ...,
        diameter_filter_profile: str | None = ...,
        virtual_patch_profile: str | None = ...,
        icap_profile: str | None = ...,
        videofilter_profile: str | None = ...,
        waf_profile: str | None = ...,
        ssh_filter_profile: str | None = ...,
        casb_profile: str | None = ...,
        logtraffic: Literal["all", "utm", "disable"] | None = ...,
        logtraffic_start: Literal["enable", "disable"] | None = ...,
        log_http_transaction: Literal["enable", "disable"] | None = ...,
        capture_packet: Literal["enable", "disable"] | None = ...,
        auto_asic_offload: Literal["enable", "disable"] | None = ...,
        wanopt: Literal["enable", "disable"] | None = ...,
        wanopt_detection: Literal["active", "passive", "off"] | None = ...,
        wanopt_passive_opt: Literal["default", "transparent", "non-transparent"] | None = ...,
        wanopt_profile: str | None = ...,
        wanopt_peer: str | None = ...,
        webcache: Literal["enable", "disable"] | None = ...,
        webcache_https: Literal["disable", "enable"] | None = ...,
        webproxy_forward_server: str | None = ...,
        traffic_shaper: str | None = ...,
        traffic_shaper_reverse: str | None = ...,
        per_ip_shaper: str | None = ...,
        nat: Literal["enable", "disable"] | None = ...,
        pcp_outbound: Literal["enable", "disable"] | None = ...,
        pcp_inbound: Literal["enable", "disable"] | None = ...,
        pcp_poolname: str | list[str] | list[dict[str, Any]] | None = ...,
        permit_any_host: Literal["enable", "disable"] | None = ...,
        permit_stun_host: Literal["enable", "disable"] | None = ...,
        fixedport: Literal["enable", "disable"] | None = ...,
        port_preserve: Literal["enable", "disable"] | None = ...,
        port_random: Literal["enable", "disable"] | None = ...,
        ippool: Literal["enable", "disable"] | None = ...,
        poolname: str | list[str] | list[dict[str, Any]] | None = ...,
        poolname6: str | list[str] | list[dict[str, Any]] | None = ...,
        session_ttl: str | None = ...,
        vlan_cos_fwd: int | None = ...,
        vlan_cos_rev: int | None = ...,
        inbound: Literal["enable", "disable"] | None = ...,
        outbound: Literal["enable", "disable"] | None = ...,
        natinbound: Literal["enable", "disable"] | None = ...,
        natoutbound: Literal["enable", "disable"] | None = ...,
        fec: Literal["enable", "disable"] | None = ...,
        wccp: Literal["enable", "disable"] | None = ...,
        ntlm: Literal["enable", "disable"] | None = ...,
        ntlm_guest: Literal["enable", "disable"] | None = ...,
        ntlm_enabled_browsers: str | list[str] | list[dict[str, Any]] | None = ...,
        fsso_agent_for_ntlm: str | None = ...,
        groups: str | list[str] | list[dict[str, Any]] | None = ...,
        users: str | list[str] | list[dict[str, Any]] | None = ...,
        fsso_groups: str | list[str] | list[dict[str, Any]] | None = ...,
        auth_path: Literal["enable", "disable"] | None = ...,
        disclaimer: Literal["enable", "disable"] | None = ...,
        email_collect: Literal["enable", "disable"] | None = ...,
        vpntunnel: str | None = ...,
        natip: str | None = ...,
        match_vip: Literal["enable", "disable"] | None = ...,
        match_vip_only: Literal["enable", "disable"] | None = ...,
        diffserv_copy: Literal["enable", "disable"] | None = ...,
        diffserv_forward: Literal["enable", "disable"] | None = ...,
        diffserv_reverse: Literal["enable", "disable"] | None = ...,
        diffservcode_forward: str | None = ...,
        diffservcode_rev: str | None = ...,
        tcp_mss_sender: int | None = ...,
        tcp_mss_receiver: int | None = ...,
        comments: str | None = ...,
        auth_cert: str | None = ...,
        auth_redirect_addr: str | None = ...,
        redirect_url: str | None = ...,
        identity_based_route: str | None = ...,
        block_notification: Literal["enable", "disable"] | None = ...,
        custom_log_fields: str | list[str] | list[dict[str, Any]] | None = ...,
        replacemsg_override_group: str | None = ...,
        srcaddr_negate: Literal["enable", "disable"] | None = ...,
        srcaddr6_negate: Literal["enable", "disable"] | None = ...,
        dstaddr_negate: Literal["enable", "disable"] | None = ...,
        dstaddr6_negate: Literal["enable", "disable"] | None = ...,
        ztna_ems_tag_negate: Literal["enable", "disable"] | None = ...,
        service_negate: Literal["enable", "disable"] | None = ...,
        internet_service_negate: Literal["enable", "disable"] | None = ...,
        internet_service_src_negate: Literal["enable", "disable"] | None = ...,
        internet_service6_negate: Literal["enable", "disable"] | None = ...,
        internet_service6_src_negate: Literal["enable", "disable"] | None = ...,
        timeout_send_rst: Literal["enable", "disable"] | None = ...,
        captive_portal_exempt: Literal["enable", "disable"] | None = ...,
        decrypted_traffic_mirror: str | None = ...,
        dsri: Literal["enable", "disable"] | None = ...,
        radius_mac_auth_bypass: Literal["enable", "disable"] | None = ...,
        radius_ip_auth_bypass: Literal["enable", "disable"] | None = ...,
        delay_tcp_npu_session: Literal["enable", "disable"] | None = ...,
        vlan_filter: str | None = ...,
        sgt_check: Literal["enable", "disable"] | None = ...,
        sgt: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    # Helper methods
    @staticmethod
    def help(field_name: str | None = ...) -> str: ...
    
    @staticmethod
    def fields(detailed: bool = ...) -> Union[list[str], list[dict[str, Any]]]: ...
    
    @staticmethod
    def field_info(field_name: str) -> FortiObject: ...
    
    @staticmethod
    def validate_field(name: str, value: Any) -> bool: ...
    
    @staticmethod
    def required_fields() -> list[str]: ...
    
    @staticmethod
    def defaults() -> FortiObject: ...
    
    @staticmethod
    def schema() -> FortiObject: ...


# ================================================================


__all__ = [
    "Policy",
    "PolicyPayload",
    "PolicyResponse",
    "PolicyObject",
]