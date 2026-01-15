from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList
from hfortix_core.types import MutationResponse

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class DnsServerPayload(TypedDict, total=False):
    """
    Type hints for system/dns_server payload fields.
    
    Configure DNS servers.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.dnsfilter.profile.ProfileEndpoint` (via: dnsfilter-profile)
        - :class:`~.system.interface.InterfaceEndpoint` (via: name)

    **Usage:**
        payload: DnsServerPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # DNS server name. | MaxLen: 15
    mode: Literal["recursive", "non-recursive", "forward-only", "resolver"]  # DNS server mode. | Default: recursive
    dnsfilter_profile: str  # DNS filter profile. | MaxLen: 47
    doh: Literal["enable", "disable"]  # Enable/disable DNS over HTTPS/443 | Default: disable
    doh3: Literal["enable", "disable"]  # Enable/disable DNS over QUIC/HTTP3/443 | Default: disable
    doq: Literal["enable", "disable"]  # Enable/disable DNS over QUIC/853 | Default: disable

# Nested TypedDicts for table field children (dict mode)

# Nested classes for table field children (object mode)


# Response TypedDict for GET returns (all fields present in API response)
class DnsServerResponse(TypedDict):
    """
    Type hints for system/dns_server API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str  # DNS server name. | MaxLen: 15
    mode: Literal["recursive", "non-recursive", "forward-only", "resolver"]  # DNS server mode. | Default: recursive
    dnsfilter_profile: str  # DNS filter profile. | MaxLen: 47
    doh: Literal["enable", "disable"]  # Enable/disable DNS over HTTPS/443 | Default: disable
    doh3: Literal["enable", "disable"]  # Enable/disable DNS over QUIC/HTTP3/443 | Default: disable
    doq: Literal["enable", "disable"]  # Enable/disable DNS over QUIC/853 | Default: disable


@final
class DnsServerObject:
    """Typed FortiObject for system/dns_server with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # DNS server name. | MaxLen: 15
    name: str
    # DNS server mode. | Default: recursive
    mode: Literal["recursive", "non-recursive", "forward-only", "resolver"]
    # DNS filter profile. | MaxLen: 47
    dnsfilter_profile: str
    # Enable/disable DNS over HTTPS/443 (default = disable). | Default: disable
    doh: Literal["enable", "disable"]
    # Enable/disable DNS over QUIC/HTTP3/443 (default = disable). | Default: disable
    doh3: Literal["enable", "disable"]
    # Enable/disable DNS over QUIC/853 (default = disable). | Default: disable
    doq: Literal["enable", "disable"]
    
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
    def to_dict(self) -> DnsServerPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class DnsServer:
    """
    Configure DNS servers.
    
    Path: system/dns_server
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
    ) -> DnsServerObject: ...
    
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
    ) -> DnsServerObject: ...
    
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
    ) -> FortiObjectList[DnsServerObject]: ...
    
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
    ) -> DnsServerObject: ...
    
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
    ) -> DnsServerObject: ...
    
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
    ) -> FortiObjectList[DnsServerObject]: ...
    
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
    ) -> DnsServerObject: ...
    
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
    ) -> DnsServerObject: ...
    
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
    ) -> FortiObjectList[DnsServerObject]: ...
    
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
    ) -> DnsServerObject | list[DnsServerObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: DnsServerPayload | None = ...,
        name: str | None = ...,
        mode: Literal["recursive", "non-recursive", "forward-only", "resolver"] | None = ...,
        dnsfilter_profile: str | None = ...,
        doh: Literal["enable", "disable"] | None = ...,
        doh3: Literal["enable", "disable"] | None = ...,
        doq: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> DnsServerObject: ...
    
    @overload
    def post(
        self,
        payload_dict: DnsServerPayload | None = ...,
        name: str | None = ...,
        mode: Literal["recursive", "non-recursive", "forward-only", "resolver"] | None = ...,
        dnsfilter_profile: str | None = ...,
        doh: Literal["enable", "disable"] | None = ...,
        doh3: Literal["enable", "disable"] | None = ...,
        doq: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: DnsServerPayload | None = ...,
        name: str | None = ...,
        mode: Literal["recursive", "non-recursive", "forward-only", "resolver"] | None = ...,
        dnsfilter_profile: str | None = ...,
        doh: Literal["enable", "disable"] | None = ...,
        doh3: Literal["enable", "disable"] | None = ...,
        doq: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def post(
        self,
        payload_dict: DnsServerPayload | None = ...,
        name: str | None = ...,
        mode: Literal["recursive", "non-recursive", "forward-only", "resolver"] | None = ...,
        dnsfilter_profile: str | None = ...,
        doh: Literal["enable", "disable"] | None = ...,
        doh3: Literal["enable", "disable"] | None = ...,
        doq: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: DnsServerPayload | None = ...,
        name: str | None = ...,
        mode: Literal["recursive", "non-recursive", "forward-only", "resolver"] | None = ...,
        dnsfilter_profile: str | None = ...,
        doh: Literal["enable", "disable"] | None = ...,
        doh3: Literal["enable", "disable"] | None = ...,
        doq: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> DnsServerObject: ...
    
    @overload
    def put(
        self,
        payload_dict: DnsServerPayload | None = ...,
        name: str | None = ...,
        mode: Literal["recursive", "non-recursive", "forward-only", "resolver"] | None = ...,
        dnsfilter_profile: str | None = ...,
        doh: Literal["enable", "disable"] | None = ...,
        doh3: Literal["enable", "disable"] | None = ...,
        doq: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: DnsServerPayload | None = ...,
        name: str | None = ...,
        mode: Literal["recursive", "non-recursive", "forward-only", "resolver"] | None = ...,
        dnsfilter_profile: str | None = ...,
        doh: Literal["enable", "disable"] | None = ...,
        doh3: Literal["enable", "disable"] | None = ...,
        doq: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def put(
        self,
        payload_dict: DnsServerPayload | None = ...,
        name: str | None = ...,
        mode: Literal["recursive", "non-recursive", "forward-only", "resolver"] | None = ...,
        dnsfilter_profile: str | None = ...,
        doh: Literal["enable", "disable"] | None = ...,
        doh3: Literal["enable", "disable"] | None = ...,
        doq: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> DnsServerObject: ...
    
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
        payload_dict: DnsServerPayload | None = ...,
        name: str | None = ...,
        mode: Literal["recursive", "non-recursive", "forward-only", "resolver"] | None = ...,
        dnsfilter_profile: str | None = ...,
        doh: Literal["enable", "disable"] | None = ...,
        doh3: Literal["enable", "disable"] | None = ...,
        doq: Literal["enable", "disable"] | None = ...,
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
    "DnsServer",
    "DnsServerPayload",
    "DnsServerResponse",
    "DnsServerObject",
]