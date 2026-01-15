from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class SamlPayload(TypedDict, total=False):
    """
    Type hints for system/saml payload fields.
    
    Global settings for SAML authentication.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.certificate.local.LocalEndpoint` (via: cert)
        - :class:`~.certificate.remote.RemoteEndpoint` (via: idp-cert)
        - :class:`~.system.accprofile.AccprofileEndpoint` (via: default-profile)

    **Usage:**
        payload: SamlPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    status: Literal["enable", "disable"]  # Enable/disable SAML authentication | Default: disable
    role: Literal["identity-provider", "service-provider"]  # SAML role. | Default: service-provider
    default_login_page: Literal["normal", "sso"]  # Choose default login page. | Default: normal
    default_profile: str  # Default profile for new SSO admin. | MaxLen: 35
    cert: str  # Certificate to sign SAML messages. | MaxLen: 35
    binding_protocol: Literal["post", "redirect"]  # IdP Binding protocol. | Default: redirect
    portal_url: str  # SP portal URL. | MaxLen: 255
    entity_id: str  # SP entity ID. | MaxLen: 255
    single_sign_on_url: str  # SP single sign-on URL. | MaxLen: 255
    single_logout_url: str  # SP single logout URL. | MaxLen: 255
    idp_entity_id: str  # IDP entity ID. | MaxLen: 255
    idp_single_sign_on_url: str  # IDP single sign-on URL. | MaxLen: 255
    idp_single_logout_url: str  # IDP single logout URL. | MaxLen: 255
    idp_cert: str  # IDP certificate name. | MaxLen: 35
    server_address: str  # Server address. | MaxLen: 63
    require_signed_resp_and_asrt: Literal["enable", "disable"]  # Require both response and assertion from IDP to be | Default: disable
    tolerance: int  # Tolerance to the range of time when the assertion | Default: 5 | Min: 0 | Max: 4294967295
    life: int  # Length of the range of time when the assertion is | Default: 30 | Min: 0 | Max: 4294967295
    service_providers: list[dict[str, Any]]  # Authorized service providers.

# Nested TypedDicts for table field children (dict mode)

class SamlServiceprovidersItem(TypedDict):
    """Type hints for service-providers table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # Name. | MaxLen: 35
    prefix: str  # Prefix. | MaxLen: 35
    sp_binding_protocol: Literal["post", "redirect"]  # SP binding protocol. | Default: post
    sp_cert: str  # SP certificate name. | MaxLen: 35
    sp_entity_id: str  # SP entity ID. | MaxLen: 255
    sp_single_sign_on_url: str  # SP single sign-on URL. | MaxLen: 255
    sp_single_logout_url: str  # SP single logout URL. | MaxLen: 255
    sp_portal_url: str  # SP portal URL. | MaxLen: 255
    idp_entity_id: str  # IDP entity ID. | MaxLen: 255
    idp_single_sign_on_url: str  # IDP single sign-on URL. | MaxLen: 255
    idp_single_logout_url: str  # IDP single logout URL. | MaxLen: 255
    assertion_attributes: str  # Customized SAML attributes to send along with asse


# Nested classes for table field children (object mode)

