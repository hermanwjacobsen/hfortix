"""
Validation helpers for system sdwan endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_STATUS = ["disable", "enable"]
VALID_BODY_LOAD_BALANCE_MODE = [
    "source-ip-based",
    "weight-based",
    "usage-based",
    "source-dest-ip-based",
    "measured-volume-based",
]
VALID_BODY_SPEEDTEST_BYPASS_ROUTING = ["disable", "enable"]
VALID_BODY_NEIGHBOR_HOLD_DOWN = ["enable", "disable"]
VALID_BODY_FAIL_DETECT = ["enable", "disable"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_sdwan_get(
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


def validate_sdwan_put(
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

    # Validate load-balance-mode if present
    if "load-balance-mode" in payload:
        value = payload.get("load-balance-mode")
        if value and value not in VALID_BODY_LOAD_BALANCE_MODE:
            return (
                False,
                f"Invalid load-balance-mode '{value}'. Must be one of: {', '.join(VALID_BODY_LOAD_BALANCE_MODE)}",
            )

    # Validate speedtest-bypass-routing if present
    if "speedtest-bypass-routing" in payload:
        value = payload.get("speedtest-bypass-routing")
        if value and value not in VALID_BODY_SPEEDTEST_BYPASS_ROUTING:
            return (
                False,
                f"Invalid speedtest-bypass-routing '{value}'. Must be one of: {', '.join(VALID_BODY_SPEEDTEST_BYPASS_ROUTING)}",
            )

    # Validate duplication-max-num if present
    if "duplication-max-num" in payload:
        value = payload.get("duplication-max-num")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 2 or int_val > 4:
                    return (
                        False,
                        "duplication-max-num must be between 2 and 4",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"duplication-max-num must be numeric, got: {value}",
                )

    # Validate duplication-max-discrepancy if present
    if "duplication-max-discrepancy" in payload:
        value = payload.get("duplication-max-discrepancy")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 250 or int_val > 1000:
                    return (
                        False,
                        "duplication-max-discrepancy must be between 250 and 1000",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"duplication-max-discrepancy must be numeric, got: {value}",
                )

    # Validate neighbor-hold-down if present
    if "neighbor-hold-down" in payload:
        value = payload.get("neighbor-hold-down")
        if value and value not in VALID_BODY_NEIGHBOR_HOLD_DOWN:
            return (
                False,
                f"Invalid neighbor-hold-down '{value}'. Must be one of: {', '.join(VALID_BODY_NEIGHBOR_HOLD_DOWN)}",
            )

    # Validate neighbor-hold-down-time if present
    if "neighbor-hold-down-time" in payload:
        value = payload.get("neighbor-hold-down-time")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 10000000:
                    return (
                        False,
                        "neighbor-hold-down-time must be between 0 and 10000000",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"neighbor-hold-down-time must be numeric, got: {value}",
                )

    # Validate app-perf-log-period if present
    if "app-perf-log-period" in payload:
        value = payload.get("app-perf-log-period")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 3600:
                    return (
                        False,
                        "app-perf-log-period must be between 0 and 3600",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"app-perf-log-period must be numeric, got: {value}",
                )

    # Validate neighbor-hold-boot-time if present
    if "neighbor-hold-boot-time" in payload:
        value = payload.get("neighbor-hold-boot-time")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 10000000:
                    return (
                        False,
                        "neighbor-hold-boot-time must be between 0 and 10000000",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"neighbor-hold-boot-time must be numeric, got: {value}",
                )

    # Validate fail-detect if present
    if "fail-detect" in payload:
        value = payload.get("fail-detect")
        if value and value not in VALID_BODY_FAIL_DETECT:
            return (
                False,
                f"Invalid fail-detect '{value}'. Must be one of: {', '.join(VALID_BODY_FAIL_DETECT)}",
            )

    return (True, None)
