from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList
from hfortix_core.types import MutationResponse

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class MobileTunnelPayload(TypedDict, total=False):
    """
    Type hints for system/mobile_tunnel payload fields.
    
    Configure Mobile tunnels, an implementation of Network Mobility (NEMO) extensions for Mobile IPv4 RFC5177.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.system.interface.InterfaceEndpoint` (via: roaming-interface)

    **Usage:**
        payload: MobileTunnelPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # Tunnel name. | MaxLen: 15
    status: Literal["disable", "enable"]  # Enable/disable this mobile tunnel. | Default: enable
    roaming_interface: str  # Select the associated interface name from availabl | MaxLen: 15
    home_agent: str  # IPv4 address of the NEMO HA | Default: 0.0.0.0
    home_address: str  # Home IP address (Format: xxx.xxx.xxx.xxx). | Default: 0.0.0.0
    renew_interval: int  # Time before lifetime expiration to send NMMO HA re | Default: 60 | Min: 5 | Max: 60
    lifetime: int  # NMMO HA registration request lifetime | Default: 65535 | Min: 180 | Max: 65535
    reg_interval: int  # NMMO HA registration interval | Default: 5 | Min: 5 | Max: 300
    reg_retry: int  # Maximum number of NMMO HA registration retries | Default: 3 | Min: 1 | Max: 30
    n_mhae_spi: int  # NEMO authentication SPI (default: 256). | Default: 256 | Min: 0 | Max: 4294967295
    n_mhae_key_type: Literal["ascii", "base64"]  # NEMO authentication key type (ASCII or base64). | Default: ascii
    n_mhae_key: str  # NEMO authentication key.
    hash_algorithm: Literal["hmac-md5"]  # Hash Algorithm (Keyed MD5). | Default: hmac-md5
    tunnel_mode: Literal["gre"]  # NEMO tunnel mode (GRE tunnel). | Default: gre
    network: list[dict[str, Any]]  # NEMO network configuration.

# Nested TypedDicts for table field children (dict mode)

class MobileTunnelNetworkItem(TypedDict):
    """Type hints for network table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    id: int  # Network entry ID. | Default: 0 | Min: 0 | Max: 4294967295
    interface: str  # Select the associated interface name from availabl | MaxLen: 15
    prefix: str  # Class IP and Netmask with correction | Default: 0.0.0.0 0.0.0.0


# Nested classes for table field children (object mode)

@final
class MobileTunnelNetworkObject:
    """Typed object for network table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Network entry ID. | Default: 0 | Min: 0 | Max: 4294967295
    id: int
    # Select the associated interface name from available options. | MaxLen: 15
    interface: str
    # Class IP and Netmask with correction | Default: 0.0.0.0 0.0.0.0
    prefix: str
    
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
class MobileTunnelResponse(TypedDict):
    """
    Type hints for system/mobile_tunnel API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str  # Tunnel name. | MaxLen: 15
    status: Literal["disable", "enable"]  # Enable/disable this mobile tunnel. | Default: enable
    roaming_interface: str  # Select the associated interface name from availabl | MaxLen: 15
    home_agent: str  # IPv4 address of the NEMO HA | Default: 0.0.0.0
    home_address: str  # Home IP address (Format: xxx.xxx.xxx.xxx). | Default: 0.0.0.0
    renew_interval: int  # Time before lifetime expiration to send NMMO HA re | Default: 60 | Min: 5 | Max: 60
    lifetime: int  # NMMO HA registration request lifetime | Default: 65535 | Min: 180 | Max: 65535
    reg_interval: int  # NMMO HA registration interval | Default: 5 | Min: 5 | Max: 300
    reg_retry: int  # Maximum number of NMMO HA registration retries | Default: 3 | Min: 1 | Max: 30
    n_mhae_spi: int  # NEMO authentication SPI (default: 256). | Default: 256 | Min: 0 | Max: 4294967295
    n_mhae_key_type: Literal["ascii", "base64"]  # NEMO authentication key type (ASCII or base64). | Default: ascii
    n_mhae_key: str  # NEMO authentication key.
    hash_algorithm: Literal["hmac-md5"]  # Hash Algorithm (Keyed MD5). | Default: hmac-md5
    tunnel_mode: Literal["gre"]  # NEMO tunnel mode (GRE tunnel). | Default: gre
    network: list[MobileTunnelNetworkItem]  # NEMO network configuration.


