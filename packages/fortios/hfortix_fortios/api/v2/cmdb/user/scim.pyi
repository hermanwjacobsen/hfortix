from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList
from hfortix_core.types import MutationResponse

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class ScimPayload(TypedDict, total=False):
    """
    Type hints for user/scim payload fields.
    
    Configure SCIM client entries.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.certificate.ca.CaEndpoint` (via: certificate)
        - :class:`~.certificate.remote.RemoteEndpoint` (via: certificate)
        - :class:`~.vpn.certificate.ca.CaEndpoint` (via: certificate)
        - :class:`~.vpn.certificate.local.LocalEndpoint` (via: token-certificate)
        - :class:`~.vpn.certificate.remote.RemoteEndpoint` (via: certificate, token-certificate)

    **Usage:**
        payload: ScimPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # SCIM client name. | MaxLen: 35
    id: int  # SCIM client ID. | Default: 0 | Min: 0 | Max: 4294967295
    status: Literal["enable", "disable"]  # Enable/disable System for Cross-domain Identity Ma | Default: disable
    base_url: str  # Server URL to receive SCIM create, read, update, d | MaxLen: 127
    auth_method: Literal["token", "base"]  # TLS client authentication methods | Default: token
    token_certificate: str  # Certificate for token verification. | MaxLen: 79
    secret: str  # Secret for token verification or base authenticati | MaxLen: 128
    certificate: str  # Certificate for client verification during TLS han | MaxLen: 79
    client_identity_check: Literal["enable", "disable"]  # Enable/disable client identity check. | Default: enable
    cascade: Literal["disable", "enable"]  # Enable/disable to follow SCIM users/groups changes | Default: disable

# Nested TypedDicts for table field children (dict mode)

# Nested classes for table field children (object mode)


# Response TypedDict for GET returns (all fields present in API response)
class ScimResponse(TypedDict):
    """
    Type hints for user/scim API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str  # SCIM client name. | MaxLen: 35
    id: int  # SCIM client ID. | Default: 0 | Min: 0 | Max: 4294967295
    status: Literal["enable", "disable"]  # Enable/disable System for Cross-domain Identity Ma | Default: disable
    base_url: str  # Server URL to receive SCIM create, read, update, d | MaxLen: 127
    auth_method: Literal["token", "base"]  # TLS client authentication methods | Default: token
    token_certificate: str  # Certificate for token verification. | MaxLen: 79
    secret: str  # Secret for token verification or base authenticati | MaxLen: 128
    certificate: str  # Certificate for client verification during TLS han | MaxLen: 79
    client_identity_check: Literal["enable", "disable"]  # Enable/disable client identity check. | Default: enable
    cascade: Literal["disable", "enable"]  # Enable/disable to follow SCIM users/groups changes | Default: disable


