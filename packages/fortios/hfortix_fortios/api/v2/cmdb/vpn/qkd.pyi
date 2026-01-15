from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject
from hfortix_core.types import MutationResponse, RawAPIResponse

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class QkdPayload(TypedDict, total=False):
    """
    Type hints for vpn/qkd payload fields.
    
    Configure Quantum Key Distribution servers
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.user.peer.PeerEndpoint` (via: peer)
        - :class:`~.user.peergrp.PeergrpEndpoint` (via: peer)

    **Usage:**
        payload: QkdPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # Quantum Key Distribution configuration name. | MaxLen: 35
    server: str  # IPv4, IPv6 or DNS address of the KME. | MaxLen: 63
    port: int  # Port to connect to on the KME. | Default: 0 | Min: 1 | Max: 65535
    id: str  # Quantum Key Distribution ID assigned by the KME. | MaxLen: 291
    peer: str  # Authenticate Quantum Key Device's certificate with | MaxLen: 35
    certificate: list[dict[str, Any]]  # Names of up to 4 certificates to offer to the KME.
    comment: str  # Comment. | MaxLen: 255

# Nested TypedDicts for table field children (dict mode)

class QkdCertificateItem(TypedDict):
    """Type hints for certificate table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # Certificate name. | MaxLen: 79


# Nested classes for table field children (object mode)

@final
class QkdCertificateObject:
    """Typed object for certificate table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Certificate name. | MaxLen: 79
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
class QkdResponse(TypedDict):
    """
    Type hints for vpn/qkd API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str  # Quantum Key Distribution configuration name. | MaxLen: 35
    server: str  # IPv4, IPv6 or DNS address of the KME. | MaxLen: 63
    port: int  # Port to connect to on the KME. | Default: 0 | Min: 1 | Max: 65535
    id: str  # Quantum Key Distribution ID assigned by the KME. | MaxLen: 291
    peer: str  # Authenticate Quantum Key Device's certificate with | MaxLen: 35
    certificate: list[QkdCertificateItem]  # Names of up to 4 certificates to offer to the KME.
    comment: str  # Comment. | MaxLen: 255


@final
class QkdObject:
    """Typed FortiObject for vpn/qkd with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Quantum Key Distribution configuration name. | MaxLen: 35
    name: str
    # IPv4, IPv6 or DNS address of the KME. | MaxLen: 63
    server: str
    # Port to connect to on the KME. | Default: 0 | Min: 1 | Max: 65535
    port: int
    # Quantum Key Distribution ID assigned by the KME. | MaxLen: 291
    id: str
    # Authenticate Quantum Key Device's certificate with the peer/ | MaxLen: 35
    peer: str
    # Names of up to 4 certificates to offer to the KME.
    certificate: list[QkdCertificateObject]
    # Comment. | MaxLen: 255
    comment: str
    
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
    def to_dict(self) -> QkdPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Qkd:
    """
    Configure Quantum Key Distribution servers
    
    Path: vpn/qkd
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
    ) -> QkdObject: ...
    
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
    ) -> QkdObject: ...
    
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
    ) -> list[QkdObject]: ...
    
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
    ) -> QkdObject: ...
    
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
    ) -> QkdObject: ...
    
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
    ) -> list[QkdObject]: ...
    
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
    ) -> QkdObject: ...
    
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
    ) -> QkdObject: ...
    
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
    ) -> list[QkdObject]: ...
    
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
    ) -> QkdObject | list[QkdObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: QkdPayload | None = ...,
        name: str | None = ...,
        server: str | None = ...,
        port: int | None = ...,
        id: str | None = ...,
        peer: str | None = ...,
        certificate: str | list[str] | list[dict[str, Any]] | None = ...,
        comment: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> QkdObject: ...
    
    @overload
    def post(
        self,
        payload_dict: QkdPayload | None = ...,
        name: str | None = ...,
        server: str | None = ...,
        port: int | None = ...,
        id: str | None = ...,
        peer: str | None = ...,
        certificate: str | list[str] | list[dict[str, Any]] | None = ...,
        comment: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    # raw_json=True returns the full API envelope
    @overload
    def post(
        self,
        payload_dict: QkdPayload | None = ...,
        name: str | None = ...,
        server: str | None = ...,
        port: int | None = ...,
        id: str | None = ...,
        peer: str | None = ...,
        certificate: str | list[str] | list[dict[str, Any]] | None = ...,
        comment: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> RawAPIResponse: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: QkdPayload | None = ...,
        name: str | None = ...,
        server: str | None = ...,
        port: int | None = ...,
        id: str | None = ...,
        peer: str | None = ...,
        certificate: str | list[str] | list[dict[str, Any]] | None = ...,
        comment: str | None = ...,
        vdom: str | bool | None = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    def post(
        self,
        payload_dict: QkdPayload | None = ...,
        name: str | None = ...,
        server: str | None = ...,
        port: int | None = ...,
        id: str | None = ...,
        peer: str | None = ...,
        certificate: str | list[str] | list[dict[str, Any]] | None = ...,
        comment: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: QkdPayload | None = ...,
        name: str | None = ...,
        server: str | None = ...,
        port: int | None = ...,
        id: str | None = ...,
        peer: str | None = ...,
        certificate: str | list[str] | list[dict[str, Any]] | None = ...,
        comment: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> QkdObject: ...
    
    @overload
    def put(
        self,
        payload_dict: QkdPayload | None = ...,
        name: str | None = ...,
        server: str | None = ...,
        port: int | None = ...,
        id: str | None = ...,
        peer: str | None = ...,
        certificate: str | list[str] | list[dict[str, Any]] | None = ...,
        comment: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    # raw_json=True returns the full API envelope
    @overload
    def put(
        self,
        payload_dict: QkdPayload | None = ...,
        name: str | None = ...,
        server: str | None = ...,
        port: int | None = ...,
        id: str | None = ...,
        peer: str | None = ...,
        certificate: str | list[str] | list[dict[str, Any]] | None = ...,
        comment: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> RawAPIResponse: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: QkdPayload | None = ...,
        name: str | None = ...,
        server: str | None = ...,
        port: int | None = ...,
        id: str | None = ...,
        peer: str | None = ...,
        certificate: str | list[str] | list[dict[str, Any]] | None = ...,
        comment: str | None = ...,
        vdom: str | bool | None = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    def put(
        self,
        payload_dict: QkdPayload | None = ...,
        name: str | None = ...,
        server: str | None = ...,
        port: int | None = ...,
        id: str | None = ...,
        peer: str | None = ...,
        certificate: str | list[str] | list[dict[str, Any]] | None = ...,
        comment: str | None = ...,
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
    ) -> QkdObject: ...
    
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
        payload_dict: QkdPayload | None = ...,
        name: str | None = ...,
        server: str | None = ...,
        port: int | None = ...,
        id: str | None = ...,
        peer: str | None = ...,
        certificate: str | list[str] | list[dict[str, Any]] | None = ...,
        comment: str | None = ...,
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
    "Qkd",
    "QkdPayload",
    "QkdResponse",
    "QkdObject",
]