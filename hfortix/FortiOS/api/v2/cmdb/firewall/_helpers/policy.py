"""
Validation helpers for firewall policy endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_STATUS = ["enable", "disable"]
VALID_BODY_ACTION = ["accept", "deny", "ipsec"]
VALID_BODY_NAT64 = ["enable", "disable"]
VALID_BODY_NAT46 = ["enable", "disable"]
VALID_BODY_ZTNA_STATUS = ["enable", "disable"]
VALID_BODY_ZTNA_DEVICE_OWNERSHIP = ["enable", "disable"]
VALID_BODY_ZTNA_TAGS_MATCH_LOGIC = ["or", "and"]
VALID_BODY_INTERNET_SERVICE = ["enable", "disable"]
VALID_BODY_INTERNET_SERVICE_SRC = ["enable", "disable"]
VALID_BODY_REPUTATION_DIRECTION = ["source", "destination"]
VALID_BODY_INTERNET_SERVICE6 = ["enable", "disable"]
VALID_BODY_INTERNET_SERVICE6_SRC = ["enable", "disable"]
VALID_BODY_REPUTATION_DIRECTION6 = ["source", "destination"]
VALID_BODY_RTP_NAT = ["disable", "enable"]
VALID_BODY_SEND_DENY_PACKET = ["disable", "enable"]
VALID_BODY_FIREWALL_SESSION_DIRTY = ["check-all", "check-new"]
VALID_BODY_SCHEDULE_TIMEOUT = ["enable", "disable"]
VALID_BODY_POLICY_EXPIRY = ["enable", "disable"]
VALID_BODY_TOS_NEGATE = ["enable", "disable"]
VALID_BODY_ANTI_REPLAY = ["enable", "disable"]
VALID_BODY_TCP_SESSION_WITHOUT_SYN = ["all", "data-only", "disable"]
VALID_BODY_GEOIP_ANYCAST = ["enable", "disable"]
VALID_BODY_GEOIP_MATCH = ["physical-location", "registered-location"]
VALID_BODY_DYNAMIC_SHAPING = ["enable", "disable"]
VALID_BODY_PASSIVE_WAN_HEALTH_MEASUREMENT = ["enable", "disable"]
VALID_BODY_APP_MONITOR = ["enable", "disable"]
VALID_BODY_UTM_STATUS = ["enable", "disable"]
VALID_BODY_INSPECTION_MODE = ["proxy", "flow"]
VALID_BODY_HTTP_POLICY_REDIRECT = ["enable", "disable", "legacy"]
VALID_BODY_SSH_POLICY_REDIRECT = ["enable", "disable"]
VALID_BODY_ZTNA_POLICY_REDIRECT = ["enable", "disable"]
VALID_BODY_PROFILE_TYPE = ["single", "group"]
VALID_BODY_LOGTRAFFIC = ["all", "utm", "disable"]
VALID_BODY_LOGTRAFFIC_START = ["enable", "disable"]
VALID_BODY_LOG_HTTP_TRANSACTION = ["enable", "disable"]
VALID_BODY_CAPTURE_PACKET = ["enable", "disable"]
VALID_BODY_AUTO_ASIC_OFFLOAD = ["enable", "disable"]
VALID_BODY_NP_ACCELERATION = ["enable", "disable"]
VALID_BODY_NAT = ["enable", "disable"]
VALID_BODY_PCP_OUTBOUND = ["enable", "disable"]
VALID_BODY_PCP_INBOUND = ["enable", "disable"]
VALID_BODY_PERMIT_ANY_HOST = ["enable", "disable"]
VALID_BODY_PERMIT_STUN_HOST = ["enable", "disable"]
VALID_BODY_FIXEDPORT = ["enable", "disable"]
VALID_BODY_PORT_PRESERVE = ["enable", "disable"]
VALID_BODY_PORT_RANDOM = ["enable", "disable"]
VALID_BODY_IPPOOL = ["enable", "disable"]
VALID_BODY_INBOUND = ["enable", "disable"]
VALID_BODY_OUTBOUND = ["enable", "disable"]
VALID_BODY_NATINBOUND = ["enable", "disable"]
VALID_BODY_NATOUTBOUND = ["enable", "disable"]
VALID_BODY_FEC = ["enable", "disable"]
VALID_BODY_WCCP = ["enable", "disable"]
VALID_BODY_NTLM = ["enable", "disable"]
VALID_BODY_NTLM_GUEST = ["enable", "disable"]
VALID_BODY_AUTH_PATH = ["enable", "disable"]
VALID_BODY_DISCLAIMER = ["enable", "disable"]
VALID_BODY_EMAIL_COLLECT = ["enable", "disable"]
VALID_BODY_MATCH_VIP = ["enable", "disable"]
VALID_BODY_MATCH_VIP_ONLY = ["enable", "disable"]
VALID_BODY_DIFFSERV_COPY = ["enable", "disable"]
VALID_BODY_DIFFSERV_FORWARD = ["enable", "disable"]
VALID_BODY_DIFFSERV_REVERSE = ["enable", "disable"]
VALID_BODY_BLOCK_NOTIFICATION = ["enable", "disable"]
VALID_BODY_SRCADDR_NEGATE = ["enable", "disable"]
VALID_BODY_SRCADDR6_NEGATE = ["enable", "disable"]
VALID_BODY_DSTADDR_NEGATE = ["enable", "disable"]
VALID_BODY_DSTADDR6_NEGATE = ["enable", "disable"]
VALID_BODY_ZTNA_EMS_TAG_NEGATE = ["enable", "disable"]
VALID_BODY_SERVICE_NEGATE = ["enable", "disable"]
VALID_BODY_INTERNET_SERVICE_NEGATE = ["enable", "disable"]
VALID_BODY_INTERNET_SERVICE_SRC_NEGATE = ["enable", "disable"]
VALID_BODY_INTERNET_SERVICE6_NEGATE = ["enable", "disable"]
VALID_BODY_INTERNET_SERVICE6_SRC_NEGATE = ["enable", "disable"]
VALID_BODY_TIMEOUT_SEND_RST = ["enable", "disable"]
VALID_BODY_CAPTIVE_PORTAL_EXEMPT = ["enable", "disable"]
VALID_BODY_DSRI = ["enable", "disable"]
VALID_BODY_RADIUS_MAC_AUTH_BYPASS = ["enable", "disable"]
VALID_BODY_RADIUS_IP_AUTH_BYPASS = ["enable", "disable"]
VALID_BODY_DELAY_TCP_NPU_SESSION = ["enable", "disable"]
VALID_BODY_SGT_CHECK = ["enable", "disable"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_policy_get(
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
# POST Validation
# ============================================================================


def validate_policy_post(payload: dict[str, Any]) -> tuple[bool, str | None]:
    """
    Validate POST request payload for creating policy.

    Args:
        payload: The payload to validate

    Returns:
        Tuple of (is_valid, error_message)
    """
    # Validate policyid if present
    if "policyid" in payload:
        value = payload.get("policyid")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967294:
                    return (
                        False,
                        "policyid must be between 0 and 4294967294",
                    )
            except (ValueError, TypeError):
                return (False, f"policyid must be numeric, got: {value}")

    # Validate status if present
    if "status" in payload:
        value = payload.get("status")
        if value and value not in VALID_BODY_STATUS:
            return (
                False,
                f"Invalid status '{value}'. Must be one of: {', '.join(VALID_BODY_STATUS)}",
            )

    # Validate name if present
    if "name" in payload:
        value = payload.get("name")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "name cannot exceed 35 characters")

    # Validate action if present
    if "action" in payload:
        value = payload.get("action")
        if value and value not in VALID_BODY_ACTION:
            return (
                False,
                f"Invalid action '{value}'. Must be one of: {', '.join(VALID_BODY_ACTION)}",
            )

    # Validate nat64 if present
    if "nat64" in payload:
        value = payload.get("nat64")
        if value and value not in VALID_BODY_NAT64:
            return (
                False,
                f"Invalid nat64 '{value}'. Must be one of: {', '.join(VALID_BODY_NAT64)}",
            )

    # Validate nat46 if present
    if "nat46" in payload:
        value = payload.get("nat46")
        if value and value not in VALID_BODY_NAT46:
            return (
                False,
                f"Invalid nat46 '{value}'. Must be one of: {', '.join(VALID_BODY_NAT46)}",
            )

    # Validate ztna-status if present
    if "ztna-status" in payload:
        value = payload.get("ztna-status")
        if value and value not in VALID_BODY_ZTNA_STATUS:
            return (
                False,
                f"Invalid ztna-status '{value}'. Must be one of: {', '.join(VALID_BODY_ZTNA_STATUS)}",
            )

    # Validate ztna-device-ownership if present
    if "ztna-device-ownership" in payload:
        value = payload.get("ztna-device-ownership")
        if value and value not in VALID_BODY_ZTNA_DEVICE_OWNERSHIP:
            return (
                False,
                f"Invalid ztna-device-ownership '{value}'. Must be one of: {', '.join(VALID_BODY_ZTNA_DEVICE_OWNERSHIP)}",
            )

    # Validate ztna-tags-match-logic if present
    if "ztna-tags-match-logic" in payload:
        value = payload.get("ztna-tags-match-logic")
        if value and value not in VALID_BODY_ZTNA_TAGS_MATCH_LOGIC:
            return (
                False,
                f"Invalid ztna-tags-match-logic '{value}'. Must be one of: {', '.join(VALID_BODY_ZTNA_TAGS_MATCH_LOGIC)}",
            )

    # Validate internet-service if present
    if "internet-service" in payload:
        value = payload.get("internet-service")
        if value and value not in VALID_BODY_INTERNET_SERVICE:
            return (
                False,
                f"Invalid internet-service '{value}'. Must be one of: {', '.join(VALID_BODY_INTERNET_SERVICE)}",
            )

    # Validate internet-service-src if present
    if "internet-service-src" in payload:
        value = payload.get("internet-service-src")
        if value and value not in VALID_BODY_INTERNET_SERVICE_SRC:
            return (
                False,
                f"Invalid internet-service-src '{value}'. Must be one of: {', '.join(VALID_BODY_INTERNET_SERVICE_SRC)}",
            )

    # Validate reputation-minimum if present
    if "reputation-minimum" in payload:
        value = payload.get("reputation-minimum")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "reputation-minimum must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"reputation-minimum must be numeric, got: {value}",
                )

    # Validate reputation-direction if present
    if "reputation-direction" in payload:
        value = payload.get("reputation-direction")
        if value and value not in VALID_BODY_REPUTATION_DIRECTION:
            return (
                False,
                f"Invalid reputation-direction '{value}'. Must be one of: {', '.join(VALID_BODY_REPUTATION_DIRECTION)}",
            )

    # Validate internet-service6 if present
    if "internet-service6" in payload:
        value = payload.get("internet-service6")
        if value and value not in VALID_BODY_INTERNET_SERVICE6:
            return (
                False,
                f"Invalid internet-service6 '{value}'. Must be one of: {', '.join(VALID_BODY_INTERNET_SERVICE6)}",
            )

    # Validate internet-service6-src if present
    if "internet-service6-src" in payload:
        value = payload.get("internet-service6-src")
        if value and value not in VALID_BODY_INTERNET_SERVICE6_SRC:
            return (
                False,
                f"Invalid internet-service6-src '{value}'. Must be one of: {', '.join(VALID_BODY_INTERNET_SERVICE6_SRC)}",
            )

    # Validate reputation-minimum6 if present
    if "reputation-minimum6" in payload:
        value = payload.get("reputation-minimum6")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "reputation-minimum6 must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"reputation-minimum6 must be numeric, got: {value}",
                )

    # Validate reputation-direction6 if present
    if "reputation-direction6" in payload:
        value = payload.get("reputation-direction6")
        if value and value not in VALID_BODY_REPUTATION_DIRECTION6:
            return (
                False,
                f"Invalid reputation-direction6 '{value}'. Must be one of: {', '.join(VALID_BODY_REPUTATION_DIRECTION6)}",
            )

    # Validate rtp-nat if present
    if "rtp-nat" in payload:
        value = payload.get("rtp-nat")
        if value and value not in VALID_BODY_RTP_NAT:
            return (
                False,
                f"Invalid rtp-nat '{value}'. Must be one of: {', '.join(VALID_BODY_RTP_NAT)}",
            )

    # Validate send-deny-packet if present
    if "send-deny-packet" in payload:
        value = payload.get("send-deny-packet")
        if value and value not in VALID_BODY_SEND_DENY_PACKET:
            return (
                False,
                f"Invalid send-deny-packet '{value}'. Must be one of: {', '.join(VALID_BODY_SEND_DENY_PACKET)}",
            )

    # Validate firewall-session-dirty if present
    if "firewall-session-dirty" in payload:
        value = payload.get("firewall-session-dirty")
        if value and value not in VALID_BODY_FIREWALL_SESSION_DIRTY:
            return (
                False,
                f"Invalid firewall-session-dirty '{value}'. Must be one of: {', '.join(VALID_BODY_FIREWALL_SESSION_DIRTY)}",
            )

    # Validate schedule if present
    if "schedule" in payload:
        value = payload.get("schedule")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "schedule cannot exceed 35 characters")

    # Validate schedule-timeout if present
    if "schedule-timeout" in payload:
        value = payload.get("schedule-timeout")
        if value and value not in VALID_BODY_SCHEDULE_TIMEOUT:
            return (
                False,
                f"Invalid schedule-timeout '{value}'. Must be one of: {', '.join(VALID_BODY_SCHEDULE_TIMEOUT)}",
            )

    # Validate policy-expiry if present
    if "policy-expiry" in payload:
        value = payload.get("policy-expiry")
        if value and value not in VALID_BODY_POLICY_EXPIRY:
            return (
                False,
                f"Invalid policy-expiry '{value}'. Must be one of: {', '.join(VALID_BODY_POLICY_EXPIRY)}",
            )

    # Validate tos-negate if present
    if "tos-negate" in payload:
        value = payload.get("tos-negate")
        if value and value not in VALID_BODY_TOS_NEGATE:
            return (
                False,
                f"Invalid tos-negate '{value}'. Must be one of: {', '.join(VALID_BODY_TOS_NEGATE)}",
            )

    # Validate anti-replay if present
    if "anti-replay" in payload:
        value = payload.get("anti-replay")
        if value and value not in VALID_BODY_ANTI_REPLAY:
            return (
                False,
                f"Invalid anti-replay '{value}'. Must be one of: {', '.join(VALID_BODY_ANTI_REPLAY)}",
            )

    # Validate tcp-session-without-syn if present
    if "tcp-session-without-syn" in payload:
        value = payload.get("tcp-session-without-syn")
        if value and value not in VALID_BODY_TCP_SESSION_WITHOUT_SYN:
            return (
                False,
                f"Invalid tcp-session-without-syn '{value}'. Must be one of: {', '.join(VALID_BODY_TCP_SESSION_WITHOUT_SYN)}",
            )

    # Validate geoip-anycast if present
    if "geoip-anycast" in payload:
        value = payload.get("geoip-anycast")
        if value and value not in VALID_BODY_GEOIP_ANYCAST:
            return (
                False,
                f"Invalid geoip-anycast '{value}'. Must be one of: {', '.join(VALID_BODY_GEOIP_ANYCAST)}",
            )

    # Validate geoip-match if present
    if "geoip-match" in payload:
        value = payload.get("geoip-match")
        if value and value not in VALID_BODY_GEOIP_MATCH:
            return (
                False,
                f"Invalid geoip-match '{value}'. Must be one of: {', '.join(VALID_BODY_GEOIP_MATCH)}",
            )

    # Validate dynamic-shaping if present
    if "dynamic-shaping" in payload:
        value = payload.get("dynamic-shaping")
        if value and value not in VALID_BODY_DYNAMIC_SHAPING:
            return (
                False,
                f"Invalid dynamic-shaping '{value}'. Must be one of: {', '.join(VALID_BODY_DYNAMIC_SHAPING)}",
            )

    # Validate passive-wan-health-measurement if present
    if "passive-wan-health-measurement" in payload:
        value = payload.get("passive-wan-health-measurement")
        if value and value not in VALID_BODY_PASSIVE_WAN_HEALTH_MEASUREMENT:
            return (
                False,
                f"Invalid passive-wan-health-measurement '{value}'. Must be one of: {', '.join(VALID_BODY_PASSIVE_WAN_HEALTH_MEASUREMENT)}",
            )

    # Validate app-monitor if present
    if "app-monitor" in payload:
        value = payload.get("app-monitor")
        if value and value not in VALID_BODY_APP_MONITOR:
            return (
                False,
                f"Invalid app-monitor '{value}'. Must be one of: {', '.join(VALID_BODY_APP_MONITOR)}",
            )

    # Validate utm-status if present
    if "utm-status" in payload:
        value = payload.get("utm-status")
        if value and value not in VALID_BODY_UTM_STATUS:
            return (
                False,
                f"Invalid utm-status '{value}'. Must be one of: {', '.join(VALID_BODY_UTM_STATUS)}",
            )

    # Validate inspection-mode if present
    if "inspection-mode" in payload:
        value = payload.get("inspection-mode")
        if value and value not in VALID_BODY_INSPECTION_MODE:
            return (
                False,
                f"Invalid inspection-mode '{value}'. Must be one of: {', '.join(VALID_BODY_INSPECTION_MODE)}",
            )

    # Validate http-policy-redirect if present
    if "http-policy-redirect" in payload:
        value = payload.get("http-policy-redirect")
        if value and value not in VALID_BODY_HTTP_POLICY_REDIRECT:
            return (
                False,
                f"Invalid http-policy-redirect '{value}'. Must be one of: {', '.join(VALID_BODY_HTTP_POLICY_REDIRECT)}",
            )

    # Validate ssh-policy-redirect if present
    if "ssh-policy-redirect" in payload:
        value = payload.get("ssh-policy-redirect")
        if value and value not in VALID_BODY_SSH_POLICY_REDIRECT:
            return (
                False,
                f"Invalid ssh-policy-redirect '{value}'. Must be one of: {', '.join(VALID_BODY_SSH_POLICY_REDIRECT)}",
            )

    # Validate ztna-policy-redirect if present
    if "ztna-policy-redirect" in payload:
        value = payload.get("ztna-policy-redirect")
        if value and value not in VALID_BODY_ZTNA_POLICY_REDIRECT:
            return (
                False,
                f"Invalid ztna-policy-redirect '{value}'. Must be one of: {', '.join(VALID_BODY_ZTNA_POLICY_REDIRECT)}",
            )

    # Validate webproxy-profile if present
    if "webproxy-profile" in payload:
        value = payload.get("webproxy-profile")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "webproxy-profile cannot exceed 63 characters")

    # Validate profile-type if present
    if "profile-type" in payload:
        value = payload.get("profile-type")
        if value and value not in VALID_BODY_PROFILE_TYPE:
            return (
                False,
                f"Invalid profile-type '{value}'. Must be one of: {', '.join(VALID_BODY_PROFILE_TYPE)}",
            )

    # Validate profile-group if present
    if "profile-group" in payload:
        value = payload.get("profile-group")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "profile-group cannot exceed 47 characters")

    # Validate profile-protocol-options if present
    if "profile-protocol-options" in payload:
        value = payload.get("profile-protocol-options")
        if value and isinstance(value, str) and len(value) > 47:
            return (
                False,
                "profile-protocol-options cannot exceed 47 characters",
            )

    # Validate ssl-ssh-profile if present
    if "ssl-ssh-profile" in payload:
        value = payload.get("ssl-ssh-profile")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "ssl-ssh-profile cannot exceed 47 characters")

    # Validate av-profile if present
    if "av-profile" in payload:
        value = payload.get("av-profile")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "av-profile cannot exceed 47 characters")

    # Validate webfilter-profile if present
    if "webfilter-profile" in payload:
        value = payload.get("webfilter-profile")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "webfilter-profile cannot exceed 47 characters")

    # Validate dnsfilter-profile if present
    if "dnsfilter-profile" in payload:
        value = payload.get("dnsfilter-profile")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "dnsfilter-profile cannot exceed 47 characters")

    # Validate emailfilter-profile if present
    if "emailfilter-profile" in payload:
        value = payload.get("emailfilter-profile")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "emailfilter-profile cannot exceed 47 characters")

    # Validate dlp-profile if present
    if "dlp-profile" in payload:
        value = payload.get("dlp-profile")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "dlp-profile cannot exceed 47 characters")

    # Validate file-filter-profile if present
    if "file-filter-profile" in payload:
        value = payload.get("file-filter-profile")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "file-filter-profile cannot exceed 47 characters")

    # Validate ips-sensor if present
    if "ips-sensor" in payload:
        value = payload.get("ips-sensor")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "ips-sensor cannot exceed 47 characters")

    # Validate application-list if present
    if "application-list" in payload:
        value = payload.get("application-list")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "application-list cannot exceed 47 characters")

    # Validate voip-profile if present
    if "voip-profile" in payload:
        value = payload.get("voip-profile")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "voip-profile cannot exceed 47 characters")

    # Validate ips-voip-filter if present
    if "ips-voip-filter" in payload:
        value = payload.get("ips-voip-filter")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "ips-voip-filter cannot exceed 47 characters")

    # Validate sctp-filter-profile if present
    if "sctp-filter-profile" in payload:
        value = payload.get("sctp-filter-profile")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "sctp-filter-profile cannot exceed 47 characters")

    # Validate diameter-filter-profile if present
    if "diameter-filter-profile" in payload:
        value = payload.get("diameter-filter-profile")
        if value and isinstance(value, str) and len(value) > 47:
            return (
                False,
                "diameter-filter-profile cannot exceed 47 characters",
            )

    # Validate virtual-patch-profile if present
    if "virtual-patch-profile" in payload:
        value = payload.get("virtual-patch-profile")
        if value and isinstance(value, str) and len(value) > 47:
            return (
                False,
                "virtual-patch-profile cannot exceed 47 characters",
            )

    # Validate icap-profile if present
    if "icap-profile" in payload:
        value = payload.get("icap-profile")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "icap-profile cannot exceed 47 characters")

    # Validate videofilter-profile if present
    if "videofilter-profile" in payload:
        value = payload.get("videofilter-profile")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "videofilter-profile cannot exceed 47 characters")

    # Validate waf-profile if present
    if "waf-profile" in payload:
        value = payload.get("waf-profile")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "waf-profile cannot exceed 47 characters")

    # Validate ssh-filter-profile if present
    if "ssh-filter-profile" in payload:
        value = payload.get("ssh-filter-profile")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "ssh-filter-profile cannot exceed 47 characters")

    # Validate casb-profile if present
    if "casb-profile" in payload:
        value = payload.get("casb-profile")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "casb-profile cannot exceed 47 characters")

    # Validate logtraffic if present
    if "logtraffic" in payload:
        value = payload.get("logtraffic")
        if value and value not in VALID_BODY_LOGTRAFFIC:
            return (
                False,
                f"Invalid logtraffic '{value}'. Must be one of: {', '.join(VALID_BODY_LOGTRAFFIC)}",
            )

    # Validate logtraffic-start if present
    if "logtraffic-start" in payload:
        value = payload.get("logtraffic-start")
        if value and value not in VALID_BODY_LOGTRAFFIC_START:
            return (
                False,
                f"Invalid logtraffic-start '{value}'. Must be one of: {', '.join(VALID_BODY_LOGTRAFFIC_START)}",
            )

    # Validate log-http-transaction if present
    if "log-http-transaction" in payload:
        value = payload.get("log-http-transaction")
        if value and value not in VALID_BODY_LOG_HTTP_TRANSACTION:
            return (
                False,
                f"Invalid log-http-transaction '{value}'. Must be one of: {', '.join(VALID_BODY_LOG_HTTP_TRANSACTION)}",
            )

    # Validate capture-packet if present
    if "capture-packet" in payload:
        value = payload.get("capture-packet")
        if value and value not in VALID_BODY_CAPTURE_PACKET:
            return (
                False,
                f"Invalid capture-packet '{value}'. Must be one of: {', '.join(VALID_BODY_CAPTURE_PACKET)}",
            )

    # Validate auto-asic-offload if present
    if "auto-asic-offload" in payload:
        value = payload.get("auto-asic-offload")
        if value and value not in VALID_BODY_AUTO_ASIC_OFFLOAD:
            return (
                False,
                f"Invalid auto-asic-offload '{value}'. Must be one of: {', '.join(VALID_BODY_AUTO_ASIC_OFFLOAD)}",
            )

    # Validate np-acceleration if present
    if "np-acceleration" in payload:
        value = payload.get("np-acceleration")
        if value and value not in VALID_BODY_NP_ACCELERATION:
            return (
                False,
                f"Invalid np-acceleration '{value}'. Must be one of: {', '.join(VALID_BODY_NP_ACCELERATION)}",
            )

    # Validate webproxy-forward-server if present
    if "webproxy-forward-server" in payload:
        value = payload.get("webproxy-forward-server")
        if value and isinstance(value, str) and len(value) > 63:
            return (
                False,
                "webproxy-forward-server cannot exceed 63 characters",
            )

    # Validate traffic-shaper if present
    if "traffic-shaper" in payload:
        value = payload.get("traffic-shaper")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "traffic-shaper cannot exceed 35 characters")

    # Validate traffic-shaper-reverse if present
    if "traffic-shaper-reverse" in payload:
        value = payload.get("traffic-shaper-reverse")
        if value and isinstance(value, str) and len(value) > 35:
            return (
                False,
                "traffic-shaper-reverse cannot exceed 35 characters",
            )

    # Validate per-ip-shaper if present
    if "per-ip-shaper" in payload:
        value = payload.get("per-ip-shaper")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "per-ip-shaper cannot exceed 35 characters")

    # Validate nat if present
    if "nat" in payload:
        value = payload.get("nat")
        if value and value not in VALID_BODY_NAT:
            return (
                False,
                f"Invalid nat '{value}'. Must be one of: {', '.join(VALID_BODY_NAT)}",
            )

    # Validate pcp-outbound if present
    if "pcp-outbound" in payload:
        value = payload.get("pcp-outbound")
        if value and value not in VALID_BODY_PCP_OUTBOUND:
            return (
                False,
                f"Invalid pcp-outbound '{value}'. Must be one of: {', '.join(VALID_BODY_PCP_OUTBOUND)}",
            )

    # Validate pcp-inbound if present
    if "pcp-inbound" in payload:
        value = payload.get("pcp-inbound")
        if value and value not in VALID_BODY_PCP_INBOUND:
            return (
                False,
                f"Invalid pcp-inbound '{value}'. Must be one of: {', '.join(VALID_BODY_PCP_INBOUND)}",
            )

    # Validate permit-any-host if present
    if "permit-any-host" in payload:
        value = payload.get("permit-any-host")
        if value and value not in VALID_BODY_PERMIT_ANY_HOST:
            return (
                False,
                f"Invalid permit-any-host '{value}'. Must be one of: {', '.join(VALID_BODY_PERMIT_ANY_HOST)}",
            )

    # Validate permit-stun-host if present
    if "permit-stun-host" in payload:
        value = payload.get("permit-stun-host")
        if value and value not in VALID_BODY_PERMIT_STUN_HOST:
            return (
                False,
                f"Invalid permit-stun-host '{value}'. Must be one of: {', '.join(VALID_BODY_PERMIT_STUN_HOST)}",
            )

    # Validate fixedport if present
    if "fixedport" in payload:
        value = payload.get("fixedport")
        if value and value not in VALID_BODY_FIXEDPORT:
            return (
                False,
                f"Invalid fixedport '{value}'. Must be one of: {', '.join(VALID_BODY_FIXEDPORT)}",
            )

    # Validate port-preserve if present
    if "port-preserve" in payload:
        value = payload.get("port-preserve")
        if value and value not in VALID_BODY_PORT_PRESERVE:
            return (
                False,
                f"Invalid port-preserve '{value}'. Must be one of: {', '.join(VALID_BODY_PORT_PRESERVE)}",
            )

    # Validate port-random if present
    if "port-random" in payload:
        value = payload.get("port-random")
        if value and value not in VALID_BODY_PORT_RANDOM:
            return (
                False,
                f"Invalid port-random '{value}'. Must be one of: {', '.join(VALID_BODY_PORT_RANDOM)}",
            )

    # Validate ippool if present
    if "ippool" in payload:
        value = payload.get("ippool")
        if value and value not in VALID_BODY_IPPOOL:
            return (
                False,
                f"Invalid ippool '{value}'. Must be one of: {', '.join(VALID_BODY_IPPOOL)}",
            )

    # Validate vlan-cos-fwd if present
    if "vlan-cos-fwd" in payload:
        value = payload.get("vlan-cos-fwd")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 7:
                    return (False, "vlan-cos-fwd must be between 0 and 7")
            except (ValueError, TypeError):
                return (False, f"vlan-cos-fwd must be numeric, got: {value}")

    # Validate vlan-cos-rev if present
    if "vlan-cos-rev" in payload:
        value = payload.get("vlan-cos-rev")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 7:
                    return (False, "vlan-cos-rev must be between 0 and 7")
            except (ValueError, TypeError):
                return (False, f"vlan-cos-rev must be numeric, got: {value}")

    # Validate inbound if present
    if "inbound" in payload:
        value = payload.get("inbound")
        if value and value not in VALID_BODY_INBOUND:
            return (
                False,
                f"Invalid inbound '{value}'. Must be one of: {', '.join(VALID_BODY_INBOUND)}",
            )

    # Validate outbound if present
    if "outbound" in payload:
        value = payload.get("outbound")
        if value and value not in VALID_BODY_OUTBOUND:
            return (
                False,
                f"Invalid outbound '{value}'. Must be one of: {', '.join(VALID_BODY_OUTBOUND)}",
            )

    # Validate natinbound if present
    if "natinbound" in payload:
        value = payload.get("natinbound")
        if value and value not in VALID_BODY_NATINBOUND:
            return (
                False,
                f"Invalid natinbound '{value}'. Must be one of: {', '.join(VALID_BODY_NATINBOUND)}",
            )

    # Validate natoutbound if present
    if "natoutbound" in payload:
        value = payload.get("natoutbound")
        if value and value not in VALID_BODY_NATOUTBOUND:
            return (
                False,
                f"Invalid natoutbound '{value}'. Must be one of: {', '.join(VALID_BODY_NATOUTBOUND)}",
            )

    # Validate fec if present
    if "fec" in payload:
        value = payload.get("fec")
        if value and value not in VALID_BODY_FEC:
            return (
                False,
                f"Invalid fec '{value}'. Must be one of: {', '.join(VALID_BODY_FEC)}",
            )

    # Validate wccp if present
    if "wccp" in payload:
        value = payload.get("wccp")
        if value and value not in VALID_BODY_WCCP:
            return (
                False,
                f"Invalid wccp '{value}'. Must be one of: {', '.join(VALID_BODY_WCCP)}",
            )

    # Validate ntlm if present
    if "ntlm" in payload:
        value = payload.get("ntlm")
        if value and value not in VALID_BODY_NTLM:
            return (
                False,
                f"Invalid ntlm '{value}'. Must be one of: {', '.join(VALID_BODY_NTLM)}",
            )

    # Validate ntlm-guest if present
    if "ntlm-guest" in payload:
        value = payload.get("ntlm-guest")
        if value and value not in VALID_BODY_NTLM_GUEST:
            return (
                False,
                f"Invalid ntlm-guest '{value}'. Must be one of: {', '.join(VALID_BODY_NTLM_GUEST)}",
            )

    # Validate fsso-agent-for-ntlm if present
    if "fsso-agent-for-ntlm" in payload:
        value = payload.get("fsso-agent-for-ntlm")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "fsso-agent-for-ntlm cannot exceed 35 characters")

    # Validate auth-path if present
    if "auth-path" in payload:
        value = payload.get("auth-path")
        if value and value not in VALID_BODY_AUTH_PATH:
            return (
                False,
                f"Invalid auth-path '{value}'. Must be one of: {', '.join(VALID_BODY_AUTH_PATH)}",
            )

    # Validate disclaimer if present
    if "disclaimer" in payload:
        value = payload.get("disclaimer")
        if value and value not in VALID_BODY_DISCLAIMER:
            return (
                False,
                f"Invalid disclaimer '{value}'. Must be one of: {', '.join(VALID_BODY_DISCLAIMER)}",
            )

    # Validate email-collect if present
    if "email-collect" in payload:
        value = payload.get("email-collect")
        if value and value not in VALID_BODY_EMAIL_COLLECT:
            return (
                False,
                f"Invalid email-collect '{value}'. Must be one of: {', '.join(VALID_BODY_EMAIL_COLLECT)}",
            )

    # Validate vpntunnel if present
    if "vpntunnel" in payload:
        value = payload.get("vpntunnel")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "vpntunnel cannot exceed 35 characters")

    # Validate match-vip if present
    if "match-vip" in payload:
        value = payload.get("match-vip")
        if value and value not in VALID_BODY_MATCH_VIP:
            return (
                False,
                f"Invalid match-vip '{value}'. Must be one of: {', '.join(VALID_BODY_MATCH_VIP)}",
            )

    # Validate match-vip-only if present
    if "match-vip-only" in payload:
        value = payload.get("match-vip-only")
        if value and value not in VALID_BODY_MATCH_VIP_ONLY:
            return (
                False,
                f"Invalid match-vip-only '{value}'. Must be one of: {', '.join(VALID_BODY_MATCH_VIP_ONLY)}",
            )

    # Validate diffserv-copy if present
    if "diffserv-copy" in payload:
        value = payload.get("diffserv-copy")
        if value and value not in VALID_BODY_DIFFSERV_COPY:
            return (
                False,
                f"Invalid diffserv-copy '{value}'. Must be one of: {', '.join(VALID_BODY_DIFFSERV_COPY)}",
            )

    # Validate diffserv-forward if present
    if "diffserv-forward" in payload:
        value = payload.get("diffserv-forward")
        if value and value not in VALID_BODY_DIFFSERV_FORWARD:
            return (
                False,
                f"Invalid diffserv-forward '{value}'. Must be one of: {', '.join(VALID_BODY_DIFFSERV_FORWARD)}",
            )

    # Validate diffserv-reverse if present
    if "diffserv-reverse" in payload:
        value = payload.get("diffserv-reverse")
        if value and value not in VALID_BODY_DIFFSERV_REVERSE:
            return (
                False,
                f"Invalid diffserv-reverse '{value}'. Must be one of: {', '.join(VALID_BODY_DIFFSERV_REVERSE)}",
            )

    # Validate tcp-mss-sender if present
    if "tcp-mss-sender" in payload:
        value = payload.get("tcp-mss-sender")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 65535:
                    return (
                        False,
                        "tcp-mss-sender must be between 0 and 65535",
                    )
            except (ValueError, TypeError):
                return (False, f"tcp-mss-sender must be numeric, got: {value}")

    # Validate tcp-mss-receiver if present
    if "tcp-mss-receiver" in payload:
        value = payload.get("tcp-mss-receiver")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 65535:
                    return (
                        False,
                        "tcp-mss-receiver must be between 0 and 65535",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"tcp-mss-receiver must be numeric, got: {value}",
                )

    # Validate comments if present
    if "comments" in payload:
        value = payload.get("comments")
        if value and isinstance(value, str) and len(value) > 1023:
            return (False, "comments cannot exceed 1023 characters")

    # Validate auth-cert if present
    if "auth-cert" in payload:
        value = payload.get("auth-cert")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "auth-cert cannot exceed 35 characters")

    # Validate auth-redirect-addr if present
    if "auth-redirect-addr" in payload:
        value = payload.get("auth-redirect-addr")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "auth-redirect-addr cannot exceed 63 characters")

    # Validate redirect-url if present
    if "redirect-url" in payload:
        value = payload.get("redirect-url")
        if value and isinstance(value, str) and len(value) > 1023:
            return (False, "redirect-url cannot exceed 1023 characters")

    # Validate identity-based-route if present
    if "identity-based-route" in payload:
        value = payload.get("identity-based-route")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "identity-based-route cannot exceed 35 characters")

    # Validate block-notification if present
    if "block-notification" in payload:
        value = payload.get("block-notification")
        if value and value not in VALID_BODY_BLOCK_NOTIFICATION:
            return (
                False,
                f"Invalid block-notification '{value}'. Must be one of: {', '.join(VALID_BODY_BLOCK_NOTIFICATION)}",
            )

    # Validate replacemsg-override-group if present
    if "replacemsg-override-group" in payload:
        value = payload.get("replacemsg-override-group")
        if value and isinstance(value, str) and len(value) > 35:
            return (
                False,
                "replacemsg-override-group cannot exceed 35 characters",
            )

    # Validate srcaddr-negate if present
    if "srcaddr-negate" in payload:
        value = payload.get("srcaddr-negate")
        if value and value not in VALID_BODY_SRCADDR_NEGATE:
            return (
                False,
                f"Invalid srcaddr-negate '{value}'. Must be one of: {', '.join(VALID_BODY_SRCADDR_NEGATE)}",
            )

    # Validate srcaddr6-negate if present
    if "srcaddr6-negate" in payload:
        value = payload.get("srcaddr6-negate")
        if value and value not in VALID_BODY_SRCADDR6_NEGATE:
            return (
                False,
                f"Invalid srcaddr6-negate '{value}'. Must be one of: {', '.join(VALID_BODY_SRCADDR6_NEGATE)}",
            )

    # Validate dstaddr-negate if present
    if "dstaddr-negate" in payload:
        value = payload.get("dstaddr-negate")
        if value and value not in VALID_BODY_DSTADDR_NEGATE:
            return (
                False,
                f"Invalid dstaddr-negate '{value}'. Must be one of: {', '.join(VALID_BODY_DSTADDR_NEGATE)}",
            )

    # Validate dstaddr6-negate if present
    if "dstaddr6-negate" in payload:
        value = payload.get("dstaddr6-negate")
        if value and value not in VALID_BODY_DSTADDR6_NEGATE:
            return (
                False,
                f"Invalid dstaddr6-negate '{value}'. Must be one of: {', '.join(VALID_BODY_DSTADDR6_NEGATE)}",
            )

    # Validate ztna-ems-tag-negate if present
    if "ztna-ems-tag-negate" in payload:
        value = payload.get("ztna-ems-tag-negate")
        if value and value not in VALID_BODY_ZTNA_EMS_TAG_NEGATE:
            return (
                False,
                f"Invalid ztna-ems-tag-negate '{value}'. Must be one of: {', '.join(VALID_BODY_ZTNA_EMS_TAG_NEGATE)}",
            )

    # Validate service-negate if present
    if "service-negate" in payload:
        value = payload.get("service-negate")
        if value and value not in VALID_BODY_SERVICE_NEGATE:
            return (
                False,
                f"Invalid service-negate '{value}'. Must be one of: {', '.join(VALID_BODY_SERVICE_NEGATE)}",
            )

    # Validate internet-service-negate if present
    if "internet-service-negate" in payload:
        value = payload.get("internet-service-negate")
        if value and value not in VALID_BODY_INTERNET_SERVICE_NEGATE:
            return (
                False,
                f"Invalid internet-service-negate '{value}'. Must be one of: {', '.join(VALID_BODY_INTERNET_SERVICE_NEGATE)}",
            )

    # Validate internet-service-src-negate if present
    if "internet-service-src-negate" in payload:
        value = payload.get("internet-service-src-negate")
        if value and value not in VALID_BODY_INTERNET_SERVICE_SRC_NEGATE:
            return (
                False,
                f"Invalid internet-service-src-negate '{value}'. Must be one of: {', '.join(VALID_BODY_INTERNET_SERVICE_SRC_NEGATE)}",
            )

    # Validate internet-service6-negate if present
    if "internet-service6-negate" in payload:
        value = payload.get("internet-service6-negate")
        if value and value not in VALID_BODY_INTERNET_SERVICE6_NEGATE:
            return (
                False,
                f"Invalid internet-service6-negate '{value}'. Must be one of: {', '.join(VALID_BODY_INTERNET_SERVICE6_NEGATE)}",
            )

    # Validate internet-service6-src-negate if present
    if "internet-service6-src-negate" in payload:
        value = payload.get("internet-service6-src-negate")
        if value and value not in VALID_BODY_INTERNET_SERVICE6_SRC_NEGATE:
            return (
                False,
                f"Invalid internet-service6-src-negate '{value}'. Must be one of: {', '.join(VALID_BODY_INTERNET_SERVICE6_SRC_NEGATE)}",
            )

    # Validate timeout-send-rst if present
    if "timeout-send-rst" in payload:
        value = payload.get("timeout-send-rst")
        if value and value not in VALID_BODY_TIMEOUT_SEND_RST:
            return (
                False,
                f"Invalid timeout-send-rst '{value}'. Must be one of: {', '.join(VALID_BODY_TIMEOUT_SEND_RST)}",
            )

    # Validate captive-portal-exempt if present
    if "captive-portal-exempt" in payload:
        value = payload.get("captive-portal-exempt")
        if value and value not in VALID_BODY_CAPTIVE_PORTAL_EXEMPT:
            return (
                False,
                f"Invalid captive-portal-exempt '{value}'. Must be one of: {', '.join(VALID_BODY_CAPTIVE_PORTAL_EXEMPT)}",
            )

    # Validate decrypted-traffic-mirror if present
    if "decrypted-traffic-mirror" in payload:
        value = payload.get("decrypted-traffic-mirror")
        if value and isinstance(value, str) and len(value) > 35:
            return (
                False,
                "decrypted-traffic-mirror cannot exceed 35 characters",
            )

    # Validate dsri if present
    if "dsri" in payload:
        value = payload.get("dsri")
        if value and value not in VALID_BODY_DSRI:
            return (
                False,
                f"Invalid dsri '{value}'. Must be one of: {', '.join(VALID_BODY_DSRI)}",
            )

    # Validate radius-mac-auth-bypass if present
    if "radius-mac-auth-bypass" in payload:
        value = payload.get("radius-mac-auth-bypass")
        if value and value not in VALID_BODY_RADIUS_MAC_AUTH_BYPASS:
            return (
                False,
                f"Invalid radius-mac-auth-bypass '{value}'. Must be one of: {', '.join(VALID_BODY_RADIUS_MAC_AUTH_BYPASS)}",
            )

    # Validate radius-ip-auth-bypass if present
    if "radius-ip-auth-bypass" in payload:
        value = payload.get("radius-ip-auth-bypass")
        if value and value not in VALID_BODY_RADIUS_IP_AUTH_BYPASS:
            return (
                False,
                f"Invalid radius-ip-auth-bypass '{value}'. Must be one of: {', '.join(VALID_BODY_RADIUS_IP_AUTH_BYPASS)}",
            )

    # Validate delay-tcp-npu-session if present
    if "delay-tcp-npu-session" in payload:
        value = payload.get("delay-tcp-npu-session")
        if value and value not in VALID_BODY_DELAY_TCP_NPU_SESSION:
            return (
                False,
                f"Invalid delay-tcp-npu-session '{value}'. Must be one of: {', '.join(VALID_BODY_DELAY_TCP_NPU_SESSION)}",
            )

    # Validate sgt-check if present
    if "sgt-check" in payload:
        value = payload.get("sgt-check")
        if value and value not in VALID_BODY_SGT_CHECK:
            return (
                False,
                f"Invalid sgt-check '{value}'. Must be one of: {', '.join(VALID_BODY_SGT_CHECK)}",
            )

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_policy_put(
    policyid: str | None = None, payload: dict[str, Any] | None = None
) -> tuple[bool, str | None]:
    """
    Validate PUT request payload for updating {endpoint_name}.

    Args:
        policyid: Object identifier (required)
        payload: The payload to validate

    Returns:
        Tuple of (is_valid, error_message)
    """
    # policyid is required for updates
    if not policyid:
        return (False, "policyid is required for PUT operation")

    # If no payload provided, nothing to validate
    if not payload:
        return (True, None)

    # Validate policyid if present
    if "policyid" in payload:
        value = payload.get("policyid")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967294:
                    return (
                        False,
                        "policyid must be between 0 and 4294967294",
                    )
            except (ValueError, TypeError):
                return (False, f"policyid must be numeric, got: {value}")

    # Validate status if present
    if "status" in payload:
        value = payload.get("status")
        if value and value not in VALID_BODY_STATUS:
            return (
                False,
                f"Invalid status '{value}'. Must be one of: {', '.join(VALID_BODY_STATUS)}",
            )

    # Validate name if present
    if "name" in payload:
        value = payload.get("name")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "name cannot exceed 35 characters")

    # Validate action if present
    if "action" in payload:
        value = payload.get("action")
        if value and value not in VALID_BODY_ACTION:
            return (
                False,
                f"Invalid action '{value}'. Must be one of: {', '.join(VALID_BODY_ACTION)}",
            )

    # Validate nat64 if present
    if "nat64" in payload:
        value = payload.get("nat64")
        if value and value not in VALID_BODY_NAT64:
            return (
                False,
                f"Invalid nat64 '{value}'. Must be one of: {', '.join(VALID_BODY_NAT64)}",
            )

    # Validate nat46 if present
    if "nat46" in payload:
        value = payload.get("nat46")
        if value and value not in VALID_BODY_NAT46:
            return (
                False,
                f"Invalid nat46 '{value}'. Must be one of: {', '.join(VALID_BODY_NAT46)}",
            )

    # Validate ztna-status if present
    if "ztna-status" in payload:
        value = payload.get("ztna-status")
        if value and value not in VALID_BODY_ZTNA_STATUS:
            return (
                False,
                f"Invalid ztna-status '{value}'. Must be one of: {', '.join(VALID_BODY_ZTNA_STATUS)}",
            )

    # Validate ztna-device-ownership if present
    if "ztna-device-ownership" in payload:
        value = payload.get("ztna-device-ownership")
        if value and value not in VALID_BODY_ZTNA_DEVICE_OWNERSHIP:
            return (
                False,
                f"Invalid ztna-device-ownership '{value}'. Must be one of: {', '.join(VALID_BODY_ZTNA_DEVICE_OWNERSHIP)}",
            )

    # Validate ztna-tags-match-logic if present
    if "ztna-tags-match-logic" in payload:
        value = payload.get("ztna-tags-match-logic")
        if value and value not in VALID_BODY_ZTNA_TAGS_MATCH_LOGIC:
            return (
                False,
                f"Invalid ztna-tags-match-logic '{value}'. Must be one of: {', '.join(VALID_BODY_ZTNA_TAGS_MATCH_LOGIC)}",
            )

    # Validate internet-service if present
    if "internet-service" in payload:
        value = payload.get("internet-service")
        if value and value not in VALID_BODY_INTERNET_SERVICE:
            return (
                False,
                f"Invalid internet-service '{value}'. Must be one of: {', '.join(VALID_BODY_INTERNET_SERVICE)}",
            )

    # Validate internet-service-src if present
    if "internet-service-src" in payload:
        value = payload.get("internet-service-src")
        if value and value not in VALID_BODY_INTERNET_SERVICE_SRC:
            return (
                False,
                f"Invalid internet-service-src '{value}'. Must be one of: {', '.join(VALID_BODY_INTERNET_SERVICE_SRC)}",
            )

    # Validate reputation-minimum if present
    if "reputation-minimum" in payload:
        value = payload.get("reputation-minimum")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "reputation-minimum must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"reputation-minimum must be numeric, got: {value}",
                )

    # Validate reputation-direction if present
    if "reputation-direction" in payload:
        value = payload.get("reputation-direction")
        if value and value not in VALID_BODY_REPUTATION_DIRECTION:
            return (
                False,
                f"Invalid reputation-direction '{value}'. Must be one of: {', '.join(VALID_BODY_REPUTATION_DIRECTION)}",
            )

    # Validate internet-service6 if present
    if "internet-service6" in payload:
        value = payload.get("internet-service6")
        if value and value not in VALID_BODY_INTERNET_SERVICE6:
            return (
                False,
                f"Invalid internet-service6 '{value}'. Must be one of: {', '.join(VALID_BODY_INTERNET_SERVICE6)}",
            )

    # Validate internet-service6-src if present
    if "internet-service6-src" in payload:
        value = payload.get("internet-service6-src")
        if value and value not in VALID_BODY_INTERNET_SERVICE6_SRC:
            return (
                False,
                f"Invalid internet-service6-src '{value}'. Must be one of: {', '.join(VALID_BODY_INTERNET_SERVICE6_SRC)}",
            )

    # Validate reputation-minimum6 if present
    if "reputation-minimum6" in payload:
        value = payload.get("reputation-minimum6")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "reputation-minimum6 must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"reputation-minimum6 must be numeric, got: {value}",
                )

    # Validate reputation-direction6 if present
    if "reputation-direction6" in payload:
        value = payload.get("reputation-direction6")
        if value and value not in VALID_BODY_REPUTATION_DIRECTION6:
            return (
                False,
                f"Invalid reputation-direction6 '{value}'. Must be one of: {', '.join(VALID_BODY_REPUTATION_DIRECTION6)}",
            )

    # Validate rtp-nat if present
    if "rtp-nat" in payload:
        value = payload.get("rtp-nat")
        if value and value not in VALID_BODY_RTP_NAT:
            return (
                False,
                f"Invalid rtp-nat '{value}'. Must be one of: {', '.join(VALID_BODY_RTP_NAT)}",
            )

    # Validate send-deny-packet if present
    if "send-deny-packet" in payload:
        value = payload.get("send-deny-packet")
        if value and value not in VALID_BODY_SEND_DENY_PACKET:
            return (
                False,
                f"Invalid send-deny-packet '{value}'. Must be one of: {', '.join(VALID_BODY_SEND_DENY_PACKET)}",
            )

    # Validate firewall-session-dirty if present
    if "firewall-session-dirty" in payload:
        value = payload.get("firewall-session-dirty")
        if value and value not in VALID_BODY_FIREWALL_SESSION_DIRTY:
            return (
                False,
                f"Invalid firewall-session-dirty '{value}'. Must be one of: {', '.join(VALID_BODY_FIREWALL_SESSION_DIRTY)}",
            )

    # Validate schedule if present
    if "schedule" in payload:
        value = payload.get("schedule")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "schedule cannot exceed 35 characters")

    # Validate schedule-timeout if present
    if "schedule-timeout" in payload:
        value = payload.get("schedule-timeout")
        if value and value not in VALID_BODY_SCHEDULE_TIMEOUT:
            return (
                False,
                f"Invalid schedule-timeout '{value}'. Must be one of: {', '.join(VALID_BODY_SCHEDULE_TIMEOUT)}",
            )

    # Validate policy-expiry if present
    if "policy-expiry" in payload:
        value = payload.get("policy-expiry")
        if value and value not in VALID_BODY_POLICY_EXPIRY:
            return (
                False,
                f"Invalid policy-expiry '{value}'. Must be one of: {', '.join(VALID_BODY_POLICY_EXPIRY)}",
            )

    # Validate tos-negate if present
    if "tos-negate" in payload:
        value = payload.get("tos-negate")
        if value and value not in VALID_BODY_TOS_NEGATE:
            return (
                False,
                f"Invalid tos-negate '{value}'. Must be one of: {', '.join(VALID_BODY_TOS_NEGATE)}",
            )

    # Validate anti-replay if present
    if "anti-replay" in payload:
        value = payload.get("anti-replay")
        if value and value not in VALID_BODY_ANTI_REPLAY:
            return (
                False,
                f"Invalid anti-replay '{value}'. Must be one of: {', '.join(VALID_BODY_ANTI_REPLAY)}",
            )

    # Validate tcp-session-without-syn if present
    if "tcp-session-without-syn" in payload:
        value = payload.get("tcp-session-without-syn")
        if value and value not in VALID_BODY_TCP_SESSION_WITHOUT_SYN:
            return (
                False,
                f"Invalid tcp-session-without-syn '{value}'. Must be one of: {', '.join(VALID_BODY_TCP_SESSION_WITHOUT_SYN)}",
            )

    # Validate geoip-anycast if present
    if "geoip-anycast" in payload:
        value = payload.get("geoip-anycast")
        if value and value not in VALID_BODY_GEOIP_ANYCAST:
            return (
                False,
                f"Invalid geoip-anycast '{value}'. Must be one of: {', '.join(VALID_BODY_GEOIP_ANYCAST)}",
            )

    # Validate geoip-match if present
    if "geoip-match" in payload:
        value = payload.get("geoip-match")
        if value and value not in VALID_BODY_GEOIP_MATCH:
            return (
                False,
                f"Invalid geoip-match '{value}'. Must be one of: {', '.join(VALID_BODY_GEOIP_MATCH)}",
            )

    # Validate dynamic-shaping if present
    if "dynamic-shaping" in payload:
        value = payload.get("dynamic-shaping")
        if value and value not in VALID_BODY_DYNAMIC_SHAPING:
            return (
                False,
                f"Invalid dynamic-shaping '{value}'. Must be one of: {', '.join(VALID_BODY_DYNAMIC_SHAPING)}",
            )

    # Validate passive-wan-health-measurement if present
    if "passive-wan-health-measurement" in payload:
        value = payload.get("passive-wan-health-measurement")
        if value and value not in VALID_BODY_PASSIVE_WAN_HEALTH_MEASUREMENT:
            return (
                False,
                f"Invalid passive-wan-health-measurement '{value}'. Must be one of: {', '.join(VALID_BODY_PASSIVE_WAN_HEALTH_MEASUREMENT)}",
            )

    # Validate app-monitor if present
    if "app-monitor" in payload:
        value = payload.get("app-monitor")
        if value and value not in VALID_BODY_APP_MONITOR:
            return (
                False,
                f"Invalid app-monitor '{value}'. Must be one of: {', '.join(VALID_BODY_APP_MONITOR)}",
            )

    # Validate utm-status if present
    if "utm-status" in payload:
        value = payload.get("utm-status")
        if value and value not in VALID_BODY_UTM_STATUS:
            return (
                False,
                f"Invalid utm-status '{value}'. Must be one of: {', '.join(VALID_BODY_UTM_STATUS)}",
            )

    # Validate inspection-mode if present
    if "inspection-mode" in payload:
        value = payload.get("inspection-mode")
        if value and value not in VALID_BODY_INSPECTION_MODE:
            return (
                False,
                f"Invalid inspection-mode '{value}'. Must be one of: {', '.join(VALID_BODY_INSPECTION_MODE)}",
            )

    # Validate http-policy-redirect if present
    if "http-policy-redirect" in payload:
        value = payload.get("http-policy-redirect")
        if value and value not in VALID_BODY_HTTP_POLICY_REDIRECT:
            return (
                False,
                f"Invalid http-policy-redirect '{value}'. Must be one of: {', '.join(VALID_BODY_HTTP_POLICY_REDIRECT)}",
            )

    # Validate ssh-policy-redirect if present
    if "ssh-policy-redirect" in payload:
        value = payload.get("ssh-policy-redirect")
        if value and value not in VALID_BODY_SSH_POLICY_REDIRECT:
            return (
                False,
                f"Invalid ssh-policy-redirect '{value}'. Must be one of: {', '.join(VALID_BODY_SSH_POLICY_REDIRECT)}",
            )

    # Validate ztna-policy-redirect if present
    if "ztna-policy-redirect" in payload:
        value = payload.get("ztna-policy-redirect")
        if value and value not in VALID_BODY_ZTNA_POLICY_REDIRECT:
            return (
                False,
                f"Invalid ztna-policy-redirect '{value}'. Must be one of: {', '.join(VALID_BODY_ZTNA_POLICY_REDIRECT)}",
            )

    # Validate webproxy-profile if present
    if "webproxy-profile" in payload:
        value = payload.get("webproxy-profile")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "webproxy-profile cannot exceed 63 characters")

    # Validate profile-type if present
    if "profile-type" in payload:
        value = payload.get("profile-type")
        if value and value not in VALID_BODY_PROFILE_TYPE:
            return (
                False,
                f"Invalid profile-type '{value}'. Must be one of: {', '.join(VALID_BODY_PROFILE_TYPE)}",
            )

    # Validate profile-group if present
    if "profile-group" in payload:
        value = payload.get("profile-group")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "profile-group cannot exceed 47 characters")

    # Validate profile-protocol-options if present
    if "profile-protocol-options" in payload:
        value = payload.get("profile-protocol-options")
        if value and isinstance(value, str) and len(value) > 47:
            return (
                False,
                "profile-protocol-options cannot exceed 47 characters",
            )

    # Validate ssl-ssh-profile if present
    if "ssl-ssh-profile" in payload:
        value = payload.get("ssl-ssh-profile")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "ssl-ssh-profile cannot exceed 47 characters")

    # Validate av-profile if present
    if "av-profile" in payload:
        value = payload.get("av-profile")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "av-profile cannot exceed 47 characters")

    # Validate webfilter-profile if present
    if "webfilter-profile" in payload:
        value = payload.get("webfilter-profile")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "webfilter-profile cannot exceed 47 characters")

    # Validate dnsfilter-profile if present
    if "dnsfilter-profile" in payload:
        value = payload.get("dnsfilter-profile")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "dnsfilter-profile cannot exceed 47 characters")

    # Validate emailfilter-profile if present
    if "emailfilter-profile" in payload:
        value = payload.get("emailfilter-profile")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "emailfilter-profile cannot exceed 47 characters")

    # Validate dlp-profile if present
    if "dlp-profile" in payload:
        value = payload.get("dlp-profile")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "dlp-profile cannot exceed 47 characters")

    # Validate file-filter-profile if present
    if "file-filter-profile" in payload:
        value = payload.get("file-filter-profile")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "file-filter-profile cannot exceed 47 characters")

    # Validate ips-sensor if present
    if "ips-sensor" in payload:
        value = payload.get("ips-sensor")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "ips-sensor cannot exceed 47 characters")

    # Validate application-list if present
    if "application-list" in payload:
        value = payload.get("application-list")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "application-list cannot exceed 47 characters")

    # Validate voip-profile if present
    if "voip-profile" in payload:
        value = payload.get("voip-profile")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "voip-profile cannot exceed 47 characters")

    # Validate ips-voip-filter if present
    if "ips-voip-filter" in payload:
        value = payload.get("ips-voip-filter")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "ips-voip-filter cannot exceed 47 characters")

    # Validate sctp-filter-profile if present
    if "sctp-filter-profile" in payload:
        value = payload.get("sctp-filter-profile")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "sctp-filter-profile cannot exceed 47 characters")

    # Validate diameter-filter-profile if present
    if "diameter-filter-profile" in payload:
        value = payload.get("diameter-filter-profile")
        if value and isinstance(value, str) and len(value) > 47:
            return (
                False,
                "diameter-filter-profile cannot exceed 47 characters",
            )

    # Validate virtual-patch-profile if present
    if "virtual-patch-profile" in payload:
        value = payload.get("virtual-patch-profile")
        if value and isinstance(value, str) and len(value) > 47:
            return (
                False,
                "virtual-patch-profile cannot exceed 47 characters",
            )

    # Validate icap-profile if present
    if "icap-profile" in payload:
        value = payload.get("icap-profile")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "icap-profile cannot exceed 47 characters")

    # Validate videofilter-profile if present
    if "videofilter-profile" in payload:
        value = payload.get("videofilter-profile")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "videofilter-profile cannot exceed 47 characters")

    # Validate waf-profile if present
    if "waf-profile" in payload:
        value = payload.get("waf-profile")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "waf-profile cannot exceed 47 characters")

    # Validate ssh-filter-profile if present
    if "ssh-filter-profile" in payload:
        value = payload.get("ssh-filter-profile")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "ssh-filter-profile cannot exceed 47 characters")

    # Validate casb-profile if present
    if "casb-profile" in payload:
        value = payload.get("casb-profile")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "casb-profile cannot exceed 47 characters")

    # Validate logtraffic if present
    if "logtraffic" in payload:
        value = payload.get("logtraffic")
        if value and value not in VALID_BODY_LOGTRAFFIC:
            return (
                False,
                f"Invalid logtraffic '{value}'. Must be one of: {', '.join(VALID_BODY_LOGTRAFFIC)}",
            )

    # Validate logtraffic-start if present
    if "logtraffic-start" in payload:
        value = payload.get("logtraffic-start")
        if value and value not in VALID_BODY_LOGTRAFFIC_START:
            return (
                False,
                f"Invalid logtraffic-start '{value}'. Must be one of: {', '.join(VALID_BODY_LOGTRAFFIC_START)}",
            )

    # Validate log-http-transaction if present
    if "log-http-transaction" in payload:
        value = payload.get("log-http-transaction")
        if value and value not in VALID_BODY_LOG_HTTP_TRANSACTION:
            return (
                False,
                f"Invalid log-http-transaction '{value}'. Must be one of: {', '.join(VALID_BODY_LOG_HTTP_TRANSACTION)}",
            )

    # Validate capture-packet if present
    if "capture-packet" in payload:
        value = payload.get("capture-packet")
        if value and value not in VALID_BODY_CAPTURE_PACKET:
            return (
                False,
                f"Invalid capture-packet '{value}'. Must be one of: {', '.join(VALID_BODY_CAPTURE_PACKET)}",
            )

    # Validate auto-asic-offload if present
    if "auto-asic-offload" in payload:
        value = payload.get("auto-asic-offload")
        if value and value not in VALID_BODY_AUTO_ASIC_OFFLOAD:
            return (
                False,
                f"Invalid auto-asic-offload '{value}'. Must be one of: {', '.join(VALID_BODY_AUTO_ASIC_OFFLOAD)}",
            )

    # Validate np-acceleration if present
    if "np-acceleration" in payload:
        value = payload.get("np-acceleration")
        if value and value not in VALID_BODY_NP_ACCELERATION:
            return (
                False,
                f"Invalid np-acceleration '{value}'. Must be one of: {', '.join(VALID_BODY_NP_ACCELERATION)}",
            )

    # Validate webproxy-forward-server if present
    if "webproxy-forward-server" in payload:
        value = payload.get("webproxy-forward-server")
        if value and isinstance(value, str) and len(value) > 63:
            return (
                False,
                "webproxy-forward-server cannot exceed 63 characters",
            )

    # Validate traffic-shaper if present
    if "traffic-shaper" in payload:
        value = payload.get("traffic-shaper")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "traffic-shaper cannot exceed 35 characters")

    # Validate traffic-shaper-reverse if present
    if "traffic-shaper-reverse" in payload:
        value = payload.get("traffic-shaper-reverse")
        if value and isinstance(value, str) and len(value) > 35:
            return (
                False,
                "traffic-shaper-reverse cannot exceed 35 characters",
            )

    # Validate per-ip-shaper if present
    if "per-ip-shaper" in payload:
        value = payload.get("per-ip-shaper")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "per-ip-shaper cannot exceed 35 characters")

    # Validate nat if present
    if "nat" in payload:
        value = payload.get("nat")
        if value and value not in VALID_BODY_NAT:
            return (
                False,
                f"Invalid nat '{value}'. Must be one of: {', '.join(VALID_BODY_NAT)}",
            )

    # Validate pcp-outbound if present
    if "pcp-outbound" in payload:
        value = payload.get("pcp-outbound")
        if value and value not in VALID_BODY_PCP_OUTBOUND:
            return (
                False,
                f"Invalid pcp-outbound '{value}'. Must be one of: {', '.join(VALID_BODY_PCP_OUTBOUND)}",
            )

    # Validate pcp-inbound if present
    if "pcp-inbound" in payload:
        value = payload.get("pcp-inbound")
        if value and value not in VALID_BODY_PCP_INBOUND:
            return (
                False,
                f"Invalid pcp-inbound '{value}'. Must be one of: {', '.join(VALID_BODY_PCP_INBOUND)}",
            )

    # Validate permit-any-host if present
    if "permit-any-host" in payload:
        value = payload.get("permit-any-host")
        if value and value not in VALID_BODY_PERMIT_ANY_HOST:
            return (
                False,
                f"Invalid permit-any-host '{value}'. Must be one of: {', '.join(VALID_BODY_PERMIT_ANY_HOST)}",
            )

    # Validate permit-stun-host if present
    if "permit-stun-host" in payload:
        value = payload.get("permit-stun-host")
        if value and value not in VALID_BODY_PERMIT_STUN_HOST:
            return (
                False,
                f"Invalid permit-stun-host '{value}'. Must be one of: {', '.join(VALID_BODY_PERMIT_STUN_HOST)}",
            )

    # Validate fixedport if present
    if "fixedport" in payload:
        value = payload.get("fixedport")
        if value and value not in VALID_BODY_FIXEDPORT:
            return (
                False,
                f"Invalid fixedport '{value}'. Must be one of: {', '.join(VALID_BODY_FIXEDPORT)}",
            )

    # Validate port-preserve if present
    if "port-preserve" in payload:
        value = payload.get("port-preserve")
        if value and value not in VALID_BODY_PORT_PRESERVE:
            return (
                False,
                f"Invalid port-preserve '{value}'. Must be one of: {', '.join(VALID_BODY_PORT_PRESERVE)}",
            )

    # Validate port-random if present
    if "port-random" in payload:
        value = payload.get("port-random")
        if value and value not in VALID_BODY_PORT_RANDOM:
            return (
                False,
                f"Invalid port-random '{value}'. Must be one of: {', '.join(VALID_BODY_PORT_RANDOM)}",
            )

    # Validate ippool if present
    if "ippool" in payload:
        value = payload.get("ippool")
        if value and value not in VALID_BODY_IPPOOL:
            return (
                False,
                f"Invalid ippool '{value}'. Must be one of: {', '.join(VALID_BODY_IPPOOL)}",
            )

    # Validate vlan-cos-fwd if present
    if "vlan-cos-fwd" in payload:
        value = payload.get("vlan-cos-fwd")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 7:
                    return (False, "vlan-cos-fwd must be between 0 and 7")
            except (ValueError, TypeError):
                return (False, f"vlan-cos-fwd must be numeric, got: {value}")

    # Validate vlan-cos-rev if present
    if "vlan-cos-rev" in payload:
        value = payload.get("vlan-cos-rev")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 7:
                    return (False, "vlan-cos-rev must be between 0 and 7")
            except (ValueError, TypeError):
                return (False, f"vlan-cos-rev must be numeric, got: {value}")

    # Validate inbound if present
    if "inbound" in payload:
        value = payload.get("inbound")
        if value and value not in VALID_BODY_INBOUND:
            return (
                False,
                f"Invalid inbound '{value}'. Must be one of: {', '.join(VALID_BODY_INBOUND)}",
            )

    # Validate outbound if present
    if "outbound" in payload:
        value = payload.get("outbound")
        if value and value not in VALID_BODY_OUTBOUND:
            return (
                False,
                f"Invalid outbound '{value}'. Must be one of: {', '.join(VALID_BODY_OUTBOUND)}",
            )

    # Validate natinbound if present
    if "natinbound" in payload:
        value = payload.get("natinbound")
        if value and value not in VALID_BODY_NATINBOUND:
            return (
                False,
                f"Invalid natinbound '{value}'. Must be one of: {', '.join(VALID_BODY_NATINBOUND)}",
            )

    # Validate natoutbound if present
    if "natoutbound" in payload:
        value = payload.get("natoutbound")
        if value and value not in VALID_BODY_NATOUTBOUND:
            return (
                False,
                f"Invalid natoutbound '{value}'. Must be one of: {', '.join(VALID_BODY_NATOUTBOUND)}",
            )

    # Validate fec if present
    if "fec" in payload:
        value = payload.get("fec")
        if value and value not in VALID_BODY_FEC:
            return (
                False,
                f"Invalid fec '{value}'. Must be one of: {', '.join(VALID_BODY_FEC)}",
            )

    # Validate wccp if present
    if "wccp" in payload:
        value = payload.get("wccp")
        if value and value not in VALID_BODY_WCCP:
            return (
                False,
                f"Invalid wccp '{value}'. Must be one of: {', '.join(VALID_BODY_WCCP)}",
            )

    # Validate ntlm if present
    if "ntlm" in payload:
        value = payload.get("ntlm")
        if value and value not in VALID_BODY_NTLM:
            return (
                False,
                f"Invalid ntlm '{value}'. Must be one of: {', '.join(VALID_BODY_NTLM)}",
            )

    # Validate ntlm-guest if present
    if "ntlm-guest" in payload:
        value = payload.get("ntlm-guest")
        if value and value not in VALID_BODY_NTLM_GUEST:
            return (
                False,
                f"Invalid ntlm-guest '{value}'. Must be one of: {', '.join(VALID_BODY_NTLM_GUEST)}",
            )

    # Validate fsso-agent-for-ntlm if present
    if "fsso-agent-for-ntlm" in payload:
        value = payload.get("fsso-agent-for-ntlm")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "fsso-agent-for-ntlm cannot exceed 35 characters")

    # Validate auth-path if present
    if "auth-path" in payload:
        value = payload.get("auth-path")
        if value and value not in VALID_BODY_AUTH_PATH:
            return (
                False,
                f"Invalid auth-path '{value}'. Must be one of: {', '.join(VALID_BODY_AUTH_PATH)}",
            )

    # Validate disclaimer if present
    if "disclaimer" in payload:
        value = payload.get("disclaimer")
        if value and value not in VALID_BODY_DISCLAIMER:
            return (
                False,
                f"Invalid disclaimer '{value}'. Must be one of: {', '.join(VALID_BODY_DISCLAIMER)}",
            )

    # Validate email-collect if present
    if "email-collect" in payload:
        value = payload.get("email-collect")
        if value and value not in VALID_BODY_EMAIL_COLLECT:
            return (
                False,
                f"Invalid email-collect '{value}'. Must be one of: {', '.join(VALID_BODY_EMAIL_COLLECT)}",
            )

    # Validate vpntunnel if present
    if "vpntunnel" in payload:
        value = payload.get("vpntunnel")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "vpntunnel cannot exceed 35 characters")

    # Validate match-vip if present
    if "match-vip" in payload:
        value = payload.get("match-vip")
        if value and value not in VALID_BODY_MATCH_VIP:
            return (
                False,
                f"Invalid match-vip '{value}'. Must be one of: {', '.join(VALID_BODY_MATCH_VIP)}",
            )

    # Validate match-vip-only if present
    if "match-vip-only" in payload:
        value = payload.get("match-vip-only")
        if value and value not in VALID_BODY_MATCH_VIP_ONLY:
            return (
                False,
                f"Invalid match-vip-only '{value}'. Must be one of: {', '.join(VALID_BODY_MATCH_VIP_ONLY)}",
            )

    # Validate diffserv-copy if present
    if "diffserv-copy" in payload:
        value = payload.get("diffserv-copy")
        if value and value not in VALID_BODY_DIFFSERV_COPY:
            return (
                False,
                f"Invalid diffserv-copy '{value}'. Must be one of: {', '.join(VALID_BODY_DIFFSERV_COPY)}",
            )

    # Validate diffserv-forward if present
    if "diffserv-forward" in payload:
        value = payload.get("diffserv-forward")
        if value and value not in VALID_BODY_DIFFSERV_FORWARD:
            return (
                False,
                f"Invalid diffserv-forward '{value}'. Must be one of: {', '.join(VALID_BODY_DIFFSERV_FORWARD)}",
            )

    # Validate diffserv-reverse if present
    if "diffserv-reverse" in payload:
        value = payload.get("diffserv-reverse")
        if value and value not in VALID_BODY_DIFFSERV_REVERSE:
            return (
                False,
                f"Invalid diffserv-reverse '{value}'. Must be one of: {', '.join(VALID_BODY_DIFFSERV_REVERSE)}",
            )

    # Validate tcp-mss-sender if present
    if "tcp-mss-sender" in payload:
        value = payload.get("tcp-mss-sender")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 65535:
                    return (
                        False,
                        "tcp-mss-sender must be between 0 and 65535",
                    )
            except (ValueError, TypeError):
                return (False, f"tcp-mss-sender must be numeric, got: {value}")

    # Validate tcp-mss-receiver if present
    if "tcp-mss-receiver" in payload:
        value = payload.get("tcp-mss-receiver")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 65535:
                    return (
                        False,
                        "tcp-mss-receiver must be between 0 and 65535",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"tcp-mss-receiver must be numeric, got: {value}",
                )

    # Validate comments if present
    if "comments" in payload:
        value = payload.get("comments")
        if value and isinstance(value, str) and len(value) > 1023:
            return (False, "comments cannot exceed 1023 characters")

    # Validate auth-cert if present
    if "auth-cert" in payload:
        value = payload.get("auth-cert")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "auth-cert cannot exceed 35 characters")

    # Validate auth-redirect-addr if present
    if "auth-redirect-addr" in payload:
        value = payload.get("auth-redirect-addr")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "auth-redirect-addr cannot exceed 63 characters")

    # Validate redirect-url if present
    if "redirect-url" in payload:
        value = payload.get("redirect-url")
        if value and isinstance(value, str) and len(value) > 1023:
            return (False, "redirect-url cannot exceed 1023 characters")

    # Validate identity-based-route if present
    if "identity-based-route" in payload:
        value = payload.get("identity-based-route")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "identity-based-route cannot exceed 35 characters")

    # Validate block-notification if present
    if "block-notification" in payload:
        value = payload.get("block-notification")
        if value and value not in VALID_BODY_BLOCK_NOTIFICATION:
            return (
                False,
                f"Invalid block-notification '{value}'. Must be one of: {', '.join(VALID_BODY_BLOCK_NOTIFICATION)}",
            )

    # Validate replacemsg-override-group if present
    if "replacemsg-override-group" in payload:
        value = payload.get("replacemsg-override-group")
        if value and isinstance(value, str) and len(value) > 35:
            return (
                False,
                "replacemsg-override-group cannot exceed 35 characters",
            )

    # Validate srcaddr-negate if present
    if "srcaddr-negate" in payload:
        value = payload.get("srcaddr-negate")
        if value and value not in VALID_BODY_SRCADDR_NEGATE:
            return (
                False,
                f"Invalid srcaddr-negate '{value}'. Must be one of: {', '.join(VALID_BODY_SRCADDR_NEGATE)}",
            )

    # Validate srcaddr6-negate if present
    if "srcaddr6-negate" in payload:
        value = payload.get("srcaddr6-negate")
        if value and value not in VALID_BODY_SRCADDR6_NEGATE:
            return (
                False,
                f"Invalid srcaddr6-negate '{value}'. Must be one of: {', '.join(VALID_BODY_SRCADDR6_NEGATE)}",
            )

    # Validate dstaddr-negate if present
    if "dstaddr-negate" in payload:
        value = payload.get("dstaddr-negate")
        if value and value not in VALID_BODY_DSTADDR_NEGATE:
            return (
                False,
                f"Invalid dstaddr-negate '{value}'. Must be one of: {', '.join(VALID_BODY_DSTADDR_NEGATE)}",
            )

    # Validate dstaddr6-negate if present
    if "dstaddr6-negate" in payload:
        value = payload.get("dstaddr6-negate")
        if value and value not in VALID_BODY_DSTADDR6_NEGATE:
            return (
                False,
                f"Invalid dstaddr6-negate '{value}'. Must be one of: {', '.join(VALID_BODY_DSTADDR6_NEGATE)}",
            )

    # Validate ztna-ems-tag-negate if present
    if "ztna-ems-tag-negate" in payload:
        value = payload.get("ztna-ems-tag-negate")
        if value and value not in VALID_BODY_ZTNA_EMS_TAG_NEGATE:
            return (
                False,
                f"Invalid ztna-ems-tag-negate '{value}'. Must be one of: {', '.join(VALID_BODY_ZTNA_EMS_TAG_NEGATE)}",
            )

    # Validate service-negate if present
    if "service-negate" in payload:
        value = payload.get("service-negate")
        if value and value not in VALID_BODY_SERVICE_NEGATE:
            return (
                False,
                f"Invalid service-negate '{value}'. Must be one of: {', '.join(VALID_BODY_SERVICE_NEGATE)}",
            )

    # Validate internet-service-negate if present
    if "internet-service-negate" in payload:
        value = payload.get("internet-service-negate")
        if value and value not in VALID_BODY_INTERNET_SERVICE_NEGATE:
            return (
                False,
                f"Invalid internet-service-negate '{value}'. Must be one of: {', '.join(VALID_BODY_INTERNET_SERVICE_NEGATE)}",
            )

    # Validate internet-service-src-negate if present
    if "internet-service-src-negate" in payload:
        value = payload.get("internet-service-src-negate")
        if value and value not in VALID_BODY_INTERNET_SERVICE_SRC_NEGATE:
            return (
                False,
                f"Invalid internet-service-src-negate '{value}'. Must be one of: {', '.join(VALID_BODY_INTERNET_SERVICE_SRC_NEGATE)}",
            )

    # Validate internet-service6-negate if present
    if "internet-service6-negate" in payload:
        value = payload.get("internet-service6-negate")
        if value and value not in VALID_BODY_INTERNET_SERVICE6_NEGATE:
            return (
                False,
                f"Invalid internet-service6-negate '{value}'. Must be one of: {', '.join(VALID_BODY_INTERNET_SERVICE6_NEGATE)}",
            )

    # Validate internet-service6-src-negate if present
    if "internet-service6-src-negate" in payload:
        value = payload.get("internet-service6-src-negate")
        if value and value not in VALID_BODY_INTERNET_SERVICE6_SRC_NEGATE:
            return (
                False,
                f"Invalid internet-service6-src-negate '{value}'. Must be one of: {', '.join(VALID_BODY_INTERNET_SERVICE6_SRC_NEGATE)}",
            )

    # Validate timeout-send-rst if present
    if "timeout-send-rst" in payload:
        value = payload.get("timeout-send-rst")
        if value and value not in VALID_BODY_TIMEOUT_SEND_RST:
            return (
                False,
                f"Invalid timeout-send-rst '{value}'. Must be one of: {', '.join(VALID_BODY_TIMEOUT_SEND_RST)}",
            )

    # Validate captive-portal-exempt if present
    if "captive-portal-exempt" in payload:
        value = payload.get("captive-portal-exempt")
        if value and value not in VALID_BODY_CAPTIVE_PORTAL_EXEMPT:
            return (
                False,
                f"Invalid captive-portal-exempt '{value}'. Must be one of: {', '.join(VALID_BODY_CAPTIVE_PORTAL_EXEMPT)}",
            )

    # Validate decrypted-traffic-mirror if present
    if "decrypted-traffic-mirror" in payload:
        value = payload.get("decrypted-traffic-mirror")
        if value and isinstance(value, str) and len(value) > 35:
            return (
                False,
                "decrypted-traffic-mirror cannot exceed 35 characters",
            )

    # Validate dsri if present
    if "dsri" in payload:
        value = payload.get("dsri")
        if value and value not in VALID_BODY_DSRI:
            return (
                False,
                f"Invalid dsri '{value}'. Must be one of: {', '.join(VALID_BODY_DSRI)}",
            )

    # Validate radius-mac-auth-bypass if present
    if "radius-mac-auth-bypass" in payload:
        value = payload.get("radius-mac-auth-bypass")
        if value and value not in VALID_BODY_RADIUS_MAC_AUTH_BYPASS:
            return (
                False,
                f"Invalid radius-mac-auth-bypass '{value}'. Must be one of: {', '.join(VALID_BODY_RADIUS_MAC_AUTH_BYPASS)}",
            )

    # Validate radius-ip-auth-bypass if present
    if "radius-ip-auth-bypass" in payload:
        value = payload.get("radius-ip-auth-bypass")
        if value and value not in VALID_BODY_RADIUS_IP_AUTH_BYPASS:
            return (
                False,
                f"Invalid radius-ip-auth-bypass '{value}'. Must be one of: {', '.join(VALID_BODY_RADIUS_IP_AUTH_BYPASS)}",
            )

    # Validate delay-tcp-npu-session if present
    if "delay-tcp-npu-session" in payload:
        value = payload.get("delay-tcp-npu-session")
        if value and value not in VALID_BODY_DELAY_TCP_NPU_SESSION:
            return (
                False,
                f"Invalid delay-tcp-npu-session '{value}'. Must be one of: {', '.join(VALID_BODY_DELAY_TCP_NPU_SESSION)}",
            )

    # Validate sgt-check if present
    if "sgt-check" in payload:
        value = payload.get("sgt-check")
        if value and value not in VALID_BODY_SGT_CHECK:
            return (
                False,
                f"Invalid sgt-check '{value}'. Must be one of: {', '.join(VALID_BODY_SGT_CHECK)}",
            )

    return (True, None)


# ============================================================================
# DELETE Validation
# ============================================================================


def validate_policy_delete(
    policyid: str | None = None,
) -> tuple[bool, str | None]:
    """
    Validate DELETE request parameters.

    Args:
        policyid: Object identifier (required)

    Returns:
        Tuple of (is_valid, error_message)
    """
    if not policyid:
        return (False, "policyid is required for DELETE operation")

    return (True, None)
