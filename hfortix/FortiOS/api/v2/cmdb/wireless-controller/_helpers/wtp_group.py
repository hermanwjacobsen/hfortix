"""
Validation helpers for wireless-controller wtp_group endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_PLATFORM_TYPE = [
    "AP-11N",
    "C24JE",
    "421E",
    "423E",
    "221E",
    "222E",
    "223E",
    "224E",
    "231E",
    "321E",
    "431F",
    "431FL",
    "432F",
    "432FR",
    "433F",
    "433FL",
    "231F",
    "231FL",
    "234F",
    "23JF",
    "831F",
    "231G",
    "233G",
    "234G",
    "431G",
    "432G",
    "433G",
    "231K",
    "231KD",
    "23JK",
    "222KL",
    "241K",
    "243K",
    "244K",
    "441K",
    "432K",
    "443K",
    "U421E",
    "U422EV",
    "U423E",
    "U221EV",
    "U223EV",
    "U24JEV",
    "U321EV",
    "U323EV",
    "U431F",
    "U433F",
    "U231F",
    "U234F",
    "U432F",
    "U231G",
    "MVP",
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_wtp_group_get(
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


def validate_wtp_group_post(
    payload: dict[str, Any],
) -> tuple[bool, str | None]:
    """
    Validate POST request payload for creating wtp_group.

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

    # Validate platform-type if present
    if "platform-type" in payload:
        value = payload.get("platform-type")
        if value and value not in VALID_BODY_PLATFORM_TYPE:
            return (
                False,
                f"Invalid platform-type '{value}'. Must be one of: {', '.join(VALID_BODY_PLATFORM_TYPE)}",
            )

    # Validate ble-major-id if present
    if "ble-major-id" in payload:
        value = payload.get("ble-major-id")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 65535:
                    return (False, "ble-major-id must be between 0 and 65535")
            except (ValueError, TypeError):
                return (False, f"ble-major-id must be numeric, got: {value}")

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_wtp_group_put(
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

    # Validate platform-type if present
    if "platform-type" in payload:
        value = payload.get("platform-type")
        if value and value not in VALID_BODY_PLATFORM_TYPE:
            return (
                False,
                f"Invalid platform-type '{value}'. Must be one of: {', '.join(VALID_BODY_PLATFORM_TYPE)}",
            )

    # Validate ble-major-id if present
    if "ble-major-id" in payload:
        value = payload.get("ble-major-id")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 65535:
                    return (False, "ble-major-id must be between 0 and 65535")
            except (ValueError, TypeError):
                return (False, f"ble-major-id must be numeric, got: {value}")

    return (True, None)


# ============================================================================
# DELETE Validation
# ============================================================================


def validate_wtp_group_delete(
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
