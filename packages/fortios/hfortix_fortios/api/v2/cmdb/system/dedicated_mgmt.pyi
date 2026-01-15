from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList
from hfortix_core.types import MutationResponse

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class DedicatedMgmtPayload(TypedDict, total=False):
    """
    Type hints for system/dedicated_mgmt payload fields.
    
    Configure dedicated management.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.system.interface.InterfaceEndpoint` (via: interface)

    **Usage:**
        payload: DedicatedMgmtPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    status: Literal["enable", "disable"]  # Enable/disable dedicated management. | Default: disable
    interface: str  # Dedicated management interface. | MaxLen: 15
    default_gateway: str  # Default gateway for dedicated management interface | Default: 0.0.0.0
    dhcp_server: Literal["enable", "disable"]  # Enable/disable DHCP server on management interface | Default: disable
    dhcp_netmask: str  # DHCP netmask. | Default: 0.0.0.0
    dhcp_start_ip: str  # DHCP start IP for dedicated management. | Default: 0.0.0.0
    dhcp_end_ip: str  # DHCP end IP for dedicated management. | Default: 0.0.0.0

# Nested TypedDicts for table field children (dict mode)

# Nested classes for table field children (object mode)


# Response TypedDict for GET returns (all fields present in API response)
class DedicatedMgmtResponse(TypedDict):
    """
    Type hints for system/dedicated_mgmt API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    status: Literal["enable", "disable"]  # Enable/disable dedicated management. | Default: disable
    interface: str  # Dedicated management interface. | MaxLen: 15
    default_gateway: str  # Default gateway for dedicated management interface | Default: 0.0.0.0
    dhcp_server: Literal["enable", "disable"]  # Enable/disable DHCP server on management interface | Default: disable
    dhcp_netmask: str  # DHCP netmask. | Default: 0.0.0.0
    dhcp_start_ip: str  # DHCP start IP for dedicated management. | Default: 0.0.0.0
    dhcp_end_ip: str  # DHCP end IP for dedicated management. | Default: 0.0.0.0


@final
class DedicatedMgmtObject:
    """Typed FortiObject for system/dedicated_mgmt with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Enable/disable dedicated management. | Default: disable
    status: Literal["enable", "disable"]
    # Dedicated management interface. | MaxLen: 15
    interface: str
    # Default gateway for dedicated management interface. | Default: 0.0.0.0
    default_gateway: str
    # Enable/disable DHCP server on management interface. | Default: disable
    dhcp_server: Literal["enable", "disable"]
    # DHCP netmask. | Default: 0.0.0.0
    dhcp_netmask: str
    # DHCP start IP for dedicated management. | Default: 0.0.0.0
    dhcp_start_ip: str
    # DHCP end IP for dedicated management. | Default: 0.0.0.0
    dhcp_end_ip: str
    
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
    def to_dict(self) -> DedicatedMgmtPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class DedicatedMgmt:
    """
    Configure dedicated management.
    
    Path: system/dedicated_mgmt
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
    ) -> DedicatedMgmtObject: ...
    
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
    ) -> DedicatedMgmtObject: ...
    
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
    ) -> DedicatedMgmtObject: ...
    
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
    ) -> DedicatedMgmtObject: ...
    
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
    ) -> DedicatedMgmtObject: ...
    
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
    ) -> DedicatedMgmtObject: ...
    
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
    ) -> DedicatedMgmtObject: ...
    
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
    ) -> DedicatedMgmtObject: ...
    
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
    ) -> DedicatedMgmtObject: ...
    
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
    ) -> DedicatedMgmtObject | dict[str, Any]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: DedicatedMgmtPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        interface: str | None = ...,
        default_gateway: str | None = ...,
        dhcp_server: Literal["enable", "disable"] | None = ...,
        dhcp_netmask: str | None = ...,
        dhcp_start_ip: str | None = ...,
        dhcp_end_ip: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> DedicatedMgmtObject: ...
    
    @overload
    def put(
        self,
        payload_dict: DedicatedMgmtPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        interface: str | None = ...,
        default_gateway: str | None = ...,
        dhcp_server: Literal["enable", "disable"] | None = ...,
        dhcp_netmask: str | None = ...,
        dhcp_start_ip: str | None = ...,
        dhcp_end_ip: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: DedicatedMgmtPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        interface: str | None = ...,
        default_gateway: str | None = ...,
        dhcp_server: Literal["enable", "disable"] | None = ...,
        dhcp_netmask: str | None = ...,
        dhcp_start_ip: str | None = ...,
        dhcp_end_ip: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def put(
        self,
        payload_dict: DedicatedMgmtPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        interface: str | None = ...,
        default_gateway: str | None = ...,
        dhcp_server: Literal["enable", "disable"] | None = ...,
        dhcp_netmask: str | None = ...,
        dhcp_start_ip: str | None = ...,
        dhcp_end_ip: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: DedicatedMgmtPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        interface: str | None = ...,
        default_gateway: str | None = ...,
        dhcp_server: Literal["enable", "disable"] | None = ...,
        dhcp_netmask: str | None = ...,
        dhcp_start_ip: str | None = ...,
        dhcp_end_ip: str | None = ...,
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
    "DedicatedMgmt",
    "DedicatedMgmtPayload",
    "DedicatedMgmtResponse",
    "DedicatedMgmtObject",
]