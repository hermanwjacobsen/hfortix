from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class BonjourProfilePayload(TypedDict, total=False):
    """
    Type hints for wireless_controller/bonjour_profile payload fields.
    
    Configure Bonjour profiles. Bonjour is Apple's zero configuration networking protocol. Bonjour profiles allow APs and FortiAPs to connect to networks using Bonjour.
    
    **Usage:**
        payload: BonjourProfilePayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # Bonjour profile name. | MaxLen: 35
    comment: str  # Comment. | MaxLen: 63
    micro_location: Literal["enable", "disable"]  # Enable/disable Micro location for Bonjour profile | Default: disable
    policy_list: list[dict[str, Any]]  # Bonjour policy list.

# Nested TypedDicts for table field children (dict mode)

class BonjourProfilePolicylistItem(TypedDict):
    """Type hints for policy-list table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    policy_id: int  # Policy ID. | Default: 0 | Min: 1 | Max: 65535
    description: str  # Description. | MaxLen: 63
    from_vlan: str  # VLAN ID from which the Bonjour service is advertis | Default: 0 | MaxLen: 63
    to_vlan: str  # VLAN ID to which the Bonjour service is made avail | Default: all | MaxLen: 63
    services: Literal["all", "airplay", "afp", "bit-torrent", "ftp", "ichat", "itunes", "printers", "samba", "scanners", "ssh", "chromecast", "miracast"]  # Bonjour services for the VLAN connecting to the Bo | Default: all


# Nested classes for table field children (object mode)

@final
class BonjourProfilePolicylistObject:
    """Typed object for policy-list table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Policy ID. | Default: 0 | Min: 1 | Max: 65535
    policy_id: int
    # Description. | MaxLen: 63
    description: str
    # VLAN ID from which the Bonjour service is advertised | Default: 0 | MaxLen: 63
    from_vlan: str
    # VLAN ID to which the Bonjour service is made available | Default: all | MaxLen: 63
    to_vlan: str
    # Bonjour services for the VLAN connecting to the Bonjour netw | Default: all
    services: Literal["all", "airplay", "afp", "bit-torrent", "ftp", "ichat", "itunes", "printers", "samba", "scanners", "ssh", "chromecast", "miracast"]
    
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
class BonjourProfileResponse(TypedDict):
    """
    Type hints for wireless_controller/bonjour_profile API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str  # Bonjour profile name. | MaxLen: 35
    comment: str  # Comment. | MaxLen: 63
    micro_location: Literal["enable", "disable"]  # Enable/disable Micro location for Bonjour profile | Default: disable
    policy_list: list[BonjourProfilePolicylistItem]  # Bonjour policy list.


@final
class BonjourProfileObject:
    """Typed FortiObject for wireless_controller/bonjour_profile with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Bonjour profile name. | MaxLen: 35
    name: str
    # Comment. | MaxLen: 63
    comment: str
    # Enable/disable Micro location for Bonjour profile | Default: disable
    micro_location: Literal["enable", "disable"]
    # Bonjour policy list.
    policy_list: list[BonjourProfilePolicylistObject]
    
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
    def to_dict(self) -> BonjourProfilePayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class BonjourProfile:
    """
    Configure Bonjour profiles. Bonjour is Apple's zero configuration networking protocol. Bonjour profiles allow APs and FortiAPs to connect to networks using Bonjour.
    
    Path: wireless_controller/bonjour_profile
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
    ) -> BonjourProfileObject: ...
    
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
    ) -> BonjourProfileObject: ...
    
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
    ) -> FortiObjectList[BonjourProfileObject]: ...
    
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
    ) -> BonjourProfileObject: ...
    
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
    ) -> BonjourProfileObject: ...
    
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
    ) -> FortiObjectList[BonjourProfileObject]: ...
    
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
    ) -> BonjourProfileObject: ...
    
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
    ) -> BonjourProfileObject: ...
    
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
    ) -> FortiObjectList[BonjourProfileObject]: ...
    
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
    ) -> BonjourProfileObject | list[BonjourProfileObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: BonjourProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        micro_location: Literal["enable", "disable"] | None = ...,
        policy_list: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> BonjourProfileObject: ...
    
    @overload
    def post(
        self,
        payload_dict: BonjourProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        micro_location: Literal["enable", "disable"] | None = ...,
        policy_list: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: BonjourProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        micro_location: Literal["enable", "disable"] | None = ...,
        policy_list: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def post(
        self,
        payload_dict: BonjourProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        micro_location: Literal["enable", "disable"] | None = ...,
        policy_list: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: BonjourProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        micro_location: Literal["enable", "disable"] | None = ...,
        policy_list: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> BonjourProfileObject: ...
    
    @overload
    def put(
        self,
        payload_dict: BonjourProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        micro_location: Literal["enable", "disable"] | None = ...,
        policy_list: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: BonjourProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        micro_location: Literal["enable", "disable"] | None = ...,
        policy_list: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def put(
        self,
        payload_dict: BonjourProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        micro_location: Literal["enable", "disable"] | None = ...,
        policy_list: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> BonjourProfileObject: ...
    
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: BonjourProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        micro_location: Literal["enable", "disable"] | None = ...,
        policy_list: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
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
    "BonjourProfile",
    "BonjourProfilePayload",
    "BonjourProfileResponse",
    "BonjourProfileObject",
]