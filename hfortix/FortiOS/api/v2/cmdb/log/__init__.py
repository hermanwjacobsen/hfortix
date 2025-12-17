"""
FortiOS Log API

Logging configuration including disk, FortiAnalyzer, syslog, and other log destinations.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ...http_client import HTTPClient


class _Disk:
    """Disk logging endpoints"""

    def __init__(self, client: "HTTPClient") -> None:
        self._client = client

    @property
    def filter(self):
        """Access disk filter endpoint"""
        if not hasattr(self, "_filter"):
            from .disk_filter import DiskFilter

            self._filter = DiskFilter(self._client)
        return self._filter

    @property
    def setting(self):
        """Access disk setting endpoint"""
        if not hasattr(self, "_setting"):
            from .disk_setting import DiskSetting

            self._setting = DiskSetting(self._client)
        return self._setting


class _FortianalyzerCloud:
    """FortiAnalyzer Cloud logging endpoints"""

    def __init__(self, client: "HTTPClient") -> None:
        self._client = client

    @property
    def filter(self):
        """Access FortiAnalyzer Cloud filter endpoint"""
        if not hasattr(self, "_filter"):
            from .fortianalyzer_cloud_filter import FortianalyzerCloudFilter

            self._filter = FortianalyzerCloudFilter(self._client)
        return self._filter

    @property
    def override_filter(self):
        """Access FortiAnalyzer Cloud override filter endpoint"""
        if not hasattr(self, "_override_filter"):
            from .fortianalyzer_cloud_override_filter import \
                FortianalyzerCloudOverrideFilter

            self._override_filter = FortianalyzerCloudOverrideFilter(self._client)
        return self._override_filter

    @property
    def override_setting(self):
        """Access FortiAnalyzer Cloud override setting endpoint"""
        if not hasattr(self, "_override_setting"):
            from .fortianalyzer_cloud_override_setting import \
                FortianalyzerCloudOverrideSetting

            self._override_setting = FortianalyzerCloudOverrideSetting(self._client)
        return self._override_setting

    @property
    def setting(self):
        """Access FortiAnalyzer Cloud setting endpoint"""
        if not hasattr(self, "_setting"):
            from .fortianalyzer_cloud_setting import FortianalyzerCloudSetting

            self._setting = FortianalyzerCloudSetting(self._client)
        return self._setting


class _Fortianalyzer:
    """FortiAnalyzer logging endpoints"""

    def __init__(self, client: "HTTPClient") -> None:
        self._client = client

    @property
    def filter(self):
        """Access FortiAnalyzer filter endpoint"""
        if not hasattr(self, "_filter"):
            from .fortianalyzer_filter import FortianalyzerFilter

            self._filter = FortianalyzerFilter(self._client)
        return self._filter

    @property
    def override_filter(self):
        """Access FortiAnalyzer override filter endpoint"""
        if not hasattr(self, "_override_filter"):
            from .fortianalyzer_override_filter import \
                FortianalyzerOverrideFilter

            self._override_filter = FortianalyzerOverrideFilter(self._client)
        return self._override_filter

    @property
    def override_setting(self):
        """Access FortiAnalyzer override setting endpoint"""
        if not hasattr(self, "_override_setting"):
            from .fortianalyzer_override_setting import \
                FortianalyzerOverrideSetting

            self._override_setting = FortianalyzerOverrideSetting(self._client)
        return self._override_setting

    @property
    def setting(self):
        """Access FortiAnalyzer setting endpoint"""
        if not hasattr(self, "_setting"):
            from .fortianalyzer_setting import FortianalyzerSetting

            self._setting = FortianalyzerSetting(self._client)
        return self._setting


class _Fortianalyzer2:
    """FortiAnalyzer2 (secondary server) logging endpoints"""

    def __init__(self, client: "HTTPClient") -> None:
        self._client = client

    @property
    def filter(self):
        """Access FortiAnalyzer2 filter endpoint"""
        if not hasattr(self, "_filter"):
            from .fortianalyzer2_filter import Fortianalyzer2Filter

            self._filter = Fortianalyzer2Filter(self._client)
        return self._filter

    @property
    def override_filter(self):
        """Access FortiAnalyzer2 override filter endpoint"""
        if not hasattr(self, "_override_filter"):
            from .fortianalyzer2_override_filter import \
                Fortianalyzer2OverrideFilter

            self._override_filter = Fortianalyzer2OverrideFilter(self._client)
        return self._override_filter

    @property
    def override_setting(self):
        """Access FortiAnalyzer2 override setting endpoint"""
        if not hasattr(self, "_override_setting"):
            from .fortianalyzer2_override_setting import \
                Fortianalyzer2OverrideSetting

            self._override_setting = Fortianalyzer2OverrideSetting(self._client)
        return self._override_setting

    @property
    def setting(self):
        """Access FortiAnalyzer2 setting endpoint"""
        if not hasattr(self, "_setting"):
            from .fortianalyzer2_setting import Fortianalyzer2Setting

            self._setting = Fortianalyzer2Setting(self._client)
        return self._setting


class _Fortianalyzer3:
    """FortiAnalyzer3 (tertiary server) logging endpoints"""

    def __init__(self, client: "HTTPClient") -> None:
        self._client = client

    @property
    def filter(self):
        """Access FortiAnalyzer3 filter endpoint"""
        if not hasattr(self, "_filter"):
            from .fortianalyzer3_filter import Fortianalyzer3Filter

            self._filter = Fortianalyzer3Filter(self._client)
        return self._filter

    @property
    def override_filter(self):
        """Access FortiAnalyzer3 override filter endpoint"""
        if not hasattr(self, "_override_filter"):
            from .fortianalyzer3_override_filter import \
                Fortianalyzer3OverrideFilter

            self._override_filter = Fortianalyzer3OverrideFilter(self._client)
        return self._override_filter

    @property
    def override_setting(self):
        """Access FortiAnalyzer3 override setting endpoint"""
        if not hasattr(self, "_override_setting"):
            from .fortianalyzer3_override_setting import \
                Fortianalyzer3OverrideSetting

            self._override_setting = Fortianalyzer3OverrideSetting(self._client)
        return self._override_setting

    @property
    def setting(self):
        """Access FortiAnalyzer3 setting endpoint"""
        if not hasattr(self, "_setting"):
            from .fortianalyzer3_setting import Fortianalyzer3Setting

            self._setting = Fortianalyzer3Setting(self._client)
        return self._setting


class _Fortiguard:
    """FortiGuard/FortiCloud logging endpoints"""

    def __init__(self, client: "HTTPClient") -> None:
        self._client = client

    @property
    def filter(self):
        """Access FortiGuard filter endpoint"""
        if not hasattr(self, "_filter"):
            from .fortiguard_filter import FortiguardFilter

            self._filter = FortiguardFilter(self._client)
        return self._filter

    @property
    def override_filter(self):
        """Access FortiGuard override filter endpoint"""
        if not hasattr(self, "_override_filter"):
            from .fortiguard_override_filter import FortiguardOverrideFilter

            self._override_filter = FortiguardOverrideFilter(self._client)
        return self._override_filter

    @property
    def override_setting(self):
        """Access FortiGuard override setting endpoint"""
        if not hasattr(self, "_override_setting"):
            from .fortiguard_override_setting import FortiguardOverrideSetting

            self._override_setting = FortiguardOverrideSetting(self._client)
        return self._override_setting

    @property
    def setting(self):
        """Access FortiGuard setting endpoint"""
        if not hasattr(self, "_setting"):
            from .fortiguard_setting import FortiguardSetting

            self._setting = FortiguardSetting(self._client)
        return self._setting


class _Memory:
    """Memory logging endpoints"""

    def __init__(self, client: "HTTPClient") -> None:
        self._client = client

    @property
    def filter(self):
        """Access memory filter endpoint"""
        if not hasattr(self, "_filter"):
            from .memory_filter import MemoryFilter

            self._filter = MemoryFilter(self._client)
        return self._filter

    @property
    def global_setting(self):
        """Access memory global setting endpoint"""
        if not hasattr(self, "_global_setting"):
            from .memory_global_setting import MemoryGlobalSetting

            self._global_setting = MemoryGlobalSetting(self._client)
        return self._global_setting

    @property
    def setting(self):
        """Access memory setting endpoint"""
        if not hasattr(self, "_setting"):
            from .memory_setting import MemorySetting

            self._setting = MemorySetting(self._client)
        return self._setting


class _NullDevice:
    """Null device logging endpoints"""

    def __init__(self, client: "HTTPClient") -> None:
        self._client = client

    @property
    def filter(self):
        """Access null device filter endpoint"""
        if not hasattr(self, "_filter"):
            from .null_device_filter import NullDeviceFilter

            self._filter = NullDeviceFilter(self._client)
        return self._filter

    @property
    def setting(self):
        """Access null device setting endpoint"""
        if not hasattr(self, "_setting"):
            from .null_device_setting import NullDeviceSetting

            self._setting = NullDeviceSetting(self._client)
        return self._setting


class _Syslogd:
    """Syslogd (remote syslog server) logging endpoints"""

    def __init__(self, client: "HTTPClient") -> None:
        self._client = client

    @property
    def filter(self):
        """Access syslogd filter endpoint"""
        if not hasattr(self, "_filter"):
            from .syslogd_filter import SyslogdFilter

            self._filter = SyslogdFilter(self._client)
        return self._filter

    @property
    def override_filter(self):
        """Access syslogd override filter endpoint"""
        if not hasattr(self, "_override_filter"):
            from .syslogd_override_filter import SyslogdOverrideFilter

            self._override_filter = SyslogdOverrideFilter(self._client)
        return self._override_filter

    @property
    def override_setting(self):
        """Access syslogd override setting endpoint"""
        if not hasattr(self, "_override_setting"):
            from .syslogd_override_setting import SyslogdOverrideSetting

            self._override_setting = SyslogdOverrideSetting(self._client)
        return self._override_setting

    @property
    def setting(self):
        """Access syslogd setting endpoint"""
        if not hasattr(self, "_setting"):
            from .syslogd_setting import SyslogdSetting

            self._setting = SyslogdSetting(self._client)
        return self._setting


class _Syslogd2:
    """Syslogd2 (secondary remote syslog server) logging endpoints"""

    def __init__(self, client: "HTTPClient") -> None:
        self._client = client

    @property
    def filter(self):
        """Access syslogd2 filter endpoint"""
        if not hasattr(self, "_filter"):
            from .syslogd2_filter import Syslogd2Filter

            self._filter = Syslogd2Filter(self._client)
        return self._filter

    @property
    def override_filter(self):
        """Access syslogd2 override filter endpoint"""
        if not hasattr(self, "_override_filter"):
            from .syslogd2_override_filter import Syslogd2OverrideFilter

            self._override_filter = Syslogd2OverrideFilter(self._client)
        return self._override_filter

    @property
    def override_setting(self):
        """Access syslogd2 override setting endpoint"""
        if not hasattr(self, "_override_setting"):
            from .syslogd2_override_setting import Syslogd2OverrideSetting

            self._override_setting = Syslogd2OverrideSetting(self._client)
        return self._override_setting

    @property
    def setting(self):
        """Access syslogd2 setting endpoint"""
        if not hasattr(self, "_setting"):
            from .syslogd2_setting import Syslogd2Setting

            self._setting = Syslogd2Setting(self._client)
        return self._setting


class _Syslogd3:
    """Syslogd3 (tertiary remote syslog server) logging endpoints"""

    def __init__(self, client: "HTTPClient") -> None:
        self._client = client

    @property
    def filter(self):
        """Access syslogd3 filter endpoint"""
        if not hasattr(self, "_filter"):
            from .syslogd3_filter import Syslogd3Filter

            self._filter = Syslogd3Filter(self._client)
        return self._filter

    @property
    def override_filter(self):
        """Access syslogd3 override filter endpoint"""
        if not hasattr(self, "_override_filter"):
            from .syslogd3_override_filter import Syslogd3OverrideFilter

            self._override_filter = Syslogd3OverrideFilter(self._client)
        return self._override_filter

    @property
    def override_setting(self):
        """Access syslogd3 override setting endpoint"""
        if not hasattr(self, "_override_setting"):
            from .syslogd3_override_setting import Syslogd3OverrideSetting

            self._override_setting = Syslogd3OverrideSetting(self._client)
        return self._override_setting

    @property
    def setting(self):
        """Access syslogd3 setting endpoint"""
        if not hasattr(self, "_setting"):
            from .syslogd3_setting import Syslogd3Setting

            self._setting = Syslogd3Setting(self._client)
        return self._setting


class _Syslogd4:
    """Syslogd4 (fourth remote syslog server) logging endpoints"""

    def __init__(self, client: "HTTPClient") -> None:
        self._client = client

    @property
    def filter(self):
        """Access syslogd4 filter endpoint"""
        if not hasattr(self, "_filter"):
            from .syslogd4_filter import Syslogd4Filter

            self._filter = Syslogd4Filter(self._client)
        return self._filter

    @property
    def override_filter(self):
        """Access syslogd4 override filter endpoint"""
        if not hasattr(self, "_override_filter"):
            from .syslogd4_override_filter import Syslogd4OverrideFilter

            self._override_filter = Syslogd4OverrideFilter(self._client)
        return self._override_filter

    @property
    def override_setting(self):
        """Access syslogd4 override setting endpoint"""
        if not hasattr(self, "_override_setting"):
            from .syslogd4_override_setting import Syslogd4OverrideSetting

            self._override_setting = Syslogd4OverrideSetting(self._client)
        return self._override_setting

    @property
    def setting(self):
        """Access syslogd4 setting endpoint"""
        if not hasattr(self, "_setting"):
            from .syslogd4_setting import Syslogd4Setting

            self._setting = Syslogd4Setting(self._client)
        return self._setting


class _TacacsAccounting:
    """TACACS+ accounting logging endpoints"""

    def __init__(self, client: "HTTPClient") -> None:
        self._client = client

    @property
    def filter(self):
        """Access TACACS+ accounting filter endpoint"""
        if not hasattr(self, "_filter"):
            from .tacacs_accounting_filter import TacacsAccountingFilter

            self._filter = TacacsAccountingFilter(self._client)
        return self._filter

    @property
    def setting(self):
        """Access TACACS+ accounting setting endpoint"""
        if not hasattr(self, "_setting"):
            from .tacacs_accounting_setting import TacacsAccountingSetting

            self._setting = TacacsAccountingSetting(self._client)
        return self._setting


class _TacacsAccounting2:
    """TACACS+ accounting2 (secondary server) logging endpoints"""

    def __init__(self, client: "HTTPClient") -> None:
        self._client = client

    @property
    def filter(self):
        """Access TACACS+ accounting2 filter endpoint"""
        if not hasattr(self, "_filter"):
            from .tacacs_accounting2_filter import TacacsAccounting2Filter

            self._filter = TacacsAccounting2Filter(self._client)
        return self._filter

    @property
    def setting(self):
        """Access TACACS+ accounting2 setting endpoint"""
        if not hasattr(self, "_setting"):
            from .tacacs_accounting2_setting import TacacsAccounting2Setting

            self._setting = TacacsAccounting2Setting(self._client)
        return self._setting


class _TacacsAccounting3:
    """TACACS+ accounting3 (tertiary server) logging endpoints"""

    def __init__(self, client: "HTTPClient") -> None:
        self._client = client

    @property
    def filter(self):
        """Access TACACS+ accounting3 filter endpoint"""
        if not hasattr(self, "_filter"):
            from .tacacs_accounting3_filter import TacacsAccounting3Filter

            self._filter = TacacsAccounting3Filter(self._client)
        return self._filter

    @property
    def setting(self):
        """Access TACACS+ accounting3 setting endpoint"""
        if not hasattr(self, "_setting"):
            from .tacacs_accounting3_setting import TacacsAccounting3Setting

            self._setting = TacacsAccounting3Setting(self._client)
        return self._setting


class _Webtrends:
    """WebTrends logging endpoints"""

    def __init__(self, client: "HTTPClient") -> None:
        self._client = client

    @property
    def filter(self):
        """Access WebTrends filter endpoint"""
        if not hasattr(self, "_filter"):
            from .webtrends_filter import WebtrendsFilter

            self._filter = WebtrendsFilter(self._client)
        return self._filter

    @property
    def setting(self):
        """Access WebTrends setting endpoint"""
        if not hasattr(self, "_setting"):
            from .webtrends_setting import WebtrendsSetting

            self._setting = WebtrendsSetting(self._client)
        return self._setting


class Log:
    """Log API endpoints"""

    def __init__(self, client: "HTTPClient") -> None:
        self._client = client

    @property
    def disk(self):
        """Access disk logging endpoints"""
        if not hasattr(self, "_disk"):
            self._disk = _Disk(self._client)
        return self._disk

    @property
    def fortianalyzer_cloud(self):
        """Access FortiAnalyzer Cloud logging endpoints"""
        if not hasattr(self, "_fortianalyzer_cloud"):
            self._fortianalyzer_cloud = _FortianalyzerCloud(self._client)
        return self._fortianalyzer_cloud

    @property
    def fortianalyzer(self):
        """Access FortiAnalyzer logging endpoints"""
        if not hasattr(self, "_fortianalyzer"):
            self._fortianalyzer = _Fortianalyzer(self._client)
        return self._fortianalyzer

    @property
    def fortianalyzer2(self):
        """Access FortiAnalyzer2 (secondary) logging endpoints"""
        if not hasattr(self, "_fortianalyzer2"):
            self._fortianalyzer2 = _Fortianalyzer2(self._client)
        return self._fortianalyzer2

    @property
    def fortianalyzer3(self):
        """Access FortiAnalyzer3 (tertiary) logging endpoints"""
        if not hasattr(self, "_fortianalyzer3"):
            self._fortianalyzer3 = _Fortianalyzer3(self._client)
        return self._fortianalyzer3

    @property
    def fortiguard(self):
        """Access FortiGuard/FortiCloud logging endpoints"""
        if not hasattr(self, "_fortiguard"):
            self._fortiguard = _Fortiguard(self._client)
        return self._fortiguard

    @property
    def memory(self):
        """Access memory logging endpoints"""
        if not hasattr(self, "_memory"):
            self._memory = _Memory(self._client)
        return self._memory

    @property
    def null_device(self):
        """Access null device logging endpoints"""
        if not hasattr(self, "_null_device"):
            self._null_device = _NullDevice(self._client)
        return self._null_device

    @property
    def syslogd(self):
        """Access syslogd (remote syslog server) logging endpoints"""
        if not hasattr(self, "_syslogd"):
            self._syslogd = _Syslogd(self._client)
        return self._syslogd

    @property
    def syslogd2(self):
        """Access syslogd2 (secondary remote syslog server) logging endpoints"""
        if not hasattr(self, "_syslogd2"):
            self._syslogd2 = _Syslogd2(self._client)
        return self._syslogd2

    @property
    def syslogd3(self):
        """Access syslogd3 (tertiary remote syslog server) logging endpoints"""
        if not hasattr(self, "_syslogd3"):
            self._syslogd3 = _Syslogd3(self._client)
        return self._syslogd3

    @property
    def syslogd4(self):
        """Access syslogd4 (fourth remote syslog server) logging endpoints"""
        if not hasattr(self, "_syslogd4"):
            self._syslogd4 = _Syslogd4(self._client)
        return self._syslogd4

    @property
    def tacacs_accounting(self):
        """Access TACACS+ accounting logging endpoints"""
        if not hasattr(self, "_tacacs_accounting"):
            self._tacacs_accounting = _TacacsAccounting(self._client)
        return self._tacacs_accounting

    @property
    def tacacs_accounting2(self):
        """Access TACACS+ accounting2 (secondary server) logging endpoints"""
        if not hasattr(self, "_tacacs_accounting2"):
            self._tacacs_accounting2 = _TacacsAccounting2(self._client)
        return self._tacacs_accounting2

    @property
    def tacacs_accounting3(self):
        """Access TACACS+ accounting3 (tertiary server) logging endpoints"""
        if not hasattr(self, "_tacacs_accounting3"):
            self._tacacs_accounting3 = _TacacsAccounting3(self._client)
        return self._tacacs_accounting3

    @property
    def webtrends(self):
        """Access WebTrends logging endpoints"""
        if not hasattr(self, "_webtrends"):
            self._webtrends = _Webtrends(self._client)
        return self._webtrends

    @property
    def custom_field(self):
        """Access custom log fields endpoint"""
        if not hasattr(self, "_custom_field"):
            from .custom_field import CustomField

            self._custom_field = CustomField(self._client)
        return self._custom_field

    @property
    def eventfilter(self):
        """Access log event filter endpoint"""
        if not hasattr(self, "_eventfilter"):
            from .eventfilter import Eventfilter

            self._eventfilter = Eventfilter(self._client)
        return self._eventfilter

    @property
    def gui_display(self):
        """Access log GUI display settings endpoint"""
        if not hasattr(self, "_gui_display"):
            from .gui_display import GuiDisplay

            self._gui_display = GuiDisplay(self._client)
        return self._gui_display

    @property
    def setting(self):
        """Access general log settings endpoint"""
        if not hasattr(self, "_setting"):
            from .setting import Setting

            self._setting = Setting(self._client)
        return self._setting

    @property
    def threat_weight(self):
        """Access threat weight settings endpoint"""
        if not hasattr(self, "_threat_weight"):
            from .threat_weight import ThreatWeight

            self._threat_weight = ThreatWeight(self._client)
        return self._threat_weight
