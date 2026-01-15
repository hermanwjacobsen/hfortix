from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class ForwardServerGroupPayload(TypedDict, total=False):
    """
    Type hints for web_proxy/forward_server_group payload fields.
    
    Configure a forward server group consisting or multiple forward servers. Supports failover and load balancing.
    
    **Usage:**
        payload: ForwardServerGroupPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # Configure a forward server group consisting one or | MaxLen: 63
    affinity: Literal["enable", "disable"]  # Enable/disable affinity, attaching a source-ip's t | Default: enable
    ldb_method: Literal["weighted", "least-session", "active-passive"]  # Load balance method: weighted or least-session. | Default: weighted
    group_down_option: Literal["block", "pass"]  # Action to take when all of the servers in the forw | Default: block
    server_list: list[dict[str, Any]]  # Add web forward servers to a list to form a server

# Nested TypedDicts for table field children (dict mode)

class ForwardServerGroupServerlistItem(TypedDict):
    """Type hints for server-list table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # Forward server name. | MaxLen: 63
    weight: int  # Optionally assign a weight of the forwarding serve | Default: 10 | Min: 1 | Max: 100


# Nested classes for table field children (object mode)

@final
class ForwardServerGroupServerlistObject:
    """Typed object for server-list table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Forward server name. | MaxLen: 63
    name: str
    # Optionally assign a weight of the forwarding server for weig | Default: 10 | Min: 1 | Max: 100
    weight: int
    
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
class ForwardServerGroupResponse(TypedDict):
    """
    Type hints for web_proxy/forward_server_group API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str  # Configure a forward server group consisting one or | MaxLen: 63
    affinity: Literal["enable", "disable"]  # Enable/disable affinity, attaching a source-ip's t | Default: enable
    ldb_method: Literal["weighted", "least-session", "active-passive"]  # Load balance method: weighted or least-session. | Default: weighted
    group_down_option: Literal["block", "pass"]  # Action to take when all of the servers in the forw | Default: block
    server_list: list[ForwardServerGroupServerlistItem]  # Add web forward servers to a list to form a server


@final
class ForwardServerGroupObject:
    """Typed FortiObject for web_proxy/forward_server_group with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Configure a forward server group consisting one or multiple | MaxLen: 63
    name: str
    # Enable/disable affinity, attaching a source-ip's traffic to | Default: enable
    affinity: Literal["enable", "disable"]
    # Load balance method: weighted or least-session. | Default: weighted
    ldb_method: Literal["weighted", "least-session", "active-passive"]
    # Action to take when all of the servers in the forward server | Default: block
    group_down_option: Literal["block", "pass"]
    # Add web forward servers to a list to form a server group. Op
    server_list: list[ForwardServerGroupServerlistObject]
    
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
    def to_dict(self) -> ForwardServerGroupPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class ForwardServerGroup:
    """
    Configure a forward server group consisting or multiple forward servers. Supports failover and load balancing.
    
    Path: web_proxy/forward_server_group
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
    ) -> ForwardServerGroupObject: ...
    
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
    ) -> ForwardServerGroupObject: ...
    
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
    ) -> FortiObjectList[ForwardServerGroupObject]: ...
    
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
    ) -> ForwardServerGroupObject: ...
    
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
    ) -> ForwardServerGroupObject: ...
    
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
    ) -> FortiObjectList[ForwardServerGroupObject]: ...
    
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
    ) -> ForwardServerGroupObject: ...
    
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
    ) -> ForwardServerGroupObject: ...
    
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
    ) -> FortiObjectList[ForwardServerGroupObject]: ...
    
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
    ) -> ForwardServerGroupObject | list[ForwardServerGroupObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: ForwardServerGroupPayload | None = ...,
        name: str | None = ...,
        affinity: Literal["enable", "disable"] | None = ...,
        ldb_method: Literal["weighted", "least-session", "active-passive"] | None = ...,
        group_down_option: Literal["block", "pass"] | None = ...,
        server_list: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> ForwardServerGroupObject: ...
    
    @overload
    def post(
        self,
        payload_dict: ForwardServerGroupPayload | None = ...,
        name: str | None = ...,
        affinity: Literal["enable", "disable"] | None = ...,
        ldb_method: Literal["weighted", "least-session", "active-passive"] | None = ...,
        group_down_option: Literal["block", "pass"] | None = ...,
        server_list: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: ForwardServerGroupPayload | None = ...,
        name: str | None = ...,
        affinity: Literal["enable", "disable"] | None = ...,
        ldb_method: Literal["weighted", "least-session", "active-passive"] | None = ...,
        group_down_option: Literal["block", "pass"] | None = ...,
        server_list: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def post(
        self,
        payload_dict: ForwardServerGroupPayload | None = ...,
        name: str | None = ...,
        affinity: Literal["enable", "disable"] | None = ...,
        ldb_method: Literal["weighted", "least-session", "active-passive"] | None = ...,
        group_down_option: Literal["block", "pass"] | None = ...,
        server_list: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: ForwardServerGroupPayload | None = ...,
        name: str | None = ...,
        affinity: Literal["enable", "disable"] | None = ...,
        ldb_method: Literal["weighted", "least-session", "active-passive"] | None = ...,
        group_down_option: Literal["block", "pass"] | None = ...,
        server_list: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> ForwardServerGroupObject: ...
    
    @overload
    def put(
        self,
        payload_dict: ForwardServerGroupPayload | None = ...,
        name: str | None = ...,
        affinity: Literal["enable", "disable"] | None = ...,
        ldb_method: Literal["weighted", "least-session", "active-passive"] | None = ...,
        group_down_option: Literal["block", "pass"] | None = ...,
        server_list: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: ForwardServerGroupPayload | None = ...,
        name: str | None = ...,
        affinity: Literal["enable", "disable"] | None = ...,
        ldb_method: Literal["weighted", "least-session", "active-passive"] | None = ...,
        group_down_option: Literal["block", "pass"] | None = ...,
        server_list: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def put(
        self,
        payload_dict: ForwardServerGroupPayload | None = ...,
        name: str | None = ...,
        affinity: Literal["enable", "disable"] | None = ...,
        ldb_method: Literal["weighted", "least-session", "active-passive"] | None = ...,
        group_down_option: Literal["block", "pass"] | None = ...,
        server_list: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> ForwardServerGroupObject: ...
    
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
        payload_dict: ForwardServerGroupPayload | None = ...,
        name: str | None = ...,
        affinity: Literal["enable", "disable"] | None = ...,
        ldb_method: Literal["weighted", "least-session", "active-passive"] | None = ...,
        group_down_option: Literal["block", "pass"] | None = ...,
        server_list: str | list[str] | list[dict[str, Any]] | None = ...,
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
    "ForwardServerGroup",
    "ForwardServerGroupPayload",
    "ForwardServerGroupResponse",
    "ForwardServerGroupObject",
]