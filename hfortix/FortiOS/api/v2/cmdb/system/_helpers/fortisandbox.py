"""
Validation helpers for system fortisandbox endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_STATUS = ["enable", "disable"]
VALID_BODY_FORTICLOUD = ["enable", "disable"]
VALID_BODY_INTERFACE_SELECT_METHOD = ["auto", "sdwan", "specify"]
VALID_BODY_ENC_ALGORITHM = ["default", "high", "low"]
VALID_BODY_SSL_MIN_PROTO_VERSION = [
    "default",
    "SSLv3",
    "TLSv1",
    "TLSv1-1",
    "TLSv1-2",
    "TLSv1-3",
]
VALID_BODY_CERTIFICATE_VERIFICATION = ["enable", "disable"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_fortisandbox_get(
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


def validate_fortisandbox_put(
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

    # Validate forticloud if present
    if "forticloud" in payload:
        value = payload.get("forticloud")
        if value and value not in VALID_BODY_FORTICLOUD:
            return (
                False,
                f"Invalid forticloud '{value}'. Must be one of: {', '.join(VALID_BODY_FORTICLOUD)}",
            )

    # Validate server if present
    if "server" in payload:
        value = payload.get("server")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "server cannot exceed 63 characters")

    # Validate source-ip if present
    if "source-ip" in payload:
        value = payload.get("source-ip")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "source-ip cannot exceed 63 characters")

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

    # Validate email if present
    if "email" in payload:
        value = payload.get("email")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "email cannot exceed 63 characters")

    # Validate ca if present
    if "ca" in payload:
        value = payload.get("ca")
        if value and isinstance(value, str) and len(value) > 79:
            return (False, "ca cannot exceed 79 characters")

    # Validate cn if present
    if "cn" in payload:
        value = payload.get("cn")
        if value and isinstance(value, str) and len(value) > 127:
            return (False, "cn cannot exceed 127 characters")

    # Validate certificate-verification if present
    if "certificate-verification" in payload:
        value = payload.get("certificate-verification")
        if value and value not in VALID_BODY_CERTIFICATE_VERIFICATION:
            return (
                False,
                f"Invalid certificate-verification '{value}'. Must be one of: {', '.join(VALID_BODY_CERTIFICATE_VERIFICATION)}",
            )

    return (True, None)
