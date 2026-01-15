from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class GeoipOverridePayload(TypedDict, total=False):
    """
    Type hints for system/geoip_override payload fields.
    
    Configure geographical location mapping for IP address(es) to override mappings from FortiGuard.
    
    **Usage:**
        payload: GeoipOverridePayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # Location name. | MaxLen: 63
    description: str  # Description. | MaxLen: 127
    country_id: str  # Two character Country ID code. | MaxLen: 2
    ip_range: list[dict[str, Any]]  # Table of IP ranges assigned to country.
    ip6_range: list[dict[str, Any]]  # Table of IPv6 ranges assigned to country.

# Nested TypedDicts for table field children (dict mode)

class GeoipOverrideIprangeItem(TypedDict):
    """Type hints for ip-range table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    id: int  # ID of individual entry in the IP range table. | Default: 0 | Min: 0 | Max: 65535
    start_ip: str  # Starting IP address, inclusive, of the address ran | Default: 0.0.0.0
    end_ip: str  # Ending IP address, inclusive, of the address range | Default: 0.0.0.0


class GeoipOverrideIp6rangeItem(TypedDict):
    """Type hints for ip6-range table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    id: int  # ID of individual entry in the IPv6 range table. | Default: 0 | Min: 0 | Max: 65535
    start_ip: str  # Starting IP address, inclusive, of the address ran | Default: ::
    end_ip: str  # Ending IP address, inclusive, of the address range | Default: ::


# Nested classes for table field children (object mode)

@final
class GeoipOverrideIprangeObject:
    """Typed object for ip-range table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # ID of individual entry in the IP range table. | Default: 0 | Min: 0 | Max: 65535
    id: int
    # Starting IP address, inclusive, of the address range | Default: 0.0.0.0
    start_ip: str
    # Ending IP address, inclusive, of the address range | Default: 0.0.0.0
    end_ip: str
    
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
class GeoipOverrideIp6rangeObject:
    """Typed object for ip6-range table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # ID of individual entry in the IPv6 range table. | Default: 0 | Min: 0 | Max: 65535
    id: int
    # Starting IP address, inclusive, of the address range | Default: ::
    start_ip: str
    # Ending IP address, inclusive, of the address range | Default: ::
    end_ip: str
    
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
class GeoipOverrideResponse(TypedDict):
    """
    Type hints for system/geoip_override API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str  # Location name. | MaxLen: 63
    description: str  # Description. | MaxLen: 127
    country_id: str  # Two character Country ID code. | MaxLen: 2
    ip_range: list[GeoipOverrideIprangeItem]  # Table of IP ranges assigned to country.
    ip6_range: list[GeoipOverrideIp6rangeItem]  # Table of IPv6 ranges assigned to country.


@final
class GeoipOverrideObject:
    """Typed FortiObject for system/geoip_override with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Location name. | MaxLen: 63
    name: str
    # Description. | MaxLen: 127
    description: str
    # Two character Country ID code. | MaxLen: 2
    country_id: str
    # Table of IP ranges assigned to country.
    ip_range: list[GeoipOverrideIprangeObject]
    # Table of IPv6 ranges assigned to country.
    ip6_range: list[GeoipOverrideIp6rangeObject]
    
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
    def to_dict(self) -> GeoipOverridePayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class GeoipOverride:
    """
    Configure geographical location mapping for IP address(es) to override mappings from FortiGuard.
    
    Path: system/geoip_override
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
    ) -> GeoipOverrideObject: ...
    
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
    ) -> GeoipOverrideObject: ...
    
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
    ) -> FortiObjectList[GeoipOverrideObject]: ...
    
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
    ) -> GeoipOverrideObject: ...
    
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
    ) -> GeoipOverrideObject: ...
    
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
    ) -> FortiObjectList[GeoipOverrideObject]: ...
    
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
    ) -> GeoipOverrideObject: ...
    
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
    ) -> GeoipOverrideObject: ...
    
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
    ) -> FortiObjectList[GeoipOverrideObject]: ...
    
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
    ) -> GeoipOverrideObject | list[GeoipOverrideObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: GeoipOverridePayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        country_id: str | None = ...,
        ip_range: str | list[str] | list[dict[str, Any]] | None = ...,
        ip6_range: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> GeoipOverrideObject: ...
    
    @overload
    def post(
        self,
        payload_dict: GeoipOverridePayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        country_id: str | None = ...,
        ip_range: str | list[str] | list[dict[str, Any]] | None = ...,
        ip6_range: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: GeoipOverridePayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        country_id: str | None = ...,
        ip_range: str | list[str] | list[dict[str, Any]] | None = ...,
        ip6_range: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def post(
        self,
        payload_dict: GeoipOverridePayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        country_id: str | None = ...,
        ip_range: str | list[str] | list[dict[str, Any]] | None = ...,
        ip6_range: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: GeoipOverridePayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        country_id: str | None = ...,
        ip_range: str | list[str] | list[dict[str, Any]] | None = ...,
        ip6_range: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> GeoipOverrideObject: ...
    
    @overload
    def put(
        self,
        payload_dict: GeoipOverridePayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        country_id: str | None = ...,
        ip_range: str | list[str] | list[dict[str, Any]] | None = ...,
        ip6_range: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: GeoipOverridePayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        country_id: str | None = ...,
        ip_range: str | list[str] | list[dict[str, Any]] | None = ...,
        ip6_range: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def put(
        self,
        payload_dict: GeoipOverridePayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        country_id: str | None = ...,
        ip_range: str | list[str] | list[dict[str, Any]] | None = ...,
        ip6_range: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> GeoipOverrideObject: ...
    
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
        payload_dict: GeoipOverridePayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        country_id: str | None = ...,
        ip_range: str | list[str] | list[dict[str, Any]] | None = ...,
        ip6_range: str | list[str] | list[dict[str, Any]] | None = ...,
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
    "GeoipOverride",
    "GeoipOverridePayload",
    "GeoipOverrideResponse",
    "GeoipOverrideObject",
]