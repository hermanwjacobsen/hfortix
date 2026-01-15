from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class GlobalPayload(TypedDict, total=False):
    """
    Type hints for ips/global_ payload fields.
    
    Configure IPS global parameter.
    
    **Usage:**
        payload: GlobalPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    fail_open: Literal["enable", "disable"]  # Enable to allow traffic if the IPS buffer is full. | Default: disable
    database: Literal["regular", "extended"]  # Regular or extended IPS database. Regular protects | Default: extended
    traffic_submit: Literal["enable", "disable"]  # Enable/disable submitting attack data found by thi | Default: disable
    anomaly_mode: Literal["periodical", "continuous"]  # Global blocking mode for rate-based anomalies. | Default: continuous
    session_limit_mode: Literal["accurate", "heuristic"]  # Method of counting concurrent sessions used by ses | Default: heuristic
    socket_size: int  # IPS socket buffer size. Max and default value depe | Default: 256 | Min: 0 | Max: 512
    engine_count: int  # Number of IPS engines running. If set to the defau | Default: 0 | Min: 0 | Max: 255
    sync_session_ttl: Literal["enable", "disable"]  # Enable/disable use of kernel session TTL for IPS s | Default: enable
    deep_app_insp_timeout: int  # Timeout for Deep application inspection | Default: 0 | Min: 0 | Max: 2147483647
    deep_app_insp_db_limit: int  # Limit on number of entries in deep application ins | Default: 0 | Min: 0 | Max: 2147483647
    exclude_signatures: Literal["none", "ot"]  # Excluded signatures. | Default: ot
    packet_log_queue_depth: int  # Packet/pcap log queue depth per IPS engine. | Default: 128 | Min: 128 | Max: 4096
    ngfw_max_scan_range: int  # NGFW policy-mode app detection threshold. | Default: 4096 | Min: 0 | Max: 4294967295
    av_mem_limit: int  # Maximum percentage of system memory allowed for us | Default: 0 | Min: 10 | Max: 50
    machine_learning_detection: Literal["enable", "disable"]  # Enable/disable machine learning detection. | Default: enable
    tls_active_probe: str  # TLS active probe configuration.

# Nested TypedDicts for table field children (dict mode)

# Nested classes for table field children (object mode)


# Response TypedDict for GET returns (all fields present in API response)
class GlobalResponse(TypedDict):
    """
    Type hints for ips/global_ API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    fail_open: Literal["enable", "disable"]  # Enable to allow traffic if the IPS buffer is full. | Default: disable
    database: Literal["regular", "extended"]  # Regular or extended IPS database. Regular protects | Default: extended
    traffic_submit: Literal["enable", "disable"]  # Enable/disable submitting attack data found by thi | Default: disable
    anomaly_mode: Literal["periodical", "continuous"]  # Global blocking mode for rate-based anomalies. | Default: continuous
    session_limit_mode: Literal["accurate", "heuristic"]  # Method of counting concurrent sessions used by ses | Default: heuristic
    socket_size: int  # IPS socket buffer size. Max and default value depe | Default: 256 | Min: 0 | Max: 512
    engine_count: int  # Number of IPS engines running. If set to the defau | Default: 0 | Min: 0 | Max: 255
    sync_session_ttl: Literal["enable", "disable"]  # Enable/disable use of kernel session TTL for IPS s | Default: enable
    deep_app_insp_timeout: int  # Timeout for Deep application inspection | Default: 0 | Min: 0 | Max: 2147483647
    deep_app_insp_db_limit: int  # Limit on number of entries in deep application ins | Default: 0 | Min: 0 | Max: 2147483647
    exclude_signatures: Literal["none", "ot"]  # Excluded signatures. | Default: ot
    packet_log_queue_depth: int  # Packet/pcap log queue depth per IPS engine. | Default: 128 | Min: 128 | Max: 4096
    ngfw_max_scan_range: int  # NGFW policy-mode app detection threshold. | Default: 4096 | Min: 0 | Max: 4294967295
    av_mem_limit: int  # Maximum percentage of system memory allowed for us | Default: 0 | Min: 10 | Max: 50
    machine_learning_detection: Literal["enable", "disable"]  # Enable/disable machine learning detection. | Default: enable
    tls_active_probe: str  # TLS active probe configuration.


