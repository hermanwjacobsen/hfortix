from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class DomainControllerPayload(TypedDict, total=False):
    """
    Type hints for user/domain_controller payload fields.
    
    Configure domain controller entries.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.system.interface.InterfaceEndpoint` (via: interface)

    **Usage:**
        payload: DomainControllerPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # Domain controller entry name. | MaxLen: 35
    ad_mode: Literal["none", "ds", "lds"]  # Set Active Directory mode. | Default: none
    hostname: str  # Hostname of the server to connect to. | MaxLen: 255
    username: str  # User name to sign in with. Must have proper permis | MaxLen: 64
    password: str  # Password for specified username. | MaxLen: 128
    ip_address: str  # Domain controller IPv4 address. | Default: 0.0.0.0
    ip6: str  # Domain controller IPv6 address. | Default: ::
    port: int  # Port to be used for communication with the domain | Default: 445 | Min: 0 | Max: 65535
    source_ip_address: str  # FortiGate IPv4 address to be used for communicatio | Default: 0.0.0.0
    source_ip6: str  # FortiGate IPv6 address to be used for communicatio | Default: ::
    source_port: int  # Source port to be used for communication with the | Default: 0 | Min: 0 | Max: 65535
    interface_select_method: Literal["auto", "sdwan", "specify"]  # Specify how to select outgoing interface to reach | Default: auto
    interface: str  # Specify outgoing interface to reach server. | MaxLen: 15
    extra_server: list[dict[str, Any]]  # Extra servers.
    domain_name: str  # Domain DNS name. | MaxLen: 255
    replication_port: int  # Port to be used for communication with the domain | Default: 0 | Min: 0 | Max: 65535
    ldap_server: list[dict[str, Any]]  # LDAP server name(s).
    change_detection: Literal["enable", "disable"]  # Enable/disable detection of a configuration change | Default: disable
    change_detection_period: int  # Minutes to detect a configuration change in the Ac | Default: 60 | Min: 5 | Max: 10080
    dns_srv_lookup: Literal["enable", "disable"]  # Enable/disable DNS service lookup. | Default: disable
    adlds_dn: str  # AD LDS distinguished name. | MaxLen: 255
    adlds_ip_address: str  # AD LDS IPv4 address. | Default: 0.0.0.0
    adlds_ip6: str  # AD LDS IPv6 address. | Default: ::
    adlds_port: int  # Port number of AD LDS service (default = 389). | Default: 389 | Min: 0 | Max: 65535

# Nested TypedDicts for table field children (dict mode)

class DomainControllerExtraserverItem(TypedDict):
    """Type hints for extra-server table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    id: int  # Server ID. | Default: 0 | Min: 1 | Max: 100
    ip_address: str  # Domain controller IP address. | Default: 0.0.0.0
    port: int  # Port to be used for communication with the domain | Default: 445 | Min: 0 | Max: 65535
    source_ip_address: str  # FortiGate IPv4 address to be used for communicatio | Default: 0.0.0.0
    source_port: int  # Source port to be used for communication with the | Default: 0 | Min: 0 | Max: 65535


class DomainControllerLdapserverItem(TypedDict):
    """Type hints for ldap-server table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # LDAP server name. | MaxLen: 79


# Nested classes for table field children (object mode)

@final
class DomainControllerExtraserverObject:
    """Typed object for extra-server table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Server ID. | Default: 0 | Min: 1 | Max: 100
    id: int
    # Domain controller IP address. | Default: 0.0.0.0
    ip_address: str
    # Port to be used for communication with the domain controller | Default: 445 | Min: 0 | Max: 65535
    port: int
    # FortiGate IPv4 address to be used for communication with the | Default: 0.0.0.0
    source_ip_address: str
    # Source port to be used for communication with the domain con | Default: 0 | Min: 0 | Max: 65535
    source_port: int
    
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
class DomainControllerLdapserverObject:
    """Typed object for ldap-server table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # LDAP server name. | MaxLen: 79
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
class DomainControllerResponse(TypedDict):
    """
    Type hints for user/domain_controller API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str  # Domain controller entry name. | MaxLen: 35
    ad_mode: Literal["none", "ds", "lds"]  # Set Active Directory mode. | Default: none
    hostname: str  # Hostname of the server to connect to. | MaxLen: 255
    username: str  # User name to sign in with. Must have proper permis | MaxLen: 64
    password: str  # Password for specified username. | MaxLen: 128
    ip_address: str  # Domain controller IPv4 address. | Default: 0.0.0.0
    ip6: str  # Domain controller IPv6 address. | Default: ::
    port: int  # Port to be used for communication with the domain | Default: 445 | Min: 0 | Max: 65535
    source_ip_address: str  # FortiGate IPv4 address to be used for communicatio | Default: 0.0.0.0
    source_ip6: str  # FortiGate IPv6 address to be used for communicatio | Default: ::
    source_port: int  # Source port to be used for communication with the | Default: 0 | Min: 0 | Max: 65535
    interface_select_method: Literal["auto", "sdwan", "specify"]  # Specify how to select outgoing interface to reach | Default: auto
    interface: str  # Specify outgoing interface to reach server. | MaxLen: 15
    extra_server: list[DomainControllerExtraserverItem]  # Extra servers.
    domain_name: str  # Domain DNS name. | MaxLen: 255
    replication_port: int  # Port to be used for communication with the domain | Default: 0 | Min: 0 | Max: 65535
    ldap_server: list[DomainControllerLdapserverItem]  # LDAP server name(s).
    change_detection: Literal["enable", "disable"]  # Enable/disable detection of a configuration change | Default: disable
    change_detection_period: int  # Minutes to detect a configuration change in the Ac | Default: 60 | Min: 5 | Max: 10080
    dns_srv_lookup: Literal["enable", "disable"]  # Enable/disable DNS service lookup. | Default: disable
    adlds_dn: str  # AD LDS distinguished name. | MaxLen: 255
    adlds_ip_address: str  # AD LDS IPv4 address. | Default: 0.0.0.0
    adlds_ip6: str  # AD LDS IPv6 address. | Default: ::
    adlds_port: int  # Port number of AD LDS service (default = 389). | Default: 389 | Min: 0 | Max: 65535


@final
class DomainControllerObject:
    """Typed FortiObject for user/domain_controller with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Domain controller entry name. | MaxLen: 35
    name: str
    # Set Active Directory mode. | Default: none
    ad_mode: Literal["none", "ds", "lds"]
    # Hostname of the server to connect to. | MaxLen: 255
    hostname: str
    # User name to sign in with. Must have proper permissions for | MaxLen: 64
    username: str
    # Password for specified username. | MaxLen: 128
    password: str
    # Domain controller IPv4 address. | Default: 0.0.0.0
    ip_address: str
    # Domain controller IPv6 address. | Default: ::
    ip6: str
    # Port to be used for communication with the domain controller | Default: 445 | Min: 0 | Max: 65535
    port: int
    # FortiGate IPv4 address to be used for communication with the | Default: 0.0.0.0
    source_ip_address: str
    # FortiGate IPv6 address to be used for communication with the | Default: ::
    source_ip6: str
    # Source port to be used for communication with the domain con | Default: 0 | Min: 0 | Max: 65535
    source_port: int
    # Specify how to select outgoing interface to reach server. | Default: auto
    interface_select_method: Literal["auto", "sdwan", "specify"]
    # Specify outgoing interface to reach server. | MaxLen: 15
    interface: str
    # Extra servers.
    extra_server: list[DomainControllerExtraserverObject]
    # Domain DNS name. | MaxLen: 255
    domain_name: str
    # Port to be used for communication with the domain controller | Default: 0 | Min: 0 | Max: 65535
    replication_port: int
    # LDAP server name(s).
    ldap_server: list[DomainControllerLdapserverObject]
    # Enable/disable detection of a configuration change in the Ac | Default: disable
    change_detection: Literal["enable", "disable"]
    # Minutes to detect a configuration change in the Active Direc | Default: 60 | Min: 5 | Max: 10080
    change_detection_period: int
    # Enable/disable DNS service lookup. | Default: disable
    dns_srv_lookup: Literal["enable", "disable"]
    # AD LDS distinguished name. | MaxLen: 255
    adlds_dn: str
    # AD LDS IPv4 address. | Default: 0.0.0.0
    adlds_ip_address: str
    # AD LDS IPv6 address. | Default: ::
    adlds_ip6: str
    # Port number of AD LDS service (default = 389). | Default: 389 | Min: 0 | Max: 65535
    adlds_port: int
    
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
    def to_dict(self) -> DomainControllerPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class DomainController:
    """
    Configure domain controller entries.
    
    Path: user/domain_controller
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
    ) -> DomainControllerObject: ...
    
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
    ) -> DomainControllerObject: ...
    
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
    ) -> FortiObjectList[DomainControllerObject]: ...
    
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
    ) -> DomainControllerObject: ...
    
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
    ) -> DomainControllerObject: ...
    
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
    ) -> FortiObjectList[DomainControllerObject]: ...
    
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
    ) -> DomainControllerObject: ...
    
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
    ) -> DomainControllerObject: ...
    
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
    ) -> FortiObjectList[DomainControllerObject]: ...
    
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
    ) -> DomainControllerObject | list[DomainControllerObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: DomainControllerPayload | None = ...,
        name: str | None = ...,
        ad_mode: Literal["none", "ds", "lds"] | None = ...,
        hostname: str | None = ...,
        username: str | None = ...,
        password: str | None = ...,
        ip_address: str | None = ...,
        ip6: str | None = ...,
        port: int | None = ...,
        source_ip_address: str | None = ...,
        source_ip6: str | None = ...,
        source_port: int | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        extra_server: str | list[str] | list[dict[str, Any]] | None = ...,
        domain_name: str | None = ...,
        replication_port: int | None = ...,
        ldap_server: str | list[str] | list[dict[str, Any]] | None = ...,
        change_detection: Literal["enable", "disable"] | None = ...,
        change_detection_period: int | None = ...,
        dns_srv_lookup: Literal["enable", "disable"] | None = ...,
        adlds_dn: str | None = ...,
        adlds_ip_address: str | None = ...,
        adlds_ip6: str | None = ...,
        adlds_port: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> DomainControllerObject: ...
    
    @overload
    def post(
        self,
        payload_dict: DomainControllerPayload | None = ...,
        name: str | None = ...,
        ad_mode: Literal["none", "ds", "lds"] | None = ...,
        hostname: str | None = ...,
        username: str | None = ...,
        password: str | None = ...,
        ip_address: str | None = ...,
        ip6: str | None = ...,
        port: int | None = ...,
        source_ip_address: str | None = ...,
        source_ip6: str | None = ...,
        source_port: int | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        extra_server: str | list[str] | list[dict[str, Any]] | None = ...,
        domain_name: str | None = ...,
        replication_port: int | None = ...,
        ldap_server: str | list[str] | list[dict[str, Any]] | None = ...,
        change_detection: Literal["enable", "disable"] | None = ...,
        change_detection_period: int | None = ...,
        dns_srv_lookup: Literal["enable", "disable"] | None = ...,
        adlds_dn: str | None = ...,
        adlds_ip_address: str | None = ...,
        adlds_ip6: str | None = ...,
        adlds_port: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: DomainControllerPayload | None = ...,
        name: str | None = ...,
        ad_mode: Literal["none", "ds", "lds"] | None = ...,
        hostname: str | None = ...,
        username: str | None = ...,
        password: str | None = ...,
        ip_address: str | None = ...,
        ip6: str | None = ...,
        port: int | None = ...,
        source_ip_address: str | None = ...,
        source_ip6: str | None = ...,
        source_port: int | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        extra_server: str | list[str] | list[dict[str, Any]] | None = ...,
        domain_name: str | None = ...,
        replication_port: int | None = ...,
        ldap_server: str | list[str] | list[dict[str, Any]] | None = ...,
        change_detection: Literal["enable", "disable"] | None = ...,
        change_detection_period: int | None = ...,
        dns_srv_lookup: Literal["enable", "disable"] | None = ...,
        adlds_dn: str | None = ...,
        adlds_ip_address: str | None = ...,
        adlds_ip6: str | None = ...,
        adlds_port: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def post(
        self,
        payload_dict: DomainControllerPayload | None = ...,
        name: str | None = ...,
        ad_mode: Literal["none", "ds", "lds"] | None = ...,
        hostname: str | None = ...,
        username: str | None = ...,
        password: str | None = ...,
        ip_address: str | None = ...,
        ip6: str | None = ...,
        port: int | None = ...,
        source_ip_address: str | None = ...,
        source_ip6: str | None = ...,
        source_port: int | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        extra_server: str | list[str] | list[dict[str, Any]] | None = ...,
        domain_name: str | None = ...,
        replication_port: int | None = ...,
        ldap_server: str | list[str] | list[dict[str, Any]] | None = ...,
        change_detection: Literal["enable", "disable"] | None = ...,
        change_detection_period: int | None = ...,
        dns_srv_lookup: Literal["enable", "disable"] | None = ...,
        adlds_dn: str | None = ...,
        adlds_ip_address: str | None = ...,
        adlds_ip6: str | None = ...,
        adlds_port: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: DomainControllerPayload | None = ...,
        name: str | None = ...,
        ad_mode: Literal["none", "ds", "lds"] | None = ...,
        hostname: str | None = ...,
        username: str | None = ...,
        password: str | None = ...,
        ip_address: str | None = ...,
        ip6: str | None = ...,
        port: int | None = ...,
        source_ip_address: str | None = ...,
        source_ip6: str | None = ...,
        source_port: int | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        extra_server: str | list[str] | list[dict[str, Any]] | None = ...,
        domain_name: str | None = ...,
        replication_port: int | None = ...,
        ldap_server: str | list[str] | list[dict[str, Any]] | None = ...,
        change_detection: Literal["enable", "disable"] | None = ...,
        change_detection_period: int | None = ...,
        dns_srv_lookup: Literal["enable", "disable"] | None = ...,
        adlds_dn: str | None = ...,
        adlds_ip_address: str | None = ...,
        adlds_ip6: str | None = ...,
        adlds_port: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> DomainControllerObject: ...
    
    @overload
    def put(
        self,
        payload_dict: DomainControllerPayload | None = ...,
        name: str | None = ...,
        ad_mode: Literal["none", "ds", "lds"] | None = ...,
        hostname: str | None = ...,
        username: str | None = ...,
        password: str | None = ...,
        ip_address: str | None = ...,
        ip6: str | None = ...,
        port: int | None = ...,
        source_ip_address: str | None = ...,
        source_ip6: str | None = ...,
        source_port: int | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        extra_server: str | list[str] | list[dict[str, Any]] | None = ...,
        domain_name: str | None = ...,
        replication_port: int | None = ...,
        ldap_server: str | list[str] | list[dict[str, Any]] | None = ...,
        change_detection: Literal["enable", "disable"] | None = ...,
        change_detection_period: int | None = ...,
        dns_srv_lookup: Literal["enable", "disable"] | None = ...,
        adlds_dn: str | None = ...,
        adlds_ip_address: str | None = ...,
        adlds_ip6: str | None = ...,
        adlds_port: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: DomainControllerPayload | None = ...,
        name: str | None = ...,
        ad_mode: Literal["none", "ds", "lds"] | None = ...,
        hostname: str | None = ...,
        username: str | None = ...,
        password: str | None = ...,
        ip_address: str | None = ...,
        ip6: str | None = ...,
        port: int | None = ...,
        source_ip_address: str | None = ...,
        source_ip6: str | None = ...,
        source_port: int | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        extra_server: str | list[str] | list[dict[str, Any]] | None = ...,
        domain_name: str | None = ...,
        replication_port: int | None = ...,
        ldap_server: str | list[str] | list[dict[str, Any]] | None = ...,
        change_detection: Literal["enable", "disable"] | None = ...,
        change_detection_period: int | None = ...,
        dns_srv_lookup: Literal["enable", "disable"] | None = ...,
        adlds_dn: str | None = ...,
        adlds_ip_address: str | None = ...,
        adlds_ip6: str | None = ...,
        adlds_port: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def put(
        self,
        payload_dict: DomainControllerPayload | None = ...,
        name: str | None = ...,
        ad_mode: Literal["none", "ds", "lds"] | None = ...,
        hostname: str | None = ...,
        username: str | None = ...,
        password: str | None = ...,
        ip_address: str | None = ...,
        ip6: str | None = ...,
        port: int | None = ...,
        source_ip_address: str | None = ...,
        source_ip6: str | None = ...,
        source_port: int | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        extra_server: str | list[str] | list[dict[str, Any]] | None = ...,
        domain_name: str | None = ...,
        replication_port: int | None = ...,
        ldap_server: str | list[str] | list[dict[str, Any]] | None = ...,
        change_detection: Literal["enable", "disable"] | None = ...,
        change_detection_period: int | None = ...,
        dns_srv_lookup: Literal["enable", "disable"] | None = ...,
        adlds_dn: str | None = ...,
        adlds_ip_address: str | None = ...,
        adlds_ip6: str | None = ...,
        adlds_port: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> DomainControllerObject: ...
    
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
        payload_dict: DomainControllerPayload | None = ...,
        name: str | None = ...,
        ad_mode: Literal["none", "ds", "lds"] | None = ...,
        hostname: str | None = ...,
        username: str | None = ...,
        password: str | None = ...,
        ip_address: str | None = ...,
        ip6: str | None = ...,
        port: int | None = ...,
        source_ip_address: str | None = ...,
        source_ip6: str | None = ...,
        source_port: int | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        extra_server: str | list[str] | list[dict[str, Any]] | None = ...,
        domain_name: str | None = ...,
        replication_port: int | None = ...,
        ldap_server: str | list[str] | list[dict[str, Any]] | None = ...,
        change_detection: Literal["enable", "disable"] | None = ...,
        change_detection_period: int | None = ...,
        dns_srv_lookup: Literal["enable", "disable"] | None = ...,
        adlds_dn: str | None = ...,
        adlds_ip_address: str | None = ...,
        adlds_ip6: str | None = ...,
        adlds_port: int | None = ...,
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
    "DomainController",
    "DomainControllerPayload",
    "DomainControllerResponse",
    "DomainControllerObject",
]