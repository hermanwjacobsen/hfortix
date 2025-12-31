"""
Validation helpers for switch-controller system endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_PARALLEL_PROCESS_OVERRIDE = ["disable", "enable"]
VALID_BODY_TUNNEL_MODE = ["compatible", "moderate", "strict"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_system_get(
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


def validate_system_put(
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

    # Validate parallel-process-override if present
    if "parallel-process-override" in payload:
        value = payload.get("parallel-process-override")
        if value and value not in VALID_BODY_PARALLEL_PROCESS_OVERRIDE:
            return (
                False,
                f"Invalid parallel-process-override '{value}'. Must be one of: {', '.join(VALID_BODY_PARALLEL_PROCESS_OVERRIDE)}",
            )

    # Validate parallel-process if present
    if "parallel-process" in payload:
        value = payload.get("parallel-process")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 24:
                    return (
                        False,
                        "parallel-process must be between 1 and 24",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"parallel-process must be numeric, got: {value}",
                )

    # Validate data-sync-interval if present
    if "data-sync-interval" in payload:
        value = payload.get("data-sync-interval")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 30 or int_val > 1800:
                    return (
                        False,
                        "data-sync-interval must be between 30 and 1800",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"data-sync-interval must be numeric, got: {value}",
                )

    # Validate iot-weight-threshold if present
    if "iot-weight-threshold" in payload:
        value = payload.get("iot-weight-threshold")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 255:
                    return (
                        False,
                        "iot-weight-threshold must be between 0 and 255",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"iot-weight-threshold must be numeric, got: {value}",
                )

    # Validate iot-scan-interval if present
    if "iot-scan-interval" in payload:
        value = payload.get("iot-scan-interval")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 2 or int_val > 10080:
                    return (
                        False,
                        "iot-scan-interval must be between 2 and 10080",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"iot-scan-interval must be numeric, got: {value}",
                )

    # Validate iot-holdoff if present
    if "iot-holdof" in payload:
        value = payload.get("iot-holdof")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 10080:
                    return (False, "iot-holdoff must be between 0 and 10080")
            except (ValueError, TypeError):
                return (False, f"iot-holdoff must be numeric, got: {value}")

    # Validate iot-mac-idle if present
    if "iot-mac-idle" in payload:
        value = payload.get("iot-mac-idle")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 10080:
                    return (False, "iot-mac-idle must be between 0 and 10080")
            except (ValueError, TypeError):
                return (False, f"iot-mac-idle must be numeric, got: {value}")

    # Validate nac-periodic-interval if present
    if "nac-periodic-interval" in payload:
        value = payload.get("nac-periodic-interval")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 5 or int_val > 180:
                    return (
                        False,
                        "nac-periodic-interval must be between 5 and 180",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"nac-periodic-interval must be numeric, got: {value}",
                )

    # Validate dynamic-periodic-interval if present
    if "dynamic-periodic-interval" in payload:
        value = payload.get("dynamic-periodic-interval")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 5 or int_val > 180:
                    return (
                        False,
                        "dynamic-periodic-interval must be between 5 and 180",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"dynamic-periodic-interval must be numeric, got: {value}",
                )

    # Validate tunnel-mode if present
    if "tunnel-mode" in payload:
        value = payload.get("tunnel-mode")
        if value and value not in VALID_BODY_TUNNEL_MODE:
            return (
                False,
                f"Invalid tunnel-mode '{value}'. Must be one of: {', '.join(VALID_BODY_TUNNEL_MODE)}",
            )

    # Validate caputp-echo-interval if present
    if "caputp-echo-interval" in payload:
        value = payload.get("caputp-echo-interval")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 8 or int_val > 600:
                    return (
                        False,
                        "caputp-echo-interval must be between 8 and 600",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"caputp-echo-interval must be numeric, got: {value}",
                )

    # Validate caputp-max-retransmit if present
    if "caputp-max-retransmit" in payload:
        value = payload.get("caputp-max-retransmit")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 64:
                    return (
                        False,
                        "caputp-max-retransmit must be between 0 and 64",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"caputp-max-retransmit must be numeric, got: {value}",
                )

    return (True, None)
