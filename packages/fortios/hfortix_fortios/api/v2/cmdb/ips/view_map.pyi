from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class ViewMapPayload(TypedDict, total=False):
    """
    Type hints for ips/view_map payload fields.
    
    Configure IPS view-map.
    
    **Usage:**
        payload: ViewMapPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    id: int  # View ID. | Default: 0 | Min: 0 | Max: 4294967295
    vdom_id: int  # VDOM ID. | Default: 0 | Min: 0 | Max: 4294967295
    policy_id: int  # Policy ID. | Default: 0 | Min: 0 | Max: 4294967295
    id_policy_id: int  # ID-based policy ID. | Default: 0 | Min: 0 | Max: 4294967295
    which: Literal["firewall", "interface", "interface6", "sniffer", "sniffer6", "explicit"]  # Policy. | Default: firewall

# Nested TypedDicts for table field children (dict mode)

# Nested classes for table field children (object mode)


# Response TypedDict for GET returns (all fields present in API response)
class ViewMapResponse(TypedDict):
    """
    Type hints for ips/view_map API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    id: int  # View ID. | Default: 0 | Min: 0 | Max: 4294967295
    vdom_id: int  # VDOM ID. | Default: 0 | Min: 0 | Max: 4294967295
    policy_id: int  # Policy ID. | Default: 0 | Min: 0 | Max: 4294967295
    id_policy_id: int  # ID-based policy ID. | Default: 0 | Min: 0 | Max: 4294967295
    which: Literal["firewall", "interface", "interface6", "sniffer", "sniffer6", "explicit"]  # Policy. | Default: firewall


@final
class ViewMapObject:
    """Typed FortiObject for ips/view_map with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # View ID. | Default: 0 | Min: 0 | Max: 4294967295
    id: int
    # VDOM ID. | Default: 0 | Min: 0 | Max: 4294967295
    vdom_id: int
    # Policy ID. | Default: 0 | Min: 0 | Max: 4294967295
    policy_id: int
    # ID-based policy ID. | Default: 0 | Min: 0 | Max: 4294967295
    id_policy_id: int
    # Policy. | Default: firewall
    which: Literal["firewall", "interface", "interface6", "sniffer", "sniffer6", "explicit"]
    
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
    def to_dict(self) -> ViewMapPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class ViewMap:
    """
    Configure IPS view-map.
    
    Path: ips/view_map
    Category: cmdb
    Primary Key: id
    """
    
    # ================================================================
    # GET OVERLOADS - Always returns FortiObject
    # Pylance matches overloads top-to-bottom, so these must come first!
    # ================================================================
    
    # With mkey as positional arg -> returns FortiObject
    @overload
    def get(
        self,
        id: int,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> ViewMapObject: ...
    
    # With mkey as keyword arg -> returns FortiObject
    @overload
    def get(
        self,
        *,
        id: int,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> ViewMapObject: ...
    
    # Without mkey -> returns list of FortiObjects
    @overload
    def get(
        self,
        id: None = None,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObjectList[ViewMapObject]: ...
    
    # ================================================================
    # (removed - all GET now returns FortiObject)
    # ================================================================
    
    # With mkey as positional arg -> returns single object
    @overload
    def get(
        self,
        id: int,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> ViewMapObject: ...
    
    # With mkey as keyword arg -> returns single object
    @overload
    def get(
        self,
        *,
        id: int,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> ViewMapObject: ...
    
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
    ) -> FortiObjectList[ViewMapObject]: ...
    
    # Dict mode with mkey provided as positional arg (single dict)
    @overload
    def get(
        self,
        id: int,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> ViewMapObject: ...
    
    # Dict mode with mkey provided as keyword arg (single dict)
    @overload
    def get(
        self,
        *,
        id: int,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> ViewMapObject: ...
    
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
    ) -> FortiObjectList[ViewMapObject]: ...
    
    # Fallback overload for all other cases
    @overload
    def get(
        self,
        id: int | None = ...,
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
        id: int | None = ...,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> ViewMapObject | list[ViewMapObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: ViewMapPayload | None = ...,
        id: int | None = ...,
        vdom_id: int | None = ...,
        policy_id: int | None = ...,
        id_policy_id: int | None = ...,
        which: Literal["firewall", "interface", "interface6", "sniffer", "sniffer6", "explicit"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> ViewMapObject: ...
    
    @overload
    def post(
        self,
        payload_dict: ViewMapPayload | None = ...,
        id: int | None = ...,
        vdom_id: int | None = ...,
        policy_id: int | None = ...,
        id_policy_id: int | None = ...,
        which: Literal["firewall", "interface", "interface6", "sniffer", "sniffer6", "explicit"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: ViewMapPayload | None = ...,
        id: int | None = ...,
        vdom_id: int | None = ...,
        policy_id: int | None = ...,
        id_policy_id: int | None = ...,
        which: Literal["firewall", "interface", "interface6", "sniffer", "sniffer6", "explicit"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def post(
        self,
        payload_dict: ViewMapPayload | None = ...,
        id: int | None = ...,
        vdom_id: int | None = ...,
        policy_id: int | None = ...,
        id_policy_id: int | None = ...,
        which: Literal["firewall", "interface", "interface6", "sniffer", "sniffer6", "explicit"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: ViewMapPayload | None = ...,
        id: int | None = ...,
        vdom_id: int | None = ...,
        policy_id: int | None = ...,
        id_policy_id: int | None = ...,
        which: Literal["firewall", "interface", "interface6", "sniffer", "sniffer6", "explicit"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> ViewMapObject: ...
    
    @overload
    def put(
        self,
        payload_dict: ViewMapPayload | None = ...,
        id: int | None = ...,
        vdom_id: int | None = ...,
        policy_id: int | None = ...,
        id_policy_id: int | None = ...,
        which: Literal["firewall", "interface", "interface6", "sniffer", "sniffer6", "explicit"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: ViewMapPayload | None = ...,
        id: int | None = ...,
        vdom_id: int | None = ...,
        policy_id: int | None = ...,
        id_policy_id: int | None = ...,
        which: Literal["firewall", "interface", "interface6", "sniffer", "sniffer6", "explicit"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def put(
        self,
        payload_dict: ViewMapPayload | None = ...,
        id: int | None = ...,
        vdom_id: int | None = ...,
        policy_id: int | None = ...,
        id_policy_id: int | None = ...,
        which: Literal["firewall", "interface", "interface6", "sniffer", "sniffer6", "explicit"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        id: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> ViewMapObject: ...
    
    @overload
    def delete(
        self,
        id: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def delete(
        self,
        id: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def delete(
        self,
        id: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def exists(
        self,
        id: int,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: ViewMapPayload | None = ...,
        id: int | None = ...,
        vdom_id: int | None = ...,
        policy_id: int | None = ...,
        id_policy_id: int | None = ...,
        which: Literal["firewall", "interface", "interface6", "sniffer", "sniffer6", "explicit"] | None = ...,
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
    "ViewMap",
    "ViewMapPayload",
    "ViewMapResponse",
    "ViewMapObject",
]