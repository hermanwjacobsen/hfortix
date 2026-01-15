from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class MacPolicyPayload(TypedDict, total=False):
    """
    Type hints for switch_controller/mac_policy payload fields.
    
    Configure MAC policy to be applied on the managed FortiSwitch devices through NAC device.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.switch-controller.traffic-policy.TrafficPolicyEndpoint` (via: traffic-policy)
        - :class:`~.system.interface.InterfaceEndpoint` (via: fortilink, vlan)

    **Usage:**
        payload: MacPolicyPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # MAC policy name. | MaxLen: 63
    description: str  # Description for the MAC policy. | MaxLen: 63
    fortilink: str  # FortiLink interface for which this MAC policy belo | MaxLen: 15
    vlan: str  # Ingress traffic VLAN assignment for the MAC addres | MaxLen: 15
    traffic_policy: str  # Traffic policy to be applied when using this MAC p | MaxLen: 63
    count: Literal["disable", "enable"]  # Enable/disable packet count on the NAC device. | Default: disable
    bounce_port_link: Literal["disable", "enable"]  # Enable/disable bouncing | Default: enable
    bounce_port_duration: int  # Bounce duration in seconds of a switch port where | Default: 5 | Min: 1 | Max: 30
    poe_reset: Literal["disable", "enable"]  # Enable/disable POE reset of a switch port where th | Default: disable

# Nested TypedDicts for table field children (dict mode)

# Nested classes for table field children (object mode)


# Response TypedDict for GET returns (all fields present in API response)
class MacPolicyResponse(TypedDict):
    """
    Type hints for switch_controller/mac_policy API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str  # MAC policy name. | MaxLen: 63
    description: str  # Description for the MAC policy. | MaxLen: 63
    fortilink: str  # FortiLink interface for which this MAC policy belo | MaxLen: 15
    vlan: str  # Ingress traffic VLAN assignment for the MAC addres | MaxLen: 15
    traffic_policy: str  # Traffic policy to be applied when using this MAC p | MaxLen: 63
    count: Literal["disable", "enable"]  # Enable/disable packet count on the NAC device. | Default: disable
    bounce_port_link: Literal["disable", "enable"]  # Enable/disable bouncing | Default: enable
    bounce_port_duration: int  # Bounce duration in seconds of a switch port where | Default: 5 | Min: 1 | Max: 30
    poe_reset: Literal["disable", "enable"]  # Enable/disable POE reset of a switch port where th | Default: disable


