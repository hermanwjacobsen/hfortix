from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList
from hfortix_core.types import MutationResponse

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class GenevePayload(TypedDict, total=False):
    """
    Type hints for system/geneve payload fields.
    
    Configure GENEVE devices.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.system.interface.InterfaceEndpoint` (via: interface)

    **Usage:**
        payload: GenevePayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # GENEVE device or interface name. Must be an unique | MaxLen: 15
    interface: str  # Outgoing interface for GENEVE encapsulated traffic | MaxLen: 15
    vni: int  # GENEVE network ID. | Default: 0 | Min: 0 | Max: 16777215
    type: Literal["ethernet", "ppp"]  # GENEVE type. | Default: ethernet
    ip_version: Literal["ipv4-unicast", "ipv6-unicast"]  # IP version to use for the GENEVE interface and so | Default: ipv4-unicast
    remote_ip: str  # IPv4 address of the GENEVE interface on the device | Default: 0.0.0.0
    remote_ip6: str  # IPv6 IP address of the GENEVE interface on the dev | Default: ::
    dstport: int  # GENEVE destination port | Default: 6081 | Min: 1 | Max: 65535

# Nested TypedDicts for table field children (dict mode)

# Nested classes for table field children (object mode)


# Response TypedDict for GET returns (all fields present in API response)
class GeneveResponse(TypedDict):
    """
    Type hints for system/geneve API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str  # GENEVE device or interface name. Must be an unique | MaxLen: 15
    interface: str  # Outgoing interface for GENEVE encapsulated traffic | MaxLen: 15
    vni: int  # GENEVE network ID. | Default: 0 | Min: 0 | Max: 16777215
    type: Literal["ethernet", "ppp"]  # GENEVE type. | Default: ethernet
    ip_version: Literal["ipv4-unicast", "ipv6-unicast"]  # IP version to use for the GENEVE interface and so | Default: ipv4-unicast
    remote_ip: str  # IPv4 address of the GENEVE interface on the device | Default: 0.0.0.0
    remote_ip6: str  # IPv6 IP address of the GENEVE interface on the dev | Default: ::
    dstport: int  # GENEVE destination port | Default: 6081 | Min: 1 | Max: 65535


@final
class GeneveObject:
    """Typed FortiObject for system/geneve with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # GENEVE device or interface name. Must be an unique interface | MaxLen: 15
    name: str
    # Outgoing interface for GENEVE encapsulated traffic. | MaxLen: 15
    interface: str
    # GENEVE network ID. | Default: 0 | Min: 0 | Max: 16777215
    vni: int
    # GENEVE type. | Default: ethernet
    type: Literal["ethernet", "ppp"]
    # IP version to use for the GENEVE interface and so for commun | Default: ipv4-unicast
    ip_version: Literal["ipv4-unicast", "ipv6-unicast"]
    # IPv4 address of the GENEVE interface on the device at the re | Default: 0.0.0.0
    remote_ip: str
    # IPv6 IP address of the GENEVE interface on the device at the | Default: ::
    remote_ip6: str
    # GENEVE destination port (1 - 65535, default = 6081). | Default: 6081 | Min: 1 | Max: 65535
    dstport: int
    
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
    def to_dict(self) -> GenevePayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Geneve:
    """
    Configure GENEVE devices.
    
    Path: system/geneve
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
    ) -> GeneveObject: ...
    
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
    ) -> GeneveObject: ...
    
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
    ) -> FortiObjectList[GeneveObject]: ...
    
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
    ) -> GeneveObject: ...
    
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
    ) -> GeneveObject: ...
    
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
    ) -> FortiObjectList[GeneveObject]: ...
    
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
    ) -> GeneveObject: ...
    
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
    ) -> GeneveObject: ...
    
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
    ) -> FortiObjectList[GeneveObject]: ...
    
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
    ) -> GeneveObject | list[GeneveObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: GenevePayload | None = ...,
        name: str | None = ...,
        interface: str | None = ...,
        vni: int | None = ...,
        type: Literal["ethernet", "ppp"] | None = ...,
        ip_version: Literal["ipv4-unicast", "ipv6-unicast"] | None = ...,
        remote_ip: str | None = ...,
        remote_ip6: str | None = ...,
        dstport: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> GeneveObject: ...
    
    @overload
    def post(
        self,
        payload_dict: GenevePayload | None = ...,
        name: str | None = ...,
        interface: str | None = ...,
        vni: int | None = ...,
        type: Literal["ethernet", "ppp"] | None = ...,
        ip_version: Literal["ipv4-unicast", "ipv6-unicast"] | None = ...,
        remote_ip: str | None = ...,
        remote_ip6: str | None = ...,
        dstport: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: GenevePayload | None = ...,
        name: str | None = ...,
        interface: str | None = ...,
        vni: int | None = ...,
        type: Literal["ethernet", "ppp"] | None = ...,
        ip_version: Literal["ipv4-unicast", "ipv6-unicast"] | None = ...,
        remote_ip: str | None = ...,
        remote_ip6: str | None = ...,
        dstport: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def post(
        self,
        payload_dict: GenevePayload | None = ...,
        name: str | None = ...,
        interface: str | None = ...,
        vni: int | None = ...,
        type: Literal["ethernet", "ppp"] | None = ...,
        ip_version: Literal["ipv4-unicast", "ipv6-unicast"] | None = ...,
        remote_ip: str | None = ...,
        remote_ip6: str | None = ...,
        dstport: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: GenevePayload | None = ...,
        name: str | None = ...,
        interface: str | None = ...,
        vni: int | None = ...,
        type: Literal["ethernet", "ppp"] | None = ...,
        ip_version: Literal["ipv4-unicast", "ipv6-unicast"] | None = ...,
        remote_ip: str | None = ...,
        remote_ip6: str | None = ...,
        dstport: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> GeneveObject: ...
    
    @overload
    def put(
        self,
        payload_dict: GenevePayload | None = ...,
        name: str | None = ...,
        interface: str | None = ...,
        vni: int | None = ...,
        type: Literal["ethernet", "ppp"] | None = ...,
        ip_version: Literal["ipv4-unicast", "ipv6-unicast"] | None = ...,
        remote_ip: str | None = ...,
        remote_ip6: str | None = ...,
        dstport: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: GenevePayload | None = ...,
        name: str | None = ...,
        interface: str | None = ...,
        vni: int | None = ...,
        type: Literal["ethernet", "ppp"] | None = ...,
        ip_version: Literal["ipv4-unicast", "ipv6-unicast"] | None = ...,
        remote_ip: str | None = ...,
        remote_ip6: str | None = ...,
        dstport: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def put(
        self,
        payload_dict: GenevePayload | None = ...,
        name: str | None = ...,
        interface: str | None = ...,
        vni: int | None = ...,
        type: Literal["ethernet", "ppp"] | None = ...,
        ip_version: Literal["ipv4-unicast", "ipv6-unicast"] | None = ...,
        remote_ip: str | None = ...,
        remote_ip6: str | None = ...,
        dstport: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> GeneveObject: ...
    
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
        payload_dict: GenevePayload | None = ...,
        name: str | None = ...,
        interface: str | None = ...,
        vni: int | None = ...,
        type: Literal["ethernet", "ppp"] | None = ...,
        ip_version: Literal["ipv4-unicast", "ipv6-unicast"] | None = ...,
        remote_ip: str | None = ...,
        remote_ip6: str | None = ...,
        dstport: int | None = ...,
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
    "Geneve",
    "GenevePayload",
    "GeneveResponse",
    "GeneveObject",
]