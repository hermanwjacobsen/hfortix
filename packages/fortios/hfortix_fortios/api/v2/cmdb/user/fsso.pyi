from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject
from hfortix_core.types import MutationResponse, RawAPIResponse

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class FssoPayload(TypedDict, total=False):
    """
    Type hints for user/fsso payload fields.
    
    Configure Fortinet Single Sign On (FSSO) agents.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.system.interface.InterfaceEndpoint` (via: interface)
        - :class:`~.user.ldap.LdapEndpoint` (via: ldap-server, user-info-server)
        - :class:`~.vpn.certificate.ca.CaEndpoint` (via: ssl-trusted-cert)
        - :class:`~.vpn.certificate.remote.RemoteEndpoint` (via: ssl-trusted-cert)

    **Usage:**
        payload: FssoPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # Name. | MaxLen: 35
    type: Literal["default", "fortinac"]  # Server type. | Default: default
    server: str  # Domain name or IP address of the first FSSO collec | MaxLen: 63
    port: int  # Port of the first FSSO collector agent. | Default: 8000 | Min: 1 | Max: 65535
    password: str  # Password of the first FSSO collector agent. | MaxLen: 128
    server2: str  # Domain name or IP address of the second FSSO colle | MaxLen: 63
    port2: int  # Port of the second FSSO collector agent. | Default: 8000 | Min: 1 | Max: 65535
    password2: str  # Password of the second FSSO collector agent. | MaxLen: 128
    server3: str  # Domain name or IP address of the third FSSO collec | MaxLen: 63
    port3: int  # Port of the third FSSO collector agent. | Default: 8000 | Min: 1 | Max: 65535
    password3: str  # Password of the third FSSO collector agent. | MaxLen: 128
    server4: str  # Domain name or IP address of the fourth FSSO colle | MaxLen: 63
    port4: int  # Port of the fourth FSSO collector agent. | Default: 8000 | Min: 1 | Max: 65535
    password4: str  # Password of the fourth FSSO collector agent. | MaxLen: 128
    server5: str  # Domain name or IP address of the fifth FSSO collec | MaxLen: 63
    port5: int  # Port of the fifth FSSO collector agent. | Default: 8000 | Min: 1 | Max: 65535
    password5: str  # Password of the fifth FSSO collector agent. | MaxLen: 128
    logon_timeout: int  # Interval in minutes to keep logons after FSSO serv | Default: 5 | Min: 1 | Max: 2880
    ldap_server: str  # LDAP server to get group information. | MaxLen: 35
    group_poll_interval: int  # Interval in minutes within to fetch groups from FS | Default: 0 | Min: 1 | Max: 2880
    ldap_poll: Literal["enable", "disable"]  # Enable/disable automatic fetching of groups from L | Default: disable
    ldap_poll_interval: int  # Interval in minutes within to fetch groups from LD | Default: 180 | Min: 1 | Max: 2880
    ldap_poll_filter: str  # Filter used to fetch groups. | Default: (objectCategory=group) | MaxLen: 2047
    user_info_server: str  # LDAP server to get user information. | MaxLen: 35
    ssl: Literal["enable", "disable"]  # Enable/disable use of SSL. | Default: disable
    sni: str  # Server Name Indication. | MaxLen: 255
    ssl_server_host_ip_check: Literal["enable", "disable"]  # Enable/disable server host/IP verification. | Default: disable
    ssl_trusted_cert: str  # Trusted server certificate or CA certificate. | MaxLen: 79
    source_ip: str  # Source IP for communications to FSSO agent. | Default: 0.0.0.0
    source_ip6: str  # IPv6 source for communications to FSSO agent. | Default: ::
    interface_select_method: Literal["auto", "sdwan", "specify"]  # Specify how to select outgoing interface to reach | Default: auto
    interface: str  # Specify outgoing interface to reach server. | MaxLen: 15
    vrf_select: int  # VRF ID used for connection to server. | Default: 0 | Min: 0 | Max: 511

# Nested TypedDicts for table field children (dict mode)

# Nested classes for table field children (object mode)


# Response TypedDict for GET returns (all fields present in API response)
class FssoResponse(TypedDict):
    """
    Type hints for user/fsso API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str  # Name. | MaxLen: 35
    type: Literal["default", "fortinac"]  # Server type. | Default: default
    server: str  # Domain name or IP address of the first FSSO collec | MaxLen: 63
    port: int  # Port of the first FSSO collector agent. | Default: 8000 | Min: 1 | Max: 65535
    password: str  # Password of the first FSSO collector agent. | MaxLen: 128
    server2: str  # Domain name or IP address of the second FSSO colle | MaxLen: 63
    port2: int  # Port of the second FSSO collector agent. | Default: 8000 | Min: 1 | Max: 65535
    password2: str  # Password of the second FSSO collector agent. | MaxLen: 128
    server3: str  # Domain name or IP address of the third FSSO collec | MaxLen: 63
    port3: int  # Port of the third FSSO collector agent. | Default: 8000 | Min: 1 | Max: 65535
    password3: str  # Password of the third FSSO collector agent. | MaxLen: 128
    server4: str  # Domain name or IP address of the fourth FSSO colle | MaxLen: 63
    port4: int  # Port of the fourth FSSO collector agent. | Default: 8000 | Min: 1 | Max: 65535
    password4: str  # Password of the fourth FSSO collector agent. | MaxLen: 128
    server5: str  # Domain name or IP address of the fifth FSSO collec | MaxLen: 63
    port5: int  # Port of the fifth FSSO collector agent. | Default: 8000 | Min: 1 | Max: 65535
    password5: str  # Password of the fifth FSSO collector agent. | MaxLen: 128
    logon_timeout: int  # Interval in minutes to keep logons after FSSO serv | Default: 5 | Min: 1 | Max: 2880
    ldap_server: str  # LDAP server to get group information. | MaxLen: 35
    group_poll_interval: int  # Interval in minutes within to fetch groups from FS | Default: 0 | Min: 1 | Max: 2880
    ldap_poll: Literal["enable", "disable"]  # Enable/disable automatic fetching of groups from L | Default: disable
    ldap_poll_interval: int  # Interval in minutes within to fetch groups from LD | Default: 180 | Min: 1 | Max: 2880
    ldap_poll_filter: str  # Filter used to fetch groups. | Default: (objectCategory=group) | MaxLen: 2047
    user_info_server: str  # LDAP server to get user information. | MaxLen: 35
    ssl: Literal["enable", "disable"]  # Enable/disable use of SSL. | Default: disable
    sni: str  # Server Name Indication. | MaxLen: 255
    ssl_server_host_ip_check: Literal["enable", "disable"]  # Enable/disable server host/IP verification. | Default: disable
    ssl_trusted_cert: str  # Trusted server certificate or CA certificate. | MaxLen: 79
    source_ip: str  # Source IP for communications to FSSO agent. | Default: 0.0.0.0
    source_ip6: str  # IPv6 source for communications to FSSO agent. | Default: ::
    interface_select_method: Literal["auto", "sdwan", "specify"]  # Specify how to select outgoing interface to reach | Default: auto
    interface: str  # Specify outgoing interface to reach server. | MaxLen: 15
    vrf_select: int  # VRF ID used for connection to server. | Default: 0 | Min: 0 | Max: 511


