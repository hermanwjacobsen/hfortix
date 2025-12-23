"""
Validation helpers for wireless-controller wag_profile endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_TUNNEL_TYPE = ["l2tpv3", "gre"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_wag_profile_get(
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


def validate_wag_profile_post(
    payload: dict[str, Any],
) -> tuple[bool, str | None]:
    """
    Validate POST request payload for creating wag_profile.

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

    # Validate comment if present
    if "comment" in payload:
        value = payload.get("comment")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "comment cannot exceed 255 characters")

    # Validate tunnel-type if present
    if "tunnel-type" in payload:
        value = payload.get("tunnel-type")
        if value and value not in VALID_BODY_TUNNEL_TYPE:
            return (
                False,
                f"Invalid tunnel-type '{value}'. Must be one of: {', '.join(VALID_BODY_TUNNEL_TYPE)}",
            )

    # Validate wag-port if present
    if "wag-port" in payload:
        value = payload.get("wag-port")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 65535:
                    return (False, "wag-port must be between 0 and 65535")
            except (ValueError, TypeError):
                return (False, f"wag-port must be numeric, got: {value}")

    # Validate ping-interval if present
    if "ping-interval" in payload:
        value = payload.get("ping-interval")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 65535:
                    return (
                        False,
                        "ping-interval must be between 1 and 65535",
                    )
            except (ValueError, TypeError):
                return (False, f"ping-interval must be numeric, got: {value}")

    # Validate ping-number if present
    if "ping-number" in payload:
        value = payload.get("ping-number")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 65535:
                    return (False, "ping-number must be between 1 and 65535")
            except (ValueError, TypeError):
                return (False, f"ping-number must be numeric, got: {value}")

    # Validate return-packet-timeout if present
    if "return-packet-timeout" in payload:
        value = payload.get("return-packet-timeout")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 65535:
                    return (
                        False,
                        "return-packet-timeout must be between 1 and 65535",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"return-packet-timeout must be numeric, got: {value}",
                )

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_wag_profile_put(
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

    # Validate comment if present
    if "comment" in payload:
        value = payload.get("comment")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "comment cannot exceed 255 characters")

    # Validate tunnel-type if present
    if "tunnel-type" in payload:
        value = payload.get("tunnel-type")
        if value and value not in VALID_BODY_TUNNEL_TYPE:
            return (
                False,
                f"Invalid tunnel-type '{value}'. Must be one of: {', '.join(VALID_BODY_TUNNEL_TYPE)}",
            )

    # Validate wag-port if present
    if "wag-port" in payload:
        value = payload.get("wag-port")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 65535:
                    return (False, "wag-port must be between 0 and 65535")
            except (ValueError, TypeError):
                return (False, f"wag-port must be numeric, got: {value}")

    # Validate ping-interval if present
    if "ping-interval" in payload:
        value = payload.get("ping-interval")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 65535:
                    return (
                        False,
                        "ping-interval must be between 1 and 65535",
                    )
            except (ValueError, TypeError):
                return (False, f"ping-interval must be numeric, got: {value}")

    # Validate ping-number if present
    if "ping-number" in payload:
        value = payload.get("ping-number")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 65535:
                    return (False, "ping-number must be between 1 and 65535")
            except (ValueError, TypeError):
                return (False, f"ping-number must be numeric, got: {value}")

    # Validate return-packet-timeout if present
    if "return-packet-timeout" in payload:
        value = payload.get("return-packet-timeout")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 65535:
                    return (
                        False,
                        "return-packet-timeout must be between 1 and 65535",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"return-packet-timeout must be numeric, got: {value}",
                )

    return (True, None)


# ============================================================================
# DELETE Validation
# ============================================================================


def validate_wag_profile_delete(
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
