"""
Validation helpers for user local endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_STATUS = ["enable", "disable"]
VALID_BODY_TYPE = ["password", "radius", "tacacs+", "ldap", "saml"]
VALID_BODY_TWO_FACTOR = [
    "disable",
    "fortitoken",
    "fortitoken-cloud",
    "email",
    "sms",
]
VALID_BODY_TWO_FACTOR_AUTHENTICATION = ["fortitoken", "email", "sms"]
VALID_BODY_TWO_FACTOR_NOTIFICATION = ["email", "sms"]
VALID_BODY_SMS_SERVER = ["fortiguard", "custom"]
VALID_BODY_AUTH_CONCURRENT_OVERRIDE = ["enable", "disable"]
VALID_BODY_USERNAME_SENSITIVITY = ["disable", "enable"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_local_get(
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


def validate_local_post(payload: dict[str, Any]) -> tuple[bool, str | None]:
    """
    Validate POST request payload for creating local.

    Args:
        payload: The payload to validate

    Returns:
        Tuple of (is_valid, error_message)
    """
    # Validate name if present
    if "name" in payload:
        value = payload.get("name")
        if value and isinstance(value, str) and len(value) > 64:
            return (False, "name cannot exceed 64 characters")

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

    # Validate type if present
    if "type" in payload:
        value = payload.get("type")
        if value and value not in VALID_BODY_TYPE:
            return (
                False,
                f"Invalid type '{value}'. Must be one of: {', '.join(VALID_BODY_TYPE)}",
            )

    # Validate ldap-server if present
    if "ldap-server" in payload:
        value = payload.get("ldap-server")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "ldap-server cannot exceed 35 characters")

    # Validate radius-server if present
    if "radius-server" in payload:
        value = payload.get("radius-server")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "radius-server cannot exceed 35 characters")

    # Validate tacacs+-server if present
    if "tacacs+-server" in payload:
        value = payload.get("tacacs+-server")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "tacacs+-server cannot exceed 35 characters")

    # Validate saml-server if present
    if "saml-server" in payload:
        value = payload.get("saml-server")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "saml-server cannot exceed 35 characters")

    # Validate two-factor if present
    if "two-factor" in payload:
        value = payload.get("two-factor")
        if value and value not in VALID_BODY_TWO_FACTOR:
            return (
                False,
                f"Invalid two-factor '{value}'. Must be one of: {', '.join(VALID_BODY_TWO_FACTOR)}",
            )

    # Validate two-factor-authentication if present
    if "two-factor-authentication" in payload:
        value = payload.get("two-factor-authentication")
        if value and value not in VALID_BODY_TWO_FACTOR_AUTHENTICATION:
            return (
                False,
                f"Invalid two-factor-authentication '{value}'. Must be one of: {', '.join(VALID_BODY_TWO_FACTOR_AUTHENTICATION)}",
            )

    # Validate two-factor-notification if present
    if "two-factor-notification" in payload:
        value = payload.get("two-factor-notification")
        if value and value not in VALID_BODY_TWO_FACTOR_NOTIFICATION:
            return (
                False,
                f"Invalid two-factor-notification '{value}'. Must be one of: {', '.join(VALID_BODY_TWO_FACTOR_NOTIFICATION)}",
            )

    # Validate fortitoken if present
    if "fortitoken" in payload:
        value = payload.get("fortitoken")
        if value and isinstance(value, str) and len(value) > 16:
            return (False, "fortitoken cannot exceed 16 characters")

    # Validate email-to if present
    if "email-to" in payload:
        value = payload.get("email-to")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "email-to cannot exceed 63 characters")

    # Validate sms-server if present
    if "sms-server" in payload:
        value = payload.get("sms-server")
        if value and value not in VALID_BODY_SMS_SERVER:
            return (
                False,
                f"Invalid sms-server '{value}'. Must be one of: {', '.join(VALID_BODY_SMS_SERVER)}",
            )

    # Validate sms-custom-server if present
    if "sms-custom-server" in payload:
        value = payload.get("sms-custom-server")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "sms-custom-server cannot exceed 35 characters")

    # Validate sms-phone if present
    if "sms-phone" in payload:
        value = payload.get("sms-phone")
        if value and isinstance(value, str) and len(value) > 15:
            return (False, "sms-phone cannot exceed 15 characters")

    # Validate passwd-policy if present
    if "passwd-policy" in payload:
        value = payload.get("passwd-policy")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "passwd-policy cannot exceed 35 characters")

    # Validate authtimeout if present
    if "authtimeout" in payload:
        value = payload.get("authtimeout")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 1440:
                    return (False, "authtimeout must be between 0 and 1440")
            except (ValueError, TypeError):
                return (False, f"authtimeout must be numeric, got: {value}")

    # Validate workstation if present
    if "workstation" in payload:
        value = payload.get("workstation")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "workstation cannot exceed 35 characters")

    # Validate auth-concurrent-override if present
    if "auth-concurrent-override" in payload:
        value = payload.get("auth-concurrent-override")
        if value and value not in VALID_BODY_AUTH_CONCURRENT_OVERRIDE:
            return (
                False,
                f"Invalid auth-concurrent-override '{value}'. Must be one of: {', '.join(VALID_BODY_AUTH_CONCURRENT_OVERRIDE)}",
            )

    # Validate auth-concurrent-value if present
    if "auth-concurrent-value" in payload:
        value = payload.get("auth-concurrent-value")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 100:
                    return (
                        False,
                        "auth-concurrent-value must be between 0 and 100",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"auth-concurrent-value must be numeric, got: {value}",
                )

    # Validate ppk-identity if present
    if "ppk-identity" in payload:
        value = payload.get("ppk-identity")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "ppk-identity cannot exceed 35 characters")

    # Validate qkd-profile if present
    if "qkd-profile" in payload:
        value = payload.get("qkd-profile")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "qkd-profile cannot exceed 35 characters")

    # Validate username-sensitivity if present
    if "username-sensitivity" in payload:
        value = payload.get("username-sensitivity")
        if value and value not in VALID_BODY_USERNAME_SENSITIVITY:
            return (
                False,
                f"Invalid username-sensitivity '{value}'. Must be one of: {', '.join(VALID_BODY_USERNAME_SENSITIVITY)}",
            )

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_local_put(
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
        if value and isinstance(value, str) and len(value) > 64:
            return (False, "name cannot exceed 64 characters")

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

    # Validate type if present
    if "type" in payload:
        value = payload.get("type")
        if value and value not in VALID_BODY_TYPE:
            return (
                False,
                f"Invalid type '{value}'. Must be one of: {', '.join(VALID_BODY_TYPE)}",
            )

    # Validate ldap-server if present
    if "ldap-server" in payload:
        value = payload.get("ldap-server")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "ldap-server cannot exceed 35 characters")

    # Validate radius-server if present
    if "radius-server" in payload:
        value = payload.get("radius-server")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "radius-server cannot exceed 35 characters")

    # Validate tacacs+-server if present
    if "tacacs+-server" in payload:
        value = payload.get("tacacs+-server")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "tacacs+-server cannot exceed 35 characters")

    # Validate saml-server if present
    if "saml-server" in payload:
        value = payload.get("saml-server")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "saml-server cannot exceed 35 characters")

    # Validate two-factor if present
    if "two-factor" in payload:
        value = payload.get("two-factor")
        if value and value not in VALID_BODY_TWO_FACTOR:
            return (
                False,
                f"Invalid two-factor '{value}'. Must be one of: {', '.join(VALID_BODY_TWO_FACTOR)}",
            )

    # Validate two-factor-authentication if present
    if "two-factor-authentication" in payload:
        value = payload.get("two-factor-authentication")
        if value and value not in VALID_BODY_TWO_FACTOR_AUTHENTICATION:
            return (
                False,
                f"Invalid two-factor-authentication '{value}'. Must be one of: {', '.join(VALID_BODY_TWO_FACTOR_AUTHENTICATION)}",
            )

    # Validate two-factor-notification if present
    if "two-factor-notification" in payload:
        value = payload.get("two-factor-notification")
        if value and value not in VALID_BODY_TWO_FACTOR_NOTIFICATION:
            return (
                False,
                f"Invalid two-factor-notification '{value}'. Must be one of: {', '.join(VALID_BODY_TWO_FACTOR_NOTIFICATION)}",
            )

    # Validate fortitoken if present
    if "fortitoken" in payload:
        value = payload.get("fortitoken")
        if value and isinstance(value, str) and len(value) > 16:
            return (False, "fortitoken cannot exceed 16 characters")

    # Validate email-to if present
    if "email-to" in payload:
        value = payload.get("email-to")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "email-to cannot exceed 63 characters")

    # Validate sms-server if present
    if "sms-server" in payload:
        value = payload.get("sms-server")
        if value and value not in VALID_BODY_SMS_SERVER:
            return (
                False,
                f"Invalid sms-server '{value}'. Must be one of: {', '.join(VALID_BODY_SMS_SERVER)}",
            )

    # Validate sms-custom-server if present
    if "sms-custom-server" in payload:
        value = payload.get("sms-custom-server")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "sms-custom-server cannot exceed 35 characters")

    # Validate sms-phone if present
    if "sms-phone" in payload:
        value = payload.get("sms-phone")
        if value and isinstance(value, str) and len(value) > 15:
            return (False, "sms-phone cannot exceed 15 characters")

    # Validate passwd-policy if present
    if "passwd-policy" in payload:
        value = payload.get("passwd-policy")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "passwd-policy cannot exceed 35 characters")

    # Validate authtimeout if present
    if "authtimeout" in payload:
        value = payload.get("authtimeout")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 1440:
                    return (False, "authtimeout must be between 0 and 1440")
            except (ValueError, TypeError):
                return (False, f"authtimeout must be numeric, got: {value}")

    # Validate workstation if present
    if "workstation" in payload:
        value = payload.get("workstation")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "workstation cannot exceed 35 characters")

    # Validate auth-concurrent-override if present
    if "auth-concurrent-override" in payload:
        value = payload.get("auth-concurrent-override")
        if value and value not in VALID_BODY_AUTH_CONCURRENT_OVERRIDE:
            return (
                False,
                f"Invalid auth-concurrent-override '{value}'. Must be one of: {', '.join(VALID_BODY_AUTH_CONCURRENT_OVERRIDE)}",
            )

    # Validate auth-concurrent-value if present
    if "auth-concurrent-value" in payload:
        value = payload.get("auth-concurrent-value")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 100:
                    return (
                        False,
                        "auth-concurrent-value must be between 0 and 100",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"auth-concurrent-value must be numeric, got: {value}",
                )

    # Validate ppk-identity if present
    if "ppk-identity" in payload:
        value = payload.get("ppk-identity")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "ppk-identity cannot exceed 35 characters")

    # Validate qkd-profile if present
    if "qkd-profile" in payload:
        value = payload.get("qkd-profile")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "qkd-profile cannot exceed 35 characters")

    # Validate username-sensitivity if present
    if "username-sensitivity" in payload:
        value = payload.get("username-sensitivity")
        if value and value not in VALID_BODY_USERNAME_SENSITIVITY:
            return (
                False,
                f"Invalid username-sensitivity '{value}'. Must be one of: {', '.join(VALID_BODY_USERNAME_SENSITIVITY)}",
            )

    return (True, None)


# ============================================================================
# DELETE Validation
# ============================================================================


def validate_local_delete(name: str | None = None) -> tuple[bool, str | None]:
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
