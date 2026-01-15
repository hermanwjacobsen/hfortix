from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList
from hfortix_core.types import MutationResponse

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class HostKeyPayload(TypedDict, total=False):
    """
    Type hints for firewall/ssh/host_key payload fields.
    
    SSH proxy host public keys.
    
    **Usage:**
        payload: HostKeyPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # SSH public key name. | MaxLen: 35
    status: Literal["trusted", "revoked"]  # Set the trust status of the public key. | Default: trusted
    type: Literal["RSA", "DSA", "ECDSA", "ED25519", "RSA-CA", "DSA-CA", "ECDSA-CA", "ED25519-CA"]  # Set the type of the public key. | Default: RSA
    nid: Literal["256", "384", "521"]  # Set the nid of the ECDSA key. | Default: 256
    usage: Literal["transparent-proxy", "access-proxy"]  # Usage for this public key. | Default: transparent-proxy
    ip: str  # IP address of the SSH server. | Default: 0.0.0.0
    port: int  # Port of the SSH server. | Default: 22 | Min: 0 | Max: 4294967295
    hostname: str  # Hostname of the SSH server to match SSH certificat | MaxLen: 255
    public_key: str  # SSH public key. | MaxLen: 32768

# Nested TypedDicts for table field children (dict mode)

# Nested classes for table field children (object mode)


# Response TypedDict for GET returns (all fields present in API response)
class HostKeyResponse(TypedDict):
    """
    Type hints for firewall/ssh/host_key API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str  # SSH public key name. | MaxLen: 35
    status: Literal["trusted", "revoked"]  # Set the trust status of the public key. | Default: trusted
    type: Literal["RSA", "DSA", "ECDSA", "ED25519", "RSA-CA", "DSA-CA", "ECDSA-CA", "ED25519-CA"]  # Set the type of the public key. | Default: RSA
    nid: Literal["256", "384", "521"]  # Set the nid of the ECDSA key. | Default: 256
    usage: Literal["transparent-proxy", "access-proxy"]  # Usage for this public key. | Default: transparent-proxy
    ip: str  # IP address of the SSH server. | Default: 0.0.0.0
    port: int  # Port of the SSH server. | Default: 22 | Min: 0 | Max: 4294967295
    hostname: str  # Hostname of the SSH server to match SSH certificat | MaxLen: 255
    public_key: str  # SSH public key. | MaxLen: 32768


