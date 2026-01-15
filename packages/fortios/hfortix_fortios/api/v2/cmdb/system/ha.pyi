from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject
from hfortix_core.types import MutationResponse, RawAPIResponse

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class HaPayload(TypedDict, total=False):
    """
    Type hints for system/ha payload fields.
    
    Configure HA.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.system.interface.InterfaceEndpoint` (via: monitor, pingserver-monitor-interface, session-sync-dev)

    **Usage:**
        payload: HaPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    group_id: int  # HA group ID | Default: 0 | Min: 0 | Max: 1023
    group_name: str  # Cluster group name. Must be the same for all membe | MaxLen: 32
    mode: Literal["standalone", "a-a", "a-p"]  # HA mode. Must be the same for all members. FGSP re | Default: standalone
    sync_packet_balance: Literal["enable", "disable"]  # Enable/disable HA packet distribution to multiple | Default: disable
    password: str  # Cluster password. Must be the same for all members | MaxLen: 128
    key: str  # Key. | MaxLen: 16
    hbdev: list[dict[str, Any]]  # Heartbeat interfaces. Must be the same for all mem
    auto_virtual_mac_interface: list[dict[str, Any]]  # The physical interface that will be assigned an au
    backup_hbdev: list[dict[str, Any]]  # Backup heartbeat interfaces. Must be the same for
    unicast_hb: Literal["enable", "disable"]  # Enable/disable unicast heartbeat. | Default: disable
    unicast_hb_peerip: str  # Unicast heartbeat peer IP. | Default: 0.0.0.0
    unicast_hb_netmask: str  # Unicast heartbeat netmask. | Default: 0.0.0.0
    session_sync_dev: list[dict[str, Any]]  # Offload session-sync process to kernel and sync se
    route_ttl: int  # TTL for primary unit routes (5 - 3600 sec). Increa | Default: 10 | Min: 5 | Max: 3600
    route_wait: int  # Time to wait before sending new routes to the clus | Default: 0 | Min: 0 | Max: 3600
    route_hold: int  # Time to wait between routing table updates to the | Default: 10 | Min: 0 | Max: 3600
    multicast_ttl: int  # HA multicast TTL on primary (5 - 3600 sec). | Default: 600 | Min: 5 | Max: 3600
    evpn_ttl: int  # HA EVPN FDB TTL on primary box (5 - 3600 sec). | Default: 60 | Min: 5 | Max: 3600
    load_balance_all: Literal["enable", "disable"]  # Enable to load balance TCP sessions. Disable to lo | Default: disable
    sync_config: Literal["enable", "disable"]  # Enable/disable configuration synchronization. | Default: enable
    encryption: Literal["enable", "disable"]  # Enable/disable heartbeat message encryption. | Default: disable
    authentication: Literal["enable", "disable"]  # Enable/disable heartbeat message authentication. | Default: disable
    hb_interval: int  # Time between sending heartbeat packets (1 - 20). I | Default: 2 | Min: 1 | Max: 20
    hb_interval_in_milliseconds: Literal["100ms", "10ms"]  # Units of heartbeat interval time between sending h | Default: 100ms
    hb_lost_threshold: int  # Number of lost heartbeats to signal a failure | Default: 20 | Min: 1 | Max: 60
    hello_holddown: int  # Time to wait before changing from hello to work st | Default: 20 | Min: 5 | Max: 300
    gratuitous_arps: Literal["enable", "disable"]  # Enable/disable gratuitous ARPs. Disable if link-fa | Default: enable
    arps: int  # Number of gratuitous ARPs (1 - 60). Lower to reduc | Default: 5 | Min: 1 | Max: 60
    arps_interval: int  # Time between gratuitous ARPs  (1 - 20 sec). Lower | Default: 8 | Min: 1 | Max: 20
    session_pickup: Literal["enable", "disable"]  # Enable/disable session pickup. Enabling it can red | Default: disable
    session_pickup_connectionless: Literal["enable", "disable"]  # Enable/disable UDP and ICMP session sync. | Default: disable
    session_pickup_expectation: Literal["enable", "disable"]  # Enable/disable session helper expectation session | Default: disable
    session_pickup_nat: Literal["enable", "disable"]  # Enable/disable NAT session sync for FGSP. | Default: disable
    session_pickup_delay: Literal["enable", "disable"]  # Enable to sync sessions longer than 30 sec. Only l | Default: disable
    link_failed_signal: Literal["enable", "disable"]  # Enable to shut down all interfaces for 1 sec after | Default: disable
    upgrade_mode: Literal["simultaneous", "uninterruptible", "local-only", "secondary-only"]  # The mode to upgrade a cluster. | Default: uninterruptible
    uninterruptible_primary_wait: int  # Number of minutes the primary HA unit waits before | Default: 30 | Min: 15 | Max: 300
    standalone_mgmt_vdom: Literal["enable", "disable"]  # Enable/disable standalone management VDOM. | Default: disable
    ha_mgmt_status: Literal["enable", "disable"]  # Enable to reserve interfaces to manage individual | Default: disable
    ha_mgmt_interfaces: list[dict[str, Any]]  # Reserve interfaces to manage individual cluster un
    ha_eth_type: str  # HA heartbeat packet Ethertype (4-digit hex). | Default: 8890 | MaxLen: 4
    hc_eth_type: str  # Transparent mode HA heartbeat packet Ethertype | Default: 8891 | MaxLen: 4
    l2ep_eth_type: str  # Telnet session HA heartbeat packet Ethertype | Default: 8893 | MaxLen: 4
    ha_uptime_diff_margin: int  # Normally you would only reduce this value for fail | Default: 300 | Min: 1 | Max: 65535
    standalone_config_sync: Literal["enable", "disable"]  # Enable/disable FGSP configuration synchronization. | Default: disable
    unicast_status: Literal["enable", "disable"]  # Enable/disable unicast connection. | Default: disable
    unicast_gateway: str  # Default route gateway for unicast interface. | Default: 0.0.0.0
    unicast_peers: list[dict[str, Any]]  # Number of unicast peers.
    schedule: Literal["none", "leastconnection", "round-robin", "weight-round-robin", "random", "ip", "ipport"]  # Type of A-A load balancing. Use none if you have e | Default: round-robin
    weight: str  # Weight-round-robin weight for each cluster unit. S | Default: 0 40
    cpu_threshold: str  # Dynamic weighted load balancing CPU usage weight a
    memory_threshold: str  # Dynamic weighted load balancing memory usage weigh
    http_proxy_threshold: str  # Dynamic weighted load balancing weight and high an
    ftp_proxy_threshold: str  # Dynamic weighted load balancing weight and high an
    imap_proxy_threshold: str  # Dynamic weighted load balancing weight and high an
    nntp_proxy_threshold: str  # Dynamic weighted load balancing weight and high an
    pop3_proxy_threshold: str  # Dynamic weighted load balancing weight and high an
    smtp_proxy_threshold: str  # Dynamic weighted load balancing weight and high an
    override: Literal["enable", "disable"]  # Enable and increase the priority of the unit that | Default: disable
    priority: int  # Increase the priority to select the primary unit | Default: 128 | Min: 0 | Max: 255
    override_wait_time: int  # Delay negotiating if override is enabled | Default: 0 | Min: 0 | Max: 3600
    monitor: list[dict[str, Any]]  # Interfaces to check for port monitoring
    pingserver_monitor_interface: list[dict[str, Any]]  # Interfaces to check for remote IP monitoring.
    pingserver_failover_threshold: int  # Remote IP monitoring failover threshold (0 - 50). | Default: 0 | Min: 0 | Max: 50
    pingserver_secondary_force_reset: Literal["enable", "disable"]  # Enable to force the cluster to negotiate after a r | Default: enable
    pingserver_flip_timeout: int  # Time to wait in minutes before renegotiating after | Default: 60 | Min: 6 | Max: 2147483647
    vcluster_status: Literal["enable", "disable"]  # Enable/disable virtual cluster for virtual cluster | Default: disable
    vcluster: list[dict[str, Any]]  # Virtual cluster table.
    ha_direct: Literal["enable", "disable"]  # Enable/disable using ha-mgmt interface for syslog, | Default: disable
    ssd_failover: Literal["enable", "disable"]  # Enable/disable automatic HA failover on SSD disk f | Default: disable
    memory_compatible_mode: Literal["enable", "disable"]  # Enable/disable memory compatible mode. | Default: disable
    memory_based_failover: Literal["enable", "disable"]  # Enable/disable memory based failover. | Default: disable
    memory_failover_threshold: int  # Memory usage threshold to trigger memory based fai | Default: 0 | Min: 0 | Max: 95
    memory_failover_monitor_period: int  # Duration of high memory usage before memory based | Default: 60 | Min: 1 | Max: 300
    memory_failover_sample_rate: int  # Rate at which memory usage is sampled in order to | Default: 1 | Min: 1 | Max: 60
    memory_failover_flip_timeout: int  # Time to wait between subsequent memory based failo | Default: 6 | Min: 6 | Max: 2147483647
    failover_hold_time: int  # Time to wait before failover | Default: 0 | Min: 0 | Max: 300
    check_secondary_dev_health: Literal["enable", "disable"]  # Enable/disable secondary dev health check for sess | Default: disable
    ipsec_phase2_proposal: Literal["aes128-sha1", "aes128-sha256", "aes128-sha384", "aes128-sha512", "aes192-sha1", "aes192-sha256", "aes192-sha384", "aes192-sha512", "aes256-sha1", "aes256-sha256", "aes256-sha384", "aes256-sha512", "aes128gcm", "aes256gcm", "chacha20poly1305"]  # IPsec phase2 proposal.
    bounce_intf_upon_failover: Literal["enable", "disable"]  # Enable/disable notification of kernel to bring dow | Default: disable
    status: str  # list ha status information

# Nested TypedDicts for table field children (dict mode)

class HaAutovirtualmacinterfaceItem(TypedDict):
    """Type hints for auto-virtual-mac-interface table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    interface_name: str  # Interface name. | MaxLen: 15


