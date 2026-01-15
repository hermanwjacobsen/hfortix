from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class EvpnPayload(TypedDict, total=False):
    """
    Type hints for system/evpn payload fields.
    
    Configure EVPN instance.
    
    **Usage:**
        payload: EvpnPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    id: int  # ID. | Default: 0 | Min: 1 | Max: 65535
    rd: str  # Route Distinguisher: AA:NN|A.B.C.D:NN. | MaxLen: 79
    import_rt: list[dict[str, Any]]  # List of import route targets.
    export_rt: list[dict[str, Any]]  # List of export route targets.
    ip_local_learning: Literal["enable", "disable"]  # Enable/disable IP address local learning. | Default: disable
    arp_suppression: Literal["enable", "disable"]  # Enable/disable ARP suppression. | Default: disable

# Nested TypedDicts for table field children (dict mode)

class EvpnImportrtItem(TypedDict):
    """Type hints for import-rt table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    route_target: str  # Route target: AA:NN|A.B.C.D:NN. | MaxLen: 79


class EvpnExportrtItem(TypedDict):
    """Type hints for export-rt table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    route_target: str  # Route target: AA:NN|A.B.C.D:NN. | MaxLen: 79


# Nested classes for table field children (object mode)

@final
class EvpnImportrtObject:
    """Typed object for import-rt table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Route target: AA:NN|A.B.C.D:NN. | MaxLen: 79
    route_target: str
    
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
class EvpnExportrtObject:
    """Typed object for export-rt table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Route target: AA:NN|A.B.C.D:NN. | MaxLen: 79
    route_target: str
    
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
class EvpnResponse(TypedDict):
    """
    Type hints for system/evpn API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    id: int  # ID. | Default: 0 | Min: 1 | Max: 65535
    rd: str  # Route Distinguisher: AA:NN|A.B.C.D:NN. | MaxLen: 79
    import_rt: list[EvpnImportrtItem]  # List of import route targets.
    export_rt: list[EvpnExportrtItem]  # List of export route targets.
    ip_local_learning: Literal["enable", "disable"]  # Enable/disable IP address local learning. | Default: disable
    arp_suppression: Literal["enable", "disable"]  # Enable/disable ARP suppression. | Default: disable


@final
class EvpnObject:
    """Typed FortiObject for system/evpn with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # ID. | Default: 0 | Min: 1 | Max: 65535
    id: int
    # Route Distinguisher: AA:NN|A.B.C.D:NN. | MaxLen: 79
    rd: str
    # List of import route targets.
    import_rt: list[EvpnImportrtObject]
    # List of export route targets.
    export_rt: list[EvpnExportrtObject]
    # Enable/disable IP address local learning. | Default: disable
    ip_local_learning: Literal["enable", "disable"]
    # Enable/disable ARP suppression. | Default: disable
    arp_suppression: Literal["enable", "disable"]
    
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
    def to_dict(self) -> EvpnPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Evpn:
    """
    Configure EVPN instance.
    
    Path: system/evpn
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
    ) -> EvpnObject: ...
    
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
    ) -> EvpnObject: ...
    
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
    ) -> FortiObjectList[EvpnObject]: ...
    
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
    ) -> EvpnObject: ...
    
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
    ) -> EvpnObject: ...
    
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
    ) -> FortiObjectList[EvpnObject]: ...
    
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
    ) -> EvpnObject: ...
    
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
    ) -> EvpnObject: ...
    
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
    ) -> FortiObjectList[EvpnObject]: ...
    
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
    ) -> EvpnObject | list[EvpnObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: EvpnPayload | None = ...,
        id: int | None = ...,
        rd: str | None = ...,
        import_rt: str | list[str] | list[dict[str, Any]] | None = ...,
        export_rt: str | list[str] | list[dict[str, Any]] | None = ...,
        ip_local_learning: Literal["enable", "disable"] | None = ...,
        arp_suppression: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> EvpnObject: ...
    
    @overload
    def post(
        self,
        payload_dict: EvpnPayload | None = ...,
        id: int | None = ...,
        rd: str | None = ...,
        import_rt: str | list[str] | list[dict[str, Any]] | None = ...,
        export_rt: str | list[str] | list[dict[str, Any]] | None = ...,
        ip_local_learning: Literal["enable", "disable"] | None = ...,
        arp_suppression: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: EvpnPayload | None = ...,
        id: int | None = ...,
        rd: str | None = ...,
        import_rt: str | list[str] | list[dict[str, Any]] | None = ...,
        export_rt: str | list[str] | list[dict[str, Any]] | None = ...,
        ip_local_learning: Literal["enable", "disable"] | None = ...,
        arp_suppression: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def post(
        self,
        payload_dict: EvpnPayload | None = ...,
        id: int | None = ...,
        rd: str | None = ...,
        import_rt: str | list[str] | list[dict[str, Any]] | None = ...,
        export_rt: str | list[str] | list[dict[str, Any]] | None = ...,
        ip_local_learning: Literal["enable", "disable"] | None = ...,
        arp_suppression: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: EvpnPayload | None = ...,
        id: int | None = ...,
        rd: str | None = ...,
        import_rt: str | list[str] | list[dict[str, Any]] | None = ...,
        export_rt: str | list[str] | list[dict[str, Any]] | None = ...,
        ip_local_learning: Literal["enable", "disable"] | None = ...,
        arp_suppression: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> EvpnObject: ...
    
    @overload
    def put(
        self,
        payload_dict: EvpnPayload | None = ...,
        id: int | None = ...,
        rd: str | None = ...,
        import_rt: str | list[str] | list[dict[str, Any]] | None = ...,
        export_rt: str | list[str] | list[dict[str, Any]] | None = ...,
        ip_local_learning: Literal["enable", "disable"] | None = ...,
        arp_suppression: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: EvpnPayload | None = ...,
        id: int | None = ...,
        rd: str | None = ...,
        import_rt: str | list[str] | list[dict[str, Any]] | None = ...,
        export_rt: str | list[str] | list[dict[str, Any]] | None = ...,
        ip_local_learning: Literal["enable", "disable"] | None = ...,
        arp_suppression: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def put(
        self,
        payload_dict: EvpnPayload | None = ...,
        id: int | None = ...,
        rd: str | None = ...,
        import_rt: str | list[str] | list[dict[str, Any]] | None = ...,
        export_rt: str | list[str] | list[dict[str, Any]] | None = ...,
        ip_local_learning: Literal["enable", "disable"] | None = ...,
        arp_suppression: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        id: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> EvpnObject: ...
    
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
        payload_dict: EvpnPayload | None = ...,
        id: int | None = ...,
        rd: str | None = ...,
        import_rt: str | list[str] | list[dict[str, Any]] | None = ...,
        export_rt: str | list[str] | list[dict[str, Any]] | None = ...,
        ip_local_learning: Literal["enable", "disable"] | None = ...,
        arp_suppression: Literal["enable", "disable"] | None = ...,
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
    "Evpn",
    "EvpnPayload",
    "EvpnResponse",
    "EvpnObject",
]