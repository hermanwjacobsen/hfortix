from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject
from hfortix_core.types import MutationResponse, RawAPIResponse

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class SamlPayload(TypedDict, total=False):
    """
    Type hints for user/saml payload fields.
    
    SAML server entry configuration.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.user.scim.ScimEndpoint` (via: scim-client)
        - :class:`~.vpn.certificate.local.LocalEndpoint` (via: cert)
        - :class:`~.vpn.certificate.remote.RemoteEndpoint` (via: idp-cert)

    **Usage:**
        payload: SamlPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # SAML server entry name. | MaxLen: 35
    cert: str  # Certificate to sign SAML messages. | MaxLen: 35
    entity_id: str  # SP entity ID. | MaxLen: 255
    single_sign_on_url: str  # SP single sign-on URL. | MaxLen: 255
    single_logout_url: str  # SP single logout URL. | MaxLen: 255
    idp_entity_id: str  # IDP entity ID. | MaxLen: 255
    idp_single_sign_on_url: str  # IDP single sign-on URL. | MaxLen: 255
    idp_single_logout_url: str  # IDP single logout url. | MaxLen: 255
    idp_cert: str  # IDP Certificate name. | MaxLen: 35
    scim_client: str  # SCIM client name. | MaxLen: 35
    scim_user_attr_type: Literal["user-name", "display-name", "external-id", "email"]  # User attribute type used to match SCIM users | Default: user-name
    scim_group_attr_type: Literal["display-name", "external-id"]  # Group attribute type used to match SCIM groups | Default: display-name
    user_name: str  # User name in assertion statement. | MaxLen: 255
    group_name: str  # Group name in assertion statement. | MaxLen: 255
    digest_method: Literal["sha1", "sha256"]  # Digest method algorithm. | Default: sha1
    require_signed_resp_and_asrt: Literal["enable", "disable"]  # Require both response and assertion from IDP to be | Default: disable
    limit_relaystate: Literal["enable", "disable"]  # Enable/disable limiting of relay-state parameter w | Default: disable
    clock_tolerance: int  # Clock skew tolerance in seconds | Default: 15 | Min: 0 | Max: 300
    adfs_claim: Literal["enable", "disable"]  # Enable/disable ADFS Claim for user/group attribute | Default: disable
    user_claim_type: Literal["email", "given-name", "name", "upn", "common-name", "email-adfs-1x", "group", "upn-adfs-1x", "role", "sur-name", "ppid", "name-identifier", "authentication-method", "deny-only-group-sid", "deny-only-primary-sid", "deny-only-primary-group-sid", "group-sid", "primary-group-sid", "primary-sid", "windows-account-name"]  # User name claim in assertion statement. | Default: upn
    group_claim_type: Literal["email", "given-name", "name", "upn", "common-name", "email-adfs-1x", "group", "upn-adfs-1x", "role", "sur-name", "ppid", "name-identifier", "authentication-method", "deny-only-group-sid", "deny-only-primary-sid", "deny-only-primary-group-sid", "group-sid", "primary-group-sid", "primary-sid", "windows-account-name"]  # Group claim in assertion statement. | Default: group
    reauth: Literal["enable", "disable"]  # Enable/disable signalling of IDP to force user re- | Default: disable

# Nested TypedDicts for table field children (dict mode)

# Nested classes for table field children (object mode)


# Response TypedDict for GET returns (all fields present in API response)
class SamlResponse(TypedDict):
    """
    Type hints for user/saml API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str  # SAML server entry name. | MaxLen: 35
    cert: str  # Certificate to sign SAML messages. | MaxLen: 35
    entity_id: str  # SP entity ID. | MaxLen: 255
    single_sign_on_url: str  # SP single sign-on URL. | MaxLen: 255
    single_logout_url: str  # SP single logout URL. | MaxLen: 255
    idp_entity_id: str  # IDP entity ID. | MaxLen: 255
    idp_single_sign_on_url: str  # IDP single sign-on URL. | MaxLen: 255
    idp_single_logout_url: str  # IDP single logout url. | MaxLen: 255
    idp_cert: str  # IDP Certificate name. | MaxLen: 35
    scim_client: str  # SCIM client name. | MaxLen: 35
    scim_user_attr_type: Literal["user-name", "display-name", "external-id", "email"]  # User attribute type used to match SCIM users | Default: user-name
    scim_group_attr_type: Literal["display-name", "external-id"]  # Group attribute type used to match SCIM groups | Default: display-name
    user_name: str  # User name in assertion statement. | MaxLen: 255
    group_name: str  # Group name in assertion statement. | MaxLen: 255
    digest_method: Literal["sha1", "sha256"]  # Digest method algorithm. | Default: sha1
    require_signed_resp_and_asrt: Literal["enable", "disable"]  # Require both response and assertion from IDP to be | Default: disable
    limit_relaystate: Literal["enable", "disable"]  # Enable/disable limiting of relay-state parameter w | Default: disable
    clock_tolerance: int  # Clock skew tolerance in seconds | Default: 15 | Min: 0 | Max: 300
    adfs_claim: Literal["enable", "disable"]  # Enable/disable ADFS Claim for user/group attribute | Default: disable
    user_claim_type: Literal["email", "given-name", "name", "upn", "common-name", "email-adfs-1x", "group", "upn-adfs-1x", "role", "sur-name", "ppid", "name-identifier", "authentication-method", "deny-only-group-sid", "deny-only-primary-sid", "deny-only-primary-group-sid", "group-sid", "primary-group-sid", "primary-sid", "windows-account-name"]  # User name claim in assertion statement. | Default: upn
    group_claim_type: Literal["email", "given-name", "name", "upn", "common-name", "email-adfs-1x", "group", "upn-adfs-1x", "role", "sur-name", "ppid", "name-identifier", "authentication-method", "deny-only-group-sid", "deny-only-primary-sid", "deny-only-primary-group-sid", "group-sid", "primary-group-sid", "primary-sid", "windows-account-name"]  # Group claim in assertion statement. | Default: group
    reauth: Literal["enable", "disable"]  # Enable/disable signalling of IDP to force user re- | Default: disable


