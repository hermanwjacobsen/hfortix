from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class PeerPayload(TypedDict, total=False):
    """
    Type hints for user/peer payload fields.
    
    Configure peer users.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.user.ldap.LdapEndpoint` (via: mfa-server)
        - :class:`~.user.radius.RadiusEndpoint` (via: mfa-server)
        - :class:`~.vpn.certificate.ca.CaEndpoint` (via: ca)
        - :class:`~.vpn.certificate.ocsp-server.OcspServerEndpoint` (via: ocsp-override-server)

    **Usage:**
        payload: PeerPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # Peer name. | MaxLen: 35
    mandatory_ca_verify: Literal["enable", "disable"]  # Determine what happens to the peer if the CA certi | Default: enable
    ca: str  # Name of the CA certificate. | MaxLen: 127
    subject: str  # Peer certificate name constraints. | MaxLen: 255
    cn: str  # Peer certificate common name. | MaxLen: 255
    cn_type: Literal["string", "email", "FQDN", "ipv4", "ipv6"]  # Peer certificate common name type. | Default: string
    mfa_mode: Literal["none", "password", "subject-identity"]  # MFA mode for remote peer authentication/authorizat | Default: none
    mfa_server: str  # Name of a remote authenticator. Performs client ac | MaxLen: 35
    mfa_username: str  # Unified username for remote authentication. | MaxLen: 35
    mfa_password: str  # Unified password for remote authentication. This f | MaxLen: 128
    ocsp_override_server: str  # Online Certificate Status Protocol (OCSP) server f | MaxLen: 35
    two_factor: Literal["enable", "disable"]  # Enable/disable two-factor authentication, applying | Default: disable
    passwd: str  # Peer's password used for two-factor authentication | MaxLen: 128

# Nested TypedDicts for table field children (dict mode)

# Nested classes for table field children (object mode)


# Response TypedDict for GET returns (all fields present in API response)
class PeerResponse(TypedDict):
    """
    Type hints for user/peer API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str  # Peer name. | MaxLen: 35
    mandatory_ca_verify: Literal["enable", "disable"]  # Determine what happens to the peer if the CA certi | Default: enable
    ca: str  # Name of the CA certificate. | MaxLen: 127
    subject: str  # Peer certificate name constraints. | MaxLen: 255
    cn: str  # Peer certificate common name. | MaxLen: 255
    cn_type: Literal["string", "email", "FQDN", "ipv4", "ipv6"]  # Peer certificate common name type. | Default: string
    mfa_mode: Literal["none", "password", "subject-identity"]  # MFA mode for remote peer authentication/authorizat | Default: none
    mfa_server: str  # Name of a remote authenticator. Performs client ac | MaxLen: 35
    mfa_username: str  # Unified username for remote authentication. | MaxLen: 35
    mfa_password: str  # Unified password for remote authentication. This f | MaxLen: 128
    ocsp_override_server: str  # Online Certificate Status Protocol (OCSP) server f | MaxLen: 35
    two_factor: Literal["enable", "disable"]  # Enable/disable two-factor authentication, applying | Default: disable
    passwd: str  # Peer's password used for two-factor authentication | MaxLen: 128


