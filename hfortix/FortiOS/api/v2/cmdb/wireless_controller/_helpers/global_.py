"""
Validation helpers for wireless-controller global_ endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_IMAGE_DOWNLOAD = ["enable", "disable"]
VALID_BODY_ROLLING_WTP_UPGRADE = ["enable", "disable"]
VALID_BODY_CONTROL_MESSAGE_OFFLOAD = [
    "ebp-frame",
    "aeroscout-tag",
    "ap-list",
    "sta-list",
    "sta-cap-list",
    "stats",
    "aeroscout-mu",
    "sta-health",
    "spectral-analysis",
]
VALID_BODY_DATA_ETHERNET_II = ["enable", "disable"]
VALID_BODY_LINK_AGGREGATION = ["enable", "disable"]
VALID_BODY_WTP_SHARE = ["enable", "disable"]
VALID_BODY_TUNNEL_MODE = ["compatible", "strict"]
VALID_BODY_AP_LOG_SERVER = ["enable", "disable"]
VALID_BODY_DFS_LAB_TEST = ["enable", "disable"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_global__get(
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


def validate_global__put(
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

    # Validate location if present
    if "location" in payload:
        value = payload.get("location")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "location cannot exceed 35 characters")

    # Validate acd-process-count if present
    if "acd-process-count" in payload:
        value = payload.get("acd-process-count")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 255:
                    return (
                        False,
                        "acd-process-count must be between 0 and 255",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"acd-process-count must be numeric, got: {value}",
                )

    # Validate wpad-process-count if present
    if "wpad-process-count" in payload:
        value = payload.get("wpad-process-count")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 255:
                    return (
                        False,
                        "wpad-process-count must be between 0 and 255",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"wpad-process-count must be numeric, got: {value}",
                )

    # Validate image-download if present
    if "image-download" in payload:
        value = payload.get("image-download")
        if value and value not in VALID_BODY_IMAGE_DOWNLOAD:
            return (
                False,
                f"Invalid image-download '{value}'. Must be one of: {', '.join(VALID_BODY_IMAGE_DOWNLOAD)}",
            )

    # Validate rolling-wtp-upgrade if present
    if "rolling-wtp-upgrade" in payload:
        value = payload.get("rolling-wtp-upgrade")
        if value and value not in VALID_BODY_ROLLING_WTP_UPGRADE:
            return (
                False,
                f"Invalid rolling-wtp-upgrade '{value}'. Must be one of: {', '.join(VALID_BODY_ROLLING_WTP_UPGRADE)}",
            )

    # Validate rolling-wtp-upgrade-threshold if present
    if "rolling-wtp-upgrade-threshold" in payload:
        value = payload.get("rolling-wtp-upgrade-threshold")
        if value and isinstance(value, str) and len(value) > 7:
            return (
                False,
                "rolling-wtp-upgrade-threshold cannot exceed 7 characters",
            )

    # Validate max-retransmit if present
    if "max-retransmit" in payload:
        value = payload.get("max-retransmit")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 64:
                    return (False, "max-retransmit must be between 0 and 64")
            except (ValueError, TypeError):
                return (False, f"max-retransmit must be numeric, got: {value}")

    # Validate control-message-offload if present
    if "control-message-offload" in payload:
        value = payload.get("control-message-offload")
        if value and value not in VALID_BODY_CONTROL_MESSAGE_OFFLOAD:
            return (
                False,
                f"Invalid control-message-offload '{value}'. Must be one of: {', '.join(VALID_BODY_CONTROL_MESSAGE_OFFLOAD)}",
            )

    # Validate data-ethernet-II if present
    if "data-ethernet-II" in payload:
        value = payload.get("data-ethernet-II")
        if value and value not in VALID_BODY_DATA_ETHERNET_II:
            return (
                False,
                f"Invalid data-ethernet-II '{value}'. Must be one of: {', '.join(VALID_BODY_DATA_ETHERNET_II)}",
            )

    # Validate link-aggregation if present
    if "link-aggregation" in payload:
        value = payload.get("link-aggregation")
        if value and value not in VALID_BODY_LINK_AGGREGATION:
            return (
                False,
                f"Invalid link-aggregation '{value}'. Must be one of: {', '.join(VALID_BODY_LINK_AGGREGATION)}",
            )

    # Validate mesh-eth-type if present
    if "mesh-eth-type" in payload:
        value = payload.get("mesh-eth-type")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 65535:
                    return (
                        False,
                        "mesh-eth-type must be between 0 and 65535",
                    )
            except (ValueError, TypeError):
                return (False, f"mesh-eth-type must be numeric, got: {value}")

    # Validate fiapp-eth-type if present
    if "fiapp-eth-type" in payload:
        value = payload.get("fiapp-eth-type")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 65535:
                    return (
                        False,
                        "fiapp-eth-type must be between 0 and 65535",
                    )
            except (ValueError, TypeError):
                return (False, f"fiapp-eth-type must be numeric, got: {value}")

    # Validate max-clients if present
    if "max-clients" in payload:
        value = payload.get("max-clients")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "max-clients must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (False, f"max-clients must be numeric, got: {value}")

    # Validate rogue-scan-mac-adjacency if present
    if "rogue-scan-mac-adjacency" in payload:
        value = payload.get("rogue-scan-mac-adjacency")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 31:
                    return (
                        False,
                        "rogue-scan-mac-adjacency must be between 0 and 31",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"rogue-scan-mac-adjacency must be numeric, got: {value}",
                )

    # Validate wtp-share if present
    if "wtp-share" in payload:
        value = payload.get("wtp-share")
        if value and value not in VALID_BODY_WTP_SHARE:
            return (
                False,
                f"Invalid wtp-share '{value}'. Must be one of: {', '.join(VALID_BODY_WTP_SHARE)}",
            )

    # Validate tunnel-mode if present
    if "tunnel-mode" in payload:
        value = payload.get("tunnel-mode")
        if value and value not in VALID_BODY_TUNNEL_MODE:
            return (
                False,
                f"Invalid tunnel-mode '{value}'. Must be one of: {', '.join(VALID_BODY_TUNNEL_MODE)}",
            )

    # Validate nac-interval if present
    if "nac-interval" in payload:
        value = payload.get("nac-interval")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 10 or int_val > 600:
                    return (False, "nac-interval must be between 10 and 600")
            except (ValueError, TypeError):
                return (False, f"nac-interval must be numeric, got: {value}")

    # Validate ap-log-server if present
    if "ap-log-server" in payload:
        value = payload.get("ap-log-server")
        if value and value not in VALID_BODY_AP_LOG_SERVER:
            return (
                False,
                f"Invalid ap-log-server '{value}'. Must be one of: {', '.join(VALID_BODY_AP_LOG_SERVER)}",
            )

    # Validate ap-log-server-port if present
    if "ap-log-server-port" in payload:
        value = payload.get("ap-log-server-port")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 65535:
                    return (
                        False,
                        "ap-log-server-port must be between 0 and 65535",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"ap-log-server-port must be numeric, got: {value}",
                )

    # Validate max-sta-offline if present
    if "max-sta-offline" in payload:
        value = payload.get("max-sta-offline")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "max-sta-offline must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"max-sta-offline must be numeric, got: {value}",
                )

    # Validate max-sta-offline-ip2mac if present
    if "max-sta-offline-ip2mac" in payload:
        value = payload.get("max-sta-offline-ip2mac")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "max-sta-offline-ip2mac must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"max-sta-offline-ip2mac must be numeric, got: {value}",
                )

    # Validate max-sta-cap if present
    if "max-sta-cap" in payload:
        value = payload.get("max-sta-cap")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "max-sta-cap must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (False, f"max-sta-cap must be numeric, got: {value}")

    # Validate max-sta-cap-wtp if present
    if "max-sta-cap-wtp" in payload:
        value = payload.get("max-sta-cap-wtp")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 8:
                    return (False, "max-sta-cap-wtp must be between 1 and 8")
            except (ValueError, TypeError):
                return (
                    False,
                    f"max-sta-cap-wtp must be numeric, got: {value}",
                )

    # Validate max-rogue-ap if present
    if "max-rogue-ap" in payload:
        value = payload.get("max-rogue-ap")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "max-rogue-ap must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (False, f"max-rogue-ap must be numeric, got: {value}")

    # Validate max-rogue-ap-wtp if present
    if "max-rogue-ap-wtp" in payload:
        value = payload.get("max-rogue-ap-wtp")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 16:
                    return (
                        False,
                        "max-rogue-ap-wtp must be between 1 and 16",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"max-rogue-ap-wtp must be numeric, got: {value}",
                )

    # Validate max-rogue-sta if present
    if "max-rogue-sta" in payload:
        value = payload.get("max-rogue-sta")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "max-rogue-sta must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (False, f"max-rogue-sta must be numeric, got: {value}")

    # Validate max-wids-entry if present
    if "max-wids-entry" in payload:
        value = payload.get("max-wids-entry")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "max-wids-entry must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (False, f"max-wids-entry must be numeric, got: {value}")

    # Validate max-ble-device if present
    if "max-ble-device" in payload:
        value = payload.get("max-ble-device")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "max-ble-device must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (False, f"max-ble-device must be numeric, got: {value}")

    # Validate dfs-lab-test if present
    if "dfs-lab-test" in payload:
        value = payload.get("dfs-lab-test")
        if value and value not in VALID_BODY_DFS_LAB_TEST:
            return (
                False,
                f"Invalid dfs-lab-test '{value}'. Must be one of: {', '.join(VALID_BODY_DFS_LAB_TEST)}",
            )

    return (True, None)