@final
class SamlObject:
    """Typed FortiObject for user/saml with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # SAML server entry name. | MaxLen: 35
    name: str
    # Certificate to sign SAML messages. | MaxLen: 35
    cert: str
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
    # IDP single logout url. | MaxLen: 255
    idp_single_logout_url: str
    # IDP Certificate name. | MaxLen: 35
    idp_cert: str
    # SCIM client name. | MaxLen: 35
    scim_client: str
    # User attribute type used to match SCIM users | Default: user-name
    scim_user_attr_type: Literal["user-name", "display-name", "external-id", "email"]
    # Group attribute type used to match SCIM groups | Default: display-name
    scim_group_attr_type: Literal["display-name", "external-id"]
    # User name in assertion statement. | MaxLen: 255
    user_name: str
    # Group name in assertion statement. | MaxLen: 255
    group_name: str
    # Digest method algorithm. | Default: sha1
    digest_method: Literal["sha1", "sha256"]
    # Require both response and assertion from IDP to be signed wh | Default: disable
    require_signed_resp_and_asrt: Literal["enable", "disable"]
    # Enable/disable limiting of relay-state parameter when it exc | Default: disable
    limit_relaystate: Literal["enable", "disable"]
    # Clock skew tolerance in seconds | Default: 15 | Min: 0 | Max: 300
    clock_tolerance: int
    # Enable/disable ADFS Claim for user/group attribute in assert | Default: disable
    adfs_claim: Literal["enable", "disable"]
    # User name claim in assertion statement. | Default: upn
    user_claim_type: Literal["email", "given-name", "name", "upn", "common-name", "email-adfs-1x", "group", "upn-adfs-1x", "role", "sur-name", "ppid", "name-identifier", "authentication-method", "deny-only-group-sid", "deny-only-primary-sid", "deny-only-primary-group-sid", "group-sid", "primary-group-sid", "primary-sid", "windows-account-name"]
    # Group claim in assertion statement. | Default: group
    group_claim_type: Literal["email", "given-name", "name", "upn", "common-name", "email-adfs-1x", "group", "upn-adfs-1x", "role", "sur-name", "ppid", "name-identifier", "authentication-method", "deny-only-group-sid", "deny-only-primary-sid", "deny-only-primary-group-sid", "group-sid", "primary-group-sid", "primary-sid", "windows-account-name"]
    # Enable/disable signalling of IDP to force user re-authentica | Default: disable
    reauth: Literal["enable", "disable"]
    
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
    SAML server entry configuration.
    
    Path: user/saml
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
    ) -> list[SamlObject]: ...
    
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
        raw_json: Literal[False] = ...,
        **kwargs: Any,
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
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> list[SamlObject]: ...
    
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
        raw_json: Literal[False] = ...,
        **kwargs: Any,
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
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> list[SamlObject]: ...
    
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
    ) -> SamlObject | list[SamlObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: SamlPayload | None = ...,
        name: str | None = ...,
        cert: str | None = ...,
        entity_id: str | None = ...,
        single_sign_on_url: str | None = ...,
        single_logout_url: str | None = ...,
        idp_entity_id: str | None = ...,
        idp_single_sign_on_url: str | None = ...,
        idp_single_logout_url: str | None = ...,
        idp_cert: str | None = ...,
        scim_client: str | None = ...,
        scim_user_attr_type: Literal["user-name", "display-name", "external-id", "email"] | None = ...,
        scim_group_attr_type: Literal["display-name", "external-id"] | None = ...,
        user_name: str | None = ...,
        group_name: str | None = ...,
        digest_method: Literal["sha1", "sha256"] | None = ...,
        require_signed_resp_and_asrt: Literal["enable", "disable"] | None = ...,
        limit_relaystate: Literal["enable", "disable"] | None = ...,
        clock_tolerance: int | None = ...,
        adfs_claim: Literal["enable", "disable"] | None = ...,
        user_claim_type: Literal["email", "given-name", "name", "upn", "common-name", "email-adfs-1x", "group", "upn-adfs-1x", "role", "sur-name", "ppid", "name-identifier", "authentication-method", "deny-only-group-sid", "deny-only-primary-sid", "deny-only-primary-group-sid", "group-sid", "primary-group-sid", "primary-sid", "windows-account-name"] | None = ...,
        group_claim_type: Literal["email", "given-name", "name", "upn", "common-name", "email-adfs-1x", "group", "upn-adfs-1x", "role", "sur-name", "ppid", "name-identifier", "authentication-method", "deny-only-group-sid", "deny-only-primary-sid", "deny-only-primary-group-sid", "group-sid", "primary-group-sid", "primary-sid", "windows-account-name"] | None = ...,
        reauth: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> SamlObject: ...
    
    @overload
    def post(
        self,
        payload_dict: SamlPayload | None = ...,
        name: str | None = ...,
        cert: str | None = ...,
        entity_id: str | None = ...,
        single_sign_on_url: str | None = ...,
        single_logout_url: str | None = ...,
        idp_entity_id: str | None = ...,
        idp_single_sign_on_url: str | None = ...,
        idp_single_logout_url: str | None = ...,
        idp_cert: str | None = ...,
        scim_client: str | None = ...,
        scim_user_attr_type: Literal["user-name", "display-name", "external-id", "email"] | None = ...,
        scim_group_attr_type: Literal["display-name", "external-id"] | None = ...,
        user_name: str | None = ...,
        group_name: str | None = ...,
        digest_method: Literal["sha1", "sha256"] | None = ...,
        require_signed_resp_and_asrt: Literal["enable", "disable"] | None = ...,
        limit_relaystate: Literal["enable", "disable"] | None = ...,
        clock_tolerance: int | None = ...,
        adfs_claim: Literal["enable", "disable"] | None = ...,
        user_claim_type: Literal["email", "given-name", "name", "upn", "common-name", "email-adfs-1x", "group", "upn-adfs-1x", "role", "sur-name", "ppid", "name-identifier", "authentication-method", "deny-only-group-sid", "deny-only-primary-sid", "deny-only-primary-group-sid", "group-sid", "primary-group-sid", "primary-sid", "windows-account-name"] | None = ...,
        group_claim_type: Literal["email", "given-name", "name", "upn", "common-name", "email-adfs-1x", "group", "upn-adfs-1x", "role", "sur-name", "ppid", "name-identifier", "authentication-method", "deny-only-group-sid", "deny-only-primary-sid", "deny-only-primary-group-sid", "group-sid", "primary-group-sid", "primary-sid", "windows-account-name"] | None = ...,
        reauth: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    # raw_json=True returns the full API envelope
    @overload
    def post(
        self,
        payload_dict: SamlPayload | None = ...,
        name: str | None = ...,
        cert: str | None = ...,
        entity_id: str | None = ...,
        single_sign_on_url: str | None = ...,
        single_logout_url: str | None = ...,
        idp_entity_id: str | None = ...,
        idp_single_sign_on_url: str | None = ...,
        idp_single_logout_url: str | None = ...,
        idp_cert: str | None = ...,
        scim_client: str | None = ...,
        scim_user_attr_type: Literal["user-name", "display-name", "external-id", "email"] | None = ...,
        scim_group_attr_type: Literal["display-name", "external-id"] | None = ...,
        user_name: str | None = ...,
        group_name: str | None = ...,
        digest_method: Literal["sha1", "sha256"] | None = ...,
        require_signed_resp_and_asrt: Literal["enable", "disable"] | None = ...,
        limit_relaystate: Literal["enable", "disable"] | None = ...,
        clock_tolerance: int | None = ...,
        adfs_claim: Literal["enable", "disable"] | None = ...,
        user_claim_type: Literal["email", "given-name", "name", "upn", "common-name", "email-adfs-1x", "group", "upn-adfs-1x", "role", "sur-name", "ppid", "name-identifier", "authentication-method", "deny-only-group-sid", "deny-only-primary-sid", "deny-only-primary-group-sid", "group-sid", "primary-group-sid", "primary-sid", "windows-account-name"] | None = ...,
        group_claim_type: Literal["email", "given-name", "name", "upn", "common-name", "email-adfs-1x", "group", "upn-adfs-1x", "role", "sur-name", "ppid", "name-identifier", "authentication-method", "deny-only-group-sid", "deny-only-primary-sid", "deny-only-primary-group-sid", "group-sid", "primary-group-sid", "primary-sid", "windows-account-name"] | None = ...,
        reauth: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> RawAPIResponse: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: SamlPayload | None = ...,
        name: str | None = ...,
        cert: str | None = ...,
        entity_id: str | None = ...,
        single_sign_on_url: str | None = ...,
        single_logout_url: str | None = ...,
        idp_entity_id: str | None = ...,
        idp_single_sign_on_url: str | None = ...,
        idp_single_logout_url: str | None = ...,
        idp_cert: str | None = ...,
        scim_client: str | None = ...,
        scim_user_attr_type: Literal["user-name", "display-name", "external-id", "email"] | None = ...,
        scim_group_attr_type: Literal["display-name", "external-id"] | None = ...,
        user_name: str | None = ...,
        group_name: str | None = ...,
        digest_method: Literal["sha1", "sha256"] | None = ...,
        require_signed_resp_and_asrt: Literal["enable", "disable"] | None = ...,
        limit_relaystate: Literal["enable", "disable"] | None = ...,
        clock_tolerance: int | None = ...,
        adfs_claim: Literal["enable", "disable"] | None = ...,
        user_claim_type: Literal["email", "given-name", "name", "upn", "common-name", "email-adfs-1x", "group", "upn-adfs-1x", "role", "sur-name", "ppid", "name-identifier", "authentication-method", "deny-only-group-sid", "deny-only-primary-sid", "deny-only-primary-group-sid", "group-sid", "primary-group-sid", "primary-sid", "windows-account-name"] | None = ...,
        group_claim_type: Literal["email", "given-name", "name", "upn", "common-name", "email-adfs-1x", "group", "upn-adfs-1x", "role", "sur-name", "ppid", "name-identifier", "authentication-method", "deny-only-group-sid", "deny-only-primary-sid", "deny-only-primary-group-sid", "group-sid", "primary-group-sid", "primary-sid", "windows-account-name"] | None = ...,
        reauth: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    def post(
        self,
        payload_dict: SamlPayload | None = ...,
        name: str | None = ...,
        cert: str | None = ...,
        entity_id: str | None = ...,
        single_sign_on_url: str | None = ...,
        single_logout_url: str | None = ...,
        idp_entity_id: str | None = ...,
        idp_single_sign_on_url: str | None = ...,
        idp_single_logout_url: str | None = ...,
        idp_cert: str | None = ...,
        scim_client: str | None = ...,
        scim_user_attr_type: Literal["user-name", "display-name", "external-id", "email"] | None = ...,
        scim_group_attr_type: Literal["display-name", "external-id"] | None = ...,
        user_name: str | None = ...,
        group_name: str | None = ...,
        digest_method: Literal["sha1", "sha256"] | None = ...,
        require_signed_resp_and_asrt: Literal["enable", "disable"] | None = ...,
        limit_relaystate: Literal["enable", "disable"] | None = ...,
        clock_tolerance: int | None = ...,
        adfs_claim: Literal["enable", "disable"] | None = ...,
        user_claim_type: Literal["email", "given-name", "name", "upn", "common-name", "email-adfs-1x", "group", "upn-adfs-1x", "role", "sur-name", "ppid", "name-identifier", "authentication-method", "deny-only-group-sid", "deny-only-primary-sid", "deny-only-primary-group-sid", "group-sid", "primary-group-sid", "primary-sid", "windows-account-name"] | None = ...,
        group_claim_type: Literal["email", "given-name", "name", "upn", "common-name", "email-adfs-1x", "group", "upn-adfs-1x", "role", "sur-name", "ppid", "name-identifier", "authentication-method", "deny-only-group-sid", "deny-only-primary-sid", "deny-only-primary-group-sid", "group-sid", "primary-group-sid", "primary-sid", "windows-account-name"] | None = ...,
        reauth: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: SamlPayload | None = ...,
        name: str | None = ...,
        cert: str | None = ...,
        entity_id: str | None = ...,
        single_sign_on_url: str | None = ...,
        single_logout_url: str | None = ...,
        idp_entity_id: str | None = ...,
        idp_single_sign_on_url: str | None = ...,
        idp_single_logout_url: str | None = ...,
        idp_cert: str | None = ...,
        scim_client: str | None = ...,
        scim_user_attr_type: Literal["user-name", "display-name", "external-id", "email"] | None = ...,
        scim_group_attr_type: Literal["display-name", "external-id"] | None = ...,
        user_name: str | None = ...,
        group_name: str | None = ...,
        digest_method: Literal["sha1", "sha256"] | None = ...,
        require_signed_resp_and_asrt: Literal["enable", "disable"] | None = ...,
        limit_relaystate: Literal["enable", "disable"] | None = ...,
        clock_tolerance: int | None = ...,
        adfs_claim: Literal["enable", "disable"] | None = ...,
        user_claim_type: Literal["email", "given-name", "name", "upn", "common-name", "email-adfs-1x", "group", "upn-adfs-1x", "role", "sur-name", "ppid", "name-identifier", "authentication-method", "deny-only-group-sid", "deny-only-primary-sid", "deny-only-primary-group-sid", "group-sid", "primary-group-sid", "primary-sid", "windows-account-name"] | None = ...,
        group_claim_type: Literal["email", "given-name", "name", "upn", "common-name", "email-adfs-1x", "group", "upn-adfs-1x", "role", "sur-name", "ppid", "name-identifier", "authentication-method", "deny-only-group-sid", "deny-only-primary-sid", "deny-only-primary-group-sid", "group-sid", "primary-group-sid", "primary-sid", "windows-account-name"] | None = ...,
        reauth: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> SamlObject: ...
    
    @overload
    def put(
        self,
        payload_dict: SamlPayload | None = ...,
        name: str | None = ...,
        cert: str | None = ...,
        entity_id: str | None = ...,
        single_sign_on_url: str | None = ...,
        single_logout_url: str | None = ...,
        idp_entity_id: str | None = ...,
        idp_single_sign_on_url: str | None = ...,
        idp_single_logout_url: str | None = ...,
        idp_cert: str | None = ...,
        scim_client: str | None = ...,
        scim_user_attr_type: Literal["user-name", "display-name", "external-id", "email"] | None = ...,
        scim_group_attr_type: Literal["display-name", "external-id"] | None = ...,
        user_name: str | None = ...,
        group_name: str | None = ...,
        digest_method: Literal["sha1", "sha256"] | None = ...,
        require_signed_resp_and_asrt: Literal["enable", "disable"] | None = ...,
        limit_relaystate: Literal["enable", "disable"] | None = ...,
        clock_tolerance: int | None = ...,
        adfs_claim: Literal["enable", "disable"] | None = ...,
        user_claim_type: Literal["email", "given-name", "name", "upn", "common-name", "email-adfs-1x", "group", "upn-adfs-1x", "role", "sur-name", "ppid", "name-identifier", "authentication-method", "deny-only-group-sid", "deny-only-primary-sid", "deny-only-primary-group-sid", "group-sid", "primary-group-sid", "primary-sid", "windows-account-name"] | None = ...,
        group_claim_type: Literal["email", "given-name", "name", "upn", "common-name", "email-adfs-1x", "group", "upn-adfs-1x", "role", "sur-name", "ppid", "name-identifier", "authentication-method", "deny-only-group-sid", "deny-only-primary-sid", "deny-only-primary-group-sid", "group-sid", "primary-group-sid", "primary-sid", "windows-account-name"] | None = ...,
        reauth: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    # raw_json=True returns the full API envelope
    @overload
    def put(
        self,
        payload_dict: SamlPayload | None = ...,
        name: str | None = ...,
        cert: str | None = ...,
        entity_id: str | None = ...,
        single_sign_on_url: str | None = ...,
        single_logout_url: str | None = ...,
        idp_entity_id: str | None = ...,
        idp_single_sign_on_url: str | None = ...,
        idp_single_logout_url: str | None = ...,
        idp_cert: str | None = ...,
        scim_client: str | None = ...,
        scim_user_attr_type: Literal["user-name", "display-name", "external-id", "email"] | None = ...,
        scim_group_attr_type: Literal["display-name", "external-id"] | None = ...,
        user_name: str | None = ...,
        group_name: str | None = ...,
        digest_method: Literal["sha1", "sha256"] | None = ...,
        require_signed_resp_and_asrt: Literal["enable", "disable"] | None = ...,
        limit_relaystate: Literal["enable", "disable"] | None = ...,
        clock_tolerance: int | None = ...,
        adfs_claim: Literal["enable", "disable"] | None = ...,
        user_claim_type: Literal["email", "given-name", "name", "upn", "common-name", "email-adfs-1x", "group", "upn-adfs-1x", "role", "sur-name", "ppid", "name-identifier", "authentication-method", "deny-only-group-sid", "deny-only-primary-sid", "deny-only-primary-group-sid", "group-sid", "primary-group-sid", "primary-sid", "windows-account-name"] | None = ...,
        group_claim_type: Literal["email", "given-name", "name", "upn", "common-name", "email-adfs-1x", "group", "upn-adfs-1x", "role", "sur-name", "ppid", "name-identifier", "authentication-method", "deny-only-group-sid", "deny-only-primary-sid", "deny-only-primary-group-sid", "group-sid", "primary-group-sid", "primary-sid", "windows-account-name"] | None = ...,
        reauth: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> RawAPIResponse: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: SamlPayload | None = ...,
        name: str | None = ...,
        cert: str | None = ...,
        entity_id: str | None = ...,
        single_sign_on_url: str | None = ...,
        single_logout_url: str | None = ...,
        idp_entity_id: str | None = ...,
        idp_single_sign_on_url: str | None = ...,
        idp_single_logout_url: str | None = ...,
        idp_cert: str | None = ...,
        scim_client: str | None = ...,
        scim_user_attr_type: Literal["user-name", "display-name", "external-id", "email"] | None = ...,
        scim_group_attr_type: Literal["display-name", "external-id"] | None = ...,
        user_name: str | None = ...,
        group_name: str | None = ...,
        digest_method: Literal["sha1", "sha256"] | None = ...,
        require_signed_resp_and_asrt: Literal["enable", "disable"] | None = ...,
        limit_relaystate: Literal["enable", "disable"] | None = ...,
        clock_tolerance: int | None = ...,
        adfs_claim: Literal["enable", "disable"] | None = ...,
        user_claim_type: Literal["email", "given-name", "name", "upn", "common-name", "email-adfs-1x", "group", "upn-adfs-1x", "role", "sur-name", "ppid", "name-identifier", "authentication-method", "deny-only-group-sid", "deny-only-primary-sid", "deny-only-primary-group-sid", "group-sid", "primary-group-sid", "primary-sid", "windows-account-name"] | None = ...,
        group_claim_type: Literal["email", "given-name", "name", "upn", "common-name", "email-adfs-1x", "group", "upn-adfs-1x", "role", "sur-name", "ppid", "name-identifier", "authentication-method", "deny-only-group-sid", "deny-only-primary-sid", "deny-only-primary-group-sid", "group-sid", "primary-group-sid", "primary-sid", "windows-account-name"] | None = ...,
        reauth: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    def put(
        self,
        payload_dict: SamlPayload | None = ...,
        name: str | None = ...,
        cert: str | None = ...,
        entity_id: str | None = ...,
        single_sign_on_url: str | None = ...,
        single_logout_url: str | None = ...,
        idp_entity_id: str | None = ...,
        idp_single_sign_on_url: str | None = ...,
        idp_single_logout_url: str | None = ...,
        idp_cert: str | None = ...,
        scim_client: str | None = ...,
        scim_user_attr_type: Literal["user-name", "display-name", "external-id", "email"] | None = ...,
        scim_group_attr_type: Literal["display-name", "external-id"] | None = ...,
        user_name: str | None = ...,
        group_name: str | None = ...,
        digest_method: Literal["sha1", "sha256"] | None = ...,
        require_signed_resp_and_asrt: Literal["enable", "disable"] | None = ...,
        limit_relaystate: Literal["enable", "disable"] | None = ...,
        clock_tolerance: int | None = ...,
        adfs_claim: Literal["enable", "disable"] | None = ...,
        user_claim_type: Literal["email", "given-name", "name", "upn", "common-name", "email-adfs-1x", "group", "upn-adfs-1x", "role", "sur-name", "ppid", "name-identifier", "authentication-method", "deny-only-group-sid", "deny-only-primary-sid", "deny-only-primary-group-sid", "group-sid", "primary-group-sid", "primary-sid", "windows-account-name"] | None = ...,
        group_claim_type: Literal["email", "given-name", "name", "upn", "common-name", "email-adfs-1x", "group", "upn-adfs-1x", "role", "sur-name", "ppid", "name-identifier", "authentication-method", "deny-only-group-sid", "deny-only-primary-sid", "deny-only-primary-group-sid", "group-sid", "primary-group-sid", "primary-sid", "windows-account-name"] | None = ...,
        reauth: Literal["enable", "disable"] | None = ...,
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
    ) -> SamlObject: ...
    
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
        payload_dict: SamlPayload | None = ...,
        name: str | None = ...,
        cert: str | None = ...,
        entity_id: str | None = ...,
        single_sign_on_url: str | None = ...,
        single_logout_url: str | None = ...,
        idp_entity_id: str | None = ...,
        idp_single_sign_on_url: str | None = ...,
        idp_single_logout_url: str | None = ...,
        idp_cert: str | None = ...,
        scim_client: str | None = ...,
        scim_user_attr_type: Literal["user-name", "display-name", "external-id", "email"] | None = ...,
        scim_group_attr_type: Literal["display-name", "external-id"] | None = ...,
        user_name: str | None = ...,
        group_name: str | None = ...,
        digest_method: Literal["sha1", "sha256"] | None = ...,
        require_signed_resp_and_asrt: Literal["enable", "disable"] | None = ...,
        limit_relaystate: Literal["enable", "disable"] | None = ...,
        clock_tolerance: int | None = ...,
        adfs_claim: Literal["enable", "disable"] | None = ...,
        user_claim_type: Literal["email", "given-name", "name", "upn", "common-name", "email-adfs-1x", "group", "upn-adfs-1x", "role", "sur-name", "ppid", "name-identifier", "authentication-method", "deny-only-group-sid", "deny-only-primary-sid", "deny-only-primary-group-sid", "group-sid", "primary-group-sid", "primary-sid", "windows-account-name"] | None = ...,
        group_claim_type: Literal["email", "given-name", "name", "upn", "common-name", "email-adfs-1x", "group", "upn-adfs-1x", "role", "sur-name", "ppid", "name-identifier", "authentication-method", "deny-only-group-sid", "deny-only-primary-sid", "deny-only-primary-group-sid", "group-sid", "primary-group-sid", "primary-sid", "windows-account-name"] | None = ...,
        reauth: Literal["enable", "disable"] | None = ...,
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
    "Saml",
    "SamlPayload",
    "SamlResponse",
    "SamlObject",
]