from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class L2tpPayload(TypedDict, total=False):
    """
    Type hints for vpn/l2tp payload fields.
    
    Configure L2TP.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.user.group.GroupEndpoint` (via: usrgrp)

    **Usage:**
        payload: L2tpPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    status: Literal["enable", "disable"]  # Enable/disable FortiGate as a L2TP gateway. | Default: disable
    eip: str  # End IP. | Default: 0.0.0.0
    sip: str  # Start IP. | Default: 0.0.0.0
    usrgrp: str  # User group. | MaxLen: 35
    enforce_ipsec: Literal["enable", "disable"]  # Enable/disable IPsec enforcement. | Default: disable
    lcp_echo_interval: int  # Time in seconds between PPPoE Link Control Protoco | Default: 5 | Min: 0 | Max: 32767
    lcp_max_echo_fails: int  # Maximum number of missed LCP echo messages before | Default: 3 | Min: 0 | Max: 32767
    hello_interval: int  # L2TP hello message interval in seconds | Default: 60 | Min: 0 | Max: 3600
    compress: Literal["enable", "disable"]  # Enable/disable data compression. | Default: disable

# Nested TypedDicts for table field children (dict mode)

# Nested classes for table field children (object mode)


# Response TypedDict for GET returns (all fields present in API response)
class L2tpResponse(TypedDict):
    """
    Type hints for vpn/l2tp API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    status: Literal["enable", "disable"]  # Enable/disable FortiGate as a L2TP gateway. | Default: disable
    eip: str  # End IP. | Default: 0.0.0.0
    sip: str  # Start IP. | Default: 0.0.0.0
    usrgrp: str  # User group. | MaxLen: 35
    enforce_ipsec: Literal["enable", "disable"]  # Enable/disable IPsec enforcement. | Default: disable
    lcp_echo_interval: int  # Time in seconds between PPPoE Link Control Protoco | Default: 5 | Min: 0 | Max: 32767
    lcp_max_echo_fails: int  # Maximum number of missed LCP echo messages before | Default: 3 | Min: 0 | Max: 32767
    hello_interval: int  # L2TP hello message interval in seconds | Default: 60 | Min: 0 | Max: 3600
    compress: Literal["enable", "disable"]  # Enable/disable data compression. | Default: disable


@final
class L2tpObject:
    """Typed FortiObject for vpn/l2tp with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Enable/disable FortiGate as a L2TP gateway. | Default: disable
    status: Literal["enable", "disable"]
    # End IP. | Default: 0.0.0.0
    eip: str
    # Start IP. | Default: 0.0.0.0
    sip: str
    # User group. | MaxLen: 35
    usrgrp: str
    # Enable/disable IPsec enforcement. | Default: disable
    enforce_ipsec: Literal["enable", "disable"]
    # Time in seconds between PPPoE Link Control Protocol (LCP) ec | Default: 5 | Min: 0 | Max: 32767
    lcp_echo_interval: int
    # Maximum number of missed LCP echo messages before disconnect | Default: 3 | Min: 0 | Max: 32767
    lcp_max_echo_fails: int
    # L2TP hello message interval in seconds | Default: 60 | Min: 0 | Max: 3600
    hello_interval: int
    # Enable/disable data compression. | Default: disable
    compress: Literal["enable", "disable"]
    
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
    def to_dict(self) -> L2tpPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class L2tp:
    """
    Configure L2TP.
    
    Path: vpn/l2tp
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
    ) -> L2tpObject: ...
    
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
    ) -> L2tpObject: ...
    
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
    ) -> L2tpObject: ...
    
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
    ) -> L2tpObject: ...
    
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
    ) -> L2tpObject: ...
    
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
    ) -> L2tpObject: ...
    
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
    ) -> L2tpObject: ...
    
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
    ) -> L2tpObject: ...
    
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
    ) -> L2tpObject: ...
    
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
    ) -> L2tpObject | dict[str, Any]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: L2tpPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        eip: str | None = ...,
        sip: str | None = ...,
        usrgrp: str | None = ...,
        enforce_ipsec: Literal["enable", "disable"] | None = ...,
        lcp_echo_interval: int | None = ...,
        lcp_max_echo_fails: int | None = ...,
        hello_interval: int | None = ...,
        compress: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> L2tpObject: ...
    
    @overload
    def put(
        self,
        payload_dict: L2tpPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        eip: str | None = ...,
        sip: str | None = ...,
        usrgrp: str | None = ...,
        enforce_ipsec: Literal["enable", "disable"] | None = ...,
        lcp_echo_interval: int | None = ...,
        lcp_max_echo_fails: int | None = ...,
        hello_interval: int | None = ...,
        compress: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: L2tpPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        eip: str | None = ...,
        sip: str | None = ...,
        usrgrp: str | None = ...,
        enforce_ipsec: Literal["enable", "disable"] | None = ...,
        lcp_echo_interval: int | None = ...,
        lcp_max_echo_fails: int | None = ...,
        hello_interval: int | None = ...,
        compress: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def put(
        self,
        payload_dict: L2tpPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        eip: str | None = ...,
        sip: str | None = ...,
        usrgrp: str | None = ...,
        enforce_ipsec: Literal["enable", "disable"] | None = ...,
        lcp_echo_interval: int | None = ...,
        lcp_max_echo_fails: int | None = ...,
        hello_interval: int | None = ...,
        compress: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: L2tpPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        eip: str | None = ...,
        sip: str | None = ...,
        usrgrp: str | None = ...,
        enforce_ipsec: Literal["enable", "disable"] | None = ...,
        lcp_echo_interval: int | None = ...,
        lcp_max_echo_fails: int | None = ...,
        hello_interval: int | None = ...,
        compress: Literal["enable", "disable"] | None = ...,
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
    "L2tp",
    "L2tpPayload",
    "L2tpResponse",
    "L2tpObject",
]