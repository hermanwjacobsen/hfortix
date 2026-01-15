from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class ApiUserPayload(TypedDict, total=False):
    """
    Type hints for system/api_user payload fields.
    
    Configure API users.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.system.accprofile.AccprofileEndpoint` (via: accprofile)

    **Usage:**
        payload: ApiUserPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # User name. | MaxLen: 35
    comments: str  # Comment. | MaxLen: 255
    api_key: str  # Admin user password. | MaxLen: 128
    accprofile: str  # Admin user access profile. | MaxLen: 35
    vdom: list[dict[str, Any]]  # Virtual domains.
    schedule: str  # Schedule name. | MaxLen: 35
    cors_allow_origin: str  # Value for Access-Control-Allow-Origin on API respo | MaxLen: 269
    peer_auth: Literal["enable", "disable"]  # Enable/disable peer authentication. | Default: disable
    peer_group: str  # Peer group name. | MaxLen: 35
    trusthost: list[dict[str, Any]]  # Trusthost.

# Nested TypedDicts for table field children (dict mode)

class ApiUserVdomItem(TypedDict):
    """Type hints for vdom table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # Virtual domain name. | MaxLen: 79


class ApiUserTrusthostItem(TypedDict):
    """Type hints for trusthost table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    id: int  # ID. | Default: 0 | Min: 0 | Max: 4294967295
    type: Literal["ipv4-trusthost", "ipv6-trusthost"]  # Trusthost type. | Default: ipv4-trusthost
    ipv4_trusthost: str  # IPv4 trusted host address. | Default: 0.0.0.0 0.0.0.0
    ipv6_trusthost: str  # IPv6 trusted host address. | Default: ::/0


# Nested classes for table field children (object mode)

@final
class ApiUserVdomObject:
    """Typed object for vdom table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Virtual domain name. | MaxLen: 79
    name: str
    
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
class ApiUserTrusthostObject:
    """Typed object for trusthost table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # ID. | Default: 0 | Min: 0 | Max: 4294967295
    id: int
    # Trusthost type. | Default: ipv4-trusthost
    type: Literal["ipv4-trusthost", "ipv6-trusthost"]
    # IPv4 trusted host address. | Default: 0.0.0.0 0.0.0.0
    ipv4_trusthost: str
    # IPv6 trusted host address. | Default: ::/0
    ipv6_trusthost: str
    
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
class ApiUserResponse(TypedDict):
    """
    Type hints for system/api_user API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str  # User name. | MaxLen: 35
    comments: str  # Comment. | MaxLen: 255
    api_key: str  # Admin user password. | MaxLen: 128
    accprofile: str  # Admin user access profile. | MaxLen: 35
    vdom: list[ApiUserVdomItem]  # Virtual domains.
    schedule: str  # Schedule name. | MaxLen: 35
    cors_allow_origin: str  # Value for Access-Control-Allow-Origin on API respo | MaxLen: 269
    peer_auth: Literal["enable", "disable"]  # Enable/disable peer authentication. | Default: disable
    peer_group: str  # Peer group name. | MaxLen: 35
    trusthost: list[ApiUserTrusthostItem]  # Trusthost.


