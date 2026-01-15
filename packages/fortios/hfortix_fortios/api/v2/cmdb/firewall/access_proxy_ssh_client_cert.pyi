from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject
from hfortix_core.types import MutationResponse, RawAPIResponse

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class AccessProxySshClientCertPayload(TypedDict, total=False):
    """
    Type hints for firewall/access_proxy_ssh_client_cert payload fields.
    
    Configure Access Proxy SSH client certificate.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.firewall.ssh.local-ca.LocalCaEndpoint` (via: auth-ca)

    **Usage:**
        payload: AccessProxySshClientCertPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # SSH client certificate name. | MaxLen: 79
    source_address: Literal["enable", "disable"]  # Enable/disable appending source-address certificat | Default: disable
    permit_x11_forwarding: Literal["enable", "disable"]  # Enable/disable appending permit-x11-forwarding cer | Default: enable
    permit_agent_forwarding: Literal["enable", "disable"]  # Enable/disable appending permit-agent-forwarding c | Default: enable
    permit_port_forwarding: Literal["enable", "disable"]  # Enable/disable appending permit-port-forwarding ce | Default: enable
    permit_pty: Literal["enable", "disable"]  # Enable/disable appending permit-pty certificate ex | Default: enable
    permit_user_rc: Literal["enable", "disable"]  # Enable/disable appending permit-user-rc certificat | Default: enable
    cert_extension: list[dict[str, Any]]  # Configure certificate extension for user certifica
    auth_ca: str  # Name of the SSH server public key authentication C | MaxLen: 79

# Nested TypedDicts for table field children (dict mode)

class AccessProxySshClientCertCertextensionItem(TypedDict):
    """Type hints for cert-extension table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # Name of certificate extension. | MaxLen: 127
    critical: Literal["no", "yes"]  # Critical option. | Default: no
    type: Literal["fixed", "user"]  # Type of certificate extension. | Default: fixed
    data: str  # Data of certificate extension. | MaxLen: 127


# Nested classes for table field children (object mode)

@final
class AccessProxySshClientCertCertextensionObject:
    """Typed object for cert-extension table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Name of certificate extension. | MaxLen: 127
    name: str
    # Critical option. | Default: no
    critical: Literal["no", "yes"]
    # Type of certificate extension. | Default: fixed
    type: Literal["fixed", "user"]
    # Data of certificate extension. | MaxLen: 127
    data: str
    
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
class AccessProxySshClientCertResponse(TypedDict):
    """
    Type hints for firewall/access_proxy_ssh_client_cert API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str  # SSH client certificate name. | MaxLen: 79
    source_address: Literal["enable", "disable"]  # Enable/disable appending source-address certificat | Default: disable
    permit_x11_forwarding: Literal["enable", "disable"]  # Enable/disable appending permit-x11-forwarding cer | Default: enable
    permit_agent_forwarding: Literal["enable", "disable"]  # Enable/disable appending permit-agent-forwarding c | Default: enable
    permit_port_forwarding: Literal["enable", "disable"]  # Enable/disable appending permit-port-forwarding ce | Default: enable
    permit_pty: Literal["enable", "disable"]  # Enable/disable appending permit-pty certificate ex | Default: enable
    permit_user_rc: Literal["enable", "disable"]  # Enable/disable appending permit-user-rc certificat | Default: enable
    cert_extension: list[AccessProxySshClientCertCertextensionItem]  # Configure certificate extension for user certifica
    auth_ca: str  # Name of the SSH server public key authentication C | MaxLen: 79