class HaBackuphbdevItem(TypedDict):
    """Type hints for backup-hbdev table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # Interface name. | MaxLen: 79


class HaHamgmtinterfacesItem(TypedDict):
    """Type hints for ha-mgmt-interfaces table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    id: int  # Table ID. | Default: 0 | Min: 0 | Max: 4294967295
    interface: str  # Interface to reserve for HA management. | MaxLen: 15
    dst: str  # Default route destination for reserved HA manageme | Default: 0.0.0.0 0.0.0.0
    gateway: str  # Default route gateway for reserved HA management i | Default: 0.0.0.0
    dst6: str  # Default IPv6 destination for reserved HA managemen | Default: ::/0
    gateway6: str  # Default IPv6 gateway for reserved HA management in | Default: ::


class HaUnicastpeersItem(TypedDict):
    """Type hints for unicast-peers table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    id: int  # Table ID. | Default: 0 | Min: 0 | Max: 4294967295
    peer_ip: str  # Unicast peer IP. | Default: 0.0.0.0


class HaVclusterItem(TypedDict):
    """Type hints for vcluster table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    vcluster_id: int  # ID. | Default: 1 | Min: 1 | Max: 30
    override: Literal["enable", "disable"]  # Enable and increase the priority of the unit that | Default: disable
    priority: int  # Increase the priority to select the primary unit | Default: 128 | Min: 0 | Max: 255
    override_wait_time: int  # Delay negotiating if override is enabled | Default: 0 | Min: 0 | Max: 3600
    monitor: str  # Interfaces to check for port monitoring
    pingserver_monitor_interface: str  # Interfaces to check for remote IP monitoring.
    pingserver_failover_threshold: int  # Remote IP monitoring failover threshold (0 - 50). | Default: 0 | Min: 0 | Max: 50
    pingserver_secondary_force_reset: Literal["enable", "disable"]  # Enable to force the cluster to negotiate after a r | Default: enable
    pingserver_flip_timeout: int  # Time to wait in minutes before renegotiating after | Default: 60 | Min: 6 | Max: 2147483647
    vdom: str  # Virtual domain(s) in the virtual cluster.


# Nested classes for table field children (object mode)

