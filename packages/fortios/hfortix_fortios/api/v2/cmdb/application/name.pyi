from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList
from hfortix_core.types import MutationResponse

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class NamePayload(TypedDict, total=False):
    """
    Type hints for application/name payload fields.
    
    Configure application signatures.
    
    **Usage:**
        payload: NamePayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # Application name. | MaxLen: 63
    id: int  # Application ID. | Default: 0 | Min: 0 | Max: 4294967295
    category: int  # Application category ID. | Default: 0 | Min: 0 | Max: 4294967295
    popularity: int  # Application popularity. | Default: 0 | Min: 0 | Max: 255
    risk: int  # Application risk. | Default: 0 | Min: 0 | Max: 255
    weight: int  # Application weight. | Default: 0 | Min: 0 | Max: 255
    protocol: str  # Application protocol.
    technology: str  # Application technology.
    behavior: str  # Application behavior.
    vendor: str  # Application vendor.
    parameters: list[dict[str, Any]]  # Application parameters.
    metadata: list[dict[str, Any]]  # Meta data.
    status: str  # print all application information

# Nested TypedDicts for table field children (dict mode)

class NameParametersItem(TypedDict):
    """Type hints for parameters table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # Parameter name. | MaxLen: 31
    default value: str  # Parameter default value. | MaxLen: 199


class NameMetadataItem(TypedDict):
    """Type hints for metadata table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    id: int  # ID. | Default: 0 | Min: 0 | Max: 4294967295
    metaid: int  # Meta ID. | Default: 0 | Min: 0 | Max: 4294967295
    valueid: int  # Value ID. | Default: 0 | Min: 0 | Max: 4294967295


# Nested classes for table field children (object mode)

@final
class NameParametersObject:
    """Typed object for parameters table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Parameter name. | MaxLen: 31
    name: str
    # Parameter default value. | MaxLen: 199
    default value: str
    
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
class NameMetadataObject:
    """Typed object for metadata table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # ID. | Default: 0 | Min: 0 | Max: 4294967295
    id: int
    # Meta ID. | Default: 0 | Min: 0 | Max: 4294967295
    metaid: int
    # Value ID. | Default: 0 | Min: 0 | Max: 4294967295
    valueid: int
    
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
class NameResponse(TypedDict):
    """
    Type hints for application/name API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str  # Application name. | MaxLen: 63
    id: int  # Application ID. | Default: 0 | Min: 0 | Max: 4294967295
    category: int  # Application category ID. | Default: 0 | Min: 0 | Max: 4294967295
    popularity: int  # Application popularity. | Default: 0 | Min: 0 | Max: 255
    risk: int  # Application risk. | Default: 0 | Min: 0 | Max: 255
    weight: int  # Application weight. | Default: 0 | Min: 0 | Max: 255
    protocol: str  # Application protocol.
    technology: str  # Application technology.
    behavior: str  # Application behavior.
    vendor: str  # Application vendor.
    parameters: list[NameParametersItem]  # Application parameters.
    metadata: list[NameMetadataItem]  # Meta data.
    status: str  # print all application information


