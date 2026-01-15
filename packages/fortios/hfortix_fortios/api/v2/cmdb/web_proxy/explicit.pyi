from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject
from hfortix_core.types import MutationResponse, RawAPIResponse

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class ExplicitPayload(TypedDict, total=False):
    """
    Type hints for web_proxy/explicit payload fields.
    
    Configure explicit Web proxy settings.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.system.interface.InterfaceEndpoint` (via: interface)

    **Usage:**
        payload: ExplicitPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    status: Literal["enable", "disable"]  # Enable/disable the explicit Web proxy for HTTP and | Default: disable
    secure_web_proxy: Literal["disable", "enable", "secure"]  # Enable/disable/require the secure web proxy for HT | Default: disable
    ftp_over_http: Literal["enable", "disable"]  # Enable to proxy FTP-over-HTTP sessions sent from a | Default: disable
    socks: Literal["enable", "disable"]  # Enable/disable the SOCKS proxy. | Default: disable
    http_incoming_port: str  # Accept incoming HTTP requests on one or more ports
    http_connection_mode: Literal["static", "multiplex", "serverpool"]  # HTTP connection mode (default = static). | Default: static
    https_incoming_port: str  # Accept incoming HTTPS requests on one or more port
    secure_web_proxy_cert: list[dict[str, Any]]  # Name of certificates for secure web proxy.
    client_cert: Literal["disable", "enable"]  # Enable/disable to request client certificate. | Default: disable
    user_agent_detect: Literal["disable", "enable"]  # Enable/disable to detect device type by HTTP user- | Default: enable
    empty_cert_action: Literal["accept", "block", "accept-unmanageable"]  # Action of an empty client certificate. | Default: block
    ssl_dh_bits: Literal["768", "1024", "1536", "2048"]  # Bit-size of Diffie-Hellman (DH) prime used in DHE- | Default: 2048
    ftp_incoming_port: str  # Accept incoming FTP-over-HTTP requests on one or m
    socks_incoming_port: str  # Accept incoming SOCKS proxy requests on one or mor
    incoming_ip: str  # Restrict the explicit HTTP proxy to only accept se | Default: 0.0.0.0
    outgoing_ip: list[dict[str, Any]]  # Outgoing HTTP requests will have this IP address a
    interface_select_method: Literal["sdwan", "specify"]  # Specify how to select outgoing interface to reach | Default: sdwan
    interface: str  # Specify outgoing interface to reach server. | MaxLen: 15
    vrf_select: int  # VRF ID used for connection to server. | Default: -1 | Min: 0 | Max: 511
    ipv6_status: Literal["enable", "disable"]  # Enable/disable allowing an IPv6 web proxy destinat | Default: disable
    incoming_ip6: str  # Restrict the explicit web proxy to only accept ses | Default: ::
    outgoing_ip6: list[dict[str, Any]]  # Outgoing HTTP requests will leave this IPv6. Multi
    strict_guest: Literal["enable", "disable"]  # Enable/disable strict guest user checking by the e | Default: disable
    pref_dns_result: Literal["ipv4", "ipv6", "ipv4-strict", "ipv6-strict"]  # Prefer resolving addresses using the configured IP | Default: ipv4
    unknown_http_version: Literal["reject", "best-effort"]  # How to handle HTTP sessions that do not comply wit | Default: reject
    realm: str  # Authentication realm used to identify the explicit | Default: default | MaxLen: 63
    sec_default_action: Literal["accept", "deny"]  # Accept or deny explicit web proxy sessions when no | Default: deny
    https_replacement_message: Literal["enable", "disable"]  # Enable/disable sending the client a replacement me | Default: enable
    message_upon_server_error: Literal["enable", "disable"]  # Enable/disable displaying a replacement message wh | Default: enable
    pac_file_server_status: Literal["enable", "disable"]  # Enable/disable Proxy Auto-Configuration (PAC) for | Default: disable
    pac_file_url: str  # PAC file access URL.
    pac_file_server_port: str  # Port number that PAC traffic from client web brows
    pac_file_through_https: Literal["enable", "disable"]  # Enable/disable to get Proxy Auto-Configuration | Default: disable
    pac_file_name: str  # Pac file name. | Default: proxy.pac | MaxLen: 63
    pac_file_data: str  # PAC file contents enclosed in quotes
    pac_policy: list[dict[str, Any]]  # PAC policies.
    ssl_algorithm: Literal["high", "medium", "low"]  # Relative strength of encryption algorithms accepte | Default: low
    trace_auth_no_rsp: Literal["enable", "disable"]  # Enable/disable logging timed-out authentication re | Default: disable

# Nested TypedDicts for table field children (dict mode)

class ExplicitSecurewebproxycertItem(TypedDict):
    """Type hints for secure-web-proxy-cert table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # Certificate list. | Default: Fortinet_SSL | MaxLen: 79