@final
class HaAutovirtualmacinterfaceObject:
    """Typed object for auto-virtual-mac-interface table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Interface name. | MaxLen: 15
    interface_name: str
    
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
class HaBackuphbdevObject:
    """Typed object for backup-hbdev table items.
    
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
class HaHamgmtinterfacesObject:
    """Typed object for ha-mgmt-interfaces table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Table ID. | Default: 0 | Min: 0 | Max: 4294967295
    id: int
    # Interface to reserve for HA management. | MaxLen: 15
    interface: str
    # Default route destination for reserved HA management interfa | Default: 0.0.0.0 0.0.0.0
    dst: str
    # Default route gateway for reserved HA management interface. | Default: 0.0.0.0
    gateway: str
    # Default IPv6 destination for reserved HA management interfac | Default: ::/0
    dst6: str
    # Default IPv6 gateway for reserved HA management interface. | Default: ::
    gateway6: str
    
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
class HaUnicastpeersObject:
    """Typed object for unicast-peers table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Table ID. | Default: 0 | Min: 0 | Max: 4294967295
    id: int
    # Unicast peer IP. | Default: 0.0.0.0
    peer_ip: str
    
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
class HaVclusterObject:
    """Typed object for vcluster table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # ID. | Default: 1 | Min: 1 | Max: 30
    vcluster_id: int
    # Enable and increase the priority of the unit that should alw | Default: disable
    override: Literal["enable", "disable"]
    # Increase the priority to select the primary unit (0 - 255). | Default: 128 | Min: 0 | Max: 255
    priority: int
    # Delay negotiating if override is enabled (0 - 3600 sec). Red | Default: 0 | Min: 0 | Max: 3600
    override_wait_time: int
    # Interfaces to check for port monitoring (or link failure).
    monitor: str
    # Interfaces to check for remote IP monitoring.
    pingserver_monitor_interface: str
    # Remote IP monitoring failover threshold (0 - 50). | Default: 0 | Min: 0 | Max: 50
    pingserver_failover_threshold: int
    # Enable to force the cluster to negotiate after a remote IP m | Default: enable
    pingserver_secondary_force_reset: Literal["enable", "disable"]
    # Time to wait in minutes before renegotiating after a remote | Default: 60 | Min: 6 | Max: 2147483647
    pingserver_flip_timeout: int
    # Virtual domain(s) in the virtual cluster.
    vdom: str
    
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
class HaResponse(TypedDict):
    """
    Type hints for system/ha API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    group_id: int  # HA group ID | Default: 0 | Min: 0 | Max: 1023
    group_name: str  # Cluster group name. Must be the same for all membe | MaxLen: 32
    mode: Literal["standalone", "a-a", "a-p"]  # HA mode. Must be the same for all members. FGSP re | Default: standalone
    sync_packet_balance: Literal["enable", "disable"]  # Enable/disable HA packet distribution to multiple | Default: disable
    password: str  # Cluster password. Must be the same for all members | MaxLen: 128
    key: str  # Key. | MaxLen: 16
    hbdev: list[dict[str, Any]]  # Heartbeat interfaces. Must be the same for all mem
    auto_virtual_mac_interface: list[HaAutovirtualmacinterfaceItem]  # The physical interface that will be assigned an au
    backup_hbdev: list[HaBackuphbdevItem]  # Backup heartbeat interfaces. Must be the same for
    unicast_hb: Literal["enable", "disable"]  # Enable/disable unicast heartbeat. | Default: disable
    unicast_hb_peerip: str  # Unicast heartbeat peer IP. | Default: 0.0.0.0
    unicast_hb_netmask: str  # Unicast heartbeat netmask. | Default: 0.0.0.0
    session_sync_dev: list[dict[str, Any]]  # Offload session-sync process to kernel and sync se
    route_ttl: int  # TTL for primary unit routes (5 - 3600 sec). Increa | Default: 10 | Min: 5 | Max: 3600
    route_wait: int  # Time to wait before sending new routes to the clus | Default: 0 | Min: 0 | Max: 3600
    route_hold: int  # Time to wait between routing table updates to the | Default: 10 | Min: 0 | Max: 3600
    multicast_ttl: int  # HA multicast TTL on primary (5 - 3600 sec). | Default: 600 | Min: 5 | Max: 3600
    evpn_ttl: int  # HA EVPN FDB TTL on primary box (5 - 3600 sec). | Default: 60 | Min: 5 | Max: 3600
    load_balance_all: Literal["enable", "disable"]  # Enable to load balance TCP sessions. Disable to lo | Default: disable
    sync_config: Literal["enable", "disable"]  # Enable/disable configuration synchronization. | Default: enable
    encryption: Literal["enable", "disable"]  # Enable/disable heartbeat message encryption. | Default: disable
    authentication: Literal["enable", "disable"]  # Enable/disable heartbeat message authentication. | Default: disable
    hb_interval: int  # Time between sending heartbeat packets (1 - 20). I | Default: 2 | Min: 1 | Max: 20
    hb_interval_in_milliseconds: Literal["100ms", "10ms"]  # Units of heartbeat interval time between sending h | Default: 100ms
    hb_lost_threshold: int  # Number of lost heartbeats to signal a failure | Default: 20 | Min: 1 | Max: 60
    hello_holddown: int  # Time to wait before changing from hello to work st | Default: 20 | Min: 5 | Max: 300
    gratuitous_arps: Literal["enable", "disable"]  # Enable/disable gratuitous ARPs. Disable if link-fa | Default: enable
    arps: int  # Number of gratuitous ARPs (1 - 60). Lower to reduc | Default: 5 | Min: 1 | Max: 60
    arps_interval: int  # Time between gratuitous ARPs  (1 - 20 sec). Lower | Default: 8 | Min: 1 | Max: 20
    session_pickup: Literal["enable", "disable"]  # Enable/disable session pickup. Enabling it can red | Default: disable
    session_pickup_connectionless: Literal["enable", "disable"]  # Enable/disable UDP and ICMP session sync. | Default: disable
    session_pickup_expectation: Literal["enable", "disable"]  # Enable/disable session helper expectation session | Default: disable
    session_pickup_nat: Literal["enable", "disable"]  # Enable/disable NAT session sync for FGSP. | Default: disable
    session_pickup_delay: Literal["enable", "disable"]  # Enable to sync sessions longer than 30 sec. Only l | Default: disable
    link_failed_signal: Literal["enable", "disable"]  # Enable to shut down all interfaces for 1 sec after | Default: disable
    upgrade_mode: Literal["simultaneous", "uninterruptible", "local-only", "secondary-only"]  # The mode to upgrade a cluster. | Default: uninterruptible
    uninterruptible_primary_wait: int  # Number of minutes the primary HA unit waits before | Default: 30 | Min: 15 | Max: 300
    standalone_mgmt_vdom: Literal["enable", "disable"]  # Enable/disable standalone management VDOM. | Default: disable
    ha_mgmt_status: Literal["enable", "disable"]  # Enable to reserve interfaces to manage individual | Default: disable
    ha_mgmt_interfaces: list[HaHamgmtinterfacesItem]  # Reserve interfaces to manage individual cluster un
    ha_eth_type: str  # HA heartbeat packet Ethertype (4-digit hex). | Default: 8890 | MaxLen: 4
    hc_eth_type: str  # Transparent mode HA heartbeat packet Ethertype | Default: 8891 | MaxLen: 4
    l2ep_eth_type: str  # Telnet session HA heartbeat packet Ethertype | Default: 8893 | MaxLen: 4
    ha_uptime_diff_margin: int  # Normally you would only reduce this value for fail | Default: 300 | Min: 1 | Max: 65535
    standalone_config_sync: Literal["enable", "disable"]  # Enable/disable FGSP configuration synchronization. | Default: disable
    unicast_status: Literal["enable", "disable"]  # Enable/disable unicast connection. | Default: disable
    unicast_gateway: str  # Default route gateway for unicast interface. | Default: 0.0.0.0
    unicast_peers: list[HaUnicastpeersItem]  # Number of unicast peers.
    schedule: Literal["none", "leastconnection", "round-robin", "weight-round-robin", "random", "ip", "ipport"]  # Type of A-A load balancing. Use none if you have e | Default: round-robin
    weight: str  # Weight-round-robin weight for each cluster unit. S | Default: 0 40
    cpu_threshold: str  # Dynamic weighted load balancing CPU usage weight a
    memory_threshold: str  # Dynamic weighted load balancing memory usage weigh
    http_proxy_threshold: str  # Dynamic weighted load balancing weight and high an
    ftp_proxy_threshold: str  # Dynamic weighted load balancing weight and high an
    imap_proxy_threshold: str  # Dynamic weighted load balancing weight and high an
    nntp_proxy_threshold: str  # Dynamic weighted load balancing weight and high an
    pop3_proxy_threshold: str  # Dynamic weighted load balancing weight and high an
    smtp_proxy_threshold: str  # Dynamic weighted load balancing weight and high an
    override: Literal["enable", "disable"]  # Enable and increase the priority of the unit that | Default: disable
    priority: int  # Increase the priority to select the primary unit | Default: 128 | Min: 0 | Max: 255
    override_wait_time: int  # Delay negotiating if override is enabled | Default: 0 | Min: 0 | Max: 3600
    monitor: list[dict[str, Any]]  # Interfaces to check for port monitoring
    pingserver_monitor_interface: list[dict[str, Any]]  # Interfaces to check for remote IP monitoring.
    pingserver_failover_threshold: int  # Remote IP monitoring failover threshold (0 - 50). | Default: 0 | Min: 0 | Max: 50
    pingserver_secondary_force_reset: Literal["enable", "disable"]  # Enable to force the cluster to negotiate after a r | Default: enable
    pingserver_flip_timeout: int  # Time to wait in minutes before renegotiating after | Default: 60 | Min: 6 | Max: 2147483647
    vcluster_status: Literal["enable", "disable"]  # Enable/disable virtual cluster for virtual cluster | Default: disable
    vcluster: list[HaVclusterItem]  # Virtual cluster table.
    ha_direct: Literal["enable", "disable"]  # Enable/disable using ha-mgmt interface for syslog, | Default: disable
    ssd_failover: Literal["enable", "disable"]  # Enable/disable automatic HA failover on SSD disk f | Default: disable
    memory_compatible_mode: Literal["enable", "disable"]  # Enable/disable memory compatible mode. | Default: disable
    memory_based_failover: Literal["enable", "disable"]  # Enable/disable memory based failover. | Default: disable
    memory_failover_threshold: int  # Memory usage threshold to trigger memory based fai | Default: 0 | Min: 0 | Max: 95
    memory_failover_monitor_period: int  # Duration of high memory usage before memory based | Default: 60 | Min: 1 | Max: 300
    memory_failover_sample_rate: int  # Rate at which memory usage is sampled in order to | Default: 1 | Min: 1 | Max: 60
    memory_failover_flip_timeout: int  # Time to wait between subsequent memory based failo | Default: 6 | Min: 6 | Max: 2147483647
    failover_hold_time: int  # Time to wait before failover | Default: 0 | Min: 0 | Max: 300
    check_secondary_dev_health: Literal["enable", "disable"]  # Enable/disable secondary dev health check for sess | Default: disable
    ipsec_phase2_proposal: Literal["aes128-sha1", "aes128-sha256", "aes128-sha384", "aes128-sha512", "aes192-sha1", "aes192-sha256", "aes192-sha384", "aes192-sha512", "aes256-sha1", "aes256-sha256", "aes256-sha384", "aes256-sha512", "aes128gcm", "aes256gcm", "chacha20poly1305"]  # IPsec phase2 proposal.
    bounce_intf_upon_failover: Literal["enable", "disable"]  # Enable/disable notification of kernel to bring dow | Default: disable
    status: str  # list ha status information


