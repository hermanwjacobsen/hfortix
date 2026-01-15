from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class IkePayload(TypedDict, total=False):
    """
    Type hints for system/ike payload fields.
    
    Configure IKE global attributes.
    
    **Usage:**
        payload: IkePayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    embryonic_limit: int  # Maximum number of IPsec tunnels to negotiate simul | Default: 10000 | Min: 50 | Max: 20000
    dh_multiprocess: Literal["enable", "disable"]  # Enable/disable multiprocess Diffie-Hellman daemon | Default: enable
    dh_worker_count: int  # Number of Diffie-Hellman workers to start. | Default: 0 | Min: 1 | Max: 2
    dh_mode: Literal["software", "hardware"]  # Use software (CPU) or hardware (CPX) to perform Di | Default: software
    dh_keypair_cache: Literal["enable", "disable"]  # Enable/disable Diffie-Hellman key pair cache. | Default: enable
    dh_keypair_count: int  # Number of key pairs to pre-generate for each Diffi | Default: 100 | Min: 0 | Max: 50000
    dh_keypair_throttle: Literal["enable", "disable"]  # Enable/disable Diffie-Hellman key pair cache CPU t | Default: enable
    dh_group_1: str  # Diffie-Hellman group 1 (MODP-768).
    dh_group_2: str  # Diffie-Hellman group 2 (MODP-1024).
    dh_group_5: str  # Diffie-Hellman group 5 (MODP-1536).
    dh_group_14: str  # Diffie-Hellman group 14 (MODP-2048).
    dh_group_15: str  # Diffie-Hellman group 15 (MODP-3072).
    dh_group_16: str  # Diffie-Hellman group 16 (MODP-4096).
    dh_group_17: str  # Diffie-Hellman group 17 (MODP-6144).
    dh_group_18: str  # Diffie-Hellman group 18 (MODP-8192).
    dh_group_19: str  # Diffie-Hellman group 19 (EC-P256).
    dh_group_20: str  # Diffie-Hellman group 20 (EC-P384).
    dh_group_21: str  # Diffie-Hellman group 21 (EC-P521).
    dh_group_27: str  # Diffie-Hellman group 27 (EC-P224BP).
    dh_group_28: str  # Diffie-Hellman group 28 (EC-P256BP).
    dh_group_29: str  # Diffie-Hellman group 29 (EC-P384BP).
    dh_group_30: str  # Diffie-Hellman group 30 (EC-P512BP).
    dh_group_31: str  # Diffie-Hellman group 31 (EC-X25519).
    dh_group_32: str  # Diffie-Hellman group 32 (EC-X448).

# Nested TypedDicts for table field children (dict mode)

# Nested classes for table field children (object mode)


# Response TypedDict for GET returns (all fields present in API response)
class IkeResponse(TypedDict):
    """
    Type hints for system/ike API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    embryonic_limit: int  # Maximum number of IPsec tunnels to negotiate simul | Default: 10000 | Min: 50 | Max: 20000
    dh_multiprocess: Literal["enable", "disable"]  # Enable/disable multiprocess Diffie-Hellman daemon | Default: enable
    dh_worker_count: int  # Number of Diffie-Hellman workers to start. | Default: 0 | Min: 1 | Max: 2
    dh_mode: Literal["software", "hardware"]  # Use software (CPU) or hardware (CPX) to perform Di | Default: software
    dh_keypair_cache: Literal["enable", "disable"]  # Enable/disable Diffie-Hellman key pair cache. | Default: enable
    dh_keypair_count: int  # Number of key pairs to pre-generate for each Diffi | Default: 100 | Min: 0 | Max: 50000
    dh_keypair_throttle: Literal["enable", "disable"]  # Enable/disable Diffie-Hellman key pair cache CPU t | Default: enable
    dh_group_1: str  # Diffie-Hellman group 1 (MODP-768).
    dh_group_2: str  # Diffie-Hellman group 2 (MODP-1024).
    dh_group_5: str  # Diffie-Hellman group 5 (MODP-1536).
    dh_group_14: str  # Diffie-Hellman group 14 (MODP-2048).
    dh_group_15: str  # Diffie-Hellman group 15 (MODP-3072).
    dh_group_16: str  # Diffie-Hellman group 16 (MODP-4096).
    dh_group_17: str  # Diffie-Hellman group 17 (MODP-6144).
    dh_group_18: str  # Diffie-Hellman group 18 (MODP-8192).
    dh_group_19: str  # Diffie-Hellman group 19 (EC-P256).
    dh_group_20: str  # Diffie-Hellman group 20 (EC-P384).
    dh_group_21: str  # Diffie-Hellman group 21 (EC-P521).
    dh_group_27: str  # Diffie-Hellman group 27 (EC-P224BP).
    dh_group_28: str  # Diffie-Hellman group 28 (EC-P256BP).
    dh_group_29: str  # Diffie-Hellman group 29 (EC-P384BP).
    dh_group_30: str  # Diffie-Hellman group 30 (EC-P512BP).
    dh_group_31: str  # Diffie-Hellman group 31 (EC-X25519).
    dh_group_32: str  # Diffie-Hellman group 32 (EC-X448).


