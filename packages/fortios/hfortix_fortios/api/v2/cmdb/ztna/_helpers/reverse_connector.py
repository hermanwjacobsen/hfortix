"""
Validation helpers for ztna reverse_connector endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_STATUS = ["enable", "disable"]
VALID_BODY_SSL_MAX_VERSION = ["tls-1.1", "tls-1.2", "tls-1.3"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_reverse_connector_get(
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


def validate_reverse_connector_post(
    payload: dict[str, Any],
) -> tuple[bool, str | None]:
    """
    Validate POST request payload for creating reverse_connector.

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

    # Validate status if present
    if "status" in payload:
        value = payload.get("status")
        if value and value not in VALID_BODY_STATUS:
            return (
                False,
                f"Invalid status '{value}'. Must be one of: {', '.join(VALID_BODY_STATUS)}",
            )

    # Validate address if present
    if "address" in payload:
        value = payload.get("address")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "address cannot exceed 255 characters")

    # Validate port if present
    if "port" in payload:
        value = payload.get("port")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 65535:
                    return (False, "port must be between 0 and 65535")
            except (ValueError, TypeError):
                return (False, f"port must be numeric, got: {value}")

    # Validate health-check-interval if present
    if "health-check-interval" in payload:
        value = payload.get("health-check-interval")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 600:
                    return (
                        False,
                        "health-check-interval must be between 0 and 600",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"health-check-interval must be numeric, got: {value}",
                )

    # Validate ssl-max-version if present
    if "ssl-max-version" in payload:
        value = payload.get("ssl-max-version")
        if value and value not in VALID_BODY_SSL_MAX_VERSION:
            return (
                False,
                f"Invalid ssl-max-version '{value}'. Must be one of: {', '.join(VALID_BODY_SSL_MAX_VERSION)}",
            )

    # Validate certificate if present
    if "certificate" in payload:
        value = payload.get("certificate")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "certificate cannot exceed 35 characters")

    # Validate trusted-server-ca if present
    if "trusted-server-ca" in payload:
        value = payload.get("trusted-server-ca")
        if value and isinstance(value, str) and len(value) > 79:
            return (False, "trusted-server-ca cannot exceed 79 characters")

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_reverse_connector_put(
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

    # Validate status if present
    if "status" in payload:
        value = payload.get("status")
        if value and value not in VALID_BODY_STATUS:
            return (
                False,
                f"Invalid status '{value}'. Must be one of: {', '.join(VALID_BODY_STATUS)}",
            )

    # Validate address if present
    if "address" in payload:
        value = payload.get("address")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "address cannot exceed 255 characters")

    # Validate port if present
    if "port" in payload:
        value = payload.get("port")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 65535:
                    return (False, "port must be between 0 and 65535")
            except (ValueError, TypeError):
                return (False, f"port must be numeric, got: {value}")

    # Validate health-check-interval if present
    if "health-check-interval" in payload:
        value = payload.get("health-check-interval")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 600:
                    return (
                        False,
                        "health-check-interval must be between 0 and 600",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"health-check-interval must be numeric, got: {value}",
                )

    # Validate ssl-max-version if present
    if "ssl-max-version" in payload:
        value = payload.get("ssl-max-version")
        if value and value not in VALID_BODY_SSL_MAX_VERSION:
            return (
                False,
                f"Invalid ssl-max-version '{value}'. Must be one of: {', '.join(VALID_BODY_SSL_MAX_VERSION)}",
            )

    # Validate certificate if present
    if "certificate" in payload:
        value = payload.get("certificate")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "certificate cannot exceed 35 characters")

    # Validate trusted-server-ca if present
    if "trusted-server-ca" in payload:
        value = payload.get("trusted-server-ca")
        if value and isinstance(value, str) and len(value) > 79:
            return (False, "trusted-server-ca cannot exceed 79 characters")

    return (True, None)


# ============================================================================
# DELETE Validation
# ============================================================================


def validate_reverse_connector_delete(
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
