"""
Validation helpers for system central_management endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_MODE = ["normal", "backup"]
VALID_BODY_TYPE = ["fortimanager", "fortiguard", "none"]
VALID_BODY_SCHEDULE_CONFIG_RESTORE = ["enable", "disable"]
VALID_BODY_SCHEDULE_SCRIPT_RESTORE = ["enable", "disable"]
VALID_BODY_ALLOW_PUSH_CONFIGURATION = ["enable", "disable"]
VALID_BODY_ALLOW_PUSH_FIRMWARE = ["enable", "disable"]
VALID_BODY_ALLOW_REMOTE_FIRMWARE_UPGRADE = ["enable", "disable"]
VALID_BODY_ALLOW_MONITOR = ["enable", "disable"]
VALID_BODY_FMG_UPDATE_PORT = ["8890", "443"]
VALID_BODY_FMG_UPDATE_HTTP_HEADER = ["enable", "disable"]
VALID_BODY_INCLUDE_DEFAULT_SERVERS = ["enable", "disable"]
VALID_BODY_ENC_ALGORITHM = ["default", "high", "low"]
VALID_BODY_INTERFACE_SELECT_METHOD = ["auto", "sdwan", "specify"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_central_management_get(
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


def validate_central_management_put(
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

    # Validate mode if present
    if "mode" in payload:
        value = payload.get("mode")
        if value and value not in VALID_BODY_MODE:
            return (
                False,
                f"Invalid mode '{value}'. Must be one of: {', '.join(VALID_BODY_MODE)}",
            )

    # Validate type if present
    if "type" in payload:
        value = payload.get("type")
        if value and value not in VALID_BODY_TYPE:
            return (
                False,
                f"Invalid type '{value}'. Must be one of: {', '.join(VALID_BODY_TYPE)}",
            )

    # Validate fortigate-cloud-sso-default-profile if present
    if "fortigate-cloud-sso-default-profile" in payload:
        value = payload.get("fortigate-cloud-sso-default-profile")
        if value and isinstance(value, str) and len(value) > 35:
            return (
                False,
                "fortigate-cloud-sso-default-profile cannot exceed 35 characters",
            )

    # Validate schedule-config-restore if present
    if "schedule-config-restore" in payload:
        value = payload.get("schedule-config-restore")
        if value and value not in VALID_BODY_SCHEDULE_CONFIG_RESTORE:
            return (
                False,
                f"Invalid schedule-config-restore '{value}'. Must be one of: {', '.join(VALID_BODY_SCHEDULE_CONFIG_RESTORE)}",
            )

    # Validate schedule-script-restore if present
    if "schedule-script-restore" in payload:
        value = payload.get("schedule-script-restore")
        if value and value not in VALID_BODY_SCHEDULE_SCRIPT_RESTORE:
            return (
                False,
                f"Invalid schedule-script-restore '{value}'. Must be one of: {', '.join(VALID_BODY_SCHEDULE_SCRIPT_RESTORE)}",
            )

    # Validate allow-push-configuration if present
    if "allow-push-configuration" in payload:
        value = payload.get("allow-push-configuration")
        if value and value not in VALID_BODY_ALLOW_PUSH_CONFIGURATION:
            return (
                False,
                f"Invalid allow-push-configuration '{value}'. Must be one of: {', '.join(VALID_BODY_ALLOW_PUSH_CONFIGURATION)}",
            )

    # Validate allow-push-firmware if present
    if "allow-push-firmware" in payload:
        value = payload.get("allow-push-firmware")
        if value and value not in VALID_BODY_ALLOW_PUSH_FIRMWARE:
            return (
                False,
                f"Invalid allow-push-firmware '{value}'. Must be one of: {', '.join(VALID_BODY_ALLOW_PUSH_FIRMWARE)}",
            )

    # Validate allow-remote-firmware-upgrade if present
    if "allow-remote-firmware-upgrade" in payload:
        value = payload.get("allow-remote-firmware-upgrade")
        if value and value not in VALID_BODY_ALLOW_REMOTE_FIRMWARE_UPGRADE:
            return (
                False,
                f"Invalid allow-remote-firmware-upgrade '{value}'. Must be one of: {', '.join(VALID_BODY_ALLOW_REMOTE_FIRMWARE_UPGRADE)}",
            )

    # Validate allow-monitor if present
    if "allow-monitor" in payload:
        value = payload.get("allow-monitor")
        if value and value not in VALID_BODY_ALLOW_MONITOR:
            return (
                False,
                f"Invalid allow-monitor '{value}'. Must be one of: {', '.join(VALID_BODY_ALLOW_MONITOR)}",
            )

    # Validate local-cert if present
    if "local-cert" in payload:
        value = payload.get("local-cert")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "local-cert cannot exceed 35 characters")

    # Validate vdom if present
    if "vdom" in payload:
        value = payload.get("vdom")
        if value and isinstance(value, str) and len(value) > 31:
            return (False, "vdom cannot exceed 31 characters")

    # Validate fmg-update-port if present
    if "fmg-update-port" in payload:
        value = payload.get("fmg-update-port")
        if value and value not in VALID_BODY_FMG_UPDATE_PORT:
            return (
                False,
                f"Invalid fmg-update-port '{value}'. Must be one of: {', '.join(VALID_BODY_FMG_UPDATE_PORT)}",
            )

    # Validate fmg-update-http-header if present
    if "fmg-update-http-header" in payload:
        value = payload.get("fmg-update-http-header")
        if value and value not in VALID_BODY_FMG_UPDATE_HTTP_HEADER:
            return (
                False,
                f"Invalid fmg-update-http-header '{value}'. Must be one of: {', '.join(VALID_BODY_FMG_UPDATE_HTTP_HEADER)}",
            )

    # Validate include-default-servers if present
    if "include-default-servers" in payload:
        value = payload.get("include-default-servers")
        if value and value not in VALID_BODY_INCLUDE_DEFAULT_SERVERS:
            return (
                False,
                f"Invalid include-default-servers '{value}'. Must be one of: {', '.join(VALID_BODY_INCLUDE_DEFAULT_SERVERS)}",
            )

    # Validate enc-algorithm if present
    if "enc-algorithm" in payload:
        value = payload.get("enc-algorithm")
        if value and value not in VALID_BODY_ENC_ALGORITHM:
            return (
                False,
                f"Invalid enc-algorithm '{value}'. Must be one of: {', '.join(VALID_BODY_ENC_ALGORITHM)}",
            )

    # Validate interface-select-method if present
    if "interface-select-method" in payload:
        value = payload.get("interface-select-method")
        if value and value not in VALID_BODY_INTERFACE_SELECT_METHOD:
            return (
                False,
                f"Invalid interface-select-method '{value}'. Must be one of: {', '.join(VALID_BODY_INTERFACE_SELECT_METHOD)}",
            )

    # Validate interface if present
    if "interface" in payload:
        value = payload.get("interface")
        if value and isinstance(value, str) and len(value) > 15:
            return (False, "interface cannot exceed 15 characters")

    # Validate vrf-select if present
    if "vrf-select" in payload:
        value = payload.get("vrf-select")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 511:
                    return (False, "vrf-select must be between 0 and 511")
            except (ValueError, TypeError):
                return (False, f"vrf-select must be numeric, got: {value}")

    return (True, None)
