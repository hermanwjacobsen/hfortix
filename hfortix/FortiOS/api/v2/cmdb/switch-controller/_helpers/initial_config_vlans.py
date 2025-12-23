"""
Validation helpers for switch-controller initial_config_vlans endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_OPTIONAL_VLANS = ["enable", "disable"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_initial_config_vlans_get(
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


def validate_initial_config_vlans_put(
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

    # Validate optional-vlans if present
    if "optional-vlans" in payload:
        value = payload.get("optional-vlans")
        if value and value not in VALID_BODY_OPTIONAL_VLANS:
            return (
                False,
                f"Invalid optional-vlans '{value}'. Must be one of: {', '.join(VALID_BODY_OPTIONAL_VLANS)}",
            )

    # Validate default-vlan if present
    if "default-vlan" in payload:
        value = payload.get("default-vlan")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "default-vlan cannot exceed 63 characters")

    # Validate quarantine if present
    if "quarantine" in payload:
        value = payload.get("quarantine")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "quarantine cannot exceed 63 characters")

    # Validate rspan if present
    if "rspan" in payload:
        value = payload.get("rspan")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "rspan cannot exceed 63 characters")

    # Validate voice if present
    if "voice" in payload:
        value = payload.get("voice")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "voice cannot exceed 63 characters")

    # Validate video if present
    if "video" in payload:
        value = payload.get("video")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "video cannot exceed 63 characters")

    # Validate nac if present
    if "nac" in payload:
        value = payload.get("nac")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "nac cannot exceed 63 characters")

    # Validate nac-segment if present
    if "nac-segment" in payload:
        value = payload.get("nac-segment")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "nac-segment cannot exceed 63 characters")

    return (True, None)
