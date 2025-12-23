"""
Validation helpers for system network_visibility endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_DESTINATION_VISIBILITY = ["disable", "enable"]
VALID_BODY_SOURCE_LOCATION = ["disable", "enable"]
VALID_BODY_DESTINATION_HOSTNAME_VISIBILITY = ["disable", "enable"]
VALID_BODY_DESTINATION_LOCATION = ["disable", "enable"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_network_visibility_get(
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


def validate_network_visibility_put(
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

    # Validate destination-visibility if present
    if "destination-visibility" in payload:
        value = payload.get("destination-visibility")
        if value and value not in VALID_BODY_DESTINATION_VISIBILITY:
            return (
                False,
                f"Invalid destination-visibility '{value}'. Must be one of: {', '.join(VALID_BODY_DESTINATION_VISIBILITY)}",
            )

    # Validate source-location if present
    if "source-location" in payload:
        value = payload.get("source-location")
        if value and value not in VALID_BODY_SOURCE_LOCATION:
            return (
                False,
                f"Invalid source-location '{value}'. Must be one of: {', '.join(VALID_BODY_SOURCE_LOCATION)}",
            )

    # Validate destination-hostname-visibility if present
    if "destination-hostname-visibility" in payload:
        value = payload.get("destination-hostname-visibility")
        if value and value not in VALID_BODY_DESTINATION_HOSTNAME_VISIBILITY:
            return (
                False,
                f"Invalid destination-hostname-visibility '{value}'. Must be one of: {', '.join(VALID_BODY_DESTINATION_HOSTNAME_VISIBILITY)}",
            )

    # Validate destination-location if present
    if "destination-location" in payload:
        value = payload.get("destination-location")
        if value and value not in VALID_BODY_DESTINATION_LOCATION:
            return (
                False,
                f"Invalid destination-location '{value}'. Must be one of: {', '.join(VALID_BODY_DESTINATION_LOCATION)}",
            )

    return (True, None)
