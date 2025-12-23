"""
Validation helpers for log fortianalyzer_setting endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_STATUS = ["enable", "disable"]
VALID_BODY_IPS_ARCHIVE = ["enable", "disable"]
VALID_BODY_FALLBACK_TO_PRIMARY = ["enable", "disable"]
VALID_BODY_CERTIFICATE_VERIFICATION = ["enable", "disable"]
VALID_BODY_ACCESS_CONFIG = ["enable", "disable"]
VALID_BODY_HMAC_ALGORITHM = ["sha256"]
VALID_BODY_ENC_ALGORITHM = ["high-medium", "high", "low"]
VALID_BODY_SSL_MIN_PROTO_VERSION = [
    "default",
    "SSLv3",
    "TLSv1",
    "TLSv1-1",
    "TLSv1-2",
    "TLSv1-3",
]
VALID_BODY_UPLOAD_OPTION = [
    "store-and-upload",
    "realtime",
    "1-minute",
    "5-minute",
]
VALID_BODY_UPLOAD_INTERVAL = ["daily", "weekly", "monthly"]
VALID_BODY_RELIABLE = ["enable", "disable"]
VALID_BODY_PRIORITY = ["default", "low"]
VALID_BODY_INTERFACE_SELECT_METHOD = ["auto", "sdwan", "specify"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_fortianalyzer_setting_get(
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


def validate_fortianalyzer_setting_put(
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

    # Validate ips-archive if present
    if "ips-archive" in payload:
        value = payload.get("ips-archive")
        if value and value not in VALID_BODY_IPS_ARCHIVE:
            return (
                False,
                f"Invalid ips-archive '{value}'. Must be one of: {', '.join(VALID_BODY_IPS_ARCHIVE)}",
            )

    # Validate server if present
    if "server" in payload:
        value = payload.get("server")
        if value and isinstance(value, str) and len(value) > 127:
            return (False, "server cannot exceed 127 characters")

    # Validate alt-server if present
    if "alt-server" in payload:
        value = payload.get("alt-server")
        if value and isinstance(value, str) and len(value) > 127:
            return (False, "alt-server cannot exceed 127 characters")

    # Validate fallback-to-primary if present
    if "fallback-to-primary" in payload:
        value = payload.get("fallback-to-primary")
        if value and value not in VALID_BODY_FALLBACK_TO_PRIMARY:
            return (
                False,
                f"Invalid fallback-to-primary '{value}'. Must be one of: {', '.join(VALID_BODY_FALLBACK_TO_PRIMARY)}",
            )

    # Validate certificate-verification if present
    if "certificate-verification" in payload:
        value = payload.get("certificate-verification")
        if value and value not in VALID_BODY_CERTIFICATE_VERIFICATION:
            return (
                False,
                f"Invalid certificate-verification '{value}'. Must be one of: {', '.join(VALID_BODY_CERTIFICATE_VERIFICATION)}",
            )

    # Validate server-cert-ca if present
    if "server-cert-ca" in payload:
        value = payload.get("server-cert-ca")
        if value and isinstance(value, str) and len(value) > 79:
            return (False, "server-cert-ca cannot exceed 79 characters")

    # Validate preshared-key if present
    if "preshared-key" in payload:
        value = payload.get("preshared-key")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "preshared-key cannot exceed 63 characters")

    # Validate access-config if present
    if "access-config" in payload:
        value = payload.get("access-config")
        if value and value not in VALID_BODY_ACCESS_CONFIG:
            return (
                False,
                f"Invalid access-config '{value}'. Must be one of: {', '.join(VALID_BODY_ACCESS_CONFIG)}",
            )

    # Validate hmac-algorithm if present
    if "hmac-algorithm" in payload:
        value = payload.get("hmac-algorithm")
        if value and value not in VALID_BODY_HMAC_ALGORITHM:
            return (
                False,
                f"Invalid hmac-algorithm '{value}'. Must be one of: {', '.join(VALID_BODY_HMAC_ALGORITHM)}",
            )

    # Validate enc-algorithm if present
    if "enc-algorithm" in payload:
        value = payload.get("enc-algorithm")
        if value and value not in VALID_BODY_ENC_ALGORITHM:
            return (
                False,
                f"Invalid enc-algorithm '{value}'. Must be one of: {', '.join(VALID_BODY_ENC_ALGORITHM)}",
            )

    # Validate ssl-min-proto-version if present
    if "ssl-min-proto-version" in payload:
        value = payload.get("ssl-min-proto-version")
        if value and value not in VALID_BODY_SSL_MIN_PROTO_VERSION:
            return (
                False,
                f"Invalid ssl-min-proto-version '{value}'. Must be one of: {', '.join(VALID_BODY_SSL_MIN_PROTO_VERSION)}",
            )

    # Validate conn-timeout if present
    if "conn-timeout" in payload:
        value = payload.get("conn-timeout")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 3600:
                    return (False, "conn-timeout must be between 1 and 3600")
            except (ValueError, TypeError):
                return (False, f"conn-timeout must be numeric, got: {value}")

    # Validate monitor-keepalive-period if present
    if "monitor-keepalive-period" in payload:
        value = payload.get("monitor-keepalive-period")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 120:
                    return (
                        False,
                        "monitor-keepalive-period must be between 1 and 120",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"monitor-keepalive-period must be numeric, got: {value}",
                )

    # Validate monitor-failure-retry-period if present
    if "monitor-failure-retry-period" in payload:
        value = payload.get("monitor-failure-retry-period")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 86400:
                    return (
                        False,
                        "monitor-failure-retry-period must be between 1 and 86400",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"monitor-failure-retry-period must be numeric, got: {value}",
                )

    # Validate certificate if present
    if "certificate" in payload:
        value = payload.get("certificate")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "certificate cannot exceed 35 characters")

    # Validate source-ip if present
    if "source-ip" in payload:
        value = payload.get("source-ip")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "source-ip cannot exceed 63 characters")

    # Validate upload-option if present
    if "upload-option" in payload:
        value = payload.get("upload-option")
        if value and value not in VALID_BODY_UPLOAD_OPTION:
            return (
                False,
                f"Invalid upload-option '{value}'. Must be one of: {', '.join(VALID_BODY_UPLOAD_OPTION)}",
            )

    # Validate upload-interval if present
    if "upload-interval" in payload:
        value = payload.get("upload-interval")
        if value and value not in VALID_BODY_UPLOAD_INTERVAL:
            return (
                False,
                f"Invalid upload-interval '{value}'. Must be one of: {', '.join(VALID_BODY_UPLOAD_INTERVAL)}",
            )

    # Validate reliable if present
    if "reliable" in payload:
        value = payload.get("reliable")
        if value and value not in VALID_BODY_RELIABLE:
            return (
                False,
                f"Invalid reliable '{value}'. Must be one of: {', '.join(VALID_BODY_RELIABLE)}",
            )

    # Validate priority if present
    if "priority" in payload:
        value = payload.get("priority")
        if value and value not in VALID_BODY_PRIORITY:
            return (
                False,
                f"Invalid priority '{value}'. Must be one of: {', '.join(VALID_BODY_PRIORITY)}",
            )

    # Validate max-log-rate if present
    if "max-log-rate" in payload:
        value = payload.get("max-log-rate")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 100000:
                    return (
                        False,
                        "max-log-rate must be between 0 and 100000",
                    )
            except (ValueError, TypeError):
                return (False, f"max-log-rate must be numeric, got: {value}")

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

    return (True, None)
