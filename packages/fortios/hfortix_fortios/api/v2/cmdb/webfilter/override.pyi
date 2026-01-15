from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject
from hfortix_core.types import MutationResponse, RawAPIResponse

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class OverridePayload(TypedDict, total=False):
    """
    Type hints for webfilter/override payload fields.
    
    Configure FortiGuard Web Filter administrative overrides.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.user.group.GroupEndpoint` (via: user-group)
        - :class:`~.webfilter.profile.ProfileEndpoint` (via: new-profile, old-profile)

    **Usage:**
        payload: OverridePayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    id: int  # Override rule ID. | Default: 0 | Min: 0 | Max: 4294967295
    status: Literal["enable", "disable"]  # Enable/disable override rule. | Default: disable
    scope: Literal["user", "user-group", "ip", "ip6"]  # Override either the specific user, user group, IPv | Default: user
    ip: str  # IPv4 address which the override applies. | Default: 0.0.0.0
    user: str  # Name of the user which the override applies. | MaxLen: 64
    user_group: str  # Specify the user group for which the override appl | MaxLen: 63
    old_profile: str  # Name of the web filter profile which the override | MaxLen: 47
    new_profile: str  # Name of the new web filter profile used by the ove | MaxLen: 47
    ip6: str  # IPv6 address which the override applies. | Default: ::
    expires: str  # Override expiration date and time, from 5 minutes | Default: 1970/01/01 00:00:00
    initiator: str  # Initiating user of override (read-only setting). | MaxLen: 64

# Nested TypedDicts for table field children (dict mode)

# Nested classes for table field children (object mode)


# Response TypedDict for GET returns (all fields present in API response)
class OverrideResponse(TypedDict):
    """
    Type hints for webfilter/override API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    id: int  # Override rule ID. | Default: 0 | Min: 0 | Max: 4294967295
    status: Literal["enable", "disable"]  # Enable/disable override rule. | Default: disable
    scope: Literal["user", "user-group", "ip", "ip6"]  # Override either the specific user, user group, IPv | Default: user
    ip: str  # IPv4 address which the override applies. | Default: 0.0.0.0
    user: str  # Name of the user which the override applies. | MaxLen: 64
    user_group: str  # Specify the user group for which the override appl | MaxLen: 63
    old_profile: str  # Name of the web filter profile which the override | MaxLen: 47
    new_profile: str  # Name of the new web filter profile used by the ove | MaxLen: 47
    ip6: str  # IPv6 address which the override applies. | Default: ::
    expires: str  # Override expiration date and time, from 5 minutes | Default: 1970/01/01 00:00:00
    initiator: str  # Initiating user of override (read-only setting). | MaxLen: 64


