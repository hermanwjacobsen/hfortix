from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList
from hfortix_core.types import MutationResponse

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class CustomPayload(TypedDict, total=False):
    """
    Type hints for ips/custom payload fields.
    
    Configure IPS custom signature.
    
    **Usage:**
        payload: CustomPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    tag: str  # Signature tag. | MaxLen: 63
    signature: str  # Custom signature enclosed in single quotes. | MaxLen: 4095
    rule_id: int  # Signature ID. | Default: 0 | Min: 0 | Max: 4294967295
    severity: str  # Relative severity of the signature, from info to c
    location: list[dict[str, Any]]  # Protect client or server traffic.
    os: list[dict[str, Any]]  # Operating system(s) that the signature protects. B
    application: list[dict[str, Any]]  # Applications to be protected. Blank for all applic
    protocol: str  # Protocol(s) that the signature scans. Blank for al
    status: Literal["disable", "enable"]  # Enable/disable this signature. | Default: enable
    log: Literal["disable", "enable"]  # Enable/disable logging. | Default: enable
    log_packet: Literal["disable", "enable"]  # Enable/disable packet logging. | Default: disable
    action: Literal["pass", "block"]  # Default action (pass or block) for this signature. | Default: pass
    comment: str  # Comment. | MaxLen: 63

# Nested TypedDicts for table field children (dict mode)

# Nested classes for table field children (object mode)


# Response TypedDict for GET returns (all fields present in API response)
class CustomResponse(TypedDict):
    """
    Type hints for ips/custom API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    tag: str  # Signature tag. | MaxLen: 63
    signature: str  # Custom signature enclosed in single quotes. | MaxLen: 4095
    rule_id: int  # Signature ID. | Default: 0 | Min: 0 | Max: 4294967295
    severity: str  # Relative severity of the signature, from info to c
    location: list[dict[str, Any]]  # Protect client or server traffic.
    os: list[dict[str, Any]]  # Operating system(s) that the signature protects. B
    application: list[dict[str, Any]]  # Applications to be protected. Blank for all applic
    protocol: str  # Protocol(s) that the signature scans. Blank for al
    status: Literal["disable", "enable"]  # Enable/disable this signature. | Default: enable
    log: Literal["disable", "enable"]  # Enable/disable logging. | Default: enable
    log_packet: Literal["disable", "enable"]  # Enable/disable packet logging. | Default: disable
    action: Literal["pass", "block"]  # Default action (pass or block) for this signature. | Default: pass
    comment: str  # Comment. | MaxLen: 63


