from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList
from hfortix_core.types import MutationResponse

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class QosProfilePayload(TypedDict, total=False):
    """
    Type hints for wireless_controller/qos_profile payload fields.
    
    Configure WiFi quality of service (QoS) profiles.
    
    **Usage:**
        payload: QosProfilePayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # WiFi QoS profile name. | MaxLen: 35
    comment: str  # Comment. | MaxLen: 63
    uplink: int  # Maximum uplink bandwidth for Virtual Access Points | Default: 0 | Min: 0 | Max: 2097152
    downlink: int  # Maximum downlink bandwidth for Virtual Access Poin | Default: 0 | Min: 0 | Max: 2097152
    uplink_sta: int  # Maximum uplink bandwidth for clients | Default: 0 | Min: 0 | Max: 2097152
    downlink_sta: int  # Maximum downlink bandwidth for clients | Default: 0 | Min: 0 | Max: 2097152
    burst: Literal["enable", "disable"]  # Enable/disable client rate burst. | Default: disable
    wmm: Literal["enable", "disable"]  # Enable/disable WiFi multi-media (WMM) control. | Default: enable
    wmm_uapsd: Literal["enable", "disable"]  # Enable/disable WMM Unscheduled Automatic Power Sav | Default: enable
    call_admission_control: Literal["enable", "disable"]  # Enable/disable WMM call admission control. | Default: disable
    call_capacity: int  # Maximum number of Voice over WLAN (VoWLAN) phones | Default: 10 | Min: 0 | Max: 60
    bandwidth_admission_control: Literal["enable", "disable"]  # Enable/disable WMM bandwidth admission control. | Default: disable
    bandwidth_capacity: int  # Maximum bandwidth capacity allowed | Default: 2000 | Min: 1 | Max: 600000
    dscp_wmm_mapping: Literal["enable", "disable"]  # Enable/disable Differentiated Services Code Point | Default: disable
    dscp_wmm_vo: list[dict[str, Any]]  # DSCP mapping for voice access (default = 48 56).
    dscp_wmm_vi: list[dict[str, Any]]  # DSCP mapping for video access (default = 32 40).
    dscp_wmm_be: list[dict[str, Any]]  # DSCP mapping for best effort access
    dscp_wmm_bk: list[dict[str, Any]]  # DSCP mapping for background access
    wmm_dscp_marking: Literal["enable", "disable"]  # Enable/disable WMM Differentiated Services Code Po | Default: disable
    wmm_vo_dscp: int  # DSCP marking for voice access (default = 48). | Default: 48 | Min: 0 | Max: 63
    wmm_vi_dscp: int  # DSCP marking for video access (default = 32). | Default: 32 | Min: 0 | Max: 63
    wmm_be_dscp: int  # DSCP marking for best effort access (default = 0). | Default: 0 | Min: 0 | Max: 63
    wmm_bk_dscp: int  # DSCP marking for background access (default = 8). | Default: 8 | Min: 0 | Max: 63

# Nested TypedDicts for table field children (dict mode)

class QosProfileDscpwmmvoItem(TypedDict):
    """Type hints for dscp-wmm-vo table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    id: int  # DSCP WMM mapping numbers (0 - 63). | Default: 0 | Min: 0 | Max: 63


class QosProfileDscpwmmviItem(TypedDict):
    """Type hints for dscp-wmm-vi table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    id: int  # DSCP WMM mapping numbers (0 - 63). | Default: 0 | Min: 0 | Max: 63


class QosProfileDscpwmmbeItem(TypedDict):
    """Type hints for dscp-wmm-be table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    id: int  # DSCP WMM mapping numbers (0 - 63). | Default: 0 | Min: 0 | Max: 63


