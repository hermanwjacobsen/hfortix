"""
Validation helpers for system dns endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_PROTOCOL = ["cleartext", "dot", "doh"]
VALID_BODY_CACHE_NOTFOUND_RESPONSES = ["disable", "enable"]
VALID_BODY_INTERFACE_SELECT_METHOD = ["auto", "sdwan", "specify"]
VALID_BODY_SERVER_SELECT_METHOD = ["least-rtt", "failover"]
VALID_BODY_LOG = ["disable", "error", "all"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_dns_get(
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


def validate_dns_put(
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

    # Validate protocol if present
    if "protocol" in payload:
        value = payload.get("protocol")
        if value and value not in VALID_BODY_PROTOCOL:
            return (
                False,
                f"Invalid protocol '{value}'. Must be one of: {', '.join(VALID_BODY_PROTOCOL)}",
            )

    # Validate ssl-certificate if present
    if "ssl-certificate" in payload:
        value = payload.get("ssl-certificate")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "ssl-certificate cannot exceed 35 characters")

    # Validate timeout if present
    if "timeout" in payload:
        value = payload.get("timeout")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 10:
                    return (False, "timeout must be between 1 and 10")
            except (ValueError, TypeError):
                return (False, f"timeout must be numeric, got: {value}")

    # Validate retry if present
    if "retry" in payload:
        value = payload.get("retry")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 5:
                    return (False, "retry must be between 0 and 5")
            except (ValueError, TypeError):
                return (False, f"retry must be numeric, got: {value}")

    # Validate dns-cache-limit if present
    if "dns-cache-limit" in payload:
        value = payload.get("dns-cache-limit")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "dns-cache-limit must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"dns-cache-limit must be numeric, got: {value}",
                )

    # Validate dns-cache-ttl if present
    if "dns-cache-ttl" in payload:
        value = payload.get("dns-cache-ttl")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 60 or int_val > 86400:
                    return (
                        False,
                        "dns-cache-ttl must be between 60 and 86400",
                    )
            except (ValueError, TypeError):
                return (False, f"dns-cache-ttl must be numeric, got: {value}")

    # Validate cache-notfound-responses if present
    if "cache-notfound-responses" in payload:
        value = payload.get("cache-notfound-responses")
        if value and value not in VALID_BODY_CACHE_NOTFOUND_RESPONSES:
            return (
                False,
                f"Invalid cache-notfound-responses '{value}'. Must be one of: {', '.join(VALID_BODY_CACHE_NOTFOUND_RESPONSES)}",
            )

    # Validate source-ip-interface if present
    if "source-ip-interface" in payload:
        value = payload.get("source-ip-interface")
        if value and isinstance(value, str) and len(value) > 15:
            return (False, "source-ip-interface cannot exceed 15 characters")

    # Validate interface-select-method if present
    if "interface-select-method" in payload:
        value = payload.get("interface-select-method")
        if value and value not in VALID_BODY_INTERFACE_SELECT_METHOD:
            return (
                False,
                f"Invalid interface-select-method '{value}'. Must be one of: {', '.join(VALID_BODY_INTERFACE_SELECT_METHOD)}",
            )

    # Validate interface if present
    if "interface" in payload:
        value = payload.get("interface")
        if value and isinstance(value, str) and len(value) > 15:
            return (False, "interface cannot exceed 15 characters")

    # Validate vrf-select if present
    if "vrf-select" in payload:
        value = payload.get("vrf-select")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 511:
                    return (False, "vrf-select must be between 0 and 511")
            except (ValueError, TypeError):
                return (False, f"vrf-select must be numeric, got: {value}")

    # Validate server-select-method if present
    if "server-select-method" in payload:
        value = payload.get("server-select-method")
        if value and value not in VALID_BODY_SERVER_SELECT_METHOD:
            return (
                False,
                f"Invalid server-select-method '{value}'. Must be one of: {', '.join(VALID_BODY_SERVER_SELECT_METHOD)}",
            )

    # Validate log if present
    if "log" in payload:
        value = payload.get("log")
        if value and value not in VALID_BODY_LOG:
            return (
                False,
                f"Invalid log '{value}'. Must be one of: {', '.join(VALID_BODY_LOG)}",
            )

    # Validate fqdn-cache-ttl if present
    if "fqdn-cache-ttl" in payload:
        value = payload.get("fqdn-cache-ttl")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 86400:
                    return (
                        False,
                        "fqdn-cache-ttl must be between 0 and 86400",
                    )
            except (ValueError, TypeError):
                return (False, f"fqdn-cache-ttl must be numeric, got: {value}")

    # Validate fqdn-max-refresh if present
    if "fqdn-max-refresh" in payload:
        value = payload.get("fqdn-max-refresh")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 3600 or int_val > 86400:
                    return (
                        False,
                        "fqdn-max-refresh must be between 3600 and 86400",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"fqdn-max-refresh must be numeric, got: {value}",
                )

    # Validate fqdn-min-refresh if present
    if "fqdn-min-refresh" in payload:
        value = payload.get("fqdn-min-refresh")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 10 or int_val > 3600:
                    return (
                        False,
                        "fqdn-min-refresh must be between 10 and 3600",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"fqdn-min-refresh must be numeric, got: {value}",
                )

    # Validate hostname-ttl if present
    if "hostname-ttl" in payload:
        value = payload.get("hostname-ttl")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 60 or int_val > 86400:
                    return (
                        False,
                        "hostname-ttl must be between 60 and 86400",
                    )
            except (ValueError, TypeError):
                return (False, f"hostname-ttl must be numeric, got: {value}")

    # Validate hostname-limit if present
    if "hostname-limit" in payload:
        value = payload.get("hostname-limit")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 50000:
                    return (
                        False,
                        "hostname-limit must be between 0 and 50000",
                    )
            except (ValueError, TypeError):
                return (False, f"hostname-limit must be numeric, got: {value}")

    return (True, None)
