"""
Validation helpers for user nac_policy endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_CATEGORY = [
    "device",
    "firewall-user",
    "ems-tag",
    "fortivoice-tag",
    "vulnerability",
]
VALID_BODY_STATUS = ["enable", "disable"]
VALID_BODY_MATCH_TYPE = ["dynamic", "override"]
VALID_BODY_MATCH_REMOVE = ["default", "link-down"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_nac_policy_get(
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


def validate_nac_policy_post(
    payload: dict[str, Any],
) -> tuple[bool, str | None]:
    """
    Validate POST request payload for creating nac_policy.

    Args:
        payload: The payload to validate

    Returns:
        Tuple of (is_valid, error_message)
    """
    # Validate name if present
    if "name" in payload:
        value = payload.get("name")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "name cannot exceed 63 characters")

    # Validate description if present
    if "description" in payload:
        value = payload.get("description")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "description cannot exceed 63 characters")

    # Validate category if present
    if "category" in payload:
        value = payload.get("category")
        if value and value not in VALID_BODY_CATEGORY:
            return (
                False,
                f"Invalid category '{value}'. Must be one of: {', '.join(VALID_BODY_CATEGORY)}",
            )

    # Validate status if present
    if "status" in payload:
        value = payload.get("status")
        if value and value not in VALID_BODY_STATUS:
            return (
                False,
                f"Invalid status '{value}'. Must be one of: {', '.join(VALID_BODY_STATUS)}",
            )

    # Validate match-type if present
    if "match-type" in payload:
        value = payload.get("match-type")
        if value and value not in VALID_BODY_MATCH_TYPE:
            return (
                False,
                f"Invalid match-type '{value}'. Must be one of: {', '.join(VALID_BODY_MATCH_TYPE)}",
            )

    # Validate match-period if present
    if "match-period" in payload:
        value = payload.get("match-period")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 120:
                    return (False, "match-period must be between 0 and 120")
            except (ValueError, TypeError):
                return (False, f"match-period must be numeric, got: {value}")

    # Validate match-remove if present
    if "match-remove" in payload:
        value = payload.get("match-remove")
        if value and value not in VALID_BODY_MATCH_REMOVE:
            return (
                False,
                f"Invalid match-remove '{value}'. Must be one of: {', '.join(VALID_BODY_MATCH_REMOVE)}",
            )

    # Validate mac if present
    if "mac" in payload:
        value = payload.get("mac")
        if value and isinstance(value, str) and len(value) > 17:
            return (False, "mac cannot exceed 17 characters")

    # Validate hw-vendor if present
    if "hw-vendor" in payload:
        value = payload.get("hw-vendor")
        if value and isinstance(value, str) and len(value) > 15:
            return (False, "hw-vendor cannot exceed 15 characters")

    # Validate type if present
    if "type" in payload:
        value = payload.get("type")
        if value and isinstance(value, str) and len(value) > 15:
            return (False, "type cannot exceed 15 characters")

    # Validate family if present
    if "family" in payload:
        value = payload.get("family")
        if value and isinstance(value, str) and len(value) > 31:
            return (False, "family cannot exceed 31 characters")

    # Validate os if present
    if "os" in payload:
        value = payload.get("os")
        if value and isinstance(value, str) and len(value) > 31:
            return (False, "os cannot exceed 31 characters")

    # Validate hw-version if present
    if "hw-version" in payload:
        value = payload.get("hw-version")
        if value and isinstance(value, str) and len(value) > 15:
            return (False, "hw-version cannot exceed 15 characters")

    # Validate sw-version if present
    if "sw-version" in payload:
        value = payload.get("sw-version")
        if value and isinstance(value, str) and len(value) > 15:
            return (False, "sw-version cannot exceed 15 characters")

    # Validate host if present
    if "host" in payload:
        value = payload.get("host")
        if value and isinstance(value, str) and len(value) > 64:
            return (False, "host cannot exceed 64 characters")

    # Validate user if present
    if "user" in payload:
        value = payload.get("user")
        if value and isinstance(value, str) and len(value) > 64:
            return (False, "user cannot exceed 64 characters")

    # Validate src if present
    if "src" in payload:
        value = payload.get("src")
        if value and isinstance(value, str) and len(value) > 15:
            return (False, "src cannot exceed 15 characters")

    # Validate user-group if present
    if "user-group" in payload:
        value = payload.get("user-group")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "user-group cannot exceed 35 characters")

    # Validate ems-tag if present
    if "ems-tag" in payload:
        value = payload.get("ems-tag")
        if value and isinstance(value, str) and len(value) > 79:
            return (False, "ems-tag cannot exceed 79 characters")

    # Validate fortivoice-tag if present
    if "fortivoice-tag" in payload:
        value = payload.get("fortivoice-tag")
        if value and isinstance(value, str) and len(value) > 79:
            return (False, "fortivoice-tag cannot exceed 79 characters")

    # Validate switch-fortilink if present
    if "switch-fortilink" in payload:
        value = payload.get("switch-fortilink")
        if value and isinstance(value, str) and len(value) > 15:
            return (False, "switch-fortilink cannot exceed 15 characters")

    # Validate switch-mac-policy if present
    if "switch-mac-policy" in payload:
        value = payload.get("switch-mac-policy")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "switch-mac-policy cannot exceed 63 characters")

    # Validate firewall-address if present
    if "firewall-address" in payload:
        value = payload.get("firewall-address")
        if value and isinstance(value, str) and len(value) > 79:
            return (False, "firewall-address cannot exceed 79 characters")

    # Validate ssid-policy if present
    if "ssid-policy" in payload:
        value = payload.get("ssid-policy")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "ssid-policy cannot exceed 35 characters")

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_nac_policy_put(
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
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "name cannot exceed 63 characters")

    # Validate description if present
    if "description" in payload:
        value = payload.get("description")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "description cannot exceed 63 characters")

    # Validate category if present
    if "category" in payload:
        value = payload.get("category")
        if value and value not in VALID_BODY_CATEGORY:
            return (
                False,
                f"Invalid category '{value}'. Must be one of: {', '.join(VALID_BODY_CATEGORY)}",
            )

    # Validate status if present
    if "status" in payload:
        value = payload.get("status")
        if value and value not in VALID_BODY_STATUS:
            return (
                False,
                f"Invalid status '{value}'. Must be one of: {', '.join(VALID_BODY_STATUS)}",
            )

    # Validate match-type if present
    if "match-type" in payload:
        value = payload.get("match-type")
        if value and value not in VALID_BODY_MATCH_TYPE:
            return (
                False,
                f"Invalid match-type '{value}'. Must be one of: {', '.join(VALID_BODY_MATCH_TYPE)}",
            )

    # Validate match-period if present
    if "match-period" in payload:
        value = payload.get("match-period")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 120:
                    return (False, "match-period must be between 0 and 120")
            except (ValueError, TypeError):
                return (False, f"match-period must be numeric, got: {value}")

    # Validate match-remove if present
    if "match-remove" in payload:
        value = payload.get("match-remove")
        if value and value not in VALID_BODY_MATCH_REMOVE:
            return (
                False,
                f"Invalid match-remove '{value}'. Must be one of: {', '.join(VALID_BODY_MATCH_REMOVE)}",
            )

    # Validate mac if present
    if "mac" in payload:
        value = payload.get("mac")
        if value and isinstance(value, str) and len(value) > 17:
            return (False, "mac cannot exceed 17 characters")

    # Validate hw-vendor if present
    if "hw-vendor" in payload:
        value = payload.get("hw-vendor")
        if value and isinstance(value, str) and len(value) > 15:
            return (False, "hw-vendor cannot exceed 15 characters")

    # Validate type if present
    if "type" in payload:
        value = payload.get("type")
        if value and isinstance(value, str) and len(value) > 15:
            return (False, "type cannot exceed 15 characters")

    # Validate family if present
    if "family" in payload:
        value = payload.get("family")
        if value and isinstance(value, str) and len(value) > 31:
            return (False, "family cannot exceed 31 characters")

    # Validate os if present
    if "os" in payload:
        value = payload.get("os")
        if value and isinstance(value, str) and len(value) > 31:
            return (False, "os cannot exceed 31 characters")

    # Validate hw-version if present
    if "hw-version" in payload:
        value = payload.get("hw-version")
        if value and isinstance(value, str) and len(value) > 15:
            return (False, "hw-version cannot exceed 15 characters")

    # Validate sw-version if present
    if "sw-version" in payload:
        value = payload.get("sw-version")
        if value and isinstance(value, str) and len(value) > 15:
            return (False, "sw-version cannot exceed 15 characters")

    # Validate host if present
    if "host" in payload:
        value = payload.get("host")
        if value and isinstance(value, str) and len(value) > 64:
            return (False, "host cannot exceed 64 characters")

    # Validate user if present
    if "user" in payload:
        value = payload.get("user")
        if value and isinstance(value, str) and len(value) > 64:
            return (False, "user cannot exceed 64 characters")

    # Validate src if present
    if "src" in payload:
        value = payload.get("src")
        if value and isinstance(value, str) and len(value) > 15:
            return (False, "src cannot exceed 15 characters")

    # Validate user-group if present
    if "user-group" in payload:
        value = payload.get("user-group")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "user-group cannot exceed 35 characters")

    # Validate ems-tag if present
    if "ems-tag" in payload:
        value = payload.get("ems-tag")
        if value and isinstance(value, str) and len(value) > 79:
            return (False, "ems-tag cannot exceed 79 characters")

    # Validate fortivoice-tag if present
    if "fortivoice-tag" in payload:
        value = payload.get("fortivoice-tag")
        if value and isinstance(value, str) and len(value) > 79:
            return (False, "fortivoice-tag cannot exceed 79 characters")

    # Validate switch-fortilink if present
    if "switch-fortilink" in payload:
        value = payload.get("switch-fortilink")
        if value and isinstance(value, str) and len(value) > 15:
            return (False, "switch-fortilink cannot exceed 15 characters")

    # Validate switch-mac-policy if present
    if "switch-mac-policy" in payload:
        value = payload.get("switch-mac-policy")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "switch-mac-policy cannot exceed 63 characters")

    # Validate firewall-address if present
    if "firewall-address" in payload:
        value = payload.get("firewall-address")
        if value and isinstance(value, str) and len(value) > 79:
            return (False, "firewall-address cannot exceed 79 characters")

    # Validate ssid-policy if present
    if "ssid-policy" in payload:
        value = payload.get("ssid-policy")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "ssid-policy cannot exceed 35 characters")

    return (True, None)


# ============================================================================
# DELETE Validation
# ============================================================================


def validate_nac_policy_delete(
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
