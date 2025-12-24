"""
Validation helpers for web-proxy global_ endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_FAST_POLICY_MATCH = ["enable", "disable"]
VALID_BODY_LDAP_USER_CACHE = ["enable", "disable"]
VALID_BODY_STRICT_WEB_CHECK = ["enable", "disable"]
VALID_BODY_FORWARD_PROXY_AUTH = ["enable", "disable"]
VALID_BODY_LEARN_CLIENT_IP = ["enable", "disable"]
VALID_BODY_ALWAYS_LEARN_CLIENT_IP = ["enable", "disable"]
VALID_BODY_LEARN_CLIENT_IP_FROM_HEADER = [
    "true-client-ip",
    "x-real-ip",
    "x-forwarded-for",
]
VALID_BODY_POLICY_PARTIAL_MATCH = ["enable", "disable"]
VALID_BODY_LOG_POLICY_PENDING = ["enable", "disable"]
VALID_BODY_LOG_FORWARD_SERVER = ["enable", "disable"]
VALID_BODY_LOG_APP_ID = ["enable", "disable"]
VALID_BODY_PROXY_TRANSPARENT_CERT_INSPECTION = ["enable", "disable"]
VALID_BODY_REQUEST_OBS_FOLD = ["replace-with-sp", "block", "keep"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_global__get(
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


def validate_global__put(
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

    # Validate ssl-cert if present
    if "ssl-cert" in payload:
        value = payload.get("ssl-cert")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "ssl-cert cannot exceed 35 characters")

    # Validate ssl-ca-cert if present
    if "ssl-ca-cert" in payload:
        value = payload.get("ssl-ca-cert")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "ssl-ca-cert cannot exceed 35 characters")

    # Validate fast-policy-match if present
    if "fast-policy-match" in payload:
        value = payload.get("fast-policy-match")
        if value and value not in VALID_BODY_FAST_POLICY_MATCH:
            return (
                False,
                f"Invalid fast-policy-match '{value}'. Must be one of: {', '.join(VALID_BODY_FAST_POLICY_MATCH)}",
            )

    # Validate ldap-user-cache if present
    if "ldap-user-cache" in payload:
        value = payload.get("ldap-user-cache")
        if value and value not in VALID_BODY_LDAP_USER_CACHE:
            return (
                False,
                f"Invalid ldap-user-cache '{value}'. Must be one of: {', '.join(VALID_BODY_LDAP_USER_CACHE)}",
            )

    # Validate proxy-fqdn if present
    if "proxy-fqdn" in payload:
        value = payload.get("proxy-fqdn")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "proxy-fqdn cannot exceed 255 characters")

    # Validate max-request-length if present
    if "max-request-length" in payload:
        value = payload.get("max-request-length")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 2 or int_val > 64:
                    return (
                        False,
                        "max-request-length must be between 2 and 64",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"max-request-length must be numeric, got: {value}",
                )

    # Validate max-message-length if present
    if "max-message-length" in payload:
        value = payload.get("max-message-length")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 16 or int_val > 256:
                    return (
                        False,
                        "max-message-length must be between 16 and 256",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"max-message-length must be numeric, got: {value}",
                )

    # Validate http2-client-window-size if present
    if "http2-client-window-size" in payload:
        value = payload.get("http2-client-window-size")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 65535 or int_val > 2147483647:
                    return (
                        False,
                        "http2-client-window-size must be between 65535 and 2147483647",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"http2-client-window-size must be numeric, got: {value}",
                )

    # Validate http2-server-window-size if present
    if "http2-server-window-size" in payload:
        value = payload.get("http2-server-window-size")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 65535 or int_val > 2147483647:
                    return (
                        False,
                        "http2-server-window-size must be between 65535 and 2147483647",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"http2-server-window-size must be numeric, got: {value}",
                )

    # Validate auth-sign-timeout if present
    if "auth-sign-timeout" in payload:
        value = payload.get("auth-sign-timeout")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 30 or int_val > 3600:
                    return (
                        False,
                        "auth-sign-timeout must be between 30 and 3600",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"auth-sign-timeout must be numeric, got: {value}",
                )

    # Validate strict-web-check if present
    if "strict-web-check" in payload:
        value = payload.get("strict-web-check")
        if value and value not in VALID_BODY_STRICT_WEB_CHECK:
            return (
                False,
                f"Invalid strict-web-check '{value}'. Must be one of: {', '.join(VALID_BODY_STRICT_WEB_CHECK)}",
            )

    # Validate forward-proxy-auth if present
    if "forward-proxy-auth" in payload:
        value = payload.get("forward-proxy-auth")
        if value and value not in VALID_BODY_FORWARD_PROXY_AUTH:
            return (
                False,
                f"Invalid forward-proxy-auth '{value}'. Must be one of: {', '.join(VALID_BODY_FORWARD_PROXY_AUTH)}",
            )

    # Validate forward-server-affinity-timeout if present
    if "forward-server-affinity-timeout" in payload:
        value = payload.get("forward-server-affinity-timeout")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 6 or int_val > 60:
                    return (
                        False,
                        "forward-server-affinity-timeout must be between 6 and 60",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"forward-server-affinity-timeout must be numeric, got: {value}",
                )

    # Validate max-waf-body-cache-length if present
    if "max-waf-body-cache-length" in payload:
        value = payload.get("max-waf-body-cache-length")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 1024:
                    return (
                        False,
                        "max-waf-body-cache-length must be between 1 and 1024",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"max-waf-body-cache-length must be numeric, got: {value}",
                )

    # Validate webproxy-profile if present
    if "webproxy-profile" in payload:
        value = payload.get("webproxy-profile")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "webproxy-profile cannot exceed 63 characters")

    # Validate learn-client-ip if present
    if "learn-client-ip" in payload:
        value = payload.get("learn-client-ip")
        if value and value not in VALID_BODY_LEARN_CLIENT_IP:
            return (
                False,
                f"Invalid learn-client-ip '{value}'. Must be one of: {', '.join(VALID_BODY_LEARN_CLIENT_IP)}",
            )

    # Validate always-learn-client-ip if present
    if "always-learn-client-ip" in payload:
        value = payload.get("always-learn-client-ip")
        if value and value not in VALID_BODY_ALWAYS_LEARN_CLIENT_IP:
            return (
                False,
                f"Invalid always-learn-client-ip '{value}'. Must be one of: {', '.join(VALID_BODY_ALWAYS_LEARN_CLIENT_IP)}",
            )

    # Validate learn-client-ip-from-header if present
    if "learn-client-ip-from-header" in payload:
        value = payload.get("learn-client-ip-from-header")
        if value and value not in VALID_BODY_LEARN_CLIENT_IP_FROM_HEADER:
            return (
                False,
                f"Invalid learn-client-ip-from-header '{value}'. Must be one of: {', '.join(VALID_BODY_LEARN_CLIENT_IP_FROM_HEADER)}",
            )

    # Validate policy-partial-match if present
    if "policy-partial-match" in payload:
        value = payload.get("policy-partial-match")
        if value and value not in VALID_BODY_POLICY_PARTIAL_MATCH:
            return (
                False,
                f"Invalid policy-partial-match '{value}'. Must be one of: {', '.join(VALID_BODY_POLICY_PARTIAL_MATCH)}",
            )

    # Validate log-policy-pending if present
    if "log-policy-pending" in payload:
        value = payload.get("log-policy-pending")
        if value and value not in VALID_BODY_LOG_POLICY_PENDING:
            return (
                False,
                f"Invalid log-policy-pending '{value}'. Must be one of: {', '.join(VALID_BODY_LOG_POLICY_PENDING)}",
            )

    # Validate log-forward-server if present
    if "log-forward-server" in payload:
        value = payload.get("log-forward-server")
        if value and value not in VALID_BODY_LOG_FORWARD_SERVER:
            return (
                False,
                f"Invalid log-forward-server '{value}'. Must be one of: {', '.join(VALID_BODY_LOG_FORWARD_SERVER)}",
            )

    # Validate log-app-id if present
    if "log-app-id" in payload:
        value = payload.get("log-app-id")
        if value and value not in VALID_BODY_LOG_APP_ID:
            return (
                False,
                f"Invalid log-app-id '{value}'. Must be one of: {', '.join(VALID_BODY_LOG_APP_ID)}",
            )

    # Validate proxy-transparent-cert-inspection if present
    if "proxy-transparent-cert-inspection" in payload:
        value = payload.get("proxy-transparent-cert-inspection")
        if value and value not in VALID_BODY_PROXY_TRANSPARENT_CERT_INSPECTION:
            return (
                False,
                f"Invalid proxy-transparent-cert-inspection '{value}'. Must be one of: {', '.join(VALID_BODY_PROXY_TRANSPARENT_CERT_INSPECTION)}",
            )

    # Validate request-obs-fold if present
    if "request-obs-fold" in payload:
        value = payload.get("request-obs-fold")
        if value and value not in VALID_BODY_REQUEST_OBS_FOLD:
            return (
                False,
                f"Invalid request-obs-fold '{value}'. Must be one of: {', '.join(VALID_BODY_REQUEST_OBS_FOLD)}",
            )

    return (True, None)
