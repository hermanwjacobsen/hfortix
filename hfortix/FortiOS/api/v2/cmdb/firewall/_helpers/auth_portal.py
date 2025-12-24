"""
Validation helpers for firewall auth_portal endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_PROXY_AUTH = ["enable", "disable"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_auth_portal_get(
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


def validate_auth_portal_put(
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

    # Validate portal-addr if present
    if "portal-addr" in payload:
        value = payload.get("portal-addr")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "portal-addr cannot exceed 63 characters")

    # Validate portal-addr6 if present
    if "portal-addr6" in payload:
        value = payload.get("portal-addr6")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "portal-addr6 cannot exceed 63 characters")

    # Validate identity-based-route if present
    if "identity-based-route" in payload:
        value = payload.get("identity-based-route")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "identity-based-route cannot exceed 35 characters")

    # Validate proxy-auth if present
    if "proxy-auth" in payload:
        value = payload.get("proxy-auth")
        if value and value not in VALID_BODY_PROXY_AUTH:
            return (
                False,
                f"Invalid proxy-auth '{value}'. Must be one of: {', '.join(VALID_BODY_PROXY_AUTH)}",
            )

    return (True, None)
