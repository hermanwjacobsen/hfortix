"""
Validation helpers for system virtual_switch endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_SPAN = ["disable", "enable"]
VALID_BODY_SPAN_DIRECTION = ["rx", "tx", "both"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_virtual_switch_get(
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


def validate_virtual_switch_post(
    payload: dict[str, Any],
) -> tuple[bool, str | None]:
    """
    Validate POST request payload for creating virtual_switch.

    Args:
        payload: The payload to validate

    Returns:
        Tuple of (is_valid, error_message)
    """
    # Validate name if present
    if "name" in payload:
        value = payload.get("name")
        if value and isinstance(value, str) and len(value) > 15:
            return (False, "name cannot exceed 15 characters")

    # Validate physical-switch if present
    if "physical-switch" in payload:
        value = payload.get("physical-switch")
        if value and isinstance(value, str) and len(value) > 15:
            return (False, "physical-switch cannot exceed 15 characters")

    # Validate vlan if present
    if "vlan" in payload:
        value = payload.get("vlan")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (False, "vlan must be between 0 and 4294967295")
            except (ValueError, TypeError):
                return (False, f"vlan must be numeric, got: {value}")

    # Validate span if present
    if "span" in payload:
        value = payload.get("span")
        if value and value not in VALID_BODY_SPAN:
            return (
                False,
                f"Invalid span '{value}'. Must be one of: {', '.join(VALID_BODY_SPAN)}",
            )

    # Validate span-source-port if present
    if "span-source-port" in payload:
        value = payload.get("span-source-port")
        if value and isinstance(value, str) and len(value) > 15:
            return (False, "span-source-port cannot exceed 15 characters")

    # Validate span-dest-port if present
    if "span-dest-port" in payload:
        value = payload.get("span-dest-port")
        if value and isinstance(value, str) and len(value) > 15:
            return (False, "span-dest-port cannot exceed 15 characters")

    # Validate span-direction if present
    if "span-direction" in payload:
        value = payload.get("span-direction")
        if value and value not in VALID_BODY_SPAN_DIRECTION:
            return (
                False,
                f"Invalid span-direction '{value}'. Must be one of: {', '.join(VALID_BODY_SPAN_DIRECTION)}",
            )

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_virtual_switch_put(
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
        if value and isinstance(value, str) and len(value) > 15:
            return (False, "name cannot exceed 15 characters")

    # Validate physical-switch if present
    if "physical-switch" in payload:
        value = payload.get("physical-switch")
        if value and isinstance(value, str) and len(value) > 15:
            return (False, "physical-switch cannot exceed 15 characters")

    # Validate vlan if present
    if "vlan" in payload:
        value = payload.get("vlan")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (False, "vlan must be between 0 and 4294967295")
            except (ValueError, TypeError):
                return (False, f"vlan must be numeric, got: {value}")

    # Validate span if present
    if "span" in payload:
        value = payload.get("span")
        if value and value not in VALID_BODY_SPAN:
            return (
                False,
                f"Invalid span '{value}'. Must be one of: {', '.join(VALID_BODY_SPAN)}",
            )

    # Validate span-source-port if present
    if "span-source-port" in payload:
        value = payload.get("span-source-port")
        if value and isinstance(value, str) and len(value) > 15:
            return (False, "span-source-port cannot exceed 15 characters")

    # Validate span-dest-port if present
    if "span-dest-port" in payload:
        value = payload.get("span-dest-port")
        if value and isinstance(value, str) and len(value) > 15:
            return (False, "span-dest-port cannot exceed 15 characters")

    # Validate span-direction if present
    if "span-direction" in payload:
        value = payload.get("span-direction")
        if value and value not in VALID_BODY_SPAN_DIRECTION:
            return (
                False,
                f"Invalid span-direction '{value}'. Must be one of: {', '.join(VALID_BODY_SPAN_DIRECTION)}",
            )

    return (True, None)


# ============================================================================
# DELETE Validation
# ============================================================================


def validate_virtual_switch_delete(
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
