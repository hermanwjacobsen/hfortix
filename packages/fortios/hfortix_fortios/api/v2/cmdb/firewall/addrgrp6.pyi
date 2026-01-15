from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList
from hfortix_core.types import MutationResponse

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class Addrgrp6Payload(TypedDict, total=False):
    """
    Type hints for firewall/addrgrp6 payload fields.
    
    Configure IPv6 address groups.
    
    **Usage:**
        payload: Addrgrp6Payload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # IPv6 address group name. | MaxLen: 79
    uuid: str  # Universally Unique Identifier | Default: 00000000-0000-0000-0000-000000000000
    color: int  # Integer value to determine the color of the icon i | Default: 0 | Min: 0 | Max: 32
    comment: str  # Comment. | MaxLen: 255
    member: list[dict[str, Any]]  # Address objects contained within the group.
    exclude: Literal["enable", "disable"]  # Enable/disable address6 exclusion. | Default: disable
    exclude_member: list[dict[str, Any]]  # Address6 exclusion member.
    tagging: list[dict[str, Any]]  # Config object tagging.
    fabric_object: Literal["enable", "disable"]  # Security Fabric global object setting. | Default: disable

# Nested TypedDicts for table field children (dict mode)

class Addrgrp6MemberItem(TypedDict):
    """Type hints for member table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # Address6/addrgrp6 name. | MaxLen: 79


class Addrgrp6ExcludememberItem(TypedDict):
    """Type hints for exclude-member table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # Address6 name. | MaxLen: 79


class Addrgrp6TaggingItem(TypedDict):
    """Type hints for tagging table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # Tagging entry name. | MaxLen: 63
    category: str  # Tag category. | MaxLen: 63
    tags: str  # Tags.


# Nested classes for table field children (object mode)

@final
class Addrgrp6MemberObject:
    """Typed object for member table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Address6/addrgrp6 name. | MaxLen: 79
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
class Addrgrp6ExcludememberObject:
    """Typed object for exclude-member table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Address6 name. | MaxLen: 79
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
class Addrgrp6TaggingObject:
    """Typed object for tagging table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Tagging entry name. | MaxLen: 63
    name: str
    # Tag category. | MaxLen: 63
    category: str
    # Tags.
    tags: str
    
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
class Addrgrp6Response(TypedDict):
    """
    Type hints for firewall/addrgrp6 API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str  # IPv6 address group name. | MaxLen: 79
    uuid: str  # Universally Unique Identifier | Default: 00000000-0000-0000-0000-000000000000
    color: int  # Integer value to determine the color of the icon i | Default: 0 | Min: 0 | Max: 32
    comment: str  # Comment. | MaxLen: 255
    member: list[Addrgrp6MemberItem]  # Address objects contained within the group.
    exclude: Literal["enable", "disable"]  # Enable/disable address6 exclusion. | Default: disable
    exclude_member: list[Addrgrp6ExcludememberItem]  # Address6 exclusion member.
    tagging: list[Addrgrp6TaggingItem]  # Config object tagging.
    fabric_object: Literal["enable", "disable"]  # Security Fabric global object setting. | Default: disable


