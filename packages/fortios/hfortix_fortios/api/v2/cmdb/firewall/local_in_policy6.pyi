from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class LocalInPolicy6Payload(TypedDict, total=False):
    """
    Type hints for firewall/local_in_policy6 payload fields.
    
    Configure user defined IPv6 local-in policies.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.firewall.schedule.group.GroupEndpoint` (via: schedule)
        - :class:`~.firewall.schedule.onetime.OnetimeEndpoint` (via: schedule)
        - :class:`~.firewall.schedule.recurring.RecurringEndpoint` (via: schedule)

    **Usage:**
        payload: LocalInPolicy6Payload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    policyid: int  # User defined local in policy ID. | Default: 0 | Min: 0 | Max: 4294967295
    uuid: str  # Universally Unique Identifier | Default: 00000000-0000-0000-0000-000000000000
    intf: list[dict[str, Any]]  # Incoming interface name from available options.
    srcaddr: list[dict[str, Any]]  # Source address object from available options.
    srcaddr_negate: Literal["enable", "disable"]  # When enabled srcaddr specifies what the source add | Default: disable
    dstaddr: list[dict[str, Any]]  # Destination address object from available options.
    internet_service6_src: Literal["enable", "disable"]  # Enable/disable use of IPv6 Internet Services in so | Default: disable
    internet_service6_src_name: list[dict[str, Any]]  # IPv6 Internet Service source name.
    internet_service6_src_group: list[dict[str, Any]]  # Internet Service6 source group name.
    internet_service6_src_custom: list[dict[str, Any]]  # Custom IPv6 Internet Service source name.
    internet_service6_src_custom_group: list[dict[str, Any]]  # Custom Internet Service6 source group name.
    internet_service6_src_fortiguard: list[dict[str, Any]]  # FortiGuard IPv6 Internet Service source name.
    dstaddr_negate: Literal["enable", "disable"]  # When enabled dstaddr specifies what the destinatio | Default: disable
    action: Literal["accept", "deny"]  # Action performed on traffic matching the policy | Default: deny
    service: list[dict[str, Any]]  # Service object from available options. Separate na
    service_negate: Literal["enable", "disable"]  # When enabled service specifies what the service mu | Default: disable
    internet_service6_src_negate: Literal["enable", "disable"]  # When enabled internet-service6-src specifies what | Default: disable
    schedule: str  # Schedule object from available options. | MaxLen: 35
    status: Literal["enable", "disable"]  # Enable/disable this local-in policy. | Default: enable
    virtual_patch: Literal["enable", "disable"]  # Enable/disable the virtual patching feature. | Default: disable
    logtraffic: Literal["enable", "disable"]  # Enable/disable local-in traffic logging. | Default: disable
    comments: str  # Comment. | MaxLen: 1023

# Nested TypedDicts for table field children (dict mode)

class LocalInPolicy6IntfItem(TypedDict):
    """Type hints for intf table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # Address name. | MaxLen: 79


class LocalInPolicy6SrcaddrItem(TypedDict):
    """Type hints for srcaddr table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # Address name. | MaxLen: 79


class LocalInPolicy6DstaddrItem(TypedDict):
    """Type hints for dstaddr table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # Address name. | MaxLen: 79


class LocalInPolicy6Internetservice6srcnameItem(TypedDict):
    """Type hints for internet-service6-src-name table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # Internet Service name. | MaxLen: 79


class LocalInPolicy6Internetservice6srcgroupItem(TypedDict):
    """Type hints for internet-service6-src-group table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # Internet Service group name. | MaxLen: 79


class LocalInPolicy6Internetservice6srccustomItem(TypedDict):
    """Type hints for internet-service6-src-custom table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # Custom Internet Service name. | MaxLen: 79


class LocalInPolicy6Internetservice6srccustomgroupItem(TypedDict):
    """Type hints for internet-service6-src-custom-group table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # Custom Internet Service6 group name. | MaxLen: 79


