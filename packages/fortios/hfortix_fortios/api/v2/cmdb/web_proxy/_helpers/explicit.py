"""
Validation helpers for web-proxy explicit endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_STATUS = ["enable", "disable"]
VALID_BODY_SECURE_WEB_PROXY = ["disable", "enable", "secure"]
VALID_BODY_FTP_OVER_HTTP = ["enable", "disable"]
VALID_BODY_SOCKS = ["enable", "disable"]
VALID_BODY_HTTP_CONNECTION_MODE = ["static", "multiplex", "serverpool"]
VALID_BODY_CLIENT_CERT = ["disable", "enable"]
VALID_BODY_USER_AGENT_DETECT = ["disable", "enable"]
VALID_BODY_EMPTY_CERT_ACTION = ["accept", "block", "accept-unmanageable"]
VALID_BODY_SSL_DH_BITS = ["768", "1024", "1536", "2048"]
VALID_BODY_INTERFACE_SELECT_METHOD = ["sdwan", "specify"]
VALID_BODY_IPV6_STATUS = ["enable", "disable"]
VALID_BODY_STRICT_GUEST = ["enable", "disable"]
VALID_BODY_PREF_DNS_RESULT = ["ipv4", "ipv6", "ipv4-strict", "ipv6-strict"]
VALID_BODY_UNKNOWN_HTTP_VERSION = ["reject", "best-effort"]
VALID_BODY_SEC_DEFAULT_ACTION = ["accept", "deny"]
VALID_BODY_HTTPS_REPLACEMENT_MESSAGE = ["enable", "disable"]
VALID_BODY_MESSAGE_UPON_SERVER_ERROR = ["enable", "disable"]
VALID_BODY_PAC_FILE_SERVER_STATUS = ["enable", "disable"]
VALID_BODY_PAC_FILE_THROUGH_HTTPS = ["enable", "disable"]
VALID_BODY_SSL_ALGORITHM = ["high", "medium", "low"]
VALID_BODY_TRACE_AUTH_NO_RSP = ["enable", "disable"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_explicit_get(
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


def validate_explicit_put(
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

    # Validate status if present
    if "status" in payload:
        value = payload.get("status")
        if value and value not in VALID_BODY_STATUS:
            return (
                False,
                f"Invalid status '{value}'. Must be one of: {', '.join(VALID_BODY_STATUS)}",
            )

    # Validate secure-web-proxy if present
    if "secure-web-proxy" in payload:
        value = payload.get("secure-web-proxy")
        if value and value not in VALID_BODY_SECURE_WEB_PROXY:
            return (
                False,
                f"Invalid secure-web-proxy '{value}'. Must be one of: {', '.join(VALID_BODY_SECURE_WEB_PROXY)}",
            )

    # Validate ftp-over-http if present
    if "ftp-over-http" in payload:
        value = payload.get("ftp-over-http")
        if value and value not in VALID_BODY_FTP_OVER_HTTP:
            return (
                False,
                f"Invalid ftp-over-http '{value}'. Must be one of: {', '.join(VALID_BODY_FTP_OVER_HTTP)}",
            )

    # Validate socks if present
    if "socks" in payload:
        value = payload.get("socks")
        if value and value not in VALID_BODY_SOCKS:
            return (
                False,
                f"Invalid socks '{value}'. Must be one of: {', '.join(VALID_BODY_SOCKS)}",
            )

    # Validate http-connection-mode if present
    if "http-connection-mode" in payload:
        value = payload.get("http-connection-mode")
        if value and value not in VALID_BODY_HTTP_CONNECTION_MODE:
            return (
                False,
                f"Invalid http-connection-mode '{value}'. Must be one of: {', '.join(VALID_BODY_HTTP_CONNECTION_MODE)}",
            )

    # Validate client-cert if present
    if "client-cert" in payload:
        value = payload.get("client-cert")
        if value and value not in VALID_BODY_CLIENT_CERT:
            return (
                False,
                f"Invalid client-cert '{value}'. Must be one of: {', '.join(VALID_BODY_CLIENT_CERT)}",
            )

    # Validate user-agent-detect if present
    if "user-agent-detect" in payload:
        value = payload.get("user-agent-detect")
        if value and value not in VALID_BODY_USER_AGENT_DETECT:
            return (
                False,
                f"Invalid user-agent-detect '{value}'. Must be one of: {', '.join(VALID_BODY_USER_AGENT_DETECT)}",
            )

    # Validate empty-cert-action if present
    if "empty-cert-action" in payload:
        value = payload.get("empty-cert-action")
        if value and value not in VALID_BODY_EMPTY_CERT_ACTION:
            return (
                False,
                f"Invalid empty-cert-action '{value}'. Must be one of: {', '.join(VALID_BODY_EMPTY_CERT_ACTION)}",
            )

    # Validate ssl-dh-bits if present
    if "ssl-dh-bits" in payload:
        value = payload.get("ssl-dh-bits")
        if value and value not in VALID_BODY_SSL_DH_BITS:
            return (
                False,
                f"Invalid ssl-dh-bits '{value}'. Must be one of: {', '.join(VALID_BODY_SSL_DH_BITS)}",
            )

    # Validate interface-select-method if present
    if "interface-select-method" in payload:
        value = payload.get("interface-select-method")
        if value and value not in VALID_BODY_INTERFACE_SELECT_METHOD:
            return (
                False,
                f"Invalid interface-select-method '{value}'. Must be one of: {', '.join(VALID_BODY_INTERFACE_SELECT_METHOD)}",
            )

    # Validate interface if present
    if "interface" in payload:
        value = payload.get("interface")
        if value and isinstance(value, str) and len(value) > 15:
            return (False, "interface cannot exceed 15 characters")

    # Validate vrf-select if present
    if "vrf-select" in payload:
        value = payload.get("vrf-select")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 511:
                    return (False, "vrf-select must be between 0 and 511")
            except (ValueError, TypeError):
                return (False, f"vrf-select must be numeric, got: {value}")

    # Validate ipv6-status if present
    if "ipv6-status" in payload:
        value = payload.get("ipv6-status")
        if value and value not in VALID_BODY_IPV6_STATUS:
            return (
                False,
                f"Invalid ipv6-status '{value}'. Must be one of: {', '.join(VALID_BODY_IPV6_STATUS)}",
            )

    # Validate strict-guest if present
    if "strict-guest" in payload:
        value = payload.get("strict-guest")
        if value and value not in VALID_BODY_STRICT_GUEST:
            return (
                False,
                f"Invalid strict-guest '{value}'. Must be one of: {', '.join(VALID_BODY_STRICT_GUEST)}",
            )

    # Validate pref-dns-result if present
    if "pref-dns-result" in payload:
        value = payload.get("pref-dns-result")
        if value and value not in VALID_BODY_PREF_DNS_RESULT:
            return (
                False,
                f"Invalid pref-dns-result '{value}'. Must be one of: {', '.join(VALID_BODY_PREF_DNS_RESULT)}",
            )

    # Validate unknown-http-version if present
    if "unknown-http-version" in payload:
        value = payload.get("unknown-http-version")
        if value and value not in VALID_BODY_UNKNOWN_HTTP_VERSION:
            return (
                False,
                f"Invalid unknown-http-version '{value}'. Must be one of: {', '.join(VALID_BODY_UNKNOWN_HTTP_VERSION)}",
            )

    # Validate realm if present
    if "realm" in payload:
        value = payload.get("realm")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "realm cannot exceed 63 characters")

    # Validate sec-default-action if present
    if "sec-default-action" in payload:
        value = payload.get("sec-default-action")
        if value and value not in VALID_BODY_SEC_DEFAULT_ACTION:
            return (
                False,
                f"Invalid sec-default-action '{value}'. Must be one of: {', '.join(VALID_BODY_SEC_DEFAULT_ACTION)}",
            )

    # Validate https-replacement-message if present
    if "https-replacement-message" in payload:
        value = payload.get("https-replacement-message")
        if value and value not in VALID_BODY_HTTPS_REPLACEMENT_MESSAGE:
            return (
                False,
                f"Invalid https-replacement-message '{value}'. Must be one of: {', '.join(VALID_BODY_HTTPS_REPLACEMENT_MESSAGE)}",
            )

    # Validate message-upon-server-error if present
    if "message-upon-server-error" in payload:
        value = payload.get("message-upon-server-error")
        if value and value not in VALID_BODY_MESSAGE_UPON_SERVER_ERROR:
            return (
                False,
                f"Invalid message-upon-server-error '{value}'. Must be one of: {', '.join(VALID_BODY_MESSAGE_UPON_SERVER_ERROR)}",
            )

    # Validate pac-file-server-status if present
    if "pac-file-server-status" in payload:
        value = payload.get("pac-file-server-status")
        if value and value not in VALID_BODY_PAC_FILE_SERVER_STATUS:
            return (
                False,
                f"Invalid pac-file-server-status '{value}'. Must be one of: {', '.join(VALID_BODY_PAC_FILE_SERVER_STATUS)}",
            )

    # Validate pac-file-through-https if present
    if "pac-file-through-https" in payload:
        value = payload.get("pac-file-through-https")
        if value and value not in VALID_BODY_PAC_FILE_THROUGH_HTTPS:
            return (
                False,
                f"Invalid pac-file-through-https '{value}'. Must be one of: {', '.join(VALID_BODY_PAC_FILE_THROUGH_HTTPS)}",
            )

    # Validate pac-file-name if present
    if "pac-file-name" in payload:
        value = payload.get("pac-file-name")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "pac-file-name cannot exceed 63 characters")

    # Validate ssl-algorithm if present
    if "ssl-algorithm" in payload:
        value = payload.get("ssl-algorithm")
        if value and value not in VALID_BODY_SSL_ALGORITHM:
            return (
                False,
                f"Invalid ssl-algorithm '{value}'. Must be one of: {', '.join(VALID_BODY_SSL_ALGORITHM)}",
            )

    # Validate trace-auth-no-rsp if present
    if "trace-auth-no-rsp" in payload:
        value = payload.get("trace-auth-no-rsp")
        if value and value not in VALID_BODY_TRACE_AUTH_NO_RSP:
            return (
                False,
                f"Invalid trace-auth-no-rsp '{value}'. Must be one of: {', '.join(VALID_BODY_TRACE_AUTH_NO_RSP)}",
            )

    return (True, None)
