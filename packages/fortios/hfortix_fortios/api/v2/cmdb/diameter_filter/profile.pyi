from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList
from hfortix_core.types import MutationResponse

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class ProfilePayload(TypedDict, total=False):
    """
    Type hints for diameter_filter/profile payload fields.
    
    Configure Diameter filter profiles.
    
    **Usage:**
        payload: ProfilePayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # Profile name. | MaxLen: 47
    comment: str  # Comment. | MaxLen: 255
    monitor_all_messages: Literal["disable", "enable"]  # Enable/disable logging for all User Name and Resul | Default: disable
    log_packet: Literal["disable", "enable"]  # Enable/disable packet log for triggered diameter s | Default: disable
    track_requests_answers: Literal["disable", "enable"]  # Enable/disable validation that each answer has a c | Default: enable
    missing_request_action: Literal["allow", "block", "reset", "monitor"]  # Action to be taken for answers without correspondi | Default: block
    protocol_version_invalid: Literal["allow", "block", "reset", "monitor"]  # Action to be taken for invalid protocol version. | Default: block
    message_length_invalid: Literal["allow", "block", "reset", "monitor"]  # Action to be taken for invalid message length. | Default: block
    request_error_flag_set: Literal["allow", "block", "reset", "monitor"]  # Action to be taken for request messages with error | Default: block
    cmd_flags_reserve_set: Literal["allow", "block", "reset", "monitor"]  # Action to be taken for messages with cmd flag rese | Default: block
    command_code_invalid: Literal["allow", "block", "reset", "monitor"]  # Action to be taken for messages with invalid comma | Default: block
    command_code_range: str  # Valid range for command codes (0-16777215).

# Nested TypedDicts for table field children (dict mode)

# Nested classes for table field children (object mode)


# Response TypedDict for GET returns (all fields present in API response)
class ProfileResponse(TypedDict):
    """
    Type hints for diameter_filter/profile API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str  # Profile name. | MaxLen: 47
    comment: str  # Comment. | MaxLen: 255
    monitor_all_messages: Literal["disable", "enable"]  # Enable/disable logging for all User Name and Resul | Default: disable
    log_packet: Literal["disable", "enable"]  # Enable/disable packet log for triggered diameter s | Default: disable
    track_requests_answers: Literal["disable", "enable"]  # Enable/disable validation that each answer has a c | Default: enable
    missing_request_action: Literal["allow", "block", "reset", "monitor"]  # Action to be taken for answers without correspondi | Default: block
    protocol_version_invalid: Literal["allow", "block", "reset", "monitor"]  # Action to be taken for invalid protocol version. | Default: block
    message_length_invalid: Literal["allow", "block", "reset", "monitor"]  # Action to be taken for invalid message length. | Default: block
    request_error_flag_set: Literal["allow", "block", "reset", "monitor"]  # Action to be taken for request messages with error | Default: block
    cmd_flags_reserve_set: Literal["allow", "block", "reset", "monitor"]  # Action to be taken for messages with cmd flag rese | Default: block
    command_code_invalid: Literal["allow", "block", "reset", "monitor"]  # Action to be taken for messages with invalid comma | Default: block
    command_code_range: str  # Valid range for command codes (0-16777215).


