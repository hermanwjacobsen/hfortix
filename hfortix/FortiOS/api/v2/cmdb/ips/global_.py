"""
FortiOS CMDB - IPS Global

Configure IPS global parameter (singleton).

API Endpoints:
    GET /api/v2/cmdb/ips/global - Get IPS global settings
    PUT /api/v2/cmdb/ips/global - Update IPS global settings
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional, Union

if TYPE_CHECKING:
    from ...http_client import HTTPClient


class Global:
    """IPS Global Settings endpoint"""

    def __init__(self, client: "HTTPClient") -> None:
        self._client = client

    def get(self, vdom: Optional[Union[str, bool]] = None, **kwargs: Any) -> dict[str, Any]:
        """
        Get IPS global settings.

        Args:
            vdom: Virtual domain name or False for global
            **kwargs: Additional parameters

        Returns:
            Dictionary containing global IPS settings

        Examples:
            >>> settings = fgt.api.cmdb.ips.global_.get()
        """
        path = "ips/global"
        return self._client.get("cmdb", path, params=kwargs if kwargs else None, vdom=vdom)

    def update(
        self,
        data_dict: Optional[dict[str, Any]] = None,
        anomaly_mode: Optional[str] = None,
        av_mem_limit: Optional[int] = None,
        cp_accel_mode: Optional[str] = None,
        database: Optional[str] = None,
        deep_app_insp_db_limit: Optional[int] = None,
        deep_app_insp_timeout: Optional[int] = None,
        engine_count: Optional[int] = None,
        exclude_signatures: Optional[str] = None,
        fail_open: Optional[str] = None,
        ips_reserve_cpu: Optional[str] = None,
        machine_learning_detection: Optional[str] = None,
        ngfw_max_scan_range: Optional[int] = None,
        np_accel_mode: Optional[str] = None,
        packet_log_queue_depth: Optional[int] = None,
        session_limit_mode: Optional[str] = None,
        socket_size: Optional[int] = None,
        sync_session_ttl: Optional[str] = None,
        tls_active_probe: Optional[dict[str, Any]] = None,
        traffic_submit: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Update IPS global settings.

        Args:
            data_dict: Complete configuration dictionary
            anomaly_mode: Global IPS anomaly mode (continuous|periodical)
            av_mem_limit: Maximum memory (MB) for antivirus processes
            cp_accel_mode: IPS CP acceleration mode (none|basic|advanced)
            database: IPS signature database (regular|extended)
            deep_app_insp_db_limit: Limit on deep application inspection sessions
            deep_app_insp_timeout: Deep application inspection timeout (seconds)
            engine_count: Number of IPS engines (0-255, 0=auto)
            exclude_signatures: Excluded signatures (none|industrial)
            fail_open: Enable/disable fail-open (enable|disable)
            ips_reserve_cpu: Enable/disable CPU reservation (disable|enable)
            machine_learning_detection: Enable/disable machine learning (enable|disable)
            ngfw_max_scan_range: Maximum NGFW scan range (1024-4096 KB)
            np_accel_mode: IPS NP acceleration mode (none|basic)
            packet_log_queue_depth: Packet log queue depth (128-2048)
            session_limit_mode: Session limit mode (accurate|heuristic)
            socket_size: IPS socket buffer size (0-256 MB, 0=auto)
            sync_session_ttl: Enable/disable sync session TTL (enable|disable)
            tls_active_probe: TLS active probe settings
            traffic_submit: Enable/disable traffic submission (disable|enable)
            vdom: Virtual domain name or False for global
            **kwargs: Additional parameters

        Returns:
            Dictionary containing update result

        Examples:
            >>> fgt.api.cmdb.ips.global_.update(
            ...     database='extended',
            ...     anomaly_mode='continuous',
            ...     engine_count=4
            ... )
        """
        data = data_dict.copy() if data_dict else {}

        param_map = {
            "anomaly-mode": anomaly_mode,
            "av-mem-limit": av_mem_limit,
            "cp-accel-mode": cp_accel_mode,
            "database": database,
            "deep-app-insp-db-limit": deep_app_insp_db_limit,
            "deep-app-insp-timeout": deep_app_insp_timeout,
            "engine-count": engine_count,
            "exclude-signatures": exclude_signatures,
            "fail-open": fail_open,
            "ips-reserve-cpu": ips_reserve_cpu,
            "machine-learning-detection": machine_learning_detection,
            "ngfw-max-scan-range": ngfw_max_scan_range,
            "np-accel-mode": np_accel_mode,
            "packet-log-queue-depth": packet_log_queue_depth,
            "session-limit-mode": session_limit_mode,
            "socket-size": socket_size,
            "sync-session-ttl": sync_session_ttl,
            "tls-active-probe": tls_active_probe,
            "traffic-submit": traffic_submit,
        }

        for key, value in param_map.items():
            if value is not None:
                data[key] = value

        data.update(kwargs)

        path = "ips/global"
        return self._client.put("cmdb", path, data=data, vdom=vdom)
