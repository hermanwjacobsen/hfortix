"""
Validation helpers for system replacemsg_image endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_IMAGE_TYPE = ["gi", "jpg", "tif", "png"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_replacemsg_image_get(
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


def validate_replacemsg_image_post(
    payload: dict[str, Any],
) -> tuple[bool, str | None]:
    """
    Validate POST request payload for creating replacemsg_image.

    Args:
        payload: The payload to validate

    Returns:
        Tuple of (is_valid, error_message)
    """
    # Validate name if present
    if "name" in payload:
        value = payload.get("name")
        if value and isinstance(value, str) and len(value) > 23:
            return (False, "name cannot exceed 23 characters")

    # Validate image-type if present
    if "image-type" in payload:
        value = payload.get("image-type")
        if value and value not in VALID_BODY_IMAGE_TYPE:
            return (
                False,
                f"Invalid image-type '{value}'. Must be one of: {', '.join(VALID_BODY_IMAGE_TYPE)}",
            )

    # Validate image-base64 if present
    if "image-base64" in payload:
        value = payload.get("image-base64")
        if value and isinstance(value, str) and len(value) > 32768:
            return (False, "image-base64 cannot exceed 32768 characters")

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_replacemsg_image_put(
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
        if value and isinstance(value, str) and len(value) > 23:
            return (False, "name cannot exceed 23 characters")

    # Validate image-type if present
    if "image-type" in payload:
        value = payload.get("image-type")
        if value and value not in VALID_BODY_IMAGE_TYPE:
            return (
                False,
                f"Invalid image-type '{value}'. Must be one of: {', '.join(VALID_BODY_IMAGE_TYPE)}",
            )

    # Validate image-base64 if present
    if "image-base64" in payload:
        value = payload.get("image-base64")
        if value and isinstance(value, str) and len(value) > 32768:
            return (False, "image-base64 cannot exceed 32768 characters")

    return (True, None)


# ============================================================================
# DELETE Validation
# ============================================================================


def validate_replacemsg_image_delete(
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
