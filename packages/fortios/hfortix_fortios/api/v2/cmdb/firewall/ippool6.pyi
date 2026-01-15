from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList
from hfortix_core.types import MutationResponse

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class Ippool6Payload(TypedDict, total=False):
    """
    Type hints for firewall/ippool6 payload fields.
    
    Configure IPv6 IP pools.
    
    **Usage:**
        payload: Ippool6Payload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # IPv6 IP pool name. | MaxLen: 79
    type: Literal["overload", "nptv6"]  # Configure IPv6 pool type (overload or NPTv6). | Default: overload
    startip: str  # First IPv6 address (inclusive) in the range for th | Default: ::
    endip: str  # Final IPv6 address (inclusive) in the range for th | Default: ::
    internal_prefix: str  # Internal NPTv6 prefix length (32 - 64). | Default: ::/0
    external_prefix: str  # External NPTv6 prefix length (32 - 64). | Default: ::/0
    comments: str  # Comment. | MaxLen: 255
    nat46: Literal["disable", "enable"]  # Enable/disable NAT46. | Default: disable
    add_nat46_route: Literal["disable", "enable"]  # Enable/disable adding NAT46 route. | Default: enable

# Nested TypedDicts for table field children (dict mode)

# Nested classes for table field children (object mode)


# Response TypedDict for GET returns (all fields present in API response)
class Ippool6Response(TypedDict):
    """
    Type hints for firewall/ippool6 API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str  # IPv6 IP pool name. | MaxLen: 79
    type: Literal["overload", "nptv6"]  # Configure IPv6 pool type (overload or NPTv6). | Default: overload
    startip: str  # First IPv6 address (inclusive) in the range for th | Default: ::
    endip: str  # Final IPv6 address (inclusive) in the range for th | Default: ::
    internal_prefix: str  # Internal NPTv6 prefix length (32 - 64). | Default: ::/0
    external_prefix: str  # External NPTv6 prefix length (32 - 64). | Default: ::/0
    comments: str  # Comment. | MaxLen: 255
    nat46: Literal["disable", "enable"]  # Enable/disable NAT46. | Default: disable
    add_nat46_route: Literal["disable", "enable"]  # Enable/disable adding NAT46 route. | Default: enable


