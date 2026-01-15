"""Type stubs for SWITCH_CONTROLLER category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .custom_command import CustomCommand
    from .dynamic_port_policy import DynamicPortPolicy
    from .flow_tracking import FlowTracking
    from .fortilink_settings import FortilinkSettings
    from .global_ import Global
    from .igmp_snooping import IgmpSnooping
    from .ip_source_guard_log import IpSourceGuardLog
    from .lldp_profile import LldpProfile
    from .lldp_settings import LldpSettings
    from .location import Location
    from .mac_policy import MacPolicy
    from .managed_switch import ManagedSwitch
    from .network_monitor_settings import NetworkMonitorSettings
    from .remote_log import RemoteLog
    from .sflow import Sflow
    from .snmp_community import SnmpCommunity
    from .snmp_sysinfo import SnmpSysinfo
    from .snmp_trap_threshold import SnmpTrapThreshold
    from .snmp_user import SnmpUser
    from .storm_control import StormControl
    from .storm_control_policy import StormControlPolicy
    from .stp_instance import StpInstance
    from .stp_settings import StpSettings
    from .switch_group import SwitchGroup
    from .switch_interface_tag import SwitchInterfaceTag
    from .switch_log import SwitchLog
    from .switch_profile import SwitchProfile
    from .system import System
    from .traffic_policy import TrafficPolicy
    from .traffic_sniffer import TrafficSniffer
    from .virtual_port_pool import VirtualPortPool
    from .vlan_policy import VlanPolicy
    from .x802_1x_settings import X8021xSettings
    from .acl import Acl
    from .auto_config import AutoConfig
    from .initial_config import InitialConfig
    from .ptp import Ptp
    from .qos import Qos
    from .security_policy import SecurityPolicy

__all__ = [
    "CustomCommand",
    "DynamicPortPolicy",
    "FlowTracking",
    "FortilinkSettings",
    "Global",
    "IgmpSnooping",
    "IpSourceGuardLog",
    "LldpProfile",
    "LldpSettings",
    "Location",
    "MacPolicy",
    "ManagedSwitch",
    "NetworkMonitorSettings",
    "RemoteLog",
    "Sflow",
    "SnmpCommunity",
    "SnmpSysinfo",
    "SnmpTrapThreshold",
    "SnmpUser",
    "StormControl",
    "StormControlPolicy",
    "StpInstance",
    "StpSettings",
    "SwitchGroup",
    "SwitchInterfaceTag",
    "SwitchLog",
    "SwitchProfile",
    "System",
    "TrafficPolicy",
    "TrafficSniffer",
    "VirtualPortPool",
    "VlanPolicy",
    "X8021xSettings",
    "SwitchController",
]


class SwitchController:
    """SWITCH_CONTROLLER API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    acl: Acl
    auto_config: AutoConfig
    initial_config: InitialConfig
    ptp: Ptp
    qos: Qos
    security_policy: SecurityPolicy
    custom_command: CustomCommand
    dynamic_port_policy: DynamicPortPolicy
    flow_tracking: FlowTracking
    fortilink_settings: FortilinkSettings
    global_: Global
    igmp_snooping: IgmpSnooping
    ip_source_guard_log: IpSourceGuardLog
    lldp_profile: LldpProfile
    lldp_settings: LldpSettings
    location: Location
    mac_policy: MacPolicy
    managed_switch: ManagedSwitch
    network_monitor_settings: NetworkMonitorSettings
    remote_log: RemoteLog
    sflow: Sflow
    snmp_community: SnmpCommunity
    snmp_sysinfo: SnmpSysinfo
    snmp_trap_threshold: SnmpTrapThreshold
    snmp_user: SnmpUser
    storm_control: StormControl
    storm_control_policy: StormControlPolicy
    stp_instance: StpInstance
    stp_settings: StpSettings
    switch_group: SwitchGroup
    switch_interface_tag: SwitchInterfaceTag
    switch_log: SwitchLog
    switch_profile: SwitchProfile
    system: System
    traffic_policy: TrafficPolicy
    traffic_sniffer: TrafficSniffer
    virtual_port_pool: VirtualPortPool
    vlan_policy: VlanPolicy
    x802_1x_settings: X8021xSettings

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize switch_controller category with HTTP client."""
        ...
