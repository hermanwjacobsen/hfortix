"""
Validation helpers for switch-controller igmp_snooping endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_FLOOD_UNKNOWN_MULTICAST = ["enable", "disable"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_igmp_snooping_get(
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


def validate_igmp_snooping_put(
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

    # Validate aging-time if present
    if "aging-time" in payload:
        value = payload.get("aging-time")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 15 or int_val > 3600:
                    return (False, "aging-time must be between 15 and 3600")
            except (ValueError, TypeError):
                return (False, f"aging-time must be numeric, got: {value}")

    # Validate flood-unknown-multicast if present
    if "flood-unknown-multicast" in payload:
        value = payload.get("flood-unknown-multicast")
        if value and value not in VALID_BODY_FLOOD_UNKNOWN_MULTICAST:
            return (
                False,
                f"Invalid flood-unknown-multicast '{value}'. Must be one of: {', '.join(VALID_BODY_FLOOD_UNKNOWN_MULTICAST)}",
            )

    # Validate query-interval if present
    if "query-interval" in payload:
        value = payload.get("query-interval")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 10 or int_val > 1200:
                    return (
                        False,
                        "query-interval must be between 10 and 1200",
                    )
            except (ValueError, TypeError):
                return (False, f"query-interval must be numeric, got: {value}")

    return (True, None)