@final
class ProfileObject:
    """Typed FortiObject for diameter_filter/profile with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Profile name. | MaxLen: 47
    name: str
    # Comment. | MaxLen: 255
    comment: str
    # Enable/disable logging for all User Name and Result Code AVP | Default: disable
    monitor_all_messages: Literal["disable", "enable"]
    # Enable/disable packet log for triggered diameter settings. | Default: disable
    log_packet: Literal["disable", "enable"]
    # Enable/disable validation that each answer has a correspondi | Default: enable
    track_requests_answers: Literal["disable", "enable"]
    # Action to be taken for answers without corresponding request | Default: block
    missing_request_action: Literal["allow", "block", "reset", "monitor"]
    # Action to be taken for invalid protocol version. | Default: block
    protocol_version_invalid: Literal["allow", "block", "reset", "monitor"]
    # Action to be taken for invalid message length. | Default: block
    message_length_invalid: Literal["allow", "block", "reset", "monitor"]
    # Action to be taken for request messages with error flag set. | Default: block
    request_error_flag_set: Literal["allow", "block", "reset", "monitor"]
    # Action to be taken for messages with cmd flag reserve bits s | Default: block
    cmd_flags_reserve_set: Literal["allow", "block", "reset", "monitor"]
    # Action to be taken for messages with invalid command code. | Default: block
    command_code_invalid: Literal["allow", "block", "reset", "monitor"]
    # Valid range for command codes (0-16777215).
    command_code_range: str
    
    # Common API response fields
    status: str
    http_status: int | None
    vdom: str | None
    
    # Methods from FortiObject
    @property
    def dict(self) -> dict[str, Any]:
        """Convert to dictionary."""
        ...
    @property
    def json(self) -> dict[str, Any]:
        """Convert to dictionary (alias for .dict)."""
        ...
    @property
    def raw(self) -> dict[str, Any]:
        """Get raw API response data."""
        ...
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> ProfilePayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Profile:
    """
    Configure Diameter filter profiles.
    
    Path: diameter_filter/profile
    Category: cmdb
    Primary Key: name
    """
    
    # ================================================================
    # GET OVERLOADS - Always returns FortiObject
    # Pylance matches overloads top-to-bottom, so these must come first!
    # ================================================================
    
    # With mkey as positional arg -> returns FortiObject
    @overload
    def get(
        self,
        name: str,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> ProfileObject: ...
    
    # With mkey as keyword arg -> returns FortiObject
    @overload
    def get(
        self,
        *,
        name: str,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> ProfileObject: ...
    
    # Without mkey -> returns list of FortiObjects
    @overload
    def get(
        self,
        name: None = None,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObjectList[ProfileObject]: ...
    
    # ================================================================
    # (removed - all GET now returns FortiObject)
    # ================================================================
    
    # With mkey as positional arg -> returns single object
    @overload
    def get(
        self,
        name: str,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> ProfileObject: ...
    
    # With mkey as keyword arg -> returns single object
    @overload
    def get(
        self,
        *,
        name: str,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> ProfileObject: ...
    
    # With no mkey -> returns list of objects
    @overload
    def get(
        self,
        *,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObjectList[ProfileObject]: ...
    
    # Dict mode with mkey provided as positional arg (single dict)
    @overload
    def get(
        self,
        name: str,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> ProfileObject: ...
    
    # Dict mode with mkey provided as keyword arg (single dict)
    @overload
    def get(
        self,
        *,
        name: str,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> ProfileObject: ...
    
    # Dict mode - list of dicts (no mkey/name provided) - keyword-only signature
    @overload
    def get(
        self,
        *,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObjectList[ProfileObject]: ...
    
    # Fallback overload for all other cases
    @overload
    def get(
        self,
        name: str | None = ...,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> Union[dict[str, Any], list[dict[str, Any]], FortiObject, list[FortiObject]]: ...
    
    def get(
        self,
        name: str | None = ...,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> ProfileObject | list[ProfileObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: ProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        monitor_all_messages: Literal["disable", "enable"] | None = ...,
        log_packet: Literal["disable", "enable"] | None = ...,
        track_requests_answers: Literal["disable", "enable"] | None = ...,
        missing_request_action: Literal["allow", "block", "reset", "monitor"] | None = ...,
        protocol_version_invalid: Literal["allow", "block", "reset", "monitor"] | None = ...,
        message_length_invalid: Literal["allow", "block", "reset", "monitor"] | None = ...,
        request_error_flag_set: Literal["allow", "block", "reset", "monitor"] | None = ...,
        cmd_flags_reserve_set: Literal["allow", "block", "reset", "monitor"] | None = ...,
        command_code_invalid: Literal["allow", "block", "reset", "monitor"] | None = ...,
        command_code_range: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> ProfileObject: ...
    
    @overload
    def post(
        self,
        payload_dict: ProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        monitor_all_messages: Literal["disable", "enable"] | None = ...,
        log_packet: Literal["disable", "enable"] | None = ...,
        track_requests_answers: Literal["disable", "enable"] | None = ...,
        missing_request_action: Literal["allow", "block", "reset", "monitor"] | None = ...,
        protocol_version_invalid: Literal["allow", "block", "reset", "monitor"] | None = ...,
        message_length_invalid: Literal["allow", "block", "reset", "monitor"] | None = ...,
        request_error_flag_set: Literal["allow", "block", "reset", "monitor"] | None = ...,
        cmd_flags_reserve_set: Literal["allow", "block", "reset", "monitor"] | None = ...,
        command_code_invalid: Literal["allow", "block", "reset", "monitor"] | None = ...,
        command_code_range: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: ProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        monitor_all_messages: Literal["disable", "enable"] | None = ...,
        log_packet: Literal["disable", "enable"] | None = ...,
        track_requests_answers: Literal["disable", "enable"] | None = ...,
        missing_request_action: Literal["allow", "block", "reset", "monitor"] | None = ...,
        protocol_version_invalid: Literal["allow", "block", "reset", "monitor"] | None = ...,
        message_length_invalid: Literal["allow", "block", "reset", "monitor"] | None = ...,
        request_error_flag_set: Literal["allow", "block", "reset", "monitor"] | None = ...,
        cmd_flags_reserve_set: Literal["allow", "block", "reset", "monitor"] | None = ...,
        command_code_invalid: Literal["allow", "block", "reset", "monitor"] | None = ...,
        command_code_range: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def post(
        self,
        payload_dict: ProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        monitor_all_messages: Literal["disable", "enable"] | None = ...,
        log_packet: Literal["disable", "enable"] | None = ...,
        track_requests_answers: Literal["disable", "enable"] | None = ...,
        missing_request_action: Literal["allow", "block", "reset", "monitor"] | None = ...,
        protocol_version_invalid: Literal["allow", "block", "reset", "monitor"] | None = ...,
        message_length_invalid: Literal["allow", "block", "reset", "monitor"] | None = ...,
        request_error_flag_set: Literal["allow", "block", "reset", "monitor"] | None = ...,
        cmd_flags_reserve_set: Literal["allow", "block", "reset", "monitor"] | None = ...,
        command_code_invalid: Literal["allow", "block", "reset", "monitor"] | None = ...,
        command_code_range: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: ProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        monitor_all_messages: Literal["disable", "enable"] | None = ...,
        log_packet: Literal["disable", "enable"] | None = ...,
        track_requests_answers: Literal["disable", "enable"] | None = ...,
        missing_request_action: Literal["allow", "block", "reset", "monitor"] | None = ...,
        protocol_version_invalid: Literal["allow", "block", "reset", "monitor"] | None = ...,
        message_length_invalid: Literal["allow", "block", "reset", "monitor"] | None = ...,
        request_error_flag_set: Literal["allow", "block", "reset", "monitor"] | None = ...,
        cmd_flags_reserve_set: Literal["allow", "block", "reset", "monitor"] | None = ...,
        command_code_invalid: Literal["allow", "block", "reset", "monitor"] | None = ...,
        command_code_range: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> ProfileObject: ...
    
    @overload
    def put(
        self,
        payload_dict: ProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        monitor_all_messages: Literal["disable", "enable"] | None = ...,
        log_packet: Literal["disable", "enable"] | None = ...,
        track_requests_answers: Literal["disable", "enable"] | None = ...,
        missing_request_action: Literal["allow", "block", "reset", "monitor"] | None = ...,
        protocol_version_invalid: Literal["allow", "block", "reset", "monitor"] | None = ...,
        message_length_invalid: Literal["allow", "block", "reset", "monitor"] | None = ...,
        request_error_flag_set: Literal["allow", "block", "reset", "monitor"] | None = ...,
        cmd_flags_reserve_set: Literal["allow", "block", "reset", "monitor"] | None = ...,
        command_code_invalid: Literal["allow", "block", "reset", "monitor"] | None = ...,
        command_code_range: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: ProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        monitor_all_messages: Literal["disable", "enable"] | None = ...,
        log_packet: Literal["disable", "enable"] | None = ...,
        track_requests_answers: Literal["disable", "enable"] | None = ...,
        missing_request_action: Literal["allow", "block", "reset", "monitor"] | None = ...,
        protocol_version_invalid: Literal["allow", "block", "reset", "monitor"] | None = ...,
        message_length_invalid: Literal["allow", "block", "reset", "monitor"] | None = ...,
        request_error_flag_set: Literal["allow", "block", "reset", "monitor"] | None = ...,
        cmd_flags_reserve_set: Literal["allow", "block", "reset", "monitor"] | None = ...,
        command_code_invalid: Literal["allow", "block", "reset", "monitor"] | None = ...,
        command_code_range: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def put(
        self,
        payload_dict: ProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        monitor_all_messages: Literal["disable", "enable"] | None = ...,
        log_packet: Literal["disable", "enable"] | None = ...,
        track_requests_answers: Literal["disable", "enable"] | None = ...,
        missing_request_action: Literal["allow", "block", "reset", "monitor"] | None = ...,
        protocol_version_invalid: Literal["allow", "block", "reset", "monitor"] | None = ...,
        message_length_invalid: Literal["allow", "block", "reset", "monitor"] | None = ...,
        request_error_flag_set: Literal["allow", "block", "reset", "monitor"] | None = ...,
        cmd_flags_reserve_set: Literal["allow", "block", "reset", "monitor"] | None = ...,
        command_code_invalid: Literal["allow", "block", "reset", "monitor"] | None = ...,
        command_code_range: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> ProfileObject: ...
    
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Default overload
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: ProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        monitor_all_messages: Literal["disable", "enable"] | None = ...,
        log_packet: Literal["disable", "enable"] | None = ...,
        track_requests_answers: Literal["disable", "enable"] | None = ...,
        missing_request_action: Literal["allow", "block", "reset", "monitor"] | None = ...,
        protocol_version_invalid: Literal["allow", "block", "reset", "monitor"] | None = ...,
        message_length_invalid: Literal["allow", "block", "reset", "monitor"] | None = ...,
        request_error_flag_set: Literal["allow", "block", "reset", "monitor"] | None = ...,
        cmd_flags_reserve_set: Literal["allow", "block", "reset", "monitor"] | None = ...,
        command_code_invalid: Literal["allow", "block", "reset", "monitor"] | None = ...,
        command_code_range: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Helper methods
    @staticmethod
    def help(field_name: str | None = ...) -> str: ...
    
    @staticmethod
    def fields(detailed: bool = ...) -> Union[list[str], list[dict[str, Any]]]: ...
    
    @staticmethod
    def field_info(field_name: str) -> FortiObject: ...
    
    @staticmethod
    def validate_field(name: str, value: Any) -> bool: ...
    
    @staticmethod
    def required_fields() -> list[str]: ...
    
    @staticmethod
    def defaults() -> FortiObject: ...
    
    @staticmethod
    def schema() -> FortiObject: ...


# ================================================================


__all__ = [
    "Profile",
    "ProfilePayload",
    "ProfileResponse",
    "ProfileObject",
]