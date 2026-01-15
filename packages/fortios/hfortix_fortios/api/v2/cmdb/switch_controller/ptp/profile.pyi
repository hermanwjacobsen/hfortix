from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList
from hfortix_core.types import MutationResponse

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class ProfilePayload(TypedDict, total=False):
    """
    Type hints for switch_controller/ptp/profile payload fields.
    
    Global PTP profile.
    
    **Usage:**
        payload: ProfilePayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # Profile name. | MaxLen: 63
    description: str  # Description. | MaxLen: 63
    mode: Literal["transparent-e2e", "transparent-p2p"]  # Select PTP mode. | Default: transparent-e2e
    ptp_profile: Literal["C37.238-2017"]  # Configure PTP power profile. | Default: C37.238-2017
    transport: Literal["l2-mcast"]  # Configure PTP transport mode. | Default: l2-mcast
    domain: int  # Configure PTP domain value | Default: 254 | Min: 0 | Max: 255
    pdelay_req_interval: Literal["1sec", "2sec", "4sec", "8sec", "16sec", "32sec"]  # Configure PTP peer delay request interval. | Default: 1sec

# Nested TypedDicts for table field children (dict mode)

# Nested classes for table field children (object mode)


# Response TypedDict for GET returns (all fields present in API response)
class ProfileResponse(TypedDict):
    """
    Type hints for switch_controller/ptp/profile API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str  # Profile name. | MaxLen: 63
    description: str  # Description. | MaxLen: 63
    mode: Literal["transparent-e2e", "transparent-p2p"]  # Select PTP mode. | Default: transparent-e2e
    ptp_profile: Literal["C37.238-2017"]  # Configure PTP power profile. | Default: C37.238-2017
    transport: Literal["l2-mcast"]  # Configure PTP transport mode. | Default: l2-mcast
    domain: int  # Configure PTP domain value | Default: 254 | Min: 0 | Max: 255
    pdelay_req_interval: Literal["1sec", "2sec", "4sec", "8sec", "16sec", "32sec"]  # Configure PTP peer delay request interval. | Default: 1sec


@final
class ProfileObject:
    """Typed FortiObject for switch_controller/ptp/profile with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Profile name. | MaxLen: 63
    name: str
    # Description. | MaxLen: 63
    description: str
    # Select PTP mode. | Default: transparent-e2e
    mode: Literal["transparent-e2e", "transparent-p2p"]
    # Configure PTP power profile. | Default: C37.238-2017
    ptp_profile: Literal["C37.238-2017"]
    # Configure PTP transport mode. | Default: l2-mcast
    transport: Literal["l2-mcast"]
    # Configure PTP domain value (0 - 255, default = 254). | Default: 254 | Min: 0 | Max: 255
    domain: int
    # Configure PTP peer delay request interval. | Default: 1sec
    pdelay_req_interval: Literal["1sec", "2sec", "4sec", "8sec", "16sec", "32sec"]
    
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
    def to_dict(self) -> ProfilePayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Profile:
    """
    Global PTP profile.
    
    Path: switch_controller/ptp/profile
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
    ) -> ProfileObject: ...
    
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
    ) -> ProfileObject: ...
    
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
    ) -> FortiObjectList[ProfileObject]: ...
    
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
    ) -> ProfileObject: ...
    
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
    ) -> ProfileObject: ...
    
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
    ) -> FortiObjectList[ProfileObject]: ...
    
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
    ) -> ProfileObject: ...
    
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
    ) -> ProfileObject: ...
    
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
    ) -> FortiObjectList[ProfileObject]: ...
    
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
    ) -> ProfileObject | list[ProfileObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: ProfilePayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        mode: Literal["transparent-e2e", "transparent-p2p"] | None = ...,
        ptp_profile: Literal["C37.238-2017"] | None = ...,
        transport: Literal["l2-mcast"] | None = ...,
        domain: int | None = ...,
        pdelay_req_interval: Literal["1sec", "2sec", "4sec", "8sec", "16sec", "32sec"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> ProfileObject: ...
    
    @overload
    def post(
        self,
        payload_dict: ProfilePayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        mode: Literal["transparent-e2e", "transparent-p2p"] | None = ...,
        ptp_profile: Literal["C37.238-2017"] | None = ...,
        transport: Literal["l2-mcast"] | None = ...,
        domain: int | None = ...,
        pdelay_req_interval: Literal["1sec", "2sec", "4sec", "8sec", "16sec", "32sec"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: ProfilePayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        mode: Literal["transparent-e2e", "transparent-p2p"] | None = ...,
        ptp_profile: Literal["C37.238-2017"] | None = ...,
        transport: Literal["l2-mcast"] | None = ...,
        domain: int | None = ...,
        pdelay_req_interval: Literal["1sec", "2sec", "4sec", "8sec", "16sec", "32sec"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def post(
        self,
        payload_dict: ProfilePayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        mode: Literal["transparent-e2e", "transparent-p2p"] | None = ...,
        ptp_profile: Literal["C37.238-2017"] | None = ...,
        transport: Literal["l2-mcast"] | None = ...,
        domain: int | None = ...,
        pdelay_req_interval: Literal["1sec", "2sec", "4sec", "8sec", "16sec", "32sec"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: ProfilePayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        mode: Literal["transparent-e2e", "transparent-p2p"] | None = ...,
        ptp_profile: Literal["C37.238-2017"] | None = ...,
        transport: Literal["l2-mcast"] | None = ...,
        domain: int | None = ...,
        pdelay_req_interval: Literal["1sec", "2sec", "4sec", "8sec", "16sec", "32sec"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> ProfileObject: ...
    
    @overload
    def put(
        self,
        payload_dict: ProfilePayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        mode: Literal["transparent-e2e", "transparent-p2p"] | None = ...,
        ptp_profile: Literal["C37.238-2017"] | None = ...,
        transport: Literal["l2-mcast"] | None = ...,
        domain: int | None = ...,
        pdelay_req_interval: Literal["1sec", "2sec", "4sec", "8sec", "16sec", "32sec"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: ProfilePayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        mode: Literal["transparent-e2e", "transparent-p2p"] | None = ...,
        ptp_profile: Literal["C37.238-2017"] | None = ...,
        transport: Literal["l2-mcast"] | None = ...,
        domain: int | None = ...,
        pdelay_req_interval: Literal["1sec", "2sec", "4sec", "8sec", "16sec", "32sec"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def put(
        self,
        payload_dict: ProfilePayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        mode: Literal["transparent-e2e", "transparent-p2p"] | None = ...,
        ptp_profile: Literal["C37.238-2017"] | None = ...,
        transport: Literal["l2-mcast"] | None = ...,
        domain: int | None = ...,
        pdelay_req_interval: Literal["1sec", "2sec", "4sec", "8sec", "16sec", "32sec"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> ProfileObject: ...
    
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Default overload
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: ProfilePayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        mode: Literal["transparent-e2e", "transparent-p2p"] | None = ...,
        ptp_profile: Literal["C37.238-2017"] | None = ...,
        transport: Literal["l2-mcast"] | None = ...,
        domain: int | None = ...,
        pdelay_req_interval: Literal["1sec", "2sec", "4sec", "8sec", "16sec", "32sec"] | None = ...,
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
    "Profile",
    "ProfilePayload",
    "ProfileResponse",
    "ProfileObject",
]