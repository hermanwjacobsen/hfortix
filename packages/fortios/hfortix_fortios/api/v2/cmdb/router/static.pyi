from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class StaticPayload(TypedDict, total=False):
    """
    Type hints for router/static payload fields.
    
    Configure IPv4 static routing tables.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.firewall.address.AddressEndpoint` (via: dstaddr)
        - :class:`~.firewall.addrgrp.AddrgrpEndpoint` (via: dstaddr)
        - :class:`~.firewall.internet-service.InternetServiceEndpoint` (via: internet-service)
        - :class:`~.firewall.internet-service-custom.InternetServiceCustomEndpoint` (via: internet-service-custom)
        - :class:`~.firewall.internet-service-fortiguard.InternetServiceFortiguardEndpoint` (via: internet-service-fortiguard)
        - :class:`~.system.interface.InterfaceEndpoint` (via: device)

    **Usage:**
        payload: StaticPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    seq_num: int  # Sequence number. | Default: 0 | Min: 0 | Max: 4294967295
    status: Literal["enable", "disable"]  # Enable/disable this static route. | Default: enable
    dst: str  # Destination IP and mask for this route. | Default: 0.0.0.0 0.0.0.0
    src: str  # Source prefix for this route. | Default: 0.0.0.0 0.0.0.0
    gateway: str  # Gateway IP for this route. | Default: 0.0.0.0
    preferred_source: str  # Preferred source IP for this route. | Default: 0.0.0.0
    distance: int  # Administrative distance (1 - 255). | Default: 10 | Min: 1 | Max: 255
    weight: int  # Administrative weight (0 - 255). | Default: 0 | Min: 0 | Max: 255
    priority: int  # Administrative priority (1 - 65535). | Default: 1 | Min: 1 | Max: 65535
    device: str  # Gateway out interface or tunnel. | MaxLen: 35
    comment: str  # Optional comments. | MaxLen: 255
    blackhole: Literal["enable", "disable"]  # Enable/disable black hole. | Default: disable
    dynamic_gateway: Literal["enable", "disable"]  # Enable use of dynamic gateway retrieved from a DHC | Default: disable
    sdwan_zone: list[dict[str, Any]]  # Choose SD-WAN Zone.
    dstaddr: str  # Name of firewall address or address group. | MaxLen: 79
    internet_service: int  # Application ID in the Internet service database. | Default: 0 | Min: 0 | Max: 4294967295
    internet_service_custom: str  # Application name in the Internet service custom da | MaxLen: 64
    internet_service_fortiguard: str  # Application name in the Internet service fortiguar | MaxLen: 64
    link_monitor_exempt: Literal["enable", "disable"]  # Enable/disable withdrawal of this static route whe | Default: disable
    tag: int  # Route tag. | Default: 0 | Min: 0 | Max: 4294967295
    vrf: int  # Virtual Routing Forwarding ID. | Default: unspecified | Min: 0 | Max: 511
    bfd: Literal["enable", "disable"]  # Enable/disable Bidirectional Forwarding Detection | Default: disable

# Nested TypedDicts for table field children (dict mode)

class StaticSdwanzoneItem(TypedDict):
    """Type hints for sdwan-zone table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # SD-WAN zone name. | MaxLen: 79


# Nested classes for table field children (object mode)

