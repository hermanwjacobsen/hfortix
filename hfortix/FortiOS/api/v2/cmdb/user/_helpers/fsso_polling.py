"""
Validation helpers for user fsso_polling endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_STATUS = ["enable", "disable"]
VALID_BODY_SMBV1 = ["enable", "disable"]
VALID_BODY_SMB_NTLMV1_AUTH = ["enable", "disable"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_fsso_polling_get(
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


def validate_fsso_polling_post(
    payload: dict[str, Any],
) -> tuple[bool, str | None]:
    """
    Validate POST request payload for creating fsso_polling.

    Args:
        payload: The payload to validate

    Returns:
        Tuple of (is_valid, error_message)
    """
    # Validate id if present
    if "id" in payload:
        value = payload.get("id")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (False, "id must be between 0 and 4294967295")
            except (ValueError, TypeError):
                return (False, f"id must be numeric, got: {value}")

    # Validate status if present
    if "status" in payload:
        value = payload.get("status")
        if value and value not in VALID_BODY_STATUS:
            return (
                False,
                f"Invalid status '{value}'. Must be one of: {', '.join(VALID_BODY_STATUS)}",
            )

    # Validate server if present
    if "server" in payload:
        value = payload.get("server")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "server cannot exceed 63 characters")

    # Validate default-domain if present
    if "default-domain" in payload:
        value = payload.get("default-domain")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "default-domain cannot exceed 35 characters")

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

    # Validate user if present
    if "user" in payload:
        value = payload.get("user")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "user cannot exceed 35 characters")

    # Validate ldap-server if present
    if "ldap-server" in payload:
        value = payload.get("ldap-server")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "ldap-server cannot exceed 35 characters")

    # Validate logon-history if present
    if "logon-history" in payload:
        value = payload.get("logon-history")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 48:
                    return (False, "logon-history must be between 0 and 48")
            except (ValueError, TypeError):
                return (False, f"logon-history must be numeric, got: {value}")

    # Validate polling-frequency if present
    if "polling-frequency" in payload:
        value = payload.get("polling-frequency")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 30:
                    return (
                        False,
                        "polling-frequency must be between 1 and 30",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"polling-frequency must be numeric, got: {value}",
                )

    # Validate smbv1 if present
    if "smbv1" in payload:
        value = payload.get("smbv1")
        if value and value not in VALID_BODY_SMBV1:
            return (
                False,
                f"Invalid smbv1 '{value}'. Must be one of: {', '.join(VALID_BODY_SMBV1)}",
            )

    # Validate smb-ntlmv1-auth if present
    if "smb-ntlmv1-auth" in payload:
        value = payload.get("smb-ntlmv1-auth")
        if value and value not in VALID_BODY_SMB_NTLMV1_AUTH:
            return (
                False,
                f"Invalid smb-ntlmv1-auth '{value}'. Must be one of: {', '.join(VALID_BODY_SMB_NTLMV1_AUTH)}",
            )

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_fsso_polling_put(
    id: str | None = None, payload: dict[str, Any] | None = None
) -> tuple[bool, str | None]:
    """
    Validate PUT request payload for updating {endpoint_name}.

    Args:
        id: Object identifier (required)
        payload: The payload to validate

    Returns:
        Tuple of (is_valid, error_message)
    """
    # id is required for updates
    if not id:
        return (False, "id is required for PUT operation")

    # If no payload provided, nothing to validate
    if not payload:
        return (True, None)

    # Validate id if present
    if "id" in payload:
        value = payload.get("id")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (False, "id must be between 0 and 4294967295")
            except (ValueError, TypeError):
                return (False, f"id must be numeric, got: {value}")

    # Validate status if present
    if "status" in payload:
        value = payload.get("status")
        if value and value not in VALID_BODY_STATUS:
            return (
                False,
                f"Invalid status '{value}'. Must be one of: {', '.join(VALID_BODY_STATUS)}",
            )

    # Validate server if present
    if "server" in payload:
        value = payload.get("server")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "server cannot exceed 63 characters")

    # Validate default-domain if present
    if "default-domain" in payload:
        value = payload.get("default-domain")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "default-domain cannot exceed 35 characters")

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

    # Validate user if present
    if "user" in payload:
        value = payload.get("user")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "user cannot exceed 35 characters")

    # Validate ldap-server if present
    if "ldap-server" in payload:
        value = payload.get("ldap-server")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "ldap-server cannot exceed 35 characters")

    # Validate logon-history if present
    if "logon-history" in payload:
        value = payload.get("logon-history")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 48:
                    return (False, "logon-history must be between 0 and 48")
            except (ValueError, TypeError):
                return (False, f"logon-history must be numeric, got: {value}")

    # Validate polling-frequency if present
    if "polling-frequency" in payload:
        value = payload.get("polling-frequency")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 30:
                    return (
                        False,
                        "polling-frequency must be between 1 and 30",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"polling-frequency must be numeric, got: {value}",
                )

    # Validate smbv1 if present
    if "smbv1" in payload:
        value = payload.get("smbv1")
        if value and value not in VALID_BODY_SMBV1:
            return (
                False,
                f"Invalid smbv1 '{value}'. Must be one of: {', '.join(VALID_BODY_SMBV1)}",
            )

    # Validate smb-ntlmv1-auth if present
    if "smb-ntlmv1-auth" in payload:
        value = payload.get("smb-ntlmv1-auth")
        if value and value not in VALID_BODY_SMB_NTLMV1_AUTH:
            return (
                False,
                f"Invalid smb-ntlmv1-auth '{value}'. Must be one of: {', '.join(VALID_BODY_SMB_NTLMV1_AUTH)}",
            )

    return (True, None)


# ============================================================================
# DELETE Validation
# ============================================================================


def validate_fsso_polling_delete(
    id: str | None = None,
) -> tuple[bool, str | None]:
    """
    Validate DELETE request parameters.

    Args:
        id: Object identifier (required)

    Returns:
        Tuple of (is_valid, error_message)
    """
    if not id:
        return (False, "id is required for DELETE operation")

    return (True, None)
