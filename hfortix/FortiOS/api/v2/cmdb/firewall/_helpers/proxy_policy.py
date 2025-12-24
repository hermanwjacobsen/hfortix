"""
Validation helpers for firewall proxy_policy endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_PROXY = [
    "explicit-web",
    "transparent-web",
    "ftp",
    "ssh",
    "ssh-tunnel",
    "access-proxy",
    "ztna-proxy",
]
VALID_BODY_ZTNA_TAGS_MATCH_LOGIC = ["or", "and"]
VALID_BODY_DEVICE_OWNERSHIP = ["enable", "disable"]
VALID_BODY_INTERNET_SERVICE = ["enable", "disable"]
VALID_BODY_INTERNET_SERVICE_NEGATE = ["enable", "disable"]
VALID_BODY_INTERNET_SERVICE6 = ["enable", "disable"]
VALID_BODY_INTERNET_SERVICE6_NEGATE = ["enable", "disable"]
VALID_BODY_SRCADDR_NEGATE = ["enable", "disable"]
VALID_BODY_DSTADDR_NEGATE = ["enable", "disable"]
VALID_BODY_ZTNA_EMS_TAG_NEGATE = ["enable", "disable"]
VALID_BODY_SERVICE_NEGATE = ["enable", "disable"]
VALID_BODY_ACTION = ["accept", "deny", "redirect", "isolate"]
VALID_BODY_STATUS = ["enable", "disable"]
VALID_BODY_LOGTRAFFIC = ["all", "utm", "disable"]
VALID_BODY_HTTP_TUNNEL_AUTH = ["enable", "disable"]
VALID_BODY_SSH_POLICY_REDIRECT = ["enable", "disable"]
VALID_BODY_TRANSPARENT = ["enable", "disable"]
VALID_BODY_DISCLAIMER = ["disable", "domain", "policy", "user"]
VALID_BODY_UTM_STATUS = ["enable", "disable"]
VALID_BODY_PROFILE_TYPE = ["single", "group"]
VALID_BODY_LOGTRAFFIC_START = ["enable", "disable"]
VALID_BODY_LOG_HTTP_TRANSACTION = ["enable", "disable"]
VALID_BODY_BLOCK_NOTIFICATION = ["enable", "disable"]
VALID_BODY_HTTPS_SUB_CATEGORY = ["enable", "disable"]
VALID_BODY_DETECT_HTTPS_IN_HTTP_REQUEST = ["enable", "disable"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_proxy_policy_get(
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


def validate_proxy_policy_post(
    payload: dict[str, Any],
) -> tuple[bool, str | None]:
    """
    Validate POST request payload for creating proxy_policy.

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
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "policyid must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (False, f"policyid must be numeric, got: {value}")

    # Validate name if present
    if "name" in payload:
        value = payload.get("name")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "name cannot exceed 35 characters")

    # Validate proxy if present
    if "proxy" in payload:
        value = payload.get("proxy")
        if value and value not in VALID_BODY_PROXY:
            return (
                False,
                f"Invalid proxy '{value}'. Must be one of: {', '.join(VALID_BODY_PROXY)}",
            )

    # Validate ztna-tags-match-logic if present
    if "ztna-tags-match-logic" in payload:
        value = payload.get("ztna-tags-match-logic")
        if value and value not in VALID_BODY_ZTNA_TAGS_MATCH_LOGIC:
            return (
                False,
                f"Invalid ztna-tags-match-logic '{value}'. Must be one of: {', '.join(VALID_BODY_ZTNA_TAGS_MATCH_LOGIC)}",
            )

    # Validate device-ownership if present
    if "device-ownership" in payload:
        value = payload.get("device-ownership")
        if value and value not in VALID_BODY_DEVICE_OWNERSHIP:
            return (
                False,
                f"Invalid device-ownership '{value}'. Must be one of: {', '.join(VALID_BODY_DEVICE_OWNERSHIP)}",
            )

    # Validate internet-service if present
    if "internet-service" in payload:
        value = payload.get("internet-service")
        if value and value not in VALID_BODY_INTERNET_SERVICE:
            return (
                False,
                f"Invalid internet-service '{value}'. Must be one of: {', '.join(VALID_BODY_INTERNET_SERVICE)}",
            )

    # Validate internet-service-negate if present
    if "internet-service-negate" in payload:
        value = payload.get("internet-service-negate")
        if value and value not in VALID_BODY_INTERNET_SERVICE_NEGATE:
            return (
                False,
                f"Invalid internet-service-negate '{value}'. Must be one of: {', '.join(VALID_BODY_INTERNET_SERVICE_NEGATE)}",
            )

    # Validate internet-service6 if present
    if "internet-service6" in payload:
        value = payload.get("internet-service6")
        if value and value not in VALID_BODY_INTERNET_SERVICE6:
            return (
                False,
                f"Invalid internet-service6 '{value}'. Must be one of: {', '.join(VALID_BODY_INTERNET_SERVICE6)}",
            )

    # Validate internet-service6-negate if present
    if "internet-service6-negate" in payload:
        value = payload.get("internet-service6-negate")
        if value and value not in VALID_BODY_INTERNET_SERVICE6_NEGATE:
            return (
                False,
                f"Invalid internet-service6-negate '{value}'. Must be one of: {', '.join(VALID_BODY_INTERNET_SERVICE6_NEGATE)}",
            )

    # Validate srcaddr-negate if present
    if "srcaddr-negate" in payload:
        value = payload.get("srcaddr-negate")
        if value and value not in VALID_BODY_SRCADDR_NEGATE:
            return (
                False,
                f"Invalid srcaddr-negate '{value}'. Must be one of: {', '.join(VALID_BODY_SRCADDR_NEGATE)}",
            )

    # Validate dstaddr-negate if present
    if "dstaddr-negate" in payload:
        value = payload.get("dstaddr-negate")
        if value and value not in VALID_BODY_DSTADDR_NEGATE:
            return (
                False,
                f"Invalid dstaddr-negate '{value}'. Must be one of: {', '.join(VALID_BODY_DSTADDR_NEGATE)}",
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

    # Validate action if present
    if "action" in payload:
        value = payload.get("action")
        if value and value not in VALID_BODY_ACTION:
            return (
                False,
                f"Invalid action '{value}'. Must be one of: {', '.join(VALID_BODY_ACTION)}",
            )

    # Validate status if present
    if "status" in payload:
        value = payload.get("status")
        if value and value not in VALID_BODY_STATUS:
            return (
                False,
                f"Invalid status '{value}'. Must be one of: {', '.join(VALID_BODY_STATUS)}",
            )

    # Validate schedule if present
    if "schedule" in payload:
        value = payload.get("schedule")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "schedule cannot exceed 35 characters")

    # Validate logtraffic if present
    if "logtraffic" in payload:
        value = payload.get("logtraffic")
        if value and value not in VALID_BODY_LOGTRAFFIC:
            return (
                False,
                f"Invalid logtraffic '{value}'. Must be one of: {', '.join(VALID_BODY_LOGTRAFFIC)}",
            )

    # Validate session-ttl if present
    if "session-ttl" in payload:
        value = payload.get("session-ttl")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 300 or int_val > 2764800:
                    return (
                        False,
                        "session-ttl must be between 300 and 2764800",
                    )
            except (ValueError, TypeError):
                return (False, f"session-ttl must be numeric, got: {value}")

    # Validate http-tunnel-auth if present
    if "http-tunnel-auth" in payload:
        value = payload.get("http-tunnel-auth")
        if value and value not in VALID_BODY_HTTP_TUNNEL_AUTH:
            return (
                False,
                f"Invalid http-tunnel-auth '{value}'. Must be one of: {', '.join(VALID_BODY_HTTP_TUNNEL_AUTH)}",
            )

    # Validate ssh-policy-redirect if present
    if "ssh-policy-redirect" in payload:
        value = payload.get("ssh-policy-redirect")
        if value and value not in VALID_BODY_SSH_POLICY_REDIRECT:
            return (
                False,
                f"Invalid ssh-policy-redirect '{value}'. Must be one of: {', '.join(VALID_BODY_SSH_POLICY_REDIRECT)}",
            )

    # Validate webproxy-forward-server if present
    if "webproxy-forward-server" in payload:
        value = payload.get("webproxy-forward-server")
        if value and isinstance(value, str) and len(value) > 63:
            return (
                False,
                "webproxy-forward-server cannot exceed 63 characters",
            )

    # Validate isolator-server if present
    if "isolator-server" in payload:
        value = payload.get("isolator-server")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "isolator-server cannot exceed 63 characters")

    # Validate webproxy-profile if present
    if "webproxy-profile" in payload:
        value = payload.get("webproxy-profile")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "webproxy-profile cannot exceed 63 characters")

    # Validate transparent if present
    if "transparent" in payload:
        value = payload.get("transparent")
        if value and value not in VALID_BODY_TRANSPARENT:
            return (
                False,
                f"Invalid transparent '{value}'. Must be one of: {', '.join(VALID_BODY_TRANSPARENT)}",
            )

    # Validate disclaimer if present
    if "disclaimer" in payload:
        value = payload.get("disclaimer")
        if value and value not in VALID_BODY_DISCLAIMER:
            return (
                False,
                f"Invalid disclaimer '{value}'. Must be one of: {', '.join(VALID_BODY_DISCLAIMER)}",
            )

    # Validate utm-status if present
    if "utm-status" in payload:
        value = payload.get("utm-status")
        if value and value not in VALID_BODY_UTM_STATUS:
            return (
                False,
                f"Invalid utm-status '{value}'. Must be one of: {', '.join(VALID_BODY_UTM_STATUS)}",
            )

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

    # Validate replacemsg-override-group if present
    if "replacemsg-override-group" in payload:
        value = payload.get("replacemsg-override-group")
        if value and isinstance(value, str) and len(value) > 35:
            return (
                False,
                "replacemsg-override-group cannot exceed 35 characters",
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

    # Validate comments if present
    if "comments" in payload:
        value = payload.get("comments")
        if value and isinstance(value, str) and len(value) > 1023:
            return (False, "comments cannot exceed 1023 characters")

    # Validate block-notification if present
    if "block-notification" in payload:
        value = payload.get("block-notification")
        if value and value not in VALID_BODY_BLOCK_NOTIFICATION:
            return (
                False,
                f"Invalid block-notification '{value}'. Must be one of: {', '.join(VALID_BODY_BLOCK_NOTIFICATION)}",
            )

    # Validate redirect-url if present
    if "redirect-url" in payload:
        value = payload.get("redirect-url")
        if value and isinstance(value, str) and len(value) > 1023:
            return (False, "redirect-url cannot exceed 1023 characters")

    # Validate https-sub-category if present
    if "https-sub-category" in payload:
        value = payload.get("https-sub-category")
        if value and value not in VALID_BODY_HTTPS_SUB_CATEGORY:
            return (
                False,
                f"Invalid https-sub-category '{value}'. Must be one of: {', '.join(VALID_BODY_HTTPS_SUB_CATEGORY)}",
            )

    # Validate decrypted-traffic-mirror if present
    if "decrypted-traffic-mirror" in payload:
        value = payload.get("decrypted-traffic-mirror")
        if value and isinstance(value, str) and len(value) > 35:
            return (
                False,
                "decrypted-traffic-mirror cannot exceed 35 characters",
            )

    # Validate detect-https-in-http-request if present
    if "detect-https-in-http-request" in payload:
        value = payload.get("detect-https-in-http-request")
        if value and value not in VALID_BODY_DETECT_HTTPS_IN_HTTP_REQUEST:
            return (
                False,
                f"Invalid detect-https-in-http-request '{value}'. Must be one of: {', '.join(VALID_BODY_DETECT_HTTPS_IN_HTTP_REQUEST)}",
            )

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_proxy_policy_put(
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
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "policyid must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (False, f"policyid must be numeric, got: {value}")

    # Validate name if present
    if "name" in payload:
        value = payload.get("name")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "name cannot exceed 35 characters")

    # Validate proxy if present
    if "proxy" in payload:
        value = payload.get("proxy")
        if value and value not in VALID_BODY_PROXY:
            return (
                False,
                f"Invalid proxy '{value}'. Must be one of: {', '.join(VALID_BODY_PROXY)}",
            )

    # Validate ztna-tags-match-logic if present
    if "ztna-tags-match-logic" in payload:
        value = payload.get("ztna-tags-match-logic")
        if value and value not in VALID_BODY_ZTNA_TAGS_MATCH_LOGIC:
            return (
                False,
                f"Invalid ztna-tags-match-logic '{value}'. Must be one of: {', '.join(VALID_BODY_ZTNA_TAGS_MATCH_LOGIC)}",
            )

    # Validate device-ownership if present
    if "device-ownership" in payload:
        value = payload.get("device-ownership")
        if value and value not in VALID_BODY_DEVICE_OWNERSHIP:
            return (
                False,
                f"Invalid device-ownership '{value}'. Must be one of: {', '.join(VALID_BODY_DEVICE_OWNERSHIP)}",
            )

    # Validate internet-service if present
    if "internet-service" in payload:
        value = payload.get("internet-service")
        if value and value not in VALID_BODY_INTERNET_SERVICE:
            return (
                False,
                f"Invalid internet-service '{value}'. Must be one of: {', '.join(VALID_BODY_INTERNET_SERVICE)}",
            )

    # Validate internet-service-negate if present
    if "internet-service-negate" in payload:
        value = payload.get("internet-service-negate")
        if value and value not in VALID_BODY_INTERNET_SERVICE_NEGATE:
            return (
                False,
                f"Invalid internet-service-negate '{value}'. Must be one of: {', '.join(VALID_BODY_INTERNET_SERVICE_NEGATE)}",
            )

    # Validate internet-service6 if present
    if "internet-service6" in payload:
        value = payload.get("internet-service6")
        if value and value not in VALID_BODY_INTERNET_SERVICE6:
            return (
                False,
                f"Invalid internet-service6 '{value}'. Must be one of: {', '.join(VALID_BODY_INTERNET_SERVICE6)}",
            )

    # Validate internet-service6-negate if present
    if "internet-service6-negate" in payload:
        value = payload.get("internet-service6-negate")
        if value and value not in VALID_BODY_INTERNET_SERVICE6_NEGATE:
            return (
                False,
                f"Invalid internet-service6-negate '{value}'. Must be one of: {', '.join(VALID_BODY_INTERNET_SERVICE6_NEGATE)}",
            )

    # Validate srcaddr-negate if present
    if "srcaddr-negate" in payload:
        value = payload.get("srcaddr-negate")
        if value and value not in VALID_BODY_SRCADDR_NEGATE:
            return (
                False,
                f"Invalid srcaddr-negate '{value}'. Must be one of: {', '.join(VALID_BODY_SRCADDR_NEGATE)}",
            )

    # Validate dstaddr-negate if present
    if "dstaddr-negate" in payload:
        value = payload.get("dstaddr-negate")
        if value and value not in VALID_BODY_DSTADDR_NEGATE:
            return (
                False,
                f"Invalid dstaddr-negate '{value}'. Must be one of: {', '.join(VALID_BODY_DSTADDR_NEGATE)}",
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

    # Validate action if present
    if "action" in payload:
        value = payload.get("action")
        if value and value not in VALID_BODY_ACTION:
            return (
                False,
                f"Invalid action '{value}'. Must be one of: {', '.join(VALID_BODY_ACTION)}",
            )

    # Validate status if present
    if "status" in payload:
        value = payload.get("status")
        if value and value not in VALID_BODY_STATUS:
            return (
                False,
                f"Invalid status '{value}'. Must be one of: {', '.join(VALID_BODY_STATUS)}",
            )

    # Validate schedule if present
    if "schedule" in payload:
        value = payload.get("schedule")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "schedule cannot exceed 35 characters")

    # Validate logtraffic if present
    if "logtraffic" in payload:
        value = payload.get("logtraffic")
        if value and value not in VALID_BODY_LOGTRAFFIC:
            return (
                False,
                f"Invalid logtraffic '{value}'. Must be one of: {', '.join(VALID_BODY_LOGTRAFFIC)}",
            )

    # Validate session-ttl if present
    if "session-ttl" in payload:
        value = payload.get("session-ttl")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 300 or int_val > 2764800:
                    return (
                        False,
                        "session-ttl must be between 300 and 2764800",
                    )
            except (ValueError, TypeError):
                return (False, f"session-ttl must be numeric, got: {value}")

    # Validate http-tunnel-auth if present
    if "http-tunnel-auth" in payload:
        value = payload.get("http-tunnel-auth")
        if value and value not in VALID_BODY_HTTP_TUNNEL_AUTH:
            return (
                False,
                f"Invalid http-tunnel-auth '{value}'. Must be one of: {', '.join(VALID_BODY_HTTP_TUNNEL_AUTH)}",
            )

    # Validate ssh-policy-redirect if present
    if "ssh-policy-redirect" in payload:
        value = payload.get("ssh-policy-redirect")
        if value and value not in VALID_BODY_SSH_POLICY_REDIRECT:
            return (
                False,
                f"Invalid ssh-policy-redirect '{value}'. Must be one of: {', '.join(VALID_BODY_SSH_POLICY_REDIRECT)}",
            )

    # Validate webproxy-forward-server if present
    if "webproxy-forward-server" in payload:
        value = payload.get("webproxy-forward-server")
        if value and isinstance(value, str) and len(value) > 63:
            return (
                False,
                "webproxy-forward-server cannot exceed 63 characters",
            )

    # Validate isolator-server if present
    if "isolator-server" in payload:
        value = payload.get("isolator-server")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "isolator-server cannot exceed 63 characters")

    # Validate webproxy-profile if present
    if "webproxy-profile" in payload:
        value = payload.get("webproxy-profile")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "webproxy-profile cannot exceed 63 characters")

    # Validate transparent if present
    if "transparent" in payload:
        value = payload.get("transparent")
        if value and value not in VALID_BODY_TRANSPARENT:
            return (
                False,
                f"Invalid transparent '{value}'. Must be one of: {', '.join(VALID_BODY_TRANSPARENT)}",
            )

    # Validate disclaimer if present
    if "disclaimer" in payload:
        value = payload.get("disclaimer")
        if value and value not in VALID_BODY_DISCLAIMER:
            return (
                False,
                f"Invalid disclaimer '{value}'. Must be one of: {', '.join(VALID_BODY_DISCLAIMER)}",
            )

    # Validate utm-status if present
    if "utm-status" in payload:
        value = payload.get("utm-status")
        if value and value not in VALID_BODY_UTM_STATUS:
            return (
                False,
                f"Invalid utm-status '{value}'. Must be one of: {', '.join(VALID_BODY_UTM_STATUS)}",
            )

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

    # Validate replacemsg-override-group if present
    if "replacemsg-override-group" in payload:
        value = payload.get("replacemsg-override-group")
        if value and isinstance(value, str) and len(value) > 35:
            return (
                False,
                "replacemsg-override-group cannot exceed 35 characters",
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

    # Validate comments if present
    if "comments" in payload:
        value = payload.get("comments")
        if value and isinstance(value, str) and len(value) > 1023:
            return (False, "comments cannot exceed 1023 characters")

    # Validate block-notification if present
    if "block-notification" in payload:
        value = payload.get("block-notification")
        if value and value not in VALID_BODY_BLOCK_NOTIFICATION:
            return (
                False,
                f"Invalid block-notification '{value}'. Must be one of: {', '.join(VALID_BODY_BLOCK_NOTIFICATION)}",
            )

    # Validate redirect-url if present
    if "redirect-url" in payload:
        value = payload.get("redirect-url")
        if value and isinstance(value, str) and len(value) > 1023:
            return (False, "redirect-url cannot exceed 1023 characters")

    # Validate https-sub-category if present
    if "https-sub-category" in payload:
        value = payload.get("https-sub-category")
        if value and value not in VALID_BODY_HTTPS_SUB_CATEGORY:
            return (
                False,
                f"Invalid https-sub-category '{value}'. Must be one of: {', '.join(VALID_BODY_HTTPS_SUB_CATEGORY)}",
            )

    # Validate decrypted-traffic-mirror if present
    if "decrypted-traffic-mirror" in payload:
        value = payload.get("decrypted-traffic-mirror")
        if value and isinstance(value, str) and len(value) > 35:
            return (
                False,
                "decrypted-traffic-mirror cannot exceed 35 characters",
            )

    # Validate detect-https-in-http-request if present
    if "detect-https-in-http-request" in payload:
        value = payload.get("detect-https-in-http-request")
        if value and value not in VALID_BODY_DETECT_HTTPS_IN_HTTP_REQUEST:
            return (
                False,
                f"Invalid detect-https-in-http-request '{value}'. Must be one of: {', '.join(VALID_BODY_DETECT_HTTPS_IN_HTTP_REQUEST)}",
            )

    return (True, None)


# ============================================================================
# DELETE Validation
# ============================================================================


def validate_proxy_policy_delete(
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
