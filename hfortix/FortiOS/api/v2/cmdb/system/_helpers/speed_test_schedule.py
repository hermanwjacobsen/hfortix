"""
Validation helpers for system speed_test_schedule endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_STATUS = ["disable", "enable"]
VALID_BODY_MODE = ["UDP", "TCP", "Auto"]
VALID_BODY_DYNAMIC_SERVER = ["disable", "enable"]
VALID_BODY_UPDATE_SHAPER = ["disable", "local", "remote", "both"]
VALID_BODY_UPDATE_INBANDWIDTH = ["disable", "enable"]
VALID_BODY_UPDATE_OUTBANDWIDTH = ["disable", "enable"]
VALID_BODY_UPDATE_INTERFACE_SHAPING = ["disable", "enable"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_speed_test_schedule_get(
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


def validate_speed_test_schedule_post(
    payload: dict[str, Any],
) -> tuple[bool, str | None]:
    """
    Validate POST request payload for creating speed_test_schedule.

    Args:
        payload: The payload to validate

    Returns:
        Tuple of (is_valid, error_message)
    """
    # Validate interface if present
    if "interface" in payload:
        value = payload.get("interface")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "interface cannot exceed 35 characters")

    # Validate status if present
    if "status" in payload:
        value = payload.get("status")
        if value and value not in VALID_BODY_STATUS:
            return (
                False,
                f"Invalid status '{value}'. Must be one of: {', '.join(VALID_BODY_STATUS)}",
            )

    # Validate server-name if present
    if "server-name" in payload:
        value = payload.get("server-name")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "server-name cannot exceed 35 characters")

    # Validate mode if present
    if "mode" in payload:
        value = payload.get("mode")
        if value and value not in VALID_BODY_MODE:
            return (
                False,
                f"Invalid mode '{value}'. Must be one of: {', '.join(VALID_BODY_MODE)}",
            )

    # Validate dynamic-server if present
    if "dynamic-server" in payload:
        value = payload.get("dynamic-server")
        if value and value not in VALID_BODY_DYNAMIC_SERVER:
            return (
                False,
                f"Invalid dynamic-server '{value}'. Must be one of: {', '.join(VALID_BODY_DYNAMIC_SERVER)}",
            )

    # Validate ctrl-port if present
    if "ctrl-port" in payload:
        value = payload.get("ctrl-port")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 65535:
                    return (False, "ctrl-port must be between 1 and 65535")
            except (ValueError, TypeError):
                return (False, f"ctrl-port must be numeric, got: {value}")

    # Validate server-port if present
    if "server-port" in payload:
        value = payload.get("server-port")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 65535:
                    return (False, "server-port must be between 1 and 65535")
            except (ValueError, TypeError):
                return (False, f"server-port must be numeric, got: {value}")

    # Validate update-shaper if present
    if "update-shaper" in payload:
        value = payload.get("update-shaper")
        if value and value not in VALID_BODY_UPDATE_SHAPER:
            return (
                False,
                f"Invalid update-shaper '{value}'. Must be one of: {', '.join(VALID_BODY_UPDATE_SHAPER)}",
            )

    # Validate update-inbandwidth if present
    if "update-inbandwidth" in payload:
        value = payload.get("update-inbandwidth")
        if value and value not in VALID_BODY_UPDATE_INBANDWIDTH:
            return (
                False,
                f"Invalid update-inbandwidth '{value}'. Must be one of: {', '.join(VALID_BODY_UPDATE_INBANDWIDTH)}",
            )

    # Validate update-outbandwidth if present
    if "update-outbandwidth" in payload:
        value = payload.get("update-outbandwidth")
        if value and value not in VALID_BODY_UPDATE_OUTBANDWIDTH:
            return (
                False,
                f"Invalid update-outbandwidth '{value}'. Must be one of: {', '.join(VALID_BODY_UPDATE_OUTBANDWIDTH)}",
            )

    # Validate update-interface-shaping if present
    if "update-interface-shaping" in payload:
        value = payload.get("update-interface-shaping")
        if value and value not in VALID_BODY_UPDATE_INTERFACE_SHAPING:
            return (
                False,
                f"Invalid update-interface-shaping '{value}'. Must be one of: {', '.join(VALID_BODY_UPDATE_INTERFACE_SHAPING)}",
            )

    # Validate update-inbandwidth-maximum if present
    if "update-inbandwidth-maximum" in payload:
        value = payload.get("update-inbandwidth-maximum")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 16776000:
                    return (
                        False,
                        "update-inbandwidth-maximum must be between 0 and 16776000",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"update-inbandwidth-maximum must be numeric, got: {value}",
                )

    # Validate update-inbandwidth-minimum if present
    if "update-inbandwidth-minimum" in payload:
        value = payload.get("update-inbandwidth-minimum")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 16776000:
                    return (
                        False,
                        "update-inbandwidth-minimum must be between 0 and 16776000",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"update-inbandwidth-minimum must be numeric, got: {value}",
                )

    # Validate update-outbandwidth-maximum if present
    if "update-outbandwidth-maximum" in payload:
        value = payload.get("update-outbandwidth-maximum")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 16776000:
                    return (
                        False,
                        "update-outbandwidth-maximum must be between 0 and 16776000",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"update-outbandwidth-maximum must be numeric, got: {value}",
                )

    # Validate update-outbandwidth-minimum if present
    if "update-outbandwidth-minimum" in payload:
        value = payload.get("update-outbandwidth-minimum")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 16776000:
                    return (
                        False,
                        "update-outbandwidth-minimum must be between 0 and 16776000",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"update-outbandwidth-minimum must be numeric, got: {value}",
                )

    # Validate expected-inbandwidth-minimum if present
    if "expected-inbandwidth-minimum" in payload:
        value = payload.get("expected-inbandwidth-minimum")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 16776000:
                    return (
                        False,
                        "expected-inbandwidth-minimum must be between 0 and 16776000",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"expected-inbandwidth-minimum must be numeric, got: {value}",
                )

    # Validate expected-inbandwidth-maximum if present
    if "expected-inbandwidth-maximum" in payload:
        value = payload.get("expected-inbandwidth-maximum")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 16776000:
                    return (
                        False,
                        "expected-inbandwidth-maximum must be between 0 and 16776000",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"expected-inbandwidth-maximum must be numeric, got: {value}",
                )

    # Validate expected-outbandwidth-minimum if present
    if "expected-outbandwidth-minimum" in payload:
        value = payload.get("expected-outbandwidth-minimum")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 16776000:
                    return (
                        False,
                        "expected-outbandwidth-minimum must be between 0 and 16776000",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"expected-outbandwidth-minimum must be numeric, got: {value}",
                )

    # Validate expected-outbandwidth-maximum if present
    if "expected-outbandwidth-maximum" in payload:
        value = payload.get("expected-outbandwidth-maximum")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 16776000:
                    return (
                        False,
                        "expected-outbandwidth-maximum must be between 0 and 16776000",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"expected-outbandwidth-maximum must be numeric, got: {value}",
                )

    # Validate retries if present
    if "retries" in payload:
        value = payload.get("retries")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 10:
                    return (False, "retries must be between 1 and 10")
            except (ValueError, TypeError):
                return (False, f"retries must be numeric, got: {value}")

    # Validate retry-pause if present
    if "retry-pause" in payload:
        value = payload.get("retry-pause")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 60 or int_val > 3600:
                    return (False, "retry-pause must be between 60 and 3600")
            except (ValueError, TypeError):
                return (False, f"retry-pause must be numeric, got: {value}")

    return (True, None)