@final
class StaticSdwanzoneObject:
    """Typed object for sdwan-zone table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # SD-WAN zone name. | MaxLen: 79
    name: str
    
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
class StaticResponse(TypedDict):
    """
    Type hints for router/static API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    seq_num: int  # Sequence number. | Default: 0 | Min: 0 | Max: 4294967295
    status: Literal["enable", "disable"]  # Enable/disable this static route. | Default: enable
    dst: str  # Destination IP and mask for this route. | Default: 0.0.0.0 0.0.0.0
    src: str  # Source prefix for this route. | Default: 0.0.0.0 0.0.0.0
    gateway: str  # Gateway IP for this route. | Default: 0.0.0.0
    preferred_source: str  # Preferred source IP for this route. | Default: 0.0.0.0
    distance: int  # Administrative distance (1 - 255). | Default: 10 | Min: 1 | Max: 255
    weight: int  # Administrative weight (0 - 255). | Default: 0 | Min: 0 | Max: 255
    priority: int  # Administrative priority (1 - 65535). | Default: 1 | Min: 1 | Max: 65535
    device: str  # Gateway out interface or tunnel. | MaxLen: 35
    comment: str  # Optional comments. | MaxLen: 255
    blackhole: Literal["enable", "disable"]  # Enable/disable black hole. | Default: disable
    dynamic_gateway: Literal["enable", "disable"]  # Enable use of dynamic gateway retrieved from a DHC | Default: disable
    sdwan_zone: list[StaticSdwanzoneItem]  # Choose SD-WAN Zone.
    dstaddr: str  # Name of firewall address or address group. | MaxLen: 79
    internet_service: int  # Application ID in the Internet service database. | Default: 0 | Min: 0 | Max: 4294967295
    internet_service_custom: str  # Application name in the Internet service custom da | MaxLen: 64
    internet_service_fortiguard: str  # Application name in the Internet service fortiguar | MaxLen: 64
    link_monitor_exempt: Literal["enable", "disable"]  # Enable/disable withdrawal of this static route whe | Default: disable
    tag: int  # Route tag. | Default: 0 | Min: 0 | Max: 4294967295
    vrf: int  # Virtual Routing Forwarding ID. | Default: unspecified | Min: 0 | Max: 511
    bfd: Literal["enable", "disable"]  # Enable/disable Bidirectional Forwarding Detection | Default: disable


