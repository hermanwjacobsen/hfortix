"""
Validation helpers for web-proxy url_match endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_STATUS = ["enable", "disable"]
VALID_BODY_CACHE_EXEMPTION = ["enable", "disable"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_url_match_get(
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


def validate_url_match_post(
    payload: dict[str, Any],
) -> tuple[bool, str | None]:
    """
    Validate POST request payload for creating url_match.

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

    # Validate status if present
    if "status" in payload:
        value = payload.get("status")
        if value and value not in VALID_BODY_STATUS:
            return (
                False,
                f"Invalid status '{value}'. Must be one of: {', '.join(VALID_BODY_STATUS)}",
            )

    # Validate url-pattern if present
    if "url-pattern" in payload:
        value = payload.get("url-pattern")
        if value and isinstance(value, str) and len(value) > 511:
            return (False, "url-pattern cannot exceed 511 characters")

    # Validate forward-server if present
    if "forward-server" in payload:
        value = payload.get("forward-server")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "forward-server cannot exceed 63 characters")

    # Validate fast-fallback if present
    if "fast-fallback" in payload:
        value = payload.get("fast-fallback")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "fast-fallback cannot exceed 63 characters")

    # Validate cache-exemption if present
    if "cache-exemption" in payload:
        value = payload.get("cache-exemption")
        if value and value not in VALID_BODY_CACHE_EXEMPTION:
            return (
                False,
                f"Invalid cache-exemption '{value}'. Must be one of: {', '.join(VALID_BODY_CACHE_EXEMPTION)}",
            )

    # Validate comment if present
    if "comment" in payload:
        value = payload.get("comment")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "comment cannot exceed 255 characters")

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_url_match_put(
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

    # Validate status if present
    if "status" in payload:
        value = payload.get("status")
        if value and value not in VALID_BODY_STATUS:
            return (
                False,
                f"Invalid status '{value}'. Must be one of: {', '.join(VALID_BODY_STATUS)}",
            )

    # Validate url-pattern if present
    if "url-pattern" in payload:
        value = payload.get("url-pattern")
        if value and isinstance(value, str) and len(value) > 511:
            return (False, "url-pattern cannot exceed 511 characters")

    # Validate forward-server if present
    if "forward-server" in payload:
        value = payload.get("forward-server")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "forward-server cannot exceed 63 characters")

    # Validate fast-fallback if present
    if "fast-fallback" in payload:
        value = payload.get("fast-fallback")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "fast-fallback cannot exceed 63 characters")

    # Validate cache-exemption if present
    if "cache-exemption" in payload:
        value = payload.get("cache-exemption")
        if value and value not in VALID_BODY_CACHE_EXEMPTION:
            return (
                False,
                f"Invalid cache-exemption '{value}'. Must be one of: {', '.join(VALID_BODY_CACHE_EXEMPTION)}",
            )

    # Validate comment if present
    if "comment" in payload:
        value = payload.get("comment")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "comment cannot exceed 255 characters")

    return (True, None)


# ============================================================================
# DELETE Validation
# ============================================================================


def validate_url_match_delete(
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
