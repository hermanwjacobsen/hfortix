from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class GreTunnelPayload(TypedDict, total=False):
    """
    Type hints for system/gre_tunnel payload fields.
    
    Configure GRE tunnel.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.system.interface.InterfaceEndpoint` (via: interface)

    **Usage:**
        payload: GreTunnelPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # Tunnel name. | MaxLen: 15
    interface: str  # Interface name. | MaxLen: 15
    ip_version: Literal["4", "6"]  # IP version to use for VPN interface. | Default: 4
    remote_gw6: str  # IPv6 address of the remote gateway. | Default: ::
    local_gw6: str  # IPv6 address of the local gateway. | Default: ::
    remote_gw: str  # IP address of the remote gateway. | Default: 0.0.0.0
    local_gw: str  # IP address of the local gateway. | Default: 0.0.0.0
    use_sdwan: Literal["disable", "enable"]  # Enable/disable use of SD-WAN to reach remote gatew | Default: disable
    sequence_number_transmission: Literal["disable", "enable"]  # Enable/disable including of sequence numbers in tr | Default: disable
    sequence_number_reception: Literal["disable", "enable"]  # Enable/disable validating sequence numbers in rece | Default: disable
    checksum_transmission: Literal["disable", "enable"]  # Enable/disable including checksums in transmitted | Default: disable
    checksum_reception: Literal["disable", "enable"]  # Enable/disable validating checksums in received GR | Default: disable
    key_outbound: int  # Include this key in transmitted GRE packets | Default: 0 | Min: 0 | Max: 4294967295
    key_inbound: int  # Require received GRE packets contain this key | Default: 0 | Min: 0 | Max: 4294967295
    dscp_copying: Literal["disable", "enable"]  # Enable/disable DSCP copying. | Default: disable
    diffservcode: str  # DiffServ setting to be applied to GRE tunnel outer
    keepalive_interval: int  # Keepalive message interval | Default: 0 | Min: 0 | Max: 32767
    keepalive_failtimes: int  # Number of consecutive unreturned keepalive message | Default: 10 | Min: 1 | Max: 255

# Nested TypedDicts for table field children (dict mode)

# Nested classes for table field children (object mode)


# Response TypedDict for GET returns (all fields present in API response)
class GreTunnelResponse(TypedDict):
    """
    Type hints for system/gre_tunnel API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str  # Tunnel name. | MaxLen: 15
    interface: str  # Interface name. | MaxLen: 15
    ip_version: Literal["4", "6"]  # IP version to use for VPN interface. | Default: 4
    remote_gw6: str  # IPv6 address of the remote gateway. | Default: ::
    local_gw6: str  # IPv6 address of the local gateway. | Default: ::
    remote_gw: str  # IP address of the remote gateway. | Default: 0.0.0.0
    local_gw: str  # IP address of the local gateway. | Default: 0.0.0.0
    use_sdwan: Literal["disable", "enable"]  # Enable/disable use of SD-WAN to reach remote gatew | Default: disable
    sequence_number_transmission: Literal["disable", "enable"]  # Enable/disable including of sequence numbers in tr | Default: disable
    sequence_number_reception: Literal["disable", "enable"]  # Enable/disable validating sequence numbers in rece | Default: disable
    checksum_transmission: Literal["disable", "enable"]  # Enable/disable including checksums in transmitted | Default: disable
    checksum_reception: Literal["disable", "enable"]  # Enable/disable validating checksums in received GR | Default: disable
    key_outbound: int  # Include this key in transmitted GRE packets | Default: 0 | Min: 0 | Max: 4294967295
    key_inbound: int  # Require received GRE packets contain this key | Default: 0 | Min: 0 | Max: 4294967295
    dscp_copying: Literal["disable", "enable"]  # Enable/disable DSCP copying. | Default: disable
    diffservcode: str  # DiffServ setting to be applied to GRE tunnel outer
    keepalive_interval: int  # Keepalive message interval | Default: 0 | Min: 0 | Max: 32767
    keepalive_failtimes: int  # Number of consecutive unreturned keepalive message | Default: 10 | Min: 1 | Max: 255


