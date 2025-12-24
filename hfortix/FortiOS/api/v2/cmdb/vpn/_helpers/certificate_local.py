"""
Validation helpers for vpn certificate_local endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_RANGE = ["global", "vdom"]
VALID_BODY_SOURCE = ["factory", "user", "bundle"]
VALID_BODY_NAME_ENCODING = ["printable", "utf8"]
VALID_BODY_IKE_LOCALID_TYPE = ["asn1dn", "fqdn"]
VALID_BODY_ENROLL_PROTOCOL = ["none", "scep", "cmpv2", "acme2", "est"]
VALID_BODY_PRIVATE_KEY_RETAIN = ["enable", "disable"]
VALID_BODY_CMP_REGENERATION_METHOD = ["keyupate", "renewal"]
VALID_BODY_EST_REGENERATION_METHOD = ["create-new-key", "use-existing-key"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_certificate_local_get(
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


def validate_certificate_local_post(
    payload: dict[str, Any],
) -> tuple[bool, str | None]:
    """
    Validate POST request payload for creating certificate_local.

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

    # Validate comments if present
    if "comments" in payload:
        value = payload.get("comments")
        if value and isinstance(value, str) and len(value) > 511:
            return (False, "comments cannot exceed 511 characters")

    # Validate scep-url if present
    if "scep-url" in payload:
        value = payload.get("scep-url")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "scep-url cannot exceed 255 characters")

    # Validate range if present
    if "range" in payload:
        value = payload.get("range")
        if value and value not in VALID_BODY_RANGE:
            return (
                False,
                f"Invalid range '{value}'. Must be one of: {', '.join(VALID_BODY_RANGE)}",
            )

    # Validate source if present
    if "source" in payload:
        value = payload.get("source")
        if value and value not in VALID_BODY_SOURCE:
            return (
                False,
                f"Invalid source '{value}'. Must be one of: {', '.join(VALID_BODY_SOURCE)}",
            )

    # Validate auto-regenerate-days if present
    if "auto-regenerate-days" in payload:
        value = payload.get("auto-regenerate-days")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "auto-regenerate-days must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"auto-regenerate-days must be numeric, got: {value}",
                )

    # Validate auto-regenerate-days-warning if present
    if "auto-regenerate-days-warning" in payload:
        value = payload.get("auto-regenerate-days-warning")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "auto-regenerate-days-warning must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"auto-regenerate-days-warning must be numeric, got: {value}",
                )

    # Validate ca-identifier if present
    if "ca-identifier" in payload:
        value = payload.get("ca-identifier")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "ca-identifier cannot exceed 255 characters")

    # Validate name-encoding if present
    if "name-encoding" in payload:
        value = payload.get("name-encoding")
        if value and value not in VALID_BODY_NAME_ENCODING:
            return (
                False,
                f"Invalid name-encoding '{value}'. Must be one of: {', '.join(VALID_BODY_NAME_ENCODING)}",
            )

    # Validate ike-localid if present
    if "ike-localid" in payload:
        value = payload.get("ike-localid")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "ike-localid cannot exceed 63 characters")

    # Validate ike-localid-type if present
    if "ike-localid-type" in payload:
        value = payload.get("ike-localid-type")
        if value and value not in VALID_BODY_IKE_LOCALID_TYPE:
            return (
                False,
                f"Invalid ike-localid-type '{value}'. Must be one of: {', '.join(VALID_BODY_IKE_LOCALID_TYPE)}",
            )

    # Validate enroll-protocol if present
    if "enroll-protocol" in payload:
        value = payload.get("enroll-protocol")
        if value and value not in VALID_BODY_ENROLL_PROTOCOL:
            return (
                False,
                f"Invalid enroll-protocol '{value}'. Must be one of: {', '.join(VALID_BODY_ENROLL_PROTOCOL)}",
            )

    # Validate private-key-retain if present
    if "private-key-retain" in payload:
        value = payload.get("private-key-retain")
        if value and value not in VALID_BODY_PRIVATE_KEY_RETAIN:
            return (
                False,
                f"Invalid private-key-retain '{value}'. Must be one of: {', '.join(VALID_BODY_PRIVATE_KEY_RETAIN)}",
            )

    # Validate cmp-server if present
    if "cmp-server" in payload:
        value = payload.get("cmp-server")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "cmp-server cannot exceed 63 characters")

    # Validate cmp-path if present
    if "cmp-path" in payload:
        value = payload.get("cmp-path")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "cmp-path cannot exceed 255 characters")

    # Validate cmp-server-cert if present
    if "cmp-server-cert" in payload:
        value = payload.get("cmp-server-cert")
        if value and isinstance(value, str) and len(value) > 79:
            return (False, "cmp-server-cert cannot exceed 79 characters")

    # Validate cmp-regeneration-method if present
    if "cmp-regeneration-method" in payload:
        value = payload.get("cmp-regeneration-method")
        if value and value not in VALID_BODY_CMP_REGENERATION_METHOD:
            return (
                False,
                f"Invalid cmp-regeneration-method '{value}'. Must be one of: {', '.join(VALID_BODY_CMP_REGENERATION_METHOD)}",
            )

    # Validate acme-ca-url if present
    if "acme-ca-url" in payload:
        value = payload.get("acme-ca-url")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "acme-ca-url cannot exceed 255 characters")

    # Validate acme-domain if present
    if "acme-domain" in payload:
        value = payload.get("acme-domain")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "acme-domain cannot exceed 255 characters")

    # Validate acme-email if present
    if "acme-email" in payload:
        value = payload.get("acme-email")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "acme-email cannot exceed 255 characters")

    # Validate acme-eab-key-id if present
    if "acme-eab-key-id" in payload:
        value = payload.get("acme-eab-key-id")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "acme-eab-key-id cannot exceed 255 characters")

    # Validate acme-rsa-key-size if present
    if "acme-rsa-key-size" in payload:
        value = payload.get("acme-rsa-key-size")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 2048 or int_val > 4096:
                    return (
                        False,
                        "acme-rsa-key-size must be between 2048 and 4096",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"acme-rsa-key-size must be numeric, got: {value}",
                )

    # Validate acme-renew-window if present
    if "acme-renew-window" in payload:
        value = payload.get("acme-renew-window")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 100:
                    return (
                        False,
                        "acme-renew-window must be between 1 and 100",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"acme-renew-window must be numeric, got: {value}",
                )

    # Validate est-server if present
    if "est-server" in payload:
        value = payload.get("est-server")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "est-server cannot exceed 255 characters")

    # Validate est-ca-id if present
    if "est-ca-id" in payload:
        value = payload.get("est-ca-id")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "est-ca-id cannot exceed 255 characters")

    # Validate est-http-username if present
    if "est-http-username" in payload:
        value = payload.get("est-http-username")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "est-http-username cannot exceed 63 characters")

    # Validate est-client-cert if present
    if "est-client-cert" in payload:
        value = payload.get("est-client-cert")
        if value and isinstance(value, str) and len(value) > 79:
            return (False, "est-client-cert cannot exceed 79 characters")

    # Validate est-server-cert if present
    if "est-server-cert" in payload:
        value = payload.get("est-server-cert")
        if value and isinstance(value, str) and len(value) > 79:
            return (False, "est-server-cert cannot exceed 79 characters")

    # Validate est-srp-username if present
    if "est-srp-username" in payload:
        value = payload.get("est-srp-username")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "est-srp-username cannot exceed 63 characters")

    # Validate est-regeneration-method if present
    if "est-regeneration-method" in payload:
        value = payload.get("est-regeneration-method")
        if value and value not in VALID_BODY_EST_REGENERATION_METHOD:
            return (
                False,
                f"Invalid est-regeneration-method '{value}'. Must be one of: {', '.join(VALID_BODY_EST_REGENERATION_METHOD)}",
            )

    return (True, None)