@final
class Addrgrp6Object:
    """Typed FortiObject for firewall/addrgrp6 with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # IPv6 address group name. | MaxLen: 79
    name: str
    # Universally Unique Identifier | Default: 00000000-0000-0000-0000-000000000000
    uuid: str
    # Integer value to determine the color of the icon in the GUI | Default: 0 | Min: 0 | Max: 32
    color: int
    # Comment. | MaxLen: 255
    comment: str
    # Address objects contained within the group.
    member: list[Addrgrp6MemberObject]
    # Enable/disable address6 exclusion. | Default: disable
    exclude: Literal["enable", "disable"]
    # Address6 exclusion member.
    exclude_member: list[Addrgrp6ExcludememberObject]
    # Config object tagging.
    tagging: list[Addrgrp6TaggingObject]
    # Security Fabric global object setting. | Default: disable
    fabric_object: Literal["enable", "disable"]
    
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
    def to_dict(self) -> Addrgrp6Payload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Addrgrp6:
    """
    Configure IPv6 address groups.
    
    Path: firewall/addrgrp6
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
    ) -> Addrgrp6Object: ...
    
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
    ) -> Addrgrp6Object: ...
    
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
    ) -> FortiObjectList[Addrgrp6Object]: ...
    
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
    ) -> Addrgrp6Object: ...
    
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
    ) -> Addrgrp6Object: ...
    
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
    ) -> FortiObjectList[Addrgrp6Object]: ...
    
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
    ) -> Addrgrp6Object: ...
    
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
    ) -> Addrgrp6Object: ...
    
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
    ) -> FortiObjectList[Addrgrp6Object]: ...
    
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
    ) -> Addrgrp6Object | list[Addrgrp6Object] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: Addrgrp6Payload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        color: int | None = ...,
        comment: str | None = ...,
        member: str | list[str] | list[dict[str, Any]] | None = ...,
        exclude: Literal["enable", "disable"] | None = ...,
        exclude_member: str | list[str] | list[dict[str, Any]] | None = ...,
        tagging: str | list[str] | list[dict[str, Any]] | None = ...,
        fabric_object: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> Addrgrp6Object: ...
    
    @overload
    def post(
        self,
        payload_dict: Addrgrp6Payload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        color: int | None = ...,
        comment: str | None = ...,
        member: str | list[str] | list[dict[str, Any]] | None = ...,
        exclude: Literal["enable", "disable"] | None = ...,
        exclude_member: str | list[str] | list[dict[str, Any]] | None = ...,
        tagging: str | list[str] | list[dict[str, Any]] | None = ...,
        fabric_object: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: Addrgrp6Payload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        color: int | None = ...,
        comment: str | None = ...,
        member: str | list[str] | list[dict[str, Any]] | None = ...,
        exclude: Literal["enable", "disable"] | None = ...,
        exclude_member: str | list[str] | list[dict[str, Any]] | None = ...,
        tagging: str | list[str] | list[dict[str, Any]] | None = ...,
        fabric_object: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def post(
        self,
        payload_dict: Addrgrp6Payload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        color: int | None = ...,
        comment: str | None = ...,
        member: str | list[str] | list[dict[str, Any]] | None = ...,
        exclude: Literal["enable", "disable"] | None = ...,
        exclude_member: str | list[str] | list[dict[str, Any]] | None = ...,
        tagging: str | list[str] | list[dict[str, Any]] | None = ...,
        fabric_object: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: Addrgrp6Payload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        color: int | None = ...,
        comment: str | None = ...,
        member: str | list[str] | list[dict[str, Any]] | None = ...,
        exclude: Literal["enable", "disable"] | None = ...,
        exclude_member: str | list[str] | list[dict[str, Any]] | None = ...,
        tagging: str | list[str] | list[dict[str, Any]] | None = ...,
        fabric_object: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> Addrgrp6Object: ...
    
    @overload
    def put(
        self,
        payload_dict: Addrgrp6Payload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        color: int | None = ...,
        comment: str | None = ...,
        member: str | list[str] | list[dict[str, Any]] | None = ...,
        exclude: Literal["enable", "disable"] | None = ...,
        exclude_member: str | list[str] | list[dict[str, Any]] | None = ...,
        tagging: str | list[str] | list[dict[str, Any]] | None = ...,
        fabric_object: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: Addrgrp6Payload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        color: int | None = ...,
        comment: str | None = ...,
        member: str | list[str] | list[dict[str, Any]] | None = ...,
        exclude: Literal["enable", "disable"] | None = ...,
        exclude_member: str | list[str] | list[dict[str, Any]] | None = ...,
        tagging: str | list[str] | list[dict[str, Any]] | None = ...,
        fabric_object: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def put(
        self,
        payload_dict: Addrgrp6Payload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        color: int | None = ...,
        comment: str | None = ...,
        member: str | list[str] | list[dict[str, Any]] | None = ...,
        exclude: Literal["enable", "disable"] | None = ...,
        exclude_member: str | list[str] | list[dict[str, Any]] | None = ...,
        tagging: str | list[str] | list[dict[str, Any]] | None = ...,
        fabric_object: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> Addrgrp6Object: ...
    
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
        payload_dict: Addrgrp6Payload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        color: int | None = ...,
        comment: str | None = ...,
        member: str | list[str] | list[dict[str, Any]] | None = ...,
        exclude: Literal["enable", "disable"] | None = ...,
        exclude_member: str | list[str] | list[dict[str, Any]] | None = ...,
        tagging: str | list[str] | list[dict[str, Any]] | None = ...,
        fabric_object: Literal["enable", "disable"] | None = ...,
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
    "Addrgrp6",
    "Addrgrp6Payload",
    "Addrgrp6Response",
    "Addrgrp6Object",
]