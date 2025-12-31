"""
Validation helpers for wireless-controller hotspot20_anqp_ip_address_type
endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_IPV6_ADDRESS_TYPE = ["not-available", "available", "not-known"]
VALID_BODY_IPV4_ADDRESS_TYPE = [
    "not-available",
    "public",
    "port-restricted",
    "single-NATed-private",
    "double-NATed-private",
    "port-restricted-and-single-NATed",
    "port-restricted-and-double-NATed",
    "not-known",
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_hotspot20_anqp_ip_address_type_get(
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


def validate_hotspot20_anqp_ip_address_type_post(
    payload: dict[str, Any],
) -> tuple[bool, str | None]:
    """
    Validate POST request payload for creating hotspot20_anqp_ip_address_type.

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

    # Validate ipv6-address-type if present
    if "ipv6-address-type" in payload:
        value = payload.get("ipv6-address-type")
        if value and value not in VALID_BODY_IPV6_ADDRESS_TYPE:
            return (
                False,
                f"Invalid ipv6-address-type '{value}'. Must be one of: {', '.join(VALID_BODY_IPV6_ADDRESS_TYPE)}",
            )

    # Validate ipv4-address-type if present
    if "ipv4-address-type" in payload:
        value = payload.get("ipv4-address-type")
        if value and value not in VALID_BODY_IPV4_ADDRESS_TYPE:
            return (
                False,
                f"Invalid ipv4-address-type '{value}'. Must be one of: {', '.join(VALID_BODY_IPV4_ADDRESS_TYPE)}",
            )

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_hotspot20_anqp_ip_address_type_put(
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

    # Validate ipv6-address-type if present
    if "ipv6-address-type" in payload:
        value = payload.get("ipv6-address-type")
        if value and value not in VALID_BODY_IPV6_ADDRESS_TYPE:
            return (
                False,
                f"Invalid ipv6-address-type '{value}'. Must be one of: {', '.join(VALID_BODY_IPV6_ADDRESS_TYPE)}",
            )

    # Validate ipv4-address-type if present
    if "ipv4-address-type" in payload:
        value = payload.get("ipv4-address-type")
        if value and value not in VALID_BODY_IPV4_ADDRESS_TYPE:
            return (
                False,
                f"Invalid ipv4-address-type '{value}'. Must be one of: {', '.join(VALID_BODY_IPV4_ADDRESS_TYPE)}",
            )

    return (True, None)


# ============================================================================
# DELETE Validation
# ============================================================================


def validate_hotspot20_anqp_ip_address_type_delete(
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
