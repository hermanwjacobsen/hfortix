from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class OcspServerPayload(TypedDict, total=False):
    """
    Type hints for vpn/certificate/ocsp_server payload fields.
    
    OCSP server configuration.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.vpn.certificate.ca.CaEndpoint` (via: cert, secondary-cert)
        - :class:`~.vpn.certificate.remote.RemoteEndpoint` (via: cert, secondary-cert)

    **Usage:**
        payload: OcspServerPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # OCSP server entry name. | MaxLen: 35
    url: str  # OCSP server URL. | MaxLen: 127
    cert: str  # OCSP server certificate. | MaxLen: 127
    secondary_url: str  # Secondary OCSP server URL. | MaxLen: 127
    secondary_cert: str  # Secondary OCSP server certificate. | MaxLen: 127
    unavail_action: Literal["revoke", "ignore"]  # Action when server is unavailable | Default: revoke
    source_ip: str  # Source IP address for dynamic AIA and OCSP queries | MaxLen: 63

# Nested TypedDicts for table field children (dict mode)

# Nested classes for table field children (object mode)


# Response TypedDict for GET returns (all fields present in API response)
class OcspServerResponse(TypedDict):
    """
    Type hints for vpn/certificate/ocsp_server API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str  # OCSP server entry name. | MaxLen: 35
    url: str  # OCSP server URL. | MaxLen: 127
    cert: str  # OCSP server certificate. | MaxLen: 127
    secondary_url: str  # Secondary OCSP server URL. | MaxLen: 127
    secondary_cert: str  # Secondary OCSP server certificate. | MaxLen: 127
    unavail_action: Literal["revoke", "ignore"]  # Action when server is unavailable | Default: revoke
    source_ip: str  # Source IP address for dynamic AIA and OCSP queries | MaxLen: 63


@final
class OcspServerObject:
    """Typed FortiObject for vpn/certificate/ocsp_server with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # OCSP server entry name. | MaxLen: 35
    name: str
    # OCSP server URL. | MaxLen: 127
    url: str
    # OCSP server certificate. | MaxLen: 127
    cert: str
    # Secondary OCSP server URL. | MaxLen: 127
    secondary_url: str
    # Secondary OCSP server certificate. | MaxLen: 127
    secondary_cert: str
    # Action when server is unavailable | Default: revoke
    unavail_action: Literal["revoke", "ignore"]
    # Source IP address for dynamic AIA and OCSP queries. | MaxLen: 63
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
    def to_dict(self) -> OcspServerPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class OcspServer:
    """
    OCSP server configuration.
    
    Path: vpn/certificate/ocsp_server
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
    ) -> OcspServerObject: ...
    
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
    ) -> OcspServerObject: ...
    
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
    ) -> FortiObjectList[OcspServerObject]: ...
    
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
    ) -> OcspServerObject: ...
    
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
    ) -> OcspServerObject: ...
    
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
    ) -> FortiObjectList[OcspServerObject]: ...
    
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
    ) -> OcspServerObject: ...
    
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
    ) -> OcspServerObject: ...
    
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
    ) -> FortiObjectList[OcspServerObject]: ...
    
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
    ) -> OcspServerObject | list[OcspServerObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: OcspServerPayload | None = ...,
        name: str | None = ...,
        url: str | None = ...,
        cert: str | None = ...,
        secondary_url: str | None = ...,
        secondary_cert: str | None = ...,
        unavail_action: Literal["revoke", "ignore"] | None = ...,
        source_ip: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> OcspServerObject: ...
    
    @overload
    def post(
        self,
        payload_dict: OcspServerPayload | None = ...,
        name: str | None = ...,
        url: str | None = ...,
        cert: str | None = ...,
        secondary_url: str | None = ...,
        secondary_cert: str | None = ...,
        unavail_action: Literal["revoke", "ignore"] | None = ...,
        source_ip: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: OcspServerPayload | None = ...,
        name: str | None = ...,
        url: str | None = ...,
        cert: str | None = ...,
        secondary_url: str | None = ...,
        secondary_cert: str | None = ...,
        unavail_action: Literal["revoke", "ignore"] | None = ...,
        source_ip: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def post(
        self,
        payload_dict: OcspServerPayload | None = ...,
        name: str | None = ...,
        url: str | None = ...,
        cert: str | None = ...,
        secondary_url: str | None = ...,
        secondary_cert: str | None = ...,
        unavail_action: Literal["revoke", "ignore"] | None = ...,
        source_ip: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: OcspServerPayload | None = ...,
        name: str | None = ...,
        url: str | None = ...,
        cert: str | None = ...,
        secondary_url: str | None = ...,
        secondary_cert: str | None = ...,
        unavail_action: Literal["revoke", "ignore"] | None = ...,
        source_ip: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> OcspServerObject: ...
    
    @overload
    def put(
        self,
        payload_dict: OcspServerPayload | None = ...,
        name: str | None = ...,
        url: str | None = ...,
        cert: str | None = ...,
        secondary_url: str | None = ...,
        secondary_cert: str | None = ...,
        unavail_action: Literal["revoke", "ignore"] | None = ...,
        source_ip: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: OcspServerPayload | None = ...,
        name: str | None = ...,
        url: str | None = ...,
        cert: str | None = ...,
        secondary_url: str | None = ...,
        secondary_cert: str | None = ...,
        unavail_action: Literal["revoke", "ignore"] | None = ...,
        source_ip: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def put(
        self,
        payload_dict: OcspServerPayload | None = ...,
        name: str | None = ...,
        url: str | None = ...,
        cert: str | None = ...,
        secondary_url: str | None = ...,
        secondary_cert: str | None = ...,
        unavail_action: Literal["revoke", "ignore"] | None = ...,
        source_ip: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> OcspServerObject: ...
    
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
        payload_dict: OcspServerPayload | None = ...,
        name: str | None = ...,
        url: str | None = ...,
        cert: str | None = ...,
        secondary_url: str | None = ...,
        secondary_cert: str | None = ...,
        unavail_action: Literal["revoke", "ignore"] | None = ...,
        source_ip: str | None = ...,
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
    "OcspServer",
    "OcspServerPayload",
    "OcspServerResponse",
    "OcspServerObject",
]