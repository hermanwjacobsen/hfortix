from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList
from hfortix_core.types import MutationResponse

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class SwitchProfilePayload(TypedDict, total=False):
    """
    Type hints for switch_controller/switch_profile payload fields.
    
    Configure FortiSwitch switch profile.
    
    **Usage:**
        payload: SwitchProfilePayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # FortiSwitch Profile name. | MaxLen: 35
    login_passwd_override: Literal["enable", "disable"]  # Enable/disable overriding the admin administrator | Default: disable
    login_passwd: str  # Login password of managed FortiSwitch. | MaxLen: 64
    login: Literal["enable", "disable"]  # Enable/disable FortiSwitch serial console. | Default: enable
    revision_backup_on_logout: Literal["enable", "disable"]  # Enable/disable automatic revision backup upon logo | Default: disable
    revision_backup_on_upgrade: Literal["enable", "disable"]  # Enable/disable automatic revision backup upon Fort | Default: disable

# Nested TypedDicts for table field children (dict mode)

# Nested classes for table field children (object mode)


# Response TypedDict for GET returns (all fields present in API response)
class SwitchProfileResponse(TypedDict):
    """
    Type hints for switch_controller/switch_profile API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str  # FortiSwitch Profile name. | MaxLen: 35
    login_passwd_override: Literal["enable", "disable"]  # Enable/disable overriding the admin administrator | Default: disable
    login_passwd: str  # Login password of managed FortiSwitch. | MaxLen: 64
    login: Literal["enable", "disable"]  # Enable/disable FortiSwitch serial console. | Default: enable
    revision_backup_on_logout: Literal["enable", "disable"]  # Enable/disable automatic revision backup upon logo | Default: disable
    revision_backup_on_upgrade: Literal["enable", "disable"]  # Enable/disable automatic revision backup upon Fort | Default: disable


@final
class SwitchProfileObject:
    """Typed FortiObject for switch_controller/switch_profile with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # FortiSwitch Profile name. | MaxLen: 35
    name: str
    # Enable/disable overriding the admin administrator password f | Default: disable
    login_passwd_override: Literal["enable", "disable"]
    # Login password of managed FortiSwitch. | MaxLen: 64
    login_passwd: str
    # Enable/disable FortiSwitch serial console. | Default: enable
    login: Literal["enable", "disable"]
    # Enable/disable automatic revision backup upon logout from Fo | Default: disable
    revision_backup_on_logout: Literal["enable", "disable"]
    # Enable/disable automatic revision backup upon FortiSwitch im | Default: disable
    revision_backup_on_upgrade: Literal["enable", "disable"]
    
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
    def to_dict(self) -> SwitchProfilePayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class SwitchProfile:
    """
    Configure FortiSwitch switch profile.
    
    Path: switch_controller/switch_profile
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
    ) -> SwitchProfileObject: ...
    
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
    ) -> SwitchProfileObject: ...
    
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
    ) -> FortiObjectList[SwitchProfileObject]: ...
    
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
    ) -> SwitchProfileObject: ...
    
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
    ) -> SwitchProfileObject: ...
    
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
    ) -> FortiObjectList[SwitchProfileObject]: ...
    
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
    ) -> SwitchProfileObject: ...
    
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
    ) -> SwitchProfileObject: ...
    
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
    ) -> FortiObjectList[SwitchProfileObject]: ...
    
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
    ) -> SwitchProfileObject | list[SwitchProfileObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: SwitchProfilePayload | None = ...,
        name: str | None = ...,
        login_passwd_override: Literal["enable", "disable"] | None = ...,
        login_passwd: str | None = ...,
        login: Literal["enable", "disable"] | None = ...,
        revision_backup_on_logout: Literal["enable", "disable"] | None = ...,
        revision_backup_on_upgrade: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> SwitchProfileObject: ...
    
    @overload
    def post(
        self,
        payload_dict: SwitchProfilePayload | None = ...,
        name: str | None = ...,
        login_passwd_override: Literal["enable", "disable"] | None = ...,
        login_passwd: str | None = ...,
        login: Literal["enable", "disable"] | None = ...,
        revision_backup_on_logout: Literal["enable", "disable"] | None = ...,
        revision_backup_on_upgrade: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: SwitchProfilePayload | None = ...,
        name: str | None = ...,
        login_passwd_override: Literal["enable", "disable"] | None = ...,
        login_passwd: str | None = ...,
        login: Literal["enable", "disable"] | None = ...,
        revision_backup_on_logout: Literal["enable", "disable"] | None = ...,
        revision_backup_on_upgrade: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def post(
        self,
        payload_dict: SwitchProfilePayload | None = ...,
        name: str | None = ...,
        login_passwd_override: Literal["enable", "disable"] | None = ...,
        login_passwd: str | None = ...,
        login: Literal["enable", "disable"] | None = ...,
        revision_backup_on_logout: Literal["enable", "disable"] | None = ...,
        revision_backup_on_upgrade: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: SwitchProfilePayload | None = ...,
        name: str | None = ...,
        login_passwd_override: Literal["enable", "disable"] | None = ...,
        login_passwd: str | None = ...,
        login: Literal["enable", "disable"] | None = ...,
        revision_backup_on_logout: Literal["enable", "disable"] | None = ...,
        revision_backup_on_upgrade: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> SwitchProfileObject: ...
    
    @overload
    def put(
        self,
        payload_dict: SwitchProfilePayload | None = ...,
        name: str | None = ...,
        login_passwd_override: Literal["enable", "disable"] | None = ...,
        login_passwd: str | None = ...,
        login: Literal["enable", "disable"] | None = ...,
        revision_backup_on_logout: Literal["enable", "disable"] | None = ...,
        revision_backup_on_upgrade: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: SwitchProfilePayload | None = ...,
        name: str | None = ...,
        login_passwd_override: Literal["enable", "disable"] | None = ...,
        login_passwd: str | None = ...,
        login: Literal["enable", "disable"] | None = ...,
        revision_backup_on_logout: Literal["enable", "disable"] | None = ...,
        revision_backup_on_upgrade: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def put(
        self,
        payload_dict: SwitchProfilePayload | None = ...,
        name: str | None = ...,
        login_passwd_override: Literal["enable", "disable"] | None = ...,
        login_passwd: str | None = ...,
        login: Literal["enable", "disable"] | None = ...,
        revision_backup_on_logout: Literal["enable", "disable"] | None = ...,
        revision_backup_on_upgrade: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> SwitchProfileObject: ...
    
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
        payload_dict: SwitchProfilePayload | None = ...,
        name: str | None = ...,
        login_passwd_override: Literal["enable", "disable"] | None = ...,
        login_passwd: str | None = ...,
        login: Literal["enable", "disable"] | None = ...,
        revision_backup_on_logout: Literal["enable", "disable"] | None = ...,
        revision_backup_on_upgrade: Literal["enable", "disable"] | None = ...,
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
    "SwitchProfile",
    "SwitchProfilePayload",
    "SwitchProfileResponse",
    "SwitchProfileObject",
]