@final
class MacPolicyObject:
    """Typed FortiObject for switch_controller/mac_policy with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # MAC policy name. | MaxLen: 63
    name: str
    # Description for the MAC policy. | MaxLen: 63
    description: str
    # FortiLink interface for which this MAC policy belongs to. | MaxLen: 15
    fortilink: str
    # Ingress traffic VLAN assignment for the MAC address matching | MaxLen: 15
    vlan: str
    # Traffic policy to be applied when using this MAC policy. | MaxLen: 63
    traffic_policy: str
    # Enable/disable packet count on the NAC device. | Default: disable
    count: Literal["disable", "enable"]
    # Enable/disable bouncing | Default: enable
    bounce_port_link: Literal["disable", "enable"]
    # Bounce duration in seconds of a switch port where this mac-p | Default: 5 | Min: 1 | Max: 30
    bounce_port_duration: int
    # Enable/disable POE reset of a switch port where this mac-pol | Default: disable
    poe_reset: Literal["disable", "enable"]
    
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
    def to_dict(self) -> MacPolicyPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class MacPolicy:
    """
    Configure MAC policy to be applied on the managed FortiSwitch devices through NAC device.
    
    Path: switch_controller/mac_policy
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
    ) -> MacPolicyObject: ...
    
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
    ) -> MacPolicyObject: ...
    
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
    ) -> FortiObjectList[MacPolicyObject]: ...
    
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
    ) -> MacPolicyObject: ...
    
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
    ) -> MacPolicyObject: ...
    
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
    ) -> FortiObjectList[MacPolicyObject]: ...
    
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
    ) -> MacPolicyObject: ...
    
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
    ) -> MacPolicyObject: ...
    
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
    ) -> FortiObjectList[MacPolicyObject]: ...
    
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
    ) -> MacPolicyObject | list[MacPolicyObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: MacPolicyPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        fortilink: str | None = ...,
        vlan: str | None = ...,
        traffic_policy: str | None = ...,
        count: Literal["disable", "enable"] | None = ...,
        bounce_port_link: Literal["disable", "enable"] | None = ...,
        bounce_port_duration: int | None = ...,
        poe_reset: Literal["disable", "enable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MacPolicyObject: ...
    
    @overload
    def post(
        self,
        payload_dict: MacPolicyPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        fortilink: str | None = ...,
        vlan: str | None = ...,
        traffic_policy: str | None = ...,
        count: Literal["disable", "enable"] | None = ...,
        bounce_port_link: Literal["disable", "enable"] | None = ...,
        bounce_port_duration: int | None = ...,
        poe_reset: Literal["disable", "enable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: MacPolicyPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        fortilink: str | None = ...,
        vlan: str | None = ...,
        traffic_policy: str | None = ...,
        count: Literal["disable", "enable"] | None = ...,
        bounce_port_link: Literal["disable", "enable"] | None = ...,
        bounce_port_duration: int | None = ...,
        poe_reset: Literal["disable", "enable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def post(
        self,
        payload_dict: MacPolicyPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        fortilink: str | None = ...,
        vlan: str | None = ...,
        traffic_policy: str | None = ...,
        count: Literal["disable", "enable"] | None = ...,
        bounce_port_link: Literal["disable", "enable"] | None = ...,
        bounce_port_duration: int | None = ...,
        poe_reset: Literal["disable", "enable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: MacPolicyPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        fortilink: str | None = ...,
        vlan: str | None = ...,
        traffic_policy: str | None = ...,
        count: Literal["disable", "enable"] | None = ...,
        bounce_port_link: Literal["disable", "enable"] | None = ...,
        bounce_port_duration: int | None = ...,
        poe_reset: Literal["disable", "enable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MacPolicyObject: ...
    
    @overload
    def put(
        self,
        payload_dict: MacPolicyPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        fortilink: str | None = ...,
        vlan: str | None = ...,
        traffic_policy: str | None = ...,
        count: Literal["disable", "enable"] | None = ...,
        bounce_port_link: Literal["disable", "enable"] | None = ...,
        bounce_port_duration: int | None = ...,
        poe_reset: Literal["disable", "enable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: MacPolicyPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        fortilink: str | None = ...,
        vlan: str | None = ...,
        traffic_policy: str | None = ...,
        count: Literal["disable", "enable"] | None = ...,
        bounce_port_link: Literal["disable", "enable"] | None = ...,
        bounce_port_duration: int | None = ...,
        poe_reset: Literal["disable", "enable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def put(
        self,
        payload_dict: MacPolicyPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        fortilink: str | None = ...,
        vlan: str | None = ...,
        traffic_policy: str | None = ...,
        count: Literal["disable", "enable"] | None = ...,
        bounce_port_link: Literal["disable", "enable"] | None = ...,
        bounce_port_duration: int | None = ...,
        poe_reset: Literal["disable", "enable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> MacPolicyObject: ...
    
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
        payload_dict: MacPolicyPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        fortilink: str | None = ...,
        vlan: str | None = ...,
        traffic_policy: str | None = ...,
        count: Literal["disable", "enable"] | None = ...,
        bounce_port_link: Literal["disable", "enable"] | None = ...,
        bounce_port_duration: int | None = ...,
        poe_reset: Literal["disable", "enable"] | None = ...,
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
    "MacPolicy",
    "MacPolicyPayload",
    "MacPolicyResponse",
    "MacPolicyObject",
]