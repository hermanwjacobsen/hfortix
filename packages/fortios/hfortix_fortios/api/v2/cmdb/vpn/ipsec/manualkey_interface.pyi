from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList
from hfortix_core.types import MutationResponse

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class ManualkeyInterfacePayload(TypedDict, total=False):
    """
    Type hints for vpn/ipsec/manualkey_interface payload fields.
    
    Configure IPsec manual keys.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.system.interface.InterfaceEndpoint` (via: interface)

    **Usage:**
        payload: ManualkeyInterfacePayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # IPsec tunnel name. | MaxLen: 15
    interface: str  # Name of the physical, aggregate, or VLAN interface | MaxLen: 15
    ip_version: Literal["4", "6"]  # IP version to use for VPN interface. | Default: 4
    addr_type: Literal["4", "6"]  # IP version to use for IP packets. | Default: 4
    remote_gw: str  # IPv4 address of the remote gateway's external inte | Default: 0.0.0.0
    remote_gw6: str  # Remote IPv6 address of VPN gateway. | Default: ::
    local_gw: str  # IPv4 address of the local gateway's external inter | Default: 0.0.0.0
    local_gw6: str  # Local IPv6 address of VPN gateway. | Default: ::
    auth_alg: Literal["null", "md5", "sha1", "sha256", "sha384", "sha512"]  # Authentication algorithm. Must be the same for bot | Default: null
    enc_alg: Literal["null", "des", "3des", "aes128", "aes192", "aes256", "aria128", "aria192", "aria256", "seed"]  # Encryption algorithm. Must be the same for both en | Default: null
    auth_key: str  # Hexadecimal authentication key in 16-digit
    enc_key: str  # Hexadecimal encryption key in 16-digit (8-byte) se
    local_spi: str  # Local SPI, a hexadecimal 8-digit (4-byte) tag. Dis
    remote_spi: str  # Remote SPI, a hexadecimal 8-digit (4-byte) tag. Di
    npu_offload: Literal["enable", "disable"]  # Enable/disable offloading IPsec VPN manual key ses | Default: enable

# Nested TypedDicts for table field children (dict mode)

# Nested classes for table field children (object mode)


# Response TypedDict for GET returns (all fields present in API response)
class ManualkeyInterfaceResponse(TypedDict):
    """
    Type hints for vpn/ipsec/manualkey_interface API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str  # IPsec tunnel name. | MaxLen: 15
    interface: str  # Name of the physical, aggregate, or VLAN interface | MaxLen: 15
    ip_version: Literal["4", "6"]  # IP version to use for VPN interface. | Default: 4
    addr_type: Literal["4", "6"]  # IP version to use for IP packets. | Default: 4
    remote_gw: str  # IPv4 address of the remote gateway's external inte | Default: 0.0.0.0
    remote_gw6: str  # Remote IPv6 address of VPN gateway. | Default: ::
    local_gw: str  # IPv4 address of the local gateway's external inter | Default: 0.0.0.0
    local_gw6: str  # Local IPv6 address of VPN gateway. | Default: ::
    auth_alg: Literal["null", "md5", "sha1", "sha256", "sha384", "sha512"]  # Authentication algorithm. Must be the same for bot | Default: null
    enc_alg: Literal["null", "des", "3des", "aes128", "aes192", "aes256", "aria128", "aria192", "aria256", "seed"]  # Encryption algorithm. Must be the same for both en | Default: null
    auth_key: str  # Hexadecimal authentication key in 16-digit
    enc_key: str  # Hexadecimal encryption key in 16-digit (8-byte) se
    local_spi: str  # Local SPI, a hexadecimal 8-digit (4-byte) tag. Dis
    remote_spi: str  # Remote SPI, a hexadecimal 8-digit (4-byte) tag. Di
    npu_offload: Literal["enable", "disable"]  # Enable/disable offloading IPsec VPN manual key ses | Default: enable


