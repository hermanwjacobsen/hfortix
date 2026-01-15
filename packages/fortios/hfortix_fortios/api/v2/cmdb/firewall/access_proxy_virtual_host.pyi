from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject
from hfortix_core.types import MutationResponse, RawAPIResponse

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class AccessProxyVirtualHostPayload(TypedDict, total=False):
    """
    Type hints for firewall/access_proxy_virtual_host payload fields.
    
    Configure Access Proxy virtual hosts.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.system.replacemsg-group.ReplacemsgGroupEndpoint` (via: replacemsg-group)

    **Usage:**
        payload: AccessProxyVirtualHostPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # Virtual host name. | MaxLen: 79
    ssl_certificate: list[dict[str, Any]]  # SSL certificates for this host.
    host: str  # The host name. | MaxLen: 79
    host_type: Literal["sub-string", "wildcard"]  # Type of host pattern. | Default: sub-string
    replacemsg_group: str  # Access-proxy-virtual-host replacement message over | MaxLen: 35
    empty_cert_action: Literal["accept", "block", "accept-unmanageable"]  # Action for an empty client certificate. | Default: block
    user_agent_detect: Literal["disable", "enable"]  # Enable/disable detecting device type by HTTP user- | Default: enable
    client_cert: Literal["disable", "enable"]  # Enable/disable requesting client certificate. | Default: enable

# Nested TypedDicts for table field children (dict mode)

class AccessProxyVirtualHostSslcertificateItem(TypedDict):
    """Type hints for ssl-certificate table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # Certificate list. | MaxLen: 79


# Nested classes for table field children (object mode)

@final
class AccessProxyVirtualHostSslcertificateObject:
    """Typed object for ssl-certificate table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Certificate list. | MaxLen: 79
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
class AccessProxyVirtualHostResponse(TypedDict):
    """
    Type hints for firewall/access_proxy_virtual_host API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str  # Virtual host name. | MaxLen: 79
    ssl_certificate: list[AccessProxyVirtualHostSslcertificateItem]  # SSL certificates for this host.
    host: str  # The host name. | MaxLen: 79
    host_type: Literal["sub-string", "wildcard"]  # Type of host pattern. | Default: sub-string
    replacemsg_group: str  # Access-proxy-virtual-host replacement message over | MaxLen: 35
    empty_cert_action: Literal["accept", "block", "accept-unmanageable"]  # Action for an empty client certificate. | Default: block
    user_agent_detect: Literal["disable", "enable"]  # Enable/disable detecting device type by HTTP user- | Default: enable
    client_cert: Literal["disable", "enable"]  # Enable/disable requesting client certificate. | Default: enable


