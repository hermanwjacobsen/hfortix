"""FortiOS CMDB - Log category"""

from .custom_field import CustomField
from .disk_filter import DiskFilter
from .disk_setting import DiskSetting
from .eventfilter import Eventfilter
from .fortianalyzer2_filter import Fortianalyzer2Filter
from .fortianalyzer2_override_filter import Fortianalyzer2OverrideFilter
from .fortianalyzer2_override_setting import Fortianalyzer2OverrideSetting
from .fortianalyzer2_setting import Fortianalyzer2Setting
from .fortianalyzer3_filter import Fortianalyzer3Filter
from .fortianalyzer3_override_filter import Fortianalyzer3OverrideFilter
from .fortianalyzer3_override_setting import Fortianalyzer3OverrideSetting
from .fortianalyzer3_setting import Fortianalyzer3Setting
from .fortianalyzer_cloud_filter import FortianalyzerCloudFilter
from .fortianalyzer_cloud_override_filter import (
    FortianalyzerCloudOverrideFilter,
)
from .fortianalyzer_cloud_override_setting import (
    FortianalyzerCloudOverrideSetting,
)
from .fortianalyzer_cloud_setting import FortianalyzerCloudSetting
from .fortianalyzer_filter import FortianalyzerFilter
from .fortianalyzer_override_filter import FortianalyzerOverrideFilter
from .fortianalyzer_override_setting import FortianalyzerOverrideSetting
from .fortianalyzer_setting import FortianalyzerSetting
from .fortiguard_filter import FortiguardFilter
from .fortiguard_override_filter import FortiguardOverrideFilter
from .fortiguard_override_setting import FortiguardOverrideSetting
from .fortiguard_setting import FortiguardSetting
from .gui_display import GuiDisplay
from .memory_filter import MemoryFilter
from .memory_global_setting import MemoryGlobalSetting
from .memory_setting import MemorySetting
from .null_device_filter import NullDeviceFilter
from .null_device_setting import NullDeviceSetting
from .setting import Setting
from .syslogd2_filter import Syslogd2Filter
from .syslogd2_override_filter import Syslogd2OverrideFilter
from .syslogd2_override_setting import Syslogd2OverrideSetting
from .syslogd2_setting import Syslogd2Setting
from .syslogd3_filter import Syslogd3Filter
from .syslogd3_override_filter import Syslogd3OverrideFilter
from .syslogd3_override_setting import Syslogd3OverrideSetting
from .syslogd3_setting import Syslogd3Setting
from .syslogd4_filter import Syslogd4Filter
from .syslogd4_override_filter import Syslogd4OverrideFilter
from .syslogd4_override_setting import Syslogd4OverrideSetting
from .syslogd4_setting import Syslogd4Setting
from .syslogd_filter import SyslogdFilter
from .syslogd_override_filter import SyslogdOverrideFilter
from .syslogd_override_setting import SyslogdOverrideSetting
from .syslogd_setting import SyslogdSetting
from .tacacs_plus_accounting2_filter import TacacsPlusAccounting2Filter
from .tacacs_plus_accounting2_setting import TacacsPlusAccounting2Setting
from .tacacs_plus_accounting3_filter import TacacsPlusAccounting3Filter
from .tacacs_plus_accounting3_setting import TacacsPlusAccounting3Setting
from .tacacs_plus_accounting_filter import TacacsPlusAccountingFilter
from .tacacs_plus_accounting_setting import TacacsPlusAccountingSetting
from .threat_weight import ThreatWeight
from .webtrends_filter import WebtrendsFilter
from .webtrends_setting import WebtrendsSetting