@final
class SamlServiceprovidersObject:
    """Typed object for service-providers table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Name. | MaxLen: 35
    name: str
    # Prefix. | MaxLen: 35
    prefix: str
    # SP binding protocol. | Default: post
    sp_binding_protocol: Literal["post", "redirect"]
    # SP certificate name. | MaxLen: 35
    sp_cert: str
    # SP entity ID. | MaxLen: 255
    sp_entity_id: str
    # SP single sign-on URL. | MaxLen: 255
    sp_single_sign_on_url: str
    # SP single logout URL. | MaxLen: 255
    sp_single_logout_url: str
    # SP portal URL. | MaxLen: 255
    sp_portal_url: str
    # IDP entity ID. | MaxLen: 255
    idp_entity_id: str
    # IDP single sign-on URL. | MaxLen: 255
    idp_single_sign_on_url: str
    # IDP single logout URL. | MaxLen: 255
    idp_single_logout_url: str
    # Customized SAML attributes to send along with assertion.
    assertion_attributes: str
    
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
class SamlResponse(TypedDict):
    """
    Type hints for system/saml API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    status: Literal["enable", "disable"]  # Enable/disable SAML authentication | Default: disable
    role: Literal["identity-provider", "service-provider"]  # SAML role. | Default: service-provider
    default_login_page: Literal["normal", "sso"]  # Choose default login page. | Default: normal
    default_profile: str  # Default profile for new SSO admin. | MaxLen: 35
    cert: str  # Certificate to sign SAML messages. | MaxLen: 35
    binding_protocol: Literal["post", "redirect"]  # IdP Binding protocol. | Default: redirect
    portal_url: str  # SP portal URL. | MaxLen: 255
    entity_id: str  # SP entity ID. | MaxLen: 255
    single_sign_on_url: str  # SP single sign-on URL. | MaxLen: 255
    single_logout_url: str  # SP single logout URL. | MaxLen: 255
    idp_entity_id: str  # IDP entity ID. | MaxLen: 255
    idp_single_sign_on_url: str  # IDP single sign-on URL. | MaxLen: 255
    idp_single_logout_url: str  # IDP single logout URL. | MaxLen: 255
    idp_cert: str  # IDP certificate name. | MaxLen: 35
    server_address: str  # Server address. | MaxLen: 63
    require_signed_resp_and_asrt: Literal["enable", "disable"]  # Require both response and assertion from IDP to be | Default: disable
    tolerance: int  # Tolerance to the range of time when the assertion | Default: 5 | Min: 0 | Max: 4294967295
    life: int  # Length of the range of time when the assertion is | Default: 30 | Min: 0 | Max: 4294967295
    service_providers: list[SamlServiceprovidersItem]  # Authorized service providers.


