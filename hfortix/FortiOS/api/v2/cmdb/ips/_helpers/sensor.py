"""
Validation helpers for ips sensor endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_BLOCK_MALICIOUS_URL = ["disable", "enable"]
VALID_BODY_SCAN_BOTNET_CONNECTIONS = ["disable", "block", "monitor"]
VALID_BODY_EXTENDED_LOG = ["enable", "disable"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_sensor_get(
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


def validate_sensor_post(payload: dict[str, Any]) -> tuple[bool, str | None]:
    """
    Validate POST request payload for creating sensor.

    Args:
        payload: The payload to validate

    Returns:
        Tuple of (is_valid, error_message)
    """
    # Validate name if present
    if "name" in payload:
        value = payload.get("name")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "name cannot exceed 47 characters")

    # Validate comment if present
    if "comment" in payload:
        value = payload.get("comment")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "comment cannot exceed 255 characters")

    # Validate replacemsg-group if present
    if "replacemsg-group" in payload:
        value = payload.get("replacemsg-group")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "replacemsg-group cannot exceed 35 characters")

    # Validate block-malicious-url if present
    if "block-malicious-url" in payload:
        value = payload.get("block-malicious-url")
        if value and value not in VALID_BODY_BLOCK_MALICIOUS_URL:
            return (
                False,
                f"Invalid block-malicious-url '{value}'. Must be one of: {', '.join(VALID_BODY_BLOCK_MALICIOUS_URL)}",
            )

    # Validate scan-botnet-connections if present
    if "scan-botnet-connections" in payload:
        value = payload.get("scan-botnet-connections")
        if value and value not in VALID_BODY_SCAN_BOTNET_CONNECTIONS:
            return (
                False,
                f"Invalid scan-botnet-connections '{value}'. Must be one of: {', '.join(VALID_BODY_SCAN_BOTNET_CONNECTIONS)}",
            )

    # Validate extended-log if present
    if "extended-log" in payload:
        value = payload.get("extended-log")
        if value and value not in VALID_BODY_EXTENDED_LOG:
            return (
                False,
                f"Invalid extended-log '{value}'. Must be one of: {', '.join(VALID_BODY_EXTENDED_LOG)}",
            )

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_sensor_put(
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
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "name cannot exceed 47 characters")

    # Validate comment if present
    if "comment" in payload:
        value = payload.get("comment")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "comment cannot exceed 255 characters")

    # Validate replacemsg-group if present
    if "replacemsg-group" in payload:
        value = payload.get("replacemsg-group")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "replacemsg-group cannot exceed 35 characters")

    # Validate block-malicious-url if present
    if "block-malicious-url" in payload:
        value = payload.get("block-malicious-url")
        if value and value not in VALID_BODY_BLOCK_MALICIOUS_URL:
            return (
                False,
                f"Invalid block-malicious-url '{value}'. Must be one of: {', '.join(VALID_BODY_BLOCK_MALICIOUS_URL)}",
            )

    # Validate scan-botnet-connections if present
    if "scan-botnet-connections" in payload:
        value = payload.get("scan-botnet-connections")
        if value and value not in VALID_BODY_SCAN_BOTNET_CONNECTIONS:
            return (
                False,
                f"Invalid scan-botnet-connections '{value}'. Must be one of: {', '.join(VALID_BODY_SCAN_BOTNET_CONNECTIONS)}",
            )

    # Validate extended-log if present
    if "extended-log" in payload:
        value = payload.get("extended-log")
        if value and value not in VALID_BODY_EXTENDED_LOG:
            return (
                False,
                f"Invalid extended-log '{value}'. Must be one of: {', '.join(VALID_BODY_EXTENDED_LOG)}",
            )

    return (True, None)


# ============================================================================
# DELETE Validation
# ============================================================================


def validate_sensor_delete(name: str | None = None) -> tuple[bool, str | None]:
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
