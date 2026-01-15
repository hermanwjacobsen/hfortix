from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList
from hfortix_core.types import MutationResponse

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class SpeedTestSchedulePayload(TypedDict, total=False):
    """
    Type hints for system/speed_test_schedule payload fields.
    
    Speed test schedule for each interface.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.system.interface.InterfaceEndpoint` (via: interface)
        - :class:`~.system.speed-test-server.SpeedTestServerEndpoint` (via: server-name)

    **Usage:**
        payload: SpeedTestSchedulePayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    interface: str  # Interface name. | MaxLen: 35
    status: Literal["disable", "enable"]  # Enable/disable scheduled speed test. | Default: enable
    diffserv: str  # DSCP used for speed test.
    server_name: str  # Speed test server name in system.speed-test-server | MaxLen: 35
    mode: Literal["UDP", "TCP", "Auto"]  # Protocol Auto(default), TCP or UDP used for speed | Default: Auto
    schedules: list[dict[str, Any]]  # Schedules for the interface.
    dynamic_server: Literal["disable", "enable"]  # Enable/disable dynamic server option. | Default: disable
    ctrl_port: int  # Port of the controller to get access token. | Default: 5200 | Min: 1 | Max: 65535
    server_port: int  # Port of the server to run speed test. | Default: 5201 | Min: 1 | Max: 65535
    update_shaper: Literal["disable", "local", "remote", "both"]  # Set egress shaper based on the test result. | Default: disable
    update_inbandwidth: Literal["disable", "enable"]  # Enable/disable bypassing interface's inbound bandw | Default: disable
    update_outbandwidth: Literal["disable", "enable"]  # Enable/disable bypassing interface's outbound band | Default: disable
    update_interface_shaping: Literal["disable", "enable"]  # Enable/disable using the speedtest results as refe | Default: disable
    update_inbandwidth_maximum: int  # Maximum downloading bandwidth (kbps) to be used in | Default: 0 | Min: 0 | Max: 16776000
    update_inbandwidth_minimum: int  # Minimum downloading bandwidth (kbps) to be conside | Default: 0 | Min: 0 | Max: 16776000
    update_outbandwidth_maximum: int  # Maximum uploading bandwidth (kbps) to be used in a | Default: 0 | Min: 0 | Max: 16776000
    update_outbandwidth_minimum: int  # Minimum uploading bandwidth (kbps) to be considere | Default: 0 | Min: 0 | Max: 16776000
    expected_inbandwidth_minimum: int  # Set the minimum inbandwidth threshold for applying | Default: 0 | Min: 0 | Max: 16776000
    expected_inbandwidth_maximum: int  # Set the maximum inbandwidth threshold for applying | Default: 0 | Min: 0 | Max: 16776000
    expected_outbandwidth_minimum: int  # Set the minimum outbandwidth threshold for applyin | Default: 0 | Min: 0 | Max: 16776000
    expected_outbandwidth_maximum: int  # Set the maximum outbandwidth threshold for applyin | Default: 0 | Min: 0 | Max: 16776000
    retries: int  # Maximum number of times the FortiGate unit will at | Default: 5 | Min: 1 | Max: 10
    retry_pause: int  # Number of seconds the FortiGate pauses between suc | Default: 300 | Min: 60 | Max: 3600

# Nested TypedDicts for table field children (dict mode)

class SpeedTestScheduleSchedulesItem(TypedDict):
    """Type hints for schedules table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # Name of a firewall recurring schedule. | MaxLen: 31


# Nested classes for table field children (object mode)