@final
class FssoObject:
    """Typed FortiObject for user/fsso with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Name. | MaxLen: 35
    name: str
    # Server type. | Default: default
    type: Literal["default", "fortinac"]
    # Domain name or IP address of the first FSSO collector agent. | MaxLen: 63
    server: str
    # Port of the first FSSO collector agent. | Default: 8000 | Min: 1 | Max: 65535
    port: int
    # Password of the first FSSO collector agent. | MaxLen: 128
    password: str
    # Domain name or IP address of the second FSSO collector agent | MaxLen: 63
    server2: str
    # Port of the second FSSO collector agent. | Default: 8000 | Min: 1 | Max: 65535
    port2: int
    # Password of the second FSSO collector agent. | MaxLen: 128
    password2: str
    # Domain name or IP address of the third FSSO collector agent. | MaxLen: 63
    server3: str
    # Port of the third FSSO collector agent. | Default: 8000 | Min: 1 | Max: 65535
    port3: int
    # Password of the third FSSO collector agent. | MaxLen: 128
    password3: str
    # Domain name or IP address of the fourth FSSO collector agent | MaxLen: 63
    server4: str
    # Port of the fourth FSSO collector agent. | Default: 8000 | Min: 1 | Max: 65535
    port4: int
    # Password of the fourth FSSO collector agent. | MaxLen: 128
    password4: str
    # Domain name or IP address of the fifth FSSO collector agent. | MaxLen: 63
    server5: str
    # Port of the fifth FSSO collector agent. | Default: 8000 | Min: 1 | Max: 65535
    port5: int
    # Password of the fifth FSSO collector agent. | MaxLen: 128
    password5: str
    # Interval in minutes to keep logons after FSSO server down. | Default: 5 | Min: 1 | Max: 2880
    logon_timeout: int
    # LDAP server to get group information. | MaxLen: 35
    ldap_server: str
    # Interval in minutes within to fetch groups from FSSO server, | Default: 0 | Min: 1 | Max: 2880
    group_poll_interval: int
    # Enable/disable automatic fetching of groups from LDAP server | Default: disable
    ldap_poll: Literal["enable", "disable"]
    # Interval in minutes within to fetch groups from LDAP server. | Default: 180 | Min: 1 | Max: 2880
    ldap_poll_interval: int
    # Filter used to fetch groups. | Default: (objectCategory=group) | MaxLen: 2047
    ldap_poll_filter: str
    # LDAP server to get user information. | MaxLen: 35
    user_info_server: str
    # Enable/disable use of SSL. | Default: disable
    ssl: Literal["enable", "disable"]
    # Server Name Indication. | MaxLen: 255
    sni: str
    # Enable/disable server host/IP verification. | Default: disable
    ssl_server_host_ip_check: Literal["enable", "disable"]
    # Trusted server certificate or CA certificate. | MaxLen: 79
    ssl_trusted_cert: str
    # Source IP for communications to FSSO agent. | Default: 0.0.0.0
    source_ip: str
    # IPv6 source for communications to FSSO agent. | Default: ::
    source_ip6: str
    # Specify how to select outgoing interface to reach server. | Default: auto
    interface_select_method: Literal["auto", "sdwan", "specify"]
    # Specify outgoing interface to reach server. | MaxLen: 15
    interface: str
    # VRF ID used for connection to server. | Default: 0 | Min: 0 | Max: 511
    vrf_select: int
    
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
    def to_dict(self) -> FssoPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Fsso:
    """
    Configure Fortinet Single Sign On (FSSO) agents.
    
    Path: user/fsso
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
    ) -> FssoObject: ...
    
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
    ) -> FssoObject: ...
    
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
    ) -> list[FssoObject]: ...
    
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
    ) -> FssoObject: ...
    
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
    ) -> FssoObject: ...
    
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
    ) -> list[FssoObject]: ...
    
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
    ) -> FssoObject: ...
    
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
    ) -> FssoObject: ...
    
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
    ) -> list[FssoObject]: ...
    
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
    ) -> FssoObject | list[FssoObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: FssoPayload | None = ...,
        name: str | None = ...,
        type: Literal["default", "fortinac"] | None = ...,
        server: str | None = ...,
        port: int | None = ...,
        password: str | None = ...,
        server2: str | None = ...,
        port2: int | None = ...,
        password2: str | None = ...,
        server3: str | None = ...,
        port3: int | None = ...,
        password3: str | None = ...,
        server4: str | None = ...,
        port4: int | None = ...,
        password4: str | None = ...,
        server5: str | None = ...,
        port5: int | None = ...,
        password5: str | None = ...,
        logon_timeout: int | None = ...,
        ldap_server: str | None = ...,
        group_poll_interval: int | None = ...,
        ldap_poll: Literal["enable", "disable"] | None = ...,
        ldap_poll_interval: int | None = ...,
        ldap_poll_filter: str | None = ...,
        user_info_server: str | None = ...,
        ssl: Literal["enable", "disable"] | None = ...,
        sni: str | None = ...,
        ssl_server_host_ip_check: Literal["enable", "disable"] | None = ...,
        ssl_trusted_cert: str | None = ...,
        source_ip: str | None = ...,
        source_ip6: str | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> FssoObject: ...
    
    @overload
    def post(
        self,
        payload_dict: FssoPayload | None = ...,
        name: str | None = ...,
        type: Literal["default", "fortinac"] | None = ...,
        server: str | None = ...,
        port: int | None = ...,
        password: str | None = ...,
        server2: str | None = ...,
        port2: int | None = ...,
        password2: str | None = ...,
        server3: str | None = ...,
        port3: int | None = ...,
        password3: str | None = ...,
        server4: str | None = ...,
        port4: int | None = ...,
        password4: str | None = ...,
        server5: str | None = ...,
        port5: int | None = ...,
        password5: str | None = ...,
        logon_timeout: int | None = ...,
        ldap_server: str | None = ...,
        group_poll_interval: int | None = ...,
        ldap_poll: Literal["enable", "disable"] | None = ...,
        ldap_poll_interval: int | None = ...,
        ldap_poll_filter: str | None = ...,
        user_info_server: str | None = ...,
        ssl: Literal["enable", "disable"] | None = ...,
        sni: str | None = ...,
        ssl_server_host_ip_check: Literal["enable", "disable"] | None = ...,
        ssl_trusted_cert: str | None = ...,
        source_ip: str | None = ...,
        source_ip6: str | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    # raw_json=True returns the full API envelope
    @overload
    def post(
        self,
        payload_dict: FssoPayload | None = ...,
        name: str | None = ...,
        type: Literal["default", "fortinac"] | None = ...,
        server: str | None = ...,
        port: int | None = ...,
        password: str | None = ...,
        server2: str | None = ...,
        port2: int | None = ...,
        password2: str | None = ...,
        server3: str | None = ...,
        port3: int | None = ...,
        password3: str | None = ...,
        server4: str | None = ...,
        port4: int | None = ...,
        password4: str | None = ...,
        server5: str | None = ...,
        port5: int | None = ...,
        password5: str | None = ...,
        logon_timeout: int | None = ...,
        ldap_server: str | None = ...,
        group_poll_interval: int | None = ...,
        ldap_poll: Literal["enable", "disable"] | None = ...,
        ldap_poll_interval: int | None = ...,
        ldap_poll_filter: str | None = ...,
        user_info_server: str | None = ...,
        ssl: Literal["enable", "disable"] | None = ...,
        sni: str | None = ...,
        ssl_server_host_ip_check: Literal["enable", "disable"] | None = ...,
        ssl_trusted_cert: str | None = ...,
        source_ip: str | None = ...,
        source_ip6: str | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> RawAPIResponse: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: FssoPayload | None = ...,
        name: str | None = ...,
        type: Literal["default", "fortinac"] | None = ...,
        server: str | None = ...,
        port: int | None = ...,
        password: str | None = ...,
        server2: str | None = ...,
        port2: int | None = ...,
        password2: str | None = ...,
        server3: str | None = ...,
        port3: int | None = ...,
        password3: str | None = ...,
        server4: str | None = ...,
        port4: int | None = ...,
        password4: str | None = ...,
        server5: str | None = ...,
        port5: int | None = ...,
        password5: str | None = ...,
        logon_timeout: int | None = ...,
        ldap_server: str | None = ...,
        group_poll_interval: int | None = ...,
        ldap_poll: Literal["enable", "disable"] | None = ...,
        ldap_poll_interval: int | None = ...,
        ldap_poll_filter: str | None = ...,
        user_info_server: str | None = ...,
        ssl: Literal["enable", "disable"] | None = ...,
        sni: str | None = ...,
        ssl_server_host_ip_check: Literal["enable", "disable"] | None = ...,
        ssl_trusted_cert: str | None = ...,
        source_ip: str | None = ...,
        source_ip6: str | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        vdom: str | bool | None = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    def post(
        self,
        payload_dict: FssoPayload | None = ...,
        name: str | None = ...,
        type: Literal["default", "fortinac"] | None = ...,
        server: str | None = ...,
        port: int | None = ...,
        password: str | None = ...,
        server2: str | None = ...,
        port2: int | None = ...,
        password2: str | None = ...,
        server3: str | None = ...,
        port3: int | None = ...,
        password3: str | None = ...,
        server4: str | None = ...,
        port4: int | None = ...,
        password4: str | None = ...,
        server5: str | None = ...,
        port5: int | None = ...,
        password5: str | None = ...,
        logon_timeout: int | None = ...,
        ldap_server: str | None = ...,
        group_poll_interval: int | None = ...,
        ldap_poll: Literal["enable", "disable"] | None = ...,
        ldap_poll_interval: int | None = ...,
        ldap_poll_filter: str | None = ...,
        user_info_server: str | None = ...,
        ssl: Literal["enable", "disable"] | None = ...,
        sni: str | None = ...,
        ssl_server_host_ip_check: Literal["enable", "disable"] | None = ...,
        ssl_trusted_cert: str | None = ...,
        source_ip: str | None = ...,
        source_ip6: str | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: FssoPayload | None = ...,
        name: str | None = ...,
        type: Literal["default", "fortinac"] | None = ...,
        server: str | None = ...,
        port: int | None = ...,
        password: str | None = ...,
        server2: str | None = ...,
        port2: int | None = ...,
        password2: str | None = ...,
        server3: str | None = ...,
        port3: int | None = ...,
        password3: str | None = ...,
        server4: str | None = ...,
        port4: int | None = ...,
        password4: str | None = ...,
        server5: str | None = ...,
        port5: int | None = ...,
        password5: str | None = ...,
        logon_timeout: int | None = ...,
        ldap_server: str | None = ...,
        group_poll_interval: int | None = ...,
        ldap_poll: Literal["enable", "disable"] | None = ...,
        ldap_poll_interval: int | None = ...,
        ldap_poll_filter: str | None = ...,
        user_info_server: str | None = ...,
        ssl: Literal["enable", "disable"] | None = ...,
        sni: str | None = ...,
        ssl_server_host_ip_check: Literal["enable", "disable"] | None = ...,
        ssl_trusted_cert: str | None = ...,
        source_ip: str | None = ...,
        source_ip6: str | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> FssoObject: ...
    
    @overload
    def put(
        self,
        payload_dict: FssoPayload | None = ...,
        name: str | None = ...,
        type: Literal["default", "fortinac"] | None = ...,
        server: str | None = ...,
        port: int | None = ...,
        password: str | None = ...,
        server2: str | None = ...,
        port2: int | None = ...,
        password2: str | None = ...,
        server3: str | None = ...,
        port3: int | None = ...,
        password3: str | None = ...,
        server4: str | None = ...,
        port4: int | None = ...,
        password4: str | None = ...,
        server5: str | None = ...,
        port5: int | None = ...,
        password5: str | None = ...,
        logon_timeout: int | None = ...,
        ldap_server: str | None = ...,
        group_poll_interval: int | None = ...,
        ldap_poll: Literal["enable", "disable"] | None = ...,
        ldap_poll_interval: int | None = ...,
        ldap_poll_filter: str | None = ...,
        user_info_server: str | None = ...,
        ssl: Literal["enable", "disable"] | None = ...,
        sni: str | None = ...,
        ssl_server_host_ip_check: Literal["enable", "disable"] | None = ...,
        ssl_trusted_cert: str | None = ...,
        source_ip: str | None = ...,
        source_ip6: str | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    # raw_json=True returns the full API envelope
    @overload
    def put(
        self,
        payload_dict: FssoPayload | None = ...,
        name: str | None = ...,
        type: Literal["default", "fortinac"] | None = ...,
        server: str | None = ...,
        port: int | None = ...,
        password: str | None = ...,
        server2: str | None = ...,
        port2: int | None = ...,
        password2: str | None = ...,
        server3: str | None = ...,
        port3: int | None = ...,
        password3: str | None = ...,
        server4: str | None = ...,
        port4: int | None = ...,
        password4: str | None = ...,
        server5: str | None = ...,
        port5: int | None = ...,
        password5: str | None = ...,
        logon_timeout: int | None = ...,
        ldap_server: str | None = ...,
        group_poll_interval: int | None = ...,
        ldap_poll: Literal["enable", "disable"] | None = ...,
        ldap_poll_interval: int | None = ...,
        ldap_poll_filter: str | None = ...,
        user_info_server: str | None = ...,
        ssl: Literal["enable", "disable"] | None = ...,
        sni: str | None = ...,
        ssl_server_host_ip_check: Literal["enable", "disable"] | None = ...,
        ssl_trusted_cert: str | None = ...,
        source_ip: str | None = ...,
        source_ip6: str | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> RawAPIResponse: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: FssoPayload | None = ...,
        name: str | None = ...,
        type: Literal["default", "fortinac"] | None = ...,
        server: str | None = ...,
        port: int | None = ...,
        password: str | None = ...,
        server2: str | None = ...,
        port2: int | None = ...,
        password2: str | None = ...,
        server3: str | None = ...,
        port3: int | None = ...,
        password3: str | None = ...,
        server4: str | None = ...,
        port4: int | None = ...,
        password4: str | None = ...,
        server5: str | None = ...,
        port5: int | None = ...,
        password5: str | None = ...,
        logon_timeout: int | None = ...,
        ldap_server: str | None = ...,
        group_poll_interval: int | None = ...,
        ldap_poll: Literal["enable", "disable"] | None = ...,
        ldap_poll_interval: int | None = ...,
        ldap_poll_filter: str | None = ...,
        user_info_server: str | None = ...,
        ssl: Literal["enable", "disable"] | None = ...,
        sni: str | None = ...,
        ssl_server_host_ip_check: Literal["enable", "disable"] | None = ...,
        ssl_trusted_cert: str | None = ...,
        source_ip: str | None = ...,
        source_ip6: str | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        vdom: str | bool | None = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    def put(
        self,
        payload_dict: FssoPayload | None = ...,
        name: str | None = ...,
        type: Literal["default", "fortinac"] | None = ...,
        server: str | None = ...,
        port: int | None = ...,
        password: str | None = ...,
        server2: str | None = ...,
        port2: int | None = ...,
        password2: str | None = ...,
        server3: str | None = ...,
        port3: int | None = ...,
        password3: str | None = ...,
        server4: str | None = ...,
        port4: int | None = ...,
        password4: str | None = ...,
        server5: str | None = ...,
        port5: int | None = ...,
        password5: str | None = ...,
        logon_timeout: int | None = ...,
        ldap_server: str | None = ...,
        group_poll_interval: int | None = ...,
        ldap_poll: Literal["enable", "disable"] | None = ...,
        ldap_poll_interval: int | None = ...,
        ldap_poll_filter: str | None = ...,
        user_info_server: str | None = ...,
        ssl: Literal["enable", "disable"] | None = ...,
        sni: str | None = ...,
        ssl_server_host_ip_check: Literal["enable", "disable"] | None = ...,
        ssl_trusted_cert: str | None = ...,
        source_ip: str | None = ...,
        source_ip6: str | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
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
    ) -> FssoObject: ...
    
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
        payload_dict: FssoPayload | None = ...,
        name: str | None = ...,
        type: Literal["default", "fortinac"] | None = ...,
        server: str | None = ...,
        port: int | None = ...,
        password: str | None = ...,
        server2: str | None = ...,
        port2: int | None = ...,
        password2: str | None = ...,
        server3: str | None = ...,
        port3: int | None = ...,
        password3: str | None = ...,
        server4: str | None = ...,
        port4: int | None = ...,
        password4: str | None = ...,
        server5: str | None = ...,
        port5: int | None = ...,
        password5: str | None = ...,
        logon_timeout: int | None = ...,
        ldap_server: str | None = ...,
        group_poll_interval: int | None = ...,
        ldap_poll: Literal["enable", "disable"] | None = ...,
        ldap_poll_interval: int | None = ...,
        ldap_poll_filter: str | None = ...,
        user_info_server: str | None = ...,
        ssl: Literal["enable", "disable"] | None = ...,
        sni: str | None = ...,
        ssl_server_host_ip_check: Literal["enable", "disable"] | None = ...,
        ssl_trusted_cert: str | None = ...,
        source_ip: str | None = ...,
        source_ip6: str | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
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
    "Fsso",
    "FssoPayload",
    "FssoResponse",
    "FssoObject",
]