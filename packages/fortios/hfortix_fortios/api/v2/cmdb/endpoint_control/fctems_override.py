"""
FortiOS CMDB - Endpoint_control fctems_override

Configuration endpoint for managing cmdb endpoint_control/fctems_override objects.

API Endpoints:
    GET    /cmdb/endpoint_control/fctems_override
    POST   /cmdb/endpoint_control/fctems_override
    PUT    /cmdb/endpoint_control/fctems_override/{identifier}
    DELETE /cmdb/endpoint_control/fctems_override/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.endpoint_control_fctems_override.get()
    >>>
    >>> # Create with auto-normalization (strings/lists converted automatically)
    >>> result = fgt.api.cmdb.endpoint_control_fctems_override.post(
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

class FctemsOverride(CRUDEndpoint, MetadataMixin):
    """FctemsOverride Operations."""
    
    # Configure metadata mixin to use this endpoint's helper module
    _helper_module_name = "fctems_override"
    
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
        """Initialize FctemsOverride endpoint."""
        self._client = client

    # ========================================================================
    # GET Method
    # Type hints provided by CRUDEndpoint protocol (no local @overload needed)
    # ========================================================================
    
    def get(
        self,
        ems_id: int | None = None,
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
        Retrieve endpoint_control/fctems_override configuration.

        Configure FortiClient Enterprise Management Server (EMS) entries.

        Args:
            ems_id: Integer identifier to retrieve specific object.
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
            >>> # Get all endpoint_control/fctems_override objects
            >>> result = fgt.api.cmdb.endpoint_control_fctems_override.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get specific endpoint_control/fctems_override by ems-id
            >>> result = fgt.api.cmdb.endpoint_control_fctems_override.get(ems_id=1)
            >>> print(result['results'])
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.endpoint_control_fctems_override.get(
            ...     filter=["name==test", "status==enable"]
            ... )
            
            >>> # Get with pagination
            >>> result = fgt.api.cmdb.endpoint_control_fctems_override.get(
            ...     start=0, count=100
            ... )
            
            >>> # Get schema information  
            >>> schema = fgt.api.cmdb.endpoint_control_fctems_override.get_schema()

        See Also:
            - post(): Create new endpoint_control/fctems_override object
            - put(): Update existing endpoint_control/fctems_override object
            - delete(): Remove endpoint_control/fctems_override object
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
        
        if ems_id:
            endpoint = "/endpoint-control/fctems-override/" + str(ems_id)
            unwrap_single = True
        else:
            endpoint = "/endpoint-control/fctems-override"
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
            >>> schema = fgt.api.cmdb.endpoint_control_fctems_override.get_schema()
            >>> print(schema['results'])
            
            >>> # Get JSON Schema format (if supported)
            >>> json_schema = fgt.api.cmdb.endpoint_control_fctems_override.get_schema(format="json-schema")
        
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
        ems_id: int | None = None,
        status: Literal["enable", "disable"] | None = None,
        name: str | None = None,
        dirty_reason: Literal["none", "mismatched-ems-sn"] | None = None,
        fortinetone_cloud_authentication: Literal["enable", "disable"] | None = None,
        cloud_authentication_access_key: Any | None = None,
        server: str | None = None,
        https_port: int | None = None,
        serial_number: str | None = None,
        tenant_id: str | None = None,
        source_ip: str | None = None,
        pull_sysinfo: Literal["enable", "disable"] | None = None,
        pull_vulnerabilities: Literal["enable", "disable"] | None = None,
        pull_tags: Literal["enable", "disable"] | None = None,
        pull_malware_hash: Literal["enable", "disable"] | None = None,
        capabilities: Literal["fabric-auth", "silent-approval", "websocket", "websocket-malware", "push-ca-certs", "common-tags-api", "tenant-id", "client-avatars", "single-vdom-connector", "fgt-sysinfo-api", "ztna-server-info", "used-tags"] | list[str] | None = None,
        call_timeout: int | None = None,
        out_of_sync_threshold: int | None = None,
        send_tags_to_all_vdoms: Literal["enable", "disable"] | None = None,
        websocket_override: Literal["enable", "disable"] | None = None,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = None,
        interface: str | None = None,
        trust_ca_cn: Literal["enable", "disable"] | None = None,
        verifying_ca: str | None = None,
        q_action: Literal["move"] | None = None,
        q_before: str | None = None,
        q_after: str | None = None,
        q_scope: str | None = None,
        vdom: str | bool | None = None,
        error_mode: Literal["raise", "return", "print"] | None = None,
        error_format: Literal["detailed", "simple", "code_only"] | None = None,
    ):  # type: ignore[no-untyped-def]
        """
        Update existing endpoint_control/fctems_override object.

        Configure FortiClient Enterprise Management Server (EMS) entries.

        Args:
            payload_dict: Object data as dict. Must include ems-id (primary key).
            ems_id: EMS ID in order (1 - 7).
            status: Enable or disable this EMS configuration.
            name: FortiClient Enterprise Management Server (EMS) name.
            dirty_reason: Dirty Reason for FortiClient EMS.
            fortinetone_cloud_authentication: Enable/disable authentication of FortiClient EMS Cloud through FortiCloud account.
            cloud_authentication_access_key: FortiClient EMS Cloud multitenancy access key
            server: FortiClient EMS FQDN or IPv4 address.
            https_port: FortiClient EMS HTTPS access port number. (1 - 65535, default: 443).
            serial_number: EMS Serial Number.
            tenant_id: EMS Tenant ID.
            source_ip: REST API call source IP.
            pull_sysinfo: Enable/disable pulling SysInfo from EMS.
            pull_vulnerabilities: Enable/disable pulling vulnerabilities from EMS.
            pull_tags: Enable/disable pulling FortiClient user tags from EMS.
            pull_malware_hash: Enable/disable pulling FortiClient malware hash from EMS.
            capabilities: List of EMS capabilities.
            call_timeout: FortiClient EMS call timeout in seconds (1 - 180 seconds, default = 30).
            out_of_sync_threshold: Outdated resource threshold in seconds (10 - 3600, default = 180).
            send_tags_to_all_vdoms: Relax restrictions on tags to send all EMS tags to all VDOMs
            websocket_override: Enable/disable override behavior for how this FortiGate unit connects to EMS using a WebSocket connection.
            interface_select_method: Specify how to select outgoing interface to reach server.
            interface: Specify outgoing interface to reach server.
            trust_ca_cn: Enable/disable trust of the EMS certificate issuer(CA) and common name(CN) for certificate auto-renewal.
            verifying_ca: Lowest CA cert on Fortigate in verified EMS cert chain.
            vdom: Virtual domain name.
            error_mode: Override client-level error_mode. "raise" raises exceptions, "return" returns error dict, "print" prints errors.
            error_format: Override client-level error_format. "detailed" provides full context, "simple" is concise, "code_only" returns just status code.

        Returns:
            FortiObject instance. Use .dict, .json, or .raw to access as dictionary.

        Raises:
            ValueError: If ems-id is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.endpoint_control_fctems_override.put(
            ...     ems_id=1,
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "ems-id": 1,
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.endpoint_control_fctems_override.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Build payload using helper function with auto-normalization
        # This automatically converts strings/lists to [{'name': '...'}] format for list fields
        # To disable auto-normalization, use build_cmdb_payload directly
        payload_data = build_api_payload(
            ems_id=ems_id,
            status=status,
            name=name,
            dirty_reason=dirty_reason,
            fortinetone_cloud_authentication=fortinetone_cloud_authentication,
            cloud_authentication_access_key=cloud_authentication_access_key,
            server=server,
            https_port=https_port,
            serial_number=serial_number,
            tenant_id=tenant_id,
            source_ip=source_ip,
            pull_sysinfo=pull_sysinfo,
            pull_vulnerabilities=pull_vulnerabilities,
            pull_tags=pull_tags,
            pull_malware_hash=pull_malware_hash,
            capabilities=capabilities,
            call_timeout=call_timeout,
            out_of_sync_threshold=out_of_sync_threshold,
            send_tags_to_all_vdoms=send_tags_to_all_vdoms,
            websocket_override=websocket_override,
            interface_select_method=interface_select_method,
            interface=interface,
            trust_ca_cn=trust_ca_cn,
            verifying_ca=verifying_ca,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.fctems_override import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/endpoint_control/fctems_override",
            )
        
        ems_id_value = payload_data.get("ems-id")
        if not ems_id_value:
            raise ValueError("ems-id is required for PUT")
        endpoint = "/endpoint-control/fctems-override/" + str(ems_id_value)

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
        ems_id: int | None = None,
        status: Literal["enable", "disable"] | None = None,
        name: str | None = None,
        dirty_reason: Literal["none", "mismatched-ems-sn"] | None = None,
        fortinetone_cloud_authentication: Literal["enable", "disable"] | None = None,
        cloud_authentication_access_key: Any | None = None,
        server: str | None = None,
        https_port: int | None = None,
        serial_number: str | None = None,
        tenant_id: str | None = None,
        source_ip: str | None = None,
        pull_sysinfo: Literal["enable", "disable"] | None = None,
        pull_vulnerabilities: Literal["enable", "disable"] | None = None,
        pull_tags: Literal["enable", "disable"] | None = None,
        pull_malware_hash: Literal["enable", "disable"] | None = None,
        capabilities: Literal["fabric-auth", "silent-approval", "websocket", "websocket-malware", "push-ca-certs", "common-tags-api", "tenant-id", "client-avatars", "single-vdom-connector", "fgt-sysinfo-api", "ztna-server-info", "used-tags"] | list[str] | None = None,
        call_timeout: int | None = None,
        out_of_sync_threshold: int | None = None,
        send_tags_to_all_vdoms: Literal["enable", "disable"] | None = None,
        websocket_override: Literal["enable", "disable"] | None = None,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = None,
        interface: str | None = None,
        trust_ca_cn: Literal["enable", "disable"] | None = None,
        verifying_ca: str | None = None,
        q_action: Literal["clone"] | None = None,
        q_nkey: str | None = None,
        q_scope: str | None = None,
        vdom: str | bool | None = None,
        error_mode: Literal["raise", "return", "print"] | None = None,
        error_format: Literal["detailed", "simple", "code_only"] | None = None,
    ):  # type: ignore[no-untyped-def]
        """
        Create new endpoint_control/fctems_override object.

        Configure FortiClient Enterprise Management Server (EMS) entries.

        Args:
            payload_dict: Complete object data as dict. Alternative to individual parameters.
            ems_id: EMS ID in order (1 - 7).
            status: Enable or disable this EMS configuration.
            name: FortiClient Enterprise Management Server (EMS) name.
            dirty_reason: Dirty Reason for FortiClient EMS.
            fortinetone_cloud_authentication: Enable/disable authentication of FortiClient EMS Cloud through FortiCloud account.
            cloud_authentication_access_key: FortiClient EMS Cloud multitenancy access key
            server: FortiClient EMS FQDN or IPv4 address.
            https_port: FortiClient EMS HTTPS access port number. (1 - 65535, default: 443).
            serial_number: EMS Serial Number.
            tenant_id: EMS Tenant ID.
            source_ip: REST API call source IP.
            pull_sysinfo: Enable/disable pulling SysInfo from EMS.
            pull_vulnerabilities: Enable/disable pulling vulnerabilities from EMS.
            pull_tags: Enable/disable pulling FortiClient user tags from EMS.
            pull_malware_hash: Enable/disable pulling FortiClient malware hash from EMS.
            capabilities: List of EMS capabilities.
            call_timeout: FortiClient EMS call timeout in seconds (1 - 180 seconds, default = 30).
            out_of_sync_threshold: Outdated resource threshold in seconds (10 - 3600, default = 180).
            send_tags_to_all_vdoms: Relax restrictions on tags to send all EMS tags to all VDOMs
            websocket_override: Enable/disable override behavior for how this FortiGate unit connects to EMS using a WebSocket connection.
            interface_select_method: Specify how to select outgoing interface to reach server.
            interface: Specify outgoing interface to reach server.
            trust_ca_cn: Enable/disable trust of the EMS certificate issuer(CA) and common name(CN) for certificate auto-renewal.
            verifying_ca: Lowest CA cert on Fortigate in verified EMS cert chain.
            vdom: Virtual domain name. Use True for global, string for specific VDOM.
            error_mode: Override client-level error_mode. "raise" raises exceptions, "return" returns error dict, "print" prints errors.
            error_format: Override client-level error_format. "detailed" provides full context, "simple" is concise, "code_only" returns just status code.

        Returns:
            FortiObject instance with created object. Use .dict, .json, or .raw to access as dictionary.

        Examples:
            >>> # Create using individual parameters
            >>> result = fgt.api.cmdb.endpoint_control_fctems_override.post(
            ...     name="example",
            ...     # ... other required fields
            ... )
            >>> print(f"Created ems-id: {result['results']}")
            
            >>> # Create using payload dict
            >>> payload = FctemsOverride.defaults()  # Start with defaults
            >>> payload['name'] = 'my-object'
            >>> result = fgt.api.cmdb.endpoint_control_fctems_override.post(payload_dict=payload)

        Note:
            Required fields: {{ ", ".join(FctemsOverride.required_fields()) }}
            
            Use FctemsOverride.help('field_name') to get field details.

        See Also:
            - get(): Retrieve objects
            - put(): Update existing object
            - set(): Intelligent create or update
        """
        # Build payload using helper function with auto-normalization
        # This automatically converts strings/lists to [{'name': '...'}] format for list fields
        # To disable auto-normalization, use build_cmdb_payload directly
        payload_data = build_api_payload(
            ems_id=ems_id,
            status=status,
            name=name,
            dirty_reason=dirty_reason,
            fortinetone_cloud_authentication=fortinetone_cloud_authentication,
            cloud_authentication_access_key=cloud_authentication_access_key,
            server=server,
            https_port=https_port,
            serial_number=serial_number,
            tenant_id=tenant_id,
            source_ip=source_ip,
            pull_sysinfo=pull_sysinfo,
            pull_vulnerabilities=pull_vulnerabilities,
            pull_tags=pull_tags,
            pull_malware_hash=pull_malware_hash,
            capabilities=capabilities,
            call_timeout=call_timeout,
            out_of_sync_threshold=out_of_sync_threshold,
            send_tags_to_all_vdoms=send_tags_to_all_vdoms,
            websocket_override=websocket_override,
            interface_select_method=interface_select_method,
            interface=interface,
            trust_ca_cn=trust_ca_cn,
            verifying_ca=verifying_ca,
            data=payload_dict,
        )

        # Check for deprecated fields and warn users
        from ._helpers.fctems_override import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/endpoint_control/fctems_override",
            )

        endpoint = "/endpoint-control/fctems-override"
        
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
        ems_id: int | None = None,
        q_scope: str | None = None,
        vdom: str | bool | None = None,
        error_mode: Literal["raise", "return", "print"] | None = None,
        error_format: Literal["detailed", "simple", "code_only"] | None = None,
    ):  # type: ignore[no-untyped-def]
        """
        Delete endpoint_control/fctems_override object.

        Configure FortiClient Enterprise Management Server (EMS) entries.

        Args:
            ems_id: Primary key identifier
            vdom: Virtual domain name
            error_mode: Override client-level error_mode. "raise" raises exceptions, "return" returns error dict, "print" prints errors.
            error_format: Override client-level error_format. "detailed" provides full context, "simple" is concise, "code_only" returns just status code.

        Returns:
            FortiObject instance. Use .dict, .json, or .raw to access as dictionary

        Raises:
            ValueError: If ems-id is not provided

        Examples:
            >>> # Delete specific object
            >>> result = fgt.api.cmdb.endpoint_control_fctems_override.delete(ems_id=1)
            
            >>> # Check for errors
            >>> if result.get('status') != 'success':
            ...     print(f"Delete failed: {result.get('error')}")

        See Also:
            - exists(): Check if object exists before deleting
            - get(): Retrieve object to verify it exists
        """
        if not ems_id:
            raise ValueError("ems-id is required for DELETE")
        endpoint = "/endpoint-control/fctems-override/" + str(ems_id)

        # Add explicit query parameters for DELETE
        params: dict[str, Any] = {}
        if q_scope is not None:
            params["scope"] = q_scope
        
        return self._client.delete(
            "cmdb", endpoint, params=params, vdom=vdom
        )

    def exists(
        self,
        ems_id: int,
        vdom: str | bool | None = None,
    ) -> Union[bool, Coroutine[Any, Any, bool]]:
        """
        Check if endpoint_control/fctems_override object exists.

        Verifies whether an object exists by attempting to retrieve it and checking the response status.

        Args:
            ems_id: Primary key identifier
            vdom: Virtual domain name

        Returns:
            True if object exists, False otherwise

        Examples:
            >>> # Check if object exists before operations
            >>> if fgt.api.cmdb.endpoint_control_fctems_override.exists(ems_id=1):
            ...     print("Object exists")
            ... else:
            ...     print("Object not found")
            
            >>> # Conditional delete
            >>> if fgt.api.cmdb.endpoint_control_fctems_override.exists(ems_id=1):
            ...     fgt.api.cmdb.endpoint_control_fctems_override.delete(ems_id=1)

        See Also:
            - get(): Retrieve full object data
            - set(): Create or update automatically based on existence
        """
        # Use direct request with silent error handling to avoid logging 404s
        # This is expected behavior for exists() - 404 just means "doesn't exist"
        endpoint = "/endpoint_control/fctems_override"
        endpoint = f"{endpoint}/{ems_id}"
        
        # Make request with silent=True to suppress 404 error logging
        # (404 is expected when checking existence - it just means "doesn't exist")
        # Use _wrapped_client to access the underlying HTTPClient directly
        # (self._client is ResponseProcessingClient, _wrapped_client is HTTPClient)
        try:
            result = self._client._wrapped_client.get(
                "cmdb",
                endpoint,
                params=None,
                vdom=vdom,
                raw_json=True,
                silent=True,
            )
            
            if isinstance(result, dict):
                # Synchronous response - check status
                return result.get("status") == "success"
            else:
                # Asynchronous response
                async def _check() -> bool:
                    r = await result
                    return r.get("status") == "success"
                return _check()
        except Exception:
            # Any error (404, network, etc.) means we can't confirm existence
            return False


    def set(
        self,
        payload_dict: dict[str, Any] | None = None,
        ems_id: int | None = None,
        status: Literal["enable", "disable"] | None = None,
        name: str | None = None,
        dirty_reason: Literal["none", "mismatched-ems-sn"] | None = None,
        fortinetone_cloud_authentication: Literal["enable", "disable"] | None = None,
        cloud_authentication_access_key: Any | None = None,
        server: str | None = None,
        https_port: int | None = None,
        serial_number: str | None = None,
        tenant_id: str | None = None,
        source_ip: str | None = None,
        pull_sysinfo: Literal["enable", "disable"] | None = None,
        pull_vulnerabilities: Literal["enable", "disable"] | None = None,
        pull_tags: Literal["enable", "disable"] | None = None,
        pull_malware_hash: Literal["enable", "disable"] | None = None,
        capabilities: Literal["fabric-auth", "silent-approval", "websocket", "websocket-malware", "push-ca-certs", "common-tags-api", "tenant-id", "client-avatars", "single-vdom-connector", "fgt-sysinfo-api", "ztna-server-info", "used-tags"] | list[str] | list[dict[str, Any]] | None = None,
        call_timeout: int | None = None,
        out_of_sync_threshold: int | None = None,
        send_tags_to_all_vdoms: Literal["enable", "disable"] | None = None,
        websocket_override: Literal["enable", "disable"] | None = None,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = None,
        interface: str | None = None,
        trust_ca_cn: Literal["enable", "disable"] | None = None,
        verifying_ca: str | None = None,
        vdom: str | bool | None = None,
        error_mode: Literal["raise", "return", "print"] | None = None,
        error_format: Literal["detailed", "simple", "code_only"] | None = None,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Create or update endpoint_control/fctems_override object (intelligent operation).

        Automatically determines whether to create (POST) or update (PUT) based on
        whether the resource exists. Requires the primary key (ems-id) in the payload.

        Args:
            payload_dict: Resource data including ems-id (primary key)
            ems_id: Field ems-id
            status: Field status
            name: Field name
            dirty_reason: Field dirty-reason
            fortinetone_cloud_authentication: Field fortinetone-cloud-authentication
            cloud_authentication_access_key: Field cloud-authentication-access-key
            server: Field server
            https_port: Field https-port
            serial_number: Field serial-number
            tenant_id: Field tenant-id
            source_ip: Field source-ip
            pull_sysinfo: Field pull-sysinfo
            pull_vulnerabilities: Field pull-vulnerabilities
            pull_tags: Field pull-tags
            pull_malware_hash: Field pull-malware-hash
            capabilities: Field capabilities
            call_timeout: Field call-timeout
            out_of_sync_threshold: Field out-of-sync-threshold
            send_tags_to_all_vdoms: Field send-tags-to-all-vdoms
            websocket_override: Field websocket-override
            interface_select_method: Field interface-select-method
            interface: Field interface
            trust_ca_cn: Field trust-ca-cn
            verifying_ca: Field verifying-ca
            vdom: Virtual domain name
            **kwargs: Additional parameters passed to PUT or POST

        Returns:
            FortiObject instance. Use .dict, .json, or .raw to access as dictionary

        Raises:
            ValueError: If ems-id is missing from payload

        Examples:
            >>> # Intelligent create or update using field parameters
            >>> result = fgt.api.cmdb.endpoint_control_fctems_override.set(
            ...     ems_id=1,
            ...     # ... other fields
            ... )
            
            >>> # Or using payload dict
            >>> payload = {
            ...     "ems-id": 1,
            ...     "field1": "value1",
            ...     "field2": "value2",
            ... }
            >>> result = fgt.api.cmdb.endpoint_control_fctems_override.set(payload_dict=payload)
            >>> # Will POST if object doesn't exist, PUT if it does
            
            >>> # Idempotent configuration
            >>> for obj_data in configuration_list:
            ...     fgt.api.cmdb.endpoint_control_fctems_override.set(payload_dict=obj_data)
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
            ems_id=ems_id,
            status=status,
            name=name,
            dirty_reason=dirty_reason,
            fortinetone_cloud_authentication=fortinetone_cloud_authentication,
            cloud_authentication_access_key=cloud_authentication_access_key,
            server=server,
            https_port=https_port,
            serial_number=serial_number,
            tenant_id=tenant_id,
            source_ip=source_ip,
            pull_sysinfo=pull_sysinfo,
            pull_vulnerabilities=pull_vulnerabilities,
            pull_tags=pull_tags,
            pull_malware_hash=pull_malware_hash,
            capabilities=capabilities,
            call_timeout=call_timeout,
            out_of_sync_threshold=out_of_sync_threshold,
            send_tags_to_all_vdoms=send_tags_to_all_vdoms,
            websocket_override=websocket_override,
            interface_select_method=interface_select_method,
            interface=interface,
            trust_ca_cn=trust_ca_cn,
            verifying_ca=verifying_ca,
            data=payload_dict,
        )
        
        mkey_value = payload_data.get("ems-id")
        if not mkey_value:
            raise ValueError("ems-id is required for set()")
        
        # Check if resource exists
        if self.exists(ems_id=mkey_value, vdom=vdom):
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
        ems_id: int,
        action: Literal["before", "after"],
        reference_ems_id: int,
        vdom: str | bool | None = None,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Move endpoint_control/fctems_override object to a new position.
        
        Reorders objects by moving one before or after another.
        
        Args:
            ems_id: Identifier of object to move
            action: Move "before" or "after" reference object
            reference_ems_id: Identifier of reference object
            vdom: Virtual domain name
            **kwargs: Additional parameters
            
        Returns:
            API response dictionary
            
        Example:
            >>> # Move policy 100 before policy 50
            >>> fgt.api.cmdb.endpoint_control_fctems_override.move(
            ...     ems_id=100,
            ...     action="before",
            ...     reference_ems_id=50
            ... )
        """
        return self._client.request(
            method="PUT",
            path=f"/api/v2/cmdb/endpoint-control/fctems-override",
            params={
                "ems-id": ems_id,
                "action": "move",
                action: reference_ems_id,
                "vdom": vdom,
                **kwargs,
            },
        )

    # ========================================================================
    # Action: Clone
    # ========================================================================
    
    def clone(
        self,
        ems_id: int,
        new_ems_id: int,
        vdom: str | bool | None = None,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Clone endpoint_control/fctems_override object.
        
        Creates a copy of an existing object with a new identifier.
        
        Args:
            ems_id: Identifier of object to clone
            new_ems_id: Identifier for the cloned object
            vdom: Virtual domain name
            **kwargs: Additional parameters
            
        Returns:
            API response dictionary
            
        Example:
            >>> # Clone an existing object
            >>> fgt.api.cmdb.endpoint_control_fctems_override.clone(
            ...     ems_id=1,
            ...     new_ems_id=100
            ... )
        """
        return self._client.request(
            method="POST",
            path=f"/api/v2/cmdb/endpoint-control/fctems-override",
            params={
                "ems-id": ems_id,
                "new_ems-id": new_ems_id,
                "action": "clone",
                "vdom": vdom,
                **kwargs,
            },
        )


