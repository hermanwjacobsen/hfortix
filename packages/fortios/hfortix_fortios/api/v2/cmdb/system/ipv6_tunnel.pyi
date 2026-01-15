from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class Ipv6TunnelPayload(TypedDict, total=False):
    """
    Type hints for system/ipv6_tunnel payload fields.
    
    Configure IPv6/IPv4 in IPv6 tunnel.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.system.interface.InterfaceEndpoint` (via: interface)

    **Usage:**
        payload: Ipv6TunnelPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # IPv6 tunnel name. | MaxLen: 15
    source: str  # Local IPv6 address of the tunnel. | Default: ::
    destination: str  # Remote IPv6 address of the tunnel. | Default: ::
    interface: str  # Interface name. | MaxLen: 15
    use_sdwan: Literal["disable", "enable"]  # Enable/disable use of SD-WAN to reach remote gatew | Default: disable
    auto_asic_offload: Literal["enable", "disable"]  # Enable/disable tunnel ASIC offloading. | Default: enable

# Nested TypedDicts for table field children (dict mode)

# Nested classes for table field children (object mode)


# Response TypedDict for GET returns (all fields present in API response)
class Ipv6TunnelResponse(TypedDict):
    """
    Type hints for system/ipv6_tunnel API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str  # IPv6 tunnel name. | MaxLen: 15
    source: str  # Local IPv6 address of the tunnel. | Default: ::
    destination: str  # Remote IPv6 address of the tunnel. | Default: ::
    interface: str  # Interface name. | MaxLen: 15
    use_sdwan: Literal["disable", "enable"]  # Enable/disable use of SD-WAN to reach remote gatew | Default: disable
    auto_asic_offload: Literal["enable", "disable"]  # Enable/disable tunnel ASIC offloading. | Default: enable


@final
class Ipv6TunnelObject:
    """Typed FortiObject for system/ipv6_tunnel with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # IPv6 tunnel name. | MaxLen: 15
    name: str
    # Local IPv6 address of the tunnel. | Default: ::
    source: str
    # Remote IPv6 address of the tunnel. | Default: ::
    destination: str
    # Interface name. | MaxLen: 15
    interface: str
    # Enable/disable use of SD-WAN to reach remote gateway. | Default: disable
    use_sdwan: Literal["disable", "enable"]
    # Enable/disable tunnel ASIC offloading. | Default: enable
    auto_asic_offload: Literal["enable", "disable"]
    
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
    def to_dict(self) -> Ipv6TunnelPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Ipv6Tunnel:
    """
    Configure IPv6/IPv4 in IPv6 tunnel.
    
    Path: system/ipv6_tunnel
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
    ) -> Ipv6TunnelObject: ...
    
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
    ) -> Ipv6TunnelObject: ...
    
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
    ) -> FortiObjectList[Ipv6TunnelObject]: ...
    
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
    ) -> Ipv6TunnelObject: ...
    
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
    ) -> Ipv6TunnelObject: ...
    
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
    ) -> FortiObjectList[Ipv6TunnelObject]: ...
    
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
    ) -> Ipv6TunnelObject: ...
    
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
    ) -> Ipv6TunnelObject: ...
    
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
    ) -> FortiObjectList[Ipv6TunnelObject]: ...
    
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
    ) -> Ipv6TunnelObject | list[Ipv6TunnelObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: Ipv6TunnelPayload | None = ...,
        name: str | None = ...,
        source: str | None = ...,
        destination: str | None = ...,
        interface: str | None = ...,
        use_sdwan: Literal["disable", "enable"] | None = ...,
        auto_asic_offload: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> Ipv6TunnelObject: ...
    
    @overload
    def post(
        self,
        payload_dict: Ipv6TunnelPayload | None = ...,
        name: str | None = ...,
        source: str | None = ...,
        destination: str | None = ...,
        interface: str | None = ...,
        use_sdwan: Literal["disable", "enable"] | None = ...,
        auto_asic_offload: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: Ipv6TunnelPayload | None = ...,
        name: str | None = ...,
        source: str | None = ...,
        destination: str | None = ...,
        interface: str | None = ...,
        use_sdwan: Literal["disable", "enable"] | None = ...,
        auto_asic_offload: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def post(
        self,
        payload_dict: Ipv6TunnelPayload | None = ...,
        name: str | None = ...,
        source: str | None = ...,
        destination: str | None = ...,
        interface: str | None = ...,
        use_sdwan: Literal["disable", "enable"] | None = ...,
        auto_asic_offload: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: Ipv6TunnelPayload | None = ...,
        name: str | None = ...,
        source: str | None = ...,
        destination: str | None = ...,
        interface: str | None = ...,
        use_sdwan: Literal["disable", "enable"] | None = ...,
        auto_asic_offload: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> Ipv6TunnelObject: ...
    
    @overload
    def put(
        self,
        payload_dict: Ipv6TunnelPayload | None = ...,
        name: str | None = ...,
        source: str | None = ...,
        destination: str | None = ...,
        interface: str | None = ...,
        use_sdwan: Literal["disable", "enable"] | None = ...,
        auto_asic_offload: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: Ipv6TunnelPayload | None = ...,
        name: str | None = ...,
        source: str | None = ...,
        destination: str | None = ...,
        interface: str | None = ...,
        use_sdwan: Literal["disable", "enable"] | None = ...,
        auto_asic_offload: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def put(
        self,
        payload_dict: Ipv6TunnelPayload | None = ...,
        name: str | None = ...,
        source: str | None = ...,
        destination: str | None = ...,
        interface: str | None = ...,
        use_sdwan: Literal["disable", "enable"] | None = ...,
        auto_asic_offload: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> Ipv6TunnelObject: ...
    
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
        payload_dict: Ipv6TunnelPayload | None = ...,
        name: str | None = ...,
        source: str | None = ...,
        destination: str | None = ...,
        interface: str | None = ...,
        use_sdwan: Literal["disable", "enable"] | None = ...,
        auto_asic_offload: Literal["enable", "disable"] | None = ...,
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
    "Ipv6Tunnel",
    "Ipv6TunnelPayload",
    "Ipv6TunnelResponse",
    "Ipv6TunnelObject",
]