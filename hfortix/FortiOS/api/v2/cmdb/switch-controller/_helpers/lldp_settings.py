"""
Validation helpers for switch-controller lldp_settings endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_MANAGEMENT_INTERFACE = ["internal", "mgmt"]
VALID_BODY_DEVICE_DETECTION = ["disable", "enable"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_lldp_settings_get(
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


def validate_lldp_settings_put(
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

    # Validate tx-hold if present
    if "tx-hold" in payload:
        value = payload.get("tx-hold")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 16:
                    return (False, "tx-hold must be between 1 and 16")
            except (ValueError, TypeError):
                return (False, f"tx-hold must be numeric, got: {value}")

    # Validate tx-interval if present
    if "tx-interval" in payload:
        value = payload.get("tx-interval")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 5 or int_val > 4095:
                    return (False, "tx-interval must be between 5 and 4095")
            except (ValueError, TypeError):
                return (False, f"tx-interval must be numeric, got: {value}")

    # Validate fast-start-interval if present
    if "fast-start-interval" in payload:
        value = payload.get("fast-start-interval")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 255:
                    return (
                        False,
                        "fast-start-interval must be between 0 and 255",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"fast-start-interval must be numeric, got: {value}",
                )

    # Validate management-interface if present
    if "management-interface" in payload:
        value = payload.get("management-interface")
        if value and value not in VALID_BODY_MANAGEMENT_INTERFACE:
            return (
                False,
                f"Invalid management-interface '{value}'. Must be one of: {', '.join(VALID_BODY_MANAGEMENT_INTERFACE)}",
            )

    # Validate device-detection if present
    if "device-detection" in payload:
        value = payload.get("device-detection")
        if value and value not in VALID_BODY_DEVICE_DETECTION:
            return (
                False,
                f"Invalid device-detection '{value}'. Must be one of: {', '.join(VALID_BODY_DEVICE_DETECTION)}",
            )

    return (True, None)
