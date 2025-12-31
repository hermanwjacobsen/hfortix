"""
Validation helpers for switch-controller auto_config_default endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_auto_config_default_get(
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


def validate_auto_config_default_put(
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

    # Validate fgt-policy if present
    if "fgt-policy" in payload:
        value = payload.get("fgt-policy")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "fgt-policy cannot exceed 63 characters")

    # Validate isl-policy if present
    if "isl-policy" in payload:
        value = payload.get("isl-policy")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "isl-policy cannot exceed 63 characters")

    # Validate icl-policy if present
    if "icl-policy" in payload:
        value = payload.get("icl-policy")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "icl-policy cannot exceed 63 characters")

    return (True, None)
