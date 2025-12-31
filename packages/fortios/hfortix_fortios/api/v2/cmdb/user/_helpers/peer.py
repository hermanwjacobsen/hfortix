"""
Validation helpers for user peer endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_MANDATORY_CA_VERIFY = ["enable", "disable"]
VALID_BODY_CN_TYPE = ["string", "email", "FQDN", "ipv4", "ipv6"]
VALID_BODY_MFA_MODE = ["none", "password", "subject-identity"]
VALID_BODY_TWO_FACTOR = ["enable", "disable"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_peer_get(
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


def validate_peer_post(payload: dict[str, Any]) -> tuple[bool, str | None]:
    """
    Validate POST request payload for creating peer.

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

    # Validate mandatory-ca-verify if present
    if "mandatory-ca-verify" in payload:
        value = payload.get("mandatory-ca-verify")
        if value and value not in VALID_BODY_MANDATORY_CA_VERIFY:
            return (
                False,
                f"Invalid mandatory-ca-verify '{value}'. Must be one of: {', '.join(VALID_BODY_MANDATORY_CA_VERIFY)}",
            )

    # Validate ca if present
    if "ca" in payload:
        value = payload.get("ca")
        if value and isinstance(value, str) and len(value) > 127:
            return (False, "ca cannot exceed 127 characters")

    # Validate subject if present
    if "subject" in payload:
        value = payload.get("subject")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "subject cannot exceed 255 characters")

    # Validate cn if present
    if "cn" in payload:
        value = payload.get("cn")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "cn cannot exceed 255 characters")

    # Validate cn-type if present
    if "cn-type" in payload:
        value = payload.get("cn-type")
        if value and value not in VALID_BODY_CN_TYPE:
            return (
                False,
                f"Invalid cn-type '{value}'. Must be one of: {', '.join(VALID_BODY_CN_TYPE)}",
            )

    # Validate mfa-mode if present
    if "mfa-mode" in payload:
        value = payload.get("mfa-mode")
        if value and value not in VALID_BODY_MFA_MODE:
            return (
                False,
                f"Invalid mfa-mode '{value}'. Must be one of: {', '.join(VALID_BODY_MFA_MODE)}",
            )

    # Validate mfa-server if present
    if "mfa-server" in payload:
        value = payload.get("mfa-server")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "mfa-server cannot exceed 35 characters")

    # Validate mfa-username if present
    if "mfa-username" in payload:
        value = payload.get("mfa-username")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "mfa-username cannot exceed 35 characters")

    # Validate ocsp-override-server if present
    if "ocsp-override-server" in payload:
        value = payload.get("ocsp-override-server")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "ocsp-override-server cannot exceed 35 characters")

    # Validate two-factor if present
    if "two-factor" in payload:
        value = payload.get("two-factor")
        if value and value not in VALID_BODY_TWO_FACTOR:
            return (
                False,
                f"Invalid two-factor '{value}'. Must be one of: {', '.join(VALID_BODY_TWO_FACTOR)}",
            )

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_peer_put(
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

    # Validate mandatory-ca-verify if present
    if "mandatory-ca-verify" in payload:
        value = payload.get("mandatory-ca-verify")
        if value and value not in VALID_BODY_MANDATORY_CA_VERIFY:
            return (
                False,
                f"Invalid mandatory-ca-verify '{value}'. Must be one of: {', '.join(VALID_BODY_MANDATORY_CA_VERIFY)}",
            )

    # Validate ca if present
    if "ca" in payload:
        value = payload.get("ca")
        if value and isinstance(value, str) and len(value) > 127:
            return (False, "ca cannot exceed 127 characters")

    # Validate subject if present
    if "subject" in payload:
        value = payload.get("subject")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "subject cannot exceed 255 characters")

    # Validate cn if present
    if "cn" in payload:
        value = payload.get("cn")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "cn cannot exceed 255 characters")

    # Validate cn-type if present
    if "cn-type" in payload:
        value = payload.get("cn-type")
        if value and value not in VALID_BODY_CN_TYPE:
            return (
                False,
                f"Invalid cn-type '{value}'. Must be one of: {', '.join(VALID_BODY_CN_TYPE)}",
            )

    # Validate mfa-mode if present
    if "mfa-mode" in payload:
        value = payload.get("mfa-mode")
        if value and value not in VALID_BODY_MFA_MODE:
            return (
                False,
                f"Invalid mfa-mode '{value}'. Must be one of: {', '.join(VALID_BODY_MFA_MODE)}",
            )

    # Validate mfa-server if present
    if "mfa-server" in payload:
        value = payload.get("mfa-server")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "mfa-server cannot exceed 35 characters")

    # Validate mfa-username if present
    if "mfa-username" in payload:
        value = payload.get("mfa-username")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "mfa-username cannot exceed 35 characters")

    # Validate ocsp-override-server if present
    if "ocsp-override-server" in payload:
        value = payload.get("ocsp-override-server")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "ocsp-override-server cannot exceed 35 characters")

    # Validate two-factor if present
    if "two-factor" in payload:
        value = payload.get("two-factor")
        if value and value not in VALID_BODY_TWO_FACTOR:
            return (
                False,
                f"Invalid two-factor '{value}'. Must be one of: {', '.join(VALID_BODY_TWO_FACTOR)}",
            )

    return (True, None)


# ============================================================================
# DELETE Validation
# ============================================================================


def validate_peer_delete(name: str | None = None) -> tuple[bool, str | None]:
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
