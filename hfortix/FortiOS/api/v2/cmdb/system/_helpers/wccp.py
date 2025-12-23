"""
Validation helpers for system wccp endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_PORTS_DEFINED = ["source", "destination"]
VALID_BODY_SERVER_TYPE = ["forward", "proxy"]
VALID_BODY_AUTHENTICATION = ["enable", "disable"]
VALID_BODY_FORWARD_METHOD = ["GRE", "L2", "any"]
VALID_BODY_CACHE_ENGINE_METHOD = ["GRE", "L2"]
VALID_BODY_SERVICE_TYPE = ["auto", "standard", "dynamic"]
VALID_BODY_PRIMARY_HASH = ["src-ip", "dst-ip", "src-port", "dst-port"]
VALID_BODY_ASSIGNMENT_BUCKET_FORMAT = ["wccp-v2", "cisco-implementation"]
VALID_BODY_RETURN_METHOD = ["GRE", "L2", "any"]
VALID_BODY_ASSIGNMENT_METHOD = ["HASH", "MASK", "any"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_wccp_get(
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


def validate_wccp_post(payload: dict[str, Any]) -> tuple[bool, str | None]:
    """
    Validate POST request payload for creating wccp.

    Args:
        payload: The payload to validate

    Returns:
        Tuple of (is_valid, error_message)
    """
    # Validate service-id if present
    if "service-id" in payload:
        value = payload.get("service-id")
        if value and isinstance(value, str) and len(value) > 3:
            return (False, "service-id cannot exceed 3 characters")

    # Validate ports-defined if present
    if "ports-defined" in payload:
        value = payload.get("ports-defined")
        if value and value not in VALID_BODY_PORTS_DEFINED:
            return (
                False,
                f"Invalid ports-defined '{value}'. Must be one of: {', '.join(VALID_BODY_PORTS_DEFINED)}",
            )

    # Validate server-type if present
    if "server-type" in payload:
        value = payload.get("server-type")
        if value and value not in VALID_BODY_SERVER_TYPE:
            return (
                False,
                f"Invalid server-type '{value}'. Must be one of: {', '.join(VALID_BODY_SERVER_TYPE)}",
            )

    # Validate authentication if present
    if "authentication" in payload:
        value = payload.get("authentication")
        if value and value not in VALID_BODY_AUTHENTICATION:
            return (
                False,
                f"Invalid authentication '{value}'. Must be one of: {', '.join(VALID_BODY_AUTHENTICATION)}",
            )

    # Validate forward-method if present
    if "forward-method" in payload:
        value = payload.get("forward-method")
        if value and value not in VALID_BODY_FORWARD_METHOD:
            return (
                False,
                f"Invalid forward-method '{value}'. Must be one of: {', '.join(VALID_BODY_FORWARD_METHOD)}",
            )

    # Validate cache-engine-method if present
    if "cache-engine-method" in payload:
        value = payload.get("cache-engine-method")
        if value and value not in VALID_BODY_CACHE_ENGINE_METHOD:
            return (
                False,
                f"Invalid cache-engine-method '{value}'. Must be one of: {', '.join(VALID_BODY_CACHE_ENGINE_METHOD)}",
            )

    # Validate service-type if present
    if "service-type" in payload:
        value = payload.get("service-type")
        if value and value not in VALID_BODY_SERVICE_TYPE:
            return (
                False,
                f"Invalid service-type '{value}'. Must be one of: {', '.join(VALID_BODY_SERVICE_TYPE)}",
            )

    # Validate primary-hash if present
    if "primary-hash" in payload:
        value = payload.get("primary-hash")
        if value and value not in VALID_BODY_PRIMARY_HASH:
            return (
                False,
                f"Invalid primary-hash '{value}'. Must be one of: {', '.join(VALID_BODY_PRIMARY_HASH)}",
            )

    # Validate priority if present
    if "priority" in payload:
        value = payload.get("priority")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 255:
                    return (False, "priority must be between 0 and 255")
            except (ValueError, TypeError):
                return (False, f"priority must be numeric, got: {value}")

    # Validate protocol if present
    if "protocol" in payload:
        value = payload.get("protocol")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 255:
                    return (False, "protocol must be between 0 and 255")
            except (ValueError, TypeError):
                return (False, f"protocol must be numeric, got: {value}")

    # Validate assignment-weight if present
    if "assignment-weight" in payload:
        value = payload.get("assignment-weight")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 255:
                    return (
                        False,
                        "assignment-weight must be between 0 and 255",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"assignment-weight must be numeric, got: {value}",
                )

    # Validate assignment-bucket-format if present
    if "assignment-bucket-format" in payload:
        value = payload.get("assignment-bucket-format")
        if value and value not in VALID_BODY_ASSIGNMENT_BUCKET_FORMAT:
            return (
                False,
                f"Invalid assignment-bucket-format '{value}'. Must be one of: {', '.join(VALID_BODY_ASSIGNMENT_BUCKET_FORMAT)}",
            )

    # Validate return-method if present
    if "return-method" in payload:
        value = payload.get("return-method")
        if value and value not in VALID_BODY_RETURN_METHOD:
            return (
                False,
                f"Invalid return-method '{value}'. Must be one of: {', '.join(VALID_BODY_RETURN_METHOD)}",
            )

    # Validate assignment-method if present
    if "assignment-method" in payload:
        value = payload.get("assignment-method")
        if value and value not in VALID_BODY_ASSIGNMENT_METHOD:
            return (
                False,
                f"Invalid assignment-method '{value}'. Must be one of: {', '.join(VALID_BODY_ASSIGNMENT_METHOD)}",
            )

    return (True, None)
