"""
FortiOS CMDB - System device_upgrade

Configuration endpoint for managing cmdb system/device_upgrade objects.

API Endpoints:
    GET    /cmdb/system/device_upgrade
    POST   /cmdb/system/device_upgrade
    PUT    /cmdb/system/device_upgrade/{identifier}
    DELETE /cmdb/system/device_upgrade/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.system_device_upgrade.get()
    >>>
    >>> # Create with auto-normalization (strings/lists converted automatically)
    >>> result = fgt.api.cmdb.system_device_upgrade.post(
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
    normalize_table_field,  # For table field normalization
)
# Import metadata mixin for schema introspection
from hfortix_fortios._helpers.metadata_mixin import MetadataMixin

# Import Protocol-based type hints (eliminates need for local @overload decorators)
from hfortix_fortios._protocols import CRUDEndpoint

class DeviceUpgrade(CRUDEndpoint, MetadataMixin):
    """DeviceUpgrade Operations."""
    
    # Configure metadata mixin to use this endpoint's helper module
    _helper_module_name = "device_upgrade"
    
    # ========================================================================
    # Table Fields Metadata (for normalization)
    # Auto-generated from schema - supports flexible input formats
    # ========================================================================
    _TABLE_FIELDS = {
        "known_ha_members": {
            "mkey": "serial",
            "required_fields": ['serial'],
            "example": "[{'serial': 'value'}]",
        },
    }
    
    # ========================================================================
    # Capabilities (from schema metadata)
    # ========================================================================
    SUPPORTS_CREATE = True
    SUPPORTS_READ = True
    SUPPORTS_UPDATE = True
    SUPPORTS_DELETE = True
    SUPPORTS_MOVE = True
    SUPPORTS_CLONE = True
    SUPPORTS_FILTERING = True
    SUPPORTS_PAGINATION = True
    SUPPORTS_SEARCH = False
    SUPPORTS_SORTING = False

    def __init__(self, client: "IHTTPClient"):
        """Initialize DeviceUpgrade endpoint."""
        self._client = client

    # ========================================================================
    # GET Method
    # Type hints provided by CRUDEndpoint protocol (no local @overload needed)
    # ========================================================================
    
    def get(
        self,
        serial: str | None = None,
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
        Retrieve system/device_upgrade configuration.

        Independent upgrades for managed devices.

        Args:
            serial: String identifier to retrieve specific object.
                If None, returns all objects.
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
            >>> # Get all system/device_upgrade objects
            >>> result = fgt.api.cmdb.system_device_upgrade.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get specific system/device_upgrade by serial
            >>> result = fgt.api.cmdb.system_device_upgrade.get(serial=1)
            >>> print(result['results'])
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.system_device_upgrade.get(
            ...     filter=["name==test", "status==enable"]
            ... )
            
            >>> # Get with pagination
            >>> result = fgt.api.cmdb.system_device_upgrade.get(
            ...     start=0, count=100
            ... )
            
            >>> # Get schema information  
            >>> schema = fgt.api.cmdb.system_device_upgrade.get_schema()

        See Also:
            - post(): Create new system/device_upgrade object
            - put(): Update existing system/device_upgrade object
            - delete(): Remove system/device_upgrade object
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
        
        if serial:
            endpoint = "/system/device-upgrade/" + str(serial)
            unwrap_single = True
        else:
            endpoint = "/system/device-upgrade"
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
            >>> schema = fgt.api.cmdb.system_device_upgrade.get_schema()
            >>> print(schema['results'])
            
            >>> # Get JSON Schema format (if supported)
            >>> json_schema = fgt.api.cmdb.system_device_upgrade.get_schema(format="json-schema")
        
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
        status: Literal["disabled", "initialized", "downloading", "device-disconnected", "ready", "coordinating", "staging", "final-check", "upgrade-devices", "cancelled", "confirmed", "done", "failed"] | None = None,
        ha_reboot_controller: str | None = None,
        next_path_index: int | None = None,
        known_ha_members: str | list[str] | list[dict[str, Any]] | None = None,
        initial_version: str | None = None,
        starter_admin: str | None = None,
        serial: str | None = None,
        timing: Literal["immediate", "scheduled"] | None = None,
        maximum_minutes: int | None = None,
        time: str | None = None,
        setup_time: str | None = None,
        upgrade_path: str | None = None,
        device_type: Literal["fortigate", "fortiswitch", "fortiap", "fortiextender"] | None = None,
        allow_download: Literal["enable", "disable"] | None = None,
        failure_reason: Literal["none", "internal", "timeout", "device-type-unsupported", "download-failed", "device-missing", "version-unavailable", "staging-failed", "reboot-failed", "device-not-reconnected", "node-not-ready", "no-final-confirmation", "no-confirmation-query", "config-error-log-nonempty", "csf-tree-not-supported", "firmware-changed", "node-failed", "image-missing"] | None = None,
        q_action: Literal["move"] | None = None,
        q_before: str | None = None,
        q_after: str | None = None,
        q_scope: str | None = None,
        vdom: str | bool | None = None,
        error_mode: Literal["raise", "return", "print"] | None = None,
        error_format: Literal["detailed", "simple", "code_only"] | None = None,
    ):  # type: ignore[no-untyped-def]
        """
        Update existing system/device_upgrade object.

        Independent upgrades for managed devices.

        Args:
            payload_dict: Object data as dict. Must include serial (primary key).
            vdom: Limit upgrade to this virtual domain (VDOM).
            status: Current status of the upgrade.
            ha_reboot_controller: Serial number of the FortiGate unit that will control the reboot process for the federated upgrade of the HA cluster.
            next_path_index: The index of the next image to upgrade to.
            known_ha_members: Known members of the HA cluster. If a member is missing at upgrade time, the upgrade will be cancelled.
                Default format: [{'serial': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'serial': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'serial': 'val1'}, ...]
                  - List of dicts: [{'serial': 'value'}] (recommended)
            initial_version: Firmware version when the upgrade was set up.
            starter_admin: Admin that started the upgrade.
            serial: Serial number of the node to include.
            timing: Run immediately or at a scheduled time.
            maximum_minutes: Maximum number of minutes to allow for immediate upgrade preparation.
            time: Scheduled upgrade execution time in UTC (hh:mm yyyy/mm/dd UTC).
            setup_time: Upgrade preparation start time in UTC (hh:mm yyyy/mm/dd UTC).
            upgrade_path: Fortinet OS image versions to upgrade through in major-minor-patch format, such as 7-0-4.
            device_type: Fortinet device type.
            allow_download: Enable/disable download firmware images.
            failure_reason: Upgrade failure reason.
            vdom: Virtual domain name.
            error_mode: Override client-level error_mode. "raise" raises exceptions, "return" returns error dict, "print" prints errors.
            error_format: Override client-level error_format. "detailed" provides full context, "simple" is concise, "code_only" returns just status code.

        Returns:
            FortiObject instance. Use .dict, .json, or .raw to access as dictionary.

        Raises:
            ValueError: If serial is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.system_device_upgrade.put(
            ...     serial=1,
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "serial": 1,
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.system_device_upgrade.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Apply normalization for table fields (supports flexible input formats)
        if known_ha_members is not None:
            known_ha_members = normalize_table_field(
                known_ha_members,
                mkey="serial",
                required_fields=['serial'],
                field_name="known_ha_members",
                example="[{'serial': 'value'}]",
            )
        
        # Build payload using helper function with auto-normalization
        # This automatically converts strings/lists to [{'name': '...'}] format for list fields
        # To disable auto-normalization, use build_cmdb_payload directly
        payload_data = build_api_payload(
            status=status,
            ha_reboot_controller=ha_reboot_controller,
            next_path_index=next_path_index,
            known_ha_members=known_ha_members,
            initial_version=initial_version,
            starter_admin=starter_admin,
            serial=serial,
            timing=timing,
            maximum_minutes=maximum_minutes,
            time=time,
            setup_time=setup_time,
            upgrade_path=upgrade_path,
            device_type=device_type,
            allow_download=allow_download,
            failure_reason=failure_reason,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.device_upgrade import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/system/device_upgrade",
            )
        
        serial_value = payload_data.get("serial")
        if not serial_value:
            raise ValueError("serial is required for PUT")
        endpoint = "/system/device-upgrade/" + str(serial_value)

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
    # POST Method
    # Type hints provided by CRUDEndpoint protocol (no local @overload needed)
    # ========================================================================
    
    def post(
        self,
        payload_dict: dict[str, Any] | None = None,
        status: Literal["disabled", "initialized", "downloading", "device-disconnected", "ready", "coordinating", "staging", "final-check", "upgrade-devices", "cancelled", "confirmed", "done", "failed"] | None = None,
        ha_reboot_controller: str | None = None,
        next_path_index: int | None = None,
        known_ha_members: str | list[str] | list[dict[str, Any]] | None = None,
        initial_version: str | None = None,
        starter_admin: str | None = None,
        serial: str | None = None,
        timing: Literal["immediate", "scheduled"] | None = None,
        maximum_minutes: int | None = None,
        time: str | None = None,
        setup_time: str | None = None,
        upgrade_path: str | None = None,
        device_type: Literal["fortigate", "fortiswitch", "fortiap", "fortiextender"] | None = None,
        allow_download: Literal["enable", "disable"] | None = None,
        failure_reason: Literal["none", "internal", "timeout", "device-type-unsupported", "download-failed", "device-missing", "version-unavailable", "staging-failed", "reboot-failed", "device-not-reconnected", "node-not-ready", "no-final-confirmation", "no-confirmation-query", "config-error-log-nonempty", "csf-tree-not-supported", "firmware-changed", "node-failed", "image-missing"] | None = None,
        q_action: Literal["clone"] | None = None,
        q_nkey: str | None = None,
        q_scope: str | None = None,
        vdom: str | bool | None = None,
        error_mode: Literal["raise", "return", "print"] | None = None,
        error_format: Literal["detailed", "simple", "code_only"] | None = None,
    ):  # type: ignore[no-untyped-def]
        """
        Create new system/device_upgrade object.

        Independent upgrades for managed devices.

        Args:
            payload_dict: Complete object data as dict. Alternative to individual parameters.
            vdom: Limit upgrade to this virtual domain (VDOM).
            status: Current status of the upgrade.
            ha_reboot_controller: Serial number of the FortiGate unit that will control the reboot process for the federated upgrade of the HA cluster.
            next_path_index: The index of the next image to upgrade to.
            known_ha_members: Known members of the HA cluster. If a member is missing at upgrade time, the upgrade will be cancelled.
                Default format: [{'serial': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'serial': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'serial': 'val1'}, ...]
                  - List of dicts: [{'serial': 'value'}] (recommended)
            initial_version: Firmware version when the upgrade was set up.
            starter_admin: Admin that started the upgrade.
            serial: Serial number of the node to include.
            timing: Run immediately or at a scheduled time.
            maximum_minutes: Maximum number of minutes to allow for immediate upgrade preparation.
            time: Scheduled upgrade execution time in UTC (hh:mm yyyy/mm/dd UTC).
            setup_time: Upgrade preparation start time in UTC (hh:mm yyyy/mm/dd UTC).
            upgrade_path: Fortinet OS image versions to upgrade through in major-minor-patch format, such as 7-0-4.
            device_type: Fortinet device type.
            allow_download: Enable/disable download firmware images.
            failure_reason: Upgrade failure reason.
            vdom: Virtual domain name. Use True for global, string for specific VDOM.
            error_mode: Override client-level error_mode. "raise" raises exceptions, "return" returns error dict, "print" prints errors.
            error_format: Override client-level error_format. "detailed" provides full context, "simple" is concise, "code_only" returns just status code.

        Returns:
            FortiObject instance with created object. Use .dict, .json, or .raw to access as dictionary.

        Examples:
            >>> # Create using individual parameters
            >>> result = fgt.api.cmdb.system_device_upgrade.post(
            ...     name="example",
            ...     # ... other required fields
            ... )
            >>> print(f"Created serial: {result['results']}")
            
            >>> # Create using payload dict
            >>> payload = DeviceUpgrade.defaults()  # Start with defaults
            >>> payload['name'] = 'my-object'
            >>> result = fgt.api.cmdb.system_device_upgrade.post(payload_dict=payload)

        Note:
            Required fields: {{ ", ".join(DeviceUpgrade.required_fields()) }}
            
            Use DeviceUpgrade.help('field_name') to get field details.

        See Also:
            - get(): Retrieve objects
            - put(): Update existing object
            - set(): Intelligent create or update
        """
        # Apply normalization for table fields (supports flexible input formats)
        if known_ha_members is not None:
            known_ha_members = normalize_table_field(
                known_ha_members,
                mkey="serial",
                required_fields=['serial'],
                field_name="known_ha_members",
                example="[{'serial': 'value'}]",
            )
        
        # Build payload using helper function with auto-normalization
        # This automatically converts strings/lists to [{'name': '...'}] format for list fields
        # To disable auto-normalization, use build_cmdb_payload directly
        payload_data = build_api_payload(
            status=status,
            ha_reboot_controller=ha_reboot_controller,
            next_path_index=next_path_index,
            known_ha_members=known_ha_members,
            initial_version=initial_version,
            starter_admin=starter_admin,
            serial=serial,
            timing=timing,
            maximum_minutes=maximum_minutes,
            time=time,
            setup_time=setup_time,
            upgrade_path=upgrade_path,
            device_type=device_type,
            allow_download=allow_download,
            failure_reason=failure_reason,
            data=payload_dict,
        )

        # Check for deprecated fields and warn users
        from ._helpers.device_upgrade import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/system/device_upgrade",
            )

        endpoint = "/system/device-upgrade"
        
        # Add explicit query parameters for POST
        params: dict[str, Any] = {}
        if q_action is not None:
            params["action"] = q_action
        if q_nkey is not None:
            params["nkey"] = q_nkey
        if q_scope is not None:
            params["scope"] = q_scope
        
        return self._client.post(
            "cmdb", endpoint, data=payload_data, params=params, vdom=vdom
        )

    # ========================================================================
    # DELETE Method
    # Type hints provided by CRUDEndpoint protocol (no local @overload needed)
    # ========================================================================
    
    def delete(
        self,
        serial: str | None = None,
        q_scope: str | None = None,
        vdom: str | bool | None = None,
        error_mode: Literal["raise", "return", "print"] | None = None,
        error_format: Literal["detailed", "simple", "code_only"] | None = None,
    ):  # type: ignore[no-untyped-def]
        """
        Delete system/device_upgrade object.

        Independent upgrades for managed devices.

        Args:
            serial: Primary key identifier
            vdom: Virtual domain name
            error_mode: Override client-level error_mode. "raise" raises exceptions, "return" returns error dict, "print" prints errors.
            error_format: Override client-level error_format. "detailed" provides full context, "simple" is concise, "code_only" returns just status code.

        Returns:
            FortiObject instance. Use .dict, .json, or .raw to access as dictionary

        Raises:
            ValueError: If serial is not provided

        Examples:
            >>> # Delete specific object
            >>> result = fgt.api.cmdb.system_device_upgrade.delete(serial=1)
            
            >>> # Check for errors
            >>> if result.get('status') != 'success':
            ...     print(f"Delete failed: {result.get('error')}")

        See Also:
            - exists(): Check if object exists before deleting
            - get(): Retrieve object to verify it exists
        """
        if not serial:
            raise ValueError("serial is required for DELETE")
        endpoint = "/system/device-upgrade/" + str(serial)

        # Add explicit query parameters for DELETE
        params: dict[str, Any] = {}
        if q_scope is not None:
            params["scope"] = q_scope
        
        return self._client.delete(
            "cmdb", endpoint, params=params, vdom=vdom
        )

    def exists(
        self,
        serial: str,
        vdom: str | bool | None = None,
    ) -> Union[bool, Coroutine[Any, Any, bool]]:
        """
        Check if system/device_upgrade object exists.

        Verifies whether an object exists by attempting to retrieve it and checking the response status.

        Args:
            serial: Primary key identifier
            vdom: Virtual domain name

        Returns:
            True if object exists, False otherwise

        Examples:
            >>> # Check if object exists before operations
            >>> if fgt.api.cmdb.system_device_upgrade.exists(serial=1):
            ...     print("Object exists")
            ... else:
            ...     print("Object not found")
            
            >>> # Conditional delete
            >>> if fgt.api.cmdb.system_device_upgrade.exists(serial=1):
            ...     fgt.api.cmdb.system_device_upgrade.delete(serial=1)

        See Also:
            - get(): Retrieve full object data
            - set(): Create or update automatically based on existence
        """
        # Try to fetch the object - 404 means it doesn't exist
        try:
            result = self.get(
                serial=serial,
                vdom=vdom
            )
            response = result.raw if hasattr(result, 'raw') else result
            
            if isinstance(response, dict):
                # Synchronous response - check status
                return is_success(response)
            else:
                # Asynchronous response
                async def _check() -> bool:
                    r = await response
                    return is_success(r)
                return _check()
        except Exception as e:
            # 404 means object doesn't exist - return False
            # Any other error should be re-raised
            error_str = str(e)
            if '404' in error_str or 'Not Found' in error_str or 'ResourceNotFoundError' in str(type(e)):
                return False
            raise


    def set(
        self,
        payload_dict: dict[str, Any] | None = None,
        status: Literal["disabled", "initialized", "downloading", "device-disconnected", "ready", "coordinating", "staging", "final-check", "upgrade-devices", "cancelled", "confirmed", "done", "failed"] | None = None,
        ha_reboot_controller: str | None = None,
        next_path_index: int | None = None,
        known_ha_members: str | list[str] | list[dict[str, Any]] | None = None,
        initial_version: str | None = None,
        starter_admin: str | None = None,
        serial: str | None = None,
        timing: Literal["immediate", "scheduled"] | None = None,
        maximum_minutes: int | None = None,
        time: str | None = None,
        setup_time: str | None = None,
        upgrade_path: str | None = None,
        device_type: Literal["fortigate", "fortiswitch", "fortiap", "fortiextender"] | None = None,
        allow_download: Literal["enable", "disable"] | None = None,
        failure_reason: Literal["none", "internal", "timeout", "device-type-unsupported", "download-failed", "device-missing", "version-unavailable", "staging-failed", "reboot-failed", "device-not-reconnected", "node-not-ready", "no-final-confirmation", "no-confirmation-query", "config-error-log-nonempty", "csf-tree-not-supported", "firmware-changed", "node-failed", "image-missing"] | None = None,
        vdom: str | bool | None = None,
        error_mode: Literal["raise", "return", "print"] | None = None,
        error_format: Literal["detailed", "simple", "code_only"] | None = None,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Create or update system/device_upgrade object (intelligent operation).

        Automatically determines whether to create (POST) or update (PUT) based on
        whether the resource exists. Requires the primary key (serial) in the payload.

        Args:
            payload_dict: Resource data including serial (primary key)
            status: Field status
            ha_reboot_controller: Field ha-reboot-controller
            next_path_index: Field next-path-index
            known_ha_members: Field known-ha-members
            initial_version: Field initial-version
            starter_admin: Field starter-admin
            serial: Field serial
            timing: Field timing
            maximum_minutes: Field maximum-minutes
            time: Field time
            setup_time: Field setup-time
            upgrade_path: Field upgrade-path
            device_type: Field device-type
            allow_download: Field allow-download
            failure_reason: Field failure-reason
            vdom: Virtual domain name
            **kwargs: Additional parameters passed to PUT or POST

        Returns:
            FortiObject instance. Use .dict, .json, or .raw to access as dictionary

        Raises:
            ValueError: If serial is missing from payload

        Examples:
            >>> # Intelligent create or update using field parameters
            >>> result = fgt.api.cmdb.system_device_upgrade.set(
            ...     serial=1,
            ...     # ... other fields
            ... )
            
            >>> # Or using payload dict
            >>> payload = {
            ...     "serial": 1,
            ...     "field1": "value1",
            ...     "field2": "value2",
            ... }
            >>> result = fgt.api.cmdb.system_device_upgrade.set(payload_dict=payload)
            >>> # Will POST if object doesn't exist, PUT if it does
            
            >>> # Idempotent configuration
            >>> for obj_data in configuration_list:
            ...     fgt.api.cmdb.system_device_upgrade.set(payload_dict=obj_data)
            >>> # Safely applies configuration regardless of current state

        Note:
            This method internally calls exists() then either post() or put().
            For performance-critical code with known state, call post() or put() directly.

        See Also:
            - post(): Create new object
            - put(): Update existing object
            - exists(): Check existence manually
        """
        # Build payload using helper function with auto-normalization
        payload_data = build_api_payload(
            status=status,
            ha_reboot_controller=ha_reboot_controller,
            next_path_index=next_path_index,
            known_ha_members=known_ha_members,
            initial_version=initial_version,
            starter_admin=starter_admin,
            serial=serial,
            timing=timing,
            maximum_minutes=maximum_minutes,
            time=time,
            setup_time=setup_time,
            upgrade_path=upgrade_path,
            device_type=device_type,
            allow_download=allow_download,
            failure_reason=failure_reason,
            data=payload_dict,
        )
        
        mkey_value = payload_data.get("serial")
        if not mkey_value:
            raise ValueError("serial is required for set()")
        
        # Check if resource exists
        if self.exists(serial=mkey_value, vdom=vdom):
            # Update existing resource
            return self.put(payload_dict=payload_data, vdom=vdom, **kwargs)
        else:
            # Create new resource
            return self.post(payload_dict=payload_data, vdom=vdom, **kwargs)

    # ========================================================================
    # Action: Move
    # ========================================================================
    
    def move(
        self,
        serial: str,
        action: Literal["before", "after"],
        reference_serial: str,
        vdom: str | bool | None = None,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Move system/device_upgrade object to a new position.
        
        Reorders objects by moving one before or after another.
        
        Args:
            serial: Identifier of object to move
            action: Move "before" or "after" reference object
            reference_serial: Identifier of reference object
            vdom: Virtual domain name
            **kwargs: Additional parameters
            
        Returns:
            API response dictionary
            
        Example:
            >>> # Move policy 100 before policy 50
            >>> fgt.api.cmdb.system_device_upgrade.move(
            ...     serial=100,
            ...     action="before",
            ...     reference_serial=50
            ... )
        """
        return self._client.request(
            method="PUT",
            path=f"/api/v2/cmdb/system/device-upgrade",
            params={
                "serial": serial,
                "action": "move",
                action: reference_serial,
                "vdom": vdom,
                **kwargs,
            },
        )

    # ========================================================================
    # Action: Clone
    # ========================================================================
    
    def clone(
        self,
        serial: str,
        new_serial: str,
        vdom: str | bool | None = None,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Clone system/device_upgrade object.
        
        Creates a copy of an existing object with a new identifier.
        
        Args:
            serial: Identifier of object to clone
            new_serial: Identifier for the cloned object
            vdom: Virtual domain name
            **kwargs: Additional parameters
            
        Returns:
            API response dictionary
            
        Example:
            >>> # Clone an existing object
            >>> fgt.api.cmdb.system_device_upgrade.clone(
            ...     serial=1,
            ...     new_serial=100
            ... )
        """
        return self._client.request(
            method="POST",
            path=f"/api/v2/cmdb/system/device-upgrade",
            params={
                "serial": serial,
                "new_serial": new_serial,
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
        serial: str,
        vdom: str | bool | None = None,
    ) -> bool:
        """
        Check if system/device_upgrade object exists.
        
        Args:
            serial: Identifier to check
            vdom: Virtual domain name
            
        Returns:
            True if object exists, False otherwise
            
        Example:
            >>> # Check before creating
            >>> if not fgt.api.cmdb.system_device_upgrade.exists(serial=1):
            ...     fgt.api.cmdb.system_device_upgrade.post(payload_dict=data)
        """
        # Try to fetch the object - 404 means it doesn't exist
        try:
            result = self.get(
                serial=serial,
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

