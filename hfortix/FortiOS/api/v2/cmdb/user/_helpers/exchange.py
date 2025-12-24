"""
Validation helpers for user exchange endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_CONNECT_PROTOCOL = [
    "rpc-over-tcp",
    "rpc-over-http",
    "rpc-over-https",
]
VALID_BODY_VALIDATE_SERVER_CERTIFICATE = ["disable", "enable"]
VALID_BODY_AUTH_TYPE = ["spnego", "ntlm", "kerberos"]
VALID_BODY_AUTH_LEVEL = ["connect", "call", "packet", "integrity", "privacy"]
VALID_BODY_HTTP_AUTH_TYPE = ["basic", "ntlm"]
VALID_BODY_SSL_MIN_PROTO_VERSION = [
    "default",
    "SSLv3",
    "TLSv1",
    "TLSv1-1",
    "TLSv1-2",
    "TLSv1-3",
]
VALID_BODY_AUTO_DISCOVER_KDC = ["enable", "disable"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_exchange_get(
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


def validate_exchange_post(payload: dict[str, Any]) -> tuple[bool, str | None]:
    """
    Validate POST request payload for creating exchange.

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

    # Validate server-name if present
    if "server-name" in payload:
        value = payload.get("server-name")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "server-name cannot exceed 63 characters")

    # Validate domain-name if present
    if "domain-name" in payload:
        value = payload.get("domain-name")
        if value and isinstance(value, str) and len(value) > 79:
            return (False, "domain-name cannot exceed 79 characters")

    # Validate username if present
    if "username" in payload:
        value = payload.get("username")
        if value and isinstance(value, str) and len(value) > 64:
            return (False, "username cannot exceed 64 characters")

    # Validate connect-protocol if present
    if "connect-protocol" in payload:
        value = payload.get("connect-protocol")
        if value and value not in VALID_BODY_CONNECT_PROTOCOL:
            return (
                False,
                f"Invalid connect-protocol '{value}'. Must be one of: {', '.join(VALID_BODY_CONNECT_PROTOCOL)}",
            )

    # Validate validate-server-certificate if present
    if "validate-server-certificate" in payload:
        value = payload.get("validate-server-certificate")
        if value and value not in VALID_BODY_VALIDATE_SERVER_CERTIFICATE:
            return (
                False,
                f"Invalid validate-server-certificate '{value}'. Must be one of: {', '.join(VALID_BODY_VALIDATE_SERVER_CERTIFICATE)}",
            )

    # Validate auth-type if present
    if "auth-type" in payload:
        value = payload.get("auth-type")
        if value and value not in VALID_BODY_AUTH_TYPE:
            return (
                False,
                f"Invalid auth-type '{value}'. Must be one of: {', '.join(VALID_BODY_AUTH_TYPE)}",
            )

    # Validate auth-level if present
    if "auth-level" in payload:
        value = payload.get("auth-level")
        if value and value not in VALID_BODY_AUTH_LEVEL:
            return (
                False,
                f"Invalid auth-level '{value}'. Must be one of: {', '.join(VALID_BODY_AUTH_LEVEL)}",
            )

    # Validate http-auth-type if present
    if "http-auth-type" in payload:
        value = payload.get("http-auth-type")
        if value and value not in VALID_BODY_HTTP_AUTH_TYPE:
            return (
                False,
                f"Invalid http-auth-type '{value}'. Must be one of: {', '.join(VALID_BODY_HTTP_AUTH_TYPE)}",
            )

    # Validate ssl-min-proto-version if present
    if "ssl-min-proto-version" in payload:
        value = payload.get("ssl-min-proto-version")
        if value and value not in VALID_BODY_SSL_MIN_PROTO_VERSION:
            return (
                False,
                f"Invalid ssl-min-proto-version '{value}'. Must be one of: {', '.join(VALID_BODY_SSL_MIN_PROTO_VERSION)}",
            )

    # Validate auto-discover-kdc if present
    if "auto-discover-kdc" in payload:
        value = payload.get("auto-discover-kdc")
        if value and value not in VALID_BODY_AUTO_DISCOVER_KDC:
            return (
                False,
                f"Invalid auto-discover-kdc '{value}'. Must be one of: {', '.join(VALID_BODY_AUTO_DISCOVER_KDC)}",
            )

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_exchange_put(
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

    # Validate server-name if present
    if "server-name" in payload:
        value = payload.get("server-name")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "server-name cannot exceed 63 characters")

    # Validate domain-name if present
    if "domain-name" in payload:
        value = payload.get("domain-name")
        if value and isinstance(value, str) and len(value) > 79:
            return (False, "domain-name cannot exceed 79 characters")

    # Validate username if present
    if "username" in payload:
        value = payload.get("username")
        if value and isinstance(value, str) and len(value) > 64:
            return (False, "username cannot exceed 64 characters")

    # Validate connect-protocol if present
    if "connect-protocol" in payload:
        value = payload.get("connect-protocol")
        if value and value not in VALID_BODY_CONNECT_PROTOCOL:
            return (
                False,
                f"Invalid connect-protocol '{value}'. Must be one of: {', '.join(VALID_BODY_CONNECT_PROTOCOL)}",
            )

    # Validate validate-server-certificate if present
    if "validate-server-certificate" in payload:
        value = payload.get("validate-server-certificate")
        if value and value not in VALID_BODY_VALIDATE_SERVER_CERTIFICATE:
            return (
                False,
                f"Invalid validate-server-certificate '{value}'. Must be one of: {', '.join(VALID_BODY_VALIDATE_SERVER_CERTIFICATE)}",
            )

    # Validate auth-type if present
    if "auth-type" in payload:
        value = payload.get("auth-type")
        if value and value not in VALID_BODY_AUTH_TYPE:
            return (
                False,
                f"Invalid auth-type '{value}'. Must be one of: {', '.join(VALID_BODY_AUTH_TYPE)}",
            )

    # Validate auth-level if present
    if "auth-level" in payload:
        value = payload.get("auth-level")
        if value and value not in VALID_BODY_AUTH_LEVEL:
            return (
                False,
                f"Invalid auth-level '{value}'. Must be one of: {', '.join(VALID_BODY_AUTH_LEVEL)}",
            )

    # Validate http-auth-type if present
    if "http-auth-type" in payload:
        value = payload.get("http-auth-type")
        if value and value not in VALID_BODY_HTTP_AUTH_TYPE:
            return (
                False,
                f"Invalid http-auth-type '{value}'. Must be one of: {', '.join(VALID_BODY_HTTP_AUTH_TYPE)}",
            )

    # Validate ssl-min-proto-version if present
    if "ssl-min-proto-version" in payload:
        value = payload.get("ssl-min-proto-version")
        if value and value not in VALID_BODY_SSL_MIN_PROTO_VERSION:
            return (
                False,
                f"Invalid ssl-min-proto-version '{value}'. Must be one of: {', '.join(VALID_BODY_SSL_MIN_PROTO_VERSION)}",
            )

    # Validate auto-discover-kdc if present
    if "auto-discover-kdc" in payload:
        value = payload.get("auto-discover-kdc")
        if value and value not in VALID_BODY_AUTO_DISCOVER_KDC:
            return (
                False,
                f"Invalid auto-discover-kdc '{value}'. Must be one of: {', '.join(VALID_BODY_AUTO_DISCOVER_KDC)}",
            )

    return (True, None)


# ============================================================================
# DELETE Validation
# ============================================================================


def validate_exchange_delete(
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
