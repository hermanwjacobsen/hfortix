from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject
from hfortix_core.types import MutationResponse, RawAPIResponse

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class TacacsPlusPayload(TypedDict, total=False):
    """
    Type hints for user/tacacs_plus payload fields.
    
    Configure TACACS+ server entries.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.system.interface.InterfaceEndpoint` (via: interface)

    **Usage:**
        payload: TacacsPlusPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # TACACS+ server entry name. | MaxLen: 35
    server: str  # Primary TACACS+ server CN domain name or IP addres | MaxLen: 63
    secondary_server: str  # Secondary TACACS+ server CN domain name or IP addr | MaxLen: 63
    tertiary_server: str  # Tertiary TACACS+ server CN domain name or IP addre | MaxLen: 63
    port: int  # Port number of the TACACS+ server. | Default: 49 | Min: 1 | Max: 65535
    key: str  # Key to access the primary server. | MaxLen: 128
    secondary_key: str  # Key to access the secondary server. | MaxLen: 128
    tertiary_key: str  # Key to access the tertiary server. | MaxLen: 128
    status_ttl: int  # Time for which server reachability is cached so th | Default: 300 | Min: 0 | Max: 600
    authen_type: Literal["mschap", "chap", "pap", "ascii", "auto"]  # Allowed authentication protocols/methods. | Default: auto
    authorization: Literal["enable", "disable"]  # Enable/disable TACACS+ authorization. | Default: disable
    source_ip: str  # Source IP address for communications to TACACS+ se | MaxLen: 63
    interface_select_method: Literal["auto", "sdwan", "specify"]  # Specify how to select outgoing interface to reach | Default: auto
    interface: str  # Specify outgoing interface to reach server. | MaxLen: 15
    vrf_select: int  # VRF ID used for connection to server. | Default: 0 | Min: 0 | Max: 511

# Nested TypedDicts for table field children (dict mode)

# Nested classes for table field children (object mode)


# Response TypedDict for GET returns (all fields present in API response)
class TacacsPlusResponse(TypedDict):
    """
    Type hints for user/tacacs_plus API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str  # TACACS+ server entry name. | MaxLen: 35
    server: str  # Primary TACACS+ server CN domain name or IP addres | MaxLen: 63
    secondary_server: str  # Secondary TACACS+ server CN domain name or IP addr | MaxLen: 63
    tertiary_server: str  # Tertiary TACACS+ server CN domain name or IP addre | MaxLen: 63
    port: int  # Port number of the TACACS+ server. | Default: 49 | Min: 1 | Max: 65535
    key: str  # Key to access the primary server. | MaxLen: 128
    secondary_key: str  # Key to access the secondary server. | MaxLen: 128
    tertiary_key: str  # Key to access the tertiary server. | MaxLen: 128
    status_ttl: int  # Time for which server reachability is cached so th | Default: 300 | Min: 0 | Max: 600
    authen_type: Literal["mschap", "chap", "pap", "ascii", "auto"]  # Allowed authentication protocols/methods. | Default: auto
    authorization: Literal["enable", "disable"]  # Enable/disable TACACS+ authorization. | Default: disable
    source_ip: str  # Source IP address for communications to TACACS+ se | MaxLen: 63
    interface_select_method: Literal["auto", "sdwan", "specify"]  # Specify how to select outgoing interface to reach | Default: auto
    interface: str  # Specify outgoing interface to reach server. | MaxLen: 15
    vrf_select: int  # VRF ID used for connection to server. | Default: 0 | Min: 0 | Max: 511


