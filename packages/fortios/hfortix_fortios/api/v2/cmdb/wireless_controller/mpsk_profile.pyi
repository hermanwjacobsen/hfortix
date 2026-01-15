from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList
from hfortix_core.types import MutationResponse

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class MpskProfilePayload(TypedDict, total=False):
    """
    Type hints for wireless_controller/mpsk_profile payload fields.
    
    Configure MPSK profile.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.user.radius.RadiusEndpoint` (via: mpsk-external-server)

    **Usage:**
        payload: MpskProfilePayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # MPSK profile name. | MaxLen: 35
    mpsk_concurrent_clients: int  # Maximum number of concurrent clients that connect | Default: 0 | Min: 0 | Max: 65535
    mpsk_external_server_auth: Literal["enable", "disable"]  # Enable/Disable MPSK external server authentication | Default: disable
    mpsk_external_server: str  # RADIUS server to be used to authenticate MPSK user | MaxLen: 35
    mpsk_type: Literal["wpa2-personal", "wpa3-sae", "wpa3-sae-transition"]  # Select the security type of keys for this profile. | Default: wpa2-personal
    mpsk_group: list[dict[str, Any]]  # List of multiple PSK groups.

# Nested TypedDicts for table field children (dict mode)

class MpskProfileMpskgroupItem(TypedDict):
    """Type hints for mpsk-group table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # MPSK group name. | MaxLen: 35
    vlan_type: Literal["no-vlan", "fixed-vlan"]  # MPSK group VLAN options. | Default: no-vlan
    vlan_id: int  # Optional VLAN ID. | Default: 0 | Min: 1 | Max: 4094
    mpsk_key: str  # List of multiple PSK entries.


# Nested classes for table field children (object mode)

@final
class MpskProfileMpskgroupObject:
    """Typed object for mpsk-group table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # MPSK group name. | MaxLen: 35
    name: str
    # MPSK group VLAN options. | Default: no-vlan
    vlan_type: Literal["no-vlan", "fixed-vlan"]
    # Optional VLAN ID. | Default: 0 | Min: 1 | Max: 4094
    vlan_id: int
    # List of multiple PSK entries.
    mpsk_key: str
    
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
class MpskProfileResponse(TypedDict):
    """
    Type hints for wireless_controller/mpsk_profile API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str  # MPSK profile name. | MaxLen: 35
    mpsk_concurrent_clients: int  # Maximum number of concurrent clients that connect | Default: 0 | Min: 0 | Max: 65535
    mpsk_external_server_auth: Literal["enable", "disable"]  # Enable/Disable MPSK external server authentication | Default: disable
    mpsk_external_server: str  # RADIUS server to be used to authenticate MPSK user | MaxLen: 35
    mpsk_type: Literal["wpa2-personal", "wpa3-sae", "wpa3-sae-transition"]  # Select the security type of keys for this profile. | Default: wpa2-personal
    mpsk_group: list[MpskProfileMpskgroupItem]  # List of multiple PSK groups.