__all__ = [
    "CustomField",
    "Eventfilter",
    "GuiDisplay",
    "Setting",
    "ThreatWeight",
    "DiskFilter",
    "DiskSetting",
    "Fortianalyzer2Filter",
    "Fortianalyzer2OverrideFilter",
    "Fortianalyzer2OverrideSetting",
    "Fortianalyzer2Setting",
    "Fortianalyzer3Filter",
    "Fortianalyzer3OverrideFilter",
    "Fortianalyzer3OverrideSetting",
    "Fortianalyzer3Setting",
    "FortianalyzerCloudFilter",
    "FortianalyzerCloudOverrideFilter",
    "FortianalyzerCloudOverrideSetting",
    "FortianalyzerCloudSetting",
    "FortianalyzerFilter",
    "FortianalyzerOverrideFilter",
    "FortianalyzerOverrideSetting",
    "FortianalyzerSetting",
    "FortiguardFilter",
    "FortiguardOverrideFilter",
    "FortiguardOverrideSetting",
    "FortiguardSetting",
    "MemoryFilter",
    "MemoryGlobalSetting",
    "MemorySetting",
    "NullDeviceFilter",
    "NullDeviceSetting",
    "Syslogd2Filter",
    "Syslogd2OverrideFilter",
    "Syslogd2OverrideSetting",
    "Syslogd2Setting",
    "Syslogd3Filter",
    "Syslogd3OverrideFilter",
    "Syslogd3OverrideSetting",
    "Syslogd3Setting",
    "Syslogd4Filter",
    "Syslogd4OverrideFilter",
    "Syslogd4OverrideSetting",
    "Syslogd4Setting",
    "SyslogdFilter",
    "SyslogdOverrideFilter",
    "SyslogdOverrideSetting",
    "SyslogdSetting",
    "TacacsPlusAccounting2Filter",
    "TacacsPlusAccounting2Setting",
    "TacacsPlusAccounting3Filter",
    "TacacsPlusAccounting3Setting",
    "TacacsPlusAccountingFilter",
    "TacacsPlusAccountingSetting",
    "WebtrendsFilter",
    "WebtrendsSetting",
]


class Disk:
    """Wrapper for disk.* endpoints."""

    def __init__(self, client):
        """Initialize Disk endpoints."""
        self.filter = DiskFilter(client)
        self.setting = DiskSetting(client)


class Fortianalyzer2:
    """Wrapper for fortianalyzer2.* endpoints."""

    def __init__(self, client):
        """Initialize Fortianalyzer2 endpoints."""
        self.filter = Fortianalyzer2Filter(client)
        self.override_filter = Fortianalyzer2OverrideFilter(client)
        self.override_setting = Fortianalyzer2OverrideSetting(client)
        self.setting = Fortianalyzer2Setting(client)


class Fortianalyzer3:
    """Wrapper for fortianalyzer3.* endpoints."""

    def __init__(self, client):
        """Initialize Fortianalyzer3 endpoints."""
        self.filter = Fortianalyzer3Filter(client)
        self.override_filter = Fortianalyzer3OverrideFilter(client)
        self.override_setting = Fortianalyzer3OverrideSetting(client)
        self.setting = Fortianalyzer3Setting(client)


class FortianalyzerCloud:
    """Wrapper for fortianalyzer_cloud.* endpoints."""

    def __init__(self, client):
        """Initialize FortianalyzerCloud endpoints."""
        self.filter = FortianalyzerCloudFilter(client)
        self.override_filter = FortianalyzerCloudOverrideFilter(client)
        self.override_setting = FortianalyzerCloudOverrideSetting(client)
        self.setting = FortianalyzerCloudSetting(client)


class Fortianalyzer:
    """Wrapper for fortianalyzer.* endpoints."""

    def __init__(self, client):
        """Initialize Fortianalyzer endpoints."""
        self.filter = FortianalyzerFilter(client)
        self.override_filter = FortianalyzerOverrideFilter(client)
        self.override_setting = FortianalyzerOverrideSetting(client)
        self.setting = FortianalyzerSetting(client)


class Fortiguard:
    """Wrapper for fortiguard.* endpoints."""

    def __init__(self, client):
        """Initialize Fortiguard endpoints."""
        self.filter = FortiguardFilter(client)
        self.override_filter = FortiguardOverrideFilter(client)
        self.override_setting = FortiguardOverrideSetting(client)
        self.setting = FortiguardSetting(client)


class Memory:
    """Wrapper for memory.* endpoints."""

    def __init__(self, client):
        """Initialize Memory endpoints."""
        self.filter = MemoryFilter(client)
        self.global_setting = MemoryGlobalSetting(client)
        self.setting = MemorySetting(client)


