"""
Validation helpers for system gre_tunnel endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_IP_VERSION = ["4", "6"]
VALID_BODY_USE_SDWAN = ["disable", "enable"]
VALID_BODY_SEQUENCE_NUMBER_TRANSMISSION = ["disable", "enable"]
VALID_BODY_SEQUENCE_NUMBER_RECEPTION = ["disable", "enable"]
VALID_BODY_CHECKSUM_TRANSMISSION = ["disable", "enable"]
VALID_BODY_CHECKSUM_RECEPTION = ["disable", "enable"]
VALID_BODY_DSCP_COPYING = ["disable", "enable"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_gre_tunnel_get(
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


def validate_gre_tunnel_post(
    payload: dict[str, Any],
) -> tuple[bool, str | None]:
    """
    Validate POST request payload for creating gre_tunnel.

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

    # Validate use-sdwan if present
    if "use-sdwan" in payload:
        value = payload.get("use-sdwan")
        if value and value not in VALID_BODY_USE_SDWAN:
            return (
                False,
                f"Invalid use-sdwan '{value}'. Must be one of: {', '.join(VALID_BODY_USE_SDWAN)}",
            )

    # Validate sequence-number-transmission if present
    if "sequence-number-transmission" in payload:
        value = payload.get("sequence-number-transmission")
        if value and value not in VALID_BODY_SEQUENCE_NUMBER_TRANSMISSION:
            return (
                False,
                f"Invalid sequence-number-transmission '{value}'. Must be one of: {', '.join(VALID_BODY_SEQUENCE_NUMBER_TRANSMISSION)}",
            )

    # Validate sequence-number-reception if present
    if "sequence-number-reception" in payload:
        value = payload.get("sequence-number-reception")
        if value and value not in VALID_BODY_SEQUENCE_NUMBER_RECEPTION:
            return (
                False,
                f"Invalid sequence-number-reception '{value}'. Must be one of: {', '.join(VALID_BODY_SEQUENCE_NUMBER_RECEPTION)}",
            )

    # Validate checksum-transmission if present
    if "checksum-transmission" in payload:
        value = payload.get("checksum-transmission")
        if value and value not in VALID_BODY_CHECKSUM_TRANSMISSION:
            return (
                False,
                f"Invalid checksum-transmission '{value}'. Must be one of: {', '.join(VALID_BODY_CHECKSUM_TRANSMISSION)}",
            )

    # Validate checksum-reception if present
    if "checksum-reception" in payload:
        value = payload.get("checksum-reception")
        if value and value not in VALID_BODY_CHECKSUM_RECEPTION:
            return (
                False,
                f"Invalid checksum-reception '{value}'. Must be one of: {', '.join(VALID_BODY_CHECKSUM_RECEPTION)}",
            )

    # Validate key-outbound if present
    if "key-outbound" in payload:
        value = payload.get("key-outbound")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "key-outbound must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (False, f"key-outbound must be numeric, got: {value}")

    # Validate key-inbound if present
    if "key-inbound" in payload:
        value = payload.get("key-inbound")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "key-inbound must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (False, f"key-inbound must be numeric, got: {value}")

    # Validate dscp-copying if present
    if "dscp-copying" in payload:
        value = payload.get("dscp-copying")
        if value and value not in VALID_BODY_DSCP_COPYING:
            return (
                False,
                f"Invalid dscp-copying '{value}'. Must be one of: {', '.join(VALID_BODY_DSCP_COPYING)}",
            )

    # Validate keepalive-interval if present
    if "keepalive-interval" in payload:
        value = payload.get("keepalive-interval")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 32767:
                    return (
                        False,
                        "keepalive-interval must be between 0 and 32767",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"keepalive-interval must be numeric, got: {value}",
                )

    # Validate keepalive-failtimes if present
    if "keepalive-failtimes" in payload:
        value = payload.get("keepalive-failtimes")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 255:
                    return (
                        False,
                        "keepalive-failtimes must be between 1 and 255",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"keepalive-failtimes must be numeric, got: {value}",
                )

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_gre_tunnel_put(
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

    # Validate use-sdwan if present
    if "use-sdwan" in payload:
        value = payload.get("use-sdwan")
        if value and value not in VALID_BODY_USE_SDWAN:
            return (
                False,
                f"Invalid use-sdwan '{value}'. Must be one of: {', '.join(VALID_BODY_USE_SDWAN)}",
            )

    # Validate sequence-number-transmission if present
    if "sequence-number-transmission" in payload:
        value = payload.get("sequence-number-transmission")
        if value and value not in VALID_BODY_SEQUENCE_NUMBER_TRANSMISSION:
            return (
                False,
                f"Invalid sequence-number-transmission '{value}'. Must be one of: {', '.join(VALID_BODY_SEQUENCE_NUMBER_TRANSMISSION)}",
            )

    # Validate sequence-number-reception if present
    if "sequence-number-reception" in payload:
        value = payload.get("sequence-number-reception")
        if value and value not in VALID_BODY_SEQUENCE_NUMBER_RECEPTION:
            return (
                False,
                f"Invalid sequence-number-reception '{value}'. Must be one of: {', '.join(VALID_BODY_SEQUENCE_NUMBER_RECEPTION)}",
            )

    # Validate checksum-transmission if present
    if "checksum-transmission" in payload:
        value = payload.get("checksum-transmission")
        if value and value not in VALID_BODY_CHECKSUM_TRANSMISSION:
            return (
                False,
                f"Invalid checksum-transmission '{value}'. Must be one of: {', '.join(VALID_BODY_CHECKSUM_TRANSMISSION)}",
            )

    # Validate checksum-reception if present
    if "checksum-reception" in payload:
        value = payload.get("checksum-reception")
        if value and value not in VALID_BODY_CHECKSUM_RECEPTION:
            return (
                False,
                f"Invalid checksum-reception '{value}'. Must be one of: {', '.join(VALID_BODY_CHECKSUM_RECEPTION)}",
            )

    # Validate key-outbound if present
    if "key-outbound" in payload:
        value = payload.get("key-outbound")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "key-outbound must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (False, f"key-outbound must be numeric, got: {value}")

    # Validate key-inbound if present
    if "key-inbound" in payload:
        value = payload.get("key-inbound")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "key-inbound must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (False, f"key-inbound must be numeric, got: {value}")

    # Validate dscp-copying if present
    if "dscp-copying" in payload:
        value = payload.get("dscp-copying")
        if value and value not in VALID_BODY_DSCP_COPYING:
            return (
                False,
                f"Invalid dscp-copying '{value}'. Must be one of: {', '.join(VALID_BODY_DSCP_COPYING)}",
            )

    # Validate keepalive-interval if present
    if "keepalive-interval" in payload:
        value = payload.get("keepalive-interval")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 32767:
                    return (
                        False,
                        "keepalive-interval must be between 0 and 32767",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"keepalive-interval must be numeric, got: {value}",
                )

    # Validate keepalive-failtimes if present
    if "keepalive-failtimes" in payload:
        value = payload.get("keepalive-failtimes")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 255:
                    return (
                        False,
                        "keepalive-failtimes must be between 1 and 255",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"keepalive-failtimes must be numeric, got: {value}",
                )

    return (True, None)


# ============================================================================
# DELETE Validation
# ============================================================================


def validate_gre_tunnel_delete(
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
