from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList
from hfortix_core.types import MutationResponse

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class ExternalIdentityProviderPayload(TypedDict, total=False):
    """
    Type hints for user/external_identity_provider payload fields.
    
    Configure external identity provider.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.system.interface.InterfaceEndpoint` (via: interface)

    **Usage:**
        payload: ExternalIdentityProviderPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # External identity provider name. | MaxLen: 35
    type: Literal["ms-graph"]  # External identity provider type.
    version: Literal["v1.0", "beta"]  # External identity API version.
    url: str  # External identity provider URL | MaxLen: 127
    user_attr_name: str  # User attribute name in authentication query. | Default: userPrincipalName | MaxLen: 63
    group_attr_name: str  # Group attribute name in authentication query. | Default: id | MaxLen: 63
    port: int  # External identity provider service port number | Default: 0 | Min: 0 | Max: 65535
    source_ip: str  # Use this IPv4/v6 address to connect to the externa | MaxLen: 63
    interface_select_method: Literal["auto", "sdwan", "specify"]  # Specify how to select outgoing interface to reach | Default: auto
    interface: str  # Specify outgoing interface to reach server. | MaxLen: 15
    vrf_select: int  # VRF ID used for connection to server. | Default: 0 | Min: 0 | Max: 511
    server_identity_check: Literal["disable", "enable"]  # Enable/disable server's identity check against its | Default: enable
    timeout: int  # Connection timeout value in seconds (default=5). | Default: 5 | Min: 1 | Max: 60

# Nested TypedDicts for table field children (dict mode)

# Nested classes for table field children (object mode)


# Response TypedDict for GET returns (all fields present in API response)
class ExternalIdentityProviderResponse(TypedDict):
    """
    Type hints for user/external_identity_provider API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str  # External identity provider name. | MaxLen: 35
    type: Literal["ms-graph"]  # External identity provider type.
    version: Literal["v1.0", "beta"]  # External identity API version.
    url: str  # External identity provider URL | MaxLen: 127
    user_attr_name: str  # User attribute name in authentication query. | Default: userPrincipalName | MaxLen: 63
    group_attr_name: str  # Group attribute name in authentication query. | Default: id | MaxLen: 63
    port: int  # External identity provider service port number | Default: 0 | Min: 0 | Max: 65535
    source_ip: str  # Use this IPv4/v6 address to connect to the externa | MaxLen: 63
    interface_select_method: Literal["auto", "sdwan", "specify"]  # Specify how to select outgoing interface to reach | Default: auto
    interface: str  # Specify outgoing interface to reach server. | MaxLen: 15
    vrf_select: int  # VRF ID used for connection to server. | Default: 0 | Min: 0 | Max: 511
    server_identity_check: Literal["disable", "enable"]  # Enable/disable server's identity check against its | Default: enable
    timeout: int  # Connection timeout value in seconds (default=5). | Default: 5 | Min: 1 | Max: 60


