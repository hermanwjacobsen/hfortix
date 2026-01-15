"""Type stubs for WIRELESS_CONTROLLER category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .access_control_list import AccessControlList
    from .ap_status import ApStatus
    from .apcfg_profile import ApcfgProfile
    from .arrp_profile import ArrpProfile
    from .ble_profile import BleProfile
    from .bonjour_profile import BonjourProfile
    from .global_ import Global
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
    from .hotspot20 import Hotspot20

__all__ = [
    "AccessControlList",
    "ApStatus",
    "ApcfgProfile",
    "ArrpProfile",
    "BleProfile",
    "BonjourProfile",
    "Global",
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
    "WirelessController",
]


class WirelessController:
    """WIRELESS_CONTROLLER API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    hotspot20: Hotspot20
    access_control_list: AccessControlList
    ap_status: ApStatus
    apcfg_profile: ApcfgProfile
    arrp_profile: ArrpProfile
    ble_profile: BleProfile
    bonjour_profile: BonjourProfile
    global_: Global
    inter_controller: InterController
    log: Log
    lw_profile: LwProfile
    mpsk_profile: MpskProfile
    nac_profile: NacProfile
    qos_profile: QosProfile
    region: Region
    setting: Setting
    snmp: Snmp
    ssid_policy: SsidPolicy
    syslog_profile: SyslogProfile
    timers: Timers
    utm_profile: UtmProfile
    vap: Vap
    vap_group: VapGroup
    wag_profile: WagProfile
    wids_profile: WidsProfile
    wtp: Wtp
    wtp_group: WtpGroup
    wtp_profile: WtpProfile

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize wireless_controller category with HTTP client."""
        ...
