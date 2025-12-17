"""
FortiOS CMDB - Log FortiAnalyzer Cloud Setting

Settings for FortiAnalyzer Cloud.

API Endpoints:
    GET  /api/v2/cmdb/log.fortianalyzer-cloud/setting  - Get configuration
    PUT  /api/v2/cmdb/log.fortianalyzer-cloud/setting  - Update configuration
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional, Union

if TYPE_CHECKING:
    from ...http_client import HTTPClient


class FortianalyzerCloudSetting:
    """Log FortiAnalyzer Cloud Setting endpoint (singleton)"""

    def __init__(self, client: "HTTPClient") -> None:
        self._client = client

    def get(self, vdom: Optional[Union[str, bool]] = None, **kwargs: Any) -> dict[str, Any]:
        """
        Get FortiAnalyzer Cloud settings.

        Args:
            vdom: Virtual domain name or False for global
            **kwargs: Additional parameters

        Returns:
            Dictionary containing FortiAnalyzer Cloud settings

        Examples:
            >>> settings = fgt.api.cmdb.log.fortianalyzer_cloud_setting.get()
        """
        path = "log.fortianalyzer-cloud/setting"
        return self._client.get("cmdb", path, params=kwargs if kwargs else None, vdom=vdom)

    def put(
        self,
        data_dict: Optional[dict[str, Any]] = None,
        status: Optional[str] = None,
        ips_archive: Optional[str] = None,
        upload_option: Optional[str] = None,
        upload_interval: Optional[str] = None,
        upload_day: Optional[str] = None,
        upload_time: Optional[str] = None,
        priority: Optional[str] = None,
        max_log_rate: Optional[int] = None,
        access_config: Optional[str] = None,
        enc_algorithm: Optional[str] = None,
        ssl_min_proto_version: Optional[str] = None,
        certificate: Optional[str] = None,
        certificate_verification: Optional[str] = None,
        serial: Optional[list[dict[str, Any]]] = None,
        preshared_key: Optional[str] = None,
        interface_select_method: Optional[str] = None,
        interface: Optional[str] = None,
        source_ip: Optional[str] = None,
        hmac_algorithm: Optional[str] = None,
        conn_timeout: Optional[int] = None,
        monitor_keepalive_period: Optional[int] = None,
        monitor_failure_retry_period: Optional[int] = None,
        vrf_select: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Update FortiAnalyzer Cloud settings.

        Args:
            data_dict: Complete configuration dictionary
            status: Enable/disable FortiAnalyzer Cloud logging (enable|disable)
            ips_archive: Enable/disable IPS packet archiving (enable|disable)
            upload_option: Configure log upload schedule (store-and-upload|realtime|1-minute|5-minute)
            upload_interval: Frequency of scheduled upload (daily|weekly|monthly)
            upload_day: Day of week or month for scheduled upload (sunday|monday|tuesday|wednesday|thursday|friday|saturday|1-31)
            upload_time: Time of day for scheduled upload (hh:mm)
            priority: Priority for FortiAnalyzer Cloud connection (default|low)
            max_log_rate: Maximum log rate in megabits per second (0-100000, 0=unlimited)
            access_config: Enable/disable access to FortiAnalyzer Cloud config synchronization (enable|disable)
            enc_algorithm: Enable/disable cloud communication encryption (default|high|low|disable)
            ssl_min_proto_version: Minimum supported SSL/TLS protocol version (default|TLSv1-1|TLSv1-2|SSLv3|TLSv1)
            certificate: Certificate for cloud authentication (string)
            certificate_verification: Enable/disable identity verification of FortiAnalyzer Cloud (enable|disable)
            serial: Serial number of FortiAnalyzer Cloud (list of serial objects)
            preshared_key: Preshared key for cloud authentication (string)
            interface_select_method: Source interface selection method (auto|sdwan|specify)
            interface: Source interface for cloud connection (string)
            source_ip: Source IP address for cloud connection (string)
            hmac_algorithm: HMAC algorithm for authentication (sha256|sha1)
            conn_timeout: Connection timeout in seconds (1-3600)
            monitor_keepalive_period: Time between keepalive requests in seconds (1-120)
            monitor_failure_retry_period: Time between connection retries in seconds (1-86400)
            vrf_select: VRF selection for cloud connection (string)
            vdom: Virtual domain name or False for global
            **kwargs: Additional parameters

        Returns:
            Dictionary containing update result

        Examples:
            >>> # Enable FortiAnalyzer Cloud with basic settings
            >>> fgt.api.cmdb.log.fortianalyzer_cloud_setting.update(
            ...     status='enable',
            ...     upload_option='realtime'
            ... )

            >>> # Configure scheduled upload with encryption
            >>> fgt.api.cmdb.log.fortianalyzer_cloud_setting.update(
            ...     status='enable',
            ...     upload_option='store-and-upload',
            ...     upload_interval='daily',
            ...     upload_time='02:00',
            ...     enc_algorithm='high',
            ...     ssl_min_proto_version='TLSv1-2'
            ... )

            >>> # Configure with certificate verification
            >>> fgt.api.cmdb.log.fortianalyzer_cloud_setting.update(
            ...     certificate_verification='enable',
            ...     certificate='Fortinet_CA',
            ...     hmac_algorithm='sha256'
            ... )
        """
        data = data_dict.copy() if data_dict else {}

        param_map = {
            "status": status,
            "ips-archive": ips_archive,
            "upload-option": upload_option,
            "upload-interval": upload_interval,
            "upload-day": upload_day,
            "upload-time": upload_time,
            "priority": priority,
            "max-log-rate": max_log_rate,
            "access-config": access_config,
            "enc-algorithm": enc_algorithm,
            "ssl-min-proto-version": ssl_min_proto_version,
            "certificate": certificate,
            "certificate-verification": certificate_verification,
            "serial": serial,
            "preshared-key": preshared_key,
            "interface-select-method": interface_select_method,
            "interface": interface,
            "source-ip": source_ip,
            "hmac-algorithm": hmac_algorithm,
            "conn-timeout": conn_timeout,
            "monitor-keepalive-period": monitor_keepalive_period,
            "monitor-failure-retry-period": monitor_failure_retry_period,
            "vrf-select": vrf_select,
        }

        for key, value in param_map.items():
            if value is not None:
                data[key] = value

        data.update(kwargs)

        path = "log.fortianalyzer-cloud/setting"
        return self._client.put("cmdb", path, data=data, vdom=vdom)