class QosProfileDscpwmmbkItem(TypedDict):
    """Type hints for dscp-wmm-bk table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    id: int  # DSCP WMM mapping numbers (0 - 63). | Default: 0 | Min: 0 | Max: 63


# Nested classes for table field children (object mode)

@final
class QosProfileDscpwmmvoObject:
    """Typed object for dscp-wmm-vo table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # DSCP WMM mapping numbers (0 - 63). | Default: 0 | Min: 0 | Max: 63
    id: int
    
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


@final
class QosProfileDscpwmmviObject:
    """Typed object for dscp-wmm-vi table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # DSCP WMM mapping numbers (0 - 63). | Default: 0 | Min: 0 | Max: 63
    id: int
    
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


@final
class QosProfileDscpwmmbeObject:
    """Typed object for dscp-wmm-be table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # DSCP WMM mapping numbers (0 - 63). | Default: 0 | Min: 0 | Max: 63
    id: int
    
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


@final
class QosProfileDscpwmmbkObject:
    """Typed object for dscp-wmm-bk table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # DSCP WMM mapping numbers (0 - 63). | Default: 0 | Min: 0 | Max: 63
    id: int
    
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
class QosProfileResponse(TypedDict):
    """
    Type hints for wireless_controller/qos_profile API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str  # WiFi QoS profile name. | MaxLen: 35
    comment: str  # Comment. | MaxLen: 63
    uplink: int  # Maximum uplink bandwidth for Virtual Access Points | Default: 0 | Min: 0 | Max: 2097152
    downlink: int  # Maximum downlink bandwidth for Virtual Access Poin | Default: 0 | Min: 0 | Max: 2097152
    uplink_sta: int  # Maximum uplink bandwidth for clients | Default: 0 | Min: 0 | Max: 2097152
    downlink_sta: int  # Maximum downlink bandwidth for clients | Default: 0 | Min: 0 | Max: 2097152
    burst: Literal["enable", "disable"]  # Enable/disable client rate burst. | Default: disable
    wmm: Literal["enable", "disable"]  # Enable/disable WiFi multi-media (WMM) control. | Default: enable
    wmm_uapsd: Literal["enable", "disable"]  # Enable/disable WMM Unscheduled Automatic Power Sav | Default: enable
    call_admission_control: Literal["enable", "disable"]  # Enable/disable WMM call admission control. | Default: disable
    call_capacity: int  # Maximum number of Voice over WLAN (VoWLAN) phones | Default: 10 | Min: 0 | Max: 60
    bandwidth_admission_control: Literal["enable", "disable"]  # Enable/disable WMM bandwidth admission control. | Default: disable
    bandwidth_capacity: int  # Maximum bandwidth capacity allowed | Default: 2000 | Min: 1 | Max: 600000
    dscp_wmm_mapping: Literal["enable", "disable"]  # Enable/disable Differentiated Services Code Point | Default: disable
    dscp_wmm_vo: list[QosProfileDscpwmmvoItem]  # DSCP mapping for voice access (default = 48 56).
    dscp_wmm_vi: list[QosProfileDscpwmmviItem]  # DSCP mapping for video access (default = 32 40).
    dscp_wmm_be: list[QosProfileDscpwmmbeItem]  # DSCP mapping for best effort access
    dscp_wmm_bk: list[QosProfileDscpwmmbkItem]  # DSCP mapping for background access
    wmm_dscp_marking: Literal["enable", "disable"]  # Enable/disable WMM Differentiated Services Code Po | Default: disable
    wmm_vo_dscp: int  # DSCP marking for voice access (default = 48). | Default: 48 | Min: 0 | Max: 63
    wmm_vi_dscp: int  # DSCP marking for video access (default = 32). | Default: 32 | Min: 0 | Max: 63
    wmm_be_dscp: int  # DSCP marking for best effort access (default = 0). | Default: 0 | Min: 0 | Max: 63
    wmm_bk_dscp: int  # DSCP marking for background access (default = 8). | Default: 8 | Min: 0 | Max: 63


