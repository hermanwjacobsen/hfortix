"""
Validation helpers for authentication rule endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_STATUS = ["enable", "disable"]
VALID_BODY_PROTOCOL = ["http", "ftp", "socks", "ssh", "ztna-portal"]
VALID_BODY_IP_BASED = ["enable", "disable"]
VALID_BODY_WEB_AUTH_COOKIE = ["enable", "disable"]
VALID_BODY_CORS_STATEFUL = ["enable", "disable"]
VALID_BODY_CERT_AUTH_COOKIE = ["enable", "disable"]
VALID_BODY_TRANSACTION_BASED = ["enable", "disable"]
VALID_BODY_WEB_PORTAL = ["enable", "disable"]
VALID_BODY_SESSION_LOGOUT = ["enable", "disable"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_rule_get(
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


def validate_rule_post(payload: dict[str, Any]) -> tuple[bool, str | None]:
    """
    Validate POST request payload for creating rule.

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

    # Validate status if present
    if "status" in payload:
        value = payload.get("status")
        if value and value not in VALID_BODY_STATUS:
            return (
                False,
                f"Invalid status '{value}'. Must be one of: {', '.join(VALID_BODY_STATUS)}",
            )

    # Validate protocol if present
    if "protocol" in payload:
        value = payload.get("protocol")
        if value and value not in VALID_BODY_PROTOCOL:
            return (
                False,
                f"Invalid protocol '{value}'. Must be one of: {', '.join(VALID_BODY_PROTOCOL)}",
            )

    # Validate ip-based if present
    if "ip-based" in payload:
        value = payload.get("ip-based")
        if value and value not in VALID_BODY_IP_BASED:
            return (
                False,
                f"Invalid ip-based '{value}'. Must be one of: {', '.join(VALID_BODY_IP_BASED)}",
            )

    # Validate active-auth-method if present
    if "active-auth-method" in payload:
        value = payload.get("active-auth-method")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "active-auth-method cannot exceed 35 characters")

    # Validate sso-auth-method if present
    if "sso-auth-method" in payload:
        value = payload.get("sso-auth-method")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "sso-auth-method cannot exceed 35 characters")

    # Validate web-auth-cookie if present
    if "web-auth-cookie" in payload:
        value = payload.get("web-auth-cookie")
        if value and value not in VALID_BODY_WEB_AUTH_COOKIE:
            return (
                False,
                f"Invalid web-auth-cookie '{value}'. Must be one of: {', '.join(VALID_BODY_WEB_AUTH_COOKIE)}",
            )

    # Validate cors-stateful if present
    if "cors-stateful" in payload:
        value = payload.get("cors-stateful")
        if value and value not in VALID_BODY_CORS_STATEFUL:
            return (
                False,
                f"Invalid cors-stateful '{value}'. Must be one of: {', '.join(VALID_BODY_CORS_STATEFUL)}",
            )

    # Validate cors-depth if present
    if "cors-depth" in payload:
        value = payload.get("cors-depth")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 8:
                    return (False, "cors-depth must be between 1 and 8")
            except (ValueError, TypeError):
                return (False, f"cors-depth must be numeric, got: {value}")

    # Validate cert-auth-cookie if present
    if "cert-auth-cookie" in payload:
        value = payload.get("cert-auth-cookie")
        if value and value not in VALID_BODY_CERT_AUTH_COOKIE:
            return (
                False,
                f"Invalid cert-auth-cookie '{value}'. Must be one of: {', '.join(VALID_BODY_CERT_AUTH_COOKIE)}",
            )

    # Validate transaction-based if present
    if "transaction-based" in payload:
        value = payload.get("transaction-based")
        if value and value not in VALID_BODY_TRANSACTION_BASED:
            return (
                False,
                f"Invalid transaction-based '{value}'. Must be one of: {', '.join(VALID_BODY_TRANSACTION_BASED)}",
            )

    # Validate web-portal if present
    if "web-portal" in payload:
        value = payload.get("web-portal")
        if value and value not in VALID_BODY_WEB_PORTAL:
            return (
                False,
                f"Invalid web-portal '{value}'. Must be one of: {', '.join(VALID_BODY_WEB_PORTAL)}",
            )

    # Validate comments if present
    if "comments" in payload:
        value = payload.get("comments")
        if value and isinstance(value, str) and len(value) > 1023:
            return (False, "comments cannot exceed 1023 characters")

    # Validate session-logout if present
    if "session-logout" in payload:
        value = payload.get("session-logout")
        if value and value not in VALID_BODY_SESSION_LOGOUT:
            return (
                False,
                f"Invalid session-logout '{value}'. Must be one of: {', '.join(VALID_BODY_SESSION_LOGOUT)}",
            )

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_rule_put(
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

    # Validate status if present
    if "status" in payload:
        value = payload.get("status")
        if value and value not in VALID_BODY_STATUS:
            return (
                False,
                f"Invalid status '{value}'. Must be one of: {', '.join(VALID_BODY_STATUS)}",
            )

    # Validate protocol if present
    if "protocol" in payload:
        value = payload.get("protocol")
        if value and value not in VALID_BODY_PROTOCOL:
            return (
                False,
                f"Invalid protocol '{value}'. Must be one of: {', '.join(VALID_BODY_PROTOCOL)}",
            )

    # Validate ip-based if present
    if "ip-based" in payload:
        value = payload.get("ip-based")
        if value and value not in VALID_BODY_IP_BASED:
            return (
                False,
                f"Invalid ip-based '{value}'. Must be one of: {', '.join(VALID_BODY_IP_BASED)}",
            )

    # Validate active-auth-method if present
    if "active-auth-method" in payload:
        value = payload.get("active-auth-method")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "active-auth-method cannot exceed 35 characters")

    # Validate sso-auth-method if present
    if "sso-auth-method" in payload:
        value = payload.get("sso-auth-method")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "sso-auth-method cannot exceed 35 characters")

    # Validate web-auth-cookie if present
    if "web-auth-cookie" in payload:
        value = payload.get("web-auth-cookie")
        if value and value not in VALID_BODY_WEB_AUTH_COOKIE:
            return (
                False,
                f"Invalid web-auth-cookie '{value}'. Must be one of: {', '.join(VALID_BODY_WEB_AUTH_COOKIE)}",
            )

    # Validate cors-stateful if present
    if "cors-stateful" in payload:
        value = payload.get("cors-stateful")
        if value and value not in VALID_BODY_CORS_STATEFUL:
            return (
                False,
                f"Invalid cors-stateful '{value}'. Must be one of: {', '.join(VALID_BODY_CORS_STATEFUL)}",
            )

    # Validate cors-depth if present
    if "cors-depth" in payload:
        value = payload.get("cors-depth")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 8:
                    return (False, "cors-depth must be between 1 and 8")
            except (ValueError, TypeError):
                return (False, f"cors-depth must be numeric, got: {value}")

    # Validate cert-auth-cookie if present
    if "cert-auth-cookie" in payload:
        value = payload.get("cert-auth-cookie")
        if value and value not in VALID_BODY_CERT_AUTH_COOKIE:
            return (
                False,
                f"Invalid cert-auth-cookie '{value}'. Must be one of: {', '.join(VALID_BODY_CERT_AUTH_COOKIE)}",
            )

    # Validate transaction-based if present
    if "transaction-based" in payload:
        value = payload.get("transaction-based")
        if value and value not in VALID_BODY_TRANSACTION_BASED:
            return (
                False,
                f"Invalid transaction-based '{value}'. Must be one of: {', '.join(VALID_BODY_TRANSACTION_BASED)}",
            )

    # Validate web-portal if present
    if "web-portal" in payload:
        value = payload.get("web-portal")
        if value and value not in VALID_BODY_WEB_PORTAL:
            return (
                False,
                f"Invalid web-portal '{value}'. Must be one of: {', '.join(VALID_BODY_WEB_PORTAL)}",
            )

    # Validate comments if present
    if "comments" in payload:
        value = payload.get("comments")
        if value and isinstance(value, str) and len(value) > 1023:
            return (False, "comments cannot exceed 1023 characters")

    # Validate session-logout if present
    if "session-logout" in payload:
        value = payload.get("session-logout")
        if value and value not in VALID_BODY_SESSION_LOGOUT:
            return (
                False,
                f"Invalid session-logout '{value}'. Must be one of: {', '.join(VALID_BODY_SESSION_LOGOUT)}",
            )

    return (True, None)


# ============================================================================
# DELETE Validation
# ============================================================================


def validate_rule_delete(name: str | None = None) -> tuple[bool, str | None]:
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
