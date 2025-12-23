"""
FortiOS Monitor - System
System monitoring, status, and diagnostics
"""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client_interface import IHTTPClient

__all__ = ["System"]

from .acme_certificate_status import AcmeCertificateStatus
from .acquired_dns import AcquiredDns
from .admin import Admin
from .api_user import ApiUser
from .automation_action import AutomationAction
from .automation_stitch import AutomationStitch
from .available_certificates import AvailableCertificates
from .available_interfaces import AvailableInterfaces
from .botnet import Botnet
from .botnet_domains import BotnetDomains
from .central_management import CentralManagement
from .certificate import Certificate
from .change_password import ChangePassword
from .check_port_availability import CheckPortAvailability
from .cluster import Cluster
from .com_log import ComLog
from .config import Config
from .config_error_log import ConfigErrorLog
from .config_revision import ConfigRevision
from .config_script import ConfigScript
from .config_sync import ConfigSync
from .crash_log import CrashLog
from .csf import Csf
from .current_admins import CurrentAdmins
from .debug import Debug
from .dhcp import Dhcp
from .dhcp6 import Dhcp6
from .disconnect_admins import DisconnectAdmins
from .external_resource import ExternalResource
from .firmware import Firmware
from .fortiguard import Fortiguard
from .fortimanager import Fortimanager
from .fsck import Fsck
from .global_resources import GlobalResources
from .global_search import GlobalSearch
from .ha_backup_hb_used import HaBackupHbUsed
from .ha_checksums import HaChecksums
from .ha_history import HaHistory
from .ha_hw_interface import HaHwInterface
from .ha_nonsync_checksums import HaNonsyncChecksums
from .ha_peer import HaPeer
from .ha_statistics import HaStatistics
from .ha_table_checksums import HaTableChecksums
from .hscalefw_license import HscalefwLicense
from .interface import Interface
from .interface_connected_admins_info import InterfaceConnectedAdminsInfo
from .ipam import Ipam
from .ipconf import Ipconf
from .link_monitor import LinkMonitor
from .logdisk import Logdisk
from .lte_modem import LteModem
from .modem import Modem
from .modem_3g import Modem3g
from .modem_5g import Modem5g
from .monitor_sensor import MonitorSensor
from .ntp import Ntp
from .object import Object
from .os import Os
from .password_policy_conform import PasswordPolicyConform
from .performance import Performance
from .private_data_encryption import PrivateDataEncryption
from .process import Process
from .resolve_fqdn import ResolveFqdn
from .resource import Resource
from .running_processes import RunningProcesses
from .sandbox import Sandbox
from .sdn_connector import SdnConnector
from .sensor_info import SensorInfo
from .status import Status
from .storage import Storage
from .time import Time
from .timezone import Timezone
from .traffic_history import TrafficHistory
from .trusted_cert_authorities import TrustedCertAuthorities
from .upgrade_report import UpgradeReport
from .usb_device import UsbDevice
from .usb_log import UsbLog
from .vdom_link import VdomLink
from .vdom_resource import VdomResource
from .vm_information import VmInformation
from .vmlicense import Vmlicense


