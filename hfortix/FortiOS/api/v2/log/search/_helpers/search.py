"""
Validation helpers for search search endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

from ...._helpers import validate_required_fields

# Valid enum values from API documentation
# ============================================================================
# GET Validation
# ============================================================================


def validate_search_get(
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
    return (True, None)


# ============================================================================
# POST Validation
# ============================================================================


def validate_search_post(payload: dict[str, Any]) -> tuple[bool, str | None]:
    """
    Validate POST request payload for creating search.

    Required fields (API documentation):
    - session_id: Provide the session ID for the request

    Args:
        payload: The payload to validate

    Returns:
        Tuple of (is_valid, error_message)
    """
    # Required fields
    required_fields = ["session_id"]

    is_valid, missing = validate_required_fields(payload, required_fields)
    if not is_valid:
        return (False, f"Missing required fields: {', '.join(missing)}")

    return (True, None)
