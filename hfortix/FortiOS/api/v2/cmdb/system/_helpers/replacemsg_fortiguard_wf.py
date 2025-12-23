"""
Validation helpers for system replacemsg_fortiguard_wf endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_HEADER = ["none", "http", "8bit"]
VALID_BODY_FORMAT = ["none", "text", "html"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_replacemsg_fortiguard_wf_get(
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


def validate_replacemsg_fortiguard_wf_post(
    payload: dict[str, Any],
) -> tuple[bool, str | None]:
    """
    Validate POST request payload for creating replacemsg_fortiguard_wf.

    Args:
        payload: The payload to validate

    Returns:
        Tuple of (is_valid, error_message)
    """
    # Validate msg-type if present
    if "msg-type" in payload:
        value = payload.get("msg-type")
        if value and isinstance(value, str) and len(value) > 28:
            return (False, "msg-type cannot exceed 28 characters")

    # Validate buffer if present
    if "buffer" in payload:
        value = payload.get("buffer")
        if value and isinstance(value, str) and len(value) > 32768:
            return (False, "buffer cannot exceed 32768 characters")

    # Validate header if present
    if "header" in payload:
        value = payload.get("header")
        if value and value not in VALID_BODY_HEADER:
            return (
                False,
                f"Invalid header '{value}'. Must be one of: {', '.join(VALID_BODY_HEADER)}",
            )

    # Validate format if present
    if "format" in payload:
        value = payload.get("format")
        if value and value not in VALID_BODY_FORMAT:
            return (
                False,
                f"Invalid format '{value}'. Must be one of: {', '.join(VALID_BODY_FORMAT)}",
            )

    return (True, None)
