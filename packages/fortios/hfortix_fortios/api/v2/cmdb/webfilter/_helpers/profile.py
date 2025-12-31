"""
Validation helpers for webfilter profile endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_FEATURE_SET = ["flow", "proxy"]
VALID_BODY_OPTIONS = [
    "activexfilter",
    "cookiefilter",
    "javafilter",
    "block-invalid-url",
    "jscript",
    "js",
    "vbs",
    "unknown",
    "intrinsic",
    "wf-referer",
    "wf-cookie",
]
VALID_BODY_HTTPS_REPLACEMSG = ["enable", "disable"]
VALID_BODY_WEB_FLOW_LOG_ENCODING = ["utf-8", "punycode"]
VALID_BODY_OVRD_PERM = [
    "bannedword-override",
    "urlfilter-override",
    "fortiguard-wf-override",
    "contenttype-check-override",
]
VALID_BODY_POST_ACTION = ["normal", "block"]
VALID_BODY_WISP = ["enable", "disable"]
VALID_BODY_WISP_ALGORITHM = [
    "primary-secondary",
    "round-robin",
    "auto-learning",
]
VALID_BODY_LOG_ALL_URL = ["enable", "disable"]
VALID_BODY_WEB_CONTENT_LOG = ["enable", "disable"]
VALID_BODY_WEB_FILTER_ACTIVEX_LOG = ["enable", "disable"]
VALID_BODY_WEB_FILTER_COMMAND_BLOCK_LOG = ["enable", "disable"]
VALID_BODY_WEB_FILTER_COOKIE_LOG = ["enable", "disable"]
VALID_BODY_WEB_FILTER_APPLET_LOG = ["enable", "disable"]
VALID_BODY_WEB_FILTER_JSCRIPT_LOG = ["enable", "disable"]
VALID_BODY_WEB_FILTER_JS_LOG = ["enable", "disable"]
VALID_BODY_WEB_FILTER_VBS_LOG = ["enable", "disable"]
VALID_BODY_WEB_FILTER_UNKNOWN_LOG = ["enable", "disable"]
VALID_BODY_WEB_FILTER_REFERER_LOG = ["enable", "disable"]
VALID_BODY_WEB_FILTER_COOKIE_REMOVAL_LOG = ["enable", "disable"]
VALID_BODY_WEB_URL_LOG = ["enable", "disable"]
VALID_BODY_WEB_INVALID_DOMAIN_LOG = ["enable", "disable"]
VALID_BODY_WEB_FTGD_ERR_LOG = ["enable", "disable"]
VALID_BODY_WEB_FTGD_QUOTA_USAGE = ["enable", "disable"]
VALID_BODY_EXTENDED_LOG = ["enable", "disable"]
VALID_BODY_WEB_EXTENDED_ALL_ACTION_LOG = ["enable", "disable"]
VALID_BODY_WEB_ANTIPHISHING_LOG = ["enable", "disable"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_profile_get(
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


def validate_profile_post(payload: dict[str, Any]) -> tuple[bool, str | None]:
    """
    Validate POST request payload for creating profile.

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

    # Validate feature-set if present
    if "feature-set" in payload:
        value = payload.get("feature-set")
        if value and value not in VALID_BODY_FEATURE_SET:
            return (
                False,
                f"Invalid feature-set '{value}'. Must be one of: {', '.join(VALID_BODY_FEATURE_SET)}",
            )

    # Validate replacemsg-group if present
    if "replacemsg-group" in payload:
        value = payload.get("replacemsg-group")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "replacemsg-group cannot exceed 35 characters")

    # Validate options if present
    if "options" in payload:
        value = payload.get("options")
        if value and value not in VALID_BODY_OPTIONS:
            return (
                False,
                f"Invalid options '{value}'. Must be one of: {', '.join(VALID_BODY_OPTIONS)}",
            )

    # Validate https-replacemsg if present
    if "https-replacemsg" in payload:
        value = payload.get("https-replacemsg")
        if value and value not in VALID_BODY_HTTPS_REPLACEMSG:
            return (
                False,
                f"Invalid https-replacemsg '{value}'. Must be one of: {', '.join(VALID_BODY_HTTPS_REPLACEMSG)}",
            )

    # Validate web-flow-log-encoding if present
    if "web-flow-log-encoding" in payload:
        value = payload.get("web-flow-log-encoding")
        if value and value not in VALID_BODY_WEB_FLOW_LOG_ENCODING:
            return (
                False,
                f"Invalid web-flow-log-encoding '{value}'. Must be one of: {', '.join(VALID_BODY_WEB_FLOW_LOG_ENCODING)}",
            )

    # Validate ovrd-perm if present
    if "ovrd-perm" in payload:
        value = payload.get("ovrd-perm")
        if value and value not in VALID_BODY_OVRD_PERM:
            return (
                False,
                f"Invalid ovrd-perm '{value}'. Must be one of: {', '.join(VALID_BODY_OVRD_PERM)}",
            )

    # Validate post-action if present
    if "post-action" in payload:
        value = payload.get("post-action")
        if value and value not in VALID_BODY_POST_ACTION:
            return (
                False,
                f"Invalid post-action '{value}'. Must be one of: {', '.join(VALID_BODY_POST_ACTION)}",
            )

    # Validate wisp if present
    if "wisp" in payload:
        value = payload.get("wisp")
        if value and value not in VALID_BODY_WISP:
            return (
                False,
                f"Invalid wisp '{value}'. Must be one of: {', '.join(VALID_BODY_WISP)}",
            )

    # Validate wisp-algorithm if present
    if "wisp-algorithm" in payload:
        value = payload.get("wisp-algorithm")
        if value and value not in VALID_BODY_WISP_ALGORITHM:
            return (
                False,
                f"Invalid wisp-algorithm '{value}'. Must be one of: {', '.join(VALID_BODY_WISP_ALGORITHM)}",
            )

    # Validate log-all-url if present
    if "log-all-url" in payload:
        value = payload.get("log-all-url")
        if value and value not in VALID_BODY_LOG_ALL_URL:
            return (
                False,
                f"Invalid log-all-url '{value}'. Must be one of: {', '.join(VALID_BODY_LOG_ALL_URL)}",
            )

    # Validate web-content-log if present
    if "web-content-log" in payload:
        value = payload.get("web-content-log")
        if value and value not in VALID_BODY_WEB_CONTENT_LOG:
            return (
                False,
                f"Invalid web-content-log '{value}'. Must be one of: {', '.join(VALID_BODY_WEB_CONTENT_LOG)}",
            )

    # Validate web-filter-activex-log if present
    if "web-filter-activex-log" in payload:
        value = payload.get("web-filter-activex-log")
        if value and value not in VALID_BODY_WEB_FILTER_ACTIVEX_LOG:
            return (
                False,
                f"Invalid web-filter-activex-log '{value}'. Must be one of: {', '.join(VALID_BODY_WEB_FILTER_ACTIVEX_LOG)}",
            )

    # Validate web-filter-command-block-log if present
    if "web-filter-command-block-log" in payload:
        value = payload.get("web-filter-command-block-log")
        if value and value not in VALID_BODY_WEB_FILTER_COMMAND_BLOCK_LOG:
            return (
                False,
                f"Invalid web-filter-command-block-log '{value}'. Must be one of: {', '.join(VALID_BODY_WEB_FILTER_COMMAND_BLOCK_LOG)}",
            )

    # Validate web-filter-cookie-log if present
    if "web-filter-cookie-log" in payload:
        value = payload.get("web-filter-cookie-log")
        if value and value not in VALID_BODY_WEB_FILTER_COOKIE_LOG:
            return (
                False,
                f"Invalid web-filter-cookie-log '{value}'. Must be one of: {', '.join(VALID_BODY_WEB_FILTER_COOKIE_LOG)}",
            )

    # Validate web-filter-applet-log if present
    if "web-filter-applet-log" in payload:
        value = payload.get("web-filter-applet-log")
        if value and value not in VALID_BODY_WEB_FILTER_APPLET_LOG:
            return (
                False,
                f"Invalid web-filter-applet-log '{value}'. Must be one of: {', '.join(VALID_BODY_WEB_FILTER_APPLET_LOG)}",
            )

    # Validate web-filter-jscript-log if present
    if "web-filter-jscript-log" in payload:
        value = payload.get("web-filter-jscript-log")
        if value and value not in VALID_BODY_WEB_FILTER_JSCRIPT_LOG:
            return (
                False,
                f"Invalid web-filter-jscript-log '{value}'. Must be one of: {', '.join(VALID_BODY_WEB_FILTER_JSCRIPT_LOG)}",
            )

    # Validate web-filter-js-log if present
    if "web-filter-js-log" in payload:
        value = payload.get("web-filter-js-log")
        if value and value not in VALID_BODY_WEB_FILTER_JS_LOG:
            return (
                False,
                f"Invalid web-filter-js-log '{value}'. Must be one of: {', '.join(VALID_BODY_WEB_FILTER_JS_LOG)}",
            )

    # Validate web-filter-vbs-log if present
    if "web-filter-vbs-log" in payload:
        value = payload.get("web-filter-vbs-log")
        if value and value not in VALID_BODY_WEB_FILTER_VBS_LOG:
            return (
                False,
                f"Invalid web-filter-vbs-log '{value}'. Must be one of: {', '.join(VALID_BODY_WEB_FILTER_VBS_LOG)}",
            )

    # Validate web-filter-unknown-log if present
    if "web-filter-unknown-log" in payload:
        value = payload.get("web-filter-unknown-log")
        if value and value not in VALID_BODY_WEB_FILTER_UNKNOWN_LOG:
            return (
                False,
                f"Invalid web-filter-unknown-log '{value}'. Must be one of: {', '.join(VALID_BODY_WEB_FILTER_UNKNOWN_LOG)}",
            )

    # Validate web-filter-referer-log if present
    if "web-filter-referer-log" in payload:
        value = payload.get("web-filter-referer-log")
        if value and value not in VALID_BODY_WEB_FILTER_REFERER_LOG:
            return (
                False,
                f"Invalid web-filter-referer-log '{value}'. Must be one of: {', '.join(VALID_BODY_WEB_FILTER_REFERER_LOG)}",
            )

    # Validate web-filter-cookie-removal-log if present
    if "web-filter-cookie-removal-log" in payload:
        value = payload.get("web-filter-cookie-removal-log")
        if value and value not in VALID_BODY_WEB_FILTER_COOKIE_REMOVAL_LOG:
            return (
                False,
                f"Invalid web-filter-cookie-removal-log '{value}'. Must be one of: {', '.join(VALID_BODY_WEB_FILTER_COOKIE_REMOVAL_LOG)}",
            )

    # Validate web-url-log if present
    if "web-url-log" in payload:
        value = payload.get("web-url-log")
        if value and value not in VALID_BODY_WEB_URL_LOG:
            return (
                False,
                f"Invalid web-url-log '{value}'. Must be one of: {', '.join(VALID_BODY_WEB_URL_LOG)}",
            )

    # Validate web-invalid-domain-log if present
    if "web-invalid-domain-log" in payload:
        value = payload.get("web-invalid-domain-log")
        if value and value not in VALID_BODY_WEB_INVALID_DOMAIN_LOG:
            return (
                False,
                f"Invalid web-invalid-domain-log '{value}'. Must be one of: {', '.join(VALID_BODY_WEB_INVALID_DOMAIN_LOG)}",
            )

    # Validate web-ftgd-err-log if present
    if "web-ftgd-err-log" in payload:
        value = payload.get("web-ftgd-err-log")
        if value and value not in VALID_BODY_WEB_FTGD_ERR_LOG:
            return (
                False,
                f"Invalid web-ftgd-err-log '{value}'. Must be one of: {', '.join(VALID_BODY_WEB_FTGD_ERR_LOG)}",
            )

    # Validate web-ftgd-quota-usage if present
    if "web-ftgd-quota-usage" in payload:
        value = payload.get("web-ftgd-quota-usage")
        if value and value not in VALID_BODY_WEB_FTGD_QUOTA_USAGE:
            return (
                False,
                f"Invalid web-ftgd-quota-usage '{value}'. Must be one of: {', '.join(VALID_BODY_WEB_FTGD_QUOTA_USAGE)}",
            )

    # Validate extended-log if present
    if "extended-log" in payload:
        value = payload.get("extended-log")
        if value and value not in VALID_BODY_EXTENDED_LOG:
            return (
                False,
                f"Invalid extended-log '{value}'. Must be one of: {', '.join(VALID_BODY_EXTENDED_LOG)}",
            )

    # Validate web-extended-all-action-log if present
    if "web-extended-all-action-log" in payload:
        value = payload.get("web-extended-all-action-log")
        if value and value not in VALID_BODY_WEB_EXTENDED_ALL_ACTION_LOG:
            return (
                False,
                f"Invalid web-extended-all-action-log '{value}'. Must be one of: {', '.join(VALID_BODY_WEB_EXTENDED_ALL_ACTION_LOG)}",
            )

    # Validate web-antiphishing-log if present
    if "web-antiphishing-log" in payload:
        value = payload.get("web-antiphishing-log")
        if value and value not in VALID_BODY_WEB_ANTIPHISHING_LOG:
            return (
                False,
                f"Invalid web-antiphishing-log '{value}'. Must be one of: {', '.join(VALID_BODY_WEB_ANTIPHISHING_LOG)}",
            )

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_profile_put(
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

    # Validate feature-set if present
    if "feature-set" in payload:
        value = payload.get("feature-set")
        if value and value not in VALID_BODY_FEATURE_SET:
            return (
                False,
                f"Invalid feature-set '{value}'. Must be one of: {', '.join(VALID_BODY_FEATURE_SET)}",
            )

    # Validate replacemsg-group if present
    if "replacemsg-group" in payload:
        value = payload.get("replacemsg-group")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "replacemsg-group cannot exceed 35 characters")

    # Validate options if present
    if "options" in payload:
        value = payload.get("options")
        if value and value not in VALID_BODY_OPTIONS:
            return (
                False,
                f"Invalid options '{value}'. Must be one of: {', '.join(VALID_BODY_OPTIONS)}",
            )

    # Validate https-replacemsg if present
    if "https-replacemsg" in payload:
        value = payload.get("https-replacemsg")
        if value and value not in VALID_BODY_HTTPS_REPLACEMSG:
            return (
                False,
                f"Invalid https-replacemsg '{value}'. Must be one of: {', '.join(VALID_BODY_HTTPS_REPLACEMSG)}",
            )

    # Validate web-flow-log-encoding if present
    if "web-flow-log-encoding" in payload:
        value = payload.get("web-flow-log-encoding")
        if value and value not in VALID_BODY_WEB_FLOW_LOG_ENCODING:
            return (
                False,
                f"Invalid web-flow-log-encoding '{value}'. Must be one of: {', '.join(VALID_BODY_WEB_FLOW_LOG_ENCODING)}",
            )

    # Validate ovrd-perm if present
    if "ovrd-perm" in payload:
        value = payload.get("ovrd-perm")
        if value and value not in VALID_BODY_OVRD_PERM:
            return (
                False,
                f"Invalid ovrd-perm '{value}'. Must be one of: {', '.join(VALID_BODY_OVRD_PERM)}",
            )

    # Validate post-action if present
    if "post-action" in payload:
        value = payload.get("post-action")
        if value and value not in VALID_BODY_POST_ACTION:
            return (
                False,
                f"Invalid post-action '{value}'. Must be one of: {', '.join(VALID_BODY_POST_ACTION)}",
            )

    # Validate wisp if present
    if "wisp" in payload:
        value = payload.get("wisp")
        if value and value not in VALID_BODY_WISP:
            return (
                False,
                f"Invalid wisp '{value}'. Must be one of: {', '.join(VALID_BODY_WISP)}",
            )

    # Validate wisp-algorithm if present
    if "wisp-algorithm" in payload:
        value = payload.get("wisp-algorithm")
        if value and value not in VALID_BODY_WISP_ALGORITHM:
            return (
                False,
                f"Invalid wisp-algorithm '{value}'. Must be one of: {', '.join(VALID_BODY_WISP_ALGORITHM)}",
            )

    # Validate log-all-url if present
    if "log-all-url" in payload:
        value = payload.get("log-all-url")
        if value and value not in VALID_BODY_LOG_ALL_URL:
            return (
                False,
                f"Invalid log-all-url '{value}'. Must be one of: {', '.join(VALID_BODY_LOG_ALL_URL)}",
            )

    # Validate web-content-log if present
    if "web-content-log" in payload:
        value = payload.get("web-content-log")
        if value and value not in VALID_BODY_WEB_CONTENT_LOG:
            return (
                False,
                f"Invalid web-content-log '{value}'. Must be one of: {', '.join(VALID_BODY_WEB_CONTENT_LOG)}",
            )

    # Validate web-filter-activex-log if present
    if "web-filter-activex-log" in payload:
        value = payload.get("web-filter-activex-log")
        if value and value not in VALID_BODY_WEB_FILTER_ACTIVEX_LOG:
            return (
                False,
                f"Invalid web-filter-activex-log '{value}'. Must be one of: {', '.join(VALID_BODY_WEB_FILTER_ACTIVEX_LOG)}",
            )

    # Validate web-filter-command-block-log if present
    if "web-filter-command-block-log" in payload:
        value = payload.get("web-filter-command-block-log")
        if value and value not in VALID_BODY_WEB_FILTER_COMMAND_BLOCK_LOG:
            return (
                False,
                f"Invalid web-filter-command-block-log '{value}'. Must be one of: {', '.join(VALID_BODY_WEB_FILTER_COMMAND_BLOCK_LOG)}",
            )

    # Validate web-filter-cookie-log if present
    if "web-filter-cookie-log" in payload:
        value = payload.get("web-filter-cookie-log")
        if value and value not in VALID_BODY_WEB_FILTER_COOKIE_LOG:
            return (
                False,
                f"Invalid web-filter-cookie-log '{value}'. Must be one of: {', '.join(VALID_BODY_WEB_FILTER_COOKIE_LOG)}",
            )

    # Validate web-filter-applet-log if present
    if "web-filter-applet-log" in payload:
        value = payload.get("web-filter-applet-log")
        if value and value not in VALID_BODY_WEB_FILTER_APPLET_LOG:
            return (
                False,
                f"Invalid web-filter-applet-log '{value}'. Must be one of: {', '.join(VALID_BODY_WEB_FILTER_APPLET_LOG)}",
            )

    # Validate web-filter-jscript-log if present
    if "web-filter-jscript-log" in payload:
        value = payload.get("web-filter-jscript-log")
        if value and value not in VALID_BODY_WEB_FILTER_JSCRIPT_LOG:
            return (
                False,
                f"Invalid web-filter-jscript-log '{value}'. Must be one of: {', '.join(VALID_BODY_WEB_FILTER_JSCRIPT_LOG)}",
            )

    # Validate web-filter-js-log if present
    if "web-filter-js-log" in payload:
        value = payload.get("web-filter-js-log")
        if value and value not in VALID_BODY_WEB_FILTER_JS_LOG:
            return (
                False,
                f"Invalid web-filter-js-log '{value}'. Must be one of: {', '.join(VALID_BODY_WEB_FILTER_JS_LOG)}",
            )

    # Validate web-filter-vbs-log if present
    if "web-filter-vbs-log" in payload:
        value = payload.get("web-filter-vbs-log")
        if value and value not in VALID_BODY_WEB_FILTER_VBS_LOG:
            return (
                False,
                f"Invalid web-filter-vbs-log '{value}'. Must be one of: {', '.join(VALID_BODY_WEB_FILTER_VBS_LOG)}",
            )

    # Validate web-filter-unknown-log if present
    if "web-filter-unknown-log" in payload:
        value = payload.get("web-filter-unknown-log")
        if value and value not in VALID_BODY_WEB_FILTER_UNKNOWN_LOG:
            return (
                False,
                f"Invalid web-filter-unknown-log '{value}'. Must be one of: {', '.join(VALID_BODY_WEB_FILTER_UNKNOWN_LOG)}",
            )

    # Validate web-filter-referer-log if present
    if "web-filter-referer-log" in payload:
        value = payload.get("web-filter-referer-log")
        if value and value not in VALID_BODY_WEB_FILTER_REFERER_LOG:
            return (
                False,
                f"Invalid web-filter-referer-log '{value}'. Must be one of: {', '.join(VALID_BODY_WEB_FILTER_REFERER_LOG)}",
            )

    # Validate web-filter-cookie-removal-log if present
    if "web-filter-cookie-removal-log" in payload:
        value = payload.get("web-filter-cookie-removal-log")
        if value and value not in VALID_BODY_WEB_FILTER_COOKIE_REMOVAL_LOG:
            return (
                False,
                f"Invalid web-filter-cookie-removal-log '{value}'. Must be one of: {', '.join(VALID_BODY_WEB_FILTER_COOKIE_REMOVAL_LOG)}",
            )

    # Validate web-url-log if present
    if "web-url-log" in payload:
        value = payload.get("web-url-log")
        if value and value not in VALID_BODY_WEB_URL_LOG:
            return (
                False,
                f"Invalid web-url-log '{value}'. Must be one of: {', '.join(VALID_BODY_WEB_URL_LOG)}",
            )

    # Validate web-invalid-domain-log if present
    if "web-invalid-domain-log" in payload:
        value = payload.get("web-invalid-domain-log")
        if value and value not in VALID_BODY_WEB_INVALID_DOMAIN_LOG:
            return (
                False,
                f"Invalid web-invalid-domain-log '{value}'. Must be one of: {', '.join(VALID_BODY_WEB_INVALID_DOMAIN_LOG)}",
            )

    # Validate web-ftgd-err-log if present
    if "web-ftgd-err-log" in payload:
        value = payload.get("web-ftgd-err-log")
        if value and value not in VALID_BODY_WEB_FTGD_ERR_LOG:
            return (
                False,
                f"Invalid web-ftgd-err-log '{value}'. Must be one of: {', '.join(VALID_BODY_WEB_FTGD_ERR_LOG)}",
            )

    # Validate web-ftgd-quota-usage if present
    if "web-ftgd-quota-usage" in payload:
        value = payload.get("web-ftgd-quota-usage")
        if value and value not in VALID_BODY_WEB_FTGD_QUOTA_USAGE:
            return (
                False,
                f"Invalid web-ftgd-quota-usage '{value}'. Must be one of: {', '.join(VALID_BODY_WEB_FTGD_QUOTA_USAGE)}",
            )

    # Validate extended-log if present
    if "extended-log" in payload:
        value = payload.get("extended-log")
        if value and value not in VALID_BODY_EXTENDED_LOG:
            return (
                False,
                f"Invalid extended-log '{value}'. Must be one of: {', '.join(VALID_BODY_EXTENDED_LOG)}",
            )

    # Validate web-extended-all-action-log if present
    if "web-extended-all-action-log" in payload:
        value = payload.get("web-extended-all-action-log")
        if value and value not in VALID_BODY_WEB_EXTENDED_ALL_ACTION_LOG:
            return (
                False,
                f"Invalid web-extended-all-action-log '{value}'. Must be one of: {', '.join(VALID_BODY_WEB_EXTENDED_ALL_ACTION_LOG)}",
            )

    # Validate web-antiphishing-log if present
    if "web-antiphishing-log" in payload:
        value = payload.get("web-antiphishing-log")
        if value and value not in VALID_BODY_WEB_ANTIPHISHING_LOG:
            return (
                False,
                f"Invalid web-antiphishing-log '{value}'. Must be one of: {', '.join(VALID_BODY_WEB_ANTIPHISHING_LOG)}",
            )

    return (True, None)


# ============================================================================
# DELETE Validation
# ============================================================================


def validate_profile_delete(
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
