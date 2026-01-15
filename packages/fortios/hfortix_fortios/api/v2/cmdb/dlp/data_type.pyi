from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class DataTypePayload(TypedDict, total=False):
    """
    Type hints for dlp/data_type payload fields.
    
    Configure predefined data type used by DLP blocking.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.dlp.dictionary.DictionaryEndpoint` (via: match-around)

    **Usage:**
        payload: DataTypePayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # Name of table containing the data type. | MaxLen: 35
    pattern: str  # Regular expression pattern string without look aro | MaxLen: 255
    verify: str  # Regular expression pattern string used to verify t | MaxLen: 255
    verify2: str  # Extra regular expression pattern string used to ve | MaxLen: 255
    match_around: str  # Dictionary to check whether it has a match around | MaxLen: 35
    look_back: int  # Number of characters required to save for verifica | Default: 1 | Min: 1 | Max: 255
    look_ahead: int  # Number of characters to obtain in advance for veri | Default: 1 | Min: 1 | Max: 255
    match_back: int  # Number of characters in front for match-around | Default: 1 | Min: 1 | Max: 4096
    match_ahead: int  # Number of characters behind for match-around | Default: 1 | Min: 1 | Max: 4096
    transform: str  # Template to transform user input to a pattern usin | MaxLen: 255
    verify_transformed_pattern: Literal["enable", "disable"]  # Enable/disable verification for transformed patter | Default: disable
    comment: str  # Optional comments. | MaxLen: 255

# Nested TypedDicts for table field children (dict mode)

# Nested classes for table field children (object mode)


# Response TypedDict for GET returns (all fields present in API response)
class DataTypeResponse(TypedDict):
    """
    Type hints for dlp/data_type API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str  # Name of table containing the data type. | MaxLen: 35
    pattern: str  # Regular expression pattern string without look aro | MaxLen: 255
    verify: str  # Regular expression pattern string used to verify t | MaxLen: 255
    verify2: str  # Extra regular expression pattern string used to ve | MaxLen: 255
    match_around: str  # Dictionary to check whether it has a match around | MaxLen: 35
    look_back: int  # Number of characters required to save for verifica | Default: 1 | Min: 1 | Max: 255
    look_ahead: int  # Number of characters to obtain in advance for veri | Default: 1 | Min: 1 | Max: 255
    match_back: int  # Number of characters in front for match-around | Default: 1 | Min: 1 | Max: 4096
    match_ahead: int  # Number of characters behind for match-around | Default: 1 | Min: 1 | Max: 4096
    transform: str  # Template to transform user input to a pattern usin | MaxLen: 255
    verify_transformed_pattern: Literal["enable", "disable"]  # Enable/disable verification for transformed patter | Default: disable
    comment: str  # Optional comments. | MaxLen: 255


