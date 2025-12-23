"""
Validation helpers for system ha_monitor endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_MONITOR_VLAN = ["enable", "disable"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_ha_monitor_get(
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


def validate_ha_monitor_put(
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

    # Validate monitor-vlan if present
    if "monitor-vlan" in payload:
        value = payload.get("monitor-vlan")
        if value and value not in VALID_BODY_MONITOR_VLAN:
            return (
                False,
                f"Invalid monitor-vlan '{value}'. Must be one of: {', '.join(VALID_BODY_MONITOR_VLAN)}",
            )

    # Validate vlan-hb-interval if present
    if "vlan-hb-interval" in payload:
        value = payload.get("vlan-hb-interval")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 30:
                    return (
                        False,
                        "vlan-hb-interval must be between 1 and 30",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"vlan-hb-interval must be numeric, got: {value}",
                )

    # Validate vlan-hb-lost-threshold if present
    if "vlan-hb-lost-threshold" in payload:
        value = payload.get("vlan-hb-lost-threshold")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 60:
                    return (
                        False,
                        "vlan-hb-lost-threshold must be between 1 and 60",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"vlan-hb-lost-threshold must be numeric, got: {value}",
                )

    return (True, None)
