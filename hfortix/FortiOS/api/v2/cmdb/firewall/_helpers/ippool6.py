"""
Validation helpers for firewall ippool6 endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_TYPE = ["overload", "nptv6"]
VALID_BODY_NAT46 = ["disable", "enable"]
VALID_BODY_ADD_NAT46_ROUTE = ["disable", "enable"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_ippool6_get(
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


def validate_ippool6_post(payload: dict[str, Any]) -> tuple[bool, str | None]:
    """
    Validate POST request payload for creating ippool6.

    Args:
        payload: The payload to validate

    Returns:
        Tuple of (is_valid, error_message)
    """
    # Validate name if present
    if "name" in payload:
        value = payload.get("name")
        if value and isinstance(value, str) and len(value) > 79:
            return (False, "name cannot exceed 79 characters")

    # Validate type if present
    if "type" in payload:
        value = payload.get("type")
        if value and value not in VALID_BODY_TYPE:
            return (
                False,
                f"Invalid type '{value}'. Must be one of: {', '.join(VALID_BODY_TYPE)}",
            )

    # Validate comments if present
    if "comments" in payload:
        value = payload.get("comments")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "comments cannot exceed 255 characters")

    # Validate nat46 if present
    if "nat46" in payload:
        value = payload.get("nat46")
        if value and value not in VALID_BODY_NAT46:
            return (
                False,
                f"Invalid nat46 '{value}'. Must be one of: {', '.join(VALID_BODY_NAT46)}",
            )

    # Validate add-nat46-route if present
    if "add-nat46-route" in payload:
        value = payload.get("add-nat46-route")
        if value and value not in VALID_BODY_ADD_NAT46_ROUTE:
            return (
                False,
                f"Invalid add-nat46-route '{value}'. Must be one of: {', '.join(VALID_BODY_ADD_NAT46_ROUTE)}",
            )

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_ippool6_put(
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
        if value and isinstance(value, str) and len(value) > 79:
            return (False, "name cannot exceed 79 characters")

    # Validate type if present
    if "type" in payload:
        value = payload.get("type")
        if value and value not in VALID_BODY_TYPE:
            return (
                False,
                f"Invalid type '{value}'. Must be one of: {', '.join(VALID_BODY_TYPE)}",
            )

    # Validate comments if present
    if "comments" in payload:
        value = payload.get("comments")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "comments cannot exceed 255 characters")

    # Validate nat46 if present
    if "nat46" in payload:
        value = payload.get("nat46")
        if value and value not in VALID_BODY_NAT46:
            return (
                False,
                f"Invalid nat46 '{value}'. Must be one of: {', '.join(VALID_BODY_NAT46)}",
            )

    # Validate add-nat46-route if present
    if "add-nat46-route" in payload:
        value = payload.get("add-nat46-route")
        if value and value not in VALID_BODY_ADD_NAT46_ROUTE:
            return (
                False,
                f"Invalid add-nat46-route '{value}'. Must be one of: {', '.join(VALID_BODY_ADD_NAT46_ROUTE)}",
            )

    return (True, None)


# ============================================================================
# DELETE Validation
# ============================================================================


def validate_ippool6_delete(
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
