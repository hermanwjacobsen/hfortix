"""
Validation helpers for ips settings endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_PROXY_INLINE_IPS = ["disable", "enable"]
VALID_BODY_HA_SESSION_PICKUP = ["connectivity", "security"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_settings_get(
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


def validate_settings_put(
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

    # Validate packet-log-history if present
    if "packet-log-history" in payload:
        value = payload.get("packet-log-history")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 255:
                    return (
                        False,
                        "packet-log-history must be between 1 and 255",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"packet-log-history must be numeric, got: {value}",
                )

    # Validate packet-log-post-attack if present
    if "packet-log-post-attack" in payload:
        value = payload.get("packet-log-post-attack")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 255:
                    return (
                        False,
                        "packet-log-post-attack must be between 0 and 255",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"packet-log-post-attack must be numeric, got: {value}",
                )

    # Validate packet-log-memory if present
    if "packet-log-memory" in payload:
        value = payload.get("packet-log-memory")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 64 or int_val > 8192:
                    return (
                        False,
                        "packet-log-memory must be between 64 and 8192",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"packet-log-memory must be numeric, got: {value}",
                )

    # Validate ips-packet-quota if present
    if "ips-packet-quota" in payload:
        value = payload.get("ips-packet-quota")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "ips-packet-quota must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"ips-packet-quota must be numeric, got: {value}",
                )

    # Validate proxy-inline-ips if present
    if "proxy-inline-ips" in payload:
        value = payload.get("proxy-inline-ips")
        if value and value not in VALID_BODY_PROXY_INLINE_IPS:
            return (
                False,
                f"Invalid proxy-inline-ips '{value}'. Must be one of: {', '.join(VALID_BODY_PROXY_INLINE_IPS)}",
            )

    # Validate ha-session-pickup if present
    if "ha-session-pickup" in payload:
        value = payload.get("ha-session-pickup")
        if value and value not in VALID_BODY_HA_SESSION_PICKUP:
            return (
                False,
                f"Invalid ha-session-pickup '{value}'. Must be one of: {', '.join(VALID_BODY_HA_SESSION_PICKUP)}",
            )

    return (True, None)