@final
class TacacsPlusObject:
    """Typed FortiObject for user/tacacs_plus with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # TACACS+ server entry name. | MaxLen: 35
    name: str
    # Primary TACACS+ server CN domain name or IP address. | MaxLen: 63
    server: str
    # Secondary TACACS+ server CN domain name or IP address. | MaxLen: 63
    secondary_server: str
    # Tertiary TACACS+ server CN domain name or IP address. | MaxLen: 63
    tertiary_server: str
    # Port number of the TACACS+ server. | Default: 49 | Min: 1 | Max: 65535
    port: int
    # Key to access the primary server. | MaxLen: 128
    key: str
    # Key to access the secondary server. | MaxLen: 128
    secondary_key: str
    # Key to access the tertiary server. | MaxLen: 128
    tertiary_key: str
    # Time for which server reachability is cached so that when a | Default: 300 | Min: 0 | Max: 600
    status_ttl: int
    # Allowed authentication protocols/methods. | Default: auto
    authen_type: Literal["mschap", "chap", "pap", "ascii", "auto"]
    # Enable/disable TACACS+ authorization. | Default: disable
    authorization: Literal["enable", "disable"]
    # Source IP address for communications to TACACS+ server. | MaxLen: 63
    source_ip: str
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
    def to_dict(self) -> TacacsPlusPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class TacacsPlus:
    """
    Configure TACACS+ server entries.
    
    Path: user/tacacs_plus
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
    ) -> TacacsPlusObject: ...
    
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
    ) -> TacacsPlusObject: ...
    
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
    ) -> list[TacacsPlusObject]: ...
    
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
    ) -> TacacsPlusObject: ...
    
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
    ) -> TacacsPlusObject: ...
    
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
    ) -> list[TacacsPlusObject]: ...
    
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
    ) -> TacacsPlusObject: ...
    
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
    ) -> TacacsPlusObject: ...
    
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
    ) -> list[TacacsPlusObject]: ...
    
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
    ) -> TacacsPlusObject | list[TacacsPlusObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: TacacsPlusPayload | None = ...,
        name: str | None = ...,
        server: str | None = ...,
        secondary_server: str | None = ...,
        tertiary_server: str | None = ...,
        port: int | None = ...,
        key: str | None = ...,
        secondary_key: str | None = ...,
        tertiary_key: str | None = ...,
        status_ttl: int | None = ...,
        authen_type: Literal["mschap", "chap", "pap", "ascii", "auto"] | None = ...,
        authorization: Literal["enable", "disable"] | None = ...,
        source_ip: str | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> TacacsPlusObject: ...
    
    @overload
    def post(
        self,
        payload_dict: TacacsPlusPayload | None = ...,
        name: str | None = ...,
        server: str | None = ...,
        secondary_server: str | None = ...,
        tertiary_server: str | None = ...,
        port: int | None = ...,
        key: str | None = ...,
        secondary_key: str | None = ...,
        tertiary_key: str | None = ...,
        status_ttl: int | None = ...,
        authen_type: Literal["mschap", "chap", "pap", "ascii", "auto"] | None = ...,
        authorization: Literal["enable", "disable"] | None = ...,
        source_ip: str | None = ...,
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
        payload_dict: TacacsPlusPayload | None = ...,
        name: str | None = ...,
        server: str | None = ...,
        secondary_server: str | None = ...,
        tertiary_server: str | None = ...,
        port: int | None = ...,
        key: str | None = ...,
        secondary_key: str | None = ...,
        tertiary_key: str | None = ...,
        status_ttl: int | None = ...,
        authen_type: Literal["mschap", "chap", "pap", "ascii", "auto"] | None = ...,
        authorization: Literal["enable", "disable"] | None = ...,
        source_ip: str | None = ...,
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
        payload_dict: TacacsPlusPayload | None = ...,
        name: str | None = ...,
        server: str | None = ...,
        secondary_server: str | None = ...,
        tertiary_server: str | None = ...,
        port: int | None = ...,
        key: str | None = ...,
        secondary_key: str | None = ...,
        tertiary_key: str | None = ...,
        status_ttl: int | None = ...,
        authen_type: Literal["mschap", "chap", "pap", "ascii", "auto"] | None = ...,
        authorization: Literal["enable", "disable"] | None = ...,
        source_ip: str | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        vdom: str | bool | None = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    def post(
        self,
        payload_dict: TacacsPlusPayload | None = ...,
        name: str | None = ...,
        server: str | None = ...,
        secondary_server: str | None = ...,
        tertiary_server: str | None = ...,
        port: int | None = ...,
        key: str | None = ...,
        secondary_key: str | None = ...,
        tertiary_key: str | None = ...,
        status_ttl: int | None = ...,
        authen_type: Literal["mschap", "chap", "pap", "ascii", "auto"] | None = ...,
        authorization: Literal["enable", "disable"] | None = ...,
        source_ip: str | None = ...,
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
        payload_dict: TacacsPlusPayload | None = ...,
        name: str | None = ...,
        server: str | None = ...,
        secondary_server: str | None = ...,
        tertiary_server: str | None = ...,
        port: int | None = ...,
        key: str | None = ...,
        secondary_key: str | None = ...,
        tertiary_key: str | None = ...,
        status_ttl: int | None = ...,
        authen_type: Literal["mschap", "chap", "pap", "ascii", "auto"] | None = ...,
        authorization: Literal["enable", "disable"] | None = ...,
        source_ip: str | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> TacacsPlusObject: ...
    
    @overload
    def put(
        self,
        payload_dict: TacacsPlusPayload | None = ...,
        name: str | None = ...,
        server: str | None = ...,
        secondary_server: str | None = ...,
        tertiary_server: str | None = ...,
        port: int | None = ...,
        key: str | None = ...,
        secondary_key: str | None = ...,
        tertiary_key: str | None = ...,
        status_ttl: int | None = ...,
        authen_type: Literal["mschap", "chap", "pap", "ascii", "auto"] | None = ...,
        authorization: Literal["enable", "disable"] | None = ...,
        source_ip: str | None = ...,
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
        payload_dict: TacacsPlusPayload | None = ...,
        name: str | None = ...,
        server: str | None = ...,
        secondary_server: str | None = ...,
        tertiary_server: str | None = ...,
        port: int | None = ...,
        key: str | None = ...,
        secondary_key: str | None = ...,
        tertiary_key: str | None = ...,
        status_ttl: int | None = ...,
        authen_type: Literal["mschap", "chap", "pap", "ascii", "auto"] | None = ...,
        authorization: Literal["enable", "disable"] | None = ...,
        source_ip: str | None = ...,
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
        payload_dict: TacacsPlusPayload | None = ...,
        name: str | None = ...,
        server: str | None = ...,
        secondary_server: str | None = ...,
        tertiary_server: str | None = ...,
        port: int | None = ...,
        key: str | None = ...,
        secondary_key: str | None = ...,
        tertiary_key: str | None = ...,
        status_ttl: int | None = ...,
        authen_type: Literal["mschap", "chap", "pap", "ascii", "auto"] | None = ...,
        authorization: Literal["enable", "disable"] | None = ...,
        source_ip: str | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        vdom: str | bool | None = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    def put(
        self,
        payload_dict: TacacsPlusPayload | None = ...,
        name: str | None = ...,
        server: str | None = ...,
        secondary_server: str | None = ...,
        tertiary_server: str | None = ...,
        port: int | None = ...,
        key: str | None = ...,
        secondary_key: str | None = ...,
        tertiary_key: str | None = ...,
        status_ttl: int | None = ...,
        authen_type: Literal["mschap", "chap", "pap", "ascii", "auto"] | None = ...,
        authorization: Literal["enable", "disable"] | None = ...,
        source_ip: str | None = ...,
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
    ) -> TacacsPlusObject: ...
    
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
        payload_dict: TacacsPlusPayload | None = ...,
        name: str | None = ...,
        server: str | None = ...,
        secondary_server: str | None = ...,
        tertiary_server: str | None = ...,
        port: int | None = ...,
        key: str | None = ...,
        secondary_key: str | None = ...,
        tertiary_key: str | None = ...,
        status_ttl: int | None = ...,
        authen_type: Literal["mschap", "chap", "pap", "ascii", "auto"] | None = ...,
        authorization: Literal["enable", "disable"] | None = ...,
        source_ip: str | None = ...,
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
    "TacacsPlus",
    "TacacsPlusPayload",
    "TacacsPlusResponse",
    "TacacsPlusObject",
]