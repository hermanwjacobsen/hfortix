"""
Validation helpers for system console endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_OUTPUT = ["standard", "more"]
VALID_BODY_LOGIN = ["enable", "disable"]
VALID_BODY_FORTIEXPLORER = ["enable", "disable"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_console_get(
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


def validate_console_put(
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

    # Validate output if present
    if "output" in payload:
        value = payload.get("output")
        if value and value not in VALID_BODY_OUTPUT:
            return (
                False,
                f"Invalid output '{value}'. Must be one of: {', '.join(VALID_BODY_OUTPUT)}",
            )

    # Validate login if present
    if "login" in payload:
        value = payload.get("login")
        if value and value not in VALID_BODY_LOGIN:
            return (
                False,
                f"Invalid login '{value}'. Must be one of: {', '.join(VALID_BODY_LOGIN)}",
            )

    # Validate fortiexplorer if present
    if "fortiexplorer" in payload:
        value = payload.get("fortiexplorer")
        if value and value not in VALID_BODY_FORTIEXPLORER:
            return (
                False,
                f"Invalid fortiexplorer '{value}'. Must be one of: {', '.join(VALID_BODY_FORTIEXPLORER)}",
            )

    return (True, None)
