"""
Validation helpers for application list endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_EXTENDED_LOG = ["enable", "disable"]
VALID_BODY_OTHER_APPLICATION_ACTION = ["pass", "block"]
VALID_BODY_APP_REPLACEMSG = ["disable", "enable"]
VALID_BODY_OTHER_APPLICATION_LOG = ["disable", "enable"]
VALID_BODY_ENFORCE_DEFAULT_APP_PORT = ["disable", "enable"]
VALID_BODY_FORCE_INCLUSION_SSL_DI_SIGS = ["disable", "enable"]
VALID_BODY_UNKNOWN_APPLICATION_ACTION = ["pass", "block"]
VALID_BODY_UNKNOWN_APPLICATION_LOG = ["disable", "enable"]
VALID_BODY_P2P_BLOCK_LIST = ["skype", "edonkey", "bittorrent"]
VALID_BODY_DEEP_APP_INSPECTION = ["disable", "enable"]
VALID_BODY_OPTIONS = ["allow-dns", "allow-icmp", "allow-http", "allow-ssl"]
VALID_BODY_CONTROL_DEFAULT_NETWORK_SERVICES = ["disable", "enable"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_list_get(
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


def validate_list_post(payload: dict[str, Any]) -> tuple[bool, str | None]:
    """
    Validate POST request payload for creating list.

    Args:
        payload: The payload to validate

    Returns:
        Tuple of (is_valid, error_message)
    """
    # Validate name if present
    if "name" in payload:
        value = payload.get("name")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "name cannot exceed 47 characters")

    # Validate comment if present
    if "comment" in payload:
        value = payload.get("comment")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "comment cannot exceed 255 characters")

    # Validate replacemsg-group if present
    if "replacemsg-group" in payload:
        value = payload.get("replacemsg-group")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "replacemsg-group cannot exceed 35 characters")

    # Validate extended-log if present
    if "extended-log" in payload:
        value = payload.get("extended-log")
        if value and value not in VALID_BODY_EXTENDED_LOG:
            return (
                False,
                f"Invalid extended-log '{value}'. Must be one of: {', '.join(VALID_BODY_EXTENDED_LOG)}",
            )

    # Validate other-application-action if present
    if "other-application-action" in payload:
        value = payload.get("other-application-action")
        if value and value not in VALID_BODY_OTHER_APPLICATION_ACTION:
            return (
                False,
                f"Invalid other-application-action '{value}'. Must be one of: {', '.join(VALID_BODY_OTHER_APPLICATION_ACTION)}",
            )

    # Validate app-replacemsg if present
    if "app-replacemsg" in payload:
        value = payload.get("app-replacemsg")
        if value and value not in VALID_BODY_APP_REPLACEMSG:
            return (
                False,
                f"Invalid app-replacemsg '{value}'. Must be one of: {', '.join(VALID_BODY_APP_REPLACEMSG)}",
            )

    # Validate other-application-log if present
    if "other-application-log" in payload:
        value = payload.get("other-application-log")
        if value and value not in VALID_BODY_OTHER_APPLICATION_LOG:
            return (
                False,
                f"Invalid other-application-log '{value}'. Must be one of: {', '.join(VALID_BODY_OTHER_APPLICATION_LOG)}",
            )

    # Validate enforce-default-app-port if present
    if "enforce-default-app-port" in payload:
        value = payload.get("enforce-default-app-port")
        if value and value not in VALID_BODY_ENFORCE_DEFAULT_APP_PORT:
            return (
                False,
                f"Invalid enforce-default-app-port '{value}'. Must be one of: {', '.join(VALID_BODY_ENFORCE_DEFAULT_APP_PORT)}",
            )

    # Validate force-inclusion-ssl-di-sigs if present
    if "force-inclusion-ssl-di-sigs" in payload:
        value = payload.get("force-inclusion-ssl-di-sigs")
        if value and value not in VALID_BODY_FORCE_INCLUSION_SSL_DI_SIGS:
            return (
                False,
                f"Invalid force-inclusion-ssl-di-sigs '{value}'. Must be one of: {', '.join(VALID_BODY_FORCE_INCLUSION_SSL_DI_SIGS)}",
            )

    # Validate unknown-application-action if present
    if "unknown-application-action" in payload:
        value = payload.get("unknown-application-action")
        if value and value not in VALID_BODY_UNKNOWN_APPLICATION_ACTION:
            return (
                False,
                f"Invalid unknown-application-action '{value}'. Must be one of: {', '.join(VALID_BODY_UNKNOWN_APPLICATION_ACTION)}",
            )

    # Validate unknown-application-log if present
    if "unknown-application-log" in payload:
        value = payload.get("unknown-application-log")
        if value and value not in VALID_BODY_UNKNOWN_APPLICATION_LOG:
            return (
                False,
                f"Invalid unknown-application-log '{value}'. Must be one of: {', '.join(VALID_BODY_UNKNOWN_APPLICATION_LOG)}",
            )

    # Validate p2p-block-list if present
    if "p2p-block-list" in payload:
        value = payload.get("p2p-block-list")
        if value and value not in VALID_BODY_P2P_BLOCK_LIST:
            return (
                False,
                f"Invalid p2p-block-list '{value}'. Must be one of: {', '.join(VALID_BODY_P2P_BLOCK_LIST)}",
            )

    # Validate deep-app-inspection if present
    if "deep-app-inspection" in payload:
        value = payload.get("deep-app-inspection")
        if value and value not in VALID_BODY_DEEP_APP_INSPECTION:
            return (
                False,
                f"Invalid deep-app-inspection '{value}'. Must be one of: {', '.join(VALID_BODY_DEEP_APP_INSPECTION)}",
            )

    # Validate options if present
    if "options" in payload:
        value = payload.get("options")
        if value and value not in VALID_BODY_OPTIONS:
            return (
                False,
                f"Invalid options '{value}'. Must be one of: {', '.join(VALID_BODY_OPTIONS)}",
            )

    # Validate control-default-network-services if present
    if "control-default-network-services" in payload:
        value = payload.get("control-default-network-services")
        if value and value not in VALID_BODY_CONTROL_DEFAULT_NETWORK_SERVICES:
            return (
                False,
                f"Invalid control-default-network-services '{value}'. Must be one of: {', '.join(VALID_BODY_CONTROL_DEFAULT_NETWORK_SERVICES)}",
            )

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_list_put(
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
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "name cannot exceed 47 characters")

    # Validate comment if present
    if "comment" in payload:
        value = payload.get("comment")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "comment cannot exceed 255 characters")

    # Validate replacemsg-group if present
    if "replacemsg-group" in payload:
        value = payload.get("replacemsg-group")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "replacemsg-group cannot exceed 35 characters")

    # Validate extended-log if present
    if "extended-log" in payload:
        value = payload.get("extended-log")
        if value and value not in VALID_BODY_EXTENDED_LOG:
            return (
                False,
                f"Invalid extended-log '{value}'. Must be one of: {', '.join(VALID_BODY_EXTENDED_LOG)}",
            )

    # Validate other-application-action if present
    if "other-application-action" in payload:
        value = payload.get("other-application-action")
        if value and value not in VALID_BODY_OTHER_APPLICATION_ACTION:
            return (
                False,
                f"Invalid other-application-action '{value}'. Must be one of: {', '.join(VALID_BODY_OTHER_APPLICATION_ACTION)}",
            )

    # Validate app-replacemsg if present
    if "app-replacemsg" in payload:
        value = payload.get("app-replacemsg")
        if value and value not in VALID_BODY_APP_REPLACEMSG:
            return (
                False,
                f"Invalid app-replacemsg '{value}'. Must be one of: {', '.join(VALID_BODY_APP_REPLACEMSG)}",
            )

    # Validate other-application-log if present
    if "other-application-log" in payload:
        value = payload.get("other-application-log")
        if value and value not in VALID_BODY_OTHER_APPLICATION_LOG:
            return (
                False,
                f"Invalid other-application-log '{value}'. Must be one of: {', '.join(VALID_BODY_OTHER_APPLICATION_LOG)}",
            )

    # Validate enforce-default-app-port if present
    if "enforce-default-app-port" in payload:
        value = payload.get("enforce-default-app-port")
        if value and value not in VALID_BODY_ENFORCE_DEFAULT_APP_PORT:
            return (
                False,
                f"Invalid enforce-default-app-port '{value}'. Must be one of: {', '.join(VALID_BODY_ENFORCE_DEFAULT_APP_PORT)}",
            )

    # Validate force-inclusion-ssl-di-sigs if present
    if "force-inclusion-ssl-di-sigs" in payload:
        value = payload.get("force-inclusion-ssl-di-sigs")
        if value and value not in VALID_BODY_FORCE_INCLUSION_SSL_DI_SIGS:
            return (
                False,
                f"Invalid force-inclusion-ssl-di-sigs '{value}'. Must be one of: {', '.join(VALID_BODY_FORCE_INCLUSION_SSL_DI_SIGS)}",
            )

    # Validate unknown-application-action if present
    if "unknown-application-action" in payload:
        value = payload.get("unknown-application-action")
        if value and value not in VALID_BODY_UNKNOWN_APPLICATION_ACTION:
            return (
                False,
                f"Invalid unknown-application-action '{value}'. Must be one of: {', '.join(VALID_BODY_UNKNOWN_APPLICATION_ACTION)}",
            )

    # Validate unknown-application-log if present
    if "unknown-application-log" in payload:
        value = payload.get("unknown-application-log")
        if value and value not in VALID_BODY_UNKNOWN_APPLICATION_LOG:
            return (
                False,
                f"Invalid unknown-application-log '{value}'. Must be one of: {', '.join(VALID_BODY_UNKNOWN_APPLICATION_LOG)}",
            )

    # Validate p2p-block-list if present
    if "p2p-block-list" in payload:
        value = payload.get("p2p-block-list")
        if value and value not in VALID_BODY_P2P_BLOCK_LIST:
            return (
                False,
                f"Invalid p2p-block-list '{value}'. Must be one of: {', '.join(VALID_BODY_P2P_BLOCK_LIST)}",
            )

    # Validate deep-app-inspection if present
    if "deep-app-inspection" in payload:
        value = payload.get("deep-app-inspection")
        if value and value not in VALID_BODY_DEEP_APP_INSPECTION:
            return (
                False,
                f"Invalid deep-app-inspection '{value}'. Must be one of: {', '.join(VALID_BODY_DEEP_APP_INSPECTION)}",
            )

    # Validate options if present
    if "options" in payload:
        value = payload.get("options")
        if value and value not in VALID_BODY_OPTIONS:
            return (
                False,
                f"Invalid options '{value}'. Must be one of: {', '.join(VALID_BODY_OPTIONS)}",
            )

    # Validate control-default-network-services if present
    if "control-default-network-services" in payload:
        value = payload.get("control-default-network-services")
        if value and value not in VALID_BODY_CONTROL_DEFAULT_NETWORK_SERVICES:
            return (
                False,
                f"Invalid control-default-network-services '{value}'. Must be one of: {', '.join(VALID_BODY_CONTROL_DEFAULT_NETWORK_SERVICES)}",
            )

    return (True, None)


# ============================================================================
# DELETE Validation
# ============================================================================


def validate_list_delete(name: str | None = None) -> tuple[bool, str | None]:
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
