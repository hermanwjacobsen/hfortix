from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class GroupPayload(TypedDict, total=False):
    """
    Type hints for application/group payload fields.
    
    Configure firewall application groups.
    
    **Usage:**
        payload: GroupPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # Application group name. | MaxLen: 63
    comment: str  # Comments. | MaxLen: 255
    type: Literal["application", "filter"]  # Application group type. | Default: application
    application: list[dict[str, Any]]  # Application ID list.
    category: list[dict[str, Any]]  # Application category ID list.
    risk: list[dict[str, Any]]  # Risk, or impact, of allowing traffic from this app
    protocols: list[dict[str, Any]]  # Application protocol filter. | Default: all
    vendor: list[dict[str, Any]]  # Application vendor filter. | Default: all
    technology: list[dict[str, Any]]  # Application technology filter. | Default: all
    behavior: list[dict[str, Any]]  # Application behavior filter. | Default: all
    popularity: Literal["1", "2", "3", "4", "5"]  # Application popularity filter | Default: 1 2 3 4 5

# Nested TypedDicts for table field children (dict mode)

class GroupApplicationItem(TypedDict):
    """Type hints for application table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    id: int  # Application IDs. | Default: 0 | Min: 0 | Max: 4294967295


class GroupCategoryItem(TypedDict):
    """Type hints for category table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    id: int  # Category IDs. | Default: 0 | Min: 0 | Max: 4294967295


class GroupRiskItem(TypedDict):
    """Type hints for risk table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    level: int  # Risk, or impact, of allowing traffic from this app | Default: 0 | Min: 0 | Max: 4294967295


# Nested classes for table field children (object mode)

@final
class GroupApplicationObject:
    """Typed object for application table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Application IDs. | Default: 0 | Min: 0 | Max: 4294967295
    id: int
    
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
class GroupCategoryObject:
    """Typed object for category table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Category IDs. | Default: 0 | Min: 0 | Max: 4294967295
    id: int
    
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
class GroupRiskObject:
    """Typed object for risk table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Risk, or impact, of allowing traffic from this application t | Default: 0 | Min: 0 | Max: 4294967295
    level: int
    
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
class GroupResponse(TypedDict):
    """
    Type hints for application/group API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str  # Application group name. | MaxLen: 63
    comment: str  # Comments. | MaxLen: 255
    type: Literal["application", "filter"]  # Application group type. | Default: application
    application: list[GroupApplicationItem]  # Application ID list.
    category: list[GroupCategoryItem]  # Application category ID list.
    risk: list[GroupRiskItem]  # Risk, or impact, of allowing traffic from this app
    protocols: list[dict[str, Any]]  # Application protocol filter. | Default: all
    vendor: list[dict[str, Any]]  # Application vendor filter. | Default: all
    technology: list[dict[str, Any]]  # Application technology filter. | Default: all
    behavior: list[dict[str, Any]]  # Application behavior filter. | Default: all
    popularity: Literal["1", "2", "3", "4", "5"]  # Application popularity filter | Default: 1 2 3 4 5


