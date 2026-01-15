from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject
from hfortix_core.types import MutationResponse, RawAPIResponse

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class NetflowPayload(TypedDict, total=False):
    """
    Type hints for system/netflow payload fields.
    
    Configure NetFlow.
    
    **Usage:**
        payload: NetflowPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    active_flow_timeout: int  # Timeout to report active flows | Default: 1800 | Min: 60 | Max: 3600
    inactive_flow_timeout: int  # Timeout for periodic report of finished flows | Default: 15 | Min: 10 | Max: 600
    template_tx_timeout: int  # Timeout for periodic template flowset transmission | Default: 1800 | Min: 60 | Max: 86400
    template_tx_counter: int  # Counter of flowset records before resending a temp | Default: 20 | Min: 10 | Max: 6000
    session_cache_size: Literal["min", "default", "max"]  # Maximum RAM usage allowed for Netflow session cach | Default: default
    exclusion_filters: list[dict[str, Any]]  # Exclusion filters
    collectors: list[dict[str, Any]]  # Netflow collectors.

# Nested TypedDicts for table field children (dict mode)

class NetflowExclusionfiltersItem(TypedDict):
    """Type hints for exclusion-filters table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    id: int  # Filter ID. | Default: 0 | Min: 0 | Max: 4294967295
    source_ip: str  # Session source address.
    destination_ip: str  # Session destination address.
    source_port: str  # Session source port number or range.
    destination_port: str  # Session destination port number or range.
    protocol: int  # Session IP protocol | Default: 255 | Min: 0 | Max: 255


class NetflowCollectorsItem(TypedDict):
    """Type hints for collectors table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    id: int  # ID. | Default: 0 | Min: 1 | Max: 6
    collector_ip: str  # Collector IP. | MaxLen: 63
    collector_port: int  # NetFlow collector port number. | Default: 2055 | Min: 0 | Max: 65535
    source_ip: str  # Source IP address for communication with the NetFl | MaxLen: 63
    source_ip_interface: str  # Name of the interface used to determine the source | MaxLen: 15
    interface_select_method: Literal["auto", "sdwan", "specify"]  # Specify how to select outgoing interface to reach | Default: auto
    interface: str  # Specify outgoing interface to reach server. | MaxLen: 15
    vrf_select: int  # VRF ID used for connection to server. | Default: 0 | Min: 0 | Max: 511


# Nested classes for table field children (object mode)

@final
class NetflowExclusionfiltersObject:
    """Typed object for exclusion-filters table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Filter ID. | Default: 0 | Min: 0 | Max: 4294967295
    id: int
    # Session source address.
    source_ip: str
    # Session destination address.
    destination_ip: str
    # Session source port number or range.
    source_port: str
    # Session destination port number or range.
    destination_port: str
    # Session IP protocol (0 - 255, default = 255, meaning any). | Default: 255 | Min: 0 | Max: 255
    protocol: int
    
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
class NetflowCollectorsObject:
    """Typed object for collectors table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # ID. | Default: 0 | Min: 1 | Max: 6
    id: int
    # Collector IP. | MaxLen: 63
    collector_ip: str
    # NetFlow collector port number. | Default: 2055 | Min: 0 | Max: 65535
    collector_port: int
    # Source IP address for communication with the NetFlow agent. | MaxLen: 63
    source_ip: str
    # Name of the interface used to determine the source IP for ex | MaxLen: 15
    source_ip_interface: str
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



# Response TypedDict for GET returns (all fields present in API response)
class NetflowResponse(TypedDict):
    """
    Type hints for system/netflow API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    active_flow_timeout: int  # Timeout to report active flows | Default: 1800 | Min: 60 | Max: 3600
    inactive_flow_timeout: int  # Timeout for periodic report of finished flows | Default: 15 | Min: 10 | Max: 600
    template_tx_timeout: int  # Timeout for periodic template flowset transmission | Default: 1800 | Min: 60 | Max: 86400
    template_tx_counter: int  # Counter of flowset records before resending a temp | Default: 20 | Min: 10 | Max: 6000
    session_cache_size: Literal["min", "default", "max"]  # Maximum RAM usage allowed for Netflow session cach | Default: default
    exclusion_filters: list[NetflowExclusionfiltersItem]  # Exclusion filters
    collectors: list[NetflowCollectorsItem]  # Netflow collectors.