@final
class AccessProxyVirtualHostObject:
    """Typed FortiObject for firewall/access_proxy_virtual_host with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Virtual host name. | MaxLen: 79
    name: str
    # SSL certificates for this host.
    ssl_certificate: list[AccessProxyVirtualHostSslcertificateObject]
    # The host name. | MaxLen: 79
    host: str
    # Type of host pattern. | Default: sub-string
    host_type: Literal["sub-string", "wildcard"]
    # Access-proxy-virtual-host replacement message override group | MaxLen: 35
    replacemsg_group: str
    # Action for an empty client certificate. | Default: block
    empty_cert_action: Literal["accept", "block", "accept-unmanageable"]
    # Enable/disable detecting device type by HTTP user-agent if n | Default: enable
    user_agent_detect: Literal["disable", "enable"]
    # Enable/disable requesting client certificate. | Default: enable
    client_cert: Literal["disable", "enable"]
    
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
    def to_dict(self) -> AccessProxyVirtualHostPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class AccessProxyVirtualHost:
    """
    Configure Access Proxy virtual hosts.
    
    Path: firewall/access_proxy_virtual_host
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
    ) -> AccessProxyVirtualHostObject: ...
    
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
    ) -> AccessProxyVirtualHostObject: ...
    
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
    ) -> list[AccessProxyVirtualHostObject]: ...
    
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
        raw_json: Literal[False] = ...,
        *,
        **kwargs: Any,
    ) -> AccessProxyVirtualHostObject: ...
    
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
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> AccessProxyVirtualHostObject: ...
    
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
    ) -> list[AccessProxyVirtualHostObject]: ...
    
    # raw_json=True returns the full API envelope
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
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> RawAPIResponse: ...
    
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
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> AccessProxyVirtualHostObject: ...
    
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
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> AccessProxyVirtualHostObject: ...
    
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
    ) -> list[AccessProxyVirtualHostObject]: ...
    
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
        raw_json: bool = ...,
        **kwargs: Any,
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
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> AccessProxyVirtualHostObject | list[AccessProxyVirtualHostObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: AccessProxyVirtualHostPayload | None = ...,
        name: str | None = ...,
        ssl_certificate: str | list[str] | list[dict[str, Any]] | None = ...,
        host: str | None = ...,
        host_type: Literal["sub-string", "wildcard"] | None = ...,
        replacemsg_group: str | None = ...,
        empty_cert_action: Literal["accept", "block", "accept-unmanageable"] | None = ...,
        user_agent_detect: Literal["disable", "enable"] | None = ...,
        client_cert: Literal["disable", "enable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> AccessProxyVirtualHostObject: ...
    
    @overload
    def post(
        self,
        payload_dict: AccessProxyVirtualHostPayload | None = ...,
        name: str | None = ...,
        ssl_certificate: str | list[str] | list[dict[str, Any]] | None = ...,
        host: str | None = ...,
        host_type: Literal["sub-string", "wildcard"] | None = ...,
        replacemsg_group: str | None = ...,
        empty_cert_action: Literal["accept", "block", "accept-unmanageable"] | None = ...,
        user_agent_detect: Literal["disable", "enable"] | None = ...,
        client_cert: Literal["disable", "enable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    # raw_json=True returns the full API envelope
    @overload
    def post(
        self,
        payload_dict: AccessProxyVirtualHostPayload | None = ...,
        name: str | None = ...,
        ssl_certificate: str | list[str] | list[dict[str, Any]] | None = ...,
        host: str | None = ...,
        host_type: Literal["sub-string", "wildcard"] | None = ...,
        replacemsg_group: str | None = ...,
        empty_cert_action: Literal["accept", "block", "accept-unmanageable"] | None = ...,
        user_agent_detect: Literal["disable", "enable"] | None = ...,
        client_cert: Literal["disable", "enable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> RawAPIResponse: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: AccessProxyVirtualHostPayload | None = ...,
        name: str | None = ...,
        ssl_certificate: str | list[str] | list[dict[str, Any]] | None = ...,
        host: str | None = ...,
        host_type: Literal["sub-string", "wildcard"] | None = ...,
        replacemsg_group: str | None = ...,
        empty_cert_action: Literal["accept", "block", "accept-unmanageable"] | None = ...,
        user_agent_detect: Literal["disable", "enable"] | None = ...,
        client_cert: Literal["disable", "enable"] | None = ...,
        vdom: str | bool | None = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    def post(
        self,
        payload_dict: AccessProxyVirtualHostPayload | None = ...,
        name: str | None = ...,
        ssl_certificate: str | list[str] | list[dict[str, Any]] | None = ...,
        host: str | None = ...,
        host_type: Literal["sub-string", "wildcard"] | None = ...,
        replacemsg_group: str | None = ...,
        empty_cert_action: Literal["accept", "block", "accept-unmanageable"] | None = ...,
        user_agent_detect: Literal["disable", "enable"] | None = ...,
        client_cert: Literal["disable", "enable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: AccessProxyVirtualHostPayload | None = ...,
        name: str | None = ...,
        ssl_certificate: str | list[str] | list[dict[str, Any]] | None = ...,
        host: str | None = ...,
        host_type: Literal["sub-string", "wildcard"] | None = ...,
        replacemsg_group: str | None = ...,
        empty_cert_action: Literal["accept", "block", "accept-unmanageable"] | None = ...,
        user_agent_detect: Literal["disable", "enable"] | None = ...,
        client_cert: Literal["disable", "enable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> AccessProxyVirtualHostObject: ...
    
    @overload
    def put(
        self,
        payload_dict: AccessProxyVirtualHostPayload | None = ...,
        name: str | None = ...,
        ssl_certificate: str | list[str] | list[dict[str, Any]] | None = ...,
        host: str | None = ...,
        host_type: Literal["sub-string", "wildcard"] | None = ...,
        replacemsg_group: str | None = ...,
        empty_cert_action: Literal["accept", "block", "accept-unmanageable"] | None = ...,
        user_agent_detect: Literal["disable", "enable"] | None = ...,
        client_cert: Literal["disable", "enable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    # raw_json=True returns the full API envelope
    @overload
    def put(
        self,
        payload_dict: AccessProxyVirtualHostPayload | None = ...,
        name: str | None = ...,
        ssl_certificate: str | list[str] | list[dict[str, Any]] | None = ...,
        host: str | None = ...,
        host_type: Literal["sub-string", "wildcard"] | None = ...,
        replacemsg_group: str | None = ...,
        empty_cert_action: Literal["accept", "block", "accept-unmanageable"] | None = ...,
        user_agent_detect: Literal["disable", "enable"] | None = ...,
        client_cert: Literal["disable", "enable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> RawAPIResponse: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: AccessProxyVirtualHostPayload | None = ...,
        name: str | None = ...,
        ssl_certificate: str | list[str] | list[dict[str, Any]] | None = ...,
        host: str | None = ...,
        host_type: Literal["sub-string", "wildcard"] | None = ...,
        replacemsg_group: str | None = ...,
        empty_cert_action: Literal["accept", "block", "accept-unmanageable"] | None = ...,
        user_agent_detect: Literal["disable", "enable"] | None = ...,
        client_cert: Literal["disable", "enable"] | None = ...,
        vdom: str | bool | None = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    def put(
        self,
        payload_dict: AccessProxyVirtualHostPayload | None = ...,
        name: str | None = ...,
        ssl_certificate: str | list[str] | list[dict[str, Any]] | None = ...,
        host: str | None = ...,
        host_type: Literal["sub-string", "wildcard"] | None = ...,
        replacemsg_group: str | None = ...,
        empty_cert_action: Literal["accept", "block", "accept-unmanageable"] | None = ...,
        user_agent_detect: Literal["disable", "enable"] | None = ...,
        client_cert: Literal["disable", "enable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> AccessProxyVirtualHostObject: ...
    
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    # raw_json=True returns the full API envelope
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> RawAPIResponse: ...
    
    # Default overload
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: AccessProxyVirtualHostPayload | None = ...,
        name: str | None = ...,
        ssl_certificate: str | list[str] | list[dict[str, Any]] | None = ...,
        host: str | None = ...,
        host_type: Literal["sub-string", "wildcard"] | None = ...,
        replacemsg_group: str | None = ...,
        empty_cert_action: Literal["accept", "block", "accept-unmanageable"] | None = ...,
        user_agent_detect: Literal["disable", "enable"] | None = ...,
        client_cert: Literal["disable", "enable"] | None = ...,
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
    "AccessProxyVirtualHost",
    "AccessProxyVirtualHostPayload",
    "AccessProxyVirtualHostResponse",
    "AccessProxyVirtualHostObject",
]