@final
class OverrideObject:
    """Typed FortiObject for webfilter/override with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Override rule ID. | Default: 0 | Min: 0 | Max: 4294967295
    id: int
    # Enable/disable override rule. | Default: disable
    status: Literal["enable", "disable"]
    # Override either the specific user, user group, IPv4 address, | Default: user
    scope: Literal["user", "user-group", "ip", "ip6"]
    # IPv4 address which the override applies. | Default: 0.0.0.0
    ip: str
    # Name of the user which the override applies. | MaxLen: 64
    user: str
    # Specify the user group for which the override applies. | MaxLen: 63
    user_group: str
    # Name of the web filter profile which the override applies. | MaxLen: 47
    old_profile: str
    # Name of the new web filter profile used by the override. | MaxLen: 47
    new_profile: str
    # IPv6 address which the override applies. | Default: ::
    ip6: str
    # Override expiration date and time, from 5 minutes to 365 fro | Default: 1970/01/01 00:00:00
    expires: str
    # Initiating user of override (read-only setting). | MaxLen: 64
    initiator: str
    
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
    def to_dict(self) -> OverridePayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Override:
    """
    Configure FortiGuard Web Filter administrative overrides.
    
    Path: webfilter/override
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
    ) -> OverrideObject: ...
    
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
    ) -> OverrideObject: ...
    
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
    ) -> list[OverrideObject]: ...
    
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
        raw_json: Literal[False] = ...,
        *,
        **kwargs: Any,
    ) -> OverrideObject: ...
    
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
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> OverrideObject: ...
    
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
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> list[OverrideObject]: ...
    
    # raw_json=True returns the full API envelope
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
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> RawAPIResponse: ...
    
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
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> OverrideObject: ...
    
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
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> OverrideObject: ...
    
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
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> list[OverrideObject]: ...
    
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
        raw_json: bool = ...,
        **kwargs: Any,
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
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> OverrideObject | list[OverrideObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: OverridePayload | None = ...,
        id: int | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        scope: Literal["user", "user-group", "ip", "ip6"] | None = ...,
        ip: str | None = ...,
        user: str | None = ...,
        user_group: str | None = ...,
        old_profile: str | None = ...,
        new_profile: str | None = ...,
        ip6: str | None = ...,
        expires: str | None = ...,
        initiator: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> OverrideObject: ...
    
    @overload
    def post(
        self,
        payload_dict: OverridePayload | None = ...,
        id: int | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        scope: Literal["user", "user-group", "ip", "ip6"] | None = ...,
        ip: str | None = ...,
        user: str | None = ...,
        user_group: str | None = ...,
        old_profile: str | None = ...,
        new_profile: str | None = ...,
        ip6: str | None = ...,
        expires: str | None = ...,
        initiator: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    # raw_json=True returns the full API envelope
    @overload
    def post(
        self,
        payload_dict: OverridePayload | None = ...,
        id: int | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        scope: Literal["user", "user-group", "ip", "ip6"] | None = ...,
        ip: str | None = ...,
        user: str | None = ...,
        user_group: str | None = ...,
        old_profile: str | None = ...,
        new_profile: str | None = ...,
        ip6: str | None = ...,
        expires: str | None = ...,
        initiator: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> RawAPIResponse: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: OverridePayload | None = ...,
        id: int | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        scope: Literal["user", "user-group", "ip", "ip6"] | None = ...,
        ip: str | None = ...,
        user: str | None = ...,
        user_group: str | None = ...,
        old_profile: str | None = ...,
        new_profile: str | None = ...,
        ip6: str | None = ...,
        expires: str | None = ...,
        initiator: str | None = ...,
        vdom: str | bool | None = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    def post(
        self,
        payload_dict: OverridePayload | None = ...,
        id: int | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        scope: Literal["user", "user-group", "ip", "ip6"] | None = ...,
        ip: str | None = ...,
        user: str | None = ...,
        user_group: str | None = ...,
        old_profile: str | None = ...,
        new_profile: str | None = ...,
        ip6: str | None = ...,
        expires: str | None = ...,
        initiator: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: OverridePayload | None = ...,
        id: int | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        scope: Literal["user", "user-group", "ip", "ip6"] | None = ...,
        ip: str | None = ...,
        user: str | None = ...,
        user_group: str | None = ...,
        old_profile: str | None = ...,
        new_profile: str | None = ...,
        ip6: str | None = ...,
        expires: str | None = ...,
        initiator: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> OverrideObject: ...
    
    @overload
    def put(
        self,
        payload_dict: OverridePayload | None = ...,
        id: int | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        scope: Literal["user", "user-group", "ip", "ip6"] | None = ...,
        ip: str | None = ...,
        user: str | None = ...,
        user_group: str | None = ...,
        old_profile: str | None = ...,
        new_profile: str | None = ...,
        ip6: str | None = ...,
        expires: str | None = ...,
        initiator: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    # raw_json=True returns the full API envelope
    @overload
    def put(
        self,
        payload_dict: OverridePayload | None = ...,
        id: int | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        scope: Literal["user", "user-group", "ip", "ip6"] | None = ...,
        ip: str | None = ...,
        user: str | None = ...,
        user_group: str | None = ...,
        old_profile: str | None = ...,
        new_profile: str | None = ...,
        ip6: str | None = ...,
        expires: str | None = ...,
        initiator: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> RawAPIResponse: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: OverridePayload | None = ...,
        id: int | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        scope: Literal["user", "user-group", "ip", "ip6"] | None = ...,
        ip: str | None = ...,
        user: str | None = ...,
        user_group: str | None = ...,
        old_profile: str | None = ...,
        new_profile: str | None = ...,
        ip6: str | None = ...,
        expires: str | None = ...,
        initiator: str | None = ...,
        vdom: str | bool | None = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    def put(
        self,
        payload_dict: OverridePayload | None = ...,
        id: int | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        scope: Literal["user", "user-group", "ip", "ip6"] | None = ...,
        ip: str | None = ...,
        user: str | None = ...,
        user_group: str | None = ...,
        old_profile: str | None = ...,
        new_profile: str | None = ...,
        ip6: str | None = ...,
        expires: str | None = ...,
        initiator: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        id: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> OverrideObject: ...
    
    @overload
    def delete(
        self,
        id: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    # raw_json=True returns the full API envelope
    @overload
    def delete(
        self,
        id: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> RawAPIResponse: ...
    
    # Default overload
    @overload
    def delete(
        self,
        id: int | None = ...,
        vdom: str | bool | None = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    def delete(
        self,
        id: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    def exists(
        self,
        id: int,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: OverridePayload | None = ...,
        id: int | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        scope: Literal["user", "user-group", "ip", "ip6"] | None = ...,
        ip: str | None = ...,
        user: str | None = ...,
        user_group: str | None = ...,
        old_profile: str | None = ...,
        new_profile: str | None = ...,
        ip6: str | None = ...,
        expires: str | None = ...,
        initiator: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
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
    "Override",
    "OverridePayload",
    "OverrideResponse",
    "OverrideObject",
]