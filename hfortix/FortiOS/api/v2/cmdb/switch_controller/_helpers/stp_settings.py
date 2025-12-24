"""
Validation helpers for switch-controller stp_settings endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_stp_settings_get(
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


def validate_stp_settings_put(
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

    # Validate revision if present
    if "revision" in payload:
        value = payload.get("revision")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 65535:
                    return (False, "revision must be between 0 and 65535")
            except (ValueError, TypeError):
                return (False, f"revision must be numeric, got: {value}")

    # Validate hello-time if present
    if "hello-time" in payload:
        value = payload.get("hello-time")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 10:
                    return (False, "hello-time must be between 1 and 10")
            except (ValueError, TypeError):
                return (False, f"hello-time must be numeric, got: {value}")

    # Validate forward-time if present
    if "forward-time" in payload:
        value = payload.get("forward-time")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 4 or int_val > 30:
                    return (False, "forward-time must be between 4 and 30")
            except (ValueError, TypeError):
                return (False, f"forward-time must be numeric, got: {value}")

    # Validate max-age if present
    if "max-age" in payload:
        value = payload.get("max-age")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 6 or int_val > 40:
                    return (False, "max-age must be between 6 and 40")
            except (ValueError, TypeError):
                return (False, f"max-age must be numeric, got: {value}")

    # Validate max-hops if present
    if "max-hops" in payload:
        value = payload.get("max-hops")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 40:
                    return (False, "max-hops must be between 1 and 40")
            except (ValueError, TypeError):
                return (False, f"max-hops must be numeric, got: {value}")

    # Validate pending-timer if present
    if "pending-timer" in payload:
        value = payload.get("pending-timer")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 15:
                    return (False, "pending-timer must be between 1 and 15")
            except (ValueError, TypeError):
                return (False, f"pending-timer must be numeric, got: {value}")

    return (True, None)
