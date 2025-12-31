"""
Validation helpers for router multicast endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_MULTICAST_ROUTING = ["enable", "disable"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_multicast_get(
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


def validate_multicast_put(
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

    # Validate route-threshold if present
    if "route-threshold" in payload:
        value = payload.get("route-threshold")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 2147483647:
                    return (
                        False,
                        "route-threshold must be between 1 and 2147483647",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"route-threshold must be numeric, got: {value}",
                )

    # Validate route-limit if present
    if "route-limit" in payload:
        value = payload.get("route-limit")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 2147483647:
                    return (
                        False,
                        "route-limit must be between 1 and 2147483647",
                    )
            except (ValueError, TypeError):
                return (False, f"route-limit must be numeric, got: {value}")

    # Validate multicast-routing if present
    if "multicast-routing" in payload:
        value = payload.get("multicast-routing")
        if value and value not in VALID_BODY_MULTICAST_ROUTING:
            return (
                False,
                f"Invalid multicast-routing '{value}'. Must be one of: {', '.join(VALID_BODY_MULTICAST_ROUTING)}",
            )

    return (True, None)