class ExplicitPacpolicyItem(TypedDict):
    """Type hints for pac-policy table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    policyid: int  # Policy ID. | Default: 0 | Min: 1 | Max: 100
    status: Literal["enable", "disable"]  # Enable/disable policy. | Default: enable
    srcaddr: str  # Source address objects.
    srcaddr6: str  # Source address6 objects.
    dstaddr: str  # Destination address objects.
    pac_file_name: str  # Pac file name. | Default: proxy.pac | MaxLen: 63
    pac_file_data: str  # PAC file contents enclosed in quotes
    comments: str  # Optional comments. | MaxLen: 1023


# Nested classes for table field children (object mode)

@final
class ExplicitSecurewebproxycertObject:
    """Typed object for secure-web-proxy-cert table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Certificate list. | Default: Fortinet_SSL | MaxLen: 79
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


@final
class ExplicitPacpolicyObject:
    """Typed object for pac-policy table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Policy ID. | Default: 0 | Min: 1 | Max: 100
    policyid: int
    # Enable/disable policy. | Default: enable
    status: Literal["enable", "disable"]
    # Source address objects.
    srcaddr: str
    # Source address6 objects.
    srcaddr6: str
    # Destination address objects.
    dstaddr: str
    # Pac file name. | Default: proxy.pac | MaxLen: 63
    pac_file_name: str
    # PAC file contents enclosed in quotes (maximum of 256K bytes)
    pac_file_data: str
    # Optional comments. | MaxLen: 1023
    comments: str
    
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
class ExplicitResponse(TypedDict):
    """
    Type hints for web_proxy/explicit API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    status: Literal["enable", "disable"]  # Enable/disable the explicit Web proxy for HTTP and | Default: disable
    secure_web_proxy: Literal["disable", "enable", "secure"]  # Enable/disable/require the secure web proxy for HT | Default: disable
    ftp_over_http: Literal["enable", "disable"]  # Enable to proxy FTP-over-HTTP sessions sent from a | Default: disable
    socks: Literal["enable", "disable"]  # Enable/disable the SOCKS proxy. | Default: disable
    http_incoming_port: str  # Accept incoming HTTP requests on one or more ports
    http_connection_mode: Literal["static", "multiplex", "serverpool"]  # HTTP connection mode (default = static). | Default: static
    https_incoming_port: str  # Accept incoming HTTPS requests on one or more port
    secure_web_proxy_cert: list[ExplicitSecurewebproxycertItem]  # Name of certificates for secure web proxy.
    client_cert: Literal["disable", "enable"]  # Enable/disable to request client certificate. | Default: disable
    user_agent_detect: Literal["disable", "enable"]  # Enable/disable to detect device type by HTTP user- | Default: enable
    empty_cert_action: Literal["accept", "block", "accept-unmanageable"]  # Action of an empty client certificate. | Default: block
    ssl_dh_bits: Literal["768", "1024", "1536", "2048"]  # Bit-size of Diffie-Hellman (DH) prime used in DHE- | Default: 2048
    ftp_incoming_port: str  # Accept incoming FTP-over-HTTP requests on one or m
    socks_incoming_port: str  # Accept incoming SOCKS proxy requests on one or mor
    incoming_ip: str  # Restrict the explicit HTTP proxy to only accept se | Default: 0.0.0.0
    outgoing_ip: list[dict[str, Any]]  # Outgoing HTTP requests will have this IP address a
    interface_select_method: Literal["sdwan", "specify"]  # Specify how to select outgoing interface to reach | Default: sdwan
    interface: str  # Specify outgoing interface to reach server. | MaxLen: 15
    vrf_select: int  # VRF ID used for connection to server. | Default: -1 | Min: 0 | Max: 511
    ipv6_status: Literal["enable", "disable"]  # Enable/disable allowing an IPv6 web proxy destinat | Default: disable
    incoming_ip6: str  # Restrict the explicit web proxy to only accept ses | Default: ::
    outgoing_ip6: list[dict[str, Any]]  # Outgoing HTTP requests will leave this IPv6. Multi
    strict_guest: Literal["enable", "disable"]  # Enable/disable strict guest user checking by the e | Default: disable
    pref_dns_result: Literal["ipv4", "ipv6", "ipv4-strict", "ipv6-strict"]  # Prefer resolving addresses using the configured IP | Default: ipv4
    unknown_http_version: Literal["reject", "best-effort"]  # How to handle HTTP sessions that do not comply wit | Default: reject
    realm: str  # Authentication realm used to identify the explicit | Default: default | MaxLen: 63
    sec_default_action: Literal["accept", "deny"]  # Accept or deny explicit web proxy sessions when no | Default: deny
    https_replacement_message: Literal["enable", "disable"]  # Enable/disable sending the client a replacement me | Default: enable
    message_upon_server_error: Literal["enable", "disable"]  # Enable/disable displaying a replacement message wh | Default: enable
    pac_file_server_status: Literal["enable", "disable"]  # Enable/disable Proxy Auto-Configuration (PAC) for | Default: disable
    pac_file_url: str  # PAC file access URL.
    pac_file_server_port: str  # Port number that PAC traffic from client web brows
    pac_file_through_https: Literal["enable", "disable"]  # Enable/disable to get Proxy Auto-Configuration | Default: disable
    pac_file_name: str  # Pac file name. | Default: proxy.pac | MaxLen: 63
    pac_file_data: str  # PAC file contents enclosed in quotes
    pac_policy: list[ExplicitPacpolicyItem]  # PAC policies.
    ssl_algorithm: Literal["high", "medium", "low"]  # Relative strength of encryption algorithms accepte | Default: low
    trace_auth_no_rsp: Literal["enable", "disable"]  # Enable/disable logging timed-out authentication re | Default: disable


