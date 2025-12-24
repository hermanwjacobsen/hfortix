"""
Validation helpers for system automation_condition endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_CONDITION_TYPE = ["cpu", "memory", "vpn"]
VALID_BODY_VPN_TUNNEL_STATE = ["tunnel-up", "tunnel-down"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_automation_condition_get(
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


def validate_automation_condition_post(
    payload: dict[str, Any],
) -> tuple[bool, str | None]:
    """
    Validate POST request payload for creating automation_condition.

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

    # Validate description if present
    if "description" in payload:
        value = payload.get("description")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "description cannot exceed 255 characters")

    # Validate condition-type if present
    if "condition-type" in payload:
        value = payload.get("condition-type")
        if value and value not in VALID_BODY_CONDITION_TYPE:
            return (
                False,
                f"Invalid condition-type '{value}'. Must be one of: {', '.join(VALID_BODY_CONDITION_TYPE)}",
            )

    # Validate cpu-usage-percent if present
    if "cpu-usage-percent" in payload:
        value = payload.get("cpu-usage-percent")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 100:
                    return (
                        False,
                        "cpu-usage-percent must be between 0 and 100",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"cpu-usage-percent must be numeric, got: {value}",
                )

    # Validate mem-usage-percent if present
    if "mem-usage-percent" in payload:
        value = payload.get("mem-usage-percent")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 100:
                    return (
                        False,
                        "mem-usage-percent must be between 0 and 100",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"mem-usage-percent must be numeric, got: {value}",
                )

    # Validate vdom if present
    if "vdom" in payload:
        value = payload.get("vdom")
        if value and isinstance(value, str) and len(value) > 31:
            return (False, "vdom cannot exceed 31 characters")

    # Validate vpn-tunnel-name if present
    if "vpn-tunnel-name" in payload:
        value = payload.get("vpn-tunnel-name")
        if value and isinstance(value, str) and len(value) > 79:
            return (False, "vpn-tunnel-name cannot exceed 79 characters")

    # Validate vpn-tunnel-state if present
    if "vpn-tunnel-state" in payload:
        value = payload.get("vpn-tunnel-state")
        if value and value not in VALID_BODY_VPN_TUNNEL_STATE:
            return (
                False,
                f"Invalid vpn-tunnel-state '{value}'. Must be one of: {', '.join(VALID_BODY_VPN_TUNNEL_STATE)}",
            )

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_automation_condition_put(
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

    # Validate description if present
    if "description" in payload:
        value = payload.get("description")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "description cannot exceed 255 characters")

    # Validate condition-type if present
    if "condition-type" in payload:
        value = payload.get("condition-type")
        if value and value not in VALID_BODY_CONDITION_TYPE:
            return (
                False,
                f"Invalid condition-type '{value}'. Must be one of: {', '.join(VALID_BODY_CONDITION_TYPE)}",
            )

    # Validate cpu-usage-percent if present
    if "cpu-usage-percent" in payload:
        value = payload.get("cpu-usage-percent")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 100:
                    return (
                        False,
                        "cpu-usage-percent must be between 0 and 100",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"cpu-usage-percent must be numeric, got: {value}",
                )

    # Validate mem-usage-percent if present
    if "mem-usage-percent" in payload:
        value = payload.get("mem-usage-percent")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 100:
                    return (
                        False,
                        "mem-usage-percent must be between 0 and 100",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"mem-usage-percent must be numeric, got: {value}",
                )

    # Validate vdom if present
    if "vdom" in payload:
        value = payload.get("vdom")
        if value and isinstance(value, str) and len(value) > 31:
            return (False, "vdom cannot exceed 31 characters")

    # Validate vpn-tunnel-name if present
    if "vpn-tunnel-name" in payload:
        value = payload.get("vpn-tunnel-name")
        if value and isinstance(value, str) and len(value) > 79:
            return (False, "vpn-tunnel-name cannot exceed 79 characters")

    # Validate vpn-tunnel-state if present
    if "vpn-tunnel-state" in payload:
        value = payload.get("vpn-tunnel-state")
        if value and value not in VALID_BODY_VPN_TUNNEL_STATE:
            return (
                False,
                f"Invalid vpn-tunnel-state '{value}'. Must be one of: {', '.join(VALID_BODY_VPN_TUNNEL_STATE)}",
            )

    return (True, None)


# ============================================================================
# DELETE Validation
# ============================================================================


def validate_automation_condition_delete(
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
