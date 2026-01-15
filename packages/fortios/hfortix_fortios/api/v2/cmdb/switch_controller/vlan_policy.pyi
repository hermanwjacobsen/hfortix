from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class VlanPolicyPayload(TypedDict, total=False):
    """
    Type hints for switch_controller/vlan_policy payload fields.
    
    Configure VLAN policy to be applied on the managed FortiSwitch ports through dynamic-port-policy.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.system.interface.InterfaceEndpoint` (via: fortilink, vlan)

    **Usage:**
        payload: VlanPolicyPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # VLAN policy name. | MaxLen: 63
    description: str  # Description for the VLAN policy. | MaxLen: 63
    fortilink: str  # FortiLink interface for which this VLAN policy bel | MaxLen: 15
    vlan: str  # Native VLAN to be applied when using this VLAN pol | MaxLen: 15
    allowed_vlans: list[dict[str, Any]]  # Allowed VLANs to be applied when using this VLAN p
    untagged_vlans: list[dict[str, Any]]  # Untagged VLANs to be applied when using this VLAN
    allowed_vlans_all: Literal["enable", "disable"]  # Enable/disable all defined VLANs when using this V | Default: disable
    discard_mode: Literal["none", "all-untagged", "all-tagged"]  # Discard mode to be applied when using this VLAN po | Default: none

# Nested TypedDicts for table field children (dict mode)

class VlanPolicyAllowedvlansItem(TypedDict):
    """Type hints for allowed-vlans table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    vlan_name: str  # VLAN name. | MaxLen: 79


class VlanPolicyUntaggedvlansItem(TypedDict):
    """Type hints for untagged-vlans table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    vlan_name: str  # VLAN name. | MaxLen: 79


# Nested classes for table field children (object mode)

@final
class VlanPolicyAllowedvlansObject:
    """Typed object for allowed-vlans table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # VLAN name. | MaxLen: 79
    vlan_name: str
    
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


@final
class VlanPolicyUntaggedvlansObject:
    """Typed object for untagged-vlans table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # VLAN name. | MaxLen: 79
    vlan_name: str
    
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
class VlanPolicyResponse(TypedDict):
    """
    Type hints for switch_controller/vlan_policy API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str  # VLAN policy name. | MaxLen: 63
    description: str  # Description for the VLAN policy. | MaxLen: 63
    fortilink: str  # FortiLink interface for which this VLAN policy bel | MaxLen: 15
    vlan: str  # Native VLAN to be applied when using this VLAN pol | MaxLen: 15
    allowed_vlans: list[VlanPolicyAllowedvlansItem]  # Allowed VLANs to be applied when using this VLAN p
    untagged_vlans: list[VlanPolicyUntaggedvlansItem]  # Untagged VLANs to be applied when using this VLAN
    allowed_vlans_all: Literal["enable", "disable"]  # Enable/disable all defined VLANs when using this V | Default: disable
    discard_mode: Literal["none", "all-untagged", "all-tagged"]  # Discard mode to be applied when using this VLAN po | Default: none


