"""
Validation helpers for firewall ldb_monitor endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_TYPE = ["ping", "tcp", "http", "https", "dns"]
VALID_BODY_DNS_PROTOCOL = ["udp", "tcp"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_ldb_monitor_get(
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


def validate_ldb_monitor_post(
    payload: dict[str, Any],
) -> tuple[bool, str | None]:
    """
    Validate POST request payload for creating ldb_monitor.

    Args:
        payload: The payload to validate

    Returns:
        Tuple of (is_valid, error_message)
    """
    # Validate name if present
    if "name" in payload:
        value = payload.get("name")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "name cannot exceed 35 characters")

    # Validate type if present
    if "type" in payload:
        value = payload.get("type")
        if value and value not in VALID_BODY_TYPE:
            return (
                False,
                f"Invalid type '{value}'. Must be one of: {', '.join(VALID_BODY_TYPE)}",
            )

    # Validate interval if present
    if "interval" in payload:
        value = payload.get("interval")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 5 or int_val > 65535:
                    return (False, "interval must be between 5 and 65535")
            except (ValueError, TypeError):
                return (False, f"interval must be numeric, got: {value}")

    # Validate timeout if present
    if "timeout" in payload:
        value = payload.get("timeout")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 255:
                    return (False, "timeout must be between 1 and 255")
            except (ValueError, TypeError):
                return (False, f"timeout must be numeric, got: {value}")

    # Validate retry if present
    if "retry" in payload:
        value = payload.get("retry")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 255:
                    return (False, "retry must be between 1 and 255")
            except (ValueError, TypeError):
                return (False, f"retry must be numeric, got: {value}")

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

    # Validate http-get if present
    if "http-get" in payload:
        value = payload.get("http-get")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "http-get cannot exceed 255 characters")

    # Validate http-match if present
    if "http-match" in payload:
        value = payload.get("http-match")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "http-match cannot exceed 255 characters")

    # Validate http-max-redirects if present
    if "http-max-redirects" in payload:
        value = payload.get("http-max-redirects")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 5:
                    return (
                        False,
                        "http-max-redirects must be between 0 and 5",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"http-max-redirects must be numeric, got: {value}",
                )

    # Validate dns-protocol if present
    if "dns-protocol" in payload:
        value = payload.get("dns-protocol")
        if value and value not in VALID_BODY_DNS_PROTOCOL:
            return (
                False,
                f"Invalid dns-protocol '{value}'. Must be one of: {', '.join(VALID_BODY_DNS_PROTOCOL)}",
            )

    # Validate dns-request-domain if present
    if "dns-request-domain" in payload:
        value = payload.get("dns-request-domain")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "dns-request-domain cannot exceed 255 characters")

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_ldb_monitor_put(
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
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "name cannot exceed 35 characters")

    # Validate type if present
    if "type" in payload:
        value = payload.get("type")
        if value and value not in VALID_BODY_TYPE:
            return (
                False,
                f"Invalid type '{value}'. Must be one of: {', '.join(VALID_BODY_TYPE)}",
            )

    # Validate interval if present
    if "interval" in payload:
        value = payload.get("interval")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 5 or int_val > 65535:
                    return (False, "interval must be between 5 and 65535")
            except (ValueError, TypeError):
                return (False, f"interval must be numeric, got: {value}")

    # Validate timeout if present
    if "timeout" in payload:
        value = payload.get("timeout")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 255:
                    return (False, "timeout must be between 1 and 255")
            except (ValueError, TypeError):
                return (False, f"timeout must be numeric, got: {value}")

    # Validate retry if present
    if "retry" in payload:
        value = payload.get("retry")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 255:
                    return (False, "retry must be between 1 and 255")
            except (ValueError, TypeError):
                return (False, f"retry must be numeric, got: {value}")

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

    # Validate http-get if present
    if "http-get" in payload:
        value = payload.get("http-get")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "http-get cannot exceed 255 characters")

    # Validate http-match if present
    if "http-match" in payload:
        value = payload.get("http-match")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "http-match cannot exceed 255 characters")

    # Validate http-max-redirects if present
    if "http-max-redirects" in payload:
        value = payload.get("http-max-redirects")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 5:
                    return (
                        False,
                        "http-max-redirects must be between 0 and 5",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"http-max-redirects must be numeric, got: {value}",
                )

    # Validate dns-protocol if present
    if "dns-protocol" in payload:
        value = payload.get("dns-protocol")
        if value and value not in VALID_BODY_DNS_PROTOCOL:
            return (
                False,
                f"Invalid dns-protocol '{value}'. Must be one of: {', '.join(VALID_BODY_DNS_PROTOCOL)}",
            )

    # Validate dns-request-domain if present
    if "dns-request-domain" in payload:
        value = payload.get("dns-request-domain")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "dns-request-domain cannot exceed 255 characters")

    return (True, None)


# ============================================================================
# DELETE Validation
# ============================================================================


def validate_ldb_monitor_delete(
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
