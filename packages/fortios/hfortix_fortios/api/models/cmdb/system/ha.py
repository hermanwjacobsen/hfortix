"""
Pydantic Models for CMDB - system/ha

Runtime validation models for system/ha configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field, field_validator
from typing import Any, Literal, Optional
from enum import Enum

# ============================================================================
# Child Table Models
# ============================================================================

class HaAutoVirtualMacInterface(BaseModel):
    """
    Child table model for auto-virtual-mac-interface.
    
    The physical interface that will be assigned an auto-generated virtual MAC address.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    interface_name: str = Field(max_length=15, default="", description="Interface name.")  # datasource: ['system.interface.name']
class HaBackupHbdev(BaseModel):
    """
    Child table model for backup-hbdev.
    
    Backup heartbeat interfaces. Must be the same for all members.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str | None = Field(max_length=79, default="", description="Interface name.")  # datasource: ['system.interface.name']
class HaHaMgmtInterfaces(BaseModel):
    """
    Child table model for ha-mgmt-interfaces.
    
    Reserve interfaces to manage individual cluster units.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    id: int | None = Field(ge=0, le=4294967295, default=0, description="Table ID.")    
    interface: str = Field(max_length=15, default="", description="Interface to reserve for HA management.")  # datasource: ['system.interface.name']    
    dst: str | None = Field(default="0.0.0.0 0.0.0.0", description="Default route destination for reserved HA management interface.")    
    gateway: str | None = Field(default="0.0.0.0", description="Default route gateway for reserved HA management interface.")    
    dst6: str | None = Field(default="::/0", description="Default IPv6 destination for reserved HA management interface.")    
    gateway6: str | None = Field(default="::", description="Default IPv6 gateway for reserved HA management interface.")
class HaUnicastPeers(BaseModel):
    """
    Child table model for unicast-peers.
    
    Number of unicast peers.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    id: int | None = Field(ge=0, le=4294967295, default=0, description="Table ID.")    
    peer_ip: str | None = Field(default="0.0.0.0", description="Unicast peer IP.")
class HaVcluster(BaseModel):
    """
    Child table model for vcluster.
    
    Virtual cluster table.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    vcluster_id: int | None = Field(ge=1, le=30, default=1, description="ID.")    
    override: Literal["enable", "disable"] | None = Field(default="disable", description="Enable and increase the priority of the unit that should always be primary (master).")    
    priority: int | None = Field(ge=0, le=255, default=128, description="Increase the priority to select the primary unit (0 - 255).")    
    override_wait_time: int | None = Field(ge=0, le=3600, default=0, description="Delay negotiating if override is enabled (0 - 3600 sec). Reduces how often the cluster negotiates.")    
    monitor: list[Monitor] = Field(default="", description="Interfaces to check for port monitoring (or link failure).")  # datasource: ['system.interface.name']    
    pingserver_monitor_interface: list[PingserverMonitorInterface] = Field(default="", description="Interfaces to check for remote IP monitoring.")  # datasource: ['system.interface.name']    
    pingserver_failover_threshold: int | None = Field(ge=0, le=50, default=0, description="Remote IP monitoring failover threshold (0 - 50).")    
    pingserver_secondary_force_reset: Literal["enable", "disable"] | None = Field(default="enable", description="Enable to force the cluster to negotiate after a remote IP monitoring failover.")    
    pingserver_flip_timeout: int | None = Field(ge=6, le=2147483647, default=60, description="Time to wait in minutes before renegotiating after a remote IP monitoring failover.")    
    vdom: list[Vdom] = Field(default=None, description="Virtual domain(s) in the virtual cluster.")
