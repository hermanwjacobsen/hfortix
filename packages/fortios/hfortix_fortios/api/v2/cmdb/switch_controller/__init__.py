"""FortiOS CMDB - Switch-controller category"""

from .acl_group import AclGroup
from .acl_ingress import AclIngress
from .auto_config_custom import AutoConfigCustom
from .auto_config_default import AutoConfigDefault
from .auto_config_policy import AutoConfigPolicy
from .custom_command import CustomCommand
from .dynamic_port_policy import DynamicPortPolicy
from .flow_tracking import FlowTracking
from .fortilink_settings import FortilinkSettings
from .global_ import Global
from .igmp_snooping import IgmpSnooping
from .initial_config_template import InitialConfigTemplate
from .initial_config_vlans import InitialConfigVlans
from .ip_source_guard_log import IpSourceGuardLog
from .lldp_profile import LldpProfile
from .lldp_settings import LldpSettings
from .location import Location
from .mac_policy import MacPolicy
from .managed_switch import ManagedSwitch
from .network_monitor_settings import NetworkMonitorSettings
from .ptp_interface_policy import PtpInterfacePolicy
from .ptp_profile import PtpProfile
from .qos_dot1p_map import QosDot1pMap
from .qos_ip_dscp_map import QosIpDscpMap
from .qos_qos_policy import QosQosPolicy
from .qos_queue_policy import QosQueuePolicy
from .remote_log import RemoteLog
from .security_policy__802_1X import SecurityPolicyEight02OneX
from .security_policy_local_access import SecurityPolicyLocalAccess
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

__all__ = [
    "AclGroup",
    "AclIngress",
    "AutoConfigCustom",
    "AutoConfigDefault",
    "AutoConfigPolicy",
    "CustomCommand",
    "DynamicPortPolicy",
    "FlowTracking",
    "FortilinkSettings",
    "Global",
    "IgmpSnooping",
    "InitialConfigTemplate",
    "InitialConfigVlans",
    "IpSourceGuardLog",
    "LldpProfile",
    "LldpSettings",
    "Location",
    "MacPolicy",
    "ManagedSwitch",
    "NetworkMonitorSettings",
    "PtpInterfacePolicy",
    "PtpProfile",
    "QosDot1pMap",
    "QosIpDscpMap",
    "QosQosPolicy",
    "QosQueuePolicy",
    "RemoteLog",
    "SecurityPolicyEight02OneX",
    "SecurityPolicyLocalAccess",
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
]


class SwitchController:
    """
    SwitchController category wrapper.

    This class provides access to all switch-controller CMDB endpoints.
    """

    def __init__(self, client):
        """
        Initialize SwitchController with all endpoint classes.

        Args:
            client: HTTPClient instance
        """
        self.acl_group = AclGroup(client)
        self.acl_ingress = AclIngress(client)
        self.auto_config_custom = AutoConfigCustom(client)
        self.auto_config_default = AutoConfigDefault(client)
        self.auto_config_policy = AutoConfigPolicy(client)
        self.custom_command = CustomCommand(client)
        self.dynamic_port_policy = DynamicPortPolicy(client)
        self.flow_tracking = FlowTracking(client)
        self.fortilink_settings = FortilinkSettings(client)
        self.global_ = Global(client)
        self.igmp_snooping = IgmpSnooping(client)
        self.initial_config_template = InitialConfigTemplate(client)
        self.initial_config_vlans = InitialConfigVlans(client)
        self.ip_source_guard_log = IpSourceGuardLog(client)
        self.lldp_profile = LldpProfile(client)
        self.lldp_settings = LldpSettings(client)
        self.location = Location(client)
        self.mac_policy = MacPolicy(client)
        self.managed_switch = ManagedSwitch(client)
        self.network_monitor_settings = NetworkMonitorSettings(client)
        self.ptp_interface_policy = PtpInterfacePolicy(client)
        self.ptp_profile = PtpProfile(client)
        self.qos_dot1p_map = QosDot1pMap(client)
        self.qos_ip_dscp_map = QosIpDscpMap(client)
        self.qos_qos_policy = QosQosPolicy(client)
        self.qos_queue_policy = QosQueuePolicy(client)
        self.remote_log = RemoteLog(client)
        self.security_policy__802_1x = SecurityPolicyEight02OneX(client)
        self.security_policy_local_access = SecurityPolicyLocalAccess(client)
        self.sflow = Sflow(client)
        self.snmp_community = SnmpCommunity(client)
        self.snmp_sysinfo = SnmpSysinfo(client)
        self.snmp_trap_threshold = SnmpTrapThreshold(client)
        self.snmp_user = SnmpUser(client)
        self.storm_control = StormControl(client)
        self.storm_control_policy = StormControlPolicy(client)
        self.stp_instance = StpInstance(client)
        self.stp_settings = StpSettings(client)
        self.switch_group = SwitchGroup(client)
        self.switch_interface_tag = SwitchInterfaceTag(client)
        self.switch_log = SwitchLog(client)
        self.switch_profile = SwitchProfile(client)
        self.system = System(client)
        self.traffic_policy = TrafficPolicy(client)
        self.traffic_sniffer = TrafficSniffer(client)
        self.virtual_port_pool = VirtualPortPool(client)
        self.vlan_policy = VlanPolicy(client)
