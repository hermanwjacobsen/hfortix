from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList
from hfortix_core.types import MutationResponse

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class StandaloneClusterPayload(TypedDict, total=False):
    """
    Type hints for system/standalone_cluster payload fields.
    
    Configure FortiGate Session Life Support Protocol (FGSP) cluster attributes.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.system.interface.InterfaceEndpoint` (via: session-sync-dev)

    **Usage:**
        payload: StandaloneClusterPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    standalone_group_id: int  # Cluster group ID (0 - 255). Must be the same for a | Default: 0 | Min: 0 | Max: 255
    group_member_id: int  # Cluster member ID (0 - 15). | Default: 0 | Min: 0 | Max: 15
    layer2_connection: Literal["available", "unavailable"]  # Indicate whether layer 2 connections are present a | Default: unavailable
    session_sync_dev: list[dict[str, Any]]  # Offload session-sync process to kernel and sync se
    encryption: Literal["enable", "disable"]  # Enable/disable encryption when synchronizing sessi | Default: disable
    psksecret: str  # Pre-shared secret for session synchronization
    asymmetric_traffic_control: Literal["cps-preferred", "strict-anti-replay"]  # Asymmetric traffic control mode. | Default: cps-preferred
    cluster_peer: list[dict[str, Any]]  # Configure FortiGate Session Life Support Protocol
    monitor_interface: list[dict[str, Any]]  # Configure a list of interfaces on which to monitor
    pingsvr_monitor_interface: list[dict[str, Any]]  # List of pingsvr monitor interface to check for rem
    monitor_prefix: list[dict[str, Any]]  # Configure a list of routing prefixes to monitor.
    helper_traffic_bounce: Literal["enable", "disable"]  # Enable/disable helper related traffic bounce. | Default: enable
    utm_traffic_bounce: Literal["enable", "disable"]  # Enable/disable UTM related traffic bounce. | Default: enable

# Nested TypedDicts for table field children (dict mode)

class StandaloneClusterClusterpeerItem(TypedDict):
    """Type hints for cluster-peer table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    sync_id: int  # Sync ID. | Default: 0 | Min: 0 | Max: 4294967295
    peervd: str  # VDOM that contains the session synchronization lin | Default: root | MaxLen: 31
    peerip: str  # IP address of the interface on the peer unit that | Default: 0.0.0.0
    syncvd: str  # Sessions from these VDOMs are synchronized using t
    down_intfs_before_sess_sync: str  # List of interfaces to be turned down before sessio
    hb_interval: int  # Heartbeat interval (1 - 20 | Default: 2 | Min: 1 | Max: 20
    hb_lost_threshold: int  # Lost heartbeat threshold (1 - 60). Increase to red | Default: 10 | Min: 1 | Max: 60
    ipsec_tunnel_sync: Literal["enable", "disable"]  # Enable/disable IPsec tunnel synchronization. | Default: enable
    secondary_add_ipsec_routes: Literal["enable", "disable"]  # Enable/disable IKE route announcement on the backu | Default: enable
    session_sync_filter: str  # Add one or more filters if you only want to synchr


class StandaloneClusterMonitorinterfaceItem(TypedDict):
    """Type hints for monitor-interface table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # Interface name. | MaxLen: 79


class StandaloneClusterPingsvrmonitorinterfaceItem(TypedDict):
    """Type hints for pingsvr-monitor-interface table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # Interface name. | MaxLen: 79


class StandaloneClusterMonitorprefixItem(TypedDict):
    """Type hints for monitor-prefix table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    id: int  # ID. | Default: 0 | Min: 0 | Max: 4294967295
    vdom: str  # VDOM name. | MaxLen: 31
    vrf: int  # VRF ID. | Default: 0 | Min: 0 | Max: 511
    prefix: str  # Prefix. | Default: 0.0.0.0 0.0.0.0


# Nested classes for table field children (object mode)

@final
class StandaloneClusterClusterpeerObject:
    """Typed object for cluster-peer table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Sync ID. | Default: 0 | Min: 0 | Max: 4294967295
    sync_id: int
    # VDOM that contains the session synchronization link interfac | Default: root | MaxLen: 31
    peervd: str
    # IP address of the interface on the peer unit that is used fo | Default: 0.0.0.0
    peerip: str
    # Sessions from these VDOMs are synchronized using this sessio
    syncvd: str
    # List of interfaces to be turned down before session synchron
    down_intfs_before_sess_sync: str
    # Heartbeat interval (1 - 20 | Default: 2 | Min: 1 | Max: 20
    hb_interval: int
    # Lost heartbeat threshold (1 - 60). Increase to reduce false | Default: 10 | Min: 1 | Max: 60
    hb_lost_threshold: int
    # Enable/disable IPsec tunnel synchronization. | Default: enable
    ipsec_tunnel_sync: Literal["enable", "disable"]
    # Enable/disable IKE route announcement on the backup unit. | Default: enable
    secondary_add_ipsec_routes: Literal["enable", "disable"]
    # Add one or more filters if you only want to synchronize some
    session_sync_filter: str
    
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
class StandaloneClusterMonitorinterfaceObject:
    """Typed object for monitor-interface table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Interface name. | MaxLen: 79
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


@final
class StandaloneClusterPingsvrmonitorinterfaceObject:
    """Typed object for pingsvr-monitor-interface table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Interface name. | MaxLen: 79
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


