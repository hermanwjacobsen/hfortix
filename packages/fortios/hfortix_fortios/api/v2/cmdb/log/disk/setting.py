"""
FortiOS CMDB - Log disk setting

Configuration endpoint for managing cmdb log/disk/setting objects.

API Endpoints:
    GET    /cmdb/log/disk/setting
    POST   /cmdb/log/disk/setting
    PUT    /cmdb/log/disk/setting/{identifier}
    DELETE /cmdb/log/disk/setting/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.log_disk_setting.get()
    >>>
    >>> # Create with auto-normalization (strings/lists converted automatically)
    >>> result = fgt.api.cmdb.log_disk_setting.post(
    ...     name="example",
    ...     srcintf="port1",  # Auto-converted to [{'name': 'port1'}]
    ...     dstintf=["port2", "port3"],  # Auto-converted to list of dicts
    ... )

Important:
    - Use **POST** to create new objects
    - Use **PUT** to update existing objects
    - Use **GET** to retrieve configuration
    - Use **DELETE** to remove objects
    - **Auto-normalization**: List fields accept strings or lists, automatically
      converted to FortiOS format [{'name': '...'}]
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Union

if TYPE_CHECKING:
    from collections.abc import Coroutine
    from hfortix_core.http.interface import IHTTPClient
    from hfortix_fortios.models import FortiObject

# Import helper functions from central _helpers module
from hfortix_fortios._helpers import (
    build_api_payload,
    build_cmdb_payload,  # Keep for backward compatibility / manual usage
    is_success,
)
# Import metadata mixin for schema introspection
from hfortix_fortios._helpers.metadata_mixin import MetadataMixin

# Import Protocol-based type hints (eliminates need for local @overload decorators)
from hfortix_fortios._protocols import CRUDEndpoint

class Setting(CRUDEndpoint, MetadataMixin):
    """Setting Operations."""
    
    # Configure metadata mixin to use this endpoint's helper module
    _helper_module_name = "setting"
    
    # ========================================================================
    # Capabilities (from schema metadata)
    # ========================================================================
    SUPPORTS_CREATE = False
    SUPPORTS_READ = True
    SUPPORTS_UPDATE = True
    SUPPORTS_DELETE = False
    SUPPORTS_MOVE = True
    SUPPORTS_CLONE = True
    SUPPORTS_FILTERING = True
    SUPPORTS_PAGINATION = True
    SUPPORTS_SEARCH = False
    SUPPORTS_SORTING = False

    def __init__(self, client: "IHTTPClient"):
        """Initialize Setting endpoint."""
        self._client = client

    # ========================================================================
    # GET Method
    # Type hints provided by CRUDEndpoint protocol (no local @overload needed)
    # ========================================================================
    
    def get(
        self,
        name: str | None = None,
        filter: list[str] | None = None,
        count: int | None = None,
        start: int | None = None,
        q_datasource: bool | None = None,
        q_skip_to: int | None = None,
        q_with_meta: bool | None = None,
        q_with_contents_hash: bool | None = None,
        q_skip: bool | None = None,
        q_format: list[str] | None = None,
        q_key: str | None = None,
        q_pattern: str | None = None,
        q_scope: str | None = None,
        q_exclude_default_values: bool | None = None,
        q_datasource_format: dict[str, Any] | None = None,
        q_unfiltered_count: int | None = None,
        q_stat_items: str | None = None,
        q_primary_keys: str | None = None,
        q_action: Literal["default", "schema"] | None = None,
        payload_dict: dict[str, Any] | None = None,
        vdom: str | bool | None = None,
        error_mode: Literal["raise", "return", "print"] | None = None,
        error_format: Literal["detailed", "simple", "code_only"] | None = None,
    ):  # type: ignore[no-untyped-def]
        """
        Retrieve log/disk/setting configuration.

        Settings for local disk logging.

        Args:
            name: Name identifier to retrieve specific object. If None, returns all objects.
            filter: List of filter expressions to limit results.
                Each filter uses format: "field==value" or "field!=value"
                Operators: ==, !=, =@ (contains), !@ (not contains), <=, <, >=, >
                Multiple filters use AND logic. For OR, use comma in single string.
                Example: ["name==test", "status==enable"] or ["name==test,name==prod"]
            count: Maximum number of entries to return (pagination).
            start: Starting entry index for pagination (0-based).
            payload_dict: Additional query parameters for advanced options:
                - datasource (bool): Include datasource information
                - with_meta (bool): Include metadata about each object
                - with_contents_hash (bool): Include checksum of object contents
                - format (list[str]): Property names to include (e.g., ["policyid", "srcintf"])
                - scope (str): Query scope - "global", "vdom", or "both"
                - action (str): Special actions - "schema", "default"
                See FortiOS REST API documentation for complete list.
            vdom: Virtual domain name. Use True for global, string for specific VDOM, None for default.
            error_mode: Override client-level error_mode. "raise" raises exceptions, "return" returns error dict, "print" prints errors.
            error_format: Override client-level error_format. "detailed" provides full context, "simple" is concise, "code_only" returns just status code.

        Returns:
            FortiObject instance or list of FortiObject instances. Returns Coroutine if using async client.
            Use .dict, .json, or .raw properties to access as dictionary.
            
            Response structure:
                - http_method: GET
                - results: Configuration object(s)
                - vdom: Virtual domain
                - path: API path
                - name: Object name (single object queries)
                - status: success/error
                - http_status: HTTP status code
                - build: FortiOS build number

        Examples:
            >>> # Get all log/disk/setting objects
            >>> result = fgt.api.cmdb.log_disk_setting.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.log_disk_setting.get(
            ...     filter=["name==test", "status==enable"]
            ... )
            
            >>> # Get with pagination
            >>> result = fgt.api.cmdb.log_disk_setting.get(
            ...     start=0, count=100
            ... )
            
            >>> # Get schema information  
            >>> schema = fgt.api.cmdb.log_disk_setting.get_schema()

        See Also:
            - post(): Create new log/disk/setting object
            - put(): Update existing log/disk/setting object
            - delete(): Remove log/disk/setting object
            - exists(): Check if object exists
            - get_schema(): Get endpoint schema/metadata
        """
        params = payload_dict.copy() if payload_dict else {}
        
        # Add explicit query parameters
        if filter is not None:
            params["filter"] = filter
        if count is not None:
            params["count"] = count
        if start is not None:
            params["start"] = start
        if q_datasource is not None:
            params["datasource"] = q_datasource
        if q_skip_to is not None:
            params["skip_to"] = q_skip_to
        if q_with_meta is not None:
            params["with_meta"] = q_with_meta
        if q_with_contents_hash is not None:
            params["with_contents_hash"] = q_with_contents_hash
        if q_skip is not None:
            params["skip"] = q_skip
        if q_format is not None:
            params["format"] = q_format
        if q_key is not None:
            params["key"] = q_key
        if q_pattern is not None:
            params["pattern"] = q_pattern
        if q_scope is not None:
            params["scope"] = q_scope
        if q_exclude_default_values is not None:
            params["exclude-default-values"] = q_exclude_default_values
        if q_datasource_format is not None:
            params["datasource_format"] = q_datasource_format
        if q_unfiltered_count is not None:
            params["unfiltered_count"] = q_unfiltered_count
        if q_stat_items is not None:
            params["stat-items"] = q_stat_items
        if q_primary_keys is not None:
            params["primary_keys"] = q_primary_keys
        if q_action is not None:
            params["action"] = q_action
        
        if name:
            endpoint = f"/log.disk/setting/{name}"
            unwrap_single = True
        else:
            endpoint = "/log.disk/setting"
            unwrap_single = False
        
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, unwrap_single=unwrap_single
        )

    def get_schema(
        self,
        vdom: str | None = None,
        format: str = "schema",
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Get schema/metadata for this endpoint.
        
        Returns the FortiOS schema definition including available fields,
        their types, required vs optional properties, enum values, nested
        structures, and default values.
        
        This queries the live firewall for its current schema, which may
        vary between FortiOS versions.
        
        Args:
            vdom: Virtual domain. None uses default VDOM.
            format: Schema format - "schema" (FortiOS native) or "json-schema" (JSON Schema standard).
                Defaults to "schema".
                
        Returns:
            Schema definition as dict. Returns Coroutine if using async client.
            
        Example:
            >>> # Get FortiOS native schema
            >>> schema = fgt.api.cmdb.log_disk_setting.get_schema()
            >>> print(schema['results'])
            
            >>> # Get JSON Schema format (if supported)
            >>> json_schema = fgt.api.cmdb.log_disk_setting.get_schema(format="json-schema")
        
        Note:
            Not all endpoints support all schema formats. The "schema" format
            is most widely supported.
        """
        return self.get(action=format, vdom=vdom)


    # ========================================================================
    # PUT Method
    # Type hints provided by CRUDEndpoint protocol (no local @overload needed)
    # ========================================================================
    
    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        status: Literal["enable", "disable"] | None = None,
        ips_archive: Literal["enable", "disable"] | None = None,
        max_log_file_size: int | None = None,
        max_policy_packet_capture_size: int | None = None,
        roll_schedule: Literal["daily", "weekly"] | None = None,
        roll_day: Literal["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"] | list[str] | None = None,
        roll_time: str | None = None,
        diskfull: Literal["overwrite", "nolog"] | None = None,
        log_quota: int | None = None,
        dlp_archive_quota: int | None = None,
        report_quota: int | None = None,
        maximum_log_age: int | None = None,
        upload: Literal["enable", "disable"] | None = None,
        upload_destination: Literal["ftp-server"] | None = None,
        uploadip: str | None = None,
        uploadport: int | None = None,
        source_ip: str | None = None,
        uploaduser: str | None = None,
        uploadpass: Any | None = None,
        uploaddir: str | None = None,
        uploadtype: Literal["traffic", "event", "virus", "webfilter", "IPS", "emailfilter", "dlp-archive", "anomaly", "voip", "dlp", "app-ctrl", "waf", "gtp", "dns", "ssh", "ssl", "file-filter", "icap", "virtual-patch", "debug"] | list[str] | None = None,
        uploadsched: Literal["disable", "enable"] | None = None,
        uploadtime: str | None = None,
        upload_delete_files: Literal["enable", "disable"] | None = None,
        upload_ssl_conn: Literal["default", "high", "low", "disable"] | None = None,
        full_first_warning_threshold: int | None = None,
        full_second_warning_threshold: int | None = None,
        full_final_warning_threshold: int | None = None,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = None,
        interface: str | None = None,
        vrf_select: int | None = None,
        q_action: Literal["move"] | None = None,
        q_before: str | None = None,
        q_after: str | None = None,
        q_scope: str | None = None,
        vdom: str | bool | None = None,
        error_mode: Literal["raise", "return", "print"] | None = None,
        error_format: Literal["detailed", "simple", "code_only"] | None = None,
    ):  # type: ignore[no-untyped-def]
        """
        Update existing log/disk/setting object.

        Settings for local disk logging.

        Args:
            payload_dict: Object data as dict. Must include name (primary key).
            status: Enable/disable local disk logging.
            ips_archive: Enable/disable IPS packet archiving to the local disk.
            max_log_file_size: Maximum log file size before rolling (1 - 100 Mbytes).
            max_policy_packet_capture_size: Maximum size of policy sniffer in MB (0 means unlimited).
            roll_schedule: Frequency to check log file for rolling.
            roll_day: Day of week on which to roll log file.
            roll_time: Time of day to roll the log file (hh:mm).
            diskfull: Action to take when disk is full. The system can overwrite the oldest log messages or stop logging when the disk is full (default = overwrite).
            log_quota: Disk log quota (MB).
            dlp_archive_quota: DLP archive quota (MB).
            report_quota: Report db quota (MB).
            maximum_log_age: Delete log files older than (days).
            upload: Enable/disable uploading log files when they are rolled.
            upload_destination: The type of server to upload log files to. Only FTP is currently supported.
            uploadip: IP address of the FTP server to upload log files to.
            uploadport: TCP port to use for communicating with the FTP server (default = 21).
            source_ip: Source IP address to use for uploading disk log files.
            uploaduser: Username required to log into the FTP server to upload disk log files.
            uploadpass: Password required to log into the FTP server to upload disk log files.
            uploaddir: The remote directory on the FTP server to upload log files to.
            uploadtype: Types of log files to upload. Separate multiple entries with a space.
            uploadsched: Set the schedule for uploading log files to the FTP server (default = disable = upload when rolling).
            uploadtime: Time of day at which log files are uploaded if uploadsched is enabled (hh:mm or hh).
            upload_delete_files: Delete log files after uploading (default = enable).
            upload_ssl_conn: Enable/disable encrypted FTPS communication to upload log files.
            full_first_warning_threshold: Log full first warning threshold as a percent (1 - 98, default = 75).
            full_second_warning_threshold: Log full second warning threshold as a percent (2 - 99, default = 90).
            full_final_warning_threshold: Log full final warning threshold as a percent (3 - 100, default = 95).
            interface_select_method: Specify how to select outgoing interface to reach server.
            interface: Specify outgoing interface to reach server.
            vrf_select: VRF ID used for connection to server.
            vdom: Virtual domain name.
            error_mode: Override client-level error_mode. "raise" raises exceptions, "return" returns error dict, "print" prints errors.
            error_format: Override client-level error_format. "detailed" provides full context, "simple" is concise, "code_only" returns just status code.

        Returns:
            FortiObject instance. Use .dict, .json, or .raw to access as dictionary.

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.log_disk_setting.put(
            ...     name="existing-object",
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "name": "existing-object",
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.log_disk_setting.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Build payload using helper function with auto-normalization
        # This automatically converts strings/lists to [{'name': '...'}] format for list fields
        # To disable auto-normalization, use build_cmdb_payload directly
        payload_data = build_api_payload(
            status=status,
            ips_archive=ips_archive,
            max_log_file_size=max_log_file_size,
            max_policy_packet_capture_size=max_policy_packet_capture_size,
            roll_schedule=roll_schedule,
            roll_day=roll_day,
            roll_time=roll_time,
            diskfull=diskfull,
            log_quota=log_quota,
            dlp_archive_quota=dlp_archive_quota,
            report_quota=report_quota,
            maximum_log_age=maximum_log_age,
            upload=upload,
            upload_destination=upload_destination,
            uploadip=uploadip,
            uploadport=uploadport,
            source_ip=source_ip,
            uploaduser=uploaduser,
            uploadpass=uploadpass,
            uploaddir=uploaddir,
            uploadtype=uploadtype,
            uploadsched=uploadsched,
            uploadtime=uploadtime,
            upload_delete_files=upload_delete_files,
            upload_ssl_conn=upload_ssl_conn,
            full_first_warning_threshold=full_first_warning_threshold,
            full_second_warning_threshold=full_second_warning_threshold,
            full_final_warning_threshold=full_final_warning_threshold,
            interface_select_method=interface_select_method,
            interface=interface,
            vrf_select=vrf_select,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.setting import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/log/disk/setting",
            )
        
        # Singleton endpoint - no identifier needed
        endpoint = "/log.disk/setting"

        # Add explicit query parameters for PUT
        params: dict[str, Any] = {}
        if q_action is not None:
            params["action"] = q_action
        if q_before is not None:
            params["before"] = q_before
        if q_after is not None:
            params["after"] = q_after
        if q_scope is not None:
            params["scope"] = q_scope
        
        return self._client.put(
            "cmdb", endpoint, data=payload_data, params=params, vdom=vdom
        )





    # ========================================================================
    # Action: Move
    # ========================================================================
    
    def move(
        self,
        name: str,
        action: Literal["before", "after"],
        reference_name: str,
        vdom: str | bool | None = None,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Move log/disk/setting object to a new position.
        
        Reorders objects by moving one before or after another.
        
        Args:
            name: Name of object to move
            action: Move "before" or "after" reference object
            reference_name: Name of reference object
            vdom: Virtual domain name
            **kwargs: Additional parameters
            
        Returns:
            API response dictionary
            
        Example:
            >>> # Move policy 100 before policy 50
            >>> fgt.api.cmdb.log_disk_setting.move(
            ...     name="object1",
            ...     action="before",
            ...     reference_name="object2"
            ... )
        """
        return self._client.request(
            method="PUT",
            path=f"/api/v2/cmdb/log.disk/setting",
            params={
                "name": name,
                "action": "move",
                action: reference_name,
                "vdom": vdom,
                **kwargs,
            },
        )

    # ========================================================================
    # Action: Clone
    # ========================================================================
    
    def clone(
        self,
        name: str,
        new_name: str,
        vdom: str | bool | None = None,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Clone log/disk/setting object.
        
        Creates a copy of an existing object with a new identifier.
        
        Args:
            name: Name of object to clone
            new_name: Name for the cloned object
            vdom: Virtual domain name
            **kwargs: Additional parameters
            
        Returns:
            API response dictionary
            
        Example:
            >>> # Clone an existing object
            >>> fgt.api.cmdb.log_disk_setting.clone(
            ...     name="template",
            ...     new_name="new-from-template"
            ... )
        """
        return self._client.request(
            method="POST",
            path=f"/api/v2/cmdb/log.disk/setting",
            params={
                "name": name,
                "new_name": new_name,
                "action": "clone",
                "vdom": vdom,
                **kwargs,
            },
        )

    # ========================================================================
    # Helper: Check Existence
    # ========================================================================
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = None,
    ) -> bool:
        """
        Check if log/disk/setting object exists.
        
        Args:
            name: Name to check
            vdom: Virtual domain name
            
        Returns:
            True if object exists, False otherwise
            
        Example:
            >>> # Check before creating
            >>> if not fgt.api.cmdb.log_disk_setting.exists(name="myobj"):
            ...     fgt.api.cmdb.log_disk_setting.post(payload_dict=data)
        """
        # Try to fetch the object - 404 means it doesn't exist
        try:
            result = self.get(
                name=name,
                vdom=vdom
            )
            response = result.raw if hasattr(result, 'raw') else result
            # Check if response indicates success
            return is_success(response)
        except Exception as e:
            # 404 means object doesn't exist - return False
            # Any other error should be re-raised
            error_str = str(e)
            if '404' in error_str or 'Not Found' in error_str or 'ResourceNotFoundError' in str(type(e)):
                return False
            raise

