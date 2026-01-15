from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class FssoPollingPayload(TypedDict, total=False):
    """
    Type hints for user/fsso_polling payload fields.
    
    Configure FSSO active directory servers for polling mode.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.user.ldap.LdapEndpoint` (via: ldap-server)

    **Usage:**
        payload: FssoPollingPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    id: int  # Active Directory server ID. | Default: 0 | Min: 0 | Max: 4294967295
    status: Literal["enable", "disable"]  # Enable/disable polling for the status of this Acti | Default: enable
    server: str  # Host name or IP address of the Active Directory se | MaxLen: 63
    default_domain: str  # Default domain managed by this Active Directory se | MaxLen: 35
    port: int  # Port to communicate with this Active Directory ser | Default: 0 | Min: 0 | Max: 65535
    user: str  # User name required to log into this Active Directo | MaxLen: 35
    password: str  # Password required to log into this Active Director | MaxLen: 128
    ldap_server: str  # LDAP server name used in LDAP connection strings. | MaxLen: 35
    logon_history: int  # Number of hours of logon history to keep, 0 means | Default: 8 | Min: 0 | Max: 48
    polling_frequency: int  # Polling frequency (every 1 to 30 seconds). | Default: 10 | Min: 1 | Max: 30
    adgrp: list[dict[str, Any]]  # LDAP Group Info.
    smbv1: Literal["enable", "disable"]  # Enable/disable support of SMBv1 for Samba. | Default: disable
    smb_ntlmv1_auth: Literal["enable", "disable"]  # Enable/disable support of NTLMv1 for Samba authent | Default: disable

# Nested TypedDicts for table field children (dict mode)

class FssoPollingAdgrpItem(TypedDict):
    """Type hints for adgrp table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # Name. | MaxLen: 511


# Nested classes for table field children (object mode)

@final
class FssoPollingAdgrpObject:
    """Typed object for adgrp table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Name. | MaxLen: 511
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
class FssoPollingResponse(TypedDict):
    """
    Type hints for user/fsso_polling API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    id: int  # Active Directory server ID. | Default: 0 | Min: 0 | Max: 4294967295
    status: Literal["enable", "disable"]  # Enable/disable polling for the status of this Acti | Default: enable
    server: str  # Host name or IP address of the Active Directory se | MaxLen: 63
    default_domain: str  # Default domain managed by this Active Directory se | MaxLen: 35
    port: int  # Port to communicate with this Active Directory ser | Default: 0 | Min: 0 | Max: 65535
    user: str  # User name required to log into this Active Directo | MaxLen: 35
    password: str  # Password required to log into this Active Director | MaxLen: 128
    ldap_server: str  # LDAP server name used in LDAP connection strings. | MaxLen: 35
    logon_history: int  # Number of hours of logon history to keep, 0 means | Default: 8 | Min: 0 | Max: 48
    polling_frequency: int  # Polling frequency (every 1 to 30 seconds). | Default: 10 | Min: 1 | Max: 30
    adgrp: list[FssoPollingAdgrpItem]  # LDAP Group Info.
    smbv1: Literal["enable", "disable"]  # Enable/disable support of SMBv1 for Samba. | Default: disable
    smb_ntlmv1_auth: Literal["enable", "disable"]  # Enable/disable support of NTLMv1 for Samba authent | Default: disable