@final
class DataTypeObject:
    """Typed FortiObject for dlp/data_type with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Name of table containing the data type. | MaxLen: 35
    name: str
    # Regular expression pattern string without look around. | MaxLen: 255
    pattern: str
    # Regular expression pattern string used to verify the data ty | MaxLen: 255
    verify: str
    # Extra regular expression pattern string used to verify the d | MaxLen: 255
    verify2: str
    # Dictionary to check whether it has a match around | MaxLen: 35
    match_around: str
    # Number of characters required to save for verification | Default: 1 | Min: 1 | Max: 255
    look_back: int
    # Number of characters to obtain in advance for verification | Default: 1 | Min: 1 | Max: 255
    look_ahead: int
    # Number of characters in front for match-around | Default: 1 | Min: 1 | Max: 4096
    match_back: int
    # Number of characters behind for match-around | Default: 1 | Min: 1 | Max: 4096
    match_ahead: int
    # Template to transform user input to a pattern using capture | MaxLen: 255
    transform: str
    # Enable/disable verification for transformed pattern. | Default: disable
    verify_transformed_pattern: Literal["enable", "disable"]
    # Optional comments. | MaxLen: 255
    comment: str
    
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
    def to_dict(self) -> DataTypePayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class DataType:
    """
    Configure predefined data type used by DLP blocking.
    
    Path: dlp/data_type
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
    ) -> DataTypeObject: ...
    
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
    ) -> DataTypeObject: ...
    
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
    ) -> FortiObjectList[DataTypeObject]: ...
    
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
    ) -> DataTypeObject: ...
    
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
    ) -> DataTypeObject: ...
    
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
    ) -> FortiObjectList[DataTypeObject]: ...
    
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
    ) -> DataTypeObject: ...
    
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
    ) -> DataTypeObject: ...
    
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
    ) -> FortiObjectList[DataTypeObject]: ...
    
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
    ) -> DataTypeObject | list[DataTypeObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: DataTypePayload | None = ...,
        name: str | None = ...,
        pattern: str | None = ...,
        verify: str | None = ...,
        verify2: str | None = ...,
        match_around: str | None = ...,
        look_back: int | None = ...,
        look_ahead: int | None = ...,
        match_back: int | None = ...,
        match_ahead: int | None = ...,
        transform: str | None = ...,
        verify_transformed_pattern: Literal["enable", "disable"] | None = ...,
        comment: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> DataTypeObject: ...
    
    @overload
    def post(
        self,
        payload_dict: DataTypePayload | None = ...,
        name: str | None = ...,
        pattern: str | None = ...,
        verify: str | None = ...,
        verify2: str | None = ...,
        match_around: str | None = ...,
        look_back: int | None = ...,
        look_ahead: int | None = ...,
        match_back: int | None = ...,
        match_ahead: int | None = ...,
        transform: str | None = ...,
        verify_transformed_pattern: Literal["enable", "disable"] | None = ...,
        comment: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: DataTypePayload | None = ...,
        name: str | None = ...,
        pattern: str | None = ...,
        verify: str | None = ...,
        verify2: str | None = ...,
        match_around: str | None = ...,
        look_back: int | None = ...,
        look_ahead: int | None = ...,
        match_back: int | None = ...,
        match_ahead: int | None = ...,
        transform: str | None = ...,
        verify_transformed_pattern: Literal["enable", "disable"] | None = ...,
        comment: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def post(
        self,
        payload_dict: DataTypePayload | None = ...,
        name: str | None = ...,
        pattern: str | None = ...,
        verify: str | None = ...,
        verify2: str | None = ...,
        match_around: str | None = ...,
        look_back: int | None = ...,
        look_ahead: int | None = ...,
        match_back: int | None = ...,
        match_ahead: int | None = ...,
        transform: str | None = ...,
        verify_transformed_pattern: Literal["enable", "disable"] | None = ...,
        comment: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: DataTypePayload | None = ...,
        name: str | None = ...,
        pattern: str | None = ...,
        verify: str | None = ...,
        verify2: str | None = ...,
        match_around: str | None = ...,
        look_back: int | None = ...,
        look_ahead: int | None = ...,
        match_back: int | None = ...,
        match_ahead: int | None = ...,
        transform: str | None = ...,
        verify_transformed_pattern: Literal["enable", "disable"] | None = ...,
        comment: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> DataTypeObject: ...
    
    @overload
    def put(
        self,
        payload_dict: DataTypePayload | None = ...,
        name: str | None = ...,
        pattern: str | None = ...,
        verify: str | None = ...,
        verify2: str | None = ...,
        match_around: str | None = ...,
        look_back: int | None = ...,
        look_ahead: int | None = ...,
        match_back: int | None = ...,
        match_ahead: int | None = ...,
        transform: str | None = ...,
        verify_transformed_pattern: Literal["enable", "disable"] | None = ...,
        comment: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: DataTypePayload | None = ...,
        name: str | None = ...,
        pattern: str | None = ...,
        verify: str | None = ...,
        verify2: str | None = ...,
        match_around: str | None = ...,
        look_back: int | None = ...,
        look_ahead: int | None = ...,
        match_back: int | None = ...,
        match_ahead: int | None = ...,
        transform: str | None = ...,
        verify_transformed_pattern: Literal["enable", "disable"] | None = ...,
        comment: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def put(
        self,
        payload_dict: DataTypePayload | None = ...,
        name: str | None = ...,
        pattern: str | None = ...,
        verify: str | None = ...,
        verify2: str | None = ...,
        match_around: str | None = ...,
        look_back: int | None = ...,
        look_ahead: int | None = ...,
        match_back: int | None = ...,
        match_ahead: int | None = ...,
        transform: str | None = ...,
        verify_transformed_pattern: Literal["enable", "disable"] | None = ...,
        comment: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> DataTypeObject: ...
    
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
        payload_dict: DataTypePayload | None = ...,
        name: str | None = ...,
        pattern: str | None = ...,
        verify: str | None = ...,
        verify2: str | None = ...,
        match_around: str | None = ...,
        look_back: int | None = ...,
        look_ahead: int | None = ...,
        match_back: int | None = ...,
        match_ahead: int | None = ...,
        transform: str | None = ...,
        verify_transformed_pattern: Literal["enable", "disable"] | None = ...,
        comment: str | None = ...,
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
    "DataType",
    "DataTypePayload",
    "DataTypeResponse",
    "DataTypeObject",
]