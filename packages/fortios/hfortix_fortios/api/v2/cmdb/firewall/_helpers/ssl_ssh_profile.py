"""
Validation helpers for firewall ssl_ssh_profile endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_ALLOWLIST = ["enable", "disable"]
VALID_BODY_BLOCK_BLOCKLISTED_CERTIFICATES = ["disable", "enable"]
VALID_BODY_SERVER_CERT_MODE = ["re-sign", "replace"]
VALID_BODY_USE_SSL_SERVER = ["disable", "enable"]
VALID_BODY_SSL_EXEMPTION_IP_RATING = ["enable", "disable"]
VALID_BODY_SSL_EXEMPTION_LOG = ["disable", "enable"]
VALID_BODY_SSL_ANOMALY_LOG = ["disable", "enable"]
VALID_BODY_SSL_NEGOTIATION_LOG = ["disable", "enable"]
VALID_BODY_SSL_SERVER_CERT_LOG = ["disable", "enable"]
VALID_BODY_SSL_HANDSHAKE_LOG = ["disable", "enable"]
VALID_BODY_RPC_OVER_HTTPS = ["enable", "disable"]
VALID_BODY_MAPI_OVER_HTTPS = ["enable", "disable"]
VALID_BODY_SUPPORTED_ALPN = ["http1-1", "http2", "all", "none"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_ssl_ssh_profile_get(
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


def validate_ssl_ssh_profile_post(
    payload: dict[str, Any],
) -> tuple[bool, str | None]:
    """
    Validate POST request payload for creating ssl_ssh_profile.

    Args:
        payload: The payload to validate

    Returns:
        Tuple of (is_valid, error_message)
    """
    # Validate name if present
    if "name" in payload:
        value = payload.get("name")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "name cannot exceed 47 characters")

    # Validate comment if present
    if "comment" in payload:
        value = payload.get("comment")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "comment cannot exceed 255 characters")

    # Validate allowlist if present
    if "allowlist" in payload:
        value = payload.get("allowlist")
        if value and value not in VALID_BODY_ALLOWLIST:
            return (
                False,
                f"Invalid allowlist '{value}'. Must be one of: {', '.join(VALID_BODY_ALLOWLIST)}",
            )

    # Validate block-blocklisted-certificates if present
    if "block-blocklisted-certificates" in payload:
        value = payload.get("block-blocklisted-certificates")
        if value and value not in VALID_BODY_BLOCK_BLOCKLISTED_CERTIFICATES:
            return (
                False,
                f"Invalid block-blocklisted-certificates '{value}'. Must be one of: {', '.join(VALID_BODY_BLOCK_BLOCKLISTED_CERTIFICATES)}",
            )

    # Validate server-cert-mode if present
    if "server-cert-mode" in payload:
        value = payload.get("server-cert-mode")
        if value and value not in VALID_BODY_SERVER_CERT_MODE:
            return (
                False,
                f"Invalid server-cert-mode '{value}'. Must be one of: {', '.join(VALID_BODY_SERVER_CERT_MODE)}",
            )

    # Validate use-ssl-server if present
    if "use-ssl-server" in payload:
        value = payload.get("use-ssl-server")
        if value and value not in VALID_BODY_USE_SSL_SERVER:
            return (
                False,
                f"Invalid use-ssl-server '{value}'. Must be one of: {', '.join(VALID_BODY_USE_SSL_SERVER)}",
            )

    # Validate caname if present
    if "caname" in payload:
        value = payload.get("caname")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "caname cannot exceed 35 characters")

    # Validate untrusted-caname if present
    if "untrusted-caname" in payload:
        value = payload.get("untrusted-caname")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "untrusted-caname cannot exceed 35 characters")

    # Validate ssl-exemption-ip-rating if present
    if "ssl-exemption-ip-rating" in payload:
        value = payload.get("ssl-exemption-ip-rating")
        if value and value not in VALID_BODY_SSL_EXEMPTION_IP_RATING:
            return (
                False,
                f"Invalid ssl-exemption-ip-rating '{value}'. Must be one of: {', '.join(VALID_BODY_SSL_EXEMPTION_IP_RATING)}",
            )

    # Validate ssl-exemption-log if present
    if "ssl-exemption-log" in payload:
        value = payload.get("ssl-exemption-log")
        if value and value not in VALID_BODY_SSL_EXEMPTION_LOG:
            return (
                False,
                f"Invalid ssl-exemption-log '{value}'. Must be one of: {', '.join(VALID_BODY_SSL_EXEMPTION_LOG)}",
            )

    # Validate ssl-anomaly-log if present
    if "ssl-anomaly-log" in payload:
        value = payload.get("ssl-anomaly-log")
        if value and value not in VALID_BODY_SSL_ANOMALY_LOG:
            return (
                False,
                f"Invalid ssl-anomaly-log '{value}'. Must be one of: {', '.join(VALID_BODY_SSL_ANOMALY_LOG)}",
            )

    # Validate ssl-negotiation-log if present
    if "ssl-negotiation-log" in payload:
        value = payload.get("ssl-negotiation-log")
        if value and value not in VALID_BODY_SSL_NEGOTIATION_LOG:
            return (
                False,
                f"Invalid ssl-negotiation-log '{value}'. Must be one of: {', '.join(VALID_BODY_SSL_NEGOTIATION_LOG)}",
            )

    # Validate ssl-server-cert-log if present
    if "ssl-server-cert-log" in payload:
        value = payload.get("ssl-server-cert-log")
        if value and value not in VALID_BODY_SSL_SERVER_CERT_LOG:
            return (
                False,
                f"Invalid ssl-server-cert-log '{value}'. Must be one of: {', '.join(VALID_BODY_SSL_SERVER_CERT_LOG)}",
            )

    # Validate ssl-handshake-log if present
    if "ssl-handshake-log" in payload:
        value = payload.get("ssl-handshake-log")
        if value and value not in VALID_BODY_SSL_HANDSHAKE_LOG:
            return (
                False,
                f"Invalid ssl-handshake-log '{value}'. Must be one of: {', '.join(VALID_BODY_SSL_HANDSHAKE_LOG)}",
            )

    # Validate rpc-over-https if present
    if "rpc-over-https" in payload:
        value = payload.get("rpc-over-https")
        if value and value not in VALID_BODY_RPC_OVER_HTTPS:
            return (
                False,
                f"Invalid rpc-over-https '{value}'. Must be one of: {', '.join(VALID_BODY_RPC_OVER_HTTPS)}",
            )

    # Validate mapi-over-https if present
    if "mapi-over-https" in payload:
        value = payload.get("mapi-over-https")
        if value and value not in VALID_BODY_MAPI_OVER_HTTPS:
            return (
                False,
                f"Invalid mapi-over-https '{value}'. Must be one of: {', '.join(VALID_BODY_MAPI_OVER_HTTPS)}",
            )

    # Validate supported-alpn if present
    if "supported-alpn" in payload:
        value = payload.get("supported-alpn")
        if value and value not in VALID_BODY_SUPPORTED_ALPN:
            return (
                False,
                f"Invalid supported-alpn '{value}'. Must be one of: {', '.join(VALID_BODY_SUPPORTED_ALPN)}",
            )

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_ssl_ssh_profile_put(
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
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "name cannot exceed 47 characters")

    # Validate comment if present
    if "comment" in payload:
        value = payload.get("comment")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "comment cannot exceed 255 characters")

    # Validate allowlist if present
    if "allowlist" in payload:
        value = payload.get("allowlist")
        if value and value not in VALID_BODY_ALLOWLIST:
            return (
                False,
                f"Invalid allowlist '{value}'. Must be one of: {', '.join(VALID_BODY_ALLOWLIST)}",
            )

    # Validate block-blocklisted-certificates if present
    if "block-blocklisted-certificates" in payload:
        value = payload.get("block-blocklisted-certificates")
        if value and value not in VALID_BODY_BLOCK_BLOCKLISTED_CERTIFICATES:
            return (
                False,
                f"Invalid block-blocklisted-certificates '{value}'. Must be one of: {', '.join(VALID_BODY_BLOCK_BLOCKLISTED_CERTIFICATES)}",
            )

    # Validate server-cert-mode if present
    if "server-cert-mode" in payload:
        value = payload.get("server-cert-mode")
        if value and value not in VALID_BODY_SERVER_CERT_MODE:
            return (
                False,
                f"Invalid server-cert-mode '{value}'. Must be one of: {', '.join(VALID_BODY_SERVER_CERT_MODE)}",
            )

    # Validate use-ssl-server if present
    if "use-ssl-server" in payload:
        value = payload.get("use-ssl-server")
        if value and value not in VALID_BODY_USE_SSL_SERVER:
            return (
                False,
                f"Invalid use-ssl-server '{value}'. Must be one of: {', '.join(VALID_BODY_USE_SSL_SERVER)}",
            )

    # Validate caname if present
    if "caname" in payload:
        value = payload.get("caname")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "caname cannot exceed 35 characters")

    # Validate untrusted-caname if present
    if "untrusted-caname" in payload:
        value = payload.get("untrusted-caname")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "untrusted-caname cannot exceed 35 characters")

    # Validate ssl-exemption-ip-rating if present
    if "ssl-exemption-ip-rating" in payload:
        value = payload.get("ssl-exemption-ip-rating")
        if value and value not in VALID_BODY_SSL_EXEMPTION_IP_RATING:
            return (
                False,
                f"Invalid ssl-exemption-ip-rating '{value}'. Must be one of: {', '.join(VALID_BODY_SSL_EXEMPTION_IP_RATING)}",
            )

    # Validate ssl-exemption-log if present
    if "ssl-exemption-log" in payload:
        value = payload.get("ssl-exemption-log")
        if value and value not in VALID_BODY_SSL_EXEMPTION_LOG:
            return (
                False,
                f"Invalid ssl-exemption-log '{value}'. Must be one of: {', '.join(VALID_BODY_SSL_EXEMPTION_LOG)}",
            )

    # Validate ssl-anomaly-log if present
    if "ssl-anomaly-log" in payload:
        value = payload.get("ssl-anomaly-log")
        if value and value not in VALID_BODY_SSL_ANOMALY_LOG:
            return (
                False,
                f"Invalid ssl-anomaly-log '{value}'. Must be one of: {', '.join(VALID_BODY_SSL_ANOMALY_LOG)}",
            )

    # Validate ssl-negotiation-log if present
    if "ssl-negotiation-log" in payload:
        value = payload.get("ssl-negotiation-log")
        if value and value not in VALID_BODY_SSL_NEGOTIATION_LOG:
            return (
                False,
                f"Invalid ssl-negotiation-log '{value}'. Must be one of: {', '.join(VALID_BODY_SSL_NEGOTIATION_LOG)}",
            )

    # Validate ssl-server-cert-log if present
    if "ssl-server-cert-log" in payload:
        value = payload.get("ssl-server-cert-log")
        if value and value not in VALID_BODY_SSL_SERVER_CERT_LOG:
            return (
                False,
                f"Invalid ssl-server-cert-log '{value}'. Must be one of: {', '.join(VALID_BODY_SSL_SERVER_CERT_LOG)}",
            )

    # Validate ssl-handshake-log if present
    if "ssl-handshake-log" in payload:
        value = payload.get("ssl-handshake-log")
        if value and value not in VALID_BODY_SSL_HANDSHAKE_LOG:
            return (
                False,
                f"Invalid ssl-handshake-log '{value}'. Must be one of: {', '.join(VALID_BODY_SSL_HANDSHAKE_LOG)}",
            )

    # Validate rpc-over-https if present
    if "rpc-over-https" in payload:
        value = payload.get("rpc-over-https")
        if value and value not in VALID_BODY_RPC_OVER_HTTPS:
            return (
                False,
                f"Invalid rpc-over-https '{value}'. Must be one of: {', '.join(VALID_BODY_RPC_OVER_HTTPS)}",
            )

    # Validate mapi-over-https if present
    if "mapi-over-https" in payload:
        value = payload.get("mapi-over-https")
        if value and value not in VALID_BODY_MAPI_OVER_HTTPS:
            return (
                False,
                f"Invalid mapi-over-https '{value}'. Must be one of: {', '.join(VALID_BODY_MAPI_OVER_HTTPS)}",
            )

    # Validate supported-alpn if present
    if "supported-alpn" in payload:
        value = payload.get("supported-alpn")
        if value and value not in VALID_BODY_SUPPORTED_ALPN:
            return (
                False,
                f"Invalid supported-alpn '{value}'. Must be one of: {', '.join(VALID_BODY_SUPPORTED_ALPN)}",
            )

    return (True, None)


# ============================================================================
# DELETE Validation
# ============================================================================


def validate_ssl_ssh_profile_delete(
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
