from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class UserActivityPayload(TypedDict, total=False):
    """
    Type hints for casb/user_activity payload fields.
    
    Configure CASB user activity.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.casb.saas-application.SaasApplicationEndpoint` (via: application)

    **Usage:**
        payload: UserActivityPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # CASB user activity name. | MaxLen: 79
    uuid: str  # Universally Unique Identifier | MaxLen: 36
    status: Literal["enable", "disable"]  # CASB user activity status. | Default: enable
    description: str  # CASB user activity description. | MaxLen: 63
    type: Literal["built-in", "customized"]  # CASB user activity type. | Default: customized
    casb_name: str  # CASB user activity signature name. | MaxLen: 79
    application: str  # CASB SaaS application name. | MaxLen: 79
    category: Literal["activity-control", "tenant-control", "domain-control", "safe-search-control", "advanced-tenant-control", "other"]  # CASB user activity category. | Default: activity-control
    match_strategy: Literal["and", "or"]  # CASB user activity match strategy. | Default: or
    match: list[dict[str, Any]]  # CASB user activity match rules.
    control_options: list[dict[str, Any]]  # CASB control options.

# Nested TypedDicts for table field children (dict mode)

class UserActivityMatchItem(TypedDict):
    """Type hints for match table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    id: int  # CASB user activity match rules ID. | Default: 0 | Min: 0 | Max: 4294967295
    strategy: Literal["and", "or"]  # CASB user activity rules strategy. | Default: and
    rules: str  # CASB user activity rules.
    tenant_extraction: str  # CASB user activity tenant extraction.


class UserActivityControloptionsItem(TypedDict):
    """Type hints for control-options table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # CASB control option name. | MaxLen: 79
    status: Literal["enable", "disable"]  # CASB control option status. | Default: enable
    operations: str  # CASB control option operations.


# Nested classes for table field children (object mode)

@final
class UserActivityMatchObject:
    """Typed object for match table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # CASB user activity match rules ID. | Default: 0 | Min: 0 | Max: 4294967295
    id: int
    # CASB user activity rules strategy. | Default: and
    strategy: Literal["and", "or"]
    # CASB user activity rules.
    rules: str
    # CASB user activity tenant extraction.
    tenant_extraction: str
    
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
class UserActivityControloptionsObject:
    """Typed object for control-options table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # CASB control option name. | MaxLen: 79
    name: str
    # CASB control option status. | Default: enable
    status: Literal["enable", "disable"]
    # CASB control option operations.
    operations: str
    
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
class UserActivityResponse(TypedDict):
    """
    Type hints for casb/user_activity API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str  # CASB user activity name. | MaxLen: 79
    uuid: str  # Universally Unique Identifier | MaxLen: 36
    status: Literal["enable", "disable"]  # CASB user activity status. | Default: enable
    description: str  # CASB user activity description. | MaxLen: 63
    type: Literal["built-in", "customized"]  # CASB user activity type. | Default: customized
    casb_name: str  # CASB user activity signature name. | MaxLen: 79
    application: str  # CASB SaaS application name. | MaxLen: 79
    category: Literal["activity-control", "tenant-control", "domain-control", "safe-search-control", "advanced-tenant-control", "other"]  # CASB user activity category. | Default: activity-control
    match_strategy: Literal["and", "or"]  # CASB user activity match strategy. | Default: or
    match: list[UserActivityMatchItem]  # CASB user activity match rules.
    control_options: list[UserActivityControloptionsItem]  # CASB control options.