@final
class StandaloneClusterMonitorprefixObject:
    """Typed object for monitor-prefix table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # ID. | Default: 0 | Min: 0 | Max: 4294967295
    id: int
    # VDOM name. | MaxLen: 31
    vdom: str
    # VRF ID. | Default: 0 | Min: 0 | Max: 511
    vrf: int
    # Prefix. | Default: 0.0.0.0 0.0.0.0
    prefix: str
    
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
class StandaloneClusterResponse(TypedDict):
    """
    Type hints for system/standalone_cluster API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    standalone_group_id: int  # Cluster group ID (0 - 255). Must be the same for a | Default: 0 | Min: 0 | Max: 255
    group_member_id: int  # Cluster member ID (0 - 15). | Default: 0 | Min: 0 | Max: 15
    layer2_connection: Literal["available", "unavailable"]  # Indicate whether layer 2 connections are present a | Default: unavailable
    session_sync_dev: list[dict[str, Any]]  # Offload session-sync process to kernel and sync se
    encryption: Literal["enable", "disable"]  # Enable/disable encryption when synchronizing sessi | Default: disable
    psksecret: str  # Pre-shared secret for session synchronization
    asymmetric_traffic_control: Literal["cps-preferred", "strict-anti-replay"]  # Asymmetric traffic control mode. | Default: cps-preferred
    cluster_peer: list[StandaloneClusterClusterpeerItem]  # Configure FortiGate Session Life Support Protocol
    monitor_interface: list[StandaloneClusterMonitorinterfaceItem]  # Configure a list of interfaces on which to monitor
    pingsvr_monitor_interface: list[StandaloneClusterPingsvrmonitorinterfaceItem]  # List of pingsvr monitor interface to check for rem
    monitor_prefix: list[StandaloneClusterMonitorprefixItem]  # Configure a list of routing prefixes to monitor.
    helper_traffic_bounce: Literal["enable", "disable"]  # Enable/disable helper related traffic bounce. | Default: enable
    utm_traffic_bounce: Literal["enable", "disable"]  # Enable/disable UTM related traffic bounce. | Default: enable


