"""
Validation helpers for vpn certificate_setting endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_OCSP_STATUS = ["enable", "mandatory", "disable"]
VALID_BODY_OCSP_OPTION = ["certificate", "server"]
VALID_BODY_INTERFACE_SELECT_METHOD = ["auto", "sdwan", "specify"]
VALID_BODY_CHECK_CA_CERT = ["enable", "disable"]
VALID_BODY_CHECK_CA_CHAIN = ["enable", "disable"]
VALID_BODY_SUBJECT_MATCH = ["substring", "value"]
VALID_BODY_SUBJECT_SET = ["subset", "superset"]
VALID_BODY_CN_MATCH = ["substring", "value"]
VALID_BODY_CN_ALLOW_MULTI = ["disable", "enable"]
VALID_BODY_STRICT_OCSP_CHECK = ["enable", "disable"]
VALID_BODY_SSL_MIN_PROTO_VERSION = [
    "default",
    "SSLv3",
    "TLSv1",
    "TLSv1-1",
    "TLSv1-2",
    "TLSv1-3",
]
VALID_BODY_CMP_SAVE_EXTRA_CERTS = ["enable", "disable"]
VALID_BODY_CMP_KEY_USAGE_CHECKING = ["enable", "disable"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_certificate_setting_get(
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


def validate_certificate_setting_put(
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

    # Validate ocsp-status if present
    if "ocsp-status" in payload:
        value = payload.get("ocsp-status")
        if value and value not in VALID_BODY_OCSP_STATUS:
            return (
                False,
                f"Invalid ocsp-status '{value}'. Must be one of: {', '.join(VALID_BODY_OCSP_STATUS)}",
            )

    # Validate ocsp-option if present
    if "ocsp-option" in payload:
        value = payload.get("ocsp-option")
        if value and value not in VALID_BODY_OCSP_OPTION:
            return (
                False,
                f"Invalid ocsp-option '{value}'. Must be one of: {', '.join(VALID_BODY_OCSP_OPTION)}",
            )

    # Validate proxy if present
    if "proxy" in payload:
        value = payload.get("proxy")
        if value and isinstance(value, str) and len(value) > 127:
            return (False, "proxy cannot exceed 127 characters")

    # Validate proxy-port if present
    if "proxy-port" in payload:
        value = payload.get("proxy-port")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 65535:
                    return (False, "proxy-port must be between 1 and 65535")
            except (ValueError, TypeError):
                return (False, f"proxy-port must be numeric, got: {value}")

    # Validate proxy-username if present
    if "proxy-username" in payload:
        value = payload.get("proxy-username")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "proxy-username cannot exceed 63 characters")

    # Validate source-ip if present
    if "source-ip" in payload:
        value = payload.get("source-ip")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "source-ip cannot exceed 63 characters")

    # Validate ocsp-default-server if present
    if "ocsp-default-server" in payload:
        value = payload.get("ocsp-default-server")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "ocsp-default-server cannot exceed 35 characters")

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

    # Validate check-ca-cert if present
    if "check-ca-cert" in payload:
        value = payload.get("check-ca-cert")
        if value and value not in VALID_BODY_CHECK_CA_CERT:
            return (
                False,
                f"Invalid check-ca-cert '{value}'. Must be one of: {', '.join(VALID_BODY_CHECK_CA_CERT)}",
            )

    # Validate check-ca-chain if present
    if "check-ca-chain" in payload:
        value = payload.get("check-ca-chain")
        if value and value not in VALID_BODY_CHECK_CA_CHAIN:
            return (
                False,
                f"Invalid check-ca-chain '{value}'. Must be one of: {', '.join(VALID_BODY_CHECK_CA_CHAIN)}",
            )

    # Validate subject-match if present
    if "subject-match" in payload:
        value = payload.get("subject-match")
        if value and value not in VALID_BODY_SUBJECT_MATCH:
            return (
                False,
                f"Invalid subject-match '{value}'. Must be one of: {', '.join(VALID_BODY_SUBJECT_MATCH)}",
            )

    # Validate subject-set if present
    if "subject-set" in payload:
        value = payload.get("subject-set")
        if value and value not in VALID_BODY_SUBJECT_SET:
            return (
                False,
                f"Invalid subject-set '{value}'. Must be one of: {', '.join(VALID_BODY_SUBJECT_SET)}",
            )

    # Validate cn-match if present
    if "cn-match" in payload:
        value = payload.get("cn-match")
        if value and value not in VALID_BODY_CN_MATCH:
            return (
                False,
                f"Invalid cn-match '{value}'. Must be one of: {', '.join(VALID_BODY_CN_MATCH)}",
            )

    # Validate cn-allow-multi if present
    if "cn-allow-multi" in payload:
        value = payload.get("cn-allow-multi")
        if value and value not in VALID_BODY_CN_ALLOW_MULTI:
            return (
                False,
                f"Invalid cn-allow-multi '{value}'. Must be one of: {', '.join(VALID_BODY_CN_ALLOW_MULTI)}",
            )

    # Validate strict-ocsp-check if present
    if "strict-ocsp-check" in payload:
        value = payload.get("strict-ocsp-check")
        if value and value not in VALID_BODY_STRICT_OCSP_CHECK:
            return (
                False,
                f"Invalid strict-ocsp-check '{value}'. Must be one of: {', '.join(VALID_BODY_STRICT_OCSP_CHECK)}",
            )

    # Validate ssl-min-proto-version if present
    if "ssl-min-proto-version" in payload:
        value = payload.get("ssl-min-proto-version")
        if value and value not in VALID_BODY_SSL_MIN_PROTO_VERSION:
            return (
                False,
                f"Invalid ssl-min-proto-version '{value}'. Must be one of: {', '.join(VALID_BODY_SSL_MIN_PROTO_VERSION)}",
            )

    # Validate cmp-save-extra-certs if present
    if "cmp-save-extra-certs" in payload:
        value = payload.get("cmp-save-extra-certs")
        if value and value not in VALID_BODY_CMP_SAVE_EXTRA_CERTS:
            return (
                False,
                f"Invalid cmp-save-extra-certs '{value}'. Must be one of: {', '.join(VALID_BODY_CMP_SAVE_EXTRA_CERTS)}",
            )

    # Validate cmp-key-usage-checking if present
    if "cmp-key-usage-checking" in payload:
        value = payload.get("cmp-key-usage-checking")
        if value and value not in VALID_BODY_CMP_KEY_USAGE_CHECKING:
            return (
                False,
                f"Invalid cmp-key-usage-checking '{value}'. Must be one of: {', '.join(VALID_BODY_CMP_KEY_USAGE_CHECKING)}",
            )

    # Validate cert-expire-warning if present
    if "cert-expire-warning" in payload:
        value = payload.get("cert-expire-warning")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 100:
                    return (
                        False,
                        "cert-expire-warning must be between 0 and 100",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"cert-expire-warning must be numeric, got: {value}",
                )

    # Validate certname-rsa1024 if present
    if "certname-rsa1024" in payload:
        value = payload.get("certname-rsa1024")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "certname-rsa1024 cannot exceed 35 characters")

    # Validate certname-rsa2048 if present
    if "certname-rsa2048" in payload:
        value = payload.get("certname-rsa2048")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "certname-rsa2048 cannot exceed 35 characters")

    # Validate certname-rsa4096 if present
    if "certname-rsa4096" in payload:
        value = payload.get("certname-rsa4096")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "certname-rsa4096 cannot exceed 35 characters")

    # Validate certname-dsa1024 if present
    if "certname-dsa1024" in payload:
        value = payload.get("certname-dsa1024")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "certname-dsa1024 cannot exceed 35 characters")

    # Validate certname-dsa2048 if present
    if "certname-dsa2048" in payload:
        value = payload.get("certname-dsa2048")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "certname-dsa2048 cannot exceed 35 characters")

    # Validate certname-ecdsa256 if present
    if "certname-ecdsa256" in payload:
        value = payload.get("certname-ecdsa256")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "certname-ecdsa256 cannot exceed 35 characters")

    # Validate certname-ecdsa384 if present
    if "certname-ecdsa384" in payload:
        value = payload.get("certname-ecdsa384")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "certname-ecdsa384 cannot exceed 35 characters")

    # Validate certname-ecdsa521 if present
    if "certname-ecdsa521" in payload:
        value = payload.get("certname-ecdsa521")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "certname-ecdsa521 cannot exceed 35 characters")

    # Validate certname-ed25519 if present
    if "certname-ed25519" in payload:
        value = payload.get("certname-ed25519")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "certname-ed25519 cannot exceed 35 characters")

    # Validate certname-ed448 if present
    if "certname-ed448" in payload:
        value = payload.get("certname-ed448")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "certname-ed448 cannot exceed 35 characters")

    return (True, None)
