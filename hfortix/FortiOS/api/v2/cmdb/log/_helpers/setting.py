"""
Validation helpers for log setting endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_RESOLVE_IP = ["enable", "disable"]
VALID_BODY_RESOLVE_PORT = ["enable", "disable"]
VALID_BODY_LOG_USER_IN_UPPER = ["enable", "disable"]
VALID_BODY_FWPOLICY_IMPLICIT_LOG = ["enable", "disable"]
VALID_BODY_FWPOLICY6_IMPLICIT_LOG = ["enable", "disable"]
VALID_BODY_EXTENDED_LOG = ["enable", "disable"]
VALID_BODY_LOCAL_IN_ALLOW = ["enable", "disable"]
VALID_BODY_LOCAL_IN_DENY_UNICAST = ["enable", "disable"]
VALID_BODY_LOCAL_IN_DENY_BROADCAST = ["enable", "disable"]
VALID_BODY_LOCAL_IN_POLICY_LOG = ["enable", "disable"]
VALID_BODY_LOCAL_OUT = ["enable", "disable"]
VALID_BODY_LOCAL_OUT_IOC_DETECTION = ["enable", "disable"]
VALID_BODY_DAEMON_LOG = ["enable", "disable"]
VALID_BODY_NEIGHBOR_EVENT = ["enable", "disable"]
VALID_BODY_BRIEF_TRAFFIC_FORMAT = ["enable", "disable"]
VALID_BODY_USER_ANONYMIZE = ["enable", "disable"]
VALID_BODY_EXPOLICY_IMPLICIT_LOG = ["enable", "disable"]
VALID_BODY_LOG_POLICY_COMMENT = ["enable", "disable"]
VALID_BODY_FAZ_OVERRIDE = ["enable", "disable"]
VALID_BODY_SYSLOG_OVERRIDE = ["enable", "disable"]
VALID_BODY_REST_API_SET = ["enable", "disable"]
VALID_BODY_REST_API_GET = ["enable", "disable"]
VALID_BODY_REST_API_PERFORMANCE = ["enable", "disable"]
VALID_BODY_LONG_LIVE_SESSION_STAT = ["enable", "disable"]
VALID_BODY_EXTENDED_UTM_LOG = ["enable", "disable"]
VALID_BODY_ZONE_NAME = ["enable", "disable"]
VALID_BODY_WEB_SVC_PERF = ["enable", "disable"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_setting_get(
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


def validate_setting_put(
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

    # Validate resolve-ip if present
    if "resolve-ip" in payload:
        value = payload.get("resolve-ip")
        if value and value not in VALID_BODY_RESOLVE_IP:
            return (
                False,
                f"Invalid resolve-ip '{value}'. Must be one of: {', '.join(VALID_BODY_RESOLVE_IP)}",
            )

    # Validate resolve-port if present
    if "resolve-port" in payload:
        value = payload.get("resolve-port")
        if value and value not in VALID_BODY_RESOLVE_PORT:
            return (
                False,
                f"Invalid resolve-port '{value}'. Must be one of: {', '.join(VALID_BODY_RESOLVE_PORT)}",
            )

    # Validate log-user-in-upper if present
    if "log-user-in-upper" in payload:
        value = payload.get("log-user-in-upper")
        if value and value not in VALID_BODY_LOG_USER_IN_UPPER:
            return (
                False,
                f"Invalid log-user-in-upper '{value}'. Must be one of: {', '.join(VALID_BODY_LOG_USER_IN_UPPER)}",
            )

    # Validate fwpolicy-implicit-log if present
    if "fwpolicy-implicit-log" in payload:
        value = payload.get("fwpolicy-implicit-log")
        if value and value not in VALID_BODY_FWPOLICY_IMPLICIT_LOG:
            return (
                False,
                f"Invalid fwpolicy-implicit-log '{value}'. Must be one of: {', '.join(VALID_BODY_FWPOLICY_IMPLICIT_LOG)}",
            )

    # Validate fwpolicy6-implicit-log if present
    if "fwpolicy6-implicit-log" in payload:
        value = payload.get("fwpolicy6-implicit-log")
        if value and value not in VALID_BODY_FWPOLICY6_IMPLICIT_LOG:
            return (
                False,
                f"Invalid fwpolicy6-implicit-log '{value}'. Must be one of: {', '.join(VALID_BODY_FWPOLICY6_IMPLICIT_LOG)}",
            )

    # Validate extended-log if present
    if "extended-log" in payload:
        value = payload.get("extended-log")
        if value and value not in VALID_BODY_EXTENDED_LOG:
            return (
                False,
                f"Invalid extended-log '{value}'. Must be one of: {', '.join(VALID_BODY_EXTENDED_LOG)}",
            )

    # Validate local-in-allow if present
    if "local-in-allow" in payload:
        value = payload.get("local-in-allow")
        if value and value not in VALID_BODY_LOCAL_IN_ALLOW:
            return (
                False,
                f"Invalid local-in-allow '{value}'. Must be one of: {', '.join(VALID_BODY_LOCAL_IN_ALLOW)}",
            )

    # Validate local-in-deny-unicast if present
    if "local-in-deny-unicast" in payload:
        value = payload.get("local-in-deny-unicast")
        if value and value not in VALID_BODY_LOCAL_IN_DENY_UNICAST:
            return (
                False,
                f"Invalid local-in-deny-unicast '{value}'. Must be one of: {', '.join(VALID_BODY_LOCAL_IN_DENY_UNICAST)}",
            )

    # Validate local-in-deny-broadcast if present
    if "local-in-deny-broadcast" in payload:
        value = payload.get("local-in-deny-broadcast")
        if value and value not in VALID_BODY_LOCAL_IN_DENY_BROADCAST:
            return (
                False,
                f"Invalid local-in-deny-broadcast '{value}'. Must be one of: {', '.join(VALID_BODY_LOCAL_IN_DENY_BROADCAST)}",
            )

    # Validate local-in-policy-log if present
    if "local-in-policy-log" in payload:
        value = payload.get("local-in-policy-log")
        if value and value not in VALID_BODY_LOCAL_IN_POLICY_LOG:
            return (
                False,
                f"Invalid local-in-policy-log '{value}'. Must be one of: {', '.join(VALID_BODY_LOCAL_IN_POLICY_LOG)}",
            )

    # Validate local-out if present
    if "local-out" in payload:
        value = payload.get("local-out")
        if value and value not in VALID_BODY_LOCAL_OUT:
            return (
                False,
                f"Invalid local-out '{value}'. Must be one of: {', '.join(VALID_BODY_LOCAL_OUT)}",
            )

    # Validate local-out-ioc-detection if present
    if "local-out-ioc-detection" in payload:
        value = payload.get("local-out-ioc-detection")
        if value and value not in VALID_BODY_LOCAL_OUT_IOC_DETECTION:
            return (
                False,
                f"Invalid local-out-ioc-detection '{value}'. Must be one of: {', '.join(VALID_BODY_LOCAL_OUT_IOC_DETECTION)}",
            )

    # Validate daemon-log if present
    if "daemon-log" in payload:
        value = payload.get("daemon-log")
        if value and value not in VALID_BODY_DAEMON_LOG:
            return (
                False,
                f"Invalid daemon-log '{value}'. Must be one of: {', '.join(VALID_BODY_DAEMON_LOG)}",
            )

    # Validate neighbor-event if present
    if "neighbor-event" in payload:
        value = payload.get("neighbor-event")
        if value and value not in VALID_BODY_NEIGHBOR_EVENT:
            return (
                False,
                f"Invalid neighbor-event '{value}'. Must be one of: {', '.join(VALID_BODY_NEIGHBOR_EVENT)}",
            )

    # Validate brief-traffic-format if present
    if "brief-traffic-format" in payload:
        value = payload.get("brief-traffic-format")
        if value and value not in VALID_BODY_BRIEF_TRAFFIC_FORMAT:
            return (
                False,
                f"Invalid brief-traffic-format '{value}'. Must be one of: {', '.join(VALID_BODY_BRIEF_TRAFFIC_FORMAT)}",
            )

    # Validate user-anonymize if present
    if "user-anonymize" in payload:
        value = payload.get("user-anonymize")
        if value and value not in VALID_BODY_USER_ANONYMIZE:
            return (
                False,
                f"Invalid user-anonymize '{value}'. Must be one of: {', '.join(VALID_BODY_USER_ANONYMIZE)}",
            )

    # Validate expolicy-implicit-log if present
    if "expolicy-implicit-log" in payload:
        value = payload.get("expolicy-implicit-log")
        if value and value not in VALID_BODY_EXPOLICY_IMPLICIT_LOG:
            return (
                False,
                f"Invalid expolicy-implicit-log '{value}'. Must be one of: {', '.join(VALID_BODY_EXPOLICY_IMPLICIT_LOG)}",
            )

    # Validate log-policy-comment if present
    if "log-policy-comment" in payload:
        value = payload.get("log-policy-comment")
        if value and value not in VALID_BODY_LOG_POLICY_COMMENT:
            return (
                False,
                f"Invalid log-policy-comment '{value}'. Must be one of: {', '.join(VALID_BODY_LOG_POLICY_COMMENT)}",
            )

    # Validate faz-override if present
    if "faz-override" in payload:
        value = payload.get("faz-override")
        if value and value not in VALID_BODY_FAZ_OVERRIDE:
            return (
                False,
                f"Invalid faz-override '{value}'. Must be one of: {', '.join(VALID_BODY_FAZ_OVERRIDE)}",
            )

    # Validate syslog-override if present
    if "syslog-override" in payload:
        value = payload.get("syslog-override")
        if value and value not in VALID_BODY_SYSLOG_OVERRIDE:
            return (
                False,
                f"Invalid syslog-override '{value}'. Must be one of: {', '.join(VALID_BODY_SYSLOG_OVERRIDE)}",
            )

    # Validate rest-api-set if present
    if "rest-api-set" in payload:
        value = payload.get("rest-api-set")
        if value and value not in VALID_BODY_REST_API_SET:
            return (
                False,
                f"Invalid rest-api-set '{value}'. Must be one of: {', '.join(VALID_BODY_REST_API_SET)}",
            )

    # Validate rest-api-get if present
    if "rest-api-get" in payload:
        value = payload.get("rest-api-get")
        if value and value not in VALID_BODY_REST_API_GET:
            return (
                False,
                f"Invalid rest-api-get '{value}'. Must be one of: {', '.join(VALID_BODY_REST_API_GET)}",
            )

    # Validate rest-api-performance if present
    if "rest-api-performance" in payload:
        value = payload.get("rest-api-performance")
        if value and value not in VALID_BODY_REST_API_PERFORMANCE:
            return (
                False,
                f"Invalid rest-api-performance '{value}'. Must be one of: {', '.join(VALID_BODY_REST_API_PERFORMANCE)}",
            )

    # Validate long-live-session-stat if present
    if "long-live-session-stat" in payload:
        value = payload.get("long-live-session-stat")
        if value and value not in VALID_BODY_LONG_LIVE_SESSION_STAT:
            return (
                False,
                f"Invalid long-live-session-stat '{value}'. Must be one of: {', '.join(VALID_BODY_LONG_LIVE_SESSION_STAT)}",
            )

    # Validate extended-utm-log if present
    if "extended-utm-log" in payload:
        value = payload.get("extended-utm-log")
        if value and value not in VALID_BODY_EXTENDED_UTM_LOG:
            return (
                False,
                f"Invalid extended-utm-log '{value}'. Must be one of: {', '.join(VALID_BODY_EXTENDED_UTM_LOG)}",
            )

    # Validate zone-name if present
    if "zone-name" in payload:
        value = payload.get("zone-name")
        if value and value not in VALID_BODY_ZONE_NAME:
            return (
                False,
                f"Invalid zone-name '{value}'. Must be one of: {', '.join(VALID_BODY_ZONE_NAME)}",
            )

    # Validate web-svc-perf if present
    if "web-svc-per" in payload:
        value = payload.get("web-svc-per")
        if value and value not in VALID_BODY_WEB_SVC_PERF:
            return (
                False,
                f"Invalid web-svc-perf '{value}'. Must be one of: {', '.join(VALID_BODY_WEB_SVC_PERF)}",
            )

    # Validate anonymization-hash if present
    if "anonymization-hash" in payload:
        value = payload.get("anonymization-hash")
        if value and isinstance(value, str) and len(value) > 32:
            return (False, "anonymization-hash cannot exceed 32 characters")

    return (True, None)
