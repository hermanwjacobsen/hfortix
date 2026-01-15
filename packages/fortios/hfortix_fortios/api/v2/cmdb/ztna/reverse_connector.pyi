from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class ReverseConnectorPayload(TypedDict, total=False):
    """
    Type hints for ztna/reverse_connector payload fields.
    
    Configure ZTNA Reverse-Connector.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.vpn.certificate.ca.CaEndpoint` (via: trusted-server-ca)
        - :class:`~.vpn.certificate.local.LocalEndpoint` (via: certificate)

    **Usage:**
        payload: ReverseConnectorPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # Reverse-Connector name | MaxLen: 35
    status: Literal["enable", "disable"]  # Reverse-Connector status. | Default: enable
    address: str  # Connector service edge adress(IP or FQDN). | MaxLen: 255
    port: int  # Port number that traffic uses to connect to connec | Default: 0 | Min: 0 | Max: 65535
    health_check_interval: int  # Health check interval in seconds | Default: 60 | Min: 0 | Max: 600
    ssl_max_version: Literal["tls-1.1", "tls-1.2", "tls-1.3"]  # Highest TLS version acceptable from a server. | Default: tls-1.3
    certificate: str  # The name of the certificate to use for SSL handsha | MaxLen: 35
    trusted_server_ca: str  # Trusted Server CA certificate used by SSL connecti | MaxLen: 79

# Nested TypedDicts for table field children (dict mode)

# Nested classes for table field children (object mode)


# Response TypedDict for GET returns (all fields present in API response)
class ReverseConnectorResponse(TypedDict):
    """
    Type hints for ztna/reverse_connector API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str  # Reverse-Connector name | MaxLen: 35
    status: Literal["enable", "disable"]  # Reverse-Connector status. | Default: enable
    address: str  # Connector service edge adress(IP or FQDN). | MaxLen: 255
    port: int  # Port number that traffic uses to connect to connec | Default: 0 | Min: 0 | Max: 65535
    health_check_interval: int  # Health check interval in seconds | Default: 60 | Min: 0 | Max: 600
    ssl_max_version: Literal["tls-1.1", "tls-1.2", "tls-1.3"]  # Highest TLS version acceptable from a server. | Default: tls-1.3
    certificate: str  # The name of the certificate to use for SSL handsha | MaxLen: 35
    trusted_server_ca: str  # Trusted Server CA certificate used by SSL connecti | MaxLen: 79


@final
class ReverseConnectorObject:
    """Typed FortiObject for ztna/reverse_connector with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Reverse-Connector name | MaxLen: 35
    name: str
    # Reverse-Connector status. | Default: enable
    status: Literal["enable", "disable"]
    # Connector service edge adress(IP or FQDN). | MaxLen: 255
    address: str
    # Port number that traffic uses to connect to connector servic | Default: 0 | Min: 0 | Max: 65535
    port: int
    # Health check interval in seconds | Default: 60 | Min: 0 | Max: 600
    health_check_interval: int
    # Highest TLS version acceptable from a server. | Default: tls-1.3
    ssl_max_version: Literal["tls-1.1", "tls-1.2", "tls-1.3"]
    # The name of the certificate to use for SSL handshake. | MaxLen: 35
    certificate: str
    # Trusted Server CA certificate used by SSL connection. | MaxLen: 79
    trusted_server_ca: str
    
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
    def to_dict(self) -> ReverseConnectorPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class ReverseConnector:
    """
    Configure ZTNA Reverse-Connector.
    
    Path: ztna/reverse_connector
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
    ) -> ReverseConnectorObject: ...
    
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
    ) -> ReverseConnectorObject: ...
    
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
    ) -> FortiObjectList[ReverseConnectorObject]: ...
    
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
    ) -> ReverseConnectorObject: ...
    
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
    ) -> ReverseConnectorObject: ...
    
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
    ) -> FortiObjectList[ReverseConnectorObject]: ...
    
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
    ) -> ReverseConnectorObject: ...
    
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
    ) -> ReverseConnectorObject: ...
    
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
    ) -> FortiObjectList[ReverseConnectorObject]: ...
    
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
    ) -> ReverseConnectorObject | list[ReverseConnectorObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: ReverseConnectorPayload | None = ...,
        name: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        address: str | None = ...,
        port: int | None = ...,
        health_check_interval: int | None = ...,
        ssl_max_version: Literal["tls-1.1", "tls-1.2", "tls-1.3"] | None = ...,
        certificate: str | None = ...,
        trusted_server_ca: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> ReverseConnectorObject: ...
    
    @overload
    def post(
        self,
        payload_dict: ReverseConnectorPayload | None = ...,
        name: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        address: str | None = ...,
        port: int | None = ...,
        health_check_interval: int | None = ...,
        ssl_max_version: Literal["tls-1.1", "tls-1.2", "tls-1.3"] | None = ...,
        certificate: str | None = ...,
        trusted_server_ca: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: ReverseConnectorPayload | None = ...,
        name: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        address: str | None = ...,
        port: int | None = ...,
        health_check_interval: int | None = ...,
        ssl_max_version: Literal["tls-1.1", "tls-1.2", "tls-1.3"] | None = ...,
        certificate: str | None = ...,
        trusted_server_ca: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def post(
        self,
        payload_dict: ReverseConnectorPayload | None = ...,
        name: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        address: str | None = ...,
        port: int | None = ...,
        health_check_interval: int | None = ...,
        ssl_max_version: Literal["tls-1.1", "tls-1.2", "tls-1.3"] | None = ...,
        certificate: str | None = ...,
        trusted_server_ca: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: ReverseConnectorPayload | None = ...,
        name: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        address: str | None = ...,
        port: int | None = ...,
        health_check_interval: int | None = ...,
        ssl_max_version: Literal["tls-1.1", "tls-1.2", "tls-1.3"] | None = ...,
        certificate: str | None = ...,
        trusted_server_ca: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> ReverseConnectorObject: ...
    
    @overload
    def put(
        self,
        payload_dict: ReverseConnectorPayload | None = ...,
        name: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        address: str | None = ...,
        port: int | None = ...,
        health_check_interval: int | None = ...,
        ssl_max_version: Literal["tls-1.1", "tls-1.2", "tls-1.3"] | None = ...,
        certificate: str | None = ...,
        trusted_server_ca: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: ReverseConnectorPayload | None = ...,
        name: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        address: str | None = ...,
        port: int | None = ...,
        health_check_interval: int | None = ...,
        ssl_max_version: Literal["tls-1.1", "tls-1.2", "tls-1.3"] | None = ...,
        certificate: str | None = ...,
        trusted_server_ca: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def put(
        self,
        payload_dict: ReverseConnectorPayload | None = ...,
        name: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        address: str | None = ...,
        port: int | None = ...,
        health_check_interval: int | None = ...,
        ssl_max_version: Literal["tls-1.1", "tls-1.2", "tls-1.3"] | None = ...,
        certificate: str | None = ...,
        trusted_server_ca: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> ReverseConnectorObject: ...
    
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
        payload_dict: ReverseConnectorPayload | None = ...,
        name: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        address: str | None = ...,
        port: int | None = ...,
        health_check_interval: int | None = ...,
        ssl_max_version: Literal["tls-1.1", "tls-1.2", "tls-1.3"] | None = ...,
        certificate: str | None = ...,
        trusted_server_ca: str | None = ...,
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
    "ReverseConnector",
    "ReverseConnectorPayload",
    "ReverseConnectorResponse",
    "ReverseConnectorObject",
]