@final
class ManualkeyInterfaceObject:
    """Typed FortiObject for vpn/ipsec/manualkey_interface with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # IPsec tunnel name. | MaxLen: 15
    name: str
    # Name of the physical, aggregate, or VLAN interface. | MaxLen: 15
    interface: str
    # IP version to use for VPN interface. | Default: 4
    ip_version: Literal["4", "6"]
    # IP version to use for IP packets. | Default: 4
    addr_type: Literal["4", "6"]
    # IPv4 address of the remote gateway's external interface. | Default: 0.0.0.0
    remote_gw: str
    # Remote IPv6 address of VPN gateway. | Default: ::
    remote_gw6: str
    # IPv4 address of the local gateway's external interface. | Default: 0.0.0.0
    local_gw: str
    # Local IPv6 address of VPN gateway. | Default: ::
    local_gw6: str
    # Authentication algorithm. Must be the same for both ends of | Default: null
    auth_alg: Literal["null", "md5", "sha1", "sha256", "sha384", "sha512"]
    # Encryption algorithm. Must be the same for both ends of the | Default: null
    enc_alg: Literal["null", "des", "3des", "aes128", "aes192", "aes256", "aria128", "aria192", "aria256", "seed"]
    # Hexadecimal authentication key in 16-digit (8-byte) segments
    auth_key: str
    # Hexadecimal encryption key in 16-digit (8-byte) segments sep
    enc_key: str
    # Local SPI, a hexadecimal 8-digit (4-byte) tag. Discerns betw
    local_spi: str
    # Remote SPI, a hexadecimal 8-digit (4-byte) tag. Discerns bet
    remote_spi: str
    # Enable/disable offloading IPsec VPN manual key sessions to N | Default: enable
    npu_offload: Literal["enable", "disable"]
    
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
    def to_dict(self) -> ManualkeyInterfacePayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class ManualkeyInterface:
    """
    Configure IPsec manual keys.
    
    Path: vpn/ipsec/manualkey_interface
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
    ) -> ManualkeyInterfaceObject: ...
    
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
    ) -> ManualkeyInterfaceObject: ...
    
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
    ) -> FortiObjectList[ManualkeyInterfaceObject]: ...
    
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
    ) -> ManualkeyInterfaceObject: ...
    
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
    ) -> ManualkeyInterfaceObject: ...
    
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
    ) -> FortiObjectList[ManualkeyInterfaceObject]: ...
    
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
    ) -> ManualkeyInterfaceObject: ...
    
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
    ) -> ManualkeyInterfaceObject: ...
    
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
    ) -> FortiObjectList[ManualkeyInterfaceObject]: ...
    
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
    ) -> ManualkeyInterfaceObject | list[ManualkeyInterfaceObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: ManualkeyInterfacePayload | None = ...,
        name: str | None = ...,
        interface: str | None = ...,
        ip_version: Literal["4", "6"] | None = ...,
        addr_type: Literal["4", "6"] | None = ...,
        remote_gw: str | None = ...,
        remote_gw6: str | None = ...,
        local_gw: str | None = ...,
        local_gw6: str | None = ...,
        auth_alg: Literal["null", "md5", "sha1", "sha256", "sha384", "sha512"] | None = ...,
        enc_alg: Literal["null", "des", "3des", "aes128", "aes192", "aes256", "aria128", "aria192", "aria256", "seed"] | None = ...,
        auth_key: str | None = ...,
        enc_key: str | None = ...,
        local_spi: str | None = ...,
        remote_spi: str | None = ...,
        npu_offload: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> ManualkeyInterfaceObject: ...
    
    @overload
    def post(
        self,
        payload_dict: ManualkeyInterfacePayload | None = ...,
        name: str | None = ...,
        interface: str | None = ...,
        ip_version: Literal["4", "6"] | None = ...,
        addr_type: Literal["4", "6"] | None = ...,
        remote_gw: str | None = ...,
        remote_gw6: str | None = ...,
        local_gw: str | None = ...,
        local_gw6: str | None = ...,
        auth_alg: Literal["null", "md5", "sha1", "sha256", "sha384", "sha512"] | None = ...,
        enc_alg: Literal["null", "des", "3des", "aes128", "aes192", "aes256", "aria128", "aria192", "aria256", "seed"] | None = ...,
        auth_key: str | None = ...,
        enc_key: str | None = ...,
        local_spi: str | None = ...,
        remote_spi: str | None = ...,
        npu_offload: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: ManualkeyInterfacePayload | None = ...,
        name: str | None = ...,
        interface: str | None = ...,
        ip_version: Literal["4", "6"] | None = ...,
        addr_type: Literal["4", "6"] | None = ...,
        remote_gw: str | None = ...,
        remote_gw6: str | None = ...,
        local_gw: str | None = ...,
        local_gw6: str | None = ...,
        auth_alg: Literal["null", "md5", "sha1", "sha256", "sha384", "sha512"] | None = ...,
        enc_alg: Literal["null", "des", "3des", "aes128", "aes192", "aes256", "aria128", "aria192", "aria256", "seed"] | None = ...,
        auth_key: str | None = ...,
        enc_key: str | None = ...,
        local_spi: str | None = ...,
        remote_spi: str | None = ...,
        npu_offload: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def post(
        self,
        payload_dict: ManualkeyInterfacePayload | None = ...,
        name: str | None = ...,
        interface: str | None = ...,
        ip_version: Literal["4", "6"] | None = ...,
        addr_type: Literal["4", "6"] | None = ...,
        remote_gw: str | None = ...,
        remote_gw6: str | None = ...,
        local_gw: str | None = ...,
        local_gw6: str | None = ...,
        auth_alg: Literal["null", "md5", "sha1", "sha256", "sha384", "sha512"] | None = ...,
        enc_alg: Literal["null", "des", "3des", "aes128", "aes192", "aes256", "aria128", "aria192", "aria256", "seed"] | None = ...,
        auth_key: str | None = ...,
        enc_key: str | None = ...,
        local_spi: str | None = ...,
        remote_spi: str | None = ...,
        npu_offload: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: ManualkeyInterfacePayload | None = ...,
        name: str | None = ...,
        interface: str | None = ...,
        ip_version: Literal["4", "6"] | None = ...,
        addr_type: Literal["4", "6"] | None = ...,
        remote_gw: str | None = ...,
        remote_gw6: str | None = ...,
        local_gw: str | None = ...,
        local_gw6: str | None = ...,
        auth_alg: Literal["null", "md5", "sha1", "sha256", "sha384", "sha512"] | None = ...,
        enc_alg: Literal["null", "des", "3des", "aes128", "aes192", "aes256", "aria128", "aria192", "aria256", "seed"] | None = ...,
        auth_key: str | None = ...,
        enc_key: str | None = ...,
        local_spi: str | None = ...,
        remote_spi: str | None = ...,
        npu_offload: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> ManualkeyInterfaceObject: ...
    
    @overload
    def put(
        self,
        payload_dict: ManualkeyInterfacePayload | None = ...,
        name: str | None = ...,
        interface: str | None = ...,
        ip_version: Literal["4", "6"] | None = ...,
        addr_type: Literal["4", "6"] | None = ...,
        remote_gw: str | None = ...,
        remote_gw6: str | None = ...,
        local_gw: str | None = ...,
        local_gw6: str | None = ...,
        auth_alg: Literal["null", "md5", "sha1", "sha256", "sha384", "sha512"] | None = ...,
        enc_alg: Literal["null", "des", "3des", "aes128", "aes192", "aes256", "aria128", "aria192", "aria256", "seed"] | None = ...,
        auth_key: str | None = ...,
        enc_key: str | None = ...,
        local_spi: str | None = ...,
        remote_spi: str | None = ...,
        npu_offload: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: ManualkeyInterfacePayload | None = ...,
        name: str | None = ...,
        interface: str | None = ...,
        ip_version: Literal["4", "6"] | None = ...,
        addr_type: Literal["4", "6"] | None = ...,
        remote_gw: str | None = ...,
        remote_gw6: str | None = ...,
        local_gw: str | None = ...,
        local_gw6: str | None = ...,
        auth_alg: Literal["null", "md5", "sha1", "sha256", "sha384", "sha512"] | None = ...,
        enc_alg: Literal["null", "des", "3des", "aes128", "aes192", "aes256", "aria128", "aria192", "aria256", "seed"] | None = ...,
        auth_key: str | None = ...,
        enc_key: str | None = ...,
        local_spi: str | None = ...,
        remote_spi: str | None = ...,
        npu_offload: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def put(
        self,
        payload_dict: ManualkeyInterfacePayload | None = ...,
        name: str | None = ...,
        interface: str | None = ...,
        ip_version: Literal["4", "6"] | None = ...,
        addr_type: Literal["4", "6"] | None = ...,
        remote_gw: str | None = ...,
        remote_gw6: str | None = ...,
        local_gw: str | None = ...,
        local_gw6: str | None = ...,
        auth_alg: Literal["null", "md5", "sha1", "sha256", "sha384", "sha512"] | None = ...,
        enc_alg: Literal["null", "des", "3des", "aes128", "aes192", "aes256", "aria128", "aria192", "aria256", "seed"] | None = ...,
        auth_key: str | None = ...,
        enc_key: str | None = ...,
        local_spi: str | None = ...,
        remote_spi: str | None = ...,
        npu_offload: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> ManualkeyInterfaceObject: ...
    
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
        payload_dict: ManualkeyInterfacePayload | None = ...,
        name: str | None = ...,
        interface: str | None = ...,
        ip_version: Literal["4", "6"] | None = ...,
        addr_type: Literal["4", "6"] | None = ...,
        remote_gw: str | None = ...,
        remote_gw6: str | None = ...,
        local_gw: str | None = ...,
        local_gw6: str | None = ...,
        auth_alg: Literal["null", "md5", "sha1", "sha256", "sha384", "sha512"] | None = ...,
        enc_alg: Literal["null", "des", "3des", "aes128", "aes192", "aes256", "aria128", "aria192", "aria256", "seed"] | None = ...,
        auth_key: str | None = ...,
        enc_key: str | None = ...,
        local_spi: str | None = ...,
        remote_spi: str | None = ...,
        npu_offload: Literal["enable", "disable"] | None = ...,
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
    "ManualkeyInterface",
    "ManualkeyInterfacePayload",
    "ManualkeyInterfaceResponse",
    "ManualkeyInterfaceObject",
]