@final
class IkeObject:
    """Typed FortiObject for system/ike with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Maximum number of IPsec tunnels to negotiate simultaneously. | Default: 10000 | Min: 50 | Max: 20000
    embryonic_limit: int
    # Enable/disable multiprocess Diffie-Hellman daemon for IKE. | Default: enable
    dh_multiprocess: Literal["enable", "disable"]
    # Number of Diffie-Hellman workers to start. | Default: 0 | Min: 1 | Max: 2
    dh_worker_count: int
    # Use software (CPU) or hardware (CPX) to perform Diffie-Hellm | Default: software
    dh_mode: Literal["software", "hardware"]
    # Enable/disable Diffie-Hellman key pair cache. | Default: enable
    dh_keypair_cache: Literal["enable", "disable"]
    # Number of key pairs to pre-generate for each Diffie-Hellman | Default: 100 | Min: 0 | Max: 50000
    dh_keypair_count: int
    # Enable/disable Diffie-Hellman key pair cache CPU throttling. | Default: enable
    dh_keypair_throttle: Literal["enable", "disable"]
    # Diffie-Hellman group 1 (MODP-768).
    dh_group_1: str
    # Diffie-Hellman group 2 (MODP-1024).
    dh_group_2: str
    # Diffie-Hellman group 5 (MODP-1536).
    dh_group_5: str
    # Diffie-Hellman group 14 (MODP-2048).
    dh_group_14: str
    # Diffie-Hellman group 15 (MODP-3072).
    dh_group_15: str
    # Diffie-Hellman group 16 (MODP-4096).
    dh_group_16: str
    # Diffie-Hellman group 17 (MODP-6144).
    dh_group_17: str
    # Diffie-Hellman group 18 (MODP-8192).
    dh_group_18: str
    # Diffie-Hellman group 19 (EC-P256).
    dh_group_19: str
    # Diffie-Hellman group 20 (EC-P384).
    dh_group_20: str
    # Diffie-Hellman group 21 (EC-P521).
    dh_group_21: str
    # Diffie-Hellman group 27 (EC-P224BP).
    dh_group_27: str
    # Diffie-Hellman group 28 (EC-P256BP).
    dh_group_28: str
    # Diffie-Hellman group 29 (EC-P384BP).
    dh_group_29: str
    # Diffie-Hellman group 30 (EC-P512BP).
    dh_group_30: str
    # Diffie-Hellman group 31 (EC-X25519).
    dh_group_31: str
    # Diffie-Hellman group 32 (EC-X448).
    dh_group_32: str
    
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
    def to_dict(self) -> IkePayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Ike:
    """
    Configure IKE global attributes.
    
    Path: system/ike
    Category: cmdb
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
    ) -> IkeObject: ...
    
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
    ) -> IkeObject: ...
    
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
    ) -> IkeObject: ...
    
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
    ) -> IkeObject: ...
    
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
    ) -> IkeObject: ...
    
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
    ) -> IkeObject: ...
    
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
    ) -> IkeObject: ...
    
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
    ) -> IkeObject: ...
    
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
    ) -> IkeObject: ...
    
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
    ) -> dict[str, Any] | FortiObject: ...
    
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
    ) -> IkeObject | dict[str, Any]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: IkePayload | None = ...,
        embryonic_limit: int | None = ...,
        dh_multiprocess: Literal["enable", "disable"] | None = ...,
        dh_worker_count: int | None = ...,
        dh_mode: Literal["software", "hardware"] | None = ...,
        dh_keypair_cache: Literal["enable", "disable"] | None = ...,
        dh_keypair_count: int | None = ...,
        dh_keypair_throttle: Literal["enable", "disable"] | None = ...,
        dh_group_1: str | None = ...,
        dh_group_2: str | None = ...,
        dh_group_5: str | None = ...,
        dh_group_14: str | None = ...,
        dh_group_15: str | None = ...,
        dh_group_16: str | None = ...,
        dh_group_17: str | None = ...,
        dh_group_18: str | None = ...,
        dh_group_19: str | None = ...,
        dh_group_20: str | None = ...,
        dh_group_21: str | None = ...,
        dh_group_27: str | None = ...,
        dh_group_28: str | None = ...,
        dh_group_29: str | None = ...,
        dh_group_30: str | None = ...,
        dh_group_31: str | None = ...,
        dh_group_32: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> IkeObject: ...
    
    @overload
    def put(
        self,
        payload_dict: IkePayload | None = ...,
        embryonic_limit: int | None = ...,
        dh_multiprocess: Literal["enable", "disable"] | None = ...,
        dh_worker_count: int | None = ...,
        dh_mode: Literal["software", "hardware"] | None = ...,
        dh_keypair_cache: Literal["enable", "disable"] | None = ...,
        dh_keypair_count: int | None = ...,
        dh_keypair_throttle: Literal["enable", "disable"] | None = ...,
        dh_group_1: str | None = ...,
        dh_group_2: str | None = ...,
        dh_group_5: str | None = ...,
        dh_group_14: str | None = ...,
        dh_group_15: str | None = ...,
        dh_group_16: str | None = ...,
        dh_group_17: str | None = ...,
        dh_group_18: str | None = ...,
        dh_group_19: str | None = ...,
        dh_group_20: str | None = ...,
        dh_group_21: str | None = ...,
        dh_group_27: str | None = ...,
        dh_group_28: str | None = ...,
        dh_group_29: str | None = ...,
        dh_group_30: str | None = ...,
        dh_group_31: str | None = ...,
        dh_group_32: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: IkePayload | None = ...,
        embryonic_limit: int | None = ...,
        dh_multiprocess: Literal["enable", "disable"] | None = ...,
        dh_worker_count: int | None = ...,
        dh_mode: Literal["software", "hardware"] | None = ...,
        dh_keypair_cache: Literal["enable", "disable"] | None = ...,
        dh_keypair_count: int | None = ...,
        dh_keypair_throttle: Literal["enable", "disable"] | None = ...,
        dh_group_1: str | None = ...,
        dh_group_2: str | None = ...,
        dh_group_5: str | None = ...,
        dh_group_14: str | None = ...,
        dh_group_15: str | None = ...,
        dh_group_16: str | None = ...,
        dh_group_17: str | None = ...,
        dh_group_18: str | None = ...,
        dh_group_19: str | None = ...,
        dh_group_20: str | None = ...,
        dh_group_21: str | None = ...,
        dh_group_27: str | None = ...,
        dh_group_28: str | None = ...,
        dh_group_29: str | None = ...,
        dh_group_30: str | None = ...,
        dh_group_31: str | None = ...,
        dh_group_32: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def put(
        self,
        payload_dict: IkePayload | None = ...,
        embryonic_limit: int | None = ...,
        dh_multiprocess: Literal["enable", "disable"] | None = ...,
        dh_worker_count: int | None = ...,
        dh_mode: Literal["software", "hardware"] | None = ...,
        dh_keypair_cache: Literal["enable", "disable"] | None = ...,
        dh_keypair_count: int | None = ...,
        dh_keypair_throttle: Literal["enable", "disable"] | None = ...,
        dh_group_1: str | None = ...,
        dh_group_2: str | None = ...,
        dh_group_5: str | None = ...,
        dh_group_14: str | None = ...,
        dh_group_15: str | None = ...,
        dh_group_16: str | None = ...,
        dh_group_17: str | None = ...,
        dh_group_18: str | None = ...,
        dh_group_19: str | None = ...,
        dh_group_20: str | None = ...,
        dh_group_21: str | None = ...,
        dh_group_27: str | None = ...,
        dh_group_28: str | None = ...,
        dh_group_29: str | None = ...,
        dh_group_30: str | None = ...,
        dh_group_31: str | None = ...,
        dh_group_32: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: IkePayload | None = ...,
        embryonic_limit: int | None = ...,
        dh_multiprocess: Literal["enable", "disable"] | None = ...,
        dh_worker_count: int | None = ...,
        dh_mode: Literal["software", "hardware"] | None = ...,
        dh_keypair_cache: Literal["enable", "disable"] | None = ...,
        dh_keypair_count: int | None = ...,
        dh_keypair_throttle: Literal["enable", "disable"] | None = ...,
        dh_group_1: str | None = ...,
        dh_group_2: str | None = ...,
        dh_group_5: str | None = ...,
        dh_group_14: str | None = ...,
        dh_group_15: str | None = ...,
        dh_group_16: str | None = ...,
        dh_group_17: str | None = ...,
        dh_group_18: str | None = ...,
        dh_group_19: str | None = ...,
        dh_group_20: str | None = ...,
        dh_group_21: str | None = ...,
        dh_group_27: str | None = ...,
        dh_group_28: str | None = ...,
        dh_group_29: str | None = ...,
        dh_group_30: str | None = ...,
        dh_group_31: str | None = ...,
        dh_group_32: str | None = ...,
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
    "Ike",
    "IkePayload",
    "IkeResponse",
    "IkeObject",
]