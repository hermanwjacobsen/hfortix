from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList
from hfortix_core.types import MutationResponse

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class IpipTunnelPayload(TypedDict, total=False):
    """
    Type hints for system/ipip_tunnel payload fields.
    
    Configure IP in IP Tunneling.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.system.interface.InterfaceEndpoint` (via: interface)

    **Usage:**
        payload: IpipTunnelPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # IPIP Tunnel name. | MaxLen: 15
    interface: str  # Interface name that is associated with the incomin | MaxLen: 15
    remote_gw: str  # IPv4 address for the remote gateway. | Default: 0.0.0.0
    local_gw: str  # IPv4 address for the local gateway. | Default: 0.0.0.0
    use_sdwan: Literal["disable", "enable"]  # Enable/disable use of SD-WAN to reach remote gatew | Default: disable
    auto_asic_offload: Literal["enable", "disable"]  # Enable/disable tunnel ASIC offloading. | Default: enable

# Nested TypedDicts for table field children (dict mode)

# Nested classes for table field children (object mode)


# Response TypedDict for GET returns (all fields present in API response)
class IpipTunnelResponse(TypedDict):
    """
    Type hints for system/ipip_tunnel API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str  # IPIP Tunnel name. | MaxLen: 15
    interface: str  # Interface name that is associated with the incomin | MaxLen: 15
    remote_gw: str  # IPv4 address for the remote gateway. | Default: 0.0.0.0
    local_gw: str  # IPv4 address for the local gateway. | Default: 0.0.0.0
    use_sdwan: Literal["disable", "enable"]  # Enable/disable use of SD-WAN to reach remote gatew | Default: disable
    auto_asic_offload: Literal["enable", "disable"]  # Enable/disable tunnel ASIC offloading. | Default: enable


@final
class IpipTunnelObject:
    """Typed FortiObject for system/ipip_tunnel with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # IPIP Tunnel name. | MaxLen: 15
    name: str
    # Interface name that is associated with the incoming traffic | MaxLen: 15
    interface: str
    # IPv4 address for the remote gateway. | Default: 0.0.0.0
    remote_gw: str
    # IPv4 address for the local gateway. | Default: 0.0.0.0
    local_gw: str
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
    def to_dict(self) -> IpipTunnelPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class IpipTunnel:
    """
    Configure IP in IP Tunneling.
    
    Path: system/ipip_tunnel
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
    ) -> IpipTunnelObject: ...
    
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
    ) -> IpipTunnelObject: ...
    
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
    ) -> FortiObjectList[IpipTunnelObject]: ...
    
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
    ) -> IpipTunnelObject: ...
    
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
    ) -> IpipTunnelObject: ...
    
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
    ) -> FortiObjectList[IpipTunnelObject]: ...
    
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
    ) -> IpipTunnelObject: ...
    
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
    ) -> IpipTunnelObject: ...
    
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
    ) -> FortiObjectList[IpipTunnelObject]: ...
    
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
    ) -> IpipTunnelObject | list[IpipTunnelObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: IpipTunnelPayload | None = ...,
        name: str | None = ...,
        interface: str | None = ...,
        remote_gw: str | None = ...,
        local_gw: str | None = ...,
        use_sdwan: Literal["disable", "enable"] | None = ...,
        auto_asic_offload: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> IpipTunnelObject: ...
    
    @overload
    def post(
        self,
        payload_dict: IpipTunnelPayload | None = ...,
        name: str | None = ...,
        interface: str | None = ...,
        remote_gw: str | None = ...,
        local_gw: str | None = ...,
        use_sdwan: Literal["disable", "enable"] | None = ...,
        auto_asic_offload: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: IpipTunnelPayload | None = ...,
        name: str | None = ...,
        interface: str | None = ...,
        remote_gw: str | None = ...,
        local_gw: str | None = ...,
        use_sdwan: Literal["disable", "enable"] | None = ...,
        auto_asic_offload: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def post(
        self,
        payload_dict: IpipTunnelPayload | None = ...,
        name: str | None = ...,
        interface: str | None = ...,
        remote_gw: str | None = ...,
        local_gw: str | None = ...,
        use_sdwan: Literal["disable", "enable"] | None = ...,
        auto_asic_offload: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: IpipTunnelPayload | None = ...,
        name: str | None = ...,
        interface: str | None = ...,
        remote_gw: str | None = ...,
        local_gw: str | None = ...,
        use_sdwan: Literal["disable", "enable"] | None = ...,
        auto_asic_offload: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> IpipTunnelObject: ...
    
    @overload
    def put(
        self,
        payload_dict: IpipTunnelPayload | None = ...,
        name: str | None = ...,
        interface: str | None = ...,
        remote_gw: str | None = ...,
        local_gw: str | None = ...,
        use_sdwan: Literal["disable", "enable"] | None = ...,
        auto_asic_offload: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: IpipTunnelPayload | None = ...,
        name: str | None = ...,
        interface: str | None = ...,
        remote_gw: str | None = ...,
        local_gw: str | None = ...,
        use_sdwan: Literal["disable", "enable"] | None = ...,
        auto_asic_offload: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def put(
        self,
        payload_dict: IpipTunnelPayload | None = ...,
        name: str | None = ...,
        interface: str | None = ...,
        remote_gw: str | None = ...,
        local_gw: str | None = ...,
        use_sdwan: Literal["disable", "enable"] | None = ...,
        auto_asic_offload: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> IpipTunnelObject: ...
    
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
        payload_dict: IpipTunnelPayload | None = ...,
        name: str | None = ...,
        interface: str | None = ...,
        remote_gw: str | None = ...,
        local_gw: str | None = ...,
        use_sdwan: Literal["disable", "enable"] | None = ...,
        auto_asic_offload: Literal["enable", "disable"] | None = ...,
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
    "IpipTunnel",
    "IpipTunnelPayload",
    "IpipTunnelResponse",
    "IpipTunnelObject",
]