@final
class GreTunnelObject:
    """Typed FortiObject for system/gre_tunnel with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Tunnel name. | MaxLen: 15
    name: str
    # Interface name. | MaxLen: 15
    interface: str
    # IP version to use for VPN interface. | Default: 4
    ip_version: Literal["4", "6"]
    # IPv6 address of the remote gateway. | Default: ::
    remote_gw6: str
    # IPv6 address of the local gateway. | Default: ::
    local_gw6: str
    # IP address of the remote gateway. | Default: 0.0.0.0
    remote_gw: str
    # IP address of the local gateway. | Default: 0.0.0.0
    local_gw: str
    # Enable/disable use of SD-WAN to reach remote gateway. | Default: disable
    use_sdwan: Literal["disable", "enable"]
    # Enable/disable including of sequence numbers in transmitted | Default: disable
    sequence_number_transmission: Literal["disable", "enable"]
    # Enable/disable validating sequence numbers in received GRE p | Default: disable
    sequence_number_reception: Literal["disable", "enable"]
    # Enable/disable including checksums in transmitted GRE packet | Default: disable
    checksum_transmission: Literal["disable", "enable"]
    # Enable/disable validating checksums in received GRE packets. | Default: disable
    checksum_reception: Literal["disable", "enable"]
    # Include this key in transmitted GRE packets (0 - 4294967295) | Default: 0 | Min: 0 | Max: 4294967295
    key_outbound: int
    # Require received GRE packets contain this key | Default: 0 | Min: 0 | Max: 4294967295
    key_inbound: int
    # Enable/disable DSCP copying. | Default: disable
    dscp_copying: Literal["disable", "enable"]
    # DiffServ setting to be applied to GRE tunnel outer IP header
    diffservcode: str
    # Keepalive message interval (0 - 32767, 0 = disabled). | Default: 0 | Min: 0 | Max: 32767
    keepalive_interval: int
    # Number of consecutive unreturned keepalive messages before a | Default: 10 | Min: 1 | Max: 255
    keepalive_failtimes: int
    
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
    def to_dict(self) -> GreTunnelPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class GreTunnel:
    """
    Configure GRE tunnel.
    
    Path: system/gre_tunnel
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
    ) -> GreTunnelObject: ...
    
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
    ) -> GreTunnelObject: ...
    
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
    ) -> FortiObjectList[GreTunnelObject]: ...
    
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
    ) -> GreTunnelObject: ...
    
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
    ) -> GreTunnelObject: ...
    
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
    ) -> FortiObjectList[GreTunnelObject]: ...
    
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
    ) -> GreTunnelObject: ...
    
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
    ) -> GreTunnelObject: ...
    
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
    ) -> FortiObjectList[GreTunnelObject]: ...
    
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
    ) -> GreTunnelObject | list[GreTunnelObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: GreTunnelPayload | None = ...,
        name: str | None = ...,
        interface: str | None = ...,
        ip_version: Literal["4", "6"] | None = ...,
        remote_gw6: str | None = ...,
        local_gw6: str | None = ...,
        remote_gw: str | None = ...,
        local_gw: str | None = ...,
        use_sdwan: Literal["disable", "enable"] | None = ...,
        sequence_number_transmission: Literal["disable", "enable"] | None = ...,
        sequence_number_reception: Literal["disable", "enable"] | None = ...,
        checksum_transmission: Literal["disable", "enable"] | None = ...,
        checksum_reception: Literal["disable", "enable"] | None = ...,
        key_outbound: int | None = ...,
        key_inbound: int | None = ...,
        dscp_copying: Literal["disable", "enable"] | None = ...,
        diffservcode: str | None = ...,
        keepalive_interval: int | None = ...,
        keepalive_failtimes: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> GreTunnelObject: ...
    
    @overload
    def post(
        self,
        payload_dict: GreTunnelPayload | None = ...,
        name: str | None = ...,
        interface: str | None = ...,
        ip_version: Literal["4", "6"] | None = ...,
        remote_gw6: str | None = ...,
        local_gw6: str | None = ...,
        remote_gw: str | None = ...,
        local_gw: str | None = ...,
        use_sdwan: Literal["disable", "enable"] | None = ...,
        sequence_number_transmission: Literal["disable", "enable"] | None = ...,
        sequence_number_reception: Literal["disable", "enable"] | None = ...,
        checksum_transmission: Literal["disable", "enable"] | None = ...,
        checksum_reception: Literal["disable", "enable"] | None = ...,
        key_outbound: int | None = ...,
        key_inbound: int | None = ...,
        dscp_copying: Literal["disable", "enable"] | None = ...,
        diffservcode: str | None = ...,
        keepalive_interval: int | None = ...,
        keepalive_failtimes: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: GreTunnelPayload | None = ...,
        name: str | None = ...,
        interface: str | None = ...,
        ip_version: Literal["4", "6"] | None = ...,
        remote_gw6: str | None = ...,
        local_gw6: str | None = ...,
        remote_gw: str | None = ...,
        local_gw: str | None = ...,
        use_sdwan: Literal["disable", "enable"] | None = ...,
        sequence_number_transmission: Literal["disable", "enable"] | None = ...,
        sequence_number_reception: Literal["disable", "enable"] | None = ...,
        checksum_transmission: Literal["disable", "enable"] | None = ...,
        checksum_reception: Literal["disable", "enable"] | None = ...,
        key_outbound: int | None = ...,
        key_inbound: int | None = ...,
        dscp_copying: Literal["disable", "enable"] | None = ...,
        diffservcode: str | None = ...,
        keepalive_interval: int | None = ...,
        keepalive_failtimes: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def post(
        self,
        payload_dict: GreTunnelPayload | None = ...,
        name: str | None = ...,
        interface: str | None = ...,
        ip_version: Literal["4", "6"] | None = ...,
        remote_gw6: str | None = ...,
        local_gw6: str | None = ...,
        remote_gw: str | None = ...,
        local_gw: str | None = ...,
        use_sdwan: Literal["disable", "enable"] | None = ...,
        sequence_number_transmission: Literal["disable", "enable"] | None = ...,
        sequence_number_reception: Literal["disable", "enable"] | None = ...,
        checksum_transmission: Literal["disable", "enable"] | None = ...,
        checksum_reception: Literal["disable", "enable"] | None = ...,
        key_outbound: int | None = ...,
        key_inbound: int | None = ...,
        dscp_copying: Literal["disable", "enable"] | None = ...,
        diffservcode: str | None = ...,
        keepalive_interval: int | None = ...,
        keepalive_failtimes: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: GreTunnelPayload | None = ...,
        name: str | None = ...,
        interface: str | None = ...,
        ip_version: Literal["4", "6"] | None = ...,
        remote_gw6: str | None = ...,
        local_gw6: str | None = ...,
        remote_gw: str | None = ...,
        local_gw: str | None = ...,
        use_sdwan: Literal["disable", "enable"] | None = ...,
        sequence_number_transmission: Literal["disable", "enable"] | None = ...,
        sequence_number_reception: Literal["disable", "enable"] | None = ...,
        checksum_transmission: Literal["disable", "enable"] | None = ...,
        checksum_reception: Literal["disable", "enable"] | None = ...,
        key_outbound: int | None = ...,
        key_inbound: int | None = ...,
        dscp_copying: Literal["disable", "enable"] | None = ...,
        diffservcode: str | None = ...,
        keepalive_interval: int | None = ...,
        keepalive_failtimes: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> GreTunnelObject: ...
    
    @overload
    def put(
        self,
        payload_dict: GreTunnelPayload | None = ...,
        name: str | None = ...,
        interface: str | None = ...,
        ip_version: Literal["4", "6"] | None = ...,
        remote_gw6: str | None = ...,
        local_gw6: str | None = ...,
        remote_gw: str | None = ...,
        local_gw: str | None = ...,
        use_sdwan: Literal["disable", "enable"] | None = ...,
        sequence_number_transmission: Literal["disable", "enable"] | None = ...,
        sequence_number_reception: Literal["disable", "enable"] | None = ...,
        checksum_transmission: Literal["disable", "enable"] | None = ...,
        checksum_reception: Literal["disable", "enable"] | None = ...,
        key_outbound: int | None = ...,
        key_inbound: int | None = ...,
        dscp_copying: Literal["disable", "enable"] | None = ...,
        diffservcode: str | None = ...,
        keepalive_interval: int | None = ...,
        keepalive_failtimes: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: GreTunnelPayload | None = ...,
        name: str | None = ...,
        interface: str | None = ...,
        ip_version: Literal["4", "6"] | None = ...,
        remote_gw6: str | None = ...,
        local_gw6: str | None = ...,
        remote_gw: str | None = ...,
        local_gw: str | None = ...,
        use_sdwan: Literal["disable", "enable"] | None = ...,
        sequence_number_transmission: Literal["disable", "enable"] | None = ...,
        sequence_number_reception: Literal["disable", "enable"] | None = ...,
        checksum_transmission: Literal["disable", "enable"] | None = ...,
        checksum_reception: Literal["disable", "enable"] | None = ...,
        key_outbound: int | None = ...,
        key_inbound: int | None = ...,
        dscp_copying: Literal["disable", "enable"] | None = ...,
        diffservcode: str | None = ...,
        keepalive_interval: int | None = ...,
        keepalive_failtimes: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def put(
        self,
        payload_dict: GreTunnelPayload | None = ...,
        name: str | None = ...,
        interface: str | None = ...,
        ip_version: Literal["4", "6"] | None = ...,
        remote_gw6: str | None = ...,
        local_gw6: str | None = ...,
        remote_gw: str | None = ...,
        local_gw: str | None = ...,
        use_sdwan: Literal["disable", "enable"] | None = ...,
        sequence_number_transmission: Literal["disable", "enable"] | None = ...,
        sequence_number_reception: Literal["disable", "enable"] | None = ...,
        checksum_transmission: Literal["disable", "enable"] | None = ...,
        checksum_reception: Literal["disable", "enable"] | None = ...,
        key_outbound: int | None = ...,
        key_inbound: int | None = ...,
        dscp_copying: Literal["disable", "enable"] | None = ...,
        diffservcode: str | None = ...,
        keepalive_interval: int | None = ...,
        keepalive_failtimes: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> GreTunnelObject: ...
    
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
        payload_dict: GreTunnelPayload | None = ...,
        name: str | None = ...,
        interface: str | None = ...,
        ip_version: Literal["4", "6"] | None = ...,
        remote_gw6: str | None = ...,
        local_gw6: str | None = ...,
        remote_gw: str | None = ...,
        local_gw: str | None = ...,
        use_sdwan: Literal["disable", "enable"] | None = ...,
        sequence_number_transmission: Literal["disable", "enable"] | None = ...,
        sequence_number_reception: Literal["disable", "enable"] | None = ...,
        checksum_transmission: Literal["disable", "enable"] | None = ...,
        checksum_reception: Literal["disable", "enable"] | None = ...,
        key_outbound: int | None = ...,
        key_inbound: int | None = ...,
        dscp_copying: Literal["disable", "enable"] | None = ...,
        diffservcode: str | None = ...,
        keepalive_interval: int | None = ...,
        keepalive_failtimes: int | None = ...,
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
    "GreTunnel",
    "GreTunnelPayload",
    "GreTunnelResponse",
    "GreTunnelObject",
]