@final
class MobileTunnelObject:
    """Typed FortiObject for system/mobile_tunnel with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Tunnel name. | MaxLen: 15
    name: str
    # Enable/disable this mobile tunnel. | Default: enable
    status: Literal["disable", "enable"]
    # Select the associated interface name from available options. | MaxLen: 15
    roaming_interface: str
    # IPv4 address of the NEMO HA (Format: xxx.xxx.xxx.xxx). | Default: 0.0.0.0
    home_agent: str
    # Home IP address (Format: xxx.xxx.xxx.xxx). | Default: 0.0.0.0
    home_address: str
    # Time before lifetime expiration to send NMMO HA re-registrat | Default: 60 | Min: 5 | Max: 60
    renew_interval: int
    # NMMO HA registration request lifetime | Default: 65535 | Min: 180 | Max: 65535
    lifetime: int
    # NMMO HA registration interval (5 - 300, default = 5). | Default: 5 | Min: 5 | Max: 300
    reg_interval: int
    # Maximum number of NMMO HA registration retries | Default: 3 | Min: 1 | Max: 30
    reg_retry: int
    # NEMO authentication SPI (default: 256). | Default: 256 | Min: 0 | Max: 4294967295
    n_mhae_spi: int
    # NEMO authentication key type (ASCII or base64). | Default: ascii
    n_mhae_key_type: Literal["ascii", "base64"]
    # NEMO authentication key.
    n_mhae_key: str
    # Hash Algorithm (Keyed MD5). | Default: hmac-md5
    hash_algorithm: Literal["hmac-md5"]
    # NEMO tunnel mode (GRE tunnel). | Default: gre
    tunnel_mode: Literal["gre"]
    # NEMO network configuration.
    network: list[MobileTunnelNetworkObject]
    
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
    def to_dict(self) -> MobileTunnelPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class MobileTunnel:
    """
    Configure Mobile tunnels, an implementation of Network Mobility (NEMO) extensions for Mobile IPv4 RFC5177.
    
    Path: system/mobile_tunnel
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
    ) -> MobileTunnelObject: ...
    
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
    ) -> MobileTunnelObject: ...
    
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
    ) -> FortiObjectList[MobileTunnelObject]: ...
    
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
    ) -> MobileTunnelObject: ...
    
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
    ) -> MobileTunnelObject: ...
    
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
    ) -> FortiObjectList[MobileTunnelObject]: ...
    
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
    ) -> MobileTunnelObject: ...
    
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
    ) -> MobileTunnelObject: ...
    
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
    ) -> FortiObjectList[MobileTunnelObject]: ...
    
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
    ) -> MobileTunnelObject | list[MobileTunnelObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: MobileTunnelPayload | None = ...,
        name: str | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        roaming_interface: str | None = ...,
        home_agent: str | None = ...,
        home_address: str | None = ...,
        renew_interval: int | None = ...,
        lifetime: int | None = ...,
        reg_interval: int | None = ...,
        reg_retry: int | None = ...,
        n_mhae_spi: int | None = ...,
        n_mhae_key_type: Literal["ascii", "base64"] | None = ...,
        n_mhae_key: str | None = ...,
        hash_algorithm: Literal["hmac-md5"] | None = ...,
        tunnel_mode: Literal["gre"] | None = ...,
        network: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MobileTunnelObject: ...
    
    @overload
    def post(
        self,
        payload_dict: MobileTunnelPayload | None = ...,
        name: str | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        roaming_interface: str | None = ...,
        home_agent: str | None = ...,
        home_address: str | None = ...,
        renew_interval: int | None = ...,
        lifetime: int | None = ...,
        reg_interval: int | None = ...,
        reg_retry: int | None = ...,
        n_mhae_spi: int | None = ...,
        n_mhae_key_type: Literal["ascii", "base64"] | None = ...,
        n_mhae_key: str | None = ...,
        hash_algorithm: Literal["hmac-md5"] | None = ...,
        tunnel_mode: Literal["gre"] | None = ...,
        network: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: MobileTunnelPayload | None = ...,
        name: str | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        roaming_interface: str | None = ...,
        home_agent: str | None = ...,
        home_address: str | None = ...,
        renew_interval: int | None = ...,
        lifetime: int | None = ...,
        reg_interval: int | None = ...,
        reg_retry: int | None = ...,
        n_mhae_spi: int | None = ...,
        n_mhae_key_type: Literal["ascii", "base64"] | None = ...,
        n_mhae_key: str | None = ...,
        hash_algorithm: Literal["hmac-md5"] | None = ...,
        tunnel_mode: Literal["gre"] | None = ...,
        network: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def post(
        self,
        payload_dict: MobileTunnelPayload | None = ...,
        name: str | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        roaming_interface: str | None = ...,
        home_agent: str | None = ...,
        home_address: str | None = ...,
        renew_interval: int | None = ...,
        lifetime: int | None = ...,
        reg_interval: int | None = ...,
        reg_retry: int | None = ...,
        n_mhae_spi: int | None = ...,
        n_mhae_key_type: Literal["ascii", "base64"] | None = ...,
        n_mhae_key: str | None = ...,
        hash_algorithm: Literal["hmac-md5"] | None = ...,
        tunnel_mode: Literal["gre"] | None = ...,
        network: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: MobileTunnelPayload | None = ...,
        name: str | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        roaming_interface: str | None = ...,
        home_agent: str | None = ...,
        home_address: str | None = ...,
        renew_interval: int | None = ...,
        lifetime: int | None = ...,
        reg_interval: int | None = ...,
        reg_retry: int | None = ...,
        n_mhae_spi: int | None = ...,
        n_mhae_key_type: Literal["ascii", "base64"] | None = ...,
        n_mhae_key: str | None = ...,
        hash_algorithm: Literal["hmac-md5"] | None = ...,
        tunnel_mode: Literal["gre"] | None = ...,
        network: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MobileTunnelObject: ...
    
    @overload
    def put(
        self,
        payload_dict: MobileTunnelPayload | None = ...,
        name: str | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        roaming_interface: str | None = ...,
        home_agent: str | None = ...,
        home_address: str | None = ...,
        renew_interval: int | None = ...,
        lifetime: int | None = ...,
        reg_interval: int | None = ...,
        reg_retry: int | None = ...,
        n_mhae_spi: int | None = ...,
        n_mhae_key_type: Literal["ascii", "base64"] | None = ...,
        n_mhae_key: str | None = ...,
        hash_algorithm: Literal["hmac-md5"] | None = ...,
        tunnel_mode: Literal["gre"] | None = ...,
        network: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: MobileTunnelPayload | None = ...,
        name: str | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        roaming_interface: str | None = ...,
        home_agent: str | None = ...,
        home_address: str | None = ...,
        renew_interval: int | None = ...,
        lifetime: int | None = ...,
        reg_interval: int | None = ...,
        reg_retry: int | None = ...,
        n_mhae_spi: int | None = ...,
        n_mhae_key_type: Literal["ascii", "base64"] | None = ...,
        n_mhae_key: str | None = ...,
        hash_algorithm: Literal["hmac-md5"] | None = ...,
        tunnel_mode: Literal["gre"] | None = ...,
        network: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def put(
        self,
        payload_dict: MobileTunnelPayload | None = ...,
        name: str | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        roaming_interface: str | None = ...,
        home_agent: str | None = ...,
        home_address: str | None = ...,
        renew_interval: int | None = ...,
        lifetime: int | None = ...,
        reg_interval: int | None = ...,
        reg_retry: int | None = ...,
        n_mhae_spi: int | None = ...,
        n_mhae_key_type: Literal["ascii", "base64"] | None = ...,
        n_mhae_key: str | None = ...,
        hash_algorithm: Literal["hmac-md5"] | None = ...,
        tunnel_mode: Literal["gre"] | None = ...,
        network: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> MobileTunnelObject: ...
    
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
        payload_dict: MobileTunnelPayload | None = ...,
        name: str | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        roaming_interface: str | None = ...,
        home_agent: str | None = ...,
        home_address: str | None = ...,
        renew_interval: int | None = ...,
        lifetime: int | None = ...,
        reg_interval: int | None = ...,
        reg_retry: int | None = ...,
        n_mhae_spi: int | None = ...,
        n_mhae_key_type: Literal["ascii", "base64"] | None = ...,
        n_mhae_key: str | None = ...,
        hash_algorithm: Literal["hmac-md5"] | None = ...,
        tunnel_mode: Literal["gre"] | None = ...,
        network: str | list[str] | list[dict[str, Any]] | None = ...,
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
    "MobileTunnel",
    "MobileTunnelPayload",
    "MobileTunnelResponse",
    "MobileTunnelObject",
]