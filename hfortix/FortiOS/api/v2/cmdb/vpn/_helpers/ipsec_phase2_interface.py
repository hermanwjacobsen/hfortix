"""
Validation helpers for vpn ipsec_phase2_interface endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_DHCP_IPSEC = ["enable", "disable"]
VALID_BODY_PROPOSAL = [
    "null-md5",
    "null-sha1",
    "null-sha256",
    "null-sha384",
    "null-sha512",
    "des-null",
    "des-md5",
    "des-sha1",
    "des-sha256",
    "des-sha384",
    "des-sha512",
    "3des-null",
    "3des-md5",
    "3des-sha1",
    "3des-sha256",
    "3des-sha384",
    "3des-sha512",
    "aes128-null",
    "aes128-md5",
    "aes128-sha1",
    "aes128-sha256",
    "aes128-sha384",
    "aes128-sha512",
    "aes128gcm",
    "aes192-null",
    "aes192-md5",
    "aes192-sha1",
    "aes192-sha256",
    "aes192-sha384",
    "aes192-sha512",
    "aes256-null",
    "aes256-md5",
    "aes256-sha1",
    "aes256-sha256",
    "aes256-sha384",
    "aes256-sha512",
    "aes256gcm",
    "chacha20poly1305",
    "aria128-null",
    "aria128-md5",
    "aria128-sha1",
    "aria128-sha256",
    "aria128-sha384",
    "aria128-sha512",
    "aria192-null",
    "aria192-md5",
    "aria192-sha1",
    "aria192-sha256",
    "aria192-sha384",
    "aria192-sha512",
    "aria256-null",
    "aria256-md5",
    "aria256-sha1",
    "aria256-sha256",
    "aria256-sha384",
    "aria256-sha512",
    "seed-null",
    "seed-md5",
    "seed-sha1",
    "seed-sha256",
    "seed-sha384",
    "seed-sha512",
]
VALID_BODY_PFS = ["enable", "disable"]
VALID_BODY_DHGRP = [
    "1",
    "2",
    "5",
    "14",
    "15",
    "16",
    "17",
    "18",
    "19",
    "20",
    "21",
    "27",
    "28",
    "29",
    "30",
    "31",
    "32",
]
VALID_BODY_ADDKE1 = [
    "0",
    "35",
    "36",
    "37",
    "1080",
    "1081",
    "1082",
    "1083",
    "1084",
    "1085",
    "1089",
    "1090",
    "1091",
    "1092",
    "1093",
    "1094",
]
VALID_BODY_ADDKE2 = [
    "0",
    "35",
    "36",
    "37",
    "1080",
    "1081",
    "1082",
    "1083",
    "1084",
    "1085",
    "1089",
    "1090",
    "1091",
    "1092",
    "1093",
    "1094",
]
VALID_BODY_ADDKE3 = [
    "0",
    "35",
    "36",
    "37",
    "1080",
    "1081",
    "1082",
    "1083",
    "1084",
    "1085",
    "1089",
    "1090",
    "1091",
    "1092",
    "1093",
    "1094",
]
VALID_BODY_ADDKE4 = [
    "0",
    "35",
    "36",
    "37",
    "1080",
    "1081",
    "1082",
    "1083",
    "1084",
    "1085",
    "1089",
    "1090",
    "1091",
    "1092",
    "1093",
    "1094",
]
VALID_BODY_ADDKE5 = [
    "0",
    "35",
    "36",
    "37",
    "1080",
    "1081",
    "1082",
    "1083",
    "1084",
    "1085",
    "1089",
    "1090",
    "1091",
    "1092",
    "1093",
    "1094",
]
VALID_BODY_ADDKE6 = [
    "0",
    "35",
    "36",
    "37",
    "1080",
    "1081",
    "1082",
    "1083",
    "1084",
    "1085",
    "1089",
    "1090",
    "1091",
    "1092",
    "1093",
    "1094",
]
VALID_BODY_ADDKE7 = [
    "0",
    "35",
    "36",
    "37",
    "1080",
    "1081",
    "1082",
    "1083",
    "1084",
    "1085",
    "1089",
    "1090",
    "1091",
    "1092",
    "1093",
    "1094",
]
VALID_BODY_REPLAY = ["enable", "disable"]
VALID_BODY_KEEPALIVE = ["enable", "disable"]
VALID_BODY_AUTO_NEGOTIATE = ["enable", "disable"]
VALID_BODY_ADD_ROUTE = ["phase1", "enable", "disable"]
VALID_BODY_INBOUND_DSCP_COPY = ["phase1", "enable", "disable"]
VALID_BODY_AUTO_DISCOVERY_SENDER = ["phase1", "enable", "disable"]
VALID_BODY_AUTO_DISCOVERY_FORWARDER = ["phase1", "enable", "disable"]
VALID_BODY_KEYLIFE_TYPE = ["seconds", "kbs", "both"]
VALID_BODY_SINGLE_SOURCE = ["enable", "disable"]
VALID_BODY_ROUTE_OVERLAP = ["use-old", "use-new", "allow"]
VALID_BODY_ENCAPSULATION = ["tunnel-mode", "transport-mode"]
VALID_BODY_L2TP = ["enable", "disable"]
VALID_BODY_INITIATOR_TS_NARROW = ["enable", "disable"]
VALID_BODY_DIFFSERV = ["enable", "disable"]
VALID_BODY_SRC_ADDR_TYPE = [
    "subnet",
    "range",
    "ip",
    "name",
    "subnet6",
    "range6",
    "ip6",
    "name6",
]
VALID_BODY_DST_ADDR_TYPE = [
    "subnet",
    "range",
    "ip",
    "name",
    "subnet6",
    "range6",
    "ip6",
    "name6",
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_ipsec_phase2_interface_get(
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


def validate_ipsec_phase2_interface_post(
    payload: dict[str, Any],
) -> tuple[bool, str | None]:
    """
    Validate POST request payload for creating ipsec_phase2_interface.

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

    # Validate phase1name if present
    if "phase1name" in payload:
        value = payload.get("phase1name")
        if value and isinstance(value, str) and len(value) > 15:
            return (False, "phase1name cannot exceed 15 characters")

    # Validate dhcp-ipsec if present
    if "dhcp-ipsec" in payload:
        value = payload.get("dhcp-ipsec")
        if value and value not in VALID_BODY_DHCP_IPSEC:
            return (
                False,
                f"Invalid dhcp-ipsec '{value}'. Must be one of: {', '.join(VALID_BODY_DHCP_IPSEC)}",
            )

    # Validate proposal if present
    if "proposal" in payload:
        value = payload.get("proposal")
        if value and value not in VALID_BODY_PROPOSAL:
            return (
                False,
                f"Invalid proposal '{value}'. Must be one of: {', '.join(VALID_BODY_PROPOSAL)}",
            )

    # Validate pfs if present
    if "pfs" in payload:
        value = payload.get("pfs")
        if value and value not in VALID_BODY_PFS:
            return (
                False,
                f"Invalid pfs '{value}'. Must be one of: {', '.join(VALID_BODY_PFS)}",
            )

    # Validate dhgrp if present
    if "dhgrp" in payload:
        value = payload.get("dhgrp")
        if value and value not in VALID_BODY_DHGRP:
            return (
                False,
                f"Invalid dhgrp '{value}'. Must be one of: {', '.join(VALID_BODY_DHGRP)}",
            )

    # Validate addke1 if present
    if "addke1" in payload:
        value = payload.get("addke1")
        if value and value not in VALID_BODY_ADDKE1:
            return (
                False,
                f"Invalid addke1 '{value}'. Must be one of: {', '.join(VALID_BODY_ADDKE1)}",
            )

    # Validate addke2 if present
    if "addke2" in payload:
        value = payload.get("addke2")
        if value and value not in VALID_BODY_ADDKE2:
            return (
                False,
                f"Invalid addke2 '{value}'. Must be one of: {', '.join(VALID_BODY_ADDKE2)}",
            )

    # Validate addke3 if present
    if "addke3" in payload:
        value = payload.get("addke3")
        if value and value not in VALID_BODY_ADDKE3:
            return (
                False,
                f"Invalid addke3 '{value}'. Must be one of: {', '.join(VALID_BODY_ADDKE3)}",
            )

    # Validate addke4 if present
    if "addke4" in payload:
        value = payload.get("addke4")
        if value and value not in VALID_BODY_ADDKE4:
            return (
                False,
                f"Invalid addke4 '{value}'. Must be one of: {', '.join(VALID_BODY_ADDKE4)}",
            )

    # Validate addke5 if present
    if "addke5" in payload:
        value = payload.get("addke5")
        if value and value not in VALID_BODY_ADDKE5:
            return (
                False,
                f"Invalid addke5 '{value}'. Must be one of: {', '.join(VALID_BODY_ADDKE5)}",
            )

    # Validate addke6 if present
    if "addke6" in payload:
        value = payload.get("addke6")
        if value and value not in VALID_BODY_ADDKE6:
            return (
                False,
                f"Invalid addke6 '{value}'. Must be one of: {', '.join(VALID_BODY_ADDKE6)}",
            )

    # Validate addke7 if present
    if "addke7" in payload:
        value = payload.get("addke7")
        if value and value not in VALID_BODY_ADDKE7:
            return (
                False,
                f"Invalid addke7 '{value}'. Must be one of: {', '.join(VALID_BODY_ADDKE7)}",
            )

    # Validate replay if present
    if "replay" in payload:
        value = payload.get("replay")
        if value and value not in VALID_BODY_REPLAY:
            return (
                False,
                f"Invalid replay '{value}'. Must be one of: {', '.join(VALID_BODY_REPLAY)}",
            )

    # Validate keepalive if present
    if "keepalive" in payload:
        value = payload.get("keepalive")
        if value and value not in VALID_BODY_KEEPALIVE:
            return (
                False,
                f"Invalid keepalive '{value}'. Must be one of: {', '.join(VALID_BODY_KEEPALIVE)}",
            )

    # Validate auto-negotiate if present
    if "auto-negotiate" in payload:
        value = payload.get("auto-negotiate")
        if value and value not in VALID_BODY_AUTO_NEGOTIATE:
            return (
                False,
                f"Invalid auto-negotiate '{value}'. Must be one of: {', '.join(VALID_BODY_AUTO_NEGOTIATE)}",
            )

    # Validate add-route if present
    if "add-route" in payload:
        value = payload.get("add-route")
        if value and value not in VALID_BODY_ADD_ROUTE:
            return (
                False,
                f"Invalid add-route '{value}'. Must be one of: {', '.join(VALID_BODY_ADD_ROUTE)}",
            )

    # Validate inbound-dscp-copy if present
    if "inbound-dscp-copy" in payload:
        value = payload.get("inbound-dscp-copy")
        if value and value not in VALID_BODY_INBOUND_DSCP_COPY:
            return (
                False,
                f"Invalid inbound-dscp-copy '{value}'. Must be one of: {', '.join(VALID_BODY_INBOUND_DSCP_COPY)}",
            )

    # Validate auto-discovery-sender if present
    if "auto-discovery-sender" in payload:
        value = payload.get("auto-discovery-sender")
        if value and value not in VALID_BODY_AUTO_DISCOVERY_SENDER:
            return (
                False,
                f"Invalid auto-discovery-sender '{value}'. Must be one of: {', '.join(VALID_BODY_AUTO_DISCOVERY_SENDER)}",
            )

    # Validate auto-discovery-forwarder if present
    if "auto-discovery-forwarder" in payload:
        value = payload.get("auto-discovery-forwarder")
        if value and value not in VALID_BODY_AUTO_DISCOVERY_FORWARDER:
            return (
                False,
                f"Invalid auto-discovery-forwarder '{value}'. Must be one of: {', '.join(VALID_BODY_AUTO_DISCOVERY_FORWARDER)}",
            )

    # Validate keylifeseconds if present
    if "keylifeseconds" in payload:
        value = payload.get("keylifeseconds")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 120 or int_val > 172800:
                    return (
                        False,
                        "keylifeseconds must be between 120 and 172800",
                    )
            except (ValueError, TypeError):
                return (False, f"keylifeseconds must be numeric, got: {value}")

    # Validate keylifekbs if present
    if "keylifekbs" in payload:
        value = payload.get("keylifekbs")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 5120 or int_val > 4294967295:
                    return (
                        False,
                        "keylifekbs must be between 5120 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (False, f"keylifekbs must be numeric, got: {value}")

    # Validate keylife-type if present
    if "keylife-type" in payload:
        value = payload.get("keylife-type")
        if value and value not in VALID_BODY_KEYLIFE_TYPE:
            return (
                False,
                f"Invalid keylife-type '{value}'. Must be one of: {', '.join(VALID_BODY_KEYLIFE_TYPE)}",
            )

    # Validate single-source if present
    if "single-source" in payload:
        value = payload.get("single-source")
        if value and value not in VALID_BODY_SINGLE_SOURCE:
            return (
                False,
                f"Invalid single-source '{value}'. Must be one of: {', '.join(VALID_BODY_SINGLE_SOURCE)}",
            )

    # Validate route-overlap if present
    if "route-overlap" in payload:
        value = payload.get("route-overlap")
        if value and value not in VALID_BODY_ROUTE_OVERLAP:
            return (
                False,
                f"Invalid route-overlap '{value}'. Must be one of: {', '.join(VALID_BODY_ROUTE_OVERLAP)}",
            )

    # Validate encapsulation if present
    if "encapsulation" in payload:
        value = payload.get("encapsulation")
        if value and value not in VALID_BODY_ENCAPSULATION:
            return (
                False,
                f"Invalid encapsulation '{value}'. Must be one of: {', '.join(VALID_BODY_ENCAPSULATION)}",
            )

    # Validate l2tp if present
    if "l2tp" in payload:
        value = payload.get("l2tp")
        if value and value not in VALID_BODY_L2TP:
            return (
                False,
                f"Invalid l2tp '{value}'. Must be one of: {', '.join(VALID_BODY_L2TP)}",
            )

    # Validate comments if present
    if "comments" in payload:
        value = payload.get("comments")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "comments cannot exceed 255 characters")

    # Validate initiator-ts-narrow if present
    if "initiator-ts-narrow" in payload:
        value = payload.get("initiator-ts-narrow")
        if value and value not in VALID_BODY_INITIATOR_TS_NARROW:
            return (
                False,
                f"Invalid initiator-ts-narrow '{value}'. Must be one of: {', '.join(VALID_BODY_INITIATOR_TS_NARROW)}",
            )

    # Validate diffserv if present
    if "diffserv" in payload:
        value = payload.get("diffserv")
        if value and value not in VALID_BODY_DIFFSERV:
            return (
                False,
                f"Invalid diffserv '{value}'. Must be one of: {', '.join(VALID_BODY_DIFFSERV)}",
            )

    # Validate protocol if present
    if "protocol" in payload:
        value = payload.get("protocol")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 255:
                    return (False, "protocol must be between 0 and 255")
            except (ValueError, TypeError):
                return (False, f"protocol must be numeric, got: {value}")

    # Validate src-name if present
    if "src-name" in payload:
        value = payload.get("src-name")
        if value and isinstance(value, str) and len(value) > 79:
            return (False, "src-name cannot exceed 79 characters")

    # Validate src-name6 if present
    if "src-name6" in payload:
        value = payload.get("src-name6")
        if value and isinstance(value, str) and len(value) > 79:
            return (False, "src-name6 cannot exceed 79 characters")

    # Validate src-addr-type if present
    if "src-addr-type" in payload:
        value = payload.get("src-addr-type")
        if value and value not in VALID_BODY_SRC_ADDR_TYPE:
            return (
                False,
                f"Invalid src-addr-type '{value}'. Must be one of: {', '.join(VALID_BODY_SRC_ADDR_TYPE)}",
            )

    # Validate src-port if present
    if "src-port" in payload:
        value = payload.get("src-port")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 65535:
                    return (False, "src-port must be between 0 and 65535")
            except (ValueError, TypeError):
                return (False, f"src-port must be numeric, got: {value}")

    # Validate dst-name if present
    if "dst-name" in payload:
        value = payload.get("dst-name")
        if value and isinstance(value, str) and len(value) > 79:
            return (False, "dst-name cannot exceed 79 characters")

    # Validate dst-name6 if present
    if "dst-name6" in payload:
        value = payload.get("dst-name6")
        if value and isinstance(value, str) and len(value) > 79:
            return (False, "dst-name6 cannot exceed 79 characters")

    # Validate dst-addr-type if present
    if "dst-addr-type" in payload:
        value = payload.get("dst-addr-type")
        if value and value not in VALID_BODY_DST_ADDR_TYPE:
            return (
                False,
                f"Invalid dst-addr-type '{value}'. Must be one of: {', '.join(VALID_BODY_DST_ADDR_TYPE)}",
            )

    # Validate dst-port if present
    if "dst-port" in payload:
        value = payload.get("dst-port")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 65535:
                    return (False, "dst-port must be between 0 and 65535")
            except (ValueError, TypeError):
                return (False, f"dst-port must be numeric, got: {value}")

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_ipsec_phase2_interface_put(
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

    # Validate phase1name if present
    if "phase1name" in payload:
        value = payload.get("phase1name")
        if value and isinstance(value, str) and len(value) > 15:
            return (False, "phase1name cannot exceed 15 characters")

    # Validate dhcp-ipsec if present
    if "dhcp-ipsec" in payload:
        value = payload.get("dhcp-ipsec")
        if value and value not in VALID_BODY_DHCP_IPSEC:
            return (
                False,
                f"Invalid dhcp-ipsec '{value}'. Must be one of: {', '.join(VALID_BODY_DHCP_IPSEC)}",
            )

    # Validate proposal if present
    if "proposal" in payload:
        value = payload.get("proposal")
        if value and value not in VALID_BODY_PROPOSAL:
            return (
                False,
                f"Invalid proposal '{value}'. Must be one of: {', '.join(VALID_BODY_PROPOSAL)}",
            )

    # Validate pfs if present
    if "pfs" in payload:
        value = payload.get("pfs")
        if value and value not in VALID_BODY_PFS:
            return (
                False,
                f"Invalid pfs '{value}'. Must be one of: {', '.join(VALID_BODY_PFS)}",
            )

    # Validate dhgrp if present
    if "dhgrp" in payload:
        value = payload.get("dhgrp")
        if value and value not in VALID_BODY_DHGRP:
            return (
                False,
                f"Invalid dhgrp '{value}'. Must be one of: {', '.join(VALID_BODY_DHGRP)}",
            )

    # Validate addke1 if present
    if "addke1" in payload:
        value = payload.get("addke1")
        if value and value not in VALID_BODY_ADDKE1:
            return (
                False,
                f"Invalid addke1 '{value}'. Must be one of: {', '.join(VALID_BODY_ADDKE1)}",
            )

    # Validate addke2 if present
    if "addke2" in payload:
        value = payload.get("addke2")
        if value and value not in VALID_BODY_ADDKE2:
            return (
                False,
                f"Invalid addke2 '{value}'. Must be one of: {', '.join(VALID_BODY_ADDKE2)}",
            )

    # Validate addke3 if present
    if "addke3" in payload:
        value = payload.get("addke3")
        if value and value not in VALID_BODY_ADDKE3:
            return (
                False,
                f"Invalid addke3 '{value}'. Must be one of: {', '.join(VALID_BODY_ADDKE3)}",
            )

    # Validate addke4 if present
    if "addke4" in payload:
        value = payload.get("addke4")
        if value and value not in VALID_BODY_ADDKE4:
            return (
                False,
                f"Invalid addke4 '{value}'. Must be one of: {', '.join(VALID_BODY_ADDKE4)}",
            )

    # Validate addke5 if present
    if "addke5" in payload:
        value = payload.get("addke5")
        if value and value not in VALID_BODY_ADDKE5:
            return (
                False,
                f"Invalid addke5 '{value}'. Must be one of: {', '.join(VALID_BODY_ADDKE5)}",
            )

    # Validate addke6 if present
    if "addke6" in payload:
        value = payload.get("addke6")
        if value and value not in VALID_BODY_ADDKE6:
            return (
                False,
                f"Invalid addke6 '{value}'. Must be one of: {', '.join(VALID_BODY_ADDKE6)}",
            )

    # Validate addke7 if present
    if "addke7" in payload:
        value = payload.get("addke7")
        if value and value not in VALID_BODY_ADDKE7:
            return (
                False,
                f"Invalid addke7 '{value}'. Must be one of: {', '.join(VALID_BODY_ADDKE7)}",
            )

    # Validate replay if present
    if "replay" in payload:
        value = payload.get("replay")
        if value and value not in VALID_BODY_REPLAY:
            return (
                False,
                f"Invalid replay '{value}'. Must be one of: {', '.join(VALID_BODY_REPLAY)}",
            )

    # Validate keepalive if present
    if "keepalive" in payload:
        value = payload.get("keepalive")
        if value and value not in VALID_BODY_KEEPALIVE:
            return (
                False,
                f"Invalid keepalive '{value}'. Must be one of: {', '.join(VALID_BODY_KEEPALIVE)}",
            )

    # Validate auto-negotiate if present
    if "auto-negotiate" in payload:
        value = payload.get("auto-negotiate")
        if value and value not in VALID_BODY_AUTO_NEGOTIATE:
            return (
                False,
                f"Invalid auto-negotiate '{value}'. Must be one of: {', '.join(VALID_BODY_AUTO_NEGOTIATE)}",
            )

    # Validate add-route if present
    if "add-route" in payload:
        value = payload.get("add-route")
        if value and value not in VALID_BODY_ADD_ROUTE:
            return (
                False,
                f"Invalid add-route '{value}'. Must be one of: {', '.join(VALID_BODY_ADD_ROUTE)}",
            )

    # Validate inbound-dscp-copy if present
    if "inbound-dscp-copy" in payload:
        value = payload.get("inbound-dscp-copy")
        if value and value not in VALID_BODY_INBOUND_DSCP_COPY:
            return (
                False,
                f"Invalid inbound-dscp-copy '{value}'. Must be one of: {', '.join(VALID_BODY_INBOUND_DSCP_COPY)}",
            )

    # Validate auto-discovery-sender if present
    if "auto-discovery-sender" in payload:
        value = payload.get("auto-discovery-sender")
        if value and value not in VALID_BODY_AUTO_DISCOVERY_SENDER:
            return (
                False,
                f"Invalid auto-discovery-sender '{value}'. Must be one of: {', '.join(VALID_BODY_AUTO_DISCOVERY_SENDER)}",
            )

    # Validate auto-discovery-forwarder if present
    if "auto-discovery-forwarder" in payload:
        value = payload.get("auto-discovery-forwarder")
        if value and value not in VALID_BODY_AUTO_DISCOVERY_FORWARDER:
            return (
                False,
                f"Invalid auto-discovery-forwarder '{value}'. Must be one of: {', '.join(VALID_BODY_AUTO_DISCOVERY_FORWARDER)}",
            )

    # Validate keylifeseconds if present
    if "keylifeseconds" in payload:
        value = payload.get("keylifeseconds")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 120 or int_val > 172800:
                    return (
                        False,
                        "keylifeseconds must be between 120 and 172800",
                    )
            except (ValueError, TypeError):
                return (False, f"keylifeseconds must be numeric, got: {value}")

    # Validate keylifekbs if present
    if "keylifekbs" in payload:
        value = payload.get("keylifekbs")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 5120 or int_val > 4294967295:
                    return (
                        False,
                        "keylifekbs must be between 5120 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (False, f"keylifekbs must be numeric, got: {value}")

    # Validate keylife-type if present
    if "keylife-type" in payload:
        value = payload.get("keylife-type")
        if value and value not in VALID_BODY_KEYLIFE_TYPE:
            return (
                False,
                f"Invalid keylife-type '{value}'. Must be one of: {', '.join(VALID_BODY_KEYLIFE_TYPE)}",
            )

    # Validate single-source if present
    if "single-source" in payload:
        value = payload.get("single-source")
        if value and value not in VALID_BODY_SINGLE_SOURCE:
            return (
                False,
                f"Invalid single-source '{value}'. Must be one of: {', '.join(VALID_BODY_SINGLE_SOURCE)}",
            )

    # Validate route-overlap if present
    if "route-overlap" in payload:
        value = payload.get("route-overlap")
        if value and value not in VALID_BODY_ROUTE_OVERLAP:
            return (
                False,
                f"Invalid route-overlap '{value}'. Must be one of: {', '.join(VALID_BODY_ROUTE_OVERLAP)}",
            )

    # Validate encapsulation if present
    if "encapsulation" in payload:
        value = payload.get("encapsulation")
        if value and value not in VALID_BODY_ENCAPSULATION:
            return (
                False,
                f"Invalid encapsulation '{value}'. Must be one of: {', '.join(VALID_BODY_ENCAPSULATION)}",
            )

    # Validate l2tp if present
    if "l2tp" in payload:
        value = payload.get("l2tp")
        if value and value not in VALID_BODY_L2TP:
            return (
                False,
                f"Invalid l2tp '{value}'. Must be one of: {', '.join(VALID_BODY_L2TP)}",
            )

    # Validate comments if present
    if "comments" in payload:
        value = payload.get("comments")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "comments cannot exceed 255 characters")

    # Validate initiator-ts-narrow if present
    if "initiator-ts-narrow" in payload:
        value = payload.get("initiator-ts-narrow")
        if value and value not in VALID_BODY_INITIATOR_TS_NARROW:
            return (
                False,
                f"Invalid initiator-ts-narrow '{value}'. Must be one of: {', '.join(VALID_BODY_INITIATOR_TS_NARROW)}",
            )

    # Validate diffserv if present
    if "diffserv" in payload:
        value = payload.get("diffserv")
        if value and value not in VALID_BODY_DIFFSERV:
            return (
                False,
                f"Invalid diffserv '{value}'. Must be one of: {', '.join(VALID_BODY_DIFFSERV)}",
            )

    # Validate protocol if present
    if "protocol" in payload:
        value = payload.get("protocol")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 255:
                    return (False, "protocol must be between 0 and 255")
            except (ValueError, TypeError):
                return (False, f"protocol must be numeric, got: {value}")

    # Validate src-name if present
    if "src-name" in payload:
        value = payload.get("src-name")
        if value and isinstance(value, str) and len(value) > 79:
            return (False, "src-name cannot exceed 79 characters")

    # Validate src-name6 if present
    if "src-name6" in payload:
        value = payload.get("src-name6")
        if value and isinstance(value, str) and len(value) > 79:
            return (False, "src-name6 cannot exceed 79 characters")

    # Validate src-addr-type if present
    if "src-addr-type" in payload:
        value = payload.get("src-addr-type")
        if value and value not in VALID_BODY_SRC_ADDR_TYPE:
            return (
                False,
                f"Invalid src-addr-type '{value}'. Must be one of: {', '.join(VALID_BODY_SRC_ADDR_TYPE)}",
            )

    # Validate src-port if present
    if "src-port" in payload:
        value = payload.get("src-port")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 65535:
                    return (False, "src-port must be between 0 and 65535")
            except (ValueError, TypeError):
                return (False, f"src-port must be numeric, got: {value}")

    # Validate dst-name if present
    if "dst-name" in payload:
        value = payload.get("dst-name")
        if value and isinstance(value, str) and len(value) > 79:
            return (False, "dst-name cannot exceed 79 characters")

    # Validate dst-name6 if present
    if "dst-name6" in payload:
        value = payload.get("dst-name6")
        if value and isinstance(value, str) and len(value) > 79:
            return (False, "dst-name6 cannot exceed 79 characters")

    # Validate dst-addr-type if present
    if "dst-addr-type" in payload:
        value = payload.get("dst-addr-type")
        if value and value not in VALID_BODY_DST_ADDR_TYPE:
            return (
                False,
                f"Invalid dst-addr-type '{value}'. Must be one of: {', '.join(VALID_BODY_DST_ADDR_TYPE)}",
            )

    # Validate dst-port if present
    if "dst-port" in payload:
        value = payload.get("dst-port")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 65535:
                    return (False, "dst-port must be between 0 and 65535")
            except (ValueError, TypeError):
                return (False, f"dst-port must be numeric, got: {value}")

    return (True, None)


# ============================================================================
# DELETE Validation
# ============================================================================


def validate_ipsec_phase2_interface_delete(
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
