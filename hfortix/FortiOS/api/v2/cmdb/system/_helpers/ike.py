"""
Validation helpers for system ike endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_DH_MULTIPROCESS = ["enable", "disable"]
VALID_BODY_DH_MODE = ["software", "hardware"]
VALID_BODY_DH_KEYPAIR_CACHE = ["enable", "disable"]
VALID_BODY_DH_KEYPAIR_THROTTLE = ["enable", "disable"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_ike_get(
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


def validate_ike_put(
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

    # Validate embryonic-limit if present
    if "embryonic-limit" in payload:
        value = payload.get("embryonic-limit")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 50 or int_val > 20000:
                    return (
                        False,
                        "embryonic-limit must be between 50 and 20000",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"embryonic-limit must be numeric, got: {value}",
                )

    # Validate dh-multiprocess if present
    if "dh-multiprocess" in payload:
        value = payload.get("dh-multiprocess")
        if value and value not in VALID_BODY_DH_MULTIPROCESS:
            return (
                False,
                f"Invalid dh-multiprocess '{value}'. Must be one of: {', '.join(VALID_BODY_DH_MULTIPROCESS)}",
            )

    # Validate dh-worker-count if present
    if "dh-worker-count" in payload:
        value = payload.get("dh-worker-count")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 8:
                    return (False, "dh-worker-count must be between 1 and 8")
            except (ValueError, TypeError):
                return (
                    False,
                    f"dh-worker-count must be numeric, got: {value}",
                )

    # Validate dh-mode if present
    if "dh-mode" in payload:
        value = payload.get("dh-mode")
        if value and value not in VALID_BODY_DH_MODE:
            return (
                False,
                f"Invalid dh-mode '{value}'. Must be one of: {', '.join(VALID_BODY_DH_MODE)}",
            )

    # Validate dh-keypair-cache if present
    if "dh-keypair-cache" in payload:
        value = payload.get("dh-keypair-cache")
        if value and value not in VALID_BODY_DH_KEYPAIR_CACHE:
            return (
                False,
                f"Invalid dh-keypair-cache '{value}'. Must be one of: {', '.join(VALID_BODY_DH_KEYPAIR_CACHE)}",
            )

    # Validate dh-keypair-count if present
    if "dh-keypair-count" in payload:
        value = payload.get("dh-keypair-count")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 50000:
                    return (
                        False,
                        "dh-keypair-count must be between 0 and 50000",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"dh-keypair-count must be numeric, got: {value}",
                )

    # Validate dh-keypair-throttle if present
    if "dh-keypair-throttle" in payload:
        value = payload.get("dh-keypair-throttle")
        if value and value not in VALID_BODY_DH_KEYPAIR_THROTTLE:
            return (
                False,
                f"Invalid dh-keypair-throttle '{value}'. Must be one of: {', '.join(VALID_BODY_DH_KEYPAIR_THROTTLE)}",
            )

    return (True, None)
