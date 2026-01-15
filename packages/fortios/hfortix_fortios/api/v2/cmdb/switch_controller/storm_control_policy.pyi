from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class StormControlPolicyPayload(TypedDict, total=False):
    """
    Type hints for switch_controller/storm_control_policy payload fields.
    
    Configure FortiSwitch storm control policy to be applied on managed-switch ports.
    
    **Usage:**
        payload: StormControlPolicyPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # Storm control policy name. | MaxLen: 63
    description: str  # Description of the storm control policy. | MaxLen: 63
    storm_control_mode: Literal["global", "override", "disabled"]  # Set Storm control mode. | Default: global
    rate: int  # Threshold rate in packets per second at which stor | Default: 500 | Min: 0 | Max: 10000000
    burst_size_level: int  # Increase level to handle bursty traffic | Default: 0 | Min: 0 | Max: 4
    unknown_unicast: Literal["enable", "disable"]  # Enable/disable storm control to drop/allow unknown | Default: disable
    unknown_multicast: Literal["enable", "disable"]  # Enable/disable storm control to drop/allow unknown | Default: disable
    broadcast: Literal["enable", "disable"]  # Enable/disable storm control to drop/allow broadca | Default: disable

# Nested TypedDicts for table field children (dict mode)

# Nested classes for table field children (object mode)


# Response TypedDict for GET returns (all fields present in API response)
class StormControlPolicyResponse(TypedDict):
    """
    Type hints for switch_controller/storm_control_policy API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str  # Storm control policy name. | MaxLen: 63
    description: str  # Description of the storm control policy. | MaxLen: 63
    storm_control_mode: Literal["global", "override", "disabled"]  # Set Storm control mode. | Default: global
    rate: int  # Threshold rate in packets per second at which stor | Default: 500 | Min: 0 | Max: 10000000
    burst_size_level: int  # Increase level to handle bursty traffic | Default: 0 | Min: 0 | Max: 4
    unknown_unicast: Literal["enable", "disable"]  # Enable/disable storm control to drop/allow unknown | Default: disable
    unknown_multicast: Literal["enable", "disable"]  # Enable/disable storm control to drop/allow unknown | Default: disable
    broadcast: Literal["enable", "disable"]  # Enable/disable storm control to drop/allow broadca | Default: disable


@final
class StormControlPolicyObject:
    """Typed FortiObject for switch_controller/storm_control_policy with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Storm control policy name. | MaxLen: 63
    name: str
    # Description of the storm control policy. | MaxLen: 63
    description: str
    # Set Storm control mode. | Default: global
    storm_control_mode: Literal["global", "override", "disabled"]
    # Threshold rate in packets per second at which storm traffic | Default: 500 | Min: 0 | Max: 10000000
    rate: int
    # Increase level to handle bursty traffic (0 - 4, default = 0) | Default: 0 | Min: 0 | Max: 4
    burst_size_level: int
    # Enable/disable storm control to drop/allow unknown unicast t | Default: disable
    unknown_unicast: Literal["enable", "disable"]
    # Enable/disable storm control to drop/allow unknown multicast | Default: disable
    unknown_multicast: Literal["enable", "disable"]
    # Enable/disable storm control to drop/allow broadcast traffic | Default: disable
    broadcast: Literal["enable", "disable"]
    
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
    def to_dict(self) -> StormControlPolicyPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class StormControlPolicy:
    """
    Configure FortiSwitch storm control policy to be applied on managed-switch ports.
    
    Path: switch_controller/storm_control_policy
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
    ) -> StormControlPolicyObject: ...
    
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
    ) -> StormControlPolicyObject: ...
    
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
    ) -> FortiObjectList[StormControlPolicyObject]: ...
    
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
    ) -> StormControlPolicyObject: ...
    
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
    ) -> StormControlPolicyObject: ...
    
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
    ) -> FortiObjectList[StormControlPolicyObject]: ...
    
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
    ) -> StormControlPolicyObject: ...
    
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
    ) -> StormControlPolicyObject: ...
    
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
    ) -> FortiObjectList[StormControlPolicyObject]: ...
    
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
    ) -> StormControlPolicyObject | list[StormControlPolicyObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: StormControlPolicyPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        storm_control_mode: Literal["global", "override", "disabled"] | None = ...,
        rate: int | None = ...,
        burst_size_level: int | None = ...,
        unknown_unicast: Literal["enable", "disable"] | None = ...,
        unknown_multicast: Literal["enable", "disable"] | None = ...,
        broadcast: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> StormControlPolicyObject: ...
    
    @overload
    def post(
        self,
        payload_dict: StormControlPolicyPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        storm_control_mode: Literal["global", "override", "disabled"] | None = ...,
        rate: int | None = ...,
        burst_size_level: int | None = ...,
        unknown_unicast: Literal["enable", "disable"] | None = ...,
        unknown_multicast: Literal["enable", "disable"] | None = ...,
        broadcast: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: StormControlPolicyPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        storm_control_mode: Literal["global", "override", "disabled"] | None = ...,
        rate: int | None = ...,
        burst_size_level: int | None = ...,
        unknown_unicast: Literal["enable", "disable"] | None = ...,
        unknown_multicast: Literal["enable", "disable"] | None = ...,
        broadcast: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def post(
        self,
        payload_dict: StormControlPolicyPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        storm_control_mode: Literal["global", "override", "disabled"] | None = ...,
        rate: int | None = ...,
        burst_size_level: int | None = ...,
        unknown_unicast: Literal["enable", "disable"] | None = ...,
        unknown_multicast: Literal["enable", "disable"] | None = ...,
        broadcast: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: StormControlPolicyPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        storm_control_mode: Literal["global", "override", "disabled"] | None = ...,
        rate: int | None = ...,
        burst_size_level: int | None = ...,
        unknown_unicast: Literal["enable", "disable"] | None = ...,
        unknown_multicast: Literal["enable", "disable"] | None = ...,
        broadcast: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> StormControlPolicyObject: ...
    
    @overload
    def put(
        self,
        payload_dict: StormControlPolicyPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        storm_control_mode: Literal["global", "override", "disabled"] | None = ...,
        rate: int | None = ...,
        burst_size_level: int | None = ...,
        unknown_unicast: Literal["enable", "disable"] | None = ...,
        unknown_multicast: Literal["enable", "disable"] | None = ...,
        broadcast: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: StormControlPolicyPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        storm_control_mode: Literal["global", "override", "disabled"] | None = ...,
        rate: int | None = ...,
        burst_size_level: int | None = ...,
        unknown_unicast: Literal["enable", "disable"] | None = ...,
        unknown_multicast: Literal["enable", "disable"] | None = ...,
        broadcast: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def put(
        self,
        payload_dict: StormControlPolicyPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        storm_control_mode: Literal["global", "override", "disabled"] | None = ...,
        rate: int | None = ...,
        burst_size_level: int | None = ...,
        unknown_unicast: Literal["enable", "disable"] | None = ...,
        unknown_multicast: Literal["enable", "disable"] | None = ...,
        broadcast: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> StormControlPolicyObject: ...
    
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
        payload_dict: StormControlPolicyPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        storm_control_mode: Literal["global", "override", "disabled"] | None = ...,
        rate: int | None = ...,
        burst_size_level: int | None = ...,
        unknown_unicast: Literal["enable", "disable"] | None = ...,
        unknown_multicast: Literal["enable", "disable"] | None = ...,
        broadcast: Literal["enable", "disable"] | None = ...,
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
    "StormControlPolicy",
    "StormControlPolicyPayload",
    "StormControlPolicyResponse",
    "StormControlPolicyObject",
]