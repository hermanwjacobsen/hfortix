from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList
from hfortix_core.types import MutationResponse

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class ArrpProfilePayload(TypedDict, total=False):
    """
    Type hints for wireless_controller/arrp_profile payload fields.
    
    Configure WiFi Automatic Radio Resource Provisioning (ARRP) profiles.
    
    **Usage:**
        payload: ArrpProfilePayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # WiFi ARRP profile name. | MaxLen: 35
    comment: str  # Comment. | MaxLen: 255
    selection_period: int  # Period in seconds to measure average channel load, | Default: 3600 | Min: 0 | Max: 65535
    monitor_period: int  # Period in seconds to measure average transmit retr | Default: 300 | Min: 0 | Max: 65535
    weight_managed_ap: int  # Weight in DARRP channel score calculation for mana | Default: 50 | Min: 0 | Max: 2000
    weight_rogue_ap: int  # Weight in DARRP channel score calculation for rogu | Default: 10 | Min: 0 | Max: 2000
    weight_noise_floor: int  # Weight in DARRP channel score calculation for nois | Default: 40 | Min: 0 | Max: 2000
    weight_channel_load: int  # Weight in DARRP channel score calculation for chan | Default: 20 | Min: 0 | Max: 2000
    weight_spectral_rssi: int  # Weight in DARRP channel score calculation for spec | Default: 40 | Min: 0 | Max: 2000
    weight_weather_channel: int  # Weight in DARRP channel score calculation for weat | Default: 0 | Min: 0 | Max: 2000
    weight_dfs_channel: int  # Weight in DARRP channel score calculation for DFS | Default: 0 | Min: 0 | Max: 2000
    threshold_ap: int  # Threshold to reject channel in DARRP channel selec | Default: 250 | Min: 0 | Max: 500
    threshold_noise_floor: str  # Threshold in dBm to reject channel in DARRP channe | Default: -85 | MaxLen: 7
    threshold_channel_load: int  # Threshold in percentage to reject channel in DARRP | Default: 60 | Min: 0 | Max: 100
    threshold_spectral_rssi: str  # Threshold in dBm to reject channel in DARRP channe | Default: -65 | MaxLen: 7
    threshold_tx_retries: int  # Threshold in percentage for transmit retries to tr | Default: 300 | Min: 0 | Max: 1000
    threshold_rx_errors: int  # Threshold in percentage for receive errors to trig | Default: 50 | Min: 0 | Max: 100
    include_weather_channel: Literal["enable", "disable"]  # Enable/disable use of weather channel in DARRP cha | Default: enable
    include_dfs_channel: Literal["enable", "disable"]  # Enable/disable use of DFS channel in DARRP channel | Default: enable
    override_darrp_optimize: Literal["enable", "disable"]  # Enable to override setting darrp-optimize and darr | Default: disable
    darrp_optimize: int  # Time for running Distributed Automatic Radio Resou | Default: 86400 | Min: 0 | Max: 86400
    darrp_optimize_schedules: list[dict[str, Any]]  # Firewall schedules for DARRP running time. DARRP w

# Nested TypedDicts for table field children (dict mode)

class ArrpProfileDarrpoptimizeschedulesItem(TypedDict):
    """Type hints for darrp-optimize-schedules table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # Schedule name. | MaxLen: 35


# Nested classes for table field children (object mode)

