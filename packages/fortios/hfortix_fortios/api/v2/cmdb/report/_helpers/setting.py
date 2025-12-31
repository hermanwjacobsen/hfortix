"""
Validation helpers for report setting endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_PDF_REPORT = ["enable", "disable"]
VALID_BODY_FORTIVIEW = ["enable", "disable"]
VALID_BODY_REPORT_SOURCE = [
    "forward-traffic",
    "sniffer-traffic",
    "local-deny-traffic",
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_setting_get(
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


def validate_setting_put(
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

    # Validate pdf-report if present
    if "pdf-report" in payload:
        value = payload.get("pdf-report")
        if value and value not in VALID_BODY_PDF_REPORT:
            return (
                False,
                f"Invalid pdf-report '{value}'. Must be one of: {', '.join(VALID_BODY_PDF_REPORT)}",
            )

    # Validate fortiview if present
    if "fortiview" in payload:
        value = payload.get("fortiview")
        if value and value not in VALID_BODY_FORTIVIEW:
            return (
                False,
                f"Invalid fortiview '{value}'. Must be one of: {', '.join(VALID_BODY_FORTIVIEW)}",
            )

    # Validate report-source if present
    if "report-source" in payload:
        value = payload.get("report-source")
        if value and value not in VALID_BODY_REPORT_SOURCE:
            return (
                False,
                f"Invalid report-source '{value}'. Must be one of: {', '.join(VALID_BODY_REPORT_SOURCE)}",
            )

    # Validate web-browsing-threshold if present
    if "web-browsing-threshold" in payload:
        value = payload.get("web-browsing-threshold")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 3 or int_val > 15:
                    return (
                        False,
                        "web-browsing-threshold must be between 3 and 15",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"web-browsing-threshold must be numeric, got: {value}",
                )

    # Validate top-n if present
    if "top-n" in payload:
        value = payload.get("top-n")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1000 or int_val > 20000:
                    return (False, "top-n must be between 1000 and 20000")
            except (ValueError, TypeError):
                return (False, f"top-n must be numeric, got: {value}")

    return (True, None)