@final
class SpeedTestScheduleSchedulesObject:
    """Typed object for schedules table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Name of a firewall recurring schedule. | MaxLen: 31
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
class SpeedTestScheduleResponse(TypedDict):
    """
    Type hints for system/speed_test_schedule API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    interface: str  # Interface name. | MaxLen: 35
    status: Literal["disable", "enable"]  # Enable/disable scheduled speed test. | Default: enable
    diffserv: str  # DSCP used for speed test.
    server_name: str  # Speed test server name in system.speed-test-server | MaxLen: 35
    mode: Literal["UDP", "TCP", "Auto"]  # Protocol Auto(default), TCP or UDP used for speed | Default: Auto
    schedules: list[SpeedTestScheduleSchedulesItem]  # Schedules for the interface.
    dynamic_server: Literal["disable", "enable"]  # Enable/disable dynamic server option. | Default: disable
    ctrl_port: int  # Port of the controller to get access token. | Default: 5200 | Min: 1 | Max: 65535
    server_port: int  # Port of the server to run speed test. | Default: 5201 | Min: 1 | Max: 65535
    update_shaper: Literal["disable", "local", "remote", "both"]  # Set egress shaper based on the test result. | Default: disable
    update_inbandwidth: Literal["disable", "enable"]  # Enable/disable bypassing interface's inbound bandw | Default: disable
    update_outbandwidth: Literal["disable", "enable"]  # Enable/disable bypassing interface's outbound band | Default: disable
    update_interface_shaping: Literal["disable", "enable"]  # Enable/disable using the speedtest results as refe | Default: disable
    update_inbandwidth_maximum: int  # Maximum downloading bandwidth (kbps) to be used in | Default: 0 | Min: 0 | Max: 16776000
    update_inbandwidth_minimum: int  # Minimum downloading bandwidth (kbps) to be conside | Default: 0 | Min: 0 | Max: 16776000
    update_outbandwidth_maximum: int  # Maximum uploading bandwidth (kbps) to be used in a | Default: 0 | Min: 0 | Max: 16776000
    update_outbandwidth_minimum: int  # Minimum uploading bandwidth (kbps) to be considere | Default: 0 | Min: 0 | Max: 16776000
    expected_inbandwidth_minimum: int  # Set the minimum inbandwidth threshold for applying | Default: 0 | Min: 0 | Max: 16776000
    expected_inbandwidth_maximum: int  # Set the maximum inbandwidth threshold for applying | Default: 0 | Min: 0 | Max: 16776000
    expected_outbandwidth_minimum: int  # Set the minimum outbandwidth threshold for applyin | Default: 0 | Min: 0 | Max: 16776000
    expected_outbandwidth_maximum: int  # Set the maximum outbandwidth threshold for applyin | Default: 0 | Min: 0 | Max: 16776000
    retries: int  # Maximum number of times the FortiGate unit will at | Default: 5 | Min: 1 | Max: 10
    retry_pause: int  # Number of seconds the FortiGate pauses between suc | Default: 300 | Min: 60 | Max: 3600


