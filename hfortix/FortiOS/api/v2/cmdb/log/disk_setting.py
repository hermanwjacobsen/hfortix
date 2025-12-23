"""
FortiOS CMDB - Cmdb Log Disk Setting

Configuration endpoint for managing cmdb log disk setting objects.

API Endpoints:
    GET    /cmdb/log/disk_setting
    PUT    /cmdb/log/disk_setting/{identifier}

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.log.disk_setting.get()
    >>>
    >>> # Get specific item (if supported)
    >>> item = fgt.api.cmdb.log.disk_setting.get(name="item_name")
    >>>
    >>> # Create new item (use POST)
    >>> result = fgt.api.cmdb.log.disk_setting.post(
    ...     name="new_item",
    ...     # ... additional parameters
    ... )
    >>>
    >>> # Update existing item (use PUT)
    >>> result = fgt.api.cmdb.log.disk_setting.put(
    ...     name="existing_item",
    ...     # ... parameters to update
    ... )
    >>>
    >>> # Delete item
    >>> result = fgt.api.cmdb.log.disk_setting.delete(name="item_name")

Important:
    - Use **POST** to create new objects (404 error if already exists)
    - Use **PUT** to update existing objects (404 error if doesn't exist)
    - Use **GET** to retrieve configuration (no changes made)
    - Use **DELETE** to remove objects (404 error if doesn't exist)
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Union

if TYPE_CHECKING:
    from collections.abc import Coroutine

    from hfortix.FortiOS.http_client_interface import IHTTPClient


class DiskSetting:
    """
    Disksetting Operations.

    Provides CRUD operations for FortiOS disksetting configuration.

    Methods:
        get(): Retrieve configuration objects
        put(): Update existing configuration objects

    Important:
        - POST creates new objects (404 if name already exists)
        - PUT updates existing objects (404 if name doesn't exist)
        - GET retrieves objects without making changes
        - DELETE removes objects (404 if name doesn't exist)
    """

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize DiskSetting endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

    def get(
        self,
        payload_dict: dict[str, Any] | None = None,
        exclude_default_values: bool | None = None,
        stat_items: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Select all entries in a CLI table.

        Args:
            exclude_default_values: Exclude properties/objects with default
            value (optional)
            stat_items: Items to count occurrence in entire response (multiple
            items should be separated by '|'). (optional)
            vdom: Virtual domain name, or False to skip. Handled by HTTPClient.
            raw_json: If True, return full API response with metadata. If
            False, return only results.
            **kwargs: Additional query parameters (filter, sort, start, count,
            format, etc.)

        Common Query Parameters (via **kwargs):
            filter: Filter results (e.g., filter='name==value')
            sort: Sort results (e.g., sort='name,asc')
            start: Starting entry index for paging
            count: Maximum number of entries to return
            format: Fields to return (e.g., format='name|type')
            See FortiOS REST API documentation for full list of query
            parameters

        Returns:
            Dictionary containing API response
        """
        params = payload_dict.copy() if payload_dict else {}
        endpoint = "/log.disk/setting"
        if exclude_default_values is not None:
            params["exclude-default-values"] = exclude_default_values
        if stat_items is not None:
            params["stat-items"] = stat_items
        params.update(kwargs)
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )

    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        before: str | None = None,
        after: str | None = None,
        status: str | None = None,
        ips_archive: str | None = None,
        max_log_file_size: int | None = None,
        max_policy_packet_capture_size: int | None = None,
        roll_schedule: str | None = None,
        roll_day: str | None = None,
        roll_time: str | None = None,
        diskfull: str | None = None,
        log_quota: int | None = None,
        dlp_archive_quota: int | None = None,
        report_quota: int | None = None,
        maximum_log_age: int | None = None,
        upload: str | None = None,
        upload_destination: str | None = None,
        uploadip: str | None = None,
        uploadport: int | None = None,
        source_ip: str | None = None,
        uploaduser: str | None = None,
        uploadpass: str | None = None,
        uploaddir: str | None = None,
        uploadtype: str | None = None,
        uploadsched: str | None = None,
        uploadtime: str | None = None,
        upload_delete_files: str | None = None,
        upload_ssl_conn: str | None = None,
        full_first_warning_threshold: int | None = None,
        full_second_warning_threshold: int | None = None,
        full_final_warning_threshold: int | None = None,
        interface_select_method: str | None = None,
        interface: str | None = None,
        vrf_select: int | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update this specific resource.

        Args:
            payload_dict: Optional dictionary of all parameters (can be passed
            as first positional arg)
            before: If *action=move*, use *before* to specify the ID of the
            resource that this resource will be moved before. (optional)
            after: If *action=move*, use *after* to specify the ID of the
            resource that this resource will be moved after. (optional)
            status: Enable/disable local disk logging. (optional)
            ips_archive: Enable/disable IPS packet archiving to the local disk.
            (optional)
            max_log_file_size: Maximum log file size before rolling (1 - 100
            Mbytes). (optional)
            max_policy_packet_capture_size: Maximum size of policy sniffer in
            MB (0 means unlimited). (optional)
            roll_schedule: Frequency to check log file for rolling. (optional)
            roll_day: Day of week on which to roll log file. (optional)
            roll_time: Time of day to roll the log file (hh:mm). (optional)
            diskfull: Action to take when disk is full. The system can
            overwrite the oldest log messages or stop logging when the disk is
            full (default = overwrite). (optional)
            log_quota: Disk log quota (MB). (optional)
            dlp_archive_quota: DLP archive quota (MB). (optional)
            report_quota: Report db quota (MB). (optional)
            maximum_log_age: Delete log files older than (days). (optional)
            upload: Enable/disable uploading log files when they are rolled.
            (optional)
            upload_destination: The type of server to upload log files to. Only
            FTP is currently supported. (optional)
            uploadip: IP address of the FTP server to upload log files to.
            (optional)
            uploadport: TCP port to use for communicating with the FTP server
            (default = 21). (optional)
            source_ip: Source IP address to use for uploading disk log files.
            (optional)
            uploaduser: Username required to log into the FTP server to upload
            disk log files. (optional)
            uploadpass: Password required to log into the FTP server to upload
            disk log files. (optional)
            uploaddir: The remote directory on the FTP server to upload log
            files to. (optional)
            uploadtype: Types of log files to upload. Separate multiple entries
            with a space. (optional)
            uploadsched: Set the schedule for uploading log files to the FTP
            server (default = disable = upload when rolling). (optional)
            uploadtime: Time of day at which log files are uploaded if
            uploadsched is enabled (hh:mm or hh). (optional)
            upload_delete_files: Delete log files after uploading (default =
            enable). (optional)
            upload_ssl_conn: Enable/disable encrypted FTPS communication to
            upload log files. (optional)
            full_first_warning_threshold: Log full first warning threshold as a
            percent (1 - 98, default = 75). (optional)
            full_second_warning_threshold: Log full second warning threshold as
            a percent (2 - 99, default = 90). (optional)
            full_final_warning_threshold: Log full final warning threshold as a
            percent (3 - 100, default = 95). (optional)
            interface_select_method: Specify how to select outgoing interface
            to reach server. (optional)
            interface: Specify outgoing interface to reach server. (optional)
            vrf_select: VRF ID used for connection to server. (optional)
            vdom: Virtual domain name, or False to skip. Handled by HTTPClient.
            raw_json: If True, return full API response with metadata. If
            False, return only results.
            **kwargs: Additional query parameters (filter, sort, start, count,
            format, etc.)

        Common Query Parameters (via **kwargs):
            filter: Filter results (e.g., filter='name==value')
            sort: Sort results (e.g., sort='name,asc')
            start: Starting entry index for paging
            count: Maximum number of entries to return
            format: Fields to return (e.g., format='name|type')
            See FortiOS REST API documentation for full list of query
            parameters

        Returns:
            Dictionary containing API response
        """
        data_payload = payload_dict.copy() if payload_dict else {}
        endpoint = "/log.disk/setting"
        if before is not None:
            data_payload["before"] = before
        if after is not None:
            data_payload["after"] = after
        if status is not None:
            data_payload["status"] = status
        if ips_archive is not None:
            data_payload["ips-archive"] = ips_archive
        if max_log_file_size is not None:
            data_payload["max-log-file-size"] = max_log_file_size
        if max_policy_packet_capture_size is not None:
            data_payload["max-policy-packet-capture-size"] = (
                max_policy_packet_capture_size
            )
        if roll_schedule is not None:
            data_payload["roll-schedule"] = roll_schedule
        if roll_day is not None:
            data_payload["roll-day"] = roll_day
        if roll_time is not None:
            data_payload["roll-time"] = roll_time
        if diskfull is not None:
            data_payload["diskfull"] = diskfull
        if log_quota is not None:
            data_payload["log-quota"] = log_quota
        if dlp_archive_quota is not None:
            data_payload["dlp-archive-quota"] = dlp_archive_quota
        if report_quota is not None:
            data_payload["report-quota"] = report_quota
        if maximum_log_age is not None:
            data_payload["maximum-log-age"] = maximum_log_age
        if upload is not None:
            data_payload["upload"] = upload
        if upload_destination is not None:
            data_payload["upload-destination"] = upload_destination
        if uploadip is not None:
            data_payload["uploadip"] = uploadip
        if uploadport is not None:
            data_payload["uploadport"] = uploadport
        if source_ip is not None:
            data_payload["source-ip"] = source_ip
        if uploaduser is not None:
            data_payload["uploaduser"] = uploaduser
        if uploadpass is not None:
            data_payload["uploadpass"] = uploadpass
        if uploaddir is not None:
            data_payload["uploaddir"] = uploaddir
        if uploadtype is not None:
            data_payload["uploadtype"] = uploadtype
        if uploadsched is not None:
            data_payload["uploadsched"] = uploadsched
        if uploadtime is not None:
            data_payload["uploadtime"] = uploadtime
        if upload_delete_files is not None:
            data_payload["upload-delete-files"] = upload_delete_files
        if upload_ssl_conn is not None:
            data_payload["upload-ssl-conn"] = upload_ssl_conn
        if full_first_warning_threshold is not None:
            data_payload["full-first-warning-threshold"] = (
                full_first_warning_threshold
            )
        if full_second_warning_threshold is not None:
            data_payload["full-second-warning-threshold"] = (
                full_second_warning_threshold
            )
        if full_final_warning_threshold is not None:
            data_payload["full-final-warning-threshold"] = (
                full_final_warning_threshold
            )
        if interface_select_method is not None:
            data_payload["interface-select-method"] = interface_select_method
        if interface is not None:
            data_payload["interface"] = interface
        if vrf_select is not None:
            data_payload["vrf-select"] = vrf_select
        data_payload.update(kwargs)
        return self._client.put(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )
