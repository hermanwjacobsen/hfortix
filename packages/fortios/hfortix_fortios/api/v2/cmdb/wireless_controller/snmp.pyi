from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList
from hfortix_core.types import MutationResponse

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class SnmpPayload(TypedDict, total=False):
    """
    Type hints for wireless_controller/snmp payload fields.
    
    Configure SNMP.
    
    **Usage:**
        payload: SnmpPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    engine_id: str  # AC SNMP engineID string (maximum 24 characters). | MaxLen: 23
    contact_info: str  # Contact Information. | MaxLen: 31
    trap_high_cpu_threshold: int  # CPU usage when trap is sent. | Default: 80 | Min: 10 | Max: 100
    trap_high_mem_threshold: int  # Memory usage when trap is sent. | Default: 80 | Min: 10 | Max: 100
    community: list[dict[str, Any]]  # SNMP Community Configuration.
    user: list[dict[str, Any]]  # SNMP User Configuration.

# Nested TypedDicts for table field children (dict mode)

class SnmpCommunityItem(TypedDict):
    """Type hints for community table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    id: int  # Community ID. | Default: 0 | Min: 0 | Max: 4294967295
    name: str  # Community name. | MaxLen: 35
    status: Literal["enable", "disable"]  # Enable/disable this SNMP community. | Default: enable
    query_v1_status: Literal["enable", "disable"]  # Enable/disable SNMP v1 queries. | Default: enable
    query_v2c_status: Literal["enable", "disable"]  # Enable/disable SNMP v2c queries. | Default: enable
    trap_v1_status: Literal["enable", "disable"]  # Enable/disable SNMP v1 traps. | Default: enable
    trap_v2c_status: Literal["enable", "disable"]  # Enable/disable SNMP v2c traps. | Default: enable
    hosts: str  # Configure IPv4 SNMP managers (hosts).
    hosts6: str  # Configure IPv6 SNMP managers (hosts).


class SnmpUserItem(TypedDict):
    """Type hints for user table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # SNMP user name. | MaxLen: 32
    status: Literal["enable", "disable"]  # SNMP user enable. | Default: enable
    queries: Literal["enable", "disable"]  # Enable/disable SNMP queries for this user. | Default: enable
    trap_status: Literal["enable", "disable"]  # Enable/disable traps for this SNMP user. | Default: disable
    security_level: Literal["no-auth-no-priv", "auth-no-priv", "auth-priv"]  # Security level for message authentication and encr | Default: no-auth-no-priv
    auth_proto: Literal["md5", "sha", "sha224", "sha256", "sha384", "sha512"]  # Authentication protocol. | Default: sha
    auth_pwd: str  # Password for authentication protocol. | MaxLen: 128
    priv_proto: Literal["aes", "des", "aes256", "aes256cisco"]  # Privacy (encryption) protocol. | Default: aes
    priv_pwd: str  # Password for privacy (encryption) protocol. | MaxLen: 128
    notify_hosts: str  # Configure SNMP User Notify Hosts.
    notify_hosts6: str  # Configure IPv6 SNMP User Notify Hosts.


# Nested classes for table field children (object mode)

@final
class SnmpCommunityObject:
    """Typed object for community table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Community ID. | Default: 0 | Min: 0 | Max: 4294967295
    id: int
    # Community name. | MaxLen: 35
    name: str
    # Enable/disable this SNMP community. | Default: enable
    status: Literal["enable", "disable"]
    # Enable/disable SNMP v1 queries. | Default: enable
    query_v1_status: Literal["enable", "disable"]
    # Enable/disable SNMP v2c queries. | Default: enable
    query_v2c_status: Literal["enable", "disable"]
    # Enable/disable SNMP v1 traps. | Default: enable
    trap_v1_status: Literal["enable", "disable"]
    # Enable/disable SNMP v2c traps. | Default: enable
    trap_v2c_status: Literal["enable", "disable"]
    # Configure IPv4 SNMP managers (hosts).
    hosts: str
    # Configure IPv6 SNMP managers (hosts).
    hosts6: str
    
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
class SnmpUserObject:
    """Typed object for user table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # SNMP user name. | MaxLen: 32
    name: str
    # SNMP user enable. | Default: enable
    status: Literal["enable", "disable"]
    # Enable/disable SNMP queries for this user. | Default: enable
    queries: Literal["enable", "disable"]
    # Enable/disable traps for this SNMP user. | Default: disable
    trap_status: Literal["enable", "disable"]
    # Security level for message authentication and encryption. | Default: no-auth-no-priv
    security_level: Literal["no-auth-no-priv", "auth-no-priv", "auth-priv"]
    # Authentication protocol. | Default: sha
    auth_proto: Literal["md5", "sha", "sha224", "sha256", "sha384", "sha512"]
    # Password for authentication protocol. | MaxLen: 128
    auth_pwd: str
    # Privacy (encryption) protocol. | Default: aes
    priv_proto: Literal["aes", "des", "aes256", "aes256cisco"]
    # Password for privacy (encryption) protocol. | MaxLen: 128
    priv_pwd: str
    # Configure SNMP User Notify Hosts.
    notify_hosts: str
    # Configure IPv6 SNMP User Notify Hosts.
    notify_hosts6: str
    
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
class SnmpResponse(TypedDict):
    """
    Type hints for wireless_controller/snmp API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    engine_id: str  # AC SNMP engineID string (maximum 24 characters). | MaxLen: 23
    contact_info: str  # Contact Information. | MaxLen: 31
    trap_high_cpu_threshold: int  # CPU usage when trap is sent. | Default: 80 | Min: 10 | Max: 100
    trap_high_mem_threshold: int  # Memory usage when trap is sent. | Default: 80 | Min: 10 | Max: 100
    community: list[SnmpCommunityItem]  # SNMP Community Configuration.
    user: list[SnmpUserItem]  # SNMP User Configuration.


