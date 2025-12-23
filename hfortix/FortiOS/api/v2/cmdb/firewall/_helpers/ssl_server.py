"""
Validation helpers for firewall ssl_server endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_SSL_MODE = ["hal", "full"]
VALID_BODY_ADD_HEADER_X_FORWARDED_PROTO = ["enable", "disable"]
VALID_BODY_SSL_DH_BITS = ["768", "1024", "1536", "2048"]
VALID_BODY_SSL_ALGORITHM = ["high", "medium", "low"]
VALID_BODY_SSL_CLIENT_RENEGOTIATION = ["allow", "deny", "secure"]
VALID_BODY_SSL_MIN_VERSION = ["tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"]
VALID_BODY_SSL_MAX_VERSION = ["tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"]
VALID_BODY_SSL_SEND_EMPTY_FRAGS = ["enable", "disable"]
VALID_BODY_URL_REWRITE = ["enable", "disable"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_ssl_server_get(
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


def validate_ssl_server_post(
    payload: dict[str, Any],
) -> tuple[bool, str | None]:
    """
    Validate POST request payload for creating ssl_server.

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

    # Validate port if present
    if "port" in payload:
        value = payload.get("port")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 65535:
                    return (False, "port must be between 1 and 65535")
            except (ValueError, TypeError):
                return (False, f"port must be numeric, got: {value}")

    # Validate ssl-mode if present
    if "ssl-mode" in payload:
        value = payload.get("ssl-mode")
        if value and value not in VALID_BODY_SSL_MODE:
            return (
                False,
                f"Invalid ssl-mode '{value}'. Must be one of: {', '.join(VALID_BODY_SSL_MODE)}",
            )

    # Validate add-header-x-forwarded-proto if present
    if "add-header-x-forwarded-proto" in payload:
        value = payload.get("add-header-x-forwarded-proto")
        if value and value not in VALID_BODY_ADD_HEADER_X_FORWARDED_PROTO:
            return (
                False,
                f"Invalid add-header-x-forwarded-proto '{value}'. Must be one of: {', '.join(VALID_BODY_ADD_HEADER_X_FORWARDED_PROTO)}",
            )

    # Validate mapped-port if present
    if "mapped-port" in payload:
        value = payload.get("mapped-port")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 65535:
                    return (False, "mapped-port must be between 1 and 65535")
            except (ValueError, TypeError):
                return (False, f"mapped-port must be numeric, got: {value}")

    # Validate ssl-dh-bits if present
    if "ssl-dh-bits" in payload:
        value = payload.get("ssl-dh-bits")
        if value and value not in VALID_BODY_SSL_DH_BITS:
            return (
                False,
                f"Invalid ssl-dh-bits '{value}'. Must be one of: {', '.join(VALID_BODY_SSL_DH_BITS)}",
            )

    # Validate ssl-algorithm if present
    if "ssl-algorithm" in payload:
        value = payload.get("ssl-algorithm")
        if value and value not in VALID_BODY_SSL_ALGORITHM:
            return (
                False,
                f"Invalid ssl-algorithm '{value}'. Must be one of: {', '.join(VALID_BODY_SSL_ALGORITHM)}",
            )

    # Validate ssl-client-renegotiation if present
    if "ssl-client-renegotiation" in payload:
        value = payload.get("ssl-client-renegotiation")
        if value and value not in VALID_BODY_SSL_CLIENT_RENEGOTIATION:
            return (
                False,
                f"Invalid ssl-client-renegotiation '{value}'. Must be one of: {', '.join(VALID_BODY_SSL_CLIENT_RENEGOTIATION)}",
            )

    # Validate ssl-min-version if present
    if "ssl-min-version" in payload:
        value = payload.get("ssl-min-version")
        if value and value not in VALID_BODY_SSL_MIN_VERSION:
            return (
                False,
                f"Invalid ssl-min-version '{value}'. Must be one of: {', '.join(VALID_BODY_SSL_MIN_VERSION)}",
            )

    # Validate ssl-max-version if present
    if "ssl-max-version" in payload:
        value = payload.get("ssl-max-version")
        if value and value not in VALID_BODY_SSL_MAX_VERSION:
            return (
                False,
                f"Invalid ssl-max-version '{value}'. Must be one of: {', '.join(VALID_BODY_SSL_MAX_VERSION)}",
            )

    # Validate ssl-send-empty-frags if present
    if "ssl-send-empty-frags" in payload:
        value = payload.get("ssl-send-empty-frags")
        if value and value not in VALID_BODY_SSL_SEND_EMPTY_FRAGS:
            return (
                False,
                f"Invalid ssl-send-empty-frags '{value}'. Must be one of: {', '.join(VALID_BODY_SSL_SEND_EMPTY_FRAGS)}",
            )

    # Validate url-rewrite if present
    if "url-rewrite" in payload:
        value = payload.get("url-rewrite")
        if value and value not in VALID_BODY_URL_REWRITE:
            return (
                False,
                f"Invalid url-rewrite '{value}'. Must be one of: {', '.join(VALID_BODY_URL_REWRITE)}",
            )

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_ssl_server_put(
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

    # Validate port if present
    if "port" in payload:
        value = payload.get("port")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 65535:
                    return (False, "port must be between 1 and 65535")
            except (ValueError, TypeError):
                return (False, f"port must be numeric, got: {value}")

    # Validate ssl-mode if present
    if "ssl-mode" in payload:
        value = payload.get("ssl-mode")
        if value and value not in VALID_BODY_SSL_MODE:
            return (
                False,
                f"Invalid ssl-mode '{value}'. Must be one of: {', '.join(VALID_BODY_SSL_MODE)}",
            )

    # Validate add-header-x-forwarded-proto if present
    if "add-header-x-forwarded-proto" in payload:
        value = payload.get("add-header-x-forwarded-proto")
        if value and value not in VALID_BODY_ADD_HEADER_X_FORWARDED_PROTO:
            return (
                False,
                f"Invalid add-header-x-forwarded-proto '{value}'. Must be one of: {', '.join(VALID_BODY_ADD_HEADER_X_FORWARDED_PROTO)}",
            )

    # Validate mapped-port if present
    if "mapped-port" in payload:
        value = payload.get("mapped-port")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 65535:
                    return (False, "mapped-port must be between 1 and 65535")
            except (ValueError, TypeError):
                return (False, f"mapped-port must be numeric, got: {value}")

    # Validate ssl-dh-bits if present
    if "ssl-dh-bits" in payload:
        value = payload.get("ssl-dh-bits")
        if value and value not in VALID_BODY_SSL_DH_BITS:
            return (
                False,
                f"Invalid ssl-dh-bits '{value}'. Must be one of: {', '.join(VALID_BODY_SSL_DH_BITS)}",
            )

    # Validate ssl-algorithm if present
    if "ssl-algorithm" in payload:
        value = payload.get("ssl-algorithm")
        if value and value not in VALID_BODY_SSL_ALGORITHM:
            return (
                False,
                f"Invalid ssl-algorithm '{value}'. Must be one of: {', '.join(VALID_BODY_SSL_ALGORITHM)}",
            )

    # Validate ssl-client-renegotiation if present
    if "ssl-client-renegotiation" in payload:
        value = payload.get("ssl-client-renegotiation")
        if value and value not in VALID_BODY_SSL_CLIENT_RENEGOTIATION:
            return (
                False,
                f"Invalid ssl-client-renegotiation '{value}'. Must be one of: {', '.join(VALID_BODY_SSL_CLIENT_RENEGOTIATION)}",
            )

    # Validate ssl-min-version if present
    if "ssl-min-version" in payload:
        value = payload.get("ssl-min-version")
        if value and value not in VALID_BODY_SSL_MIN_VERSION:
            return (
                False,
                f"Invalid ssl-min-version '{value}'. Must be one of: {', '.join(VALID_BODY_SSL_MIN_VERSION)}",
            )

    # Validate ssl-max-version if present
    if "ssl-max-version" in payload:
        value = payload.get("ssl-max-version")
        if value and value not in VALID_BODY_SSL_MAX_VERSION:
            return (
                False,
                f"Invalid ssl-max-version '{value}'. Must be one of: {', '.join(VALID_BODY_SSL_MAX_VERSION)}",
            )

    # Validate ssl-send-empty-frags if present
    if "ssl-send-empty-frags" in payload:
        value = payload.get("ssl-send-empty-frags")
        if value and value not in VALID_BODY_SSL_SEND_EMPTY_FRAGS:
            return (
                False,
                f"Invalid ssl-send-empty-frags '{value}'. Must be one of: {', '.join(VALID_BODY_SSL_SEND_EMPTY_FRAGS)}",
            )

    # Validate url-rewrite if present
    if "url-rewrite" in payload:
        value = payload.get("url-rewrite")
        if value and value not in VALID_BODY_URL_REWRITE:
            return (
                False,
                f"Invalid url-rewrite '{value}'. Must be one of: {', '.join(VALID_BODY_URL_REWRITE)}",
            )

    return (True, None)


# ============================================================================
# DELETE Validation
# ============================================================================


def validate_ssl_server_delete(
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
