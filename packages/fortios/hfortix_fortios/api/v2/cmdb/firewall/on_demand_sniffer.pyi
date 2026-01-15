from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class OnDemandSnifferPayload(TypedDict, total=False):
    """
    Type hints for firewall/on_demand_sniffer payload fields.
    
    Configure on-demand packet sniffer.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.system.interface.InterfaceEndpoint` (via: interface)

    **Usage:**
        payload: OnDemandSnifferPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # On-demand packet sniffer name. | MaxLen: 35
    interface: str  # Interface name that on-demand packet sniffer will | MaxLen: 35
    max_packet_count: int  # Maximum number of packets to capture per on-demand | Default: 0 | Min: 1 | Max: 20000
    hosts: list[dict[str, Any]]  # IPv4 or IPv6 hosts to filter in this traffic sniff
    ports: list[dict[str, Any]]  # Ports to filter for in this traffic sniffer.
    protocols: list[dict[str, Any]]  # Protocols to filter in this traffic sniffer.
    non_ip_packet: Literal["enable", "disable"]  # Include non-IP packets. | Default: disable
    advanced_filter: str  # Advanced freeform filter that will be used over ex | MaxLen: 255

# Nested TypedDicts for table field children (dict mode)

class OnDemandSnifferHostsItem(TypedDict):
    """Type hints for hosts table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    host: str  # IPv4 or IPv6 host. | MaxLen: 255


class OnDemandSnifferPortsItem(TypedDict):
    """Type hints for ports table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    port: int  # Port to filter in this traffic sniffer. | Default: 0 | Min: 1 | Max: 65536


class OnDemandSnifferProtocolsItem(TypedDict):
    """Type hints for protocols table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    protocol: int  # Integer value for the protocol type as defined by | Default: 0 | Min: 0 | Max: 255


# Nested classes for table field children (object mode)

@final
class OnDemandSnifferHostsObject:
    """Typed object for hosts table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # IPv4 or IPv6 host. | MaxLen: 255
    host: str
    
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
class OnDemandSnifferPortsObject:
    """Typed object for ports table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Port to filter in this traffic sniffer. | Default: 0 | Min: 1 | Max: 65536
    port: int
    
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
class OnDemandSnifferProtocolsObject:
    """Typed object for protocols table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Integer value for the protocol type as defined by IANA | Default: 0 | Min: 0 | Max: 255
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



# Response TypedDict for GET returns (all fields present in API response)
class OnDemandSnifferResponse(TypedDict):
    """
    Type hints for firewall/on_demand_sniffer API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str  # On-demand packet sniffer name. | MaxLen: 35
    interface: str  # Interface name that on-demand packet sniffer will | MaxLen: 35
    max_packet_count: int  # Maximum number of packets to capture per on-demand | Default: 0 | Min: 1 | Max: 20000
    hosts: list[OnDemandSnifferHostsItem]  # IPv4 or IPv6 hosts to filter in this traffic sniff
    ports: list[OnDemandSnifferPortsItem]  # Ports to filter for in this traffic sniffer.
    protocols: list[OnDemandSnifferProtocolsItem]  # Protocols to filter in this traffic sniffer.
    non_ip_packet: Literal["enable", "disable"]  # Include non-IP packets. | Default: disable
    advanced_filter: str  # Advanced freeform filter that will be used over ex | MaxLen: 255


