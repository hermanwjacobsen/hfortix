"""
FortiOS CMDB - System automation_action

Configuration endpoint for managing cmdb system/automation_action objects.

API Endpoints:
    GET    /cmdb/system/automation_action
    POST   /cmdb/system/automation_action
    PUT    /cmdb/system/automation_action/{identifier}
    DELETE /cmdb/system/automation_action/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.system_automation_action.get()
    >>>
    >>> # Create with auto-normalization (strings/lists converted automatically)
    >>> result = fgt.api.cmdb.system_automation_action.post(
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

class AutomationAction(CRUDEndpoint, MetadataMixin):
    """AutomationAction Operations."""
    
    # Configure metadata mixin to use this endpoint's helper module
    _helper_module_name = "automation_action"
    
    # ========================================================================
    # Table Fields Metadata (for normalization)
    # Auto-generated from schema - supports flexible input formats
    # ========================================================================
    _TABLE_FIELDS = {
        "email_to": {
            "mkey": "name",
            "required_fields": ['name'],
            "example": "[{'name': 'value'}]",
        },
        "http_headers": {
            "mkey": "id",
            "required_fields": ['key', 'value'],
            "example": "[{'key': 'value', 'value': 'value'}]",
        },
        "form_data": {
            "mkey": "id",
            "required_fields": ['key', 'value'],
            "example": "[{'key': 'value', 'value': 'value'}]",
        },
        "sdn_connector": {
            "mkey": "name",
            "required_fields": ['name'],
            "example": "[{'name': 'value'}]",
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
        """Initialize AutomationAction endpoint."""
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
        Retrieve system/automation_action configuration.

        Action for automation stitches.

        Args:
            name: String identifier to retrieve specific object.
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
            >>> # Get all system/automation_action objects
            >>> result = fgt.api.cmdb.system_automation_action.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get specific system/automation_action by name
            >>> result = fgt.api.cmdb.system_automation_action.get(name=1)
            >>> print(result['results'])
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.system_automation_action.get(
            ...     filter=["name==test", "status==enable"]
            ... )
            
            >>> # Get with pagination
            >>> result = fgt.api.cmdb.system_automation_action.get(
            ...     start=0, count=100
            ... )
            
            >>> # Get schema information  
            >>> schema = fgt.api.cmdb.system_automation_action.get_schema()

        See Also:
            - post(): Create new system/automation_action object
            - put(): Update existing system/automation_action object
            - delete(): Remove system/automation_action object
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
            endpoint = "/system/automation-action/" + str(name)
            unwrap_single = True
        else:
            endpoint = "/system/automation-action"
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
            >>> schema = fgt.api.cmdb.system_automation_action.get_schema()
            >>> print(schema['results'])
            
            >>> # Get JSON Schema format (if supported)
            >>> json_schema = fgt.api.cmdb.system_automation_action.get_schema(format="json-schema")
        
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
        name: str | None = None,
        description: str | None = None,
        action_type: Literal["email", "fortiexplorer-notification", "alert", "disable-ssid", "system-actions", "quarantine", "quarantine-forticlient", "quarantine-nsx", "quarantine-fortinac", "ban-ip", "aws-lambda", "azure-function", "google-cloud-function", "alicloud-function", "webhook", "cli-script", "diagnose-script", "regular-expression", "slack-notification", "microsoft-teams-notification"] | None = None,
        system_action: Literal["reboot", "shutdown", "backup-config"] | None = None,
        tls_certificate: str | None = None,
        forticare_email: Literal["enable", "disable"] | None = None,
        email_to: str | list[str] | list[dict[str, Any]] | None = None,
        email_from: str | None = None,
        email_subject: str | None = None,
        minimum_interval: int | None = None,
        aws_api_key: Any | None = None,
        azure_function_authorization: Literal["anonymous", "function", "admin"] | None = None,
        azure_api_key: Any | None = None,
        alicloud_function_authorization: Literal["anonymous", "function"] | None = None,
        alicloud_access_key_id: str | None = None,
        alicloud_access_key_secret: Any | None = None,
        message_type: Literal["text", "json", "form-data"] | None = None,
        message: str | None = None,
        replacement_message: Literal["enable", "disable"] | None = None,
        replacemsg_group: str | None = None,
        protocol: Literal["http", "https"] | None = None,
        method: Literal["post", "put", "get", "patch", "delete"] | None = None,
        uri: str | None = None,
        http_body: str | None = None,
        port: int | None = None,
        http_headers: str | list[str] | list[dict[str, Any]] | None = None,
        form_data: str | list[str] | list[dict[str, Any]] | None = None,
        verify_host_cert: Literal["enable", "disable"] | None = None,
        script: str | None = None,
        output_size: int | None = None,
        timeout: int | None = None,
        duration: int | None = None,
        output_interval: int | None = None,
        file_only: Literal["enable", "disable"] | None = None,
        execute_security_fabric: Literal["enable", "disable"] | None = None,
        accprofile: str | None = None,
        regular_expression: str | None = None,
        log_debug_print: Literal["enable", "disable"] | None = None,
        security_tag: str | None = None,
        sdn_connector: str | list[str] | list[dict[str, Any]] | None = None,
        q_action: Literal["move"] | None = None,
        q_before: str | None = None,
        q_after: str | None = None,
        q_scope: str | None = None,
        vdom: str | bool | None = None,
        error_mode: Literal["raise", "return", "print"] | None = None,
        error_format: Literal["detailed", "simple", "code_only"] | None = None,
    ):  # type: ignore[no-untyped-def]
        """
        Update existing system/automation_action object.

        Action for automation stitches.

        Args:
            payload_dict: Object data as dict. Must include name (primary key).
            name: Name.
            description: Description.
            action_type: Action type.
            system_action: System action type.
            tls_certificate: Custom TLS certificate for API request.
            forticare_email: Enable/disable use of your FortiCare email address as the email-to address.
            email_to: Email addresses.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            email_from: Email sender name.
            email_subject: Email subject.
            minimum_interval: Limit execution to no more than once in this interval (in seconds).
            aws_api_key: AWS API Gateway API key.
            azure_function_authorization: Azure function authorization level.
            azure_api_key: Azure function API key.
            alicloud_function_authorization: AliCloud function authorization type.
            alicloud_access_key_id: AliCloud AccessKey ID.
            alicloud_access_key_secret: AliCloud AccessKey secret.
            message_type: Message type.
            message: Message content.
            replacement_message: Enable/disable replacement message.
            replacemsg_group: Replacement message group.
            protocol: Request protocol.
            method: Request method (POST, PUT, GET, PATCH or DELETE).
            uri: Request API URI.
            http_body: Request body (if necessary). Should be serialized json string.
            port: Protocol port.
            http_headers: Request headers.
                Default format: [{'key': 'value', 'value': 'value'}]
                Required format: List of dicts with keys: key, value
                  (String format not allowed due to multiple required fields)
            form_data: Form data parts for content type multipart/form-data.
                Default format: [{'key': 'value', 'value': 'value'}]
                Required format: List of dicts with keys: key, value
                  (String format not allowed due to multiple required fields)
            verify_host_cert: Enable/disable verification of the remote host certificate.
            script: CLI script.
            output_size: Number of megabytes to limit script output to (1 - 1024, default = 10).
            timeout: Maximum running time for this script in seconds (0 = no timeout).
            duration: Maximum running time for this script in seconds.
            output_interval: Collect the outputs for each output-interval in seconds (0 = no intermediate output).
            file_only: Enable/disable the output in files only.
            execute_security_fabric: Enable/disable execution of CLI script on all or only one FortiGate unit in the Security Fabric.
            accprofile: Access profile for CLI script action to access FortiGate features.
            regular_expression: Regular expression string.
            log_debug_print: Enable/disable logging debug print output from diagnose action.
            security_tag: NSX security tag.
            sdn_connector: NSX SDN connector names.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            vdom: Virtual domain name.
            error_mode: Override client-level error_mode. "raise" raises exceptions, "return" returns error dict, "print" prints errors.
            error_format: Override client-level error_format. "detailed" provides full context, "simple" is concise, "code_only" returns just status code.

        Returns:
            FortiObject instance. Use .dict, .json, or .raw to access as dictionary.

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.system_automation_action.put(
            ...     name=1,
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "name": 1,
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.system_automation_action.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Apply normalization for table fields (supports flexible input formats)
        if email_to is not None:
            email_to = normalize_table_field(
                email_to,
                mkey="name",
                required_fields=['name'],
                field_name="email_to",
                example="[{'name': 'value'}]",
            )
        if http_headers is not None:
            http_headers = normalize_table_field(
                http_headers,
                mkey="id",
                required_fields=['key', 'value'],
                field_name="http_headers",
                example="[{'key': 'value', 'value': 'value'}]",
            )
        if form_data is not None:
            form_data = normalize_table_field(
                form_data,
                mkey="id",
                required_fields=['key', 'value'],
                field_name="form_data",
                example="[{'key': 'value', 'value': 'value'}]",
            )
        if sdn_connector is not None:
            sdn_connector = normalize_table_field(
                sdn_connector,
                mkey="name",
                required_fields=['name'],
                field_name="sdn_connector",
                example="[{'name': 'value'}]",
            )
        
        # Build payload using helper function with auto-normalization
        # This automatically converts strings/lists to [{'name': '...'}] format for list fields
        # To disable auto-normalization, use build_cmdb_payload directly
        payload_data = build_api_payload(
            name=name,
            description=description,
            action_type=action_type,
            system_action=system_action,
            tls_certificate=tls_certificate,
            forticare_email=forticare_email,
            email_to=email_to,
            email_from=email_from,
            email_subject=email_subject,
            minimum_interval=minimum_interval,
            aws_api_key=aws_api_key,
            azure_function_authorization=azure_function_authorization,
            azure_api_key=azure_api_key,
            alicloud_function_authorization=alicloud_function_authorization,
            alicloud_access_key_id=alicloud_access_key_id,
            alicloud_access_key_secret=alicloud_access_key_secret,
            message_type=message_type,
            message=message,
            replacement_message=replacement_message,
            replacemsg_group=replacemsg_group,
            protocol=protocol,
            method=method,
            uri=uri,
            http_body=http_body,
            port=port,
            http_headers=http_headers,
            form_data=form_data,
            verify_host_cert=verify_host_cert,
            script=script,
            output_size=output_size,
            timeout=timeout,
            duration=duration,
            output_interval=output_interval,
            file_only=file_only,
            execute_security_fabric=execute_security_fabric,
            accprofile=accprofile,
            regular_expression=regular_expression,
            log_debug_print=log_debug_print,
            security_tag=security_tag,
            sdn_connector=sdn_connector,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.automation_action import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/system/automation_action",
            )
        
        name_value = payload_data.get("name")
        if not name_value:
            raise ValueError("name is required for PUT")
        endpoint = "/system/automation-action/" + str(name_value)

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
        name: str | None = None,
        description: str | None = None,
        action_type: Literal["email", "fortiexplorer-notification", "alert", "disable-ssid", "system-actions", "quarantine", "quarantine-forticlient", "quarantine-nsx", "quarantine-fortinac", "ban-ip", "aws-lambda", "azure-function", "google-cloud-function", "alicloud-function", "webhook", "cli-script", "diagnose-script", "regular-expression", "slack-notification", "microsoft-teams-notification"] | None = None,
        system_action: Literal["reboot", "shutdown", "backup-config"] | None = None,
        tls_certificate: str | None = None,
        forticare_email: Literal["enable", "disable"] | None = None,
        email_to: str | list[str] | list[dict[str, Any]] | None = None,
        email_from: str | None = None,
        email_subject: str | None = None,
        minimum_interval: int | None = None,
        aws_api_key: Any | None = None,
        azure_function_authorization: Literal["anonymous", "function", "admin"] | None = None,
        azure_api_key: Any | None = None,
        alicloud_function_authorization: Literal["anonymous", "function"] | None = None,
        alicloud_access_key_id: str | None = None,
        alicloud_access_key_secret: Any | None = None,
        message_type: Literal["text", "json", "form-data"] | None = None,
        message: str | None = None,
        replacement_message: Literal["enable", "disable"] | None = None,
        replacemsg_group: str | None = None,
        protocol: Literal["http", "https"] | None = None,
        method: Literal["post", "put", "get", "patch", "delete"] | None = None,
        uri: str | None = None,
        http_body: str | None = None,
        port: int | None = None,
        http_headers: str | list[str] | list[dict[str, Any]] | None = None,
        form_data: str | list[str] | list[dict[str, Any]] | None = None,
        verify_host_cert: Literal["enable", "disable"] | None = None,
        script: str | None = None,
        output_size: int | None = None,
        timeout: int | None = None,
        duration: int | None = None,
        output_interval: int | None = None,
        file_only: Literal["enable", "disable"] | None = None,
        execute_security_fabric: Literal["enable", "disable"] | None = None,
        accprofile: str | None = None,
        regular_expression: str | None = None,
        log_debug_print: Literal["enable", "disable"] | None = None,
        security_tag: str | None = None,
        sdn_connector: str | list[str] | list[dict[str, Any]] | None = None,
        q_action: Literal["clone"] | None = None,
        q_nkey: str | None = None,
        q_scope: str | None = None,
        vdom: str | bool | None = None,
        error_mode: Literal["raise", "return", "print"] | None = None,
        error_format: Literal["detailed", "simple", "code_only"] | None = None,
    ):  # type: ignore[no-untyped-def]
        """
        Create new system/automation_action object.

        Action for automation stitches.

        Args:
            payload_dict: Complete object data as dict. Alternative to individual parameters.
            name: Name.
            description: Description.
            action_type: Action type.
            system_action: System action type.
            tls_certificate: Custom TLS certificate for API request.
            forticare_email: Enable/disable use of your FortiCare email address as the email-to address.
            email_to: Email addresses.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            email_from: Email sender name.
            email_subject: Email subject.
            minimum_interval: Limit execution to no more than once in this interval (in seconds).
            aws_api_key: AWS API Gateway API key.
            azure_function_authorization: Azure function authorization level.
            azure_api_key: Azure function API key.
            alicloud_function_authorization: AliCloud function authorization type.
            alicloud_access_key_id: AliCloud AccessKey ID.
            alicloud_access_key_secret: AliCloud AccessKey secret.
            message_type: Message type.
            message: Message content.
            replacement_message: Enable/disable replacement message.
            replacemsg_group: Replacement message group.
            protocol: Request protocol.
            method: Request method (POST, PUT, GET, PATCH or DELETE).
            uri: Request API URI.
            http_body: Request body (if necessary). Should be serialized json string.
            port: Protocol port.
            http_headers: Request headers.
                Default format: [{'key': 'value', 'value': 'value'}]
                Required format: List of dicts with keys: key, value
                  (String format not allowed due to multiple required fields)
            form_data: Form data parts for content type multipart/form-data.
                Default format: [{'key': 'value', 'value': 'value'}]
                Required format: List of dicts with keys: key, value
                  (String format not allowed due to multiple required fields)
            verify_host_cert: Enable/disable verification of the remote host certificate.
            script: CLI script.
            output_size: Number of megabytes to limit script output to (1 - 1024, default = 10).
            timeout: Maximum running time for this script in seconds (0 = no timeout).
            duration: Maximum running time for this script in seconds.
            output_interval: Collect the outputs for each output-interval in seconds (0 = no intermediate output).
            file_only: Enable/disable the output in files only.
            execute_security_fabric: Enable/disable execution of CLI script on all or only one FortiGate unit in the Security Fabric.
            accprofile: Access profile for CLI script action to access FortiGate features.
            regular_expression: Regular expression string.
            log_debug_print: Enable/disable logging debug print output from diagnose action.
            security_tag: NSX security tag.
            sdn_connector: NSX SDN connector names.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            vdom: Virtual domain name. Use True for global, string for specific VDOM.
            error_mode: Override client-level error_mode. "raise" raises exceptions, "return" returns error dict, "print" prints errors.
            error_format: Override client-level error_format. "detailed" provides full context, "simple" is concise, "code_only" returns just status code.

        Returns:
            FortiObject instance with created object. Use .dict, .json, or .raw to access as dictionary.

        Examples:
            >>> # Create using individual parameters
            >>> result = fgt.api.cmdb.system_automation_action.post(
            ...     name="example",
            ...     # ... other required fields
            ... )
            >>> print(f"Created name: {result['results']}")
            
            >>> # Create using payload dict
            >>> payload = AutomationAction.defaults()  # Start with defaults
            >>> payload['name'] = 'my-object'
            >>> result = fgt.api.cmdb.system_automation_action.post(payload_dict=payload)

        Note:
            Required fields: {{ ", ".join(AutomationAction.required_fields()) }}
            
            Use AutomationAction.help('field_name') to get field details.

        See Also:
            - get(): Retrieve objects
            - put(): Update existing object
            - set(): Intelligent create or update
        """
        # Apply normalization for table fields (supports flexible input formats)
        if email_to is not None:
            email_to = normalize_table_field(
                email_to,
                mkey="name",
                required_fields=['name'],
                field_name="email_to",
                example="[{'name': 'value'}]",
            )
        if http_headers is not None:
            http_headers = normalize_table_field(
                http_headers,
                mkey="id",
                required_fields=['key', 'value'],
                field_name="http_headers",
                example="[{'key': 'value', 'value': 'value'}]",
            )
        if form_data is not None:
            form_data = normalize_table_field(
                form_data,
                mkey="id",
                required_fields=['key', 'value'],
                field_name="form_data",
                example="[{'key': 'value', 'value': 'value'}]",
            )
        if sdn_connector is not None:
            sdn_connector = normalize_table_field(
                sdn_connector,
                mkey="name",
                required_fields=['name'],
                field_name="sdn_connector",
                example="[{'name': 'value'}]",
            )
        
        # Build payload using helper function with auto-normalization
        # This automatically converts strings/lists to [{'name': '...'}] format for list fields
        # To disable auto-normalization, use build_cmdb_payload directly
        payload_data = build_api_payload(
            name=name,
            description=description,
            action_type=action_type,
            system_action=system_action,
            tls_certificate=tls_certificate,
            forticare_email=forticare_email,
            email_to=email_to,
            email_from=email_from,
            email_subject=email_subject,
            minimum_interval=minimum_interval,
            aws_api_key=aws_api_key,
            azure_function_authorization=azure_function_authorization,
            azure_api_key=azure_api_key,
            alicloud_function_authorization=alicloud_function_authorization,
            alicloud_access_key_id=alicloud_access_key_id,
            alicloud_access_key_secret=alicloud_access_key_secret,
            message_type=message_type,
            message=message,
            replacement_message=replacement_message,
            replacemsg_group=replacemsg_group,
            protocol=protocol,
            method=method,
            uri=uri,
            http_body=http_body,
            port=port,
            http_headers=http_headers,
            form_data=form_data,
            verify_host_cert=verify_host_cert,
            script=script,
            output_size=output_size,
            timeout=timeout,
            duration=duration,
            output_interval=output_interval,
            file_only=file_only,
            execute_security_fabric=execute_security_fabric,
            accprofile=accprofile,
            regular_expression=regular_expression,
            log_debug_print=log_debug_print,
            security_tag=security_tag,
            sdn_connector=sdn_connector,
            data=payload_dict,
        )

        # Check for deprecated fields and warn users
        from ._helpers.automation_action import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/system/automation_action",
            )

        endpoint = "/system/automation-action"
        
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
        name: str | None = None,
        q_scope: str | None = None,
        vdom: str | bool | None = None,
        error_mode: Literal["raise", "return", "print"] | None = None,
        error_format: Literal["detailed", "simple", "code_only"] | None = None,
    ):  # type: ignore[no-untyped-def]
        """
        Delete system/automation_action object.

        Action for automation stitches.

        Args:
            name: Primary key identifier
            vdom: Virtual domain name
            error_mode: Override client-level error_mode. "raise" raises exceptions, "return" returns error dict, "print" prints errors.
            error_format: Override client-level error_format. "detailed" provides full context, "simple" is concise, "code_only" returns just status code.

        Returns:
            FortiObject instance. Use .dict, .json, or .raw to access as dictionary

        Raises:
            ValueError: If name is not provided

        Examples:
            >>> # Delete specific object
            >>> result = fgt.api.cmdb.system_automation_action.delete(name=1)
            
            >>> # Check for errors
            >>> if result.get('status') != 'success':
            ...     print(f"Delete failed: {result.get('error')}")

        See Also:
            - exists(): Check if object exists before deleting
            - get(): Retrieve object to verify it exists
        """
        if not name:
            raise ValueError("name is required for DELETE")
        endpoint = "/system/automation-action/" + str(name)

        # Add explicit query parameters for DELETE
        params: dict[str, Any] = {}
        if q_scope is not None:
            params["scope"] = q_scope
        
        return self._client.delete(
            "cmdb", endpoint, params=params, vdom=vdom
        )

    def exists(
        self,
        name: str,
        vdom: str | bool | None = None,
    ) -> Union[bool, Coroutine[Any, Any, bool]]:
        """
        Check if system/automation_action object exists.

        Verifies whether an object exists by attempting to retrieve it and checking the response status.

        Args:
            name: Primary key identifier
            vdom: Virtual domain name

        Returns:
            True if object exists, False otherwise

        Examples:
            >>> # Check if object exists before operations
            >>> if fgt.api.cmdb.system_automation_action.exists(name=1):
            ...     print("Object exists")
            ... else:
            ...     print("Object not found")
            
            >>> # Conditional delete
            >>> if fgt.api.cmdb.system_automation_action.exists(name=1):
            ...     fgt.api.cmdb.system_automation_action.delete(name=1)

        See Also:
            - get(): Retrieve full object data
            - set(): Create or update automatically based on existence
        """
        # Use direct request with silent error handling to avoid logging 404s
        # This is expected behavior for exists() - 404 just means "doesn't exist"
        endpoint = "/system/automation_action"
        endpoint = f"{endpoint}/{name}"
        
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
        name: str | None = None,
        description: str | None = None,
        action_type: Literal["email", "fortiexplorer-notification", "alert", "disable-ssid", "system-actions", "quarantine", "quarantine-forticlient", "quarantine-nsx", "quarantine-fortinac", "ban-ip", "aws-lambda", "azure-function", "google-cloud-function", "alicloud-function", "webhook", "cli-script", "diagnose-script", "regular-expression", "slack-notification", "microsoft-teams-notification"] | None = None,
        system_action: Literal["reboot", "shutdown", "backup-config"] | None = None,
        tls_certificate: str | None = None,
        forticare_email: Literal["enable", "disable"] | None = None,
        email_to: str | list[str] | list[dict[str, Any]] | None = None,
        email_from: str | None = None,
        email_subject: str | None = None,
        minimum_interval: int | None = None,
        aws_api_key: Any | None = None,
        azure_function_authorization: Literal["anonymous", "function", "admin"] | None = None,
        azure_api_key: Any | None = None,
        alicloud_function_authorization: Literal["anonymous", "function"] | None = None,
        alicloud_access_key_id: str | None = None,
        alicloud_access_key_secret: Any | None = None,
        message_type: Literal["text", "json", "form-data"] | None = None,
        message: str | None = None,
        replacement_message: Literal["enable", "disable"] | None = None,
        replacemsg_group: str | None = None,
        protocol: Literal["http", "https"] | None = None,
        method: Literal["post", "put", "get", "patch", "delete"] | None = None,
        uri: str | None = None,
        http_body: str | None = None,
        port: int | None = None,
        http_headers: str | list[str] | list[dict[str, Any]] | None = None,
        form_data: str | list[str] | list[dict[str, Any]] | None = None,
        verify_host_cert: Literal["enable", "disable"] | None = None,
        script: str | None = None,
        output_size: int | None = None,
        timeout: int | None = None,
        duration: int | None = None,
        output_interval: int | None = None,
        file_only: Literal["enable", "disable"] | None = None,
        execute_security_fabric: Literal["enable", "disable"] | None = None,
        accprofile: str | None = None,
        regular_expression: str | None = None,
        log_debug_print: Literal["enable", "disable"] | None = None,
        security_tag: str | None = None,
        sdn_connector: str | list[str] | list[dict[str, Any]] | None = None,
        vdom: str | bool | None = None,
        error_mode: Literal["raise", "return", "print"] | None = None,
        error_format: Literal["detailed", "simple", "code_only"] | None = None,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Create or update system/automation_action object (intelligent operation).

        Automatically determines whether to create (POST) or update (PUT) based on
        whether the resource exists. Requires the primary key (name) in the payload.

        Args:
            payload_dict: Resource data including name (primary key)
            name: Field name
            description: Field description
            action_type: Field action-type
            system_action: Field system-action
            tls_certificate: Field tls-certificate
            forticare_email: Field forticare-email
            email_to: Field email-to
            email_from: Field email-from
            email_subject: Field email-subject
            minimum_interval: Field minimum-interval
            aws_api_key: Field aws-api-key
            azure_function_authorization: Field azure-function-authorization
            azure_api_key: Field azure-api-key
            alicloud_function_authorization: Field alicloud-function-authorization
            alicloud_access_key_id: Field alicloud-access-key-id
            alicloud_access_key_secret: Field alicloud-access-key-secret
            message_type: Field message-type
            message: Field message
            replacement_message: Field replacement-message
            replacemsg_group: Field replacemsg-group
            protocol: Field protocol
            method: Field method
            uri: Field uri
            http_body: Field http-body
            port: Field port
            http_headers: Field http-headers
            form_data: Field form-data
            verify_host_cert: Field verify-host-cert
            script: Field script
            output_size: Field output-size
            timeout: Field timeout
            duration: Field duration
            output_interval: Field output-interval
            file_only: Field file-only
            execute_security_fabric: Field execute-security-fabric
            accprofile: Field accprofile
            regular_expression: Field regular-expression
            log_debug_print: Field log-debug-print
            security_tag: Field security-tag
            sdn_connector: Field sdn-connector
            vdom: Virtual domain name
            **kwargs: Additional parameters passed to PUT or POST

        Returns:
            FortiObject instance. Use .dict, .json, or .raw to access as dictionary

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Intelligent create or update using field parameters
            >>> result = fgt.api.cmdb.system_automation_action.set(
            ...     name=1,
            ...     # ... other fields
            ... )
            
            >>> # Or using payload dict
            >>> payload = {
            ...     "name": 1,
            ...     "field1": "value1",
            ...     "field2": "value2",
            ... }
            >>> result = fgt.api.cmdb.system_automation_action.set(payload_dict=payload)
            >>> # Will POST if object doesn't exist, PUT if it does
            
            >>> # Idempotent configuration
            >>> for obj_data in configuration_list:
            ...     fgt.api.cmdb.system_automation_action.set(payload_dict=obj_data)
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
            name=name,
            description=description,
            action_type=action_type,
            system_action=system_action,
            tls_certificate=tls_certificate,
            forticare_email=forticare_email,
            email_to=email_to,
            email_from=email_from,
            email_subject=email_subject,
            minimum_interval=minimum_interval,
            aws_api_key=aws_api_key,
            azure_function_authorization=azure_function_authorization,
            azure_api_key=azure_api_key,
            alicloud_function_authorization=alicloud_function_authorization,
            alicloud_access_key_id=alicloud_access_key_id,
            alicloud_access_key_secret=alicloud_access_key_secret,
            message_type=message_type,
            message=message,
            replacement_message=replacement_message,
            replacemsg_group=replacemsg_group,
            protocol=protocol,
            method=method,
            uri=uri,
            http_body=http_body,
            port=port,
            http_headers=http_headers,
            form_data=form_data,
            verify_host_cert=verify_host_cert,
            script=script,
            output_size=output_size,
            timeout=timeout,
            duration=duration,
            output_interval=output_interval,
            file_only=file_only,
            execute_security_fabric=execute_security_fabric,
            accprofile=accprofile,
            regular_expression=regular_expression,
            log_debug_print=log_debug_print,
            security_tag=security_tag,
            sdn_connector=sdn_connector,
            data=payload_dict,
        )
        
        mkey_value = payload_data.get("name")
        if not mkey_value:
            raise ValueError("name is required for set()")
        
        # Check if resource exists
        if self.exists(name=mkey_value, vdom=vdom):
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
        name: str,
        action: Literal["before", "after"],
        reference_name: str,
        vdom: str | bool | None = None,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Move system/automation_action object to a new position.
        
        Reorders objects by moving one before or after another.
        
        Args:
            name: Identifier of object to move
            action: Move "before" or "after" reference object
            reference_name: Identifier of reference object
            vdom: Virtual domain name
            **kwargs: Additional parameters
            
        Returns:
            API response dictionary
            
        Example:
            >>> # Move policy 100 before policy 50
            >>> fgt.api.cmdb.system_automation_action.move(
            ...     name=100,
            ...     action="before",
            ...     reference_name=50
            ... )
        """
        return self._client.request(
            method="PUT",
            path=f"/api/v2/cmdb/system/automation-action",
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
        Clone system/automation_action object.
        
        Creates a copy of an existing object with a new identifier.
        
        Args:
            name: Identifier of object to clone
            new_name: Identifier for the cloned object
            vdom: Virtual domain name
            **kwargs: Additional parameters
            
        Returns:
            API response dictionary
            
        Example:
            >>> # Clone an existing object
            >>> fgt.api.cmdb.system_automation_action.clone(
            ...     name=1,
            ...     new_name=100
            ... )
        """
        return self._client.request(
            method="POST",
            path=f"/api/v2/cmdb/system/automation-action",
            params={
                "name": name,
                "new_name": new_name,
                "action": "clone",
                "vdom": vdom,
                **kwargs,
            },
        )


