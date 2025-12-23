"""FortiOS CMDB - System category"""

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
from .autoupdate_schedule import AutoupdateSchedule
from .central_management import CentralManagement
from .cloud_service import CloudService
from .console import Console
from .csf import Csf
from .custom_language import CustomLanguage
from .ddns import Ddns
from .dedicated_mgmt import DedicatedMgmt
from .device_upgrade import DeviceUpgrade
from .device_upgrade_exemptions import DeviceUpgradeExemptions
from .dhcp6_server import Dhcp6Server
from .dhcp_server import DhcpServer
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
from .lldp_network_policy import LldpNetworkPolicy
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
from .replacemsg_admin import ReplacemsgAdmin
from .replacemsg_alertmail import ReplacemsgAlertmail
from .replacemsg_auth import ReplacemsgAuth
from .replacemsg_automation import ReplacemsgAutomation
from .replacemsg_fortiguard_wf import ReplacemsgFortiguardWf
from .replacemsg_group import ReplacemsgGroup
from .replacemsg_http import ReplacemsgHttp
from .replacemsg_image import ReplacemsgImage
from .replacemsg_mail import ReplacemsgMail
from .replacemsg_nac_quar import ReplacemsgNacQuar
from .replacemsg_spam import ReplacemsgSpam
from .replacemsg_sslvpn import ReplacemsgSslvpn
from .replacemsg_traffic_quota import ReplacemsgTrafficQuota
from .replacemsg_utm import ReplacemsgUtm
from .resource_limits import ResourceLimits
from .saml import Saml
from .sdn_connector import SdnConnector
from .sdn_proxy import SdnProxy
from .sdn_vpn import SdnVpn
from .sdwan import Sdwan
from .security_rating_controls import SecurityRatingControls
from .security_rating_settings import SecurityRatingSettings
from .session_helper import SessionHelper
from .session_ttl import SessionTtl
from .settings import Settings
from .sflow import Sflow
from .sit_tunnel import SitTunnel
from .sms_server import SmsServer
from .snmp_community import SnmpCommunity
from .snmp_mib_view import SnmpMibView
from .snmp_rmon_stat import SnmpRmonStat
from .snmp_sysinfo import SnmpSysinfo
from .snmp_user import SnmpUser
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
    "AutoupdateSchedule",
    "CentralManagement",
    "CloudService",
    "Console",
    "Cs",
    "CustomLanguage",
    "Ddns",
    "DedicatedMgmt",
    "DeviceUpgrade",
    "DeviceUpgradeExemptions",
    "Dhcp6Server",
    "DhcpServer",
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
    "LldpNetworkPolicy",
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
    "ReplacemsgAdmin",
    "ReplacemsgAlertmail",
    "ReplacemsgAuth",
    "ReplacemsgAutomation",
    "ReplacemsgFortiguardW",
    "ReplacemsgGroup",
    "ReplacemsgHttp",
    "ReplacemsgImage",
    "ReplacemsgMail",
    "ReplacemsgNacQuar",
    "ReplacemsgSpam",
    "ReplacemsgSslvpn",
    "ReplacemsgTrafficQuota",
    "ReplacemsgUtm",
    "ResourceLimits",
    "Saml",
    "SdnConnector",
    "SdnProxy",
    "SdnVpn",
    "Sdwan",
    "SecurityRatingControls",
    "SecurityRatingSettings",
    "SessionHelper",
    "SessionTtl",
    "Settings",
    "Sflow",
    "SitTunnel",
    "SmsServer",
    "SnmpCommunity",
    "SnmpMibView",
    "SnmpRmonStat",
    "SnmpSysinfo",
    "SnmpUser",
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
]


