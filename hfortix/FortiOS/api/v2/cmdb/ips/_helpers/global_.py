"""
Validation helpers for ips global_ endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_FAIL_OPEN = ["enable", "disable"]
VALID_BODY_DATABASE = ["regular", "extended"]
VALID_BODY_TRAFFIC_SUBMIT = ["enable", "disable"]
VALID_BODY_ANOMALY_MODE = ["periodical", "continuous"]
VALID_BODY_SESSION_LIMIT_MODE = ["accurate", "heuristic"]
VALID_BODY_SYNC_SESSION_TTL = ["enable", "disable"]
VALID_BODY_NP_ACCEL_MODE = ["none", "basic"]
VALID_BODY_IPS_RESERVE_CPU = ["disable", "enable"]
VALID_BODY_CP_ACCEL_MODE = ["none", "basic", "advanced"]
VALID_BODY_EXCLUDE_SIGNATURES = ["none", "ot"]
VALID_BODY_MACHINE_LEARNING_DETECTION = ["enable", "disable"]
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

    # Validate fail-open if present
    if "fail-open" in payload:
        value = payload.get("fail-open")
        if value and value not in VALID_BODY_FAIL_OPEN:
            return (
                False,
                f"Invalid fail-open '{value}'. Must be one of: {', '.join(VALID_BODY_FAIL_OPEN)}",
            )

    # Validate database if present
    if "database" in payload:
        value = payload.get("database")
        if value and value not in VALID_BODY_DATABASE:
            return (
                False,
                f"Invalid database '{value}'. Must be one of: {', '.join(VALID_BODY_DATABASE)}",
            )

    # Validate traffic-submit if present
    if "traffic-submit" in payload:
        value = payload.get("traffic-submit")
        if value and value not in VALID_BODY_TRAFFIC_SUBMIT:
            return (
                False,
                f"Invalid traffic-submit '{value}'. Must be one of: {', '.join(VALID_BODY_TRAFFIC_SUBMIT)}",
            )

    # Validate anomaly-mode if present
    if "anomaly-mode" in payload:
        value = payload.get("anomaly-mode")
        if value and value not in VALID_BODY_ANOMALY_MODE:
            return (
                False,
                f"Invalid anomaly-mode '{value}'. Must be one of: {', '.join(VALID_BODY_ANOMALY_MODE)}",
            )

    # Validate session-limit-mode if present
    if "session-limit-mode" in payload:
        value = payload.get("session-limit-mode")
        if value and value not in VALID_BODY_SESSION_LIMIT_MODE:
            return (
                False,
                f"Invalid session-limit-mode '{value}'. Must be one of: {', '.join(VALID_BODY_SESSION_LIMIT_MODE)}",
            )

    # Validate socket-size if present
    if "socket-size" in payload:
        value = payload.get("socket-size")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 128:
                    return (False, "socket-size must be between 0 and 128")
            except (ValueError, TypeError):
                return (False, f"socket-size must be numeric, got: {value}")

    # Validate engine-count if present
    if "engine-count" in payload:
        value = payload.get("engine-count")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 255:
                    return (False, "engine-count must be between 0 and 255")
            except (ValueError, TypeError):
                return (False, f"engine-count must be numeric, got: {value}")

    # Validate sync-session-ttl if present
    if "sync-session-ttl" in payload:
        value = payload.get("sync-session-ttl")
        if value and value not in VALID_BODY_SYNC_SESSION_TTL:
            return (
                False,
                f"Invalid sync-session-ttl '{value}'. Must be one of: {', '.join(VALID_BODY_SYNC_SESSION_TTL)}",
            )

    # Validate np-accel-mode if present
    if "np-accel-mode" in payload:
        value = payload.get("np-accel-mode")
        if value and value not in VALID_BODY_NP_ACCEL_MODE:
            return (
                False,
                f"Invalid np-accel-mode '{value}'. Must be one of: {', '.join(VALID_BODY_NP_ACCEL_MODE)}",
            )

    # Validate ips-reserve-cpu if present
    if "ips-reserve-cpu" in payload:
        value = payload.get("ips-reserve-cpu")
        if value and value not in VALID_BODY_IPS_RESERVE_CPU:
            return (
                False,
                f"Invalid ips-reserve-cpu '{value}'. Must be one of: {', '.join(VALID_BODY_IPS_RESERVE_CPU)}",
            )

    # Validate cp-accel-mode if present
    if "cp-accel-mode" in payload:
        value = payload.get("cp-accel-mode")
        if value and value not in VALID_BODY_CP_ACCEL_MODE:
            return (
                False,
                f"Invalid cp-accel-mode '{value}'. Must be one of: {', '.join(VALID_BODY_CP_ACCEL_MODE)}",
            )

    # Validate deep-app-insp-timeout if present
    if "deep-app-insp-timeout" in payload:
        value = payload.get("deep-app-insp-timeout")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 2147483647:
                    return (
                        False,
                        "deep-app-insp-timeout must be between 0 and 2147483647",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"deep-app-insp-timeout must be numeric, got: {value}",
                )

    # Validate deep-app-insp-db-limit if present
    if "deep-app-insp-db-limit" in payload:
        value = payload.get("deep-app-insp-db-limit")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 2147483647:
                    return (
                        False,
                        "deep-app-insp-db-limit must be between 0 and 2147483647",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"deep-app-insp-db-limit must be numeric, got: {value}",
                )

    # Validate exclude-signatures if present
    if "exclude-signatures" in payload:
        value = payload.get("exclude-signatures")
        if value and value not in VALID_BODY_EXCLUDE_SIGNATURES:
            return (
                False,
                f"Invalid exclude-signatures '{value}'. Must be one of: {', '.join(VALID_BODY_EXCLUDE_SIGNATURES)}",
            )

    # Validate packet-log-queue-depth if present
    if "packet-log-queue-depth" in payload:
        value = payload.get("packet-log-queue-depth")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 128 or int_val > 4096:
                    return (
                        False,
                        "packet-log-queue-depth must be between 128 and 4096",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"packet-log-queue-depth must be numeric, got: {value}",
                )

    # Validate ngfw-max-scan-range if present
    if "ngfw-max-scan-range" in payload:
        value = payload.get("ngfw-max-scan-range")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "ngfw-max-scan-range must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"ngfw-max-scan-range must be numeric, got: {value}",
                )

    # Validate av-mem-limit if present
    if "av-mem-limit" in payload:
        value = payload.get("av-mem-limit")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 10 or int_val > 50:
                    return (False, "av-mem-limit must be between 10 and 50")
            except (ValueError, TypeError):
                return (False, f"av-mem-limit must be numeric, got: {value}")

    # Validate machine-learning-detection if present
    if "machine-learning-detection" in payload:
        value = payload.get("machine-learning-detection")
        if value and value not in VALID_BODY_MACHINE_LEARNING_DETECTION:
            return (
                False,
                f"Invalid machine-learning-detection '{value}'. Must be one of: {', '.join(VALID_BODY_MACHINE_LEARNING_DETECTION)}",
            )

    return (True, None)
