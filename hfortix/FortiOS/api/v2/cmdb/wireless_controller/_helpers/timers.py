"""
Validation helpers for wireless-controller timers endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_timers_get(
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


def validate_timers_put(
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

    # Validate echo-interval if present
    if "echo-interval" in payload:
        value = payload.get("echo-interval")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 255:
                    return (False, "echo-interval must be between 1 and 255")
            except (ValueError, TypeError):
                return (False, f"echo-interval must be numeric, got: {value}")

    # Validate nat-session-keep-alive if present
    if "nat-session-keep-alive" in payload:
        value = payload.get("nat-session-keep-alive")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 255:
                    return (
                        False,
                        "nat-session-keep-alive must be between 0 and 255",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"nat-session-keep-alive must be numeric, got: {value}",
                )

    # Validate discovery-interval if present
    if "discovery-interval" in payload:
        value = payload.get("discovery-interval")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 2 or int_val > 180:
                    return (
                        False,
                        "discovery-interval must be between 2 and 180",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"discovery-interval must be numeric, got: {value}",
                )

    # Validate client-idle-timeout if present
    if "client-idle-timeout" in payload:
        value = payload.get("client-idle-timeout")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 20 or int_val > 3600:
                    return (
                        False,
                        "client-idle-timeout must be between 20 and 3600",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"client-idle-timeout must be numeric, got: {value}",
                )

    # Validate client-idle-rehome-timeout if present
    if "client-idle-rehome-timeout" in payload:
        value = payload.get("client-idle-rehome-timeout")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 2 or int_val > 3600:
                    return (
                        False,
                        "client-idle-rehome-timeout must be between 2 and 3600",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"client-idle-rehome-timeout must be numeric, got: {value}",
                )

    # Validate auth-timeout if present
    if "auth-timeout" in payload:
        value = payload.get("auth-timeout")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 5 or int_val > 30:
                    return (False, "auth-timeout must be between 5 and 30")
            except (ValueError, TypeError):
                return (False, f"auth-timeout must be numeric, got: {value}")

    # Validate rogue-ap-log if present
    if "rogue-ap-log" in payload:
        value = payload.get("rogue-ap-log")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 1440:
                    return (False, "rogue-ap-log must be between 0 and 1440")
            except (ValueError, TypeError):
                return (False, f"rogue-ap-log must be numeric, got: {value}")

    # Validate fake-ap-log if present
    if "fake-ap-log" in payload:
        value = payload.get("fake-ap-log")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 1440:
                    return (False, "fake-ap-log must be between 1 and 1440")
            except (ValueError, TypeError):
                return (False, f"fake-ap-log must be numeric, got: {value}")

    # Validate sta-offline-cleanup if present
    if "sta-offline-cleanup" in payload:
        value = payload.get("sta-offline-cleanup")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "sta-offline-cleanup must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"sta-offline-cleanup must be numeric, got: {value}",
                )

    # Validate sta-offline-ip2mac-cleanup if present
    if "sta-offline-ip2mac-cleanup" in payload:
        value = payload.get("sta-offline-ip2mac-cleanup")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "sta-offline-ip2mac-cleanup must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"sta-offline-ip2mac-cleanup must be numeric, got: {value}",
                )

    # Validate sta-cap-cleanup if present
    if "sta-cap-cleanup" in payload:
        value = payload.get("sta-cap-cleanup")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "sta-cap-cleanup must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"sta-cap-cleanup must be numeric, got: {value}",
                )

    # Validate rogue-ap-cleanup if present
    if "rogue-ap-cleanup" in payload:
        value = payload.get("rogue-ap-cleanup")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "rogue-ap-cleanup must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"rogue-ap-cleanup must be numeric, got: {value}",
                )

    # Validate rogue-sta-cleanup if present
    if "rogue-sta-cleanup" in payload:
        value = payload.get("rogue-sta-cleanup")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "rogue-sta-cleanup must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"rogue-sta-cleanup must be numeric, got: {value}",
                )

    # Validate wids-entry-cleanup if present
    if "wids-entry-cleanup" in payload:
        value = payload.get("wids-entry-cleanup")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "wids-entry-cleanup must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"wids-entry-cleanup must be numeric, got: {value}",
                )

    # Validate ble-device-cleanup if present
    if "ble-device-cleanup" in payload:
        value = payload.get("ble-device-cleanup")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "ble-device-cleanup must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"ble-device-cleanup must be numeric, got: {value}",
                )

    # Validate sta-stats-interval if present
    if "sta-stats-interval" in payload:
        value = payload.get("sta-stats-interval")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 255:
                    return (
                        False,
                        "sta-stats-interval must be between 1 and 255",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"sta-stats-interval must be numeric, got: {value}",
                )

    # Validate vap-stats-interval if present
    if "vap-stats-interval" in payload:
        value = payload.get("vap-stats-interval")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 255:
                    return (
                        False,
                        "vap-stats-interval must be between 1 and 255",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"vap-stats-interval must be numeric, got: {value}",
                )

    # Validate radio-stats-interval if present
    if "radio-stats-interval" in payload:
        value = payload.get("radio-stats-interval")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 255:
                    return (
                        False,
                        "radio-stats-interval must be between 1 and 255",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"radio-stats-interval must be numeric, got: {value}",
                )

    # Validate sta-capability-interval if present
    if "sta-capability-interval" in payload:
        value = payload.get("sta-capability-interval")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 255:
                    return (
                        False,
                        "sta-capability-interval must be between 1 and 255",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"sta-capability-interval must be numeric, got: {value}",
                )

    # Validate sta-locate-timer if present
    if "sta-locate-timer" in payload:
        value = payload.get("sta-locate-timer")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 86400:
                    return (
                        False,
                        "sta-locate-timer must be between 0 and 86400",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"sta-locate-timer must be numeric, got: {value}",
                )

    # Validate ipsec-intf-cleanup if present
    if "ipsec-intf-cleanup" in payload:
        value = payload.get("ipsec-intf-cleanup")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 30 or int_val > 3600:
                    return (
                        False,
                        "ipsec-intf-cleanup must be between 30 and 3600",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"ipsec-intf-cleanup must be numeric, got: {value}",
                )

    # Validate ble-scan-report-intv if present
    if "ble-scan-report-intv" in payload:
        value = payload.get("ble-scan-report-intv")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 10 or int_val > 3600:
                    return (
                        False,
                        "ble-scan-report-intv must be between 10 and 3600",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"ble-scan-report-intv must be numeric, got: {value}",
                )

    # Validate drma-interval if present
    if "drma-interval" in payload:
        value = payload.get("drma-interval")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 1440:
                    return (False, "drma-interval must be between 1 and 1440")
            except (ValueError, TypeError):
                return (False, f"drma-interval must be numeric, got: {value}")

    # Validate ap-reboot-wait-interval1 if present
    if "ap-reboot-wait-interval1" in payload:
        value = payload.get("ap-reboot-wait-interval1")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 5 or int_val > 65535:
                    return (
                        False,
                        "ap-reboot-wait-interval1 must be between 5 and 65535",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"ap-reboot-wait-interval1 must be numeric, got: {value}",
                )

    # Validate ap-reboot-wait-time if present
    if "ap-reboot-wait-time" in payload:
        value = payload.get("ap-reboot-wait-time")
        if value and isinstance(value, str) and len(value) > 7:
            return (False, "ap-reboot-wait-time cannot exceed 7 characters")

    # Validate ap-reboot-wait-interval2 if present
    if "ap-reboot-wait-interval2" in payload:
        value = payload.get("ap-reboot-wait-interval2")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 5 or int_val > 65535:
                    return (
                        False,
                        "ap-reboot-wait-interval2 must be between 5 and 65535",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"ap-reboot-wait-interval2 must be numeric, got: {value}",
                )

    return (True, None)
