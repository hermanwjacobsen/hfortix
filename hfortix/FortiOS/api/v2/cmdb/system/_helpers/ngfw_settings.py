"""
Validation helpers for system ngfw_settings endpoint.

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


def validate_ngfw_settings_get(
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


def validate_ngfw_settings_put(
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

    # Validate match-timeout if present
    if "match-timeout" in payload:
        value = payload.get("match-timeout")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 1800:
                    return (False, "match-timeout must be between 0 and 1800")
            except (ValueError, TypeError):
                return (False, f"match-timeout must be numeric, got: {value}")

    # Validate tcp-match-timeout if present
    if "tcp-match-timeout" in payload:
        value = payload.get("tcp-match-timeout")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 1800:
                    return (
                        False,
                        "tcp-match-timeout must be between 0 and 1800",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"tcp-match-timeout must be numeric, got: {value}",
                )

    # Validate tcp-halfopen-match-timeout if present
    if "tcp-halfopen-match-timeout" in payload:
        value = payload.get("tcp-halfopen-match-timeout")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 300:
                    return (
                        False,
                        "tcp-halfopen-match-timeout must be between 0 and 300",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"tcp-halfopen-match-timeout must be numeric, got: {value}",
                )

    return (True, None)
