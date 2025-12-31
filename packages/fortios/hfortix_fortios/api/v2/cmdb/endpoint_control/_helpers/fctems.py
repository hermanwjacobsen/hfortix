"""
Validation helpers for endpoint-control fctems endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_STATUS = ["enable", "disable"]
VALID_BODY_DIRTY_REASON = ["none", "mismatched-ems-sn"]
VALID_BODY_FORTINETONE_CLOUD_AUTHENTICATION = ["enable", "disable"]
VALID_BODY_PULL_SYSINFO = ["enable", "disable"]
VALID_BODY_PULL_VULNERABILITIES = ["enable", "disable"]
VALID_BODY_PULL_TAGS = ["enable", "disable"]
VALID_BODY_PULL_MALWARE_HASH = ["enable", "disable"]
VALID_BODY_CAPABILITIES = [
    "fabric-auth",
    "silent-approval",
    "websocket",
    "websocket-malware",
    "push-ca-certs",
    "common-tags-api",
    "tenant-id",
    "client-avatars",
    "single-vdom-connector",
    "fgt-sysinfo-api",
    "ztna-server-info",
    "used-tags",
]
VALID_BODY_SEND_TAGS_TO_ALL_VDOMS = ["enable", "disable"]
VALID_BODY_WEBSOCKET_OVERRIDE = ["enable", "disable"]
VALID_BODY_INTERFACE_SELECT_METHOD = ["auto", "sdwan", "specify"]
VALID_BODY_TRUST_CA_CN = ["enable", "disable"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_fctems_get(
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


def validate_fctems_post(payload: dict[str, Any]) -> tuple[bool, str | None]:
    """
    Validate POST request payload for creating fctems.

    Args:
        payload: The payload to validate

    Returns:
        Tuple of (is_valid, error_message)
    """
    # Validate ems-id if present
    if "ems-id" in payload:
        value = payload.get("ems-id")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 7:
                    return (False, "ems-id must be between 1 and 7")
            except (ValueError, TypeError):
                return (False, f"ems-id must be numeric, got: {value}")

    # Validate status if present
    if "status" in payload:
        value = payload.get("status")
        if value and value not in VALID_BODY_STATUS:
            return (
                False,
                f"Invalid status '{value}'. Must be one of: {', '.join(VALID_BODY_STATUS)}",
            )

    # Validate name if present
    if "name" in payload:
        value = payload.get("name")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "name cannot exceed 35 characters")

    # Validate dirty-reason if present
    if "dirty-reason" in payload:
        value = payload.get("dirty-reason")
        if value and value not in VALID_BODY_DIRTY_REASON:
            return (
                False,
                f"Invalid dirty-reason '{value}'. Must be one of: {', '.join(VALID_BODY_DIRTY_REASON)}",
            )

    # Validate fortinetone-cloud-authentication if present
    if "fortinetone-cloud-authentication" in payload:
        value = payload.get("fortinetone-cloud-authentication")
        if value and value not in VALID_BODY_FORTINETONE_CLOUD_AUTHENTICATION:
            return (
                False,
                f"Invalid fortinetone-cloud-authentication '{value}'. Must be one of: {', '.join(VALID_BODY_FORTINETONE_CLOUD_AUTHENTICATION)}",
            )

    # Validate server if present
    if "server" in payload:
        value = payload.get("server")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "server cannot exceed 255 characters")

    # Validate https-port if present
    if "https-port" in payload:
        value = payload.get("https-port")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 65535:
                    return (False, "https-port must be between 1 and 65535")
            except (ValueError, TypeError):
                return (False, f"https-port must be numeric, got: {value}")

    # Validate serial-number if present
    if "serial-number" in payload:
        value = payload.get("serial-number")
        if value and isinstance(value, str) and len(value) > 16:
            return (False, "serial-number cannot exceed 16 characters")

    # Validate tenant-id if present
    if "tenant-id" in payload:
        value = payload.get("tenant-id")
        if value and isinstance(value, str) and len(value) > 32:
            return (False, "tenant-id cannot exceed 32 characters")

    # Validate pull-sysinfo if present
    if "pull-sysinfo" in payload:
        value = payload.get("pull-sysinfo")
        if value and value not in VALID_BODY_PULL_SYSINFO:
            return (
                False,
                f"Invalid pull-sysinfo '{value}'. Must be one of: {', '.join(VALID_BODY_PULL_SYSINFO)}",
            )

    # Validate pull-vulnerabilities if present
    if "pull-vulnerabilities" in payload:
        value = payload.get("pull-vulnerabilities")
        if value and value not in VALID_BODY_PULL_VULNERABILITIES:
            return (
                False,
                f"Invalid pull-vulnerabilities '{value}'. Must be one of: {', '.join(VALID_BODY_PULL_VULNERABILITIES)}",
            )

    # Validate pull-tags if present
    if "pull-tags" in payload:
        value = payload.get("pull-tags")
        if value and value not in VALID_BODY_PULL_TAGS:
            return (
                False,
                f"Invalid pull-tags '{value}'. Must be one of: {', '.join(VALID_BODY_PULL_TAGS)}",
            )

    # Validate pull-malware-hash if present
    if "pull-malware-hash" in payload:
        value = payload.get("pull-malware-hash")
        if value and value not in VALID_BODY_PULL_MALWARE_HASH:
            return (
                False,
                f"Invalid pull-malware-hash '{value}'. Must be one of: {', '.join(VALID_BODY_PULL_MALWARE_HASH)}",
            )

    # Validate capabilities if present
    if "capabilities" in payload:
        value = payload.get("capabilities")
        if value and value not in VALID_BODY_CAPABILITIES:
            return (
                False,
                f"Invalid capabilities '{value}'. Must be one of: {', '.join(VALID_BODY_CAPABILITIES)}",
            )

    # Validate call-timeout if present
    if "call-timeout" in payload:
        value = payload.get("call-timeout")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 180:
                    return (False, "call-timeout must be between 1 and 180")
            except (ValueError, TypeError):
                return (False, f"call-timeout must be numeric, got: {value}")

    # Validate out-of-sync-threshold if present
    if "out-of-sync-threshold" in payload:
        value = payload.get("out-of-sync-threshold")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 10 or int_val > 3600:
                    return (
                        False,
                        "out-of-sync-threshold must be between 10 and 3600",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"out-of-sync-threshold must be numeric, got: {value}",
                )

    # Validate send-tags-to-all-vdoms if present
    if "send-tags-to-all-vdoms" in payload:
        value = payload.get("send-tags-to-all-vdoms")
        if value and value not in VALID_BODY_SEND_TAGS_TO_ALL_VDOMS:
            return (
                False,
                f"Invalid send-tags-to-all-vdoms '{value}'. Must be one of: {', '.join(VALID_BODY_SEND_TAGS_TO_ALL_VDOMS)}",
            )

    # Validate websocket-override if present
    if "websocket-override" in payload:
        value = payload.get("websocket-override")
        if value and value not in VALID_BODY_WEBSOCKET_OVERRIDE:
            return (
                False,
                f"Invalid websocket-override '{value}'. Must be one of: {', '.join(VALID_BODY_WEBSOCKET_OVERRIDE)}",
            )

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

    # Validate trust-ca-cn if present
    if "trust-ca-cn" in payload:
        value = payload.get("trust-ca-cn")
        if value and value not in VALID_BODY_TRUST_CA_CN:
            return (
                False,
                f"Invalid trust-ca-cn '{value}'. Must be one of: {', '.join(VALID_BODY_TRUST_CA_CN)}",
            )

    # Validate verifying-ca if present
    if "verifying-ca" in payload:
        value = payload.get("verifying-ca")
        if value and isinstance(value, str) and len(value) > 79:
            return (False, "verifying-ca cannot exceed 79 characters")

    return (True, None)