class LocalInPolicy6Internetservice6srcfortiguardItem(TypedDict):
    """Type hints for internet-service6-src-fortiguard table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # FortiGuard Internet Service name. | MaxLen: 79


class LocalInPolicy6ServiceItem(TypedDict):
    """Type hints for service table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # Service name. | MaxLen: 79


# Nested classes for table field children (object mode)

@final
class LocalInPolicy6IntfObject:
    """Typed object for intf table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Address name. | MaxLen: 79
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
class LocalInPolicy6SrcaddrObject:
    """Typed object for srcaddr table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Address name. | MaxLen: 79
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
class LocalInPolicy6DstaddrObject:
    """Typed object for dstaddr table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Address name. | MaxLen: 79
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
class LocalInPolicy6Internetservice6srcnameObject:
    """Typed object for internet-service6-src-name table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Internet Service name. | MaxLen: 79
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
class LocalInPolicy6Internetservice6srcgroupObject:
    """Typed object for internet-service6-src-group table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Internet Service group name. | MaxLen: 79
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
class LocalInPolicy6Internetservice6srccustomObject:
    """Typed object for internet-service6-src-custom table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Custom Internet Service name. | MaxLen: 79
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
class LocalInPolicy6Internetservice6srccustomgroupObject:
    """Typed object for internet-service6-src-custom-group table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Custom Internet Service6 group name. | MaxLen: 79
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
class LocalInPolicy6Internetservice6srcfortiguardObject:
    """Typed object for internet-service6-src-fortiguard table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # FortiGuard Internet Service name. | MaxLen: 79
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
class LocalInPolicy6ServiceObject:
    """Typed object for service table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Service name. | MaxLen: 79
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



# Response TypedDict for GET returns (all fields present in API response)
class LocalInPolicy6Response(TypedDict):
    """
    Type hints for firewall/local_in_policy6 API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    policyid: int  # User defined local in policy ID. | Default: 0 | Min: 0 | Max: 4294967295
    uuid: str  # Universally Unique Identifier | Default: 00000000-0000-0000-0000-000000000000
    intf: list[LocalInPolicy6IntfItem]  # Incoming interface name from available options.
    srcaddr: list[LocalInPolicy6SrcaddrItem]  # Source address object from available options.
    srcaddr_negate: Literal["enable", "disable"]  # When enabled srcaddr specifies what the source add | Default: disable
    dstaddr: list[LocalInPolicy6DstaddrItem]  # Destination address object from available options.
    internet_service6_src: Literal["enable", "disable"]  # Enable/disable use of IPv6 Internet Services in so | Default: disable
    internet_service6_src_name: list[LocalInPolicy6Internetservice6srcnameItem]  # IPv6 Internet Service source name.
    internet_service6_src_group: list[LocalInPolicy6Internetservice6srcgroupItem]  # Internet Service6 source group name.
    internet_service6_src_custom: list[LocalInPolicy6Internetservice6srccustomItem]  # Custom IPv6 Internet Service source name.
    internet_service6_src_custom_group: list[LocalInPolicy6Internetservice6srccustomgroupItem]  # Custom Internet Service6 source group name.
    internet_service6_src_fortiguard: list[LocalInPolicy6Internetservice6srcfortiguardItem]  # FortiGuard IPv6 Internet Service source name.
    dstaddr_negate: Literal["enable", "disable"]  # When enabled dstaddr specifies what the destinatio | Default: disable
    action: Literal["accept", "deny"]  # Action performed on traffic matching the policy | Default: deny
    service: list[LocalInPolicy6ServiceItem]  # Service object from available options. Separate na
    service_negate: Literal["enable", "disable"]  # When enabled service specifies what the service mu | Default: disable
    internet_service6_src_negate: Literal["enable", "disable"]  # When enabled internet-service6-src specifies what | Default: disable
    schedule: str  # Schedule object from available options. | MaxLen: 35
    status: Literal["enable", "disable"]  # Enable/disable this local-in policy. | Default: enable
    virtual_patch: Literal["enable", "disable"]  # Enable/disable the virtual patching feature. | Default: disable
    logtraffic: Literal["enable", "disable"]  # Enable/disable local-in traffic logging. | Default: disable
    comments: str  # Comment. | MaxLen: 1023