@final
class FssoPollingObject:
    """Typed FortiObject for user/fsso_polling with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Active Directory server ID. | Default: 0 | Min: 0 | Max: 4294967295
    id: int
    # Enable/disable polling for the status of this Active Directo | Default: enable
    status: Literal["enable", "disable"]
    # Host name or IP address of the Active Directory server. | MaxLen: 63
    server: str
    # Default domain managed by this Active Directory server. | MaxLen: 35
    default_domain: str
    # Port to communicate with this Active Directory server. | Default: 0 | Min: 0 | Max: 65535
    port: int
    # User name required to log into this Active Directory server. | MaxLen: 35
    user: str
    # Password required to log into this Active Directory server. | MaxLen: 128
    password: str
    # LDAP server name used in LDAP connection strings. | MaxLen: 35
    ldap_server: str
    # Number of hours of logon history to keep, 0 means keep all h | Default: 8 | Min: 0 | Max: 48
    logon_history: int
    # Polling frequency (every 1 to 30 seconds). | Default: 10 | Min: 1 | Max: 30
    polling_frequency: int
    # LDAP Group Info.
    adgrp: list[FssoPollingAdgrpObject]
    # Enable/disable support of SMBv1 for Samba. | Default: disable
    smbv1: Literal["enable", "disable"]
    # Enable/disable support of NTLMv1 for Samba authentication. | Default: disable
    smb_ntlmv1_auth: Literal["enable", "disable"]
    
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
    def to_dict(self) -> FssoPollingPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class FssoPolling:
    """
    Configure FSSO active directory servers for polling mode.
    
    Path: user/fsso_polling
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
    ) -> FssoPollingObject: ...
    
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
    ) -> FssoPollingObject: ...
    
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
    ) -> FortiObjectList[FssoPollingObject]: ...
    
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
    ) -> FssoPollingObject: ...
    
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
    ) -> FssoPollingObject: ...
    
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
    ) -> FortiObjectList[FssoPollingObject]: ...
    
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
    ) -> FssoPollingObject: ...
    
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
    ) -> FssoPollingObject: ...
    
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
    ) -> FortiObjectList[FssoPollingObject]: ...
    
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
    ) -> FssoPollingObject | list[FssoPollingObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: FssoPollingPayload | None = ...,
        id: int | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        server: str | None = ...,
        default_domain: str | None = ...,
        port: int | None = ...,
        user: str | None = ...,
        password: str | None = ...,
        ldap_server: str | None = ...,
        logon_history: int | None = ...,
        polling_frequency: int | None = ...,
        adgrp: str | list[str] | list[dict[str, Any]] | None = ...,
        smbv1: Literal["enable", "disable"] | None = ...,
        smb_ntlmv1_auth: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FssoPollingObject: ...
    
    @overload
    def post(
        self,
        payload_dict: FssoPollingPayload | None = ...,
        id: int | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        server: str | None = ...,
        default_domain: str | None = ...,
        port: int | None = ...,
        user: str | None = ...,
        password: str | None = ...,
        ldap_server: str | None = ...,
        logon_history: int | None = ...,
        polling_frequency: int | None = ...,
        adgrp: str | list[str] | list[dict[str, Any]] | None = ...,
        smbv1: Literal["enable", "disable"] | None = ...,
        smb_ntlmv1_auth: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: FssoPollingPayload | None = ...,
        id: int | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        server: str | None = ...,
        default_domain: str | None = ...,
        port: int | None = ...,
        user: str | None = ...,
        password: str | None = ...,
        ldap_server: str | None = ...,
        logon_history: int | None = ...,
        polling_frequency: int | None = ...,
        adgrp: str | list[str] | list[dict[str, Any]] | None = ...,
        smbv1: Literal["enable", "disable"] | None = ...,
        smb_ntlmv1_auth: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def post(
        self,
        payload_dict: FssoPollingPayload | None = ...,
        id: int | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        server: str | None = ...,
        default_domain: str | None = ...,
        port: int | None = ...,
        user: str | None = ...,
        password: str | None = ...,
        ldap_server: str | None = ...,
        logon_history: int | None = ...,
        polling_frequency: int | None = ...,
        adgrp: str | list[str] | list[dict[str, Any]] | None = ...,
        smbv1: Literal["enable", "disable"] | None = ...,
        smb_ntlmv1_auth: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: FssoPollingPayload | None = ...,
        id: int | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        server: str | None = ...,
        default_domain: str | None = ...,
        port: int | None = ...,
        user: str | None = ...,
        password: str | None = ...,
        ldap_server: str | None = ...,
        logon_history: int | None = ...,
        polling_frequency: int | None = ...,
        adgrp: str | list[str] | list[dict[str, Any]] | None = ...,
        smbv1: Literal["enable", "disable"] | None = ...,
        smb_ntlmv1_auth: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FssoPollingObject: ...
    
    @overload
    def put(
        self,
        payload_dict: FssoPollingPayload | None = ...,
        id: int | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        server: str | None = ...,
        default_domain: str | None = ...,
        port: int | None = ...,
        user: str | None = ...,
        password: str | None = ...,
        ldap_server: str | None = ...,
        logon_history: int | None = ...,
        polling_frequency: int | None = ...,
        adgrp: str | list[str] | list[dict[str, Any]] | None = ...,
        smbv1: Literal["enable", "disable"] | None = ...,
        smb_ntlmv1_auth: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: FssoPollingPayload | None = ...,
        id: int | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        server: str | None = ...,
        default_domain: str | None = ...,
        port: int | None = ...,
        user: str | None = ...,
        password: str | None = ...,
        ldap_server: str | None = ...,
        logon_history: int | None = ...,
        polling_frequency: int | None = ...,
        adgrp: str | list[str] | list[dict[str, Any]] | None = ...,
        smbv1: Literal["enable", "disable"] | None = ...,
        smb_ntlmv1_auth: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def put(
        self,
        payload_dict: FssoPollingPayload | None = ...,
        id: int | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        server: str | None = ...,
        default_domain: str | None = ...,
        port: int | None = ...,
        user: str | None = ...,
        password: str | None = ...,
        ldap_server: str | None = ...,
        logon_history: int | None = ...,
        polling_frequency: int | None = ...,
        adgrp: str | list[str] | list[dict[str, Any]] | None = ...,
        smbv1: Literal["enable", "disable"] | None = ...,
        smb_ntlmv1_auth: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        id: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> FssoPollingObject: ...
    
    @overload
    def delete(
        self,
        id: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def delete(
        self,
        id: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def delete(
        self,
        id: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def exists(
        self,
        id: int,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: FssoPollingPayload | None = ...,
        id: int | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        server: str | None = ...,
        default_domain: str | None = ...,
        port: int | None = ...,
        user: str | None = ...,
        password: str | None = ...,
        ldap_server: str | None = ...,
        logon_history: int | None = ...,
        polling_frequency: int | None = ...,
        adgrp: str | list[str] | list[dict[str, Any]] | None = ...,
        smbv1: Literal["enable", "disable"] | None = ...,
        smb_ntlmv1_auth: Literal["enable", "disable"] | None = ...,
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
    "FssoPolling",
    "FssoPollingPayload",
    "FssoPollingResponse",
    "FssoPollingObject",
]