@final
class CustomObject:
    """Typed FortiObject for ips/custom with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Signature tag. | MaxLen: 63
    tag: str
    # Custom signature enclosed in single quotes. | MaxLen: 4095
    signature: str
    # Signature ID. | Default: 0 | Min: 0 | Max: 4294967295
    rule_id: int
    # Relative severity of the signature, from info to critical. L
    severity: str
    # Protect client or server traffic.
    location: list[dict[str, Any]]
    # Operating system(s) that the signature protects. Blank for a
    os: list[dict[str, Any]]
    # Applications to be protected. Blank for all applications.
    application: list[dict[str, Any]]
    # Protocol(s) that the signature scans. Blank for all protocol
    protocol: str
    # Enable/disable this signature. | Default: enable
    status: Literal["disable", "enable"]
    # Enable/disable logging. | Default: enable
    log: Literal["disable", "enable"]
    # Enable/disable packet logging. | Default: disable
    log_packet: Literal["disable", "enable"]
    # Default action (pass or block) for this signature. | Default: pass
    action: Literal["pass", "block"]
    # Comment. | MaxLen: 63
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
    def to_dict(self) -> CustomPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Custom:
    """
    Configure IPS custom signature.
    
    Path: ips/custom
    Category: cmdb
    Primary Key: tag
    """
    
    # ================================================================
    # GET OVERLOADS - Always returns FortiObject
    # Pylance matches overloads top-to-bottom, so these must come first!
    # ================================================================
    
    # With mkey as positional arg -> returns FortiObject
    @overload
    def get(
        self,
        tag: str,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> CustomObject: ...
    
    # With mkey as keyword arg -> returns FortiObject
    @overload
    def get(
        self,
        *,
        tag: str,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> CustomObject: ...
    
    # Without mkey -> returns list of FortiObjects
    @overload
    def get(
        self,
        tag: None = None,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObjectList[CustomObject]: ...
    
    # ================================================================
    # (removed - all GET now returns FortiObject)
    # ================================================================
    
    # With mkey as positional arg -> returns single object
    @overload
    def get(
        self,
        tag: str,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> CustomObject: ...
    
    # With mkey as keyword arg -> returns single object
    @overload
    def get(
        self,
        *,
        tag: str,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> CustomObject: ...
    
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
    ) -> FortiObjectList[CustomObject]: ...
    
    # Dict mode with mkey provided as positional arg (single dict)
    @overload
    def get(
        self,
        tag: str,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> CustomObject: ...
    
    # Dict mode with mkey provided as keyword arg (single dict)
    @overload
    def get(
        self,
        *,
        tag: str,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> CustomObject: ...
    
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
    ) -> FortiObjectList[CustomObject]: ...
    
    # Fallback overload for all other cases
    @overload
    def get(
        self,
        tag: str | None = ...,
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
        tag: str | None = ...,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> CustomObject | list[CustomObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: CustomPayload | None = ...,
        tag: str | None = ...,
        signature: str | None = ...,
        rule_id: int | None = ...,
        severity: str | None = ...,
        location: str | list[str] | None = ...,
        os: str | list[str] | None = ...,
        application: str | list[str] | None = ...,
        protocol: str | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        log: Literal["disable", "enable"] | None = ...,
        log_packet: Literal["disable", "enable"] | None = ...,
        action: Literal["pass", "block"] | None = ...,
        comment: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> CustomObject: ...
    
    @overload
    def post(
        self,
        payload_dict: CustomPayload | None = ...,
        tag: str | None = ...,
        signature: str | None = ...,
        rule_id: int | None = ...,
        severity: str | None = ...,
        location: str | list[str] | None = ...,
        os: str | list[str] | None = ...,
        application: str | list[str] | None = ...,
        protocol: str | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        log: Literal["disable", "enable"] | None = ...,
        log_packet: Literal["disable", "enable"] | None = ...,
        action: Literal["pass", "block"] | None = ...,
        comment: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: CustomPayload | None = ...,
        tag: str | None = ...,
        signature: str | None = ...,
        rule_id: int | None = ...,
        severity: str | None = ...,
        location: str | list[str] | None = ...,
        os: str | list[str] | None = ...,
        application: str | list[str] | None = ...,
        protocol: str | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        log: Literal["disable", "enable"] | None = ...,
        log_packet: Literal["disable", "enable"] | None = ...,
        action: Literal["pass", "block"] | None = ...,
        comment: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def post(
        self,
        payload_dict: CustomPayload | None = ...,
        tag: str | None = ...,
        signature: str | None = ...,
        rule_id: int | None = ...,
        severity: str | None = ...,
        location: str | list[str] | None = ...,
        os: str | list[str] | None = ...,
        application: str | list[str] | None = ...,
        protocol: str | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        log: Literal["disable", "enable"] | None = ...,
        log_packet: Literal["disable", "enable"] | None = ...,
        action: Literal["pass", "block"] | None = ...,
        comment: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: CustomPayload | None = ...,
        tag: str | None = ...,
        signature: str | None = ...,
        rule_id: int | None = ...,
        severity: str | None = ...,
        location: str | list[str] | None = ...,
        os: str | list[str] | None = ...,
        application: str | list[str] | None = ...,
        protocol: str | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        log: Literal["disable", "enable"] | None = ...,
        log_packet: Literal["disable", "enable"] | None = ...,
        action: Literal["pass", "block"] | None = ...,
        comment: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> CustomObject: ...
    
    @overload
    def put(
        self,
        payload_dict: CustomPayload | None = ...,
        tag: str | None = ...,
        signature: str | None = ...,
        rule_id: int | None = ...,
        severity: str | None = ...,
        location: str | list[str] | None = ...,
        os: str | list[str] | None = ...,
        application: str | list[str] | None = ...,
        protocol: str | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        log: Literal["disable", "enable"] | None = ...,
        log_packet: Literal["disable", "enable"] | None = ...,
        action: Literal["pass", "block"] | None = ...,
        comment: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: CustomPayload | None = ...,
        tag: str | None = ...,
        signature: str | None = ...,
        rule_id: int | None = ...,
        severity: str | None = ...,
        location: str | list[str] | None = ...,
        os: str | list[str] | None = ...,
        application: str | list[str] | None = ...,
        protocol: str | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        log: Literal["disable", "enable"] | None = ...,
        log_packet: Literal["disable", "enable"] | None = ...,
        action: Literal["pass", "block"] | None = ...,
        comment: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def put(
        self,
        payload_dict: CustomPayload | None = ...,
        tag: str | None = ...,
        signature: str | None = ...,
        rule_id: int | None = ...,
        severity: str | None = ...,
        location: str | list[str] | None = ...,
        os: str | list[str] | None = ...,
        application: str | list[str] | None = ...,
        protocol: str | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        log: Literal["disable", "enable"] | None = ...,
        log_packet: Literal["disable", "enable"] | None = ...,
        action: Literal["pass", "block"] | None = ...,
        comment: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        tag: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> CustomObject: ...
    
    @overload
    def delete(
        self,
        tag: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Default overload
    @overload
    def delete(
        self,
        tag: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def delete(
        self,
        tag: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def exists(
        self,
        tag: str,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: CustomPayload | None = ...,
        tag: str | None = ...,
        signature: str | None = ...,
        rule_id: int | None = ...,
        severity: str | None = ...,
        location: str | list[str] | None = ...,
        os: str | list[str] | None = ...,
        application: str | list[str] | None = ...,
        protocol: str | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        log: Literal["disable", "enable"] | None = ...,
        log_packet: Literal["disable", "enable"] | None = ...,
        action: Literal["pass", "block"] | None = ...,
        comment: str | None = ...,
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
    "Custom",
    "CustomPayload",
    "CustomResponse",
    "CustomObject",
]