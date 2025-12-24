"""
Validation helpers for system dhcp6_server endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_STATUS = ["disable", "enable"]
VALID_BODY_RAPID_COMMIT = ["disable", "enable"]
VALID_BODY_DNS_SERVICE = ["delegated", "default", "specify"]
VALID_BODY_DNS_SEARCH_LIST = ["delegated", "specify"]
VALID_BODY_DELEGATED_PREFIX_ROUTE = ["disable", "enable"]
VALID_BODY_IP_MODE = ["range", "delegated"]
VALID_BODY_PREFIX_MODE = ["dhcp6", "ra"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_dhcp6_server_get(
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


def validate_dhcp6_server_post(
    payload: dict[str, Any],
) -> tuple[bool, str | None]:
    """
    Validate POST request payload for creating dhcp6_server.

    Args:
        payload: The payload to validate

    Returns:
        Tuple of (is_valid, error_message)
    """
    # Validate id if present
    if "id" in payload:
        value = payload.get("id")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (False, "id must be between 0 and 4294967295")
            except (ValueError, TypeError):
                return (False, f"id must be numeric, got: {value}")

    # Validate status if present
    if "status" in payload:
        value = payload.get("status")
        if value and value not in VALID_BODY_STATUS:
            return (
                False,
                f"Invalid status '{value}'. Must be one of: {', '.join(VALID_BODY_STATUS)}",
            )

    # Validate rapid-commit if present
    if "rapid-commit" in payload:
        value = payload.get("rapid-commit")
        if value and value not in VALID_BODY_RAPID_COMMIT:
            return (
                False,
                f"Invalid rapid-commit '{value}'. Must be one of: {', '.join(VALID_BODY_RAPID_COMMIT)}",
            )

    # Validate lease-time if present
    if "lease-time" in payload:
        value = payload.get("lease-time")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 300 or int_val > 8640000:
                    return (
                        False,
                        "lease-time must be between 300 and 8640000",
                    )
            except (ValueError, TypeError):
                return (False, f"lease-time must be numeric, got: {value}")

    # Validate dns-service if present
    if "dns-service" in payload:
        value = payload.get("dns-service")
        if value and value not in VALID_BODY_DNS_SERVICE:
            return (
                False,
                f"Invalid dns-service '{value}'. Must be one of: {', '.join(VALID_BODY_DNS_SERVICE)}",
            )

    # Validate dns-search-list if present
    if "dns-search-list" in payload:
        value = payload.get("dns-search-list")
        if value and value not in VALID_BODY_DNS_SEARCH_LIST:
            return (
                False,
                f"Invalid dns-search-list '{value}'. Must be one of: {', '.join(VALID_BODY_DNS_SEARCH_LIST)}",
            )

    # Validate domain if present
    if "domain" in payload:
        value = payload.get("domain")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "domain cannot exceed 35 characters")

    # Validate interface if present
    if "interface" in payload:
        value = payload.get("interface")
        if value and isinstance(value, str) and len(value) > 15:
            return (False, "interface cannot exceed 15 characters")

    # Validate delegated-prefix-route if present
    if "delegated-prefix-route" in payload:
        value = payload.get("delegated-prefix-route")
        if value and value not in VALID_BODY_DELEGATED_PREFIX_ROUTE:
            return (
                False,
                f"Invalid delegated-prefix-route '{value}'. Must be one of: {', '.join(VALID_BODY_DELEGATED_PREFIX_ROUTE)}",
            )

    # Validate upstream-interface if present
    if "upstream-interface" in payload:
        value = payload.get("upstream-interface")
        if value and isinstance(value, str) and len(value) > 15:
            return (False, "upstream-interface cannot exceed 15 characters")

    # Validate delegated-prefix-iaid if present
    if "delegated-prefix-iaid" in payload:
        value = payload.get("delegated-prefix-iaid")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "delegated-prefix-iaid must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"delegated-prefix-iaid must be numeric, got: {value}",
                )

    # Validate ip-mode if present
    if "ip-mode" in payload:
        value = payload.get("ip-mode")
        if value and value not in VALID_BODY_IP_MODE:
            return (
                False,
                f"Invalid ip-mode '{value}'. Must be one of: {', '.join(VALID_BODY_IP_MODE)}",
            )

    # Validate prefix-mode if present
    if "prefix-mode" in payload:
        value = payload.get("prefix-mode")
        if value and value not in VALID_BODY_PREFIX_MODE:
            return (
                False,
                f"Invalid prefix-mode '{value}'. Must be one of: {', '.join(VALID_BODY_PREFIX_MODE)}",
            )

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_dhcp6_server_put(
    id: str | None = None, payload: dict[str, Any] | None = None
) -> tuple[bool, str | None]:
    """
    Validate PUT request payload for updating {endpoint_name}.

    Args:
        id: Object identifier (required)
        payload: The payload to validate

    Returns:
        Tuple of (is_valid, error_message)
    """
    # id is required for updates
    if not id:
        return (False, "id is required for PUT operation")

    # If no payload provided, nothing to validate
    if not payload:
        return (True, None)

    # Validate id if present
    if "id" in payload:
        value = payload.get("id")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (False, "id must be between 0 and 4294967295")
            except (ValueError, TypeError):
                return (False, f"id must be numeric, got: {value}")

    # Validate status if present
    if "status" in payload:
        value = payload.get("status")
        if value and value not in VALID_BODY_STATUS:
            return (
                False,
                f"Invalid status '{value}'. Must be one of: {', '.join(VALID_BODY_STATUS)}",
            )

    # Validate rapid-commit if present
    if "rapid-commit" in payload:
        value = payload.get("rapid-commit")
        if value and value not in VALID_BODY_RAPID_COMMIT:
            return (
                False,
                f"Invalid rapid-commit '{value}'. Must be one of: {', '.join(VALID_BODY_RAPID_COMMIT)}",
            )

    # Validate lease-time if present
    if "lease-time" in payload:
        value = payload.get("lease-time")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 300 or int_val > 8640000:
                    return (
                        False,
                        "lease-time must be between 300 and 8640000",
                    )
            except (ValueError, TypeError):
                return (False, f"lease-time must be numeric, got: {value}")

    # Validate dns-service if present
    if "dns-service" in payload:
        value = payload.get("dns-service")
        if value and value not in VALID_BODY_DNS_SERVICE:
            return (
                False,
                f"Invalid dns-service '{value}'. Must be one of: {', '.join(VALID_BODY_DNS_SERVICE)}",
            )

    # Validate dns-search-list if present
    if "dns-search-list" in payload:
        value = payload.get("dns-search-list")
        if value and value not in VALID_BODY_DNS_SEARCH_LIST:
            return (
                False,
                f"Invalid dns-search-list '{value}'. Must be one of: {', '.join(VALID_BODY_DNS_SEARCH_LIST)}",
            )

    # Validate domain if present
    if "domain" in payload:
        value = payload.get("domain")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "domain cannot exceed 35 characters")

    # Validate interface if present
    if "interface" in payload:
        value = payload.get("interface")
        if value and isinstance(value, str) and len(value) > 15:
            return (False, "interface cannot exceed 15 characters")

    # Validate delegated-prefix-route if present
    if "delegated-prefix-route" in payload:
        value = payload.get("delegated-prefix-route")
        if value and value not in VALID_BODY_DELEGATED_PREFIX_ROUTE:
            return (
                False,
                f"Invalid delegated-prefix-route '{value}'. Must be one of: {', '.join(VALID_BODY_DELEGATED_PREFIX_ROUTE)}",
            )

    # Validate upstream-interface if present
    if "upstream-interface" in payload:
        value = payload.get("upstream-interface")
        if value and isinstance(value, str) and len(value) > 15:
            return (False, "upstream-interface cannot exceed 15 characters")

    # Validate delegated-prefix-iaid if present
    if "delegated-prefix-iaid" in payload:
        value = payload.get("delegated-prefix-iaid")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "delegated-prefix-iaid must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"delegated-prefix-iaid must be numeric, got: {value}",
                )

    # Validate ip-mode if present
    if "ip-mode" in payload:
        value = payload.get("ip-mode")
        if value and value not in VALID_BODY_IP_MODE:
            return (
                False,
                f"Invalid ip-mode '{value}'. Must be one of: {', '.join(VALID_BODY_IP_MODE)}",
            )

    # Validate prefix-mode if present
    if "prefix-mode" in payload:
        value = payload.get("prefix-mode")
        if value and value not in VALID_BODY_PREFIX_MODE:
            return (
                False,
                f"Invalid prefix-mode '{value}'. Must be one of: {', '.join(VALID_BODY_PREFIX_MODE)}",
            )

    return (True, None)


# ============================================================================
# DELETE Validation
# ============================================================================


def validate_dhcp6_server_delete(
    id: str | None = None,
) -> tuple[bool, str | None]:
    """
    Validate DELETE request parameters.

    Args:
        id: Object identifier (required)

    Returns:
        Tuple of (is_valid, error_message)
    """
    if not id:
        return (False, "id is required for DELETE operation")

    return (True, None)
