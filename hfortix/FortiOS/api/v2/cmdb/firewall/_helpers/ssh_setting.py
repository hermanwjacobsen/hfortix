"""
Validation helpers for firewall ssh_setting endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_HOST_TRUSTED_CHECKING = ["enable", "disable"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_ssh_setting_get(
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


def validate_ssh_setting_put(
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

    # Validate hostkey-rsa2048 if present
    if "hostkey-rsa2048" in payload:
        value = payload.get("hostkey-rsa2048")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "hostkey-rsa2048 cannot exceed 35 characters")

    # Validate hostkey-dsa1024 if present
    if "hostkey-dsa1024" in payload:
        value = payload.get("hostkey-dsa1024")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "hostkey-dsa1024 cannot exceed 35 characters")

    # Validate hostkey-ecdsa256 if present
    if "hostkey-ecdsa256" in payload:
        value = payload.get("hostkey-ecdsa256")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "hostkey-ecdsa256 cannot exceed 35 characters")

    # Validate hostkey-ecdsa384 if present
    if "hostkey-ecdsa384" in payload:
        value = payload.get("hostkey-ecdsa384")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "hostkey-ecdsa384 cannot exceed 35 characters")

    # Validate hostkey-ecdsa521 if present
    if "hostkey-ecdsa521" in payload:
        value = payload.get("hostkey-ecdsa521")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "hostkey-ecdsa521 cannot exceed 35 characters")

    # Validate hostkey-ed25519 if present
    if "hostkey-ed25519" in payload:
        value = payload.get("hostkey-ed25519")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "hostkey-ed25519 cannot exceed 35 characters")

    # Validate host-trusted-checking if present
    if "host-trusted-checking" in payload:
        value = payload.get("host-trusted-checking")
        if value and value not in VALID_BODY_HOST_TRUSTED_CHECKING:
            return (
                False,
                f"Invalid host-trusted-checking '{value}'. Must be one of: {', '.join(VALID_BODY_HOST_TRUSTED_CHECKING)}",
            )

    return (True, None)
