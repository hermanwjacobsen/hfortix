"""FortiOS CMDB - Wireless-controller category"""

from .access_control_list import AccessControlList
from .ap_status import ApStatus
from .apcfg_profile import ApcfgProfile
from .arrp_profile import ArrpProfile
from .ble_profile import BleProfile
from .bonjour_profile import BonjourProfile
from .global_ import Global
from .hotspot20_anqp_3gpp_cellular import Hotspot20AnqpThreeGppCellular
from .hotspot20_anqp_ip_address_type import Hotspot20AnqpIpAddressType
from .hotspot20_anqp_nai_realm import Hotspot20AnqpNaiRealm
from .hotspot20_anqp_network_auth_type import Hotspot20AnqpNetworkAuthType
from .hotspot20_anqp_roaming_consortium import Hotspot20AnqpRoamingConsortium
from .hotspot20_anqp_venue_name import Hotspot20AnqpVenueName
from .hotspot20_anqp_venue_url import Hotspot20AnqpVenueUrl
from .hotspot20_h2qp_advice_of_charge import Hotspot20H2qpAdviceOfCharge
from .hotspot20_h2qp_conn_capability import Hotspot20H2qpConnCapability
from .hotspot20_h2qp_operator_name import Hotspot20H2qpOperatorName
from .hotspot20_h2qp_osu_provider import Hotspot20H2qpOsuProvider
from .hotspot20_h2qp_osu_provider_nai import Hotspot20H2qpOsuProviderNai
from .hotspot20_h2qp_terms_and_conditions import (
    Hotspot20H2qpTermsAndConditions,
)
from .hotspot20_h2qp_wan_metric import Hotspot20H2qpWanMetric
from .hotspot20_hs_profile import Hotspot20HsProfile
from .hotspot20_icon import Hotspot20Icon
from .hotspot20_qos_map import Hotspot20QosMap
from .inter_controller import InterController
from .log import Log
from .lw_profile import LwProfile
from .mpsk_profile import MpskProfile
from .nac_profile import NacProfile
from .qos_profile import QosProfile
from .region import Region
from .setting import Setting
from .snmp import Snmp
from .ssid_policy import SsidPolicy
from .syslog_profile import SyslogProfile
from .timers import Timers
from .utm_profile import UtmProfile
from .vap import Vap
from .vap_group import VapGroup
from .wag_profile import WagProfile
from .wids_profile import WidsProfile
from .wtp import Wtp
from .wtp_group import WtpGroup
from .wtp_profile import WtpProfile

__all__ = [
    "AccessControlList",
    "ApStatus",
    "ApcfgProfile",
    "ArrpProfile",
    "BleProfile",
    "BonjourProfile",
    "Global",
    "Hotspot20AnqpThreeGppCellular",
    "Hotspot20AnqpIpAddressType",
    "Hotspot20AnqpNaiRealm",
    "Hotspot20AnqpNetworkAuthType",
    "Hotspot20AnqpRoamingConsortium",
    "Hotspot20AnqpVenueName",
    "Hotspot20AnqpVenueUrl",
    "Hotspot20H2qpAdviceOfCharge",
    "Hotspot20H2qpConnCapability",
    "Hotspot20H2qpOperatorName",
    "Hotspot20H2qpOsuProvider",
    "Hotspot20H2qpOsuProviderNai",
    "Hotspot20H2qpTermsAndConditions",
    "Hotspot20H2qpWanMetric",
    "Hotspot20HsProfile",
    "Hotspot20Icon",
    "Hotspot20QosMap",
    "InterController",
    "Log",
    "LwProfile",
    "MpskProfile",
    "NacProfile",
    "QosProfile",
    "Region",
    "Setting",
    "Snmp",
    "SsidPolicy",
    "SyslogProfile",
    "Timers",
    "UtmProfile",
    "Vap",
    "VapGroup",
    "WagProfile",
    "WidsProfile",
    "Wtp",
    "WtpGroup",
    "WtpProfile",
]


class WirelessController:
    """
    WirelessController category wrapper.

    This class provides access to all wireless-controller CMDB endpoints.
    """

    def __init__(self, client):
        """
        Initialize WirelessController with all endpoint classes.

        Args:
            client: HTTPClient instance
        """
        self.access_control_list = AccessControlList(client)
        self.ap_status = ApStatus(client)
        self.apcfg_profile = ApcfgProfile(client)
        self.arrp_profile = ArrpProfile(client)
        self.ble_profile = BleProfile(client)
        self.bonjour_profile = BonjourProfile(client)
        self.global_ = Global(client)
        self.hotspot20_anqp_3gpp_cellular = Hotspot20AnqpThreeGppCellular(
            client
        )
        self.hotspot20_anqp_ip_address_type = Hotspot20AnqpIpAddressType(
            client
        )
        self.hotspot20_anqp_nai_realm = Hotspot20AnqpNaiRealm(client)
        self.hotspot20_anqp_network_auth_type = Hotspot20AnqpNetworkAuthType(
            client
        )
        self.hotspot20_anqp_roaming_consortium = (
            Hotspot20AnqpRoamingConsortium(client)
        )
        self.hotspot20_anqp_venue_name = Hotspot20AnqpVenueName(client)
        self.hotspot20_anqp_venue_url = Hotspot20AnqpVenueUrl(client)
        self.hotspot20_h2qp_advice_of_charge = Hotspot20H2qpAdviceOfCharge(
            client
        )
        self.hotspot20_h2qp_conn_capability = Hotspot20H2qpConnCapability(
            client
        )
        self.hotspot20_h2qp_operator_name = Hotspot20H2qpOperatorName(client)
        self.hotspot20_h2qp_osu_provider = Hotspot20H2qpOsuProvider(client)
        self.hotspot20_h2qp_osu_provider_nai = Hotspot20H2qpOsuProviderNai(
            client
        )
        self.hotspot20_h2qp_terms_and_conditions = (
            Hotspot20H2qpTermsAndConditions(client)
        )
        self.hotspot20_h2qp_wan_metric = Hotspot20H2qpWanMetric(client)
        self.hotspot20_hs_profile = Hotspot20HsProfile(client)
        self.hotspot20_icon = Hotspot20Icon(client)
        self.hotspot20_qos_map = Hotspot20QosMap(client)
        self.inter_controller = InterController(client)
        self.log = Log(client)
        self.lw_profile = LwProfile(client)
        self.mpsk_profile = MpskProfile(client)
        self.nac_profile = NacProfile(client)
        self.qos_profile = QosProfile(client)
        self.region = Region(client)
        self.setting = Setting(client)
        self.snmp = Snmp(client)
        self.ssid_policy = SsidPolicy(client)
        self.syslog_profile = SyslogProfile(client)
        self.timers = Timers(client)
        self.utm_profile = UtmProfile(client)
        self.vap = Vap(client)
        self.vap_group = VapGroup(client)
        self.wag_profile = WagProfile(client)
        self.wids_profile = WidsProfile(client)
        self.wtp = Wtp(client)
        self.wtp_group = WtpGroup(client)
        self.wtp_profile = WtpProfile(client)