@final
class ScimObject:
    """Typed FortiObject for user/scim with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # SCIM client name. | MaxLen: 35
    name: str
    # SCIM client ID. | Default: 0 | Min: 0 | Max: 4294967295
    id: int
    # Enable/disable System for Cross-domain Identity Management | Default: disable
    status: Literal["enable", "disable"]
    # Server URL to receive SCIM create, read, update, delete | MaxLen: 127
    base_url: str
    # TLS client authentication methods (default = bearer token). | Default: token
    auth_method: Literal["token", "base"]
    # Certificate for token verification. | MaxLen: 79
    token_certificate: str
    # Secret for token verification or base authentication. | MaxLen: 128
    secret: str
    # Certificate for client verification during TLS handshake. | MaxLen: 79
    certificate: str
    # Enable/disable client identity check. | Default: enable
    client_identity_check: Literal["enable", "disable"]
    # Enable/disable to follow SCIM users/groups changes in IDP. | Default: disable
    cascade: Literal["disable", "enable"]
    
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
    def to_dict(self) -> ScimPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Scim:
    """
    Configure SCIM client entries.
    
    Path: user/scim
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
    ) -> ScimObject: ...
    
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
    ) -> ScimObject: ...
    
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
    ) -> FortiObjectList[ScimObject]: ...
    
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
    ) -> ScimObject: ...
    
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
    ) -> ScimObject: ...
    
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
    ) -> FortiObjectList[ScimObject]: ...
    
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
    ) -> ScimObject: ...
    
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
    ) -> ScimObject: ...
    
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
    ) -> FortiObjectList[ScimObject]: ...
    
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
    ) -> ScimObject | list[ScimObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: ScimPayload | None = ...,
        name: str | None = ...,
        id: int | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        base_url: str | None = ...,
        auth_method: Literal["token", "base"] | None = ...,
        token_certificate: str | None = ...,
        secret: str | None = ...,
        certificate: str | None = ...,
        client_identity_check: Literal["enable", "disable"] | None = ...,
        cascade: Literal["disable", "enable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> ScimObject: ...
    
    @overload
    def post(
        self,
        payload_dict: ScimPayload | None = ...,
        name: str | None = ...,
        id: int | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        base_url: str | None = ...,
        auth_method: Literal["token", "base"] | None = ...,
        token_certificate: str | None = ...,
        secret: str | None = ...,
        certificate: str | None = ...,
        client_identity_check: Literal["enable", "disable"] | None = ...,
        cascade: Literal["disable", "enable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: ScimPayload | None = ...,
        name: str | None = ...,
        id: int | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        base_url: str | None = ...,
        auth_method: Literal["token", "base"] | None = ...,
        token_certificate: str | None = ...,
        secret: str | None = ...,
        certificate: str | None = ...,
        client_identity_check: Literal["enable", "disable"] | None = ...,
        cascade: Literal["disable", "enable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def post(
        self,
        payload_dict: ScimPayload | None = ...,
        name: str | None = ...,
        id: int | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        base_url: str | None = ...,
        auth_method: Literal["token", "base"] | None = ...,
        token_certificate: str | None = ...,
        secret: str | None = ...,
        certificate: str | None = ...,
        client_identity_check: Literal["enable", "disable"] | None = ...,
        cascade: Literal["disable", "enable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: ScimPayload | None = ...,
        name: str | None = ...,
        id: int | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        base_url: str | None = ...,
        auth_method: Literal["token", "base"] | None = ...,
        token_certificate: str | None = ...,
        secret: str | None = ...,
        certificate: str | None = ...,
        client_identity_check: Literal["enable", "disable"] | None = ...,
        cascade: Literal["disable", "enable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> ScimObject: ...
    
    @overload
    def put(
        self,
        payload_dict: ScimPayload | None = ...,
        name: str | None = ...,
        id: int | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        base_url: str | None = ...,
        auth_method: Literal["token", "base"] | None = ...,
        token_certificate: str | None = ...,
        secret: str | None = ...,
        certificate: str | None = ...,
        client_identity_check: Literal["enable", "disable"] | None = ...,
        cascade: Literal["disable", "enable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: ScimPayload | None = ...,
        name: str | None = ...,
        id: int | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        base_url: str | None = ...,
        auth_method: Literal["token", "base"] | None = ...,
        token_certificate: str | None = ...,
        secret: str | None = ...,
        certificate: str | None = ...,
        client_identity_check: Literal["enable", "disable"] | None = ...,
        cascade: Literal["disable", "enable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def put(
        self,
        payload_dict: ScimPayload | None = ...,
        name: str | None = ...,
        id: int | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        base_url: str | None = ...,
        auth_method: Literal["token", "base"] | None = ...,
        token_certificate: str | None = ...,
        secret: str | None = ...,
        certificate: str | None = ...,
        client_identity_check: Literal["enable", "disable"] | None = ...,
        cascade: Literal["disable", "enable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> ScimObject: ...
    
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
        payload_dict: ScimPayload | None = ...,
        name: str | None = ...,
        id: int | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        base_url: str | None = ...,
        auth_method: Literal["token", "base"] | None = ...,
        token_certificate: str | None = ...,
        secret: str | None = ...,
        certificate: str | None = ...,
        client_identity_check: Literal["enable", "disable"] | None = ...,
        cascade: Literal["disable", "enable"] | None = ...,
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
    "Scim",
    "ScimPayload",
    "ScimResponse",
    "ScimObject",
]