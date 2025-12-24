"""
Validation helpers for system csf endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_STATUS = ["enable", "disable"]
VALID_BODY_UPSTREAM_INTERFACE_SELECT_METHOD = ["auto", "sdwan", "specify"]
VALID_BODY_ACCEPT_AUTH_BY_CERT = ["disable", "enable"]
VALID_BODY_LOG_UNIFICATION = ["disable", "enable"]
VALID_BODY_AUTHORIZATION_REQUEST_TYPE = ["serial", "certificate"]
VALID_BODY_DOWNSTREAM_ACCESS = ["enable", "disable"]
VALID_BODY_LEGACY_AUTHENTICATION = ["disable", "enable"]
VALID_BODY_CONFIGURATION_SYNC = ["default", "local"]
VALID_BODY_FABRIC_OBJECT_UNIFICATION = ["default", "local"]
VALID_BODY_SAML_CONFIGURATION_SYNC = ["default", "local"]
VALID_BODY_FORTICLOUD_ACCOUNT_ENFORCEMENT = ["enable", "disable"]
VALID_BODY_FILE_MGMT = ["enable", "disable"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_csf_get(
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


def validate_csf_put(
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

    # Validate status if present
    if "status" in payload:
        value = payload.get("status")
        if value and value not in VALID_BODY_STATUS:
            return (
                False,
                f"Invalid status '{value}'. Must be one of: {', '.join(VALID_BODY_STATUS)}",
            )

    # Validate uid if present
    if "uid" in payload:
        value = payload.get("uid")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "uid cannot exceed 35 characters")

    # Validate upstream if present
    if "upstream" in payload:
        value = payload.get("upstream")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "upstream cannot exceed 255 characters")

    # Validate upstream-interface-select-method if present
    if "upstream-interface-select-method" in payload:
        value = payload.get("upstream-interface-select-method")
        if value and value not in VALID_BODY_UPSTREAM_INTERFACE_SELECT_METHOD:
            return (
                False,
                f"Invalid upstream-interface-select-method '{value}'. Must be one of: {', '.join(VALID_BODY_UPSTREAM_INTERFACE_SELECT_METHOD)}",
            )

    # Validate upstream-interface if present
    if "upstream-interface" in payload:
        value = payload.get("upstream-interface")
        if value and isinstance(value, str) and len(value) > 15:
            return (False, "upstream-interface cannot exceed 15 characters")

    # Validate upstream-port if present
    if "upstream-port" in payload:
        value = payload.get("upstream-port")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 65535:
                    return (
                        False,
                        "upstream-port must be between 1 and 65535",
                    )
            except (ValueError, TypeError):
                return (False, f"upstream-port must be numeric, got: {value}")

    # Validate group-name if present
    if "group-name" in payload:
        value = payload.get("group-name")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "group-name cannot exceed 35 characters")

    # Validate accept-auth-by-cert if present
    if "accept-auth-by-cert" in payload:
        value = payload.get("accept-auth-by-cert")
        if value and value not in VALID_BODY_ACCEPT_AUTH_BY_CERT:
            return (
                False,
                f"Invalid accept-auth-by-cert '{value}'. Must be one of: {', '.join(VALID_BODY_ACCEPT_AUTH_BY_CERT)}",
            )

    # Validate log-unification if present
    if "log-unification" in payload:
        value = payload.get("log-unification")
        if value and value not in VALID_BODY_LOG_UNIFICATION:
            return (
                False,
                f"Invalid log-unification '{value}'. Must be one of: {', '.join(VALID_BODY_LOG_UNIFICATION)}",
            )

    # Validate authorization-request-type if present
    if "authorization-request-type" in payload:
        value = payload.get("authorization-request-type")
        if value and value not in VALID_BODY_AUTHORIZATION_REQUEST_TYPE:
            return (
                False,
                f"Invalid authorization-request-type '{value}'. Must be one of: {', '.join(VALID_BODY_AUTHORIZATION_REQUEST_TYPE)}",
            )

    # Validate certificate if present
    if "certificate" in payload:
        value = payload.get("certificate")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "certificate cannot exceed 35 characters")

    # Validate fabric-workers if present
    if "fabric-workers" in payload:
        value = payload.get("fabric-workers")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 4:
                    return (False, "fabric-workers must be between 1 and 4")
            except (ValueError, TypeError):
                return (False, f"fabric-workers must be numeric, got: {value}")

    # Validate downstream-access if present
    if "downstream-access" in payload:
        value = payload.get("downstream-access")
        if value and value not in VALID_BODY_DOWNSTREAM_ACCESS:
            return (
                False,
                f"Invalid downstream-access '{value}'. Must be one of: {', '.join(VALID_BODY_DOWNSTREAM_ACCESS)}",
            )

    # Validate legacy-authentication if present
    if "legacy-authentication" in payload:
        value = payload.get("legacy-authentication")
        if value and value not in VALID_BODY_LEGACY_AUTHENTICATION:
            return (
                False,
                f"Invalid legacy-authentication '{value}'. Must be one of: {', '.join(VALID_BODY_LEGACY_AUTHENTICATION)}",
            )

    # Validate downstream-accprofile if present
    if "downstream-accprofile" in payload:
        value = payload.get("downstream-accprofile")
        if value and isinstance(value, str) and len(value) > 35:
            return (
                False,
                "downstream-accprofile cannot exceed 35 characters",
            )

    # Validate configuration-sync if present
    if "configuration-sync" in payload:
        value = payload.get("configuration-sync")
        if value and value not in VALID_BODY_CONFIGURATION_SYNC:
            return (
                False,
                f"Invalid configuration-sync '{value}'. Must be one of: {', '.join(VALID_BODY_CONFIGURATION_SYNC)}",
            )

    # Validate fabric-object-unification if present
    if "fabric-object-unification" in payload:
        value = payload.get("fabric-object-unification")
        if value and value not in VALID_BODY_FABRIC_OBJECT_UNIFICATION:
            return (
                False,
                f"Invalid fabric-object-unification '{value}'. Must be one of: {', '.join(VALID_BODY_FABRIC_OBJECT_UNIFICATION)}",
            )

    # Validate saml-configuration-sync if present
    if "saml-configuration-sync" in payload:
        value = payload.get("saml-configuration-sync")
        if value and value not in VALID_BODY_SAML_CONFIGURATION_SYNC:
            return (
                False,
                f"Invalid saml-configuration-sync '{value}'. Must be one of: {', '.join(VALID_BODY_SAML_CONFIGURATION_SYNC)}",
            )

    # Validate forticloud-account-enforcement if present
    if "forticloud-account-enforcement" in payload:
        value = payload.get("forticloud-account-enforcement")
        if value and value not in VALID_BODY_FORTICLOUD_ACCOUNT_ENFORCEMENT:
            return (
                False,
                f"Invalid forticloud-account-enforcement '{value}'. Must be one of: {', '.join(VALID_BODY_FORTICLOUD_ACCOUNT_ENFORCEMENT)}",
            )

    # Validate file-mgmt if present
    if "file-mgmt" in payload:
        value = payload.get("file-mgmt")
        if value and value not in VALID_BODY_FILE_MGMT:
            return (
                False,
                f"Invalid file-mgmt '{value}'. Must be one of: {', '.join(VALID_BODY_FILE_MGMT)}",
            )

    # Validate file-quota if present
    if "file-quota" in payload:
        value = payload.get("file-quota")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "file-quota must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (False, f"file-quota must be numeric, got: {value}")

    # Validate file-quota-warning if present
    if "file-quota-warning" in payload:
        value = payload.get("file-quota-warning")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 99:
                    return (
                        False,
                        "file-quota-warning must be between 1 and 99",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"file-quota-warning must be numeric, got: {value}",
                )

    return (True, None)