@final
class SpeedTestScheduleObject:
    """Typed FortiObject for system/speed_test_schedule with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Interface name. | MaxLen: 35
    interface: str
    # Enable/disable scheduled speed test. | Default: enable
    status: Literal["disable", "enable"]
    # DSCP used for speed test.
    diffserv: str
    # Speed test server name in system.speed-test-server list or l | MaxLen: 35
    server_name: str
    # Protocol Auto(default), TCP or UDP used for speed test. | Default: Auto
    mode: Literal["UDP", "TCP", "Auto"]
    # Schedules for the interface.
    schedules: list[SpeedTestScheduleSchedulesObject]
    # Enable/disable dynamic server option. | Default: disable
    dynamic_server: Literal["disable", "enable"]
    # Port of the controller to get access token. | Default: 5200 | Min: 1 | Max: 65535
    ctrl_port: int
    # Port of the server to run speed test. | Default: 5201 | Min: 1 | Max: 65535
    server_port: int
    # Set egress shaper based on the test result. | Default: disable
    update_shaper: Literal["disable", "local", "remote", "both"]
    # Enable/disable bypassing interface's inbound bandwidth setti | Default: disable
    update_inbandwidth: Literal["disable", "enable"]
    # Enable/disable bypassing interface's outbound bandwidth sett | Default: disable
    update_outbandwidth: Literal["disable", "enable"]
    # Enable/disable using the speedtest results as reference for | Default: disable
    update_interface_shaping: Literal["disable", "enable"]
    # Maximum downloading bandwidth (kbps) to be used in a speed t | Default: 0 | Min: 0 | Max: 16776000
    update_inbandwidth_maximum: int
    # Minimum downloading bandwidth (kbps) to be considered effect | Default: 0 | Min: 0 | Max: 16776000
    update_inbandwidth_minimum: int
    # Maximum uploading bandwidth (kbps) to be used in a speed tes | Default: 0 | Min: 0 | Max: 16776000
    update_outbandwidth_maximum: int
    # Minimum uploading bandwidth (kbps) to be considered effectiv | Default: 0 | Min: 0 | Max: 16776000
    update_outbandwidth_minimum: int
    # Set the minimum inbandwidth threshold for applying speedtest | Default: 0 | Min: 0 | Max: 16776000
    expected_inbandwidth_minimum: int
    # Set the maximum inbandwidth threshold for applying speedtest | Default: 0 | Min: 0 | Max: 16776000
    expected_inbandwidth_maximum: int
    # Set the minimum outbandwidth threshold for applying speedtes | Default: 0 | Min: 0 | Max: 16776000
    expected_outbandwidth_minimum: int
    # Set the maximum outbandwidth threshold for applying speedtes | Default: 0 | Min: 0 | Max: 16776000
    expected_outbandwidth_maximum: int
    # Maximum number of times the FortiGate unit will attempt to c | Default: 5 | Min: 1 | Max: 10
    retries: int
    # Number of seconds the FortiGate pauses between successive sp | Default: 300 | Min: 60 | Max: 3600
    retry_pause: int
    
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
    def to_dict(self) -> SpeedTestSchedulePayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class SpeedTestSchedule:
    """
    Speed test schedule for each interface.
    
    Path: system/speed_test_schedule
    Category: cmdb
    Primary Key: interface
    """
    
    # ================================================================
    # GET OVERLOADS - Always returns FortiObject
    # Pylance matches overloads top-to-bottom, so these must come first!
    # ================================================================
    
    # With mkey as positional arg -> returns FortiObject
    @overload
    def get(
        self,
        interface: str,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> SpeedTestScheduleObject: ...
    
    # With mkey as keyword arg -> returns FortiObject
    @overload
    def get(
        self,
        *,
        interface: str,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> SpeedTestScheduleObject: ...
    
    # Without mkey -> returns list of FortiObjects
    @overload
    def get(
        self,
        interface: None = None,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObjectList[SpeedTestScheduleObject]: ...
    
    # ================================================================
    # (removed - all GET now returns FortiObject)
    # ================================================================
    
    # With mkey as positional arg -> returns single object
    @overload
    def get(
        self,
        interface: str,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> SpeedTestScheduleObject: ...
    
    # With mkey as keyword arg -> returns single object
    @overload
    def get(
        self,
        *,
        interface: str,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> SpeedTestScheduleObject: ...
    
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
    ) -> FortiObjectList[SpeedTestScheduleObject]: ...
    
    # Dict mode with mkey provided as positional arg (single dict)
    @overload
    def get(
        self,
        interface: str,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> SpeedTestScheduleObject: ...
    
    # Dict mode with mkey provided as keyword arg (single dict)
    @overload
    def get(
        self,
        *,
        interface: str,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> SpeedTestScheduleObject: ...
    
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
    ) -> FortiObjectList[SpeedTestScheduleObject]: ...
    
    # Fallback overload for all other cases
    @overload
    def get(
        self,
        interface: str | None = ...,
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
        interface: str | None = ...,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> SpeedTestScheduleObject | list[SpeedTestScheduleObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: SpeedTestSchedulePayload | None = ...,
        interface: str | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        diffserv: str | None = ...,
        server_name: str | None = ...,
        mode: Literal["UDP", "TCP", "Auto"] | None = ...,
        schedules: str | list[str] | list[dict[str, Any]] | None = ...,
        dynamic_server: Literal["disable", "enable"] | None = ...,
        ctrl_port: int | None = ...,
        server_port: int | None = ...,
        update_shaper: Literal["disable", "local", "remote", "both"] | None = ...,
        update_inbandwidth: Literal["disable", "enable"] | None = ...,
        update_outbandwidth: Literal["disable", "enable"] | None = ...,
        update_interface_shaping: Literal["disable", "enable"] | None = ...,
        update_inbandwidth_maximum: int | None = ...,
        update_inbandwidth_minimum: int | None = ...,
        update_outbandwidth_maximum: int | None = ...,
        update_outbandwidth_minimum: int | None = ...,
        expected_inbandwidth_minimum: int | None = ...,
        expected_inbandwidth_maximum: int | None = ...,
        expected_outbandwidth_minimum: int | None = ...,
        expected_outbandwidth_maximum: int | None = ...,
        retries: int | None = ...,
        retry_pause: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> SpeedTestScheduleObject: ...
    
    @overload
    def post(
        self,
        payload_dict: SpeedTestSchedulePayload | None = ...,
        interface: str | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        diffserv: str | None = ...,
        server_name: str | None = ...,
        mode: Literal["UDP", "TCP", "Auto"] | None = ...,
        schedules: str | list[str] | list[dict[str, Any]] | None = ...,
        dynamic_server: Literal["disable", "enable"] | None = ...,
        ctrl_port: int | None = ...,
        server_port: int | None = ...,
        update_shaper: Literal["disable", "local", "remote", "both"] | None = ...,
        update_inbandwidth: Literal["disable", "enable"] | None = ...,
        update_outbandwidth: Literal["disable", "enable"] | None = ...,
        update_interface_shaping: Literal["disable", "enable"] | None = ...,
        update_inbandwidth_maximum: int | None = ...,
        update_inbandwidth_minimum: int | None = ...,
        update_outbandwidth_maximum: int | None = ...,
        update_outbandwidth_minimum: int | None = ...,
        expected_inbandwidth_minimum: int | None = ...,
        expected_inbandwidth_maximum: int | None = ...,
        expected_outbandwidth_minimum: int | None = ...,
        expected_outbandwidth_maximum: int | None = ...,
        retries: int | None = ...,
        retry_pause: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: SpeedTestSchedulePayload | None = ...,
        interface: str | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        diffserv: str | None = ...,
        server_name: str | None = ...,
        mode: Literal["UDP", "TCP", "Auto"] | None = ...,
        schedules: str | list[str] | list[dict[str, Any]] | None = ...,
        dynamic_server: Literal["disable", "enable"] | None = ...,
        ctrl_port: int | None = ...,
        server_port: int | None = ...,
        update_shaper: Literal["disable", "local", "remote", "both"] | None = ...,
        update_inbandwidth: Literal["disable", "enable"] | None = ...,
        update_outbandwidth: Literal["disable", "enable"] | None = ...,
        update_interface_shaping: Literal["disable", "enable"] | None = ...,
        update_inbandwidth_maximum: int | None = ...,
        update_inbandwidth_minimum: int | None = ...,
        update_outbandwidth_maximum: int | None = ...,
        update_outbandwidth_minimum: int | None = ...,
        expected_inbandwidth_minimum: int | None = ...,
        expected_inbandwidth_maximum: int | None = ...,
        expected_outbandwidth_minimum: int | None = ...,
        expected_outbandwidth_maximum: int | None = ...,
        retries: int | None = ...,
        retry_pause: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def post(
        self,
        payload_dict: SpeedTestSchedulePayload | None = ...,
        interface: str | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        diffserv: str | None = ...,
        server_name: str | None = ...,
        mode: Literal["UDP", "TCP", "Auto"] | None = ...,
        schedules: str | list[str] | list[dict[str, Any]] | None = ...,
        dynamic_server: Literal["disable", "enable"] | None = ...,
        ctrl_port: int | None = ...,
        server_port: int | None = ...,
        update_shaper: Literal["disable", "local", "remote", "both"] | None = ...,
        update_inbandwidth: Literal["disable", "enable"] | None = ...,
        update_outbandwidth: Literal["disable", "enable"] | None = ...,
        update_interface_shaping: Literal["disable", "enable"] | None = ...,
        update_inbandwidth_maximum: int | None = ...,
        update_inbandwidth_minimum: int | None = ...,
        update_outbandwidth_maximum: int | None = ...,
        update_outbandwidth_minimum: int | None = ...,
        expected_inbandwidth_minimum: int | None = ...,
        expected_inbandwidth_maximum: int | None = ...,
        expected_outbandwidth_minimum: int | None = ...,
        expected_outbandwidth_maximum: int | None = ...,
        retries: int | None = ...,
        retry_pause: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: SpeedTestSchedulePayload | None = ...,
        interface: str | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        diffserv: str | None = ...,
        server_name: str | None = ...,
        mode: Literal["UDP", "TCP", "Auto"] | None = ...,
        schedules: str | list[str] | list[dict[str, Any]] | None = ...,
        dynamic_server: Literal["disable", "enable"] | None = ...,
        ctrl_port: int | None = ...,
        server_port: int | None = ...,
        update_shaper: Literal["disable", "local", "remote", "both"] | None = ...,
        update_inbandwidth: Literal["disable", "enable"] | None = ...,
        update_outbandwidth: Literal["disable", "enable"] | None = ...,
        update_interface_shaping: Literal["disable", "enable"] | None = ...,
        update_inbandwidth_maximum: int | None = ...,
        update_inbandwidth_minimum: int | None = ...,
        update_outbandwidth_maximum: int | None = ...,
        update_outbandwidth_minimum: int | None = ...,
        expected_inbandwidth_minimum: int | None = ...,
        expected_inbandwidth_maximum: int | None = ...,
        expected_outbandwidth_minimum: int | None = ...,
        expected_outbandwidth_maximum: int | None = ...,
        retries: int | None = ...,
        retry_pause: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> SpeedTestScheduleObject: ...
    
    @overload
    def put(
        self,
        payload_dict: SpeedTestSchedulePayload | None = ...,
        interface: str | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        diffserv: str | None = ...,
        server_name: str | None = ...,
        mode: Literal["UDP", "TCP", "Auto"] | None = ...,
        schedules: str | list[str] | list[dict[str, Any]] | None = ...,
        dynamic_server: Literal["disable", "enable"] | None = ...,
        ctrl_port: int | None = ...,
        server_port: int | None = ...,
        update_shaper: Literal["disable", "local", "remote", "both"] | None = ...,
        update_inbandwidth: Literal["disable", "enable"] | None = ...,
        update_outbandwidth: Literal["disable", "enable"] | None = ...,
        update_interface_shaping: Literal["disable", "enable"] | None = ...,
        update_inbandwidth_maximum: int | None = ...,
        update_inbandwidth_minimum: int | None = ...,
        update_outbandwidth_maximum: int | None = ...,
        update_outbandwidth_minimum: int | None = ...,
        expected_inbandwidth_minimum: int | None = ...,
        expected_inbandwidth_maximum: int | None = ...,
        expected_outbandwidth_minimum: int | None = ...,
        expected_outbandwidth_maximum: int | None = ...,
        retries: int | None = ...,
        retry_pause: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: SpeedTestSchedulePayload | None = ...,
        interface: str | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        diffserv: str | None = ...,
        server_name: str | None = ...,
        mode: Literal["UDP", "TCP", "Auto"] | None = ...,
        schedules: str | list[str] | list[dict[str, Any]] | None = ...,
        dynamic_server: Literal["disable", "enable"] | None = ...,
        ctrl_port: int | None = ...,
        server_port: int | None = ...,
        update_shaper: Literal["disable", "local", "remote", "both"] | None = ...,
        update_inbandwidth: Literal["disable", "enable"] | None = ...,
        update_outbandwidth: Literal["disable", "enable"] | None = ...,
        update_interface_shaping: Literal["disable", "enable"] | None = ...,
        update_inbandwidth_maximum: int | None = ...,
        update_inbandwidth_minimum: int | None = ...,
        update_outbandwidth_maximum: int | None = ...,
        update_outbandwidth_minimum: int | None = ...,
        expected_inbandwidth_minimum: int | None = ...,
        expected_inbandwidth_maximum: int | None = ...,
        expected_outbandwidth_minimum: int | None = ...,
        expected_outbandwidth_maximum: int | None = ...,
        retries: int | None = ...,
        retry_pause: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def put(
        self,
        payload_dict: SpeedTestSchedulePayload | None = ...,
        interface: str | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        diffserv: str | None = ...,
        server_name: str | None = ...,
        mode: Literal["UDP", "TCP", "Auto"] | None = ...,
        schedules: str | list[str] | list[dict[str, Any]] | None = ...,
        dynamic_server: Literal["disable", "enable"] | None = ...,
        ctrl_port: int | None = ...,
        server_port: int | None = ...,
        update_shaper: Literal["disable", "local", "remote", "both"] | None = ...,
        update_inbandwidth: Literal["disable", "enable"] | None = ...,
        update_outbandwidth: Literal["disable", "enable"] | None = ...,
        update_interface_shaping: Literal["disable", "enable"] | None = ...,
        update_inbandwidth_maximum: int | None = ...,
        update_inbandwidth_minimum: int | None = ...,
        update_outbandwidth_maximum: int | None = ...,
        update_outbandwidth_minimum: int | None = ...,
        expected_inbandwidth_minimum: int | None = ...,
        expected_inbandwidth_maximum: int | None = ...,
        expected_outbandwidth_minimum: int | None = ...,
        expected_outbandwidth_maximum: int | None = ...,
        retries: int | None = ...,
        retry_pause: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        interface: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> SpeedTestScheduleObject: ...
    
    @overload
    def delete(
        self,
        interface: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Default overload
    @overload
    def delete(
        self,
        interface: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def delete(
        self,
        interface: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def exists(
        self,
        interface: str,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: SpeedTestSchedulePayload | None = ...,
        interface: str | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        diffserv: str | None = ...,
        server_name: str | None = ...,
        mode: Literal["UDP", "TCP", "Auto"] | None = ...,
        schedules: str | list[str] | list[dict[str, Any]] | None = ...,
        dynamic_server: Literal["disable", "enable"] | None = ...,
        ctrl_port: int | None = ...,
        server_port: int | None = ...,
        update_shaper: Literal["disable", "local", "remote", "both"] | None = ...,
        update_inbandwidth: Literal["disable", "enable"] | None = ...,
        update_outbandwidth: Literal["disable", "enable"] | None = ...,
        update_interface_shaping: Literal["disable", "enable"] | None = ...,
        update_inbandwidth_maximum: int | None = ...,
        update_inbandwidth_minimum: int | None = ...,
        update_outbandwidth_maximum: int | None = ...,
        update_outbandwidth_minimum: int | None = ...,
        expected_inbandwidth_minimum: int | None = ...,
        expected_inbandwidth_maximum: int | None = ...,
        expected_outbandwidth_minimum: int | None = ...,
        expected_outbandwidth_maximum: int | None = ...,
        retries: int | None = ...,
        retry_pause: int | None = ...,
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
    "SpeedTestSchedule",
    "SpeedTestSchedulePayload",
    "SpeedTestScheduleResponse",
    "SpeedTestScheduleObject",
]