@final
class SamlObject:
    """Typed FortiObject for system/saml with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Enable/disable SAML authentication (default = disable). | Default: disable
    status: Literal["enable", "disable"]
    # SAML role. | Default: service-provider
    role: Literal["identity-provider", "service-provider"]
    # Choose default login page. | Default: normal
    default_login_page: Literal["normal", "sso"]
    # Default profile for new SSO admin. | MaxLen: 35
    default_profile: str
    # Certificate to sign SAML messages. | MaxLen: 35
    cert: str
    # IdP Binding protocol. | Default: redirect
    binding_protocol: Literal["post", "redirect"]
    # SP portal URL. | MaxLen: 255
    portal_url: str
    # SP entity ID. | MaxLen: 255
    entity_id: str
    # SP single sign-on URL. | MaxLen: 255
    single_sign_on_url: str
    # SP single logout URL. | MaxLen: 255
    single_logout_url: str
    # IDP entity ID. | MaxLen: 255
    idp_entity_id: str
    # IDP single sign-on URL. | MaxLen: 255
    idp_single_sign_on_url: str
    # IDP single logout URL. | MaxLen: 255
    idp_single_logout_url: str
    # IDP certificate name. | MaxLen: 35
    idp_cert: str
    # Server address. | MaxLen: 63
    server_address: str
    # Require both response and assertion from IDP to be signed wh | Default: disable
    require_signed_resp_and_asrt: Literal["enable", "disable"]
    # Tolerance to the range of time when the assertion is valid | Default: 5 | Min: 0 | Max: 4294967295
    tolerance: int
    # Length of the range of time when the assertion is valid | Default: 30 | Min: 0 | Max: 4294967295
    life: int
    # Authorized service providers.
    service_providers: list[SamlServiceprovidersObject]
    
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
    def to_dict(self) -> SamlPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Saml:
    """
    Global settings for SAML authentication.
    
    Path: system/saml
    Category: cmdb
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
    ) -> SamlObject: ...
    
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
    ) -> SamlObject: ...
    
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
    ) -> SamlObject: ...
    
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
    ) -> SamlObject: ...
    
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
    ) -> SamlObject: ...
    
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
    ) -> SamlObject: ...
    
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
    ) -> SamlObject: ...
    
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
    ) -> SamlObject: ...
    
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
    ) -> SamlObject: ...
    
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
    ) -> dict[str, Any] | FortiObject: ...
    
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
    ) -> SamlObject | dict[str, Any]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: SamlPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        role: Literal["identity-provider", "service-provider"] | None = ...,
        default_login_page: Literal["normal", "sso"] | None = ...,
        default_profile: str | None = ...,
        cert: str | None = ...,
        binding_protocol: Literal["post", "redirect"] | None = ...,
        portal_url: str | None = ...,
        entity_id: str | None = ...,
        single_sign_on_url: str | None = ...,
        single_logout_url: str | None = ...,
        idp_entity_id: str | None = ...,
        idp_single_sign_on_url: str | None = ...,
        idp_single_logout_url: str | None = ...,
        idp_cert: str | None = ...,
        server_address: str | None = ...,
        require_signed_resp_and_asrt: Literal["enable", "disable"] | None = ...,
        tolerance: int | None = ...,
        life: int | None = ...,
        service_providers: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> SamlObject: ...
    
    @overload
    def put(
        self,
        payload_dict: SamlPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        role: Literal["identity-provider", "service-provider"] | None = ...,
        default_login_page: Literal["normal", "sso"] | None = ...,
        default_profile: str | None = ...,
        cert: str | None = ...,
        binding_protocol: Literal["post", "redirect"] | None = ...,
        portal_url: str | None = ...,
        entity_id: str | None = ...,
        single_sign_on_url: str | None = ...,
        single_logout_url: str | None = ...,
        idp_entity_id: str | None = ...,
        idp_single_sign_on_url: str | None = ...,
        idp_single_logout_url: str | None = ...,
        idp_cert: str | None = ...,
        server_address: str | None = ...,
        require_signed_resp_and_asrt: Literal["enable", "disable"] | None = ...,
        tolerance: int | None = ...,
        life: int | None = ...,
        service_providers: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: SamlPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        role: Literal["identity-provider", "service-provider"] | None = ...,
        default_login_page: Literal["normal", "sso"] | None = ...,
        default_profile: str | None = ...,
        cert: str | None = ...,
        binding_protocol: Literal["post", "redirect"] | None = ...,
        portal_url: str | None = ...,
        entity_id: str | None = ...,
        single_sign_on_url: str | None = ...,
        single_logout_url: str | None = ...,
        idp_entity_id: str | None = ...,
        idp_single_sign_on_url: str | None = ...,
        idp_single_logout_url: str | None = ...,
        idp_cert: str | None = ...,
        server_address: str | None = ...,
        require_signed_resp_and_asrt: Literal["enable", "disable"] | None = ...,
        tolerance: int | None = ...,
        life: int | None = ...,
        service_providers: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def put(
        self,
        payload_dict: SamlPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        role: Literal["identity-provider", "service-provider"] | None = ...,
        default_login_page: Literal["normal", "sso"] | None = ...,
        default_profile: str | None = ...,
        cert: str | None = ...,
        binding_protocol: Literal["post", "redirect"] | None = ...,
        portal_url: str | None = ...,
        entity_id: str | None = ...,
        single_sign_on_url: str | None = ...,
        single_logout_url: str | None = ...,
        idp_entity_id: str | None = ...,
        idp_single_sign_on_url: str | None = ...,
        idp_single_logout_url: str | None = ...,
        idp_cert: str | None = ...,
        server_address: str | None = ...,
        require_signed_resp_and_asrt: Literal["enable", "disable"] | None = ...,
        tolerance: int | None = ...,
        life: int | None = ...,
        service_providers: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: SamlPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        role: Literal["identity-provider", "service-provider"] | None = ...,
        default_login_page: Literal["normal", "sso"] | None = ...,
        default_profile: str | None = ...,
        cert: str | None = ...,
        binding_protocol: Literal["post", "redirect"] | None = ...,
        portal_url: str | None = ...,
        entity_id: str | None = ...,
        single_sign_on_url: str | None = ...,
        single_logout_url: str | None = ...,
        idp_entity_id: str | None = ...,
        idp_single_sign_on_url: str | None = ...,
        idp_single_logout_url: str | None = ...,
        idp_cert: str | None = ...,
        server_address: str | None = ...,
        require_signed_resp_and_asrt: Literal["enable", "disable"] | None = ...,
        tolerance: int | None = ...,
        life: int | None = ...,
        service_providers: str | list[str] | list[dict[str, Any]] | None = ...,
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
    "Saml",
    "SamlPayload",
    "SamlResponse",
    "SamlObject",
]