class HaStatus(BaseModel):
    """
    Child table model for status.
    
    list ha status information
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    vcluster_id: Any = Field(default=None, description="<enter> to show all vcluster or input vcluster-id")
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================

class HaUpgrade_modeEnum(str, Enum):
    """Allowed values for upgrade_mode field."""
    SIMULTANEOUS = "simultaneous"    UNINTERRUPTIBLE = "uninterruptible"    LOCAL_ONLY = "local-only"    SECONDARY_ONLY = "secondary-only"
class HaScheduleEnum(str, Enum):
    """Allowed values for schedule field."""
    NONE = "none"    LEASTCONNECTION = "leastconnection"    ROUND_ROBIN = "round-robin"    WEIGHT_ROUND_ROBIN = "weight-round-robin"    RANDOM = "random"    IP = "ip"    IPPORT = "ipport"
class HaIpsec_phase2_proposalEnum(str, Enum):
    """Allowed values for ipsec_phase2_proposal field."""
    AES128_SHA1 = "aes128-sha1"    AES128_SHA256 = "aes128-sha256"    AES128_SHA384 = "aes128-sha384"    AES128_SHA512 = "aes128-sha512"    AES192_SHA1 = "aes192-sha1"    AES192_SHA256 = "aes192-sha256"    AES192_SHA384 = "aes192-sha384"    AES192_SHA512 = "aes192-sha512"    AES256_SHA1 = "aes256-sha1"    AES256_SHA256 = "aes256-sha256"    AES256_SHA384 = "aes256-sha384"    AES256_SHA512 = "aes256-sha512"    AES128GCM = "aes128gcm"    AES256GCM = "aes256gcm"    CHACHA20POLY1305 = "chacha20poly1305"

# ============================================================================
# Main Model
# ============================================================================

class HaModel(BaseModel):
    """
    Pydantic model for system/ha configuration.
    
    Configure HA.
    
    Validation Rules:        - group_id: min=0 max=1023 pattern=        - group_name: max_length=32 pattern=        - mode: pattern=        - sync_packet_balance: pattern=        - password: max_length=128 pattern=        - key: max_length=16 pattern=        - hbdev: pattern=        - auto_virtual_mac_interface: pattern=        - backup_hbdev: pattern=        - unicast_hb: pattern=        - unicast_hb_peerip: pattern=        - unicast_hb_netmask: pattern=        - session_sync_dev: pattern=        - route_ttl: min=5 max=3600 pattern=        - route_wait: min=0 max=3600 pattern=        - route_hold: min=0 max=3600 pattern=        - multicast_ttl: min=5 max=3600 pattern=        - evpn_ttl: min=5 max=3600 pattern=        - load_balance_all: pattern=        - sync_config: pattern=        - encryption: pattern=        - authentication: pattern=        - hb_interval: min=1 max=20 pattern=        - hb_interval_in_milliseconds: pattern=        - hb_lost_threshold: min=1 max=60 pattern=        - hello_holddown: min=5 max=300 pattern=        - gratuitous_arps: pattern=        - arps: min=1 max=60 pattern=        - arps_interval: min=1 max=20 pattern=        - session_pickup: pattern=        - session_pickup_connectionless: pattern=        - session_pickup_expectation: pattern=        - session_pickup_nat: pattern=        - session_pickup_delay: pattern=        - link_failed_signal: pattern=        - upgrade_mode: pattern=        - uninterruptible_primary_wait: min=15 max=300 pattern=        - standalone_mgmt_vdom: pattern=        - ha_mgmt_status: pattern=        - ha_mgmt_interfaces: pattern=        - ha_eth_type: max_length=4 pattern=        - hc_eth_type: max_length=4 pattern=        - l2ep_eth_type: max_length=4 pattern=        - ha_uptime_diff_margin: min=1 max=65535 pattern=        - standalone_config_sync: pattern=        - unicast_status: pattern=        - unicast_gateway: pattern=        - unicast_peers: pattern=        - schedule: pattern=        - weight: pattern=        - cpu_threshold: pattern=        - memory_threshold: pattern=        - http_proxy_threshold: pattern=        - ftp_proxy_threshold: pattern=        - imap_proxy_threshold: pattern=        - nntp_proxy_threshold: pattern=        - pop3_proxy_threshold: pattern=        - smtp_proxy_threshold: pattern=        - override: pattern=        - priority: min=0 max=255 pattern=        - override_wait_time: min=0 max=3600 pattern=        - monitor: pattern=        - pingserver_monitor_interface: pattern=        - pingserver_failover_threshold: min=0 max=50 pattern=        - pingserver_secondary_force_reset: pattern=        - pingserver_flip_timeout: min=6 max=2147483647 pattern=        - vcluster_status: pattern=        - vcluster: pattern=        - ha_direct: pattern=        - ssd_failover: pattern=        - memory_compatible_mode: pattern=        - memory_based_failover: pattern=        - memory_failover_threshold: min=0 max=95 pattern=        - memory_failover_monitor_period: min=1 max=300 pattern=        - memory_failover_sample_rate: min=1 max=60 pattern=        - memory_failover_flip_timeout: min=6 max=2147483647 pattern=        - failover_hold_time: min=0 max=300 pattern=        - check_secondary_dev_health: pattern=        - ipsec_phase2_proposal: pattern=        - bounce_intf_upon_failover: pattern=        - status: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    group_id: int | None = Field(ge=0, le=1023, default=0, description="HA group ID  (0 - 1023;  or 0 - 7 when there are more than 2 vclusters). Must be the same for all members.")    
    group_name: str | None = Field(max_length=32, default="", description="Cluster group name. Must be the same for all members.")    
    mode: Literal["standalone", "a-a", "a-p"] | None = Field(default="standalone", description="HA mode. Must be the same for all members. FGSP requires standalone.")    
    sync_packet_balance: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable HA packet distribution to multiple CPUs.")    
    password: Any = Field(max_length=128, default=None, description="Cluster password. Must be the same for all members.")    
    key: Any = Field(max_length=16, default=None, description="Key.")    
    hbdev: list[Hbdev] = Field(default="", description="Heartbeat interfaces. Must be the same for all members.")    
    auto_virtual_mac_interface: list[AutoVirtualMacInterface] = Field(default=None, description="The physical interface that will be assigned an auto-generated virtual MAC address.")    
    backup_hbdev: list[BackupHbdev] = Field(default=None, description="Backup heartbeat interfaces. Must be the same for all members.")    
    unicast_hb: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable unicast heartbeat.")    
    unicast_hb_peerip: str | None = Field(default="0.0.0.0", description="Unicast heartbeat peer IP.")    
    unicast_hb_netmask: str | None = Field(default="0.0.0.0", description="Unicast heartbeat netmask.")    
    session_sync_dev: list[SessionSyncDev] = Field(default="", description="Offload session-sync process to kernel and sync sessions using connected interface(s) directly.")  # datasource: ['system.interface.name']    
    route_ttl: int | None = Field(ge=5, le=3600, default=10, description="TTL for primary unit routes (5 - 3600 sec). Increase to maintain active routes during failover.")    
    route_wait: int | None = Field(ge=0, le=3600, default=0, description="Time to wait before sending new routes to the cluster (0 - 3600 sec).")    
    route_hold: int | None = Field(ge=0, le=3600, default=10, description="Time to wait between routing table updates to the cluster (0 - 3600 sec).")    
    multicast_ttl: int | None = Field(ge=5, le=3600, default=600, description="HA multicast TTL on primary (5 - 3600 sec).")    
    evpn_ttl: int | None = Field(ge=5, le=3600, default=60, description="HA EVPN FDB TTL on primary box (5 - 3600 sec).")    
    load_balance_all: Literal["enable", "disable"] | None = Field(default="disable", description="Enable to load balance TCP sessions. Disable to load balance proxy sessions only.")    
    sync_config: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable configuration synchronization.")    
    encryption: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable heartbeat message encryption.")    
    authentication: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable heartbeat message authentication.")    
    hb_interval: int | None = Field(ge=1, le=20, default=2, description="Time between sending heartbeat packets (1 - 20). Increase to reduce false positives.")    
    hb_interval_in_milliseconds: Literal["100ms", "10ms"] | None = Field(default="100ms", description="Units of heartbeat interval time between sending heartbeat packets. Default is 100ms.")    
    hb_lost_threshold: int | None = Field(ge=1, le=60, default=20, description="Number of lost heartbeats to signal a failure (1 - 60). Increase to reduce false positives.")    
    hello_holddown: int | None = Field(ge=5, le=300, default=20, description="Time to wait before changing from hello to work state (5 - 300 sec).")    
    gratuitous_arps: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable gratuitous ARPs. Disable if link-failed-signal enabled.")    
    arps: int | None = Field(ge=1, le=60, default=5, description="Number of gratuitous ARPs (1 - 60). Lower to reduce traffic. Higher to reduce failover time.")    
    arps_interval: int | None = Field(ge=1, le=20, default=8, description="Time between gratuitous ARPs  (1 - 20 sec). Lower to reduce failover time. Higher to reduce traffic.")    
    session_pickup: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable session pickup. Enabling it can reduce session down time when fail over happens.")    
    session_pickup_connectionless: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable UDP and ICMP session sync.")    
    session_pickup_expectation: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable session helper expectation session sync for FGSP.")    
    session_pickup_nat: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable NAT session sync for FGSP.")    
    session_pickup_delay: Literal["enable", "disable"] | None = Field(default="disable", description="Enable to sync sessions longer than 30 sec. Only longer lived sessions need to be synced.")    
    link_failed_signal: Literal["enable", "disable"] | None = Field(default="disable", description="Enable to shut down all interfaces for 1 sec after a failover. Use if gratuitous ARPs do not update network.")    
    upgrade_mode: UpgradeModeEnum | None = Field(default="uninterruptible", description="The mode to upgrade a cluster.")    
    uninterruptible_primary_wait: int | None = Field(ge=15, le=300, default=30, description="Number of minutes the primary HA unit waits before the secondary HA unit is considered upgraded and the system is started before starting its own upgrade (15 - 300, default = 30).")    
    standalone_mgmt_vdom: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable standalone management VDOM.")    
    ha_mgmt_status: Literal["enable", "disable"] | None = Field(default="disable", description="Enable to reserve interfaces to manage individual cluster units.")    
    ha_mgmt_interfaces: list[HaMgmtInterfaces] = Field(default=None, description="Reserve interfaces to manage individual cluster units.")    
    ha_eth_type: str | None = Field(max_length=4, default="8890", description="HA heartbeat packet Ethertype (4-digit hex).")    
    hc_eth_type: str | None = Field(max_length=4, default="8891", description="Transparent mode HA heartbeat packet Ethertype (4-digit hex).")    
    l2ep_eth_type: str | None = Field(max_length=4, default="8893", description="Telnet session HA heartbeat packet Ethertype (4-digit hex).")    
    ha_uptime_diff_margin: int | None = Field(ge=1, le=65535, default=300, description="Normally you would only reduce this value for failover testing.")    
    standalone_config_sync: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable FGSP configuration synchronization.")    
    unicast_status: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable unicast connection.")    
    unicast_gateway: str | None = Field(default="0.0.0.0", description="Default route gateway for unicast interface.")    
    unicast_peers: list[UnicastPeers] = Field(default=None, description="Number of unicast peers.")    
    schedule: ScheduleEnum | None = Field(default="round-robin", description="Type of A-A load balancing. Use none if you have external load balancers.")    
    weight: str | None = Field(default="0 40", description="Weight-round-robin weight for each cluster unit. Syntax <priority> <weight>.")    
    cpu_threshold: str | None = Field(default="", description="Dynamic weighted load balancing CPU usage weight and high and low thresholds.")    
    memory_threshold: str | None = Field(default="", description="Dynamic weighted load balancing memory usage weight and high and low thresholds.")    
    http_proxy_threshold: str | None = Field(default="", description="Dynamic weighted load balancing weight and high and low number of HTTP proxy sessions.")    
    ftp_proxy_threshold: str | None = Field(default="", description="Dynamic weighted load balancing weight and high and low number of FTP proxy sessions.")    
    imap_proxy_threshold: str | None = Field(default="", description="Dynamic weighted load balancing weight and high and low number of IMAP proxy sessions.")    
    nntp_proxy_threshold: str | None = Field(default="", description="Dynamic weighted load balancing weight and high and low number of NNTP proxy sessions.")    
    pop3_proxy_threshold: str | None = Field(default="", description="Dynamic weighted load balancing weight and high and low number of POP3 proxy sessions.")    
    smtp_proxy_threshold: str | None = Field(default="", description="Dynamic weighted load balancing weight and high and low number of SMTP proxy sessions.")    
    override: Literal["enable", "disable"] | None = Field(default="disable", description="Enable and increase the priority of the unit that should always be primary (master).")    
    priority: int | None = Field(ge=0, le=255, default=128, description="Increase the priority to select the primary unit (0 - 255).")    
    override_wait_time: int | None = Field(ge=0, le=3600, default=0, description="Delay negotiating if override is enabled (0 - 3600 sec). Reduces how often the cluster negotiates.")    
    monitor: list[Monitor] = Field(default="", description="Interfaces to check for port monitoring (or link failure).")  # datasource: ['system.interface.name']    
    pingserver_monitor_interface: list[PingserverMonitorInterface] = Field(default="", description="Interfaces to check for remote IP monitoring.")  # datasource: ['system.interface.name']    
    pingserver_failover_threshold: int | None = Field(ge=0, le=50, default=0, description="Remote IP monitoring failover threshold (0 - 50).")    
    pingserver_secondary_force_reset: Literal["enable", "disable"] | None = Field(default="enable", description="Enable to force the cluster to negotiate after a remote IP monitoring failover.")    
    pingserver_flip_timeout: int | None = Field(ge=6, le=2147483647, default=60, description="Time to wait in minutes before renegotiating after a remote IP monitoring failover.")    
    vcluster_status: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable virtual cluster for virtual clustering.")    
    vcluster: list[Vcluster] = Field(default=None, description="Virtual cluster table.")    
    ha_direct: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable using ha-mgmt interface for syslog, remote authentication (RADIUS), FortiAnalyzer, FortiSandbox, sFlow, and Netflow.")    
    ssd_failover: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable automatic HA failover on SSD disk failure.")    
    memory_compatible_mode: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable memory compatible mode.")    
    memory_based_failover: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable memory based failover.")    
    memory_failover_threshold: int | None = Field(ge=0, le=95, default=0, description="Memory usage threshold to trigger memory based failover (0 means using conserve mode threshold in system.global).")    
    memory_failover_monitor_period: int | None = Field(ge=1, le=300, default=60, description="Duration of high memory usage before memory based failover is triggered in seconds (1 - 300, default = 60).")    
    memory_failover_sample_rate: int | None = Field(ge=1, le=60, default=1, description="Rate at which memory usage is sampled in order to measure memory usage in seconds (1 - 60, default = 1).")    
    memory_failover_flip_timeout: int | None = Field(ge=6, le=2147483647, default=6, description="Time to wait between subsequent memory based failovers in minutes (6 - 2147483647, default = 6).")    
    failover_hold_time: int | None = Field(ge=0, le=300, default=0, description="Time to wait before failover (0 - 300 sec, default = 0), to avoid flip.")    
    check_secondary_dev_health: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable secondary dev health check for session load-balance in HA A-A mode.")    
    ipsec_phase2_proposal: list[IpsecPhase2Proposal] = Field(default="", description="IPsec phase2 proposal.")    
    bounce_intf_upon_failover: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable notification of kernel to bring down and up all monitored interfaces. The setting is used during failovers if gratuitous ARPs do not update the network.")    
    status: list[Status] = Field(default=None, description="list ha status information")    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
    @field_validator('session_sync_dev')
    @classmethod
    def validate_session_sync_dev(cls, v: Any) -> Any:
        """
        Validate session_sync_dev field.
        
        Datasource: ['system.interface.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('monitor')
    @classmethod
    def validate_monitor(cls, v: Any) -> Any:
        """
        Validate monitor field.
        
        Datasource: ['system.interface.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('pingserver_monitor_interface')
    @classmethod
    def validate_pingserver_monitor_interface(cls, v: Any) -> Any:
        """
        Validate pingserver_monitor_interface field.
        
        Datasource: ['system.interface.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    # ========================================================================
    # Helper Methods
    # ========================================================================
    
    def to_fortios_dict(self) -> dict[str, Any]:
        """
        Convert model to FortiOS API payload format.
        
        Returns:
            Dict suitable for POST/PUT operations
        """
        # Export with exclude_none to avoid sending null values
        return self.model_dump(exclude_none=True, by_alias=True)
    
    @classmethod
    def from_fortios_response(cls, data: dict[str, Any]) -> "":
        """
        Create model instance from FortiOS API response.
        
        Args:
            data: Response data from API
            
        Returns:
            Validated model instance
        """
        return cls(**data)
    # ========================================================================
    # Datasource Validation Methods
    # ========================================================================    
    async def validate_auto_virtual_mac_interface_references(self, client: Any) -> list[str]:
        """
        Validate auto_virtual_mac_interface references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - system/interface        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = HaModel(
            ...     auto_virtual_mac_interface=[{"interface-name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_auto_virtual_mac_interface_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.system.ha.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "auto_virtual_mac_interface", [])
        if not values:
            return errors
        
        for item in values:
            if isinstance(item, dict):
                value = item.get("interface-name")
            else:
                value = getattr(item, "interface-name", None)
            
            if not value:
                continue
            
            # Check all datasource endpoints
            found = False
            if await client.api.cmdb.system.interface.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"Auto-Virtual-Mac-Interface '{value}' not found in "
                    "system/interface"
                )        
        return errors    
    async def validate_backup_hbdev_references(self, client: Any) -> list[str]:
        """
        Validate backup_hbdev references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - system/interface        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = HaModel(
            ...     backup_hbdev=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_backup_hbdev_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.system.ha.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "backup_hbdev", [])
        if not values:
            return errors
        
        for item in values:
            if isinstance(item, dict):
                value = item.get("name")
            else:
                value = getattr(item, "name", None)
            
            if not value:
                continue
            
            # Check all datasource endpoints
            found = False
            if await client.api.cmdb.system.interface.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"Backup-Hbdev '{value}' not found in "
                    "system/interface"
                )        
        return errors    
    async def validate_session_sync_dev_references(self, client: Any) -> list[str]:
        """
        Validate session_sync_dev references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - system/interface        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = HaModel(
            ...     session_sync_dev="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_session_sync_dev_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.system.ha.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "session_sync_dev", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.system.interface.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Session-Sync-Dev '{value}' not found in "
                "system/interface"
            )        
        return errors    
    async def validate_ha_mgmt_interfaces_references(self, client: Any) -> list[str]:
        """
        Validate ha_mgmt_interfaces references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - system/interface        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = HaModel(
            ...     ha_mgmt_interfaces=[{"interface": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_ha_mgmt_interfaces_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.system.ha.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "ha_mgmt_interfaces", [])
        if not values:
            return errors
        
        for item in values:
            if isinstance(item, dict):
                value = item.get("interface")
            else:
                value = getattr(item, "interface", None)
            
            if not value:
                continue
            
            # Check all datasource endpoints
            found = False
            if await client.api.cmdb.system.interface.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"Ha-Mgmt-Interfaces '{value}' not found in "
                    "system/interface"
                )        
        return errors    
    async def validate_monitor_references(self, client: Any) -> list[str]:
        """
        Validate monitor references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - system/interface        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = HaModel(
            ...     monitor="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_monitor_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.system.ha.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "monitor", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.system.interface.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Monitor '{value}' not found in "
                "system/interface"
            )        
        return errors    
    async def validate_pingserver_monitor_interface_references(self, client: Any) -> list[str]:
        """
        Validate pingserver_monitor_interface references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - system/interface        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = HaModel(
            ...     pingserver_monitor_interface="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_pingserver_monitor_interface_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.system.ha.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "pingserver_monitor_interface", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.system.interface.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Pingserver-Monitor-Interface '{value}' not found in "
                "system/interface"
            )        
        return errors    
    async def validate_vcluster_references(self, client: Any) -> list[str]:
        """
        Validate vcluster references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - system/interface        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = HaModel(
            ...     vcluster=[{"pingserver-monitor-interface": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_vcluster_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.system.ha.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "vcluster", [])
        if not values:
            return errors
        
        for item in values:
            if isinstance(item, dict):
                value = item.get("pingserver-monitor-interface")
            else:
                value = getattr(item, "pingserver-monitor-interface", None)
            
            if not value:
                continue
            
            # Check all datasource endpoints
            found = False
            if await client.api.cmdb.system.interface.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"Vcluster '{value}' not found in "
                    "system/interface"
                )        
        return errors    
    async def validate_all_references(self, client: Any) -> list[str]:
        """
        Validate ALL datasource references in this model.
        
        Convenience method that runs all validate_*_references() methods
        and aggregates the results.
        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of all validation errors found
            
        Example:
            >>> errors = await policy.validate_all_references(fgt._client)
            >>> if errors:
            ...     for error in errors:
            ...         print(f"  - {error}")
        """
        all_errors = []
        
        errors = await self.validate_auto_virtual_mac_interface_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_backup_hbdev_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_session_sync_dev_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_ha_mgmt_interfaces_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_monitor_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_pingserver_monitor_interface_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_vcluster_references(client)
        all_errors.extend(errors)        
        return all_errors

# ============================================================================
# Type Aliases for Convenience
# ============================================================================

Dict = dict[str, Any]  # For backward compatibility

# ============================================================================
# Module Exports
# ============================================================================

__all__ = [
    "HaModel",    "HaAutoVirtualMacInterface",    "HaBackupHbdev",    "HaHaMgmtInterfaces",    "HaUnicastPeers",    "HaVcluster",    "HaStatus",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T22:00:17.572614Z
# ============================================================================