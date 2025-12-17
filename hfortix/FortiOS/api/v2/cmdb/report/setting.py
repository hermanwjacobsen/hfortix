"""
Report setting endpoint module.

This module provides access to the report/setting endpoint
for configuring general report settings.

API Path: report/setting
"""

from typing import TYPE_CHECKING, Any, Dict, Optional

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client import HTTPClient


class Setting:
    """
    Interface for configuring report settings.

    This class provides methods to manage general report settings.
    This is a singleton endpoint (GET/PUT only).

    Example usage:
        # Get current report settings
        settings = fgt.api.cmdb.report.setting.get()

        # Update report settings
        fgt.api.cmdb.report.setting.update(
            pdf_report='enable',
            report_source='forward-traffic'
        )
    """

    def __init__(self, client: "HTTPClient") -> None:
        """
        Initialize the Setting instance.

        Args:
            client: The HTTP client used to communicate with the FortiOS device
        """
        self._client = client
        self._endpoint = "report/setting"

    def get(self) -> Dict[str, Any]:
        """
        Retrieve current report settings.

        Returns:
            Dictionary containing report settings

        Example:
            >>> result = fgt.api.cmdb.report.setting.get()
            >>> print(result['pdf-report'])
            'enable'
        """
        return self._client.get("cmdb", self._endpoint)

    def update(
        self,
        data_dict: Optional[Dict[str, Any]] = None,
        fortiview: Optional[str] = None,
        pdf_report: Optional[str] = None,
        report_source: Optional[str] = None,
        top_n: Optional[int] = None,
        web_browsing_threshold: Optional[int] = None,
        **kwargs: Any,
    ) -> Dict[str, Any]:
        """
        Update report settings.

        Args:
            data_dict: Dictionary with API format parameters
            fortiview: Enable/disable FortiView (enable | disable)
            pdf_report: Enable/disable PDF report (enable | disable)
            report_source: Report source (forward-traffic | sniffer-traffic | local-deny-traffic)
            top_n: Number of top items to display
            web_browsing_threshold: Web browsing threshold
            **kwargs: Additional parameters

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.cmdb.report.setting.update(
            ...     pdf_report='enable',
            ...     report_source='forward-traffic',
            ...     top_n=100
            ... )
        """
        payload = dict(data_dict) if data_dict else {}

        param_map = {
            "fortiview": "fortiview",
            "pdf_report": "pdf-report",
            "report_source": "report-source",
            "top_n": "top-n",
            "web_browsing_threshold": "web-browsing-threshold",
        }

        for py_name, api_name in param_map.items():
            value = locals().get(py_name)
            if value is not None:
                payload[api_name] = value

        payload.update(kwargs)

        return self._client.put("cmdb", self._endpoint, data=payload)
