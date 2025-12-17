"""
FortiOS CMDB - Log FortiAnalyzer Setting

Global FortiAnalyzer settings.

API Endpoints:
    GET  /api/v2/cmdb/log.fortianalyzer/setting  - Get configuration
    PUT  /api/v2/cmdb/log.fortianalyzer/setting  - Update configuration
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional, Union

if TYPE_CHECKING:
    from ...http_client import HTTPClient


class FortianalyzerSetting:
    """Log FortiAnalyzer Setting endpoint (singleton)"""

    def __init__(self, client: "HTTPClient") -> None:
        self._client = client

    def get(self, vdom: Optional[Union[str, bool]] = None, **kwargs: Any) -> dict[str, Any]:
        """
        Get FortiAnalyzer settings.

        Args:
            vdom: Virtual domain name or False for global
            **kwargs: Additional parameters

        Returns:
            Dictionary containing FortiAnalyzer settings

        Examples:
            >>> settings = fgt.api.cmdb.log.fortianalyzer_setting.get()
        """
        path = "log.fortianalyzer/setting"
        return self._client.get("cmdb", path, params=kwargs if kwargs else None, vdom=vdom)

    def put(
        self,
        data_dict: Optional[dict[str, Any]] = None,
        status: Optional[str] = None,
        certificate: Optional[str] = None,
        server: Optional[str] = None,
        alt_server: Optional[str] = None,
        fallback_to_primary: Optional[str] = None,
        certificate_verification: Optional[str] = None,
        server_cert_ca: Optional[str] = None,
        serial: Optional[list[dict[str, Any]]] = None,
        preshared_key: Optional[str] = None,
        access_config: Optional[str] = None,
        hmac_algorithm: Optional[str] = None,
        enc_algorithm: Optional[str] = None,
        ssl_min_proto_version: Optional[str] = None,
        conn_timeout: Optional[int] = None,
        monitor_keepalive_period: Optional[int] = None,
        monitor_failure_retry_period: Optional[int] = None,
        reliable: Optional[str] = None,
        priority: Optional[str] = None,
        max_log_rate: Optional[int] = None,
        interface_select_method: Optional[str] = None,
        interface: Optional[str] = None,
        source_ip: Optional[str] = None,
        upload_option: Optional[str] = None,
        upload_interval: Optional[str] = None,
        upload_day: Optional[str] = None,
        upload_time: Optional[str] = None,
        ips_archive: Optional[str] = None,
        vrf_select: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Update FortiAnalyzer settings.

        Args:
            data_dict: Complete configuration dictionary
            status: Enable/disable FortiAnalyzer logging (enable|disable)
            certificate: Certificate for FortiAnalyzer authentication (string)
            server: FortiAnalyzer server IP address or FQDN (string)
            alt_server: Alternative FortiAnalyzer server IP address or FQDN (string)
            fallback_to_primary: Enable/disable fallback to primary server (enable|disable)
            certificate_verification: Enable/disable identity verification of FortiAnalyzer (enable|disable)
            server_cert_ca: Server certificate CA for verification (string)
            serial: Serial number of FortiAnalyzer (list of serial objects)
            preshared_key: Preshared key for authentication (string)
            access_config: Enable/disable access to FortiAnalyzer config synchronization (enable|disable)
            hmac_algorithm: HMAC algorithm for authentication (sha256|sha1)
            enc_algorithm: Enable/disable communication encryption (default|high|low|disable)
            ssl_min_proto_version: Minimum supported SSL/TLS protocol version (default|TLSv1-1|TLSv1-2|SSLv3|TLSv1)
            conn_timeout: Connection timeout in seconds (1-3600)
            monitor_keepalive_period: Time between keepalive requests in seconds (1-120)
            monitor_failure_retry_period: Time between connection retries in seconds (1-86400)
            reliable: Enable/disable reliable logging to FortiAnalyzer (enable|disable)
            priority: Priority for FortiAnalyzer connection (default|low)
            max_log_rate: Maximum log rate in megabits per second (0-100000, 0=unlimited)
            interface_select_method: Source interface selection method (auto|sdwan|specify)
            interface: Source interface for FortiAnalyzer connection (string)
            source_ip: Source IP address for FortiAnalyzer connection (string)
            upload_option: Configure log upload schedule (store-and-upload|realtime|1-minute|5-minute)
            upload_interval: Frequency of scheduled upload (daily|weekly|monthly)
            upload_day: Day of week or month for scheduled upload (sunday|monday|tuesday|wednesday|thursday|friday|saturday|1-31)
            upload_time: Time of day for scheduled upload (hh:mm)
            ips_archive: Enable/disable IPS packet archiving (enable|disable)
            vrf_select: VRF selection for FortiAnalyzer connection (string)
            vdom: Virtual domain name or False for global
            **kwargs: Additional parameters

        Returns:
            Dictionary containing update result

        Examples:
            >>> # Enable FortiAnalyzer with basic settings
            >>> fgt.api.cmdb.log.fortianalyzer_setting.update(
            ...     status='enable',
            ...     server='192.168.1.100',
            ...     upload_option='realtime'
            ... )

            >>> # Configure with encryption and certificate verification
            >>> fgt.api.cmdb.log.fortianalyzer_setting.update(
            ...     status='enable',
            ...     server='faz.example.com',
            ...     certificate_verification='enable',
            ...     enc_algorithm='high',
            ...     ssl_min_proto_version='TLSv1-2',
            ...     hmac_algorithm='sha256'
            ... )

            >>> # Configure scheduled upload
            >>> fgt.api.cmdb.log.fortianalyzer_setting.update(
            ...     upload_option='store-and-upload',
            ...     upload_interval='daily',
            ...     upload_time='02:00'
            ... )
        """
        data = data_dict.copy() if data_dict else {}

        param_map = {
            "status": status,
            "certificate": certificate,
            "server": server,
            "alt-server": alt_server,
            "fallback-to-primary": fallback_to_primary,
            "certificate-verification": certificate_verification,
            "server-cert-ca": server_cert_ca,
            "serial": serial,
            "preshared-key": preshared_key,
            "access-config": access_config,
            "hmac-algorithm": hmac_algorithm,
            "enc-algorithm": enc_algorithm,
            "ssl-min-proto-version": ssl_min_proto_version,
            "conn-timeout": conn_timeout,
            "monitor-keepalive-period": monitor_keepalive_period,
            "monitor-failure-retry-period": monitor_failure_retry_period,
            "reliable": reliable,
            "priority": priority,
            "max-log-rate": max_log_rate,
            "interface-select-method": interface_select_method,
            "interface": interface,
            "source-ip": source_ip,
            "upload-option": upload_option,
            "upload-interval": upload_interval,
            "upload-day": upload_day,
            "upload-time": upload_time,
            "ips-archive": ips_archive,
            "vrf-select": vrf_select,
        }

        for key, value in param_map.items():
            if value is not None:
                data[key] = value

        data.update(kwargs)

        path = "log.fortianalyzer/setting"
        return self._client.put("cmdb", path, data=data, vdom=vdom)
