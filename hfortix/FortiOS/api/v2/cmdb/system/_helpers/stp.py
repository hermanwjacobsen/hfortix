"""
Validation helpers for system stp endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_SWITCH_PRIORITY = [
    "0",
    "4096",
    "8192",
    "12288",
    "16384",
    "20480",
    "24576",
    "28672",
    "32768",
    "36864",
    "40960",
    "45056",
    "49152",
    "53248",
    "57344",
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_stp_get(
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


def validate_stp_put(
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

    # Validate switch-priority if present
    if "switch-priority" in payload:
        value = payload.get("switch-priority")
        if value and value not in VALID_BODY_SWITCH_PRIORITY:
            return (
                False,
                f"Invalid switch-priority '{value}'. Must be one of: {', '.join(VALID_BODY_SWITCH_PRIORITY)}",
            )

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

    # Validate forward-delay if present
    if "forward-delay" in payload:
        value = payload.get("forward-delay")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 4 or int_val > 30:
                    return (False, "forward-delay must be between 4 and 30")
            except (ValueError, TypeError):
                return (False, f"forward-delay must be numeric, got: {value}")

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

    return (True, None)
