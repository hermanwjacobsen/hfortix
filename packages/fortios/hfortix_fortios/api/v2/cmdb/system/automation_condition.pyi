from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class AutomationConditionPayload(TypedDict, total=False):
    """
    Type hints for system/automation_condition payload fields.
    
    Condition for automation stitches.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.system.vdom.VdomEndpoint` (via: vdom)

    **Usage:**
        payload: AutomationConditionPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # Name. | MaxLen: 35
    description: str  # Description. | MaxLen: 255
    condition_type: Literal["cpu", "memory", "vpn"]  # Condition type. | Default: cpu
    cpu_usage_percent: int  # CPU usage reaches specified percentage. | Default: 0 | Min: 0 | Max: 100
    mem_usage_percent: int  # Memory usage reaches specified percentage. | Default: 0 | Min: 0 | Max: 100
    vdom: str  # Virtual domain which the tunnel belongs to. | Default: root | MaxLen: 31
    vpn_tunnel_name: str  # VPN tunnel name. | MaxLen: 79
    vpn_tunnel_state: Literal["tunnel-up", "tunnel-down"]  # VPN tunnel state. | Default: tunnel-up

# Nested TypedDicts for table field children (dict mode)

# Nested classes for table field children (object mode)


# Response TypedDict for GET returns (all fields present in API response)
class AutomationConditionResponse(TypedDict):
    """
    Type hints for system/automation_condition API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str  # Name. | MaxLen: 35
    description: str  # Description. | MaxLen: 255
    condition_type: Literal["cpu", "memory", "vpn"]  # Condition type. | Default: cpu
    cpu_usage_percent: int  # CPU usage reaches specified percentage. | Default: 0 | Min: 0 | Max: 100
    mem_usage_percent: int  # Memory usage reaches specified percentage. | Default: 0 | Min: 0 | Max: 100
    vdom: str  # Virtual domain which the tunnel belongs to. | Default: root | MaxLen: 31
    vpn_tunnel_name: str  # VPN tunnel name. | MaxLen: 79
    vpn_tunnel_state: Literal["tunnel-up", "tunnel-down"]  # VPN tunnel state. | Default: tunnel-up


@final
class AutomationConditionObject:
    """Typed FortiObject for system/automation_condition with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Name. | MaxLen: 35
    name: str
    # Description. | MaxLen: 255
    description: str
    # Condition type. | Default: cpu
    condition_type: Literal["cpu", "memory", "vpn"]
    # CPU usage reaches specified percentage. | Default: 0 | Min: 0 | Max: 100
    cpu_usage_percent: int
    # Memory usage reaches specified percentage. | Default: 0 | Min: 0 | Max: 100
    mem_usage_percent: int
    # Virtual domain which the tunnel belongs to. | Default: root | MaxLen: 31
    vdom: str
    # VPN tunnel name. | MaxLen: 79
    vpn_tunnel_name: str
    # VPN tunnel state. | Default: tunnel-up
    vpn_tunnel_state: Literal["tunnel-up", "tunnel-down"]
    
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
    def to_dict(self) -> AutomationConditionPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class AutomationCondition:
    """
    Condition for automation stitches.
    
    Path: system/automation_condition
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
    ) -> AutomationConditionObject: ...
    
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
    ) -> AutomationConditionObject: ...
    
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
    ) -> FortiObjectList[AutomationConditionObject]: ...
    
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
    ) -> AutomationConditionObject: ...
    
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
    ) -> AutomationConditionObject: ...
    
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
    ) -> FortiObjectList[AutomationConditionObject]: ...
    
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
    ) -> AutomationConditionObject: ...
    
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
    ) -> AutomationConditionObject: ...
    
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
    ) -> FortiObjectList[AutomationConditionObject]: ...
    
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
    ) -> AutomationConditionObject | list[AutomationConditionObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: AutomationConditionPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        condition_type: Literal["cpu", "memory", "vpn"] | None = ...,
        cpu_usage_percent: int | None = ...,
        mem_usage_percent: int | None = ...,
        vpn_tunnel_name: str | None = ...,
        vpn_tunnel_state: Literal["tunnel-up", "tunnel-down"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> AutomationConditionObject: ...
    
    @overload
    def post(
        self,
        payload_dict: AutomationConditionPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        condition_type: Literal["cpu", "memory", "vpn"] | None = ...,
        cpu_usage_percent: int | None = ...,
        mem_usage_percent: int | None = ...,
        vpn_tunnel_name: str | None = ...,
        vpn_tunnel_state: Literal["tunnel-up", "tunnel-down"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: AutomationConditionPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        condition_type: Literal["cpu", "memory", "vpn"] | None = ...,
        cpu_usage_percent: int | None = ...,
        mem_usage_percent: int | None = ...,
        vpn_tunnel_name: str | None = ...,
        vpn_tunnel_state: Literal["tunnel-up", "tunnel-down"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def post(
        self,
        payload_dict: AutomationConditionPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        condition_type: Literal["cpu", "memory", "vpn"] | None = ...,
        cpu_usage_percent: int | None = ...,
        mem_usage_percent: int | None = ...,
        vpn_tunnel_name: str | None = ...,
        vpn_tunnel_state: Literal["tunnel-up", "tunnel-down"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: AutomationConditionPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        condition_type: Literal["cpu", "memory", "vpn"] | None = ...,
        cpu_usage_percent: int | None = ...,
        mem_usage_percent: int | None = ...,
        vpn_tunnel_name: str | None = ...,
        vpn_tunnel_state: Literal["tunnel-up", "tunnel-down"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> AutomationConditionObject: ...
    
    @overload
    def put(
        self,
        payload_dict: AutomationConditionPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        condition_type: Literal["cpu", "memory", "vpn"] | None = ...,
        cpu_usage_percent: int | None = ...,
        mem_usage_percent: int | None = ...,
        vpn_tunnel_name: str | None = ...,
        vpn_tunnel_state: Literal["tunnel-up", "tunnel-down"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: AutomationConditionPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        condition_type: Literal["cpu", "memory", "vpn"] | None = ...,
        cpu_usage_percent: int | None = ...,
        mem_usage_percent: int | None = ...,
        vpn_tunnel_name: str | None = ...,
        vpn_tunnel_state: Literal["tunnel-up", "tunnel-down"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def put(
        self,
        payload_dict: AutomationConditionPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        condition_type: Literal["cpu", "memory", "vpn"] | None = ...,
        cpu_usage_percent: int | None = ...,
        mem_usage_percent: int | None = ...,
        vpn_tunnel_name: str | None = ...,
        vpn_tunnel_state: Literal["tunnel-up", "tunnel-down"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> AutomationConditionObject: ...
    
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
        payload_dict: AutomationConditionPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        condition_type: Literal["cpu", "memory", "vpn"] | None = ...,
        cpu_usage_percent: int | None = ...,
        mem_usage_percent: int | None = ...,
        vpn_tunnel_name: str | None = ...,
        vpn_tunnel_state: Literal["tunnel-up", "tunnel-down"] | None = ...,
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
    "AutomationCondition",
    "AutomationConditionPayload",
    "AutomationConditionResponse",
    "AutomationConditionObject",
]