@final
class ExternalIdentityProviderObject:
    """Typed FortiObject for user/external_identity_provider with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # External identity provider name. | MaxLen: 35
    name: str
    # External identity provider type.
    type: Literal["ms-graph"]
    # External identity API version.
    version: Literal["v1.0", "beta"]
    # External identity provider URL | MaxLen: 127
    url: str
    # User attribute name in authentication query. | Default: userPrincipalName | MaxLen: 63
    user_attr_name: str
    # Group attribute name in authentication query. | Default: id | MaxLen: 63
    group_attr_name: str
    # External identity provider service port number | Default: 0 | Min: 0 | Max: 65535
    port: int
    # Use this IPv4/v6 address to connect to the external identity | MaxLen: 63
    source_ip: str
    # Specify how to select outgoing interface to reach server. | Default: auto
    interface_select_method: Literal["auto", "sdwan", "specify"]
    # Specify outgoing interface to reach server. | MaxLen: 15
    interface: str
    # VRF ID used for connection to server. | Default: 0 | Min: 0 | Max: 511
    vrf_select: int
    # Enable/disable server's identity check against its certifica | Default: enable
    server_identity_check: Literal["disable", "enable"]
    # Connection timeout value in seconds (default=5). | Default: 5 | Min: 1 | Max: 60
    timeout: int
    
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
    def to_dict(self) -> ExternalIdentityProviderPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class ExternalIdentityProvider:
    """
    Configure external identity provider.
    
    Path: user/external_identity_provider
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
    ) -> ExternalIdentityProviderObject: ...
    
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
    ) -> ExternalIdentityProviderObject: ...
    
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
    ) -> FortiObjectList[ExternalIdentityProviderObject]: ...
    
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
    ) -> ExternalIdentityProviderObject: ...
    
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
    ) -> ExternalIdentityProviderObject: ...
    
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
    ) -> FortiObjectList[ExternalIdentityProviderObject]: ...
    
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
    ) -> ExternalIdentityProviderObject: ...
    
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
    ) -> ExternalIdentityProviderObject: ...
    
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
    ) -> FortiObjectList[ExternalIdentityProviderObject]: ...
    
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
    ) -> ExternalIdentityProviderObject | list[ExternalIdentityProviderObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: ExternalIdentityProviderPayload | None = ...,
        name: str | None = ...,
        type: Literal["ms-graph"] | None = ...,
        version: Literal["v1.0", "beta"] | None = ...,
        url: str | None = ...,
        user_attr_name: str | None = ...,
        group_attr_name: str | None = ...,
        port: int | None = ...,
        source_ip: str | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        server_identity_check: Literal["disable", "enable"] | None = ...,
        timeout: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> ExternalIdentityProviderObject: ...
    
    @overload
    def post(
        self,
        payload_dict: ExternalIdentityProviderPayload | None = ...,
        name: str | None = ...,
        type: Literal["ms-graph"] | None = ...,
        version: Literal["v1.0", "beta"] | None = ...,
        url: str | None = ...,
        user_attr_name: str | None = ...,
        group_attr_name: str | None = ...,
        port: int | None = ...,
        source_ip: str | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        server_identity_check: Literal["disable", "enable"] | None = ...,
        timeout: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: ExternalIdentityProviderPayload | None = ...,
        name: str | None = ...,
        type: Literal["ms-graph"] | None = ...,
        version: Literal["v1.0", "beta"] | None = ...,
        url: str | None = ...,
        user_attr_name: str | None = ...,
        group_attr_name: str | None = ...,
        port: int | None = ...,
        source_ip: str | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        server_identity_check: Literal["disable", "enable"] | None = ...,
        timeout: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def post(
        self,
        payload_dict: ExternalIdentityProviderPayload | None = ...,
        name: str | None = ...,
        type: Literal["ms-graph"] | None = ...,
        version: Literal["v1.0", "beta"] | None = ...,
        url: str | None = ...,
        user_attr_name: str | None = ...,
        group_attr_name: str | None = ...,
        port: int | None = ...,
        source_ip: str | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        server_identity_check: Literal["disable", "enable"] | None = ...,
        timeout: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: ExternalIdentityProviderPayload | None = ...,
        name: str | None = ...,
        type: Literal["ms-graph"] | None = ...,
        version: Literal["v1.0", "beta"] | None = ...,
        url: str | None = ...,
        user_attr_name: str | None = ...,
        group_attr_name: str | None = ...,
        port: int | None = ...,
        source_ip: str | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        server_identity_check: Literal["disable", "enable"] | None = ...,
        timeout: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> ExternalIdentityProviderObject: ...
    
    @overload
    def put(
        self,
        payload_dict: ExternalIdentityProviderPayload | None = ...,
        name: str | None = ...,
        type: Literal["ms-graph"] | None = ...,
        version: Literal["v1.0", "beta"] | None = ...,
        url: str | None = ...,
        user_attr_name: str | None = ...,
        group_attr_name: str | None = ...,
        port: int | None = ...,
        source_ip: str | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        server_identity_check: Literal["disable", "enable"] | None = ...,
        timeout: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: ExternalIdentityProviderPayload | None = ...,
        name: str | None = ...,
        type: Literal["ms-graph"] | None = ...,
        version: Literal["v1.0", "beta"] | None = ...,
        url: str | None = ...,
        user_attr_name: str | None = ...,
        group_attr_name: str | None = ...,
        port: int | None = ...,
        source_ip: str | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        server_identity_check: Literal["disable", "enable"] | None = ...,
        timeout: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def put(
        self,
        payload_dict: ExternalIdentityProviderPayload | None = ...,
        name: str | None = ...,
        type: Literal["ms-graph"] | None = ...,
        version: Literal["v1.0", "beta"] | None = ...,
        url: str | None = ...,
        user_attr_name: str | None = ...,
        group_attr_name: str | None = ...,
        port: int | None = ...,
        source_ip: str | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        server_identity_check: Literal["disable", "enable"] | None = ...,
        timeout: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> ExternalIdentityProviderObject: ...
    
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
        payload_dict: ExternalIdentityProviderPayload | None = ...,
        name: str | None = ...,
        type: Literal["ms-graph"] | None = ...,
        version: Literal["v1.0", "beta"] | None = ...,
        url: str | None = ...,
        user_attr_name: str | None = ...,
        group_attr_name: str | None = ...,
        port: int | None = ...,
        source_ip: str | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        server_identity_check: Literal["disable", "enable"] | None = ...,
        timeout: int | None = ...,
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
    "ExternalIdentityProvider",
    "ExternalIdentityProviderPayload",
    "ExternalIdentityProviderResponse",
    "ExternalIdentityProviderObject",
]