@final
class NetflowObject:
    """Typed FortiObject for system/netflow with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Timeout to report active flows | Default: 1800 | Min: 60 | Max: 3600
    active_flow_timeout: int
    # Timeout for periodic report of finished flows | Default: 15 | Min: 10 | Max: 600
    inactive_flow_timeout: int
    # Timeout for periodic template flowset transmission | Default: 1800 | Min: 60 | Max: 86400
    template_tx_timeout: int
    # Counter of flowset records before resending a template flows | Default: 20 | Min: 10 | Max: 6000
    template_tx_counter: int
    # Maximum RAM usage allowed for Netflow session cache. | Default: default
    session_cache_size: Literal["min", "default", "max"]
    # Exclusion filters
    exclusion_filters: list[NetflowExclusionfiltersObject]
    # Netflow collectors.
    collectors: list[NetflowCollectorsObject]
    
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
    def to_dict(self) -> NetflowPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Netflow:
    """
    Configure NetFlow.
    
    Path: system/netflow
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
    ) -> NetflowObject: ...
    
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
    ) -> NetflowObject: ...
    
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
    ) -> NetflowObject: ...
    
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
    ) -> NetflowObject: ...
    
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
    ) -> NetflowObject: ...
    
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
    ) -> NetflowObject: ...
    
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
    ) -> NetflowObject: ...
    
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
    ) -> NetflowObject: ...
    
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
    ) -> NetflowObject: ...
    
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
    ) -> NetflowObject | dict[str, Any]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: NetflowPayload | None = ...,
        active_flow_timeout: int | None = ...,
        inactive_flow_timeout: int | None = ...,
        template_tx_timeout: int | None = ...,
        template_tx_counter: int | None = ...,
        session_cache_size: Literal["min", "default", "max"] | None = ...,
        exclusion_filters: str | list[str] | list[dict[str, Any]] | None = ...,
        collectors: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> NetflowObject: ...
    
    @overload
    def put(
        self,
        payload_dict: NetflowPayload | None = ...,
        active_flow_timeout: int | None = ...,
        inactive_flow_timeout: int | None = ...,
        template_tx_timeout: int | None = ...,
        template_tx_counter: int | None = ...,
        session_cache_size: Literal["min", "default", "max"] | None = ...,
        exclusion_filters: str | list[str] | list[dict[str, Any]] | None = ...,
        collectors: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    # raw_json=True returns the full API envelope
    @overload
    def put(
        self,
        payload_dict: NetflowPayload | None = ...,
        active_flow_timeout: int | None = ...,
        inactive_flow_timeout: int | None = ...,
        template_tx_timeout: int | None = ...,
        template_tx_counter: int | None = ...,
        session_cache_size: Literal["min", "default", "max"] | None = ...,
        exclusion_filters: str | list[str] | list[dict[str, Any]] | None = ...,
        collectors: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> RawAPIResponse: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: NetflowPayload | None = ...,
        active_flow_timeout: int | None = ...,
        inactive_flow_timeout: int | None = ...,
        template_tx_timeout: int | None = ...,
        template_tx_counter: int | None = ...,
        session_cache_size: Literal["min", "default", "max"] | None = ...,
        exclusion_filters: str | list[str] | list[dict[str, Any]] | None = ...,
        collectors: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    def put(
        self,
        payload_dict: NetflowPayload | None = ...,
        active_flow_timeout: int | None = ...,
        inactive_flow_timeout: int | None = ...,
        template_tx_timeout: int | None = ...,
        template_tx_counter: int | None = ...,
        session_cache_size: Literal["min", "default", "max"] | None = ...,
        exclusion_filters: str | list[str] | list[dict[str, Any]] | None = ...,
        collectors: str | list[str] | list[dict[str, Any]] | None = ...,
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
        payload_dict: NetflowPayload | None = ...,
        active_flow_timeout: int | None = ...,
        inactive_flow_timeout: int | None = ...,
        template_tx_timeout: int | None = ...,
        template_tx_counter: int | None = ...,
        session_cache_size: Literal["min", "default", "max"] | None = ...,
        exclusion_filters: str | list[str] | list[dict[str, Any]] | None = ...,
        collectors: str | list[str] | list[dict[str, Any]] | None = ...,
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
    "Netflow",
    "NetflowPayload",
    "NetflowResponse",
    "NetflowObject",
]