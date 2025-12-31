"""
Validation helpers for firewall shaping_policy endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_STATUS = ["enable", "disable"]
VALID_BODY_IP_VERSION = ["4", "6"]
VALID_BODY_TRAFFIC_TYPE = ["forwarding", "local-in", "local-out"]
VALID_BODY_INTERNET_SERVICE = ["enable", "disable"]
VALID_BODY_INTERNET_SERVICE_SRC = ["enable", "disable"]
VALID_BODY_TOS_NEGATE = ["enable", "disable"]
VALID_BODY_DIFFSERV_FORWARD = ["enable", "disable"]
VALID_BODY_DIFFSERV_REVERSE = ["enable", "disable"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_shaping_policy_get(
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


def validate_shaping_policy_post(
    payload: dict[str, Any],
) -> tuple[bool, str | None]:
    """
    Validate POST request payload for creating shaping_policy.

    Args:
        payload: The payload to validate

    Returns:
        Tuple of (is_valid, error_message)
    """
    # Validate id if present
    if "id" in payload:
        value = payload.get("id")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (False, "id must be between 0 and 4294967295")
            except (ValueError, TypeError):
                return (False, f"id must be numeric, got: {value}")

    # Validate name if present
    if "name" in payload:
        value = payload.get("name")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "name cannot exceed 35 characters")

    # Validate comment if present
    if "comment" in payload:
        value = payload.get("comment")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "comment cannot exceed 255 characters")

    # Validate status if present
    if "status" in payload:
        value = payload.get("status")
        if value and value not in VALID_BODY_STATUS:
            return (
                False,
                f"Invalid status '{value}'. Must be one of: {', '.join(VALID_BODY_STATUS)}",
            )

    # Validate ip-version if present
    if "ip-version" in payload:
        value = payload.get("ip-version")
        if value and value not in VALID_BODY_IP_VERSION:
            return (
                False,
                f"Invalid ip-version '{value}'. Must be one of: {', '.join(VALID_BODY_IP_VERSION)}",
            )

    # Validate traffic-type if present
    if "traffic-type" in payload:
        value = payload.get("traffic-type")
        if value and value not in VALID_BODY_TRAFFIC_TYPE:
            return (
                False,
                f"Invalid traffic-type '{value}'. Must be one of: {', '.join(VALID_BODY_TRAFFIC_TYPE)}",
            )

    # Validate internet-service if present
    if "internet-service" in payload:
        value = payload.get("internet-service")
        if value and value not in VALID_BODY_INTERNET_SERVICE:
            return (
                False,
                f"Invalid internet-service '{value}'. Must be one of: {', '.join(VALID_BODY_INTERNET_SERVICE)}",
            )

    # Validate internet-service-src if present
    if "internet-service-src" in payload:
        value = payload.get("internet-service-src")
        if value and value not in VALID_BODY_INTERNET_SERVICE_SRC:
            return (
                False,
                f"Invalid internet-service-src '{value}'. Must be one of: {', '.join(VALID_BODY_INTERNET_SERVICE_SRC)}",
            )

    # Validate schedule if present
    if "schedule" in payload:
        value = payload.get("schedule")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "schedule cannot exceed 35 characters")

    # Validate tos-negate if present
    if "tos-negate" in payload:
        value = payload.get("tos-negate")
        if value and value not in VALID_BODY_TOS_NEGATE:
            return (
                False,
                f"Invalid tos-negate '{value}'. Must be one of: {', '.join(VALID_BODY_TOS_NEGATE)}",
            )

    # Validate traffic-shaper if present
    if "traffic-shaper" in payload:
        value = payload.get("traffic-shaper")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "traffic-shaper cannot exceed 35 characters")

    # Validate traffic-shaper-reverse if present
    if "traffic-shaper-reverse" in payload:
        value = payload.get("traffic-shaper-reverse")
        if value and isinstance(value, str) and len(value) > 35:
            return (
                False,
                "traffic-shaper-reverse cannot exceed 35 characters",
            )

    # Validate per-ip-shaper if present
    if "per-ip-shaper" in payload:
        value = payload.get("per-ip-shaper")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "per-ip-shaper cannot exceed 35 characters")

    # Validate class-id if present
    if "class-id" in payload:
        value = payload.get("class-id")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "class-id must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (False, f"class-id must be numeric, got: {value}")

    # Validate diffserv-forward if present
    if "diffserv-forward" in payload:
        value = payload.get("diffserv-forward")
        if value and value not in VALID_BODY_DIFFSERV_FORWARD:
            return (
                False,
                f"Invalid diffserv-forward '{value}'. Must be one of: {', '.join(VALID_BODY_DIFFSERV_FORWARD)}",
            )

    # Validate diffserv-reverse if present
    if "diffserv-reverse" in payload:
        value = payload.get("diffserv-reverse")
        if value and value not in VALID_BODY_DIFFSERV_REVERSE:
            return (
                False,
                f"Invalid diffserv-reverse '{value}'. Must be one of: {', '.join(VALID_BODY_DIFFSERV_REVERSE)}",
            )

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_shaping_policy_put(
    id: str | None = None, payload: dict[str, Any] | None = None
) -> tuple[bool, str | None]:
    """
    Validate PUT request payload for updating {endpoint_name}.

    Args:
        id: Object identifier (required)
        payload: The payload to validate

    Returns:
        Tuple of (is_valid, error_message)
    """
    # id is required for updates
    if not id:
        return (False, "id is required for PUT operation")

    # If no payload provided, nothing to validate
    if not payload:
        return (True, None)

    # Validate id if present
    if "id" in payload:
        value = payload.get("id")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (False, "id must be between 0 and 4294967295")
            except (ValueError, TypeError):
                return (False, f"id must be numeric, got: {value}")

    # Validate name if present
    if "name" in payload:
        value = payload.get("name")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "name cannot exceed 35 characters")

    # Validate comment if present
    if "comment" in payload:
        value = payload.get("comment")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "comment cannot exceed 255 characters")

    # Validate status if present
    if "status" in payload:
        value = payload.get("status")
        if value and value not in VALID_BODY_STATUS:
            return (
                False,
                f"Invalid status '{value}'. Must be one of: {', '.join(VALID_BODY_STATUS)}",
            )

    # Validate ip-version if present
    if "ip-version" in payload:
        value = payload.get("ip-version")
        if value and value not in VALID_BODY_IP_VERSION:
            return (
                False,
                f"Invalid ip-version '{value}'. Must be one of: {', '.join(VALID_BODY_IP_VERSION)}",
            )

    # Validate traffic-type if present
    if "traffic-type" in payload:
        value = payload.get("traffic-type")
        if value and value not in VALID_BODY_TRAFFIC_TYPE:
            return (
                False,
                f"Invalid traffic-type '{value}'. Must be one of: {', '.join(VALID_BODY_TRAFFIC_TYPE)}",
            )

    # Validate internet-service if present
    if "internet-service" in payload:
        value = payload.get("internet-service")
        if value and value not in VALID_BODY_INTERNET_SERVICE:
            return (
                False,
                f"Invalid internet-service '{value}'. Must be one of: {', '.join(VALID_BODY_INTERNET_SERVICE)}",
            )

    # Validate internet-service-src if present
    if "internet-service-src" in payload:
        value = payload.get("internet-service-src")
        if value and value not in VALID_BODY_INTERNET_SERVICE_SRC:
            return (
                False,
                f"Invalid internet-service-src '{value}'. Must be one of: {', '.join(VALID_BODY_INTERNET_SERVICE_SRC)}",
            )

    # Validate schedule if present
    if "schedule" in payload:
        value = payload.get("schedule")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "schedule cannot exceed 35 characters")

    # Validate tos-negate if present
    if "tos-negate" in payload:
        value = payload.get("tos-negate")
        if value and value not in VALID_BODY_TOS_NEGATE:
            return (
                False,
                f"Invalid tos-negate '{value}'. Must be one of: {', '.join(VALID_BODY_TOS_NEGATE)}",
            )

    # Validate traffic-shaper if present
    if "traffic-shaper" in payload:
        value = payload.get("traffic-shaper")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "traffic-shaper cannot exceed 35 characters")

    # Validate traffic-shaper-reverse if present
    if "traffic-shaper-reverse" in payload:
        value = payload.get("traffic-shaper-reverse")
        if value and isinstance(value, str) and len(value) > 35:
            return (
                False,
                "traffic-shaper-reverse cannot exceed 35 characters",
            )

    # Validate per-ip-shaper if present
    if "per-ip-shaper" in payload:
        value = payload.get("per-ip-shaper")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "per-ip-shaper cannot exceed 35 characters")

    # Validate class-id if present
    if "class-id" in payload:
        value = payload.get("class-id")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "class-id must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (False, f"class-id must be numeric, got: {value}")

    # Validate diffserv-forward if present
    if "diffserv-forward" in payload:
        value = payload.get("diffserv-forward")
        if value and value not in VALID_BODY_DIFFSERV_FORWARD:
            return (
                False,
                f"Invalid diffserv-forward '{value}'. Must be one of: {', '.join(VALID_BODY_DIFFSERV_FORWARD)}",
            )

    # Validate diffserv-reverse if present
    if "diffserv-reverse" in payload:
        value = payload.get("diffserv-reverse")
        if value and value not in VALID_BODY_DIFFSERV_REVERSE:
            return (
                False,
                f"Invalid diffserv-reverse '{value}'. Must be one of: {', '.join(VALID_BODY_DIFFSERV_REVERSE)}",
            )

    return (True, None)


# ============================================================================
# DELETE Validation
# ============================================================================


def validate_shaping_policy_delete(
    id: str | None = None,
) -> tuple[bool, str | None]:
    """
    Validate DELETE request parameters.

    Args:
        id: Object identifier (required)

    Returns:
        Tuple of (is_valid, error_message)
    """
    if not id:
        return (False, "id is required for DELETE operation")

    return (True, None)
