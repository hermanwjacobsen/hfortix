from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject
from hfortix_core.types import MutationResponse, RawAPIResponse

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class LocalPayload(TypedDict, total=False):
    """
    Type hints for user/local payload fields.
    
    Configure local users.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.system.sms-server.SmsServerEndpoint` (via: sms-custom-server)
        - :class:`~.user.fortitoken.FortitokenEndpoint` (via: fortitoken)
        - :class:`~.user.ldap.LdapEndpoint` (via: ldap-server)
        - :class:`~.user.password-policy.PasswordPolicyEndpoint` (via: passwd-policy)
        - :class:`~.user.radius.RadiusEndpoint` (via: radius-server)
        - :class:`~.user.saml.SamlEndpoint` (via: saml-server)
        - :class:`~.user.tacacs+.TacacsPlusEndpoint` (via: tacacs+-server)
        - :class:`~.vpn.qkd.QkdEndpoint` (via: qkd-profile)

    **Usage:**
        payload: LocalPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # Local user name. | MaxLen: 64
    id: int  # User ID. | Default: 0 | Min: 0 | Max: 4294967295
    status: Literal["enable", "disable"]  # Enable/disable allowing the local user to authenti | Default: enable
    type: Literal["password", "radius", "tacacs+", "ldap", "saml"]  # Authentication method. | Default: password
    passwd: str  # User's password. | MaxLen: 128
    ldap_server: str  # Name of LDAP server with which the user must authe | MaxLen: 35
    radius_server: str  # Name of RADIUS server with which the user must aut | MaxLen: 35
    tacacs_plus_server: str  # Name of TACACS+ server with which the user must au | MaxLen: 35
    saml_server: str  # Name of SAML server with which the user must authe | MaxLen: 35
    two_factor: Literal["disable", "fortitoken", "fortitoken-cloud", "email", "sms"]  # Enable/disable two-factor authentication. | Default: disable
    two_factor_authentication: Literal["fortitoken", "email", "sms"]  # Authentication method by FortiToken Cloud.
    two_factor_notification: Literal["email", "sms"]  # Notification method for user activation by FortiTo
    fortitoken: str  # Two-factor recipient's FortiToken serial number. | MaxLen: 16
    email_to: str  # Two-factor recipient's email address. | MaxLen: 63
    sms_server: Literal["fortiguard", "custom"]  # Send SMS through FortiGuard or other external serv | Default: fortiguard
    sms_custom_server: str  # Two-factor recipient's SMS server. | MaxLen: 35
    sms_phone: str  # Two-factor recipient's mobile phone number. | MaxLen: 15
    passwd_policy: str  # Password policy to apply to this user, as defined | MaxLen: 35
    passwd_time: str  # Time of the last password update.
    authtimeout: int  # Time in minutes before the authentication timeout | Default: 0 | Min: 0 | Max: 1440
    workstation: str  # Name of the remote user workstation, if you want t | MaxLen: 35
    auth_concurrent_override: Literal["enable", "disable"]  # Enable/disable overriding the policy-auth-concurre | Default: disable
    auth_concurrent_value: int  # Maximum number of concurrent logins permitted from | Default: 0 | Min: 0 | Max: 100
    ppk_secret: str  # IKEv2 Postquantum Preshared Key
    ppk_identity: str  # IKEv2 Postquantum Preshared Key Identity. | MaxLen: 35
    qkd_profile: str  # Quantum Key Distribution (QKD) profile. | MaxLen: 35
    username_sensitivity: Literal["disable", "enable"]  # Enable/disable case and accent sensitivity when pe | Default: enable

# Nested TypedDicts for table field children (dict mode)

# Nested classes for table field children (object mode)


# Response TypedDict for GET returns (all fields present in API response)
class LocalResponse(TypedDict):
    """
    Type hints for user/local API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str  # Local user name. | MaxLen: 64
    id: int  # User ID. | Default: 0 | Min: 0 | Max: 4294967295
    status: Literal["enable", "disable"]  # Enable/disable allowing the local user to authenti | Default: enable
    type: Literal["password", "radius", "tacacs+", "ldap", "saml"]  # Authentication method. | Default: password
    passwd: str  # User's password. | MaxLen: 128
    ldap_server: str  # Name of LDAP server with which the user must authe | MaxLen: 35
    radius_server: str  # Name of RADIUS server with which the user must aut | MaxLen: 35
    tacacs_plus_server: str  # Name of TACACS+ server with which the user must au | MaxLen: 35
    saml_server: str  # Name of SAML server with which the user must authe | MaxLen: 35
    two_factor: Literal["disable", "fortitoken", "fortitoken-cloud", "email", "sms"]  # Enable/disable two-factor authentication. | Default: disable
    two_factor_authentication: Literal["fortitoken", "email", "sms"]  # Authentication method by FortiToken Cloud.
    two_factor_notification: Literal["email", "sms"]  # Notification method for user activation by FortiTo
    fortitoken: str  # Two-factor recipient's FortiToken serial number. | MaxLen: 16
    email_to: str  # Two-factor recipient's email address. | MaxLen: 63
    sms_server: Literal["fortiguard", "custom"]  # Send SMS through FortiGuard or other external serv | Default: fortiguard
    sms_custom_server: str  # Two-factor recipient's SMS server. | MaxLen: 35
    sms_phone: str  # Two-factor recipient's mobile phone number. | MaxLen: 15
    passwd_policy: str  # Password policy to apply to this user, as defined | MaxLen: 35
    passwd_time: str  # Time of the last password update.
    authtimeout: int  # Time in minutes before the authentication timeout | Default: 0 | Min: 0 | Max: 1440
    workstation: str  # Name of the remote user workstation, if you want t | MaxLen: 35
    auth_concurrent_override: Literal["enable", "disable"]  # Enable/disable overriding the policy-auth-concurre | Default: disable
    auth_concurrent_value: int  # Maximum number of concurrent logins permitted from | Default: 0 | Min: 0 | Max: 100
    ppk_secret: str  # IKEv2 Postquantum Preshared Key
    ppk_identity: str  # IKEv2 Postquantum Preshared Key Identity. | MaxLen: 35
    qkd_profile: str  # Quantum Key Distribution (QKD) profile. | MaxLen: 35
    username_sensitivity: Literal["disable", "enable"]  # Enable/disable case and accent sensitivity when pe | Default: enable