@final
class QosProfileObject:
    """Typed FortiObject for wireless_controller/qos_profile with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # WiFi QoS profile name. | MaxLen: 35
    name: str
    # Comment. | MaxLen: 63
    comment: str
    # Maximum uplink bandwidth for Virtual Access Points (VAPs) | Default: 0 | Min: 0 | Max: 2097152
    uplink: int
    # Maximum downlink bandwidth for Virtual Access Points (VAPs) | Default: 0 | Min: 0 | Max: 2097152
    downlink: int
    # Maximum uplink bandwidth for clients | Default: 0 | Min: 0 | Max: 2097152
    uplink_sta: int
    # Maximum downlink bandwidth for clients | Default: 0 | Min: 0 | Max: 2097152
    downlink_sta: int
    # Enable/disable client rate burst. | Default: disable
    burst: Literal["enable", "disable"]
    # Enable/disable WiFi multi-media (WMM) control. | Default: enable
    wmm: Literal["enable", "disable"]
    # Enable/disable WMM Unscheduled Automatic Power Save Delivery | Default: enable
    wmm_uapsd: Literal["enable", "disable"]
    # Enable/disable WMM call admission control. | Default: disable
    call_admission_control: Literal["enable", "disable"]
    # Maximum number of Voice over WLAN (VoWLAN) phones allowed | Default: 10 | Min: 0 | Max: 60
    call_capacity: int
    # Enable/disable WMM bandwidth admission control. | Default: disable
    bandwidth_admission_control: Literal["enable", "disable"]
    # Maximum bandwidth capacity allowed | Default: 2000 | Min: 1 | Max: 600000
    bandwidth_capacity: int
    # Enable/disable Differentiated Services Code Point (DSCP) map | Default: disable
    dscp_wmm_mapping: Literal["enable", "disable"]
    # DSCP mapping for voice access (default = 48 56).
    dscp_wmm_vo: list[QosProfileDscpwmmvoObject]
    # DSCP mapping for video access (default = 32 40).
    dscp_wmm_vi: list[QosProfileDscpwmmviObject]
    # DSCP mapping for best effort access (default = 0 24).
    dscp_wmm_be: list[QosProfileDscpwmmbeObject]
    # DSCP mapping for background access (default = 8 16).
    dscp_wmm_bk: list[QosProfileDscpwmmbkObject]
    # Enable/disable WMM Differentiated Services Code Point (DSCP) | Default: disable
    wmm_dscp_marking: Literal["enable", "disable"]
    # DSCP marking for voice access (default = 48). | Default: 48 | Min: 0 | Max: 63
    wmm_vo_dscp: int
    # DSCP marking for video access (default = 32). | Default: 32 | Min: 0 | Max: 63
    wmm_vi_dscp: int
    # DSCP marking for best effort access (default = 0). | Default: 0 | Min: 0 | Max: 63
    wmm_be_dscp: int
    # DSCP marking for background access (default = 8). | Default: 8 | Min: 0 | Max: 63
    wmm_bk_dscp: int
    
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
    def to_dict(self) -> QosProfilePayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class QosProfile:
    """
    Configure WiFi quality of service (QoS) profiles.
    
    Path: wireless_controller/qos_profile
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
    ) -> QosProfileObject: ...
    
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
    ) -> QosProfileObject: ...
    
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
    ) -> FortiObjectList[QosProfileObject]: ...
    
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
    ) -> QosProfileObject: ...
    
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
    ) -> QosProfileObject: ...
    
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
    ) -> FortiObjectList[QosProfileObject]: ...
    
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
    ) -> QosProfileObject: ...
    
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
    ) -> QosProfileObject: ...
    
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
    ) -> FortiObjectList[QosProfileObject]: ...
    
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
    ) -> QosProfileObject | list[QosProfileObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: QosProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        uplink: int | None = ...,
        downlink: int | None = ...,
        uplink_sta: int | None = ...,
        downlink_sta: int | None = ...,
        burst: Literal["enable", "disable"] | None = ...,
        wmm: Literal["enable", "disable"] | None = ...,
        wmm_uapsd: Literal["enable", "disable"] | None = ...,
        call_admission_control: Literal["enable", "disable"] | None = ...,
        call_capacity: int | None = ...,
        bandwidth_admission_control: Literal["enable", "disable"] | None = ...,
        bandwidth_capacity: int | None = ...,
        dscp_wmm_mapping: Literal["enable", "disable"] | None = ...,
        dscp_wmm_vo: str | list[str] | list[dict[str, Any]] | None = ...,
        dscp_wmm_vi: str | list[str] | list[dict[str, Any]] | None = ...,
        dscp_wmm_be: str | list[str] | list[dict[str, Any]] | None = ...,
        dscp_wmm_bk: str | list[str] | list[dict[str, Any]] | None = ...,
        wmm_dscp_marking: Literal["enable", "disable"] | None = ...,
        wmm_vo_dscp: int | None = ...,
        wmm_vi_dscp: int | None = ...,
        wmm_be_dscp: int | None = ...,
        wmm_bk_dscp: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> QosProfileObject: ...
    
    @overload
    def post(
        self,
        payload_dict: QosProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        uplink: int | None = ...,
        downlink: int | None = ...,
        uplink_sta: int | None = ...,
        downlink_sta: int | None = ...,
        burst: Literal["enable", "disable"] | None = ...,
        wmm: Literal["enable", "disable"] | None = ...,
        wmm_uapsd: Literal["enable", "disable"] | None = ...,
        call_admission_control: Literal["enable", "disable"] | None = ...,
        call_capacity: int | None = ...,
        bandwidth_admission_control: Literal["enable", "disable"] | None = ...,
        bandwidth_capacity: int | None = ...,
        dscp_wmm_mapping: Literal["enable", "disable"] | None = ...,
        dscp_wmm_vo: str | list[str] | list[dict[str, Any]] | None = ...,
        dscp_wmm_vi: str | list[str] | list[dict[str, Any]] | None = ...,
        dscp_wmm_be: str | list[str] | list[dict[str, Any]] | None = ...,
        dscp_wmm_bk: str | list[str] | list[dict[str, Any]] | None = ...,
        wmm_dscp_marking: Literal["enable", "disable"] | None = ...,
        wmm_vo_dscp: int | None = ...,
        wmm_vi_dscp: int | None = ...,
        wmm_be_dscp: int | None = ...,
        wmm_bk_dscp: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: QosProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        uplink: int | None = ...,
        downlink: int | None = ...,
        uplink_sta: int | None = ...,
        downlink_sta: int | None = ...,
        burst: Literal["enable", "disable"] | None = ...,
        wmm: Literal["enable", "disable"] | None = ...,
        wmm_uapsd: Literal["enable", "disable"] | None = ...,
        call_admission_control: Literal["enable", "disable"] | None = ...,
        call_capacity: int | None = ...,
        bandwidth_admission_control: Literal["enable", "disable"] | None = ...,
        bandwidth_capacity: int | None = ...,
        dscp_wmm_mapping: Literal["enable", "disable"] | None = ...,
        dscp_wmm_vo: str | list[str] | list[dict[str, Any]] | None = ...,
        dscp_wmm_vi: str | list[str] | list[dict[str, Any]] | None = ...,
        dscp_wmm_be: str | list[str] | list[dict[str, Any]] | None = ...,
        dscp_wmm_bk: str | list[str] | list[dict[str, Any]] | None = ...,
        wmm_dscp_marking: Literal["enable", "disable"] | None = ...,
        wmm_vo_dscp: int | None = ...,
        wmm_vi_dscp: int | None = ...,
        wmm_be_dscp: int | None = ...,
        wmm_bk_dscp: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def post(
        self,
        payload_dict: QosProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        uplink: int | None = ...,
        downlink: int | None = ...,
        uplink_sta: int | None = ...,
        downlink_sta: int | None = ...,
        burst: Literal["enable", "disable"] | None = ...,
        wmm: Literal["enable", "disable"] | None = ...,
        wmm_uapsd: Literal["enable", "disable"] | None = ...,
        call_admission_control: Literal["enable", "disable"] | None = ...,
        call_capacity: int | None = ...,
        bandwidth_admission_control: Literal["enable", "disable"] | None = ...,
        bandwidth_capacity: int | None = ...,
        dscp_wmm_mapping: Literal["enable", "disable"] | None = ...,
        dscp_wmm_vo: str | list[str] | list[dict[str, Any]] | None = ...,
        dscp_wmm_vi: str | list[str] | list[dict[str, Any]] | None = ...,
        dscp_wmm_be: str | list[str] | list[dict[str, Any]] | None = ...,
        dscp_wmm_bk: str | list[str] | list[dict[str, Any]] | None = ...,
        wmm_dscp_marking: Literal["enable", "disable"] | None = ...,
        wmm_vo_dscp: int | None = ...,
        wmm_vi_dscp: int | None = ...,
        wmm_be_dscp: int | None = ...,
        wmm_bk_dscp: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: QosProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        uplink: int | None = ...,
        downlink: int | None = ...,
        uplink_sta: int | None = ...,
        downlink_sta: int | None = ...,
        burst: Literal["enable", "disable"] | None = ...,
        wmm: Literal["enable", "disable"] | None = ...,
        wmm_uapsd: Literal["enable", "disable"] | None = ...,
        call_admission_control: Literal["enable", "disable"] | None = ...,
        call_capacity: int | None = ...,
        bandwidth_admission_control: Literal["enable", "disable"] | None = ...,
        bandwidth_capacity: int | None = ...,
        dscp_wmm_mapping: Literal["enable", "disable"] | None = ...,
        dscp_wmm_vo: str | list[str] | list[dict[str, Any]] | None = ...,
        dscp_wmm_vi: str | list[str] | list[dict[str, Any]] | None = ...,
        dscp_wmm_be: str | list[str] | list[dict[str, Any]] | None = ...,
        dscp_wmm_bk: str | list[str] | list[dict[str, Any]] | None = ...,
        wmm_dscp_marking: Literal["enable", "disable"] | None = ...,
        wmm_vo_dscp: int | None = ...,
        wmm_vi_dscp: int | None = ...,
        wmm_be_dscp: int | None = ...,
        wmm_bk_dscp: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> QosProfileObject: ...
    
    @overload
    def put(
        self,
        payload_dict: QosProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        uplink: int | None = ...,
        downlink: int | None = ...,
        uplink_sta: int | None = ...,
        downlink_sta: int | None = ...,
        burst: Literal["enable", "disable"] | None = ...,
        wmm: Literal["enable", "disable"] | None = ...,
        wmm_uapsd: Literal["enable", "disable"] | None = ...,
        call_admission_control: Literal["enable", "disable"] | None = ...,
        call_capacity: int | None = ...,
        bandwidth_admission_control: Literal["enable", "disable"] | None = ...,
        bandwidth_capacity: int | None = ...,
        dscp_wmm_mapping: Literal["enable", "disable"] | None = ...,
        dscp_wmm_vo: str | list[str] | list[dict[str, Any]] | None = ...,
        dscp_wmm_vi: str | list[str] | list[dict[str, Any]] | None = ...,
        dscp_wmm_be: str | list[str] | list[dict[str, Any]] | None = ...,
        dscp_wmm_bk: str | list[str] | list[dict[str, Any]] | None = ...,
        wmm_dscp_marking: Literal["enable", "disable"] | None = ...,
        wmm_vo_dscp: int | None = ...,
        wmm_vi_dscp: int | None = ...,
        wmm_be_dscp: int | None = ...,
        wmm_bk_dscp: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: QosProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        uplink: int | None = ...,
        downlink: int | None = ...,
        uplink_sta: int | None = ...,
        downlink_sta: int | None = ...,
        burst: Literal["enable", "disable"] | None = ...,
        wmm: Literal["enable", "disable"] | None = ...,
        wmm_uapsd: Literal["enable", "disable"] | None = ...,
        call_admission_control: Literal["enable", "disable"] | None = ...,
        call_capacity: int | None = ...,
        bandwidth_admission_control: Literal["enable", "disable"] | None = ...,
        bandwidth_capacity: int | None = ...,
        dscp_wmm_mapping: Literal["enable", "disable"] | None = ...,
        dscp_wmm_vo: str | list[str] | list[dict[str, Any]] | None = ...,
        dscp_wmm_vi: str | list[str] | list[dict[str, Any]] | None = ...,
        dscp_wmm_be: str | list[str] | list[dict[str, Any]] | None = ...,
        dscp_wmm_bk: str | list[str] | list[dict[str, Any]] | None = ...,
        wmm_dscp_marking: Literal["enable", "disable"] | None = ...,
        wmm_vo_dscp: int | None = ...,
        wmm_vi_dscp: int | None = ...,
        wmm_be_dscp: int | None = ...,
        wmm_bk_dscp: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def put(
        self,
        payload_dict: QosProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        uplink: int | None = ...,
        downlink: int | None = ...,
        uplink_sta: int | None = ...,
        downlink_sta: int | None = ...,
        burst: Literal["enable", "disable"] | None = ...,
        wmm: Literal["enable", "disable"] | None = ...,
        wmm_uapsd: Literal["enable", "disable"] | None = ...,
        call_admission_control: Literal["enable", "disable"] | None = ...,
        call_capacity: int | None = ...,
        bandwidth_admission_control: Literal["enable", "disable"] | None = ...,
        bandwidth_capacity: int | None = ...,
        dscp_wmm_mapping: Literal["enable", "disable"] | None = ...,
        dscp_wmm_vo: str | list[str] | list[dict[str, Any]] | None = ...,
        dscp_wmm_vi: str | list[str] | list[dict[str, Any]] | None = ...,
        dscp_wmm_be: str | list[str] | list[dict[str, Any]] | None = ...,
        dscp_wmm_bk: str | list[str] | list[dict[str, Any]] | None = ...,
        wmm_dscp_marking: Literal["enable", "disable"] | None = ...,
        wmm_vo_dscp: int | None = ...,
        wmm_vi_dscp: int | None = ...,
        wmm_be_dscp: int | None = ...,
        wmm_bk_dscp: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> QosProfileObject: ...
    
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
        payload_dict: QosProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        uplink: int | None = ...,
        downlink: int | None = ...,
        uplink_sta: int | None = ...,
        downlink_sta: int | None = ...,
        burst: Literal["enable", "disable"] | None = ...,
        wmm: Literal["enable", "disable"] | None = ...,
        wmm_uapsd: Literal["enable", "disable"] | None = ...,
        call_admission_control: Literal["enable", "disable"] | None = ...,
        call_capacity: int | None = ...,
        bandwidth_admission_control: Literal["enable", "disable"] | None = ...,
        bandwidth_capacity: int | None = ...,
        dscp_wmm_mapping: Literal["enable", "disable"] | None = ...,
        dscp_wmm_vo: str | list[str] | list[dict[str, Any]] | None = ...,
        dscp_wmm_vi: str | list[str] | list[dict[str, Any]] | None = ...,
        dscp_wmm_be: str | list[str] | list[dict[str, Any]] | None = ...,
        dscp_wmm_bk: str | list[str] | list[dict[str, Any]] | None = ...,
        wmm_dscp_marking: Literal["enable", "disable"] | None = ...,
        wmm_vo_dscp: int | None = ...,
        wmm_vi_dscp: int | None = ...,
        wmm_be_dscp: int | None = ...,
        wmm_bk_dscp: int | None = ...,
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
    "QosProfile",
    "QosProfilePayload",
    "QosProfileResponse",
    "QosProfileObject",
]