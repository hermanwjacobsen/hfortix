from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class AdminPayload(TypedDict, total=False):
    """
    Type hints for system/admin payload fields.
    
    Configure admin users.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.certificate.remote.RemoteEndpoint` (via: ssh-certificate)
        - :class:`~.system.accprofile.AccprofileEndpoint` (via: accprofile)
        - :class:`~.system.custom-language.CustomLanguageEndpoint` (via: guest-lang)
        - :class:`~.system.sms-server.SmsServerEndpoint` (via: sms-custom-server)

    **Usage:**
        payload: AdminPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # User name. | MaxLen: 64
    vdom: list[dict[str, Any]]  # Virtual domain(s) that the administrator can acces
    remote_auth: Literal["enable", "disable"]  # Enable/disable authentication using a remote RADIU | Default: disable
    remote_group: str  # User group name used for remote auth. | MaxLen: 35
    wildcard: Literal["enable", "disable"]  # Enable/disable wildcard RADIUS authentication. | Default: disable
    password: str  # Admin user password. | MaxLen: 128
    peer_auth: Literal["enable", "disable"]  # Set to enable peer certificate authentication | Default: disable
    peer_group: str  # Name of peer group defined under config user group | MaxLen: 35
    trusthost1: str  # Any IPv4 address or subnet address and netmask fro | Default: 0.0.0.0 0.0.0.0
    trusthost2: str  # Any IPv4 address or subnet address and netmask fro | Default: 0.0.0.0 0.0.0.0
    trusthost3: str  # Any IPv4 address or subnet address and netmask fro | Default: 0.0.0.0 0.0.0.0
    trusthost4: str  # Any IPv4 address or subnet address and netmask fro | Default: 0.0.0.0 0.0.0.0
    trusthost5: str  # Any IPv4 address or subnet address and netmask fro | Default: 0.0.0.0 0.0.0.0
    trusthost6: str  # Any IPv4 address or subnet address and netmask fro | Default: 0.0.0.0 0.0.0.0
    trusthost7: str  # Any IPv4 address or subnet address and netmask fro | Default: 0.0.0.0 0.0.0.0
    trusthost8: str  # Any IPv4 address or subnet address and netmask fro | Default: 0.0.0.0 0.0.0.0
    trusthost9: str  # Any IPv4 address or subnet address and netmask fro | Default: 0.0.0.0 0.0.0.0
    trusthost10: str  # Any IPv4 address or subnet address and netmask fro | Default: 0.0.0.0 0.0.0.0
    ip6_trusthost1: str  # Any IPv6 address from which the administrator can | Default: ::/0
    ip6_trusthost2: str  # Any IPv6 address from which the administrator can | Default: ::/0
    ip6_trusthost3: str  # Any IPv6 address from which the administrator can | Default: ::/0
    ip6_trusthost4: str  # Any IPv6 address from which the administrator can | Default: ::/0
    ip6_trusthost5: str  # Any IPv6 address from which the administrator can | Default: ::/0
    ip6_trusthost6: str  # Any IPv6 address from which the administrator can | Default: ::/0
    ip6_trusthost7: str  # Any IPv6 address from which the administrator can | Default: ::/0
    ip6_trusthost8: str  # Any IPv6 address from which the administrator can | Default: ::/0
    ip6_trusthost9: str  # Any IPv6 address from which the administrator can | Default: ::/0
    ip6_trusthost10: str  # Any IPv6 address from which the administrator can | Default: ::/0
    accprofile: str  # Access profile for this administrator. Access prof | MaxLen: 35
    allow_remove_admin_session: Literal["enable", "disable"]  # Enable/disable allow admin session to be removed b | Default: enable
    comments: str  # Comment. | MaxLen: 255
    ssh_public_key1: str  # Public key of an SSH client. The client is authent
    ssh_public_key2: str  # Public key of an SSH client. The client is authent
    ssh_public_key3: str  # Public key of an SSH client. The client is authent
    ssh_certificate: str  # Select the certificate to be used by the FortiGate | MaxLen: 35
    schedule: str  # Firewall schedule used to restrict when the admini | MaxLen: 35
    accprofile_override: Literal["enable", "disable"]  # Enable to use the name of an access profile provid | Default: disable
    vdom_override: Literal["enable", "disable"]  # Enable to use the names of VDOMs provided by the r | Default: disable
    password_expire: str  # Password expire time. | Default: 0000-00-00 00:00:00
    force_password_change: Literal["enable", "disable"]  # Enable/disable force password change on next login | Default: disable
    two_factor: Literal["disable", "fortitoken", "fortitoken-cloud", "email", "sms"]  # Enable/disable two-factor authentication. | Default: disable
    two_factor_authentication: Literal["fortitoken", "email", "sms"]  # Authentication method by FortiToken Cloud.
    two_factor_notification: Literal["email", "sms"]  # Notification method for user activation by FortiTo
    fortitoken: str  # This administrator's FortiToken serial number. | MaxLen: 16
    email_to: str  # This administrator's email address. | MaxLen: 63
    sms_server: Literal["fortiguard", "custom"]  # Send SMS messages using the FortiGuard SMS server | Default: fortiguard
    sms_custom_server: str  # Custom SMS server to send SMS messages to. | MaxLen: 35
    sms_phone: str  # Phone number on which the administrator receives S | MaxLen: 15
    guest_auth: Literal["disable", "enable"]  # Enable/disable guest authentication. | Default: disable
    guest_usergroups: list[dict[str, Any]]  # Select guest user groups.
    guest_lang: str  # Guest management portal language. | MaxLen: 35
    status: str  # print admin status information
    list: str  # print admin list information

# Nested TypedDicts for table field children (dict mode)

class AdminVdomItem(TypedDict):
    """Type hints for vdom table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # Virtual domain name. | MaxLen: 79


