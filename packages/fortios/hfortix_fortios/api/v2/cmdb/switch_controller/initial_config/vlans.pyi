from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList
from hfortix_core.types import MutationResponse

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class VlansPayload(TypedDict, total=False):
    """
    Type hints for switch_controller/initial_config/vlans payload fields.
    
    Configure initial template for auto-generated VLAN interfaces.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.switch-controller.initial-config.template.TemplateEndpoint` (via: default-vlan, nac, nac-segment, +4 more)

    **Usage:**
        payload: VlansPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    optional_vlans: Literal["enable", "disable"]  # Auto-generate pre-configured VLANs upon switch dis | Default: enable
    default_vlan: str  # Default VLAN (native) assigned to all switch ports | Default: _default | MaxLen: 63
    quarantine: str  # VLAN for quarantined traffic. | Default: quarantine | MaxLen: 63
    rspan: str  # VLAN for RSPAN/ERSPAN mirrored traffic. | Default: rspan | MaxLen: 63
    voice: str  # VLAN dedicated for voice devices. | Default: voice | MaxLen: 63
    video: str  # VLAN dedicated for video devices. | Default: video | MaxLen: 63
    nac: str  # VLAN for NAC onboarding devices. | Default: onboarding | MaxLen: 63
    nac_segment: str  # VLAN for NAC segment primary interface. | Default: nac_segment | MaxLen: 63

# Nested TypedDicts for table field children (dict mode)

# Nested classes for table field children (object mode)


# Response TypedDict for GET returns (all fields present in API response)
class VlansResponse(TypedDict):
    """
    Type hints for switch_controller/initial_config/vlans API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    optional_vlans: Literal["enable", "disable"]  # Auto-generate pre-configured VLANs upon switch dis | Default: enable
    default_vlan: str  # Default VLAN (native) assigned to all switch ports | Default: _default | MaxLen: 63
    quarantine: str  # VLAN for quarantined traffic. | Default: quarantine | MaxLen: 63
    rspan: str  # VLAN for RSPAN/ERSPAN mirrored traffic. | Default: rspan | MaxLen: 63
    voice: str  # VLAN dedicated for voice devices. | Default: voice | MaxLen: 63
    video: str  # VLAN dedicated for video devices. | Default: video | MaxLen: 63
    nac: str  # VLAN for NAC onboarding devices. | Default: onboarding | MaxLen: 63
    nac_segment: str  # VLAN for NAC segment primary interface. | Default: nac_segment | MaxLen: 63


@final
class VlansObject:
    """Typed FortiObject for switch_controller/initial_config/vlans with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Auto-generate pre-configured VLANs upon switch discovery. | Default: enable
    optional_vlans: Literal["enable", "disable"]
    # Default VLAN (native) assigned to all switch ports upon disc | Default: _default | MaxLen: 63
    default_vlan: str
    # VLAN for quarantined traffic. | Default: quarantine | MaxLen: 63
    quarantine: str
    # VLAN for RSPAN/ERSPAN mirrored traffic. | Default: rspan | MaxLen: 63
    rspan: str
    # VLAN dedicated for voice devices. | Default: voice | MaxLen: 63
    voice: str
    # VLAN dedicated for video devices. | Default: video | MaxLen: 63
    video: str
    # VLAN for NAC onboarding devices. | Default: onboarding | MaxLen: 63
    nac: str
    # VLAN for NAC segment primary interface. | Default: nac_segment | MaxLen: 63
    nac_segment: str
    
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
    def to_dict(self) -> VlansPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Vlans:
    """
    Configure initial template for auto-generated VLAN interfaces.
    
    Path: switch_controller/initial_config/vlans
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
    ) -> VlansObject: ...
    
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
    ) -> VlansObject: ...
    
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
    ) -> VlansObject: ...
    
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
    ) -> VlansObject: ...
    
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
    ) -> VlansObject: ...
    
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
    ) -> VlansObject: ...
    
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
    ) -> VlansObject: ...
    
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
    ) -> VlansObject: ...
    
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
    ) -> VlansObject: ...
    
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
    ) -> VlansObject | dict[str, Any]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: VlansPayload | None = ...,
        optional_vlans: Literal["enable", "disable"] | None = ...,
        default_vlan: str | None = ...,
        quarantine: str | None = ...,
        rspan: str | None = ...,
        voice: str | None = ...,
        video: str | None = ...,
        nac: str | None = ...,
        nac_segment: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> VlansObject: ...
    
    @overload
    def put(
        self,
        payload_dict: VlansPayload | None = ...,
        optional_vlans: Literal["enable", "disable"] | None = ...,
        default_vlan: str | None = ...,
        quarantine: str | None = ...,
        rspan: str | None = ...,
        voice: str | None = ...,
        video: str | None = ...,
        nac: str | None = ...,
        nac_segment: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: VlansPayload | None = ...,
        optional_vlans: Literal["enable", "disable"] | None = ...,
        default_vlan: str | None = ...,
        quarantine: str | None = ...,
        rspan: str | None = ...,
        voice: str | None = ...,
        video: str | None = ...,
        nac: str | None = ...,
        nac_segment: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def put(
        self,
        payload_dict: VlansPayload | None = ...,
        optional_vlans: Literal["enable", "disable"] | None = ...,
        default_vlan: str | None = ...,
        quarantine: str | None = ...,
        rspan: str | None = ...,
        voice: str | None = ...,
        video: str | None = ...,
        nac: str | None = ...,
        nac_segment: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: VlansPayload | None = ...,
        optional_vlans: Literal["enable", "disable"] | None = ...,
        default_vlan: str | None = ...,
        quarantine: str | None = ...,
        rspan: str | None = ...,
        voice: str | None = ...,
        video: str | None = ...,
        nac: str | None = ...,
        nac_segment: str | None = ...,
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
    "Vlans",
    "VlansPayload",
    "VlansResponse",
    "VlansObject",
]