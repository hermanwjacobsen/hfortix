from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList
from hfortix_core.types import MutationResponse

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class NtpPayload(TypedDict, total=False):
    """
    Type hints for system/ntp payload fields.
    
    Configure system NTP information.
    
    **Usage:**
        payload: NtpPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    ntpsync: Literal["enable", "disable"]  # Enable/disable setting the FortiGate system time b | Default: disable
    type: Literal["fortiguard", "custom"]  # Use the FortiGuard NTP server or any other availab | Default: fortiguard
    syncinterval: int  # NTP synchronization interval (1 - 1440 min). | Default: 60 | Min: 1 | Max: 1440
    ntpserver: list[dict[str, Any]]  # Configure the FortiGate to connect to any availabl
    source_ip: str  # Source IP address for communication to the NTP ser | Default: 0.0.0.0
    source_ip6: str  # Source IPv6 address for communication to the NTP s | Default: ::
    server_mode: Literal["enable", "disable"]  # Enable/disable FortiGate NTP Server Mode. Your For | Default: disable
    authentication: Literal["enable", "disable"]  # Enable/disable authentication. | Default: disable
    key_type: Literal["MD5", "SHA1", "SHA256"]  # Key type for authentication (MD5, SHA1, SHA256). | Default: MD5
    key: str  # Key for authentication. | MaxLen: 64
    key_id: int  # Key ID for authentication. | Default: 0 | Min: 0 | Max: 4294967295
    interface: list[dict[str, Any]]  # FortiGate interface(s) with NTP server mode enable

# Nested TypedDicts for table field children (dict mode)

class NtpNtpserverItem(TypedDict):
    """Type hints for ntpserver table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    id: int  # NTP server ID. | Default: 0 | Min: 0 | Max: 4294967295
    server: str  # IP address or hostname of the NTP Server. | MaxLen: 63
    ntpv3: Literal["enable", "disable"]  # Enable to use NTPv3 instead of NTPv4. | Default: disable
    authentication: Literal["enable", "disable"]  # Enable/disable authentication. | Default: disable
    key_type: Literal["MD5", "SHA1", "SHA256"]  # Select NTP authentication type. | Default: MD5
    key: str  # Key for MD5(NTPv3)/SHA1(NTPv4)/SHA256(NTPv4) authe | MaxLen: 64
    key_id: int  # Key ID for authentication. | Default: 0 | Min: 0 | Max: 4294967295
    ip_type: Literal["IPv6", "IPv4", "Both"]  # Choose to connect to IPv4 or/and IPv6 NTP server. | Default: Both
    interface_select_method: Literal["auto", "sdwan", "specify"]  # Specify how to select outgoing interface to reach | Default: auto
    interface: str  # Specify outgoing interface to reach server. | MaxLen: 15
    vrf_select: int  # VRF ID used for connection to server. | Default: 0 | Min: 0 | Max: 511


class NtpInterfaceItem(TypedDict):
    """Type hints for interface table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    interface_name: str  # Interface name. | MaxLen: 79


# Nested classes for table field children (object mode)

@final
class NtpNtpserverObject:
    """Typed object for ntpserver table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # NTP server ID. | Default: 0 | Min: 0 | Max: 4294967295
    id: int
    # IP address or hostname of the NTP Server. | MaxLen: 63
    server: str
    # Enable to use NTPv3 instead of NTPv4. | Default: disable
    ntpv3: Literal["enable", "disable"]
    # Enable/disable authentication. | Default: disable
    authentication: Literal["enable", "disable"]
    # Select NTP authentication type. | Default: MD5
    key_type: Literal["MD5", "SHA1", "SHA256"]
    # Key for MD5(NTPv3)/SHA1(NTPv4)/SHA256(NTPv4) authentication. | MaxLen: 64
    key: str
    # Key ID for authentication. | Default: 0 | Min: 0 | Max: 4294967295
    key_id: int
    # Choose to connect to IPv4 or/and IPv6 NTP server. | Default: Both
    ip_type: Literal["IPv6", "IPv4", "Both"]
    # Specify how to select outgoing interface to reach server. | Default: auto
    interface_select_method: Literal["auto", "sdwan", "specify"]
    # Specify outgoing interface to reach server. | MaxLen: 15
    interface: str
    # VRF ID used for connection to server. | Default: 0 | Min: 0 | Max: 511
    vrf_select: int
    
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
class NtpInterfaceObject:
    """Typed object for interface table items.
    
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
class NtpResponse(TypedDict):
    """
    Type hints for system/ntp API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    ntpsync: Literal["enable", "disable"]  # Enable/disable setting the FortiGate system time b | Default: disable
    type: Literal["fortiguard", "custom"]  # Use the FortiGuard NTP server or any other availab | Default: fortiguard
    syncinterval: int  # NTP synchronization interval (1 - 1440 min). | Default: 60 | Min: 1 | Max: 1440
    ntpserver: list[NtpNtpserverItem]  # Configure the FortiGate to connect to any availabl
    source_ip: str  # Source IP address for communication to the NTP ser | Default: 0.0.0.0
    source_ip6: str  # Source IPv6 address for communication to the NTP s | Default: ::
    server_mode: Literal["enable", "disable"]  # Enable/disable FortiGate NTP Server Mode. Your For | Default: disable
    authentication: Literal["enable", "disable"]  # Enable/disable authentication. | Default: disable
    key_type: Literal["MD5", "SHA1", "SHA256"]  # Key type for authentication (MD5, SHA1, SHA256). | Default: MD5
    key: str  # Key for authentication. | MaxLen: 64
    key_id: int  # Key ID for authentication. | Default: 0 | Min: 0 | Max: 4294967295
    interface: list[NtpInterfaceItem]  # FortiGate interface(s) with NTP server mode enable


