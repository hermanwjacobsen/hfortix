"""
Validation helpers for wireless-controller inter_controller endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_INTER_CONTROLLER_MODE = ["disable", "l2-roaming", "1+1"]
VALID_BODY_L3_ROAMING = ["enable", "disable"]
VALID_BODY_INTER_CONTROLLER_PRI = ["primary", "secondary"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_inter_controller_get(
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


def validate_inter_controller_put(
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

    # Validate inter-controller-mode if present
    if "inter-controller-mode" in payload:
        value = payload.get("inter-controller-mode")
        if value and value not in VALID_BODY_INTER_CONTROLLER_MODE:
            return (
                False,
                f"Invalid inter-controller-mode '{value}'. Must be one of: {', '.join(VALID_BODY_INTER_CONTROLLER_MODE)}",
            )

    # Validate l3-roaming if present
    if "l3-roaming" in payload:
        value = payload.get("l3-roaming")
        if value and value not in VALID_BODY_L3_ROAMING:
            return (
                False,
                f"Invalid l3-roaming '{value}'. Must be one of: {', '.join(VALID_BODY_L3_ROAMING)}",
            )

    # Validate inter-controller-pri if present
    if "inter-controller-pri" in payload:
        value = payload.get("inter-controller-pri")
        if value and value not in VALID_BODY_INTER_CONTROLLER_PRI:
            return (
                False,
                f"Invalid inter-controller-pri '{value}'. Must be one of: {', '.join(VALID_BODY_INTER_CONTROLLER_PRI)}",
            )

    # Validate fast-failover-max if present
    if "fast-failover-max" in payload:
        value = payload.get("fast-failover-max")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 3 or int_val > 64:
                    return (
                        False,
                        "fast-failover-max must be between 3 and 64",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"fast-failover-max must be numeric, got: {value}",
                )

    # Validate fast-failover-wait if present
    if "fast-failover-wait" in payload:
        value = payload.get("fast-failover-wait")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 10 or int_val > 86400:
                    return (
                        False,
                        "fast-failover-wait must be between 10 and 86400",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"fast-failover-wait must be numeric, got: {value}",
                )

    return (True, None)