@final
class LocalObject:
    """Typed FortiObject for user/local with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Local user name. | MaxLen: 64
    name: str
    # User ID. | Default: 0 | Min: 0 | Max: 4294967295
    id: int
    # Enable/disable allowing the local user to authenticate with | Default: enable
    status: Literal["enable", "disable"]
    # Authentication method. | Default: password
    type: Literal["password", "radius", "tacacs+", "ldap", "saml"]
    # User's password. | MaxLen: 128
    passwd: str
    # Name of LDAP server with which the user must authenticate. | MaxLen: 35
    ldap_server: str
    # Name of RADIUS server with which the user must authenticate. | MaxLen: 35
    radius_server: str
    # Name of TACACS+ server with which the user must authenticate | MaxLen: 35
    tacacs_plus_server: str
    # Name of SAML server with which the user must authenticate. | MaxLen: 35
    saml_server: str
    # Enable/disable two-factor authentication. | Default: disable
    two_factor: Literal["disable", "fortitoken", "fortitoken-cloud", "email", "sms"]
    # Authentication method by FortiToken Cloud.
    two_factor_authentication: Literal["fortitoken", "email", "sms"]
    # Notification method for user activation by FortiToken Cloud.
    two_factor_notification: Literal["email", "sms"]
    # Two-factor recipient's FortiToken serial number. | MaxLen: 16
    fortitoken: str
    # Two-factor recipient's email address. | MaxLen: 63
    email_to: str
    # Send SMS through FortiGuard or other external server. | Default: fortiguard
    sms_server: Literal["fortiguard", "custom"]
    # Two-factor recipient's SMS server. | MaxLen: 35
    sms_custom_server: str
    # Two-factor recipient's mobile phone number. | MaxLen: 15
    sms_phone: str
    # Password policy to apply to this user, as defined in config | MaxLen: 35
    passwd_policy: str
    # Time of the last password update.
    passwd_time: str
    # Time in minutes before the authentication timeout for a user | Default: 0 | Min: 0 | Max: 1440
    authtimeout: int
    # Name of the remote user workstation, if you want to limit th | MaxLen: 35
    workstation: str
    # Enable/disable overriding the policy-auth-concurrent under c | Default: disable
    auth_concurrent_override: Literal["enable", "disable"]
    # Maximum number of concurrent logins permitted from the same | Default: 0 | Min: 0 | Max: 100
    auth_concurrent_value: int
    # IKEv2 Postquantum Preshared Key
    ppk_secret: str
    # IKEv2 Postquantum Preshared Key Identity. | MaxLen: 35
    ppk_identity: str
    # Quantum Key Distribution (QKD) profile. | MaxLen: 35
    qkd_profile: str
    # Enable/disable case and accent sensitivity when performing u | Default: enable
    username_sensitivity: Literal["disable", "enable"]
    
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
    def to_dict(self) -> LocalPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Local:
    """
    Configure local users.
    
    Path: user/local
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
    ) -> LocalObject: ...
    
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
    ) -> LocalObject: ...
    
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
    ) -> list[LocalObject]: ...
    
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
    ) -> LocalObject: ...
    
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
    ) -> LocalObject: ...
    
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
    ) -> list[LocalObject]: ...
    
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
    ) -> LocalObject: ...
    
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
    ) -> LocalObject: ...
    
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
    ) -> list[LocalObject]: ...
    
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
    ) -> LocalObject | list[LocalObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: LocalPayload | None = ...,
        name: str | None = ...,
        id: int | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        type: Literal["password", "radius", "tacacs+", "ldap", "saml"] | None = ...,
        passwd: str | None = ...,
        ldap_server: str | None = ...,
        radius_server: str | None = ...,
        tacacs_plus_server: str | None = ...,
        saml_server: str | None = ...,
        two_factor: Literal["disable", "fortitoken", "fortitoken-cloud", "email", "sms"] | None = ...,
        two_factor_authentication: Literal["fortitoken", "email", "sms"] | None = ...,
        two_factor_notification: Literal["email", "sms"] | None = ...,
        fortitoken: str | None = ...,
        email_to: str | None = ...,
        sms_server: Literal["fortiguard", "custom"] | None = ...,
        sms_custom_server: str | None = ...,
        sms_phone: str | None = ...,
        passwd_policy: str | None = ...,
        passwd_time: str | None = ...,
        authtimeout: int | None = ...,
        workstation: str | None = ...,
        auth_concurrent_override: Literal["enable", "disable"] | None = ...,
        auth_concurrent_value: int | None = ...,
        ppk_secret: str | None = ...,
        ppk_identity: str | None = ...,
        qkd_profile: str | None = ...,
        username_sensitivity: Literal["disable", "enable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> LocalObject: ...
    
    @overload
    def post(
        self,
        payload_dict: LocalPayload | None = ...,
        name: str | None = ...,
        id: int | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        type: Literal["password", "radius", "tacacs+", "ldap", "saml"] | None = ...,
        passwd: str | None = ...,
        ldap_server: str | None = ...,
        radius_server: str | None = ...,
        tacacs_plus_server: str | None = ...,
        saml_server: str | None = ...,
        two_factor: Literal["disable", "fortitoken", "fortitoken-cloud", "email", "sms"] | None = ...,
        two_factor_authentication: Literal["fortitoken", "email", "sms"] | None = ...,
        two_factor_notification: Literal["email", "sms"] | None = ...,
        fortitoken: str | None = ...,
        email_to: str | None = ...,
        sms_server: Literal["fortiguard", "custom"] | None = ...,
        sms_custom_server: str | None = ...,
        sms_phone: str | None = ...,
        passwd_policy: str | None = ...,
        passwd_time: str | None = ...,
        authtimeout: int | None = ...,
        workstation: str | None = ...,
        auth_concurrent_override: Literal["enable", "disable"] | None = ...,
        auth_concurrent_value: int | None = ...,
        ppk_secret: str | None = ...,
        ppk_identity: str | None = ...,
        qkd_profile: str | None = ...,
        username_sensitivity: Literal["disable", "enable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    # raw_json=True returns the full API envelope
    @overload
    def post(
        self,
        payload_dict: LocalPayload | None = ...,
        name: str | None = ...,
        id: int | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        type: Literal["password", "radius", "tacacs+", "ldap", "saml"] | None = ...,
        passwd: str | None = ...,
        ldap_server: str | None = ...,
        radius_server: str | None = ...,
        tacacs_plus_server: str | None = ...,
        saml_server: str | None = ...,
        two_factor: Literal["disable", "fortitoken", "fortitoken-cloud", "email", "sms"] | None = ...,
        two_factor_authentication: Literal["fortitoken", "email", "sms"] | None = ...,
        two_factor_notification: Literal["email", "sms"] | None = ...,
        fortitoken: str | None = ...,
        email_to: str | None = ...,
        sms_server: Literal["fortiguard", "custom"] | None = ...,
        sms_custom_server: str | None = ...,
        sms_phone: str | None = ...,
        passwd_policy: str | None = ...,
        passwd_time: str | None = ...,
        authtimeout: int | None = ...,
        workstation: str | None = ...,
        auth_concurrent_override: Literal["enable", "disable"] | None = ...,
        auth_concurrent_value: int | None = ...,
        ppk_secret: str | None = ...,
        ppk_identity: str | None = ...,
        qkd_profile: str | None = ...,
        username_sensitivity: Literal["disable", "enable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> RawAPIResponse: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: LocalPayload | None = ...,
        name: str | None = ...,
        id: int | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        type: Literal["password", "radius", "tacacs+", "ldap", "saml"] | None = ...,
        passwd: str | None = ...,
        ldap_server: str | None = ...,
        radius_server: str | None = ...,
        tacacs_plus_server: str | None = ...,
        saml_server: str | None = ...,
        two_factor: Literal["disable", "fortitoken", "fortitoken-cloud", "email", "sms"] | None = ...,
        two_factor_authentication: Literal["fortitoken", "email", "sms"] | None = ...,
        two_factor_notification: Literal["email", "sms"] | None = ...,
        fortitoken: str | None = ...,
        email_to: str | None = ...,
        sms_server: Literal["fortiguard", "custom"] | None = ...,
        sms_custom_server: str | None = ...,
        sms_phone: str | None = ...,
        passwd_policy: str | None = ...,
        passwd_time: str | None = ...,
        authtimeout: int | None = ...,
        workstation: str | None = ...,
        auth_concurrent_override: Literal["enable", "disable"] | None = ...,
        auth_concurrent_value: int | None = ...,
        ppk_secret: str | None = ...,
        ppk_identity: str | None = ...,
        qkd_profile: str | None = ...,
        username_sensitivity: Literal["disable", "enable"] | None = ...,
        vdom: str | bool | None = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    def post(
        self,
        payload_dict: LocalPayload | None = ...,
        name: str | None = ...,
        id: int | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        type: Literal["password", "radius", "tacacs+", "ldap", "saml"] | None = ...,
        passwd: str | None = ...,
        ldap_server: str | None = ...,
        radius_server: str | None = ...,
        tacacs_plus_server: str | None = ...,
        saml_server: str | None = ...,
        two_factor: Literal["disable", "fortitoken", "fortitoken-cloud", "email", "sms"] | None = ...,
        two_factor_authentication: Literal["fortitoken", "email", "sms"] | None = ...,
        two_factor_notification: Literal["email", "sms"] | None = ...,
        fortitoken: str | None = ...,
        email_to: str | None = ...,
        sms_server: Literal["fortiguard", "custom"] | None = ...,
        sms_custom_server: str | None = ...,
        sms_phone: str | None = ...,
        passwd_policy: str | None = ...,
        passwd_time: str | None = ...,
        authtimeout: int | None = ...,
        workstation: str | None = ...,
        auth_concurrent_override: Literal["enable", "disable"] | None = ...,
        auth_concurrent_value: int | None = ...,
        ppk_secret: str | None = ...,
        ppk_identity: str | None = ...,
        qkd_profile: str | None = ...,
        username_sensitivity: Literal["disable", "enable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: LocalPayload | None = ...,
        name: str | None = ...,
        id: int | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        type: Literal["password", "radius", "tacacs+", "ldap", "saml"] | None = ...,
        passwd: str | None = ...,
        ldap_server: str | None = ...,
        radius_server: str | None = ...,
        tacacs_plus_server: str | None = ...,
        saml_server: str | None = ...,
        two_factor: Literal["disable", "fortitoken", "fortitoken-cloud", "email", "sms"] | None = ...,
        two_factor_authentication: Literal["fortitoken", "email", "sms"] | None = ...,
        two_factor_notification: Literal["email", "sms"] | None = ...,
        fortitoken: str | None = ...,
        email_to: str | None = ...,
        sms_server: Literal["fortiguard", "custom"] | None = ...,
        sms_custom_server: str | None = ...,
        sms_phone: str | None = ...,
        passwd_policy: str | None = ...,
        passwd_time: str | None = ...,
        authtimeout: int | None = ...,
        workstation: str | None = ...,
        auth_concurrent_override: Literal["enable", "disable"] | None = ...,
        auth_concurrent_value: int | None = ...,
        ppk_secret: str | None = ...,
        ppk_identity: str | None = ...,
        qkd_profile: str | None = ...,
        username_sensitivity: Literal["disable", "enable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> LocalObject: ...
    
    @overload
    def put(
        self,
        payload_dict: LocalPayload | None = ...,
        name: str | None = ...,
        id: int | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        type: Literal["password", "radius", "tacacs+", "ldap", "saml"] | None = ...,
        passwd: str | None = ...,
        ldap_server: str | None = ...,
        radius_server: str | None = ...,
        tacacs_plus_server: str | None = ...,
        saml_server: str | None = ...,
        two_factor: Literal["disable", "fortitoken", "fortitoken-cloud", "email", "sms"] | None = ...,
        two_factor_authentication: Literal["fortitoken", "email", "sms"] | None = ...,
        two_factor_notification: Literal["email", "sms"] | None = ...,
        fortitoken: str | None = ...,
        email_to: str | None = ...,
        sms_server: Literal["fortiguard", "custom"] | None = ...,
        sms_custom_server: str | None = ...,
        sms_phone: str | None = ...,
        passwd_policy: str | None = ...,
        passwd_time: str | None = ...,
        authtimeout: int | None = ...,
        workstation: str | None = ...,
        auth_concurrent_override: Literal["enable", "disable"] | None = ...,
        auth_concurrent_value: int | None = ...,
        ppk_secret: str | None = ...,
        ppk_identity: str | None = ...,
        qkd_profile: str | None = ...,
        username_sensitivity: Literal["disable", "enable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    # raw_json=True returns the full API envelope
    @overload
    def put(
        self,
        payload_dict: LocalPayload | None = ...,
        name: str | None = ...,
        id: int | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        type: Literal["password", "radius", "tacacs+", "ldap", "saml"] | None = ...,
        passwd: str | None = ...,
        ldap_server: str | None = ...,
        radius_server: str | None = ...,
        tacacs_plus_server: str | None = ...,
        saml_server: str | None = ...,
        two_factor: Literal["disable", "fortitoken", "fortitoken-cloud", "email", "sms"] | None = ...,
        two_factor_authentication: Literal["fortitoken", "email", "sms"] | None = ...,
        two_factor_notification: Literal["email", "sms"] | None = ...,
        fortitoken: str | None = ...,
        email_to: str | None = ...,
        sms_server: Literal["fortiguard", "custom"] | None = ...,
        sms_custom_server: str | None = ...,
        sms_phone: str | None = ...,
        passwd_policy: str | None = ...,
        passwd_time: str | None = ...,
        authtimeout: int | None = ...,
        workstation: str | None = ...,
        auth_concurrent_override: Literal["enable", "disable"] | None = ...,
        auth_concurrent_value: int | None = ...,
        ppk_secret: str | None = ...,
        ppk_identity: str | None = ...,
        qkd_profile: str | None = ...,
        username_sensitivity: Literal["disable", "enable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> RawAPIResponse: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: LocalPayload | None = ...,
        name: str | None = ...,
        id: int | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        type: Literal["password", "radius", "tacacs+", "ldap", "saml"] | None = ...,
        passwd: str | None = ...,
        ldap_server: str | None = ...,
        radius_server: str | None = ...,
        tacacs_plus_server: str | None = ...,
        saml_server: str | None = ...,
        two_factor: Literal["disable", "fortitoken", "fortitoken-cloud", "email", "sms"] | None = ...,
        two_factor_authentication: Literal["fortitoken", "email", "sms"] | None = ...,
        two_factor_notification: Literal["email", "sms"] | None = ...,
        fortitoken: str | None = ...,
        email_to: str | None = ...,
        sms_server: Literal["fortiguard", "custom"] | None = ...,
        sms_custom_server: str | None = ...,
        sms_phone: str | None = ...,
        passwd_policy: str | None = ...,
        passwd_time: str | None = ...,
        authtimeout: int | None = ...,
        workstation: str | None = ...,
        auth_concurrent_override: Literal["enable", "disable"] | None = ...,
        auth_concurrent_value: int | None = ...,
        ppk_secret: str | None = ...,
        ppk_identity: str | None = ...,
        qkd_profile: str | None = ...,
        username_sensitivity: Literal["disable", "enable"] | None = ...,
        vdom: str | bool | None = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    def put(
        self,
        payload_dict: LocalPayload | None = ...,
        name: str | None = ...,
        id: int | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        type: Literal["password", "radius", "tacacs+", "ldap", "saml"] | None = ...,
        passwd: str | None = ...,
        ldap_server: str | None = ...,
        radius_server: str | None = ...,
        tacacs_plus_server: str | None = ...,
        saml_server: str | None = ...,
        two_factor: Literal["disable", "fortitoken", "fortitoken-cloud", "email", "sms"] | None = ...,
        two_factor_authentication: Literal["fortitoken", "email", "sms"] | None = ...,
        two_factor_notification: Literal["email", "sms"] | None = ...,
        fortitoken: str | None = ...,
        email_to: str | None = ...,
        sms_server: Literal["fortiguard", "custom"] | None = ...,
        sms_custom_server: str | None = ...,
        sms_phone: str | None = ...,
        passwd_policy: str | None = ...,
        passwd_time: str | None = ...,
        authtimeout: int | None = ...,
        workstation: str | None = ...,
        auth_concurrent_override: Literal["enable", "disable"] | None = ...,
        auth_concurrent_value: int | None = ...,
        ppk_secret: str | None = ...,
        ppk_identity: str | None = ...,
        qkd_profile: str | None = ...,
        username_sensitivity: Literal["disable", "enable"] | None = ...,
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
    ) -> LocalObject: ...
    
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
        payload_dict: LocalPayload | None = ...,
        name: str | None = ...,
        id: int | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        type: Literal["password", "radius", "tacacs+", "ldap", "saml"] | None = ...,
        passwd: str | None = ...,
        ldap_server: str | None = ...,
        radius_server: str | None = ...,
        tacacs_plus_server: str | None = ...,
        saml_server: str | None = ...,
        two_factor: Literal["disable", "fortitoken", "fortitoken-cloud", "email", "sms"] | None = ...,
        two_factor_authentication: Literal["fortitoken", "email", "sms"] | None = ...,
        two_factor_notification: Literal["email", "sms"] | None = ...,
        fortitoken: str | None = ...,
        email_to: str | None = ...,
        sms_server: Literal["fortiguard", "custom"] | None = ...,
        sms_custom_server: str | None = ...,
        sms_phone: str | None = ...,
        passwd_policy: str | None = ...,
        passwd_time: str | None = ...,
        authtimeout: int | None = ...,
        workstation: str | None = ...,
        auth_concurrent_override: Literal["enable", "disable"] | None = ...,
        auth_concurrent_value: int | None = ...,
        ppk_secret: str | None = ...,
        ppk_identity: str | None = ...,
        qkd_profile: str | None = ...,
        username_sensitivity: Literal["disable", "enable"] | None = ...,
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
    "Local",
    "LocalPayload",
    "LocalResponse",
    "LocalObject",
]