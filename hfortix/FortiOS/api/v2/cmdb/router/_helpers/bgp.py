"""
Validation helpers for router bgp endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_ALWAYS_COMPARE_MED = ["enable", "disable"]
VALID_BODY_BESTPATH_AS_PATH_IGNORE = ["enable", "disable"]
VALID_BODY_BESTPATH_CMP_CONFED_ASPATH = ["enable", "disable"]
VALID_BODY_BESTPATH_CMP_ROUTERID = ["enable", "disable"]
VALID_BODY_BESTPATH_MED_CONFED = ["enable", "disable"]
VALID_BODY_BESTPATH_MED_MISSING_AS_WORST = ["enable", "disable"]
VALID_BODY_CLIENT_TO_CLIENT_REFLECTION = ["enable", "disable"]
VALID_BODY_DAMPENING = ["enable", "disable"]
VALID_BODY_DETERMINISTIC_MED = ["enable", "disable"]
VALID_BODY_EBGP_MULTIPATH = ["enable", "disable"]
VALID_BODY_IBGP_MULTIPATH = ["enable", "disable"]
VALID_BODY_ENFORCE_FIRST_AS = ["enable", "disable"]
VALID_BODY_FAST_EXTERNAL_FAILOVER = ["enable", "disable"]
VALID_BODY_LOG_NEIGHBOUR_CHANGES = ["enable", "disable"]
VALID_BODY_NETWORK_IMPORT_CHECK = ["enable", "disable"]
VALID_BODY_IGNORE_OPTIONAL_CAPABILITY = ["enable", "disable"]
VALID_BODY_ADDITIONAL_PATH = ["enable", "disable"]
VALID_BODY_ADDITIONAL_PATH6 = ["enable", "disable"]
VALID_BODY_ADDITIONAL_PATH_VPNV4 = ["enable", "disable"]
VALID_BODY_ADDITIONAL_PATH_VPNV6 = ["enable", "disable"]
VALID_BODY_MULTIPATH_RECURSIVE_DISTANCE = ["enable", "disable"]
VALID_BODY_RECURSIVE_NEXT_HOP = ["enable", "disable"]
VALID_BODY_RECURSIVE_INHERIT_PRIORITY = ["enable", "disable"]
VALID_BODY_TAG_RESOLVE_MODE = ["disable", "preferred", "merge", "merge-all"]
VALID_BODY_SYNCHRONIZATION = ["enable", "disable"]
VALID_BODY_GRACEFUL_RESTART = ["enable", "disable"]
VALID_BODY_GRACEFUL_END_ON_TIMER = ["enable", "disable"]
VALID_BODY_CROSS_FAMILY_CONDITIONAL_ADV = ["enable", "disable"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_bgp_get(
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


def validate_bgp_put(
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

    # Validate keepalive-timer if present
    if "keepalive-timer" in payload:
        value = payload.get("keepalive-timer")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 65535:
                    return (
                        False,
                        "keepalive-timer must be between 0 and 65535",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"keepalive-timer must be numeric, got: {value}",
                )

    # Validate holdtime-timer if present
    if "holdtime-timer" in payload:
        value = payload.get("holdtime-timer")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 3 or int_val > 65535:
                    return (
                        False,
                        "holdtime-timer must be between 3 and 65535",
                    )
            except (ValueError, TypeError):
                return (False, f"holdtime-timer must be numeric, got: {value}")

    # Validate always-compare-med if present
    if "always-compare-med" in payload:
        value = payload.get("always-compare-med")
        if value and value not in VALID_BODY_ALWAYS_COMPARE_MED:
            return (
                False,
                f"Invalid always-compare-med '{value}'. Must be one of: {', '.join(VALID_BODY_ALWAYS_COMPARE_MED)}",
            )

    # Validate bestpath-as-path-ignore if present
    if "bestpath-as-path-ignore" in payload:
        value = payload.get("bestpath-as-path-ignore")
        if value and value not in VALID_BODY_BESTPATH_AS_PATH_IGNORE:
            return (
                False,
                f"Invalid bestpath-as-path-ignore '{value}'. Must be one of: {', '.join(VALID_BODY_BESTPATH_AS_PATH_IGNORE)}",
            )

    # Validate bestpath-cmp-confed-aspath if present
    if "bestpath-cmp-confed-aspath" in payload:
        value = payload.get("bestpath-cmp-confed-aspath")
        if value and value not in VALID_BODY_BESTPATH_CMP_CONFED_ASPATH:
            return (
                False,
                f"Invalid bestpath-cmp-confed-aspath '{value}'. Must be one of: {', '.join(VALID_BODY_BESTPATH_CMP_CONFED_ASPATH)}",
            )

    # Validate bestpath-cmp-routerid if present
    if "bestpath-cmp-routerid" in payload:
        value = payload.get("bestpath-cmp-routerid")
        if value and value not in VALID_BODY_BESTPATH_CMP_ROUTERID:
            return (
                False,
                f"Invalid bestpath-cmp-routerid '{value}'. Must be one of: {', '.join(VALID_BODY_BESTPATH_CMP_ROUTERID)}",
            )

    # Validate bestpath-med-confed if present
    if "bestpath-med-confed" in payload:
        value = payload.get("bestpath-med-confed")
        if value and value not in VALID_BODY_BESTPATH_MED_CONFED:
            return (
                False,
                f"Invalid bestpath-med-confed '{value}'. Must be one of: {', '.join(VALID_BODY_BESTPATH_MED_CONFED)}",
            )

    # Validate bestpath-med-missing-as-worst if present
    if "bestpath-med-missing-as-worst" in payload:
        value = payload.get("bestpath-med-missing-as-worst")
        if value and value not in VALID_BODY_BESTPATH_MED_MISSING_AS_WORST:
            return (
                False,
                f"Invalid bestpath-med-missing-as-worst '{value}'. Must be one of: {', '.join(VALID_BODY_BESTPATH_MED_MISSING_AS_WORST)}",
            )

    # Validate client-to-client-reflection if present
    if "client-to-client-reflection" in payload:
        value = payload.get("client-to-client-reflection")
        if value and value not in VALID_BODY_CLIENT_TO_CLIENT_REFLECTION:
            return (
                False,
                f"Invalid client-to-client-reflection '{value}'. Must be one of: {', '.join(VALID_BODY_CLIENT_TO_CLIENT_REFLECTION)}",
            )

    # Validate dampening if present
    if "dampening" in payload:
        value = payload.get("dampening")
        if value and value not in VALID_BODY_DAMPENING:
            return (
                False,
                f"Invalid dampening '{value}'. Must be one of: {', '.join(VALID_BODY_DAMPENING)}",
            )

    # Validate deterministic-med if present
    if "deterministic-med" in payload:
        value = payload.get("deterministic-med")
        if value and value not in VALID_BODY_DETERMINISTIC_MED:
            return (
                False,
                f"Invalid deterministic-med '{value}'. Must be one of: {', '.join(VALID_BODY_DETERMINISTIC_MED)}",
            )

    # Validate ebgp-multipath if present
    if "ebgp-multipath" in payload:
        value = payload.get("ebgp-multipath")
        if value and value not in VALID_BODY_EBGP_MULTIPATH:
            return (
                False,
                f"Invalid ebgp-multipath '{value}'. Must be one of: {', '.join(VALID_BODY_EBGP_MULTIPATH)}",
            )

    # Validate ibgp-multipath if present
    if "ibgp-multipath" in payload:
        value = payload.get("ibgp-multipath")
        if value and value not in VALID_BODY_IBGP_MULTIPATH:
            return (
                False,
                f"Invalid ibgp-multipath '{value}'. Must be one of: {', '.join(VALID_BODY_IBGP_MULTIPATH)}",
            )

    # Validate enforce-first-as if present
    if "enforce-first-as" in payload:
        value = payload.get("enforce-first-as")
        if value and value not in VALID_BODY_ENFORCE_FIRST_AS:
            return (
                False,
                f"Invalid enforce-first-as '{value}'. Must be one of: {', '.join(VALID_BODY_ENFORCE_FIRST_AS)}",
            )

    # Validate fast-external-failover if present
    if "fast-external-failover" in payload:
        value = payload.get("fast-external-failover")
        if value and value not in VALID_BODY_FAST_EXTERNAL_FAILOVER:
            return (
                False,
                f"Invalid fast-external-failover '{value}'. Must be one of: {', '.join(VALID_BODY_FAST_EXTERNAL_FAILOVER)}",
            )

    # Validate log-neighbour-changes if present
    if "log-neighbour-changes" in payload:
        value = payload.get("log-neighbour-changes")
        if value and value not in VALID_BODY_LOG_NEIGHBOUR_CHANGES:
            return (
                False,
                f"Invalid log-neighbour-changes '{value}'. Must be one of: {', '.join(VALID_BODY_LOG_NEIGHBOUR_CHANGES)}",
            )

    # Validate network-import-check if present
    if "network-import-check" in payload:
        value = payload.get("network-import-check")
        if value and value not in VALID_BODY_NETWORK_IMPORT_CHECK:
            return (
                False,
                f"Invalid network-import-check '{value}'. Must be one of: {', '.join(VALID_BODY_NETWORK_IMPORT_CHECK)}",
            )

    # Validate ignore-optional-capability if present
    if "ignore-optional-capability" in payload:
        value = payload.get("ignore-optional-capability")
        if value and value not in VALID_BODY_IGNORE_OPTIONAL_CAPABILITY:
            return (
                False,
                f"Invalid ignore-optional-capability '{value}'. Must be one of: {', '.join(VALID_BODY_IGNORE_OPTIONAL_CAPABILITY)}",
            )

    # Validate additional-path if present
    if "additional-path" in payload:
        value = payload.get("additional-path")
        if value and value not in VALID_BODY_ADDITIONAL_PATH:
            return (
                False,
                f"Invalid additional-path '{value}'. Must be one of: {', '.join(VALID_BODY_ADDITIONAL_PATH)}",
            )

    # Validate additional-path6 if present
    if "additional-path6" in payload:
        value = payload.get("additional-path6")
        if value and value not in VALID_BODY_ADDITIONAL_PATH6:
            return (
                False,
                f"Invalid additional-path6 '{value}'. Must be one of: {', '.join(VALID_BODY_ADDITIONAL_PATH6)}",
            )

    # Validate additional-path-vpnv4 if present
    if "additional-path-vpnv4" in payload:
        value = payload.get("additional-path-vpnv4")
        if value and value not in VALID_BODY_ADDITIONAL_PATH_VPNV4:
            return (
                False,
                f"Invalid additional-path-vpnv4 '{value}'. Must be one of: {', '.join(VALID_BODY_ADDITIONAL_PATH_VPNV4)}",
            )

    # Validate additional-path-vpnv6 if present
    if "additional-path-vpnv6" in payload:
        value = payload.get("additional-path-vpnv6")
        if value and value not in VALID_BODY_ADDITIONAL_PATH_VPNV6:
            return (
                False,
                f"Invalid additional-path-vpnv6 '{value}'. Must be one of: {', '.join(VALID_BODY_ADDITIONAL_PATH_VPNV6)}",
            )

    # Validate multipath-recursive-distance if present
    if "multipath-recursive-distance" in payload:
        value = payload.get("multipath-recursive-distance")
        if value and value not in VALID_BODY_MULTIPATH_RECURSIVE_DISTANCE:
            return (
                False,
                f"Invalid multipath-recursive-distance '{value}'. Must be one of: {', '.join(VALID_BODY_MULTIPATH_RECURSIVE_DISTANCE)}",
            )

    # Validate recursive-next-hop if present
    if "recursive-next-hop" in payload:
        value = payload.get("recursive-next-hop")
        if value and value not in VALID_BODY_RECURSIVE_NEXT_HOP:
            return (
                False,
                f"Invalid recursive-next-hop '{value}'. Must be one of: {', '.join(VALID_BODY_RECURSIVE_NEXT_HOP)}",
            )

    # Validate recursive-inherit-priority if present
    if "recursive-inherit-priority" in payload:
        value = payload.get("recursive-inherit-priority")
        if value and value not in VALID_BODY_RECURSIVE_INHERIT_PRIORITY:
            return (
                False,
                f"Invalid recursive-inherit-priority '{value}'. Must be one of: {', '.join(VALID_BODY_RECURSIVE_INHERIT_PRIORITY)}",
            )

    # Validate tag-resolve-mode if present
    if "tag-resolve-mode" in payload:
        value = payload.get("tag-resolve-mode")
        if value and value not in VALID_BODY_TAG_RESOLVE_MODE:
            return (
                False,
                f"Invalid tag-resolve-mode '{value}'. Must be one of: {', '.join(VALID_BODY_TAG_RESOLVE_MODE)}",
            )

    # Validate confederation-identifier if present
    if "confederation-identifier" in payload:
        value = payload.get("confederation-identifier")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 4294967295:
                    return (
                        False,
                        "confederation-identifier must be between 1 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"confederation-identifier must be numeric, got: {value}",
                )

    # Validate dampening-route-map if present
    if "dampening-route-map" in payload:
        value = payload.get("dampening-route-map")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "dampening-route-map cannot exceed 35 characters")

    # Validate dampening-reachability-half-life if present
    if "dampening-reachability-half-life" in payload:
        value = payload.get("dampening-reachability-half-life")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 45:
                    return (
                        False,
                        "dampening-reachability-half-life must be between 1 and 45",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"dampening-reachability-half-life must be numeric, got: {value}",
                )

    # Validate dampening-reuse if present
    if "dampening-reuse" in payload:
        value = payload.get("dampening-reuse")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 20000:
                    return (
                        False,
                        "dampening-reuse must be between 1 and 20000",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"dampening-reuse must be numeric, got: {value}",
                )

    # Validate dampening-suppress if present
    if "dampening-suppress" in payload:
        value = payload.get("dampening-suppress")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 20000:
                    return (
                        False,
                        "dampening-suppress must be between 1 and 20000",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"dampening-suppress must be numeric, got: {value}",
                )

    # Validate dampening-max-suppress-time if present
    if "dampening-max-suppress-time" in payload:
        value = payload.get("dampening-max-suppress-time")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 255:
                    return (
                        False,
                        "dampening-max-suppress-time must be between 1 and 255",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"dampening-max-suppress-time must be numeric, got: {value}",
                )

    # Validate dampening-unreachability-half-life if present
    if "dampening-unreachability-half-life" in payload:
        value = payload.get("dampening-unreachability-half-life")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 45:
                    return (
                        False,
                        "dampening-unreachability-half-life must be between 1 and 45",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"dampening-unreachability-half-life must be numeric, got: {value}",
                )

    # Validate default-local-preference if present
    if "default-local-preference" in payload:
        value = payload.get("default-local-preference")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "default-local-preference must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"default-local-preference must be numeric, got: {value}",
                )

    # Validate scan-time if present
    if "scan-time" in payload:
        value = payload.get("scan-time")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 5 or int_val > 60:
                    return (False, "scan-time must be between 5 and 60")
            except (ValueError, TypeError):
                return (False, f"scan-time must be numeric, got: {value}")

    # Validate distance-external if present
    if "distance-external" in payload:
        value = payload.get("distance-external")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 255:
                    return (
                        False,
                        "distance-external must be between 1 and 255",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"distance-external must be numeric, got: {value}",
                )

    # Validate distance-internal if present
    if "distance-internal" in payload:
        value = payload.get("distance-internal")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 255:
                    return (
                        False,
                        "distance-internal must be between 1 and 255",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"distance-internal must be numeric, got: {value}",
                )

    # Validate distance-local if present
    if "distance-local" in payload:
        value = payload.get("distance-local")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 255:
                    return (False, "distance-local must be between 1 and 255")
            except (ValueError, TypeError):
                return (False, f"distance-local must be numeric, got: {value}")

    # Validate synchronization if present
    if "synchronization" in payload:
        value = payload.get("synchronization")
        if value and value not in VALID_BODY_SYNCHRONIZATION:
            return (
                False,
                f"Invalid synchronization '{value}'. Must be one of: {', '.join(VALID_BODY_SYNCHRONIZATION)}",
            )

    # Validate graceful-restart if present
    if "graceful-restart" in payload:
        value = payload.get("graceful-restart")
        if value and value not in VALID_BODY_GRACEFUL_RESTART:
            return (
                False,
                f"Invalid graceful-restart '{value}'. Must be one of: {', '.join(VALID_BODY_GRACEFUL_RESTART)}",
            )

    # Validate graceful-restart-time if present
    if "graceful-restart-time" in payload:
        value = payload.get("graceful-restart-time")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 3600:
                    return (
                        False,
                        "graceful-restart-time must be between 1 and 3600",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"graceful-restart-time must be numeric, got: {value}",
                )

    # Validate graceful-stalepath-time if present
    if "graceful-stalepath-time" in payload:
        value = payload.get("graceful-stalepath-time")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 3600:
                    return (
                        False,
                        "graceful-stalepath-time must be between 1 and 3600",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"graceful-stalepath-time must be numeric, got: {value}",
                )

    # Validate graceful-update-delay if present
    if "graceful-update-delay" in payload:
        value = payload.get("graceful-update-delay")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 3600:
                    return (
                        False,
                        "graceful-update-delay must be between 1 and 3600",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"graceful-update-delay must be numeric, got: {value}",
                )

    # Validate graceful-end-on-timer if present
    if "graceful-end-on-timer" in payload:
        value = payload.get("graceful-end-on-timer")
        if value and value not in VALID_BODY_GRACEFUL_END_ON_TIMER:
            return (
                False,
                f"Invalid graceful-end-on-timer '{value}'. Must be one of: {', '.join(VALID_BODY_GRACEFUL_END_ON_TIMER)}",
            )

    # Validate additional-path-select if present
    if "additional-path-select" in payload:
        value = payload.get("additional-path-select")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 2 or int_val > 255:
                    return (
                        False,
                        "additional-path-select must be between 2 and 255",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"additional-path-select must be numeric, got: {value}",
                )

    # Validate additional-path-select6 if present
    if "additional-path-select6" in payload:
        value = payload.get("additional-path-select6")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 2 or int_val > 255:
                    return (
                        False,
                        "additional-path-select6 must be between 2 and 255",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"additional-path-select6 must be numeric, got: {value}",
                )

    # Validate additional-path-select-vpnv4 if present
    if "additional-path-select-vpnv4" in payload:
        value = payload.get("additional-path-select-vpnv4")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 2 or int_val > 255:
                    return (
                        False,
                        "additional-path-select-vpnv4 must be between 2 and 255",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"additional-path-select-vpnv4 must be numeric, got: {value}",
                )

    # Validate additional-path-select-vpnv6 if present
    if "additional-path-select-vpnv6" in payload:
        value = payload.get("additional-path-select-vpnv6")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 2 or int_val > 255:
                    return (
                        False,
                        "additional-path-select-vpnv6 must be between 2 and 255",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"additional-path-select-vpnv6 must be numeric, got: {value}",
                )

    # Validate cross-family-conditional-adv if present
    if "cross-family-conditional-adv" in payload:
        value = payload.get("cross-family-conditional-adv")
        if value and value not in VALID_BODY_CROSS_FAMILY_CONDITIONAL_ADV:
            return (
                False,
                f"Invalid cross-family-conditional-adv '{value}'. Must be one of: {', '.join(VALID_BODY_CROSS_FAMILY_CONDITIONAL_ADV)}",
            )

    return (True, None)
