"""
Validation helpers for log syslogd4_override_setting endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_STATUS = ["enable", "disable"]
VALID_BODY_MODE = ["udp", "legacy-reliable", "reliable"]
VALID_BODY_USE_MANAGEMENT_VDOM = ["enable", "disable"]
VALID_BODY_FACILITY = [
    "kernel",
    "user",
    "mail",
    "daemon",
    "auth",
    "syslog",
    "lpr",
    "news",
    "uucp",
    "cron",
    "authpriv",
    "ftp",
    "ntp",
    "audit",
    "alert",
    "clock",
    "local0",
    "local1",
    "local2",
    "local3",
    "local4",
    "local5",
    "local6",
    "local7",
]
VALID_BODY_FORMAT = ["default", "csv", "ce", "rfc5424", "json"]
VALID_BODY_PRIORITY = ["default", "low"]
VALID_BODY_ENC_ALGORITHM = ["high-medium", "high", "low", "disable"]
VALID_BODY_SSL_MIN_PROTO_VERSION = [
    "default",
    "SSLv3",
    "TLSv1",
    "TLSv1-1",
    "TLSv1-2",
    "TLSv1-3",
]
VALID_BODY_INTERFACE_SELECT_METHOD = ["auto", "sdwan", "specify"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_syslogd4_override_setting_get(
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


def validate_syslogd4_override_setting_put(
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

    # Validate status if present
    if "status" in payload:
        value = payload.get("status")
        if value and value not in VALID_BODY_STATUS:
            return (
                False,
                f"Invalid status '{value}'. Must be one of: {', '.join(VALID_BODY_STATUS)}",
            )

    # Validate server if present
    if "server" in payload:
        value = payload.get("server")
        if value and isinstance(value, str) and len(value) > 127:
            return (False, "server cannot exceed 127 characters")

    # Validate mode if present
    if "mode" in payload:
        value = payload.get("mode")
        if value and value not in VALID_BODY_MODE:
            return (
                False,
                f"Invalid mode '{value}'. Must be one of: {', '.join(VALID_BODY_MODE)}",
            )

    # Validate use-management-vdom if present
    if "use-management-vdom" in payload:
        value = payload.get("use-management-vdom")
        if value and value not in VALID_BODY_USE_MANAGEMENT_VDOM:
            return (
                False,
                f"Invalid use-management-vdom '{value}'. Must be one of: {', '.join(VALID_BODY_USE_MANAGEMENT_VDOM)}",
            )

    # Validate port if present
    if "port" in payload:
        value = payload.get("port")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 65535:
                    return (False, "port must be between 0 and 65535")
            except (ValueError, TypeError):
                return (False, f"port must be numeric, got: {value}")

    # Validate facility if present
    if "facility" in payload:
        value = payload.get("facility")
        if value and value not in VALID_BODY_FACILITY:
            return (
                False,
                f"Invalid facility '{value}'. Must be one of: {', '.join(VALID_BODY_FACILITY)}",
            )

    # Validate source-ip-interface if present
    if "source-ip-interface" in payload:
        value = payload.get("source-ip-interface")
        if value and isinstance(value, str) and len(value) > 15:
            return (False, "source-ip-interface cannot exceed 15 characters")

    # Validate source-ip if present
    if "source-ip" in payload:
        value = payload.get("source-ip")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "source-ip cannot exceed 63 characters")

    # Validate format if present
    if "format" in payload:
        value = payload.get("format")
        if value and value not in VALID_BODY_FORMAT:
            return (
                False,
                f"Invalid format '{value}'. Must be one of: {', '.join(VALID_BODY_FORMAT)}",
            )

    # Validate priority if present
    if "priority" in payload:
        value = payload.get("priority")
        if value and value not in VALID_BODY_PRIORITY:
            return (
                False,
                f"Invalid priority '{value}'. Must be one of: {', '.join(VALID_BODY_PRIORITY)}",
            )

    # Validate max-log-rate if present
    if "max-log-rate" in payload:
        value = payload.get("max-log-rate")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 100000:
                    return (
                        False,
                        "max-log-rate must be between 0 and 100000",
                    )
            except (ValueError, TypeError):
                return (False, f"max-log-rate must be numeric, got: {value}")

    # Validate enc-algorithm if present
    if "enc-algorithm" in payload:
        value = payload.get("enc-algorithm")
        if value and value not in VALID_BODY_ENC_ALGORITHM:
            return (
                False,
                f"Invalid enc-algorithm '{value}'. Must be one of: {', '.join(VALID_BODY_ENC_ALGORITHM)}",
            )

    # Validate ssl-min-proto-version if present
    if "ssl-min-proto-version" in payload:
        value = payload.get("ssl-min-proto-version")
        if value and value not in VALID_BODY_SSL_MIN_PROTO_VERSION:
            return (
                False,
                f"Invalid ssl-min-proto-version '{value}'. Must be one of: {', '.join(VALID_BODY_SSL_MIN_PROTO_VERSION)}",
            )

    # Validate certificate if present
    if "certificate" in payload:
        value = payload.get("certificate")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "certificate cannot exceed 35 characters")

    # Validate interface-select-method if present
    if "interface-select-method" in payload:
        value = payload.get("interface-select-method")
        if value and value not in VALID_BODY_INTERFACE_SELECT_METHOD:
            return (
                False,
                f"Invalid interface-select-method '{value}'. Must be one of: {', '.join(VALID_BODY_INTERFACE_SELECT_METHOD)}",
            )

    # Validate interface if present
    if "interface" in payload:
        value = payload.get("interface")
        if value and isinstance(value, str) and len(value) > 15:
            return (False, "interface cannot exceed 15 characters")

    # Validate vrf-select if present
    if "vrf-select" in payload:
        value = payload.get("vrf-select")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 511:
                    return (False, "vrf-select must be between 0 and 511")
            except (ValueError, TypeError):
                return (False, f"vrf-select must be numeric, got: {value}")

    return (True, None)
