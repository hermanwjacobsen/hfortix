"""
Validation helpers for extension-controller dataplan endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_MODEM_ID = ["modem1", "modem2", "all"]
VALID_BODY_TYPE = ["carrier", "slot", "iccid", "generic"]
VALID_BODY_SLOT = ["sim1", "sim2"]
VALID_BODY_AUTH_TYPE = ["none", "pap", "chap"]
VALID_BODY_PDN = ["ipv4-only", "ipv6-only", "ipv4-ipv6"]
VALID_BODY_OVERAGE = ["disable", "enable"]
VALID_BODY_PRIVATE_NETWORK = ["disable", "enable"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_dataplan_get(
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


def validate_dataplan_post(payload: dict[str, Any]) -> tuple[bool, str | None]:
    """
    Validate POST request payload for creating dataplan.

    Args:
        payload: The payload to validate

    Returns:
        Tuple of (is_valid, error_message)
    """
    # Validate name if present
    if "name" in payload:
        value = payload.get("name")
        if value and isinstance(value, str) and len(value) > 31:
            return (False, "name cannot exceed 31 characters")

    # Validate modem-id if present
    if "modem-id" in payload:
        value = payload.get("modem-id")
        if value and value not in VALID_BODY_MODEM_ID:
            return (
                False,
                f"Invalid modem-id '{value}'. Must be one of: {', '.join(VALID_BODY_MODEM_ID)}",
            )

    # Validate type if present
    if "type" in payload:
        value = payload.get("type")
        if value and value not in VALID_BODY_TYPE:
            return (
                False,
                f"Invalid type '{value}'. Must be one of: {', '.join(VALID_BODY_TYPE)}",
            )

    # Validate slot if present
    if "slot" in payload:
        value = payload.get("slot")
        if value and value not in VALID_BODY_SLOT:
            return (
                False,
                f"Invalid slot '{value}'. Must be one of: {', '.join(VALID_BODY_SLOT)}",
            )

    # Validate iccid if present
    if "iccid" in payload:
        value = payload.get("iccid")
        if value and isinstance(value, str) and len(value) > 31:
            return (False, "iccid cannot exceed 31 characters")

    # Validate carrier if present
    if "carrier" in payload:
        value = payload.get("carrier")
        if value and isinstance(value, str) and len(value) > 31:
            return (False, "carrier cannot exceed 31 characters")

    # Validate apn if present
    if "apn" in payload:
        value = payload.get("apn")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "apn cannot exceed 63 characters")

    # Validate auth-type if present
    if "auth-type" in payload:
        value = payload.get("auth-type")
        if value and value not in VALID_BODY_AUTH_TYPE:
            return (
                False,
                f"Invalid auth-type '{value}'. Must be one of: {', '.join(VALID_BODY_AUTH_TYPE)}",
            )

    # Validate username if present
    if "username" in payload:
        value = payload.get("username")
        if value and isinstance(value, str) and len(value) > 127:
            return (False, "username cannot exceed 127 characters")

    # Validate pdn if present
    if "pdn" in payload:
        value = payload.get("pdn")
        if value and value not in VALID_BODY_PDN:
            return (
                False,
                f"Invalid pdn '{value}'. Must be one of: {', '.join(VALID_BODY_PDN)}",
            )

    # Validate signal-threshold if present
    if "signal-threshold" in payload:
        value = payload.get("signal-threshold")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 50 or int_val > 100:
                    return (
                        False,
                        "signal-threshold must be between 50 and 100",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"signal-threshold must be numeric, got: {value}",
                )

    # Validate signal-period if present
    if "signal-period" in payload:
        value = payload.get("signal-period")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 600 or int_val > 18000:
                    return (
                        False,
                        "signal-period must be between 600 and 18000",
                    )
            except (ValueError, TypeError):
                return (False, f"signal-period must be numeric, got: {value}")

    # Validate capacity if present
    if "capacity" in payload:
        value = payload.get("capacity")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 102400000:
                    return (False, "capacity must be between 0 and 102400000")
            except (ValueError, TypeError):
                return (False, f"capacity must be numeric, got: {value}")

    # Validate monthly-fee if present
    if "monthly-fee" in payload:
        value = payload.get("monthly-fee")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 1000000:
                    return (
                        False,
                        "monthly-fee must be between 0 and 1000000",
                    )
            except (ValueError, TypeError):
                return (False, f"monthly-fee must be numeric, got: {value}")

    # Validate billing-date if present
    if "billing-date" in payload:
        value = payload.get("billing-date")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 31:
                    return (False, "billing-date must be between 1 and 31")
            except (ValueError, TypeError):
                return (False, f"billing-date must be numeric, got: {value}")

    # Validate overage if present
    if "overage" in payload:
        value = payload.get("overage")
        if value and value not in VALID_BODY_OVERAGE:
            return (
                False,
                f"Invalid overage '{value}'. Must be one of: {', '.join(VALID_BODY_OVERAGE)}",
            )

    # Validate preferred-subnet if present
    if "preferred-subnet" in payload:
        value = payload.get("preferred-subnet")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 32:
                    return (
                        False,
                        "preferred-subnet must be between 0 and 32",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"preferred-subnet must be numeric, got: {value}",
                )

    # Validate private-network if present
    if "private-network" in payload:
        value = payload.get("private-network")
        if value and value not in VALID_BODY_PRIVATE_NETWORK:
            return (
                False,
                f"Invalid private-network '{value}'. Must be one of: {', '.join(VALID_BODY_PRIVATE_NETWORK)}",
            )

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_dataplan_put(
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
        if value and isinstance(value, str) and len(value) > 31:
            return (False, "name cannot exceed 31 characters")

    # Validate modem-id if present
    if "modem-id" in payload:
        value = payload.get("modem-id")
        if value and value not in VALID_BODY_MODEM_ID:
            return (
                False,
                f"Invalid modem-id '{value}'. Must be one of: {', '.join(VALID_BODY_MODEM_ID)}",
            )

    # Validate type if present
    if "type" in payload:
        value = payload.get("type")
        if value and value not in VALID_BODY_TYPE:
            return (
                False,
                f"Invalid type '{value}'. Must be one of: {', '.join(VALID_BODY_TYPE)}",
            )

    # Validate slot if present
    if "slot" in payload:
        value = payload.get("slot")
        if value and value not in VALID_BODY_SLOT:
            return (
                False,
                f"Invalid slot '{value}'. Must be one of: {', '.join(VALID_BODY_SLOT)}",
            )

    # Validate iccid if present
    if "iccid" in payload:
        value = payload.get("iccid")
        if value and isinstance(value, str) and len(value) > 31:
            return (False, "iccid cannot exceed 31 characters")

    # Validate carrier if present
    if "carrier" in payload:
        value = payload.get("carrier")
        if value and isinstance(value, str) and len(value) > 31:
            return (False, "carrier cannot exceed 31 characters")

    # Validate apn if present
    if "apn" in payload:
        value = payload.get("apn")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "apn cannot exceed 63 characters")

    # Validate auth-type if present
    if "auth-type" in payload:
        value = payload.get("auth-type")
        if value and value not in VALID_BODY_AUTH_TYPE:
            return (
                False,
                f"Invalid auth-type '{value}'. Must be one of: {', '.join(VALID_BODY_AUTH_TYPE)}",
            )

    # Validate username if present
    if "username" in payload:
        value = payload.get("username")
        if value and isinstance(value, str) and len(value) > 127:
            return (False, "username cannot exceed 127 characters")

    # Validate pdn if present
    if "pdn" in payload:
        value = payload.get("pdn")
        if value and value not in VALID_BODY_PDN:
            return (
                False,
                f"Invalid pdn '{value}'. Must be one of: {', '.join(VALID_BODY_PDN)}",
            )

    # Validate signal-threshold if present
    if "signal-threshold" in payload:
        value = payload.get("signal-threshold")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 50 or int_val > 100:
                    return (
                        False,
                        "signal-threshold must be between 50 and 100",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"signal-threshold must be numeric, got: {value}",
                )

    # Validate signal-period if present
    if "signal-period" in payload:
        value = payload.get("signal-period")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 600 or int_val > 18000:
                    return (
                        False,
                        "signal-period must be between 600 and 18000",
                    )
            except (ValueError, TypeError):
                return (False, f"signal-period must be numeric, got: {value}")

    # Validate capacity if present
    if "capacity" in payload:
        value = payload.get("capacity")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 102400000:
                    return (False, "capacity must be between 0 and 102400000")
            except (ValueError, TypeError):
                return (False, f"capacity must be numeric, got: {value}")

    # Validate monthly-fee if present
    if "monthly-fee" in payload:
        value = payload.get("monthly-fee")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 1000000:
                    return (
                        False,
                        "monthly-fee must be between 0 and 1000000",
                    )
            except (ValueError, TypeError):
                return (False, f"monthly-fee must be numeric, got: {value}")

    # Validate billing-date if present
    if "billing-date" in payload:
        value = payload.get("billing-date")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 31:
                    return (False, "billing-date must be between 1 and 31")
            except (ValueError, TypeError):
                return (False, f"billing-date must be numeric, got: {value}")

    # Validate overage if present
    if "overage" in payload:
        value = payload.get("overage")
        if value and value not in VALID_BODY_OVERAGE:
            return (
                False,
                f"Invalid overage '{value}'. Must be one of: {', '.join(VALID_BODY_OVERAGE)}",
            )

    # Validate preferred-subnet if present
    if "preferred-subnet" in payload:
        value = payload.get("preferred-subnet")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 32:
                    return (
                        False,
                        "preferred-subnet must be between 0 and 32",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"preferred-subnet must be numeric, got: {value}",
                )

    # Validate private-network if present
    if "private-network" in payload:
        value = payload.get("private-network")
        if value and value not in VALID_BODY_PRIVATE_NETWORK:
            return (
                False,
                f"Invalid private-network '{value}'. Must be one of: {', '.join(VALID_BODY_PRIVATE_NETWORK)}",
            )

    return (True, None)


# ============================================================================
# DELETE Validation
# ============================================================================


def validate_dataplan_delete(
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
