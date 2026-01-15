from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject
from hfortix_core.types import MutationResponse, RawAPIResponse

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class UrlfilterPayload(TypedDict, total=False):
    """
    Type hints for webfilter/urlfilter payload fields.
    
    Configure URL filter lists.
    
    **Usage:**
        payload: UrlfilterPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    id: int  # ID. | Default: 0 | Min: 0 | Max: 4294967295
    name: str  # Name of URL filter list. | MaxLen: 63
    comment: str  # Optional comments. | MaxLen: 255
    one_arm_ips_urlfilter: Literal["enable", "disable"]  # Enable/disable DNS resolver for one-arm IPS URL fi | Default: disable
    ip_addr_block: Literal["enable", "disable"]  # Enable/disable blocking URLs when the hostname app | Default: disable
    ip4_mapped_ip6: Literal["enable", "disable"]  # Enable/disable matching of IPv4 mapped IPv6 URLs. | Default: disable
    include_subdomains: Literal["enable", "disable"]  # Enable/disable matching subdomains. Applies only t | Default: enable
    entries: list[dict[str, Any]]  # URL filter entries.

# Nested TypedDicts for table field children (dict mode)

class UrlfilterEntriesItem(TypedDict):
    """Type hints for entries table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    id: int  # Id. | Default: 0 | Min: 0 | Max: 4294967295
    url: str  # URL to be filtered. | MaxLen: 511
    type: Literal["simple", "regex", "wildcard"]  # Filter type (simple, regex, or wildcard). | Default: simple
    action: Literal["exempt", "block", "allow", "monitor"]  # Action to take for URL filter matches. | Default: exempt
    antiphish_action: Literal["block", "log"]  # Action to take for AntiPhishing matches. | Default: block
    status: Literal["enable", "disable"]  # Enable/disable this URL filter. | Default: enable
    exempt: Literal["av", "web-content", "activex-java-cookie", "dlp", "fortiguard", "range-block", "pass", "antiphish", "all"]  # If action is set to exempt, select the security pr | Default: av web-content activex-java-cookie dlp fortiguard range-block antiphish all
    web_proxy_profile: str  # Web proxy profile. | MaxLen: 63
    referrer_host: str  # Referrer host name. | MaxLen: 255
    dns_address_family: Literal["ipv4", "ipv6", "both"]  # Resolve IPv4 address, IPv6 address, or both from D | Default: ipv4
    comment: str  # Comment. | MaxLen: 255


# Nested classes for table field children (object mode)

@final
class UrlfilterEntriesObject:
    """Typed object for entries table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Id. | Default: 0 | Min: 0 | Max: 4294967295
    id: int
    # URL to be filtered. | MaxLen: 511
    url: str
    # Filter type (simple, regex, or wildcard). | Default: simple
    type: Literal["simple", "regex", "wildcard"]
    # Action to take for URL filter matches. | Default: exempt
    action: Literal["exempt", "block", "allow", "monitor"]
    # Action to take for AntiPhishing matches. | Default: block
    antiphish_action: Literal["block", "log"]
    # Enable/disable this URL filter. | Default: enable
    status: Literal["enable", "disable"]
    # If action is set to exempt, select the security profile oper | Default: av web-content activex-java-cookie dlp fortiguard range-block antiphish all
    exempt: Literal["av", "web-content", "activex-java-cookie", "dlp", "fortiguard", "range-block", "pass", "antiphish", "all"]
    # Web proxy profile. | MaxLen: 63
    web_proxy_profile: str
    # Referrer host name. | MaxLen: 255
    referrer_host: str
    # Resolve IPv4 address, IPv6 address, or both from DNS server. | Default: ipv4
    dns_address_family: Literal["ipv4", "ipv6", "both"]
    # Comment. | MaxLen: 255
    comment: str
    
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
class UrlfilterResponse(TypedDict):
    """
    Type hints for webfilter/urlfilter API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    id: int  # ID. | Default: 0 | Min: 0 | Max: 4294967295
    name: str  # Name of URL filter list. | MaxLen: 63
    comment: str  # Optional comments. | MaxLen: 255
    one_arm_ips_urlfilter: Literal["enable", "disable"]  # Enable/disable DNS resolver for one-arm IPS URL fi | Default: disable
    ip_addr_block: Literal["enable", "disable"]  # Enable/disable blocking URLs when the hostname app | Default: disable
    ip4_mapped_ip6: Literal["enable", "disable"]  # Enable/disable matching of IPv4 mapped IPv6 URLs. | Default: disable
    include_subdomains: Literal["enable", "disable"]  # Enable/disable matching subdomains. Applies only t | Default: enable
    entries: list[UrlfilterEntriesItem]  # URL filter entries.


