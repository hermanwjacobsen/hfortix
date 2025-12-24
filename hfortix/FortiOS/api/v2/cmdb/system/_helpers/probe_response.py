"""
Validation helpers for system probe_response endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_TTL_MODE = ["reinit", "decrease", "retain"]
VALID_BODY_MODE = ["none", "http-probe", "twamp"]
VALID_BODY_SECURITY_MODE = ["none", "authentication"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_probe_response_get(
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


def validate_probe_response_put(
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

    # Validate port if present
    if "port" in payload:
        value = payload.get("port")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 65535:
                    return (False, "port must be between 1 and 65535")
            except (ValueError, TypeError):
                return (False, f"port must be numeric, got: {value}")

    # Validate http-probe-value if present
    if "http-probe-value" in payload:
        value = payload.get("http-probe-value")
        if value and isinstance(value, str) and len(value) > 1024:
            return (False, "http-probe-value cannot exceed 1024 characters")

    # Validate ttl-mode if present
    if "ttl-mode" in payload:
        value = payload.get("ttl-mode")
        if value and value not in VALID_BODY_TTL_MODE:
            return (
                False,
                f"Invalid ttl-mode '{value}'. Must be one of: {', '.join(VALID_BODY_TTL_MODE)}",
            )

    # Validate mode if present
    if "mode" in payload:
        value = payload.get("mode")
        if value and value not in VALID_BODY_MODE:
            return (
                False,
                f"Invalid mode '{value}'. Must be one of: {', '.join(VALID_BODY_MODE)}",
            )

    # Validate security-mode if present
    if "security-mode" in payload:
        value = payload.get("security-mode")
        if value and value not in VALID_BODY_SECURITY_MODE:
            return (
                False,
                f"Invalid security-mode '{value}'. Must be one of: {', '.join(VALID_BODY_SECURITY_MODE)}",
            )

    # Validate timeout if present
    if "timeout" in payload:
        value = payload.get("timeout")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 10 or int_val > 3600:
                    return (False, "timeout must be between 10 and 3600")
            except (ValueError, TypeError):
                return (False, f"timeout must be numeric, got: {value}")

    return (True, None)
