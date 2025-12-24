"""
Validation helpers for web-proxy profile endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_HEADER_CLIENT_IP = ["pass", "add", "remove"]
VALID_BODY_HEADER_VIA_REQUEST = ["pass", "add", "remove"]
VALID_BODY_HEADER_VIA_RESPONSE = ["pass", "add", "remove"]
VALID_BODY_HEADER_CLIENT_CERT = ["pass", "add", "remove"]
VALID_BODY_HEADER_X_FORWARDED_FOR = ["pass", "add", "remove"]
VALID_BODY_HEADER_X_FORWARDED_CLIENT_CERT = ["pass", "add", "remove"]
VALID_BODY_HEADER_FRONT_END_HTTPS = ["pass", "add", "remove"]
VALID_BODY_HEADER_X_AUTHENTICATED_USER = ["pass", "add", "remove"]
VALID_BODY_HEADER_X_AUTHENTICATED_GROUPS = ["pass", "add", "remove"]
VALID_BODY_STRIP_ENCODING = ["enable", "disable"]
VALID_BODY_LOG_HEADER_CHANGE = ["enable", "disable"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_profile_get(
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


def validate_profile_post(payload: dict[str, Any]) -> tuple[bool, str | None]:
    """
    Validate POST request payload for creating profile.

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

    # Validate header-client-ip if present
    if "header-client-ip" in payload:
        value = payload.get("header-client-ip")
        if value and value not in VALID_BODY_HEADER_CLIENT_IP:
            return (
                False,
                f"Invalid header-client-ip '{value}'. Must be one of: {', '.join(VALID_BODY_HEADER_CLIENT_IP)}",
            )

    # Validate header-via-request if present
    if "header-via-request" in payload:
        value = payload.get("header-via-request")
        if value and value not in VALID_BODY_HEADER_VIA_REQUEST:
            return (
                False,
                f"Invalid header-via-request '{value}'. Must be one of: {', '.join(VALID_BODY_HEADER_VIA_REQUEST)}",
            )

    # Validate header-via-response if present
    if "header-via-response" in payload:
        value = payload.get("header-via-response")
        if value and value not in VALID_BODY_HEADER_VIA_RESPONSE:
            return (
                False,
                f"Invalid header-via-response '{value}'. Must be one of: {', '.join(VALID_BODY_HEADER_VIA_RESPONSE)}",
            )

    # Validate header-client-cert if present
    if "header-client-cert" in payload:
        value = payload.get("header-client-cert")
        if value and value not in VALID_BODY_HEADER_CLIENT_CERT:
            return (
                False,
                f"Invalid header-client-cert '{value}'. Must be one of: {', '.join(VALID_BODY_HEADER_CLIENT_CERT)}",
            )

    # Validate header-x-forwarded-for if present
    if "header-x-forwarded-for" in payload:
        value = payload.get("header-x-forwarded-for")
        if value and value not in VALID_BODY_HEADER_X_FORWARDED_FOR:
            return (
                False,
                f"Invalid header-x-forwarded-for '{value}'. Must be one of: {', '.join(VALID_BODY_HEADER_X_FORWARDED_FOR)}",
            )

    # Validate header-x-forwarded-client-cert if present
    if "header-x-forwarded-client-cert" in payload:
        value = payload.get("header-x-forwarded-client-cert")
        if value and value not in VALID_BODY_HEADER_X_FORWARDED_CLIENT_CERT:
            return (
                False,
                f"Invalid header-x-forwarded-client-cert '{value}'. Must be one of: {', '.join(VALID_BODY_HEADER_X_FORWARDED_CLIENT_CERT)}",
            )

    # Validate header-front-end-https if present
    if "header-front-end-https" in payload:
        value = payload.get("header-front-end-https")
        if value and value not in VALID_BODY_HEADER_FRONT_END_HTTPS:
            return (
                False,
                f"Invalid header-front-end-https '{value}'. Must be one of: {', '.join(VALID_BODY_HEADER_FRONT_END_HTTPS)}",
            )

    # Validate header-x-authenticated-user if present
    if "header-x-authenticated-user" in payload:
        value = payload.get("header-x-authenticated-user")
        if value and value not in VALID_BODY_HEADER_X_AUTHENTICATED_USER:
            return (
                False,
                f"Invalid header-x-authenticated-user '{value}'. Must be one of: {', '.join(VALID_BODY_HEADER_X_AUTHENTICATED_USER)}",
            )

    # Validate header-x-authenticated-groups if present
    if "header-x-authenticated-groups" in payload:
        value = payload.get("header-x-authenticated-groups")
        if value and value not in VALID_BODY_HEADER_X_AUTHENTICATED_GROUPS:
            return (
                False,
                f"Invalid header-x-authenticated-groups '{value}'. Must be one of: {', '.join(VALID_BODY_HEADER_X_AUTHENTICATED_GROUPS)}",
            )

    # Validate strip-encoding if present
    if "strip-encoding" in payload:
        value = payload.get("strip-encoding")
        if value and value not in VALID_BODY_STRIP_ENCODING:
            return (
                False,
                f"Invalid strip-encoding '{value}'. Must be one of: {', '.join(VALID_BODY_STRIP_ENCODING)}",
            )

    # Validate log-header-change if present
    if "log-header-change" in payload:
        value = payload.get("log-header-change")
        if value and value not in VALID_BODY_LOG_HEADER_CHANGE:
            return (
                False,
                f"Invalid log-header-change '{value}'. Must be one of: {', '.join(VALID_BODY_LOG_HEADER_CHANGE)}",
            )

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_profile_put(
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

    # Validate header-client-ip if present
    if "header-client-ip" in payload:
        value = payload.get("header-client-ip")
        if value and value not in VALID_BODY_HEADER_CLIENT_IP:
            return (
                False,
                f"Invalid header-client-ip '{value}'. Must be one of: {', '.join(VALID_BODY_HEADER_CLIENT_IP)}",
            )

    # Validate header-via-request if present
    if "header-via-request" in payload:
        value = payload.get("header-via-request")
        if value and value not in VALID_BODY_HEADER_VIA_REQUEST:
            return (
                False,
                f"Invalid header-via-request '{value}'. Must be one of: {', '.join(VALID_BODY_HEADER_VIA_REQUEST)}",
            )

    # Validate header-via-response if present
    if "header-via-response" in payload:
        value = payload.get("header-via-response")
        if value and value not in VALID_BODY_HEADER_VIA_RESPONSE:
            return (
                False,
                f"Invalid header-via-response '{value}'. Must be one of: {', '.join(VALID_BODY_HEADER_VIA_RESPONSE)}",
            )

    # Validate header-client-cert if present
    if "header-client-cert" in payload:
        value = payload.get("header-client-cert")
        if value and value not in VALID_BODY_HEADER_CLIENT_CERT:
            return (
                False,
                f"Invalid header-client-cert '{value}'. Must be one of: {', '.join(VALID_BODY_HEADER_CLIENT_CERT)}",
            )

    # Validate header-x-forwarded-for if present
    if "header-x-forwarded-for" in payload:
        value = payload.get("header-x-forwarded-for")
        if value and value not in VALID_BODY_HEADER_X_FORWARDED_FOR:
            return (
                False,
                f"Invalid header-x-forwarded-for '{value}'. Must be one of: {', '.join(VALID_BODY_HEADER_X_FORWARDED_FOR)}",
            )

    # Validate header-x-forwarded-client-cert if present
    if "header-x-forwarded-client-cert" in payload:
        value = payload.get("header-x-forwarded-client-cert")
        if value and value not in VALID_BODY_HEADER_X_FORWARDED_CLIENT_CERT:
            return (
                False,
                f"Invalid header-x-forwarded-client-cert '{value}'. Must be one of: {', '.join(VALID_BODY_HEADER_X_FORWARDED_CLIENT_CERT)}",
            )

    # Validate header-front-end-https if present
    if "header-front-end-https" in payload:
        value = payload.get("header-front-end-https")
        if value and value not in VALID_BODY_HEADER_FRONT_END_HTTPS:
            return (
                False,
                f"Invalid header-front-end-https '{value}'. Must be one of: {', '.join(VALID_BODY_HEADER_FRONT_END_HTTPS)}",
            )

    # Validate header-x-authenticated-user if present
    if "header-x-authenticated-user" in payload:
        value = payload.get("header-x-authenticated-user")
        if value and value not in VALID_BODY_HEADER_X_AUTHENTICATED_USER:
            return (
                False,
                f"Invalid header-x-authenticated-user '{value}'. Must be one of: {', '.join(VALID_BODY_HEADER_X_AUTHENTICATED_USER)}",
            )

    # Validate header-x-authenticated-groups if present
    if "header-x-authenticated-groups" in payload:
        value = payload.get("header-x-authenticated-groups")
        if value and value not in VALID_BODY_HEADER_X_AUTHENTICATED_GROUPS:
            return (
                False,
                f"Invalid header-x-authenticated-groups '{value}'. Must be one of: {', '.join(VALID_BODY_HEADER_X_AUTHENTICATED_GROUPS)}",
            )

    # Validate strip-encoding if present
    if "strip-encoding" in payload:
        value = payload.get("strip-encoding")
        if value and value not in VALID_BODY_STRIP_ENCODING:
            return (
                False,
                f"Invalid strip-encoding '{value}'. Must be one of: {', '.join(VALID_BODY_STRIP_ENCODING)}",
            )

    # Validate log-header-change if present
    if "log-header-change" in payload:
        value = payload.get("log-header-change")
        if value and value not in VALID_BODY_LOG_HEADER_CHANGE:
            return (
                False,
                f"Invalid log-header-change '{value}'. Must be one of: {', '.join(VALID_BODY_LOG_HEADER_CHANGE)}",
            )

    return (True, None)


# ============================================================================
# DELETE Validation
# ============================================================================


def validate_profile_delete(
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
