"""
Validation helpers for emailfilter fortishield endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_SPAM_SUBMIT_FORCE = ["enable", "disable"]
VALID_BODY_SPAM_SUBMIT_TXT2HTM = ["enable", "disable"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_fortishield_get(
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


def validate_fortishield_put(
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

    # Validate spam-submit-srv if present
    if "spam-submit-srv" in payload:
        value = payload.get("spam-submit-srv")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "spam-submit-srv cannot exceed 63 characters")

    # Validate spam-submit-force if present
    if "spam-submit-force" in payload:
        value = payload.get("spam-submit-force")
        if value and value not in VALID_BODY_SPAM_SUBMIT_FORCE:
            return (
                False,
                f"Invalid spam-submit-force '{value}'. Must be one of: {', '.join(VALID_BODY_SPAM_SUBMIT_FORCE)}",
            )

    # Validate spam-submit-txt2htm if present
    if "spam-submit-txt2htm" in payload:
        value = payload.get("spam-submit-txt2htm")
        if value and value not in VALID_BODY_SPAM_SUBMIT_TXT2HTM:
            return (
                False,
                f"Invalid spam-submit-txt2htm '{value}'. Must be one of: {', '.join(VALID_BODY_SPAM_SUBMIT_TXT2HTM)}",
            )

    return (True, None)
