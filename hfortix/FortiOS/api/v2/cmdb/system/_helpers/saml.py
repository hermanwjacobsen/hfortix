"""
Validation helpers for system saml endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_STATUS = ["enable", "disable"]
VALID_BODY_ROLE = ["identity-provider", "service-provider"]
VALID_BODY_DEFAULT_LOGIN_PAGE = ["normal", "sso"]
VALID_BODY_BINDING_PROTOCOL = ["post", "redirect"]
VALID_BODY_REQUIRE_SIGNED_RESP_AND_ASRT = ["enable", "disable"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_saml_get(
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


def validate_saml_put(
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

    # Validate role if present
    if "role" in payload:
        value = payload.get("role")
        if value and value not in VALID_BODY_ROLE:
            return (
                False,
                f"Invalid role '{value}'. Must be one of: {', '.join(VALID_BODY_ROLE)}",
            )

    # Validate default-login-page if present
    if "default-login-page" in payload:
        value = payload.get("default-login-page")
        if value and value not in VALID_BODY_DEFAULT_LOGIN_PAGE:
            return (
                False,
                f"Invalid default-login-page '{value}'. Must be one of: {', '.join(VALID_BODY_DEFAULT_LOGIN_PAGE)}",
            )

    # Validate default-profile if present
    if "default-profile" in payload:
        value = payload.get("default-profile")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "default-profile cannot exceed 35 characters")

    # Validate cert if present
    if "cert" in payload:
        value = payload.get("cert")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "cert cannot exceed 35 characters")

    # Validate binding-protocol if present
    if "binding-protocol" in payload:
        value = payload.get("binding-protocol")
        if value and value not in VALID_BODY_BINDING_PROTOCOL:
            return (
                False,
                f"Invalid binding-protocol '{value}'. Must be one of: {', '.join(VALID_BODY_BINDING_PROTOCOL)}",
            )

    # Validate portal-url if present
    if "portal-url" in payload:
        value = payload.get("portal-url")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "portal-url cannot exceed 255 characters")

    # Validate entity-id if present
    if "entity-id" in payload:
        value = payload.get("entity-id")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "entity-id cannot exceed 255 characters")

    # Validate single-sign-on-url if present
    if "single-sign-on-url" in payload:
        value = payload.get("single-sign-on-url")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "single-sign-on-url cannot exceed 255 characters")

    # Validate single-logout-url if present
    if "single-logout-url" in payload:
        value = payload.get("single-logout-url")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "single-logout-url cannot exceed 255 characters")

    # Validate idp-entity-id if present
    if "idp-entity-id" in payload:
        value = payload.get("idp-entity-id")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "idp-entity-id cannot exceed 255 characters")

    # Validate idp-single-sign-on-url if present
    if "idp-single-sign-on-url" in payload:
        value = payload.get("idp-single-sign-on-url")
        if value and isinstance(value, str) and len(value) > 255:
            return (
                False,
                "idp-single-sign-on-url cannot exceed 255 characters",
            )

    # Validate idp-single-logout-url if present
    if "idp-single-logout-url" in payload:
        value = payload.get("idp-single-logout-url")
        if value and isinstance(value, str) and len(value) > 255:
            return (
                False,
                "idp-single-logout-url cannot exceed 255 characters",
            )

    # Validate idp-cert if present
    if "idp-cert" in payload:
        value = payload.get("idp-cert")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "idp-cert cannot exceed 35 characters")

    # Validate server-address if present
    if "server-address" in payload:
        value = payload.get("server-address")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "server-address cannot exceed 63 characters")

    # Validate require-signed-resp-and-asrt if present
    if "require-signed-resp-and-asrt" in payload:
        value = payload.get("require-signed-resp-and-asrt")
        if value and value not in VALID_BODY_REQUIRE_SIGNED_RESP_AND_ASRT:
            return (
                False,
                f"Invalid require-signed-resp-and-asrt '{value}'. Must be one of: {', '.join(VALID_BODY_REQUIRE_SIGNED_RESP_AND_ASRT)}",
            )

    # Validate tolerance if present
    if "tolerance" in payload:
        value = payload.get("tolerance")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "tolerance must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (False, f"tolerance must be numeric, got: {value}")

    # Validate life if present
    if "life" in payload:
        value = payload.get("life")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (False, "life must be between 0 and 4294967295")
            except (ValueError, TypeError):
                return (False, f"life must be numeric, got: {value}")

    return (True, None)
