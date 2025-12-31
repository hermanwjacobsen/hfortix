"""
Validation helpers for system snmp_sysinfo endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_STATUS = ["enable", "disable"]
VALID_BODY_ENGINE_ID_TYPE = ["text", "hex", "mac"]
VALID_BODY_APPEND_INDEX = ["enable", "disable"]
VALID_BODY_NON_MGMT_VDOM_QUERY = ["enable", "disable"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_snmp_sysinfo_get(
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


def validate_snmp_sysinfo_put(
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

    # Validate engine-id-type if present
    if "engine-id-type" in payload:
        value = payload.get("engine-id-type")
        if value and value not in VALID_BODY_ENGINE_ID_TYPE:
            return (
                False,
                f"Invalid engine-id-type '{value}'. Must be one of: {', '.join(VALID_BODY_ENGINE_ID_TYPE)}",
            )

    # Validate engine-id if present
    if "engine-id" in payload:
        value = payload.get("engine-id")
        if value and isinstance(value, str) and len(value) > 54:
            return (False, "engine-id cannot exceed 54 characters")

    # Validate description if present
    if "description" in payload:
        value = payload.get("description")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "description cannot exceed 255 characters")

    # Validate contact-info if present
    if "contact-info" in payload:
        value = payload.get("contact-info")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "contact-info cannot exceed 255 characters")

    # Validate location if present
    if "location" in payload:
        value = payload.get("location")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "location cannot exceed 255 characters")

    # Validate trap-high-cpu-threshold if present
    if "trap-high-cpu-threshold" in payload:
        value = payload.get("trap-high-cpu-threshold")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 100:
                    return (
                        False,
                        "trap-high-cpu-threshold must be between 1 and 100",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"trap-high-cpu-threshold must be numeric, got: {value}",
                )

    # Validate trap-low-memory-threshold if present
    if "trap-low-memory-threshold" in payload:
        value = payload.get("trap-low-memory-threshold")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 100:
                    return (
                        False,
                        "trap-low-memory-threshold must be between 1 and 100",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"trap-low-memory-threshold must be numeric, got: {value}",
                )

    # Validate trap-log-full-threshold if present
    if "trap-log-full-threshold" in payload:
        value = payload.get("trap-log-full-threshold")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 100:
                    return (
                        False,
                        "trap-log-full-threshold must be between 1 and 100",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"trap-log-full-threshold must be numeric, got: {value}",
                )

    # Validate trap-free-memory-threshold if present
    if "trap-free-memory-threshold" in payload:
        value = payload.get("trap-free-memory-threshold")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 100:
                    return (
                        False,
                        "trap-free-memory-threshold must be between 1 and 100",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"trap-free-memory-threshold must be numeric, got: {value}",
                )

    # Validate trap-freeable-memory-threshold if present
    if "trap-freeable-memory-threshold" in payload:
        value = payload.get("trap-freeable-memory-threshold")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 100:
                    return (
                        False,
                        "trap-freeable-memory-threshold must be between 1 and 100",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"trap-freeable-memory-threshold must be numeric, got: {value}",
                )

    # Validate append-index if present
    if "append-index" in payload:
        value = payload.get("append-index")
        if value and value not in VALID_BODY_APPEND_INDEX:
            return (
                False,
                f"Invalid append-index '{value}'. Must be one of: {', '.join(VALID_BODY_APPEND_INDEX)}",
            )

    # Validate non-mgmt-vdom-query if present
    if "non-mgmt-vdom-query" in payload:
        value = payload.get("non-mgmt-vdom-query")
        if value and value not in VALID_BODY_NON_MGMT_VDOM_QUERY:
            return (
                False,
                f"Invalid non-mgmt-vdom-query '{value}'. Must be one of: {', '.join(VALID_BODY_NON_MGMT_VDOM_QUERY)}",
            )

    return (True, None)
