from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList
from hfortix_core.types import MutationResponse

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class AccessControlListPayload(TypedDict, total=False):
    """
    Type hints for wireless_controller/access_control_list payload fields.
    
    Configure WiFi bridge access control list.
    
    **Usage:**
        payload: AccessControlListPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # AP access control list name. | MaxLen: 35
    comment: str  # Description. | MaxLen: 63
    layer3_ipv4_rules: list[dict[str, Any]]  # AP ACL layer3 ipv4 rule list.
    layer3_ipv6_rules: list[dict[str, Any]]  # AP ACL layer3 ipv6 rule list.

# Nested TypedDicts for table field children (dict mode)

class AccessControlListLayer3ipv4rulesItem(TypedDict):
    """Type hints for layer3-ipv4-rules table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    rule_id: int  # Rule ID (1 - 65535). | Default: 0 | Min: 1 | Max: 65535
    comment: str  # Description. | MaxLen: 63
    srcaddr: str  # Source IP address
    srcport: int  # Source port (0 - 65535, default = 0, meaning any). | Default: 0 | Min: 0 | Max: 65535
    dstaddr: str  # Destination IP address
    dstport: int  # Destination port | Default: 0 | Min: 0 | Max: 65535
    protocol: int  # Protocol type as defined by IANA | Default: 255 | Min: 0 | Max: 255
    action: Literal["allow", "deny"]  # Policy action (allow | deny).


class AccessControlListLayer3ipv6rulesItem(TypedDict):
    """Type hints for layer3-ipv6-rules table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    rule_id: int  # Rule ID (1 - 65535). | Default: 0 | Min: 1 | Max: 65535
    comment: str  # Description. | MaxLen: 63
    srcaddr: str  # Source IPv6 address
    srcport: int  # Source port (0 - 65535, default = 0, meaning any). | Default: 0 | Min: 0 | Max: 65535
    dstaddr: str  # Destination IPv6 address
    dstport: int  # Destination port | Default: 0 | Min: 0 | Max: 65535
    protocol: int  # Protocol type as defined by IANA | Default: 255 | Min: 0 | Max: 255
    action: Literal["allow", "deny"]  # Policy action (allow | deny).


# Nested classes for table field children (object mode)

@final
class AccessControlListLayer3ipv4rulesObject:
    """Typed object for layer3-ipv4-rules table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Rule ID (1 - 65535). | Default: 0 | Min: 1 | Max: 65535
    rule_id: int
    # Description. | MaxLen: 63
    comment: str
    # Source IP address
    srcaddr: str
    # Source port (0 - 65535, default = 0, meaning any). | Default: 0 | Min: 0 | Max: 65535
    srcport: int
    # Destination IP address
    dstaddr: str
    # Destination port (0 - 65535, default = 0, meaning any). | Default: 0 | Min: 0 | Max: 65535
    dstport: int
    # Protocol type as defined by IANA | Default: 255 | Min: 0 | Max: 255
    protocol: int
    # Policy action (allow | deny).
    action: Literal["allow", "deny"]
    
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
class AccessControlListLayer3ipv6rulesObject:
    """Typed object for layer3-ipv6-rules table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Rule ID (1 - 65535). | Default: 0 | Min: 1 | Max: 65535
    rule_id: int
    # Description. | MaxLen: 63
    comment: str
    # Source IPv6 address
    srcaddr: str
    # Source port (0 - 65535, default = 0, meaning any). | Default: 0 | Min: 0 | Max: 65535
    srcport: int
    # Destination IPv6 address
    dstaddr: str
    # Destination port (0 - 65535, default = 0, meaning any). | Default: 0 | Min: 0 | Max: 65535
    dstport: int
    # Protocol type as defined by IANA | Default: 255 | Min: 0 | Max: 255
    protocol: int
    # Policy action (allow | deny).
    action: Literal["allow", "deny"]
    
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
class AccessControlListResponse(TypedDict):
    """
    Type hints for wireless_controller/access_control_list API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str  # AP access control list name. | MaxLen: 35
    comment: str  # Description. | MaxLen: 63
    layer3_ipv4_rules: list[AccessControlListLayer3ipv4rulesItem]  # AP ACL layer3 ipv4 rule list.
    layer3_ipv6_rules: list[AccessControlListLayer3ipv6rulesItem]  # AP ACL layer3 ipv6 rule list.


@final
class AccessControlListObject:
    """Typed FortiObject for wireless_controller/access_control_list with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # AP access control list name. | MaxLen: 35
    name: str
    # Description. | MaxLen: 63
    comment: str
    # AP ACL layer3 ipv4 rule list.
    layer3_ipv4_rules: list[AccessControlListLayer3ipv4rulesObject]
    # AP ACL layer3 ipv6 rule list.
    layer3_ipv6_rules: list[AccessControlListLayer3ipv6rulesObject]
    
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
    def to_dict(self) -> AccessControlListPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class AccessControlList:
    """
    Configure WiFi bridge access control list.
    
    Path: wireless_controller/access_control_list
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
    ) -> AccessControlListObject: ...
    
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
    ) -> AccessControlListObject: ...
    
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
    ) -> FortiObjectList[AccessControlListObject]: ...
    
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
    ) -> AccessControlListObject: ...
    
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
    ) -> AccessControlListObject: ...
    
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
    ) -> FortiObjectList[AccessControlListObject]: ...
    
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
    ) -> AccessControlListObject: ...
    
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
    ) -> AccessControlListObject: ...
    
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
    ) -> FortiObjectList[AccessControlListObject]: ...
    
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
    ) -> AccessControlListObject | list[AccessControlListObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: AccessControlListPayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        layer3_ipv4_rules: str | list[str] | list[dict[str, Any]] | None = ...,
        layer3_ipv6_rules: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> AccessControlListObject: ...
    
    @overload
    def post(
        self,
        payload_dict: AccessControlListPayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        layer3_ipv4_rules: str | list[str] | list[dict[str, Any]] | None = ...,
        layer3_ipv6_rules: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: AccessControlListPayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        layer3_ipv4_rules: str | list[str] | list[dict[str, Any]] | None = ...,
        layer3_ipv6_rules: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def post(
        self,
        payload_dict: AccessControlListPayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        layer3_ipv4_rules: str | list[str] | list[dict[str, Any]] | None = ...,
        layer3_ipv6_rules: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: AccessControlListPayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        layer3_ipv4_rules: str | list[str] | list[dict[str, Any]] | None = ...,
        layer3_ipv6_rules: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> AccessControlListObject: ...
    
    @overload
    def put(
        self,
        payload_dict: AccessControlListPayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        layer3_ipv4_rules: str | list[str] | list[dict[str, Any]] | None = ...,
        layer3_ipv6_rules: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: AccessControlListPayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        layer3_ipv4_rules: str | list[str] | list[dict[str, Any]] | None = ...,
        layer3_ipv6_rules: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def put(
        self,
        payload_dict: AccessControlListPayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        layer3_ipv4_rules: str | list[str] | list[dict[str, Any]] | None = ...,
        layer3_ipv6_rules: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> AccessControlListObject: ...
    
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
        payload_dict: AccessControlListPayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        layer3_ipv4_rules: str | list[str] | list[dict[str, Any]] | None = ...,
        layer3_ipv6_rules: str | list[str] | list[dict[str, Any]] | None = ...,
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
    "AccessControlList",
    "AccessControlListPayload",
    "AccessControlListResponse",
    "AccessControlListObject",
]