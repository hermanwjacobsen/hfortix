"""
Validation helpers for system automation_action endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_ACTION_TYPE = [
    "email",
    "fortiexplorer-notification",
    "alert",
    "disable-ssid",
    "system-actions",
    "quarantine",
    "quarantine-forticlient",
    "quarantine-nsx",
    "quarantine-fortinac",
    "ban-ip",
    "aws-lambda",
    "azure-function",
    "google-cloud-function",
    "alicloud-function",
    "webhook",
    "cli-script",
    "diagnose-script",
    "regular-expression",
    "slack-notification",
    "microsoft-teams-notification",
]
VALID_BODY_SYSTEM_ACTION = ["reboot", "shutdown", "backup-config"]
VALID_BODY_FORTICARE_EMAIL = ["enable", "disable"]
VALID_BODY_AZURE_FUNCTION_AUTHORIZATION = ["anonymous", "function", "admin"]
VALID_BODY_ALICLOUD_FUNCTION_AUTHORIZATION = ["anonymous", "function"]
VALID_BODY_MESSAGE_TYPE = ["text", "json", "form-data"]
VALID_BODY_REPLACEMENT_MESSAGE = ["enable", "disable"]
VALID_BODY_PROTOCOL = ["http", "https"]
VALID_BODY_METHOD = ["post", "put", "get", "patch", "delete"]
VALID_BODY_VERIFY_HOST_CERT = ["enable", "disable"]
VALID_BODY_FILE_ONLY = ["enable", "disable"]
VALID_BODY_EXECUTE_SECURITY_FABRIC = ["enable", "disable"]
VALID_BODY_LOG_DEBUG_PRINT = ["enable", "disable"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_automation_action_get(
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


def validate_automation_action_post(
    payload: dict[str, Any],
) -> tuple[bool, str | None]:
    """
    Validate POST request payload for creating automation_action.

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

    # Validate description if present
    if "description" in payload:
        value = payload.get("description")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "description cannot exceed 255 characters")

    # Validate action-type if present
    if "action-type" in payload:
        value = payload.get("action-type")
        if value and value not in VALID_BODY_ACTION_TYPE:
            return (
                False,
                f"Invalid action-type '{value}'. Must be one of: {', '.join(VALID_BODY_ACTION_TYPE)}",
            )

    # Validate system-action if present
    if "system-action" in payload:
        value = payload.get("system-action")
        if value and value not in VALID_BODY_SYSTEM_ACTION:
            return (
                False,
                f"Invalid system-action '{value}'. Must be one of: {', '.join(VALID_BODY_SYSTEM_ACTION)}",
            )

    # Validate tls-certificate if present
    if "tls-certificate" in payload:
        value = payload.get("tls-certificate")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "tls-certificate cannot exceed 35 characters")

    # Validate forticare-email if present
    if "forticare-email" in payload:
        value = payload.get("forticare-email")
        if value and value not in VALID_BODY_FORTICARE_EMAIL:
            return (
                False,
                f"Invalid forticare-email '{value}'. Must be one of: {', '.join(VALID_BODY_FORTICARE_EMAIL)}",
            )

    # Validate email-from if present
    if "email-from" in payload:
        value = payload.get("email-from")
        if value and isinstance(value, str) and len(value) > 127:
            return (False, "email-from cannot exceed 127 characters")

    # Validate email-subject if present
    if "email-subject" in payload:
        value = payload.get("email-subject")
        if value and isinstance(value, str) and len(value) > 511:
            return (False, "email-subject cannot exceed 511 characters")

    # Validate minimum-interval if present
    if "minimum-interval" in payload:
        value = payload.get("minimum-interval")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 2592000:
                    return (
                        False,
                        "minimum-interval must be between 0 and 2592000",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"minimum-interval must be numeric, got: {value}",
                )

    # Validate azure-function-authorization if present
    if "azure-function-authorization" in payload:
        value = payload.get("azure-function-authorization")
        if value and value not in VALID_BODY_AZURE_FUNCTION_AUTHORIZATION:
            return (
                False,
                f"Invalid azure-function-authorization '{value}'. Must be one of: {', '.join(VALID_BODY_AZURE_FUNCTION_AUTHORIZATION)}",
            )

    # Validate alicloud-function-authorization if present
    if "alicloud-function-authorization" in payload:
        value = payload.get("alicloud-function-authorization")
        if value and value not in VALID_BODY_ALICLOUD_FUNCTION_AUTHORIZATION:
            return (
                False,
                f"Invalid alicloud-function-authorization '{value}'. Must be one of: {', '.join(VALID_BODY_ALICLOUD_FUNCTION_AUTHORIZATION)}",
            )

    # Validate alicloud-access-key-id if present
    if "alicloud-access-key-id" in payload:
        value = payload.get("alicloud-access-key-id")
        if value and isinstance(value, str) and len(value) > 35:
            return (
                False,
                "alicloud-access-key-id cannot exceed 35 characters",
            )

    # Validate message-type if present
    if "message-type" in payload:
        value = payload.get("message-type")
        if value and value not in VALID_BODY_MESSAGE_TYPE:
            return (
                False,
                f"Invalid message-type '{value}'. Must be one of: {', '.join(VALID_BODY_MESSAGE_TYPE)}",
            )

    # Validate message if present
    if "message" in payload:
        value = payload.get("message")
        if value and isinstance(value, str) and len(value) > 4095:
            return (False, "message cannot exceed 4095 characters")

    # Validate replacement-message if present
    if "replacement-message" in payload:
        value = payload.get("replacement-message")
        if value and value not in VALID_BODY_REPLACEMENT_MESSAGE:
            return (
                False,
                f"Invalid replacement-message '{value}'. Must be one of: {', '.join(VALID_BODY_REPLACEMENT_MESSAGE)}",
            )

    # Validate replacemsg-group if present
    if "replacemsg-group" in payload:
        value = payload.get("replacemsg-group")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "replacemsg-group cannot exceed 35 characters")

    # Validate protocol if present
    if "protocol" in payload:
        value = payload.get("protocol")
        if value and value not in VALID_BODY_PROTOCOL:
            return (
                False,
                f"Invalid protocol '{value}'. Must be one of: {', '.join(VALID_BODY_PROTOCOL)}",
            )

    # Validate method if present
    if "method" in payload:
        value = payload.get("method")
        if value and value not in VALID_BODY_METHOD:
            return (
                False,
                f"Invalid method '{value}'. Must be one of: {', '.join(VALID_BODY_METHOD)}",
            )

    # Validate uri if present
    if "uri" in payload:
        value = payload.get("uri")
        if value and isinstance(value, str) and len(value) > 1023:
            return (False, "uri cannot exceed 1023 characters")

    # Validate http-body if present
    if "http-body" in payload:
        value = payload.get("http-body")
        if value and isinstance(value, str) and len(value) > 4095:
            return (False, "http-body cannot exceed 4095 characters")

    # Validate port if present
    if "port" in payload:
        value = payload.get("port")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 65535:
                    return (False, "port must be between 1 and 65535")
            except (ValueError, TypeError):
                return (False, f"port must be numeric, got: {value}")

    # Validate verify-host-cert if present
    if "verify-host-cert" in payload:
        value = payload.get("verify-host-cert")
        if value and value not in VALID_BODY_VERIFY_HOST_CERT:
            return (
                False,
                f"Invalid verify-host-cert '{value}'. Must be one of: {', '.join(VALID_BODY_VERIFY_HOST_CERT)}",
            )

    # Validate script if present
    if "script" in payload:
        value = payload.get("script")
        if value and isinstance(value, str) and len(value) > 1023:
            return (False, "script cannot exceed 1023 characters")

    # Validate output-size if present
    if "output-size" in payload:
        value = payload.get("output-size")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 1024:
                    return (False, "output-size must be between 1 and 1024")
            except (ValueError, TypeError):
                return (False, f"output-size must be numeric, got: {value}")

    # Validate timeout if present
    if "timeout" in payload:
        value = payload.get("timeout")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 300:
                    return (False, "timeout must be between 0 and 300")
            except (ValueError, TypeError):
                return (False, f"timeout must be numeric, got: {value}")

    # Validate duration if present
    if "duration" in payload:
        value = payload.get("duration")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 36000:
                    return (False, "duration must be between 1 and 36000")
            except (ValueError, TypeError):
                return (False, f"duration must be numeric, got: {value}")

    # Validate output-interval if present
    if "output-interval" in payload:
        value = payload.get("output-interval")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 36000:
                    return (
                        False,
                        "output-interval must be between 0 and 36000",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"output-interval must be numeric, got: {value}",
                )

    # Validate file-only if present
    if "file-only" in payload:
        value = payload.get("file-only")
        if value and value not in VALID_BODY_FILE_ONLY:
            return (
                False,
                f"Invalid file-only '{value}'. Must be one of: {', '.join(VALID_BODY_FILE_ONLY)}",
            )

    # Validate execute-security-fabric if present
    if "execute-security-fabric" in payload:
        value = payload.get("execute-security-fabric")
        if value and value not in VALID_BODY_EXECUTE_SECURITY_FABRIC:
            return (
                False,
                f"Invalid execute-security-fabric '{value}'. Must be one of: {', '.join(VALID_BODY_EXECUTE_SECURITY_FABRIC)}",
            )

    # Validate accprofile if present
    if "accprofile" in payload:
        value = payload.get("accprofile")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "accprofile cannot exceed 35 characters")

    # Validate regular-expression if present
    if "regular-expression" in payload:
        value = payload.get("regular-expression")
        if value and isinstance(value, str) and len(value) > 1023:
            return (False, "regular-expression cannot exceed 1023 characters")

    # Validate log-debug-print if present
    if "log-debug-print" in payload:
        value = payload.get("log-debug-print")
        if value and value not in VALID_BODY_LOG_DEBUG_PRINT:
            return (
                False,
                f"Invalid log-debug-print '{value}'. Must be one of: {', '.join(VALID_BODY_LOG_DEBUG_PRINT)}",
            )

    # Validate security-tag if present
    if "security-tag" in payload:
        value = payload.get("security-tag")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "security-tag cannot exceed 255 characters")

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_automation_action_put(
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

    # Validate description if present
    if "description" in payload:
        value = payload.get("description")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "description cannot exceed 255 characters")

    # Validate action-type if present
    if "action-type" in payload:
        value = payload.get("action-type")
        if value and value not in VALID_BODY_ACTION_TYPE:
            return (
                False,
                f"Invalid action-type '{value}'. Must be one of: {', '.join(VALID_BODY_ACTION_TYPE)}",
            )

    # Validate system-action if present
    if "system-action" in payload:
        value = payload.get("system-action")
        if value and value not in VALID_BODY_SYSTEM_ACTION:
            return (
                False,
                f"Invalid system-action '{value}'. Must be one of: {', '.join(VALID_BODY_SYSTEM_ACTION)}",
            )

    # Validate tls-certificate if present
    if "tls-certificate" in payload:
        value = payload.get("tls-certificate")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "tls-certificate cannot exceed 35 characters")

    # Validate forticare-email if present
    if "forticare-email" in payload:
        value = payload.get("forticare-email")
        if value and value not in VALID_BODY_FORTICARE_EMAIL:
            return (
                False,
                f"Invalid forticare-email '{value}'. Must be one of: {', '.join(VALID_BODY_FORTICARE_EMAIL)}",
            )

    # Validate email-from if present
    if "email-from" in payload:
        value = payload.get("email-from")
        if value and isinstance(value, str) and len(value) > 127:
            return (False, "email-from cannot exceed 127 characters")

    # Validate email-subject if present
    if "email-subject" in payload:
        value = payload.get("email-subject")
        if value and isinstance(value, str) and len(value) > 511:
            return (False, "email-subject cannot exceed 511 characters")

    # Validate minimum-interval if present
    if "minimum-interval" in payload:
        value = payload.get("minimum-interval")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 2592000:
                    return (
                        False,
                        "minimum-interval must be between 0 and 2592000",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"minimum-interval must be numeric, got: {value}",
                )

    # Validate azure-function-authorization if present
    if "azure-function-authorization" in payload:
        value = payload.get("azure-function-authorization")
        if value and value not in VALID_BODY_AZURE_FUNCTION_AUTHORIZATION:
            return (
                False,
                f"Invalid azure-function-authorization '{value}'. Must be one of: {', '.join(VALID_BODY_AZURE_FUNCTION_AUTHORIZATION)}",
            )

    # Validate alicloud-function-authorization if present
    if "alicloud-function-authorization" in payload:
        value = payload.get("alicloud-function-authorization")
        if value and value not in VALID_BODY_ALICLOUD_FUNCTION_AUTHORIZATION:
            return (
                False,
                f"Invalid alicloud-function-authorization '{value}'. Must be one of: {', '.join(VALID_BODY_ALICLOUD_FUNCTION_AUTHORIZATION)}",
            )

    # Validate alicloud-access-key-id if present
    if "alicloud-access-key-id" in payload:
        value = payload.get("alicloud-access-key-id")
        if value and isinstance(value, str) and len(value) > 35:
            return (
                False,
                "alicloud-access-key-id cannot exceed 35 characters",
            )

    # Validate message-type if present
    if "message-type" in payload:
        value = payload.get("message-type")
        if value and value not in VALID_BODY_MESSAGE_TYPE:
            return (
                False,
                f"Invalid message-type '{value}'. Must be one of: {', '.join(VALID_BODY_MESSAGE_TYPE)}",
            )

    # Validate message if present
    if "message" in payload:
        value = payload.get("message")
        if value and isinstance(value, str) and len(value) > 4095:
            return (False, "message cannot exceed 4095 characters")

    # Validate replacement-message if present
    if "replacement-message" in payload:
        value = payload.get("replacement-message")
        if value and value not in VALID_BODY_REPLACEMENT_MESSAGE:
            return (
                False,
                f"Invalid replacement-message '{value}'. Must be one of: {', '.join(VALID_BODY_REPLACEMENT_MESSAGE)}",
            )

    # Validate replacemsg-group if present
    if "replacemsg-group" in payload:
        value = payload.get("replacemsg-group")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "replacemsg-group cannot exceed 35 characters")

    # Validate protocol if present
    if "protocol" in payload:
        value = payload.get("protocol")
        if value and value not in VALID_BODY_PROTOCOL:
            return (
                False,
                f"Invalid protocol '{value}'. Must be one of: {', '.join(VALID_BODY_PROTOCOL)}",
            )

    # Validate method if present
    if "method" in payload:
        value = payload.get("method")
        if value and value not in VALID_BODY_METHOD:
            return (
                False,
                f"Invalid method '{value}'. Must be one of: {', '.join(VALID_BODY_METHOD)}",
            )

    # Validate uri if present
    if "uri" in payload:
        value = payload.get("uri")
        if value and isinstance(value, str) and len(value) > 1023:
            return (False, "uri cannot exceed 1023 characters")

    # Validate http-body if present
    if "http-body" in payload:
        value = payload.get("http-body")
        if value and isinstance(value, str) and len(value) > 4095:
            return (False, "http-body cannot exceed 4095 characters")

    # Validate port if present
    if "port" in payload:
        value = payload.get("port")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 65535:
                    return (False, "port must be between 1 and 65535")
            except (ValueError, TypeError):
                return (False, f"port must be numeric, got: {value}")

    # Validate verify-host-cert if present
    if "verify-host-cert" in payload:
        value = payload.get("verify-host-cert")
        if value and value not in VALID_BODY_VERIFY_HOST_CERT:
            return (
                False,
                f"Invalid verify-host-cert '{value}'. Must be one of: {', '.join(VALID_BODY_VERIFY_HOST_CERT)}",
            )

    # Validate script if present
    if "script" in payload:
        value = payload.get("script")
        if value and isinstance(value, str) and len(value) > 1023:
            return (False, "script cannot exceed 1023 characters")

    # Validate output-size if present
    if "output-size" in payload:
        value = payload.get("output-size")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 1024:
                    return (False, "output-size must be between 1 and 1024")
            except (ValueError, TypeError):
                return (False, f"output-size must be numeric, got: {value}")

    # Validate timeout if present
    if "timeout" in payload:
        value = payload.get("timeout")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 300:
                    return (False, "timeout must be between 0 and 300")
            except (ValueError, TypeError):
                return (False, f"timeout must be numeric, got: {value}")

    # Validate duration if present
    if "duration" in payload:
        value = payload.get("duration")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 36000:
                    return (False, "duration must be between 1 and 36000")
            except (ValueError, TypeError):
                return (False, f"duration must be numeric, got: {value}")

    # Validate output-interval if present
    if "output-interval" in payload:
        value = payload.get("output-interval")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 36000:
                    return (
                        False,
                        "output-interval must be between 0 and 36000",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"output-interval must be numeric, got: {value}",
                )

    # Validate file-only if present
    if "file-only" in payload:
        value = payload.get("file-only")
        if value and value not in VALID_BODY_FILE_ONLY:
            return (
                False,
                f"Invalid file-only '{value}'. Must be one of: {', '.join(VALID_BODY_FILE_ONLY)}",
            )

    # Validate execute-security-fabric if present
    if "execute-security-fabric" in payload:
        value = payload.get("execute-security-fabric")
        if value and value not in VALID_BODY_EXECUTE_SECURITY_FABRIC:
            return (
                False,
                f"Invalid execute-security-fabric '{value}'. Must be one of: {', '.join(VALID_BODY_EXECUTE_SECURITY_FABRIC)}",
            )

    # Validate accprofile if present
    if "accprofile" in payload:
        value = payload.get("accprofile")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "accprofile cannot exceed 35 characters")

    # Validate regular-expression if present
    if "regular-expression" in payload:
        value = payload.get("regular-expression")
        if value and isinstance(value, str) and len(value) > 1023:
            return (False, "regular-expression cannot exceed 1023 characters")

    # Validate log-debug-print if present
    if "log-debug-print" in payload:
        value = payload.get("log-debug-print")
        if value and value not in VALID_BODY_LOG_DEBUG_PRINT:
            return (
                False,
                f"Invalid log-debug-print '{value}'. Must be one of: {', '.join(VALID_BODY_LOG_DEBUG_PRINT)}",
            )

    # Validate security-tag if present
    if "security-tag" in payload:
        value = payload.get("security-tag")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "security-tag cannot exceed 255 characters")

    return (True, None)


# ============================================================================
# DELETE Validation
# ============================================================================


def validate_automation_action_delete(
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
