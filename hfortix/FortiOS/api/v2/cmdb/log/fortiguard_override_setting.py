"""
FortiOS CMDB - Log FortiGuard Override Setting

Override global FortiCloud logging settings for VDOMs.

API Endpoints:
    GET  /api/v2/cmdb/log.fortiguard/override-setting  - Get configuration
    PUT  /api/v2/cmdb/log.fortiguard/override-setting  - Update configuration
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional, Union

if TYPE_CHECKING:
    from ...http_client import HTTPClient


class FortiguardOverrideSetting:
    """Log FortiGuard Override Setting endpoint (singleton)"""

    def __init__(self, client: "HTTPClient") -> None:
        self._client = client

    def get(self, vdom: Optional[Union[str, bool]] = None, **kwargs: Any) -> dict[str, Any]:
        """
        Get FortiGuard override settings.

        Args:
            vdom: Virtual domain name or False for global
            **kwargs: Additional parameters

        Returns:
            Dictionary containing FortiGuard override settings

        Examples:
            >>> settings = fgt.api.cmdb.log.fortiguard_override_setting.get()
        """
        path = "log.fortiguard/override-setting"
        return self._client.get("cmdb", path, params=kwargs if kwargs else None, vdom=vdom)

    def put(
        self,
        data_dict: Optional[dict[str, Any]] = None,
        override: Optional[str] = None,
        status: Optional[str] = None,
        upload_option: Optional[str] = None,
        upload_interval: Optional[str] = None,
        upload_day: Optional[str] = None,
        upload_time: Optional[str] = None,
        priority: Optional[str] = None,
        max_log_rate: Optional[int] = None,
        access_config: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Update FortiGuard override settings for VDOM-specific FortiCloud configuration.

        Args:
            data_dict: Complete configuration dictionary
            override: Enable/disable override (enable|disable)
            status: Enable/disable FortiGuard logging (enable|disable)
            upload_option: Configure log upload schedule (store-and-upload|realtime|1-minute|5-minute)
            upload_interval: Frequency of scheduled upload (daily|weekly|monthly)
            upload_day: Day of week or month for scheduled upload (sunday|monday|tuesday|wednesday|thursday|friday|saturday|1-31)
            upload_time: Time of day for scheduled upload (hh:mm)
            priority: Priority for FortiGuard connection (default|low)
            max_log_rate: Maximum log rate in megabits per second (0-100000, 0=unlimited)
            access_config: Enable/disable access to FortiGuard config synchronization (enable|disable)
            vdom: Virtual domain name or False for global
            **kwargs: Additional parameters

        Returns:
            Dictionary containing update result

        Examples:
            >>> # Enable VDOM-specific FortiGuard override
            >>> fgt.api.cmdb.log.fortiguard_override_setting.update(
            ...     override='enable',
            ...     status='enable',
            ...     upload_option='realtime',
            ...     vdom='vdom1'
            ... )
        """
        data = data_dict.copy() if data_dict else {}

        param_map = {
            "override": override,
            "status": status,
            "upload-option": upload_option,
            "upload-interval": upload_interval,
            "upload-day": upload_day,
            "upload-time": upload_time,
            "priority": priority,
            "max-log-rate": max_log_rate,
            "access-config": access_config,
        }

        for key, value in param_map.items():
            if value is not None:
                data[key] = value

        data.update(kwargs)

        path = "log.fortiguard/override-setting"
        return self._client.put("cmdb", path, data=data, vdom=vdom)
