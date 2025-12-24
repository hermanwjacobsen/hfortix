"""
Validation helpers for system modem endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_STATUS = ["enable", "disable"]
VALID_BODY_MODE = ["standalone", "redundant"]
VALID_BODY_AUTO_DIAL = ["enable", "disable"]
VALID_BODY_DIAL_ON_DEMAND = ["enable", "disable"]
VALID_BODY_REDIAL = ["none", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
VALID_BODY_DONT_SEND_CR1 = ["enable", "disable"]
VALID_BODY_PEER_MODEM1 = ["generic", "actiontec", "ascend_TNT"]
VALID_BODY_PPP_ECHO_REQUEST1 = ["enable", "disable"]
VALID_BODY_AUTHTYPE1 = ["pap", "chap", "mschap", "mschapv2"]
VALID_BODY_DONT_SEND_CR2 = ["enable", "disable"]
VALID_BODY_PEER_MODEM2 = ["generic", "actiontec", "ascend_TNT"]
VALID_BODY_PPP_ECHO_REQUEST2 = ["enable", "disable"]
VALID_BODY_AUTHTYPE2 = ["pap", "chap", "mschap", "mschapv2"]
VALID_BODY_DONT_SEND_CR3 = ["enable", "disable"]
VALID_BODY_PEER_MODEM3 = ["generic", "actiontec", "ascend_TNT"]
VALID_BODY_PPP_ECHO_REQUEST3 = ["enable", "disable"]
VALID_BODY_ALTMODE = ["enable", "disable"]
VALID_BODY_AUTHTYPE3 = ["pap", "chap", "mschap", "mschapv2"]
VALID_BODY_TRAFFIC_CHECK = ["enable", "disable"]
VALID_BODY_ACTION = ["dial", "stop", "none"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_modem_get(
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


def validate_modem_put(
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

    # Validate pin-init if present
    if "pin-init" in payload:
        value = payload.get("pin-init")
        if value and isinstance(value, str) and len(value) > 127:
            return (False, "pin-init cannot exceed 127 characters")

    # Validate network-init if present
    if "network-init" in payload:
        value = payload.get("network-init")
        if value and isinstance(value, str) and len(value) > 127:
            return (False, "network-init cannot exceed 127 characters")

    # Validate lockdown-lac if present
    if "lockdown-lac" in payload:
        value = payload.get("lockdown-lac")
        if value and isinstance(value, str) and len(value) > 127:
            return (False, "lockdown-lac cannot exceed 127 characters")

    # Validate mode if present
    if "mode" in payload:
        value = payload.get("mode")
        if value and value not in VALID_BODY_MODE:
            return (
                False,
                f"Invalid mode '{value}'. Must be one of: {', '.join(VALID_BODY_MODE)}",
            )

    # Validate auto-dial if present
    if "auto-dial" in payload:
        value = payload.get("auto-dial")
        if value and value not in VALID_BODY_AUTO_DIAL:
            return (
                False,
                f"Invalid auto-dial '{value}'. Must be one of: {', '.join(VALID_BODY_AUTO_DIAL)}",
            )

    # Validate dial-on-demand if present
    if "dial-on-demand" in payload:
        value = payload.get("dial-on-demand")
        if value and value not in VALID_BODY_DIAL_ON_DEMAND:
            return (
                False,
                f"Invalid dial-on-demand '{value}'. Must be one of: {', '.join(VALID_BODY_DIAL_ON_DEMAND)}",
            )

    # Validate idle-timer if present
    if "idle-timer" in payload:
        value = payload.get("idle-timer")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 9999:
                    return (False, "idle-timer must be between 1 and 9999")
            except (ValueError, TypeError):
                return (False, f"idle-timer must be numeric, got: {value}")

    # Validate redial if present
    if "redial" in payload:
        value = payload.get("redial")
        if value and value not in VALID_BODY_REDIAL:
            return (
                False,
                f"Invalid redial '{value}'. Must be one of: {', '.join(VALID_BODY_REDIAL)}",
            )

    # Validate reset if present
    if "reset" in payload:
        value = payload.get("reset")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 10:
                    return (False, "reset must be between 0 and 10")
            except (ValueError, TypeError):
                return (False, f"reset must be numeric, got: {value}")

    # Validate holddown-timer if present
    if "holddown-timer" in payload:
        value = payload.get("holddown-timer")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 60:
                    return (False, "holddown-timer must be between 1 and 60")
            except (ValueError, TypeError):
                return (False, f"holddown-timer must be numeric, got: {value}")

    # Validate connect-timeout if present
    if "connect-timeout" in payload:
        value = payload.get("connect-timeout")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 30 or int_val > 255:
                    return (
                        False,
                        "connect-timeout must be between 30 and 255",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"connect-timeout must be numeric, got: {value}",
                )

    # Validate interface if present
    if "interface" in payload:
        value = payload.get("interface")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "interface cannot exceed 63 characters")

    # Validate wireless-port if present
    if "wireless-port" in payload:
        value = payload.get("wireless-port")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "wireless-port must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (False, f"wireless-port must be numeric, got: {value}")

    # Validate dont-send-CR1 if present
    if "dont-send-CR1" in payload:
        value = payload.get("dont-send-CR1")
        if value and value not in VALID_BODY_DONT_SEND_CR1:
            return (
                False,
                f"Invalid dont-send-CR1 '{value}'. Must be one of: {', '.join(VALID_BODY_DONT_SEND_CR1)}",
            )

    # Validate phone1 if present
    if "phone1" in payload:
        value = payload.get("phone1")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "phone1 cannot exceed 63 characters")

    # Validate dial-cmd1 if present
    if "dial-cmd1" in payload:
        value = payload.get("dial-cmd1")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "dial-cmd1 cannot exceed 63 characters")

    # Validate username1 if present
    if "username1" in payload:
        value = payload.get("username1")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "username1 cannot exceed 63 characters")

    # Validate extra-init1 if present
    if "extra-init1" in payload:
        value = payload.get("extra-init1")
        if value and isinstance(value, str) and len(value) > 127:
            return (False, "extra-init1 cannot exceed 127 characters")

    # Validate peer-modem1 if present
    if "peer-modem1" in payload:
        value = payload.get("peer-modem1")
        if value and value not in VALID_BODY_PEER_MODEM1:
            return (
                False,
                f"Invalid peer-modem1 '{value}'. Must be one of: {', '.join(VALID_BODY_PEER_MODEM1)}",
            )

    # Validate ppp-echo-request1 if present
    if "ppp-echo-request1" in payload:
        value = payload.get("ppp-echo-request1")
        if value and value not in VALID_BODY_PPP_ECHO_REQUEST1:
            return (
                False,
                f"Invalid ppp-echo-request1 '{value}'. Must be one of: {', '.join(VALID_BODY_PPP_ECHO_REQUEST1)}",
            )

    # Validate authtype1 if present
    if "authtype1" in payload:
        value = payload.get("authtype1")
        if value and value not in VALID_BODY_AUTHTYPE1:
            return (
                False,
                f"Invalid authtype1 '{value}'. Must be one of: {', '.join(VALID_BODY_AUTHTYPE1)}",
            )

    # Validate dont-send-CR2 if present
    if "dont-send-CR2" in payload:
        value = payload.get("dont-send-CR2")
        if value and value not in VALID_BODY_DONT_SEND_CR2:
            return (
                False,
                f"Invalid dont-send-CR2 '{value}'. Must be one of: {', '.join(VALID_BODY_DONT_SEND_CR2)}",
            )

    # Validate phone2 if present
    if "phone2" in payload:
        value = payload.get("phone2")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "phone2 cannot exceed 63 characters")

    # Validate dial-cmd2 if present
    if "dial-cmd2" in payload:
        value = payload.get("dial-cmd2")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "dial-cmd2 cannot exceed 63 characters")

    # Validate username2 if present
    if "username2" in payload:
        value = payload.get("username2")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "username2 cannot exceed 63 characters")

    # Validate extra-init2 if present
    if "extra-init2" in payload:
        value = payload.get("extra-init2")
        if value and isinstance(value, str) and len(value) > 127:
            return (False, "extra-init2 cannot exceed 127 characters")

    # Validate peer-modem2 if present
    if "peer-modem2" in payload:
        value = payload.get("peer-modem2")
        if value and value not in VALID_BODY_PEER_MODEM2:
            return (
                False,
                f"Invalid peer-modem2 '{value}'. Must be one of: {', '.join(VALID_BODY_PEER_MODEM2)}",
            )

    # Validate ppp-echo-request2 if present
    if "ppp-echo-request2" in payload:
        value = payload.get("ppp-echo-request2")
        if value and value not in VALID_BODY_PPP_ECHO_REQUEST2:
            return (
                False,
                f"Invalid ppp-echo-request2 '{value}'. Must be one of: {', '.join(VALID_BODY_PPP_ECHO_REQUEST2)}",
            )

    # Validate authtype2 if present
    if "authtype2" in payload:
        value = payload.get("authtype2")
        if value and value not in VALID_BODY_AUTHTYPE2:
            return (
                False,
                f"Invalid authtype2 '{value}'. Must be one of: {', '.join(VALID_BODY_AUTHTYPE2)}",
            )

    # Validate dont-send-CR3 if present
    if "dont-send-CR3" in payload:
        value = payload.get("dont-send-CR3")
        if value and value not in VALID_BODY_DONT_SEND_CR3:
            return (
                False,
                f"Invalid dont-send-CR3 '{value}'. Must be one of: {', '.join(VALID_BODY_DONT_SEND_CR3)}",
            )

    # Validate phone3 if present
    if "phone3" in payload:
        value = payload.get("phone3")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "phone3 cannot exceed 63 characters")

    # Validate dial-cmd3 if present
    if "dial-cmd3" in payload:
        value = payload.get("dial-cmd3")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "dial-cmd3 cannot exceed 63 characters")

    # Validate username3 if present
    if "username3" in payload:
        value = payload.get("username3")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "username3 cannot exceed 63 characters")

    # Validate extra-init3 if present
    if "extra-init3" in payload:
        value = payload.get("extra-init3")
        if value and isinstance(value, str) and len(value) > 127:
            return (False, "extra-init3 cannot exceed 127 characters")

    # Validate peer-modem3 if present
    if "peer-modem3" in payload:
        value = payload.get("peer-modem3")
        if value and value not in VALID_BODY_PEER_MODEM3:
            return (
                False,
                f"Invalid peer-modem3 '{value}'. Must be one of: {', '.join(VALID_BODY_PEER_MODEM3)}",
            )

    # Validate ppp-echo-request3 if present
    if "ppp-echo-request3" in payload:
        value = payload.get("ppp-echo-request3")
        if value and value not in VALID_BODY_PPP_ECHO_REQUEST3:
            return (
                False,
                f"Invalid ppp-echo-request3 '{value}'. Must be one of: {', '.join(VALID_BODY_PPP_ECHO_REQUEST3)}",
            )

    # Validate altmode if present
    if "altmode" in payload:
        value = payload.get("altmode")
        if value and value not in VALID_BODY_ALTMODE:
            return (
                False,
                f"Invalid altmode '{value}'. Must be one of: {', '.join(VALID_BODY_ALTMODE)}",
            )

    # Validate authtype3 if present
    if "authtype3" in payload:
        value = payload.get("authtype3")
        if value and value not in VALID_BODY_AUTHTYPE3:
            return (
                False,
                f"Invalid authtype3 '{value}'. Must be one of: {', '.join(VALID_BODY_AUTHTYPE3)}",
            )

    # Validate traffic-check if present
    if "traffic-check" in payload:
        value = payload.get("traffic-check")
        if value and value not in VALID_BODY_TRAFFIC_CHECK:
            return (
                False,
                f"Invalid traffic-check '{value}'. Must be one of: {', '.join(VALID_BODY_TRAFFIC_CHECK)}",
            )

    # Validate action if present
    if "action" in payload:
        value = payload.get("action")
        if value and value not in VALID_BODY_ACTION:
            return (
                False,
                f"Invalid action '{value}'. Must be one of: {', '.join(VALID_BODY_ACTION)}",
            )

    # Validate distance if present
    if "distance" in payload:
        value = payload.get("distance")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 255:
                    return (False, "distance must be between 1 and 255")
            except (ValueError, TypeError):
                return (False, f"distance must be numeric, got: {value}")

    # Validate priority if present
    if "priority" in payload:
        value = payload.get("priority")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 65535:
                    return (False, "priority must be between 1 and 65535")
            except (ValueError, TypeError):
                return (False, f"priority must be numeric, got: {value}")

    return (True, None)