@final
class PeerObject:
    """Typed FortiObject for user/peer with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Peer name. | MaxLen: 35
    name: str
    # Determine what happens to the peer if the CA certificate is | Default: enable
    mandatory_ca_verify: Literal["enable", "disable"]
    # Name of the CA certificate. | MaxLen: 127
    ca: str
    # Peer certificate name constraints. | MaxLen: 255
    subject: str
    # Peer certificate common name. | MaxLen: 255
    cn: str
    # Peer certificate common name type. | Default: string
    cn_type: Literal["string", "email", "FQDN", "ipv4", "ipv6"]
    # MFA mode for remote peer authentication/authorization. | Default: none
    mfa_mode: Literal["none", "password", "subject-identity"]
    # Name of a remote authenticator. Performs client access right | MaxLen: 35
    mfa_server: str
    # Unified username for remote authentication. | MaxLen: 35
    mfa_username: str
    # Unified password for remote authentication. This field may b | MaxLen: 128
    mfa_password: str
    # Online Certificate Status Protocol (OCSP) server for certifi | MaxLen: 35
    ocsp_override_server: str
    # Enable/disable two-factor authentication, applying certifica | Default: disable
    two_factor: Literal["enable", "disable"]
    # Peer's password used for two-factor authentication. | MaxLen: 128
    passwd: str
    
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
    def to_dict(self) -> PeerPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Peer:
    """
    Configure peer users.
    
    Path: user/peer
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
    ) -> PeerObject: ...
    
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
    ) -> PeerObject: ...
    
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
    ) -> FortiObjectList[PeerObject]: ...
    
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
    ) -> PeerObject: ...
    
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
    ) -> PeerObject: ...
    
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
    ) -> FortiObjectList[PeerObject]: ...
    
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
    ) -> PeerObject: ...
    
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
    ) -> PeerObject: ...
    
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
    ) -> FortiObjectList[PeerObject]: ...
    
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
    ) -> PeerObject | list[PeerObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: PeerPayload | None = ...,
        name: str | None = ...,
        mandatory_ca_verify: Literal["enable", "disable"] | None = ...,
        ca: str | None = ...,
        subject: str | None = ...,
        cn: str | None = ...,
        cn_type: Literal["string", "email", "FQDN", "ipv4", "ipv6"] | None = ...,
        mfa_mode: Literal["none", "password", "subject-identity"] | None = ...,
        mfa_server: str | None = ...,
        mfa_username: str | None = ...,
        mfa_password: str | None = ...,
        ocsp_override_server: str | None = ...,
        two_factor: Literal["enable", "disable"] | None = ...,
        passwd: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> PeerObject: ...
    
    @overload
    def post(
        self,
        payload_dict: PeerPayload | None = ...,
        name: str | None = ...,
        mandatory_ca_verify: Literal["enable", "disable"] | None = ...,
        ca: str | None = ...,
        subject: str | None = ...,
        cn: str | None = ...,
        cn_type: Literal["string", "email", "FQDN", "ipv4", "ipv6"] | None = ...,
        mfa_mode: Literal["none", "password", "subject-identity"] | None = ...,
        mfa_server: str | None = ...,
        mfa_username: str | None = ...,
        mfa_password: str | None = ...,
        ocsp_override_server: str | None = ...,
        two_factor: Literal["enable", "disable"] | None = ...,
        passwd: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: PeerPayload | None = ...,
        name: str | None = ...,
        mandatory_ca_verify: Literal["enable", "disable"] | None = ...,
        ca: str | None = ...,
        subject: str | None = ...,
        cn: str | None = ...,
        cn_type: Literal["string", "email", "FQDN", "ipv4", "ipv6"] | None = ...,
        mfa_mode: Literal["none", "password", "subject-identity"] | None = ...,
        mfa_server: str | None = ...,
        mfa_username: str | None = ...,
        mfa_password: str | None = ...,
        ocsp_override_server: str | None = ...,
        two_factor: Literal["enable", "disable"] | None = ...,
        passwd: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def post(
        self,
        payload_dict: PeerPayload | None = ...,
        name: str | None = ...,
        mandatory_ca_verify: Literal["enable", "disable"] | None = ...,
        ca: str | None = ...,
        subject: str | None = ...,
        cn: str | None = ...,
        cn_type: Literal["string", "email", "FQDN", "ipv4", "ipv6"] | None = ...,
        mfa_mode: Literal["none", "password", "subject-identity"] | None = ...,
        mfa_server: str | None = ...,
        mfa_username: str | None = ...,
        mfa_password: str | None = ...,
        ocsp_override_server: str | None = ...,
        two_factor: Literal["enable", "disable"] | None = ...,
        passwd: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: PeerPayload | None = ...,
        name: str | None = ...,
        mandatory_ca_verify: Literal["enable", "disable"] | None = ...,
        ca: str | None = ...,
        subject: str | None = ...,
        cn: str | None = ...,
        cn_type: Literal["string", "email", "FQDN", "ipv4", "ipv6"] | None = ...,
        mfa_mode: Literal["none", "password", "subject-identity"] | None = ...,
        mfa_server: str | None = ...,
        mfa_username: str | None = ...,
        mfa_password: str | None = ...,
        ocsp_override_server: str | None = ...,
        two_factor: Literal["enable", "disable"] | None = ...,
        passwd: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> PeerObject: ...
    
    @overload
    def put(
        self,
        payload_dict: PeerPayload | None = ...,
        name: str | None = ...,
        mandatory_ca_verify: Literal["enable", "disable"] | None = ...,
        ca: str | None = ...,
        subject: str | None = ...,
        cn: str | None = ...,
        cn_type: Literal["string", "email", "FQDN", "ipv4", "ipv6"] | None = ...,
        mfa_mode: Literal["none", "password", "subject-identity"] | None = ...,
        mfa_server: str | None = ...,
        mfa_username: str | None = ...,
        mfa_password: str | None = ...,
        ocsp_override_server: str | None = ...,
        two_factor: Literal["enable", "disable"] | None = ...,
        passwd: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: PeerPayload | None = ...,
        name: str | None = ...,
        mandatory_ca_verify: Literal["enable", "disable"] | None = ...,
        ca: str | None = ...,
        subject: str | None = ...,
        cn: str | None = ...,
        cn_type: Literal["string", "email", "FQDN", "ipv4", "ipv6"] | None = ...,
        mfa_mode: Literal["none", "password", "subject-identity"] | None = ...,
        mfa_server: str | None = ...,
        mfa_username: str | None = ...,
        mfa_password: str | None = ...,
        ocsp_override_server: str | None = ...,
        two_factor: Literal["enable", "disable"] | None = ...,
        passwd: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def put(
        self,
        payload_dict: PeerPayload | None = ...,
        name: str | None = ...,
        mandatory_ca_verify: Literal["enable", "disable"] | None = ...,
        ca: str | None = ...,
        subject: str | None = ...,
        cn: str | None = ...,
        cn_type: Literal["string", "email", "FQDN", "ipv4", "ipv6"] | None = ...,
        mfa_mode: Literal["none", "password", "subject-identity"] | None = ...,
        mfa_server: str | None = ...,
        mfa_username: str | None = ...,
        mfa_password: str | None = ...,
        ocsp_override_server: str | None = ...,
        two_factor: Literal["enable", "disable"] | None = ...,
        passwd: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> PeerObject: ...
    
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
        payload_dict: PeerPayload | None = ...,
        name: str | None = ...,
        mandatory_ca_verify: Literal["enable", "disable"] | None = ...,
        ca: str | None = ...,
        subject: str | None = ...,
        cn: str | None = ...,
        cn_type: Literal["string", "email", "FQDN", "ipv4", "ipv6"] | None = ...,
        mfa_mode: Literal["none", "password", "subject-identity"] | None = ...,
        mfa_server: str | None = ...,
        mfa_username: str | None = ...,
        mfa_password: str | None = ...,
        ocsp_override_server: str | None = ...,
        two_factor: Literal["enable", "disable"] | None = ...,
        passwd: str | None = ...,
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
    "Peer",
    "PeerPayload",
    "PeerResponse",
    "PeerObject",
]