"""
Validation helpers for system settings endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_VDOM_TYPE = ["traffic", "lan-extension", "admin"]
VALID_BODY_OPMODE = ["nat", "transparent"]
VALID_BODY_NGFW_MODE = ["profile-based", "policy-based"]
VALID_BODY_HTTP_EXTERNAL_DEST = ["fortiweb", "forticache"]
VALID_BODY_FIREWALL_SESSION_DIRTY = [
    "check-all",
    "check-new",
    "check-policy-option",
]
VALID_BODY_BFD = ["enable", "disable"]
VALID_BODY_BFD_DONT_ENFORCE_SRC_PORT = ["enable", "disable"]
VALID_BODY_UTF8_SPAM_TAGGING = ["enable", "disable"]
VALID_BODY_WCCP_CACHE_ENGINE = ["enable", "disable"]
VALID_BODY_VPN_STATS_LOG = ["ipsec", "pptp", "l2tp"]
VALID_BODY_V4_ECMP_MODE = [
    "source-ip-based",
    "weight-based",
    "usage-based",
    "source-dest-ip-based",
]
VALID_BODY_FW_SESSION_HAIRPIN = ["enable", "disable"]
VALID_BODY_PRP_TRAILER_ACTION = ["enable", "disable"]
VALID_BODY_SNAT_HAIRPIN_TRAFFIC = ["enable", "disable"]
VALID_BODY_DHCP_PROXY = ["enable", "disable"]
VALID_BODY_DHCP_PROXY_INTERFACE_SELECT_METHOD = ["auto", "sdwan", "specify"]
VALID_BODY_CENTRAL_NAT = ["enable", "disable"]
VALID_BODY_LLDP_RECEPTION = ["enable", "disable", "global"]
VALID_BODY_LLDP_TRANSMISSION = ["enable", "disable", "global"]
VALID_BODY_LINK_DOWN_ACCESS = ["enable", "disable"]
VALID_BODY_NAT46_GENERATE_IPV6_FRAGMENT_HEADER = ["enable", "disable"]
VALID_BODY_NAT46_FORCE_IPV4_PACKET_FORWARDING = ["enable", "disable"]
VALID_BODY_NAT64_FORCE_IPV6_PACKET_FORWARDING = ["enable", "disable"]
VALID_BODY_DETECT_UNKNOWN_ESP = ["enable", "disable"]
VALID_BODY_INTREE_SES_BEST_ROUTE = ["force", "disable"]
VALID_BODY_AUXILIARY_SESSION = ["enable", "disable"]
VALID_BODY_ASYMROUTE = ["enable", "disable"]
VALID_BODY_ASYMROUTE_ICMP = ["enable", "disable"]
VALID_BODY_TCP_SESSION_WITHOUT_SYN = ["enable", "disable"]
VALID_BODY_SES_DENIED_TRAFFIC = ["enable", "disable"]
VALID_BODY_SES_DENIED_MULTICAST_TRAFFIC = ["enable", "disable"]
VALID_BODY_STRICT_SRC_CHECK = ["enable", "disable"]
VALID_BODY_ALLOW_LINKDOWN_PATH = ["enable", "disable"]
VALID_BODY_ASYMROUTE6 = ["enable", "disable"]
VALID_BODY_ASYMROUTE6_ICMP = ["enable", "disable"]
VALID_BODY_SCTP_SESSION_WITHOUT_INIT = ["enable", "disable"]
VALID_BODY_SIP_EXPECTATION = ["enable", "disable"]
VALID_BODY_SIP_NAT_TRACE = ["enable", "disable"]
VALID_BODY_H323_DIRECT_MODEL = ["disable", "enable"]
VALID_BODY_STATUS = ["enable", "disable"]
VALID_BODY_MULTICAST_FORWARD = ["enable", "disable"]
VALID_BODY_MULTICAST_TTL_NOTCHANGE = ["enable", "disable"]
VALID_BODY_MULTICAST_SKIP_POLICY = ["enable", "disable"]
VALID_BODY_ALLOW_SUBNET_OVERLAP = ["enable", "disable"]
VALID_BODY_DENY_TCP_WITH_ICMP = ["enable", "disable"]
VALID_BODY_EMAIL_PORTAL_CHECK_DNS = ["disable", "enable"]
VALID_BODY_DEFAULT_VOIP_ALG_MODE = ["proxy-based", "kernel-helper-based"]
VALID_BODY_GUI_ICAP = ["enable", "disable"]
VALID_BODY_GUI_IMPLICIT_POLICY = ["enable", "disable"]
VALID_BODY_GUI_DNS_DATABASE = ["enable", "disable"]
VALID_BODY_GUI_LOAD_BALANCE = ["enable", "disable"]
VALID_BODY_GUI_MULTICAST_POLICY = ["enable", "disable"]
VALID_BODY_GUI_DOS_POLICY = ["enable", "disable"]
VALID_BODY_GUI_OBJECT_COLORS = ["enable", "disable"]
VALID_BODY_GUI_ROUTE_TAG_ADDRESS_CREATION = ["enable", "disable"]
VALID_BODY_GUI_VOIP_PROFILE = ["enable", "disable"]
VALID_BODY_GUI_AP_PROFILE = ["enable", "disable"]
VALID_BODY_GUI_SECURITY_PROFILE_GROUP = ["enable", "disable"]
VALID_BODY_GUI_LOCAL_IN_POLICY = ["enable", "disable"]
VALID_BODY_GUI_EXPLICIT_PROXY = ["enable", "disable"]
VALID_BODY_GUI_DYNAMIC_ROUTING = ["enable", "disable"]
VALID_BODY_GUI_POLICY_BASED_IPSEC = ["enable", "disable"]
VALID_BODY_GUI_THREAT_WEIGHT = ["enable", "disable"]
VALID_BODY_GUI_SPAMFILTER = ["enable", "disable"]
VALID_BODY_GUI_FILE_FILTER = ["enable", "disable"]
VALID_BODY_GUI_APPLICATION_CONTROL = ["enable", "disable"]
VALID_BODY_GUI_IPS = ["enable", "disable"]
VALID_BODY_GUI_DHCP_ADVANCED = ["enable", "disable"]
VALID_BODY_GUI_VPN = ["enable", "disable"]
VALID_BODY_GUI_WIRELESS_CONTROLLER = ["enable", "disable"]
VALID_BODY_GUI_ADVANCED_WIRELESS_FEATURES = ["enable", "disable"]
VALID_BODY_GUI_SWITCH_CONTROLLER = ["enable", "disable"]
VALID_BODY_GUI_FORTIAP_SPLIT_TUNNELING = ["enable", "disable"]
VALID_BODY_GUI_WEBFILTER_ADVANCED = ["enable", "disable"]
VALID_BODY_GUI_TRAFFIC_SHAPING = ["enable", "disable"]
VALID_BODY_GUI_WAN_LOAD_BALANCING = ["enable", "disable"]
VALID_BODY_GUI_ANTIVIRUS = ["enable", "disable"]
VALID_BODY_GUI_WEBFILTER = ["enable", "disable"]
VALID_BODY_GUI_VIDEOFILTER = ["enable", "disable"]
VALID_BODY_GUI_DNSFILTER = ["enable", "disable"]
VALID_BODY_GUI_WAF_PROFILE = ["enable", "disable"]
VALID_BODY_GUI_DLP_PROFILE = ["enable", "disable"]
VALID_BODY_GUI_DLP_ADVANCED = ["enable", "disable"]
VALID_BODY_GUI_VIRTUAL_PATCH_PROFILE = ["enable", "disable"]
VALID_BODY_GUI_CASB = ["enable", "disable"]
VALID_BODY_GUI_FORTIEXTENDER_CONTROLLER = ["enable", "disable"]
VALID_BODY_GUI_ADVANCED_POLICY = ["enable", "disable"]
VALID_BODY_GUI_ALLOW_UNNAMED_POLICY = ["enable", "disable"]
VALID_BODY_GUI_EMAIL_COLLECTION = ["enable", "disable"]
VALID_BODY_GUI_MULTIPLE_INTERFACE_POLICY = ["enable", "disable"]
VALID_BODY_GUI_POLICY_DISCLAIMER = ["enable", "disable"]
VALID_BODY_GUI_ZTNA = ["enable", "disable"]
VALID_BODY_GUI_OT = ["enable", "disable"]
VALID_BODY_GUI_DYNAMIC_DEVICE_OS_ID = ["enable", "disable"]
VALID_BODY_IKE_SESSION_RESUME = ["enable", "disable"]
VALID_BODY_IKE_QUICK_CRASH_DETECT = ["enable", "disable"]
VALID_BODY_IKE_DN_FORMAT = ["with-space", "no-space"]
VALID_BODY_IKE_POLICY_ROUTE = ["enable", "disable"]
VALID_BODY_IKE_DETAILED_EVENT_LOGS = ["disable", "enable"]
VALID_BODY_BLOCK_LAND_ATTACK = ["disable", "enable"]
VALID_BODY_DEFAULT_APP_PORT_AS_SERVICE = ["enable", "disable"]
VALID_BODY_FQDN_SESSION_CHECK = ["enable", "disable"]
VALID_BODY_EXT_RESOURCE_SESSION_CHECK = ["enable", "disable"]
VALID_BODY_DYN_ADDR_SESSION_CHECK = ["enable", "disable"]
VALID_BODY_GUI_ENFORCE_CHANGE_SUMMARY = ["disable", "require", "optional"]
VALID_BODY_INTERNET_SERVICE_DATABASE_CACHE = ["disable", "enable"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_settings_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate GET request parameters.

    Args:
        attr: Attribute filter (optional)
        filters: Additional filter parameters
        **params: Other query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Example:
        >>> # List all objects
        >>> is_valid, error = {func_name}()
    """
    # Validate query parameters if present
    if "action" in params:
        value = params.get("action")
        if value and value not in VALID_QUERY_ACTION:
            return (
                False,
                f"Invalid query parameter 'action'='{value}'. Must be one of: {', '.join(VALID_QUERY_ACTION)}",
            )

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_settings_put(
    payload: dict[str, Any] | None = None,
) -> tuple[bool, str | None]:
    """
    Validate PUT request payload for updating {endpoint_name}.

    Args:
        payload: The payload to validate

    Returns:
        Tuple of (is_valid, error_message)
    """
    # If no payload provided, nothing to validate
    if not payload:
        return (True, None)

    # Validate comments if present
    if "comments" in payload:
        value = payload.get("comments")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "comments cannot exceed 255 characters")

    # Validate vdom-type if present
    if "vdom-type" in payload:
        value = payload.get("vdom-type")
        if value and value not in VALID_BODY_VDOM_TYPE:
            return (
                False,
                f"Invalid vdom-type '{value}'. Must be one of: {', '.join(VALID_BODY_VDOM_TYPE)}",
            )

    # Validate lan-extension-controller-addr if present
    if "lan-extension-controller-addr" in payload:
        value = payload.get("lan-extension-controller-addr")
        if value and isinstance(value, str) and len(value) > 255:
            return (
                False,
                "lan-extension-controller-addr cannot exceed 255 characters",
            )

    # Validate lan-extension-controller-port if present
    if "lan-extension-controller-port" in payload:
        value = payload.get("lan-extension-controller-port")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1024 or int_val > 65535:
                    return (
                        False,
                        "lan-extension-controller-port must be between 1024 and 65535",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"lan-extension-controller-port must be numeric, got: {value}",
                )

    # Validate opmode if present
    if "opmode" in payload:
        value = payload.get("opmode")
        if value and value not in VALID_BODY_OPMODE:
            return (
                False,
                f"Invalid opmode '{value}'. Must be one of: {', '.join(VALID_BODY_OPMODE)}",
            )

    # Validate ngfw-mode if present
    if "ngfw-mode" in payload:
        value = payload.get("ngfw-mode")
        if value and value not in VALID_BODY_NGFW_MODE:
            return (
                False,
                f"Invalid ngfw-mode '{value}'. Must be one of: {', '.join(VALID_BODY_NGFW_MODE)}",
            )

    # Validate http-external-dest if present
    if "http-external-dest" in payload:
        value = payload.get("http-external-dest")
        if value and value not in VALID_BODY_HTTP_EXTERNAL_DEST:
            return (
                False,
                f"Invalid http-external-dest '{value}'. Must be one of: {', '.join(VALID_BODY_HTTP_EXTERNAL_DEST)}",
            )

    # Validate firewall-session-dirty if present
    if "firewall-session-dirty" in payload:
        value = payload.get("firewall-session-dirty")
        if value and value not in VALID_BODY_FIREWALL_SESSION_DIRTY:
            return (
                False,
                f"Invalid firewall-session-dirty '{value}'. Must be one of: {', '.join(VALID_BODY_FIREWALL_SESSION_DIRTY)}",
            )

    # Validate device if present
    if "device" in payload:
        value = payload.get("device")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "device cannot exceed 35 characters")

    # Validate bfd if present
    if "bfd" in payload:
        value = payload.get("bfd")
        if value and value not in VALID_BODY_BFD:
            return (
                False,
                f"Invalid bfd '{value}'. Must be one of: {', '.join(VALID_BODY_BFD)}",
            )

    # Validate bfd-desired-min-tx if present
    if "bfd-desired-min-tx" in payload:
        value = payload.get("bfd-desired-min-tx")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 100000:
                    return (
                        False,
                        "bfd-desired-min-tx must be between 1 and 100000",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"bfd-desired-min-tx must be numeric, got: {value}",
                )

    # Validate bfd-required-min-rx if present
    if "bfd-required-min-rx" in payload:
        value = payload.get("bfd-required-min-rx")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 100000:
                    return (
                        False,
                        "bfd-required-min-rx must be between 1 and 100000",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"bfd-required-min-rx must be numeric, got: {value}",
                )

    # Validate bfd-detect-mult if present
    if "bfd-detect-mult" in payload:
        value = payload.get("bfd-detect-mult")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 50:
                    return (False, "bfd-detect-mult must be between 1 and 50")
            except (ValueError, TypeError):
                return (
                    False,
                    f"bfd-detect-mult must be numeric, got: {value}",
                )

    # Validate bfd-dont-enforce-src-port if present
    if "bfd-dont-enforce-src-port" in payload:
        value = payload.get("bfd-dont-enforce-src-port")
        if value and value not in VALID_BODY_BFD_DONT_ENFORCE_SRC_PORT:
            return (
                False,
                f"Invalid bfd-dont-enforce-src-port '{value}'. Must be one of: {', '.join(VALID_BODY_BFD_DONT_ENFORCE_SRC_PORT)}",
            )

    # Validate utf8-spam-tagging if present
    if "utf8-spam-tagging" in payload:
        value = payload.get("utf8-spam-tagging")
        if value and value not in VALID_BODY_UTF8_SPAM_TAGGING:
            return (
                False,
                f"Invalid utf8-spam-tagging '{value}'. Must be one of: {', '.join(VALID_BODY_UTF8_SPAM_TAGGING)}",
            )

    # Validate wccp-cache-engine if present
    if "wccp-cache-engine" in payload:
        value = payload.get("wccp-cache-engine")
        if value and value not in VALID_BODY_WCCP_CACHE_ENGINE:
            return (
                False,
                f"Invalid wccp-cache-engine '{value}'. Must be one of: {', '.join(VALID_BODY_WCCP_CACHE_ENGINE)}",
            )

    # Validate vpn-stats-log if present
    if "vpn-stats-log" in payload:
        value = payload.get("vpn-stats-log")
        if value and value not in VALID_BODY_VPN_STATS_LOG:
            return (
                False,
                f"Invalid vpn-stats-log '{value}'. Must be one of: {', '.join(VALID_BODY_VPN_STATS_LOG)}",
            )

    # Validate vpn-stats-period if present
    if "vpn-stats-period" in payload:
        value = payload.get("vpn-stats-period")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "vpn-stats-period must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"vpn-stats-period must be numeric, got: {value}",
                )

    # Validate v4-ecmp-mode if present
    if "v4-ecmp-mode" in payload:
        value = payload.get("v4-ecmp-mode")
        if value and value not in VALID_BODY_V4_ECMP_MODE:
            return (
                False,
                f"Invalid v4-ecmp-mode '{value}'. Must be one of: {', '.join(VALID_BODY_V4_ECMP_MODE)}",
            )

    # Validate mac-ttl if present
    if "mac-ttl" in payload:
        value = payload.get("mac-ttl")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 300 or int_val > 8640000:
                    return (False, "mac-ttl must be between 300 and 8640000")
            except (ValueError, TypeError):
                return (False, f"mac-ttl must be numeric, got: {value}")

    # Validate fw-session-hairpin if present
    if "fw-session-hairpin" in payload:
        value = payload.get("fw-session-hairpin")
        if value and value not in VALID_BODY_FW_SESSION_HAIRPIN:
            return (
                False,
                f"Invalid fw-session-hairpin '{value}'. Must be one of: {', '.join(VALID_BODY_FW_SESSION_HAIRPIN)}",
            )

    # Validate prp-trailer-action if present
    if "prp-trailer-action" in payload:
        value = payload.get("prp-trailer-action")
        if value and value not in VALID_BODY_PRP_TRAILER_ACTION:
            return (
                False,
                f"Invalid prp-trailer-action '{value}'. Must be one of: {', '.join(VALID_BODY_PRP_TRAILER_ACTION)}",
            )

    # Validate snat-hairpin-traffic if present
    if "snat-hairpin-traffic" in payload:
        value = payload.get("snat-hairpin-traffic")
        if value and value not in VALID_BODY_SNAT_HAIRPIN_TRAFFIC:
            return (
                False,
                f"Invalid snat-hairpin-traffic '{value}'. Must be one of: {', '.join(VALID_BODY_SNAT_HAIRPIN_TRAFFIC)}",
            )

    # Validate dhcp-proxy if present
    if "dhcp-proxy" in payload:
        value = payload.get("dhcp-proxy")
        if value and value not in VALID_BODY_DHCP_PROXY:
            return (
                False,
                f"Invalid dhcp-proxy '{value}'. Must be one of: {', '.join(VALID_BODY_DHCP_PROXY)}",
            )

    # Validate dhcp-proxy-interface-select-method if present
    if "dhcp-proxy-interface-select-method" in payload:
        value = payload.get("dhcp-proxy-interface-select-method")
        if (
            value
            and value not in VALID_BODY_DHCP_PROXY_INTERFACE_SELECT_METHOD
        ):
            return (
                False,
                f"Invalid dhcp-proxy-interface-select-method '{value}'. Must be one of: {', '.join(VALID_BODY_DHCP_PROXY_INTERFACE_SELECT_METHOD)}",
            )

    # Validate dhcp-proxy-interface if present
    if "dhcp-proxy-interface" in payload:
        value = payload.get("dhcp-proxy-interface")
        if value and isinstance(value, str) and len(value) > 15:
            return (False, "dhcp-proxy-interface cannot exceed 15 characters")

    # Validate dhcp-proxy-vrf-select if present
    if "dhcp-proxy-vrf-select" in payload:
        value = payload.get("dhcp-proxy-vrf-select")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 511:
                    return (
                        False,
                        "dhcp-proxy-vrf-select must be between 0 and 511",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"dhcp-proxy-vrf-select must be numeric, got: {value}",
                )

    # Validate central-nat if present
    if "central-nat" in payload:
        value = payload.get("central-nat")
        if value and value not in VALID_BODY_CENTRAL_NAT:
            return (
                False,
                f"Invalid central-nat '{value}'. Must be one of: {', '.join(VALID_BODY_CENTRAL_NAT)}",
            )

    # Validate lldp-reception if present
    if "lldp-reception" in payload:
        value = payload.get("lldp-reception")
        if value and value not in VALID_BODY_LLDP_RECEPTION:
            return (
                False,
                f"Invalid lldp-reception '{value}'. Must be one of: {', '.join(VALID_BODY_LLDP_RECEPTION)}",
            )

    # Validate lldp-transmission if present
    if "lldp-transmission" in payload:
        value = payload.get("lldp-transmission")
        if value and value not in VALID_BODY_LLDP_TRANSMISSION:
            return (
                False,
                f"Invalid lldp-transmission '{value}'. Must be one of: {', '.join(VALID_BODY_LLDP_TRANSMISSION)}",
            )

    # Validate link-down-access if present
    if "link-down-access" in payload:
        value = payload.get("link-down-access")
        if value and value not in VALID_BODY_LINK_DOWN_ACCESS:
            return (
                False,
                f"Invalid link-down-access '{value}'. Must be one of: {', '.join(VALID_BODY_LINK_DOWN_ACCESS)}",
            )

    # Validate nat46-generate-ipv6-fragment-header if present
    if "nat46-generate-ipv6-fragment-header" in payload:
        value = payload.get("nat46-generate-ipv6-fragment-header")
        if (
            value
            and value not in VALID_BODY_NAT46_GENERATE_IPV6_FRAGMENT_HEADER
        ):
            return (
                False,
                f"Invalid nat46-generate-ipv6-fragment-header '{value}'. Must be one of: {', '.join(VALID_BODY_NAT46_GENERATE_IPV6_FRAGMENT_HEADER)}",
            )

    # Validate nat46-force-ipv4-packet-forwarding if present
    if "nat46-force-ipv4-packet-forwarding" in payload:
        value = payload.get("nat46-force-ipv4-packet-forwarding")
        if (
            value
            and value not in VALID_BODY_NAT46_FORCE_IPV4_PACKET_FORWARDING
        ):
            return (
                False,
                f"Invalid nat46-force-ipv4-packet-forwarding '{value}'. Must be one of: {', '.join(VALID_BODY_NAT46_FORCE_IPV4_PACKET_FORWARDING)}",
            )

    # Validate nat64-force-ipv6-packet-forwarding if present
    if "nat64-force-ipv6-packet-forwarding" in payload:
        value = payload.get("nat64-force-ipv6-packet-forwarding")
        if (
            value
            and value not in VALID_BODY_NAT64_FORCE_IPV6_PACKET_FORWARDING
        ):
            return (
                False,
                f"Invalid nat64-force-ipv6-packet-forwarding '{value}'. Must be one of: {', '.join(VALID_BODY_NAT64_FORCE_IPV6_PACKET_FORWARDING)}",
            )

    # Validate detect-unknown-esp if present
    if "detect-unknown-esp" in payload:
        value = payload.get("detect-unknown-esp")
        if value and value not in VALID_BODY_DETECT_UNKNOWN_ESP:
            return (
                False,
                f"Invalid detect-unknown-esp '{value}'. Must be one of: {', '.join(VALID_BODY_DETECT_UNKNOWN_ESP)}",
            )

    # Validate intree-ses-best-route if present
    if "intree-ses-best-route" in payload:
        value = payload.get("intree-ses-best-route")
        if value and value not in VALID_BODY_INTREE_SES_BEST_ROUTE:
            return (
                False,
                f"Invalid intree-ses-best-route '{value}'. Must be one of: {', '.join(VALID_BODY_INTREE_SES_BEST_ROUTE)}",
            )

    # Validate auxiliary-session if present
    if "auxiliary-session" in payload:
        value = payload.get("auxiliary-session")
        if value and value not in VALID_BODY_AUXILIARY_SESSION:
            return (
                False,
                f"Invalid auxiliary-session '{value}'. Must be one of: {', '.join(VALID_BODY_AUXILIARY_SESSION)}",
            )

    # Validate asymroute if present
    if "asymroute" in payload:
        value = payload.get("asymroute")
        if value and value not in VALID_BODY_ASYMROUTE:
            return (
                False,
                f"Invalid asymroute '{value}'. Must be one of: {', '.join(VALID_BODY_ASYMROUTE)}",
            )

    # Validate asymroute-icmp if present
    if "asymroute-icmp" in payload:
        value = payload.get("asymroute-icmp")
        if value and value not in VALID_BODY_ASYMROUTE_ICMP:
            return (
                False,
                f"Invalid asymroute-icmp '{value}'. Must be one of: {', '.join(VALID_BODY_ASYMROUTE_ICMP)}",
            )

    # Validate tcp-session-without-syn if present
    if "tcp-session-without-syn" in payload:
        value = payload.get("tcp-session-without-syn")
        if value and value not in VALID_BODY_TCP_SESSION_WITHOUT_SYN:
            return (
                False,
                f"Invalid tcp-session-without-syn '{value}'. Must be one of: {', '.join(VALID_BODY_TCP_SESSION_WITHOUT_SYN)}",
            )

    # Validate ses-denied-traffic if present
    if "ses-denied-traffic" in payload:
        value = payload.get("ses-denied-traffic")
        if value and value not in VALID_BODY_SES_DENIED_TRAFFIC:
            return (
                False,
                f"Invalid ses-denied-traffic '{value}'. Must be one of: {', '.join(VALID_BODY_SES_DENIED_TRAFFIC)}",
            )

    # Validate ses-denied-multicast-traffic if present
    if "ses-denied-multicast-traffic" in payload:
        value = payload.get("ses-denied-multicast-traffic")
        if value and value not in VALID_BODY_SES_DENIED_MULTICAST_TRAFFIC:
            return (
                False,
                f"Invalid ses-denied-multicast-traffic '{value}'. Must be one of: {', '.join(VALID_BODY_SES_DENIED_MULTICAST_TRAFFIC)}",
            )

    # Validate strict-src-check if present
    if "strict-src-check" in payload:
        value = payload.get("strict-src-check")
        if value and value not in VALID_BODY_STRICT_SRC_CHECK:
            return (
                False,
                f"Invalid strict-src-check '{value}'. Must be one of: {', '.join(VALID_BODY_STRICT_SRC_CHECK)}",
            )

    # Validate allow-linkdown-path if present
    if "allow-linkdown-path" in payload:
        value = payload.get("allow-linkdown-path")
        if value and value not in VALID_BODY_ALLOW_LINKDOWN_PATH:
            return (
                False,
                f"Invalid allow-linkdown-path '{value}'. Must be one of: {', '.join(VALID_BODY_ALLOW_LINKDOWN_PATH)}",
            )

    # Validate asymroute6 if present
    if "asymroute6" in payload:
        value = payload.get("asymroute6")
        if value and value not in VALID_BODY_ASYMROUTE6:
            return (
                False,
                f"Invalid asymroute6 '{value}'. Must be one of: {', '.join(VALID_BODY_ASYMROUTE6)}",
            )

    # Validate asymroute6-icmp if present
    if "asymroute6-icmp" in payload:
        value = payload.get("asymroute6-icmp")
        if value and value not in VALID_BODY_ASYMROUTE6_ICMP:
            return (
                False,
                f"Invalid asymroute6-icmp '{value}'. Must be one of: {', '.join(VALID_BODY_ASYMROUTE6_ICMP)}",
            )

    # Validate sctp-session-without-init if present
    if "sctp-session-without-init" in payload:
        value = payload.get("sctp-session-without-init")
        if value and value not in VALID_BODY_SCTP_SESSION_WITHOUT_INIT:
            return (
                False,
                f"Invalid sctp-session-without-init '{value}'. Must be one of: {', '.join(VALID_BODY_SCTP_SESSION_WITHOUT_INIT)}",
            )

    # Validate sip-expectation if present
    if "sip-expectation" in payload:
        value = payload.get("sip-expectation")
        if value and value not in VALID_BODY_SIP_EXPECTATION:
            return (
                False,
                f"Invalid sip-expectation '{value}'. Must be one of: {', '.join(VALID_BODY_SIP_EXPECTATION)}",
            )

    # Validate sip-nat-trace if present
    if "sip-nat-trace" in payload:
        value = payload.get("sip-nat-trace")
        if value and value not in VALID_BODY_SIP_NAT_TRACE:
            return (
                False,
                f"Invalid sip-nat-trace '{value}'. Must be one of: {', '.join(VALID_BODY_SIP_NAT_TRACE)}",
            )

    # Validate h323-direct-model if present
    if "h323-direct-model" in payload:
        value = payload.get("h323-direct-model")
        if value and value not in VALID_BODY_H323_DIRECT_MODEL:
            return (
                False,
                f"Invalid h323-direct-model '{value}'. Must be one of: {', '.join(VALID_BODY_H323_DIRECT_MODEL)}",
            )

    # Validate status if present
    if "status" in payload:
        value = payload.get("status")
        if value and value not in VALID_BODY_STATUS:
            return (
                False,
                f"Invalid status '{value}'. Must be one of: {', '.join(VALID_BODY_STATUS)}",
            )

    # Validate sip-tcp-port if present
    if "sip-tcp-port" in payload:
        value = payload.get("sip-tcp-port")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 65535:
                    return (False, "sip-tcp-port must be between 1 and 65535")
            except (ValueError, TypeError):
                return (False, f"sip-tcp-port must be numeric, got: {value}")

    # Validate sip-udp-port if present
    if "sip-udp-port" in payload:
        value = payload.get("sip-udp-port")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 65535:
                    return (False, "sip-udp-port must be between 1 and 65535")
            except (ValueError, TypeError):
                return (False, f"sip-udp-port must be numeric, got: {value}")

    # Validate sip-ssl-port if present
    if "sip-ssl-port" in payload:
        value = payload.get("sip-ssl-port")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 65535:
                    return (False, "sip-ssl-port must be between 0 and 65535")
            except (ValueError, TypeError):
                return (False, f"sip-ssl-port must be numeric, got: {value}")

    # Validate sccp-port if present
    if "sccp-port" in payload:
        value = payload.get("sccp-port")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 65535:
                    return (False, "sccp-port must be between 0 and 65535")
            except (ValueError, TypeError):
                return (False, f"sccp-port must be numeric, got: {value}")

    # Validate multicast-forward if present
    if "multicast-forward" in payload:
        value = payload.get("multicast-forward")
        if value and value not in VALID_BODY_MULTICAST_FORWARD:
            return (
                False,
                f"Invalid multicast-forward '{value}'. Must be one of: {', '.join(VALID_BODY_MULTICAST_FORWARD)}",
            )

    # Validate multicast-ttl-notchange if present
    if "multicast-ttl-notchange" in payload:
        value = payload.get("multicast-ttl-notchange")
        if value and value not in VALID_BODY_MULTICAST_TTL_NOTCHANGE:
            return (
                False,
                f"Invalid multicast-ttl-notchange '{value}'. Must be one of: {', '.join(VALID_BODY_MULTICAST_TTL_NOTCHANGE)}",
            )

    # Validate multicast-skip-policy if present
    if "multicast-skip-policy" in payload:
        value = payload.get("multicast-skip-policy")
        if value and value not in VALID_BODY_MULTICAST_SKIP_POLICY:
            return (
                False,
                f"Invalid multicast-skip-policy '{value}'. Must be one of: {', '.join(VALID_BODY_MULTICAST_SKIP_POLICY)}",
            )

    # Validate allow-subnet-overlap if present
    if "allow-subnet-overlap" in payload:
        value = payload.get("allow-subnet-overlap")
        if value and value not in VALID_BODY_ALLOW_SUBNET_OVERLAP:
            return (
                False,
                f"Invalid allow-subnet-overlap '{value}'. Must be one of: {', '.join(VALID_BODY_ALLOW_SUBNET_OVERLAP)}",
            )

    # Validate deny-tcp-with-icmp if present
    if "deny-tcp-with-icmp" in payload:
        value = payload.get("deny-tcp-with-icmp")
        if value and value not in VALID_BODY_DENY_TCP_WITH_ICMP:
            return (
                False,
                f"Invalid deny-tcp-with-icmp '{value}'. Must be one of: {', '.join(VALID_BODY_DENY_TCP_WITH_ICMP)}",
            )

    # Validate ecmp-max-paths if present
    if "ecmp-max-paths" in payload:
        value = payload.get("ecmp-max-paths")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 255:
                    return (False, "ecmp-max-paths must be between 1 and 255")
            except (ValueError, TypeError):
                return (False, f"ecmp-max-paths must be numeric, got: {value}")

    # Validate discovered-device-timeout if present
    if "discovered-device-timeout" in payload:
        value = payload.get("discovered-device-timeout")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 365:
                    return (
                        False,
                        "discovered-device-timeout must be between 1 and 365",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"discovered-device-timeout must be numeric, got: {value}",
                )

    # Validate email-portal-check-dns if present
    if "email-portal-check-dns" in payload:
        value = payload.get("email-portal-check-dns")
        if value and value not in VALID_BODY_EMAIL_PORTAL_CHECK_DNS:
            return (
                False,
                f"Invalid email-portal-check-dns '{value}'. Must be one of: {', '.join(VALID_BODY_EMAIL_PORTAL_CHECK_DNS)}",
            )

    # Validate default-voip-alg-mode if present
    if "default-voip-alg-mode" in payload:
        value = payload.get("default-voip-alg-mode")
        if value and value not in VALID_BODY_DEFAULT_VOIP_ALG_MODE:
            return (
                False,
                f"Invalid default-voip-alg-mode '{value}'. Must be one of: {', '.join(VALID_BODY_DEFAULT_VOIP_ALG_MODE)}",
            )

    # Validate gui-icap if present
    if "gui-icap" in payload:
        value = payload.get("gui-icap")
        if value and value not in VALID_BODY_GUI_ICAP:
            return (
                False,
                f"Invalid gui-icap '{value}'. Must be one of: {', '.join(VALID_BODY_GUI_ICAP)}",
            )

    # Validate gui-implicit-policy if present
    if "gui-implicit-policy" in payload:
        value = payload.get("gui-implicit-policy")
        if value and value not in VALID_BODY_GUI_IMPLICIT_POLICY:
            return (
                False,
                f"Invalid gui-implicit-policy '{value}'. Must be one of: {', '.join(VALID_BODY_GUI_IMPLICIT_POLICY)}",
            )

    # Validate gui-dns-database if present
    if "gui-dns-database" in payload:
        value = payload.get("gui-dns-database")
        if value and value not in VALID_BODY_GUI_DNS_DATABASE:
            return (
                False,
                f"Invalid gui-dns-database '{value}'. Must be one of: {', '.join(VALID_BODY_GUI_DNS_DATABASE)}",
            )

    # Validate gui-load-balance if present
    if "gui-load-balance" in payload:
        value = payload.get("gui-load-balance")
        if value and value not in VALID_BODY_GUI_LOAD_BALANCE:
            return (
                False,
                f"Invalid gui-load-balance '{value}'. Must be one of: {', '.join(VALID_BODY_GUI_LOAD_BALANCE)}",
            )

    # Validate gui-multicast-policy if present
    if "gui-multicast-policy" in payload:
        value = payload.get("gui-multicast-policy")
        if value and value not in VALID_BODY_GUI_MULTICAST_POLICY:
            return (
                False,
                f"Invalid gui-multicast-policy '{value}'. Must be one of: {', '.join(VALID_BODY_GUI_MULTICAST_POLICY)}",
            )

    # Validate gui-dos-policy if present
    if "gui-dos-policy" in payload:
        value = payload.get("gui-dos-policy")
        if value and value not in VALID_BODY_GUI_DOS_POLICY:
            return (
                False,
                f"Invalid gui-dos-policy '{value}'. Must be one of: {', '.join(VALID_BODY_GUI_DOS_POLICY)}",
            )

    # Validate gui-object-colors if present
    if "gui-object-colors" in payload:
        value = payload.get("gui-object-colors")
        if value and value not in VALID_BODY_GUI_OBJECT_COLORS:
            return (
                False,
                f"Invalid gui-object-colors '{value}'. Must be one of: {', '.join(VALID_BODY_GUI_OBJECT_COLORS)}",
            )

    # Validate gui-route-tag-address-creation if present
    if "gui-route-tag-address-creation" in payload:
        value = payload.get("gui-route-tag-address-creation")
        if value and value not in VALID_BODY_GUI_ROUTE_TAG_ADDRESS_CREATION:
            return (
                False,
                f"Invalid gui-route-tag-address-creation '{value}'. Must be one of: {', '.join(VALID_BODY_GUI_ROUTE_TAG_ADDRESS_CREATION)}",
            )

    # Validate gui-voip-profile if present
    if "gui-voip-profile" in payload:
        value = payload.get("gui-voip-profile")
        if value and value not in VALID_BODY_GUI_VOIP_PROFILE:
            return (
                False,
                f"Invalid gui-voip-profile '{value}'. Must be one of: {', '.join(VALID_BODY_GUI_VOIP_PROFILE)}",
            )

    # Validate gui-ap-profile if present
    if "gui-ap-profile" in payload:
        value = payload.get("gui-ap-profile")
        if value and value not in VALID_BODY_GUI_AP_PROFILE:
            return (
                False,
                f"Invalid gui-ap-profile '{value}'. Must be one of: {', '.join(VALID_BODY_GUI_AP_PROFILE)}",
            )

    # Validate gui-security-profile-group if present
    if "gui-security-profile-group" in payload:
        value = payload.get("gui-security-profile-group")
        if value and value not in VALID_BODY_GUI_SECURITY_PROFILE_GROUP:
            return (
                False,
                f"Invalid gui-security-profile-group '{value}'. Must be one of: {', '.join(VALID_BODY_GUI_SECURITY_PROFILE_GROUP)}",
            )

    # Validate gui-local-in-policy if present
    if "gui-local-in-policy" in payload:
        value = payload.get("gui-local-in-policy")
        if value and value not in VALID_BODY_GUI_LOCAL_IN_POLICY:
            return (
                False,
                f"Invalid gui-local-in-policy '{value}'. Must be one of: {', '.join(VALID_BODY_GUI_LOCAL_IN_POLICY)}",
            )

    # Validate gui-explicit-proxy if present
    if "gui-explicit-proxy" in payload:
        value = payload.get("gui-explicit-proxy")
        if value and value not in VALID_BODY_GUI_EXPLICIT_PROXY:
            return (
                False,
                f"Invalid gui-explicit-proxy '{value}'. Must be one of: {', '.join(VALID_BODY_GUI_EXPLICIT_PROXY)}",
            )

    # Validate gui-dynamic-routing if present
    if "gui-dynamic-routing" in payload:
        value = payload.get("gui-dynamic-routing")
        if value and value not in VALID_BODY_GUI_DYNAMIC_ROUTING:
            return (
                False,
                f"Invalid gui-dynamic-routing '{value}'. Must be one of: {', '.join(VALID_BODY_GUI_DYNAMIC_ROUTING)}",
            )

    # Validate gui-policy-based-ipsec if present
    if "gui-policy-based-ipsec" in payload:
        value = payload.get("gui-policy-based-ipsec")
        if value and value not in VALID_BODY_GUI_POLICY_BASED_IPSEC:
            return (
                False,
                f"Invalid gui-policy-based-ipsec '{value}'. Must be one of: {', '.join(VALID_BODY_GUI_POLICY_BASED_IPSEC)}",
            )

    # Validate gui-threat-weight if present
    if "gui-threat-weight" in payload:
        value = payload.get("gui-threat-weight")
        if value and value not in VALID_BODY_GUI_THREAT_WEIGHT:
            return (
                False,
                f"Invalid gui-threat-weight '{value}'. Must be one of: {', '.join(VALID_BODY_GUI_THREAT_WEIGHT)}",
            )

    # Validate gui-spamfilter if present
    if "gui-spamfilter" in payload:
        value = payload.get("gui-spamfilter")
        if value and value not in VALID_BODY_GUI_SPAMFILTER:
            return (
                False,
                f"Invalid gui-spamfilter '{value}'. Must be one of: {', '.join(VALID_BODY_GUI_SPAMFILTER)}",
            )

    # Validate gui-file-filter if present
    if "gui-file-filter" in payload:
        value = payload.get("gui-file-filter")
        if value and value not in VALID_BODY_GUI_FILE_FILTER:
            return (
                False,
                f"Invalid gui-file-filter '{value}'. Must be one of: {', '.join(VALID_BODY_GUI_FILE_FILTER)}",
            )

    # Validate gui-application-control if present
    if "gui-application-control" in payload:
        value = payload.get("gui-application-control")
        if value and value not in VALID_BODY_GUI_APPLICATION_CONTROL:
            return (
                False,
                f"Invalid gui-application-control '{value}'. Must be one of: {', '.join(VALID_BODY_GUI_APPLICATION_CONTROL)}",
            )

    # Validate gui-ips if present
    if "gui-ips" in payload:
        value = payload.get("gui-ips")
        if value and value not in VALID_BODY_GUI_IPS:
            return (
                False,
                f"Invalid gui-ips '{value}'. Must be one of: {', '.join(VALID_BODY_GUI_IPS)}",
            )

    # Validate gui-dhcp-advanced if present
    if "gui-dhcp-advanced" in payload:
        value = payload.get("gui-dhcp-advanced")
        if value and value not in VALID_BODY_GUI_DHCP_ADVANCED:
            return (
                False,
                f"Invalid gui-dhcp-advanced '{value}'. Must be one of: {', '.join(VALID_BODY_GUI_DHCP_ADVANCED)}",
            )

    # Validate gui-vpn if present
    if "gui-vpn" in payload:
        value = payload.get("gui-vpn")
        if value and value not in VALID_BODY_GUI_VPN:
            return (
                False,
                f"Invalid gui-vpn '{value}'. Must be one of: {', '.join(VALID_BODY_GUI_VPN)}",
            )

    # Validate gui-wireless-controller if present
    if "gui-wireless-controller" in payload:
        value = payload.get("gui-wireless-controller")
        if value and value not in VALID_BODY_GUI_WIRELESS_CONTROLLER:
            return (
                False,
                f"Invalid gui-wireless-controller '{value}'. Must be one of: {', '.join(VALID_BODY_GUI_WIRELESS_CONTROLLER)}",
            )

    # Validate gui-advanced-wireless-features if present
    if "gui-advanced-wireless-features" in payload:
        value = payload.get("gui-advanced-wireless-features")
        if value and value not in VALID_BODY_GUI_ADVANCED_WIRELESS_FEATURES:
            return (
                False,
                f"Invalid gui-advanced-wireless-features '{value}'. Must be one of: {', '.join(VALID_BODY_GUI_ADVANCED_WIRELESS_FEATURES)}",
            )

    # Validate gui-switch-controller if present
    if "gui-switch-controller" in payload:
        value = payload.get("gui-switch-controller")
        if value and value not in VALID_BODY_GUI_SWITCH_CONTROLLER:
            return (
                False,
                f"Invalid gui-switch-controller '{value}'. Must be one of: {', '.join(VALID_BODY_GUI_SWITCH_CONTROLLER)}",
            )

    # Validate gui-fortiap-split-tunneling if present
    if "gui-fortiap-split-tunneling" in payload:
        value = payload.get("gui-fortiap-split-tunneling")
        if value and value not in VALID_BODY_GUI_FORTIAP_SPLIT_TUNNELING:
            return (
                False,
                f"Invalid gui-fortiap-split-tunneling '{value}'. Must be one of: {', '.join(VALID_BODY_GUI_FORTIAP_SPLIT_TUNNELING)}",
            )

    # Validate gui-webfilter-advanced if present
    if "gui-webfilter-advanced" in payload:
        value = payload.get("gui-webfilter-advanced")
        if value and value not in VALID_BODY_GUI_WEBFILTER_ADVANCED:
            return (
                False,
                f"Invalid gui-webfilter-advanced '{value}'. Must be one of: {', '.join(VALID_BODY_GUI_WEBFILTER_ADVANCED)}",
            )

    # Validate gui-traffic-shaping if present
    if "gui-traffic-shaping" in payload:
        value = payload.get("gui-traffic-shaping")
        if value and value not in VALID_BODY_GUI_TRAFFIC_SHAPING:
            return (
                False,
                f"Invalid gui-traffic-shaping '{value}'. Must be one of: {', '.join(VALID_BODY_GUI_TRAFFIC_SHAPING)}",
            )

    # Validate gui-wan-load-balancing if present
    if "gui-wan-load-balancing" in payload:
        value = payload.get("gui-wan-load-balancing")
        if value and value not in VALID_BODY_GUI_WAN_LOAD_BALANCING:
            return (
                False,
                f"Invalid gui-wan-load-balancing '{value}'. Must be one of: {', '.join(VALID_BODY_GUI_WAN_LOAD_BALANCING)}",
            )

    # Validate gui-antivirus if present
    if "gui-antivirus" in payload:
        value = payload.get("gui-antivirus")
        if value and value not in VALID_BODY_GUI_ANTIVIRUS:
            return (
                False,
                f"Invalid gui-antivirus '{value}'. Must be one of: {', '.join(VALID_BODY_GUI_ANTIVIRUS)}",
            )

    # Validate gui-webfilter if present
    if "gui-webfilter" in payload:
        value = payload.get("gui-webfilter")
        if value and value not in VALID_BODY_GUI_WEBFILTER:
            return (
                False,
                f"Invalid gui-webfilter '{value}'. Must be one of: {', '.join(VALID_BODY_GUI_WEBFILTER)}",
            )

    # Validate gui-videofilter if present
    if "gui-videofilter" in payload:
        value = payload.get("gui-videofilter")
        if value and value not in VALID_BODY_GUI_VIDEOFILTER:
            return (
                False,
                f"Invalid gui-videofilter '{value}'. Must be one of: {', '.join(VALID_BODY_GUI_VIDEOFILTER)}",
            )

    # Validate gui-dnsfilter if present
    if "gui-dnsfilter" in payload:
        value = payload.get("gui-dnsfilter")
        if value and value not in VALID_BODY_GUI_DNSFILTER:
            return (
                False,
                f"Invalid gui-dnsfilter '{value}'. Must be one of: {', '.join(VALID_BODY_GUI_DNSFILTER)}",
            )

    # Validate gui-waf-profile if present
    if "gui-waf-profile" in payload:
        value = payload.get("gui-waf-profile")
        if value and value not in VALID_BODY_GUI_WAF_PROFILE:
            return (
                False,
                f"Invalid gui-waf-profile '{value}'. Must be one of: {', '.join(VALID_BODY_GUI_WAF_PROFILE)}",
            )

    # Validate gui-dlp-profile if present
    if "gui-dlp-profile" in payload:
        value = payload.get("gui-dlp-profile")
        if value and value not in VALID_BODY_GUI_DLP_PROFILE:
            return (
                False,
                f"Invalid gui-dlp-profile '{value}'. Must be one of: {', '.join(VALID_BODY_GUI_DLP_PROFILE)}",
            )

    # Validate gui-dlp-advanced if present
    if "gui-dlp-advanced" in payload:
        value = payload.get("gui-dlp-advanced")
        if value and value not in VALID_BODY_GUI_DLP_ADVANCED:
            return (
                False,
                f"Invalid gui-dlp-advanced '{value}'. Must be one of: {', '.join(VALID_BODY_GUI_DLP_ADVANCED)}",
            )

    # Validate gui-virtual-patch-profile if present
    if "gui-virtual-patch-profile" in payload:
        value = payload.get("gui-virtual-patch-profile")
        if value and value not in VALID_BODY_GUI_VIRTUAL_PATCH_PROFILE:
            return (
                False,
                f"Invalid gui-virtual-patch-profile '{value}'. Must be one of: {', '.join(VALID_BODY_GUI_VIRTUAL_PATCH_PROFILE)}",
            )

    # Validate gui-casb if present
    if "gui-casb" in payload:
        value = payload.get("gui-casb")
        if value and value not in VALID_BODY_GUI_CASB:
            return (
                False,
                f"Invalid gui-casb '{value}'. Must be one of: {', '.join(VALID_BODY_GUI_CASB)}",
            )

    # Validate gui-fortiextender-controller if present
    if "gui-fortiextender-controller" in payload:
        value = payload.get("gui-fortiextender-controller")
        if value and value not in VALID_BODY_GUI_FORTIEXTENDER_CONTROLLER:
            return (
                False,
                f"Invalid gui-fortiextender-controller '{value}'. Must be one of: {', '.join(VALID_BODY_GUI_FORTIEXTENDER_CONTROLLER)}",
            )

    # Validate gui-advanced-policy if present
    if "gui-advanced-policy" in payload:
        value = payload.get("gui-advanced-policy")
        if value and value not in VALID_BODY_GUI_ADVANCED_POLICY:
            return (
                False,
                f"Invalid gui-advanced-policy '{value}'. Must be one of: {', '.join(VALID_BODY_GUI_ADVANCED_POLICY)}",
            )

    # Validate gui-allow-unnamed-policy if present
    if "gui-allow-unnamed-policy" in payload:
        value = payload.get("gui-allow-unnamed-policy")
        if value and value not in VALID_BODY_GUI_ALLOW_UNNAMED_POLICY:
            return (
                False,
                f"Invalid gui-allow-unnamed-policy '{value}'. Must be one of: {', '.join(VALID_BODY_GUI_ALLOW_UNNAMED_POLICY)}",
            )

    # Validate gui-email-collection if present
    if "gui-email-collection" in payload:
        value = payload.get("gui-email-collection")
        if value and value not in VALID_BODY_GUI_EMAIL_COLLECTION:
            return (
                False,
                f"Invalid gui-email-collection '{value}'. Must be one of: {', '.join(VALID_BODY_GUI_EMAIL_COLLECTION)}",
            )

    # Validate gui-multiple-interface-policy if present
    if "gui-multiple-interface-policy" in payload:
        value = payload.get("gui-multiple-interface-policy")
        if value and value not in VALID_BODY_GUI_MULTIPLE_INTERFACE_POLICY:
            return (
                False,
                f"Invalid gui-multiple-interface-policy '{value}'. Must be one of: {', '.join(VALID_BODY_GUI_MULTIPLE_INTERFACE_POLICY)}",
            )

    # Validate gui-policy-disclaimer if present
    if "gui-policy-disclaimer" in payload:
        value = payload.get("gui-policy-disclaimer")
        if value and value not in VALID_BODY_GUI_POLICY_DISCLAIMER:
            return (
                False,
                f"Invalid gui-policy-disclaimer '{value}'. Must be one of: {', '.join(VALID_BODY_GUI_POLICY_DISCLAIMER)}",
            )

    # Validate gui-ztna if present
    if "gui-ztna" in payload:
        value = payload.get("gui-ztna")
        if value and value not in VALID_BODY_GUI_ZTNA:
            return (
                False,
                f"Invalid gui-ztna '{value}'. Must be one of: {', '.join(VALID_BODY_GUI_ZTNA)}",
            )

    # Validate gui-ot if present
    if "gui-ot" in payload:
        value = payload.get("gui-ot")
        if value and value not in VALID_BODY_GUI_OT:
            return (
                False,
                f"Invalid gui-ot '{value}'. Must be one of: {', '.join(VALID_BODY_GUI_OT)}",
            )

    # Validate gui-dynamic-device-os-id if present
    if "gui-dynamic-device-os-id" in payload:
        value = payload.get("gui-dynamic-device-os-id")
        if value and value not in VALID_BODY_GUI_DYNAMIC_DEVICE_OS_ID:
            return (
                False,
                f"Invalid gui-dynamic-device-os-id '{value}'. Must be one of: {', '.join(VALID_BODY_GUI_DYNAMIC_DEVICE_OS_ID)}",
            )

    # Validate ike-session-resume if present
    if "ike-session-resume" in payload:
        value = payload.get("ike-session-resume")
        if value and value not in VALID_BODY_IKE_SESSION_RESUME:
            return (
                False,
                f"Invalid ike-session-resume '{value}'. Must be one of: {', '.join(VALID_BODY_IKE_SESSION_RESUME)}",
            )

    # Validate ike-quick-crash-detect if present
    if "ike-quick-crash-detect" in payload:
        value = payload.get("ike-quick-crash-detect")
        if value and value not in VALID_BODY_IKE_QUICK_CRASH_DETECT:
            return (
                False,
                f"Invalid ike-quick-crash-detect '{value}'. Must be one of: {', '.join(VALID_BODY_IKE_QUICK_CRASH_DETECT)}",
            )

    # Validate ike-dn-format if present
    if "ike-dn-format" in payload:
        value = payload.get("ike-dn-format")
        if value and value not in VALID_BODY_IKE_DN_FORMAT:
            return (
                False,
                f"Invalid ike-dn-format '{value}'. Must be one of: {', '.join(VALID_BODY_IKE_DN_FORMAT)}",
            )

    # Validate ike-port if present
    if "ike-port" in payload:
        value = payload.get("ike-port")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1024 or int_val > 65535:
                    return (False, "ike-port must be between 1024 and 65535")
            except (ValueError, TypeError):
                return (False, f"ike-port must be numeric, got: {value}")

    # Validate ike-tcp-port if present
    if "ike-tcp-port" in payload:
        value = payload.get("ike-tcp-port")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 65535:
                    return (False, "ike-tcp-port must be between 1 and 65535")
            except (ValueError, TypeError):
                return (False, f"ike-tcp-port must be numeric, got: {value}")

    # Validate ike-policy-route if present
    if "ike-policy-route" in payload:
        value = payload.get("ike-policy-route")
        if value and value not in VALID_BODY_IKE_POLICY_ROUTE:
            return (
                False,
                f"Invalid ike-policy-route '{value}'. Must be one of: {', '.join(VALID_BODY_IKE_POLICY_ROUTE)}",
            )

    # Validate ike-detailed-event-logs if present
    if "ike-detailed-event-logs" in payload:
        value = payload.get("ike-detailed-event-logs")
        if value and value not in VALID_BODY_IKE_DETAILED_EVENT_LOGS:
            return (
                False,
                f"Invalid ike-detailed-event-logs '{value}'. Must be one of: {', '.join(VALID_BODY_IKE_DETAILED_EVENT_LOGS)}",
            )

    # Validate block-land-attack if present
    if "block-land-attack" in payload:
        value = payload.get("block-land-attack")
        if value and value not in VALID_BODY_BLOCK_LAND_ATTACK:
            return (
                False,
                f"Invalid block-land-attack '{value}'. Must be one of: {', '.join(VALID_BODY_BLOCK_LAND_ATTACK)}",
            )

    # Validate default-app-port-as-service if present
    if "default-app-port-as-service" in payload:
        value = payload.get("default-app-port-as-service")
        if value and value not in VALID_BODY_DEFAULT_APP_PORT_AS_SERVICE:
            return (
                False,
                f"Invalid default-app-port-as-service '{value}'. Must be one of: {', '.join(VALID_BODY_DEFAULT_APP_PORT_AS_SERVICE)}",
            )

    # Validate fqdn-session-check if present
    if "fqdn-session-check" in payload:
        value = payload.get("fqdn-session-check")
        if value and value not in VALID_BODY_FQDN_SESSION_CHECK:
            return (
                False,
                f"Invalid fqdn-session-check '{value}'. Must be one of: {', '.join(VALID_BODY_FQDN_SESSION_CHECK)}",
            )

    # Validate ext-resource-session-check if present
    if "ext-resource-session-check" in payload:
        value = payload.get("ext-resource-session-check")
        if value and value not in VALID_BODY_EXT_RESOURCE_SESSION_CHECK:
            return (
                False,
                f"Invalid ext-resource-session-check '{value}'. Must be one of: {', '.join(VALID_BODY_EXT_RESOURCE_SESSION_CHECK)}",
            )

    # Validate dyn-addr-session-check if present
    if "dyn-addr-session-check" in payload:
        value = payload.get("dyn-addr-session-check")
        if value and value not in VALID_BODY_DYN_ADDR_SESSION_CHECK:
            return (
                False,
                f"Invalid dyn-addr-session-check '{value}'. Must be one of: {', '.join(VALID_BODY_DYN_ADDR_SESSION_CHECK)}",
            )

    # Validate default-policy-expiry-days if present
    if "default-policy-expiry-days" in payload:
        value = payload.get("default-policy-expiry-days")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 365:
                    return (
                        False,
                        "default-policy-expiry-days must be between 0 and 365",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"default-policy-expiry-days must be numeric, got: {value}",
                )

    # Validate gui-enforce-change-summary if present
    if "gui-enforce-change-summary" in payload:
        value = payload.get("gui-enforce-change-summary")
        if value and value not in VALID_BODY_GUI_ENFORCE_CHANGE_SUMMARY:
            return (
                False,
                f"Invalid gui-enforce-change-summary '{value}'. Must be one of: {', '.join(VALID_BODY_GUI_ENFORCE_CHANGE_SUMMARY)}",
            )

    # Validate internet-service-database-cache if present
    if "internet-service-database-cache" in payload:
        value = payload.get("internet-service-database-cache")
        if value and value not in VALID_BODY_INTERNET_SERVICE_DATABASE_CACHE:
            return (
                False,
                f"Invalid internet-service-database-cache '{value}'. Must be one of: {', '.join(VALID_BODY_INTERNET_SERVICE_DATABASE_CACHE)}",
            )

    # Validate internet-service-app-ctrl-size if present
    if "internet-service-app-ctrl-size" in payload:
        value = payload.get("internet-service-app-ctrl-size")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "internet-service-app-ctrl-size must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"internet-service-app-ctrl-size must be numeric, got: {value}",
                )

    return (True, None)
