"""
Validation helpers for system fips_cc endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_STATUS = ["enable", "disable"]
VALID_BODY_KEY_GENERATION_SELF_TEST = ["enable", "disable"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_fips_cc_get(
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


def validate_fips_cc_put(
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

    # Validate self-test-period if present
    if "self-test-period" in payload:
        value = payload.get("self-test-period")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 5 or int_val > 1440:
                    return (
                        False,
                        "self-test-period must be between 5 and 1440",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"self-test-period must be numeric, got: {value}",
                )

    # Validate key-generation-self-test if present
    if "key-generation-self-test" in payload:
        value = payload.get("key-generation-self-test")
        if value and value not in VALID_BODY_KEY_GENERATION_SELF_TEST:
            return (
                False,
                f"Invalid key-generation-self-test '{value}'. Must be one of: {', '.join(VALID_BODY_KEY_GENERATION_SELF_TEST)}",
            )

    return (True, None)
