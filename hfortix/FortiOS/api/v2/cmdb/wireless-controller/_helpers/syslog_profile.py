"""
Validation helpers for wireless-controller syslog_profile endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_SERVER_STATUS = ["enable", "disable"]
VALID_BODY_SERVER_TYPE = ["standard", "fortianalyzer"]
VALID_BODY_LOG_LEVEL = [
    "emergency",
    "alert",
    "critical",
    "error",
    "warning",
    "notification",
    "information",
    "debugging",
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_syslog_profile_get(
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


def validate_syslog_profile_post(
    payload: dict[str, Any],
) -> tuple[bool, str | None]:
    """
    Validate POST request payload for creating syslog_profile.

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

    # Validate comment if present
    if "comment" in payload:
        value = payload.get("comment")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "comment cannot exceed 255 characters")

    # Validate server-status if present
    if "server-status" in payload:
        value = payload.get("server-status")
        if value and value not in VALID_BODY_SERVER_STATUS:
            return (
                False,
                f"Invalid server-status '{value}'. Must be one of: {', '.join(VALID_BODY_SERVER_STATUS)}",
            )

    # Validate server if present
    if "server" in payload:
        value = payload.get("server")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "server cannot exceed 63 characters")

    # Validate server-port if present
    if "server-port" in payload:
        value = payload.get("server-port")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 65535:
                    return (False, "server-port must be between 0 and 65535")
            except (ValueError, TypeError):
                return (False, f"server-port must be numeric, got: {value}")

    # Validate server-type if present
    if "server-type" in payload:
        value = payload.get("server-type")
        if value and value not in VALID_BODY_SERVER_TYPE:
            return (
                False,
                f"Invalid server-type '{value}'. Must be one of: {', '.join(VALID_BODY_SERVER_TYPE)}",
            )

    # Validate log-level if present
    if "log-level" in payload:
        value = payload.get("log-level")
        if value and value not in VALID_BODY_LOG_LEVEL:
            return (
                False,
                f"Invalid log-level '{value}'. Must be one of: {', '.join(VALID_BODY_LOG_LEVEL)}",
            )

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_syslog_profile_put(
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

    # Validate comment if present
    if "comment" in payload:
        value = payload.get("comment")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "comment cannot exceed 255 characters")

    # Validate server-status if present
    if "server-status" in payload:
        value = payload.get("server-status")
        if value and value not in VALID_BODY_SERVER_STATUS:
            return (
                False,
                f"Invalid server-status '{value}'. Must be one of: {', '.join(VALID_BODY_SERVER_STATUS)}",
            )

    # Validate server if present
    if "server" in payload:
        value = payload.get("server")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "server cannot exceed 63 characters")

    # Validate server-port if present
    if "server-port" in payload:
        value = payload.get("server-port")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 65535:
                    return (False, "server-port must be between 0 and 65535")
            except (ValueError, TypeError):
                return (False, f"server-port must be numeric, got: {value}")

    # Validate server-type if present
    if "server-type" in payload:
        value = payload.get("server-type")
        if value and value not in VALID_BODY_SERVER_TYPE:
            return (
                False,
                f"Invalid server-type '{value}'. Must be one of: {', '.join(VALID_BODY_SERVER_TYPE)}",
            )

    # Validate log-level if present
    if "log-level" in payload:
        value = payload.get("log-level")
        if value and value not in VALID_BODY_LOG_LEVEL:
            return (
                False,
                f"Invalid log-level '{value}'. Must be one of: {', '.join(VALID_BODY_LOG_LEVEL)}",
            )

    return (True, None)


# ============================================================================
# DELETE Validation
# ============================================================================


def validate_syslog_profile_delete(
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