@final
class ApiUserObject:
    """Typed FortiObject for system/api_user with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # User name. | MaxLen: 35
    name: str
    # Comment. | MaxLen: 255
    comments: str
    # Admin user password. | MaxLen: 128
    api_key: str
    # Admin user access profile. | MaxLen: 35
    accprofile: str
    # Virtual domains.
    vdom: list[ApiUserVdomObject]
    # Schedule name. | MaxLen: 35
    schedule: str
    # Value for Access-Control-Allow-Origin on API responses. Avoi | MaxLen: 269
    cors_allow_origin: str
    # Enable/disable peer authentication. | Default: disable
    peer_auth: Literal["enable", "disable"]
    # Peer group name. | MaxLen: 35
    peer_group: str
    # Trusthost.
    trusthost: list[ApiUserTrusthostObject]
    
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
    def to_dict(self) -> ApiUserPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class ApiUser:
    """
    Configure API users.
    
    Path: system/api_user
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
    ) -> ApiUserObject: ...
    
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
    ) -> ApiUserObject: ...
    
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
    ) -> FortiObjectList[ApiUserObject]: ...
    
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
    ) -> ApiUserObject: ...
    
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
    ) -> ApiUserObject: ...
    
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
    ) -> FortiObjectList[ApiUserObject]: ...
    
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
    ) -> ApiUserObject: ...
    
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
    ) -> ApiUserObject: ...
    
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
    ) -> FortiObjectList[ApiUserObject]: ...
    
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
    ) -> ApiUserObject | list[ApiUserObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: ApiUserPayload | None = ...,
        name: str | None = ...,
        comments: str | None = ...,
        api_key: str | None = ...,
        accprofile: str | None = ...,
        schedule: str | None = ...,
        cors_allow_origin: str | None = ...,
        peer_auth: Literal["enable", "disable"] | None = ...,
        peer_group: str | None = ...,
        trusthost: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> ApiUserObject: ...
    
    @overload
    def post(
        self,
        payload_dict: ApiUserPayload | None = ...,
        name: str | None = ...,
        comments: str | None = ...,
        api_key: str | None = ...,
        accprofile: str | None = ...,
        schedule: str | None = ...,
        cors_allow_origin: str | None = ...,
        peer_auth: Literal["enable", "disable"] | None = ...,
        peer_group: str | None = ...,
        trusthost: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: ApiUserPayload | None = ...,
        name: str | None = ...,
        comments: str | None = ...,
        api_key: str | None = ...,
        accprofile: str | None = ...,
        schedule: str | None = ...,
        cors_allow_origin: str | None = ...,
        peer_auth: Literal["enable", "disable"] | None = ...,
        peer_group: str | None = ...,
        trusthost: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def post(
        self,
        payload_dict: ApiUserPayload | None = ...,
        name: str | None = ...,
        comments: str | None = ...,
        api_key: str | None = ...,
        accprofile: str | None = ...,
        schedule: str | None = ...,
        cors_allow_origin: str | None = ...,
        peer_auth: Literal["enable", "disable"] | None = ...,
        peer_group: str | None = ...,
        trusthost: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: ApiUserPayload | None = ...,
        name: str | None = ...,
        comments: str | None = ...,
        api_key: str | None = ...,
        accprofile: str | None = ...,
        schedule: str | None = ...,
        cors_allow_origin: str | None = ...,
        peer_auth: Literal["enable", "disable"] | None = ...,
        peer_group: str | None = ...,
        trusthost: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> ApiUserObject: ...
    
    @overload
    def put(
        self,
        payload_dict: ApiUserPayload | None = ...,
        name: str | None = ...,
        comments: str | None = ...,
        api_key: str | None = ...,
        accprofile: str | None = ...,
        schedule: str | None = ...,
        cors_allow_origin: str | None = ...,
        peer_auth: Literal["enable", "disable"] | None = ...,
        peer_group: str | None = ...,
        trusthost: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: ApiUserPayload | None = ...,
        name: str | None = ...,
        comments: str | None = ...,
        api_key: str | None = ...,
        accprofile: str | None = ...,
        schedule: str | None = ...,
        cors_allow_origin: str | None = ...,
        peer_auth: Literal["enable", "disable"] | None = ...,
        peer_group: str | None = ...,
        trusthost: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def put(
        self,
        payload_dict: ApiUserPayload | None = ...,
        name: str | None = ...,
        comments: str | None = ...,
        api_key: str | None = ...,
        accprofile: str | None = ...,
        schedule: str | None = ...,
        cors_allow_origin: str | None = ...,
        peer_auth: Literal["enable", "disable"] | None = ...,
        peer_group: str | None = ...,
        trusthost: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> ApiUserObject: ...
    
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
        payload_dict: ApiUserPayload | None = ...,
        name: str | None = ...,
        comments: str | None = ...,
        api_key: str | None = ...,
        accprofile: str | None = ...,
        schedule: str | None = ...,
        cors_allow_origin: str | None = ...,
        peer_auth: Literal["enable", "disable"] | None = ...,
        peer_group: str | None = ...,
        trusthost: str | list[str] | list[dict[str, Any]] | None = ...,
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
    "ApiUser",
    "ApiUserPayload",
    "ApiUserResponse",
    "ApiUserObject",
]