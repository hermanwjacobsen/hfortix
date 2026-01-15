from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList
from hfortix_core.types import MutationResponse

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class SwitchInterfacePayload(TypedDict, total=False):
    """
    Type hints for system/switch_interface payload fields.
    
    Configure software switch interfaces by grouping physical and WiFi interfaces.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.system.interface.InterfaceEndpoint` (via: span-dest-port)
        - :class:`~.system.vdom.VdomEndpoint` (via: vdom)

    **Usage:**
        payload: SwitchInterfacePayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # Interface name | MaxLen: 15
    vdom: str  # VDOM that the software switch belongs to. | MaxLen: 31
    span_dest_port: str  # SPAN destination port name. All traffic on the SPA | MaxLen: 15
    span_source_port: list[dict[str, Any]]  # Physical interface name. Port spanning echoes all
    member: list[dict[str, Any]]  # Names of the interfaces that belong to the virtual
    type: Literal["switch", "hub"]  # Type of switch based on functionality: switch for | Default: switch
    intra_switch_policy: Literal["implicit", "explicit"]  # Allow any traffic between switch interfaces or req | Default: implicit
    mac_ttl: int  # Duration for which MAC addresses are held in the A | Default: 300 | Min: 300 | Max: 8640000
    span: Literal["disable", "enable"]  # Enable/disable port spanning. Port spanning echoes | Default: disable
    span_direction: Literal["rx", "tx", "both"]  # The direction in which the SPAN port operates, eit | Default: both

# Nested TypedDicts for table field children (dict mode)

class SwitchInterfaceSpansourceportItem(TypedDict):
    """Type hints for span-source-port table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    interface_name: str  # Physical interface name. | MaxLen: 79


class SwitchInterfaceMemberItem(TypedDict):
    """Type hints for member table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    interface_name: str  # Interface name. | MaxLen: 79


# Nested classes for table field children (object mode)

@final
class SwitchInterfaceSpansourceportObject:
    """Typed object for span-source-port table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Physical interface name. | MaxLen: 79
    interface_name: str
    
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
class SwitchInterfaceMemberObject:
    """Typed object for member table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Interface name. | MaxLen: 79
    interface_name: str
    
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
class SwitchInterfaceResponse(TypedDict):
    """
    Type hints for system/switch_interface API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str  # Interface name | MaxLen: 15
    vdom: str  # VDOM that the software switch belongs to. | MaxLen: 31
    span_dest_port: str  # SPAN destination port name. All traffic on the SPA | MaxLen: 15
    span_source_port: list[SwitchInterfaceSpansourceportItem]  # Physical interface name. Port spanning echoes all
    member: list[SwitchInterfaceMemberItem]  # Names of the interfaces that belong to the virtual
    type: Literal["switch", "hub"]  # Type of switch based on functionality: switch for | Default: switch
    intra_switch_policy: Literal["implicit", "explicit"]  # Allow any traffic between switch interfaces or req | Default: implicit
    mac_ttl: int  # Duration for which MAC addresses are held in the A | Default: 300 | Min: 300 | Max: 8640000
    span: Literal["disable", "enable"]  # Enable/disable port spanning. Port spanning echoes | Default: disable
    span_direction: Literal["rx", "tx", "both"]  # The direction in which the SPAN port operates, eit | Default: both


