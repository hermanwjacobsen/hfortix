from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList
from hfortix_core.types import MutationResponse

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class AlarmPayload(TypedDict, total=False):
    """
    Type hints for system/alarm payload fields.
    
    Configure alarm.
    
    **Usage:**
        payload: AlarmPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    status: Literal["enable", "disable"]  # Enable/disable alarm. | Default: disable
    audible: Literal["enable", "disable"]  # Enable/disable audible alarm. | Default: disable
    groups: list[dict[str, Any]]  # Alarm groups.

# Nested TypedDicts for table field children (dict mode)

class AlarmGroupsItem(TypedDict):
    """Type hints for groups table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    id: int  # Group ID. | Default: 0 | Min: 0 | Max: 4294967295
    period: int  # Time period in seconds (0 = from start up). | Default: 0 | Min: 0 | Max: 4294967295
    admin_auth_failure_threshold: int  # Admin authentication failure threshold. | Default: 0 | Min: 0 | Max: 1024
    admin_auth_lockout_threshold: int  # Admin authentication lockout threshold. | Default: 0 | Min: 0 | Max: 1024
    user_auth_failure_threshold: int  # User authentication failure threshold. | Default: 0 | Min: 0 | Max: 1024
    user_auth_lockout_threshold: int  # User authentication lockout threshold. | Default: 0 | Min: 0 | Max: 1024
    replay_attempt_threshold: int  # Replay attempt threshold. | Default: 0 | Min: 0 | Max: 1024
    self_test_failure_threshold: int  # Self-test failure threshold. | Default: 0 | Min: 0 | Max: 1
    log_full_warning_threshold: int  # Log full warning threshold. | Default: 0 | Min: 0 | Max: 1024
    encryption_failure_threshold: int  # Encryption failure threshold. | Default: 0 | Min: 0 | Max: 1024
    decryption_failure_threshold: int  # Decryption failure threshold. | Default: 0 | Min: 0 | Max: 1024
    fw_policy_violations: str  # Firewall policy violations.
    fw_policy_id: int  # Firewall policy ID. | Default: 0 | Min: 0 | Max: 4294967295
    fw_policy_id_threshold: int  # Firewall policy ID threshold. | Default: 0 | Min: 0 | Max: 1024


# Nested classes for table field children (object mode)

@final
class AlarmGroupsObject:
    """Typed object for groups table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Group ID. | Default: 0 | Min: 0 | Max: 4294967295
    id: int
    # Time period in seconds (0 = from start up). | Default: 0 | Min: 0 | Max: 4294967295
    period: int
    # Admin authentication failure threshold. | Default: 0 | Min: 0 | Max: 1024
    admin_auth_failure_threshold: int
    # Admin authentication lockout threshold. | Default: 0 | Min: 0 | Max: 1024
    admin_auth_lockout_threshold: int
    # User authentication failure threshold. | Default: 0 | Min: 0 | Max: 1024
    user_auth_failure_threshold: int
    # User authentication lockout threshold. | Default: 0 | Min: 0 | Max: 1024
    user_auth_lockout_threshold: int
    # Replay attempt threshold. | Default: 0 | Min: 0 | Max: 1024
    replay_attempt_threshold: int
    # Self-test failure threshold. | Default: 0 | Min: 0 | Max: 1
    self_test_failure_threshold: int
    # Log full warning threshold. | Default: 0 | Min: 0 | Max: 1024
    log_full_warning_threshold: int
    # Encryption failure threshold. | Default: 0 | Min: 0 | Max: 1024
    encryption_failure_threshold: int
    # Decryption failure threshold. | Default: 0 | Min: 0 | Max: 1024
    decryption_failure_threshold: int
    # Firewall policy violations.
    fw_policy_violations: str
    # Firewall policy ID. | Default: 0 | Min: 0 | Max: 4294967295
    fw_policy_id: int
    # Firewall policy ID threshold. | Default: 0 | Min: 0 | Max: 1024
    fw_policy_id_threshold: int
    
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
    def to_dict(self) -> FortiObject: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...



# Response TypedDict for GET returns (all fields present in API response)
class AlarmResponse(TypedDict):
    """
    Type hints for system/alarm API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    status: Literal["enable", "disable"]  # Enable/disable alarm. | Default: disable
    audible: Literal["enable", "disable"]  # Enable/disable audible alarm. | Default: disable
    groups: list[AlarmGroupsItem]  # Alarm groups.


@final
class AlarmObject:
    """Typed FortiObject for system/alarm with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Enable/disable alarm. | Default: disable
    status: Literal["enable", "disable"]
    # Enable/disable audible alarm. | Default: disable
    audible: Literal["enable", "disable"]
    # Alarm groups.
    groups: list[AlarmGroupsObject]
    
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
    def to_dict(self) -> AlarmPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Alarm:
    """
    Configure alarm.
    
    Path: system/alarm
    Category: cmdb
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
    ) -> AlarmObject: ...
    
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
    ) -> AlarmObject: ...
    
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
    ) -> AlarmObject: ...
    
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
    ) -> AlarmObject: ...
    
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
    ) -> AlarmObject: ...
    
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
    ) -> AlarmObject: ...
    
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
    ) -> AlarmObject: ...
    
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
    ) -> AlarmObject: ...
    
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
    ) -> AlarmObject: ...
    
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
    ) -> dict[str, Any] | FortiObject: ...
    
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
    ) -> AlarmObject | dict[str, Any]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: AlarmPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        audible: Literal["enable", "disable"] | None = ...,
        groups: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> AlarmObject: ...
    
    @overload
    def put(
        self,
        payload_dict: AlarmPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        audible: Literal["enable", "disable"] | None = ...,
        groups: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: AlarmPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        audible: Literal["enable", "disable"] | None = ...,
        groups: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def put(
        self,
        payload_dict: AlarmPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        audible: Literal["enable", "disable"] | None = ...,
        groups: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: AlarmPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        audible: Literal["enable", "disable"] | None = ...,
        groups: str | list[str] | list[dict[str, Any]] | None = ...,
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
    "Alarm",
    "AlarmPayload",
    "AlarmResponse",
    "AlarmObject",
]