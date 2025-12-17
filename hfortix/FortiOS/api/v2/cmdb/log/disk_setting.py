"""
FortiOS CMDB - Log Disk Setting

Settings for local disk logging.

API Endpoints:
    GET  /api/v2/cmdb/log.disk/setting  - Get configuration
    PUT  /api/v2/cmdb/log.disk/setting  - Update configuration
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional, Union

if TYPE_CHECKING:
    from ...http_client import HTTPClient


class DiskSetting:
    """Log Disk Setting endpoint (singleton)"""

    def __init__(self, client: "HTTPClient") -> None:
        self._client = client

    def get(self, vdom: Optional[Union[str, bool]] = None, **kwargs: Any) -> dict[str, Any]:
        """
        Get disk log settings.

        Args:
            vdom: Virtual domain name or False for global
            **kwargs: Additional parameters

        Returns:
            Dictionary containing disk log settings

        Examples:
            >>> settings = fgt.api.cmdb.log.disk_setting.get()
        """
        path = "log.disk/setting"
        return self._client.get("cmdb", path, params=kwargs if kwargs else None, vdom=vdom)

    def put(
        self,
        data_dict: Optional[dict[str, Any]] = None,
        status: Optional[str] = None,
        ips_archive: Optional[str] = None,
        max_log_file_size: Optional[int] = None,
        max_policy_packet_capture_size: Optional[int] = None,
        roll_schedule: Optional[str] = None,
        roll_day: Optional[str] = None,
        roll_time: Optional[str] = None,
        diskfull: Optional[str] = None,
        log_quota: Optional[int] = None,
        dlp_archive_quota: Optional[int] = None,
        report_quota: Optional[int] = None,
        maximum_log_age: Optional[int] = None,
        upload: Optional[str] = None,
        upload_destination: Optional[str] = None,
        uploadip: Optional[str] = None,
        uploadport: Optional[int] = None,
        source_ip: Optional[str] = None,
        uploaduser: Optional[str] = None,
        uploadpass: Optional[str] = None,
        uploaddir: Optional[str] = None,
        uploadtype: Optional[str] = None,
        uploadsched: Optional[str] = None,
        uploadtime: Optional[str] = None,
        upload_delete_files: Optional[str] = None,
        upload_ssl_conn: Optional[str] = None,
        full_first_warning_threshold: Optional[int] = None,
        full_second_warning_threshold: Optional[int] = None,
        full_final_warning_threshold: Optional[int] = None,
        interface_select_method: Optional[str] = None,
        interface: Optional[str] = None,
        vrf_select: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Update disk log settings.

        Args:
            data_dict: Complete configuration dictionary
            status: Enable/disable local disk logging (enable|disable)
            ips_archive: Enable/disable IPS packet archive logging (enable|disable)
            max_log_file_size: Maximum log file size before rolling (1-1000 MB)
            max_policy_packet_capture_size: Maximum packet capture size (0-10000 KB)
            roll_schedule: Frequency to check log file for rolling (daily|weekly)
            roll_day: Day of week to roll log file
            roll_time: Time to roll the log file (hh:mm)
            diskfull: Action to take when disk is full (overwrite|nolog)
            log_quota: Disk log quota in MB (0 = unlimited)
            dlp_archive_quota: DLP archive quota in MB
            report_quota: Report quota in MB
            maximum_log_age: Maximum log age in days (0 = unlimited)
            upload: Enable/disable upload to remote server (enable|disable)
            upload_destination: Upload destination (ftp-server)
            uploadip: IP address of upload server
            uploadport: Upload server port
            source_ip: Source IP for uploads
            uploaduser: Upload username
            uploadpass: Upload password
            uploaddir: Upload directory
            uploadtype: Upload log type (traffic|event|virus|webfilter|IPS|spamfilter|dlp-archive|anomaly|voip|dlp|app-ctrl|waf|netscan|gtp|dns|ssh|ssl|file-filter|icap|ztna)
            uploadsched: Upload schedule name
            uploadtime: Time to upload logs (hh:mm)
            upload_delete_files: Delete log files after upload (enable|disable)
            upload_ssl_conn: SSL connection for upload (default|high|low|disable)
            full_first_warning_threshold: First warning threshold percentage (1-98)
            full_second_warning_threshold: Second warning threshold percentage (2-99)
            full_final_warning_threshold: Final warning threshold percentage (3-100)
            interface_select_method: Interface selection method (auto|sdwan|specify)
            interface: Outgoing interface
            vrf_select: VRF selection (0-31)
            vdom: Virtual domain name or False for global
            **kwargs: Additional parameters

        Returns:
            Dictionary containing update result

        Examples:
            >>> # Enable disk logging
            >>> fgt.api.cmdb.log.disk_setting.update(status='enable')

            >>> # Configure rolling
            >>> fgt.api.cmdb.log.disk_setting.update(
            ...     max_log_file_size=100,
            ...     roll_schedule='daily',
            ...     roll_time='00:00'
            ... )

            >>> # Configure upload
            >>> fgt.api.cmdb.log.disk_setting.update(
            ...     upload='enable',
            ...     uploadip='192.0.2.100',
            ...     uploadport=21,
            ...     uploaduser='loguser'
            ... )
        """
        data = data_dict.copy() if data_dict else {}

        param_map = {
            "status": status,
            "ips-archive": ips_archive,
            "max-log-file-size": max_log_file_size,
            "max-policy-packet-capture-size": max_policy_packet_capture_size,
            "roll-schedule": roll_schedule,
            "roll-day": roll_day,
            "roll-time": roll_time,
            "diskfull": diskfull,
            "log-quota": log_quota,
            "dlp-archive-quota": dlp_archive_quota,
            "report-quota": report_quota,
            "maximum-log-age": maximum_log_age,
            "upload": upload,
            "upload-destination": upload_destination,
            "uploadip": uploadip,
            "uploadport": uploadport,
            "source-ip": source_ip,
            "uploaduser": uploaduser,
            "uploadpass": uploadpass,
            "uploaddir": uploaddir,
            "uploadtype": uploadtype,
            "uploadsched": uploadsched,
            "uploadtime": uploadtime,
            "upload-delete-files": upload_delete_files,
            "upload-ssl-conn": upload_ssl_conn,
            "full-first-warning-threshold": full_first_warning_threshold,
            "full-second-warning-threshold": full_second_warning_threshold,
            "full-final-warning-threshold": full_final_warning_threshold,
            "interface-select-method": interface_select_method,
            "interface": interface,
            "vrf-select": vrf_select,
        }

        for key, value in param_map.items():
            if value is not None:
                data[key] = value

        data.update(kwargs)

        path = "log.disk/setting"
        return self._client.put("cmdb", path, data=data, vdom=vdom)