class AdminGuestusergroupsItem(TypedDict):
    """Type hints for guest-usergroups table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # Select guest user groups. | MaxLen: 79


# Nested classes for table field children (object mode)

@final
class AdminVdomObject:
    """Typed object for vdom table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Virtual domain name. | MaxLen: 79
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
class AdminGuestusergroupsObject:
    """Typed object for guest-usergroups table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Select guest user groups. | MaxLen: 79
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
class AdminResponse(TypedDict):
    """
    Type hints for system/admin API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str  # User name. | MaxLen: 64
    vdom: list[AdminVdomItem]  # Virtual domain(s) that the administrator can acces
    remote_auth: Literal["enable", "disable"]  # Enable/disable authentication using a remote RADIU | Default: disable
    remote_group: str  # User group name used for remote auth. | MaxLen: 35
    wildcard: Literal["enable", "disable"]  # Enable/disable wildcard RADIUS authentication. | Default: disable
    password: str  # Admin user password. | MaxLen: 128
    peer_auth: Literal["enable", "disable"]  # Set to enable peer certificate authentication | Default: disable
    peer_group: str  # Name of peer group defined under config user group | MaxLen: 35
    trusthost1: str  # Any IPv4 address or subnet address and netmask fro | Default: 0.0.0.0 0.0.0.0
    trusthost2: str  # Any IPv4 address or subnet address and netmask fro | Default: 0.0.0.0 0.0.0.0
    trusthost3: str  # Any IPv4 address or subnet address and netmask fro | Default: 0.0.0.0 0.0.0.0
    trusthost4: str  # Any IPv4 address or subnet address and netmask fro | Default: 0.0.0.0 0.0.0.0
    trusthost5: str  # Any IPv4 address or subnet address and netmask fro | Default: 0.0.0.0 0.0.0.0
    trusthost6: str  # Any IPv4 address or subnet address and netmask fro | Default: 0.0.0.0 0.0.0.0
    trusthost7: str  # Any IPv4 address or subnet address and netmask fro | Default: 0.0.0.0 0.0.0.0
    trusthost8: str  # Any IPv4 address or subnet address and netmask fro | Default: 0.0.0.0 0.0.0.0
    trusthost9: str  # Any IPv4 address or subnet address and netmask fro | Default: 0.0.0.0 0.0.0.0
    trusthost10: str  # Any IPv4 address or subnet address and netmask fro | Default: 0.0.0.0 0.0.0.0
    ip6_trusthost1: str  # Any IPv6 address from which the administrator can | Default: ::/0
    ip6_trusthost2: str  # Any IPv6 address from which the administrator can | Default: ::/0
    ip6_trusthost3: str  # Any IPv6 address from which the administrator can | Default: ::/0
    ip6_trusthost4: str  # Any IPv6 address from which the administrator can | Default: ::/0
    ip6_trusthost5: str  # Any IPv6 address from which the administrator can | Default: ::/0
    ip6_trusthost6: str  # Any IPv6 address from which the administrator can | Default: ::/0
    ip6_trusthost7: str  # Any IPv6 address from which the administrator can | Default: ::/0
    ip6_trusthost8: str  # Any IPv6 address from which the administrator can | Default: ::/0
    ip6_trusthost9: str  # Any IPv6 address from which the administrator can | Default: ::/0
    ip6_trusthost10: str  # Any IPv6 address from which the administrator can | Default: ::/0
    accprofile: str  # Access profile for this administrator. Access prof | MaxLen: 35
    allow_remove_admin_session: Literal["enable", "disable"]  # Enable/disable allow admin session to be removed b | Default: enable
    comments: str  # Comment. | MaxLen: 255
    ssh_public_key1: str  # Public key of an SSH client. The client is authent
    ssh_public_key2: str  # Public key of an SSH client. The client is authent
    ssh_public_key3: str  # Public key of an SSH client. The client is authent
    ssh_certificate: str  # Select the certificate to be used by the FortiGate | MaxLen: 35
    schedule: str  # Firewall schedule used to restrict when the admini | MaxLen: 35
    accprofile_override: Literal["enable", "disable"]  # Enable to use the name of an access profile provid | Default: disable
    vdom_override: Literal["enable", "disable"]  # Enable to use the names of VDOMs provided by the r | Default: disable
    password_expire: str  # Password expire time. | Default: 0000-00-00 00:00:00
    force_password_change: Literal["enable", "disable"]  # Enable/disable force password change on next login | Default: disable
    two_factor: Literal["disable", "fortitoken", "fortitoken-cloud", "email", "sms"]  # Enable/disable two-factor authentication. | Default: disable
    two_factor_authentication: Literal["fortitoken", "email", "sms"]  # Authentication method by FortiToken Cloud.
    two_factor_notification: Literal["email", "sms"]  # Notification method for user activation by FortiTo
    fortitoken: str  # This administrator's FortiToken serial number. | MaxLen: 16
    email_to: str  # This administrator's email address. | MaxLen: 63
    sms_server: Literal["fortiguard", "custom"]  # Send SMS messages using the FortiGuard SMS server | Default: fortiguard
    sms_custom_server: str  # Custom SMS server to send SMS messages to. | MaxLen: 35
    sms_phone: str  # Phone number on which the administrator receives S | MaxLen: 15
    guest_auth: Literal["disable", "enable"]  # Enable/disable guest authentication. | Default: disable
    guest_usergroups: list[AdminGuestusergroupsItem]  # Select guest user groups.
    guest_lang: str  # Guest management portal language. | MaxLen: 35
    status: str  # print admin status information
    list: str  # print admin list information


