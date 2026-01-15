"""Type stubs for SYSTEM category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .acme_certificate_status import AcmeCertificateStatus
    from .acquired_dns import AcquiredDns
    from .available_certificates import AvailableCertificates
    from .check_port_availability import CheckPortAvailability
    from .current_admins import CurrentAdmins
    from .global_resources import GlobalResources
    from .global_search import GlobalSearch
    from .ha_backup_hb_used import HaBackupHbUsed
    from .ha_checksums import HaChecksums
    from .ha_history import HaHistory
    from .ha_hw_interface import HaHwInterface
    from .ha_nonsync_checksums import HaNonsyncChecksums
    from .ha_statistics import HaStatistics
    from .ha_table_checksums import HaTableChecksums
    from .interface_connected_admins_info import InterfaceConnectedAdminsInfo
    from .ipconf import Ipconf
    from .link_monitor import LinkMonitor
    from .modem3g import Modem3g
    from .monitor_sensor import MonitorSensor
    from .resolve_fqdn import ResolveFqdn
    from .running_processes import RunningProcesses
    from .sensor_info import SensorInfo
    from .status import Status
    from .storage import Storage
    from .timezone import Timezone
    from .trusted_cert_authorities import TrustedCertAuthorities
    from .vdom_link import VdomLink
    from .vdom_resource import VdomResource
    from .vm_information import VmInformation
    from .admin import Admin
    from .api_user import ApiUser
    from .automation_action import AutomationAction
    from .automation_stitch import AutomationStitch
    from .available_interfaces import AvailableInterfaces
    from .botnet import Botnet
    from .botnet_domains import BotnetDomains
    from .central_management import CentralManagement
    from .certificate import Certificate
    from .change_password import ChangePassword
    from .cluster import Cluster
    from .com_log import ComLog
    from .config import Config
    from .config_error_log import ConfigErrorLog
    from .config_revision import ConfigRevision
    from .config_script import ConfigScript
    from .config_sync import ConfigSync
    from .crash_log import CrashLog
    from .csf import Csf
    from .debug import Debug
    from .dhcp import Dhcp
    from .dhcp6 import Dhcp6
    from .disconnect_admins import DisconnectAdmins
    from .external_resource import ExternalResource
    from .firmware import Firmware
    from .fortiguard import Fortiguard
    from .fortimanager import Fortimanager
    from .fsck import Fsck
    from .ha_peer import HaPeer
    from .hscalefw_license import HscalefwLicense
    from .interface import Interface
    from .ipam import Ipam
    from .logdisk import Logdisk
    from .lte_modem import LteModem
    from .modem import Modem
    from .modem5g import Modem5g
    from .ntp import Ntp
    from .object import Object
    from .os import Os
    from .password_policy_conform import PasswordPolicyConform
    from .performance import Performance
    from .private_data_encryption import PrivateDataEncryption
    from .process import Process
    from .resource import Resource
    from .sandbox import Sandbox
    from .sdn_connector import SdnConnector
    from .time import Time
    from .traffic_history import TrafficHistory
    from .upgrade_report import UpgradeReport
    from .usb_device import UsbDevice
    from .usb_log import UsbLog
    from .vmlicense import Vmlicense

__all__ = [
    "AcmeCertificateStatus",
    "AcquiredDns",
    "AvailableCertificates",
    "CheckPortAvailability",
    "CurrentAdmins",
    "GlobalResources",
    "GlobalSearch",
    "HaBackupHbUsed",
    "HaChecksums",
    "HaHistory",
    "HaHwInterface",
    "HaNonsyncChecksums",
    "HaStatistics",
    "HaTableChecksums",
    "InterfaceConnectedAdminsInfo",
    "Ipconf",
    "LinkMonitor",
    "Modem3g",
    "MonitorSensor",
    "ResolveFqdn",
    "RunningProcesses",
    "SensorInfo",
    "Status",
    "Storage",
    "Timezone",
    "TrustedCertAuthorities",
    "VdomLink",
    "VdomResource",
    "VmInformation",
    "System",
]


class System:
    """SYSTEM API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    admin: Admin
    api_user: ApiUser
    automation_action: AutomationAction
    automation_stitch: AutomationStitch
    available_interfaces: AvailableInterfaces
    botnet: Botnet
    botnet_domains: BotnetDomains
    central_management: CentralManagement
    certificate: Certificate
    change_password: ChangePassword
    cluster: Cluster
    com_log: ComLog
    config: Config
    config_error_log: ConfigErrorLog
    config_revision: ConfigRevision
    config_script: ConfigScript
    config_sync: ConfigSync
    crash_log: CrashLog
    csf: Csf
    debug: Debug
    dhcp: Dhcp
    dhcp6: Dhcp6
    disconnect_admins: DisconnectAdmins
    external_resource: ExternalResource
    firmware: Firmware
    fortiguard: Fortiguard
    fortimanager: Fortimanager
    fsck: Fsck
    ha_peer: HaPeer
    hscalefw_license: HscalefwLicense
    interface: Interface
    ipam: Ipam
    logdisk: Logdisk
    lte_modem: LteModem
    modem: Modem
    modem5g: Modem5g
    ntp: Ntp
    object: Object
    os: Os
    password_policy_conform: PasswordPolicyConform
    performance: Performance
    private_data_encryption: PrivateDataEncryption
    process: Process
    resource: Resource
    sandbox: Sandbox
    sdn_connector: SdnConnector
    time: Time
    traffic_history: TrafficHistory
    upgrade_report: UpgradeReport
    usb_device: UsbDevice
    usb_log: UsbLog
    vmlicense: Vmlicense
    acme_certificate_status: AcmeCertificateStatus
    acquired_dns: AcquiredDns
    available_certificates: AvailableCertificates
    check_port_availability: CheckPortAvailability
    current_admins: CurrentAdmins
    global_resources: GlobalResources
    global_search: GlobalSearch
    ha_backup_hb_used: HaBackupHbUsed
    ha_checksums: HaChecksums
    ha_history: HaHistory
    ha_hw_interface: HaHwInterface
    ha_nonsync_checksums: HaNonsyncChecksums
    ha_statistics: HaStatistics
    ha_table_checksums: HaTableChecksums
    interface_connected_admins_info: InterfaceConnectedAdminsInfo
    ipconf: Ipconf
    link_monitor: LinkMonitor
    modem3g: Modem3g
    monitor_sensor: MonitorSensor
    resolve_fqdn: ResolveFqdn
    running_processes: RunningProcesses
    sensor_info: SensorInfo
    status: Status
    storage: Storage
    timezone: Timezone
    trusted_cert_authorities: TrustedCertAuthorities
    vdom_link: VdomLink
    vdom_resource: VdomResource
    vm_information: VmInformation

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize system category with HTTP client."""
        ...
