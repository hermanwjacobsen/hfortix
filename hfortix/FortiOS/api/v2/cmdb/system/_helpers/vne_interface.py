"""
Validation helpers for system vne_interface endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_AUTO_ASIC_OFFLOAD = ["enable", "disable"]
VALID_BODY_MODE = ["map-e", "fixed-ip", "ds-lite"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_vne_interface_get(
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


def validate_vne_interface_post(
    payload: dict[str, Any],
) -> tuple[bool, str | None]:
    """
    Validate POST request payload for creating vne_interface.

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

    # Validate ssl-certificate if present
    if "ssl-certificate" in payload:
        value = payload.get("ssl-certificate")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "ssl-certificate cannot exceed 35 characters")

    # Validate auto-asic-offload if present
    if "auto-asic-offload" in payload:
        value = payload.get("auto-asic-offload")
        if value and value not in VALID_BODY_AUTO_ASIC_OFFLOAD:
            return (
                False,
                f"Invalid auto-asic-offload '{value}'. Must be one of: {', '.join(VALID_BODY_AUTO_ASIC_OFFLOAD)}",
            )

    # Validate br if present
    if "br" in payload:
        value = payload.get("br")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "br cannot exceed 255 characters")

    # Validate update-url if present
    if "update-url" in payload:
        value = payload.get("update-url")
        if value and isinstance(value, str) and len(value) > 511:
            return (False, "update-url cannot exceed 511 characters")

    # Validate mode if present
    if "mode" in payload:
        value = payload.get("mode")
        if value and value not in VALID_BODY_MODE:
            return (
                False,
                f"Invalid mode '{value}'. Must be one of: {', '.join(VALID_BODY_MODE)}",
            )

    # Validate http-username if present
    if "http-username" in payload:
        value = payload.get("http-username")
        if value and isinstance(value, str) and len(value) > 64:
            return (False, "http-username cannot exceed 64 characters")

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_vne_interface_put(
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

    # Validate ssl-certificate if present
    if "ssl-certificate" in payload:
        value = payload.get("ssl-certificate")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "ssl-certificate cannot exceed 35 characters")

    # Validate auto-asic-offload if present
    if "auto-asic-offload" in payload:
        value = payload.get("auto-asic-offload")
        if value and value not in VALID_BODY_AUTO_ASIC_OFFLOAD:
            return (
                False,
                f"Invalid auto-asic-offload '{value}'. Must be one of: {', '.join(VALID_BODY_AUTO_ASIC_OFFLOAD)}",
            )

    # Validate br if present
    if "br" in payload:
        value = payload.get("br")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "br cannot exceed 255 characters")

    # Validate update-url if present
    if "update-url" in payload:
        value = payload.get("update-url")
        if value and isinstance(value, str) and len(value) > 511:
            return (False, "update-url cannot exceed 511 characters")

    # Validate mode if present
    if "mode" in payload:
        value = payload.get("mode")
        if value and value not in VALID_BODY_MODE:
            return (
                False,
                f"Invalid mode '{value}'. Must be one of: {', '.join(VALID_BODY_MODE)}",
            )

    # Validate http-username if present
    if "http-username" in payload:
        value = payload.get("http-username")
        if value and isinstance(value, str) and len(value) > 64:
            return (False, "http-username cannot exceed 64 characters")

    return (True, None)


# ============================================================================
# DELETE Validation
# ============================================================================


def validate_vne_interface_delete(
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
