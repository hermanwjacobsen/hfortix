"""
Validation helpers for router static endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_STATUS = ["enable", "disable"]
VALID_BODY_BLACKHOLE = ["enable", "disable"]
VALID_BODY_DYNAMIC_GATEWAY = ["enable", "disable"]
VALID_BODY_LINK_MONITOR_EXEMPT = ["enable", "disable"]
VALID_BODY_BFD = ["enable", "disable"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_static_get(
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


def validate_static_post(payload: dict[str, Any]) -> tuple[bool, str | None]:
    """
    Validate POST request payload for creating static.

    Args:
        payload: The payload to validate

    Returns:
        Tuple of (is_valid, error_message)
    """
    # Validate seq-num if present
    if "seq-num" in payload:
        value = payload.get("seq-num")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (False, "seq-num must be between 0 and 4294967295")
            except (ValueError, TypeError):
                return (False, f"seq-num must be numeric, got: {value}")

    # Validate status if present
    if "status" in payload:
        value = payload.get("status")
        if value and value not in VALID_BODY_STATUS:
            return (
                False,
                f"Invalid status '{value}'. Must be one of: {', '.join(VALID_BODY_STATUS)}",
            )

    # Validate distance if present
    if "distance" in payload:
        value = payload.get("distance")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 255:
                    return (False, "distance must be between 1 and 255")
            except (ValueError, TypeError):
                return (False, f"distance must be numeric, got: {value}")

    # Validate weight if present
    if "weight" in payload:
        value = payload.get("weight")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 255:
                    return (False, "weight must be between 0 and 255")
            except (ValueError, TypeError):
                return (False, f"weight must be numeric, got: {value}")

    # Validate priority if present
    if "priority" in payload:
        value = payload.get("priority")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 65535:
                    return (False, "priority must be between 1 and 65535")
            except (ValueError, TypeError):
                return (False, f"priority must be numeric, got: {value}")

    # Validate device if present
    if "device" in payload:
        value = payload.get("device")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "device cannot exceed 35 characters")

    # Validate comment if present
    if "comment" in payload:
        value = payload.get("comment")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "comment cannot exceed 255 characters")

    # Validate blackhole if present
    if "blackhole" in payload:
        value = payload.get("blackhole")
        if value and value not in VALID_BODY_BLACKHOLE:
            return (
                False,
                f"Invalid blackhole '{value}'. Must be one of: {', '.join(VALID_BODY_BLACKHOLE)}",
            )

    # Validate dynamic-gateway if present
    if "dynamic-gateway" in payload:
        value = payload.get("dynamic-gateway")
        if value and value not in VALID_BODY_DYNAMIC_GATEWAY:
            return (
                False,
                f"Invalid dynamic-gateway '{value}'. Must be one of: {', '.join(VALID_BODY_DYNAMIC_GATEWAY)}",
            )

    # Validate dstaddr if present
    if "dstaddr" in payload:
        value = payload.get("dstaddr")
        if value and isinstance(value, str) and len(value) > 79:
            return (False, "dstaddr cannot exceed 79 characters")

    # Validate internet-service if present
    if "internet-service" in payload:
        value = payload.get("internet-service")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "internet-service must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"internet-service must be numeric, got: {value}",
                )

    # Validate internet-service-custom if present
    if "internet-service-custom" in payload:
        value = payload.get("internet-service-custom")
        if value and isinstance(value, str) and len(value) > 64:
            return (
                False,
                "internet-service-custom cannot exceed 64 characters",
            )

    # Validate internet-service-fortiguard if present
    if "internet-service-fortiguard" in payload:
        value = payload.get("internet-service-fortiguard")
        if value and isinstance(value, str) and len(value) > 64:
            return (
                False,
                "internet-service-fortiguard cannot exceed 64 characters",
            )

    # Validate link-monitor-exempt if present
    if "link-monitor-exempt" in payload:
        value = payload.get("link-monitor-exempt")
        if value and value not in VALID_BODY_LINK_MONITOR_EXEMPT:
            return (
                False,
                f"Invalid link-monitor-exempt '{value}'. Must be one of: {', '.join(VALID_BODY_LINK_MONITOR_EXEMPT)}",
            )

    # Validate tag if present
    if "tag" in payload:
        value = payload.get("tag")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (False, "tag must be between 0 and 4294967295")
            except (ValueError, TypeError):
                return (False, f"tag must be numeric, got: {value}")

    # Validate vrf if present
    if "vr" in payload:
        value = payload.get("vr")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 511:
                    return (False, "vrf must be between 0 and 511")
            except (ValueError, TypeError):
                return (False, f"vrf must be numeric, got: {value}")

    # Validate bfd if present
    if "bfd" in payload:
        value = payload.get("bfd")
        if value and value not in VALID_BODY_BFD:
            return (
                False,
                f"Invalid bfd '{value}'. Must be one of: {', '.join(VALID_BODY_BFD)}",
            )

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_static_put(
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

    # Validate seq-num if present
    if "seq-num" in payload:
        value = payload.get("seq-num")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (False, "seq-num must be between 0 and 4294967295")
            except (ValueError, TypeError):
                return (False, f"seq-num must be numeric, got: {value}")

    # Validate status if present
    if "status" in payload:
        value = payload.get("status")
        if value and value not in VALID_BODY_STATUS:
            return (
                False,
                f"Invalid status '{value}'. Must be one of: {', '.join(VALID_BODY_STATUS)}",
            )

    # Validate distance if present
    if "distance" in payload:
        value = payload.get("distance")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 255:
                    return (False, "distance must be between 1 and 255")
            except (ValueError, TypeError):
                return (False, f"distance must be numeric, got: {value}")

    # Validate weight if present
    if "weight" in payload:
        value = payload.get("weight")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 255:
                    return (False, "weight must be between 0 and 255")
            except (ValueError, TypeError):
                return (False, f"weight must be numeric, got: {value}")

    # Validate priority if present
    if "priority" in payload:
        value = payload.get("priority")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 65535:
                    return (False, "priority must be between 1 and 65535")
            except (ValueError, TypeError):
                return (False, f"priority must be numeric, got: {value}")

    # Validate device if present
    if "device" in payload:
        value = payload.get("device")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "device cannot exceed 35 characters")

    # Validate comment if present
    if "comment" in payload:
        value = payload.get("comment")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "comment cannot exceed 255 characters")

    # Validate blackhole if present
    if "blackhole" in payload:
        value = payload.get("blackhole")
        if value and value not in VALID_BODY_BLACKHOLE:
            return (
                False,
                f"Invalid blackhole '{value}'. Must be one of: {', '.join(VALID_BODY_BLACKHOLE)}",
            )

    # Validate dynamic-gateway if present
    if "dynamic-gateway" in payload:
        value = payload.get("dynamic-gateway")
        if value and value not in VALID_BODY_DYNAMIC_GATEWAY:
            return (
                False,
                f"Invalid dynamic-gateway '{value}'. Must be one of: {', '.join(VALID_BODY_DYNAMIC_GATEWAY)}",
            )

    # Validate dstaddr if present
    if "dstaddr" in payload:
        value = payload.get("dstaddr")
        if value and isinstance(value, str) and len(value) > 79:
            return (False, "dstaddr cannot exceed 79 characters")

    # Validate internet-service if present
    if "internet-service" in payload:
        value = payload.get("internet-service")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "internet-service must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"internet-service must be numeric, got: {value}",
                )

    # Validate internet-service-custom if present
    if "internet-service-custom" in payload:
        value = payload.get("internet-service-custom")
        if value and isinstance(value, str) and len(value) > 64:
            return (
                False,
                "internet-service-custom cannot exceed 64 characters",
            )

    # Validate internet-service-fortiguard if present
    if "internet-service-fortiguard" in payload:
        value = payload.get("internet-service-fortiguard")
        if value and isinstance(value, str) and len(value) > 64:
            return (
                False,
                "internet-service-fortiguard cannot exceed 64 characters",
            )

    # Validate link-monitor-exempt if present
    if "link-monitor-exempt" in payload:
        value = payload.get("link-monitor-exempt")
        if value and value not in VALID_BODY_LINK_MONITOR_EXEMPT:
            return (
                False,
                f"Invalid link-monitor-exempt '{value}'. Must be one of: {', '.join(VALID_BODY_LINK_MONITOR_EXEMPT)}",
            )

    # Validate tag if present
    if "tag" in payload:
        value = payload.get("tag")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (False, "tag must be between 0 and 4294967295")
            except (ValueError, TypeError):
                return (False, f"tag must be numeric, got: {value}")

    # Validate vrf if present
    if "vr" in payload:
        value = payload.get("vr")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 511:
                    return (False, "vrf must be between 0 and 511")
            except (ValueError, TypeError):
                return (False, f"vrf must be numeric, got: {value}")

    # Validate bfd if present
    if "bfd" in payload:
        value = payload.get("bfd")
        if value and value not in VALID_BODY_BFD:
            return (
                False,
                f"Invalid bfd '{value}'. Must be one of: {', '.join(VALID_BODY_BFD)}",
            )

    return (True, None)


# ============================================================================
# DELETE Validation
# ============================================================================


def validate_static_delete() -> tuple[bool, str | None]:
    """
    Validate DELETE request parameters.

    Args:

    Returns:
        Tuple of (is_valid, error_message)
    """
    return (True, None)
