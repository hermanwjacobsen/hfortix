"""
Validation helpers for authentication setting endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_PERSISTENT_COOKIE = ["enable", "disable"]
VALID_BODY_IP_AUTH_COOKIE = ["enable", "disable"]
VALID_BODY_CAPTIVE_PORTAL_TYPE = ["fqdn", "ip"]
VALID_BODY_CERT_AUTH = ["enable", "disable"]
VALID_BODY_AUTH_HTTPS = ["enable", "disable"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_setting_get(
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


def validate_setting_put(
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

    # Validate active-auth-scheme if present
    if "active-auth-scheme" in payload:
        value = payload.get("active-auth-scheme")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "active-auth-scheme cannot exceed 35 characters")

    # Validate sso-auth-scheme if present
    if "sso-auth-scheme" in payload:
        value = payload.get("sso-auth-scheme")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "sso-auth-scheme cannot exceed 35 characters")

    # Validate persistent-cookie if present
    if "persistent-cookie" in payload:
        value = payload.get("persistent-cookie")
        if value and value not in VALID_BODY_PERSISTENT_COOKIE:
            return (
                False,
                f"Invalid persistent-cookie '{value}'. Must be one of: {', '.join(VALID_BODY_PERSISTENT_COOKIE)}",
            )

    # Validate ip-auth-cookie if present
    if "ip-auth-cookie" in payload:
        value = payload.get("ip-auth-cookie")
        if value and value not in VALID_BODY_IP_AUTH_COOKIE:
            return (
                False,
                f"Invalid ip-auth-cookie '{value}'. Must be one of: {', '.join(VALID_BODY_IP_AUTH_COOKIE)}",
            )

    # Validate cookie-max-age if present
    if "cookie-max-age" in payload:
        value = payload.get("cookie-max-age")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 30 or int_val > 10080:
                    return (
                        False,
                        "cookie-max-age must be between 30 and 10080",
                    )
            except (ValueError, TypeError):
                return (False, f"cookie-max-age must be numeric, got: {value}")

    # Validate cookie-refresh-div if present
    if "cookie-refresh-div" in payload:
        value = payload.get("cookie-refresh-div")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 2 or int_val > 4:
                    return (
                        False,
                        "cookie-refresh-div must be between 2 and 4",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"cookie-refresh-div must be numeric, got: {value}",
                )

    # Validate captive-portal-type if present
    if "captive-portal-type" in payload:
        value = payload.get("captive-portal-type")
        if value and value not in VALID_BODY_CAPTIVE_PORTAL_TYPE:
            return (
                False,
                f"Invalid captive-portal-type '{value}'. Must be one of: {', '.join(VALID_BODY_CAPTIVE_PORTAL_TYPE)}",
            )

    # Validate captive-portal if present
    if "captive-portal" in payload:
        value = payload.get("captive-portal")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "captive-portal cannot exceed 255 characters")

    # Validate captive-portal6 if present
    if "captive-portal6" in payload:
        value = payload.get("captive-portal6")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "captive-portal6 cannot exceed 255 characters")

    # Validate cert-auth if present
    if "cert-auth" in payload:
        value = payload.get("cert-auth")
        if value and value not in VALID_BODY_CERT_AUTH:
            return (
                False,
                f"Invalid cert-auth '{value}'. Must be one of: {', '.join(VALID_BODY_CERT_AUTH)}",
            )

    # Validate cert-captive-portal if present
    if "cert-captive-portal" in payload:
        value = payload.get("cert-captive-portal")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "cert-captive-portal cannot exceed 255 characters")

    # Validate cert-captive-portal-port if present
    if "cert-captive-portal-port" in payload:
        value = payload.get("cert-captive-portal-port")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 65535:
                    return (
                        False,
                        "cert-captive-portal-port must be between 1 and 65535",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"cert-captive-portal-port must be numeric, got: {value}",
                )

    # Validate captive-portal-port if present
    if "captive-portal-port" in payload:
        value = payload.get("captive-portal-port")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 65535:
                    return (
                        False,
                        "captive-portal-port must be between 1 and 65535",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"captive-portal-port must be numeric, got: {value}",
                )

    # Validate auth-https if present
    if "auth-https" in payload:
        value = payload.get("auth-https")
        if value and value not in VALID_BODY_AUTH_HTTPS:
            return (
                False,
                f"Invalid auth-https '{value}'. Must be one of: {', '.join(VALID_BODY_AUTH_HTTPS)}",
            )

    # Validate captive-portal-ssl-port if present
    if "captive-portal-ssl-port" in payload:
        value = payload.get("captive-portal-ssl-port")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 65535:
                    return (
                        False,
                        "captive-portal-ssl-port must be between 1 and 65535",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"captive-portal-ssl-port must be numeric, got: {value}",
                )

    return (True, None)
