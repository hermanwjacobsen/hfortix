"""
Validation helpers for ztna web_portal endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_LOG_BLOCKED_TRAFFIC = ["disable", "enable"]
VALID_BODY_AUTH_PORTAL = ["disable", "enable"]
VALID_BODY_DISPLAY_BOOKMARK = ["enable", "disable"]
VALID_BODY_FOCUS_BOOKMARK = ["enable", "disable"]
VALID_BODY_DISPLAY_STATUS = ["enable", "disable"]
VALID_BODY_DISPLAY_HISTORY = ["enable", "disable"]
VALID_BODY_POLICY_AUTH_SSO = ["enable", "disable"]
VALID_BODY_THEME = [
    "jade",
    "neutrino",
    "mariner",
    "graphite",
    "melongene",
    "jet-stream",
    "security-fabric",
    "dark-matter",
    "onyx",
    "eclipse",
]
VALID_BODY_CLIPBOARD = ["enable", "disable"]
VALID_BODY_FORTICLIENT_DOWNLOAD = ["enable", "disable"]
VALID_BODY_CUSTOMIZE_FORTICLIENT_DOWNLOAD_URL = ["enable", "disable"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_web_portal_get(
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


def validate_web_portal_post(
    payload: dict[str, Any],
) -> tuple[bool, str | None]:
    """
    Validate POST request payload for creating web_portal.

    Args:
        payload: The payload to validate

    Returns:
        Tuple of (is_valid, error_message)
    """
    # Validate name if present
    if "name" in payload:
        value = payload.get("name")
        if value and isinstance(value, str) and len(value) > 79:
            return (False, "name cannot exceed 79 characters")

    # Validate vip if present
    if "vip" in payload:
        value = payload.get("vip")
        if value and isinstance(value, str) and len(value) > 79:
            return (False, "vip cannot exceed 79 characters")

    # Validate host if present
    if "host" in payload:
        value = payload.get("host")
        if value and isinstance(value, str) and len(value) > 79:
            return (False, "host cannot exceed 79 characters")

    # Validate decrypted-traffic-mirror if present
    if "decrypted-traffic-mirror" in payload:
        value = payload.get("decrypted-traffic-mirror")
        if value and isinstance(value, str) and len(value) > 35:
            return (
                False,
                "decrypted-traffic-mirror cannot exceed 35 characters",
            )

    # Validate log-blocked-traffic if present
    if "log-blocked-traffic" in payload:
        value = payload.get("log-blocked-traffic")
        if value and value not in VALID_BODY_LOG_BLOCKED_TRAFFIC:
            return (
                False,
                f"Invalid log-blocked-traffic '{value}'. Must be one of: {', '.join(VALID_BODY_LOG_BLOCKED_TRAFFIC)}",
            )

    # Validate auth-portal if present
    if "auth-portal" in payload:
        value = payload.get("auth-portal")
        if value and value not in VALID_BODY_AUTH_PORTAL:
            return (
                False,
                f"Invalid auth-portal '{value}'. Must be one of: {', '.join(VALID_BODY_AUTH_PORTAL)}",
            )

    # Validate auth-virtual-host if present
    if "auth-virtual-host" in payload:
        value = payload.get("auth-virtual-host")
        if value and isinstance(value, str) and len(value) > 79:
            return (False, "auth-virtual-host cannot exceed 79 characters")

    # Validate vip6 if present
    if "vip6" in payload:
        value = payload.get("vip6")
        if value and isinstance(value, str) and len(value) > 79:
            return (False, "vip6 cannot exceed 79 characters")

    # Validate auth-rule if present
    if "auth-rule" in payload:
        value = payload.get("auth-rule")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "auth-rule cannot exceed 35 characters")

    # Validate display-bookmark if present
    if "display-bookmark" in payload:
        value = payload.get("display-bookmark")
        if value and value not in VALID_BODY_DISPLAY_BOOKMARK:
            return (
                False,
                f"Invalid display-bookmark '{value}'. Must be one of: {', '.join(VALID_BODY_DISPLAY_BOOKMARK)}",
            )

    # Validate focus-bookmark if present
    if "focus-bookmark" in payload:
        value = payload.get("focus-bookmark")
        if value and value not in VALID_BODY_FOCUS_BOOKMARK:
            return (
                False,
                f"Invalid focus-bookmark '{value}'. Must be one of: {', '.join(VALID_BODY_FOCUS_BOOKMARK)}",
            )

    # Validate display-status if present
    if "display-status" in payload:
        value = payload.get("display-status")
        if value and value not in VALID_BODY_DISPLAY_STATUS:
            return (
                False,
                f"Invalid display-status '{value}'. Must be one of: {', '.join(VALID_BODY_DISPLAY_STATUS)}",
            )

    # Validate display-history if present
    if "display-history" in payload:
        value = payload.get("display-history")
        if value and value not in VALID_BODY_DISPLAY_HISTORY:
            return (
                False,
                f"Invalid display-history '{value}'. Must be one of: {', '.join(VALID_BODY_DISPLAY_HISTORY)}",
            )

    # Validate policy-auth-sso if present
    if "policy-auth-sso" in payload:
        value = payload.get("policy-auth-sso")
        if value and value not in VALID_BODY_POLICY_AUTH_SSO:
            return (
                False,
                f"Invalid policy-auth-sso '{value}'. Must be one of: {', '.join(VALID_BODY_POLICY_AUTH_SSO)}",
            )

    # Validate heading if present
    if "heading" in payload:
        value = payload.get("heading")
        if value and isinstance(value, str) and len(value) > 31:
            return (False, "heading cannot exceed 31 characters")

    # Validate theme if present
    if "theme" in payload:
        value = payload.get("theme")
        if value and value not in VALID_BODY_THEME:
            return (
                False,
                f"Invalid theme '{value}'. Must be one of: {', '.join(VALID_BODY_THEME)}",
            )

    # Validate clipboard if present
    if "clipboard" in payload:
        value = payload.get("clipboard")
        if value and value not in VALID_BODY_CLIPBOARD:
            return (
                False,
                f"Invalid clipboard '{value}'. Must be one of: {', '.join(VALID_BODY_CLIPBOARD)}",
            )

    # Validate default-window-width if present
    if "default-window-width" in payload:
        value = payload.get("default-window-width")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 65535:
                    return (
                        False,
                        "default-window-width must be between 0 and 65535",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"default-window-width must be numeric, got: {value}",
                )

    # Validate default-window-height if present
    if "default-window-height" in payload:
        value = payload.get("default-window-height")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 65535:
                    return (
                        False,
                        "default-window-height must be between 0 and 65535",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"default-window-height must be numeric, got: {value}",
                )

    # Validate cookie-age if present
    if "cookie-age" in payload:
        value = payload.get("cookie-age")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 525600:
                    return (False, "cookie-age must be between 0 and 525600")
            except (ValueError, TypeError):
                return (False, f"cookie-age must be numeric, got: {value}")

    # Validate forticlient-download if present
    if "forticlient-download" in payload:
        value = payload.get("forticlient-download")
        if value and value not in VALID_BODY_FORTICLIENT_DOWNLOAD:
            return (
                False,
                f"Invalid forticlient-download '{value}'. Must be one of: {', '.join(VALID_BODY_FORTICLIENT_DOWNLOAD)}",
            )

    # Validate customize-forticlient-download-url if present
    if "customize-forticlient-download-url" in payload:
        value = payload.get("customize-forticlient-download-url")
        if (
            value
            and value not in VALID_BODY_CUSTOMIZE_FORTICLIENT_DOWNLOAD_URL
        ):
            return (
                False,
                f"Invalid customize-forticlient-download-url '{value}'. Must be one of: {', '.join(VALID_BODY_CUSTOMIZE_FORTICLIENT_DOWNLOAD_URL)}",
            )

    # Validate windows-forticlient-download-url if present
    if "windows-forticlient-download-url" in payload:
        value = payload.get("windows-forticlient-download-url")
        if value and isinstance(value, str) and len(value) > 1023:
            return (
                False,
                "windows-forticlient-download-url cannot exceed 1023 characters",
            )

    # Validate macos-forticlient-download-url if present
    if "macos-forticlient-download-url" in payload:
        value = payload.get("macos-forticlient-download-url")
        if value and isinstance(value, str) and len(value) > 1023:
            return (
                False,
                "macos-forticlient-download-url cannot exceed 1023 characters",
            )

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_web_portal_put(
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
        if value and isinstance(value, str) and len(value) > 79:
            return (False, "name cannot exceed 79 characters")

    # Validate vip if present
    if "vip" in payload:
        value = payload.get("vip")
        if value and isinstance(value, str) and len(value) > 79:
            return (False, "vip cannot exceed 79 characters")

    # Validate host if present
    if "host" in payload:
        value = payload.get("host")
        if value and isinstance(value, str) and len(value) > 79:
            return (False, "host cannot exceed 79 characters")

    # Validate decrypted-traffic-mirror if present
    if "decrypted-traffic-mirror" in payload:
        value = payload.get("decrypted-traffic-mirror")
        if value and isinstance(value, str) and len(value) > 35:
            return (
                False,
                "decrypted-traffic-mirror cannot exceed 35 characters",
            )

    # Validate log-blocked-traffic if present
    if "log-blocked-traffic" in payload:
        value = payload.get("log-blocked-traffic")
        if value and value not in VALID_BODY_LOG_BLOCKED_TRAFFIC:
            return (
                False,
                f"Invalid log-blocked-traffic '{value}'. Must be one of: {', '.join(VALID_BODY_LOG_BLOCKED_TRAFFIC)}",
            )

    # Validate auth-portal if present
    if "auth-portal" in payload:
        value = payload.get("auth-portal")
        if value and value not in VALID_BODY_AUTH_PORTAL:
            return (
                False,
                f"Invalid auth-portal '{value}'. Must be one of: {', '.join(VALID_BODY_AUTH_PORTAL)}",
            )

    # Validate auth-virtual-host if present
    if "auth-virtual-host" in payload:
        value = payload.get("auth-virtual-host")
        if value and isinstance(value, str) and len(value) > 79:
            return (False, "auth-virtual-host cannot exceed 79 characters")

    # Validate vip6 if present
    if "vip6" in payload:
        value = payload.get("vip6")
        if value and isinstance(value, str) and len(value) > 79:
            return (False, "vip6 cannot exceed 79 characters")

    # Validate auth-rule if present
    if "auth-rule" in payload:
        value = payload.get("auth-rule")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "auth-rule cannot exceed 35 characters")

    # Validate display-bookmark if present
    if "display-bookmark" in payload:
        value = payload.get("display-bookmark")
        if value and value not in VALID_BODY_DISPLAY_BOOKMARK:
            return (
                False,
                f"Invalid display-bookmark '{value}'. Must be one of: {', '.join(VALID_BODY_DISPLAY_BOOKMARK)}",
            )

    # Validate focus-bookmark if present
    if "focus-bookmark" in payload:
        value = payload.get("focus-bookmark")
        if value and value not in VALID_BODY_FOCUS_BOOKMARK:
            return (
                False,
                f"Invalid focus-bookmark '{value}'. Must be one of: {', '.join(VALID_BODY_FOCUS_BOOKMARK)}",
            )

    # Validate display-status if present
    if "display-status" in payload:
        value = payload.get("display-status")
        if value and value not in VALID_BODY_DISPLAY_STATUS:
            return (
                False,
                f"Invalid display-status '{value}'. Must be one of: {', '.join(VALID_BODY_DISPLAY_STATUS)}",
            )

    # Validate display-history if present
    if "display-history" in payload:
        value = payload.get("display-history")
        if value and value not in VALID_BODY_DISPLAY_HISTORY:
            return (
                False,
                f"Invalid display-history '{value}'. Must be one of: {', '.join(VALID_BODY_DISPLAY_HISTORY)}",
            )

    # Validate policy-auth-sso if present
    if "policy-auth-sso" in payload:
        value = payload.get("policy-auth-sso")
        if value and value not in VALID_BODY_POLICY_AUTH_SSO:
            return (
                False,
                f"Invalid policy-auth-sso '{value}'. Must be one of: {', '.join(VALID_BODY_POLICY_AUTH_SSO)}",
            )

    # Validate heading if present
    if "heading" in payload:
        value = payload.get("heading")
        if value and isinstance(value, str) and len(value) > 31:
            return (False, "heading cannot exceed 31 characters")

    # Validate theme if present
    if "theme" in payload:
        value = payload.get("theme")
        if value and value not in VALID_BODY_THEME:
            return (
                False,
                f"Invalid theme '{value}'. Must be one of: {', '.join(VALID_BODY_THEME)}",
            )

    # Validate clipboard if present
    if "clipboard" in payload:
        value = payload.get("clipboard")
        if value and value not in VALID_BODY_CLIPBOARD:
            return (
                False,
                f"Invalid clipboard '{value}'. Must be one of: {', '.join(VALID_BODY_CLIPBOARD)}",
            )

    # Validate default-window-width if present
    if "default-window-width" in payload:
        value = payload.get("default-window-width")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 65535:
                    return (
                        False,
                        "default-window-width must be between 0 and 65535",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"default-window-width must be numeric, got: {value}",
                )

    # Validate default-window-height if present
    if "default-window-height" in payload:
        value = payload.get("default-window-height")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 65535:
                    return (
                        False,
                        "default-window-height must be between 0 and 65535",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"default-window-height must be numeric, got: {value}",
                )

    # Validate cookie-age if present
    if "cookie-age" in payload:
        value = payload.get("cookie-age")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 525600:
                    return (False, "cookie-age must be between 0 and 525600")
            except (ValueError, TypeError):
                return (False, f"cookie-age must be numeric, got: {value}")

    # Validate forticlient-download if present
    if "forticlient-download" in payload:
        value = payload.get("forticlient-download")
        if value and value not in VALID_BODY_FORTICLIENT_DOWNLOAD:
            return (
                False,
                f"Invalid forticlient-download '{value}'. Must be one of: {', '.join(VALID_BODY_FORTICLIENT_DOWNLOAD)}",
            )

    # Validate customize-forticlient-download-url if present
    if "customize-forticlient-download-url" in payload:
        value = payload.get("customize-forticlient-download-url")
        if (
            value
            and value not in VALID_BODY_CUSTOMIZE_FORTICLIENT_DOWNLOAD_URL
        ):
            return (
                False,
                f"Invalid customize-forticlient-download-url '{value}'. Must be one of: {', '.join(VALID_BODY_CUSTOMIZE_FORTICLIENT_DOWNLOAD_URL)}",
            )

    # Validate windows-forticlient-download-url if present
    if "windows-forticlient-download-url" in payload:
        value = payload.get("windows-forticlient-download-url")
        if value and isinstance(value, str) and len(value) > 1023:
            return (
                False,
                "windows-forticlient-download-url cannot exceed 1023 characters",
            )

    # Validate macos-forticlient-download-url if present
    if "macos-forticlient-download-url" in payload:
        value = payload.get("macos-forticlient-download-url")
        if value and isinstance(value, str) and len(value) > 1023:
            return (
                False,
                "macos-forticlient-download-url cannot exceed 1023 characters",
            )

    return (True, None)


# ============================================================================
# DELETE Validation
# ============================================================================


def validate_web_portal_delete(
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
