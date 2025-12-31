"""
Validation helpers for system np6xlite endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_FASTPATH = ["disable", "enable"]
VALID_BODY_PER_SESSION_ACCOUNTING = ["disable", "traffic-log-only", "enable"]
VALID_BODY_IPSEC_INNER_FRAGMENT = ["disable", "enable"]
VALID_BODY_IPSEC_THROUGHPUT_MSG_FREQUENCY = [
    "disable",
    "32kb",
    "64kb",
    "128kb",
    "256kb",
    "512kb",
    "1mb",
    "2mb",
    "4mb",
    "8mb",
    "16mb",
    "32mb",
    "64mb",
    "128mb",
    "256mb",
    "512mb",
    "1gb",
]
VALID_BODY_IPSEC_STS_TIMEOUT = [
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "10",
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_np6xlite_get(
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


def validate_np6xlite_post(payload: dict[str, Any]) -> tuple[bool, str | None]:
    """
    Validate POST request payload for creating np6xlite.

    Args:
        payload: The payload to validate

    Returns:
        Tuple of (is_valid, error_message)
    """
    # Validate name if present
    if "name" in payload:
        value = payload.get("name")
        if value and isinstance(value, str) and len(value) > 31:
            return (False, "name cannot exceed 31 characters")

    # Validate fastpath if present
    if "fastpath" in payload:
        value = payload.get("fastpath")
        if value and value not in VALID_BODY_FASTPATH:
            return (
                False,
                f"Invalid fastpath '{value}'. Must be one of: {', '.join(VALID_BODY_FASTPATH)}",
            )

    # Validate per-session-accounting if present
    if "per-session-accounting" in payload:
        value = payload.get("per-session-accounting")
        if value and value not in VALID_BODY_PER_SESSION_ACCOUNTING:
            return (
                False,
                f"Invalid per-session-accounting '{value}'. Must be one of: {', '.join(VALID_BODY_PER_SESSION_ACCOUNTING)}",
            )

    # Validate session-timeout-interval if present
    if "session-timeout-interval" in payload:
        value = payload.get("session-timeout-interval")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 1000:
                    return (
                        False,
                        "session-timeout-interval must be between 0 and 1000",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"session-timeout-interval must be numeric, got: {value}",
                )

    # Validate ipsec-inner-fragment if present
    if "ipsec-inner-fragment" in payload:
        value = payload.get("ipsec-inner-fragment")
        if value and value not in VALID_BODY_IPSEC_INNER_FRAGMENT:
            return (
                False,
                f"Invalid ipsec-inner-fragment '{value}'. Must be one of: {', '.join(VALID_BODY_IPSEC_INNER_FRAGMENT)}",
            )

    # Validate ipsec-throughput-msg-frequency if present
    if "ipsec-throughput-msg-frequency" in payload:
        value = payload.get("ipsec-throughput-msg-frequency")
        if value and value not in VALID_BODY_IPSEC_THROUGHPUT_MSG_FREQUENCY:
            return (
                False,
                f"Invalid ipsec-throughput-msg-frequency '{value}'. Must be one of: {', '.join(VALID_BODY_IPSEC_THROUGHPUT_MSG_FREQUENCY)}",
            )

    # Validate ipsec-sts-timeout if present
    if "ipsec-sts-timeout" in payload:
        value = payload.get("ipsec-sts-timeout")
        if value and value not in VALID_BODY_IPSEC_STS_TIMEOUT:
            return (
                False,
                f"Invalid ipsec-sts-timeout '{value}'. Must be one of: {', '.join(VALID_BODY_IPSEC_STS_TIMEOUT)}",
            )

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_np6xlite_put(
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
        if value and isinstance(value, str) and len(value) > 31:
            return (False, "name cannot exceed 31 characters")

    # Validate fastpath if present
    if "fastpath" in payload:
        value = payload.get("fastpath")
        if value and value not in VALID_BODY_FASTPATH:
            return (
                False,
                f"Invalid fastpath '{value}'. Must be one of: {', '.join(VALID_BODY_FASTPATH)}",
            )

    # Validate per-session-accounting if present
    if "per-session-accounting" in payload:
        value = payload.get("per-session-accounting")
        if value and value not in VALID_BODY_PER_SESSION_ACCOUNTING:
            return (
                False,
                f"Invalid per-session-accounting '{value}'. Must be one of: {', '.join(VALID_BODY_PER_SESSION_ACCOUNTING)}",
            )

    # Validate session-timeout-interval if present
    if "session-timeout-interval" in payload:
        value = payload.get("session-timeout-interval")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 1000:
                    return (
                        False,
                        "session-timeout-interval must be between 0 and 1000",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"session-timeout-interval must be numeric, got: {value}",
                )

    # Validate ipsec-inner-fragment if present
    if "ipsec-inner-fragment" in payload:
        value = payload.get("ipsec-inner-fragment")
        if value and value not in VALID_BODY_IPSEC_INNER_FRAGMENT:
            return (
                False,
                f"Invalid ipsec-inner-fragment '{value}'. Must be one of: {', '.join(VALID_BODY_IPSEC_INNER_FRAGMENT)}",
            )

    # Validate ipsec-throughput-msg-frequency if present
    if "ipsec-throughput-msg-frequency" in payload:
        value = payload.get("ipsec-throughput-msg-frequency")
        if value and value not in VALID_BODY_IPSEC_THROUGHPUT_MSG_FREQUENCY:
            return (
                False,
                f"Invalid ipsec-throughput-msg-frequency '{value}'. Must be one of: {', '.join(VALID_BODY_IPSEC_THROUGHPUT_MSG_FREQUENCY)}",
            )

    # Validate ipsec-sts-timeout if present
    if "ipsec-sts-timeout" in payload:
        value = payload.get("ipsec-sts-timeout")
        if value and value not in VALID_BODY_IPSEC_STS_TIMEOUT:
            return (
                False,
                f"Invalid ipsec-sts-timeout '{value}'. Must be one of: {', '.join(VALID_BODY_IPSEC_STS_TIMEOUT)}",
            )

    return (True, None)


# ============================================================================
# DELETE Validation
# ============================================================================


def validate_np6xlite_delete(
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
