"""
Validation helpers for system cloud_service endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_VENDOR = ["unknown", "google-cloud-kms"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_cloud_service_get(
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
# POST Validation
# ============================================================================


def validate_cloud_service_post(
    payload: dict[str, Any],
) -> tuple[bool, str | None]:
    """
    Validate POST request payload for creating cloud_service.

    Args:
        payload: The payload to validate

    Returns:
        Tuple of (is_valid, error_message)
    """
    # Validate name if present
    if "name" in payload:
        value = payload.get("name")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "name cannot exceed 35 characters")

    # Validate vendor if present
    if "vendor" in payload:
        value = payload.get("vendor")
        if value and value not in VALID_BODY_VENDOR:
            return (
                False,
                f"Invalid vendor '{value}'. Must be one of: {', '.join(VALID_BODY_VENDOR)}",
            )

    # Validate traffic-vdom if present
    if "traffic-vdom" in payload:
        value = payload.get("traffic-vdom")
        if value and isinstance(value, str) and len(value) > 31:
            return (False, "traffic-vdom cannot exceed 31 characters")

    # Validate gck-service-account if present
    if "gck-service-account" in payload:
        value = payload.get("gck-service-account")
        if value and isinstance(value, str) and len(value) > 285:
            return (False, "gck-service-account cannot exceed 285 characters")

    # Validate gck-private-key if present
    if "gck-private-key" in payload:
        value = payload.get("gck-private-key")
        if value and isinstance(value, str) and len(value) > 8191:
            return (False, "gck-private-key cannot exceed 8191 characters")

    # Validate gck-keyid if present
    if "gck-keyid" in payload:
        value = payload.get("gck-keyid")
        if value and isinstance(value, str) and len(value) > 127:
            return (False, "gck-keyid cannot exceed 127 characters")

    # Validate gck-access-token-lifetime if present
    if "gck-access-token-lifetime" in payload:
        value = payload.get("gck-access-token-lifetime")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 3600:
                    return (
                        False,
                        "gck-access-token-lifetime must be between 1 and 3600",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"gck-access-token-lifetime must be numeric, got: {value}",
                )

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_cloud_service_put(
    name: str | None = None, payload: dict[str, Any] | None = None
) -> tuple[bool, str | None]:
    """
    Validate PUT request payload for updating {endpoint_name}.

    Args:
        name: Object identifier (required)
        payload: The payload to validate

    Returns:
        Tuple of (is_valid, error_message)
    """
    # name is required for updates
    if not name:
        return (False, "name is required for PUT operation")

    # If no payload provided, nothing to validate
    if not payload:
        return (True, None)

    # Validate name if present
    if "name" in payload:
        value = payload.get("name")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "name cannot exceed 35 characters")

    # Validate vendor if present
    if "vendor" in payload:
        value = payload.get("vendor")
        if value and value not in VALID_BODY_VENDOR:
            return (
                False,
                f"Invalid vendor '{value}'. Must be one of: {', '.join(VALID_BODY_VENDOR)}",
            )

    # Validate traffic-vdom if present
    if "traffic-vdom" in payload:
        value = payload.get("traffic-vdom")
        if value and isinstance(value, str) and len(value) > 31:
            return (False, "traffic-vdom cannot exceed 31 characters")

    # Validate gck-service-account if present
    if "gck-service-account" in payload:
        value = payload.get("gck-service-account")
        if value and isinstance(value, str) and len(value) > 285:
            return (False, "gck-service-account cannot exceed 285 characters")

    # Validate gck-private-key if present
    if "gck-private-key" in payload:
        value = payload.get("gck-private-key")
        if value and isinstance(value, str) and len(value) > 8191:
            return (False, "gck-private-key cannot exceed 8191 characters")

    # Validate gck-keyid if present
    if "gck-keyid" in payload:
        value = payload.get("gck-keyid")
        if value and isinstance(value, str) and len(value) > 127:
            return (False, "gck-keyid cannot exceed 127 characters")

    # Validate gck-access-token-lifetime if present
    if "gck-access-token-lifetime" in payload:
        value = payload.get("gck-access-token-lifetime")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 3600:
                    return (
                        False,
                        "gck-access-token-lifetime must be between 1 and 3600",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"gck-access-token-lifetime must be numeric, got: {value}",
                )

    return (True, None)


# ============================================================================
# DELETE Validation
# ============================================================================


def validate_cloud_service_delete(
    name: str | None = None,
) -> tuple[bool, str | None]:
    """
    Validate DELETE request parameters.

    Args:
        name: Object identifier (required)

    Returns:
        Tuple of (is_valid, error_message)
    """
    if not name:
        return (False, "name is required for DELETE operation")

    return (True, None)
