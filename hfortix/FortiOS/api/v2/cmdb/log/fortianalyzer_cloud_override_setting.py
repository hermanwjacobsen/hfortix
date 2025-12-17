"""
FortiOS CMDB - Log FortiAnalyzer Cloud Override Setting

Override settings for FortiAnalyzer Cloud in VDOMs.

API Endpoints:
    GET /api/v2/cmdb/log.fortianalyzer-cloud/override-setting - Get FortiAnalyzer Cloud override setting
    PUT /api/v2/cmdb/log.fortianalyzer-cloud/override-setting - Update FortiAnalyzer Cloud override setting
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional, Union

if TYPE_CHECKING:
    from ...http_client import HTTPClient


class FortianalyzerCloudOverrideSetting:
    """Log FortiAnalyzer Cloud Override Setting endpoint (singleton)"""

    def __init__(self, client: "HTTPClient") -> None:
        self._client = client

    def get(self, vdom: Optional[Union[str, bool]] = None, **kwargs: Any) -> dict[str, Any]:
        """
        Get FortiAnalyzer Cloud override setting.

        Args:
            vdom: Virtual domain name or False for global
            **kwargs: Additional parameters

        Returns:
            Dictionary containing FortiAnalyzer Cloud override setting

        Examples:
            >>> settings = fgt.api.cmdb.log.fortianalyzer_cloud_override_setting.get()
        """
        path = "log.fortianalyzer-cloud/override-setting"
        return self._client.get("cmdb", path, params=kwargs if kwargs else None, vdom=vdom)

    def put(
        self,
        data_dict: Optional[dict[str, Any]] = None,
        status: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Update FortiAnalyzer Cloud override setting.

        Args:
            data_dict: Complete configuration dictionary
            status: Enable/disable override of global settings (enable|disable)
            vdom: Virtual domain name or False for global
            **kwargs: Additional parameters

        Returns:
            Dictionary containing update result

        Examples:
            >>> # Enable VDOM-specific override
            >>> fgt.api.cmdb.log.fortianalyzer_cloud_override_setting.update(
            ...     status='enable',
            ...     vdom='vdom1'
            ... )

            >>> # Disable override
            >>> fgt.api.cmdb.log.fortianalyzer_cloud_override_setting.update(status='disable')
        """
        data = data_dict.copy() if data_dict else {}

        if status is not None:
            data["status"] = status

        data.update(kwargs)

        path = "log.fortianalyzer-cloud/override-setting"
        return self._client.put("cmdb", path, data=data, vdom=vdom)
