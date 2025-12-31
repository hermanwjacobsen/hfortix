"""
Validation helpers for firewall on_demand_sniffer endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_NON_IP_PACKET = ["enable", "disable"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_on_demand_sniffer_get(
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


def validate_on_demand_sniffer_post(
    payload: dict[str, Any],
) -> tuple[bool, str | None]:
    """
    Validate POST request payload for creating on_demand_sniffer.

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
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "interface cannot exceed 35 characters")

    # Validate max-packet-count if present
    if "max-packet-count" in payload:
        value = payload.get("max-packet-count")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 4000:
                    return (
                        False,
                        "max-packet-count must be between 1 and 4000",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"max-packet-count must be numeric, got: {value}",
                )

    # Validate non-ip-packet if present
    if "non-ip-packet" in payload:
        value = payload.get("non-ip-packet")
        if value and value not in VALID_BODY_NON_IP_PACKET:
            return (
                False,
                f"Invalid non-ip-packet '{value}'. Must be one of: {', '.join(VALID_BODY_NON_IP_PACKET)}",
            )

    # Validate advanced-filter if present
    if "advanced-filter" in payload:
        value = payload.get("advanced-filter")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "advanced-filter cannot exceed 255 characters")

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_on_demand_sniffer_put(
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
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "interface cannot exceed 35 characters")

    # Validate max-packet-count if present
    if "max-packet-count" in payload:
        value = payload.get("max-packet-count")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 4000:
                    return (
                        False,
                        "max-packet-count must be between 1 and 4000",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"max-packet-count must be numeric, got: {value}",
                )

    # Validate non-ip-packet if present
    if "non-ip-packet" in payload:
        value = payload.get("non-ip-packet")
        if value and value not in VALID_BODY_NON_IP_PACKET:
            return (
                False,
                f"Invalid non-ip-packet '{value}'. Must be one of: {', '.join(VALID_BODY_NON_IP_PACKET)}",
            )

    # Validate advanced-filter if present
    if "advanced-filter" in payload:
        value = payload.get("advanced-filter")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "advanced-filter cannot exceed 255 characters")

    return (True, None)


# ============================================================================
# DELETE Validation
# ============================================================================


def validate_on_demand_sniffer_delete(
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