@final
class StandaloneClusterObject:
    """Typed FortiObject for system/standalone_cluster with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Cluster group ID (0 - 255). Must be the same for all members | Default: 0 | Min: 0 | Max: 255
    standalone_group_id: int
    # Cluster member ID (0 - 15). | Default: 0 | Min: 0 | Max: 15
    group_member_id: int
    # Indicate whether layer 2 connections are present among FGSP | Default: unavailable
    layer2_connection: Literal["available", "unavailable"]
    # Offload session-sync process to kernel and sync sessions usi
    session_sync_dev: list[dict[str, Any]]
    # Enable/disable encryption when synchronizing sessions. | Default: disable
    encryption: Literal["enable", "disable"]
    # Pre-shared secret for session synchronization
    psksecret: str
    # Asymmetric traffic control mode. | Default: cps-preferred
    asymmetric_traffic_control: Literal["cps-preferred", "strict-anti-replay"]
    # Configure FortiGate Session Life Support Protocol (FGSP) ses
    cluster_peer: list[StandaloneClusterClusterpeerObject]
    # Configure a list of interfaces on which to monitor itself. M
    monitor_interface: list[StandaloneClusterMonitorinterfaceObject]
    # List of pingsvr monitor interface to check for remote IP mon
    pingsvr_monitor_interface: list[StandaloneClusterPingsvrmonitorinterfaceObject]
    # Configure a list of routing prefixes to monitor.
    monitor_prefix: list[StandaloneClusterMonitorprefixObject]
    # Enable/disable helper related traffic bounce. | Default: enable
    helper_traffic_bounce: Literal["enable", "disable"]
    # Enable/disable UTM related traffic bounce. | Default: enable
    utm_traffic_bounce: Literal["enable", "disable"]
    
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
    def to_dict(self) -> StandaloneClusterPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class StandaloneCluster:
    """
    Configure FortiGate Session Life Support Protocol (FGSP) cluster attributes.
    
    Path: system/standalone_cluster
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
    ) -> StandaloneClusterObject: ...
    
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
    ) -> StandaloneClusterObject: ...
    
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
    ) -> StandaloneClusterObject: ...
    
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
    ) -> StandaloneClusterObject: ...
    
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
    ) -> StandaloneClusterObject: ...
    
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
    ) -> StandaloneClusterObject: ...
    
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
    ) -> StandaloneClusterObject: ...
    
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
    ) -> StandaloneClusterObject: ...
    
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
    ) -> StandaloneClusterObject: ...
    
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
    ) -> StandaloneClusterObject | dict[str, Any]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: StandaloneClusterPayload | None = ...,
        standalone_group_id: int | None = ...,
        group_member_id: int | None = ...,
        layer2_connection: Literal["available", "unavailable"] | None = ...,
        session_sync_dev: str | list[str] | None = ...,
        encryption: Literal["enable", "disable"] | None = ...,
        psksecret: str | None = ...,
        asymmetric_traffic_control: Literal["cps-preferred", "strict-anti-replay"] | None = ...,
        cluster_peer: str | list[str] | list[dict[str, Any]] | None = ...,
        monitor_interface: str | list[str] | list[dict[str, Any]] | None = ...,
        pingsvr_monitor_interface: str | list[str] | list[dict[str, Any]] | None = ...,
        monitor_prefix: str | list[str] | list[dict[str, Any]] | None = ...,
        helper_traffic_bounce: Literal["enable", "disable"] | None = ...,
        utm_traffic_bounce: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> StandaloneClusterObject: ...
    
    @overload
    def put(
        self,
        payload_dict: StandaloneClusterPayload | None = ...,
        standalone_group_id: int | None = ...,
        group_member_id: int | None = ...,
        layer2_connection: Literal["available", "unavailable"] | None = ...,
        session_sync_dev: str | list[str] | None = ...,
        encryption: Literal["enable", "disable"] | None = ...,
        psksecret: str | None = ...,
        asymmetric_traffic_control: Literal["cps-preferred", "strict-anti-replay"] | None = ...,
        cluster_peer: str | list[str] | list[dict[str, Any]] | None = ...,
        monitor_interface: str | list[str] | list[dict[str, Any]] | None = ...,
        pingsvr_monitor_interface: str | list[str] | list[dict[str, Any]] | None = ...,
        monitor_prefix: str | list[str] | list[dict[str, Any]] | None = ...,
        helper_traffic_bounce: Literal["enable", "disable"] | None = ...,
        utm_traffic_bounce: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: StandaloneClusterPayload | None = ...,
        standalone_group_id: int | None = ...,
        group_member_id: int | None = ...,
        layer2_connection: Literal["available", "unavailable"] | None = ...,
        session_sync_dev: str | list[str] | None = ...,
        encryption: Literal["enable", "disable"] | None = ...,
        psksecret: str | None = ...,
        asymmetric_traffic_control: Literal["cps-preferred", "strict-anti-replay"] | None = ...,
        cluster_peer: str | list[str] | list[dict[str, Any]] | None = ...,
        monitor_interface: str | list[str] | list[dict[str, Any]] | None = ...,
        pingsvr_monitor_interface: str | list[str] | list[dict[str, Any]] | None = ...,
        monitor_prefix: str | list[str] | list[dict[str, Any]] | None = ...,
        helper_traffic_bounce: Literal["enable", "disable"] | None = ...,
        utm_traffic_bounce: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def put(
        self,
        payload_dict: StandaloneClusterPayload | None = ...,
        standalone_group_id: int | None = ...,
        group_member_id: int | None = ...,
        layer2_connection: Literal["available", "unavailable"] | None = ...,
        session_sync_dev: str | list[str] | None = ...,
        encryption: Literal["enable", "disable"] | None = ...,
        psksecret: str | None = ...,
        asymmetric_traffic_control: Literal["cps-preferred", "strict-anti-replay"] | None = ...,
        cluster_peer: str | list[str] | list[dict[str, Any]] | None = ...,
        monitor_interface: str | list[str] | list[dict[str, Any]] | None = ...,
        pingsvr_monitor_interface: str | list[str] | list[dict[str, Any]] | None = ...,
        monitor_prefix: str | list[str] | list[dict[str, Any]] | None = ...,
        helper_traffic_bounce: Literal["enable", "disable"] | None = ...,
        utm_traffic_bounce: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: StandaloneClusterPayload | None = ...,
        standalone_group_id: int | None = ...,
        group_member_id: int | None = ...,
        layer2_connection: Literal["available", "unavailable"] | None = ...,
        session_sync_dev: str | list[str] | None = ...,
        encryption: Literal["enable", "disable"] | None = ...,
        psksecret: str | None = ...,
        asymmetric_traffic_control: Literal["cps-preferred", "strict-anti-replay"] | None = ...,
        cluster_peer: str | list[str] | list[dict[str, Any]] | None = ...,
        monitor_interface: str | list[str] | list[dict[str, Any]] | None = ...,
        pingsvr_monitor_interface: str | list[str] | list[dict[str, Any]] | None = ...,
        monitor_prefix: str | list[str] | list[dict[str, Any]] | None = ...,
        helper_traffic_bounce: Literal["enable", "disable"] | None = ...,
        utm_traffic_bounce: Literal["enable", "disable"] | None = ...,
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
    "StandaloneCluster",
    "StandaloneClusterPayload",
    "StandaloneClusterResponse",
    "StandaloneClusterObject",
]