@final
class HostKeyObject:
    """Typed FortiObject for firewall/ssh/host_key with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # SSH public key name. | MaxLen: 35
    name: str
    # Set the trust status of the public key. | Default: trusted
    status: Literal["trusted", "revoked"]
    # Set the type of the public key. | Default: RSA
    type: Literal["RSA", "DSA", "ECDSA", "ED25519", "RSA-CA", "DSA-CA", "ECDSA-CA", "ED25519-CA"]
    # Set the nid of the ECDSA key. | Default: 256
    nid: Literal["256", "384", "521"]
    # Usage for this public key. | Default: transparent-proxy
    usage: Literal["transparent-proxy", "access-proxy"]
    # IP address of the SSH server. | Default: 0.0.0.0
    ip: str
    # Port of the SSH server. | Default: 22 | Min: 0 | Max: 4294967295
    port: int
    # Hostname of the SSH server to match SSH certificate principa | MaxLen: 255
    hostname: str
    # SSH public key. | MaxLen: 32768
    public_key: str
    
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
    def to_dict(self) -> HostKeyPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class HostKey:
    """
    SSH proxy host public keys.
    
    Path: firewall/ssh/host_key
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
    ) -> HostKeyObject: ...
    
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
    ) -> HostKeyObject: ...
    
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
    ) -> FortiObjectList[HostKeyObject]: ...
    
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
    ) -> HostKeyObject: ...
    
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
    ) -> HostKeyObject: ...
    
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
    ) -> FortiObjectList[HostKeyObject]: ...
    
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
    ) -> HostKeyObject: ...
    
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
    ) -> HostKeyObject: ...
    
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
    ) -> FortiObjectList[HostKeyObject]: ...
    
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
    ) -> HostKeyObject | list[HostKeyObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: HostKeyPayload | None = ...,
        name: str | None = ...,
        status: Literal["trusted", "revoked"] | None = ...,
        type: Literal["RSA", "DSA", "ECDSA", "ED25519", "RSA-CA", "DSA-CA", "ECDSA-CA", "ED25519-CA"] | None = ...,
        nid: Literal["256", "384", "521"] | None = ...,
        usage: Literal["transparent-proxy", "access-proxy"] | None = ...,
        ip: str | None = ...,
        port: int | None = ...,
        hostname: str | None = ...,
        public_key: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> HostKeyObject: ...
    
    @overload
    def post(
        self,
        payload_dict: HostKeyPayload | None = ...,
        name: str | None = ...,
        status: Literal["trusted", "revoked"] | None = ...,
        type: Literal["RSA", "DSA", "ECDSA", "ED25519", "RSA-CA", "DSA-CA", "ECDSA-CA", "ED25519-CA"] | None = ...,
        nid: Literal["256", "384", "521"] | None = ...,
        usage: Literal["transparent-proxy", "access-proxy"] | None = ...,
        ip: str | None = ...,
        port: int | None = ...,
        hostname: str | None = ...,
        public_key: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: HostKeyPayload | None = ...,
        name: str | None = ...,
        status: Literal["trusted", "revoked"] | None = ...,
        type: Literal["RSA", "DSA", "ECDSA", "ED25519", "RSA-CA", "DSA-CA", "ECDSA-CA", "ED25519-CA"] | None = ...,
        nid: Literal["256", "384", "521"] | None = ...,
        usage: Literal["transparent-proxy", "access-proxy"] | None = ...,
        ip: str | None = ...,
        port: int | None = ...,
        hostname: str | None = ...,
        public_key: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def post(
        self,
        payload_dict: HostKeyPayload | None = ...,
        name: str | None = ...,
        status: Literal["trusted", "revoked"] | None = ...,
        type: Literal["RSA", "DSA", "ECDSA", "ED25519", "RSA-CA", "DSA-CA", "ECDSA-CA", "ED25519-CA"] | None = ...,
        nid: Literal["256", "384", "521"] | None = ...,
        usage: Literal["transparent-proxy", "access-proxy"] | None = ...,
        ip: str | None = ...,
        port: int | None = ...,
        hostname: str | None = ...,
        public_key: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: HostKeyPayload | None = ...,
        name: str | None = ...,
        status: Literal["trusted", "revoked"] | None = ...,
        type: Literal["RSA", "DSA", "ECDSA", "ED25519", "RSA-CA", "DSA-CA", "ECDSA-CA", "ED25519-CA"] | None = ...,
        nid: Literal["256", "384", "521"] | None = ...,
        usage: Literal["transparent-proxy", "access-proxy"] | None = ...,
        ip: str | None = ...,
        port: int | None = ...,
        hostname: str | None = ...,
        public_key: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> HostKeyObject: ...
    
    @overload
    def put(
        self,
        payload_dict: HostKeyPayload | None = ...,
        name: str | None = ...,
        status: Literal["trusted", "revoked"] | None = ...,
        type: Literal["RSA", "DSA", "ECDSA", "ED25519", "RSA-CA", "DSA-CA", "ECDSA-CA", "ED25519-CA"] | None = ...,
        nid: Literal["256", "384", "521"] | None = ...,
        usage: Literal["transparent-proxy", "access-proxy"] | None = ...,
        ip: str | None = ...,
        port: int | None = ...,
        hostname: str | None = ...,
        public_key: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: HostKeyPayload | None = ...,
        name: str | None = ...,
        status: Literal["trusted", "revoked"] | None = ...,
        type: Literal["RSA", "DSA", "ECDSA", "ED25519", "RSA-CA", "DSA-CA", "ECDSA-CA", "ED25519-CA"] | None = ...,
        nid: Literal["256", "384", "521"] | None = ...,
        usage: Literal["transparent-proxy", "access-proxy"] | None = ...,
        ip: str | None = ...,
        port: int | None = ...,
        hostname: str | None = ...,
        public_key: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def put(
        self,
        payload_dict: HostKeyPayload | None = ...,
        name: str | None = ...,
        status: Literal["trusted", "revoked"] | None = ...,
        type: Literal["RSA", "DSA", "ECDSA", "ED25519", "RSA-CA", "DSA-CA", "ECDSA-CA", "ED25519-CA"] | None = ...,
        nid: Literal["256", "384", "521"] | None = ...,
        usage: Literal["transparent-proxy", "access-proxy"] | None = ...,
        ip: str | None = ...,
        port: int | None = ...,
        hostname: str | None = ...,
        public_key: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> HostKeyObject: ...
    
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
        payload_dict: HostKeyPayload | None = ...,
        name: str | None = ...,
        status: Literal["trusted", "revoked"] | None = ...,
        type: Literal["RSA", "DSA", "ECDSA", "ED25519", "RSA-CA", "DSA-CA", "ECDSA-CA", "ED25519-CA"] | None = ...,
        nid: Literal["256", "384", "521"] | None = ...,
        usage: Literal["transparent-proxy", "access-proxy"] | None = ...,
        ip: str | None = ...,
        port: int | None = ...,
        hostname: str | None = ...,
        public_key: str | None = ...,
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
    "HostKey",
    "HostKeyPayload",
    "HostKeyResponse",
    "HostKeyObject",
]