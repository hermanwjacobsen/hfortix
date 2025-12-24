"""
Validation helpers for wireless-controller ble_profile endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_ADVERTISING = ["ibeacon", "eddystone-uid", "eddystone-url"]
VALID_BODY_TXPOWER = [
    "0",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "10",
    "11",
    "12",
    "13",
    "14",
    "15",
    "16",
    "17",
]
VALID_BODY_BLE_SCANNING = ["enable", "disable"]
VALID_BODY_SCAN_TYPE = ["active", "passive"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_ble_profile_get(
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


def validate_ble_profile_post(
    payload: dict[str, Any],
) -> tuple[bool, str | None]:
    """
    Validate POST request payload for creating ble_profile.

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

    # Validate comment if present
    if "comment" in payload:
        value = payload.get("comment")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "comment cannot exceed 63 characters")

    # Validate advertising if present
    if "advertising" in payload:
        value = payload.get("advertising")
        if value and value not in VALID_BODY_ADVERTISING:
            return (
                False,
                f"Invalid advertising '{value}'. Must be one of: {', '.join(VALID_BODY_ADVERTISING)}",
            )

    # Validate ibeacon-uuid if present
    if "ibeacon-uuid" in payload:
        value = payload.get("ibeacon-uuid")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "ibeacon-uuid cannot exceed 63 characters")

    # Validate major-id if present
    if "major-id" in payload:
        value = payload.get("major-id")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 65535:
                    return (False, "major-id must be between 0 and 65535")
            except (ValueError, TypeError):
                return (False, f"major-id must be numeric, got: {value}")

    # Validate minor-id if present
    if "minor-id" in payload:
        value = payload.get("minor-id")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 65535:
                    return (False, "minor-id must be between 0 and 65535")
            except (ValueError, TypeError):
                return (False, f"minor-id must be numeric, got: {value}")

    # Validate eddystone-namespace if present
    if "eddystone-namespace" in payload:
        value = payload.get("eddystone-namespace")
        if value and isinstance(value, str) and len(value) > 20:
            return (False, "eddystone-namespace cannot exceed 20 characters")

    # Validate eddystone-instance if present
    if "eddystone-instance" in payload:
        value = payload.get("eddystone-instance")
        if value and isinstance(value, str) and len(value) > 12:
            return (False, "eddystone-instance cannot exceed 12 characters")

    # Validate eddystone-url if present
    if "eddystone-url" in payload:
        value = payload.get("eddystone-url")
        if value and isinstance(value, str) and len(value) > 127:
            return (False, "eddystone-url cannot exceed 127 characters")

    # Validate txpower if present
    if "txpower" in payload:
        value = payload.get("txpower")
        if value and value not in VALID_BODY_TXPOWER:
            return (
                False,
                f"Invalid txpower '{value}'. Must be one of: {', '.join(VALID_BODY_TXPOWER)}",
            )

    # Validate beacon-interval if present
    if "beacon-interval" in payload:
        value = payload.get("beacon-interval")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 40 or int_val > 3500:
                    return (
                        False,
                        "beacon-interval must be between 40 and 3500",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"beacon-interval must be numeric, got: {value}",
                )

    # Validate ble-scanning if present
    if "ble-scanning" in payload:
        value = payload.get("ble-scanning")
        if value and value not in VALID_BODY_BLE_SCANNING:
            return (
                False,
                f"Invalid ble-scanning '{value}'. Must be one of: {', '.join(VALID_BODY_BLE_SCANNING)}",
            )

    # Validate scan-type if present
    if "scan-type" in payload:
        value = payload.get("scan-type")
        if value and value not in VALID_BODY_SCAN_TYPE:
            return (
                False,
                f"Invalid scan-type '{value}'. Must be one of: {', '.join(VALID_BODY_SCAN_TYPE)}",
            )

    # Validate scan-threshold if present
    if "scan-threshold" in payload:
        value = payload.get("scan-threshold")
        if value and isinstance(value, str) and len(value) > 7:
            return (False, "scan-threshold cannot exceed 7 characters")

    # Validate scan-period if present
    if "scan-period" in payload:
        value = payload.get("scan-period")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1000 or int_val > 10000:
                    return (
                        False,
                        "scan-period must be between 1000 and 10000",
                    )
            except (ValueError, TypeError):
                return (False, f"scan-period must be numeric, got: {value}")

    # Validate scan-time if present
    if "scan-time" in payload:
        value = payload.get("scan-time")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1000 or int_val > 10000:
                    return (False, "scan-time must be between 1000 and 10000")
            except (ValueError, TypeError):
                return (False, f"scan-time must be numeric, got: {value}")

    # Validate scan-interval if present
    if "scan-interval" in payload:
        value = payload.get("scan-interval")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 10 or int_val > 1000:
                    return (
                        False,
                        "scan-interval must be between 10 and 1000",
                    )
            except (ValueError, TypeError):
                return (False, f"scan-interval must be numeric, got: {value}")

    # Validate scan-window if present
    if "scan-window" in payload:
        value = payload.get("scan-window")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 10 or int_val > 1000:
                    return (False, "scan-window must be between 10 and 1000")
            except (ValueError, TypeError):
                return (False, f"scan-window must be numeric, got: {value}")

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_ble_profile_put(
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

    # Validate comment if present
    if "comment" in payload:
        value = payload.get("comment")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "comment cannot exceed 63 characters")

    # Validate advertising if present
    if "advertising" in payload:
        value = payload.get("advertising")
        if value and value not in VALID_BODY_ADVERTISING:
            return (
                False,
                f"Invalid advertising '{value}'. Must be one of: {', '.join(VALID_BODY_ADVERTISING)}",
            )

    # Validate ibeacon-uuid if present
    if "ibeacon-uuid" in payload:
        value = payload.get("ibeacon-uuid")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "ibeacon-uuid cannot exceed 63 characters")

    # Validate major-id if present
    if "major-id" in payload:
        value = payload.get("major-id")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 65535:
                    return (False, "major-id must be between 0 and 65535")
            except (ValueError, TypeError):
                return (False, f"major-id must be numeric, got: {value}")

    # Validate minor-id if present
    if "minor-id" in payload:
        value = payload.get("minor-id")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 65535:
                    return (False, "minor-id must be between 0 and 65535")
            except (ValueError, TypeError):
                return (False, f"minor-id must be numeric, got: {value}")

    # Validate eddystone-namespace if present
    if "eddystone-namespace" in payload:
        value = payload.get("eddystone-namespace")
        if value and isinstance(value, str) and len(value) > 20:
            return (False, "eddystone-namespace cannot exceed 20 characters")

    # Validate eddystone-instance if present
    if "eddystone-instance" in payload:
        value = payload.get("eddystone-instance")
        if value and isinstance(value, str) and len(value) > 12:
            return (False, "eddystone-instance cannot exceed 12 characters")

    # Validate eddystone-url if present
    if "eddystone-url" in payload:
        value = payload.get("eddystone-url")
        if value and isinstance(value, str) and len(value) > 127:
            return (False, "eddystone-url cannot exceed 127 characters")

    # Validate txpower if present
    if "txpower" in payload:
        value = payload.get("txpower")
        if value and value not in VALID_BODY_TXPOWER:
            return (
                False,
                f"Invalid txpower '{value}'. Must be one of: {', '.join(VALID_BODY_TXPOWER)}",
            )

    # Validate beacon-interval if present
    if "beacon-interval" in payload:
        value = payload.get("beacon-interval")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 40 or int_val > 3500:
                    return (
                        False,
                        "beacon-interval must be between 40 and 3500",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"beacon-interval must be numeric, got: {value}",
                )

    # Validate ble-scanning if present
    if "ble-scanning" in payload:
        value = payload.get("ble-scanning")
        if value and value not in VALID_BODY_BLE_SCANNING:
            return (
                False,
                f"Invalid ble-scanning '{value}'. Must be one of: {', '.join(VALID_BODY_BLE_SCANNING)}",
            )

    # Validate scan-type if present
    if "scan-type" in payload:
        value = payload.get("scan-type")
        if value and value not in VALID_BODY_SCAN_TYPE:
            return (
                False,
                f"Invalid scan-type '{value}'. Must be one of: {', '.join(VALID_BODY_SCAN_TYPE)}",
            )

    # Validate scan-threshold if present
    if "scan-threshold" in payload:
        value = payload.get("scan-threshold")
        if value and isinstance(value, str) and len(value) > 7:
            return (False, "scan-threshold cannot exceed 7 characters")

    # Validate scan-period if present
    if "scan-period" in payload:
        value = payload.get("scan-period")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1000 or int_val > 10000:
                    return (
                        False,
                        "scan-period must be between 1000 and 10000",
                    )
            except (ValueError, TypeError):
                return (False, f"scan-period must be numeric, got: {value}")

    # Validate scan-time if present
    if "scan-time" in payload:
        value = payload.get("scan-time")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1000 or int_val > 10000:
                    return (False, "scan-time must be between 1000 and 10000")
            except (ValueError, TypeError):
                return (False, f"scan-time must be numeric, got: {value}")

    # Validate scan-interval if present
    if "scan-interval" in payload:
        value = payload.get("scan-interval")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 10 or int_val > 1000:
                    return (
                        False,
                        "scan-interval must be between 10 and 1000",
                    )
            except (ValueError, TypeError):
                return (False, f"scan-interval must be numeric, got: {value}")

    # Validate scan-window if present
    if "scan-window" in payload:
        value = payload.get("scan-window")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 10 or int_val > 1000:
                    return (False, "scan-window must be between 10 and 1000")
            except (ValueError, TypeError):
                return (False, f"scan-window must be numeric, got: {value}")

    return (True, None)


# ============================================================================
# DELETE Validation
# ============================================================================


def validate_ble_profile_delete(
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