@final
class UserActivityObject:
    """Typed FortiObject for casb/user_activity with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # CASB user activity name. | MaxLen: 79
    name: str
    # Universally Unique Identifier | MaxLen: 36
    uuid: str
    # CASB user activity status. | Default: enable
    status: Literal["enable", "disable"]
    # CASB user activity description. | MaxLen: 63
    description: str
    # CASB user activity type. | Default: customized
    type: Literal["built-in", "customized"]
    # CASB user activity signature name. | MaxLen: 79
    casb_name: str
    # CASB SaaS application name. | MaxLen: 79
    application: str
    # CASB user activity category. | Default: activity-control
    category: Literal["activity-control", "tenant-control", "domain-control", "safe-search-control", "advanced-tenant-control", "other"]
    # CASB user activity match strategy. | Default: or
    match_strategy: Literal["and", "or"]
    # CASB user activity match rules.
    match: list[UserActivityMatchObject]
    # CASB control options.
    control_options: list[UserActivityControloptionsObject]
    
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
    def to_dict(self) -> UserActivityPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class UserActivity:
    """
    Configure CASB user activity.
    
    Path: casb/user_activity
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
    ) -> UserActivityObject: ...
    
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
    ) -> UserActivityObject: ...
    
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
    ) -> FortiObjectList[UserActivityObject]: ...
    
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
    ) -> UserActivityObject: ...
    
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
    ) -> UserActivityObject: ...
    
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
    ) -> FortiObjectList[UserActivityObject]: ...
    
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
    ) -> UserActivityObject: ...
    
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
    ) -> UserActivityObject: ...
    
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
    ) -> FortiObjectList[UserActivityObject]: ...
    
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
    ) -> UserActivityObject | list[UserActivityObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: UserActivityPayload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        description: str | None = ...,
        type: Literal["built-in", "customized"] | None = ...,
        casb_name: str | None = ...,
        application: str | None = ...,
        category: Literal["activity-control", "tenant-control", "domain-control", "safe-search-control", "advanced-tenant-control", "other"] | None = ...,
        match_strategy: Literal["and", "or"] | None = ...,
        match: str | list[str] | list[dict[str, Any]] | None = ...,
        control_options: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> UserActivityObject: ...
    
    @overload
    def post(
        self,
        payload_dict: UserActivityPayload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        description: str | None = ...,
        type: Literal["built-in", "customized"] | None = ...,
        casb_name: str | None = ...,
        application: str | None = ...,
        category: Literal["activity-control", "tenant-control", "domain-control", "safe-search-control", "advanced-tenant-control", "other"] | None = ...,
        match_strategy: Literal["and", "or"] | None = ...,
        match: str | list[str] | list[dict[str, Any]] | None = ...,
        control_options: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: UserActivityPayload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        description: str | None = ...,
        type: Literal["built-in", "customized"] | None = ...,
        casb_name: str | None = ...,
        application: str | None = ...,
        category: Literal["activity-control", "tenant-control", "domain-control", "safe-search-control", "advanced-tenant-control", "other"] | None = ...,
        match_strategy: Literal["and", "or"] | None = ...,
        match: str | list[str] | list[dict[str, Any]] | None = ...,
        control_options: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def post(
        self,
        payload_dict: UserActivityPayload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        description: str | None = ...,
        type: Literal["built-in", "customized"] | None = ...,
        casb_name: str | None = ...,
        application: str | None = ...,
        category: Literal["activity-control", "tenant-control", "domain-control", "safe-search-control", "advanced-tenant-control", "other"] | None = ...,
        match_strategy: Literal["and", "or"] | None = ...,
        match: str | list[str] | list[dict[str, Any]] | None = ...,
        control_options: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: UserActivityPayload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        description: str | None = ...,
        type: Literal["built-in", "customized"] | None = ...,
        casb_name: str | None = ...,
        application: str | None = ...,
        category: Literal["activity-control", "tenant-control", "domain-control", "safe-search-control", "advanced-tenant-control", "other"] | None = ...,
        match_strategy: Literal["and", "or"] | None = ...,
        match: str | list[str] | list[dict[str, Any]] | None = ...,
        control_options: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> UserActivityObject: ...
    
    @overload
    def put(
        self,
        payload_dict: UserActivityPayload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        description: str | None = ...,
        type: Literal["built-in", "customized"] | None = ...,
        casb_name: str | None = ...,
        application: str | None = ...,
        category: Literal["activity-control", "tenant-control", "domain-control", "safe-search-control", "advanced-tenant-control", "other"] | None = ...,
        match_strategy: Literal["and", "or"] | None = ...,
        match: str | list[str] | list[dict[str, Any]] | None = ...,
        control_options: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: UserActivityPayload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        description: str | None = ...,
        type: Literal["built-in", "customized"] | None = ...,
        casb_name: str | None = ...,
        application: str | None = ...,
        category: Literal["activity-control", "tenant-control", "domain-control", "safe-search-control", "advanced-tenant-control", "other"] | None = ...,
        match_strategy: Literal["and", "or"] | None = ...,
        match: str | list[str] | list[dict[str, Any]] | None = ...,
        control_options: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def put(
        self,
        payload_dict: UserActivityPayload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        description: str | None = ...,
        type: Literal["built-in", "customized"] | None = ...,
        casb_name: str | None = ...,
        application: str | None = ...,
        category: Literal["activity-control", "tenant-control", "domain-control", "safe-search-control", "advanced-tenant-control", "other"] | None = ...,
        match_strategy: Literal["and", "or"] | None = ...,
        match: str | list[str] | list[dict[str, Any]] | None = ...,
        control_options: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> UserActivityObject: ...
    
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
        payload_dict: UserActivityPayload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        description: str | None = ...,
        type: Literal["built-in", "customized"] | None = ...,
        casb_name: str | None = ...,
        application: str | None = ...,
        category: Literal["activity-control", "tenant-control", "domain-control", "safe-search-control", "advanced-tenant-control", "other"] | None = ...,
        match_strategy: Literal["and", "or"] | None = ...,
        match: str | list[str] | list[dict[str, Any]] | None = ...,
        control_options: str | list[str] | list[dict[str, Any]] | None = ...,
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
    "UserActivity",
    "UserActivityPayload",
    "UserActivityResponse",
    "UserActivityObject",
]