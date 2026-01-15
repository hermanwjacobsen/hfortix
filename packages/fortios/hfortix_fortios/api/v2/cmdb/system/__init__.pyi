"""Type stubs for SYSTEM category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .accprofile import Accprofile
    from .acme import Acme
    from .admin import Admin
    from .affinity_interrupt import AffinityInterrupt
    from .affinity_packet_redistribution import AffinityPacketRedistribution
    from .alarm import Alarm
    from .alias import Alias
    from .api_user import ApiUser
    from .arp_table import ArpTable
    from .auto_install import AutoInstall
    from .auto_script import AutoScript
    from .automation_action import AutomationAction
    from .automation_condition import AutomationCondition
    from .automation_destination import AutomationDestination
    from .automation_stitch import AutomationStitch
    from .automation_trigger import AutomationTrigger
    from .central_management import CentralManagement
    from .cloud_service import CloudService
    from .console import Console
    from .csf import Csf
    from .custom_language import CustomLanguage
    from .ddns import Ddns
    from .dedicated_mgmt import DedicatedMgmt
    from .device_upgrade import DeviceUpgrade
    from .device_upgrade_exemptions import DeviceUpgradeExemptions
    from .dns import Dns
    from .dns64 import Dns64
    from .dns_database import DnsDatabase
    from .dns_server import DnsServer
    from .dscp_based_priority import DscpBasedPriority
    from .email_server import EmailServer
    from .evpn import Evpn
    from .external_resource import ExternalResource
    from .fabric_vpn import FabricVpn
    from .federated_upgrade import FederatedUpgrade
    from .fips_cc import FipsCc
    from .fortiguard import Fortiguard
    from .fortisandbox import Fortisandbox
    from .fsso_polling import FssoPolling
    from .ftm_push import FtmPush
    from .geneve import Geneve
    from .geoip_country import GeoipCountry
    from .geoip_override import GeoipOverride
    from .global_ import Global
    from .gre_tunnel import GreTunnel
    from .ha import Ha
    from .ha_monitor import HaMonitor
    from .health_check_fortiguard import HealthCheckFortiguard
    from .ike import Ike
    from .interface import Interface
    from .ipam import Ipam
    from .ipip_tunnel import IpipTunnel
    from .ips import Ips
    from .ips_urlfilter_dns import IpsUrlfilterDns
    from .ips_urlfilter_dns6 import IpsUrlfilterDns6
    from .ipsec_aggregate import IpsecAggregate
    from .ipv6_neighbor_cache import Ipv6NeighborCache
    from .ipv6_tunnel import Ipv6Tunnel
    from .link_monitor import LinkMonitor
    from .lte_modem import LteModem
    from .mac_address_table import MacAddressTable
    from .mobile_tunnel import MobileTunnel
    from .modem import Modem
    from .nd_proxy import NdProxy
    from .netflow import Netflow
    from .network_visibility import NetworkVisibility
    from .ngfw_settings import NgfwSettings
    from .np6xlite import Np6xlite
    from .npu import Npu
    from .ntp import Ntp
    from .object_tagging import ObjectTagging
    from .password_policy import PasswordPolicy
    from .password_policy_guest_admin import PasswordPolicyGuestAdmin
    from .pcp_server import PcpServer
    from .physical_switch import PhysicalSwitch
    from .pppoe_interface import PppoeInterface
    from .probe_response import ProbeResponse
    from .proxy_arp import ProxyArp
    from .ptp import Ptp
    from .replacemsg_group import ReplacemsgGroup
    from .replacemsg_image import ReplacemsgImage
    from .resource_limits import ResourceLimits
    from .saml import Saml
    from .sdn_connector import SdnConnector
    from .sdn_proxy import SdnProxy
    from .sdn_vpn import SdnVpn
    from .sdwan import Sdwan
    from .session_helper import SessionHelper
    from .session_ttl import SessionTtl
    from .settings import Settings
    from .sflow import Sflow
    from .sit_tunnel import SitTunnel
    from .sms_server import SmsServer
    from .sov_sase import SovSase
    from .speed_test_schedule import SpeedTestSchedule
    from .speed_test_server import SpeedTestServer
    from .speed_test_setting import SpeedTestSetting
    from .ssh_config import SshConfig
    from .sso_admin import SsoAdmin
    from .sso_forticloud_admin import SsoForticloudAdmin
    from .sso_fortigate_cloud_admin import SsoFortigateCloudAdmin
    from .standalone_cluster import StandaloneCluster
    from .storage import Storage
    from .stp import Stp
    from .switch_interface import SwitchInterface
    from .timezone import Timezone
    from .tos_based_priority import TosBasedPriority
    from .vdom import Vdom
    from .vdom_dns import VdomDns
    from .vdom_exception import VdomException
    from .vdom_link import VdomLink
    from .vdom_netflow import VdomNetflow
    from .vdom_property import VdomProperty
    from .vdom_radius_server import VdomRadiusServer
    from .vdom_sflow import VdomSflow
    from .virtual_switch import VirtualSwitch
    from .virtual_wire_pair import VirtualWirePair
    from .vne_interface import VneInterface
    from .vxlan import Vxlan
    from .wccp import Wccp
    from .zone import Zone
    from .autoupdate import Autoupdate
    from .dhcp import Dhcp
    from .dhcp6 import Dhcp6
    from .lldp import Lldp
    from .modem3g import Modem3g
    from .replacemsg import Replacemsg
    from .security_rating import SecurityRating
    from .snmp import Snmp

__all__ = [
    "Accprofile",
    "Acme",
    "Admin",
    "AffinityInterrupt",
    "AffinityPacketRedistribution",
    "Alarm",
    "Alias",
    "ApiUser",
    "ArpTable",
    "AutoInstall",
    "AutoScript",
    "AutomationAction",
    "AutomationCondition",
    "AutomationDestination",
    "AutomationStitch",
    "AutomationTrigger",
    "CentralManagement",
    "CloudService",
    "Console",
    "Csf",
    "CustomLanguage",
    "Ddns",
    "DedicatedMgmt",
    "DeviceUpgrade",
    "DeviceUpgradeExemptions",
    "Dns",
    "Dns64",
    "DnsDatabase",
    "DnsServer",
    "DscpBasedPriority",
    "EmailServer",
    "Evpn",
    "ExternalResource",
    "FabricVpn",
    "FederatedUpgrade",
    "FipsCc",
    "Fortiguard",
    "Fortisandbox",
    "FssoPolling",
    "FtmPush",
    "Geneve",
    "GeoipCountry",
    "GeoipOverride",
    "Global",
    "GreTunnel",
    "Ha",
    "HaMonitor",
    "HealthCheckFortiguard",
    "Ike",
    "Interface",
    "Ipam",
    "IpipTunnel",
    "Ips",
    "IpsUrlfilterDns",
    "IpsUrlfilterDns6",
    "IpsecAggregate",
    "Ipv6NeighborCache",
    "Ipv6Tunnel",
    "LinkMonitor",
    "LteModem",
    "MacAddressTable",
    "MobileTunnel",
    "Modem",
    "NdProxy",
    "Netflow",
    "NetworkVisibility",
    "NgfwSettings",
    "Np6xlite",
    "Npu",
    "Ntp",
    "ObjectTagging",
    "PasswordPolicy",
    "PasswordPolicyGuestAdmin",
    "PcpServer",
    "PhysicalSwitch",
    "PppoeInterface",
    "ProbeResponse",
    "ProxyArp",
    "Ptp",
    "ReplacemsgGroup",
    "ReplacemsgImage",
    "ResourceLimits",
    "Saml",
    "SdnConnector",
    "SdnProxy",
    "SdnVpn",
    "Sdwan",
    "SessionHelper",
    "SessionTtl",
    "Settings",
    "Sflow",
    "SitTunnel",
    "SmsServer",
    "SovSase",
    "SpeedTestSchedule",
    "SpeedTestServer",
    "SpeedTestSetting",
    "SshConfig",
    "SsoAdmin",
    "SsoForticloudAdmin",
    "SsoFortigateCloudAdmin",
    "StandaloneCluster",
    "Storage",
    "Stp",
    "SwitchInterface",
    "Timezone",
    "TosBasedPriority",
    "Vdom",
    "VdomDns",
    "VdomException",
    "VdomLink",
    "VdomNetflow",
    "VdomProperty",
    "VdomRadiusServer",
    "VdomSflow",
    "VirtualSwitch",
    "VirtualWirePair",
    "VneInterface",
    "Vxlan",
    "Wccp",
    "Zone",
    "System",
]


class System:
    """SYSTEM API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    autoupdate: Autoupdate
    dhcp: Dhcp
    dhcp6: Dhcp6
    lldp: Lldp
    modem3g: Modem3g
    replacemsg: Replacemsg
    security_rating: SecurityRating
    snmp: Snmp
    accprofile: Accprofile
    acme: Acme
    admin: Admin
    affinity_interrupt: AffinityInterrupt
    affinity_packet_redistribution: AffinityPacketRedistribution
    alarm: Alarm
    alias: Alias
    api_user: ApiUser
    arp_table: ArpTable
    auto_install: AutoInstall
    auto_script: AutoScript
    automation_action: AutomationAction
    automation_condition: AutomationCondition
    automation_destination: AutomationDestination
    automation_stitch: AutomationStitch
    automation_trigger: AutomationTrigger
    central_management: CentralManagement
    cloud_service: CloudService
    console: Console
    csf: Csf
    custom_language: CustomLanguage
    ddns: Ddns
    dedicated_mgmt: DedicatedMgmt
    device_upgrade: DeviceUpgrade
    device_upgrade_exemptions: DeviceUpgradeExemptions
    dns: Dns
    dns64: Dns64
    dns_database: DnsDatabase
    dns_server: DnsServer
    dscp_based_priority: DscpBasedPriority
    email_server: EmailServer
    evpn: Evpn
    external_resource: ExternalResource
    fabric_vpn: FabricVpn
    federated_upgrade: FederatedUpgrade
    fips_cc: FipsCc
    fortiguard: Fortiguard
    fortisandbox: Fortisandbox
    fsso_polling: FssoPolling
    ftm_push: FtmPush
    geneve: Geneve
    geoip_country: GeoipCountry
    geoip_override: GeoipOverride
    global_: Global
    gre_tunnel: GreTunnel
    ha: Ha
    ha_monitor: HaMonitor
    health_check_fortiguard: HealthCheckFortiguard
    ike: Ike
    interface: Interface
    ipam: Ipam
    ipip_tunnel: IpipTunnel
    ips: Ips
    ips_urlfilter_dns: IpsUrlfilterDns
    ips_urlfilter_dns6: IpsUrlfilterDns6
    ipsec_aggregate: IpsecAggregate
    ipv6_neighbor_cache: Ipv6NeighborCache
    ipv6_tunnel: Ipv6Tunnel
    link_monitor: LinkMonitor
    lte_modem: LteModem
    mac_address_table: MacAddressTable
    mobile_tunnel: MobileTunnel
    modem: Modem
    nd_proxy: NdProxy
    netflow: Netflow
    network_visibility: NetworkVisibility
    ngfw_settings: NgfwSettings
    np6xlite: Np6xlite
    npu: Npu
    ntp: Ntp
    object_tagging: ObjectTagging
    password_policy: PasswordPolicy
    password_policy_guest_admin: PasswordPolicyGuestAdmin
    pcp_server: PcpServer
    physical_switch: PhysicalSwitch
    pppoe_interface: PppoeInterface
    probe_response: ProbeResponse
    proxy_arp: ProxyArp
    ptp: Ptp
    replacemsg_group: ReplacemsgGroup
    replacemsg_image: ReplacemsgImage
    resource_limits: ResourceLimits
    saml: Saml
    sdn_connector: SdnConnector
    sdn_proxy: SdnProxy
    sdn_vpn: SdnVpn
    sdwan: Sdwan
    session_helper: SessionHelper
    session_ttl: SessionTtl
    settings: Settings
    sflow: Sflow
    sit_tunnel: SitTunnel
    sms_server: SmsServer
    sov_sase: SovSase
    speed_test_schedule: SpeedTestSchedule
    speed_test_server: SpeedTestServer
    speed_test_setting: SpeedTestSetting
    ssh_config: SshConfig
    sso_admin: SsoAdmin
    sso_forticloud_admin: SsoForticloudAdmin
    sso_fortigate_cloud_admin: SsoFortigateCloudAdmin
    standalone_cluster: StandaloneCluster
    storage: Storage
    stp: Stp
    switch_interface: SwitchInterface
    timezone: Timezone
    tos_based_priority: TosBasedPriority
    vdom: Vdom
    vdom_dns: VdomDns
    vdom_exception: VdomException
    vdom_link: VdomLink
    vdom_netflow: VdomNetflow
    vdom_property: VdomProperty
    vdom_radius_server: VdomRadiusServer
    vdom_sflow: VdomSflow
    virtual_switch: VirtualSwitch
    virtual_wire_pair: VirtualWirePair
    vne_interface: VneInterface
    vxlan: Vxlan
    wccp: Wccp
    zone: Zone

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize system category with HTTP client."""
        ...
