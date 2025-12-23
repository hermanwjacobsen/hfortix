"""
Validation helpers for switch-controller flow_tracking endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_SAMPLE_MODE = ["local", "perimeter", "device-ingress"]
VALID_BODY_FORMAT = ["netflow1", "netflow5", "netflow9", "ipfix"]
VALID_BODY_LEVEL = ["vlan", "ip", "port", "proto", "mac"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_flow_tracking_get(
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


def validate_flow_tracking_put(
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

    # Validate sample-mode if present
    if "sample-mode" in payload:
        value = payload.get("sample-mode")
        if value and value not in VALID_BODY_SAMPLE_MODE:
            return (
                False,
                f"Invalid sample-mode '{value}'. Must be one of: {', '.join(VALID_BODY_SAMPLE_MODE)}",
            )

    # Validate sample-rate if present
    if "sample-rate" in payload:
        value = payload.get("sample-rate")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 99999:
                    return (False, "sample-rate must be between 0 and 99999")
            except (ValueError, TypeError):
                return (False, f"sample-rate must be numeric, got: {value}")

    # Validate format if present
    if "format" in payload:
        value = payload.get("format")
        if value and value not in VALID_BODY_FORMAT:
            return (
                False,
                f"Invalid format '{value}'. Must be one of: {', '.join(VALID_BODY_FORMAT)}",
            )

    # Validate level if present
    if "level" in payload:
        value = payload.get("level")
        if value and value not in VALID_BODY_LEVEL:
            return (
                False,
                f"Invalid level '{value}'. Must be one of: {', '.join(VALID_BODY_LEVEL)}",
            )

    # Validate max-export-pkt-size if present
    if "max-export-pkt-size" in payload:
        value = payload.get("max-export-pkt-size")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 512 or int_val > 9216:
                    return (
                        False,
                        "max-export-pkt-size must be between 512 and 9216",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"max-export-pkt-size must be numeric, got: {value}",
                )

    # Validate template-export-period if present
    if "template-export-period" in payload:
        value = payload.get("template-export-period")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 60:
                    return (
                        False,
                        "template-export-period must be between 1 and 60",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"template-export-period must be numeric, got: {value}",
                )

    # Validate timeout-general if present
    if "timeout-general" in payload:
        value = payload.get("timeout-general")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 60 or int_val > 604800:
                    return (
                        False,
                        "timeout-general must be between 60 and 604800",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"timeout-general must be numeric, got: {value}",
                )

    # Validate timeout-icmp if present
    if "timeout-icmp" in payload:
        value = payload.get("timeout-icmp")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 60 or int_val > 604800:
                    return (
                        False,
                        "timeout-icmp must be between 60 and 604800",
                    )
            except (ValueError, TypeError):
                return (False, f"timeout-icmp must be numeric, got: {value}")

    # Validate timeout-max if present
    if "timeout-max" in payload:
        value = payload.get("timeout-max")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 60 or int_val > 604800:
                    return (
                        False,
                        "timeout-max must be between 60 and 604800",
                    )
            except (ValueError, TypeError):
                return (False, f"timeout-max must be numeric, got: {value}")

    # Validate timeout-tcp if present
    if "timeout-tcp" in payload:
        value = payload.get("timeout-tcp")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 60 or int_val > 604800:
                    return (
                        False,
                        "timeout-tcp must be between 60 and 604800",
                    )
            except (ValueError, TypeError):
                return (False, f"timeout-tcp must be numeric, got: {value}")

    # Validate timeout-tcp-fin if present
    if "timeout-tcp-fin" in payload:
        value = payload.get("timeout-tcp-fin")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 60 or int_val > 604800:
                    return (
                        False,
                        "timeout-tcp-fin must be between 60 and 604800",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"timeout-tcp-fin must be numeric, got: {value}",
                )

    # Validate timeout-tcp-rst if present
    if "timeout-tcp-rst" in payload:
        value = payload.get("timeout-tcp-rst")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 60 or int_val > 604800:
                    return (
                        False,
                        "timeout-tcp-rst must be between 60 and 604800",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"timeout-tcp-rst must be numeric, got: {value}",
                )

    # Validate timeout-udp if present
    if "timeout-udp" in payload:
        value = payload.get("timeout-udp")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 60 or int_val > 604800:
                    return (
                        False,
                        "timeout-udp must be between 60 and 604800",
                    )
            except (ValueError, TypeError):
                return (False, f"timeout-udp must be numeric, got: {value}")

    return (True, None)
