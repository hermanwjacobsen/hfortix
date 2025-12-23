"""
Validation helpers for wireless-controller arrp_profile endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_INCLUDE_WEATHER_CHANNEL = ["enable", "disable"]
VALID_BODY_INCLUDE_DFS_CHANNEL = ["enable", "disable"]
VALID_BODY_OVERRIDE_DARRP_OPTIMIZE = ["enable", "disable"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_arrp_profile_get(
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


def validate_arrp_profile_post(
    payload: dict[str, Any],
) -> tuple[bool, str | None]:
    """
    Validate POST request payload for creating arrp_profile.

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
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "comment cannot exceed 255 characters")

    # Validate selection-period if present
    if "selection-period" in payload:
        value = payload.get("selection-period")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 65535:
                    return (
                        False,
                        "selection-period must be between 0 and 65535",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"selection-period must be numeric, got: {value}",
                )

    # Validate monitor-period if present
    if "monitor-period" in payload:
        value = payload.get("monitor-period")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 65535:
                    return (
                        False,
                        "monitor-period must be between 0 and 65535",
                    )
            except (ValueError, TypeError):
                return (False, f"monitor-period must be numeric, got: {value}")

    # Validate weight-managed-ap if present
    if "weight-managed-ap" in payload:
        value = payload.get("weight-managed-ap")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 2000:
                    return (
                        False,
                        "weight-managed-ap must be between 0 and 2000",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"weight-managed-ap must be numeric, got: {value}",
                )

    # Validate weight-rogue-ap if present
    if "weight-rogue-ap" in payload:
        value = payload.get("weight-rogue-ap")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 2000:
                    return (
                        False,
                        "weight-rogue-ap must be between 0 and 2000",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"weight-rogue-ap must be numeric, got: {value}",
                )

    # Validate weight-noise-floor if present
    if "weight-noise-floor" in payload:
        value = payload.get("weight-noise-floor")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 2000:
                    return (
                        False,
                        "weight-noise-floor must be between 0 and 2000",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"weight-noise-floor must be numeric, got: {value}",
                )

    # Validate weight-channel-load if present
    if "weight-channel-load" in payload:
        value = payload.get("weight-channel-load")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 2000:
                    return (
                        False,
                        "weight-channel-load must be between 0 and 2000",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"weight-channel-load must be numeric, got: {value}",
                )

    # Validate weight-spectral-rssi if present
    if "weight-spectral-rssi" in payload:
        value = payload.get("weight-spectral-rssi")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 2000:
                    return (
                        False,
                        "weight-spectral-rssi must be between 0 and 2000",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"weight-spectral-rssi must be numeric, got: {value}",
                )

    # Validate weight-weather-channel if present
    if "weight-weather-channel" in payload:
        value = payload.get("weight-weather-channel")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 2000:
                    return (
                        False,
                        "weight-weather-channel must be between 0 and 2000",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"weight-weather-channel must be numeric, got: {value}",
                )

    # Validate weight-dfs-channel if present
    if "weight-dfs-channel" in payload:
        value = payload.get("weight-dfs-channel")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 2000:
                    return (
                        False,
                        "weight-dfs-channel must be between 0 and 2000",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"weight-dfs-channel must be numeric, got: {value}",
                )

    # Validate threshold-ap if present
    if "threshold-ap" in payload:
        value = payload.get("threshold-ap")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 500:
                    return (False, "threshold-ap must be between 0 and 500")
            except (ValueError, TypeError):
                return (False, f"threshold-ap must be numeric, got: {value}")

    # Validate threshold-noise-floor if present
    if "threshold-noise-floor" in payload:
        value = payload.get("threshold-noise-floor")
        if value and isinstance(value, str) and len(value) > 7:
            return (False, "threshold-noise-floor cannot exceed 7 characters")

    # Validate threshold-channel-load if present
    if "threshold-channel-load" in payload:
        value = payload.get("threshold-channel-load")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 100:
                    return (
                        False,
                        "threshold-channel-load must be between 0 and 100",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"threshold-channel-load must be numeric, got: {value}",
                )

    # Validate threshold-spectral-rssi if present
    if "threshold-spectral-rssi" in payload:
        value = payload.get("threshold-spectral-rssi")
        if value and isinstance(value, str) and len(value) > 7:
            return (
                False,
                "threshold-spectral-rssi cannot exceed 7 characters",
            )

    # Validate threshold-tx-retries if present
    if "threshold-tx-retries" in payload:
        value = payload.get("threshold-tx-retries")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 1000:
                    return (
                        False,
                        "threshold-tx-retries must be between 0 and 1000",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"threshold-tx-retries must be numeric, got: {value}",
                )

    # Validate threshold-rx-errors if present
    if "threshold-rx-errors" in payload:
        value = payload.get("threshold-rx-errors")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 100:
                    return (
                        False,
                        "threshold-rx-errors must be between 0 and 100",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"threshold-rx-errors must be numeric, got: {value}",
                )

    # Validate include-weather-channel if present
    if "include-weather-channel" in payload:
        value = payload.get("include-weather-channel")
        if value and value not in VALID_BODY_INCLUDE_WEATHER_CHANNEL:
            return (
                False,
                f"Invalid include-weather-channel '{value}'. Must be one of: {', '.join(VALID_BODY_INCLUDE_WEATHER_CHANNEL)}",
            )

    # Validate include-dfs-channel if present
    if "include-dfs-channel" in payload:
        value = payload.get("include-dfs-channel")
        if value and value not in VALID_BODY_INCLUDE_DFS_CHANNEL:
            return (
                False,
                f"Invalid include-dfs-channel '{value}'. Must be one of: {', '.join(VALID_BODY_INCLUDE_DFS_CHANNEL)}",
            )

    # Validate override-darrp-optimize if present
    if "override-darrp-optimize" in payload:
        value = payload.get("override-darrp-optimize")
        if value and value not in VALID_BODY_OVERRIDE_DARRP_OPTIMIZE:
            return (
                False,
                f"Invalid override-darrp-optimize '{value}'. Must be one of: {', '.join(VALID_BODY_OVERRIDE_DARRP_OPTIMIZE)}",
            )

    # Validate darrp-optimize if present
    if "darrp-optimize" in payload:
        value = payload.get("darrp-optimize")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 86400:
                    return (
                        False,
                        "darrp-optimize must be between 0 and 86400",
                    )
            except (ValueError, TypeError):
                return (False, f"darrp-optimize must be numeric, got: {value}")

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_arrp_profile_put(
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
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "comment cannot exceed 255 characters")

    # Validate selection-period if present
    if "selection-period" in payload:
        value = payload.get("selection-period")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 65535:
                    return (
                        False,
                        "selection-period must be between 0 and 65535",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"selection-period must be numeric, got: {value}",
                )

    # Validate monitor-period if present
    if "monitor-period" in payload:
        value = payload.get("monitor-period")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 65535:
                    return (
                        False,
                        "monitor-period must be between 0 and 65535",
                    )
            except (ValueError, TypeError):
                return (False, f"monitor-period must be numeric, got: {value}")

    # Validate weight-managed-ap if present
    if "weight-managed-ap" in payload:
        value = payload.get("weight-managed-ap")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 2000:
                    return (
                        False,
                        "weight-managed-ap must be between 0 and 2000",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"weight-managed-ap must be numeric, got: {value}",
                )

    # Validate weight-rogue-ap if present
    if "weight-rogue-ap" in payload:
        value = payload.get("weight-rogue-ap")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 2000:
                    return (
                        False,
                        "weight-rogue-ap must be between 0 and 2000",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"weight-rogue-ap must be numeric, got: {value}",
                )

    # Validate weight-noise-floor if present
    if "weight-noise-floor" in payload:
        value = payload.get("weight-noise-floor")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 2000:
                    return (
                        False,
                        "weight-noise-floor must be between 0 and 2000",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"weight-noise-floor must be numeric, got: {value}",
                )

    # Validate weight-channel-load if present
    if "weight-channel-load" in payload:
        value = payload.get("weight-channel-load")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 2000:
                    return (
                        False,
                        "weight-channel-load must be between 0 and 2000",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"weight-channel-load must be numeric, got: {value}",
                )

    # Validate weight-spectral-rssi if present
    if "weight-spectral-rssi" in payload:
        value = payload.get("weight-spectral-rssi")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 2000:
                    return (
                        False,
                        "weight-spectral-rssi must be between 0 and 2000",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"weight-spectral-rssi must be numeric, got: {value}",
                )

    # Validate weight-weather-channel if present
    if "weight-weather-channel" in payload:
        value = payload.get("weight-weather-channel")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 2000:
                    return (
                        False,
                        "weight-weather-channel must be between 0 and 2000",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"weight-weather-channel must be numeric, got: {value}",
                )

    # Validate weight-dfs-channel if present
    if "weight-dfs-channel" in payload:
        value = payload.get("weight-dfs-channel")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 2000:
                    return (
                        False,
                        "weight-dfs-channel must be between 0 and 2000",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"weight-dfs-channel must be numeric, got: {value}",
                )

    # Validate threshold-ap if present
    if "threshold-ap" in payload:
        value = payload.get("threshold-ap")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 500:
                    return (False, "threshold-ap must be between 0 and 500")
            except (ValueError, TypeError):
                return (False, f"threshold-ap must be numeric, got: {value}")

    # Validate threshold-noise-floor if present
    if "threshold-noise-floor" in payload:
        value = payload.get("threshold-noise-floor")
        if value and isinstance(value, str) and len(value) > 7:
            return (False, "threshold-noise-floor cannot exceed 7 characters")

    # Validate threshold-channel-load if present
    if "threshold-channel-load" in payload:
        value = payload.get("threshold-channel-load")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 100:
                    return (
                        False,
                        "threshold-channel-load must be between 0 and 100",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"threshold-channel-load must be numeric, got: {value}",
                )

    # Validate threshold-spectral-rssi if present
    if "threshold-spectral-rssi" in payload:
        value = payload.get("threshold-spectral-rssi")
        if value and isinstance(value, str) and len(value) > 7:
            return (
                False,
                "threshold-spectral-rssi cannot exceed 7 characters",
            )

    # Validate threshold-tx-retries if present
    if "threshold-tx-retries" in payload:
        value = payload.get("threshold-tx-retries")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 1000:
                    return (
                        False,
                        "threshold-tx-retries must be between 0 and 1000",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"threshold-tx-retries must be numeric, got: {value}",
                )

    # Validate threshold-rx-errors if present
    if "threshold-rx-errors" in payload:
        value = payload.get("threshold-rx-errors")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 100:
                    return (
                        False,
                        "threshold-rx-errors must be between 0 and 100",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"threshold-rx-errors must be numeric, got: {value}",
                )

    # Validate include-weather-channel if present
    if "include-weather-channel" in payload:
        value = payload.get("include-weather-channel")
        if value and value not in VALID_BODY_INCLUDE_WEATHER_CHANNEL:
            return (
                False,
                f"Invalid include-weather-channel '{value}'. Must be one of: {', '.join(VALID_BODY_INCLUDE_WEATHER_CHANNEL)}",
            )

    # Validate include-dfs-channel if present
    if "include-dfs-channel" in payload:
        value = payload.get("include-dfs-channel")
        if value and value not in VALID_BODY_INCLUDE_DFS_CHANNEL:
            return (
                False,
                f"Invalid include-dfs-channel '{value}'. Must be one of: {', '.join(VALID_BODY_INCLUDE_DFS_CHANNEL)}",
            )

    # Validate override-darrp-optimize if present
    if "override-darrp-optimize" in payload:
        value = payload.get("override-darrp-optimize")
        if value and value not in VALID_BODY_OVERRIDE_DARRP_OPTIMIZE:
            return (
                False,
                f"Invalid override-darrp-optimize '{value}'. Must be one of: {', '.join(VALID_BODY_OVERRIDE_DARRP_OPTIMIZE)}",
            )

    # Validate darrp-optimize if present
    if "darrp-optimize" in payload:
        value = payload.get("darrp-optimize")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 86400:
                    return (
                        False,
                        "darrp-optimize must be between 0 and 86400",
                    )
            except (ValueError, TypeError):
                return (False, f"darrp-optimize must be numeric, got: {value}")

    return (True, None)


# ============================================================================
# DELETE Validation
# ============================================================================


def validate_arrp_profile_delete(
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
