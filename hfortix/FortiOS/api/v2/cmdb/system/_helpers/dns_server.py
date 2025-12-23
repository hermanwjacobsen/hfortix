"""
Validation helpers for system dns_server endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_MODE = ["recursive", "non-recursive", "forward-only", "resolver"]
VALID_BODY_DOH = ["enable", "disable"]
VALID_BODY_DOH3 = ["enable", "disable"]
VALID_BODY_DOQ = ["enable", "disable"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_dns_server_get(
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


def validate_dns_server_post(
    payload: dict[str, Any],
) -> tuple[bool, str | None]:
    """
    Validate POST request payload for creating dns_server.

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

    # Validate mode if present
    if "mode" in payload:
        value = payload.get("mode")
        if value and value not in VALID_BODY_MODE:
            return (
                False,
                f"Invalid mode '{value}'. Must be one of: {', '.join(VALID_BODY_MODE)}",
            )

    # Validate dnsfilter-profile if present
    if "dnsfilter-profile" in payload:
        value = payload.get("dnsfilter-profile")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "dnsfilter-profile cannot exceed 47 characters")

    # Validate doh if present
    if "doh" in payload:
        value = payload.get("doh")
        if value and value not in VALID_BODY_DOH:
            return (
                False,
                f"Invalid doh '{value}'. Must be one of: {', '.join(VALID_BODY_DOH)}",
            )

    # Validate doh3 if present
    if "doh3" in payload:
        value = payload.get("doh3")
        if value and value not in VALID_BODY_DOH3:
            return (
                False,
                f"Invalid doh3 '{value}'. Must be one of: {', '.join(VALID_BODY_DOH3)}",
            )

    # Validate doq if present
    if "doq" in payload:
        value = payload.get("doq")
        if value and value not in VALID_BODY_DOQ:
            return (
                False,
                f"Invalid doq '{value}'. Must be one of: {', '.join(VALID_BODY_DOQ)}",
            )

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_dns_server_put(
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

    # Validate mode if present
    if "mode" in payload:
        value = payload.get("mode")
        if value and value not in VALID_BODY_MODE:
            return (
                False,
                f"Invalid mode '{value}'. Must be one of: {', '.join(VALID_BODY_MODE)}",
            )

    # Validate dnsfilter-profile if present
    if "dnsfilter-profile" in payload:
        value = payload.get("dnsfilter-profile")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "dnsfilter-profile cannot exceed 47 characters")

    # Validate doh if present
    if "doh" in payload:
        value = payload.get("doh")
        if value and value not in VALID_BODY_DOH:
            return (
                False,
                f"Invalid doh '{value}'. Must be one of: {', '.join(VALID_BODY_DOH)}",
            )

    # Validate doh3 if present
    if "doh3" in payload:
        value = payload.get("doh3")
        if value and value not in VALID_BODY_DOH3:
            return (
                False,
                f"Invalid doh3 '{value}'. Must be one of: {', '.join(VALID_BODY_DOH3)}",
            )

    # Validate doq if present
    if "doq" in payload:
        value = payload.get("doq")
        if value and value not in VALID_BODY_DOQ:
            return (
                False,
                f"Invalid doq '{value}'. Must be one of: {', '.join(VALID_BODY_DOQ)}",
            )

    return (True, None)


# ============================================================================
# DELETE Validation
# ============================================================================


def validate_dns_server_delete(
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
