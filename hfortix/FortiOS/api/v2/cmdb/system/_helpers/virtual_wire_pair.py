"""
Validation helpers for system virtual_wire_pair endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_WILDCARD_VLAN = ["enable", "disable"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_virtual_wire_pair_get(
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


def validate_virtual_wire_pair_post(
    payload: dict[str, Any],
) -> tuple[bool, str | None]:
    """
    Validate POST request payload for creating virtual_wire_pair.

    Args:
        payload: The payload to validate

    Returns:
        Tuple of (is_valid, error_message)
    """
    # Validate name if present
    if "name" in payload:
        value = payload.get("name")
        if value and isinstance(value, str) and len(value) > 11:
            return (False, "name cannot exceed 11 characters")

    # Validate wildcard-vlan if present
    if "wildcard-vlan" in payload:
        value = payload.get("wildcard-vlan")
        if value and value not in VALID_BODY_WILDCARD_VLAN:
            return (
                False,
                f"Invalid wildcard-vlan '{value}'. Must be one of: {', '.join(VALID_BODY_WILDCARD_VLAN)}",
            )

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_virtual_wire_pair_put(
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
        if value and isinstance(value, str) and len(value) > 11:
            return (False, "name cannot exceed 11 characters")

    # Validate wildcard-vlan if present
    if "wildcard-vlan" in payload:
        value = payload.get("wildcard-vlan")
        if value and value not in VALID_BODY_WILDCARD_VLAN:
            return (
                False,
                f"Invalid wildcard-vlan '{value}'. Must be one of: {', '.join(VALID_BODY_WILDCARD_VLAN)}",
            )

    return (True, None)


# ============================================================================
# DELETE Validation
# ============================================================================


def validate_virtual_wire_pair_delete(
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