@final
class ArrpProfileDarrpoptimizeschedulesObject:
    """Typed object for darrp-optimize-schedules table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Schedule name. | MaxLen: 35
    name: str
    
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
class ArrpProfileResponse(TypedDict):
    """
    Type hints for wireless_controller/arrp_profile API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str  # WiFi ARRP profile name. | MaxLen: 35
    comment: str  # Comment. | MaxLen: 255
    selection_period: int  # Period in seconds to measure average channel load, | Default: 3600 | Min: 0 | Max: 65535
    monitor_period: int  # Period in seconds to measure average transmit retr | Default: 300 | Min: 0 | Max: 65535
    weight_managed_ap: int  # Weight in DARRP channel score calculation for mana | Default: 50 | Min: 0 | Max: 2000
    weight_rogue_ap: int  # Weight in DARRP channel score calculation for rogu | Default: 10 | Min: 0 | Max: 2000
    weight_noise_floor: int  # Weight in DARRP channel score calculation for nois | Default: 40 | Min: 0 | Max: 2000
    weight_channel_load: int  # Weight in DARRP channel score calculation for chan | Default: 20 | Min: 0 | Max: 2000
    weight_spectral_rssi: int  # Weight in DARRP channel score calculation for spec | Default: 40 | Min: 0 | Max: 2000
    weight_weather_channel: int  # Weight in DARRP channel score calculation for weat | Default: 0 | Min: 0 | Max: 2000
    weight_dfs_channel: int  # Weight in DARRP channel score calculation for DFS | Default: 0 | Min: 0 | Max: 2000
    threshold_ap: int  # Threshold to reject channel in DARRP channel selec | Default: 250 | Min: 0 | Max: 500
    threshold_noise_floor: str  # Threshold in dBm to reject channel in DARRP channe | Default: -85 | MaxLen: 7
    threshold_channel_load: int  # Threshold in percentage to reject channel in DARRP | Default: 60 | Min: 0 | Max: 100
    threshold_spectral_rssi: str  # Threshold in dBm to reject channel in DARRP channe | Default: -65 | MaxLen: 7
    threshold_tx_retries: int  # Threshold in percentage for transmit retries to tr | Default: 300 | Min: 0 | Max: 1000
    threshold_rx_errors: int  # Threshold in percentage for receive errors to trig | Default: 50 | Min: 0 | Max: 100
    include_weather_channel: Literal["enable", "disable"]  # Enable/disable use of weather channel in DARRP cha | Default: enable
    include_dfs_channel: Literal["enable", "disable"]  # Enable/disable use of DFS channel in DARRP channel | Default: enable
    override_darrp_optimize: Literal["enable", "disable"]  # Enable to override setting darrp-optimize and darr | Default: disable
    darrp_optimize: int  # Time for running Distributed Automatic Radio Resou | Default: 86400 | Min: 0 | Max: 86400
    darrp_optimize_schedules: list[ArrpProfileDarrpoptimizeschedulesItem]  # Firewall schedules for DARRP running time. DARRP w