@final
class OnDemandSnifferObject:
    """Typed FortiObject for firewall/on_demand_sniffer with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # On-demand packet sniffer name. | MaxLen: 35
    name: str
    # Interface name that on-demand packet sniffer will take place | MaxLen: 35
    interface: str
    # Maximum number of packets to capture per on-demand packet sn | Default: 0 | Min: 1 | Max: 20000
    max_packet_count: int
    # IPv4 or IPv6 hosts to filter in this traffic sniffer.
    hosts: list[OnDemandSnifferHostsObject]
    # Ports to filter for in this traffic sniffer.
    ports: list[OnDemandSnifferPortsObject]
    # Protocols to filter in this traffic sniffer.
    protocols: list[OnDemandSnifferProtocolsObject]
    # Include non-IP packets. | Default: disable
    non_ip_packet: Literal["enable", "disable"]
    # Advanced freeform filter that will be used over existing fil | MaxLen: 255
    advanced_filter: str
    
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
    def to_dict(self) -> OnDemandSnifferPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class OnDemandSniffer:
    """
    Configure on-demand packet sniffer.
    
    Path: firewall/on_demand_sniffer
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
    ) -> OnDemandSnifferObject: ...
    
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
    ) -> OnDemandSnifferObject: ...
    
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
    ) -> FortiObjectList[OnDemandSnifferObject]: ...
    
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
    ) -> OnDemandSnifferObject: ...
    
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
    ) -> OnDemandSnifferObject: ...
    
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
    ) -> FortiObjectList[OnDemandSnifferObject]: ...
    
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
    ) -> OnDemandSnifferObject: ...
    
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
    ) -> OnDemandSnifferObject: ...
    
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
    ) -> FortiObjectList[OnDemandSnifferObject]: ...
    
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
    ) -> OnDemandSnifferObject | list[OnDemandSnifferObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: OnDemandSnifferPayload | None = ...,
        name: str | None = ...,
        interface: str | None = ...,
        max_packet_count: int | None = ...,
        hosts: str | list[str] | list[dict[str, Any]] | None = ...,
        ports: str | list[str] | list[dict[str, Any]] | None = ...,
        protocols: str | list[str] | list[dict[str, Any]] | None = ...,
        non_ip_packet: Literal["enable", "disable"] | None = ...,
        advanced_filter: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> OnDemandSnifferObject: ...
    
    @overload
    def post(
        self,
        payload_dict: OnDemandSnifferPayload | None = ...,
        name: str | None = ...,
        interface: str | None = ...,
        max_packet_count: int | None = ...,
        hosts: str | list[str] | list[dict[str, Any]] | None = ...,
        ports: str | list[str] | list[dict[str, Any]] | None = ...,
        protocols: str | list[str] | list[dict[str, Any]] | None = ...,
        non_ip_packet: Literal["enable", "disable"] | None = ...,
        advanced_filter: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: OnDemandSnifferPayload | None = ...,
        name: str | None = ...,
        interface: str | None = ...,
        max_packet_count: int | None = ...,
        hosts: str | list[str] | list[dict[str, Any]] | None = ...,
        ports: str | list[str] | list[dict[str, Any]] | None = ...,
        protocols: str | list[str] | list[dict[str, Any]] | None = ...,
        non_ip_packet: Literal["enable", "disable"] | None = ...,
        advanced_filter: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def post(
        self,
        payload_dict: OnDemandSnifferPayload | None = ...,
        name: str | None = ...,
        interface: str | None = ...,
        max_packet_count: int | None = ...,
        hosts: str | list[str] | list[dict[str, Any]] | None = ...,
        ports: str | list[str] | list[dict[str, Any]] | None = ...,
        protocols: str | list[str] | list[dict[str, Any]] | None = ...,
        non_ip_packet: Literal["enable", "disable"] | None = ...,
        advanced_filter: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: OnDemandSnifferPayload | None = ...,
        name: str | None = ...,
        interface: str | None = ...,
        max_packet_count: int | None = ...,
        hosts: str | list[str] | list[dict[str, Any]] | None = ...,
        ports: str | list[str] | list[dict[str, Any]] | None = ...,
        protocols: str | list[str] | list[dict[str, Any]] | None = ...,
        non_ip_packet: Literal["enable", "disable"] | None = ...,
        advanced_filter: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> OnDemandSnifferObject: ...
    
    @overload
    def put(
        self,
        payload_dict: OnDemandSnifferPayload | None = ...,
        name: str | None = ...,
        interface: str | None = ...,
        max_packet_count: int | None = ...,
        hosts: str | list[str] | list[dict[str, Any]] | None = ...,
        ports: str | list[str] | list[dict[str, Any]] | None = ...,
        protocols: str | list[str] | list[dict[str, Any]] | None = ...,
        non_ip_packet: Literal["enable", "disable"] | None = ...,
        advanced_filter: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: OnDemandSnifferPayload | None = ...,
        name: str | None = ...,
        interface: str | None = ...,
        max_packet_count: int | None = ...,
        hosts: str | list[str] | list[dict[str, Any]] | None = ...,
        ports: str | list[str] | list[dict[str, Any]] | None = ...,
        protocols: str | list[str] | list[dict[str, Any]] | None = ...,
        non_ip_packet: Literal["enable", "disable"] | None = ...,
        advanced_filter: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def put(
        self,
        payload_dict: OnDemandSnifferPayload | None = ...,
        name: str | None = ...,
        interface: str | None = ...,
        max_packet_count: int | None = ...,
        hosts: str | list[str] | list[dict[str, Any]] | None = ...,
        ports: str | list[str] | list[dict[str, Any]] | None = ...,
        protocols: str | list[str] | list[dict[str, Any]] | None = ...,
        non_ip_packet: Literal["enable", "disable"] | None = ...,
        advanced_filter: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> OnDemandSnifferObject: ...
    
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
        payload_dict: OnDemandSnifferPayload | None = ...,
        name: str | None = ...,
        interface: str | None = ...,
        max_packet_count: int | None = ...,
        hosts: str | list[str] | list[dict[str, Any]] | None = ...,
        ports: str | list[str] | list[dict[str, Any]] | None = ...,
        protocols: str | list[str] | list[dict[str, Any]] | None = ...,
        non_ip_packet: Literal["enable", "disable"] | None = ...,
        advanced_filter: str | None = ...,
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
    "OnDemandSniffer",
    "OnDemandSnifferPayload",
    "OnDemandSnifferResponse",
    "OnDemandSnifferObject",
]