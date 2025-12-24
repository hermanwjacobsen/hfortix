"""
Validation helpers for system api_user endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_PEER_AUTH = ["enable", "disable"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_api_user_get(
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


def validate_api_user_post(payload: dict[str, Any]) -> tuple[bool, str | None]:
    """
    Validate POST request payload for creating api_user.

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

    # Validate comments if present
    if "comments" in payload:
        value = payload.get("comments")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "comments cannot exceed 255 characters")

    # Validate accprofile if present
    if "accprofile" in payload:
        value = payload.get("accprofile")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "accprofile cannot exceed 35 characters")

    # Validate schedule if present
    if "schedule" in payload:
        value = payload.get("schedule")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "schedule cannot exceed 35 characters")

    # Validate cors-allow-origin if present
    if "cors-allow-origin" in payload:
        value = payload.get("cors-allow-origin")
        if value and isinstance(value, str) and len(value) > 269:
            return (False, "cors-allow-origin cannot exceed 269 characters")

    # Validate peer-auth if present
    if "peer-auth" in payload:
        value = payload.get("peer-auth")
        if value and value not in VALID_BODY_PEER_AUTH:
            return (
                False,
                f"Invalid peer-auth '{value}'. Must be one of: {', '.join(VALID_BODY_PEER_AUTH)}",
            )

    # Validate peer-group if present
    if "peer-group" in payload:
        value = payload.get("peer-group")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "peer-group cannot exceed 35 characters")

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_api_user_put(
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

    # Validate comments if present
    if "comments" in payload:
        value = payload.get("comments")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "comments cannot exceed 255 characters")

    # Validate accprofile if present
    if "accprofile" in payload:
        value = payload.get("accprofile")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "accprofile cannot exceed 35 characters")

    # Validate schedule if present
    if "schedule" in payload:
        value = payload.get("schedule")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "schedule cannot exceed 35 characters")

    # Validate cors-allow-origin if present
    if "cors-allow-origin" in payload:
        value = payload.get("cors-allow-origin")
        if value and isinstance(value, str) and len(value) > 269:
            return (False, "cors-allow-origin cannot exceed 269 characters")

    # Validate peer-auth if present
    if "peer-auth" in payload:
        value = payload.get("peer-auth")
        if value and value not in VALID_BODY_PEER_AUTH:
            return (
                False,
                f"Invalid peer-auth '{value}'. Must be one of: {', '.join(VALID_BODY_PEER_AUTH)}",
            )

    # Validate peer-group if present
    if "peer-group" in payload:
        value = payload.get("peer-group")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "peer-group cannot exceed 35 characters")

    return (True, None)


# ============================================================================
# DELETE Validation
# ============================================================================


def validate_api_user_delete(
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