@final
class ExplicitObject:
    """Typed FortiObject for web_proxy/explicit with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Enable/disable the explicit Web proxy for HTTP and HTTPS ses | Default: disable
    status: Literal["enable", "disable"]
    # Enable/disable/require the secure web proxy for HTTP and HTT | Default: disable
    secure_web_proxy: Literal["disable", "enable", "secure"]
    # Enable to proxy FTP-over-HTTP sessions sent from a web brows | Default: disable
    ftp_over_http: Literal["enable", "disable"]
    # Enable/disable the SOCKS proxy. | Default: disable
    socks: Literal["enable", "disable"]
    # Accept incoming HTTP requests on one or more ports
    http_incoming_port: str
    # HTTP connection mode (default = static). | Default: static
    http_connection_mode: Literal["static", "multiplex", "serverpool"]
    # Accept incoming HTTPS requests on one or more ports
    https_incoming_port: str
    # Name of certificates for secure web proxy.
    secure_web_proxy_cert: list[ExplicitSecurewebproxycertObject]
    # Enable/disable to request client certificate. | Default: disable
    client_cert: Literal["disable", "enable"]
    # Enable/disable to detect device type by HTTP user-agent if n | Default: enable
    user_agent_detect: Literal["disable", "enable"]
    # Action of an empty client certificate. | Default: block
    empty_cert_action: Literal["accept", "block", "accept-unmanageable"]
    # Bit-size of Diffie-Hellman (DH) prime used in DHE-RSA negoti | Default: 2048
    ssl_dh_bits: Literal["768", "1024", "1536", "2048"]
    # Accept incoming FTP-over-HTTP requests on one or more ports
    ftp_incoming_port: str
    # Accept incoming SOCKS proxy requests on one or more ports
    socks_incoming_port: str
    # Restrict the explicit HTTP proxy to only accept sessions fro | Default: 0.0.0.0
    incoming_ip: str
    # Outgoing HTTP requests will have this IP address as their so
    outgoing_ip: list[dict[str, Any]]
    # Specify how to select outgoing interface to reach server. | Default: sdwan
    interface_select_method: Literal["sdwan", "specify"]
    # Specify outgoing interface to reach server. | MaxLen: 15
    interface: str
    # VRF ID used for connection to server. | Default: -1 | Min: 0 | Max: 511
    vrf_select: int
    # Enable/disable allowing an IPv6 web proxy destination in pol | Default: disable
    ipv6_status: Literal["enable", "disable"]
    # Restrict the explicit web proxy to only accept sessions from | Default: ::
    incoming_ip6: str
    # Outgoing HTTP requests will leave this IPv6. Multiple interf
    outgoing_ip6: list[dict[str, Any]]
    # Enable/disable strict guest user checking by the explicit we | Default: disable
    strict_guest: Literal["enable", "disable"]
    # Prefer resolving addresses using the configured IPv4 or IPv6 | Default: ipv4
    pref_dns_result: Literal["ipv4", "ipv6", "ipv4-strict", "ipv6-strict"]
    # How to handle HTTP sessions that do not comply with HTTP 0.9 | Default: reject
    unknown_http_version: Literal["reject", "best-effort"]
    # Authentication realm used to identify the explicit web proxy | Default: default | MaxLen: 63
    realm: str
    # Accept or deny explicit web proxy sessions when no web proxy | Default: deny
    sec_default_action: Literal["accept", "deny"]
    # Enable/disable sending the client a replacement message for | Default: enable
    https_replacement_message: Literal["enable", "disable"]
    # Enable/disable displaying a replacement message when a serve | Default: enable
    message_upon_server_error: Literal["enable", "disable"]
    # Enable/disable Proxy Auto-Configuration (PAC) for users of t | Default: disable
    pac_file_server_status: Literal["enable", "disable"]
    # PAC file access URL.
    pac_file_url: str
    # Port number that PAC traffic from client web browsers uses t
    pac_file_server_port: str
    # Enable/disable to get Proxy Auto-Configuration (PAC) through | Default: disable
    pac_file_through_https: Literal["enable", "disable"]
    # Pac file name. | Default: proxy.pac | MaxLen: 63
    pac_file_name: str
    # PAC file contents enclosed in quotes (maximum of 256K bytes)
    pac_file_data: str
    # PAC policies.
    pac_policy: list[ExplicitPacpolicyObject]
    # Relative strength of encryption algorithms accepted in HTTPS | Default: low
    ssl_algorithm: Literal["high", "medium", "low"]
    # Enable/disable logging timed-out authentication requests. | Default: disable
    trace_auth_no_rsp: Literal["enable", "disable"]
    
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
    def to_dict(self) -> ExplicitPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Explicit:
    """
    Configure explicit Web proxy settings.
    
    Path: web_proxy/explicit
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
    ) -> ExplicitObject: ...
    
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
    ) -> ExplicitObject: ...
    
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
    ) -> ExplicitObject: ...
    
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
    ) -> ExplicitObject: ...
    
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
    ) -> ExplicitObject: ...
    
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
    ) -> ExplicitObject: ...
    
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
    ) -> ExplicitObject: ...
    
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
    ) -> ExplicitObject: ...
    
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
    ) -> ExplicitObject: ...
    
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
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> ExplicitObject | dict[str, Any]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: ExplicitPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        secure_web_proxy: Literal["disable", "enable", "secure"] | None = ...,
        ftp_over_http: Literal["enable", "disable"] | None = ...,
        socks: Literal["enable", "disable"] | None = ...,
        http_incoming_port: str | None = ...,
        http_connection_mode: Literal["static", "multiplex", "serverpool"] | None = ...,
        https_incoming_port: str | None = ...,
        secure_web_proxy_cert: str | list[str] | list[dict[str, Any]] | None = ...,
        client_cert: Literal["disable", "enable"] | None = ...,
        user_agent_detect: Literal["disable", "enable"] | None = ...,
        empty_cert_action: Literal["accept", "block", "accept-unmanageable"] | None = ...,
        ssl_dh_bits: Literal["768", "1024", "1536", "2048"] | None = ...,
        ftp_incoming_port: str | None = ...,
        socks_incoming_port: str | None = ...,
        incoming_ip: str | None = ...,
        outgoing_ip: str | list[str] | None = ...,
        interface_select_method: Literal["sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        ipv6_status: Literal["enable", "disable"] | None = ...,
        incoming_ip6: str | None = ...,
        outgoing_ip6: str | list[str] | None = ...,
        strict_guest: Literal["enable", "disable"] | None = ...,
        pref_dns_result: Literal["ipv4", "ipv6", "ipv4-strict", "ipv6-strict"] | None = ...,
        unknown_http_version: Literal["reject", "best-effort"] | None = ...,
        realm: str | None = ...,
        sec_default_action: Literal["accept", "deny"] | None = ...,
        https_replacement_message: Literal["enable", "disable"] | None = ...,
        message_upon_server_error: Literal["enable", "disable"] | None = ...,
        pac_file_server_status: Literal["enable", "disable"] | None = ...,
        pac_file_url: str | None = ...,
        pac_file_server_port: str | None = ...,
        pac_file_through_https: Literal["enable", "disable"] | None = ...,
        pac_file_name: str | None = ...,
        pac_file_data: str | None = ...,
        pac_policy: str | list[str] | list[dict[str, Any]] | None = ...,
        ssl_algorithm: Literal["high", "medium", "low"] | None = ...,
        trace_auth_no_rsp: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> ExplicitObject: ...
    
    @overload
    def put(
        self,
        payload_dict: ExplicitPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        secure_web_proxy: Literal["disable", "enable", "secure"] | None = ...,
        ftp_over_http: Literal["enable", "disable"] | None = ...,
        socks: Literal["enable", "disable"] | None = ...,
        http_incoming_port: str | None = ...,
        http_connection_mode: Literal["static", "multiplex", "serverpool"] | None = ...,
        https_incoming_port: str | None = ...,
        secure_web_proxy_cert: str | list[str] | list[dict[str, Any]] | None = ...,
        client_cert: Literal["disable", "enable"] | None = ...,
        user_agent_detect: Literal["disable", "enable"] | None = ...,
        empty_cert_action: Literal["accept", "block", "accept-unmanageable"] | None = ...,
        ssl_dh_bits: Literal["768", "1024", "1536", "2048"] | None = ...,
        ftp_incoming_port: str | None = ...,
        socks_incoming_port: str | None = ...,
        incoming_ip: str | None = ...,
        outgoing_ip: str | list[str] | None = ...,
        interface_select_method: Literal["sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        ipv6_status: Literal["enable", "disable"] | None = ...,
        incoming_ip6: str | None = ...,
        outgoing_ip6: str | list[str] | None = ...,
        strict_guest: Literal["enable", "disable"] | None = ...,
        pref_dns_result: Literal["ipv4", "ipv6", "ipv4-strict", "ipv6-strict"] | None = ...,
        unknown_http_version: Literal["reject", "best-effort"] | None = ...,
        realm: str | None = ...,
        sec_default_action: Literal["accept", "deny"] | None = ...,
        https_replacement_message: Literal["enable", "disable"] | None = ...,
        message_upon_server_error: Literal["enable", "disable"] | None = ...,
        pac_file_server_status: Literal["enable", "disable"] | None = ...,
        pac_file_url: str | None = ...,
        pac_file_server_port: str | None = ...,
        pac_file_through_https: Literal["enable", "disable"] | None = ...,
        pac_file_name: str | None = ...,
        pac_file_data: str | None = ...,
        pac_policy: str | list[str] | list[dict[str, Any]] | None = ...,
        ssl_algorithm: Literal["high", "medium", "low"] | None = ...,
        trace_auth_no_rsp: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    # raw_json=True returns the full API envelope
    @overload
    def put(
        self,
        payload_dict: ExplicitPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        secure_web_proxy: Literal["disable", "enable", "secure"] | None = ...,
        ftp_over_http: Literal["enable", "disable"] | None = ...,
        socks: Literal["enable", "disable"] | None = ...,
        http_incoming_port: str | None = ...,
        http_connection_mode: Literal["static", "multiplex", "serverpool"] | None = ...,
        https_incoming_port: str | None = ...,
        secure_web_proxy_cert: str | list[str] | list[dict[str, Any]] | None = ...,
        client_cert: Literal["disable", "enable"] | None = ...,
        user_agent_detect: Literal["disable", "enable"] | None = ...,
        empty_cert_action: Literal["accept", "block", "accept-unmanageable"] | None = ...,
        ssl_dh_bits: Literal["768", "1024", "1536", "2048"] | None = ...,
        ftp_incoming_port: str | None = ...,
        socks_incoming_port: str | None = ...,
        incoming_ip: str | None = ...,
        outgoing_ip: str | list[str] | None = ...,
        interface_select_method: Literal["sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        ipv6_status: Literal["enable", "disable"] | None = ...,
        incoming_ip6: str | None = ...,
        outgoing_ip6: str | list[str] | None = ...,
        strict_guest: Literal["enable", "disable"] | None = ...,
        pref_dns_result: Literal["ipv4", "ipv6", "ipv4-strict", "ipv6-strict"] | None = ...,
        unknown_http_version: Literal["reject", "best-effort"] | None = ...,
        realm: str | None = ...,
        sec_default_action: Literal["accept", "deny"] | None = ...,
        https_replacement_message: Literal["enable", "disable"] | None = ...,
        message_upon_server_error: Literal["enable", "disable"] | None = ...,
        pac_file_server_status: Literal["enable", "disable"] | None = ...,
        pac_file_url: str | None = ...,
        pac_file_server_port: str | None = ...,
        pac_file_through_https: Literal["enable", "disable"] | None = ...,
        pac_file_name: str | None = ...,
        pac_file_data: str | None = ...,
        pac_policy: str | list[str] | list[dict[str, Any]] | None = ...,
        ssl_algorithm: Literal["high", "medium", "low"] | None = ...,
        trace_auth_no_rsp: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> RawAPIResponse: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: ExplicitPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        secure_web_proxy: Literal["disable", "enable", "secure"] | None = ...,
        ftp_over_http: Literal["enable", "disable"] | None = ...,
        socks: Literal["enable", "disable"] | None = ...,
        http_incoming_port: str | None = ...,
        http_connection_mode: Literal["static", "multiplex", "serverpool"] | None = ...,
        https_incoming_port: str | None = ...,
        secure_web_proxy_cert: str | list[str] | list[dict[str, Any]] | None = ...,
        client_cert: Literal["disable", "enable"] | None = ...,
        user_agent_detect: Literal["disable", "enable"] | None = ...,
        empty_cert_action: Literal["accept", "block", "accept-unmanageable"] | None = ...,
        ssl_dh_bits: Literal["768", "1024", "1536", "2048"] | None = ...,
        ftp_incoming_port: str | None = ...,
        socks_incoming_port: str | None = ...,
        incoming_ip: str | None = ...,
        outgoing_ip: str | list[str] | None = ...,
        interface_select_method: Literal["sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        ipv6_status: Literal["enable", "disable"] | None = ...,
        incoming_ip6: str | None = ...,
        outgoing_ip6: str | list[str] | None = ...,
        strict_guest: Literal["enable", "disable"] | None = ...,
        pref_dns_result: Literal["ipv4", "ipv6", "ipv4-strict", "ipv6-strict"] | None = ...,
        unknown_http_version: Literal["reject", "best-effort"] | None = ...,
        realm: str | None = ...,
        sec_default_action: Literal["accept", "deny"] | None = ...,
        https_replacement_message: Literal["enable", "disable"] | None = ...,
        message_upon_server_error: Literal["enable", "disable"] | None = ...,
        pac_file_server_status: Literal["enable", "disable"] | None = ...,
        pac_file_url: str | None = ...,
        pac_file_server_port: str | None = ...,
        pac_file_through_https: Literal["enable", "disable"] | None = ...,
        pac_file_name: str | None = ...,
        pac_file_data: str | None = ...,
        pac_policy: str | list[str] | list[dict[str, Any]] | None = ...,
        ssl_algorithm: Literal["high", "medium", "low"] | None = ...,
        trace_auth_no_rsp: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    def put(
        self,
        payload_dict: ExplicitPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        secure_web_proxy: Literal["disable", "enable", "secure"] | None = ...,
        ftp_over_http: Literal["enable", "disable"] | None = ...,
        socks: Literal["enable", "disable"] | None = ...,
        http_incoming_port: str | None = ...,
        http_connection_mode: Literal["static", "multiplex", "serverpool"] | None = ...,
        https_incoming_port: str | None = ...,
        secure_web_proxy_cert: str | list[str] | list[dict[str, Any]] | None = ...,
        client_cert: Literal["disable", "enable"] | None = ...,
        user_agent_detect: Literal["disable", "enable"] | None = ...,
        empty_cert_action: Literal["accept", "block", "accept-unmanageable"] | None = ...,
        ssl_dh_bits: Literal["768", "1024", "1536", "2048"] | None = ...,
        ftp_incoming_port: str | None = ...,
        socks_incoming_port: str | None = ...,
        incoming_ip: str | None = ...,
        outgoing_ip: str | list[str] | None = ...,
        interface_select_method: Literal["sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        ipv6_status: Literal["enable", "disable"] | None = ...,
        incoming_ip6: str | None = ...,
        outgoing_ip6: str | list[str] | None = ...,
        strict_guest: Literal["enable", "disable"] | None = ...,
        pref_dns_result: Literal["ipv4", "ipv6", "ipv4-strict", "ipv6-strict"] | None = ...,
        unknown_http_version: Literal["reject", "best-effort"] | None = ...,
        realm: str | None = ...,
        sec_default_action: Literal["accept", "deny"] | None = ...,
        https_replacement_message: Literal["enable", "disable"] | None = ...,
        message_upon_server_error: Literal["enable", "disable"] | None = ...,
        pac_file_server_status: Literal["enable", "disable"] | None = ...,
        pac_file_url: str | None = ...,
        pac_file_server_port: str | None = ...,
        pac_file_through_https: Literal["enable", "disable"] | None = ...,
        pac_file_name: str | None = ...,
        pac_file_data: str | None = ...,
        pac_policy: str | list[str] | list[dict[str, Any]] | None = ...,
        ssl_algorithm: Literal["high", "medium", "low"] | None = ...,
        trace_auth_no_rsp: Literal["enable", "disable"] | None = ...,
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
        payload_dict: ExplicitPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        secure_web_proxy: Literal["disable", "enable", "secure"] | None = ...,
        ftp_over_http: Literal["enable", "disable"] | None = ...,
        socks: Literal["enable", "disable"] | None = ...,
        http_incoming_port: str | None = ...,
        http_connection_mode: Literal["static", "multiplex", "serverpool"] | None = ...,
        https_incoming_port: str | None = ...,
        secure_web_proxy_cert: str | list[str] | list[dict[str, Any]] | None = ...,
        client_cert: Literal["disable", "enable"] | None = ...,
        user_agent_detect: Literal["disable", "enable"] | None = ...,
        empty_cert_action: Literal["accept", "block", "accept-unmanageable"] | None = ...,
        ssl_dh_bits: Literal["768", "1024", "1536", "2048"] | None = ...,
        ftp_incoming_port: str | None = ...,
        socks_incoming_port: str | None = ...,
        incoming_ip: str | None = ...,
        outgoing_ip: str | list[str] | None = ...,
        interface_select_method: Literal["sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        ipv6_status: Literal["enable", "disable"] | None = ...,
        incoming_ip6: str | None = ...,
        outgoing_ip6: str | list[str] | None = ...,
        strict_guest: Literal["enable", "disable"] | None = ...,
        pref_dns_result: Literal["ipv4", "ipv6", "ipv4-strict", "ipv6-strict"] | None = ...,
        unknown_http_version: Literal["reject", "best-effort"] | None = ...,
        realm: str | None = ...,
        sec_default_action: Literal["accept", "deny"] | None = ...,
        https_replacement_message: Literal["enable", "disable"] | None = ...,
        message_upon_server_error: Literal["enable", "disable"] | None = ...,
        pac_file_server_status: Literal["enable", "disable"] | None = ...,
        pac_file_url: str | None = ...,
        pac_file_server_port: str | None = ...,
        pac_file_through_https: Literal["enable", "disable"] | None = ...,
        pac_file_name: str | None = ...,
        pac_file_data: str | None = ...,
        pac_policy: str | list[str] | list[dict[str, Any]] | None = ...,
        ssl_algorithm: Literal["high", "medium", "low"] | None = ...,
        trace_auth_no_rsp: Literal["enable", "disable"] | None = ...,
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
    "Explicit",
    "ExplicitPayload",
    "ExplicitResponse",
    "ExplicitObject",
]