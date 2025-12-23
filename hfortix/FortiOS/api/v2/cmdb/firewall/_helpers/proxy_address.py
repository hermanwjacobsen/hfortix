"""
Validation helpers for firewall proxy_address endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_TYPE = [
    "host-regex",
    "url",
    "category",
    "method",
    "ua",
    "header",
    "src-advanced",
    "dst-advanced",
    "saas",
]
VALID_BODY_REFERRER = ["enable", "disable"]
VALID_BODY_METHOD = [
    "get",
    "post",
    "put",
    "head",
    "connect",
    "trace",
    "options",
    "delete",
    "update",
    "patch",
    "other",
]
VALID_BODY_UA = ["chrome", "ms", "firefox", "safari", "ie", "edge", "other"]
VALID_BODY_CASE_SENSITIVITY = ["disable", "enable"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_proxy_address_get(
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


def validate_proxy_address_post(
    payload: dict[str, Any],
) -> tuple[bool, str | None]:
    """
    Validate POST request payload for creating proxy_address.

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

    # Validate host if present
    if "host" in payload:
        value = payload.get("host")
        if value and isinstance(value, str) and len(value) > 79:
            return (False, "host cannot exceed 79 characters")

    # Validate host-regex if present
    if "host-regex" in payload:
        value = payload.get("host-regex")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "host-regex cannot exceed 255 characters")

    # Validate path if present
    if "path" in payload:
        value = payload.get("path")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "path cannot exceed 255 characters")

    # Validate query if present
    if "query" in payload:
        value = payload.get("query")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "query cannot exceed 255 characters")

    # Validate referrer if present
    if "referrer" in payload:
        value = payload.get("referrer")
        if value and value not in VALID_BODY_REFERRER:
            return (
                False,
                f"Invalid referrer '{value}'. Must be one of: {', '.join(VALID_BODY_REFERRER)}",
            )

    # Validate method if present
    if "method" in payload:
        value = payload.get("method")
        if value and value not in VALID_BODY_METHOD:
            return (
                False,
                f"Invalid method '{value}'. Must be one of: {', '.join(VALID_BODY_METHOD)}",
            )

    # Validate ua if present
    if "ua" in payload:
        value = payload.get("ua")
        if value and value not in VALID_BODY_UA:
            return (
                False,
                f"Invalid ua '{value}'. Must be one of: {', '.join(VALID_BODY_UA)}",
            )

    # Validate ua-min-ver if present
    if "ua-min-ver" in payload:
        value = payload.get("ua-min-ver")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "ua-min-ver cannot exceed 63 characters")

    # Validate ua-max-ver if present
    if "ua-max-ver" in payload:
        value = payload.get("ua-max-ver")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "ua-max-ver cannot exceed 63 characters")

    # Validate header-name if present
    if "header-name" in payload:
        value = payload.get("header-name")
        if value and isinstance(value, str) and len(value) > 79:
            return (False, "header-name cannot exceed 79 characters")

    # Validate header if present
    if "header" in payload:
        value = payload.get("header")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "header cannot exceed 255 characters")

    # Validate case-sensitivity if present
    if "case-sensitivity" in payload:
        value = payload.get("case-sensitivity")
        if value and value not in VALID_BODY_CASE_SENSITIVITY:
            return (
                False,
                f"Invalid case-sensitivity '{value}'. Must be one of: {', '.join(VALID_BODY_CASE_SENSITIVITY)}",
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

    # Validate comment if present
    if "comment" in payload:
        value = payload.get("comment")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "comment cannot exceed 255 characters")

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_proxy_address_put(
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

    # Validate host if present
    if "host" in payload:
        value = payload.get("host")
        if value and isinstance(value, str) and len(value) > 79:
            return (False, "host cannot exceed 79 characters")

    # Validate host-regex if present
    if "host-regex" in payload:
        value = payload.get("host-regex")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "host-regex cannot exceed 255 characters")

    # Validate path if present
    if "path" in payload:
        value = payload.get("path")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "path cannot exceed 255 characters")

    # Validate query if present
    if "query" in payload:
        value = payload.get("query")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "query cannot exceed 255 characters")

    # Validate referrer if present
    if "referrer" in payload:
        value = payload.get("referrer")
        if value and value not in VALID_BODY_REFERRER:
            return (
                False,
                f"Invalid referrer '{value}'. Must be one of: {', '.join(VALID_BODY_REFERRER)}",
            )

    # Validate method if present
    if "method" in payload:
        value = payload.get("method")
        if value and value not in VALID_BODY_METHOD:
            return (
                False,
                f"Invalid method '{value}'. Must be one of: {', '.join(VALID_BODY_METHOD)}",
            )

    # Validate ua if present
    if "ua" in payload:
        value = payload.get("ua")
        if value and value not in VALID_BODY_UA:
            return (
                False,
                f"Invalid ua '{value}'. Must be one of: {', '.join(VALID_BODY_UA)}",
            )

    # Validate ua-min-ver if present
    if "ua-min-ver" in payload:
        value = payload.get("ua-min-ver")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "ua-min-ver cannot exceed 63 characters")

    # Validate ua-max-ver if present
    if "ua-max-ver" in payload:
        value = payload.get("ua-max-ver")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "ua-max-ver cannot exceed 63 characters")

    # Validate header-name if present
    if "header-name" in payload:
        value = payload.get("header-name")
        if value and isinstance(value, str) and len(value) > 79:
            return (False, "header-name cannot exceed 79 characters")

    # Validate header if present
    if "header" in payload:
        value = payload.get("header")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "header cannot exceed 255 characters")

    # Validate case-sensitivity if present
    if "case-sensitivity" in payload:
        value = payload.get("case-sensitivity")
        if value and value not in VALID_BODY_CASE_SENSITIVITY:
            return (
                False,
                f"Invalid case-sensitivity '{value}'. Must be one of: {', '.join(VALID_BODY_CASE_SENSITIVITY)}",
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

    # Validate comment if present
    if "comment" in payload:
        value = payload.get("comment")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "comment cannot exceed 255 characters")

    return (True, None)


# ============================================================================
# DELETE Validation
# ============================================================================


def validate_proxy_address_delete(
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
