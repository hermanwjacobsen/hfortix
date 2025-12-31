"""
Validation helpers for system dns_database endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_STATUS = ["enable", "disable"]
VALID_BODY_TYPE = ["primary", "secondary"]
VALID_BODY_VIEW = ["shadow", "public", "shadow-ztna", "proxy"]
VALID_BODY_AUTHORITATIVE = ["enable", "disable"]
VALID_BODY_INTERFACE_SELECT_METHOD = ["auto", "sdwan", "specify"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_dns_database_get(
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


def validate_dns_database_post(
    payload: dict[str, Any],
) -> tuple[bool, str | None]:
    """
    Validate POST request payload for creating dns_database.

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

    # Validate status if present
    if "status" in payload:
        value = payload.get("status")
        if value and value not in VALID_BODY_STATUS:
            return (
                False,
                f"Invalid status '{value}'. Must be one of: {', '.join(VALID_BODY_STATUS)}",
            )

    # Validate domain if present
    if "domain" in payload:
        value = payload.get("domain")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "domain cannot exceed 255 characters")

    # Validate type if present
    if "type" in payload:
        value = payload.get("type")
        if value and value not in VALID_BODY_TYPE:
            return (
                False,
                f"Invalid type '{value}'. Must be one of: {', '.join(VALID_BODY_TYPE)}",
            )

    # Validate view if present
    if "view" in payload:
        value = payload.get("view")
        if value and value not in VALID_BODY_VIEW:
            return (
                False,
                f"Invalid view '{value}'. Must be one of: {', '.join(VALID_BODY_VIEW)}",
            )

    # Validate primary-name if present
    if "primary-name" in payload:
        value = payload.get("primary-name")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "primary-name cannot exceed 255 characters")

    # Validate contact if present
    if "contact" in payload:
        value = payload.get("contact")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "contact cannot exceed 255 characters")

    # Validate ttl if present
    if "ttl" in payload:
        value = payload.get("ttl")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 2147483647:
                    return (False, "ttl must be between 0 and 2147483647")
            except (ValueError, TypeError):
                return (False, f"ttl must be numeric, got: {value}")

    # Validate authoritative if present
    if "authoritative" in payload:
        value = payload.get("authoritative")
        if value and value not in VALID_BODY_AUTHORITATIVE:
            return (
                False,
                f"Invalid authoritative '{value}'. Must be one of: {', '.join(VALID_BODY_AUTHORITATIVE)}",
            )

    # Validate source-ip-interface if present
    if "source-ip-interface" in payload:
        value = payload.get("source-ip-interface")
        if value and isinstance(value, str) and len(value) > 15:
            return (False, "source-ip-interface cannot exceed 15 characters")

    # Validate rr-max if present
    if "rr-max" in payload:
        value = payload.get("rr-max")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 10 or int_val > 65536:
                    return (False, "rr-max must be between 10 and 65536")
            except (ValueError, TypeError):
                return (False, f"rr-max must be numeric, got: {value}")

    # Validate interface-select-method if present
    if "interface-select-method" in payload:
        value = payload.get("interface-select-method")
        if value and value not in VALID_BODY_INTERFACE_SELECT_METHOD:
            return (
                False,
                f"Invalid interface-select-method '{value}'. Must be one of: {', '.join(VALID_BODY_INTERFACE_SELECT_METHOD)}",
            )

    # Validate interface if present
    if "interface" in payload:
        value = payload.get("interface")
        if value and isinstance(value, str) and len(value) > 15:
            return (False, "interface cannot exceed 15 characters")

    # Validate vrf-select if present
    if "vrf-select" in payload:
        value = payload.get("vrf-select")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 511:
                    return (False, "vrf-select must be between 0 and 511")
            except (ValueError, TypeError):
                return (False, f"vrf-select must be numeric, got: {value}")

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_dns_database_put(
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

    # Validate status if present
    if "status" in payload:
        value = payload.get("status")
        if value and value not in VALID_BODY_STATUS:
            return (
                False,
                f"Invalid status '{value}'. Must be one of: {', '.join(VALID_BODY_STATUS)}",
            )

    # Validate domain if present
    if "domain" in payload:
        value = payload.get("domain")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "domain cannot exceed 255 characters")

    # Validate type if present
    if "type" in payload:
        value = payload.get("type")
        if value and value not in VALID_BODY_TYPE:
            return (
                False,
                f"Invalid type '{value}'. Must be one of: {', '.join(VALID_BODY_TYPE)}",
            )

    # Validate view if present
    if "view" in payload:
        value = payload.get("view")
        if value and value not in VALID_BODY_VIEW:
            return (
                False,
                f"Invalid view '{value}'. Must be one of: {', '.join(VALID_BODY_VIEW)}",
            )

    # Validate primary-name if present
    if "primary-name" in payload:
        value = payload.get("primary-name")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "primary-name cannot exceed 255 characters")

    # Validate contact if present
    if "contact" in payload:
        value = payload.get("contact")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "contact cannot exceed 255 characters")

    # Validate ttl if present
    if "ttl" in payload:
        value = payload.get("ttl")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 2147483647:
                    return (False, "ttl must be between 0 and 2147483647")
            except (ValueError, TypeError):
                return (False, f"ttl must be numeric, got: {value}")

    # Validate authoritative if present
    if "authoritative" in payload:
        value = payload.get("authoritative")
        if value and value not in VALID_BODY_AUTHORITATIVE:
            return (
                False,
                f"Invalid authoritative '{value}'. Must be one of: {', '.join(VALID_BODY_AUTHORITATIVE)}",
            )

    # Validate source-ip-interface if present
    if "source-ip-interface" in payload:
        value = payload.get("source-ip-interface")
        if value and isinstance(value, str) and len(value) > 15:
            return (False, "source-ip-interface cannot exceed 15 characters")

    # Validate rr-max if present
    if "rr-max" in payload:
        value = payload.get("rr-max")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 10 or int_val > 65536:
                    return (False, "rr-max must be between 10 and 65536")
            except (ValueError, TypeError):
                return (False, f"rr-max must be numeric, got: {value}")

    # Validate interface-select-method if present
    if "interface-select-method" in payload:
        value = payload.get("interface-select-method")
        if value and value not in VALID_BODY_INTERFACE_SELECT_METHOD:
            return (
                False,
                f"Invalid interface-select-method '{value}'. Must be one of: {', '.join(VALID_BODY_INTERFACE_SELECT_METHOD)}",
            )

    # Validate interface if present
    if "interface" in payload:
        value = payload.get("interface")
        if value and isinstance(value, str) and len(value) > 15:
            return (False, "interface cannot exceed 15 characters")

    # Validate vrf-select if present
    if "vrf-select" in payload:
        value = payload.get("vrf-select")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 511:
                    return (False, "vrf-select must be between 0 and 511")
            except (ValueError, TypeError):
                return (False, f"vrf-select must be numeric, got: {value}")

    return (True, None)


# ============================================================================
# DELETE Validation
# ============================================================================


def validate_dns_database_delete(
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
