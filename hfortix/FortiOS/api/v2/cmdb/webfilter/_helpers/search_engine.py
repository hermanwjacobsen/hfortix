"""
Validation helpers for webfilter search_engine endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_SAFESEARCH = [
    "disable",
    "url",
    "header",
    "translate",
    "yt-pattern",
    "yt-scan",
    "yt-video",
    "yt-channel",
]
VALID_BODY_CHARSET = ["utf-8", "gb2312"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_search_engine_get(
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


def validate_search_engine_post(
    payload: dict[str, Any],
) -> tuple[bool, str | None]:
    """
    Validate POST request payload for creating search_engine.

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

    # Validate hostname if present
    if "hostname" in payload:
        value = payload.get("hostname")
        if value and isinstance(value, str) and len(value) > 127:
            return (False, "hostname cannot exceed 127 characters")

    # Validate url if present
    if "url" in payload:
        value = payload.get("url")
        if value and isinstance(value, str) and len(value) > 127:
            return (False, "url cannot exceed 127 characters")

    # Validate query if present
    if "query" in payload:
        value = payload.get("query")
        if value and isinstance(value, str) and len(value) > 15:
            return (False, "query cannot exceed 15 characters")

    # Validate safesearch if present
    if "safesearch" in payload:
        value = payload.get("safesearch")
        if value and value not in VALID_BODY_SAFESEARCH:
            return (
                False,
                f"Invalid safesearch '{value}'. Must be one of: {', '.join(VALID_BODY_SAFESEARCH)}",
            )

    # Validate charset if present
    if "charset" in payload:
        value = payload.get("charset")
        if value and value not in VALID_BODY_CHARSET:
            return (
                False,
                f"Invalid charset '{value}'. Must be one of: {', '.join(VALID_BODY_CHARSET)}",
            )

    # Validate safesearch-str if present
    if "safesearch-str" in payload:
        value = payload.get("safesearch-str")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "safesearch-str cannot exceed 255 characters")

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_search_engine_put(
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

    # Validate hostname if present
    if "hostname" in payload:
        value = payload.get("hostname")
        if value and isinstance(value, str) and len(value) > 127:
            return (False, "hostname cannot exceed 127 characters")

    # Validate url if present
    if "url" in payload:
        value = payload.get("url")
        if value and isinstance(value, str) and len(value) > 127:
            return (False, "url cannot exceed 127 characters")

    # Validate query if present
    if "query" in payload:
        value = payload.get("query")
        if value and isinstance(value, str) and len(value) > 15:
            return (False, "query cannot exceed 15 characters")

    # Validate safesearch if present
    if "safesearch" in payload:
        value = payload.get("safesearch")
        if value and value not in VALID_BODY_SAFESEARCH:
            return (
                False,
                f"Invalid safesearch '{value}'. Must be one of: {', '.join(VALID_BODY_SAFESEARCH)}",
            )

    # Validate charset if present
    if "charset" in payload:
        value = payload.get("charset")
        if value and value not in VALID_BODY_CHARSET:
            return (
                False,
                f"Invalid charset '{value}'. Must be one of: {', '.join(VALID_BODY_CHARSET)}",
            )

    # Validate safesearch-str if present
    if "safesearch-str" in payload:
        value = payload.get("safesearch-str")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "safesearch-str cannot exceed 255 characters")

    return (True, None)


# ============================================================================
# DELETE Validation
# ============================================================================


def validate_search_engine_delete(
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