@final
class StaticObject:
    """Typed FortiObject for router/static with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Sequence number. | Default: 0 | Min: 0 | Max: 4294967295
    seq_num: int
    # Enable/disable this static route. | Default: enable
    status: Literal["enable", "disable"]
    # Destination IP and mask for this route. | Default: 0.0.0.0 0.0.0.0
    dst: str
    # Source prefix for this route. | Default: 0.0.0.0 0.0.0.0
    src: str
    # Gateway IP for this route. | Default: 0.0.0.0
    gateway: str
    # Preferred source IP for this route. | Default: 0.0.0.0
    preferred_source: str
    # Administrative distance (1 - 255). | Default: 10 | Min: 1 | Max: 255
    distance: int
    # Administrative weight (0 - 255). | Default: 0 | Min: 0 | Max: 255
    weight: int
    # Administrative priority (1 - 65535). | Default: 1 | Min: 1 | Max: 65535
    priority: int
    # Gateway out interface or tunnel. | MaxLen: 35
    device: str
    # Optional comments. | MaxLen: 255
    comment: str
    # Enable/disable black hole. | Default: disable
    blackhole: Literal["enable", "disable"]
    # Enable use of dynamic gateway retrieved from a DHCP or PPP s | Default: disable
    dynamic_gateway: Literal["enable", "disable"]
    # Choose SD-WAN Zone.
    sdwan_zone: list[StaticSdwanzoneObject]
    # Name of firewall address or address group. | MaxLen: 79
    dstaddr: str
    # Application ID in the Internet service database. | Default: 0 | Min: 0 | Max: 4294967295
    internet_service: int
    # Application name in the Internet service custom database. | MaxLen: 64
    internet_service_custom: str
    # Application name in the Internet service fortiguard database | MaxLen: 64
    internet_service_fortiguard: str
    # Enable/disable withdrawal of this static route when link mon | Default: disable
    link_monitor_exempt: Literal["enable", "disable"]
    # Route tag. | Default: 0 | Min: 0 | Max: 4294967295
    tag: int
    # Virtual Routing Forwarding ID. | Default: unspecified | Min: 0 | Max: 511
    vrf: int
    # Enable/disable Bidirectional Forwarding Detection (BFD). | Default: disable
    bfd: Literal["enable", "disable"]
    
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
    def to_dict(self) -> StaticPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Static:
    """
    Configure IPv4 static routing tables.
    
    Path: router/static
    Category: cmdb
    Primary Key: seq-num
    """
    
    # ================================================================
    # GET OVERLOADS - Always returns FortiObject
    # Pylance matches overloads top-to-bottom, so these must come first!
    # ================================================================
    
    # With mkey as positional arg -> returns FortiObject
    @overload
    def get(
        self,
        seq_num: int,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> StaticObject: ...
    
    # With mkey as keyword arg -> returns FortiObject
    @overload
    def get(
        self,
        *,
        seq_num: int,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> StaticObject: ...
    
    # Without mkey -> returns list of FortiObjects
    @overload
    def get(
        self,
        seq_num: None = None,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObjectList[StaticObject]: ...
    
    # ================================================================
    # (removed - all GET now returns FortiObject)
    # ================================================================
    
    # With mkey as positional arg -> returns single object
    @overload
    def get(
        self,
        seq_num: int,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> StaticObject: ...
    
    # With mkey as keyword arg -> returns single object
    @overload
    def get(
        self,
        *,
        seq_num: int,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> StaticObject: ...
    
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
    ) -> FortiObjectList[StaticObject]: ...
    
    # Dict mode with mkey provided as positional arg (single dict)
    @overload
    def get(
        self,
        seq_num: int,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> StaticObject: ...
    
    # Dict mode with mkey provided as keyword arg (single dict)
    @overload
    def get(
        self,
        *,
        seq_num: int,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> StaticObject: ...
    
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
    ) -> FortiObjectList[StaticObject]: ...
    
    # Fallback overload for all other cases
    @overload
    def get(
        self,
        seq_num: int | None = ...,
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
        seq_num: int | None = ...,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> StaticObject | list[StaticObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: StaticPayload | None = ...,
        seq_num: int | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        dst: str | None = ...,
        src: str | None = ...,
        gateway: str | None = ...,
        preferred_source: str | None = ...,
        distance: int | None = ...,
        weight: int | None = ...,
        priority: int | None = ...,
        device: str | None = ...,
        comment: str | None = ...,
        blackhole: Literal["enable", "disable"] | None = ...,
        dynamic_gateway: Literal["enable", "disable"] | None = ...,
        sdwan_zone: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr: str | None = ...,
        internet_service: int | None = ...,
        internet_service_custom: str | None = ...,
        internet_service_fortiguard: str | None = ...,
        link_monitor_exempt: Literal["enable", "disable"] | None = ...,
        tag: int | None = ...,
        vrf: int | None = ...,
        bfd: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> StaticObject: ...
    
    @overload
    def post(
        self,
        payload_dict: StaticPayload | None = ...,
        seq_num: int | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        dst: str | None = ...,
        src: str | None = ...,
        gateway: str | None = ...,
        preferred_source: str | None = ...,
        distance: int | None = ...,
        weight: int | None = ...,
        priority: int | None = ...,
        device: str | None = ...,
        comment: str | None = ...,
        blackhole: Literal["enable", "disable"] | None = ...,
        dynamic_gateway: Literal["enable", "disable"] | None = ...,
        sdwan_zone: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr: str | None = ...,
        internet_service: int | None = ...,
        internet_service_custom: str | None = ...,
        internet_service_fortiguard: str | None = ...,
        link_monitor_exempt: Literal["enable", "disable"] | None = ...,
        tag: int | None = ...,
        vrf: int | None = ...,
        bfd: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: StaticPayload | None = ...,
        seq_num: int | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        dst: str | None = ...,
        src: str | None = ...,
        gateway: str | None = ...,
        preferred_source: str | None = ...,
        distance: int | None = ...,
        weight: int | None = ...,
        priority: int | None = ...,
        device: str | None = ...,
        comment: str | None = ...,
        blackhole: Literal["enable", "disable"] | None = ...,
        dynamic_gateway: Literal["enable", "disable"] | None = ...,
        sdwan_zone: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr: str | None = ...,
        internet_service: int | None = ...,
        internet_service_custom: str | None = ...,
        internet_service_fortiguard: str | None = ...,
        link_monitor_exempt: Literal["enable", "disable"] | None = ...,
        tag: int | None = ...,
        vrf: int | None = ...,
        bfd: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def post(
        self,
        payload_dict: StaticPayload | None = ...,
        seq_num: int | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        dst: str | None = ...,
        src: str | None = ...,
        gateway: str | None = ...,
        preferred_source: str | None = ...,
        distance: int | None = ...,
        weight: int | None = ...,
        priority: int | None = ...,
        device: str | None = ...,
        comment: str | None = ...,
        blackhole: Literal["enable", "disable"] | None = ...,
        dynamic_gateway: Literal["enable", "disable"] | None = ...,
        sdwan_zone: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr: str | None = ...,
        internet_service: int | None = ...,
        internet_service_custom: str | None = ...,
        internet_service_fortiguard: str | None = ...,
        link_monitor_exempt: Literal["enable", "disable"] | None = ...,
        tag: int | None = ...,
        vrf: int | None = ...,
        bfd: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: StaticPayload | None = ...,
        seq_num: int | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        dst: str | None = ...,
        src: str | None = ...,
        gateway: str | None = ...,
        preferred_source: str | None = ...,
        distance: int | None = ...,
        weight: int | None = ...,
        priority: int | None = ...,
        device: str | None = ...,
        comment: str | None = ...,
        blackhole: Literal["enable", "disable"] | None = ...,
        dynamic_gateway: Literal["enable", "disable"] | None = ...,
        sdwan_zone: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr: str | None = ...,
        internet_service: int | None = ...,
        internet_service_custom: str | None = ...,
        internet_service_fortiguard: str | None = ...,
        link_monitor_exempt: Literal["enable", "disable"] | None = ...,
        tag: int | None = ...,
        vrf: int | None = ...,
        bfd: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> StaticObject: ...
    
    @overload
    def put(
        self,
        payload_dict: StaticPayload | None = ...,
        seq_num: int | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        dst: str | None = ...,
        src: str | None = ...,
        gateway: str | None = ...,
        preferred_source: str | None = ...,
        distance: int | None = ...,
        weight: int | None = ...,
        priority: int | None = ...,
        device: str | None = ...,
        comment: str | None = ...,
        blackhole: Literal["enable", "disable"] | None = ...,
        dynamic_gateway: Literal["enable", "disable"] | None = ...,
        sdwan_zone: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr: str | None = ...,
        internet_service: int | None = ...,
        internet_service_custom: str | None = ...,
        internet_service_fortiguard: str | None = ...,
        link_monitor_exempt: Literal["enable", "disable"] | None = ...,
        tag: int | None = ...,
        vrf: int | None = ...,
        bfd: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: StaticPayload | None = ...,
        seq_num: int | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        dst: str | None = ...,
        src: str | None = ...,
        gateway: str | None = ...,
        preferred_source: str | None = ...,
        distance: int | None = ...,
        weight: int | None = ...,
        priority: int | None = ...,
        device: str | None = ...,
        comment: str | None = ...,
        blackhole: Literal["enable", "disable"] | None = ...,
        dynamic_gateway: Literal["enable", "disable"] | None = ...,
        sdwan_zone: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr: str | None = ...,
        internet_service: int | None = ...,
        internet_service_custom: str | None = ...,
        internet_service_fortiguard: str | None = ...,
        link_monitor_exempt: Literal["enable", "disable"] | None = ...,
        tag: int | None = ...,
        vrf: int | None = ...,
        bfd: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def put(
        self,
        payload_dict: StaticPayload | None = ...,
        seq_num: int | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        dst: str | None = ...,
        src: str | None = ...,
        gateway: str | None = ...,
        preferred_source: str | None = ...,
        distance: int | None = ...,
        weight: int | None = ...,
        priority: int | None = ...,
        device: str | None = ...,
        comment: str | None = ...,
        blackhole: Literal["enable", "disable"] | None = ...,
        dynamic_gateway: Literal["enable", "disable"] | None = ...,
        sdwan_zone: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr: str | None = ...,
        internet_service: int | None = ...,
        internet_service_custom: str | None = ...,
        internet_service_fortiguard: str | None = ...,
        link_monitor_exempt: Literal["enable", "disable"] | None = ...,
        tag: int | None = ...,
        vrf: int | None = ...,
        bfd: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        seq_num: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> StaticObject: ...
    
    @overload
    def delete(
        self,
        seq_num: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def delete(
        self,
        seq_num: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def delete(
        self,
        seq_num: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def exists(
        self,
        seq_num: int,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: StaticPayload | None = ...,
        seq_num: int | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        dst: str | None = ...,
        src: str | None = ...,
        gateway: str | None = ...,
        preferred_source: str | None = ...,
        distance: int | None = ...,
        weight: int | None = ...,
        priority: int | None = ...,
        device: str | None = ...,
        comment: str | None = ...,
        blackhole: Literal["enable", "disable"] | None = ...,
        dynamic_gateway: Literal["enable", "disable"] | None = ...,
        sdwan_zone: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr: str | None = ...,
        internet_service: int | None = ...,
        internet_service_custom: str | None = ...,
        internet_service_fortiguard: str | None = ...,
        link_monitor_exempt: Literal["enable", "disable"] | None = ...,
        tag: int | None = ...,
        vrf: int | None = ...,
        bfd: Literal["enable", "disable"] | None = ...,
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
    "Static",
    "StaticPayload",
    "StaticResponse",
    "StaticObject",
]