@final
class LocalInPolicy6Object:
    """Typed FortiObject for firewall/local_in_policy6 with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # User defined local in policy ID. | Default: 0 | Min: 0 | Max: 4294967295
    policyid: int
    # Universally Unique Identifier | Default: 00000000-0000-0000-0000-000000000000
    uuid: str
    # Incoming interface name from available options.
    intf: list[LocalInPolicy6IntfObject]
    # Source address object from available options.
    srcaddr: list[LocalInPolicy6SrcaddrObject]
    # When enabled srcaddr specifies what the source address must | Default: disable
    srcaddr_negate: Literal["enable", "disable"]
    # Destination address object from available options.
    dstaddr: list[LocalInPolicy6DstaddrObject]
    # Enable/disable use of IPv6 Internet Services in source for t | Default: disable
    internet_service6_src: Literal["enable", "disable"]
    # IPv6 Internet Service source name.
    internet_service6_src_name: list[LocalInPolicy6Internetservice6srcnameObject]
    # Internet Service6 source group name.
    internet_service6_src_group: list[LocalInPolicy6Internetservice6srcgroupObject]
    # Custom IPv6 Internet Service source name.
    internet_service6_src_custom: list[LocalInPolicy6Internetservice6srccustomObject]
    # Custom Internet Service6 source group name.
    internet_service6_src_custom_group: list[LocalInPolicy6Internetservice6srccustomgroupObject]
    # FortiGuard IPv6 Internet Service source name.
    internet_service6_src_fortiguard: list[LocalInPolicy6Internetservice6srcfortiguardObject]
    # When enabled dstaddr specifies what the destination address | Default: disable
    dstaddr_negate: Literal["enable", "disable"]
    # Action performed on traffic matching the policy | Default: deny
    action: Literal["accept", "deny"]
    # Service object from available options. Separate names with a
    service: list[LocalInPolicy6ServiceObject]
    # When enabled service specifies what the service must NOT be. | Default: disable
    service_negate: Literal["enable", "disable"]
    # When enabled internet-service6-src specifies what the servic | Default: disable
    internet_service6_src_negate: Literal["enable", "disable"]
    # Schedule object from available options. | MaxLen: 35
    schedule: str
    # Enable/disable this local-in policy. | Default: enable
    status: Literal["enable", "disable"]
    # Enable/disable the virtual patching feature. | Default: disable
    virtual_patch: Literal["enable", "disable"]
    # Enable/disable local-in traffic logging. | Default: disable
    logtraffic: Literal["enable", "disable"]
    # Comment. | MaxLen: 1023
    comments: str
    
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
    def to_dict(self) -> LocalInPolicy6Payload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class LocalInPolicy6:
    """
    Configure user defined IPv6 local-in policies.
    
    Path: firewall/local_in_policy6
    Category: cmdb
    Primary Key: policyid
    """
    
    # ================================================================
    # GET OVERLOADS - Always returns FortiObject
    # Pylance matches overloads top-to-bottom, so these must come first!
    # ================================================================
    
    # With mkey as positional arg -> returns FortiObject
    @overload
    def get(
        self,
        policyid: int,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> LocalInPolicy6Object: ...
    
    # With mkey as keyword arg -> returns FortiObject
    @overload
    def get(
        self,
        *,
        policyid: int,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> LocalInPolicy6Object: ...
    
    # Without mkey -> returns list of FortiObjects
    @overload
    def get(
        self,
        policyid: None = None,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObjectList[LocalInPolicy6Object]: ...
    
    # ================================================================
    # (removed - all GET now returns FortiObject)
    # ================================================================
    
    # With mkey as positional arg -> returns single object
    @overload
    def get(
        self,
        policyid: int,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> LocalInPolicy6Object: ...
    
    # With mkey as keyword arg -> returns single object
    @overload
    def get(
        self,
        *,
        policyid: int,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> LocalInPolicy6Object: ...
    
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
    ) -> FortiObjectList[LocalInPolicy6Object]: ...
    
    # Dict mode with mkey provided as positional arg (single dict)
    @overload
    def get(
        self,
        policyid: int,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> LocalInPolicy6Object: ...
    
    # Dict mode with mkey provided as keyword arg (single dict)
    @overload
    def get(
        self,
        *,
        policyid: int,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> LocalInPolicy6Object: ...
    
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
    ) -> FortiObjectList[LocalInPolicy6Object]: ...
    
    # Fallback overload for all other cases
    @overload
    def get(
        self,
        policyid: int | None = ...,
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
        policyid: int | None = ...,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> LocalInPolicy6Object | list[LocalInPolicy6Object] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: LocalInPolicy6Payload | None = ...,
        policyid: int | None = ...,
        uuid: str | None = ...,
        intf: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr_negate: Literal["enable", "disable"] | None = ...,
        dstaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src: Literal["enable", "disable"] | None = ...,
        internet_service6_src_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr_negate: Literal["enable", "disable"] | None = ...,
        action: Literal["accept", "deny"] | None = ...,
        service: str | list[str] | list[dict[str, Any]] | None = ...,
        service_negate: Literal["enable", "disable"] | None = ...,
        internet_service6_src_negate: Literal["enable", "disable"] | None = ...,
        schedule: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        virtual_patch: Literal["enable", "disable"] | None = ...,
        logtraffic: Literal["enable", "disable"] | None = ...,
        comments: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> LocalInPolicy6Object: ...
    
    @overload
    def post(
        self,
        payload_dict: LocalInPolicy6Payload | None = ...,
        policyid: int | None = ...,
        uuid: str | None = ...,
        intf: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr_negate: Literal["enable", "disable"] | None = ...,
        dstaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src: Literal["enable", "disable"] | None = ...,
        internet_service6_src_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr_negate: Literal["enable", "disable"] | None = ...,
        action: Literal["accept", "deny"] | None = ...,
        service: str | list[str] | list[dict[str, Any]] | None = ...,
        service_negate: Literal["enable", "disable"] | None = ...,
        internet_service6_src_negate: Literal["enable", "disable"] | None = ...,
        schedule: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        virtual_patch: Literal["enable", "disable"] | None = ...,
        logtraffic: Literal["enable", "disable"] | None = ...,
        comments: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: LocalInPolicy6Payload | None = ...,
        policyid: int | None = ...,
        uuid: str | None = ...,
        intf: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr_negate: Literal["enable", "disable"] | None = ...,
        dstaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src: Literal["enable", "disable"] | None = ...,
        internet_service6_src_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr_negate: Literal["enable", "disable"] | None = ...,
        action: Literal["accept", "deny"] | None = ...,
        service: str | list[str] | list[dict[str, Any]] | None = ...,
        service_negate: Literal["enable", "disable"] | None = ...,
        internet_service6_src_negate: Literal["enable", "disable"] | None = ...,
        schedule: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        virtual_patch: Literal["enable", "disable"] | None = ...,
        logtraffic: Literal["enable", "disable"] | None = ...,
        comments: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def post(
        self,
        payload_dict: LocalInPolicy6Payload | None = ...,
        policyid: int | None = ...,
        uuid: str | None = ...,
        intf: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr_negate: Literal["enable", "disable"] | None = ...,
        dstaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src: Literal["enable", "disable"] | None = ...,
        internet_service6_src_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr_negate: Literal["enable", "disable"] | None = ...,
        action: Literal["accept", "deny"] | None = ...,
        service: str | list[str] | list[dict[str, Any]] | None = ...,
        service_negate: Literal["enable", "disable"] | None = ...,
        internet_service6_src_negate: Literal["enable", "disable"] | None = ...,
        schedule: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        virtual_patch: Literal["enable", "disable"] | None = ...,
        logtraffic: Literal["enable", "disable"] | None = ...,
        comments: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: LocalInPolicy6Payload | None = ...,
        policyid: int | None = ...,
        uuid: str | None = ...,
        intf: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr_negate: Literal["enable", "disable"] | None = ...,
        dstaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src: Literal["enable", "disable"] | None = ...,
        internet_service6_src_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr_negate: Literal["enable", "disable"] | None = ...,
        action: Literal["accept", "deny"] | None = ...,
        service: str | list[str] | list[dict[str, Any]] | None = ...,
        service_negate: Literal["enable", "disable"] | None = ...,
        internet_service6_src_negate: Literal["enable", "disable"] | None = ...,
        schedule: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        virtual_patch: Literal["enable", "disable"] | None = ...,
        logtraffic: Literal["enable", "disable"] | None = ...,
        comments: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> LocalInPolicy6Object: ...
    
    @overload
    def put(
        self,
        payload_dict: LocalInPolicy6Payload | None = ...,
        policyid: int | None = ...,
        uuid: str | None = ...,
        intf: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr_negate: Literal["enable", "disable"] | None = ...,
        dstaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src: Literal["enable", "disable"] | None = ...,
        internet_service6_src_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr_negate: Literal["enable", "disable"] | None = ...,
        action: Literal["accept", "deny"] | None = ...,
        service: str | list[str] | list[dict[str, Any]] | None = ...,
        service_negate: Literal["enable", "disable"] | None = ...,
        internet_service6_src_negate: Literal["enable", "disable"] | None = ...,
        schedule: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        virtual_patch: Literal["enable", "disable"] | None = ...,
        logtraffic: Literal["enable", "disable"] | None = ...,
        comments: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: LocalInPolicy6Payload | None = ...,
        policyid: int | None = ...,
        uuid: str | None = ...,
        intf: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr_negate: Literal["enable", "disable"] | None = ...,
        dstaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src: Literal["enable", "disable"] | None = ...,
        internet_service6_src_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr_negate: Literal["enable", "disable"] | None = ...,
        action: Literal["accept", "deny"] | None = ...,
        service: str | list[str] | list[dict[str, Any]] | None = ...,
        service_negate: Literal["enable", "disable"] | None = ...,
        internet_service6_src_negate: Literal["enable", "disable"] | None = ...,
        schedule: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        virtual_patch: Literal["enable", "disable"] | None = ...,
        logtraffic: Literal["enable", "disable"] | None = ...,
        comments: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def put(
        self,
        payload_dict: LocalInPolicy6Payload | None = ...,
        policyid: int | None = ...,
        uuid: str | None = ...,
        intf: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr_negate: Literal["enable", "disable"] | None = ...,
        dstaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src: Literal["enable", "disable"] | None = ...,
        internet_service6_src_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr_negate: Literal["enable", "disable"] | None = ...,
        action: Literal["accept", "deny"] | None = ...,
        service: str | list[str] | list[dict[str, Any]] | None = ...,
        service_negate: Literal["enable", "disable"] | None = ...,
        internet_service6_src_negate: Literal["enable", "disable"] | None = ...,
        schedule: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        virtual_patch: Literal["enable", "disable"] | None = ...,
        logtraffic: Literal["enable", "disable"] | None = ...,
        comments: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        policyid: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> LocalInPolicy6Object: ...
    
    @overload
    def delete(
        self,
        policyid: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def delete(
        self,
        policyid: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def delete(
        self,
        policyid: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def exists(
        self,
        policyid: int,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: LocalInPolicy6Payload | None = ...,
        policyid: int | None = ...,
        uuid: str | None = ...,
        intf: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr_negate: Literal["enable", "disable"] | None = ...,
        dstaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src: Literal["enable", "disable"] | None = ...,
        internet_service6_src_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr_negate: Literal["enable", "disable"] | None = ...,
        action: Literal["accept", "deny"] | None = ...,
        service: str | list[str] | list[dict[str, Any]] | None = ...,
        service_negate: Literal["enable", "disable"] | None = ...,
        internet_service6_src_negate: Literal["enable", "disable"] | None = ...,
        schedule: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        virtual_patch: Literal["enable", "disable"] | None = ...,
        logtraffic: Literal["enable", "disable"] | None = ...,
        comments: str | None = ...,
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
    "LocalInPolicy6",
    "LocalInPolicy6Payload",
    "LocalInPolicy6Response",
    "LocalInPolicy6Object",
]