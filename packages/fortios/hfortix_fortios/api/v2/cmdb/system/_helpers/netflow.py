"""
Validation helpers for system netflow endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_SESSION_CACHE_SIZE = ["min", "default", "max"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_netflow_get(
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


def validate_netflow_put(
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

    # Validate active-flow-timeout if present
    if "active-flow-timeout" in payload:
        value = payload.get("active-flow-timeout")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 60 or int_val > 3600:
                    return (
                        False,
                        "active-flow-timeout must be between 60 and 3600",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"active-flow-timeout must be numeric, got: {value}",
                )

    # Validate inactive-flow-timeout if present
    if "inactive-flow-timeout" in payload:
        value = payload.get("inactive-flow-timeout")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 10 or int_val > 600:
                    return (
                        False,
                        "inactive-flow-timeout must be between 10 and 600",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"inactive-flow-timeout must be numeric, got: {value}",
                )

    # Validate template-tx-timeout if present
    if "template-tx-timeout" in payload:
        value = payload.get("template-tx-timeout")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 60 or int_val > 86400:
                    return (
                        False,
                        "template-tx-timeout must be between 60 and 86400",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"template-tx-timeout must be numeric, got: {value}",
                )

    # Validate template-tx-counter if present
    if "template-tx-counter" in payload:
        value = payload.get("template-tx-counter")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 10 or int_val > 6000:
                    return (
                        False,
                        "template-tx-counter must be between 10 and 6000",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"template-tx-counter must be numeric, got: {value}",
                )

    # Validate session-cache-size if present
    if "session-cache-size" in payload:
        value = payload.get("session-cache-size")
        if value and value not in VALID_BODY_SESSION_CACHE_SIZE:
            return (
                False,
                f"Invalid session-cache-size '{value}'. Must be one of: {', '.join(VALID_BODY_SESSION_CACHE_SIZE)}",
            )

    return (True, None)
