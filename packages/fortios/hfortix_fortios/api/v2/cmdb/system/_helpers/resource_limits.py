"""
Validation helpers for system resource_limits endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_resource_limits_get(
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


def validate_resource_limits_put(
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

    # Validate session if present
    if "session" in payload:
        value = payload.get("session")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (False, "session must be between 0 and 4294967295")
            except (ValueError, TypeError):
                return (False, f"session must be numeric, got: {value}")

    # Validate ipsec-phase1 if present
    if "ipsec-phase1" in payload:
        value = payload.get("ipsec-phase1")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "ipsec-phase1 must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (False, f"ipsec-phase1 must be numeric, got: {value}")

    # Validate ipsec-phase2 if present
    if "ipsec-phase2" in payload:
        value = payload.get("ipsec-phase2")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "ipsec-phase2 must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (False, f"ipsec-phase2 must be numeric, got: {value}")

    # Validate ipsec-phase1-interface if present
    if "ipsec-phase1-interface" in payload:
        value = payload.get("ipsec-phase1-interface")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "ipsec-phase1-interface must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"ipsec-phase1-interface must be numeric, got: {value}",
                )

    # Validate ipsec-phase2-interface if present
    if "ipsec-phase2-interface" in payload:
        value = payload.get("ipsec-phase2-interface")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "ipsec-phase2-interface must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"ipsec-phase2-interface must be numeric, got: {value}",
                )

    # Validate dialup-tunnel if present
    if "dialup-tunnel" in payload:
        value = payload.get("dialup-tunnel")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "dialup-tunnel must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (False, f"dialup-tunnel must be numeric, got: {value}")

    # Validate firewall-policy if present
    if "firewall-policy" in payload:
        value = payload.get("firewall-policy")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "firewall-policy must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"firewall-policy must be numeric, got: {value}",
                )

    # Validate firewall-address if present
    if "firewall-address" in payload:
        value = payload.get("firewall-address")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "firewall-address must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"firewall-address must be numeric, got: {value}",
                )

    # Validate firewall-addrgrp if present
    if "firewall-addrgrp" in payload:
        value = payload.get("firewall-addrgrp")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "firewall-addrgrp must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"firewall-addrgrp must be numeric, got: {value}",
                )

    # Validate custom-service if present
    if "custom-service" in payload:
        value = payload.get("custom-service")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "custom-service must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (False, f"custom-service must be numeric, got: {value}")

    # Validate service-group if present
    if "service-group" in payload:
        value = payload.get("service-group")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "service-group must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (False, f"service-group must be numeric, got: {value}")

    # Validate onetime-schedule if present
    if "onetime-schedule" in payload:
        value = payload.get("onetime-schedule")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "onetime-schedule must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"onetime-schedule must be numeric, got: {value}",
                )

    # Validate recurring-schedule if present
    if "recurring-schedule" in payload:
        value = payload.get("recurring-schedule")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "recurring-schedule must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"recurring-schedule must be numeric, got: {value}",
                )

    # Validate user if present
    if "user" in payload:
        value = payload.get("user")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (False, "user must be between 0 and 4294967295")
            except (ValueError, TypeError):
                return (False, f"user must be numeric, got: {value}")

    # Validate user-group if present
    if "user-group" in payload:
        value = payload.get("user-group")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "user-group must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (False, f"user-group must be numeric, got: {value}")

    # Validate log-disk-quota if present
    if "log-disk-quota" in payload:
        value = payload.get("log-disk-quota")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "log-disk-quota must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (False, f"log-disk-quota must be numeric, got: {value}")

    return (True, None)
