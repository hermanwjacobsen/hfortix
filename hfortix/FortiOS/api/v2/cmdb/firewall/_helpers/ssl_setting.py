"""
Validation helpers for firewall ssl_setting endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_SSL_DH_BITS = ["768", "1024", "1536", "2048"]
VALID_BODY_SSL_SEND_EMPTY_FRAGS = ["enable", "disable"]
VALID_BODY_NO_MATCHING_CIPHER_ACTION = ["bypass", "drop"]
VALID_BODY_RESIGNED_SHORT_LIVED_CERTIFICATE = ["enable", "disable"]
VALID_BODY_ABBREVIATE_HANDSHAKE = ["enable", "disable"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_ssl_setting_get(
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


def validate_ssl_setting_put(
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

    # Validate proxy-connect-timeout if present
    if "proxy-connect-timeout" in payload:
        value = payload.get("proxy-connect-timeout")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 60:
                    return (
                        False,
                        "proxy-connect-timeout must be between 1 and 60",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"proxy-connect-timeout must be numeric, got: {value}",
                )

    # Validate ssl-dh-bits if present
    if "ssl-dh-bits" in payload:
        value = payload.get("ssl-dh-bits")
        if value and value not in VALID_BODY_SSL_DH_BITS:
            return (
                False,
                f"Invalid ssl-dh-bits '{value}'. Must be one of: {', '.join(VALID_BODY_SSL_DH_BITS)}",
            )

    # Validate ssl-send-empty-frags if present
    if "ssl-send-empty-frags" in payload:
        value = payload.get("ssl-send-empty-frags")
        if value and value not in VALID_BODY_SSL_SEND_EMPTY_FRAGS:
            return (
                False,
                f"Invalid ssl-send-empty-frags '{value}'. Must be one of: {', '.join(VALID_BODY_SSL_SEND_EMPTY_FRAGS)}",
            )

    # Validate no-matching-cipher-action if present
    if "no-matching-cipher-action" in payload:
        value = payload.get("no-matching-cipher-action")
        if value and value not in VALID_BODY_NO_MATCHING_CIPHER_ACTION:
            return (
                False,
                f"Invalid no-matching-cipher-action '{value}'. Must be one of: {', '.join(VALID_BODY_NO_MATCHING_CIPHER_ACTION)}",
            )

    # Validate cert-manager-cache-timeout if present
    if "cert-manager-cache-timeout" in payload:
        value = payload.get("cert-manager-cache-timeout")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 24 or int_val > 720:
                    return (
                        False,
                        "cert-manager-cache-timeout must be between 24 and 720",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"cert-manager-cache-timeout must be numeric, got: {value}",
                )

    # Validate resigned-short-lived-certificate if present
    if "resigned-short-lived-certificate" in payload:
        value = payload.get("resigned-short-lived-certificate")
        if value and value not in VALID_BODY_RESIGNED_SHORT_LIVED_CERTIFICATE:
            return (
                False,
                f"Invalid resigned-short-lived-certificate '{value}'. Must be one of: {', '.join(VALID_BODY_RESIGNED_SHORT_LIVED_CERTIFICATE)}",
            )

    # Validate cert-cache-capacity if present
    if "cert-cache-capacity" in payload:
        value = payload.get("cert-cache-capacity")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 500:
                    return (
                        False,
                        "cert-cache-capacity must be between 0 and 500",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"cert-cache-capacity must be numeric, got: {value}",
                )

    # Validate cert-cache-timeout if present
    if "cert-cache-timeout" in payload:
        value = payload.get("cert-cache-timeout")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 120:
                    return (
                        False,
                        "cert-cache-timeout must be between 1 and 120",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"cert-cache-timeout must be numeric, got: {value}",
                )

    # Validate session-cache-capacity if present
    if "session-cache-capacity" in payload:
        value = payload.get("session-cache-capacity")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 1000:
                    return (
                        False,
                        "session-cache-capacity must be between 0 and 1000",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"session-cache-capacity must be numeric, got: {value}",
                )

    # Validate session-cache-timeout if present
    if "session-cache-timeout" in payload:
        value = payload.get("session-cache-timeout")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 60:
                    return (
                        False,
                        "session-cache-timeout must be between 1 and 60",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"session-cache-timeout must be numeric, got: {value}",
                )

    # Validate kxp-queue-threshold if present
    if "kxp-queue-threshold" in payload:
        value = payload.get("kxp-queue-threshold")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 512:
                    return (
                        False,
                        "kxp-queue-threshold must be between 0 and 512",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"kxp-queue-threshold must be numeric, got: {value}",
                )

    # Validate ssl-queue-threshold if present
    if "ssl-queue-threshold" in payload:
        value = payload.get("ssl-queue-threshold")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 512:
                    return (
                        False,
                        "ssl-queue-threshold must be between 0 and 512",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"ssl-queue-threshold must be numeric, got: {value}",
                )

    # Validate abbreviate-handshake if present
    if "abbreviate-handshake" in payload:
        value = payload.get("abbreviate-handshake")
        if value and value not in VALID_BODY_ABBREVIATE_HANDSHAKE:
            return (
                False,
                f"Invalid abbreviate-handshake '{value}'. Must be one of: {', '.join(VALID_BODY_ABBREVIATE_HANDSHAKE)}",
            )

    return (True, None)
