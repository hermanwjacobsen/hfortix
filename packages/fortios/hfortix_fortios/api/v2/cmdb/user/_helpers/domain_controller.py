"""
Validation helpers for user domain_controller endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_AD_MODE = ["none", "ds", "lds"]
VALID_BODY_INTERFACE_SELECT_METHOD = ["auto", "sdwan", "specify"]
VALID_BODY_CHANGE_DETECTION = ["enable", "disable"]
VALID_BODY_DNS_SRV_LOOKUP = ["enable", "disable"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_domain_controller_get(
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


def validate_domain_controller_post(
    payload: dict[str, Any],
) -> tuple[bool, str | None]:
    """
    Validate POST request payload for creating domain_controller.

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

    # Validate ad-mode if present
    if "ad-mode" in payload:
        value = payload.get("ad-mode")
        if value and value not in VALID_BODY_AD_MODE:
            return (
                False,
                f"Invalid ad-mode '{value}'. Must be one of: {', '.join(VALID_BODY_AD_MODE)}",
            )

    # Validate hostname if present
    if "hostname" in payload:
        value = payload.get("hostname")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "hostname cannot exceed 255 characters")

    # Validate username if present
    if "username" in payload:
        value = payload.get("username")
        if value and isinstance(value, str) and len(value) > 64:
            return (False, "username cannot exceed 64 characters")

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

    # Validate source-port if present
    if "source-port" in payload:
        value = payload.get("source-port")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 65535:
                    return (False, "source-port must be between 0 and 65535")
            except (ValueError, TypeError):
                return (False, f"source-port must be numeric, got: {value}")

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

    # Validate domain-name if present
    if "domain-name" in payload:
        value = payload.get("domain-name")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "domain-name cannot exceed 255 characters")

    # Validate replication-port if present
    if "replication-port" in payload:
        value = payload.get("replication-port")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 65535:
                    return (
                        False,
                        "replication-port must be between 0 and 65535",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"replication-port must be numeric, got: {value}",
                )

    # Validate change-detection if present
    if "change-detection" in payload:
        value = payload.get("change-detection")
        if value and value not in VALID_BODY_CHANGE_DETECTION:
            return (
                False,
                f"Invalid change-detection '{value}'. Must be one of: {', '.join(VALID_BODY_CHANGE_DETECTION)}",
            )

    # Validate change-detection-period if present
    if "change-detection-period" in payload:
        value = payload.get("change-detection-period")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 5 or int_val > 10080:
                    return (
                        False,
                        "change-detection-period must be between 5 and 10080",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"change-detection-period must be numeric, got: {value}",
                )

    # Validate dns-srv-lookup if present
    if "dns-srv-lookup" in payload:
        value = payload.get("dns-srv-lookup")
        if value and value not in VALID_BODY_DNS_SRV_LOOKUP:
            return (
                False,
                f"Invalid dns-srv-lookup '{value}'. Must be one of: {', '.join(VALID_BODY_DNS_SRV_LOOKUP)}",
            )

    # Validate adlds-dn if present
    if "adlds-dn" in payload:
        value = payload.get("adlds-dn")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "adlds-dn cannot exceed 255 characters")

    # Validate adlds-port if present
    if "adlds-port" in payload:
        value = payload.get("adlds-port")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 65535:
                    return (False, "adlds-port must be between 0 and 65535")
            except (ValueError, TypeError):
                return (False, f"adlds-port must be numeric, got: {value}")

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_domain_controller_put(
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

    # Validate ad-mode if present
    if "ad-mode" in payload:
        value = payload.get("ad-mode")
        if value and value not in VALID_BODY_AD_MODE:
            return (
                False,
                f"Invalid ad-mode '{value}'. Must be one of: {', '.join(VALID_BODY_AD_MODE)}",
            )

    # Validate hostname if present
    if "hostname" in payload:
        value = payload.get("hostname")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "hostname cannot exceed 255 characters")

    # Validate username if present
    if "username" in payload:
        value = payload.get("username")
        if value and isinstance(value, str) and len(value) > 64:
            return (False, "username cannot exceed 64 characters")

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

    # Validate source-port if present
    if "source-port" in payload:
        value = payload.get("source-port")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 65535:
                    return (False, "source-port must be between 0 and 65535")
            except (ValueError, TypeError):
                return (False, f"source-port must be numeric, got: {value}")

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

    # Validate domain-name if present
    if "domain-name" in payload:
        value = payload.get("domain-name")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "domain-name cannot exceed 255 characters")

    # Validate replication-port if present
    if "replication-port" in payload:
        value = payload.get("replication-port")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 65535:
                    return (
                        False,
                        "replication-port must be between 0 and 65535",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"replication-port must be numeric, got: {value}",
                )

    # Validate change-detection if present
    if "change-detection" in payload:
        value = payload.get("change-detection")
        if value and value not in VALID_BODY_CHANGE_DETECTION:
            return (
                False,
                f"Invalid change-detection '{value}'. Must be one of: {', '.join(VALID_BODY_CHANGE_DETECTION)}",
            )

    # Validate change-detection-period if present
    if "change-detection-period" in payload:
        value = payload.get("change-detection-period")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 5 or int_val > 10080:
                    return (
                        False,
                        "change-detection-period must be between 5 and 10080",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"change-detection-period must be numeric, got: {value}",
                )

    # Validate dns-srv-lookup if present
    if "dns-srv-lookup" in payload:
        value = payload.get("dns-srv-lookup")
        if value and value not in VALID_BODY_DNS_SRV_LOOKUP:
            return (
                False,
                f"Invalid dns-srv-lookup '{value}'. Must be one of: {', '.join(VALID_BODY_DNS_SRV_LOOKUP)}",
            )

    # Validate adlds-dn if present
    if "adlds-dn" in payload:
        value = payload.get("adlds-dn")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "adlds-dn cannot exceed 255 characters")

    # Validate adlds-port if present
    if "adlds-port" in payload:
        value = payload.get("adlds-port")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 65535:
                    return (False, "adlds-port must be between 0 and 65535")
            except (ValueError, TypeError):
                return (False, f"adlds-port must be numeric, got: {value}")

    return (True, None)


# ============================================================================
# DELETE Validation
# ============================================================================


def validate_domain_controller_delete(
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