@final
class VlanPolicyObject:
    """Typed FortiObject for switch_controller/vlan_policy with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # VLAN policy name. | MaxLen: 63
    name: str
    # Description for the VLAN policy. | MaxLen: 63
    description: str
    # FortiLink interface for which this VLAN policy belongs to. | MaxLen: 15
    fortilink: str
    # Native VLAN to be applied when using this VLAN policy. | MaxLen: 15
    vlan: str
    # Allowed VLANs to be applied when using this VLAN policy.
    allowed_vlans: list[VlanPolicyAllowedvlansObject]
    # Untagged VLANs to be applied when using this VLAN policy.
    untagged_vlans: list[VlanPolicyUntaggedvlansObject]
    # Enable/disable all defined VLANs when using this VLAN policy | Default: disable
    allowed_vlans_all: Literal["enable", "disable"]
    # Discard mode to be applied when using this VLAN policy. | Default: none
    discard_mode: Literal["none", "all-untagged", "all-tagged"]
    
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
    def to_dict(self) -> VlanPolicyPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class VlanPolicy:
    """
    Configure VLAN policy to be applied on the managed FortiSwitch ports through dynamic-port-policy.
    
    Path: switch_controller/vlan_policy
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
    ) -> VlanPolicyObject: ...
    
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
    ) -> VlanPolicyObject: ...
    
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
    ) -> FortiObjectList[VlanPolicyObject]: ...
    
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
    ) -> VlanPolicyObject: ...
    
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
    ) -> VlanPolicyObject: ...
    
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
    ) -> FortiObjectList[VlanPolicyObject]: ...
    
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
    ) -> VlanPolicyObject: ...
    
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
    ) -> VlanPolicyObject: ...
    
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
    ) -> FortiObjectList[VlanPolicyObject]: ...
    
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
    ) -> VlanPolicyObject | list[VlanPolicyObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: VlanPolicyPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        fortilink: str | None = ...,
        vlan: str | None = ...,
        allowed_vlans: str | list[str] | list[dict[str, Any]] | None = ...,
        untagged_vlans: str | list[str] | list[dict[str, Any]] | None = ...,
        allowed_vlans_all: Literal["enable", "disable"] | None = ...,
        discard_mode: Literal["none", "all-untagged", "all-tagged"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> VlanPolicyObject: ...
    
    @overload
    def post(
        self,
        payload_dict: VlanPolicyPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        fortilink: str | None = ...,
        vlan: str | None = ...,
        allowed_vlans: str | list[str] | list[dict[str, Any]] | None = ...,
        untagged_vlans: str | list[str] | list[dict[str, Any]] | None = ...,
        allowed_vlans_all: Literal["enable", "disable"] | None = ...,
        discard_mode: Literal["none", "all-untagged", "all-tagged"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: VlanPolicyPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        fortilink: str | None = ...,
        vlan: str | None = ...,
        allowed_vlans: str | list[str] | list[dict[str, Any]] | None = ...,
        untagged_vlans: str | list[str] | list[dict[str, Any]] | None = ...,
        allowed_vlans_all: Literal["enable", "disable"] | None = ...,
        discard_mode: Literal["none", "all-untagged", "all-tagged"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def post(
        self,
        payload_dict: VlanPolicyPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        fortilink: str | None = ...,
        vlan: str | None = ...,
        allowed_vlans: str | list[str] | list[dict[str, Any]] | None = ...,
        untagged_vlans: str | list[str] | list[dict[str, Any]] | None = ...,
        allowed_vlans_all: Literal["enable", "disable"] | None = ...,
        discard_mode: Literal["none", "all-untagged", "all-tagged"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: VlanPolicyPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        fortilink: str | None = ...,
        vlan: str | None = ...,
        allowed_vlans: str | list[str] | list[dict[str, Any]] | None = ...,
        untagged_vlans: str | list[str] | list[dict[str, Any]] | None = ...,
        allowed_vlans_all: Literal["enable", "disable"] | None = ...,
        discard_mode: Literal["none", "all-untagged", "all-tagged"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> VlanPolicyObject: ...
    
    @overload
    def put(
        self,
        payload_dict: VlanPolicyPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        fortilink: str | None = ...,
        vlan: str | None = ...,
        allowed_vlans: str | list[str] | list[dict[str, Any]] | None = ...,
        untagged_vlans: str | list[str] | list[dict[str, Any]] | None = ...,
        allowed_vlans_all: Literal["enable", "disable"] | None = ...,
        discard_mode: Literal["none", "all-untagged", "all-tagged"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: VlanPolicyPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        fortilink: str | None = ...,
        vlan: str | None = ...,
        allowed_vlans: str | list[str] | list[dict[str, Any]] | None = ...,
        untagged_vlans: str | list[str] | list[dict[str, Any]] | None = ...,
        allowed_vlans_all: Literal["enable", "disable"] | None = ...,
        discard_mode: Literal["none", "all-untagged", "all-tagged"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def put(
        self,
        payload_dict: VlanPolicyPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        fortilink: str | None = ...,
        vlan: str | None = ...,
        allowed_vlans: str | list[str] | list[dict[str, Any]] | None = ...,
        untagged_vlans: str | list[str] | list[dict[str, Any]] | None = ...,
        allowed_vlans_all: Literal["enable", "disable"] | None = ...,
        discard_mode: Literal["none", "all-untagged", "all-tagged"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> VlanPolicyObject: ...
    
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
        payload_dict: VlanPolicyPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        fortilink: str | None = ...,
        vlan: str | None = ...,
        allowed_vlans: str | list[str] | list[dict[str, Any]] | None = ...,
        untagged_vlans: str | list[str] | list[dict[str, Any]] | None = ...,
        allowed_vlans_all: Literal["enable", "disable"] | None = ...,
        discard_mode: Literal["none", "all-untagged", "all-tagged"] | None = ...,
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
    "VlanPolicy",
    "VlanPolicyPayload",
    "VlanPolicyResponse",
    "VlanPolicyObject",
]