@final
class UrlfilterObject:
    """Typed FortiObject for webfilter/urlfilter with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # ID. | Default: 0 | Min: 0 | Max: 4294967295
    id: int
    # Name of URL filter list. | MaxLen: 63
    name: str
    # Optional comments. | MaxLen: 255
    comment: str
    # Enable/disable DNS resolver for one-arm IPS URL filter opera | Default: disable
    one_arm_ips_urlfilter: Literal["enable", "disable"]
    # Enable/disable blocking URLs when the hostname appears as an | Default: disable
    ip_addr_block: Literal["enable", "disable"]
    # Enable/disable matching of IPv4 mapped IPv6 URLs. | Default: disable
    ip4_mapped_ip6: Literal["enable", "disable"]
    # Enable/disable matching subdomains. Applies only to simple t | Default: enable
    include_subdomains: Literal["enable", "disable"]
    # URL filter entries.
    entries: list[UrlfilterEntriesObject]
    
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
    def to_dict(self) -> UrlfilterPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Urlfilter:
    """
    Configure URL filter lists.
    
    Path: webfilter/urlfilter
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
    ) -> UrlfilterObject: ...
    
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
    ) -> UrlfilterObject: ...
    
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
    ) -> list[UrlfilterObject]: ...
    
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
    ) -> UrlfilterObject: ...
    
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
    ) -> UrlfilterObject: ...
    
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
    ) -> list[UrlfilterObject]: ...
    
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
    ) -> UrlfilterObject: ...
    
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
    ) -> UrlfilterObject: ...
    
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
    ) -> list[UrlfilterObject]: ...
    
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
    ) -> UrlfilterObject | list[UrlfilterObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: UrlfilterPayload | None = ...,
        id: int | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        one_arm_ips_urlfilter: Literal["enable", "disable"] | None = ...,
        ip_addr_block: Literal["enable", "disable"] | None = ...,
        ip4_mapped_ip6: Literal["enable", "disable"] | None = ...,
        include_subdomains: Literal["enable", "disable"] | None = ...,
        entries: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> UrlfilterObject: ...
    
    @overload
    def post(
        self,
        payload_dict: UrlfilterPayload | None = ...,
        id: int | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        one_arm_ips_urlfilter: Literal["enable", "disable"] | None = ...,
        ip_addr_block: Literal["enable", "disable"] | None = ...,
        ip4_mapped_ip6: Literal["enable", "disable"] | None = ...,
        include_subdomains: Literal["enable", "disable"] | None = ...,
        entries: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    # raw_json=True returns the full API envelope
    @overload
    def post(
        self,
        payload_dict: UrlfilterPayload | None = ...,
        id: int | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        one_arm_ips_urlfilter: Literal["enable", "disable"] | None = ...,
        ip_addr_block: Literal["enable", "disable"] | None = ...,
        ip4_mapped_ip6: Literal["enable", "disable"] | None = ...,
        include_subdomains: Literal["enable", "disable"] | None = ...,
        entries: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> RawAPIResponse: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: UrlfilterPayload | None = ...,
        id: int | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        one_arm_ips_urlfilter: Literal["enable", "disable"] | None = ...,
        ip_addr_block: Literal["enable", "disable"] | None = ...,
        ip4_mapped_ip6: Literal["enable", "disable"] | None = ...,
        include_subdomains: Literal["enable", "disable"] | None = ...,
        entries: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    def post(
        self,
        payload_dict: UrlfilterPayload | None = ...,
        id: int | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        one_arm_ips_urlfilter: Literal["enable", "disable"] | None = ...,
        ip_addr_block: Literal["enable", "disable"] | None = ...,
        ip4_mapped_ip6: Literal["enable", "disable"] | None = ...,
        include_subdomains: Literal["enable", "disable"] | None = ...,
        entries: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: UrlfilterPayload | None = ...,
        id: int | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        one_arm_ips_urlfilter: Literal["enable", "disable"] | None = ...,
        ip_addr_block: Literal["enable", "disable"] | None = ...,
        ip4_mapped_ip6: Literal["enable", "disable"] | None = ...,
        include_subdomains: Literal["enable", "disable"] | None = ...,
        entries: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> UrlfilterObject: ...
    
    @overload
    def put(
        self,
        payload_dict: UrlfilterPayload | None = ...,
        id: int | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        one_arm_ips_urlfilter: Literal["enable", "disable"] | None = ...,
        ip_addr_block: Literal["enable", "disable"] | None = ...,
        ip4_mapped_ip6: Literal["enable", "disable"] | None = ...,
        include_subdomains: Literal["enable", "disable"] | None = ...,
        entries: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    # raw_json=True returns the full API envelope
    @overload
    def put(
        self,
        payload_dict: UrlfilterPayload | None = ...,
        id: int | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        one_arm_ips_urlfilter: Literal["enable", "disable"] | None = ...,
        ip_addr_block: Literal["enable", "disable"] | None = ...,
        ip4_mapped_ip6: Literal["enable", "disable"] | None = ...,
        include_subdomains: Literal["enable", "disable"] | None = ...,
        entries: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> RawAPIResponse: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: UrlfilterPayload | None = ...,
        id: int | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        one_arm_ips_urlfilter: Literal["enable", "disable"] | None = ...,
        ip_addr_block: Literal["enable", "disable"] | None = ...,
        ip4_mapped_ip6: Literal["enable", "disable"] | None = ...,
        include_subdomains: Literal["enable", "disable"] | None = ...,
        entries: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    def put(
        self,
        payload_dict: UrlfilterPayload | None = ...,
        id: int | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        one_arm_ips_urlfilter: Literal["enable", "disable"] | None = ...,
        ip_addr_block: Literal["enable", "disable"] | None = ...,
        ip4_mapped_ip6: Literal["enable", "disable"] | None = ...,
        include_subdomains: Literal["enable", "disable"] | None = ...,
        entries: str | list[str] | list[dict[str, Any]] | None = ...,
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
    ) -> UrlfilterObject: ...
    
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
        payload_dict: UrlfilterPayload | None = ...,
        id: int | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        one_arm_ips_urlfilter: Literal["enable", "disable"] | None = ...,
        ip_addr_block: Literal["enable", "disable"] | None = ...,
        ip4_mapped_ip6: Literal["enable", "disable"] | None = ...,
        include_subdomains: Literal["enable", "disable"] | None = ...,
        entries: str | list[str] | list[dict[str, Any]] | None = ...,
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
    "Urlfilter",
    "UrlfilterPayload",
    "UrlfilterResponse",
    "UrlfilterObject",
]