class NullDevice:
    """Wrapper for null_device.* endpoints."""

    def __init__(self, client):
        """Initialize NullDevice endpoints."""
        self.filter = NullDeviceFilter(client)
        self.setting = NullDeviceSetting(client)


class Syslogd2:
    """Wrapper for syslogd2.* endpoints."""

    def __init__(self, client):
        """Initialize Syslogd2 endpoints."""
        self.filter = Syslogd2Filter(client)
        self.override_filter = Syslogd2OverrideFilter(client)
        self.override_setting = Syslogd2OverrideSetting(client)
        self.setting = Syslogd2Setting(client)


class Syslogd3:
    """Wrapper for syslogd3.* endpoints."""

    def __init__(self, client):
        """Initialize Syslogd3 endpoints."""
        self.filter = Syslogd3Filter(client)
        self.override_filter = Syslogd3OverrideFilter(client)
        self.override_setting = Syslogd3OverrideSetting(client)
        self.setting = Syslogd3Setting(client)


class Syslogd4:
    """Wrapper for syslogd4.* endpoints."""

    def __init__(self, client):
        """Initialize Syslogd4 endpoints."""
        self.filter = Syslogd4Filter(client)
        self.override_filter = Syslogd4OverrideFilter(client)
        self.override_setting = Syslogd4OverrideSetting(client)
        self.setting = Syslogd4Setting(client)


class Syslogd:
    """Wrapper for syslogd.* endpoints."""

    def __init__(self, client):
        """Initialize Syslogd endpoints."""
        self.filter = SyslogdFilter(client)
        self.override_filter = SyslogdOverrideFilter(client)
        self.override_setting = SyslogdOverrideSetting(client)
        self.setting = SyslogdSetting(client)


class TacacsAccounting2:
    """Wrapper for tacacs_plus_accounting2.* endpoints."""

    def __init__(self, client):
        """Initialize TacacsAccounting2 endpoints."""
        self.filter = TacacsPlusAccounting2Filter(client)
        self.setting = TacacsPlusAccounting2Setting(client)


class TacacsAccounting3:
    """Wrapper for tacacs_plus_accounting3.* endpoints."""

    def __init__(self, client):
        """Initialize TacacsAccounting3 endpoints."""
        self.filter = TacacsPlusAccounting3Filter(client)
        self.setting = TacacsPlusAccounting3Setting(client)


class TacacsAccounting:
    """Wrapper for tacacs_plus_accounting.* endpoints."""

    def __init__(self, client):
        """Initialize TacacsAccounting endpoints."""
        self.filter = TacacsPlusAccountingFilter(client)
        self.setting = TacacsPlusAccountingSetting(client)


class Webtrends:
    """Wrapper for webtrends.* endpoints."""

    def __init__(self, client):
        """Initialize Webtrends endpoints."""
        self.filter = WebtrendsFilter(client)
        self.setting = WebtrendsSetting(client)


class Log:
    """
    Log category wrapper.

    This class provides access to all log CMDB endpoints.
    """

    def __init__(self, client):
        """
        Initialize Log with all endpoint classes.

        Args:
            client: HTTPClient instance
        """
        self.custom_field = CustomField(client)
        self.eventfilter = Eventfilter(client)
        self.gui_display = GuiDisplay(client)
        self.setting = Setting(client)
        self.threat_weight = ThreatWeight(client)
        self.disk = Disk(client)
        self.fortianalyzer2 = Fortianalyzer2(client)
        self.fortianalyzer3 = Fortianalyzer3(client)
        self.fortianalyzer_cloud = FortianalyzerCloud(client)
        self.fortianalyzer = Fortianalyzer(client)
        self.fortiguard = Fortiguard(client)
        self.memory = Memory(client)
        self.null_device = NullDevice(client)
        self.syslogd2 = Syslogd2(client)
        self.syslogd3 = Syslogd3(client)
        self.syslogd4 = Syslogd4(client)
        self.syslogd = Syslogd(client)
        self.tacacs_accounting2 = TacacsAccounting2(client)
        self.tacacs_accounting3 = TacacsAccounting3(client)
        self.tacacs_accounting = TacacsAccounting(client)
        self.webtrends = Webtrends(client)