class System:
    """System Monitor category class"""

    def __init__(self, client: "IHTTPClient") -> None:
        """
        Initialize System Monitor category

        Args:
            client: HTTP client implementing IHTTPClient protocol
        """
        self._client = client

        # Initialize endpoints
        self.modem_3g = Modem3g(client)
        self.modem_5g = Modem5g(client)
        self.acme_certificate_status = AcmeCertificateStatus(client)
        self.acquired_dns = AcquiredDns(client)
        self.admin = Admin(client)
        self.api_user = ApiUser(client)
        self.automation_action = AutomationAction(client)
        self.automation_stitch = AutomationStitch(client)
        self.available_certificates = AvailableCertificates(client)
        self.available_interfaces = AvailableInterfaces(client)
        self.botnet = Botnet(client)
        self.botnet_domains = BotnetDomains(client)
        self.central_management = CentralManagement(client)
        self.certificate = Certificate(client)
        self.change_password = ChangePassword(client)
        self.check_port_availability = CheckPortAvailability(client)
        self.cluster = Cluster(client)
        self.com_log = ComLog(client)
        self.config = Config(client)
        self.config_error_log = ConfigErrorLog(client)
        self.config_revision = ConfigRevision(client)
        self.config_script = ConfigScript(client)
        self.config_sync = ConfigSync(client)
        self.crash_log = CrashLog(client)
        self.csf = Csf(client)
        self.current_admins = CurrentAdmins(client)
        self.debug = Debug(client)
        self.dhcp = Dhcp(client)
        self.dhcp6 = Dhcp6(client)
        self.disconnect_admins = DisconnectAdmins(client)
        self.external_resource = ExternalResource(client)
        self.firmware = Firmware(client)
        self.fortiguard = Fortiguard(client)
        self.fortimanager = Fortimanager(client)
        self.fsck = Fsck(client)
        self.global_resources = GlobalResources(client)
        self.global_search = GlobalSearch(client)
        self.ha_backup_hb_used = HaBackupHbUsed(client)
        self.ha_checksums = HaChecksums(client)
        self.ha_history = HaHistory(client)
        self.ha_hw_interface = HaHwInterface(client)
        self.ha_nonsync_checksums = HaNonsyncChecksums(client)
        self.ha_peer = HaPeer(client)
        self.ha_statistics = HaStatistics(client)
        self.ha_table_checksums = HaTableChecksums(client)
        self.hscalefw_license = HscalefwLicense(client)
        self.interface = Interface(client)
        self.interface_connected_admins_info = InterfaceConnectedAdminsInfo(
            client
        )
        self.ipam = Ipam(client)
        self.ipconf = Ipconf(client)
        self.link_monitor = LinkMonitor(client)
        self.logdisk = Logdisk(client)
        self.lte_modem = LteModem(client)
        self.modem = Modem(client)
        self.monitor_sensor = MonitorSensor(client)
        self.ntp = Ntp(client)
        self.object = Object(client)
        self.os = Os(client)
        self.password_policy_conform = PasswordPolicyConform(client)
        self.performance = Performance(client)
        self.private_data_encryption = PrivateDataEncryption(client)
        self.process = Process(client)
        self.resolve_fqdn = ResolveFqdn(client)
        self.resource = Resource(client)
        self.running_processes = RunningProcesses(client)
        self.sandbox = Sandbox(client)
        self.sdn_connector = SdnConnector(client)
        self.sensor_info = SensorInfo(client)
        self.status = Status(client)
        self.storage = Storage(client)
        self.time = Time(client)
        self.timezone = Timezone(client)
        self.traffic_history = TrafficHistory(client)
        self.trusted_cert_authorities = TrustedCertAuthorities(client)
        self.upgrade_report = UpgradeReport(client)
        self.usb_device = UsbDevice(client)
        self.usb_log = UsbLog(client)
        self.vdom_link = VdomLink(client)
        self.vdom_resource = VdomResource(client)
        self.vm_information = VmInformation(client)
        self.vmlicense = Vmlicense(client)

    def __dir__(self):
        """Control autocomplete to show only public attributes"""
        return [
            "3g_modem",
            "5g_modem",
            "acme_certificate_status",
            "acquired_dns",
            "admin",
            "api_user",
            "automation_action",
            "automation_stitch",
            "available_certificates",
            "available_interfaces",
            "botnet",
            "botnet_domains",
            "central_management",
            "certificate",
            "change_password",
            "check_port_availability",
            "cluster",
            "com_log",
            "config",
            "config_error_log",
            "config_revision",
            "config_script",
            "config_sync",
            "crash_log",
            "cs",
            "current_admins",
            "debug",
            "dhcp",
            "dhcp6",
            "disconnect_admins",
            "external_resource",
            "firmware",
            "fortiguard",
            "fortimanager",
            "fsck",
            "global_resources",
            "global_search",
            "ha_backup_hb_used",
            "ha_checksums",
            "ha_history",
            "ha_hw_interface",
            "ha_nonsync_checksums",
            "ha_peer",
            "ha_statistics",
            "ha_table_checksums",
            "hscalefw_license",
            "interface",
            "interface_connected_admins_info",
            "ipam",
            "ipcon",
            "link_monitor",
            "logdisk",
            "lte_modem",
            "modem",
            "monitor_sensor",
            "ntp",
            "object",
            "os",
            "password_policy_conform",
            "performance",
            "private_data_encryption",
            "process",
            "resolve_fqdn",
            "resource",
            "running_processes",
            "sandbox",
            "sdn_connector",
            "sensor_info",
            "status",
            "storage",
            "time",
            "timezone",
            "traffic_history",
            "trusted_cert_authorities",
            "upgrade_report",
            "usb_device",
            "usb_log",
            "vdom_link",
            "vdom_resource",
            "vm_information",
            "vmlicense",
        ]
