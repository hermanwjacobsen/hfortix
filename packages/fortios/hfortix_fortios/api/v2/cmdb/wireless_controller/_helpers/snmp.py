"""
Validation helpers for wireless-controller snmp endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_snmp_get(
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


def validate_snmp_put(
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

    # Validate engine-id if present
    if "engine-id" in payload:
        value = payload.get("engine-id")
        if value and isinstance(value, str) and len(value) > 23:
            return (False, "engine-id cannot exceed 23 characters")

    # Validate contact-info if present
    if "contact-info" in payload:
        value = payload.get("contact-info")
        if value and isinstance(value, str) and len(value) > 31:
            return (False, "contact-info cannot exceed 31 characters")

    # Validate trap-high-cpu-threshold if present
    if "trap-high-cpu-threshold" in payload:
        value = payload.get("trap-high-cpu-threshold")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 10 or int_val > 100:
                    return (
                        False,
                        "trap-high-cpu-threshold must be between 10 and 100",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"trap-high-cpu-threshold must be numeric, got: {value}",
                )

    # Validate trap-high-mem-threshold if present
    if "trap-high-mem-threshold" in payload:
        value = payload.get("trap-high-mem-threshold")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 10 or int_val > 100:
                    return (
                        False,
                        "trap-high-mem-threshold must be between 10 and 100",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"trap-high-mem-threshold must be numeric, got: {value}",
                )

    return (True, None)