@final
class GroupObject:
    """Typed FortiObject for application/group with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Application group name. | MaxLen: 63
    name: str
    # Comments. | MaxLen: 255
    comment: str
    # Application group type. | Default: application
    type: Literal["application", "filter"]
    # Application ID list.
    application: list[GroupApplicationObject]
    # Application category ID list.
    category: list[GroupCategoryObject]
    # Risk, or impact, of allowing traffic from this application t
    risk: list[GroupRiskObject]
    # Application protocol filter. | Default: all
    protocols: list[dict[str, Any]]
    # Application vendor filter. | Default: all
    vendor: list[dict[str, Any]]
    # Application technology filter. | Default: all
    technology: list[dict[str, Any]]
    # Application behavior filter. | Default: all
    behavior: list[dict[str, Any]]
    # Application popularity filter | Default: 1 2 3 4 5
    popularity: Literal["1", "2", "3", "4", "5"]
    
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
    def to_dict(self) -> GroupPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Group:
    """
    Configure firewall application groups.
    
    Path: application/group
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
    ) -> GroupObject: ...
    
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
    ) -> GroupObject: ...
    
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
    ) -> FortiObjectList[GroupObject]: ...
    
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
    ) -> GroupObject: ...
    
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
    ) -> GroupObject: ...
    
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
    ) -> FortiObjectList[GroupObject]: ...
    
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
    ) -> GroupObject: ...
    
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
    ) -> GroupObject: ...
    
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
    ) -> FortiObjectList[GroupObject]: ...
    
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
    ) -> GroupObject | list[GroupObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: GroupPayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        type: Literal["application", "filter"] | None = ...,
        application: str | list[str] | list[dict[str, Any]] | None = ...,
        category: str | list[str] | list[dict[str, Any]] | None = ...,
        risk: str | list[str] | list[dict[str, Any]] | None = ...,
        protocols: str | list[str] | None = ...,
        vendor: str | list[str] | None = ...,
        technology: str | list[str] | None = ...,
        behavior: str | list[str] | None = ...,
        popularity: Literal["1", "2", "3", "4", "5"] | list[str] | None = ...,
        vdom: str | bool | None = ...,
    ) -> GroupObject: ...
    
    @overload
    def post(
        self,
        payload_dict: GroupPayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        type: Literal["application", "filter"] | None = ...,
        application: str | list[str] | list[dict[str, Any]] | None = ...,
        category: str | list[str] | list[dict[str, Any]] | None = ...,
        risk: str | list[str] | list[dict[str, Any]] | None = ...,
        protocols: str | list[str] | None = ...,
        vendor: str | list[str] | None = ...,
        technology: str | list[str] | None = ...,
        behavior: str | list[str] | None = ...,
        popularity: Literal["1", "2", "3", "4", "5"] | list[str] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: GroupPayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        type: Literal["application", "filter"] | None = ...,
        application: str | list[str] | list[dict[str, Any]] | None = ...,
        category: str | list[str] | list[dict[str, Any]] | None = ...,
        risk: str | list[str] | list[dict[str, Any]] | None = ...,
        protocols: str | list[str] | None = ...,
        vendor: str | list[str] | None = ...,
        technology: str | list[str] | None = ...,
        behavior: str | list[str] | None = ...,
        popularity: Literal["1", "2", "3", "4", "5"] | list[str] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def post(
        self,
        payload_dict: GroupPayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        type: Literal["application", "filter"] | None = ...,
        application: str | list[str] | list[dict[str, Any]] | None = ...,
        category: str | list[str] | list[dict[str, Any]] | None = ...,
        risk: str | list[str] | list[dict[str, Any]] | None = ...,
        protocols: str | list[str] | None = ...,
        vendor: str | list[str] | None = ...,
        technology: str | list[str] | None = ...,
        behavior: str | list[str] | None = ...,
        popularity: Literal["1", "2", "3", "4", "5"] | list[str] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: GroupPayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        type: Literal["application", "filter"] | None = ...,
        application: str | list[str] | list[dict[str, Any]] | None = ...,
        category: str | list[str] | list[dict[str, Any]] | None = ...,
        risk: str | list[str] | list[dict[str, Any]] | None = ...,
        protocols: str | list[str] | None = ...,
        vendor: str | list[str] | None = ...,
        technology: str | list[str] | None = ...,
        behavior: str | list[str] | None = ...,
        popularity: Literal["1", "2", "3", "4", "5"] | list[str] | None = ...,
        vdom: str | bool | None = ...,
    ) -> GroupObject: ...
    
    @overload
    def put(
        self,
        payload_dict: GroupPayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        type: Literal["application", "filter"] | None = ...,
        application: str | list[str] | list[dict[str, Any]] | None = ...,
        category: str | list[str] | list[dict[str, Any]] | None = ...,
        risk: str | list[str] | list[dict[str, Any]] | None = ...,
        protocols: str | list[str] | None = ...,
        vendor: str | list[str] | None = ...,
        technology: str | list[str] | None = ...,
        behavior: str | list[str] | None = ...,
        popularity: Literal["1", "2", "3", "4", "5"] | list[str] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: GroupPayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        type: Literal["application", "filter"] | None = ...,
        application: str | list[str] | list[dict[str, Any]] | None = ...,
        category: str | list[str] | list[dict[str, Any]] | None = ...,
        risk: str | list[str] | list[dict[str, Any]] | None = ...,
        protocols: str | list[str] | None = ...,
        vendor: str | list[str] | None = ...,
        technology: str | list[str] | None = ...,
        behavior: str | list[str] | None = ...,
        popularity: Literal["1", "2", "3", "4", "5"] | list[str] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def put(
        self,
        payload_dict: GroupPayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        type: Literal["application", "filter"] | None = ...,
        application: str | list[str] | list[dict[str, Any]] | None = ...,
        category: str | list[str] | list[dict[str, Any]] | None = ...,
        risk: str | list[str] | list[dict[str, Any]] | None = ...,
        protocols: str | list[str] | None = ...,
        vendor: str | list[str] | None = ...,
        technology: str | list[str] | None = ...,
        behavior: str | list[str] | None = ...,
        popularity: Literal["1", "2", "3", "4", "5"] | list[str] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> GroupObject: ...
    
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
        payload_dict: GroupPayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        type: Literal["application", "filter"] | None = ...,
        application: str | list[str] | list[dict[str, Any]] | None = ...,
        category: str | list[str] | list[dict[str, Any]] | None = ...,
        risk: str | list[str] | list[dict[str, Any]] | None = ...,
        protocols: str | list[str] | None = ...,
        vendor: str | list[str] | None = ...,
        technology: str | list[str] | None = ...,
        behavior: str | list[str] | None = ...,
        popularity: Literal["1", "2", "3", "4", "5"] | list[str] | None = ...,
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
    "Group",
    "GroupPayload",
    "GroupResponse",
    "GroupObject",
]