@final
class AdminObject:
    """Typed FortiObject for system/admin with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # User name. | MaxLen: 64
    name: str
    # Virtual domain(s) that the administrator can access.
    vdom: list[AdminVdomObject]
    # Enable/disable authentication using a remote RADIUS, LDAP, o | Default: disable
    remote_auth: Literal["enable", "disable"]
    # User group name used for remote auth. | MaxLen: 35
    remote_group: str
    # Enable/disable wildcard RADIUS authentication. | Default: disable
    wildcard: Literal["enable", "disable"]
    # Admin user password. | MaxLen: 128
    password: str
    # Set to enable peer certificate authentication | Default: disable
    peer_auth: Literal["enable", "disable"]
    # Name of peer group defined under config user group which has | MaxLen: 35
    peer_group: str
    # Any IPv4 address or subnet address and netmask from which th | Default: 0.0.0.0 0.0.0.0
    trusthost1: str
    # Any IPv4 address or subnet address and netmask from which th | Default: 0.0.0.0 0.0.0.0
    trusthost2: str
    # Any IPv4 address or subnet address and netmask from which th | Default: 0.0.0.0 0.0.0.0
    trusthost3: str
    # Any IPv4 address or subnet address and netmask from which th | Default: 0.0.0.0 0.0.0.0
    trusthost4: str
    # Any IPv4 address or subnet address and netmask from which th | Default: 0.0.0.0 0.0.0.0
    trusthost5: str
    # Any IPv4 address or subnet address and netmask from which th | Default: 0.0.0.0 0.0.0.0
    trusthost6: str
    # Any IPv4 address or subnet address and netmask from which th | Default: 0.0.0.0 0.0.0.0
    trusthost7: str
    # Any IPv4 address or subnet address and netmask from which th | Default: 0.0.0.0 0.0.0.0
    trusthost8: str
    # Any IPv4 address or subnet address and netmask from which th | Default: 0.0.0.0 0.0.0.0
    trusthost9: str
    # Any IPv4 address or subnet address and netmask from which th | Default: 0.0.0.0 0.0.0.0
    trusthost10: str
    # Any IPv6 address from which the administrator can connect to | Default: ::/0
    ip6_trusthost1: str
    # Any IPv6 address from which the administrator can connect to | Default: ::/0
    ip6_trusthost2: str
    # Any IPv6 address from which the administrator can connect to | Default: ::/0
    ip6_trusthost3: str
    # Any IPv6 address from which the administrator can connect to | Default: ::/0
    ip6_trusthost4: str
    # Any IPv6 address from which the administrator can connect to | Default: ::/0
    ip6_trusthost5: str
    # Any IPv6 address from which the administrator can connect to | Default: ::/0
    ip6_trusthost6: str
    # Any IPv6 address from which the administrator can connect to | Default: ::/0
    ip6_trusthost7: str
    # Any IPv6 address from which the administrator can connect to | Default: ::/0
    ip6_trusthost8: str
    # Any IPv6 address from which the administrator can connect to | Default: ::/0
    ip6_trusthost9: str
    # Any IPv6 address from which the administrator can connect to | Default: ::/0
    ip6_trusthost10: str
    # Access profile for this administrator. Access profiles contr | MaxLen: 35
    accprofile: str
    # Enable/disable allow admin session to be removed by privileg | Default: enable
    allow_remove_admin_session: Literal["enable", "disable"]
    # Comment. | MaxLen: 255
    comments: str
    # Public key of an SSH client. The client is authenticated wit
    ssh_public_key1: str
    # Public key of an SSH client. The client is authenticated wit
    ssh_public_key2: str
    # Public key of an SSH client. The client is authenticated wit
    ssh_public_key3: str
    # Select the certificate to be used by the FortiGate for authe | MaxLen: 35
    ssh_certificate: str
    # Firewall schedule used to restrict when the administrator ca | MaxLen: 35
    schedule: str
    # Enable to use the name of an access profile provided by the | Default: disable
    accprofile_override: Literal["enable", "disable"]
    # Enable to use the names of VDOMs provided by the remote auth | Default: disable
    vdom_override: Literal["enable", "disable"]
    # Password expire time. | Default: 0000-00-00 00:00:00
    password_expire: str
    # Enable/disable force password change on next login. | Default: disable
    force_password_change: Literal["enable", "disable"]
    # Enable/disable two-factor authentication. | Default: disable
    two_factor: Literal["disable", "fortitoken", "fortitoken-cloud", "email", "sms"]
    # Authentication method by FortiToken Cloud.
    two_factor_authentication: Literal["fortitoken", "email", "sms"]
    # Notification method for user activation by FortiToken Cloud.
    two_factor_notification: Literal["email", "sms"]
    # This administrator's FortiToken serial number. | MaxLen: 16
    fortitoken: str
    # This administrator's email address. | MaxLen: 63
    email_to: str
    # Send SMS messages using the FortiGuard SMS server or a custo | Default: fortiguard
    sms_server: Literal["fortiguard", "custom"]
    # Custom SMS server to send SMS messages to. | MaxLen: 35
    sms_custom_server: str
    # Phone number on which the administrator receives SMS message | MaxLen: 15
    sms_phone: str
    # Enable/disable guest authentication. | Default: disable
    guest_auth: Literal["disable", "enable"]
    # Select guest user groups.
    guest_usergroups: list[AdminGuestusergroupsObject]
    # Guest management portal language. | MaxLen: 35
    guest_lang: str
    # print admin status information
    status: str
    # print admin list information
    list: str
    
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
    def to_dict(self) -> AdminPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Admin:
    """
    Configure admin users.
    
    Path: system/admin
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
    ) -> AdminObject: ...
    
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
    ) -> AdminObject: ...
    
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
    ) -> FortiObjectList[AdminObject]: ...
    
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
    ) -> AdminObject: ...
    
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
    ) -> AdminObject: ...
    
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
    ) -> FortiObjectList[AdminObject]: ...
    
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
    ) -> AdminObject: ...
    
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
    ) -> AdminObject: ...
    
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
    ) -> FortiObjectList[AdminObject]: ...
    
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
    ) -> AdminObject | list[AdminObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: AdminPayload | None = ...,
        name: str | None = ...,
        remote_auth: Literal["enable", "disable"] | None = ...,
        remote_group: str | None = ...,
        wildcard: Literal["enable", "disable"] | None = ...,
        password: str | None = ...,
        peer_auth: Literal["enable", "disable"] | None = ...,
        peer_group: str | None = ...,
        trusthost1: str | None = ...,
        trusthost2: str | None = ...,
        trusthost3: str | None = ...,
        trusthost4: str | None = ...,
        trusthost5: str | None = ...,
        trusthost6: str | None = ...,
        trusthost7: str | None = ...,
        trusthost8: str | None = ...,
        trusthost9: str | None = ...,
        trusthost10: str | None = ...,
        ip6_trusthost1: str | None = ...,
        ip6_trusthost2: str | None = ...,
        ip6_trusthost3: str | None = ...,
        ip6_trusthost4: str | None = ...,
        ip6_trusthost5: str | None = ...,
        ip6_trusthost6: str | None = ...,
        ip6_trusthost7: str | None = ...,
        ip6_trusthost8: str | None = ...,
        ip6_trusthost9: str | None = ...,
        ip6_trusthost10: str | None = ...,
        accprofile: str | None = ...,
        allow_remove_admin_session: Literal["enable", "disable"] | None = ...,
        comments: str | None = ...,
        ssh_public_key1: str | None = ...,
        ssh_public_key2: str | None = ...,
        ssh_public_key3: str | None = ...,
        ssh_certificate: str | None = ...,
        schedule: str | None = ...,
        accprofile_override: Literal["enable", "disable"] | None = ...,
        vdom_override: Literal["enable", "disable"] | None = ...,
        password_expire: str | None = ...,
        force_password_change: Literal["enable", "disable"] | None = ...,
        two_factor: Literal["disable", "fortitoken", "fortitoken-cloud", "email", "sms"] | None = ...,
        two_factor_authentication: Literal["fortitoken", "email", "sms"] | None = ...,
        two_factor_notification: Literal["email", "sms"] | None = ...,
        fortitoken: str | None = ...,
        email_to: str | None = ...,
        sms_server: Literal["fortiguard", "custom"] | None = ...,
        sms_custom_server: str | None = ...,
        sms_phone: str | None = ...,
        guest_auth: Literal["disable", "enable"] | None = ...,
        guest_usergroups: str | list[str] | list[dict[str, Any]] | None = ...,
        guest_lang: str | None = ...,
        status: str | None = ...,
        list: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> AdminObject: ...
    
    @overload
    def post(
        self,
        payload_dict: AdminPayload | None = ...,
        name: str | None = ...,
        remote_auth: Literal["enable", "disable"] | None = ...,
        remote_group: str | None = ...,
        wildcard: Literal["enable", "disable"] | None = ...,
        password: str | None = ...,
        peer_auth: Literal["enable", "disable"] | None = ...,
        peer_group: str | None = ...,
        trusthost1: str | None = ...,
        trusthost2: str | None = ...,
        trusthost3: str | None = ...,
        trusthost4: str | None = ...,
        trusthost5: str | None = ...,
        trusthost6: str | None = ...,
        trusthost7: str | None = ...,
        trusthost8: str | None = ...,
        trusthost9: str | None = ...,
        trusthost10: str | None = ...,
        ip6_trusthost1: str | None = ...,
        ip6_trusthost2: str | None = ...,
        ip6_trusthost3: str | None = ...,
        ip6_trusthost4: str | None = ...,
        ip6_trusthost5: str | None = ...,
        ip6_trusthost6: str | None = ...,
        ip6_trusthost7: str | None = ...,
        ip6_trusthost8: str | None = ...,
        ip6_trusthost9: str | None = ...,
        ip6_trusthost10: str | None = ...,
        accprofile: str | None = ...,
        allow_remove_admin_session: Literal["enable", "disable"] | None = ...,
        comments: str | None = ...,
        ssh_public_key1: str | None = ...,
        ssh_public_key2: str | None = ...,
        ssh_public_key3: str | None = ...,
        ssh_certificate: str | None = ...,
        schedule: str | None = ...,
        accprofile_override: Literal["enable", "disable"] | None = ...,
        vdom_override: Literal["enable", "disable"] | None = ...,
        password_expire: str | None = ...,
        force_password_change: Literal["enable", "disable"] | None = ...,
        two_factor: Literal["disable", "fortitoken", "fortitoken-cloud", "email", "sms"] | None = ...,
        two_factor_authentication: Literal["fortitoken", "email", "sms"] | None = ...,
        two_factor_notification: Literal["email", "sms"] | None = ...,
        fortitoken: str | None = ...,
        email_to: str | None = ...,
        sms_server: Literal["fortiguard", "custom"] | None = ...,
        sms_custom_server: str | None = ...,
        sms_phone: str | None = ...,
        guest_auth: Literal["disable", "enable"] | None = ...,
        guest_usergroups: str | list[str] | list[dict[str, Any]] | None = ...,
        guest_lang: str | None = ...,
        status: str | None = ...,
        list: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: AdminPayload | None = ...,
        name: str | None = ...,
        remote_auth: Literal["enable", "disable"] | None = ...,
        remote_group: str | None = ...,
        wildcard: Literal["enable", "disable"] | None = ...,
        password: str | None = ...,
        peer_auth: Literal["enable", "disable"] | None = ...,
        peer_group: str | None = ...,
        trusthost1: str | None = ...,
        trusthost2: str | None = ...,
        trusthost3: str | None = ...,
        trusthost4: str | None = ...,
        trusthost5: str | None = ...,
        trusthost6: str | None = ...,
        trusthost7: str | None = ...,
        trusthost8: str | None = ...,
        trusthost9: str | None = ...,
        trusthost10: str | None = ...,
        ip6_trusthost1: str | None = ...,
        ip6_trusthost2: str | None = ...,
        ip6_trusthost3: str | None = ...,
        ip6_trusthost4: str | None = ...,
        ip6_trusthost5: str | None = ...,
        ip6_trusthost6: str | None = ...,
        ip6_trusthost7: str | None = ...,
        ip6_trusthost8: str | None = ...,
        ip6_trusthost9: str | None = ...,
        ip6_trusthost10: str | None = ...,
        accprofile: str | None = ...,
        allow_remove_admin_session: Literal["enable", "disable"] | None = ...,
        comments: str | None = ...,
        ssh_public_key1: str | None = ...,
        ssh_public_key2: str | None = ...,
        ssh_public_key3: str | None = ...,
        ssh_certificate: str | None = ...,
        schedule: str | None = ...,
        accprofile_override: Literal["enable", "disable"] | None = ...,
        vdom_override: Literal["enable", "disable"] | None = ...,
        password_expire: str | None = ...,
        force_password_change: Literal["enable", "disable"] | None = ...,
        two_factor: Literal["disable", "fortitoken", "fortitoken-cloud", "email", "sms"] | None = ...,
        two_factor_authentication: Literal["fortitoken", "email", "sms"] | None = ...,
        two_factor_notification: Literal["email", "sms"] | None = ...,
        fortitoken: str | None = ...,
        email_to: str | None = ...,
        sms_server: Literal["fortiguard", "custom"] | None = ...,
        sms_custom_server: str | None = ...,
        sms_phone: str | None = ...,
        guest_auth: Literal["disable", "enable"] | None = ...,
        guest_usergroups: str | list[str] | list[dict[str, Any]] | None = ...,
        guest_lang: str | None = ...,
        status: str | None = ...,
        list: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def post(
        self,
        payload_dict: AdminPayload | None = ...,
        name: str | None = ...,
        remote_auth: Literal["enable", "disable"] | None = ...,
        remote_group: str | None = ...,
        wildcard: Literal["enable", "disable"] | None = ...,
        password: str | None = ...,
        peer_auth: Literal["enable", "disable"] | None = ...,
        peer_group: str | None = ...,
        trusthost1: str | None = ...,
        trusthost2: str | None = ...,
        trusthost3: str | None = ...,
        trusthost4: str | None = ...,
        trusthost5: str | None = ...,
        trusthost6: str | None = ...,
        trusthost7: str | None = ...,
        trusthost8: str | None = ...,
        trusthost9: str | None = ...,
        trusthost10: str | None = ...,
        ip6_trusthost1: str | None = ...,
        ip6_trusthost2: str | None = ...,
        ip6_trusthost3: str | None = ...,
        ip6_trusthost4: str | None = ...,
        ip6_trusthost5: str | None = ...,
        ip6_trusthost6: str | None = ...,
        ip6_trusthost7: str | None = ...,
        ip6_trusthost8: str | None = ...,
        ip6_trusthost9: str | None = ...,
        ip6_trusthost10: str | None = ...,
        accprofile: str | None = ...,
        allow_remove_admin_session: Literal["enable", "disable"] | None = ...,
        comments: str | None = ...,
        ssh_public_key1: str | None = ...,
        ssh_public_key2: str | None = ...,
        ssh_public_key3: str | None = ...,
        ssh_certificate: str | None = ...,
        schedule: str | None = ...,
        accprofile_override: Literal["enable", "disable"] | None = ...,
        vdom_override: Literal["enable", "disable"] | None = ...,
        password_expire: str | None = ...,
        force_password_change: Literal["enable", "disable"] | None = ...,
        two_factor: Literal["disable", "fortitoken", "fortitoken-cloud", "email", "sms"] | None = ...,
        two_factor_authentication: Literal["fortitoken", "email", "sms"] | None = ...,
        two_factor_notification: Literal["email", "sms"] | None = ...,
        fortitoken: str | None = ...,
        email_to: str | None = ...,
        sms_server: Literal["fortiguard", "custom"] | None = ...,
        sms_custom_server: str | None = ...,
        sms_phone: str | None = ...,
        guest_auth: Literal["disable", "enable"] | None = ...,
        guest_usergroups: str | list[str] | list[dict[str, Any]] | None = ...,
        guest_lang: str | None = ...,
        status: str | None = ...,
        list: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: AdminPayload | None = ...,
        name: str | None = ...,
        remote_auth: Literal["enable", "disable"] | None = ...,
        remote_group: str | None = ...,
        wildcard: Literal["enable", "disable"] | None = ...,
        password: str | None = ...,
        peer_auth: Literal["enable", "disable"] | None = ...,
        peer_group: str | None = ...,
        trusthost1: str | None = ...,
        trusthost2: str | None = ...,
        trusthost3: str | None = ...,
        trusthost4: str | None = ...,
        trusthost5: str | None = ...,
        trusthost6: str | None = ...,
        trusthost7: str | None = ...,
        trusthost8: str | None = ...,
        trusthost9: str | None = ...,
        trusthost10: str | None = ...,
        ip6_trusthost1: str | None = ...,
        ip6_trusthost2: str | None = ...,
        ip6_trusthost3: str | None = ...,
        ip6_trusthost4: str | None = ...,
        ip6_trusthost5: str | None = ...,
        ip6_trusthost6: str | None = ...,
        ip6_trusthost7: str | None = ...,
        ip6_trusthost8: str | None = ...,
        ip6_trusthost9: str | None = ...,
        ip6_trusthost10: str | None = ...,
        accprofile: str | None = ...,
        allow_remove_admin_session: Literal["enable", "disable"] | None = ...,
        comments: str | None = ...,
        ssh_public_key1: str | None = ...,
        ssh_public_key2: str | None = ...,
        ssh_public_key3: str | None = ...,
        ssh_certificate: str | None = ...,
        schedule: str | None = ...,
        accprofile_override: Literal["enable", "disable"] | None = ...,
        vdom_override: Literal["enable", "disable"] | None = ...,
        password_expire: str | None = ...,
        force_password_change: Literal["enable", "disable"] | None = ...,
        two_factor: Literal["disable", "fortitoken", "fortitoken-cloud", "email", "sms"] | None = ...,
        two_factor_authentication: Literal["fortitoken", "email", "sms"] | None = ...,
        two_factor_notification: Literal["email", "sms"] | None = ...,
        fortitoken: str | None = ...,
        email_to: str | None = ...,
        sms_server: Literal["fortiguard", "custom"] | None = ...,
        sms_custom_server: str | None = ...,
        sms_phone: str | None = ...,
        guest_auth: Literal["disable", "enable"] | None = ...,
        guest_usergroups: str | list[str] | list[dict[str, Any]] | None = ...,
        guest_lang: str | None = ...,
        status: str | None = ...,
        list: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> AdminObject: ...
    
    @overload
    def put(
        self,
        payload_dict: AdminPayload | None = ...,
        name: str | None = ...,
        remote_auth: Literal["enable", "disable"] | None = ...,
        remote_group: str | None = ...,
        wildcard: Literal["enable", "disable"] | None = ...,
        password: str | None = ...,
        peer_auth: Literal["enable", "disable"] | None = ...,
        peer_group: str | None = ...,
        trusthost1: str | None = ...,
        trusthost2: str | None = ...,
        trusthost3: str | None = ...,
        trusthost4: str | None = ...,
        trusthost5: str | None = ...,
        trusthost6: str | None = ...,
        trusthost7: str | None = ...,
        trusthost8: str | None = ...,
        trusthost9: str | None = ...,
        trusthost10: str | None = ...,
        ip6_trusthost1: str | None = ...,
        ip6_trusthost2: str | None = ...,
        ip6_trusthost3: str | None = ...,
        ip6_trusthost4: str | None = ...,
        ip6_trusthost5: str | None = ...,
        ip6_trusthost6: str | None = ...,
        ip6_trusthost7: str | None = ...,
        ip6_trusthost8: str | None = ...,
        ip6_trusthost9: str | None = ...,
        ip6_trusthost10: str | None = ...,
        accprofile: str | None = ...,
        allow_remove_admin_session: Literal["enable", "disable"] | None = ...,
        comments: str | None = ...,
        ssh_public_key1: str | None = ...,
        ssh_public_key2: str | None = ...,
        ssh_public_key3: str | None = ...,
        ssh_certificate: str | None = ...,
        schedule: str | None = ...,
        accprofile_override: Literal["enable", "disable"] | None = ...,
        vdom_override: Literal["enable", "disable"] | None = ...,
        password_expire: str | None = ...,
        force_password_change: Literal["enable", "disable"] | None = ...,
        two_factor: Literal["disable", "fortitoken", "fortitoken-cloud", "email", "sms"] | None = ...,
        two_factor_authentication: Literal["fortitoken", "email", "sms"] | None = ...,
        two_factor_notification: Literal["email", "sms"] | None = ...,
        fortitoken: str | None = ...,
        email_to: str | None = ...,
        sms_server: Literal["fortiguard", "custom"] | None = ...,
        sms_custom_server: str | None = ...,
        sms_phone: str | None = ...,
        guest_auth: Literal["disable", "enable"] | None = ...,
        guest_usergroups: str | list[str] | list[dict[str, Any]] | None = ...,
        guest_lang: str | None = ...,
        status: str | None = ...,
        list: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: AdminPayload | None = ...,
        name: str | None = ...,
        remote_auth: Literal["enable", "disable"] | None = ...,
        remote_group: str | None = ...,
        wildcard: Literal["enable", "disable"] | None = ...,
        password: str | None = ...,
        peer_auth: Literal["enable", "disable"] | None = ...,
        peer_group: str | None = ...,
        trusthost1: str | None = ...,
        trusthost2: str | None = ...,
        trusthost3: str | None = ...,
        trusthost4: str | None = ...,
        trusthost5: str | None = ...,
        trusthost6: str | None = ...,
        trusthost7: str | None = ...,
        trusthost8: str | None = ...,
        trusthost9: str | None = ...,
        trusthost10: str | None = ...,
        ip6_trusthost1: str | None = ...,
        ip6_trusthost2: str | None = ...,
        ip6_trusthost3: str | None = ...,
        ip6_trusthost4: str | None = ...,
        ip6_trusthost5: str | None = ...,
        ip6_trusthost6: str | None = ...,
        ip6_trusthost7: str | None = ...,
        ip6_trusthost8: str | None = ...,
        ip6_trusthost9: str | None = ...,
        ip6_trusthost10: str | None = ...,
        accprofile: str | None = ...,
        allow_remove_admin_session: Literal["enable", "disable"] | None = ...,
        comments: str | None = ...,
        ssh_public_key1: str | None = ...,
        ssh_public_key2: str | None = ...,
        ssh_public_key3: str | None = ...,
        ssh_certificate: str | None = ...,
        schedule: str | None = ...,
        accprofile_override: Literal["enable", "disable"] | None = ...,
        vdom_override: Literal["enable", "disable"] | None = ...,
        password_expire: str | None = ...,
        force_password_change: Literal["enable", "disable"] | None = ...,
        two_factor: Literal["disable", "fortitoken", "fortitoken-cloud", "email", "sms"] | None = ...,
        two_factor_authentication: Literal["fortitoken", "email", "sms"] | None = ...,
        two_factor_notification: Literal["email", "sms"] | None = ...,
        fortitoken: str | None = ...,
        email_to: str | None = ...,
        sms_server: Literal["fortiguard", "custom"] | None = ...,
        sms_custom_server: str | None = ...,
        sms_phone: str | None = ...,
        guest_auth: Literal["disable", "enable"] | None = ...,
        guest_usergroups: str | list[str] | list[dict[str, Any]] | None = ...,
        guest_lang: str | None = ...,
        status: str | None = ...,
        list: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def put(
        self,
        payload_dict: AdminPayload | None = ...,
        name: str | None = ...,
        remote_auth: Literal["enable", "disable"] | None = ...,
        remote_group: str | None = ...,
        wildcard: Literal["enable", "disable"] | None = ...,
        password: str | None = ...,
        peer_auth: Literal["enable", "disable"] | None = ...,
        peer_group: str | None = ...,
        trusthost1: str | None = ...,
        trusthost2: str | None = ...,
        trusthost3: str | None = ...,
        trusthost4: str | None = ...,
        trusthost5: str | None = ...,
        trusthost6: str | None = ...,
        trusthost7: str | None = ...,
        trusthost8: str | None = ...,
        trusthost9: str | None = ...,
        trusthost10: str | None = ...,
        ip6_trusthost1: str | None = ...,
        ip6_trusthost2: str | None = ...,
        ip6_trusthost3: str | None = ...,
        ip6_trusthost4: str | None = ...,
        ip6_trusthost5: str | None = ...,
        ip6_trusthost6: str | None = ...,
        ip6_trusthost7: str | None = ...,
        ip6_trusthost8: str | None = ...,
        ip6_trusthost9: str | None = ...,
        ip6_trusthost10: str | None = ...,
        accprofile: str | None = ...,
        allow_remove_admin_session: Literal["enable", "disable"] | None = ...,
        comments: str | None = ...,
        ssh_public_key1: str | None = ...,
        ssh_public_key2: str | None = ...,
        ssh_public_key3: str | None = ...,
        ssh_certificate: str | None = ...,
        schedule: str | None = ...,
        accprofile_override: Literal["enable", "disable"] | None = ...,
        vdom_override: Literal["enable", "disable"] | None = ...,
        password_expire: str | None = ...,
        force_password_change: Literal["enable", "disable"] | None = ...,
        two_factor: Literal["disable", "fortitoken", "fortitoken-cloud", "email", "sms"] | None = ...,
        two_factor_authentication: Literal["fortitoken", "email", "sms"] | None = ...,
        two_factor_notification: Literal["email", "sms"] | None = ...,
        fortitoken: str | None = ...,
        email_to: str | None = ...,
        sms_server: Literal["fortiguard", "custom"] | None = ...,
        sms_custom_server: str | None = ...,
        sms_phone: str | None = ...,
        guest_auth: Literal["disable", "enable"] | None = ...,
        guest_usergroups: str | list[str] | list[dict[str, Any]] | None = ...,
        guest_lang: str | None = ...,
        status: str | None = ...,
        list: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> AdminObject: ...
    
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
        payload_dict: AdminPayload | None = ...,
        name: str | None = ...,
        remote_auth: Literal["enable", "disable"] | None = ...,
        remote_group: str | None = ...,
        wildcard: Literal["enable", "disable"] | None = ...,
        password: str | None = ...,
        peer_auth: Literal["enable", "disable"] | None = ...,
        peer_group: str | None = ...,
        trusthost1: str | None = ...,
        trusthost2: str | None = ...,
        trusthost3: str | None = ...,
        trusthost4: str | None = ...,
        trusthost5: str | None = ...,
        trusthost6: str | None = ...,
        trusthost7: str | None = ...,
        trusthost8: str | None = ...,
        trusthost9: str | None = ...,
        trusthost10: str | None = ...,
        ip6_trusthost1: str | None = ...,
        ip6_trusthost2: str | None = ...,
        ip6_trusthost3: str | None = ...,
        ip6_trusthost4: str | None = ...,
        ip6_trusthost5: str | None = ...,
        ip6_trusthost6: str | None = ...,
        ip6_trusthost7: str | None = ...,
        ip6_trusthost8: str | None = ...,
        ip6_trusthost9: str | None = ...,
        ip6_trusthost10: str | None = ...,
        accprofile: str | None = ...,
        allow_remove_admin_session: Literal["enable", "disable"] | None = ...,
        comments: str | None = ...,
        ssh_public_key1: str | None = ...,
        ssh_public_key2: str | None = ...,
        ssh_public_key3: str | None = ...,
        ssh_certificate: str | None = ...,
        schedule: str | None = ...,
        accprofile_override: Literal["enable", "disable"] | None = ...,
        vdom_override: Literal["enable", "disable"] | None = ...,
        password_expire: str | None = ...,
        force_password_change: Literal["enable", "disable"] | None = ...,
        two_factor: Literal["disable", "fortitoken", "fortitoken-cloud", "email", "sms"] | None = ...,
        two_factor_authentication: Literal["fortitoken", "email", "sms"] | None = ...,
        two_factor_notification: Literal["email", "sms"] | None = ...,
        fortitoken: str | None = ...,
        email_to: str | None = ...,
        sms_server: Literal["fortiguard", "custom"] | None = ...,
        sms_custom_server: str | None = ...,
        sms_phone: str | None = ...,
        guest_auth: Literal["disable", "enable"] | None = ...,
        guest_usergroups: str | list[str] | list[dict[str, Any]] | None = ...,
        guest_lang: str | None = ...,
        status: str | None = ...,
        list: str | None = ...,
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
    "Admin",
    "AdminPayload",
    "AdminResponse",
    "AdminObject",
]