@final
class GlobalObject:
    """Typed FortiObject for ips/global_ with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Enable to allow traffic if the IPS buffer is full. Default i | Default: disable
    fail_open: Literal["enable", "disable"]
    # Regular or extended IPS database. Regular protects against t | Default: extended
    database: Literal["regular", "extended"]
    # Enable/disable submitting attack data found by this FortiGat | Default: disable
    traffic_submit: Literal["enable", "disable"]
    # Global blocking mode for rate-based anomalies. | Default: continuous
    anomaly_mode: Literal["periodical", "continuous"]
    # Method of counting concurrent sessions used by session limit | Default: heuristic
    session_limit_mode: Literal["accurate", "heuristic"]
    # IPS socket buffer size. Max and default value depend on avai | Default: 256 | Min: 0 | Max: 512
    socket_size: int
    # Number of IPS engines running. If set to the default value o | Default: 0 | Min: 0 | Max: 255
    engine_count: int
    # Enable/disable use of kernel session TTL for IPS sessions. | Default: enable
    sync_session_ttl: Literal["enable", "disable"]
    # Timeout for Deep application inspection | Default: 0 | Min: 0 | Max: 2147483647
    deep_app_insp_timeout: int
    # Limit on number of entries in deep application inspection da | Default: 0 | Min: 0 | Max: 2147483647
    deep_app_insp_db_limit: int
    # Excluded signatures. | Default: ot
    exclude_signatures: Literal["none", "ot"]
    # Packet/pcap log queue depth per IPS engine. | Default: 128 | Min: 128 | Max: 4096
    packet_log_queue_depth: int
    # NGFW policy-mode app detection threshold. | Default: 4096 | Min: 0 | Max: 4294967295
    ngfw_max_scan_range: int
    # Maximum percentage of system memory allowed for use on AV sc | Default: 0 | Min: 10 | Max: 50
    av_mem_limit: int
    # Enable/disable machine learning detection. | Default: enable
    machine_learning_detection: Literal["enable", "disable"]
    # TLS active probe configuration.
    tls_active_probe: str
    
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
    def to_dict(self) -> GlobalPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Global:
    """
    Configure IPS global parameter.
    
    Path: ips/global_
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
    ) -> GlobalObject: ...
    
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
    ) -> GlobalObject: ...
    
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
    ) -> GlobalObject: ...
    
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
    ) -> GlobalObject: ...
    
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
    ) -> GlobalObject: ...
    
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
    ) -> GlobalObject: ...
    
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
    ) -> GlobalObject: ...
    
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
    ) -> GlobalObject: ...
    
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
    ) -> GlobalObject: ...
    
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
    ) -> GlobalObject | dict[str, Any]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: GlobalPayload | None = ...,
        fail_open: Literal["enable", "disable"] | None = ...,
        database: Literal["regular", "extended"] | None = ...,
        traffic_submit: Literal["enable", "disable"] | None = ...,
        anomaly_mode: Literal["periodical", "continuous"] | None = ...,
        session_limit_mode: Literal["accurate", "heuristic"] | None = ...,
        socket_size: int | None = ...,
        engine_count: int | None = ...,
        sync_session_ttl: Literal["enable", "disable"] | None = ...,
        deep_app_insp_timeout: int | None = ...,
        deep_app_insp_db_limit: int | None = ...,
        exclude_signatures: Literal["none", "ot"] | None = ...,
        packet_log_queue_depth: int | None = ...,
        ngfw_max_scan_range: int | None = ...,
        av_mem_limit: int | None = ...,
        machine_learning_detection: Literal["enable", "disable"] | None = ...,
        tls_active_probe: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> GlobalObject: ...
    
    @overload
    def put(
        self,
        payload_dict: GlobalPayload | None = ...,
        fail_open: Literal["enable", "disable"] | None = ...,
        database: Literal["regular", "extended"] | None = ...,
        traffic_submit: Literal["enable", "disable"] | None = ...,
        anomaly_mode: Literal["periodical", "continuous"] | None = ...,
        session_limit_mode: Literal["accurate", "heuristic"] | None = ...,
        socket_size: int | None = ...,
        engine_count: int | None = ...,
        sync_session_ttl: Literal["enable", "disable"] | None = ...,
        deep_app_insp_timeout: int | None = ...,
        deep_app_insp_db_limit: int | None = ...,
        exclude_signatures: Literal["none", "ot"] | None = ...,
        packet_log_queue_depth: int | None = ...,
        ngfw_max_scan_range: int | None = ...,
        av_mem_limit: int | None = ...,
        machine_learning_detection: Literal["enable", "disable"] | None = ...,
        tls_active_probe: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: GlobalPayload | None = ...,
        fail_open: Literal["enable", "disable"] | None = ...,
        database: Literal["regular", "extended"] | None = ...,
        traffic_submit: Literal["enable", "disable"] | None = ...,
        anomaly_mode: Literal["periodical", "continuous"] | None = ...,
        session_limit_mode: Literal["accurate", "heuristic"] | None = ...,
        socket_size: int | None = ...,
        engine_count: int | None = ...,
        sync_session_ttl: Literal["enable", "disable"] | None = ...,
        deep_app_insp_timeout: int | None = ...,
        deep_app_insp_db_limit: int | None = ...,
        exclude_signatures: Literal["none", "ot"] | None = ...,
        packet_log_queue_depth: int | None = ...,
        ngfw_max_scan_range: int | None = ...,
        av_mem_limit: int | None = ...,
        machine_learning_detection: Literal["enable", "disable"] | None = ...,
        tls_active_probe: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def put(
        self,
        payload_dict: GlobalPayload | None = ...,
        fail_open: Literal["enable", "disable"] | None = ...,
        database: Literal["regular", "extended"] | None = ...,
        traffic_submit: Literal["enable", "disable"] | None = ...,
        anomaly_mode: Literal["periodical", "continuous"] | None = ...,
        session_limit_mode: Literal["accurate", "heuristic"] | None = ...,
        socket_size: int | None = ...,
        engine_count: int | None = ...,
        sync_session_ttl: Literal["enable", "disable"] | None = ...,
        deep_app_insp_timeout: int | None = ...,
        deep_app_insp_db_limit: int | None = ...,
        exclude_signatures: Literal["none", "ot"] | None = ...,
        packet_log_queue_depth: int | None = ...,
        ngfw_max_scan_range: int | None = ...,
        av_mem_limit: int | None = ...,
        machine_learning_detection: Literal["enable", "disable"] | None = ...,
        tls_active_probe: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: GlobalPayload | None = ...,
        fail_open: Literal["enable", "disable"] | None = ...,
        database: Literal["regular", "extended"] | None = ...,
        traffic_submit: Literal["enable", "disable"] | None = ...,
        anomaly_mode: Literal["periodical", "continuous"] | None = ...,
        session_limit_mode: Literal["accurate", "heuristic"] | None = ...,
        socket_size: int | None = ...,
        engine_count: int | None = ...,
        sync_session_ttl: Literal["enable", "disable"] | None = ...,
        deep_app_insp_timeout: int | None = ...,
        deep_app_insp_db_limit: int | None = ...,
        exclude_signatures: Literal["none", "ot"] | None = ...,
        packet_log_queue_depth: int | None = ...,
        ngfw_max_scan_range: int | None = ...,
        av_mem_limit: int | None = ...,
        machine_learning_detection: Literal["enable", "disable"] | None = ...,
        tls_active_probe: str | None = ...,
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
    "Global",
    "GlobalPayload",
    "GlobalResponse",
    "GlobalObject",
]