@final
class ArrpProfileObject:
    """Typed FortiObject for wireless_controller/arrp_profile with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # WiFi ARRP profile name. | MaxLen: 35
    name: str
    # Comment. | MaxLen: 255
    comment: str
    # Period in seconds to measure average channel load, noise flo | Default: 3600 | Min: 0 | Max: 65535
    selection_period: int
    # Period in seconds to measure average transmit retries and re | Default: 300 | Min: 0 | Max: 65535
    monitor_period: int
    # Weight in DARRP channel score calculation for managed APs | Default: 50 | Min: 0 | Max: 2000
    weight_managed_ap: int
    # Weight in DARRP channel score calculation for rogue APs | Default: 10 | Min: 0 | Max: 2000
    weight_rogue_ap: int
    # Weight in DARRP channel score calculation for noise floor | Default: 40 | Min: 0 | Max: 2000
    weight_noise_floor: int
    # Weight in DARRP channel score calculation for channel load | Default: 20 | Min: 0 | Max: 2000
    weight_channel_load: int
    # Weight in DARRP channel score calculation for spectral RSSI | Default: 40 | Min: 0 | Max: 2000
    weight_spectral_rssi: int
    # Weight in DARRP channel score calculation for weather channe | Default: 0 | Min: 0 | Max: 2000
    weight_weather_channel: int
    # Weight in DARRP channel score calculation for DFS channel | Default: 0 | Min: 0 | Max: 2000
    weight_dfs_channel: int
    # Threshold to reject channel in DARRP channel selection phase | Default: 250 | Min: 0 | Max: 500
    threshold_ap: int
    # Threshold in dBm to reject channel in DARRP channel selectio | Default: -85 | MaxLen: 7
    threshold_noise_floor: str
    # Threshold in percentage to reject channel in DARRP channel s | Default: 60 | Min: 0 | Max: 100
    threshold_channel_load: int
    # Threshold in dBm to reject channel in DARRP channel selectio | Default: -65 | MaxLen: 7
    threshold_spectral_rssi: str
    # Threshold in percentage for transmit retries to trigger chan | Default: 300 | Min: 0 | Max: 1000
    threshold_tx_retries: int
    # Threshold in percentage for receive errors to trigger channe | Default: 50 | Min: 0 | Max: 100
    threshold_rx_errors: int
    # Enable/disable use of weather channel in DARRP channel selec | Default: enable
    include_weather_channel: Literal["enable", "disable"]
    # Enable/disable use of DFS channel in DARRP channel selection | Default: enable
    include_dfs_channel: Literal["enable", "disable"]
    # Enable to override setting darrp-optimize and darrp-optimize | Default: disable
    override_darrp_optimize: Literal["enable", "disable"]
    # Time for running Distributed Automatic Radio Resource Provis | Default: 86400 | Min: 0 | Max: 86400
    darrp_optimize: int
    # Firewall schedules for DARRP running time. DARRP will run pe
    darrp_optimize_schedules: list[ArrpProfileDarrpoptimizeschedulesObject]
    
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
    def to_dict(self) -> ArrpProfilePayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class ArrpProfile:
    """
    Configure WiFi Automatic Radio Resource Provisioning (ARRP) profiles.
    
    Path: wireless_controller/arrp_profile
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
    ) -> ArrpProfileObject: ...
    
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
    ) -> ArrpProfileObject: ...
    
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
    ) -> FortiObjectList[ArrpProfileObject]: ...
    
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
    ) -> ArrpProfileObject: ...
    
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
    ) -> ArrpProfileObject: ...
    
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
    ) -> FortiObjectList[ArrpProfileObject]: ...
    
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
    ) -> ArrpProfileObject: ...
    
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
    ) -> ArrpProfileObject: ...
    
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
    ) -> FortiObjectList[ArrpProfileObject]: ...
    
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
    ) -> ArrpProfileObject | list[ArrpProfileObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: ArrpProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        selection_period: int | None = ...,
        monitor_period: int | None = ...,
        weight_managed_ap: int | None = ...,
        weight_rogue_ap: int | None = ...,
        weight_noise_floor: int | None = ...,
        weight_channel_load: int | None = ...,
        weight_spectral_rssi: int | None = ...,
        weight_weather_channel: int | None = ...,
        weight_dfs_channel: int | None = ...,
        threshold_ap: int | None = ...,
        threshold_noise_floor: str | None = ...,
        threshold_channel_load: int | None = ...,
        threshold_spectral_rssi: str | None = ...,
        threshold_tx_retries: int | None = ...,
        threshold_rx_errors: int | None = ...,
        include_weather_channel: Literal["enable", "disable"] | None = ...,
        include_dfs_channel: Literal["enable", "disable"] | None = ...,
        override_darrp_optimize: Literal["enable", "disable"] | None = ...,
        darrp_optimize: int | None = ...,
        darrp_optimize_schedules: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> ArrpProfileObject: ...
    
    @overload
    def post(
        self,
        payload_dict: ArrpProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        selection_period: int | None = ...,
        monitor_period: int | None = ...,
        weight_managed_ap: int | None = ...,
        weight_rogue_ap: int | None = ...,
        weight_noise_floor: int | None = ...,
        weight_channel_load: int | None = ...,
        weight_spectral_rssi: int | None = ...,
        weight_weather_channel: int | None = ...,
        weight_dfs_channel: int | None = ...,
        threshold_ap: int | None = ...,
        threshold_noise_floor: str | None = ...,
        threshold_channel_load: int | None = ...,
        threshold_spectral_rssi: str | None = ...,
        threshold_tx_retries: int | None = ...,
        threshold_rx_errors: int | None = ...,
        include_weather_channel: Literal["enable", "disable"] | None = ...,
        include_dfs_channel: Literal["enable", "disable"] | None = ...,
        override_darrp_optimize: Literal["enable", "disable"] | None = ...,
        darrp_optimize: int | None = ...,
        darrp_optimize_schedules: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: ArrpProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        selection_period: int | None = ...,
        monitor_period: int | None = ...,
        weight_managed_ap: int | None = ...,
        weight_rogue_ap: int | None = ...,
        weight_noise_floor: int | None = ...,
        weight_channel_load: int | None = ...,
        weight_spectral_rssi: int | None = ...,
        weight_weather_channel: int | None = ...,
        weight_dfs_channel: int | None = ...,
        threshold_ap: int | None = ...,
        threshold_noise_floor: str | None = ...,
        threshold_channel_load: int | None = ...,
        threshold_spectral_rssi: str | None = ...,
        threshold_tx_retries: int | None = ...,
        threshold_rx_errors: int | None = ...,
        include_weather_channel: Literal["enable", "disable"] | None = ...,
        include_dfs_channel: Literal["enable", "disable"] | None = ...,
        override_darrp_optimize: Literal["enable", "disable"] | None = ...,
        darrp_optimize: int | None = ...,
        darrp_optimize_schedules: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def post(
        self,
        payload_dict: ArrpProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        selection_period: int | None = ...,
        monitor_period: int | None = ...,
        weight_managed_ap: int | None = ...,
        weight_rogue_ap: int | None = ...,
        weight_noise_floor: int | None = ...,
        weight_channel_load: int | None = ...,
        weight_spectral_rssi: int | None = ...,
        weight_weather_channel: int | None = ...,
        weight_dfs_channel: int | None = ...,
        threshold_ap: int | None = ...,
        threshold_noise_floor: str | None = ...,
        threshold_channel_load: int | None = ...,
        threshold_spectral_rssi: str | None = ...,
        threshold_tx_retries: int | None = ...,
        threshold_rx_errors: int | None = ...,
        include_weather_channel: Literal["enable", "disable"] | None = ...,
        include_dfs_channel: Literal["enable", "disable"] | None = ...,
        override_darrp_optimize: Literal["enable", "disable"] | None = ...,
        darrp_optimize: int | None = ...,
        darrp_optimize_schedules: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: ArrpProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        selection_period: int | None = ...,
        monitor_period: int | None = ...,
        weight_managed_ap: int | None = ...,
        weight_rogue_ap: int | None = ...,
        weight_noise_floor: int | None = ...,
        weight_channel_load: int | None = ...,
        weight_spectral_rssi: int | None = ...,
        weight_weather_channel: int | None = ...,
        weight_dfs_channel: int | None = ...,
        threshold_ap: int | None = ...,
        threshold_noise_floor: str | None = ...,
        threshold_channel_load: int | None = ...,
        threshold_spectral_rssi: str | None = ...,
        threshold_tx_retries: int | None = ...,
        threshold_rx_errors: int | None = ...,
        include_weather_channel: Literal["enable", "disable"] | None = ...,
        include_dfs_channel: Literal["enable", "disable"] | None = ...,
        override_darrp_optimize: Literal["enable", "disable"] | None = ...,
        darrp_optimize: int | None = ...,
        darrp_optimize_schedules: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> ArrpProfileObject: ...
    
    @overload
    def put(
        self,
        payload_dict: ArrpProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        selection_period: int | None = ...,
        monitor_period: int | None = ...,
        weight_managed_ap: int | None = ...,
        weight_rogue_ap: int | None = ...,
        weight_noise_floor: int | None = ...,
        weight_channel_load: int | None = ...,
        weight_spectral_rssi: int | None = ...,
        weight_weather_channel: int | None = ...,
        weight_dfs_channel: int | None = ...,
        threshold_ap: int | None = ...,
        threshold_noise_floor: str | None = ...,
        threshold_channel_load: int | None = ...,
        threshold_spectral_rssi: str | None = ...,
        threshold_tx_retries: int | None = ...,
        threshold_rx_errors: int | None = ...,
        include_weather_channel: Literal["enable", "disable"] | None = ...,
        include_dfs_channel: Literal["enable", "disable"] | None = ...,
        override_darrp_optimize: Literal["enable", "disable"] | None = ...,
        darrp_optimize: int | None = ...,
        darrp_optimize_schedules: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: ArrpProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        selection_period: int | None = ...,
        monitor_period: int | None = ...,
        weight_managed_ap: int | None = ...,
        weight_rogue_ap: int | None = ...,
        weight_noise_floor: int | None = ...,
        weight_channel_load: int | None = ...,
        weight_spectral_rssi: int | None = ...,
        weight_weather_channel: int | None = ...,
        weight_dfs_channel: int | None = ...,
        threshold_ap: int | None = ...,
        threshold_noise_floor: str | None = ...,
        threshold_channel_load: int | None = ...,
        threshold_spectral_rssi: str | None = ...,
        threshold_tx_retries: int | None = ...,
        threshold_rx_errors: int | None = ...,
        include_weather_channel: Literal["enable", "disable"] | None = ...,
        include_dfs_channel: Literal["enable", "disable"] | None = ...,
        override_darrp_optimize: Literal["enable", "disable"] | None = ...,
        darrp_optimize: int | None = ...,
        darrp_optimize_schedules: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def put(
        self,
        payload_dict: ArrpProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        selection_period: int | None = ...,
        monitor_period: int | None = ...,
        weight_managed_ap: int | None = ...,
        weight_rogue_ap: int | None = ...,
        weight_noise_floor: int | None = ...,
        weight_channel_load: int | None = ...,
        weight_spectral_rssi: int | None = ...,
        weight_weather_channel: int | None = ...,
        weight_dfs_channel: int | None = ...,
        threshold_ap: int | None = ...,
        threshold_noise_floor: str | None = ...,
        threshold_channel_load: int | None = ...,
        threshold_spectral_rssi: str | None = ...,
        threshold_tx_retries: int | None = ...,
        threshold_rx_errors: int | None = ...,
        include_weather_channel: Literal["enable", "disable"] | None = ...,
        include_dfs_channel: Literal["enable", "disable"] | None = ...,
        override_darrp_optimize: Literal["enable", "disable"] | None = ...,
        darrp_optimize: int | None = ...,
        darrp_optimize_schedules: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> ArrpProfileObject: ...
    
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
        payload_dict: ArrpProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        selection_period: int | None = ...,
        monitor_period: int | None = ...,
        weight_managed_ap: int | None = ...,
        weight_rogue_ap: int | None = ...,
        weight_noise_floor: int | None = ...,
        weight_channel_load: int | None = ...,
        weight_spectral_rssi: int | None = ...,
        weight_weather_channel: int | None = ...,
        weight_dfs_channel: int | None = ...,
        threshold_ap: int | None = ...,
        threshold_noise_floor: str | None = ...,
        threshold_channel_load: int | None = ...,
        threshold_spectral_rssi: str | None = ...,
        threshold_tx_retries: int | None = ...,
        threshold_rx_errors: int | None = ...,
        include_weather_channel: Literal["enable", "disable"] | None = ...,
        include_dfs_channel: Literal["enable", "disable"] | None = ...,
        override_darrp_optimize: Literal["enable", "disable"] | None = ...,
        darrp_optimize: int | None = ...,
        darrp_optimize_schedules: str | list[str] | list[dict[str, Any]] | None = ...,
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
    "ArrpProfile",
    "ArrpProfilePayload",
    "ArrpProfileResponse",
    "ArrpProfileObject",
]