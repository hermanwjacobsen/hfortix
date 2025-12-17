"""
FortiOS CMDB - Log FortiAnalyzer2 Override Setting

Override settings for FortiAnalyzer (secondary server) in VDOMs.

API Endpoints:
    GET /api/v2/cmdb/log.fortianalyzer2/override-setting - Get FortiAnalyzer2 override settings
    PUT /api/v2/cmdb/log.fortianalyzer2/override-setting - Update FortiAnalyzer2 override settings
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional, Union

if TYPE_CHECKING:
    from ...http_client import HTTPClient


class Fortianalyzer2OverrideSetting:
    """Log FortiAnalyzer2 Override Setting endpoint (singleton)"""

    def __init__(self, client: "HTTPClient") -> None:
        self._client = client

    def get(self, vdom: Optional[Union[str, bool]] = None, **kwargs: Any) -> dict[str, Any]:
        """
        Get FortiAnalyzer2 override settings.

        Args:
            vdom: Virtual domain name or False for global
            **kwargs: Additional parameters

        Returns:
            Dictionary containing FortiAnalyzer2 override settings

        Examples:
            >>> settings = fgt.api.cmdb.log.fortianalyzer2_override_setting.get()
        """
        path = "log.fortianalyzer2/override-setting"
        return self._client.get("cmdb", path, params=kwargs if kwargs else None, vdom=vdom)

    def update(
        self,
        data_dict: Optional[dict[str, Any]] = None,
        status: Optional[str] = None,
        override: Optional[str] = None,
        use_management_vdom: Optional[str] = None,
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
        Update FortiAnalyzer2 override settings for VDOM-specific configuration.

        Args:
            data_dict: Complete configuration dictionary
            status: Enable/disable FortiAnalyzer2 logging (enable|disable)
            override: Enable/disable override (enable|disable)
            use_management_vdom: Enable/disable use of management VDOM (enable|disable)
            certificate: Certificate for authentication (string)
            server: FortiAnalyzer2 server IP address or FQDN (string)
            alt_server: Alternative server IP address or FQDN (string)
            fallback_to_primary: Enable/disable fallback to primary server (enable|disable)
            certificate_verification: Enable/disable identity verification (enable|disable)
            server_cert_ca: Server certificate CA (string)
            serial: Serial number (list of serial objects)
            preshared_key: Preshared key (string)
            access_config: Enable/disable config synchronization (enable|disable)
            hmac_algorithm: HMAC algorithm (sha256|sha1)
            enc_algorithm: Communication encryption (default|high|low|disable)
            ssl_min_proto_version: Minimum SSL/TLS version (default|TLSv1-1|TLSv1-2|SSLv3|TLSv1)
            conn_timeout: Connection timeout in seconds (1-3600)
            monitor_keepalive_period: Keepalive period in seconds (1-120)
            monitor_failure_retry_period: Retry period in seconds (1-86400)
            reliable: Enable/disable reliable logging (enable|disable)
            priority: Priority (default|low)
            max_log_rate: Maximum log rate in Mbps (0-100000)
            interface_select_method: Interface selection (auto|sdwan|specify)
            interface: Source interface (string)
            source_ip: Source IP address (string)
            upload_option: Upload schedule (store-and-upload|realtime|1-minute|5-minute)
            upload_interval: Upload frequency (daily|weekly|monthly)
            upload_day: Upload day (sunday-saturday|1-31)
            upload_time: Upload time (hh:mm)
            ips_archive: Enable/disable IPS archiving (enable|disable)
            vrf_select: VRF selection (string)
            vdom: Virtual domain name or False for global
            **kwargs: Additional parameters

        Returns:
            Dictionary containing update result

        Examples:
            >>> fgt.api.cmdb.log.fortianalyzer2_override_setting.update(
            ...     override='enable',
            ...     status='enable',
            ...     server='192.168.1.101',
            ...     vdom='vdom1'
            ... )
        """
        data = data_dict.copy() if data_dict else {}

        param_map = {
            "status": status,
            "override": override,
            "use-management-vdom": use_management_vdom,
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

        path = "log.fortianalyzer2/override-setting"
        return self._client.put("cmdb", path, data=data, vdom=vdom)
