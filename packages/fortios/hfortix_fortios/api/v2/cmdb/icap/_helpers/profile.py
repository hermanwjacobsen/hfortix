"""
Validation helpers for icap profile endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_REQUEST = ["disable", "enable"]
VALID_BODY_RESPONSE = ["disable", "enable"]
VALID_BODY_FILE_TRANSFER = ["ssh", "ftp"]
VALID_BODY_STREAMING_CONTENT_BYPASS = ["disable", "enable"]
VALID_BODY_OCR_ONLY = ["disable", "enable"]
VALID_BODY_204_RESPONSE = ["disable", "enable"]
VALID_BODY_PREVIEW = ["disable", "enable"]
VALID_BODY_REQUEST_FAILURE = ["error", "bypass"]
VALID_BODY_RESPONSE_FAILURE = ["error", "bypass"]
VALID_BODY_FILE_TRANSFER_FAILURE = ["error", "bypass"]
VALID_BODY_METHODS = [
    "delete",
    "get",
    "head",
    "options",
    "post",
    "put",
    "trace",
    "connect",
    "other",
]
VALID_BODY_RESPONSE_REQ_HDR = ["disable", "enable"]
VALID_BODY_RESPMOD_DEFAULT_ACTION = ["forward", "bypass"]
VALID_BODY_ICAP_BLOCK_LOG = ["disable", "enable"]
VALID_BODY_CHUNK_ENCAP = ["disable", "enable"]
VALID_BODY_EXTENSION_FEATURE = ["scan-progress"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_profile_get(
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


def validate_profile_post(payload: dict[str, Any]) -> tuple[bool, str | None]:
    """
    Validate POST request payload for creating profile.

    Args:
        payload: The payload to validate

    Returns:
        Tuple of (is_valid, error_message)
    """
    # Validate replacemsg-group if present
    if "replacemsg-group" in payload:
        value = payload.get("replacemsg-group")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "replacemsg-group cannot exceed 35 characters")

    # Validate name if present
    if "name" in payload:
        value = payload.get("name")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "name cannot exceed 47 characters")

    # Validate comment if present
    if "comment" in payload:
        value = payload.get("comment")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "comment cannot exceed 255 characters")

    # Validate request if present
    if "request" in payload:
        value = payload.get("request")
        if value and value not in VALID_BODY_REQUEST:
            return (
                False,
                f"Invalid request '{value}'. Must be one of: {', '.join(VALID_BODY_REQUEST)}",
            )

    # Validate response if present
    if "response" in payload:
        value = payload.get("response")
        if value and value not in VALID_BODY_RESPONSE:
            return (
                False,
                f"Invalid response '{value}'. Must be one of: {', '.join(VALID_BODY_RESPONSE)}",
            )

    # Validate file-transfer if present
    if "file-transfer" in payload:
        value = payload.get("file-transfer")
        if value and value not in VALID_BODY_FILE_TRANSFER:
            return (
                False,
                f"Invalid file-transfer '{value}'. Must be one of: {', '.join(VALID_BODY_FILE_TRANSFER)}",
            )

    # Validate streaming-content-bypass if present
    if "streaming-content-bypass" in payload:
        value = payload.get("streaming-content-bypass")
        if value and value not in VALID_BODY_STREAMING_CONTENT_BYPASS:
            return (
                False,
                f"Invalid streaming-content-bypass '{value}'. Must be one of: {', '.join(VALID_BODY_STREAMING_CONTENT_BYPASS)}",
            )

    # Validate ocr-only if present
    if "ocr-only" in payload:
        value = payload.get("ocr-only")
        if value and value not in VALID_BODY_OCR_ONLY:
            return (
                False,
                f"Invalid ocr-only '{value}'. Must be one of: {', '.join(VALID_BODY_OCR_ONLY)}",
            )

    # Validate 204-size-limit if present
    if "204-size-limit" in payload:
        value = payload.get("204-size-limit")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 10:
                    return (False, "204-size-limit must be between 1 and 10")
            except (ValueError, TypeError):
                return (False, f"204-size-limit must be numeric, got: {value}")

    # Validate 204-response if present
    if "204-response" in payload:
        value = payload.get("204-response")
        if value and value not in VALID_BODY_204_RESPONSE:
            return (
                False,
                f"Invalid 204-response '{value}'. Must be one of: {', '.join(VALID_BODY_204_RESPONSE)}",
            )

    # Validate preview if present
    if "preview" in payload:
        value = payload.get("preview")
        if value and value not in VALID_BODY_PREVIEW:
            return (
                False,
                f"Invalid preview '{value}'. Must be one of: {', '.join(VALID_BODY_PREVIEW)}",
            )

    # Validate preview-data-length if present
    if "preview-data-length" in payload:
        value = payload.get("preview-data-length")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4096:
                    return (
                        False,
                        "preview-data-length must be between 0 and 4096",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"preview-data-length must be numeric, got: {value}",
                )

    # Validate request-server if present
    if "request-server" in payload:
        value = payload.get("request-server")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "request-server cannot exceed 63 characters")

    # Validate response-server if present
    if "response-server" in payload:
        value = payload.get("response-server")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "response-server cannot exceed 63 characters")

    # Validate file-transfer-server if present
    if "file-transfer-server" in payload:
        value = payload.get("file-transfer-server")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "file-transfer-server cannot exceed 63 characters")

    # Validate request-failure if present
    if "request-failure" in payload:
        value = payload.get("request-failure")
        if value and value not in VALID_BODY_REQUEST_FAILURE:
            return (
                False,
                f"Invalid request-failure '{value}'. Must be one of: {', '.join(VALID_BODY_REQUEST_FAILURE)}",
            )

    # Validate response-failure if present
    if "response-failure" in payload:
        value = payload.get("response-failure")
        if value and value not in VALID_BODY_RESPONSE_FAILURE:
            return (
                False,
                f"Invalid response-failure '{value}'. Must be one of: {', '.join(VALID_BODY_RESPONSE_FAILURE)}",
            )

    # Validate file-transfer-failure if present
    if "file-transfer-failure" in payload:
        value = payload.get("file-transfer-failure")
        if value and value not in VALID_BODY_FILE_TRANSFER_FAILURE:
            return (
                False,
                f"Invalid file-transfer-failure '{value}'. Must be one of: {', '.join(VALID_BODY_FILE_TRANSFER_FAILURE)}",
            )

    # Validate request-path if present
    if "request-path" in payload:
        value = payload.get("request-path")
        if value and isinstance(value, str) and len(value) > 127:
            return (False, "request-path cannot exceed 127 characters")

    # Validate response-path if present
    if "response-path" in payload:
        value = payload.get("response-path")
        if value and isinstance(value, str) and len(value) > 127:
            return (False, "response-path cannot exceed 127 characters")

    # Validate file-transfer-path if present
    if "file-transfer-path" in payload:
        value = payload.get("file-transfer-path")
        if value and isinstance(value, str) and len(value) > 127:
            return (False, "file-transfer-path cannot exceed 127 characters")

    # Validate methods if present
    if "methods" in payload:
        value = payload.get("methods")
        if value and value not in VALID_BODY_METHODS:
            return (
                False,
                f"Invalid methods '{value}'. Must be one of: {', '.join(VALID_BODY_METHODS)}",
            )

    # Validate response-req-hdr if present
    if "response-req-hdr" in payload:
        value = payload.get("response-req-hdr")
        if value and value not in VALID_BODY_RESPONSE_REQ_HDR:
            return (
                False,
                f"Invalid response-req-hdr '{value}'. Must be one of: {', '.join(VALID_BODY_RESPONSE_REQ_HDR)}",
            )

    # Validate respmod-default-action if present
    if "respmod-default-action" in payload:
        value = payload.get("respmod-default-action")
        if value and value not in VALID_BODY_RESPMOD_DEFAULT_ACTION:
            return (
                False,
                f"Invalid respmod-default-action '{value}'. Must be one of: {', '.join(VALID_BODY_RESPMOD_DEFAULT_ACTION)}",
            )

    # Validate icap-block-log if present
    if "icap-block-log" in payload:
        value = payload.get("icap-block-log")
        if value and value not in VALID_BODY_ICAP_BLOCK_LOG:
            return (
                False,
                f"Invalid icap-block-log '{value}'. Must be one of: {', '.join(VALID_BODY_ICAP_BLOCK_LOG)}",
            )

    # Validate chunk-encap if present
    if "chunk-encap" in payload:
        value = payload.get("chunk-encap")
        if value and value not in VALID_BODY_CHUNK_ENCAP:
            return (
                False,
                f"Invalid chunk-encap '{value}'. Must be one of: {', '.join(VALID_BODY_CHUNK_ENCAP)}",
            )

    # Validate extension-feature if present
    if "extension-feature" in payload:
        value = payload.get("extension-feature")
        if value and value not in VALID_BODY_EXTENSION_FEATURE:
            return (
                False,
                f"Invalid extension-feature '{value}'. Must be one of: {', '.join(VALID_BODY_EXTENSION_FEATURE)}",
            )

    # Validate scan-progress-interval if present
    if "scan-progress-interval" in payload:
        value = payload.get("scan-progress-interval")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 5 or int_val > 30:
                    return (
                        False,
                        "scan-progress-interval must be between 5 and 30",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"scan-progress-interval must be numeric, got: {value}",
                )

    # Validate timeout if present
    if "timeout" in payload:
        value = payload.get("timeout")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 30 or int_val > 3600:
                    return (False, "timeout must be between 30 and 3600")
            except (ValueError, TypeError):
                return (False, f"timeout must be numeric, got: {value}")

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_profile_put(
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

    # Validate replacemsg-group if present
    if "replacemsg-group" in payload:
        value = payload.get("replacemsg-group")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "replacemsg-group cannot exceed 35 characters")

    # Validate name if present
    if "name" in payload:
        value = payload.get("name")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "name cannot exceed 47 characters")

    # Validate comment if present
    if "comment" in payload:
        value = payload.get("comment")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "comment cannot exceed 255 characters")

    # Validate request if present
    if "request" in payload:
        value = payload.get("request")
        if value and value not in VALID_BODY_REQUEST:
            return (
                False,
                f"Invalid request '{value}'. Must be one of: {', '.join(VALID_BODY_REQUEST)}",
            )

    # Validate response if present
    if "response" in payload:
        value = payload.get("response")
        if value and value not in VALID_BODY_RESPONSE:
            return (
                False,
                f"Invalid response '{value}'. Must be one of: {', '.join(VALID_BODY_RESPONSE)}",
            )

    # Validate file-transfer if present
    if "file-transfer" in payload:
        value = payload.get("file-transfer")
        if value and value not in VALID_BODY_FILE_TRANSFER:
            return (
                False,
                f"Invalid file-transfer '{value}'. Must be one of: {', '.join(VALID_BODY_FILE_TRANSFER)}",
            )

    # Validate streaming-content-bypass if present
    if "streaming-content-bypass" in payload:
        value = payload.get("streaming-content-bypass")
        if value and value not in VALID_BODY_STREAMING_CONTENT_BYPASS:
            return (
                False,
                f"Invalid streaming-content-bypass '{value}'. Must be one of: {', '.join(VALID_BODY_STREAMING_CONTENT_BYPASS)}",
            )

    # Validate ocr-only if present
    if "ocr-only" in payload:
        value = payload.get("ocr-only")
        if value and value not in VALID_BODY_OCR_ONLY:
            return (
                False,
                f"Invalid ocr-only '{value}'. Must be one of: {', '.join(VALID_BODY_OCR_ONLY)}",
            )

    # Validate 204-size-limit if present
    if "204-size-limit" in payload:
        value = payload.get("204-size-limit")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 10:
                    return (False, "204-size-limit must be between 1 and 10")
            except (ValueError, TypeError):
                return (False, f"204-size-limit must be numeric, got: {value}")

    # Validate 204-response if present
    if "204-response" in payload:
        value = payload.get("204-response")
        if value and value not in VALID_BODY_204_RESPONSE:
            return (
                False,
                f"Invalid 204-response '{value}'. Must be one of: {', '.join(VALID_BODY_204_RESPONSE)}",
            )

    # Validate preview if present
    if "preview" in payload:
        value = payload.get("preview")
        if value and value not in VALID_BODY_PREVIEW:
            return (
                False,
                f"Invalid preview '{value}'. Must be one of: {', '.join(VALID_BODY_PREVIEW)}",
            )

    # Validate preview-data-length if present
    if "preview-data-length" in payload:
        value = payload.get("preview-data-length")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4096:
                    return (
                        False,
                        "preview-data-length must be between 0 and 4096",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"preview-data-length must be numeric, got: {value}",
                )

    # Validate request-server if present
    if "request-server" in payload:
        value = payload.get("request-server")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "request-server cannot exceed 63 characters")

    # Validate response-server if present
    if "response-server" in payload:
        value = payload.get("response-server")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "response-server cannot exceed 63 characters")

    # Validate file-transfer-server if present
    if "file-transfer-server" in payload:
        value = payload.get("file-transfer-server")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "file-transfer-server cannot exceed 63 characters")

    # Validate request-failure if present
    if "request-failure" in payload:
        value = payload.get("request-failure")
        if value and value not in VALID_BODY_REQUEST_FAILURE:
            return (
                False,
                f"Invalid request-failure '{value}'. Must be one of: {', '.join(VALID_BODY_REQUEST_FAILURE)}",
            )

    # Validate response-failure if present
    if "response-failure" in payload:
        value = payload.get("response-failure")
        if value and value not in VALID_BODY_RESPONSE_FAILURE:
            return (
                False,
                f"Invalid response-failure '{value}'. Must be one of: {', '.join(VALID_BODY_RESPONSE_FAILURE)}",
            )

    # Validate file-transfer-failure if present
    if "file-transfer-failure" in payload:
        value = payload.get("file-transfer-failure")
        if value and value not in VALID_BODY_FILE_TRANSFER_FAILURE:
            return (
                False,
                f"Invalid file-transfer-failure '{value}'. Must be one of: {', '.join(VALID_BODY_FILE_TRANSFER_FAILURE)}",
            )

    # Validate request-path if present
    if "request-path" in payload:
        value = payload.get("request-path")
        if value and isinstance(value, str) and len(value) > 127:
            return (False, "request-path cannot exceed 127 characters")

    # Validate response-path if present
    if "response-path" in payload:
        value = payload.get("response-path")
        if value and isinstance(value, str) and len(value) > 127:
            return (False, "response-path cannot exceed 127 characters")

    # Validate file-transfer-path if present
    if "file-transfer-path" in payload:
        value = payload.get("file-transfer-path")
        if value and isinstance(value, str) and len(value) > 127:
            return (False, "file-transfer-path cannot exceed 127 characters")

    # Validate methods if present
    if "methods" in payload:
        value = payload.get("methods")
        if value and value not in VALID_BODY_METHODS:
            return (
                False,
                f"Invalid methods '{value}'. Must be one of: {', '.join(VALID_BODY_METHODS)}",
            )

    # Validate response-req-hdr if present
    if "response-req-hdr" in payload:
        value = payload.get("response-req-hdr")
        if value and value not in VALID_BODY_RESPONSE_REQ_HDR:
            return (
                False,
                f"Invalid response-req-hdr '{value}'. Must be one of: {', '.join(VALID_BODY_RESPONSE_REQ_HDR)}",
            )

    # Validate respmod-default-action if present
    if "respmod-default-action" in payload:
        value = payload.get("respmod-default-action")
        if value and value not in VALID_BODY_RESPMOD_DEFAULT_ACTION:
            return (
                False,
                f"Invalid respmod-default-action '{value}'. Must be one of: {', '.join(VALID_BODY_RESPMOD_DEFAULT_ACTION)}",
            )

    # Validate icap-block-log if present
    if "icap-block-log" in payload:
        value = payload.get("icap-block-log")
        if value and value not in VALID_BODY_ICAP_BLOCK_LOG:
            return (
                False,
                f"Invalid icap-block-log '{value}'. Must be one of: {', '.join(VALID_BODY_ICAP_BLOCK_LOG)}",
            )

    # Validate chunk-encap if present
    if "chunk-encap" in payload:
        value = payload.get("chunk-encap")
        if value and value not in VALID_BODY_CHUNK_ENCAP:
            return (
                False,
                f"Invalid chunk-encap '{value}'. Must be one of: {', '.join(VALID_BODY_CHUNK_ENCAP)}",
            )

    # Validate extension-feature if present
    if "extension-feature" in payload:
        value = payload.get("extension-feature")
        if value and value not in VALID_BODY_EXTENSION_FEATURE:
            return (
                False,
                f"Invalid extension-feature '{value}'. Must be one of: {', '.join(VALID_BODY_EXTENSION_FEATURE)}",
            )

    # Validate scan-progress-interval if present
    if "scan-progress-interval" in payload:
        value = payload.get("scan-progress-interval")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 5 or int_val > 30:
                    return (
                        False,
                        "scan-progress-interval must be between 5 and 30",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"scan-progress-interval must be numeric, got: {value}",
                )

    # Validate timeout if present
    if "timeout" in payload:
        value = payload.get("timeout")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 30 or int_val > 3600:
                    return (False, "timeout must be between 30 and 3600")
            except (ValueError, TypeError):
                return (False, f"timeout must be numeric, got: {value}")

    return (True, None)


# ============================================================================
# DELETE Validation
# ============================================================================


def validate_profile_delete(
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
