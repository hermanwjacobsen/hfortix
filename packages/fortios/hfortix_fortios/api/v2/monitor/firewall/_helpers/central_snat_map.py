"""
Validation helpers for firewall central_snat_map endpoint.

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


def validate_central_snat_map_get(
    policyid: str | None = None,
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate GET request parameters.

    Args:
        policyid: Object identifier (optional for list, required for specific)
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
        >>> is_valid, error = validate_central_snat_map_get(policyid="value")
        >>> if not is_valid:
        ...     raise ValueError(error)
    """
    # policyid is optional - if None, returns list of all objects
    # Validate format only if provided and not empty
    if policyid is not None and str(policyid).strip():
        if not isinstance(policyid, (str, int)):
            return (False, "policyid must be a string or integer")

    return (True, None)


# ============================================================================
# POST Validation
# ============================================================================


def validate_central_snat_map_post(
    payload: dict[str, Any],
) -> tuple[bool, str | None]:
    """
    Validate POST request payload for creating central_snat_map.

    Args:
        payload: The payload to validate

    Returns:
        Tuple of (is_valid, error_message)
    """
    return (True, None)