@final
class HaObject:
    """Typed FortiObject for system/ha with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # HA group ID | Default: 0 | Min: 0 | Max: 1023
    group_id: int
    # Cluster group name. Must be the same for all members. | MaxLen: 32
    group_name: str
    # HA mode. Must be the same for all members. FGSP requires sta | Default: standalone
    mode: Literal["standalone", "a-a", "a-p"]
    # Enable/disable HA packet distribution to multiple CPUs. | Default: disable
    sync_packet_balance: Literal["enable", "disable"]
    # Cluster password. Must be the same for all members. | MaxLen: 128
    password: str
    # Key. | MaxLen: 16
    key: str
    # Heartbeat interfaces. Must be the same for all members.
    hbdev: list[dict[str, Any]]
    # The physical interface that will be assigned an auto-generat
    auto_virtual_mac_interface: list[HaAutovirtualmacinterfaceObject]
    # Backup heartbeat interfaces. Must be the same for all member
    backup_hbdev: list[HaBackuphbdevObject]
    # Enable/disable unicast heartbeat. | Default: disable
    unicast_hb: Literal["enable", "disable"]
    # Unicast heartbeat peer IP. | Default: 0.0.0.0
    unicast_hb_peerip: str
    # Unicast heartbeat netmask. | Default: 0.0.0.0
    unicast_hb_netmask: str
    # Offload session-sync process to kernel and sync sessions usi
    session_sync_dev: list[dict[str, Any]]
    # TTL for primary unit routes (5 - 3600 sec). Increase to main | Default: 10 | Min: 5 | Max: 3600
    route_ttl: int
    # Time to wait before sending new routes to the cluster | Default: 0 | Min: 0 | Max: 3600
    route_wait: int
    # Time to wait between routing table updates to the cluster | Default: 10 | Min: 0 | Max: 3600
    route_hold: int
    # HA multicast TTL on primary (5 - 3600 sec). | Default: 600 | Min: 5 | Max: 3600
    multicast_ttl: int
    # HA EVPN FDB TTL on primary box (5 - 3600 sec). | Default: 60 | Min: 5 | Max: 3600
    evpn_ttl: int
    # Enable to load balance TCP sessions. Disable to load balance | Default: disable
    load_balance_all: Literal["enable", "disable"]
    # Enable/disable configuration synchronization. | Default: enable
    sync_config: Literal["enable", "disable"]
    # Enable/disable heartbeat message encryption. | Default: disable
    encryption: Literal["enable", "disable"]
    # Enable/disable heartbeat message authentication. | Default: disable
    authentication: Literal["enable", "disable"]
    # Time between sending heartbeat packets (1 - 20). Increase to | Default: 2 | Min: 1 | Max: 20
    hb_interval: int
    # Units of heartbeat interval time between sending heartbeat p | Default: 100ms
    hb_interval_in_milliseconds: Literal["100ms", "10ms"]
    # Number of lost heartbeats to signal a failure (1 - 60). Incr | Default: 20 | Min: 1 | Max: 60
    hb_lost_threshold: int
    # Time to wait before changing from hello to work state | Default: 20 | Min: 5 | Max: 300
    hello_holddown: int
    # Enable/disable gratuitous ARPs. Disable if link-failed-signa | Default: enable
    gratuitous_arps: Literal["enable", "disable"]
    # Number of gratuitous ARPs (1 - 60). Lower to reduce traffic. | Default: 5 | Min: 1 | Max: 60
    arps: int
    # Time between gratuitous ARPs  (1 - 20 sec). Lower to reduce | Default: 8 | Min: 1 | Max: 20
    arps_interval: int
    # Enable/disable session pickup. Enabling it can reduce sessio | Default: disable
    session_pickup: Literal["enable", "disable"]
    # Enable/disable UDP and ICMP session sync. | Default: disable
    session_pickup_connectionless: Literal["enable", "disable"]
    # Enable/disable session helper expectation session sync for F | Default: disable
    session_pickup_expectation: Literal["enable", "disable"]
    # Enable/disable NAT session sync for FGSP. | Default: disable
    session_pickup_nat: Literal["enable", "disable"]
    # Enable to sync sessions longer than 30 sec. Only longer live | Default: disable
    session_pickup_delay: Literal["enable", "disable"]
    # Enable to shut down all interfaces for 1 sec after a failove | Default: disable
    link_failed_signal: Literal["enable", "disable"]
    # The mode to upgrade a cluster. | Default: uninterruptible
    upgrade_mode: Literal["simultaneous", "uninterruptible", "local-only", "secondary-only"]
    # Number of minutes the primary HA unit waits before the secon | Default: 30 | Min: 15 | Max: 300
    uninterruptible_primary_wait: int
    # Enable/disable standalone management VDOM. | Default: disable
    standalone_mgmt_vdom: Literal["enable", "disable"]
    # Enable to reserve interfaces to manage individual cluster un | Default: disable
    ha_mgmt_status: Literal["enable", "disable"]
    # Reserve interfaces to manage individual cluster units.
    ha_mgmt_interfaces: list[HaHamgmtinterfacesObject]
    # HA heartbeat packet Ethertype (4-digit hex). | Default: 8890 | MaxLen: 4
    ha_eth_type: str
    # Transparent mode HA heartbeat packet Ethertype (4-digit hex) | Default: 8891 | MaxLen: 4
    hc_eth_type: str
    # Telnet session HA heartbeat packet Ethertype (4-digit hex). | Default: 8893 | MaxLen: 4
    l2ep_eth_type: str
    # Normally you would only reduce this value for failover testi | Default: 300 | Min: 1 | Max: 65535
    ha_uptime_diff_margin: int
    # Enable/disable FGSP configuration synchronization. | Default: disable
    standalone_config_sync: Literal["enable", "disable"]
    # Enable/disable unicast connection. | Default: disable
    unicast_status: Literal["enable", "disable"]
    # Default route gateway for unicast interface. | Default: 0.0.0.0
    unicast_gateway: str
    # Number of unicast peers.
    unicast_peers: list[HaUnicastpeersObject]
    # Type of A-A load balancing. Use none if you have external lo | Default: round-robin
    schedule: Literal["none", "leastconnection", "round-robin", "weight-round-robin", "random", "ip", "ipport"]
    # Weight-round-robin weight for each cluster unit. Syntax <pri | Default: 0 40
    weight: str
    # Dynamic weighted load balancing CPU usage weight and high an
    cpu_threshold: str
    # Dynamic weighted load balancing memory usage weight and high
    memory_threshold: str
    # Dynamic weighted load balancing weight and high and low numb
    http_proxy_threshold: str
    # Dynamic weighted load balancing weight and high and low numb
    ftp_proxy_threshold: str
    # Dynamic weighted load balancing weight and high and low numb
    imap_proxy_threshold: str
    # Dynamic weighted load balancing weight and high and low numb
    nntp_proxy_threshold: str
    # Dynamic weighted load balancing weight and high and low numb
    pop3_proxy_threshold: str
    # Dynamic weighted load balancing weight and high and low numb
    smtp_proxy_threshold: str
    # Enable and increase the priority of the unit that should alw | Default: disable
    override: Literal["enable", "disable"]
    # Increase the priority to select the primary unit (0 - 255). | Default: 128 | Min: 0 | Max: 255
    priority: int
    # Delay negotiating if override is enabled (0 - 3600 sec). Red | Default: 0 | Min: 0 | Max: 3600
    override_wait_time: int
    # Interfaces to check for port monitoring (or link failure).
    monitor: list[dict[str, Any]]
    # Interfaces to check for remote IP monitoring.
    pingserver_monitor_interface: list[dict[str, Any]]
    # Remote IP monitoring failover threshold (0 - 50). | Default: 0 | Min: 0 | Max: 50
    pingserver_failover_threshold: int
    # Enable to force the cluster to negotiate after a remote IP m | Default: enable
    pingserver_secondary_force_reset: Literal["enable", "disable"]
    # Time to wait in minutes before renegotiating after a remote | Default: 60 | Min: 6 | Max: 2147483647
    pingserver_flip_timeout: int
    # Enable/disable virtual cluster for virtual clustering. | Default: disable
    vcluster_status: Literal["enable", "disable"]
    # Virtual cluster table.
    vcluster: list[HaVclusterObject]
    # Enable/disable using ha-mgmt interface for syslog, remote au | Default: disable
    ha_direct: Literal["enable", "disable"]
    # Enable/disable automatic HA failover on SSD disk failure. | Default: disable
    ssd_failover: Literal["enable", "disable"]
    # Enable/disable memory compatible mode. | Default: disable
    memory_compatible_mode: Literal["enable", "disable"]
    # Enable/disable memory based failover. | Default: disable
    memory_based_failover: Literal["enable", "disable"]
    # Memory usage threshold to trigger memory based failover | Default: 0 | Min: 0 | Max: 95
    memory_failover_threshold: int
    # Duration of high memory usage before memory based failover i | Default: 60 | Min: 1 | Max: 300
    memory_failover_monitor_period: int
    # Rate at which memory usage is sampled in order to measure me | Default: 1 | Min: 1 | Max: 60
    memory_failover_sample_rate: int
    # Time to wait between subsequent memory based failovers in mi | Default: 6 | Min: 6 | Max: 2147483647
    memory_failover_flip_timeout: int
    # Time to wait before failover (0 - 300 sec, default = 0), to | Default: 0 | Min: 0 | Max: 300
    failover_hold_time: int
    # Enable/disable secondary dev health check for session load-b | Default: disable
    check_secondary_dev_health: Literal["enable", "disable"]
    # IPsec phase2 proposal.
    ipsec_phase2_proposal: Literal["aes128-sha1", "aes128-sha256", "aes128-sha384", "aes128-sha512", "aes192-sha1", "aes192-sha256", "aes192-sha384", "aes192-sha512", "aes256-sha1", "aes256-sha256", "aes256-sha384", "aes256-sha512", "aes128gcm", "aes256gcm", "chacha20poly1305"]
    # Enable/disable notification of kernel to bring down and up a | Default: disable
    bounce_intf_upon_failover: Literal["enable", "disable"]
    # list ha status information
    status: str
    
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
    def to_dict(self) -> HaPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Ha:
    """
    Configure HA.
    
    Path: system/ha
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
    ) -> HaObject: ...
    
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
    ) -> HaObject: ...
    
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
    ) -> HaObject: ...
    
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
        raw_json: Literal[False] = ...,
        *,
        **kwargs: Any,
    ) -> HaObject: ...
    
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
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> HaObject: ...
    
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
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> HaObject: ...
    
    # raw_json=True returns the full API envelope
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
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> RawAPIResponse: ...
    
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
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> HaObject: ...
    
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
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> HaObject: ...
    
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
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> HaObject: ...
    
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
        raw_json: bool = ...,
        **kwargs: Any,
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
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> HaObject | dict[str, Any]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: HaPayload | None = ...,
        group_id: int | None = ...,
        group_name: str | None = ...,
        mode: Literal["standalone", "a-a", "a-p"] | None = ...,
        sync_packet_balance: Literal["enable", "disable"] | None = ...,
        password: str | None = ...,
        key: str | None = ...,
        hbdev: str | list[str] | None = ...,
        auto_virtual_mac_interface: str | list[str] | list[dict[str, Any]] | None = ...,
        backup_hbdev: str | list[str] | list[dict[str, Any]] | None = ...,
        unicast_hb: Literal["enable", "disable"] | None = ...,
        unicast_hb_peerip: str | None = ...,
        unicast_hb_netmask: str | None = ...,
        session_sync_dev: str | list[str] | None = ...,
        route_ttl: int | None = ...,
        route_wait: int | None = ...,
        route_hold: int | None = ...,
        multicast_ttl: int | None = ...,
        evpn_ttl: int | None = ...,
        load_balance_all: Literal["enable", "disable"] | None = ...,
        sync_config: Literal["enable", "disable"] | None = ...,
        encryption: Literal["enable", "disable"] | None = ...,
        authentication: Literal["enable", "disable"] | None = ...,
        hb_interval: int | None = ...,
        hb_interval_in_milliseconds: Literal["100ms", "10ms"] | None = ...,
        hb_lost_threshold: int | None = ...,
        hello_holddown: int | None = ...,
        gratuitous_arps: Literal["enable", "disable"] | None = ...,
        arps: int | None = ...,
        arps_interval: int | None = ...,
        session_pickup: Literal["enable", "disable"] | None = ...,
        session_pickup_connectionless: Literal["enable", "disable"] | None = ...,
        session_pickup_expectation: Literal["enable", "disable"] | None = ...,
        session_pickup_nat: Literal["enable", "disable"] | None = ...,
        session_pickup_delay: Literal["enable", "disable"] | None = ...,
        link_failed_signal: Literal["enable", "disable"] | None = ...,
        upgrade_mode: Literal["simultaneous", "uninterruptible", "local-only", "secondary-only"] | None = ...,
        uninterruptible_primary_wait: int | None = ...,
        standalone_mgmt_vdom: Literal["enable", "disable"] | None = ...,
        ha_mgmt_status: Literal["enable", "disable"] | None = ...,
        ha_mgmt_interfaces: str | list[str] | list[dict[str, Any]] | None = ...,
        ha_eth_type: str | None = ...,
        hc_eth_type: str | None = ...,
        l2ep_eth_type: str | None = ...,
        ha_uptime_diff_margin: int | None = ...,
        standalone_config_sync: Literal["enable", "disable"] | None = ...,
        unicast_status: Literal["enable", "disable"] | None = ...,
        unicast_gateway: str | None = ...,
        unicast_peers: str | list[str] | list[dict[str, Any]] | None = ...,
        schedule: Literal["none", "leastconnection", "round-robin", "weight-round-robin", "random", "ip", "ipport"] | None = ...,
        weight: str | None = ...,
        cpu_threshold: str | None = ...,
        memory_threshold: str | None = ...,
        http_proxy_threshold: str | None = ...,
        ftp_proxy_threshold: str | None = ...,
        imap_proxy_threshold: str | None = ...,
        nntp_proxy_threshold: str | None = ...,
        pop3_proxy_threshold: str | None = ...,
        smtp_proxy_threshold: str | None = ...,
        override: Literal["enable", "disable"] | None = ...,
        priority: int | None = ...,
        override_wait_time: int | None = ...,
        monitor: str | list[str] | None = ...,
        pingserver_monitor_interface: str | list[str] | None = ...,
        pingserver_failover_threshold: int | None = ...,
        pingserver_secondary_force_reset: Literal["enable", "disable"] | None = ...,
        pingserver_flip_timeout: int | None = ...,
        vcluster_status: Literal["enable", "disable"] | None = ...,
        vcluster: str | list[str] | list[dict[str, Any]] | None = ...,
        ha_direct: Literal["enable", "disable"] | None = ...,
        ssd_failover: Literal["enable", "disable"] | None = ...,
        memory_compatible_mode: Literal["enable", "disable"] | None = ...,
        memory_based_failover: Literal["enable", "disable"] | None = ...,
        memory_failover_threshold: int | None = ...,
        memory_failover_monitor_period: int | None = ...,
        memory_failover_sample_rate: int | None = ...,
        memory_failover_flip_timeout: int | None = ...,
        failover_hold_time: int | None = ...,
        check_secondary_dev_health: Literal["enable", "disable"] | None = ...,
        ipsec_phase2_proposal: Literal["aes128-sha1", "aes128-sha256", "aes128-sha384", "aes128-sha512", "aes192-sha1", "aes192-sha256", "aes192-sha384", "aes192-sha512", "aes256-sha1", "aes256-sha256", "aes256-sha384", "aes256-sha512", "aes128gcm", "aes256gcm", "chacha20poly1305"] | list[str] | None = ...,
        bounce_intf_upon_failover: Literal["enable", "disable"] | None = ...,
        status: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> HaObject: ...
    
    @overload
    def put(
        self,
        payload_dict: HaPayload | None = ...,
        group_id: int | None = ...,
        group_name: str | None = ...,
        mode: Literal["standalone", "a-a", "a-p"] | None = ...,
        sync_packet_balance: Literal["enable", "disable"] | None = ...,
        password: str | None = ...,
        key: str | None = ...,
        hbdev: str | list[str] | None = ...,
        auto_virtual_mac_interface: str | list[str] | list[dict[str, Any]] | None = ...,
        backup_hbdev: str | list[str] | list[dict[str, Any]] | None = ...,
        unicast_hb: Literal["enable", "disable"] | None = ...,
        unicast_hb_peerip: str | None = ...,
        unicast_hb_netmask: str | None = ...,
        session_sync_dev: str | list[str] | None = ...,
        route_ttl: int | None = ...,
        route_wait: int | None = ...,
        route_hold: int | None = ...,
        multicast_ttl: int | None = ...,
        evpn_ttl: int | None = ...,
        load_balance_all: Literal["enable", "disable"] | None = ...,
        sync_config: Literal["enable", "disable"] | None = ...,
        encryption: Literal["enable", "disable"] | None = ...,
        authentication: Literal["enable", "disable"] | None = ...,
        hb_interval: int | None = ...,
        hb_interval_in_milliseconds: Literal["100ms", "10ms"] | None = ...,
        hb_lost_threshold: int | None = ...,
        hello_holddown: int | None = ...,
        gratuitous_arps: Literal["enable", "disable"] | None = ...,
        arps: int | None = ...,
        arps_interval: int | None = ...,
        session_pickup: Literal["enable", "disable"] | None = ...,
        session_pickup_connectionless: Literal["enable", "disable"] | None = ...,
        session_pickup_expectation: Literal["enable", "disable"] | None = ...,
        session_pickup_nat: Literal["enable", "disable"] | None = ...,
        session_pickup_delay: Literal["enable", "disable"] | None = ...,
        link_failed_signal: Literal["enable", "disable"] | None = ...,
        upgrade_mode: Literal["simultaneous", "uninterruptible", "local-only", "secondary-only"] | None = ...,
        uninterruptible_primary_wait: int | None = ...,
        standalone_mgmt_vdom: Literal["enable", "disable"] | None = ...,
        ha_mgmt_status: Literal["enable", "disable"] | None = ...,
        ha_mgmt_interfaces: str | list[str] | list[dict[str, Any]] | None = ...,
        ha_eth_type: str | None = ...,
        hc_eth_type: str | None = ...,
        l2ep_eth_type: str | None = ...,
        ha_uptime_diff_margin: int | None = ...,
        standalone_config_sync: Literal["enable", "disable"] | None = ...,
        unicast_status: Literal["enable", "disable"] | None = ...,
        unicast_gateway: str | None = ...,
        unicast_peers: str | list[str] | list[dict[str, Any]] | None = ...,
        schedule: Literal["none", "leastconnection", "round-robin", "weight-round-robin", "random", "ip", "ipport"] | None = ...,
        weight: str | None = ...,
        cpu_threshold: str | None = ...,
        memory_threshold: str | None = ...,
        http_proxy_threshold: str | None = ...,
        ftp_proxy_threshold: str | None = ...,
        imap_proxy_threshold: str | None = ...,
        nntp_proxy_threshold: str | None = ...,
        pop3_proxy_threshold: str | None = ...,
        smtp_proxy_threshold: str | None = ...,
        override: Literal["enable", "disable"] | None = ...,
        priority: int | None = ...,
        override_wait_time: int | None = ...,
        monitor: str | list[str] | None = ...,
        pingserver_monitor_interface: str | list[str] | None = ...,
        pingserver_failover_threshold: int | None = ...,
        pingserver_secondary_force_reset: Literal["enable", "disable"] | None = ...,
        pingserver_flip_timeout: int | None = ...,
        vcluster_status: Literal["enable", "disable"] | None = ...,
        vcluster: str | list[str] | list[dict[str, Any]] | None = ...,
        ha_direct: Literal["enable", "disable"] | None = ...,
        ssd_failover: Literal["enable", "disable"] | None = ...,
        memory_compatible_mode: Literal["enable", "disable"] | None = ...,
        memory_based_failover: Literal["enable", "disable"] | None = ...,
        memory_failover_threshold: int | None = ...,
        memory_failover_monitor_period: int | None = ...,
        memory_failover_sample_rate: int | None = ...,
        memory_failover_flip_timeout: int | None = ...,
        failover_hold_time: int | None = ...,
        check_secondary_dev_health: Literal["enable", "disable"] | None = ...,
        ipsec_phase2_proposal: Literal["aes128-sha1", "aes128-sha256", "aes128-sha384", "aes128-sha512", "aes192-sha1", "aes192-sha256", "aes192-sha384", "aes192-sha512", "aes256-sha1", "aes256-sha256", "aes256-sha384", "aes256-sha512", "aes128gcm", "aes256gcm", "chacha20poly1305"] | list[str] | None = ...,
        bounce_intf_upon_failover: Literal["enable", "disable"] | None = ...,
        status: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    # raw_json=True returns the full API envelope
    @overload
    def put(
        self,
        payload_dict: HaPayload | None = ...,
        group_id: int | None = ...,
        group_name: str | None = ...,
        mode: Literal["standalone", "a-a", "a-p"] | None = ...,
        sync_packet_balance: Literal["enable", "disable"] | None = ...,
        password: str | None = ...,
        key: str | None = ...,
        hbdev: str | list[str] | None = ...,
        auto_virtual_mac_interface: str | list[str] | list[dict[str, Any]] | None = ...,
        backup_hbdev: str | list[str] | list[dict[str, Any]] | None = ...,
        unicast_hb: Literal["enable", "disable"] | None = ...,
        unicast_hb_peerip: str | None = ...,
        unicast_hb_netmask: str | None = ...,
        session_sync_dev: str | list[str] | None = ...,
        route_ttl: int | None = ...,
        route_wait: int | None = ...,
        route_hold: int | None = ...,
        multicast_ttl: int | None = ...,
        evpn_ttl: int | None = ...,
        load_balance_all: Literal["enable", "disable"] | None = ...,
        sync_config: Literal["enable", "disable"] | None = ...,
        encryption: Literal["enable", "disable"] | None = ...,
        authentication: Literal["enable", "disable"] | None = ...,
        hb_interval: int | None = ...,
        hb_interval_in_milliseconds: Literal["100ms", "10ms"] | None = ...,
        hb_lost_threshold: int | None = ...,
        hello_holddown: int | None = ...,
        gratuitous_arps: Literal["enable", "disable"] | None = ...,
        arps: int | None = ...,
        arps_interval: int | None = ...,
        session_pickup: Literal["enable", "disable"] | None = ...,
        session_pickup_connectionless: Literal["enable", "disable"] | None = ...,
        session_pickup_expectation: Literal["enable", "disable"] | None = ...,
        session_pickup_nat: Literal["enable", "disable"] | None = ...,
        session_pickup_delay: Literal["enable", "disable"] | None = ...,
        link_failed_signal: Literal["enable", "disable"] | None = ...,
        upgrade_mode: Literal["simultaneous", "uninterruptible", "local-only", "secondary-only"] | None = ...,
        uninterruptible_primary_wait: int | None = ...,
        standalone_mgmt_vdom: Literal["enable", "disable"] | None = ...,
        ha_mgmt_status: Literal["enable", "disable"] | None = ...,
        ha_mgmt_interfaces: str | list[str] | list[dict[str, Any]] | None = ...,
        ha_eth_type: str | None = ...,
        hc_eth_type: str | None = ...,
        l2ep_eth_type: str | None = ...,
        ha_uptime_diff_margin: int | None = ...,
        standalone_config_sync: Literal["enable", "disable"] | None = ...,
        unicast_status: Literal["enable", "disable"] | None = ...,
        unicast_gateway: str | None = ...,
        unicast_peers: str | list[str] | list[dict[str, Any]] | None = ...,
        schedule: Literal["none", "leastconnection", "round-robin", "weight-round-robin", "random", "ip", "ipport"] | None = ...,
        weight: str | None = ...,
        cpu_threshold: str | None = ...,
        memory_threshold: str | None = ...,
        http_proxy_threshold: str | None = ...,
        ftp_proxy_threshold: str | None = ...,
        imap_proxy_threshold: str | None = ...,
        nntp_proxy_threshold: str | None = ...,
        pop3_proxy_threshold: str | None = ...,
        smtp_proxy_threshold: str | None = ...,
        override: Literal["enable", "disable"] | None = ...,
        priority: int | None = ...,
        override_wait_time: int | None = ...,
        monitor: str | list[str] | None = ...,
        pingserver_monitor_interface: str | list[str] | None = ...,
        pingserver_failover_threshold: int | None = ...,
        pingserver_secondary_force_reset: Literal["enable", "disable"] | None = ...,
        pingserver_flip_timeout: int | None = ...,
        vcluster_status: Literal["enable", "disable"] | None = ...,
        vcluster: str | list[str] | list[dict[str, Any]] | None = ...,
        ha_direct: Literal["enable", "disable"] | None = ...,
        ssd_failover: Literal["enable", "disable"] | None = ...,
        memory_compatible_mode: Literal["enable", "disable"] | None = ...,
        memory_based_failover: Literal["enable", "disable"] | None = ...,
        memory_failover_threshold: int | None = ...,
        memory_failover_monitor_period: int | None = ...,
        memory_failover_sample_rate: int | None = ...,
        memory_failover_flip_timeout: int | None = ...,
        failover_hold_time: int | None = ...,
        check_secondary_dev_health: Literal["enable", "disable"] | None = ...,
        ipsec_phase2_proposal: Literal["aes128-sha1", "aes128-sha256", "aes128-sha384", "aes128-sha512", "aes192-sha1", "aes192-sha256", "aes192-sha384", "aes192-sha512", "aes256-sha1", "aes256-sha256", "aes256-sha384", "aes256-sha512", "aes128gcm", "aes256gcm", "chacha20poly1305"] | list[str] | None = ...,
        bounce_intf_upon_failover: Literal["enable", "disable"] | None = ...,
        status: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> RawAPIResponse: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: HaPayload | None = ...,
        group_id: int | None = ...,
        group_name: str | None = ...,
        mode: Literal["standalone", "a-a", "a-p"] | None = ...,
        sync_packet_balance: Literal["enable", "disable"] | None = ...,
        password: str | None = ...,
        key: str | None = ...,
        hbdev: str | list[str] | None = ...,
        auto_virtual_mac_interface: str | list[str] | list[dict[str, Any]] | None = ...,
        backup_hbdev: str | list[str] | list[dict[str, Any]] | None = ...,
        unicast_hb: Literal["enable", "disable"] | None = ...,
        unicast_hb_peerip: str | None = ...,
        unicast_hb_netmask: str | None = ...,
        session_sync_dev: str | list[str] | None = ...,
        route_ttl: int | None = ...,
        route_wait: int | None = ...,
        route_hold: int | None = ...,
        multicast_ttl: int | None = ...,
        evpn_ttl: int | None = ...,
        load_balance_all: Literal["enable", "disable"] | None = ...,
        sync_config: Literal["enable", "disable"] | None = ...,
        encryption: Literal["enable", "disable"] | None = ...,
        authentication: Literal["enable", "disable"] | None = ...,
        hb_interval: int | None = ...,
        hb_interval_in_milliseconds: Literal["100ms", "10ms"] | None = ...,
        hb_lost_threshold: int | None = ...,
        hello_holddown: int | None = ...,
        gratuitous_arps: Literal["enable", "disable"] | None = ...,
        arps: int | None = ...,
        arps_interval: int | None = ...,
        session_pickup: Literal["enable", "disable"] | None = ...,
        session_pickup_connectionless: Literal["enable", "disable"] | None = ...,
        session_pickup_expectation: Literal["enable", "disable"] | None = ...,
        session_pickup_nat: Literal["enable", "disable"] | None = ...,
        session_pickup_delay: Literal["enable", "disable"] | None = ...,
        link_failed_signal: Literal["enable", "disable"] | None = ...,
        upgrade_mode: Literal["simultaneous", "uninterruptible", "local-only", "secondary-only"] | None = ...,
        uninterruptible_primary_wait: int | None = ...,
        standalone_mgmt_vdom: Literal["enable", "disable"] | None = ...,
        ha_mgmt_status: Literal["enable", "disable"] | None = ...,
        ha_mgmt_interfaces: str | list[str] | list[dict[str, Any]] | None = ...,
        ha_eth_type: str | None = ...,
        hc_eth_type: str | None = ...,
        l2ep_eth_type: str | None = ...,
        ha_uptime_diff_margin: int | None = ...,
        standalone_config_sync: Literal["enable", "disable"] | None = ...,
        unicast_status: Literal["enable", "disable"] | None = ...,
        unicast_gateway: str | None = ...,
        unicast_peers: str | list[str] | list[dict[str, Any]] | None = ...,
        schedule: Literal["none", "leastconnection", "round-robin", "weight-round-robin", "random", "ip", "ipport"] | None = ...,
        weight: str | None = ...,
        cpu_threshold: str | None = ...,
        memory_threshold: str | None = ...,
        http_proxy_threshold: str | None = ...,
        ftp_proxy_threshold: str | None = ...,
        imap_proxy_threshold: str | None = ...,
        nntp_proxy_threshold: str | None = ...,
        pop3_proxy_threshold: str | None = ...,
        smtp_proxy_threshold: str | None = ...,
        override: Literal["enable", "disable"] | None = ...,
        priority: int | None = ...,
        override_wait_time: int | None = ...,
        monitor: str | list[str] | None = ...,
        pingserver_monitor_interface: str | list[str] | None = ...,
        pingserver_failover_threshold: int | None = ...,
        pingserver_secondary_force_reset: Literal["enable", "disable"] | None = ...,
        pingserver_flip_timeout: int | None = ...,
        vcluster_status: Literal["enable", "disable"] | None = ...,
        vcluster: str | list[str] | list[dict[str, Any]] | None = ...,
        ha_direct: Literal["enable", "disable"] | None = ...,
        ssd_failover: Literal["enable", "disable"] | None = ...,
        memory_compatible_mode: Literal["enable", "disable"] | None = ...,
        memory_based_failover: Literal["enable", "disable"] | None = ...,
        memory_failover_threshold: int | None = ...,
        memory_failover_monitor_period: int | None = ...,
        memory_failover_sample_rate: int | None = ...,
        memory_failover_flip_timeout: int | None = ...,
        failover_hold_time: int | None = ...,
        check_secondary_dev_health: Literal["enable", "disable"] | None = ...,
        ipsec_phase2_proposal: Literal["aes128-sha1", "aes128-sha256", "aes128-sha384", "aes128-sha512", "aes192-sha1", "aes192-sha256", "aes192-sha384", "aes192-sha512", "aes256-sha1", "aes256-sha256", "aes256-sha384", "aes256-sha512", "aes128gcm", "aes256gcm", "chacha20poly1305"] | list[str] | None = ...,
        bounce_intf_upon_failover: Literal["enable", "disable"] | None = ...,
        status: str | None = ...,
        vdom: str | bool | None = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    def put(
        self,
        payload_dict: HaPayload | None = ...,
        group_id: int | None = ...,
        group_name: str | None = ...,
        mode: Literal["standalone", "a-a", "a-p"] | None = ...,
        sync_packet_balance: Literal["enable", "disable"] | None = ...,
        password: str | None = ...,
        key: str | None = ...,
        hbdev: str | list[str] | None = ...,
        auto_virtual_mac_interface: str | list[str] | list[dict[str, Any]] | None = ...,
        backup_hbdev: str | list[str] | list[dict[str, Any]] | None = ...,
        unicast_hb: Literal["enable", "disable"] | None = ...,
        unicast_hb_peerip: str | None = ...,
        unicast_hb_netmask: str | None = ...,
        session_sync_dev: str | list[str] | None = ...,
        route_ttl: int | None = ...,
        route_wait: int | None = ...,
        route_hold: int | None = ...,
        multicast_ttl: int | None = ...,
        evpn_ttl: int | None = ...,
        load_balance_all: Literal["enable", "disable"] | None = ...,
        sync_config: Literal["enable", "disable"] | None = ...,
        encryption: Literal["enable", "disable"] | None = ...,
        authentication: Literal["enable", "disable"] | None = ...,
        hb_interval: int | None = ...,
        hb_interval_in_milliseconds: Literal["100ms", "10ms"] | None = ...,
        hb_lost_threshold: int | None = ...,
        hello_holddown: int | None = ...,
        gratuitous_arps: Literal["enable", "disable"] | None = ...,
        arps: int | None = ...,
        arps_interval: int | None = ...,
        session_pickup: Literal["enable", "disable"] | None = ...,
        session_pickup_connectionless: Literal["enable", "disable"] | None = ...,
        session_pickup_expectation: Literal["enable", "disable"] | None = ...,
        session_pickup_nat: Literal["enable", "disable"] | None = ...,
        session_pickup_delay: Literal["enable", "disable"] | None = ...,
        link_failed_signal: Literal["enable", "disable"] | None = ...,
        upgrade_mode: Literal["simultaneous", "uninterruptible", "local-only", "secondary-only"] | None = ...,
        uninterruptible_primary_wait: int | None = ...,
        standalone_mgmt_vdom: Literal["enable", "disable"] | None = ...,
        ha_mgmt_status: Literal["enable", "disable"] | None = ...,
        ha_mgmt_interfaces: str | list[str] | list[dict[str, Any]] | None = ...,
        ha_eth_type: str | None = ...,
        hc_eth_type: str | None = ...,
        l2ep_eth_type: str | None = ...,
        ha_uptime_diff_margin: int | None = ...,
        standalone_config_sync: Literal["enable", "disable"] | None = ...,
        unicast_status: Literal["enable", "disable"] | None = ...,
        unicast_gateway: str | None = ...,
        unicast_peers: str | list[str] | list[dict[str, Any]] | None = ...,
        schedule: Literal["none", "leastconnection", "round-robin", "weight-round-robin", "random", "ip", "ipport"] | None = ...,
        weight: str | None = ...,
        cpu_threshold: str | None = ...,
        memory_threshold: str | None = ...,
        http_proxy_threshold: str | None = ...,
        ftp_proxy_threshold: str | None = ...,
        imap_proxy_threshold: str | None = ...,
        nntp_proxy_threshold: str | None = ...,
        pop3_proxy_threshold: str | None = ...,
        smtp_proxy_threshold: str | None = ...,
        override: Literal["enable", "disable"] | None = ...,
        priority: int | None = ...,
        override_wait_time: int | None = ...,
        monitor: str | list[str] | None = ...,
        pingserver_monitor_interface: str | list[str] | None = ...,
        pingserver_failover_threshold: int | None = ...,
        pingserver_secondary_force_reset: Literal["enable", "disable"] | None = ...,
        pingserver_flip_timeout: int | None = ...,
        vcluster_status: Literal["enable", "disable"] | None = ...,
        vcluster: str | list[str] | list[dict[str, Any]] | None = ...,
        ha_direct: Literal["enable", "disable"] | None = ...,
        ssd_failover: Literal["enable", "disable"] | None = ...,
        memory_compatible_mode: Literal["enable", "disable"] | None = ...,
        memory_based_failover: Literal["enable", "disable"] | None = ...,
        memory_failover_threshold: int | None = ...,
        memory_failover_monitor_period: int | None = ...,
        memory_failover_sample_rate: int | None = ...,
        memory_failover_flip_timeout: int | None = ...,
        failover_hold_time: int | None = ...,
        check_secondary_dev_health: Literal["enable", "disable"] | None = ...,
        ipsec_phase2_proposal: Literal["aes128-sha1", "aes128-sha256", "aes128-sha384", "aes128-sha512", "aes192-sha1", "aes192-sha256", "aes192-sha384", "aes192-sha512", "aes256-sha1", "aes256-sha256", "aes256-sha384", "aes256-sha512", "aes128gcm", "aes256gcm", "chacha20poly1305"] | list[str] | None = ...,
        bounce_intf_upon_failover: Literal["enable", "disable"] | None = ...,
        status: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: HaPayload | None = ...,
        group_id: int | None = ...,
        group_name: str | None = ...,
        mode: Literal["standalone", "a-a", "a-p"] | None = ...,
        sync_packet_balance: Literal["enable", "disable"] | None = ...,
        password: str | None = ...,
        key: str | None = ...,
        hbdev: str | list[str] | None = ...,
        auto_virtual_mac_interface: str | list[str] | list[dict[str, Any]] | None = ...,
        backup_hbdev: str | list[str] | list[dict[str, Any]] | None = ...,
        unicast_hb: Literal["enable", "disable"] | None = ...,
        unicast_hb_peerip: str | None = ...,
        unicast_hb_netmask: str | None = ...,
        session_sync_dev: str | list[str] | None = ...,
        route_ttl: int | None = ...,
        route_wait: int | None = ...,
        route_hold: int | None = ...,
        multicast_ttl: int | None = ...,
        evpn_ttl: int | None = ...,
        load_balance_all: Literal["enable", "disable"] | None = ...,
        sync_config: Literal["enable", "disable"] | None = ...,
        encryption: Literal["enable", "disable"] | None = ...,
        authentication: Literal["enable", "disable"] | None = ...,
        hb_interval: int | None = ...,
        hb_interval_in_milliseconds: Literal["100ms", "10ms"] | None = ...,
        hb_lost_threshold: int | None = ...,
        hello_holddown: int | None = ...,
        gratuitous_arps: Literal["enable", "disable"] | None = ...,
        arps: int | None = ...,
        arps_interval: int | None = ...,
        session_pickup: Literal["enable", "disable"] | None = ...,
        session_pickup_connectionless: Literal["enable", "disable"] | None = ...,
        session_pickup_expectation: Literal["enable", "disable"] | None = ...,
        session_pickup_nat: Literal["enable", "disable"] | None = ...,
        session_pickup_delay: Literal["enable", "disable"] | None = ...,
        link_failed_signal: Literal["enable", "disable"] | None = ...,
        upgrade_mode: Literal["simultaneous", "uninterruptible", "local-only", "secondary-only"] | None = ...,
        uninterruptible_primary_wait: int | None = ...,
        standalone_mgmt_vdom: Literal["enable", "disable"] | None = ...,
        ha_mgmt_status: Literal["enable", "disable"] | None = ...,
        ha_mgmt_interfaces: str | list[str] | list[dict[str, Any]] | None = ...,
        ha_eth_type: str | None = ...,
        hc_eth_type: str | None = ...,
        l2ep_eth_type: str | None = ...,
        ha_uptime_diff_margin: int | None = ...,
        standalone_config_sync: Literal["enable", "disable"] | None = ...,
        unicast_status: Literal["enable", "disable"] | None = ...,
        unicast_gateway: str | None = ...,
        unicast_peers: str | list[str] | list[dict[str, Any]] | None = ...,
        schedule: Literal["none", "leastconnection", "round-robin", "weight-round-robin", "random", "ip", "ipport"] | None = ...,
        weight: str | None = ...,
        cpu_threshold: str | None = ...,
        memory_threshold: str | None = ...,
        http_proxy_threshold: str | None = ...,
        ftp_proxy_threshold: str | None = ...,
        imap_proxy_threshold: str | None = ...,
        nntp_proxy_threshold: str | None = ...,
        pop3_proxy_threshold: str | None = ...,
        smtp_proxy_threshold: str | None = ...,
        override: Literal["enable", "disable"] | None = ...,
        priority: int | None = ...,
        override_wait_time: int | None = ...,
        monitor: str | list[str] | None = ...,
        pingserver_monitor_interface: str | list[str] | None = ...,
        pingserver_failover_threshold: int | None = ...,
        pingserver_secondary_force_reset: Literal["enable", "disable"] | None = ...,
        pingserver_flip_timeout: int | None = ...,
        vcluster_status: Literal["enable", "disable"] | None = ...,
        vcluster: str | list[str] | list[dict[str, Any]] | None = ...,
        ha_direct: Literal["enable", "disable"] | None = ...,
        ssd_failover: Literal["enable", "disable"] | None = ...,
        memory_compatible_mode: Literal["enable", "disable"] | None = ...,
        memory_based_failover: Literal["enable", "disable"] | None = ...,
        memory_failover_threshold: int | None = ...,
        memory_failover_monitor_period: int | None = ...,
        memory_failover_sample_rate: int | None = ...,
        memory_failover_flip_timeout: int | None = ...,
        failover_hold_time: int | None = ...,
        check_secondary_dev_health: Literal["enable", "disable"] | None = ...,
        ipsec_phase2_proposal: Literal["aes128-sha1", "aes128-sha256", "aes128-sha384", "aes128-sha512", "aes192-sha1", "aes192-sha256", "aes192-sha384", "aes192-sha512", "aes256-sha1", "aes256-sha256", "aes256-sha384", "aes256-sha512", "aes128gcm", "aes256gcm", "chacha20poly1305"] | list[str] | None = ...,
        bounce_intf_upon_failover: Literal["enable", "disable"] | None = ...,
        status: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
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
    "Ha",
    "HaPayload",
    "HaResponse",
    "HaObject",
]