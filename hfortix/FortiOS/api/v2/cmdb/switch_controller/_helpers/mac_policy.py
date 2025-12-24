"""
Validation helpers for switch-controller mac_policy endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_COUNT = ["disable", "enable"]
VALID_BODY_BOUNCE_PORT_LINK = ["disable", "enable"]
VALID_BODY_POE_RESET = ["disable", "enable"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_mac_policy_get(
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


def validate_mac_policy_post(
    payload: dict[str, Any],
) -> tuple[bool, str | None]:
    """
    Validate POST request payload for creating mac_policy.

    Args:
        payload: The payload to validate

    Returns:
        Tuple of (is_valid, error_message)
    """
    # Validate name if present
    if "name" in payload:
        value = payload.get("name")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "name cannot exceed 63 characters")

    # Validate description if present
    if "description" in payload:
        value = payload.get("description")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "description cannot exceed 63 characters")

    # Validate fortilink if present
    if "fortilink" in payload:
        value = payload.get("fortilink")
        if value and isinstance(value, str) and len(value) > 15:
            return (False, "fortilink cannot exceed 15 characters")

    # Validate vlan if present
    if "vlan" in payload:
        value = payload.get("vlan")
        if value and isinstance(value, str) and len(value) > 15:
            return (False, "vlan cannot exceed 15 characters")

    # Validate traffic-policy if present
    if "traffic-policy" in payload:
        value = payload.get("traffic-policy")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "traffic-policy cannot exceed 63 characters")

    # Validate count if present
    if "count" in payload:
        value = payload.get("count")
        if value and value not in VALID_BODY_COUNT:
            return (
                False,
                f"Invalid count '{value}'. Must be one of: {', '.join(VALID_BODY_COUNT)}",
            )

    # Validate bounce-port-link if present
    if "bounce-port-link" in payload:
        value = payload.get("bounce-port-link")
        if value and value not in VALID_BODY_BOUNCE_PORT_LINK:
            return (
                False,
                f"Invalid bounce-port-link '{value}'. Must be one of: {', '.join(VALID_BODY_BOUNCE_PORT_LINK)}",
            )

    # Validate bounce-port-duration if present
    if "bounce-port-duration" in payload:
        value = payload.get("bounce-port-duration")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 30:
                    return (
                        False,
                        "bounce-port-duration must be between 1 and 30",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"bounce-port-duration must be numeric, got: {value}",
                )

    # Validate poe-reset if present
    if "poe-reset" in payload:
        value = payload.get("poe-reset")
        if value and value not in VALID_BODY_POE_RESET:
            return (
                False,
                f"Invalid poe-reset '{value}'. Must be one of: {', '.join(VALID_BODY_POE_RESET)}",
            )

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_mac_policy_put(
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
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "name cannot exceed 63 characters")

    # Validate description if present
    if "description" in payload:
        value = payload.get("description")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "description cannot exceed 63 characters")

    # Validate fortilink if present
    if "fortilink" in payload:
        value = payload.get("fortilink")
        if value and isinstance(value, str) and len(value) > 15:
            return (False, "fortilink cannot exceed 15 characters")

    # Validate vlan if present
    if "vlan" in payload:
        value = payload.get("vlan")
        if value and isinstance(value, str) and len(value) > 15:
            return (False, "vlan cannot exceed 15 characters")

    # Validate traffic-policy if present
    if "traffic-policy" in payload:
        value = payload.get("traffic-policy")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "traffic-policy cannot exceed 63 characters")

    # Validate count if present
    if "count" in payload:
        value = payload.get("count")
        if value and value not in VALID_BODY_COUNT:
            return (
                False,
                f"Invalid count '{value}'. Must be one of: {', '.join(VALID_BODY_COUNT)}",
            )

    # Validate bounce-port-link if present
    if "bounce-port-link" in payload:
        value = payload.get("bounce-port-link")
        if value and value not in VALID_BODY_BOUNCE_PORT_LINK:
            return (
                False,
                f"Invalid bounce-port-link '{value}'. Must be one of: {', '.join(VALID_BODY_BOUNCE_PORT_LINK)}",
            )

    # Validate bounce-port-duration if present
    if "bounce-port-duration" in payload:
        value = payload.get("bounce-port-duration")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 30:
                    return (
                        False,
                        "bounce-port-duration must be between 1 and 30",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"bounce-port-duration must be numeric, got: {value}",
                )

    # Validate poe-reset if present
    if "poe-reset" in payload:
        value = payload.get("poe-reset")
        if value and value not in VALID_BODY_POE_RESET:
            return (
                False,
                f"Invalid poe-reset '{value}'. Must be one of: {', '.join(VALID_BODY_POE_RESET)}",
            )

    return (True, None)


# ============================================================================
# DELETE Validation
# ============================================================================


def validate_mac_policy_delete(
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
