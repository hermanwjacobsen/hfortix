from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject
from hfortix_core.types import MutationResponse, RawAPIResponse

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class KrbKeytabPayload(TypedDict, total=False):
    """
    Type hints for user/krb_keytab payload fields.
    
    Configure Kerberos keytab entries.
    
    **Usage:**
        payload: KrbKeytabPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # Kerberos keytab entry name. | MaxLen: 35
    pac_data: Literal["enable", "disable"]  # Enable/disable parsing PAC data in the ticket. | Default: enable
    principal: str  # Kerberos service principal. For example, HTTP/myfg | MaxLen: 511
    ldap_server: list[dict[str, Any]]  # LDAP server name(s).
    keytab: str  # Base64 coded keytab file containing a pre-shared k | MaxLen: 8191

# Nested TypedDicts for table field children (dict mode)

class KrbKeytabLdapserverItem(TypedDict):
    """Type hints for ldap-server table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # LDAP server name. | MaxLen: 79


# Nested classes for table field children (object mode)

@final
class KrbKeytabLdapserverObject:
    """Typed object for ldap-server table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # LDAP server name. | MaxLen: 79
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
class KrbKeytabResponse(TypedDict):
    """
    Type hints for user/krb_keytab API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str  # Kerberos keytab entry name. | MaxLen: 35
    pac_data: Literal["enable", "disable"]  # Enable/disable parsing PAC data in the ticket. | Default: enable
    principal: str  # Kerberos service principal. For example, HTTP/myfg | MaxLen: 511
    ldap_server: list[KrbKeytabLdapserverItem]  # LDAP server name(s).
    keytab: str  # Base64 coded keytab file containing a pre-shared k | MaxLen: 8191


@final
class KrbKeytabObject:
    """Typed FortiObject for user/krb_keytab with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Kerberos keytab entry name. | MaxLen: 35
    name: str
    # Enable/disable parsing PAC data in the ticket. | Default: enable
    pac_data: Literal["enable", "disable"]
    # Kerberos service principal. For example, HTTP/myfgt.example. | MaxLen: 511
    principal: str
    # LDAP server name(s).
    ldap_server: list[KrbKeytabLdapserverObject]
    # Base64 coded keytab file containing a pre-shared key. | MaxLen: 8191
    keytab: str
    
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
    def to_dict(self) -> KrbKeytabPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class KrbKeytab:
    """
    Configure Kerberos keytab entries.
    
    Path: user/krb_keytab
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
    ) -> KrbKeytabObject: ...
    
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
    ) -> KrbKeytabObject: ...
    
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
    ) -> list[KrbKeytabObject]: ...
    
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
    ) -> KrbKeytabObject: ...
    
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
    ) -> KrbKeytabObject: ...
    
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
    ) -> list[KrbKeytabObject]: ...
    
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
    ) -> KrbKeytabObject: ...
    
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
    ) -> KrbKeytabObject: ...
    
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
    ) -> list[KrbKeytabObject]: ...
    
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
    ) -> KrbKeytabObject | list[KrbKeytabObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: KrbKeytabPayload | None = ...,
        name: str | None = ...,
        pac_data: Literal["enable", "disable"] | None = ...,
        principal: str | None = ...,
        ldap_server: str | list[str] | list[dict[str, Any]] | None = ...,
        keytab: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> KrbKeytabObject: ...
    
    @overload
    def post(
        self,
        payload_dict: KrbKeytabPayload | None = ...,
        name: str | None = ...,
        pac_data: Literal["enable", "disable"] | None = ...,
        principal: str | None = ...,
        ldap_server: str | list[str] | list[dict[str, Any]] | None = ...,
        keytab: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    # raw_json=True returns the full API envelope
    @overload
    def post(
        self,
        payload_dict: KrbKeytabPayload | None = ...,
        name: str | None = ...,
        pac_data: Literal["enable", "disable"] | None = ...,
        principal: str | None = ...,
        ldap_server: str | list[str] | list[dict[str, Any]] | None = ...,
        keytab: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> RawAPIResponse: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: KrbKeytabPayload | None = ...,
        name: str | None = ...,
        pac_data: Literal["enable", "disable"] | None = ...,
        principal: str | None = ...,
        ldap_server: str | list[str] | list[dict[str, Any]] | None = ...,
        keytab: str | None = ...,
        vdom: str | bool | None = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    def post(
        self,
        payload_dict: KrbKeytabPayload | None = ...,
        name: str | None = ...,
        pac_data: Literal["enable", "disable"] | None = ...,
        principal: str | None = ...,
        ldap_server: str | list[str] | list[dict[str, Any]] | None = ...,
        keytab: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: KrbKeytabPayload | None = ...,
        name: str | None = ...,
        pac_data: Literal["enable", "disable"] | None = ...,
        principal: str | None = ...,
        ldap_server: str | list[str] | list[dict[str, Any]] | None = ...,
        keytab: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> KrbKeytabObject: ...
    
    @overload
    def put(
        self,
        payload_dict: KrbKeytabPayload | None = ...,
        name: str | None = ...,
        pac_data: Literal["enable", "disable"] | None = ...,
        principal: str | None = ...,
        ldap_server: str | list[str] | list[dict[str, Any]] | None = ...,
        keytab: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    # raw_json=True returns the full API envelope
    @overload
    def put(
        self,
        payload_dict: KrbKeytabPayload | None = ...,
        name: str | None = ...,
        pac_data: Literal["enable", "disable"] | None = ...,
        principal: str | None = ...,
        ldap_server: str | list[str] | list[dict[str, Any]] | None = ...,
        keytab: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> RawAPIResponse: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: KrbKeytabPayload | None = ...,
        name: str | None = ...,
        pac_data: Literal["enable", "disable"] | None = ...,
        principal: str | None = ...,
        ldap_server: str | list[str] | list[dict[str, Any]] | None = ...,
        keytab: str | None = ...,
        vdom: str | bool | None = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    def put(
        self,
        payload_dict: KrbKeytabPayload | None = ...,
        name: str | None = ...,
        pac_data: Literal["enable", "disable"] | None = ...,
        principal: str | None = ...,
        ldap_server: str | list[str] | list[dict[str, Any]] | None = ...,
        keytab: str | None = ...,
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
    ) -> KrbKeytabObject: ...
    
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
        payload_dict: KrbKeytabPayload | None = ...,
        name: str | None = ...,
        pac_data: Literal["enable", "disable"] | None = ...,
        principal: str | None = ...,
        ldap_server: str | list[str] | list[dict[str, Any]] | None = ...,
        keytab: str | None = ...,
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
    "KrbKeytab",
    "KrbKeytabPayload",
    "KrbKeytabResponse",
    "KrbKeytabObject",
]