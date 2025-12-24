"""
Validation helpers for vpn ipsec_manualkey_interface endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_IP_VERSION = ["4", "6"]
VALID_BODY_ADDR_TYPE = ["4", "6"]
VALID_BODY_AUTH_ALG = ["null", "md5", "sha1", "sha256", "sha384", "sha512"]
VALID_BODY_ENC_ALG = [
    "null",
    "des",
    "3des",
    "aes128",
    "aes192",
    "aes256",
    "aria128",
    "aria192",
    "aria256",
    "seed",
]
VALID_BODY_NPU_OFFLOAD = ["enable", "disable"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_ipsec_manualkey_interface_get(
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


def validate_ipsec_manualkey_interface_post(
    payload: dict[str, Any],
) -> tuple[bool, str | None]:
    """
    Validate POST request payload for creating ipsec_manualkey_interface.

    Args:
        payload: The payload to validate

    Returns:
        Tuple of (is_valid, error_message)
    """
    # Validate name if present
    if "name" in payload:
        value = payload.get("name")
        if value and isinstance(value, str) and len(value) > 15:
            return (False, "name cannot exceed 15 characters")

    # Validate interface if present
    if "interface" in payload:
        value = payload.get("interface")
        if value and isinstance(value, str) and len(value) > 15:
            return (False, "interface cannot exceed 15 characters")

    # Validate ip-version if present
    if "ip-version" in payload:
        value = payload.get("ip-version")
        if value and value not in VALID_BODY_IP_VERSION:
            return (
                False,
                f"Invalid ip-version '{value}'. Must be one of: {', '.join(VALID_BODY_IP_VERSION)}",
            )

    # Validate addr-type if present
    if "addr-type" in payload:
        value = payload.get("addr-type")
        if value and value not in VALID_BODY_ADDR_TYPE:
            return (
                False,
                f"Invalid addr-type '{value}'. Must be one of: {', '.join(VALID_BODY_ADDR_TYPE)}",
            )

    # Validate auth-alg if present
    if "auth-alg" in payload:
        value = payload.get("auth-alg")
        if value and value not in VALID_BODY_AUTH_ALG:
            return (
                False,
                f"Invalid auth-alg '{value}'. Must be one of: {', '.join(VALID_BODY_AUTH_ALG)}",
            )

    # Validate enc-alg if present
    if "enc-alg" in payload:
        value = payload.get("enc-alg")
        if value and value not in VALID_BODY_ENC_ALG:
            return (
                False,
                f"Invalid enc-alg '{value}'. Must be one of: {', '.join(VALID_BODY_ENC_ALG)}",
            )

    # Validate npu-offload if present
    if "npu-offload" in payload:
        value = payload.get("npu-offload")
        if value and value not in VALID_BODY_NPU_OFFLOAD:
            return (
                False,
                f"Invalid npu-offload '{value}'. Must be one of: {', '.join(VALID_BODY_NPU_OFFLOAD)}",
            )

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_ipsec_manualkey_interface_put(
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
        if value and isinstance(value, str) and len(value) > 15:
            return (False, "name cannot exceed 15 characters")

    # Validate interface if present
    if "interface" in payload:
        value = payload.get("interface")
        if value and isinstance(value, str) and len(value) > 15:
            return (False, "interface cannot exceed 15 characters")

    # Validate ip-version if present
    if "ip-version" in payload:
        value = payload.get("ip-version")
        if value and value not in VALID_BODY_IP_VERSION:
            return (
                False,
                f"Invalid ip-version '{value}'. Must be one of: {', '.join(VALID_BODY_IP_VERSION)}",
            )

    # Validate addr-type if present
    if "addr-type" in payload:
        value = payload.get("addr-type")
        if value and value not in VALID_BODY_ADDR_TYPE:
            return (
                False,
                f"Invalid addr-type '{value}'. Must be one of: {', '.join(VALID_BODY_ADDR_TYPE)}",
            )

    # Validate auth-alg if present
    if "auth-alg" in payload:
        value = payload.get("auth-alg")
        if value and value not in VALID_BODY_AUTH_ALG:
            return (
                False,
                f"Invalid auth-alg '{value}'. Must be one of: {', '.join(VALID_BODY_AUTH_ALG)}",
            )

    # Validate enc-alg if present
    if "enc-alg" in payload:
        value = payload.get("enc-alg")
        if value and value not in VALID_BODY_ENC_ALG:
            return (
                False,
                f"Invalid enc-alg '{value}'. Must be one of: {', '.join(VALID_BODY_ENC_ALG)}",
            )

    # Validate npu-offload if present
    if "npu-offload" in payload:
        value = payload.get("npu-offload")
        if value and value not in VALID_BODY_NPU_OFFLOAD:
            return (
                False,
                f"Invalid npu-offload '{value}'. Must be one of: {', '.join(VALID_BODY_NPU_OFFLOAD)}",
            )

    return (True, None)


# ============================================================================
# DELETE Validation
# ============================================================================


def validate_ipsec_manualkey_interface_delete(
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