@final
class NtpObject:
    """Typed FortiObject for system/ntp with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Enable/disable setting the FortiGate system time by synchron | Default: disable
    ntpsync: Literal["enable", "disable"]
    # Use the FortiGuard NTP server or any other available NTP Ser | Default: fortiguard
    type: Literal["fortiguard", "custom"]
    # NTP synchronization interval (1 - 1440 min). | Default: 60 | Min: 1 | Max: 1440
    syncinterval: int
    # Configure the FortiGate to connect to any available third-pa
    ntpserver: list[NtpNtpserverObject]
    # Source IP address for communication to the NTP server. | Default: 0.0.0.0
    source_ip: str
    # Source IPv6 address for communication to the NTP server. | Default: ::
    source_ip6: str
    # Enable/disable FortiGate NTP Server Mode. Your FortiGate bec | Default: disable
    server_mode: Literal["enable", "disable"]
    # Enable/disable authentication. | Default: disable
    authentication: Literal["enable", "disable"]
    # Key type for authentication (MD5, SHA1, SHA256). | Default: MD5
    key_type: Literal["MD5", "SHA1", "SHA256"]
    # Key for authentication. | MaxLen: 64
    key: str
    # Key ID for authentication. | Default: 0 | Min: 0 | Max: 4294967295
    key_id: int
    # FortiGate interface(s) with NTP server mode enabled. Devices
    interface: list[NtpInterfaceObject]
    
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
    def to_dict(self) -> NtpPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Ntp:
    """
    Configure system NTP information.
    
    Path: system/ntp
    Category: cmdb
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
    ) -> NtpObject: ...
    
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
    ) -> NtpObject: ...
    
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
    ) -> NtpObject: ...
    
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
    ) -> NtpObject: ...
    
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
    ) -> NtpObject: ...
    
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
    ) -> NtpObject: ...
    
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
    ) -> NtpObject: ...
    
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
    ) -> NtpObject: ...
    
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
    ) -> NtpObject: ...
    
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
    ) -> dict[str, Any] | FortiObject: ...
    
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
    ) -> NtpObject | dict[str, Any]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: NtpPayload | None = ...,
        ntpsync: Literal["enable", "disable"] | None = ...,
        type: Literal["fortiguard", "custom"] | None = ...,
        syncinterval: int | None = ...,
        ntpserver: str | list[str] | list[dict[str, Any]] | None = ...,
        source_ip: str | None = ...,
        source_ip6: str | None = ...,
        server_mode: Literal["enable", "disable"] | None = ...,
        authentication: Literal["enable", "disable"] | None = ...,
        key_type: Literal["MD5", "SHA1", "SHA256"] | None = ...,
        key: str | None = ...,
        key_id: int | None = ...,
        interface: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> NtpObject: ...
    
    @overload
    def put(
        self,
        payload_dict: NtpPayload | None = ...,
        ntpsync: Literal["enable", "disable"] | None = ...,
        type: Literal["fortiguard", "custom"] | None = ...,
        syncinterval: int | None = ...,
        ntpserver: str | list[str] | list[dict[str, Any]] | None = ...,
        source_ip: str | None = ...,
        source_ip6: str | None = ...,
        server_mode: Literal["enable", "disable"] | None = ...,
        authentication: Literal["enable", "disable"] | None = ...,
        key_type: Literal["MD5", "SHA1", "SHA256"] | None = ...,
        key: str | None = ...,
        key_id: int | None = ...,
        interface: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: NtpPayload | None = ...,
        ntpsync: Literal["enable", "disable"] | None = ...,
        type: Literal["fortiguard", "custom"] | None = ...,
        syncinterval: int | None = ...,
        ntpserver: str | list[str] | list[dict[str, Any]] | None = ...,
        source_ip: str | None = ...,
        source_ip6: str | None = ...,
        server_mode: Literal["enable", "disable"] | None = ...,
        authentication: Literal["enable", "disable"] | None = ...,
        key_type: Literal["MD5", "SHA1", "SHA256"] | None = ...,
        key: str | None = ...,
        key_id: int | None = ...,
        interface: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def put(
        self,
        payload_dict: NtpPayload | None = ...,
        ntpsync: Literal["enable", "disable"] | None = ...,
        type: Literal["fortiguard", "custom"] | None = ...,
        syncinterval: int | None = ...,
        ntpserver: str | list[str] | list[dict[str, Any]] | None = ...,
        source_ip: str | None = ...,
        source_ip6: str | None = ...,
        server_mode: Literal["enable", "disable"] | None = ...,
        authentication: Literal["enable", "disable"] | None = ...,
        key_type: Literal["MD5", "SHA1", "SHA256"] | None = ...,
        key: str | None = ...,
        key_id: int | None = ...,
        interface: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: NtpPayload | None = ...,
        ntpsync: Literal["enable", "disable"] | None = ...,
        type: Literal["fortiguard", "custom"] | None = ...,
        syncinterval: int | None = ...,
        ntpserver: str | list[str] | list[dict[str, Any]] | None = ...,
        source_ip: str | None = ...,
        source_ip6: str | None = ...,
        server_mode: Literal["enable", "disable"] | None = ...,
        authentication: Literal["enable", "disable"] | None = ...,
        key_type: Literal["MD5", "SHA1", "SHA256"] | None = ...,
        key: str | None = ...,
        key_id: int | None = ...,
        interface: str | list[str] | list[dict[str, Any]] | None = ...,
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
    "Ntp",
    "NtpPayload",
    "NtpResponse",
    "NtpObject",
]