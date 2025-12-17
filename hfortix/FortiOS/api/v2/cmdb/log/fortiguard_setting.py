"""
FortiOS CMDB - Log FortiGuard Setting

Configure logging to FortiCloud.

API Endpoints:
    GET /api/v2/cmdb/log.fortiguard/setting - Get FortiGuard settings
    PUT /api/v2/cmdb/log.fortiguard/setting - Update FortiGuard settings
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional, Union

if TYPE_CHECKING:
    from ...http_client import HTTPClient


class FortiguardSetting:
    """Log FortiGuard Setting endpoint (singleton)"""

    def __init__(self, client: "HTTPClient") -> None:
        self._client = client

    def get(self, vdom: Optional[Union[str, bool]] = None, **kwargs: Any) -> dict[str, Any]:
        """
        Get FortiGuard settings.

        Args:
            vdom: Virtual domain name or False for global
            **kwargs: Additional parameters

        Returns:
            Dictionary containing FortiGuard settings

        Examples:
            >>> settings = fgt.api.cmdb.log.fortiguard_setting.get()
        """
        path = "log.fortiguard/setting"
        return self._client.get("cmdb", path, params=kwargs if kwargs else None, vdom=vdom)

    def update(
        self,
        data_dict: Optional[dict[str, Any]] = None,
        status: Optional[str] = None,
        upload_option: Optional[str] = None,
        upload_interval: Optional[str] = None,
        upload_day: Optional[str] = None,
        upload_time: Optional[str] = None,
        priority: Optional[str] = None,
        max_log_rate: Optional[int] = None,
        access_config: Optional[str] = None,
        enc_algorithm: Optional[str] = None,
        ssl_min_proto_version: Optional[str] = None,
        conn_timeout: Optional[int] = None,
        interface_select_method: Optional[str] = None,
        interface: Optional[str] = None,
        source_ip: Optional[str] = None,
        vrf_select: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Update FortiGuard settings for FortiCloud logging.

        Args:
            data_dict: Complete configuration dictionary
            status: Enable/disable FortiGuard logging (enable|disable)
            upload_option: Configure log upload schedule (store-and-upload|realtime|1-minute|5-minute)
            upload_interval: Frequency of scheduled upload (daily|weekly|monthly)
            upload_day: Day of week or month for scheduled upload (sunday|monday|tuesday|wednesday|thursday|friday|saturday|1-31)
            upload_time: Time of day for scheduled upload (hh:mm)
            priority: Priority for FortiGuard connection (default|low)
            max_log_rate: Maximum log rate in megabits per second (0-100000, 0=unlimited)
            access_config: Enable/disable access to FortiGuard config synchronization (enable|disable)
            enc_algorithm: Enable/disable FortiCloud communication encryption (default|high|low|disable)
            ssl_min_proto_version: Minimum supported SSL/TLS protocol version (default|TLSv1-1|TLSv1-2|SSLv3|TLSv1)
            conn_timeout: Connection timeout in seconds (1-3600)
            interface_select_method: Source interface selection method (auto|sdwan|specify)
            interface: Source interface for FortiCloud connection (string)
            source_ip: Source IP address for FortiCloud connection (string)
            vrf_select: VRF selection for FortiCloud connection (string)
            vdom: Virtual domain name or False for global
            **kwargs: Additional parameters

        Returns:
            Dictionary containing update result

        Examples:
            >>> # Enable FortiGuard with basic settings
            >>> fgt.api.cmdb.log.fortiguard_setting.update(
            ...     status='enable',
            ...     upload_option='realtime'
            ... )

            >>> # Configure scheduled upload with encryption
            >>> fgt.api.cmdb.log.fortiguard_setting.update(
            ...     status='enable',
            ...     upload_option='store-and-upload',
            ...     upload_interval='daily',
            ...     upload_time='02:00',
            ...     enc_algorithm='high',
            ...     ssl_min_proto_version='TLSv1-2'
            ... )
        """
        data = data_dict.copy() if data_dict else {}

        param_map = {
            "status": status,
            "upload-option": upload_option,
            "upload-interval": upload_interval,
            "upload-day": upload_day,
            "upload-time": upload_time,
            "priority": priority,
            "max-log-rate": max_log_rate,
            "access-config": access_config,
            "enc-algorithm": enc_algorithm,
            "ssl-min-proto-version": ssl_min_proto_version,
            "conn-timeout": conn_timeout,
            "interface-select-method": interface_select_method,
            "interface": interface,
            "source-ip": source_ip,
            "vrf-select": vrf_select,
        }

        for key, value in param_map.items():
            if value is not None:
                data[key] = value

        data.update(kwargs)

        path = "log.fortiguard/setting"
        return self._client.put("cmdb", path, data=data, vdom=vdom)
