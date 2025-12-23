"""
Validation helpers for firewall addrgrp endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_TYPE = ["default", "folder"]
VALID_BODY_CATEGORY = ["default", "ztna-ems-tag", "ztna-geo-tag"]
VALID_BODY_ALLOW_ROUTING = ["enable", "disable"]
VALID_BODY_EXCLUDE = ["enable", "disable"]
VALID_BODY_FABRIC_OBJECT = ["enable", "disable"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_addrgrp_get(
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


def validate_addrgrp_post(payload: dict[str, Any]) -> tuple[bool, str | None]:
    """
    Validate POST request payload for creating addrgrp.

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

    # Validate category if present
    if "category" in payload:
        value = payload.get("category")
        if value and value not in VALID_BODY_CATEGORY:
            return (
                False,
                f"Invalid category '{value}'. Must be one of: {', '.join(VALID_BODY_CATEGORY)}",
            )

    # Validate allow-routing if present
    if "allow-routing" in payload:
        value = payload.get("allow-routing")
        if value and value not in VALID_BODY_ALLOW_ROUTING:
            return (
                False,
                f"Invalid allow-routing '{value}'. Must be one of: {', '.join(VALID_BODY_ALLOW_ROUTING)}",
            )

    # Validate comment if present
    if "comment" in payload:
        value = payload.get("comment")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "comment cannot exceed 255 characters")

    # Validate exclude if present
    if "exclude" in payload:
        value = payload.get("exclude")
        if value and value not in VALID_BODY_EXCLUDE:
            return (
                False,
                f"Invalid exclude '{value}'. Must be one of: {', '.join(VALID_BODY_EXCLUDE)}",
            )

    # Validate color if present
    if "color" in payload:
        value = payload.get("color")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 32:
                    return (False, "color must be between 0 and 32")
            except (ValueError, TypeError):
                return (False, f"color must be numeric, got: {value}")

    # Validate fabric-object if present
    if "fabric-object" in payload:
        value = payload.get("fabric-object")
        if value and value not in VALID_BODY_FABRIC_OBJECT:
            return (
                False,
                f"Invalid fabric-object '{value}'. Must be one of: {', '.join(VALID_BODY_FABRIC_OBJECT)}",
            )

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_addrgrp_put(
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

    # Validate category if present
    if "category" in payload:
        value = payload.get("category")
        if value and value not in VALID_BODY_CATEGORY:
            return (
                False,
                f"Invalid category '{value}'. Must be one of: {', '.join(VALID_BODY_CATEGORY)}",
            )

    # Validate allow-routing if present
    if "allow-routing" in payload:
        value = payload.get("allow-routing")
        if value and value not in VALID_BODY_ALLOW_ROUTING:
            return (
                False,
                f"Invalid allow-routing '{value}'. Must be one of: {', '.join(VALID_BODY_ALLOW_ROUTING)}",
            )

    # Validate comment if present
    if "comment" in payload:
        value = payload.get("comment")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "comment cannot exceed 255 characters")

    # Validate exclude if present
    if "exclude" in payload:
        value = payload.get("exclude")
        if value and value not in VALID_BODY_EXCLUDE:
            return (
                False,
                f"Invalid exclude '{value}'. Must be one of: {', '.join(VALID_BODY_EXCLUDE)}",
            )

    # Validate color if present
    if "color" in payload:
        value = payload.get("color")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 32:
                    return (False, "color must be between 0 and 32")
            except (ValueError, TypeError):
                return (False, f"color must be numeric, got: {value}")

    # Validate fabric-object if present
    if "fabric-object" in payload:
        value = payload.get("fabric-object")
        if value and value not in VALID_BODY_FABRIC_OBJECT:
            return (
                False,
                f"Invalid fabric-object '{value}'. Must be one of: {', '.join(VALID_BODY_FABRIC_OBJECT)}",
            )

    return (True, None)


# ============================================================================
# DELETE Validation
# ============================================================================


def validate_addrgrp_delete(
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