class System:
    """
    System category wrapper.

    This class provides access to all system CMDB endpoints.
    """

    def __init__(self, client):
        """
        Initialize System with all endpoint classes.

        Args:
            client: HTTPClient instance
        """
        self.accprofile = Accprofile(client)
        self.acme = Acme(client)
        self.admin = Admin(client)
        self.affinity_interrupt = AffinityInterrupt(client)
        self.affinity_packet_redistribution = AffinityPacketRedistribution(
            client
        )
        self.alarm = Alarm(client)
        self.alias = Alias(client)
        self.api_user = ApiUser(client)
        self.arp_table = ArpTable(client)
        self.auto_install = AutoInstall(client)
        self.auto_script = AutoScript(client)
        self.automation_action = AutomationAction(client)
        self.automation_condition = AutomationCondition(client)
        self.automation_destination = AutomationDestination(client)
        self.automation_stitch = AutomationStitch(client)
        self.automation_trigger = AutomationTrigger(client)
        self.autoupdate_schedule = AutoupdateSchedule(client)
        self.central_management = CentralManagement(client)
        self.cloud_service = CloudService(client)
        self.console = Console(client)
        self.csf = Csf(client)
        self.custom_language = CustomLanguage(client)
        self.ddns = Ddns(client)
        self.dedicated_mgmt = DedicatedMgmt(client)
        self.device_upgrade = DeviceUpgrade(client)
        self.device_upgrade_exemptions = DeviceUpgradeExemptions(client)
        self.dhcp6_server = Dhcp6Server(client)
        self.dhcp_server = DhcpServer(client)
        self.dns = Dns(client)
        self.dns64 = Dns64(client)
        self.dns_database = DnsDatabase(client)
        self.dns_server = DnsServer(client)
        self.dscp_based_priority = DscpBasedPriority(client)
        self.email_server = EmailServer(client)
        self.evpn = Evpn(client)
        self.external_resource = ExternalResource(client)
        self.fabric_vpn = FabricVpn(client)
        self.federated_upgrade = FederatedUpgrade(client)
        self.fips_cc = FipsCc(client)
        self.fortiguard = Fortiguard(client)
        self.fortisandbox = Fortisandbox(client)
        self.fsso_polling = FssoPolling(client)
        self.ftm_push = FtmPush(client)
        self.geneve = Geneve(client)
        self.geoip_country = GeoipCountry(client)
        self.geoip_override = GeoipOverride(client)
        self.global_ = Global(client)
        self.gre_tunnel = GreTunnel(client)
        self.ha = Ha(client)
        self.ha_monitor = HaMonitor(client)
        self.health_check_fortiguard = HealthCheckFortiguard(client)
        self.ike = Ike(client)
        self.interface = Interface(client)
        self.ipam = Ipam(client)
        self.ipip_tunnel = IpipTunnel(client)
        self.ips = Ips(client)
        self.ips_urlfilter_dns = IpsUrlfilterDns(client)
        self.ips_urlfilter_dns6 = IpsUrlfilterDns6(client)
        self.ipsec_aggregate = IpsecAggregate(client)
        self.ipv6_neighbor_cache = Ipv6NeighborCache(client)
        self.ipv6_tunnel = Ipv6Tunnel(client)
        self.link_monitor = LinkMonitor(client)
        self.lldp_network_policy = LldpNetworkPolicy(client)
        self.lte_modem = LteModem(client)
        self.mac_address_table = MacAddressTable(client)
        self.mobile_tunnel = MobileTunnel(client)
        self.modem = Modem(client)
        self.nd_proxy = NdProxy(client)
        self.netflow = Netflow(client)
        self.network_visibility = NetworkVisibility(client)
        self.ngfw_settings = NgfwSettings(client)
        self.np6xlite = Np6xlite(client)
        self.npu = Npu(client)
        self.ntp = Ntp(client)
        self.object_tagging = ObjectTagging(client)
        self.password_policy = PasswordPolicy(client)
        self.password_policy_guest_admin = PasswordPolicyGuestAdmin(client)
        self.pcp_server = PcpServer(client)
        self.physical_switch = PhysicalSwitch(client)
        self.pppoe_interface = PppoeInterface(client)
        self.probe_response = ProbeResponse(client)
        self.proxy_arp = ProxyArp(client)
        self.ptp = Ptp(client)
        self.replacemsg_admin = ReplacemsgAdmin(client)
        self.replacemsg_alertmail = ReplacemsgAlertmail(client)
        self.replacemsg_auth = ReplacemsgAuth(client)
        self.replacemsg_automation = ReplacemsgAutomation(client)
        self.replacemsg_fortiguard_wf = ReplacemsgFortiguardWf(client)
        self.replacemsg_group = ReplacemsgGroup(client)
        self.replacemsg_http = ReplacemsgHttp(client)
        self.replacemsg_image = ReplacemsgImage(client)
        self.replacemsg_mail = ReplacemsgMail(client)
        self.replacemsg_nac_quar = ReplacemsgNacQuar(client)
        self.replacemsg_spam = ReplacemsgSpam(client)
        self.replacemsg_sslvpn = ReplacemsgSslvpn(client)
        self.replacemsg_traffic_quota = ReplacemsgTrafficQuota(client)
        self.replacemsg_utm = ReplacemsgUtm(client)
        self.resource_limits = ResourceLimits(client)
        self.saml = Saml(client)
        self.sdn_connector = SdnConnector(client)
        self.sdn_proxy = SdnProxy(client)
        self.sdn_vpn = SdnVpn(client)
        self.sdwan = Sdwan(client)
        self.security_rating_controls = SecurityRatingControls(client)
        self.security_rating_settings = SecurityRatingSettings(client)
        self.session_helper = SessionHelper(client)
        self.session_ttl = SessionTtl(client)
        self.settings = Settings(client)
        self.sflow = Sflow(client)
        self.sit_tunnel = SitTunnel(client)
        self.sms_server = SmsServer(client)
        self.snmp_community = SnmpCommunity(client)
        self.snmp_mib_view = SnmpMibView(client)
        self.snmp_rmon_stat = SnmpRmonStat(client)
        self.snmp_sysinfo = SnmpSysinfo(client)
        self.snmp_user = SnmpUser(client)
        self.sov_sase = SovSase(client)
        self.speed_test_schedule = SpeedTestSchedule(client)
        self.speed_test_server = SpeedTestServer(client)
        self.speed_test_setting = SpeedTestSetting(client)
        self.ssh_config = SshConfig(client)
        self.sso_admin = SsoAdmin(client)
        self.sso_forticloud_admin = SsoForticloudAdmin(client)
        self.sso_fortigate_cloud_admin = SsoFortigateCloudAdmin(client)
        self.standalone_cluster = StandaloneCluster(client)
        self.storage = Storage(client)
        self.stp = Stp(client)
        self.switch_interface = SwitchInterface(client)
        self.timezone = Timezone(client)
        self.tos_based_priority = TosBasedPriority(client)
        self.vdom = Vdom(client)
        self.vdom_dns = VdomDns(client)
        self.vdom_exception = VdomException(client)
        self.vdom_link = VdomLink(client)
        self.vdom_netflow = VdomNetflow(client)
        self.vdom_property = VdomProperty(client)
        self.vdom_radius_server = VdomRadiusServer(client)
        self.vdom_sflow = VdomSflow(client)
        self.virtual_switch = VirtualSwitch(client)
        self.virtual_wire_pair = VirtualWirePair(client)
        self.vne_interface = VneInterface(client)
        self.vxlan = Vxlan(client)
        self.wccp = Wccp(client)
        self.zone = Zone(client)
