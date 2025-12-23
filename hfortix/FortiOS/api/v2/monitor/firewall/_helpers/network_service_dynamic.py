"""
Validation helpers for firewall network_service_dynamic endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
# ============================================================================
# GET Validation
# ============================================================================


def validate_network_service_dynamic_get(
    mkey: str | None = None,
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate GET request parameters.

    Args:
        mkey: Object identifier (optional for list, required for specific)
        attr: Attribute filter (optional)
        filters: Additional filter parameters
        **params: Other query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Example:
        >>> # List all objects
        >>> is_valid, error = {func_name}()
        >>>
        >>> # Get specific object
        >>> is_valid, error =
        validate_network_service_dynamic_get(mkey="value")
        >>> if not is_valid:
        ...     raise ValueError(error)
    """
    # mkey is optional - if None, returns list of all objects
    # Validate format only if provided and not empty
    if mkey is not None and str(mkey).strip():
        if not isinstance(mkey, (str, int)):
            return (False, "mkey must be a string or integer")

    return (True, None)


# ============================================================================
# POST Validation
# ============================================================================


def validate_network_service_dynamic_post(
    payload: dict[str, Any],
) -> tuple[bool, str | None]:
    """
    Validate POST request payload for creating network_service_dynamic.

    Args:
        payload: The payload to validate

    Returns:
        Tuple of (is_valid, error_message)
    """
    return (True, None)