@final
class SnmpObject:
    """Typed FortiObject for wireless_controller/snmp with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # AC SNMP engineID string (maximum 24 characters). | MaxLen: 23
    engine_id: str
    # Contact Information. | MaxLen: 31
    contact_info: str
    # CPU usage when trap is sent. | Default: 80 | Min: 10 | Max: 100
    trap_high_cpu_threshold: int
    # Memory usage when trap is sent. | Default: 80 | Min: 10 | Max: 100
    trap_high_mem_threshold: int
    # SNMP Community Configuration.
    community: list[SnmpCommunityObject]
    # SNMP User Configuration.
    user: list[SnmpUserObject]
    
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
    def to_dict(self) -> SnmpPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Snmp:
    """
    Configure SNMP.
    
    Path: wireless_controller/snmp
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
    ) -> SnmpObject: ...
    
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
    ) -> SnmpObject: ...
    
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
    ) -> SnmpObject: ...
    
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
    ) -> SnmpObject: ...
    
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
    ) -> SnmpObject: ...
    
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
    ) -> SnmpObject: ...
    
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
    ) -> SnmpObject: ...
    
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
    ) -> SnmpObject: ...
    
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
    ) -> SnmpObject: ...
    
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
    ) -> SnmpObject | dict[str, Any]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: SnmpPayload | None = ...,
        engine_id: str | None = ...,
        contact_info: str | None = ...,
        trap_high_cpu_threshold: int | None = ...,
        trap_high_mem_threshold: int | None = ...,
        community: str | list[str] | list[dict[str, Any]] | None = ...,
        user: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> SnmpObject: ...
    
    @overload
    def put(
        self,
        payload_dict: SnmpPayload | None = ...,
        engine_id: str | None = ...,
        contact_info: str | None = ...,
        trap_high_cpu_threshold: int | None = ...,
        trap_high_mem_threshold: int | None = ...,
        community: str | list[str] | list[dict[str, Any]] | None = ...,
        user: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: SnmpPayload | None = ...,
        engine_id: str | None = ...,
        contact_info: str | None = ...,
        trap_high_cpu_threshold: int | None = ...,
        trap_high_mem_threshold: int | None = ...,
        community: str | list[str] | list[dict[str, Any]] | None = ...,
        user: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def put(
        self,
        payload_dict: SnmpPayload | None = ...,
        engine_id: str | None = ...,
        contact_info: str | None = ...,
        trap_high_cpu_threshold: int | None = ...,
        trap_high_mem_threshold: int | None = ...,
        community: str | list[str] | list[dict[str, Any]] | None = ...,
        user: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: SnmpPayload | None = ...,
        engine_id: str | None = ...,
        contact_info: str | None = ...,
        trap_high_cpu_threshold: int | None = ...,
        trap_high_mem_threshold: int | None = ...,
        community: str | list[str] | list[dict[str, Any]] | None = ...,
        user: str | list[str] | list[dict[str, Any]] | None = ...,
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
    "Snmp",
    "SnmpPayload",
    "SnmpResponse",
    "SnmpObject",
]