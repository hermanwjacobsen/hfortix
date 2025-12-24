"""
Validation helpers for system ha endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_MODE = ["standalone", "a-a", "a-p"]
VALID_BODY_SYNC_PACKET_BALANCE = ["enable", "disable"]
VALID_BODY_LOAD_BALANCE_ALL = ["enable", "disable"]
VALID_BODY_SYNC_CONFIG = ["enable", "disable"]
VALID_BODY_ENCRYPTION = ["enable", "disable"]
VALID_BODY_AUTHENTICATION = ["enable", "disable"]
VALID_BODY_HB_INTERVAL_IN_MILLISECONDS = ["100ms", "10ms"]
VALID_BODY_GRATUITOUS_ARPS = ["enable", "disable"]
VALID_BODY_SESSION_PICKUP = ["enable", "disable"]
VALID_BODY_SESSION_PICKUP_CONNECTIONLESS = ["enable", "disable"]
VALID_BODY_SESSION_PICKUP_EXPECTATION = ["enable", "disable"]
VALID_BODY_SESSION_PICKUP_NAT = ["enable", "disable"]
VALID_BODY_SESSION_PICKUP_DELAY = ["enable", "disable"]
VALID_BODY_LINK_FAILED_SIGNAL = ["enable", "disable"]
VALID_BODY_UPGRADE_MODE = [
    "simultaneous",
    "uninterruptible",
    "local-only",
    "secondary-only",
]
VALID_BODY_STANDALONE_MGMT_VDOM = ["enable", "disable"]
VALID_BODY_HA_MGMT_STATUS = ["enable", "disable"]
VALID_BODY_STANDALONE_CONFIG_SYNC = ["enable", "disable"]
VALID_BODY_LOGICAL_SN = ["enable", "disable"]
VALID_BODY_SCHEDULE = [
    "none",
    "leastconnection",
    "round-robin",
    "weight-round-robin",
    "random",
    "ip",
    "ipport",
]
VALID_BODY_OVERRIDE = ["enable", "disable"]
VALID_BODY_PINGSERVER_SECONDARY_FORCE_RESET = ["enable", "disable"]
VALID_BODY_VCLUSTER_STATUS = ["enable", "disable"]
VALID_BODY_HA_DIRECT = ["enable", "disable"]
VALID_BODY_SSD_FAILOVER = ["enable", "disable"]
VALID_BODY_MEMORY_COMPATIBLE_MODE = ["enable", "disable"]
VALID_BODY_MEMORY_BASED_FAILOVER = ["enable", "disable"]
VALID_BODY_CHECK_SECONDARY_DEV_HEALTH = ["enable", "disable"]
VALID_BODY_IPSEC_PHASE2_PROPOSAL = [
    "aes128-sha1",
    "aes128-sha256",
    "aes128-sha384",
    "aes128-sha512",
    "aes192-sha1",
    "aes192-sha256",
    "aes192-sha384",
    "aes192-sha512",
    "aes256-sha1",
    "aes256-sha256",
    "aes256-sha384",
    "aes256-sha512",
    "aes128gcm",
    "aes256gcm",
    "chacha20poly1305",
]
VALID_BODY_BOUNCE_INTF_UPON_FAILOVER = ["enable", "disable"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_ha_get(
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


def validate_ha_put(
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

    # Validate group-id if present
    if "group-id" in payload:
        value = payload.get("group-id")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 1023:
                    return (False, "group-id must be between 0 and 1023")
            except (ValueError, TypeError):
                return (False, f"group-id must be numeric, got: {value}")

    # Validate group-name if present
    if "group-name" in payload:
        value = payload.get("group-name")
        if value and isinstance(value, str) and len(value) > 32:
            return (False, "group-name cannot exceed 32 characters")

    # Validate mode if present
    if "mode" in payload:
        value = payload.get("mode")
        if value and value not in VALID_BODY_MODE:
            return (
                False,
                f"Invalid mode '{value}'. Must be one of: {', '.join(VALID_BODY_MODE)}",
            )

    # Validate sync-packet-balance if present
    if "sync-packet-balance" in payload:
        value = payload.get("sync-packet-balance")
        if value and value not in VALID_BODY_SYNC_PACKET_BALANCE:
            return (
                False,
                f"Invalid sync-packet-balance '{value}'. Must be one of: {', '.join(VALID_BODY_SYNC_PACKET_BALANCE)}",
            )

    # Validate route-ttl if present
    if "route-ttl" in payload:
        value = payload.get("route-ttl")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 5 or int_val > 3600:
                    return (False, "route-ttl must be between 5 and 3600")
            except (ValueError, TypeError):
                return (False, f"route-ttl must be numeric, got: {value}")

    # Validate route-wait if present
    if "route-wait" in payload:
        value = payload.get("route-wait")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 3600:
                    return (False, "route-wait must be between 0 and 3600")
            except (ValueError, TypeError):
                return (False, f"route-wait must be numeric, got: {value}")

    # Validate route-hold if present
    if "route-hold" in payload:
        value = payload.get("route-hold")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 3600:
                    return (False, "route-hold must be between 0 and 3600")
            except (ValueError, TypeError):
                return (False, f"route-hold must be numeric, got: {value}")

    # Validate multicast-ttl if present
    if "multicast-ttl" in payload:
        value = payload.get("multicast-ttl")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 5 or int_val > 3600:
                    return (False, "multicast-ttl must be between 5 and 3600")
            except (ValueError, TypeError):
                return (False, f"multicast-ttl must be numeric, got: {value}")

    # Validate evpn-ttl if present
    if "evpn-ttl" in payload:
        value = payload.get("evpn-ttl")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 5 or int_val > 3600:
                    return (False, "evpn-ttl must be between 5 and 3600")
            except (ValueError, TypeError):
                return (False, f"evpn-ttl must be numeric, got: {value}")

    # Validate load-balance-all if present
    if "load-balance-all" in payload:
        value = payload.get("load-balance-all")
        if value and value not in VALID_BODY_LOAD_BALANCE_ALL:
            return (
                False,
                f"Invalid load-balance-all '{value}'. Must be one of: {', '.join(VALID_BODY_LOAD_BALANCE_ALL)}",
            )

    # Validate sync-config if present
    if "sync-config" in payload:
        value = payload.get("sync-config")
        if value and value not in VALID_BODY_SYNC_CONFIG:
            return (
                False,
                f"Invalid sync-config '{value}'. Must be one of: {', '.join(VALID_BODY_SYNC_CONFIG)}",
            )

    # Validate encryption if present
    if "encryption" in payload:
        value = payload.get("encryption")
        if value and value not in VALID_BODY_ENCRYPTION:
            return (
                False,
                f"Invalid encryption '{value}'. Must be one of: {', '.join(VALID_BODY_ENCRYPTION)}",
            )

    # Validate authentication if present
    if "authentication" in payload:
        value = payload.get("authentication")
        if value and value not in VALID_BODY_AUTHENTICATION:
            return (
                False,
                f"Invalid authentication '{value}'. Must be one of: {', '.join(VALID_BODY_AUTHENTICATION)}",
            )

    # Validate hb-interval if present
    if "hb-interval" in payload:
        value = payload.get("hb-interval")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 20:
                    return (False, "hb-interval must be between 1 and 20")
            except (ValueError, TypeError):
                return (False, f"hb-interval must be numeric, got: {value}")

    # Validate hb-interval-in-milliseconds if present
    if "hb-interval-in-milliseconds" in payload:
        value = payload.get("hb-interval-in-milliseconds")
        if value and value not in VALID_BODY_HB_INTERVAL_IN_MILLISECONDS:
            return (
                False,
                f"Invalid hb-interval-in-milliseconds '{value}'. Must be one of: {', '.join(VALID_BODY_HB_INTERVAL_IN_MILLISECONDS)}",
            )

    # Validate hb-lost-threshold if present
    if "hb-lost-threshold" in payload:
        value = payload.get("hb-lost-threshold")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 60:
                    return (
                        False,
                        "hb-lost-threshold must be between 1 and 60",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"hb-lost-threshold must be numeric, got: {value}",
                )

    # Validate hello-holddown if present
    if "hello-holddown" in payload:
        value = payload.get("hello-holddown")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 5 or int_val > 300:
                    return (False, "hello-holddown must be between 5 and 300")
            except (ValueError, TypeError):
                return (False, f"hello-holddown must be numeric, got: {value}")

    # Validate gratuitous-arps if present
    if "gratuitous-arps" in payload:
        value = payload.get("gratuitous-arps")
        if value and value not in VALID_BODY_GRATUITOUS_ARPS:
            return (
                False,
                f"Invalid gratuitous-arps '{value}'. Must be one of: {', '.join(VALID_BODY_GRATUITOUS_ARPS)}",
            )

    # Validate arps if present
    if "arps" in payload:
        value = payload.get("arps")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 60:
                    return (False, "arps must be between 1 and 60")
            except (ValueError, TypeError):
                return (False, f"arps must be numeric, got: {value}")

    # Validate arps-interval if present
    if "arps-interval" in payload:
        value = payload.get("arps-interval")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 20:
                    return (False, "arps-interval must be between 1 and 20")
            except (ValueError, TypeError):
                return (False, f"arps-interval must be numeric, got: {value}")

    # Validate session-pickup if present
    if "session-pickup" in payload:
        value = payload.get("session-pickup")
        if value and value not in VALID_BODY_SESSION_PICKUP:
            return (
                False,
                f"Invalid session-pickup '{value}'. Must be one of: {', '.join(VALID_BODY_SESSION_PICKUP)}",
            )

    # Validate session-pickup-connectionless if present
    if "session-pickup-connectionless" in payload:
        value = payload.get("session-pickup-connectionless")
        if value and value not in VALID_BODY_SESSION_PICKUP_CONNECTIONLESS:
            return (
                False,
                f"Invalid session-pickup-connectionless '{value}'. Must be one of: {', '.join(VALID_BODY_SESSION_PICKUP_CONNECTIONLESS)}",
            )

    # Validate session-pickup-expectation if present
    if "session-pickup-expectation" in payload:
        value = payload.get("session-pickup-expectation")
        if value and value not in VALID_BODY_SESSION_PICKUP_EXPECTATION:
            return (
                False,
                f"Invalid session-pickup-expectation '{value}'. Must be one of: {', '.join(VALID_BODY_SESSION_PICKUP_EXPECTATION)}",
            )

    # Validate session-pickup-nat if present
    if "session-pickup-nat" in payload:
        value = payload.get("session-pickup-nat")
        if value and value not in VALID_BODY_SESSION_PICKUP_NAT:
            return (
                False,
                f"Invalid session-pickup-nat '{value}'. Must be one of: {', '.join(VALID_BODY_SESSION_PICKUP_NAT)}",
            )

    # Validate session-pickup-delay if present
    if "session-pickup-delay" in payload:
        value = payload.get("session-pickup-delay")
        if value and value not in VALID_BODY_SESSION_PICKUP_DELAY:
            return (
                False,
                f"Invalid session-pickup-delay '{value}'. Must be one of: {', '.join(VALID_BODY_SESSION_PICKUP_DELAY)}",
            )

    # Validate link-failed-signal if present
    if "link-failed-signal" in payload:
        value = payload.get("link-failed-signal")
        if value and value not in VALID_BODY_LINK_FAILED_SIGNAL:
            return (
                False,
                f"Invalid link-failed-signal '{value}'. Must be one of: {', '.join(VALID_BODY_LINK_FAILED_SIGNAL)}",
            )

    # Validate upgrade-mode if present
    if "upgrade-mode" in payload:
        value = payload.get("upgrade-mode")
        if value and value not in VALID_BODY_UPGRADE_MODE:
            return (
                False,
                f"Invalid upgrade-mode '{value}'. Must be one of: {', '.join(VALID_BODY_UPGRADE_MODE)}",
            )

    # Validate uninterruptible-primary-wait if present
    if "uninterruptible-primary-wait" in payload:
        value = payload.get("uninterruptible-primary-wait")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 15 or int_val > 300:
                    return (
                        False,
                        "uninterruptible-primary-wait must be between 15 and 300",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"uninterruptible-primary-wait must be numeric, got: {value}",
                )

    # Validate standalone-mgmt-vdom if present
    if "standalone-mgmt-vdom" in payload:
        value = payload.get("standalone-mgmt-vdom")
        if value and value not in VALID_BODY_STANDALONE_MGMT_VDOM:
            return (
                False,
                f"Invalid standalone-mgmt-vdom '{value}'. Must be one of: {', '.join(VALID_BODY_STANDALONE_MGMT_VDOM)}",
            )

    # Validate ha-mgmt-status if present
    if "ha-mgmt-status" in payload:
        value = payload.get("ha-mgmt-status")
        if value and value not in VALID_BODY_HA_MGMT_STATUS:
            return (
                False,
                f"Invalid ha-mgmt-status '{value}'. Must be one of: {', '.join(VALID_BODY_HA_MGMT_STATUS)}",
            )

    # Validate ha-eth-type if present
    if "ha-eth-type" in payload:
        value = payload.get("ha-eth-type")
        if value and isinstance(value, str) and len(value) > 4:
            return (False, "ha-eth-type cannot exceed 4 characters")

    # Validate hc-eth-type if present
    if "hc-eth-type" in payload:
        value = payload.get("hc-eth-type")
        if value and isinstance(value, str) and len(value) > 4:
            return (False, "hc-eth-type cannot exceed 4 characters")

    # Validate l2ep-eth-type if present
    if "l2ep-eth-type" in payload:
        value = payload.get("l2ep-eth-type")
        if value and isinstance(value, str) and len(value) > 4:
            return (False, "l2ep-eth-type cannot exceed 4 characters")

    # Validate ha-uptime-diff-margin if present
    if "ha-uptime-diff-margin" in payload:
        value = payload.get("ha-uptime-diff-margin")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 65535:
                    return (
                        False,
                        "ha-uptime-diff-margin must be between 1 and 65535",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"ha-uptime-diff-margin must be numeric, got: {value}",
                )

    # Validate standalone-config-sync if present
    if "standalone-config-sync" in payload:
        value = payload.get("standalone-config-sync")
        if value and value not in VALID_BODY_STANDALONE_CONFIG_SYNC:
            return (
                False,
                f"Invalid standalone-config-sync '{value}'. Must be one of: {', '.join(VALID_BODY_STANDALONE_CONFIG_SYNC)}",
            )

    # Validate logical-sn if present
    if "logical-sn" in payload:
        value = payload.get("logical-sn")
        if value and value not in VALID_BODY_LOGICAL_SN:
            return (
                False,
                f"Invalid logical-sn '{value}'. Must be one of: {', '.join(VALID_BODY_LOGICAL_SN)}",
            )

    # Validate schedule if present
    if "schedule" in payload:
        value = payload.get("schedule")
        if value and value not in VALID_BODY_SCHEDULE:
            return (
                False,
                f"Invalid schedule '{value}'. Must be one of: {', '.join(VALID_BODY_SCHEDULE)}",
            )

    # Validate override if present
    if "override" in payload:
        value = payload.get("override")
        if value and value not in VALID_BODY_OVERRIDE:
            return (
                False,
                f"Invalid override '{value}'. Must be one of: {', '.join(VALID_BODY_OVERRIDE)}",
            )

    # Validate priority if present
    if "priority" in payload:
        value = payload.get("priority")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 255:
                    return (False, "priority must be between 0 and 255")
            except (ValueError, TypeError):
                return (False, f"priority must be numeric, got: {value}")

    # Validate override-wait-time if present
    if "override-wait-time" in payload:
        value = payload.get("override-wait-time")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 3600:
                    return (
                        False,
                        "override-wait-time must be between 0 and 3600",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"override-wait-time must be numeric, got: {value}",
                )

    # Validate pingserver-failover-threshold if present
    if "pingserver-failover-threshold" in payload:
        value = payload.get("pingserver-failover-threshold")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 50:
                    return (
                        False,
                        "pingserver-failover-threshold must be between 0 and 50",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"pingserver-failover-threshold must be numeric, got: {value}",
                )

    # Validate pingserver-secondary-force-reset if present
    if "pingserver-secondary-force-reset" in payload:
        value = payload.get("pingserver-secondary-force-reset")
        if value and value not in VALID_BODY_PINGSERVER_SECONDARY_FORCE_RESET:
            return (
                False,
                f"Invalid pingserver-secondary-force-reset '{value}'. Must be one of: {', '.join(VALID_BODY_PINGSERVER_SECONDARY_FORCE_RESET)}",
            )

    # Validate pingserver-flip-timeout if present
    if "pingserver-flip-timeout" in payload:
        value = payload.get("pingserver-flip-timeout")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 6 or int_val > 2147483647:
                    return (
                        False,
                        "pingserver-flip-timeout must be between 6 and 2147483647",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"pingserver-flip-timeout must be numeric, got: {value}",
                )

    # Validate vcluster-status if present
    if "vcluster-status" in payload:
        value = payload.get("vcluster-status")
        if value and value not in VALID_BODY_VCLUSTER_STATUS:
            return (
                False,
                f"Invalid vcluster-status '{value}'. Must be one of: {', '.join(VALID_BODY_VCLUSTER_STATUS)}",
            )

    # Validate ha-direct if present
    if "ha-direct" in payload:
        value = payload.get("ha-direct")
        if value and value not in VALID_BODY_HA_DIRECT:
            return (
                False,
                f"Invalid ha-direct '{value}'. Must be one of: {', '.join(VALID_BODY_HA_DIRECT)}",
            )

    # Validate ssd-failover if present
    if "ssd-failover" in payload:
        value = payload.get("ssd-failover")
        if value and value not in VALID_BODY_SSD_FAILOVER:
            return (
                False,
                f"Invalid ssd-failover '{value}'. Must be one of: {', '.join(VALID_BODY_SSD_FAILOVER)}",
            )

    # Validate memory-compatible-mode if present
    if "memory-compatible-mode" in payload:
        value = payload.get("memory-compatible-mode")
        if value and value not in VALID_BODY_MEMORY_COMPATIBLE_MODE:
            return (
                False,
                f"Invalid memory-compatible-mode '{value}'. Must be one of: {', '.join(VALID_BODY_MEMORY_COMPATIBLE_MODE)}",
            )

    # Validate memory-based-failover if present
    if "memory-based-failover" in payload:
        value = payload.get("memory-based-failover")
        if value and value not in VALID_BODY_MEMORY_BASED_FAILOVER:
            return (
                False,
                f"Invalid memory-based-failover '{value}'. Must be one of: {', '.join(VALID_BODY_MEMORY_BASED_FAILOVER)}",
            )

    # Validate memory-failover-threshold if present
    if "memory-failover-threshold" in payload:
        value = payload.get("memory-failover-threshold")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 95:
                    return (
                        False,
                        "memory-failover-threshold must be between 0 and 95",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"memory-failover-threshold must be numeric, got: {value}",
                )

    # Validate memory-failover-monitor-period if present
    if "memory-failover-monitor-period" in payload:
        value = payload.get("memory-failover-monitor-period")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 300:
                    return (
                        False,
                        "memory-failover-monitor-period must be between 1 and 300",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"memory-failover-monitor-period must be numeric, got: {value}",
                )

    # Validate memory-failover-sample-rate if present
    if "memory-failover-sample-rate" in payload:
        value = payload.get("memory-failover-sample-rate")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 60:
                    return (
                        False,
                        "memory-failover-sample-rate must be between 1 and 60",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"memory-failover-sample-rate must be numeric, got: {value}",
                )

    # Validate memory-failover-flip-timeout if present
    if "memory-failover-flip-timeout" in payload:
        value = payload.get("memory-failover-flip-timeout")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 6 or int_val > 2147483647:
                    return (
                        False,
                        "memory-failover-flip-timeout must be between 6 and 2147483647",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"memory-failover-flip-timeout must be numeric, got: {value}",
                )

    # Validate failover-hold-time if present
    if "failover-hold-time" in payload:
        value = payload.get("failover-hold-time")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 300:
                    return (
                        False,
                        "failover-hold-time must be between 0 and 300",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"failover-hold-time must be numeric, got: {value}",
                )

    # Validate check-secondary-dev-health if present
    if "check-secondary-dev-health" in payload:
        value = payload.get("check-secondary-dev-health")
        if value and value not in VALID_BODY_CHECK_SECONDARY_DEV_HEALTH:
            return (
                False,
                f"Invalid check-secondary-dev-health '{value}'. Must be one of: {', '.join(VALID_BODY_CHECK_SECONDARY_DEV_HEALTH)}",
            )

    # Validate ipsec-phase2-proposal if present
    if "ipsec-phase2-proposal" in payload:
        value = payload.get("ipsec-phase2-proposal")
        if value and value not in VALID_BODY_IPSEC_PHASE2_PROPOSAL:
            return (
                False,
                f"Invalid ipsec-phase2-proposal '{value}'. Must be one of: {', '.join(VALID_BODY_IPSEC_PHASE2_PROPOSAL)}",
            )

    # Validate bounce-intf-upon-failover if present
    if "bounce-intf-upon-failover" in payload:
        value = payload.get("bounce-intf-upon-failover")
        if value and value not in VALID_BODY_BOUNCE_INTF_UPON_FAILOVER:
            return (
                False,
                f"Invalid bounce-intf-upon-failover '{value}'. Must be one of: {', '.join(VALID_BODY_BOUNCE_INTF_UPON_FAILOVER)}",
            )

    return (True, None)
