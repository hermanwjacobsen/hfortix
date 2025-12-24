"""
Validation helpers for system sdn_vpn endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_REMOTE_TYPE = ["vgw", "tgw"]
VALID_BODY_ROUTING_TYPE = ["static", "dynamic"]
VALID_BODY_NAT_TRAVERSAL = ["disable", "enable"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_sdn_vpn_get(
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


def validate_sdn_vpn_post(payload: dict[str, Any]) -> tuple[bool, str | None]:
    """
    Validate POST request payload for creating sdn_vpn.

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

    # Validate sdn if present
    if "sdn" in payload:
        value = payload.get("sdn")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "sdn cannot exceed 35 characters")

    # Validate remote-type if present
    if "remote-type" in payload:
        value = payload.get("remote-type")
        if value and value not in VALID_BODY_REMOTE_TYPE:
            return (
                False,
                f"Invalid remote-type '{value}'. Must be one of: {', '.join(VALID_BODY_REMOTE_TYPE)}",
            )

    # Validate routing-type if present
    if "routing-type" in payload:
        value = payload.get("routing-type")
        if value and value not in VALID_BODY_ROUTING_TYPE:
            return (
                False,
                f"Invalid routing-type '{value}'. Must be one of: {', '.join(VALID_BODY_ROUTING_TYPE)}",
            )

    # Validate vgw-id if present
    if "vgw-id" in payload:
        value = payload.get("vgw-id")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "vgw-id cannot exceed 63 characters")

    # Validate tgw-id if present
    if "tgw-id" in payload:
        value = payload.get("tgw-id")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "tgw-id cannot exceed 63 characters")

    # Validate subnet-id if present
    if "subnet-id" in payload:
        value = payload.get("subnet-id")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "subnet-id cannot exceed 63 characters")

    # Validate bgp-as if present
    if "bgp-as" in payload:
        value = payload.get("bgp-as")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 4294967295:
                    return (False, "bgp-as must be between 1 and 4294967295")
            except (ValueError, TypeError):
                return (False, f"bgp-as must be numeric, got: {value}")

    # Validate nat-traversal if present
    if "nat-traversal" in payload:
        value = payload.get("nat-traversal")
        if value and value not in VALID_BODY_NAT_TRAVERSAL:
            return (
                False,
                f"Invalid nat-traversal '{value}'. Must be one of: {', '.join(VALID_BODY_NAT_TRAVERSAL)}",
            )

    # Validate tunnel-interface if present
    if "tunnel-interface" in payload:
        value = payload.get("tunnel-interface")
        if value and isinstance(value, str) and len(value) > 15:
            return (False, "tunnel-interface cannot exceed 15 characters")

    # Validate internal-interface if present
    if "internal-interface" in payload:
        value = payload.get("internal-interface")
        if value and isinstance(value, str) and len(value) > 15:
            return (False, "internal-interface cannot exceed 15 characters")

    # Validate cgw-name if present
    if "cgw-name" in payload:
        value = payload.get("cgw-name")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "cgw-name cannot exceed 35 characters")

    # Validate type if present
    if "type" in payload:
        value = payload.get("type")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 65535:
                    return (False, "type must be between 0 and 65535")
            except (ValueError, TypeError):
                return (False, f"type must be numeric, got: {value}")

    # Validate status if present
    if "status" in payload:
        value = payload.get("status")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 255:
                    return (False, "status must be between 0 and 255")
            except (ValueError, TypeError):
                return (False, f"status must be numeric, got: {value}")

    # Validate code if present
    if "code" in payload:
        value = payload.get("code")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 255:
                    return (False, "code must be between 0 and 255")
            except (ValueError, TypeError):
                return (False, f"code must be numeric, got: {value}")

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_sdn_vpn_put(
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

    # Validate sdn if present
    if "sdn" in payload:
        value = payload.get("sdn")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "sdn cannot exceed 35 characters")

    # Validate remote-type if present
    if "remote-type" in payload:
        value = payload.get("remote-type")
        if value and value not in VALID_BODY_REMOTE_TYPE:
            return (
                False,
                f"Invalid remote-type '{value}'. Must be one of: {', '.join(VALID_BODY_REMOTE_TYPE)}",
            )

    # Validate routing-type if present
    if "routing-type" in payload:
        value = payload.get("routing-type")
        if value and value not in VALID_BODY_ROUTING_TYPE:
            return (
                False,
                f"Invalid routing-type '{value}'. Must be one of: {', '.join(VALID_BODY_ROUTING_TYPE)}",
            )

    # Validate vgw-id if present
    if "vgw-id" in payload:
        value = payload.get("vgw-id")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "vgw-id cannot exceed 63 characters")

    # Validate tgw-id if present
    if "tgw-id" in payload:
        value = payload.get("tgw-id")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "tgw-id cannot exceed 63 characters")

    # Validate subnet-id if present
    if "subnet-id" in payload:
        value = payload.get("subnet-id")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "subnet-id cannot exceed 63 characters")

    # Validate bgp-as if present
    if "bgp-as" in payload:
        value = payload.get("bgp-as")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 4294967295:
                    return (False, "bgp-as must be between 1 and 4294967295")
            except (ValueError, TypeError):
                return (False, f"bgp-as must be numeric, got: {value}")

    # Validate nat-traversal if present
    if "nat-traversal" in payload:
        value = payload.get("nat-traversal")
        if value and value not in VALID_BODY_NAT_TRAVERSAL:
            return (
                False,
                f"Invalid nat-traversal '{value}'. Must be one of: {', '.join(VALID_BODY_NAT_TRAVERSAL)}",
            )

    # Validate tunnel-interface if present
    if "tunnel-interface" in payload:
        value = payload.get("tunnel-interface")
        if value and isinstance(value, str) and len(value) > 15:
            return (False, "tunnel-interface cannot exceed 15 characters")

    # Validate internal-interface if present
    if "internal-interface" in payload:
        value = payload.get("internal-interface")
        if value and isinstance(value, str) and len(value) > 15:
            return (False, "internal-interface cannot exceed 15 characters")

    # Validate cgw-name if present
    if "cgw-name" in payload:
        value = payload.get("cgw-name")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "cgw-name cannot exceed 35 characters")

    # Validate type if present
    if "type" in payload:
        value = payload.get("type")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 65535:
                    return (False, "type must be between 0 and 65535")
            except (ValueError, TypeError):
                return (False, f"type must be numeric, got: {value}")

    # Validate status if present
    if "status" in payload:
        value = payload.get("status")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 255:
                    return (False, "status must be between 0 and 255")
            except (ValueError, TypeError):
                return (False, f"status must be numeric, got: {value}")

    # Validate code if present
    if "code" in payload:
        value = payload.get("code")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 255:
                    return (False, "code must be between 0 and 255")
            except (ValueError, TypeError):
                return (False, f"code must be numeric, got: {value}")

    return (True, None)


# ============================================================================
# DELETE Validation
# ============================================================================


def validate_sdn_vpn_delete(
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
