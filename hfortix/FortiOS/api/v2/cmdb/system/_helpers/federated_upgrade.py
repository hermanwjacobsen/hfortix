"""
Validation helpers for system federated_upgrade endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_STATUS = [
    "disabled",
    "initialized",
    "downloading",
    "device-disconnected",
    "ready",
    "coordinating",
    "staging",
    "final-check",
    "upgrade-devices",
    "cancelled",
    "confirmed",
    "done",
    "dry-run-done",
    "failed",
]
VALID_BODY_SOURCE = ["user", "auto-firmware-upgrade", "forced-upgrade"]
VALID_BODY_FAILURE_REASON = [
    "none",
    "internal",
    "timeout",
    "device-type-unsupported",
    "download-failed",
    "device-missing",
    "version-unavailable",
    "staging-failed",
    "reboot-failed",
    "device-not-reconnected",
    "node-not-ready",
    "no-final-confirmation",
    "no-confirmation-query",
    "config-error-log-nonempty",
    "csf-tree-not-supported",
    "firmware-changed",
    "node-failed",
    "image-missing",
]
VALID_BODY_IGNORE_SIGNING_ERRORS = ["enable", "disable"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_federated_upgrade_get(
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


def validate_federated_upgrade_put(
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

    # Validate source if present
    if "source" in payload:
        value = payload.get("source")
        if value and value not in VALID_BODY_SOURCE:
            return (
                False,
                f"Invalid source '{value}'. Must be one of: {', '.join(VALID_BODY_SOURCE)}",
            )

    # Validate failure-reason if present
    if "failure-reason" in payload:
        value = payload.get("failure-reason")
        if value and value not in VALID_BODY_FAILURE_REASON:
            return (
                False,
                f"Invalid failure-reason '{value}'. Must be one of: {', '.join(VALID_BODY_FAILURE_REASON)}",
            )

    # Validate failure-device if present
    if "failure-device" in payload:
        value = payload.get("failure-device")
        if value and isinstance(value, str) and len(value) > 79:
            return (False, "failure-device cannot exceed 79 characters")

    # Validate upgrade-id if present
    if "upgrade-id" in payload:
        value = payload.get("upgrade-id")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "upgrade-id must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (False, f"upgrade-id must be numeric, got: {value}")

    # Validate next-path-index if present
    if "next-path-index" in payload:
        value = payload.get("next-path-index")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 10:
                    return (False, "next-path-index must be between 0 and 10")
            except (ValueError, TypeError):
                return (
                    False,
                    f"next-path-index must be numeric, got: {value}",
                )

    # Validate ignore-signing-errors if present
    if "ignore-signing-errors" in payload:
        value = payload.get("ignore-signing-errors")
        if value and value not in VALID_BODY_IGNORE_SIGNING_ERRORS:
            return (
                False,
                f"Invalid ignore-signing-errors '{value}'. Must be one of: {', '.join(VALID_BODY_IGNORE_SIGNING_ERRORS)}",
            )

    # Validate ha-reboot-controller if present
    if "ha-reboot-controller" in payload:
        value = payload.get("ha-reboot-controller")
        if value and isinstance(value, str) and len(value) > 79:
            return (False, "ha-reboot-controller cannot exceed 79 characters")

    # Validate starter-admin if present
    if "starter-admin" in payload:
        value = payload.get("starter-admin")
        if value and isinstance(value, str) and len(value) > 64:
            return (False, "starter-admin cannot exceed 64 characters")

    return (True, None)
