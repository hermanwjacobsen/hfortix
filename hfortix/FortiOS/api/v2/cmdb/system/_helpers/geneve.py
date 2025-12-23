"""
Validation helpers for system geneve endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_TYPE = ["ethernet", "ppp"]
VALID_BODY_IP_VERSION = ["ipv4-unicast", "ipv6-unicast"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_geneve_get(
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


def validate_geneve_post(payload: dict[str, Any]) -> tuple[bool, str | None]:
    """
    Validate POST request payload for creating geneve.

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

    # Validate vni if present
    if "vni" in payload:
        value = payload.get("vni")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 16777215:
                    return (False, "vni must be between 0 and 16777215")
            except (ValueError, TypeError):
                return (False, f"vni must be numeric, got: {value}")

    # Validate type if present
    if "type" in payload:
        value = payload.get("type")
        if value and value not in VALID_BODY_TYPE:
            return (
                False,
                f"Invalid type '{value}'. Must be one of: {', '.join(VALID_BODY_TYPE)}",
            )

    # Validate ip-version if present
    if "ip-version" in payload:
        value = payload.get("ip-version")
        if value and value not in VALID_BODY_IP_VERSION:
            return (
                False,
                f"Invalid ip-version '{value}'. Must be one of: {', '.join(VALID_BODY_IP_VERSION)}",
            )

    # Validate dstport if present
    if "dstport" in payload:
        value = payload.get("dstport")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 65535:
                    return (False, "dstport must be between 1 and 65535")
            except (ValueError, TypeError):
                return (False, f"dstport must be numeric, got: {value}")

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_geneve_put(
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

    # Validate vni if present
    if "vni" in payload:
        value = payload.get("vni")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 16777215:
                    return (False, "vni must be between 0 and 16777215")
            except (ValueError, TypeError):
                return (False, f"vni must be numeric, got: {value}")

    # Validate type if present
    if "type" in payload:
        value = payload.get("type")
        if value and value not in VALID_BODY_TYPE:
            return (
                False,
                f"Invalid type '{value}'. Must be one of: {', '.join(VALID_BODY_TYPE)}",
            )

    # Validate ip-version if present
    if "ip-version" in payload:
        value = payload.get("ip-version")
        if value and value not in VALID_BODY_IP_VERSION:
            return (
                False,
                f"Invalid ip-version '{value}'. Must be one of: {', '.join(VALID_BODY_IP_VERSION)}",
            )

    # Validate dstport if present
    if "dstport" in payload:
        value = payload.get("dstport")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 65535:
                    return (False, "dstport must be between 1 and 65535")
            except (ValueError, TypeError):
                return (False, f"dstport must be numeric, got: {value}")

    return (True, None)


# ============================================================================
# DELETE Validation
# ============================================================================


def validate_geneve_delete(name: str | None = None) -> tuple[bool, str | None]:
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
