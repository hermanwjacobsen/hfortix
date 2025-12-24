"""
Validation helpers for switch-controller qos_qos_policy endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_qos_qos_policy_get(
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


def validate_qos_qos_policy_post(
    payload: dict[str, Any],
) -> tuple[bool, str | None]:
    """
    Validate POST request payload for creating qos_qos_policy.

    Args:
        payload: The payload to validate

    Returns:
        Tuple of (is_valid, error_message)
    """
    # Validate name if present
    if "name" in payload:
        value = payload.get("name")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "name cannot exceed 63 characters")

    # Validate default-cos if present
    if "default-cos" in payload:
        value = payload.get("default-cos")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 7:
                    return (False, "default-cos must be between 0 and 7")
            except (ValueError, TypeError):
                return (False, f"default-cos must be numeric, got: {value}")

    # Validate trust-dot1p-map if present
    if "trust-dot1p-map" in payload:
        value = payload.get("trust-dot1p-map")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "trust-dot1p-map cannot exceed 63 characters")

    # Validate trust-ip-dscp-map if present
    if "trust-ip-dscp-map" in payload:
        value = payload.get("trust-ip-dscp-map")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "trust-ip-dscp-map cannot exceed 63 characters")

    # Validate queue-policy if present
    if "queue-policy" in payload:
        value = payload.get("queue-policy")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "queue-policy cannot exceed 63 characters")

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_qos_qos_policy_put(
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
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "name cannot exceed 63 characters")

    # Validate default-cos if present
    if "default-cos" in payload:
        value = payload.get("default-cos")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 7:
                    return (False, "default-cos must be between 0 and 7")
            except (ValueError, TypeError):
                return (False, f"default-cos must be numeric, got: {value}")

    # Validate trust-dot1p-map if present
    if "trust-dot1p-map" in payload:
        value = payload.get("trust-dot1p-map")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "trust-dot1p-map cannot exceed 63 characters")

    # Validate trust-ip-dscp-map if present
    if "trust-ip-dscp-map" in payload:
        value = payload.get("trust-ip-dscp-map")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "trust-ip-dscp-map cannot exceed 63 characters")

    # Validate queue-policy if present
    if "queue-policy" in payload:
        value = payload.get("queue-policy")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "queue-policy cannot exceed 63 characters")

    return (True, None)


# ============================================================================
# DELETE Validation
# ============================================================================


def validate_qos_qos_policy_delete(
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
