"""
Validation helpers for wireless-controller wtp endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_ADMIN = ["discovered", "disable", "enable"]
VALID_BODY_FIRMWARE_PROVISION_LATEST = ["disable", "once"]
VALID_BODY_OVERRIDE_LED_STATE = ["enable", "disable"]
VALID_BODY_LED_STATE = ["enable", "disable"]
VALID_BODY_OVERRIDE_WAN_PORT_MODE = ["enable", "disable"]
VALID_BODY_WAN_PORT_MODE = ["wan-lan", "wan-only"]
VALID_BODY_OVERRIDE_IP_FRAGMENT = ["enable", "disable"]
VALID_BODY_IP_FRAGMENT_PREVENTING = ["tcp-mss-adjust", "icmp-unreachable"]
VALID_BODY_OVERRIDE_SPLIT_TUNNEL = ["enable", "disable"]
VALID_BODY_SPLIT_TUNNELING_ACL_PATH = ["tunnel", "local"]
VALID_BODY_SPLIT_TUNNELING_ACL_LOCAL_AP_SUBNET = ["enable", "disable"]
VALID_BODY_OVERRIDE_LAN = ["enable", "disable"]
VALID_BODY_OVERRIDE_ALLOWACCESS = ["enable", "disable"]
VALID_BODY_ALLOWACCESS = ["https", "ssh", "snmp"]
VALID_BODY_OVERRIDE_LOGIN_PASSWD_CHANGE = ["enable", "disable"]
VALID_BODY_LOGIN_PASSWD_CHANGE = ["yes", "default", "no"]
VALID_BODY_OVERRIDE_DEFAULT_MESH_ROOT = ["enable", "disable"]
VALID_BODY_DEFAULT_MESH_ROOT = ["enable", "disable"]
VALID_BODY_IMAGE_DOWNLOAD = ["enable", "disable"]
VALID_BODY_MESH_BRIDGE_ENABLE = ["default", "enable", "disable"]
VALID_BODY_PURDUE_LEVEL = ["1", "1.5", "2", "2.5", "3", "3.5", "4", "5", "5.5"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_wtp_get(
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


def validate_wtp_post(payload: dict[str, Any]) -> tuple[bool, str | None]:
    """
    Validate POST request payload for creating wtp.

    Args:
        payload: The payload to validate

    Returns:
        Tuple of (is_valid, error_message)
    """
    # Validate wtp-id if present
    if "wtp-id" in payload:
        value = payload.get("wtp-id")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "wtp-id cannot exceed 35 characters")

    # Validate index if present
    if "index" in payload:
        value = payload.get("index")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (False, "index must be between 0 and 4294967295")
            except (ValueError, TypeError):
                return (False, f"index must be numeric, got: {value}")

    # Validate admin if present
    if "admin" in payload:
        value = payload.get("admin")
        if value and value not in VALID_BODY_ADMIN:
            return (
                False,
                f"Invalid admin '{value}'. Must be one of: {', '.join(VALID_BODY_ADMIN)}",
            )

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

    # Validate comment if present
    if "comment" in payload:
        value = payload.get("comment")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "comment cannot exceed 255 characters")

    # Validate region if present
    if "region" in payload:
        value = payload.get("region")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "region cannot exceed 35 characters")

    # Validate region-x if present
    if "region-x" in payload:
        value = payload.get("region-x")
        if value and isinstance(value, str) and len(value) > 15:
            return (False, "region-x cannot exceed 15 characters")

    # Validate region-y if present
    if "region-y" in payload:
        value = payload.get("region-y")
        if value and isinstance(value, str) and len(value) > 15:
            return (False, "region-y cannot exceed 15 characters")

    # Validate firmware-provision if present
    if "firmware-provision" in payload:
        value = payload.get("firmware-provision")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "firmware-provision cannot exceed 35 characters")

    # Validate firmware-provision-latest if present
    if "firmware-provision-latest" in payload:
        value = payload.get("firmware-provision-latest")
        if value and value not in VALID_BODY_FIRMWARE_PROVISION_LATEST:
            return (
                False,
                f"Invalid firmware-provision-latest '{value}'. Must be one of: {', '.join(VALID_BODY_FIRMWARE_PROVISION_LATEST)}",
            )

    # Validate wtp-profile if present
    if "wtp-profile" in payload:
        value = payload.get("wtp-profile")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "wtp-profile cannot exceed 35 characters")

    # Validate apcfg-profile if present
    if "apcfg-profile" in payload:
        value = payload.get("apcfg-profile")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "apcfg-profile cannot exceed 35 characters")

    # Validate bonjour-profile if present
    if "bonjour-profile" in payload:
        value = payload.get("bonjour-profile")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "bonjour-profile cannot exceed 35 characters")

    # Validate ble-major-id if present
    if "ble-major-id" in payload:
        value = payload.get("ble-major-id")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 65535:
                    return (False, "ble-major-id must be between 0 and 65535")
            except (ValueError, TypeError):
                return (False, f"ble-major-id must be numeric, got: {value}")

    # Validate ble-minor-id if present
    if "ble-minor-id" in payload:
        value = payload.get("ble-minor-id")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 65535:
                    return (False, "ble-minor-id must be between 0 and 65535")
            except (ValueError, TypeError):
                return (False, f"ble-minor-id must be numeric, got: {value}")

    # Validate override-led-state if present
    if "override-led-state" in payload:
        value = payload.get("override-led-state")
        if value and value not in VALID_BODY_OVERRIDE_LED_STATE:
            return (
                False,
                f"Invalid override-led-state '{value}'. Must be one of: {', '.join(VALID_BODY_OVERRIDE_LED_STATE)}",
            )

    # Validate led-state if present
    if "led-state" in payload:
        value = payload.get("led-state")
        if value and value not in VALID_BODY_LED_STATE:
            return (
                False,
                f"Invalid led-state '{value}'. Must be one of: {', '.join(VALID_BODY_LED_STATE)}",
            )

    # Validate override-wan-port-mode if present
    if "override-wan-port-mode" in payload:
        value = payload.get("override-wan-port-mode")
        if value and value not in VALID_BODY_OVERRIDE_WAN_PORT_MODE:
            return (
                False,
                f"Invalid override-wan-port-mode '{value}'. Must be one of: {', '.join(VALID_BODY_OVERRIDE_WAN_PORT_MODE)}",
            )

    # Validate wan-port-mode if present
    if "wan-port-mode" in payload:
        value = payload.get("wan-port-mode")
        if value and value not in VALID_BODY_WAN_PORT_MODE:
            return (
                False,
                f"Invalid wan-port-mode '{value}'. Must be one of: {', '.join(VALID_BODY_WAN_PORT_MODE)}",
            )

    # Validate override-ip-fragment if present
    if "override-ip-fragment" in payload:
        value = payload.get("override-ip-fragment")
        if value and value not in VALID_BODY_OVERRIDE_IP_FRAGMENT:
            return (
                False,
                f"Invalid override-ip-fragment '{value}'. Must be one of: {', '.join(VALID_BODY_OVERRIDE_IP_FRAGMENT)}",
            )

    # Validate ip-fragment-preventing if present
    if "ip-fragment-preventing" in payload:
        value = payload.get("ip-fragment-preventing")
        if value and value not in VALID_BODY_IP_FRAGMENT_PREVENTING:
            return (
                False,
                f"Invalid ip-fragment-preventing '{value}'. Must be one of: {', '.join(VALID_BODY_IP_FRAGMENT_PREVENTING)}",
            )

    # Validate tun-mtu-uplink if present
    if "tun-mtu-uplink" in payload:
        value = payload.get("tun-mtu-uplink")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 576 or int_val > 1500:
                    return (
                        False,
                        "tun-mtu-uplink must be between 576 and 1500",
                    )
            except (ValueError, TypeError):
                return (False, f"tun-mtu-uplink must be numeric, got: {value}")

    # Validate tun-mtu-downlink if present
    if "tun-mtu-downlink" in payload:
        value = payload.get("tun-mtu-downlink")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 576 or int_val > 1500:
                    return (
                        False,
                        "tun-mtu-downlink must be between 576 and 1500",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"tun-mtu-downlink must be numeric, got: {value}",
                )

    # Validate override-split-tunnel if present
    if "override-split-tunnel" in payload:
        value = payload.get("override-split-tunnel")
        if value and value not in VALID_BODY_OVERRIDE_SPLIT_TUNNEL:
            return (
                False,
                f"Invalid override-split-tunnel '{value}'. Must be one of: {', '.join(VALID_BODY_OVERRIDE_SPLIT_TUNNEL)}",
            )

    # Validate split-tunneling-acl-path if present
    if "split-tunneling-acl-path" in payload:
        value = payload.get("split-tunneling-acl-path")
        if value and value not in VALID_BODY_SPLIT_TUNNELING_ACL_PATH:
            return (
                False,
                f"Invalid split-tunneling-acl-path '{value}'. Must be one of: {', '.join(VALID_BODY_SPLIT_TUNNELING_ACL_PATH)}",
            )

    # Validate split-tunneling-acl-local-ap-subnet if present
    if "split-tunneling-acl-local-ap-subnet" in payload:
        value = payload.get("split-tunneling-acl-local-ap-subnet")
        if (
            value
            and value not in VALID_BODY_SPLIT_TUNNELING_ACL_LOCAL_AP_SUBNET
        ):
            return (
                False,
                f"Invalid split-tunneling-acl-local-ap-subnet '{value}'. Must be one of: {', '.join(VALID_BODY_SPLIT_TUNNELING_ACL_LOCAL_AP_SUBNET)}",
            )

    # Validate override-lan if present
    if "override-lan" in payload:
        value = payload.get("override-lan")
        if value and value not in VALID_BODY_OVERRIDE_LAN:
            return (
                False,
                f"Invalid override-lan '{value}'. Must be one of: {', '.join(VALID_BODY_OVERRIDE_LAN)}",
            )

    # Validate override-allowaccess if present
    if "override-allowaccess" in payload:
        value = payload.get("override-allowaccess")
        if value and value not in VALID_BODY_OVERRIDE_ALLOWACCESS:
            return (
                False,
                f"Invalid override-allowaccess '{value}'. Must be one of: {', '.join(VALID_BODY_OVERRIDE_ALLOWACCESS)}",
            )

    # Validate allowaccess if present
    if "allowaccess" in payload:
        value = payload.get("allowaccess")
        if value and value not in VALID_BODY_ALLOWACCESS:
            return (
                False,
                f"Invalid allowaccess '{value}'. Must be one of: {', '.join(VALID_BODY_ALLOWACCESS)}",
            )

    # Validate override-login-passwd-change if present
    if "override-login-passwd-change" in payload:
        value = payload.get("override-login-passwd-change")
        if value and value not in VALID_BODY_OVERRIDE_LOGIN_PASSWD_CHANGE:
            return (
                False,
                f"Invalid override-login-passwd-change '{value}'. Must be one of: {', '.join(VALID_BODY_OVERRIDE_LOGIN_PASSWD_CHANGE)}",
            )

    # Validate login-passwd-change if present
    if "login-passwd-change" in payload:
        value = payload.get("login-passwd-change")
        if value and value not in VALID_BODY_LOGIN_PASSWD_CHANGE:
            return (
                False,
                f"Invalid login-passwd-change '{value}'. Must be one of: {', '.join(VALID_BODY_LOGIN_PASSWD_CHANGE)}",
            )

    # Validate override-default-mesh-root if present
    if "override-default-mesh-root" in payload:
        value = payload.get("override-default-mesh-root")
        if value and value not in VALID_BODY_OVERRIDE_DEFAULT_MESH_ROOT:
            return (
                False,
                f"Invalid override-default-mesh-root '{value}'. Must be one of: {', '.join(VALID_BODY_OVERRIDE_DEFAULT_MESH_ROOT)}",
            )

    # Validate default-mesh-root if present
    if "default-mesh-root" in payload:
        value = payload.get("default-mesh-root")
        if value and value not in VALID_BODY_DEFAULT_MESH_ROOT:
            return (
                False,
                f"Invalid default-mesh-root '{value}'. Must be one of: {', '.join(VALID_BODY_DEFAULT_MESH_ROOT)}",
            )

    # Validate image-download if present
    if "image-download" in payload:
        value = payload.get("image-download")
        if value and value not in VALID_BODY_IMAGE_DOWNLOAD:
            return (
                False,
                f"Invalid image-download '{value}'. Must be one of: {', '.join(VALID_BODY_IMAGE_DOWNLOAD)}",
            )

    # Validate mesh-bridge-enable if present
    if "mesh-bridge-enable" in payload:
        value = payload.get("mesh-bridge-enable")
        if value and value not in VALID_BODY_MESH_BRIDGE_ENABLE:
            return (
                False,
                f"Invalid mesh-bridge-enable '{value}'. Must be one of: {', '.join(VALID_BODY_MESH_BRIDGE_ENABLE)}",
            )

    # Validate purdue-level if present
    if "purdue-level" in payload:
        value = payload.get("purdue-level")
        if value and value not in VALID_BODY_PURDUE_LEVEL:
            return (
                False,
                f"Invalid purdue-level '{value}'. Must be one of: {', '.join(VALID_BODY_PURDUE_LEVEL)}",
            )

    # Validate coordinate-latitude if present
    if "coordinate-latitude" in payload:
        value = payload.get("coordinate-latitude")
        if value and isinstance(value, str) and len(value) > 19:
            return (False, "coordinate-latitude cannot exceed 19 characters")

    # Validate coordinate-longitude if present
    if "coordinate-longitude" in payload:
        value = payload.get("coordinate-longitude")
        if value and isinstance(value, str) and len(value) > 19:
            return (False, "coordinate-longitude cannot exceed 19 characters")

    return (True, None)
