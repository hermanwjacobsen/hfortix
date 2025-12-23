"""
Validation helpers for casb user_activity endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_STATUS = ["enable", "disable"]
VALID_BODY_TYPE = ["built-in", "customized"]
VALID_BODY_CATEGORY = [
    "activity-control",
    "tenant-control",
    "domain-control",
    "safe-search-control",
    "advanced-tenant-control",
    "other",
]
VALID_BODY_MATCH_STRATEGY = ["and", "or"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_user_activity_get(
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


def validate_user_activity_post(
    payload: dict[str, Any],
) -> tuple[bool, str | None]:
    """
    Validate POST request payload for creating user_activity.

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

    # Validate uuid if present
    if "uuid" in payload:
        value = payload.get("uuid")
        if value and isinstance(value, str) and len(value) > 36:
            return (False, "uuid cannot exceed 36 characters")

    # Validate status if present
    if "status" in payload:
        value = payload.get("status")
        if value and value not in VALID_BODY_STATUS:
            return (
                False,
                f"Invalid status '{value}'. Must be one of: {', '.join(VALID_BODY_STATUS)}",
            )

    # Validate description if present
    if "description" in payload:
        value = payload.get("description")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "description cannot exceed 63 characters")

    # Validate type if present
    if "type" in payload:
        value = payload.get("type")
        if value and value not in VALID_BODY_TYPE:
            return (
                False,
                f"Invalid type '{value}'. Must be one of: {', '.join(VALID_BODY_TYPE)}",
            )

    # Validate casb-name if present
    if "casb-name" in payload:
        value = payload.get("casb-name")
        if value and isinstance(value, str) and len(value) > 79:
            return (False, "casb-name cannot exceed 79 characters")

    # Validate application if present
    if "application" in payload:
        value = payload.get("application")
        if value and isinstance(value, str) and len(value) > 79:
            return (False, "application cannot exceed 79 characters")

    # Validate category if present
    if "category" in payload:
        value = payload.get("category")
        if value and value not in VALID_BODY_CATEGORY:
            return (
                False,
                f"Invalid category '{value}'. Must be one of: {', '.join(VALID_BODY_CATEGORY)}",
            )

    # Validate match-strategy if present
    if "match-strategy" in payload:
        value = payload.get("match-strategy")
        if value and value not in VALID_BODY_MATCH_STRATEGY:
            return (
                False,
                f"Invalid match-strategy '{value}'. Must be one of: {', '.join(VALID_BODY_MATCH_STRATEGY)}",
            )

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_user_activity_put(
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

    # Validate uuid if present
    if "uuid" in payload:
        value = payload.get("uuid")
        if value and isinstance(value, str) and len(value) > 36:
            return (False, "uuid cannot exceed 36 characters")

    # Validate status if present
    if "status" in payload:
        value = payload.get("status")
        if value and value not in VALID_BODY_STATUS:
            return (
                False,
                f"Invalid status '{value}'. Must be one of: {', '.join(VALID_BODY_STATUS)}",
            )

    # Validate description if present
    if "description" in payload:
        value = payload.get("description")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "description cannot exceed 63 characters")

    # Validate type if present
    if "type" in payload:
        value = payload.get("type")
        if value and value not in VALID_BODY_TYPE:
            return (
                False,
                f"Invalid type '{value}'. Must be one of: {', '.join(VALID_BODY_TYPE)}",
            )

    # Validate casb-name if present
    if "casb-name" in payload:
        value = payload.get("casb-name")
        if value and isinstance(value, str) and len(value) > 79:
            return (False, "casb-name cannot exceed 79 characters")

    # Validate application if present
    if "application" in payload:
        value = payload.get("application")
        if value and isinstance(value, str) and len(value) > 79:
            return (False, "application cannot exceed 79 characters")

    # Validate category if present
    if "category" in payload:
        value = payload.get("category")
        if value and value not in VALID_BODY_CATEGORY:
            return (
                False,
                f"Invalid category '{value}'. Must be one of: {', '.join(VALID_BODY_CATEGORY)}",
            )

    # Validate match-strategy if present
    if "match-strategy" in payload:
        value = payload.get("match-strategy")
        if value and value not in VALID_BODY_MATCH_STRATEGY:
            return (
                False,
                f"Invalid match-strategy '{value}'. Must be one of: {', '.join(VALID_BODY_MATCH_STRATEGY)}",
            )

    return (True, None)


# ============================================================================
# DELETE Validation
# ============================================================================


def validate_user_activity_delete(
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
