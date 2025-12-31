"""
Validation helpers for system ipam endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_STATUS = ["enable", "disable"]
VALID_BODY_SERVER_TYPE = ["fabric-root"]
VALID_BODY_AUTOMATIC_CONFLICT_RESOLUTION = ["disable", "enable"]
VALID_BODY_REQUIRE_SUBNET_SIZE_MATCH = ["disable", "enable"]
VALID_BODY_MANAGE_LAN_ADDRESSES = ["disable", "enable"]
VALID_BODY_MANAGE_LAN_EXTENSION_ADDRESSES = ["disable", "enable"]
VALID_BODY_MANAGE_SSID_ADDRESSES = ["disable", "enable"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_ipam_get(
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


def validate_ipam_put(
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

    # Validate status if present
    if "status" in payload:
        value = payload.get("status")
        if value and value not in VALID_BODY_STATUS:
            return (
                False,
                f"Invalid status '{value}'. Must be one of: {', '.join(VALID_BODY_STATUS)}",
            )

    # Validate server-type if present
    if "server-type" in payload:
        value = payload.get("server-type")
        if value and value not in VALID_BODY_SERVER_TYPE:
            return (
                False,
                f"Invalid server-type '{value}'. Must be one of: {', '.join(VALID_BODY_SERVER_TYPE)}",
            )

    # Validate automatic-conflict-resolution if present
    if "automatic-conflict-resolution" in payload:
        value = payload.get("automatic-conflict-resolution")
        if value and value not in VALID_BODY_AUTOMATIC_CONFLICT_RESOLUTION:
            return (
                False,
                f"Invalid automatic-conflict-resolution '{value}'. Must be one of: {', '.join(VALID_BODY_AUTOMATIC_CONFLICT_RESOLUTION)}",
            )

    # Validate require-subnet-size-match if present
    if "require-subnet-size-match" in payload:
        value = payload.get("require-subnet-size-match")
        if value and value not in VALID_BODY_REQUIRE_SUBNET_SIZE_MATCH:
            return (
                False,
                f"Invalid require-subnet-size-match '{value}'. Must be one of: {', '.join(VALID_BODY_REQUIRE_SUBNET_SIZE_MATCH)}",
            )

    # Validate manage-lan-addresses if present
    if "manage-lan-addresses" in payload:
        value = payload.get("manage-lan-addresses")
        if value and value not in VALID_BODY_MANAGE_LAN_ADDRESSES:
            return (
                False,
                f"Invalid manage-lan-addresses '{value}'. Must be one of: {', '.join(VALID_BODY_MANAGE_LAN_ADDRESSES)}",
            )

    # Validate manage-lan-extension-addresses if present
    if "manage-lan-extension-addresses" in payload:
        value = payload.get("manage-lan-extension-addresses")
        if value and value not in VALID_BODY_MANAGE_LAN_EXTENSION_ADDRESSES:
            return (
                False,
                f"Invalid manage-lan-extension-addresses '{value}'. Must be one of: {', '.join(VALID_BODY_MANAGE_LAN_EXTENSION_ADDRESSES)}",
            )

    # Validate manage-ssid-addresses if present
    if "manage-ssid-addresses" in payload:
        value = payload.get("manage-ssid-addresses")
        if value and value not in VALID_BODY_MANAGE_SSID_ADDRESSES:
            return (
                False,
                f"Invalid manage-ssid-addresses '{value}'. Must be one of: {', '.join(VALID_BODY_MANAGE_SSID_ADDRESSES)}",
            )

    return (True, None)