@final
class SwitchInterfaceObject:
    """Typed FortiObject for system/switch_interface with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Interface name | MaxLen: 15
    name: str
    # VDOM that the software switch belongs to. | MaxLen: 31
    vdom: str
    # SPAN destination port name. All traffic on the SPAN source p | MaxLen: 15
    span_dest_port: str
    # Physical interface name. Port spanning echoes all traffic on
    span_source_port: list[SwitchInterfaceSpansourceportObject]
    # Names of the interfaces that belong to the virtual switch.
    member: list[SwitchInterfaceMemberObject]
    # Type of switch based on functionality: switch for normal fun | Default: switch
    type: Literal["switch", "hub"]
    # Allow any traffic between switch interfaces or require firew | Default: implicit
    intra_switch_policy: Literal["implicit", "explicit"]
    # Duration for which MAC addresses are held in the ARP table | Default: 300 | Min: 300 | Max: 8640000
    mac_ttl: int
    # Enable/disable port spanning. Port spanning echoes traffic r | Default: disable
    span: Literal["disable", "enable"]
    # The direction in which the SPAN port operates, either: rx, t | Default: both
    span_direction: Literal["rx", "tx", "both"]
    
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
    def to_dict(self) -> SwitchInterfacePayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class SwitchInterface:
    """
    Configure software switch interfaces by grouping physical and WiFi interfaces.
    
    Path: system/switch_interface
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
    ) -> SwitchInterfaceObject: ...
    
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
    ) -> SwitchInterfaceObject: ...
    
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
    ) -> FortiObjectList[SwitchInterfaceObject]: ...
    
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
    ) -> SwitchInterfaceObject: ...
    
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
    ) -> SwitchInterfaceObject: ...
    
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
    ) -> FortiObjectList[SwitchInterfaceObject]: ...
    
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
    ) -> SwitchInterfaceObject: ...
    
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
    ) -> SwitchInterfaceObject: ...
    
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
    ) -> FortiObjectList[SwitchInterfaceObject]: ...
    
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
    ) -> SwitchInterfaceObject | list[SwitchInterfaceObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: SwitchInterfacePayload | None = ...,
        name: str | None = ...,
        span_dest_port: str | None = ...,
        span_source_port: str | list[str] | list[dict[str, Any]] | None = ...,
        member: str | list[str] | list[dict[str, Any]] | None = ...,
        type: Literal["switch", "hub"] | None = ...,
        intra_switch_policy: Literal["implicit", "explicit"] | None = ...,
        mac_ttl: int | None = ...,
        span: Literal["disable", "enable"] | None = ...,
        span_direction: Literal["rx", "tx", "both"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> SwitchInterfaceObject: ...
    
    @overload
    def post(
        self,
        payload_dict: SwitchInterfacePayload | None = ...,
        name: str | None = ...,
        span_dest_port: str | None = ...,
        span_source_port: str | list[str] | list[dict[str, Any]] | None = ...,
        member: str | list[str] | list[dict[str, Any]] | None = ...,
        type: Literal["switch", "hub"] | None = ...,
        intra_switch_policy: Literal["implicit", "explicit"] | None = ...,
        mac_ttl: int | None = ...,
        span: Literal["disable", "enable"] | None = ...,
        span_direction: Literal["rx", "tx", "both"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: SwitchInterfacePayload | None = ...,
        name: str | None = ...,
        span_dest_port: str | None = ...,
        span_source_port: str | list[str] | list[dict[str, Any]] | None = ...,
        member: str | list[str] | list[dict[str, Any]] | None = ...,
        type: Literal["switch", "hub"] | None = ...,
        intra_switch_policy: Literal["implicit", "explicit"] | None = ...,
        mac_ttl: int | None = ...,
        span: Literal["disable", "enable"] | None = ...,
        span_direction: Literal["rx", "tx", "both"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def post(
        self,
        payload_dict: SwitchInterfacePayload | None = ...,
        name: str | None = ...,
        span_dest_port: str | None = ...,
        span_source_port: str | list[str] | list[dict[str, Any]] | None = ...,
        member: str | list[str] | list[dict[str, Any]] | None = ...,
        type: Literal["switch", "hub"] | None = ...,
        intra_switch_policy: Literal["implicit", "explicit"] | None = ...,
        mac_ttl: int | None = ...,
        span: Literal["disable", "enable"] | None = ...,
        span_direction: Literal["rx", "tx", "both"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: SwitchInterfacePayload | None = ...,
        name: str | None = ...,
        span_dest_port: str | None = ...,
        span_source_port: str | list[str] | list[dict[str, Any]] | None = ...,
        member: str | list[str] | list[dict[str, Any]] | None = ...,
        type: Literal["switch", "hub"] | None = ...,
        intra_switch_policy: Literal["implicit", "explicit"] | None = ...,
        mac_ttl: int | None = ...,
        span: Literal["disable", "enable"] | None = ...,
        span_direction: Literal["rx", "tx", "both"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> SwitchInterfaceObject: ...
    
    @overload
    def put(
        self,
        payload_dict: SwitchInterfacePayload | None = ...,
        name: str | None = ...,
        span_dest_port: str | None = ...,
        span_source_port: str | list[str] | list[dict[str, Any]] | None = ...,
        member: str | list[str] | list[dict[str, Any]] | None = ...,
        type: Literal["switch", "hub"] | None = ...,
        intra_switch_policy: Literal["implicit", "explicit"] | None = ...,
        mac_ttl: int | None = ...,
        span: Literal["disable", "enable"] | None = ...,
        span_direction: Literal["rx", "tx", "both"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: SwitchInterfacePayload | None = ...,
        name: str | None = ...,
        span_dest_port: str | None = ...,
        span_source_port: str | list[str] | list[dict[str, Any]] | None = ...,
        member: str | list[str] | list[dict[str, Any]] | None = ...,
        type: Literal["switch", "hub"] | None = ...,
        intra_switch_policy: Literal["implicit", "explicit"] | None = ...,
        mac_ttl: int | None = ...,
        span: Literal["disable", "enable"] | None = ...,
        span_direction: Literal["rx", "tx", "both"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def put(
        self,
        payload_dict: SwitchInterfacePayload | None = ...,
        name: str | None = ...,
        span_dest_port: str | None = ...,
        span_source_port: str | list[str] | list[dict[str, Any]] | None = ...,
        member: str | list[str] | list[dict[str, Any]] | None = ...,
        type: Literal["switch", "hub"] | None = ...,
        intra_switch_policy: Literal["implicit", "explicit"] | None = ...,
        mac_ttl: int | None = ...,
        span: Literal["disable", "enable"] | None = ...,
        span_direction: Literal["rx", "tx", "both"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> SwitchInterfaceObject: ...
    
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
        payload_dict: SwitchInterfacePayload | None = ...,
        name: str | None = ...,
        span_dest_port: str | None = ...,
        span_source_port: str | list[str] | list[dict[str, Any]] | None = ...,
        member: str | list[str] | list[dict[str, Any]] | None = ...,
        type: Literal["switch", "hub"] | None = ...,
        intra_switch_policy: Literal["implicit", "explicit"] | None = ...,
        mac_ttl: int | None = ...,
        span: Literal["disable", "enable"] | None = ...,
        span_direction: Literal["rx", "tx", "both"] | None = ...,
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
    "SwitchInterface",
    "SwitchInterfacePayload",
    "SwitchInterfaceResponse",
    "SwitchInterfaceObject",
]