@final
class NameObject:
    """Typed FortiObject for application/name with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Application name. | MaxLen: 63
    name: str
    # Application ID. | Default: 0 | Min: 0 | Max: 4294967295
    id: int
    # Application category ID. | Default: 0 | Min: 0 | Max: 4294967295
    category: int
    # Application popularity. | Default: 0 | Min: 0 | Max: 255
    popularity: int
    # Application risk. | Default: 0 | Min: 0 | Max: 255
    risk: int
    # Application weight. | Default: 0 | Min: 0 | Max: 255
    weight: int
    # Application protocol.
    protocol: str
    # Application technology.
    technology: str
    # Application behavior.
    behavior: str
    # Application vendor.
    vendor: str
    # Application parameters.
    parameters: list[NameParametersObject]
    # Meta data.
    metadata: list[NameMetadataObject]
    # print all application information
    status: str
    
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
    def to_dict(self) -> NamePayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Name:
    """
    Configure application signatures.
    
    Path: application/name
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
    ) -> NameObject: ...
    
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
    ) -> NameObject: ...
    
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
    ) -> FortiObjectList[NameObject]: ...
    
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
    ) -> NameObject: ...
    
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
    ) -> NameObject: ...
    
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
    ) -> FortiObjectList[NameObject]: ...
    
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
    ) -> NameObject: ...
    
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
    ) -> NameObject: ...
    
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
    ) -> FortiObjectList[NameObject]: ...
    
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
    ) -> NameObject | list[NameObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: NamePayload | None = ...,
        name: str | None = ...,
        id: int | None = ...,
        category: int | None = ...,
        popularity: int | None = ...,
        risk: int | None = ...,
        weight: int | None = ...,
        protocol: str | None = ...,
        technology: str | None = ...,
        behavior: str | None = ...,
        vendor: str | None = ...,
        parameters: str | list[str] | list[dict[str, Any]] | None = ...,
        metadata: str | list[str] | list[dict[str, Any]] | None = ...,
        status: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> NameObject: ...
    
    @overload
    def post(
        self,
        payload_dict: NamePayload | None = ...,
        name: str | None = ...,
        id: int | None = ...,
        category: int | None = ...,
        popularity: int | None = ...,
        risk: int | None = ...,
        weight: int | None = ...,
        protocol: str | None = ...,
        technology: str | None = ...,
        behavior: str | None = ...,
        vendor: str | None = ...,
        parameters: str | list[str] | list[dict[str, Any]] | None = ...,
        metadata: str | list[str] | list[dict[str, Any]] | None = ...,
        status: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: NamePayload | None = ...,
        name: str | None = ...,
        id: int | None = ...,
        category: int | None = ...,
        popularity: int | None = ...,
        risk: int | None = ...,
        weight: int | None = ...,
        protocol: str | None = ...,
        technology: str | None = ...,
        behavior: str | None = ...,
        vendor: str | None = ...,
        parameters: str | list[str] | list[dict[str, Any]] | None = ...,
        metadata: str | list[str] | list[dict[str, Any]] | None = ...,
        status: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def post(
        self,
        payload_dict: NamePayload | None = ...,
        name: str | None = ...,
        id: int | None = ...,
        category: int | None = ...,
        popularity: int | None = ...,
        risk: int | None = ...,
        weight: int | None = ...,
        protocol: str | None = ...,
        technology: str | None = ...,
        behavior: str | None = ...,
        vendor: str | None = ...,
        parameters: str | list[str] | list[dict[str, Any]] | None = ...,
        metadata: str | list[str] | list[dict[str, Any]] | None = ...,
        status: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: NamePayload | None = ...,
        name: str | None = ...,
        id: int | None = ...,
        category: int | None = ...,
        popularity: int | None = ...,
        risk: int | None = ...,
        weight: int | None = ...,
        protocol: str | None = ...,
        technology: str | None = ...,
        behavior: str | None = ...,
        vendor: str | None = ...,
        parameters: str | list[str] | list[dict[str, Any]] | None = ...,
        metadata: str | list[str] | list[dict[str, Any]] | None = ...,
        status: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> NameObject: ...
    
    @overload
    def put(
        self,
        payload_dict: NamePayload | None = ...,
        name: str | None = ...,
        id: int | None = ...,
        category: int | None = ...,
        popularity: int | None = ...,
        risk: int | None = ...,
        weight: int | None = ...,
        protocol: str | None = ...,
        technology: str | None = ...,
        behavior: str | None = ...,
        vendor: str | None = ...,
        parameters: str | list[str] | list[dict[str, Any]] | None = ...,
        metadata: str | list[str] | list[dict[str, Any]] | None = ...,
        status: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: NamePayload | None = ...,
        name: str | None = ...,
        id: int | None = ...,
        category: int | None = ...,
        popularity: int | None = ...,
        risk: int | None = ...,
        weight: int | None = ...,
        protocol: str | None = ...,
        technology: str | None = ...,
        behavior: str | None = ...,
        vendor: str | None = ...,
        parameters: str | list[str] | list[dict[str, Any]] | None = ...,
        metadata: str | list[str] | list[dict[str, Any]] | None = ...,
        status: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def put(
        self,
        payload_dict: NamePayload | None = ...,
        name: str | None = ...,
        id: int | None = ...,
        category: int | None = ...,
        popularity: int | None = ...,
        risk: int | None = ...,
        weight: int | None = ...,
        protocol: str | None = ...,
        technology: str | None = ...,
        behavior: str | None = ...,
        vendor: str | None = ...,
        parameters: str | list[str] | list[dict[str, Any]] | None = ...,
        metadata: str | list[str] | list[dict[str, Any]] | None = ...,
        status: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> NameObject: ...
    
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
        payload_dict: NamePayload | None = ...,
        name: str | None = ...,
        id: int | None = ...,
        category: int | None = ...,
        popularity: int | None = ...,
        risk: int | None = ...,
        weight: int | None = ...,
        protocol: str | None = ...,
        technology: str | None = ...,
        behavior: str | None = ...,
        vendor: str | None = ...,
        parameters: str | list[str] | list[dict[str, Any]] | None = ...,
        metadata: str | list[str] | list[dict[str, Any]] | None = ...,
        status: str | None = ...,
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
    "Name",
    "NamePayload",
    "NameResponse",
    "NameObject",
]