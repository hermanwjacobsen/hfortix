"""
Validation helpers for firewall service_custom endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_PROXY = ["enable", "disable"]
VALID_BODY_PROTOCOL = [
    "TCP/UDP/UDP-Lite/SCTP",
    "ICMP",
    "ICMP6",
    "IP",
    "HTTP",
    "FTP",
    "CONNECT",
    "SOCKS-TCP",
    "SOCKS-UDP",
    "ALL",
]
VALID_BODY_HELPER = [
    "auto",
    "disable",
    "ftp",
    "tftp",
    "ras",
    "h323",
    "tns",
    "mms",
    "sip",
    "pptp",
    "rtsp",
    "dns-udp",
    "dns-tcp",
    "pmap",
    "rsh",
    "dcerpc",
    "mgcp",
]
VALID_BODY_CHECK_RESET_RANGE = ["disable", "strict", "default"]
VALID_BODY_APP_SERVICE_TYPE = ["disable", "app-id", "app-category"]
VALID_BODY_FABRIC_OBJECT = ["enable", "disable"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_service_custom_get(
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


def validate_service_custom_post(
    payload: dict[str, Any],
) -> tuple[bool, str | None]:
    """
    Validate POST request payload for creating service_custom.

    Args:
        payload: The payload to validate

    Returns:
        Tuple of (is_valid, error_message)
    """
    # Validate name if present
    if "name" in payload:
        value = payload.get("name")
        if value and isinstance(value, str) and len(value) > 79:
            return (False, "name cannot exceed 79 characters")

    # Validate proxy if present
    if "proxy" in payload:
        value = payload.get("proxy")
        if value and value not in VALID_BODY_PROXY:
            return (
                False,
                f"Invalid proxy '{value}'. Must be one of: {', '.join(VALID_BODY_PROXY)}",
            )

    # Validate category if present
    if "category" in payload:
        value = payload.get("category")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "category cannot exceed 63 characters")

    # Validate protocol if present
    if "protocol" in payload:
        value = payload.get("protocol")
        if value and value not in VALID_BODY_PROTOCOL:
            return (
                False,
                f"Invalid protocol '{value}'. Must be one of: {', '.join(VALID_BODY_PROTOCOL)}",
            )

    # Validate helper if present
    if "helper" in payload:
        value = payload.get("helper")
        if value and value not in VALID_BODY_HELPER:
            return (
                False,
                f"Invalid helper '{value}'. Must be one of: {', '.join(VALID_BODY_HELPER)}",
            )

    # Validate fqdn if present
    if "fqdn" in payload:
        value = payload.get("fqdn")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "fqdn cannot exceed 255 characters")

    # Validate protocol-number if present
    if "protocol-number" in payload:
        value = payload.get("protocol-number")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 254:
                    return (
                        False,
                        "protocol-number must be between 0 and 254",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"protocol-number must be numeric, got: {value}",
                )

    # Validate icmptype if present
    if "icmptype" in payload:
        value = payload.get("icmptype")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "icmptype must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (False, f"icmptype must be numeric, got: {value}")

    # Validate icmpcode if present
    if "icmpcode" in payload:
        value = payload.get("icmpcode")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 255:
                    return (False, "icmpcode must be between 0 and 255")
            except (ValueError, TypeError):
                return (False, f"icmpcode must be numeric, got: {value}")

    # Validate tcp-halfclose-timer if present
    if "tcp-halfclose-timer" in payload:
        value = payload.get("tcp-halfclose-timer")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 86400:
                    return (
                        False,
                        "tcp-halfclose-timer must be between 0 and 86400",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"tcp-halfclose-timer must be numeric, got: {value}",
                )

    # Validate tcp-halfopen-timer if present
    if "tcp-halfopen-timer" in payload:
        value = payload.get("tcp-halfopen-timer")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 86400:
                    return (
                        False,
                        "tcp-halfopen-timer must be between 0 and 86400",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"tcp-halfopen-timer must be numeric, got: {value}",
                )

    # Validate tcp-timewait-timer if present
    if "tcp-timewait-timer" in payload:
        value = payload.get("tcp-timewait-timer")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 300:
                    return (
                        False,
                        "tcp-timewait-timer must be between 0 and 300",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"tcp-timewait-timer must be numeric, got: {value}",
                )

    # Validate tcp-rst-timer if present
    if "tcp-rst-timer" in payload:
        value = payload.get("tcp-rst-timer")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 5 or int_val > 300:
                    return (False, "tcp-rst-timer must be between 5 and 300")
            except (ValueError, TypeError):
                return (False, f"tcp-rst-timer must be numeric, got: {value}")

    # Validate udp-idle-timer if present
    if "udp-idle-timer" in payload:
        value = payload.get("udp-idle-timer")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 86400:
                    return (
                        False,
                        "udp-idle-timer must be between 0 and 86400",
                    )
            except (ValueError, TypeError):
                return (False, f"udp-idle-timer must be numeric, got: {value}")

    # Validate check-reset-range if present
    if "check-reset-range" in payload:
        value = payload.get("check-reset-range")
        if value and value not in VALID_BODY_CHECK_RESET_RANGE:
            return (
                False,
                f"Invalid check-reset-range '{value}'. Must be one of: {', '.join(VALID_BODY_CHECK_RESET_RANGE)}",
            )

    # Validate comment if present
    if "comment" in payload:
        value = payload.get("comment")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "comment cannot exceed 255 characters")

    # Validate color if present
    if "color" in payload:
        value = payload.get("color")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 32:
                    return (False, "color must be between 0 and 32")
            except (ValueError, TypeError):
                return (False, f"color must be numeric, got: {value}")

    # Validate app-service-type if present
    if "app-service-type" in payload:
        value = payload.get("app-service-type")
        if value and value not in VALID_BODY_APP_SERVICE_TYPE:
            return (
                False,
                f"Invalid app-service-type '{value}'. Must be one of: {', '.join(VALID_BODY_APP_SERVICE_TYPE)}",
            )

    # Validate fabric-object if present
    if "fabric-object" in payload:
        value = payload.get("fabric-object")
        if value and value not in VALID_BODY_FABRIC_OBJECT:
            return (
                False,
                f"Invalid fabric-object '{value}'. Must be one of: {', '.join(VALID_BODY_FABRIC_OBJECT)}",
            )

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_service_custom_put(
    name: str | None = None, payload: dict[str, Any] | None = None
) -> tuple[bool, str | None]:
    """
    Validate PUT request payload for updating {endpoint_name}.

    Args:
        name: Object identifier (required)
        payload: The payload to validate

    Returns:
        Tuple of (is_valid, error_message)
    """
    # name is required for updates
    if not name:
        return (False, "name is required for PUT operation")

    # If no payload provided, nothing to validate
    if not payload:
        return (True, None)

    # Validate name if present
    if "name" in payload:
        value = payload.get("name")
        if value and isinstance(value, str) and len(value) > 79:
            return (False, "name cannot exceed 79 characters")

    # Validate proxy if present
    if "proxy" in payload:
        value = payload.get("proxy")
        if value and value not in VALID_BODY_PROXY:
            return (
                False,
                f"Invalid proxy '{value}'. Must be one of: {', '.join(VALID_BODY_PROXY)}",
            )

    # Validate category if present
    if "category" in payload:
        value = payload.get("category")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "category cannot exceed 63 characters")

    # Validate protocol if present
    if "protocol" in payload:
        value = payload.get("protocol")
        if value and value not in VALID_BODY_PROTOCOL:
            return (
                False,
                f"Invalid protocol '{value}'. Must be one of: {', '.join(VALID_BODY_PROTOCOL)}",
            )

    # Validate helper if present
    if "helper" in payload:
        value = payload.get("helper")
        if value and value not in VALID_BODY_HELPER:
            return (
                False,
                f"Invalid helper '{value}'. Must be one of: {', '.join(VALID_BODY_HELPER)}",
            )

    # Validate fqdn if present
    if "fqdn" in payload:
        value = payload.get("fqdn")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "fqdn cannot exceed 255 characters")

    # Validate protocol-number if present
    if "protocol-number" in payload:
        value = payload.get("protocol-number")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 254:
                    return (
                        False,
                        "protocol-number must be between 0 and 254",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"protocol-number must be numeric, got: {value}",
                )

    # Validate icmptype if present
    if "icmptype" in payload:
        value = payload.get("icmptype")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "icmptype must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (False, f"icmptype must be numeric, got: {value}")

    # Validate icmpcode if present
    if "icmpcode" in payload:
        value = payload.get("icmpcode")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 255:
                    return (False, "icmpcode must be between 0 and 255")
            except (ValueError, TypeError):
                return (False, f"icmpcode must be numeric, got: {value}")

    # Validate tcp-halfclose-timer if present
    if "tcp-halfclose-timer" in payload:
        value = payload.get("tcp-halfclose-timer")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 86400:
                    return (
                        False,
                        "tcp-halfclose-timer must be between 0 and 86400",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"tcp-halfclose-timer must be numeric, got: {value}",
                )

    # Validate tcp-halfopen-timer if present
    if "tcp-halfopen-timer" in payload:
        value = payload.get("tcp-halfopen-timer")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 86400:
                    return (
                        False,
                        "tcp-halfopen-timer must be between 0 and 86400",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"tcp-halfopen-timer must be numeric, got: {value}",
                )

    # Validate tcp-timewait-timer if present
    if "tcp-timewait-timer" in payload:
        value = payload.get("tcp-timewait-timer")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 300:
                    return (
                        False,
                        "tcp-timewait-timer must be between 0 and 300",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"tcp-timewait-timer must be numeric, got: {value}",
                )

    # Validate tcp-rst-timer if present
    if "tcp-rst-timer" in payload:
        value = payload.get("tcp-rst-timer")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 5 or int_val > 300:
                    return (False, "tcp-rst-timer must be between 5 and 300")
            except (ValueError, TypeError):
                return (False, f"tcp-rst-timer must be numeric, got: {value}")

    # Validate udp-idle-timer if present
    if "udp-idle-timer" in payload:
        value = payload.get("udp-idle-timer")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 86400:
                    return (
                        False,
                        "udp-idle-timer must be between 0 and 86400",
                    )
            except (ValueError, TypeError):
                return (False, f"udp-idle-timer must be numeric, got: {value}")

    # Validate check-reset-range if present
    if "check-reset-range" in payload:
        value = payload.get("check-reset-range")
        if value and value not in VALID_BODY_CHECK_RESET_RANGE:
            return (
                False,
                f"Invalid check-reset-range '{value}'. Must be one of: {', '.join(VALID_BODY_CHECK_RESET_RANGE)}",
            )

    # Validate comment if present
    if "comment" in payload:
        value = payload.get("comment")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "comment cannot exceed 255 characters")

    # Validate color if present
    if "color" in payload:
        value = payload.get("color")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 32:
                    return (False, "color must be between 0 and 32")
            except (ValueError, TypeError):
                return (False, f"color must be numeric, got: {value}")

    # Validate app-service-type if present
    if "app-service-type" in payload:
        value = payload.get("app-service-type")
        if value and value not in VALID_BODY_APP_SERVICE_TYPE:
            return (
                False,
                f"Invalid app-service-type '{value}'. Must be one of: {', '.join(VALID_BODY_APP_SERVICE_TYPE)}",
            )

    # Validate fabric-object if present
    if "fabric-object" in payload:
        value = payload.get("fabric-object")
        if value and value not in VALID_BODY_FABRIC_OBJECT:
            return (
                False,
                f"Invalid fabric-object '{value}'. Must be one of: {', '.join(VALID_BODY_FABRIC_OBJECT)}",
            )

    return (True, None)


# ============================================================================
# DELETE Validation
# ============================================================================


def validate_service_custom_delete(
    name: str | None = None,
) -> tuple[bool, str | None]:
    """
    Validate DELETE request parameters.

    Args:
        name: Object identifier (required)

    Returns:
        Tuple of (is_valid, error_message)
    """
    if not name:
        return (False, "name is required for DELETE operation")

    return (True, None)
