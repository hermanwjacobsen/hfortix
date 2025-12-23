"""
Validation helpers for user setting endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_AUTH_TYPE = ["http", "https", "ftp", "telnet"]
VALID_BODY_AUTH_SECURE_HTTP = ["enable", "disable"]
VALID_BODY_AUTH_HTTP_BASIC = ["enable", "disable"]
VALID_BODY_AUTH_SSL_ALLOW_RENEGOTIATION = ["enable", "disable"]
VALID_BODY_AUTH_SRC_MAC = ["enable", "disable"]
VALID_BODY_AUTH_ON_DEMAND = ["always", "implicitly"]
VALID_BODY_AUTH_TIMEOUT_TYPE = ["idle-timeout", "hard-timeout", "new-session"]
VALID_BODY_RADIUS_SES_TIMEOUT_ACT = ["hard-timeout", "ignore-timeout"]
VALID_BODY_PER_POLICY_DISCLAIMER = ["enable", "disable"]
VALID_BODY_AUTH_SSL_MIN_PROTO_VERSION = [
    "default",
    "SSLv3",
    "TLSv1",
    "TLSv1-1",
    "TLSv1-2",
    "TLSv1-3",
]
VALID_BODY_AUTH_SSL_MAX_PROTO_VERSION = [
    "sslv3",
    "tlsv1",
    "tlsv1-1",
    "tlsv1-2",
    "tlsv1-3",
]
VALID_BODY_AUTH_SSL_SIGALGS = ["no-rsa-pss", "all"]
VALID_BODY_CORS = ["disable", "enable"]
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

    # Validate auth-type if present
    if "auth-type" in payload:
        value = payload.get("auth-type")
        if value and value not in VALID_BODY_AUTH_TYPE:
            return (
                False,
                f"Invalid auth-type '{value}'. Must be one of: {', '.join(VALID_BODY_AUTH_TYPE)}",
            )

    # Validate auth-cert if present
    if "auth-cert" in payload:
        value = payload.get("auth-cert")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "auth-cert cannot exceed 35 characters")

    # Validate auth-ca-cert if present
    if "auth-ca-cert" in payload:
        value = payload.get("auth-ca-cert")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "auth-ca-cert cannot exceed 35 characters")

    # Validate auth-secure-http if present
    if "auth-secure-http" in payload:
        value = payload.get("auth-secure-http")
        if value and value not in VALID_BODY_AUTH_SECURE_HTTP:
            return (
                False,
                f"Invalid auth-secure-http '{value}'. Must be one of: {', '.join(VALID_BODY_AUTH_SECURE_HTTP)}",
            )

    # Validate auth-http-basic if present
    if "auth-http-basic" in payload:
        value = payload.get("auth-http-basic")
        if value and value not in VALID_BODY_AUTH_HTTP_BASIC:
            return (
                False,
                f"Invalid auth-http-basic '{value}'. Must be one of: {', '.join(VALID_BODY_AUTH_HTTP_BASIC)}",
            )

    # Validate auth-ssl-allow-renegotiation if present
    if "auth-ssl-allow-renegotiation" in payload:
        value = payload.get("auth-ssl-allow-renegotiation")
        if value and value not in VALID_BODY_AUTH_SSL_ALLOW_RENEGOTIATION:
            return (
                False,
                f"Invalid auth-ssl-allow-renegotiation '{value}'. Must be one of: {', '.join(VALID_BODY_AUTH_SSL_ALLOW_RENEGOTIATION)}",
            )

    # Validate auth-src-mac if present
    if "auth-src-mac" in payload:
        value = payload.get("auth-src-mac")
        if value and value not in VALID_BODY_AUTH_SRC_MAC:
            return (
                False,
                f"Invalid auth-src-mac '{value}'. Must be one of: {', '.join(VALID_BODY_AUTH_SRC_MAC)}",
            )

    # Validate auth-on-demand if present
    if "auth-on-demand" in payload:
        value = payload.get("auth-on-demand")
        if value and value not in VALID_BODY_AUTH_ON_DEMAND:
            return (
                False,
                f"Invalid auth-on-demand '{value}'. Must be one of: {', '.join(VALID_BODY_AUTH_ON_DEMAND)}",
            )

    # Validate auth-timeout if present
    if "auth-timeout" in payload:
        value = payload.get("auth-timeout")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 1440:
                    return (False, "auth-timeout must be between 1 and 1440")
            except (ValueError, TypeError):
                return (False, f"auth-timeout must be numeric, got: {value}")

    # Validate auth-timeout-type if present
    if "auth-timeout-type" in payload:
        value = payload.get("auth-timeout-type")
        if value and value not in VALID_BODY_AUTH_TIMEOUT_TYPE:
            return (
                False,
                f"Invalid auth-timeout-type '{value}'. Must be one of: {', '.join(VALID_BODY_AUTH_TIMEOUT_TYPE)}",
            )

    # Validate auth-portal-timeout if present
    if "auth-portal-timeout" in payload:
        value = payload.get("auth-portal-timeout")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 30:
                    return (
                        False,
                        "auth-portal-timeout must be between 1 and 30",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"auth-portal-timeout must be numeric, got: {value}",
                )

    # Validate radius-ses-timeout-act if present
    if "radius-ses-timeout-act" in payload:
        value = payload.get("radius-ses-timeout-act")
        if value and value not in VALID_BODY_RADIUS_SES_TIMEOUT_ACT:
            return (
                False,
                f"Invalid radius-ses-timeout-act '{value}'. Must be one of: {', '.join(VALID_BODY_RADIUS_SES_TIMEOUT_ACT)}",
            )

    # Validate auth-blackout-time if present
    if "auth-blackout-time" in payload:
        value = payload.get("auth-blackout-time")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 3600:
                    return (
                        False,
                        "auth-blackout-time must be between 0 and 3600",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"auth-blackout-time must be numeric, got: {value}",
                )

    # Validate auth-invalid-max if present
    if "auth-invalid-max" in payload:
        value = payload.get("auth-invalid-max")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 100:
                    return (
                        False,
                        "auth-invalid-max must be between 1 and 100",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"auth-invalid-max must be numeric, got: {value}",
                )

    # Validate auth-lockout-threshold if present
    if "auth-lockout-threshold" in payload:
        value = payload.get("auth-lockout-threshold")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 10:
                    return (
                        False,
                        "auth-lockout-threshold must be between 1 and 10",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"auth-lockout-threshold must be numeric, got: {value}",
                )

    # Validate auth-lockout-duration if present
    if "auth-lockout-duration" in payload:
        value = payload.get("auth-lockout-duration")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "auth-lockout-duration must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"auth-lockout-duration must be numeric, got: {value}",
                )

    # Validate per-policy-disclaimer if present
    if "per-policy-disclaimer" in payload:
        value = payload.get("per-policy-disclaimer")
        if value and value not in VALID_BODY_PER_POLICY_DISCLAIMER:
            return (
                False,
                f"Invalid per-policy-disclaimer '{value}'. Must be one of: {', '.join(VALID_BODY_PER_POLICY_DISCLAIMER)}",
            )

    # Validate auth-ssl-min-proto-version if present
    if "auth-ssl-min-proto-version" in payload:
        value = payload.get("auth-ssl-min-proto-version")
        if value and value not in VALID_BODY_AUTH_SSL_MIN_PROTO_VERSION:
            return (
                False,
                f"Invalid auth-ssl-min-proto-version '{value}'. Must be one of: {', '.join(VALID_BODY_AUTH_SSL_MIN_PROTO_VERSION)}",
            )

    # Validate auth-ssl-max-proto-version if present
    if "auth-ssl-max-proto-version" in payload:
        value = payload.get("auth-ssl-max-proto-version")
        if value and value not in VALID_BODY_AUTH_SSL_MAX_PROTO_VERSION:
            return (
                False,
                f"Invalid auth-ssl-max-proto-version '{value}'. Must be one of: {', '.join(VALID_BODY_AUTH_SSL_MAX_PROTO_VERSION)}",
            )

    # Validate auth-ssl-sigalgs if present
    if "auth-ssl-sigalgs" in payload:
        value = payload.get("auth-ssl-sigalgs")
        if value and value not in VALID_BODY_AUTH_SSL_SIGALGS:
            return (
                False,
                f"Invalid auth-ssl-sigalgs '{value}'. Must be one of: {', '.join(VALID_BODY_AUTH_SSL_SIGALGS)}",
            )

    # Validate default-user-password-policy if present
    if "default-user-password-policy" in payload:
        value = payload.get("default-user-password-policy")
        if value and isinstance(value, str) and len(value) > 35:
            return (
                False,
                "default-user-password-policy cannot exceed 35 characters",
            )

    # Validate cors if present
    if "cors" in payload:
        value = payload.get("cors")
        if value and value not in VALID_BODY_CORS:
            return (
                False,
                f"Invalid cors '{value}'. Must be one of: {', '.join(VALID_BODY_CORS)}",
            )

    return (True, None)
