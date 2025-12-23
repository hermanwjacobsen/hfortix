"""
Validation helpers for vpn ipsec_manualkey endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_AUTHENTICATION = [
    "null",
    "md5",
    "sha1",
    "sha256",
    "sha384",
    "sha512",
]
VALID_BODY_ENCRYPTION = [
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


def validate_ipsec_manualkey_get(
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


def validate_ipsec_manualkey_post(
    payload: dict[str, Any],
) -> tuple[bool, str | None]:
    """
    Validate POST request payload for creating ipsec_manualkey.

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

    # Validate interface if present
    if "interface" in payload:
        value = payload.get("interface")
        if value and isinstance(value, str) and len(value) > 15:
            return (False, "interface cannot exceed 15 characters")

    # Validate authentication if present
    if "authentication" in payload:
        value = payload.get("authentication")
        if value and value not in VALID_BODY_AUTHENTICATION:
            return (
                False,
                f"Invalid authentication '{value}'. Must be one of: {', '.join(VALID_BODY_AUTHENTICATION)}",
            )

    # Validate encryption if present
    if "encryption" in payload:
        value = payload.get("encryption")
        if value and value not in VALID_BODY_ENCRYPTION:
            return (
                False,
                f"Invalid encryption '{value}'. Must be one of: {', '.join(VALID_BODY_ENCRYPTION)}",
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


def validate_ipsec_manualkey_put(
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
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "name cannot exceed 35 characters")

    # Validate interface if present
    if "interface" in payload:
        value = payload.get("interface")
        if value and isinstance(value, str) and len(value) > 15:
            return (False, "interface cannot exceed 15 characters")

    # Validate authentication if present
    if "authentication" in payload:
        value = payload.get("authentication")
        if value and value not in VALID_BODY_AUTHENTICATION:
            return (
                False,
                f"Invalid authentication '{value}'. Must be one of: {', '.join(VALID_BODY_AUTHENTICATION)}",
            )

    # Validate encryption if present
    if "encryption" in payload:
        value = payload.get("encryption")
        if value and value not in VALID_BODY_ENCRYPTION:
            return (
                False,
                f"Invalid encryption '{value}'. Must be one of: {', '.join(VALID_BODY_ENCRYPTION)}",
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


def validate_ipsec_manualkey_delete(
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
