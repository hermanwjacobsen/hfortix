"""
Validation helpers for switch-controller storm_control endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_UNKNOWN_UNICAST = ["enable", "disable"]
VALID_BODY_UNKNOWN_MULTICAST = ["enable", "disable"]
VALID_BODY_BROADCAST = ["enable", "disable"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_storm_control_get(
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


def validate_storm_control_put(
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

    # Validate rate if present
    if "rate" in payload:
        value = payload.get("rate")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 10000000:
                    return (False, "rate must be between 0 and 10000000")
            except (ValueError, TypeError):
                return (False, f"rate must be numeric, got: {value}")

    # Validate burst-size-level if present
    if "burst-size-level" in payload:
        value = payload.get("burst-size-level")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4:
                    return (False, "burst-size-level must be between 0 and 4")
            except (ValueError, TypeError):
                return (
                    False,
                    f"burst-size-level must be numeric, got: {value}",
                )

    # Validate unknown-unicast if present
    if "unknown-unicast" in payload:
        value = payload.get("unknown-unicast")
        if value and value not in VALID_BODY_UNKNOWN_UNICAST:
            return (
                False,
                f"Invalid unknown-unicast '{value}'. Must be one of: {', '.join(VALID_BODY_UNKNOWN_UNICAST)}",
            )

    # Validate unknown-multicast if present
    if "unknown-multicast" in payload:
        value = payload.get("unknown-multicast")
        if value and value not in VALID_BODY_UNKNOWN_MULTICAST:
            return (
                False,
                f"Invalid unknown-multicast '{value}'. Must be one of: {', '.join(VALID_BODY_UNKNOWN_MULTICAST)}",
            )

    # Validate broadcast if present
    if "broadcast" in payload:
        value = payload.get("broadcast")
        if value and value not in VALID_BODY_BROADCAST:
            return (
                False,
                f"Invalid broadcast '{value}'. Must be one of: {', '.join(VALID_BODY_BROADCAST)}",
            )

    return (True, None)
