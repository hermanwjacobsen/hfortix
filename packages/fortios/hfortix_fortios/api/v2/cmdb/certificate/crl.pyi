from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject
from hfortix_core.types import MutationResponse, RawAPIResponse

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class CrlPayload(TypedDict, total=False):
    """
    Type hints for certificate/crl payload fields.
    
    Certificate Revocation List as a PEM file.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.certificate.local.LocalEndpoint` (via: scep-cert)
        - :class:`~.system.vdom.VdomEndpoint` (via: update-vdom)

    **Usage:**
        payload: CrlPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # Name. | MaxLen: 35
    crl: str  # Certificate Revocation List as a PEM file.
    range: Literal["global", "vdom"]  # Either global or VDOM IP address range for the cer | Default: global
    source: Literal["factory", "user", "bundle"]  # Certificate source type. | Default: user
    update_vdom: str  # VDOM for CRL update. | Default: root | MaxLen: 31
    ldap_server: str  # LDAP server name for CRL auto-update. | MaxLen: 35
    ldap_username: str  # LDAP server user name. | MaxLen: 63
    ldap_password: str  # LDAP server user password. | MaxLen: 128
    http_url: str  # HTTP server URL for CRL auto-update. | MaxLen: 255
    scep_url: str  # SCEP server URL for CRL auto-update. | MaxLen: 255
    scep_cert: str  # Local certificate for SCEP communication for CRL a | Default: Fortinet_CA_SSL | MaxLen: 35
    update_interval: int  # Time in seconds before the FortiGate checks for an | Default: 0 | Min: 0 | Max: 4294967295
    source_ip: str  # Source IP address for communications to a HTTP or | Default: 0.0.0.0

# Nested TypedDicts for table field children (dict mode)

# Nested classes for table field children (object mode)


# Response TypedDict for GET returns (all fields present in API response)
class CrlResponse(TypedDict):
    """
    Type hints for certificate/crl API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str  # Name. | MaxLen: 35
    crl: str  # Certificate Revocation List as a PEM file.
    range: Literal["global", "vdom"]  # Either global or VDOM IP address range for the cer | Default: global
    source: Literal["factory", "user", "bundle"]  # Certificate source type. | Default: user
    update_vdom: str  # VDOM for CRL update. | Default: root | MaxLen: 31
    ldap_server: str  # LDAP server name for CRL auto-update. | MaxLen: 35
    ldap_username: str  # LDAP server user name. | MaxLen: 63
    ldap_password: str  # LDAP server user password. | MaxLen: 128
    http_url: str  # HTTP server URL for CRL auto-update. | MaxLen: 255
    scep_url: str  # SCEP server URL for CRL auto-update. | MaxLen: 255
    scep_cert: str  # Local certificate for SCEP communication for CRL a | Default: Fortinet_CA_SSL | MaxLen: 35
    update_interval: int  # Time in seconds before the FortiGate checks for an | Default: 0 | Min: 0 | Max: 4294967295
    source_ip: str  # Source IP address for communications to a HTTP or | Default: 0.0.0.0


