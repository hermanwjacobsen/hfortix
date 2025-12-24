"""
Validation helpers for system mobile_tunnel endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_STATUS = ["disable", "enable"]
VALID_BODY_N_MHAE_KEY_TYPE = ["ascii", "base64"]
VALID_BODY_HASH_ALGORITHM = ["hmac-md5"]
VALID_BODY_TUNNEL_MODE = ["gre"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_mobile_tunnel_get(
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


def validate_mobile_tunnel_post(
    payload: dict[str, Any],
) -> tuple[bool, str | None]:
    """
    Validate POST request payload for creating mobile_tunnel.

    Args:
        payload: The payload to validate

    Returns:
        Tuple of (is_valid, error_message)
    """
    # Validate name if present
    if "name" in payload:
        value = payload.get("name")
        if value and isinstance(value, str) and len(value) > 15:
            return (False, "name cannot exceed 15 characters")

    # Validate status if present
    if "status" in payload:
        value = payload.get("status")
        if value and value not in VALID_BODY_STATUS:
            return (
                False,
                f"Invalid status '{value}'. Must be one of: {', '.join(VALID_BODY_STATUS)}",
            )

    # Validate roaming-interface if present
    if "roaming-interface" in payload:
        value = payload.get("roaming-interface")
        if value and isinstance(value, str) and len(value) > 15:
            return (False, "roaming-interface cannot exceed 15 characters")

    # Validate renew-interval if present
    if "renew-interval" in payload:
        value = payload.get("renew-interval")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 5 or int_val > 60:
                    return (False, "renew-interval must be between 5 and 60")
            except (ValueError, TypeError):
                return (False, f"renew-interval must be numeric, got: {value}")

    # Validate lifetime if present
    if "lifetime" in payload:
        value = payload.get("lifetime")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 180 or int_val > 65535:
                    return (False, "lifetime must be between 180 and 65535")
            except (ValueError, TypeError):
                return (False, f"lifetime must be numeric, got: {value}")

    # Validate reg-interval if present
    if "reg-interval" in payload:
        value = payload.get("reg-interval")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 5 or int_val > 300:
                    return (False, "reg-interval must be between 5 and 300")
            except (ValueError, TypeError):
                return (False, f"reg-interval must be numeric, got: {value}")

    # Validate reg-retry if present
    if "reg-retry" in payload:
        value = payload.get("reg-retry")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 30:
                    return (False, "reg-retry must be between 1 and 30")
            except (ValueError, TypeError):
                return (False, f"reg-retry must be numeric, got: {value}")

    # Validate n-mhae-spi if present
    if "n-mhae-spi" in payload:
        value = payload.get("n-mhae-spi")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "n-mhae-spi must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (False, f"n-mhae-spi must be numeric, got: {value}")

    # Validate n-mhae-key-type if present
    if "n-mhae-key-type" in payload:
        value = payload.get("n-mhae-key-type")
        if value and value not in VALID_BODY_N_MHAE_KEY_TYPE:
            return (
                False,
                f"Invalid n-mhae-key-type '{value}'. Must be one of: {', '.join(VALID_BODY_N_MHAE_KEY_TYPE)}",
            )

    # Validate hash-algorithm if present
    if "hash-algorithm" in payload:
        value = payload.get("hash-algorithm")
        if value and value not in VALID_BODY_HASH_ALGORITHM:
            return (
                False,
                f"Invalid hash-algorithm '{value}'. Must be one of: {', '.join(VALID_BODY_HASH_ALGORITHM)}",
            )

    # Validate tunnel-mode if present
    if "tunnel-mode" in payload:
        value = payload.get("tunnel-mode")
        if value and value not in VALID_BODY_TUNNEL_MODE:
            return (
                False,
                f"Invalid tunnel-mode '{value}'. Must be one of: {', '.join(VALID_BODY_TUNNEL_MODE)}",
            )

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_mobile_tunnel_put(
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
        if value and isinstance(value, str) and len(value) > 15:
            return (False, "name cannot exceed 15 characters")

    # Validate status if present
    if "status" in payload:
        value = payload.get("status")
        if value and value not in VALID_BODY_STATUS:
            return (
                False,
                f"Invalid status '{value}'. Must be one of: {', '.join(VALID_BODY_STATUS)}",
            )

    # Validate roaming-interface if present
    if "roaming-interface" in payload:
        value = payload.get("roaming-interface")
        if value and isinstance(value, str) and len(value) > 15:
            return (False, "roaming-interface cannot exceed 15 characters")

    # Validate renew-interval if present
    if "renew-interval" in payload:
        value = payload.get("renew-interval")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 5 or int_val > 60:
                    return (False, "renew-interval must be between 5 and 60")
            except (ValueError, TypeError):
                return (False, f"renew-interval must be numeric, got: {value}")

    # Validate lifetime if present
    if "lifetime" in payload:
        value = payload.get("lifetime")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 180 or int_val > 65535:
                    return (False, "lifetime must be between 180 and 65535")
            except (ValueError, TypeError):
                return (False, f"lifetime must be numeric, got: {value}")

    # Validate reg-interval if present
    if "reg-interval" in payload:
        value = payload.get("reg-interval")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 5 or int_val > 300:
                    return (False, "reg-interval must be between 5 and 300")
            except (ValueError, TypeError):
                return (False, f"reg-interval must be numeric, got: {value}")

    # Validate reg-retry if present
    if "reg-retry" in payload:
        value = payload.get("reg-retry")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 30:
                    return (False, "reg-retry must be between 1 and 30")
            except (ValueError, TypeError):
                return (False, f"reg-retry must be numeric, got: {value}")

    # Validate n-mhae-spi if present
    if "n-mhae-spi" in payload:
        value = payload.get("n-mhae-spi")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "n-mhae-spi must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (False, f"n-mhae-spi must be numeric, got: {value}")

    # Validate n-mhae-key-type if present
    if "n-mhae-key-type" in payload:
        value = payload.get("n-mhae-key-type")
        if value and value not in VALID_BODY_N_MHAE_KEY_TYPE:
            return (
                False,
                f"Invalid n-mhae-key-type '{value}'. Must be one of: {', '.join(VALID_BODY_N_MHAE_KEY_TYPE)}",
            )

    # Validate hash-algorithm if present
    if "hash-algorithm" in payload:
        value = payload.get("hash-algorithm")
        if value and value not in VALID_BODY_HASH_ALGORITHM:
            return (
                False,
                f"Invalid hash-algorithm '{value}'. Must be one of: {', '.join(VALID_BODY_HASH_ALGORITHM)}",
            )

    # Validate tunnel-mode if present
    if "tunnel-mode" in payload:
        value = payload.get("tunnel-mode")
        if value and value not in VALID_BODY_TUNNEL_MODE:
            return (
                False,
                f"Invalid tunnel-mode '{value}'. Must be one of: {', '.join(VALID_BODY_TUNNEL_MODE)}",
            )

    return (True, None)


# ============================================================================
# DELETE Validation
# ============================================================================


def validate_mobile_tunnel_delete(
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