@final
class Ippool6Object:
    """Typed FortiObject for firewall/ippool6 with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # IPv6 IP pool name. | MaxLen: 79
    name: str
    # Configure IPv6 pool type (overload or NPTv6). | Default: overload
    type: Literal["overload", "nptv6"]
    # First IPv6 address (inclusive) in the range for the address | Default: ::
    startip: str
    # Final IPv6 address (inclusive) in the range for the address | Default: ::
    endip: str
    # Internal NPTv6 prefix length (32 - 64). | Default: ::/0
    internal_prefix: str
    # External NPTv6 prefix length (32 - 64). | Default: ::/0
    external_prefix: str
    # Comment. | MaxLen: 255
    comments: str
    # Enable/disable NAT46. | Default: disable
    nat46: Literal["disable", "enable"]
    # Enable/disable adding NAT46 route. | Default: enable
    add_nat46_route: Literal["disable", "enable"]
    
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
    def to_dict(self) -> Ippool6Payload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Ippool6:
    """
    Configure IPv6 IP pools.
    
    Path: firewall/ippool6
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
    ) -> Ippool6Object: ...
    
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
    ) -> Ippool6Object: ...
    
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
    ) -> FortiObjectList[Ippool6Object]: ...
    
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
    ) -> Ippool6Object: ...
    
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
    ) -> Ippool6Object: ...
    
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
    ) -> FortiObjectList[Ippool6Object]: ...
    
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
    ) -> Ippool6Object: ...
    
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
    ) -> Ippool6Object: ...
    
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
    ) -> FortiObjectList[Ippool6Object]: ...
    
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
    ) -> Ippool6Object | list[Ippool6Object] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: Ippool6Payload | None = ...,
        name: str | None = ...,
        type: Literal["overload", "nptv6"] | None = ...,
        startip: str | None = ...,
        endip: str | None = ...,
        internal_prefix: str | None = ...,
        external_prefix: str | None = ...,
        comments: str | None = ...,
        nat46: Literal["disable", "enable"] | None = ...,
        add_nat46_route: Literal["disable", "enable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> Ippool6Object: ...
    
    @overload
    def post(
        self,
        payload_dict: Ippool6Payload | None = ...,
        name: str | None = ...,
        type: Literal["overload", "nptv6"] | None = ...,
        startip: str | None = ...,
        endip: str | None = ...,
        internal_prefix: str | None = ...,
        external_prefix: str | None = ...,
        comments: str | None = ...,
        nat46: Literal["disable", "enable"] | None = ...,
        add_nat46_route: Literal["disable", "enable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: Ippool6Payload | None = ...,
        name: str | None = ...,
        type: Literal["overload", "nptv6"] | None = ...,
        startip: str | None = ...,
        endip: str | None = ...,
        internal_prefix: str | None = ...,
        external_prefix: str | None = ...,
        comments: str | None = ...,
        nat46: Literal["disable", "enable"] | None = ...,
        add_nat46_route: Literal["disable", "enable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def post(
        self,
        payload_dict: Ippool6Payload | None = ...,
        name: str | None = ...,
        type: Literal["overload", "nptv6"] | None = ...,
        startip: str | None = ...,
        endip: str | None = ...,
        internal_prefix: str | None = ...,
        external_prefix: str | None = ...,
        comments: str | None = ...,
        nat46: Literal["disable", "enable"] | None = ...,
        add_nat46_route: Literal["disable", "enable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: Ippool6Payload | None = ...,
        name: str | None = ...,
        type: Literal["overload", "nptv6"] | None = ...,
        startip: str | None = ...,
        endip: str | None = ...,
        internal_prefix: str | None = ...,
        external_prefix: str | None = ...,
        comments: str | None = ...,
        nat46: Literal["disable", "enable"] | None = ...,
        add_nat46_route: Literal["disable", "enable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> Ippool6Object: ...
    
    @overload
    def put(
        self,
        payload_dict: Ippool6Payload | None = ...,
        name: str | None = ...,
        type: Literal["overload", "nptv6"] | None = ...,
        startip: str | None = ...,
        endip: str | None = ...,
        internal_prefix: str | None = ...,
        external_prefix: str | None = ...,
        comments: str | None = ...,
        nat46: Literal["disable", "enable"] | None = ...,
        add_nat46_route: Literal["disable", "enable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: Ippool6Payload | None = ...,
        name: str | None = ...,
        type: Literal["overload", "nptv6"] | None = ...,
        startip: str | None = ...,
        endip: str | None = ...,
        internal_prefix: str | None = ...,
        external_prefix: str | None = ...,
        comments: str | None = ...,
        nat46: Literal["disable", "enable"] | None = ...,
        add_nat46_route: Literal["disable", "enable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def put(
        self,
        payload_dict: Ippool6Payload | None = ...,
        name: str | None = ...,
        type: Literal["overload", "nptv6"] | None = ...,
        startip: str | None = ...,
        endip: str | None = ...,
        internal_prefix: str | None = ...,
        external_prefix: str | None = ...,
        comments: str | None = ...,
        nat46: Literal["disable", "enable"] | None = ...,
        add_nat46_route: Literal["disable", "enable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> Ippool6Object: ...
    
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
        payload_dict: Ippool6Payload | None = ...,
        name: str | None = ...,
        type: Literal["overload", "nptv6"] | None = ...,
        startip: str | None = ...,
        endip: str | None = ...,
        internal_prefix: str | None = ...,
        external_prefix: str | None = ...,
        comments: str | None = ...,
        nat46: Literal["disable", "enable"] | None = ...,
        add_nat46_route: Literal["disable", "enable"] | None = ...,
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
    "Ippool6",
    "Ippool6Payload",
    "Ippool6Response",
    "Ippool6Object",
]