from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject
from hfortix_core.types import MutationResponse, RawAPIResponse

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class VneInterfacePayload(TypedDict, total=False):
    """
    Type hints for system/vne_interface payload fields.
    
    Configure virtual network enabler tunnels.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.certificate.local.LocalEndpoint` (via: ssl-certificate)
        - :class:`~.system.interface.InterfaceEndpoint` (via: interface)

    **Usage:**
        payload: VneInterfacePayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # VNE tunnel name. | MaxLen: 15
    interface: str  # Interface name. | MaxLen: 15
    ssl_certificate: str  # Name of local certificate for SSL connections. | Default: Fortinet_Factory | MaxLen: 35
    bmr_hostname: str  # BMR hostname. | MaxLen: 128
    auto_asic_offload: Literal["enable", "disable"]  # Enable/disable tunnel ASIC offloading. | Default: enable
    ipv4_address: str  # Tunnel IPv4 address and netmask. | Default: 0.0.0.0 0.0.0.0
    br: str  # IPv6 address or FQDN of the border relay. | MaxLen: 255
    update_url: str  # URL of provisioning server. | MaxLen: 511
    mode: Literal["map-e", "fixed-ip", "ds-lite"]  # VNE tunnel mode. | Default: map-e
    http_username: str  # HTTP authentication user name. | MaxLen: 64
    http_password: str  # HTTP authentication password. | MaxLen: 128

# Nested TypedDicts for table field children (dict mode)

# Nested classes for table field children (object mode)


# Response TypedDict for GET returns (all fields present in API response)
class VneInterfaceResponse(TypedDict):
    """
    Type hints for system/vne_interface API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str  # VNE tunnel name. | MaxLen: 15
    interface: str  # Interface name. | MaxLen: 15
    ssl_certificate: str  # Name of local certificate for SSL connections. | Default: Fortinet_Factory | MaxLen: 35
    bmr_hostname: str  # BMR hostname. | MaxLen: 128
    auto_asic_offload: Literal["enable", "disable"]  # Enable/disable tunnel ASIC offloading. | Default: enable
    ipv4_address: str  # Tunnel IPv4 address and netmask. | Default: 0.0.0.0 0.0.0.0
    br: str  # IPv6 address or FQDN of the border relay. | MaxLen: 255
    update_url: str  # URL of provisioning server. | MaxLen: 511
    mode: Literal["map-e", "fixed-ip", "ds-lite"]  # VNE tunnel mode. | Default: map-e
    http_username: str  # HTTP authentication user name. | MaxLen: 64
    http_password: str  # HTTP authentication password. | MaxLen: 128