@final
class AccessProxySshClientCertObject:
    """Typed FortiObject for firewall/access_proxy_ssh_client_cert with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # SSH client certificate name. | MaxLen: 79
    name: str
    # Enable/disable appending source-address certificate critical | Default: disable
    source_address: Literal["enable", "disable"]
    # Enable/disable appending permit-x11-forwarding certificate e | Default: enable
    permit_x11_forwarding: Literal["enable", "disable"]
    # Enable/disable appending permit-agent-forwarding certificate | Default: enable
    permit_agent_forwarding: Literal["enable", "disable"]
    # Enable/disable appending permit-port-forwarding certificate | Default: enable
    permit_port_forwarding: Literal["enable", "disable"]
    # Enable/disable appending permit-pty certificate extension. | Default: enable
    permit_pty: Literal["enable", "disable"]
    # Enable/disable appending permit-user-rc certificate extensio | Default: enable
    permit_user_rc: Literal["enable", "disable"]
    # Configure certificate extension for user certificate.
    cert_extension: list[AccessProxySshClientCertCertextensionObject]
    # Name of the SSH server public key authentication CA. | MaxLen: 79
    auth_ca: str
    
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
    def to_dict(self) -> AccessProxySshClientCertPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class AccessProxySshClientCert:
    """
    Configure Access Proxy SSH client certificate.
    
    Path: firewall/access_proxy_ssh_client_cert
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
    ) -> AccessProxySshClientCertObject: ...
    
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
    ) -> AccessProxySshClientCertObject: ...
    
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
    ) -> list[AccessProxySshClientCertObject]: ...
    
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
    ) -> AccessProxySshClientCertObject: ...
    
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
    ) -> AccessProxySshClientCertObject: ...
    
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
    ) -> list[AccessProxySshClientCertObject]: ...
    
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
    ) -> AccessProxySshClientCertObject: ...
    
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
    ) -> AccessProxySshClientCertObject: ...
    
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
    ) -> list[AccessProxySshClientCertObject]: ...
    
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
    ) -> AccessProxySshClientCertObject | list[AccessProxySshClientCertObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: AccessProxySshClientCertPayload | None = ...,
        name: str | None = ...,
        source_address: Literal["enable", "disable"] | None = ...,
        permit_x11_forwarding: Literal["enable", "disable"] | None = ...,
        permit_agent_forwarding: Literal["enable", "disable"] | None = ...,
        permit_port_forwarding: Literal["enable", "disable"] | None = ...,
        permit_pty: Literal["enable", "disable"] | None = ...,
        permit_user_rc: Literal["enable", "disable"] | None = ...,
        cert_extension: str | list[str] | list[dict[str, Any]] | None = ...,
        auth_ca: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> AccessProxySshClientCertObject: ...
    
    @overload
    def post(
        self,
        payload_dict: AccessProxySshClientCertPayload | None = ...,
        name: str | None = ...,
        source_address: Literal["enable", "disable"] | None = ...,
        permit_x11_forwarding: Literal["enable", "disable"] | None = ...,
        permit_agent_forwarding: Literal["enable", "disable"] | None = ...,
        permit_port_forwarding: Literal["enable", "disable"] | None = ...,
        permit_pty: Literal["enable", "disable"] | None = ...,
        permit_user_rc: Literal["enable", "disable"] | None = ...,
        cert_extension: str | list[str] | list[dict[str, Any]] | None = ...,
        auth_ca: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    # raw_json=True returns the full API envelope
    @overload
    def post(
        self,
        payload_dict: AccessProxySshClientCertPayload | None = ...,
        name: str | None = ...,
        source_address: Literal["enable", "disable"] | None = ...,
        permit_x11_forwarding: Literal["enable", "disable"] | None = ...,
        permit_agent_forwarding: Literal["enable", "disable"] | None = ...,
        permit_port_forwarding: Literal["enable", "disable"] | None = ...,
        permit_pty: Literal["enable", "disable"] | None = ...,
        permit_user_rc: Literal["enable", "disable"] | None = ...,
        cert_extension: str | list[str] | list[dict[str, Any]] | None = ...,
        auth_ca: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> RawAPIResponse: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: AccessProxySshClientCertPayload | None = ...,
        name: str | None = ...,
        source_address: Literal["enable", "disable"] | None = ...,
        permit_x11_forwarding: Literal["enable", "disable"] | None = ...,
        permit_agent_forwarding: Literal["enable", "disable"] | None = ...,
        permit_port_forwarding: Literal["enable", "disable"] | None = ...,
        permit_pty: Literal["enable", "disable"] | None = ...,
        permit_user_rc: Literal["enable", "disable"] | None = ...,
        cert_extension: str | list[str] | list[dict[str, Any]] | None = ...,
        auth_ca: str | None = ...,
        vdom: str | bool | None = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    def post(
        self,
        payload_dict: AccessProxySshClientCertPayload | None = ...,
        name: str | None = ...,
        source_address: Literal["enable", "disable"] | None = ...,
        permit_x11_forwarding: Literal["enable", "disable"] | None = ...,
        permit_agent_forwarding: Literal["enable", "disable"] | None = ...,
        permit_port_forwarding: Literal["enable", "disable"] | None = ...,
        permit_pty: Literal["enable", "disable"] | None = ...,
        permit_user_rc: Literal["enable", "disable"] | None = ...,
        cert_extension: str | list[str] | list[dict[str, Any]] | None = ...,
        auth_ca: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: AccessProxySshClientCertPayload | None = ...,
        name: str | None = ...,
        source_address: Literal["enable", "disable"] | None = ...,
        permit_x11_forwarding: Literal["enable", "disable"] | None = ...,
        permit_agent_forwarding: Literal["enable", "disable"] | None = ...,
        permit_port_forwarding: Literal["enable", "disable"] | None = ...,
        permit_pty: Literal["enable", "disable"] | None = ...,
        permit_user_rc: Literal["enable", "disable"] | None = ...,
        cert_extension: str | list[str] | list[dict[str, Any]] | None = ...,
        auth_ca: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> AccessProxySshClientCertObject: ...
    
    @overload
    def put(
        self,
        payload_dict: AccessProxySshClientCertPayload | None = ...,
        name: str | None = ...,
        source_address: Literal["enable", "disable"] | None = ...,
        permit_x11_forwarding: Literal["enable", "disable"] | None = ...,
        permit_agent_forwarding: Literal["enable", "disable"] | None = ...,
        permit_port_forwarding: Literal["enable", "disable"] | None = ...,
        permit_pty: Literal["enable", "disable"] | None = ...,
        permit_user_rc: Literal["enable", "disable"] | None = ...,
        cert_extension: str | list[str] | list[dict[str, Any]] | None = ...,
        auth_ca: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    # raw_json=True returns the full API envelope
    @overload
    def put(
        self,
        payload_dict: AccessProxySshClientCertPayload | None = ...,
        name: str | None = ...,
        source_address: Literal["enable", "disable"] | None = ...,
        permit_x11_forwarding: Literal["enable", "disable"] | None = ...,
        permit_agent_forwarding: Literal["enable", "disable"] | None = ...,
        permit_port_forwarding: Literal["enable", "disable"] | None = ...,
        permit_pty: Literal["enable", "disable"] | None = ...,
        permit_user_rc: Literal["enable", "disable"] | None = ...,
        cert_extension: str | list[str] | list[dict[str, Any]] | None = ...,
        auth_ca: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> RawAPIResponse: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: AccessProxySshClientCertPayload | None = ...,
        name: str | None = ...,
        source_address: Literal["enable", "disable"] | None = ...,
        permit_x11_forwarding: Literal["enable", "disable"] | None = ...,
        permit_agent_forwarding: Literal["enable", "disable"] | None = ...,
        permit_port_forwarding: Literal["enable", "disable"] | None = ...,
        permit_pty: Literal["enable", "disable"] | None = ...,
        permit_user_rc: Literal["enable", "disable"] | None = ...,
        cert_extension: str | list[str] | list[dict[str, Any]] | None = ...,
        auth_ca: str | None = ...,
        vdom: str | bool | None = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    def put(
        self,
        payload_dict: AccessProxySshClientCertPayload | None = ...,
        name: str | None = ...,
        source_address: Literal["enable", "disable"] | None = ...,
        permit_x11_forwarding: Literal["enable", "disable"] | None = ...,
        permit_agent_forwarding: Literal["enable", "disable"] | None = ...,
        permit_port_forwarding: Literal["enable", "disable"] | None = ...,
        permit_pty: Literal["enable", "disable"] | None = ...,
        permit_user_rc: Literal["enable", "disable"] | None = ...,
        cert_extension: str | list[str] | list[dict[str, Any]] | None = ...,
        auth_ca: str | None = ...,
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
    ) -> AccessProxySshClientCertObject: ...
    
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
        payload_dict: AccessProxySshClientCertPayload | None = ...,
        name: str | None = ...,
        source_address: Literal["enable", "disable"] | None = ...,
        permit_x11_forwarding: Literal["enable", "disable"] | None = ...,
        permit_agent_forwarding: Literal["enable", "disable"] | None = ...,
        permit_port_forwarding: Literal["enable", "disable"] | None = ...,
        permit_pty: Literal["enable", "disable"] | None = ...,
        permit_user_rc: Literal["enable", "disable"] | None = ...,
        cert_extension: str | list[str] | list[dict[str, Any]] | None = ...,
        auth_ca: str | None = ...,
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
    "AccessProxySshClientCert",
    "AccessProxySshClientCertPayload",
    "AccessProxySshClientCertResponse",
    "AccessProxySshClientCertObject",
]