@final
class MpskProfileObject:
    """Typed FortiObject for wireless_controller/mpsk_profile with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # MPSK profile name. | MaxLen: 35
    name: str
    # Maximum number of concurrent clients that connect using the | Default: 0 | Min: 0 | Max: 65535
    mpsk_concurrent_clients: int
    # Enable/Disable MPSK external server authentication | Default: disable
    mpsk_external_server_auth: Literal["enable", "disable"]
    # RADIUS server to be used to authenticate MPSK users. | MaxLen: 35
    mpsk_external_server: str
    # Select the security type of keys for this profile. | Default: wpa2-personal
    mpsk_type: Literal["wpa2-personal", "wpa3-sae", "wpa3-sae-transition"]
    # List of multiple PSK groups.
    mpsk_group: list[MpskProfileMpskgroupObject]
    
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
    def to_dict(self) -> MpskProfilePayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class MpskProfile:
    """
    Configure MPSK profile.
    
    Path: wireless_controller/mpsk_profile
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
    ) -> MpskProfileObject: ...
    
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
    ) -> MpskProfileObject: ...
    
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
    ) -> FortiObjectList[MpskProfileObject]: ...
    
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
    ) -> MpskProfileObject: ...
    
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
    ) -> MpskProfileObject: ...
    
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
    ) -> FortiObjectList[MpskProfileObject]: ...
    
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
    ) -> MpskProfileObject: ...
    
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
    ) -> MpskProfileObject: ...
    
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
    ) -> FortiObjectList[MpskProfileObject]: ...
    
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
    ) -> MpskProfileObject | list[MpskProfileObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: MpskProfilePayload | None = ...,
        name: str | None = ...,
        mpsk_concurrent_clients: int | None = ...,
        mpsk_external_server_auth: Literal["enable", "disable"] | None = ...,
        mpsk_external_server: str | None = ...,
        mpsk_type: Literal["wpa2-personal", "wpa3-sae", "wpa3-sae-transition"] | None = ...,
        mpsk_group: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MpskProfileObject: ...
    
    @overload
    def post(
        self,
        payload_dict: MpskProfilePayload | None = ...,
        name: str | None = ...,
        mpsk_concurrent_clients: int | None = ...,
        mpsk_external_server_auth: Literal["enable", "disable"] | None = ...,
        mpsk_external_server: str | None = ...,
        mpsk_type: Literal["wpa2-personal", "wpa3-sae", "wpa3-sae-transition"] | None = ...,
        mpsk_group: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: MpskProfilePayload | None = ...,
        name: str | None = ...,
        mpsk_concurrent_clients: int | None = ...,
        mpsk_external_server_auth: Literal["enable", "disable"] | None = ...,
        mpsk_external_server: str | None = ...,
        mpsk_type: Literal["wpa2-personal", "wpa3-sae", "wpa3-sae-transition"] | None = ...,
        mpsk_group: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def post(
        self,
        payload_dict: MpskProfilePayload | None = ...,
        name: str | None = ...,
        mpsk_concurrent_clients: int | None = ...,
        mpsk_external_server_auth: Literal["enable", "disable"] | None = ...,
        mpsk_external_server: str | None = ...,
        mpsk_type: Literal["wpa2-personal", "wpa3-sae", "wpa3-sae-transition"] | None = ...,
        mpsk_group: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: MpskProfilePayload | None = ...,
        name: str | None = ...,
        mpsk_concurrent_clients: int | None = ...,
        mpsk_external_server_auth: Literal["enable", "disable"] | None = ...,
        mpsk_external_server: str | None = ...,
        mpsk_type: Literal["wpa2-personal", "wpa3-sae", "wpa3-sae-transition"] | None = ...,
        mpsk_group: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MpskProfileObject: ...
    
    @overload
    def put(
        self,
        payload_dict: MpskProfilePayload | None = ...,
        name: str | None = ...,
        mpsk_concurrent_clients: int | None = ...,
        mpsk_external_server_auth: Literal["enable", "disable"] | None = ...,
        mpsk_external_server: str | None = ...,
        mpsk_type: Literal["wpa2-personal", "wpa3-sae", "wpa3-sae-transition"] | None = ...,
        mpsk_group: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: MpskProfilePayload | None = ...,
        name: str | None = ...,
        mpsk_concurrent_clients: int | None = ...,
        mpsk_external_server_auth: Literal["enable", "disable"] | None = ...,
        mpsk_external_server: str | None = ...,
        mpsk_type: Literal["wpa2-personal", "wpa3-sae", "wpa3-sae-transition"] | None = ...,
        mpsk_group: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def put(
        self,
        payload_dict: MpskProfilePayload | None = ...,
        name: str | None = ...,
        mpsk_concurrent_clients: int | None = ...,
        mpsk_external_server_auth: Literal["enable", "disable"] | None = ...,
        mpsk_external_server: str | None = ...,
        mpsk_type: Literal["wpa2-personal", "wpa3-sae", "wpa3-sae-transition"] | None = ...,
        mpsk_group: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> MpskProfileObject: ...
    
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
        payload_dict: MpskProfilePayload | None = ...,
        name: str | None = ...,
        mpsk_concurrent_clients: int | None = ...,
        mpsk_external_server_auth: Literal["enable", "disable"] | None = ...,
        mpsk_external_server: str | None = ...,
        mpsk_type: Literal["wpa2-personal", "wpa3-sae", "wpa3-sae-transition"] | None = ...,
        mpsk_group: str | list[str] | list[dict[str, Any]] | None = ...,
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
    "MpskProfile",
    "MpskProfilePayload",
    "MpskProfileResponse",
    "MpskProfileObject",
]