@final
class CrlObject:
    """Typed FortiObject for certificate/crl with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Name. | MaxLen: 35
    name: str
    # Certificate Revocation List as a PEM file.
    crl: str
    # Either global or VDOM IP address range for the certificate. | Default: global
    range: Literal["global", "vdom"]
    # Certificate source type. | Default: user
    source: Literal["factory", "user", "bundle"]
    # VDOM for CRL update. | Default: root | MaxLen: 31
    update_vdom: str
    # LDAP server name for CRL auto-update. | MaxLen: 35
    ldap_server: str
    # LDAP server user name. | MaxLen: 63
    ldap_username: str
    # LDAP server user password. | MaxLen: 128
    ldap_password: str
    # HTTP server URL for CRL auto-update. | MaxLen: 255
    http_url: str
    # SCEP server URL for CRL auto-update. | MaxLen: 255
    scep_url: str
    # Local certificate for SCEP communication for CRL auto-update | Default: Fortinet_CA_SSL | MaxLen: 35
    scep_cert: str
    # Time in seconds before the FortiGate checks for an updated C | Default: 0 | Min: 0 | Max: 4294967295
    update_interval: int
    # Source IP address for communications to a HTTP or SCEP CA se | Default: 0.0.0.0
    source_ip: str
    
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
    def to_dict(self) -> CrlPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Crl:
    """
    Certificate Revocation List as a PEM file.
    
    Path: certificate/crl
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
    ) -> CrlObject: ...
    
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
    ) -> CrlObject: ...
    
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
    ) -> list[CrlObject]: ...
    
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
    ) -> CrlObject: ...
    
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
    ) -> CrlObject: ...
    
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
    ) -> list[CrlObject]: ...
    
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
    ) -> CrlObject: ...
    
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
    ) -> CrlObject: ...
    
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
    ) -> list[CrlObject]: ...
    
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
    ) -> CrlObject | list[CrlObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: CrlPayload | None = ...,
        name: str | None = ...,
        crl: str | None = ...,
        range: Literal["global", "vdom"] | None = ...,
        source: Literal["factory", "user", "bundle"] | None = ...,
        update_vdom: str | None = ...,
        ldap_server: str | None = ...,
        ldap_username: str | None = ...,
        ldap_password: str | None = ...,
        http_url: str | None = ...,
        scep_url: str | None = ...,
        scep_cert: str | None = ...,
        update_interval: int | None = ...,
        source_ip: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> CrlObject: ...
    
    @overload
    def put(
        self,
        payload_dict: CrlPayload | None = ...,
        name: str | None = ...,
        crl: str | None = ...,
        range: Literal["global", "vdom"] | None = ...,
        source: Literal["factory", "user", "bundle"] | None = ...,
        update_vdom: str | None = ...,
        ldap_server: str | None = ...,
        ldap_username: str | None = ...,
        ldap_password: str | None = ...,
        http_url: str | None = ...,
        scep_url: str | None = ...,
        scep_cert: str | None = ...,
        update_interval: int | None = ...,
        source_ip: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    # raw_json=True returns the full API envelope
    @overload
    def put(
        self,
        payload_dict: CrlPayload | None = ...,
        name: str | None = ...,
        crl: str | None = ...,
        range: Literal["global", "vdom"] | None = ...,
        source: Literal["factory", "user", "bundle"] | None = ...,
        update_vdom: str | None = ...,
        ldap_server: str | None = ...,
        ldap_username: str | None = ...,
        ldap_password: str | None = ...,
        http_url: str | None = ...,
        scep_url: str | None = ...,
        scep_cert: str | None = ...,
        update_interval: int | None = ...,
        source_ip: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> RawAPIResponse: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: CrlPayload | None = ...,
        name: str | None = ...,
        crl: str | None = ...,
        range: Literal["global", "vdom"] | None = ...,
        source: Literal["factory", "user", "bundle"] | None = ...,
        update_vdom: str | None = ...,
        ldap_server: str | None = ...,
        ldap_username: str | None = ...,
        ldap_password: str | None = ...,
        http_url: str | None = ...,
        scep_url: str | None = ...,
        scep_cert: str | None = ...,
        update_interval: int | None = ...,
        source_ip: str | None = ...,
        vdom: str | bool | None = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    def put(
        self,
        payload_dict: CrlPayload | None = ...,
        name: str | None = ...,
        crl: str | None = ...,
        range: Literal["global", "vdom"] | None = ...,
        source: Literal["factory", "user", "bundle"] | None = ...,
        update_vdom: str | None = ...,
        ldap_server: str | None = ...,
        ldap_username: str | None = ...,
        ldap_password: str | None = ...,
        http_url: str | None = ...,
        scep_url: str | None = ...,
        scep_cert: str | None = ...,
        update_interval: int | None = ...,
        source_ip: str | None = ...,
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
        payload_dict: CrlPayload | None = ...,
        name: str | None = ...,
        crl: str | None = ...,
        range: Literal["global", "vdom"] | None = ...,
        source: Literal["factory", "user", "bundle"] | None = ...,
        update_vdom: str | None = ...,
        ldap_server: str | None = ...,
        ldap_username: str | None = ...,
        ldap_password: str | None = ...,
        http_url: str | None = ...,
        scep_url: str | None = ...,
        scep_cert: str | None = ...,
        update_interval: int | None = ...,
        source_ip: str | None = ...,
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
    "Crl",
    "CrlPayload",
    "CrlResponse",
    "CrlObject",
]