@final
class VneInterfaceObject:
    """Typed FortiObject for system/vne_interface with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # VNE tunnel name. | MaxLen: 15
    name: str
    # Interface name. | MaxLen: 15
    interface: str
    # Name of local certificate for SSL connections. | Default: Fortinet_Factory | MaxLen: 35
    ssl_certificate: str
    # BMR hostname. | MaxLen: 128
    bmr_hostname: str
    # Enable/disable tunnel ASIC offloading. | Default: enable
    auto_asic_offload: Literal["enable", "disable"]
    # Tunnel IPv4 address and netmask. | Default: 0.0.0.0 0.0.0.0
    ipv4_address: str
    # IPv6 address or FQDN of the border relay. | MaxLen: 255
    br: str
    # URL of provisioning server. | MaxLen: 511
    update_url: str
    # VNE tunnel mode. | Default: map-e
    mode: Literal["map-e", "fixed-ip", "ds-lite"]
    # HTTP authentication user name. | MaxLen: 64
    http_username: str
    # HTTP authentication password. | MaxLen: 128
    http_password: str
    
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
    def to_dict(self) -> VneInterfacePayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class VneInterface:
    """
    Configure virtual network enabler tunnels.
    
    Path: system/vne_interface
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
    ) -> VneInterfaceObject: ...
    
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
    ) -> VneInterfaceObject: ...
    
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
    ) -> list[VneInterfaceObject]: ...
    
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
        raw_json: Literal[False] = ...,
        *,
        **kwargs: Any,
    ) -> VneInterfaceObject: ...
    
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
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> VneInterfaceObject: ...
    
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
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> list[VneInterfaceObject]: ...
    
    # raw_json=True returns the full API envelope
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
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> RawAPIResponse: ...
    
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
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> VneInterfaceObject: ...
    
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
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> VneInterfaceObject: ...
    
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
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> list[VneInterfaceObject]: ...
    
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
        raw_json: bool = ...,
        **kwargs: Any,
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
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> VneInterfaceObject | list[VneInterfaceObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: VneInterfacePayload | None = ...,
        name: str | None = ...,
        interface: str | None = ...,
        ssl_certificate: str | None = ...,
        bmr_hostname: str | None = ...,
        auto_asic_offload: Literal["enable", "disable"] | None = ...,
        ipv4_address: str | None = ...,
        br: str | None = ...,
        update_url: str | None = ...,
        mode: Literal["map-e", "fixed-ip", "ds-lite"] | None = ...,
        http_username: str | None = ...,
        http_password: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> VneInterfaceObject: ...
    
    @overload
    def post(
        self,
        payload_dict: VneInterfacePayload | None = ...,
        name: str | None = ...,
        interface: str | None = ...,
        ssl_certificate: str | None = ...,
        bmr_hostname: str | None = ...,
        auto_asic_offload: Literal["enable", "disable"] | None = ...,
        ipv4_address: str | None = ...,
        br: str | None = ...,
        update_url: str | None = ...,
        mode: Literal["map-e", "fixed-ip", "ds-lite"] | None = ...,
        http_username: str | None = ...,
        http_password: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    # raw_json=True returns the full API envelope
    @overload
    def post(
        self,
        payload_dict: VneInterfacePayload | None = ...,
        name: str | None = ...,
        interface: str | None = ...,
        ssl_certificate: str | None = ...,
        bmr_hostname: str | None = ...,
        auto_asic_offload: Literal["enable", "disable"] | None = ...,
        ipv4_address: str | None = ...,
        br: str | None = ...,
        update_url: str | None = ...,
        mode: Literal["map-e", "fixed-ip", "ds-lite"] | None = ...,
        http_username: str | None = ...,
        http_password: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> RawAPIResponse: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: VneInterfacePayload | None = ...,
        name: str | None = ...,
        interface: str | None = ...,
        ssl_certificate: str | None = ...,
        bmr_hostname: str | None = ...,
        auto_asic_offload: Literal["enable", "disable"] | None = ...,
        ipv4_address: str | None = ...,
        br: str | None = ...,
        update_url: str | None = ...,
        mode: Literal["map-e", "fixed-ip", "ds-lite"] | None = ...,
        http_username: str | None = ...,
        http_password: str | None = ...,
        vdom: str | bool | None = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    def post(
        self,
        payload_dict: VneInterfacePayload | None = ...,
        name: str | None = ...,
        interface: str | None = ...,
        ssl_certificate: str | None = ...,
        bmr_hostname: str | None = ...,
        auto_asic_offload: Literal["enable", "disable"] | None = ...,
        ipv4_address: str | None = ...,
        br: str | None = ...,
        update_url: str | None = ...,
        mode: Literal["map-e", "fixed-ip", "ds-lite"] | None = ...,
        http_username: str | None = ...,
        http_password: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: VneInterfacePayload | None = ...,
        name: str | None = ...,
        interface: str | None = ...,
        ssl_certificate: str | None = ...,
        bmr_hostname: str | None = ...,
        auto_asic_offload: Literal["enable", "disable"] | None = ...,
        ipv4_address: str | None = ...,
        br: str | None = ...,
        update_url: str | None = ...,
        mode: Literal["map-e", "fixed-ip", "ds-lite"] | None = ...,
        http_username: str | None = ...,
        http_password: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> VneInterfaceObject: ...
    
    @overload
    def put(
        self,
        payload_dict: VneInterfacePayload | None = ...,
        name: str | None = ...,
        interface: str | None = ...,
        ssl_certificate: str | None = ...,
        bmr_hostname: str | None = ...,
        auto_asic_offload: Literal["enable", "disable"] | None = ...,
        ipv4_address: str | None = ...,
        br: str | None = ...,
        update_url: str | None = ...,
        mode: Literal["map-e", "fixed-ip", "ds-lite"] | None = ...,
        http_username: str | None = ...,
        http_password: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    # raw_json=True returns the full API envelope
    @overload
    def put(
        self,
        payload_dict: VneInterfacePayload | None = ...,
        name: str | None = ...,
        interface: str | None = ...,
        ssl_certificate: str | None = ...,
        bmr_hostname: str | None = ...,
        auto_asic_offload: Literal["enable", "disable"] | None = ...,
        ipv4_address: str | None = ...,
        br: str | None = ...,
        update_url: str | None = ...,
        mode: Literal["map-e", "fixed-ip", "ds-lite"] | None = ...,
        http_username: str | None = ...,
        http_password: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> RawAPIResponse: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: VneInterfacePayload | None = ...,
        name: str | None = ...,
        interface: str | None = ...,
        ssl_certificate: str | None = ...,
        bmr_hostname: str | None = ...,
        auto_asic_offload: Literal["enable", "disable"] | None = ...,
        ipv4_address: str | None = ...,
        br: str | None = ...,
        update_url: str | None = ...,
        mode: Literal["map-e", "fixed-ip", "ds-lite"] | None = ...,
        http_username: str | None = ...,
        http_password: str | None = ...,
        vdom: str | bool | None = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    def put(
        self,
        payload_dict: VneInterfacePayload | None = ...,
        name: str | None = ...,
        interface: str | None = ...,
        ssl_certificate: str | None = ...,
        bmr_hostname: str | None = ...,
        auto_asic_offload: Literal["enable", "disable"] | None = ...,
        ipv4_address: str | None = ...,
        br: str | None = ...,
        update_url: str | None = ...,
        mode: Literal["map-e", "fixed-ip", "ds-lite"] | None = ...,
        http_username: str | None = ...,
        http_password: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> VneInterfaceObject: ...
    
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    # raw_json=True returns the full API envelope
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> RawAPIResponse: ...
    
    # Default overload
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: VneInterfacePayload | None = ...,
        name: str | None = ...,
        interface: str | None = ...,
        ssl_certificate: str | None = ...,
        bmr_hostname: str | None = ...,
        auto_asic_offload: Literal["enable", "disable"] | None = ...,
        ipv4_address: str | None = ...,
        br: str | None = ...,
        update_url: str | None = ...,
        mode: Literal["map-e", "fixed-ip", "ds-lite"] | None = ...,
        http_username: str | None = ...,
        http_password: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
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
    "VneInterface",
    "VneInterfacePayload",
    "VneInterfaceResponse",
    "VneInterfaceObject",
]