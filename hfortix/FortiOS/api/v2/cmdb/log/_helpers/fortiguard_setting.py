"""
Validation helpers for log fortiguard_setting endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_STATUS = ["enable", "disable"]
VALID_BODY_UPLOAD_OPTION = [
    "store-and-upload",
    "realtime",
    "1-minute",
    "5-minute",
]
VALID_BODY_UPLOAD_INTERVAL = ["daily", "weekly", "monthly"]
VALID_BODY_PRIORITY = ["default", "low"]
VALID_BODY_ACCESS_CONFIG = ["enable", "disable"]
VALID_BODY_ENC_ALGORITHM = ["high-medium", "high", "low"]
VALID_BODY_SSL_MIN_PROTO_VERSION = [
    "default",
    "SSLv3",
    "TLSv1",
    "TLSv1-1",
    "TLSv1-2",
    "TLSv1-3",
]
VALID_BODY_INTERFACE_SELECT_METHOD = ["auto", "sdwan", "specify"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_fortiguard_setting_get(
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


def validate_fortiguard_setting_put(
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

    # Validate upload-option if present
    if "upload-option" in payload:
        value = payload.get("upload-option")
        if value and value not in VALID_BODY_UPLOAD_OPTION:
            return (
                False,
                f"Invalid upload-option '{value}'. Must be one of: {', '.join(VALID_BODY_UPLOAD_OPTION)}",
            )

    # Validate upload-interval if present
    if "upload-interval" in payload:
        value = payload.get("upload-interval")
        if value and value not in VALID_BODY_UPLOAD_INTERVAL:
            return (
                False,
                f"Invalid upload-interval '{value}'. Must be one of: {', '.join(VALID_BODY_UPLOAD_INTERVAL)}",
            )

    # Validate priority if present
    if "priority" in payload:
        value = payload.get("priority")
        if value and value not in VALID_BODY_PRIORITY:
            return (
                False,
                f"Invalid priority '{value}'. Must be one of: {', '.join(VALID_BODY_PRIORITY)}",
            )

    # Validate max-log-rate if present
    if "max-log-rate" in payload:
        value = payload.get("max-log-rate")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 100000:
                    return (
                        False,
                        "max-log-rate must be between 0 and 100000",
                    )
            except (ValueError, TypeError):
                return (False, f"max-log-rate must be numeric, got: {value}")

    # Validate access-config if present
    if "access-config" in payload:
        value = payload.get("access-config")
        if value and value not in VALID_BODY_ACCESS_CONFIG:
            return (
                False,
                f"Invalid access-config '{value}'. Must be one of: {', '.join(VALID_BODY_ACCESS_CONFIG)}",
            )

    # Validate enc-algorithm if present
    if "enc-algorithm" in payload:
        value = payload.get("enc-algorithm")
        if value and value not in VALID_BODY_ENC_ALGORITHM:
            return (
                False,
                f"Invalid enc-algorithm '{value}'. Must be one of: {', '.join(VALID_BODY_ENC_ALGORITHM)}",
            )

    # Validate ssl-min-proto-version if present
    if "ssl-min-proto-version" in payload:
        value = payload.get("ssl-min-proto-version")
        if value and value not in VALID_BODY_SSL_MIN_PROTO_VERSION:
            return (
                False,
                f"Invalid ssl-min-proto-version '{value}'. Must be one of: {', '.join(VALID_BODY_SSL_MIN_PROTO_VERSION)}",
            )

    # Validate conn-timeout if present
    if "conn-timeout" in payload:
        value = payload.get("conn-timeout")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 3600:
                    return (False, "conn-timeout must be between 1 and 3600")
            except (ValueError, TypeError):
                return (False, f"conn-timeout must be numeric, got: {value}")

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
