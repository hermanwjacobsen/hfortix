"""
FortiOS Monitor - Log
Log device operations and management
"""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ....http_client import HTTPClient

__all__ = ["Log"]

from .av_archive import AvArchive
from .current_disk_usage import CurrentDiskUsage
from .device import Device
from .feature_set import FeatureSet
from .fortianalyzer import Fortianalyzer
from .fortianalyzer_queue import FortianalyzerQueue
from .forticloud import Forticloud
from .forticloud_report import ForticloudReport
from .forticloud_report_list import ForticloudReportList
from .historic_daily_remote_logs import HistoricDailyRemoteLogs
from .hourly_disk_usage import HourlyDiskUsage
from .local_report import LocalReport
from .local_report_list import LocalReportList
from .policy_archive import PolicyArchive
from .stats import Stats


class Log:
    """Log Monitor category class"""

    def __init__(self, client: "HTTPClient") -> None:
        """
        Initialize Log Monitor category

        Args:
            client: HTTPClient instance
        """
        self._client = client

        # Initialize endpoints
        self.av_archive = AvArchive(client)
        self.current_disk_usage = CurrentDiskUsage(client)
        self.device = Device(client)
        self.feature_set = FeatureSet(client)
        self.fortianalyzer = Fortianalyzer(client)
        self.fortianalyzer_queue = FortianalyzerQueue(client)
        self.forticloud = Forticloud(client)
        self.forticloud_report = ForticloudReport(client)
        self.forticloud_report_list = ForticloudReportList(client)
        self.historic_daily_remote_logs = HistoricDailyRemoteLogs(client)
        self.hourly_disk_usage = HourlyDiskUsage(client)
        self.local_report = LocalReport(client)
        self.local_report_list = LocalReportList(client)
        self.policy_archive = PolicyArchive(client)
        self.stats = Stats(client)

    def __dir__(self):
        """Control autocomplete to show only public attributes"""
        return [
            "av_archive",
            "current_disk_usage",
            "device",
            "feature_set",
            "fortianalyzer",
            "fortianalyzer_queue",
            "forticloud",
            "forticloud_report",
            "forticloud_report_list",
            "historic_daily_remote_logs",
            "hourly_disk_usage",
            "local_report",
            "local_report_list",
            "policy_archive",
            "stats"
        ]
