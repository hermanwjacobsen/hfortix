"""
Validation helpers for log gui_display endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_RESOLVE_HOSTS = ["enable", "disable"]
VALID_BODY_RESOLVE_APPS = ["enable", "disable"]
VALID_BODY_FORTIVIEW_UNSCANNED_APPS = ["enable", "disable"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_gui_display_get(
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
# PUT Validation
# ============================================================================


def validate_gui_display_put(
    payload: dict[str, Any] | None = None,
) -> tuple[bool, str | None]:
    """
    Validate PUT request payload for updating {endpoint_name}.

    Args:
        payload: The payload to validate

    Returns:
        Tuple of (is_valid, error_message)
    """
    # If no payload provided, nothing to validate
    if not payload:
        return (True, None)

    # Validate resolve-hosts if present
    if "resolve-hosts" in payload:
        value = payload.get("resolve-hosts")
        if value and value not in VALID_BODY_RESOLVE_HOSTS:
            return (
                False,
                f"Invalid resolve-hosts '{value}'. Must be one of: {', '.join(VALID_BODY_RESOLVE_HOSTS)}",
            )

    # Validate resolve-apps if present
    if "resolve-apps" in payload:
        value = payload.get("resolve-apps")
        if value and value not in VALID_BODY_RESOLVE_APPS:
            return (
                False,
                f"Invalid resolve-apps '{value}'. Must be one of: {', '.join(VALID_BODY_RESOLVE_APPS)}",
            )

    # Validate fortiview-unscanned-apps if present
    if "fortiview-unscanned-apps" in payload:
        value = payload.get("fortiview-unscanned-apps")
        if value and value not in VALID_BODY_FORTIVIEW_UNSCANNED_APPS:
            return (
                False,
                f"Invalid fortiview-unscanned-apps '{value}'. Must be one of: {', '.join(VALID_BODY_FORTIVIEW_UNSCANNED_APPS)}",
            )

    return (True, None)
