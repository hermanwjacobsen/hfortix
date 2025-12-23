"""
Validation helpers for system auto_install endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_AUTO_INSTALL_CONFIG = ["enable", "disable"]
VALID_BODY_AUTO_INSTALL_IMAGE = ["enable", "disable"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_auto_install_get(
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


def validate_auto_install_put(
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

    # Validate auto-install-config if present
    if "auto-install-config" in payload:
        value = payload.get("auto-install-config")
        if value and value not in VALID_BODY_AUTO_INSTALL_CONFIG:
            return (
                False,
                f"Invalid auto-install-config '{value}'. Must be one of: {', '.join(VALID_BODY_AUTO_INSTALL_CONFIG)}",
            )

    # Validate auto-install-image if present
    if "auto-install-image" in payload:
        value = payload.get("auto-install-image")
        if value and value not in VALID_BODY_AUTO_INSTALL_IMAGE:
            return (
                False,
                f"Invalid auto-install-image '{value}'. Must be one of: {', '.join(VALID_BODY_AUTO_INSTALL_IMAGE)}",
            )

    # Validate default-config-file if present
    if "default-config-file" in payload:
        value = payload.get("default-config-file")
        if value and isinstance(value, str) and len(value) > 127:
            return (False, "default-config-file cannot exceed 127 characters")

    # Validate default-image-file if present
    if "default-image-file" in payload:
        value = payload.get("default-image-file")
        if value and isinstance(value, str) and len(value) > 127:
            return (False, "default-image-file cannot exceed 127 characters")

    return (True, None)
