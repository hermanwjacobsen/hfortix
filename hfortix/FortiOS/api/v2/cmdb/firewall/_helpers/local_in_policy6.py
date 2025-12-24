"""
Validation helpers for firewall local_in_policy6 endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_SRCADDR_NEGATE = ["enable", "disable"]
VALID_BODY_INTERNET_SERVICE6_SRC = ["enable", "disable"]
VALID_BODY_DSTADDR_NEGATE = ["enable", "disable"]
VALID_BODY_ACTION = ["accept", "deny"]
VALID_BODY_SERVICE_NEGATE = ["enable", "disable"]
VALID_BODY_INTERNET_SERVICE6_SRC_NEGATE = ["enable", "disable"]
VALID_BODY_STATUS = ["enable", "disable"]
VALID_BODY_VIRTUAL_PATCH = ["enable", "disable"]
VALID_BODY_LOGTRAFFIC = ["enable", "disable"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_local_in_policy6_get(
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


def validate_local_in_policy6_post(
    payload: dict[str, Any],
) -> tuple[bool, str | None]:
    """
    Validate POST request payload for creating local_in_policy6.

    Args:
        payload: The payload to validate

    Returns:
        Tuple of (is_valid, error_message)
    """
    # Validate policyid if present
    if "policyid" in payload:
        value = payload.get("policyid")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "policyid must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (False, f"policyid must be numeric, got: {value}")

    # Validate srcaddr-negate if present
    if "srcaddr-negate" in payload:
        value = payload.get("srcaddr-negate")
        if value and value not in VALID_BODY_SRCADDR_NEGATE:
            return (
                False,
                f"Invalid srcaddr-negate '{value}'. Must be one of: {', '.join(VALID_BODY_SRCADDR_NEGATE)}",
            )

    # Validate internet-service6-src if present
    if "internet-service6-src" in payload:
        value = payload.get("internet-service6-src")
        if value and value not in VALID_BODY_INTERNET_SERVICE6_SRC:
            return (
                False,
                f"Invalid internet-service6-src '{value}'. Must be one of: {', '.join(VALID_BODY_INTERNET_SERVICE6_SRC)}",
            )

    # Validate dstaddr-negate if present
    if "dstaddr-negate" in payload:
        value = payload.get("dstaddr-negate")
        if value and value not in VALID_BODY_DSTADDR_NEGATE:
            return (
                False,
                f"Invalid dstaddr-negate '{value}'. Must be one of: {', '.join(VALID_BODY_DSTADDR_NEGATE)}",
            )

    # Validate action if present
    if "action" in payload:
        value = payload.get("action")
        if value and value not in VALID_BODY_ACTION:
            return (
                False,
                f"Invalid action '{value}'. Must be one of: {', '.join(VALID_BODY_ACTION)}",
            )

    # Validate service-negate if present
    if "service-negate" in payload:
        value = payload.get("service-negate")
        if value and value not in VALID_BODY_SERVICE_NEGATE:
            return (
                False,
                f"Invalid service-negate '{value}'. Must be one of: {', '.join(VALID_BODY_SERVICE_NEGATE)}",
            )

    # Validate internet-service6-src-negate if present
    if "internet-service6-src-negate" in payload:
        value = payload.get("internet-service6-src-negate")
        if value and value not in VALID_BODY_INTERNET_SERVICE6_SRC_NEGATE:
            return (
                False,
                f"Invalid internet-service6-src-negate '{value}'. Must be one of: {', '.join(VALID_BODY_INTERNET_SERVICE6_SRC_NEGATE)}",
            )

    # Validate schedule if present
    if "schedule" in payload:
        value = payload.get("schedule")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "schedule cannot exceed 35 characters")

    # Validate status if present
    if "status" in payload:
        value = payload.get("status")
        if value and value not in VALID_BODY_STATUS:
            return (
                False,
                f"Invalid status '{value}'. Must be one of: {', '.join(VALID_BODY_STATUS)}",
            )

    # Validate virtual-patch if present
    if "virtual-patch" in payload:
        value = payload.get("virtual-patch")
        if value and value not in VALID_BODY_VIRTUAL_PATCH:
            return (
                False,
                f"Invalid virtual-patch '{value}'. Must be one of: {', '.join(VALID_BODY_VIRTUAL_PATCH)}",
            )

    # Validate logtraffic if present
    if "logtraffic" in payload:
        value = payload.get("logtraffic")
        if value and value not in VALID_BODY_LOGTRAFFIC:
            return (
                False,
                f"Invalid logtraffic '{value}'. Must be one of: {', '.join(VALID_BODY_LOGTRAFFIC)}",
            )

    # Validate comments if present
    if "comments" in payload:
        value = payload.get("comments")
        if value and isinstance(value, str) and len(value) > 1023:
            return (False, "comments cannot exceed 1023 characters")

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_local_in_policy6_put(
    policyid: str | None = None, payload: dict[str, Any] | None = None
) -> tuple[bool, str | None]:
    """
    Validate PUT request payload for updating {endpoint_name}.

    Args:
        policyid: Object identifier (required)
        payload: The payload to validate

    Returns:
        Tuple of (is_valid, error_message)
    """
    # policyid is required for updates
    if not policyid:
        return (False, "policyid is required for PUT operation")

    # If no payload provided, nothing to validate
    if not payload:
        return (True, None)

    # Validate policyid if present
    if "policyid" in payload:
        value = payload.get("policyid")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "policyid must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (False, f"policyid must be numeric, got: {value}")

    # Validate srcaddr-negate if present
    if "srcaddr-negate" in payload:
        value = payload.get("srcaddr-negate")
        if value and value not in VALID_BODY_SRCADDR_NEGATE:
            return (
                False,
                f"Invalid srcaddr-negate '{value}'. Must be one of: {', '.join(VALID_BODY_SRCADDR_NEGATE)}",
            )

    # Validate internet-service6-src if present
    if "internet-service6-src" in payload:
        value = payload.get("internet-service6-src")
        if value and value not in VALID_BODY_INTERNET_SERVICE6_SRC:
            return (
                False,
                f"Invalid internet-service6-src '{value}'. Must be one of: {', '.join(VALID_BODY_INTERNET_SERVICE6_SRC)}",
            )

    # Validate dstaddr-negate if present
    if "dstaddr-negate" in payload:
        value = payload.get("dstaddr-negate")
        if value and value not in VALID_BODY_DSTADDR_NEGATE:
            return (
                False,
                f"Invalid dstaddr-negate '{value}'. Must be one of: {', '.join(VALID_BODY_DSTADDR_NEGATE)}",
            )

    # Validate action if present
    if "action" in payload:
        value = payload.get("action")
        if value and value not in VALID_BODY_ACTION:
            return (
                False,
                f"Invalid action '{value}'. Must be one of: {', '.join(VALID_BODY_ACTION)}",
            )

    # Validate service-negate if present
    if "service-negate" in payload:
        value = payload.get("service-negate")
        if value and value not in VALID_BODY_SERVICE_NEGATE:
            return (
                False,
                f"Invalid service-negate '{value}'. Must be one of: {', '.join(VALID_BODY_SERVICE_NEGATE)}",
            )

    # Validate internet-service6-src-negate if present
    if "internet-service6-src-negate" in payload:
        value = payload.get("internet-service6-src-negate")
        if value and value not in VALID_BODY_INTERNET_SERVICE6_SRC_NEGATE:
            return (
                False,
                f"Invalid internet-service6-src-negate '{value}'. Must be one of: {', '.join(VALID_BODY_INTERNET_SERVICE6_SRC_NEGATE)}",
            )

    # Validate schedule if present
    if "schedule" in payload:
        value = payload.get("schedule")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "schedule cannot exceed 35 characters")

    # Validate status if present
    if "status" in payload:
        value = payload.get("status")
        if value and value not in VALID_BODY_STATUS:
            return (
                False,
                f"Invalid status '{value}'. Must be one of: {', '.join(VALID_BODY_STATUS)}",
            )

    # Validate virtual-patch if present
    if "virtual-patch" in payload:
        value = payload.get("virtual-patch")
        if value and value not in VALID_BODY_VIRTUAL_PATCH:
            return (
                False,
                f"Invalid virtual-patch '{value}'. Must be one of: {', '.join(VALID_BODY_VIRTUAL_PATCH)}",
            )

    # Validate logtraffic if present
    if "logtraffic" in payload:
        value = payload.get("logtraffic")
        if value and value not in VALID_BODY_LOGTRAFFIC:
            return (
                False,
                f"Invalid logtraffic '{value}'. Must be one of: {', '.join(VALID_BODY_LOGTRAFFIC)}",
            )

    # Validate comments if present
    if "comments" in payload:
        value = payload.get("comments")
        if value and isinstance(value, str) and len(value) > 1023:
            return (False, "comments cannot exceed 1023 characters")

    return (True, None)


# ============================================================================
# DELETE Validation
# ============================================================================


def validate_local_in_policy6_delete(
    policyid: str | None = None,
) -> tuple[bool, str | None]:
    """
    Validate DELETE request parameters.

    Args:
        policyid: Object identifier (required)

    Returns:
        Tuple of (is_valid, error_message)
    """
    if not policyid:
        return (False, "policyid is required for DELETE operation")

    return (True, None)
