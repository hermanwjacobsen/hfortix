"""
Validation helpers for firewall central_snat_map endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_STATUS = ["enable", "disable"]
VALID_BODY_TYPE = ["ipv4", "ipv6"]
VALID_BODY_NAT = ["disable", "enable"]
VALID_BODY_NAT46 = ["enable", "disable"]
VALID_BODY_NAT64 = ["enable", "disable"]
VALID_BODY_PORT_PRESERVE = ["enable", "disable"]
VALID_BODY_PORT_RANDOM = ["enable", "disable"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_central_snat_map_get(
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


def validate_central_snat_map_post(
    payload: dict[str, Any],
) -> tuple[bool, str | None]:
    """
    Validate POST request payload for creating central_snat_map.

    Args:
        payload: The payload to validate

    Returns:
        Tuple of (is_valid, error_message)
    """
    # Validate policyid if present
    if "policyid" in payload:
        value = payload.get("policyid")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "policyid must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (False, f"policyid must be numeric, got: {value}")

    # Validate status if present
    if "status" in payload:
        value = payload.get("status")
        if value and value not in VALID_BODY_STATUS:
            return (
                False,
                f"Invalid status '{value}'. Must be one of: {', '.join(VALID_BODY_STATUS)}",
            )

    # Validate type if present
    if "type" in payload:
        value = payload.get("type")
        if value and value not in VALID_BODY_TYPE:
            return (
                False,
                f"Invalid type '{value}'. Must be one of: {', '.join(VALID_BODY_TYPE)}",
            )

    # Validate protocol if present
    if "protocol" in payload:
        value = payload.get("protocol")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 255:
                    return (False, "protocol must be between 0 and 255")
            except (ValueError, TypeError):
                return (False, f"protocol must be numeric, got: {value}")

    # Validate nat if present
    if "nat" in payload:
        value = payload.get("nat")
        if value and value not in VALID_BODY_NAT:
            return (
                False,
                f"Invalid nat '{value}'. Must be one of: {', '.join(VALID_BODY_NAT)}",
            )

    # Validate nat46 if present
    if "nat46" in payload:
        value = payload.get("nat46")
        if value and value not in VALID_BODY_NAT46:
            return (
                False,
                f"Invalid nat46 '{value}'. Must be one of: {', '.join(VALID_BODY_NAT46)}",
            )

    # Validate nat64 if present
    if "nat64" in payload:
        value = payload.get("nat64")
        if value and value not in VALID_BODY_NAT64:
            return (
                False,
                f"Invalid nat64 '{value}'. Must be one of: {', '.join(VALID_BODY_NAT64)}",
            )

    # Validate port-preserve if present
    if "port-preserve" in payload:
        value = payload.get("port-preserve")
        if value and value not in VALID_BODY_PORT_PRESERVE:
            return (
                False,
                f"Invalid port-preserve '{value}'. Must be one of: {', '.join(VALID_BODY_PORT_PRESERVE)}",
            )

    # Validate port-random if present
    if "port-random" in payload:
        value = payload.get("port-random")
        if value and value not in VALID_BODY_PORT_RANDOM:
            return (
                False,
                f"Invalid port-random '{value}'. Must be one of: {', '.join(VALID_BODY_PORT_RANDOM)}",
            )

    # Validate comments if present
    if "comments" in payload:
        value = payload.get("comments")
        if value and isinstance(value, str) and len(value) > 1023:
            return (False, "comments cannot exceed 1023 characters")

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_central_snat_map_put(
    policyid: str | None = None, payload: dict[str, Any] | None = None
) -> tuple[bool, str | None]:
    """
    Validate PUT request payload for updating {endpoint_name}.

    Args:
        policyid: Object identifier (required)
        payload: The payload to validate

    Returns:
        Tuple of (is_valid, error_message)
    """
    # policyid is required for updates
    if not policyid:
        return (False, "policyid is required for PUT operation")

    # If no payload provided, nothing to validate
    if not payload:
        return (True, None)

    # Validate policyid if present
    if "policyid" in payload:
        value = payload.get("policyid")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "policyid must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (False, f"policyid must be numeric, got: {value}")

    # Validate status if present
    if "status" in payload:
        value = payload.get("status")
        if value and value not in VALID_BODY_STATUS:
            return (
                False,
                f"Invalid status '{value}'. Must be one of: {', '.join(VALID_BODY_STATUS)}",
            )

    # Validate type if present
    if "type" in payload:
        value = payload.get("type")
        if value and value not in VALID_BODY_TYPE:
            return (
                False,
                f"Invalid type '{value}'. Must be one of: {', '.join(VALID_BODY_TYPE)}",
            )

    # Validate protocol if present
    if "protocol" in payload:
        value = payload.get("protocol")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 255:
                    return (False, "protocol must be between 0 and 255")
            except (ValueError, TypeError):
                return (False, f"protocol must be numeric, got: {value}")

    # Validate nat if present
    if "nat" in payload:
        value = payload.get("nat")
        if value and value not in VALID_BODY_NAT:
            return (
                False,
                f"Invalid nat '{value}'. Must be one of: {', '.join(VALID_BODY_NAT)}",
            )

    # Validate nat46 if present
    if "nat46" in payload:
        value = payload.get("nat46")
        if value and value not in VALID_BODY_NAT46:
            return (
                False,
                f"Invalid nat46 '{value}'. Must be one of: {', '.join(VALID_BODY_NAT46)}",
            )

    # Validate nat64 if present
    if "nat64" in payload:
        value = payload.get("nat64")
        if value and value not in VALID_BODY_NAT64:
            return (
                False,
                f"Invalid nat64 '{value}'. Must be one of: {', '.join(VALID_BODY_NAT64)}",
            )

    # Validate port-preserve if present
    if "port-preserve" in payload:
        value = payload.get("port-preserve")
        if value and value not in VALID_BODY_PORT_PRESERVE:
            return (
                False,
                f"Invalid port-preserve '{value}'. Must be one of: {', '.join(VALID_BODY_PORT_PRESERVE)}",
            )

    # Validate port-random if present
    if "port-random" in payload:
        value = payload.get("port-random")
        if value and value not in VALID_BODY_PORT_RANDOM:
            return (
                False,
                f"Invalid port-random '{value}'. Must be one of: {', '.join(VALID_BODY_PORT_RANDOM)}",
            )

    # Validate comments if present
    if "comments" in payload:
        value = payload.get("comments")
        if value and isinstance(value, str) and len(value) > 1023:
            return (False, "comments cannot exceed 1023 characters")

    return (True, None)


# ============================================================================
# DELETE Validation
# ============================================================================


def validate_central_snat_map_delete(
    policyid: str | None = None,
) -> tuple[bool, str | None]:
    """
    Validate DELETE request parameters.

    Args:
        policyid: Object identifier (required)

    Returns:
        Tuple of (is_valid, error_message)
    """
    if not policyid:
        return (False, "policyid is required for DELETE operation")

    return (True, None)
