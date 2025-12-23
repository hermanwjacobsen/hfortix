"""
Validation helpers for wireless-controller log endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_STATUS = ["enable", "disable"]
VALID_BODY_ADDRGRP_LOG = [
    "emergency",
    "alert",
    "critical",
    "error",
    "warning",
    "notification",
    "information",
    "debug",
]
VALID_BODY_BLE_LOG = [
    "emergency",
    "alert",
    "critical",
    "error",
    "warning",
    "notification",
    "information",
    "debug",
]
VALID_BODY_CLB_LOG = [
    "emergency",
    "alert",
    "critical",
    "error",
    "warning",
    "notification",
    "information",
    "debug",
]
VALID_BODY_DHCP_STARV_LOG = [
    "emergency",
    "alert",
    "critical",
    "error",
    "warning",
    "notification",
    "information",
    "debug",
]
VALID_BODY_LED_SCHED_LOG = [
    "emergency",
    "alert",
    "critical",
    "error",
    "warning",
    "notification",
    "information",
    "debug",
]
VALID_BODY_RADIO_EVENT_LOG = [
    "emergency",
    "alert",
    "critical",
    "error",
    "warning",
    "notification",
    "information",
    "debug",
]
VALID_BODY_ROGUE_EVENT_LOG = [
    "emergency",
    "alert",
    "critical",
    "error",
    "warning",
    "notification",
    "information",
    "debug",
]
VALID_BODY_STA_EVENT_LOG = [
    "emergency",
    "alert",
    "critical",
    "error",
    "warning",
    "notification",
    "information",
    "debug",
]
VALID_BODY_STA_LOCATE_LOG = [
    "emergency",
    "alert",
    "critical",
    "error",
    "warning",
    "notification",
    "information",
    "debug",
]
VALID_BODY_WIDS_LOG = [
    "emergency",
    "alert",
    "critical",
    "error",
    "warning",
    "notification",
    "information",
    "debug",
]
VALID_BODY_WTP_EVENT_LOG = [
    "emergency",
    "alert",
    "critical",
    "error",
    "warning",
    "notification",
    "information",
    "debug",
]
VALID_BODY_WTP_FIPS_EVENT_LOG = [
    "emergency",
    "alert",
    "critical",
    "error",
    "warning",
    "notification",
    "information",
    "debug",
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_log_get(
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


def validate_log_put(
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

    # Validate addrgrp-log if present
    if "addrgrp-log" in payload:
        value = payload.get("addrgrp-log")
        if value and value not in VALID_BODY_ADDRGRP_LOG:
            return (
                False,
                f"Invalid addrgrp-log '{value}'. Must be one of: {', '.join(VALID_BODY_ADDRGRP_LOG)}",
            )

    # Validate ble-log if present
    if "ble-log" in payload:
        value = payload.get("ble-log")
        if value and value not in VALID_BODY_BLE_LOG:
            return (
                False,
                f"Invalid ble-log '{value}'. Must be one of: {', '.join(VALID_BODY_BLE_LOG)}",
            )

    # Validate clb-log if present
    if "clb-log" in payload:
        value = payload.get("clb-log")
        if value and value not in VALID_BODY_CLB_LOG:
            return (
                False,
                f"Invalid clb-log '{value}'. Must be one of: {', '.join(VALID_BODY_CLB_LOG)}",
            )

    # Validate dhcp-starv-log if present
    if "dhcp-starv-log" in payload:
        value = payload.get("dhcp-starv-log")
        if value and value not in VALID_BODY_DHCP_STARV_LOG:
            return (
                False,
                f"Invalid dhcp-starv-log '{value}'. Must be one of: {', '.join(VALID_BODY_DHCP_STARV_LOG)}",
            )

    # Validate led-sched-log if present
    if "led-sched-log" in payload:
        value = payload.get("led-sched-log")
        if value and value not in VALID_BODY_LED_SCHED_LOG:
            return (
                False,
                f"Invalid led-sched-log '{value}'. Must be one of: {', '.join(VALID_BODY_LED_SCHED_LOG)}",
            )

    # Validate radio-event-log if present
    if "radio-event-log" in payload:
        value = payload.get("radio-event-log")
        if value and value not in VALID_BODY_RADIO_EVENT_LOG:
            return (
                False,
                f"Invalid radio-event-log '{value}'. Must be one of: {', '.join(VALID_BODY_RADIO_EVENT_LOG)}",
            )

    # Validate rogue-event-log if present
    if "rogue-event-log" in payload:
        value = payload.get("rogue-event-log")
        if value and value not in VALID_BODY_ROGUE_EVENT_LOG:
            return (
                False,
                f"Invalid rogue-event-log '{value}'. Must be one of: {', '.join(VALID_BODY_ROGUE_EVENT_LOG)}",
            )

    # Validate sta-event-log if present
    if "sta-event-log" in payload:
        value = payload.get("sta-event-log")
        if value and value not in VALID_BODY_STA_EVENT_LOG:
            return (
                False,
                f"Invalid sta-event-log '{value}'. Must be one of: {', '.join(VALID_BODY_STA_EVENT_LOG)}",
            )

    # Validate sta-locate-log if present
    if "sta-locate-log" in payload:
        value = payload.get("sta-locate-log")
        if value and value not in VALID_BODY_STA_LOCATE_LOG:
            return (
                False,
                f"Invalid sta-locate-log '{value}'. Must be one of: {', '.join(VALID_BODY_STA_LOCATE_LOG)}",
            )

    # Validate wids-log if present
    if "wids-log" in payload:
        value = payload.get("wids-log")
        if value and value not in VALID_BODY_WIDS_LOG:
            return (
                False,
                f"Invalid wids-log '{value}'. Must be one of: {', '.join(VALID_BODY_WIDS_LOG)}",
            )

    # Validate wtp-event-log if present
    if "wtp-event-log" in payload:
        value = payload.get("wtp-event-log")
        if value and value not in VALID_BODY_WTP_EVENT_LOG:
            return (
                False,
                f"Invalid wtp-event-log '{value}'. Must be one of: {', '.join(VALID_BODY_WTP_EVENT_LOG)}",
            )

    # Validate wtp-fips-event-log if present
    if "wtp-fips-event-log" in payload:
        value = payload.get("wtp-fips-event-log")
        if value and value not in VALID_BODY_WTP_FIPS_EVENT_LOG:
            return (
                False,
                f"Invalid wtp-fips-event-log '{value}'. Must be one of: {', '.join(VALID_BODY_WTP_FIPS_EVENT_LOG)}",
            )

    return (True, None)
