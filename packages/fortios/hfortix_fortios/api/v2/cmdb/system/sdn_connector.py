"""
FortiOS CMDB - System sdn_connector

Configuration endpoint for managing cmdb system/sdn_connector objects.

API Endpoints:
    GET    /cmdb/system/sdn_connector
    POST   /cmdb/system/sdn_connector
    PUT    /cmdb/system/sdn_connector/{identifier}
    DELETE /cmdb/system/sdn_connector/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.system_sdn_connector.get()
    >>>
    >>> # Create with auto-normalization (strings/lists converted automatically)
    >>> result = fgt.api.cmdb.system_sdn_connector.post(
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

class SdnConnector(CRUDEndpoint, MetadataMixin):
    """SdnConnector Operations."""
    
    # Configure metadata mixin to use this endpoint's helper module
    _helper_module_name = "sdn_connector"
    
    # ========================================================================
    # Table Fields Metadata (for normalization)
    # Auto-generated from schema - supports flexible input formats
    # ========================================================================
    _TABLE_FIELDS = {
        "server_list": {
            "mkey": "ip",
            "required_fields": ['ip'],
            "example": "[{'ip': '192.168.1.10'}]",
        },
        "external_account_list": {
            "mkey": "role-arn",
            "required_fields": ['role-arn', 'region-list'],
            "example": "[{'role-arn': 'value', 'region-list': 'value'}]",
        },
        "nic": {
            "mkey": "name",
            "required_fields": ['name'],
            "example": "[{'name': 'value'}]",
        },
        "route_table": {
            "mkey": "name",
            "required_fields": ['name'],
            "example": "[{'name': 'value'}]",
        },
        "compartment_list": {
            "mkey": "compartment-id",
            "required_fields": ['compartment-id'],
            "example": "[{'compartment-id': 'value'}]",
        },
        "oci_region_list": {
            "mkey": "region",
            "required_fields": ['region'],
            "example": "[{'region': 'value'}]",
        },
        "external_ip": {
            "mkey": "name",
            "required_fields": ['name'],
            "example": "[{'name': 'value'}]",
        },
        "route": {
            "mkey": "name",
            "required_fields": ['name'],
            "example": "[{'name': 'value'}]",
        },
        "gcp_project_list": {
            "mkey": "id",
            "required_fields": ['id'],
            "example": "[{'id': 1}]",
        },
        "forwarding_rule": {
            "mkey": "rule-name",
            "required_fields": ['rule-name', 'target'],
            "example": "[{'rule-name': 'value', 'target': 'value'}]",
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
        """Initialize SdnConnector endpoint."""
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
        Retrieve system/sdn_connector configuration.

        Configure connection to SDN Connector.

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
            >>> # Get all system/sdn_connector objects
            >>> result = fgt.api.cmdb.system_sdn_connector.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get specific system/sdn_connector by name
            >>> result = fgt.api.cmdb.system_sdn_connector.get(name=1)
            >>> print(result['results'])
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.system_sdn_connector.get(
            ...     filter=["name==test", "status==enable"]
            ... )
            
            >>> # Get with pagination
            >>> result = fgt.api.cmdb.system_sdn_connector.get(
            ...     start=0, count=100
            ... )
            
            >>> # Get schema information  
            >>> schema = fgt.api.cmdb.system_sdn_connector.get_schema()

        See Also:
            - post(): Create new system/sdn_connector object
            - put(): Update existing system/sdn_connector object
            - delete(): Remove system/sdn_connector object
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
            endpoint = "/system/sdn-connector/" + str(name)
            unwrap_single = True
        else:
            endpoint = "/system/sdn-connector"
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
            >>> schema = fgt.api.cmdb.system_sdn_connector.get_schema()
            >>> print(schema['results'])
            
            >>> # Get JSON Schema format (if supported)
            >>> json_schema = fgt.api.cmdb.system_sdn_connector.get_schema(format="json-schema")
        
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
        status: Literal["disable", "enable"] | None = None,
        type: Literal["aci", "alicloud", "aws", "azure", "gcp", "nsx", "nuage", "oci", "openstack", "kubernetes", "vmware", "sepm", "aci-direct", "ibm", "nutanix", "sap"] | None = None,
        proxy: str | None = None,
        use_metadata_iam: Literal["disable", "enable"] | None = None,
        microsoft_365: Literal["disable", "enable"] | None = None,
        ha_status: Literal["disable", "enable"] | None = None,
        verify_certificate: Literal["disable", "enable"] | None = None,
        server: str | None = None,
        server_list: str | list[str] | list[dict[str, Any]] | None = None,
        server_port: int | None = None,
        message_server_port: int | None = None,
        username: str | None = None,
        password: Any | None = None,
        vcenter_server: str | None = None,
        vcenter_username: str | None = None,
        vcenter_password: Any | None = None,
        access_key: str | None = None,
        secret_key: Any | None = None,
        region: str | None = None,
        vpc_id: str | None = None,
        alt_resource_ip: Literal["disable", "enable"] | None = None,
        external_account_list: str | list[str] | list[dict[str, Any]] | None = None,
        tenant_id: str | None = None,
        client_id: str | None = None,
        client_secret: Any | None = None,
        subscription_id: str | None = None,
        resource_group: str | None = None,
        login_endpoint: str | None = None,
        resource_url: str | None = None,
        azure_region: Literal["global", "china", "germany", "usgov", "local"] | None = None,
        nic: str | list[str] | list[dict[str, Any]] | None = None,
        route_table: str | list[str] | list[dict[str, Any]] | None = None,
        user_id: str | None = None,
        compartment_list: str | list[str] | list[dict[str, Any]] | None = None,
        oci_region_list: str | list[str] | list[dict[str, Any]] | None = None,
        oci_region_type: Literal["commercial", "government"] | None = None,
        oci_cert: str | None = None,
        oci_fingerprint: str | None = None,
        external_ip: str | list[str] | list[dict[str, Any]] | None = None,
        route: str | list[str] | list[dict[str, Any]] | None = None,
        gcp_project_list: str | list[str] | list[dict[str, Any]] | None = None,
        forwarding_rule: str | list[str] | list[dict[str, Any]] | None = None,
        service_account: str | None = None,
        private_key: str | None = None,
        secret_token: str | None = None,
        domain: str | None = None,
        group_name: str | None = None,
        server_cert: str | None = None,
        server_ca_cert: str | None = None,
        api_key: Any | None = None,
        ibm_region: Literal["dallas", "washington-dc", "london", "frankfurt", "sydney", "tokyo", "osaka", "toronto", "sao-paulo", "madrid"] | None = None,
        par_id: str | None = None,
        update_interval: int | None = None,
        q_action: Literal["move"] | None = None,
        q_before: str | None = None,
        q_after: str | None = None,
        q_scope: str | None = None,
        vdom: str | bool | None = None,
        error_mode: Literal["raise", "return", "print"] | None = None,
        error_format: Literal["detailed", "simple", "code_only"] | None = None,
    ):  # type: ignore[no-untyped-def]
        """
        Update existing system/sdn_connector object.

        Configure connection to SDN Connector.

        Args:
            payload_dict: Object data as dict. Must include name (primary key).
            name: SDN connector name.
            status: Enable/disable connection to the remote SDN connector.
            type: Type of SDN connector.
            proxy: SDN proxy.
            use_metadata_iam: Enable/disable use of IAM role from metadata to call API.
            microsoft_365: Enable to use as Microsoft 365 connector.
            ha_status: Enable/disable use for FortiGate HA service.
            verify_certificate: Enable/disable server certificate verification.
            vdom: Virtual domain name of the remote SDN connector.
            server: Server address of the remote SDN connector.
            server_list: Server address list of the remote SDN connector.
                Default format: [{'ip': '192.168.1.10'}]
                Supported formats:
                  - Single string: "value" → [{'ip': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'ip': 'val1'}, ...]
                  - List of dicts: [{'ip': '192.168.1.10'}] (recommended)
            server_port: Port number of the remote SDN connector.
            message_server_port: HTTP port number of the SAP message server.
            username: Username of the remote SDN connector as login credentials.
            password: Password of the remote SDN connector as login credentials.
            vcenter_server: vCenter server address for NSX quarantine.
            vcenter_username: vCenter server username for NSX quarantine.
            vcenter_password: vCenter server password for NSX quarantine.
            access_key: AWS / ACS access key ID.
            secret_key: AWS / ACS secret access key.
            region: AWS / ACS region name.
            vpc_id: AWS VPC ID.
            alt_resource_ip: Enable/disable AWS alternative resource IP.
            external_account_list: Configure AWS external account list.
                Default format: [{'role-arn': 'value', 'region-list': 'value'}]
                Required format: List of dicts with keys: role-arn, region-list
                  (String format not allowed due to multiple required fields)
            tenant_id: Tenant ID (directory ID).
            client_id: Azure client ID (application ID).
            client_secret: Azure client secret (application key).
            subscription_id: Azure subscription ID.
            resource_group: Azure resource group.
            login_endpoint: Azure Stack login endpoint.
            resource_url: Azure Stack resource URL.
            azure_region: Azure server region.
            nic: Configure Azure network interface.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            route_table: Configure Azure route table.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            user_id: User ID.
            compartment_list: Configure OCI compartment list.
                Default format: [{'compartment-id': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'compartment-id': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'compartment-id': 'val1'}, ...]
                  - List of dicts: [{'compartment-id': 'value'}] (recommended)
            oci_region_list: Configure OCI region list.
                Default format: [{'region': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'region': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'region': 'val1'}, ...]
                  - List of dicts: [{'region': 'value'}] (recommended)
            oci_region_type: OCI region type.
            oci_cert: OCI certificate.
            oci_fingerprint: OCI pubkey fingerprint.
            external_ip: Configure GCP external IP.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            route: Configure GCP route.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            gcp_project_list: Configure GCP project list.
                Default format: [{'id': 1}]
                Supported formats:
                  - Single string: "value" → [{'id': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'id': 'val1'}, ...]
                  - List of dicts: [{'id': 1}] (recommended)
            forwarding_rule: Configure GCP forwarding rule.
                Default format: [{'rule-name': 'value', 'target': 'value'}]
                Required format: List of dicts with keys: rule-name, target
                  (String format not allowed due to multiple required fields)
            service_account: GCP service account email.
            private_key: Private key of GCP service account.
            secret_token: Secret token of Kubernetes service account.
            domain: Domain name.
            group_name: Full path group name of computers.
            server_cert: Trust servers that contain this certificate only.
            server_ca_cert: Trust only those servers whose certificate is directly/indirectly signed by this certificate.
            api_key: IBM cloud API key or service ID API key.
            ibm_region: IBM cloud region name.
            par_id: Public address range ID.
            update_interval: Dynamic object update interval (30 - 3600 sec, default = 60, 0 = disabled).
            vdom: Virtual domain name.
            error_mode: Override client-level error_mode. "raise" raises exceptions, "return" returns error dict, "print" prints errors.
            error_format: Override client-level error_format. "detailed" provides full context, "simple" is concise, "code_only" returns just status code.

        Returns:
            FortiObject instance. Use .dict, .json, or .raw to access as dictionary.

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.system_sdn_connector.put(
            ...     name=1,
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "name": 1,
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.system_sdn_connector.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Apply normalization for table fields (supports flexible input formats)
        if server_list is not None:
            server_list = normalize_table_field(
                server_list,
                mkey="ip",
                required_fields=['ip'],
                field_name="server_list",
                example="[{'ip': '192.168.1.10'}]",
            )
        if external_account_list is not None:
            external_account_list = normalize_table_field(
                external_account_list,
                mkey="role-arn",
                required_fields=['role-arn', 'region-list'],
                field_name="external_account_list",
                example="[{'role-arn': 'value', 'region-list': 'value'}]",
            )
        if nic is not None:
            nic = normalize_table_field(
                nic,
                mkey="name",
                required_fields=['name'],
                field_name="nic",
                example="[{'name': 'value'}]",
            )
        if route_table is not None:
            route_table = normalize_table_field(
                route_table,
                mkey="name",
                required_fields=['name'],
                field_name="route_table",
                example="[{'name': 'value'}]",
            )
        if compartment_list is not None:
            compartment_list = normalize_table_field(
                compartment_list,
                mkey="compartment-id",
                required_fields=['compartment-id'],
                field_name="compartment_list",
                example="[{'compartment-id': 'value'}]",
            )
        if oci_region_list is not None:
            oci_region_list = normalize_table_field(
                oci_region_list,
                mkey="region",
                required_fields=['region'],
                field_name="oci_region_list",
                example="[{'region': 'value'}]",
            )
        if external_ip is not None:
            external_ip = normalize_table_field(
                external_ip,
                mkey="name",
                required_fields=['name'],
                field_name="external_ip",
                example="[{'name': 'value'}]",
            )
        if route is not None:
            route = normalize_table_field(
                route,
                mkey="name",
                required_fields=['name'],
                field_name="route",
                example="[{'name': 'value'}]",
            )
        if gcp_project_list is not None:
            gcp_project_list = normalize_table_field(
                gcp_project_list,
                mkey="id",
                required_fields=['id'],
                field_name="gcp_project_list",
                example="[{'id': 1}]",
            )
        if forwarding_rule is not None:
            forwarding_rule = normalize_table_field(
                forwarding_rule,
                mkey="rule-name",
                required_fields=['rule-name', 'target'],
                field_name="forwarding_rule",
                example="[{'rule-name': 'value', 'target': 'value'}]",
            )
        
        # Build payload using helper function with auto-normalization
        # This automatically converts strings/lists to [{'name': '...'}] format for list fields
        # To disable auto-normalization, use build_cmdb_payload directly
        payload_data = build_api_payload(
            name=name,
            status=status,
            type=type,
            proxy=proxy,
            use_metadata_iam=use_metadata_iam,
            microsoft_365=microsoft_365,
            ha_status=ha_status,
            verify_certificate=verify_certificate,
            server=server,
            server_list=server_list,
            server_port=server_port,
            message_server_port=message_server_port,
            username=username,
            password=password,
            vcenter_server=vcenter_server,
            vcenter_username=vcenter_username,
            vcenter_password=vcenter_password,
            access_key=access_key,
            secret_key=secret_key,
            region=region,
            vpc_id=vpc_id,
            alt_resource_ip=alt_resource_ip,
            external_account_list=external_account_list,
            tenant_id=tenant_id,
            client_id=client_id,
            client_secret=client_secret,
            subscription_id=subscription_id,
            resource_group=resource_group,
            login_endpoint=login_endpoint,
            resource_url=resource_url,
            azure_region=azure_region,
            nic=nic,
            route_table=route_table,
            user_id=user_id,
            compartment_list=compartment_list,
            oci_region_list=oci_region_list,
            oci_region_type=oci_region_type,
            oci_cert=oci_cert,
            oci_fingerprint=oci_fingerprint,
            external_ip=external_ip,
            route=route,
            gcp_project_list=gcp_project_list,
            forwarding_rule=forwarding_rule,
            service_account=service_account,
            private_key=private_key,
            secret_token=secret_token,
            domain=domain,
            group_name=group_name,
            server_cert=server_cert,
            server_ca_cert=server_ca_cert,
            api_key=api_key,
            ibm_region=ibm_region,
            par_id=par_id,
            update_interval=update_interval,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.sdn_connector import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/system/sdn_connector",
            )
        
        name_value = payload_data.get("name")
        if not name_value:
            raise ValueError("name is required for PUT")
        endpoint = "/system/sdn-connector/" + str(name_value)

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
        status: Literal["disable", "enable"] | None = None,
        type: Literal["aci", "alicloud", "aws", "azure", "gcp", "nsx", "nuage", "oci", "openstack", "kubernetes", "vmware", "sepm", "aci-direct", "ibm", "nutanix", "sap"] | None = None,
        proxy: str | None = None,
        use_metadata_iam: Literal["disable", "enable"] | None = None,
        microsoft_365: Literal["disable", "enable"] | None = None,
        ha_status: Literal["disable", "enable"] | None = None,
        verify_certificate: Literal["disable", "enable"] | None = None,
        server: str | None = None,
        server_list: str | list[str] | list[dict[str, Any]] | None = None,
        server_port: int | None = None,
        message_server_port: int | None = None,
        username: str | None = None,
        password: Any | None = None,
        vcenter_server: str | None = None,
        vcenter_username: str | None = None,
        vcenter_password: Any | None = None,
        access_key: str | None = None,
        secret_key: Any | None = None,
        region: str | None = None,
        vpc_id: str | None = None,
        alt_resource_ip: Literal["disable", "enable"] | None = None,
        external_account_list: str | list[str] | list[dict[str, Any]] | None = None,
        tenant_id: str | None = None,
        client_id: str | None = None,
        client_secret: Any | None = None,
        subscription_id: str | None = None,
        resource_group: str | None = None,
        login_endpoint: str | None = None,
        resource_url: str | None = None,
        azure_region: Literal["global", "china", "germany", "usgov", "local"] | None = None,
        nic: str | list[str] | list[dict[str, Any]] | None = None,
        route_table: str | list[str] | list[dict[str, Any]] | None = None,
        user_id: str | None = None,
        compartment_list: str | list[str] | list[dict[str, Any]] | None = None,
        oci_region_list: str | list[str] | list[dict[str, Any]] | None = None,
        oci_region_type: Literal["commercial", "government"] | None = None,
        oci_cert: str | None = None,
        oci_fingerprint: str | None = None,
        external_ip: str | list[str] | list[dict[str, Any]] | None = None,
        route: str | list[str] | list[dict[str, Any]] | None = None,
        gcp_project_list: str | list[str] | list[dict[str, Any]] | None = None,
        forwarding_rule: str | list[str] | list[dict[str, Any]] | None = None,
        service_account: str | None = None,
        private_key: str | None = None,
        secret_token: str | None = None,
        domain: str | None = None,
        group_name: str | None = None,
        server_cert: str | None = None,
        server_ca_cert: str | None = None,
        api_key: Any | None = None,
        ibm_region: Literal["dallas", "washington-dc", "london", "frankfurt", "sydney", "tokyo", "osaka", "toronto", "sao-paulo", "madrid"] | None = None,
        par_id: str | None = None,
        update_interval: int | None = None,
        q_action: Literal["clone"] | None = None,
        q_nkey: str | None = None,
        q_scope: str | None = None,
        vdom: str | bool | None = None,
        error_mode: Literal["raise", "return", "print"] | None = None,
        error_format: Literal["detailed", "simple", "code_only"] | None = None,
    ):  # type: ignore[no-untyped-def]
        """
        Create new system/sdn_connector object.

        Configure connection to SDN Connector.

        Args:
            payload_dict: Complete object data as dict. Alternative to individual parameters.
            name: SDN connector name.
            status: Enable/disable connection to the remote SDN connector.
            type: Type of SDN connector.
            proxy: SDN proxy.
            use_metadata_iam: Enable/disable use of IAM role from metadata to call API.
            microsoft_365: Enable to use as Microsoft 365 connector.
            ha_status: Enable/disable use for FortiGate HA service.
            verify_certificate: Enable/disable server certificate verification.
            vdom: Virtual domain name of the remote SDN connector.
            server: Server address of the remote SDN connector.
            server_list: Server address list of the remote SDN connector.
                Default format: [{'ip': '192.168.1.10'}]
                Supported formats:
                  - Single string: "value" → [{'ip': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'ip': 'val1'}, ...]
                  - List of dicts: [{'ip': '192.168.1.10'}] (recommended)
            server_port: Port number of the remote SDN connector.
            message_server_port: HTTP port number of the SAP message server.
            username: Username of the remote SDN connector as login credentials.
            password: Password of the remote SDN connector as login credentials.
            vcenter_server: vCenter server address for NSX quarantine.
            vcenter_username: vCenter server username for NSX quarantine.
            vcenter_password: vCenter server password for NSX quarantine.
            access_key: AWS / ACS access key ID.
            secret_key: AWS / ACS secret access key.
            region: AWS / ACS region name.
            vpc_id: AWS VPC ID.
            alt_resource_ip: Enable/disable AWS alternative resource IP.
            external_account_list: Configure AWS external account list.
                Default format: [{'role-arn': 'value', 'region-list': 'value'}]
                Required format: List of dicts with keys: role-arn, region-list
                  (String format not allowed due to multiple required fields)
            tenant_id: Tenant ID (directory ID).
            client_id: Azure client ID (application ID).
            client_secret: Azure client secret (application key).
            subscription_id: Azure subscription ID.
            resource_group: Azure resource group.
            login_endpoint: Azure Stack login endpoint.
            resource_url: Azure Stack resource URL.
            azure_region: Azure server region.
            nic: Configure Azure network interface.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            route_table: Configure Azure route table.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            user_id: User ID.
            compartment_list: Configure OCI compartment list.
                Default format: [{'compartment-id': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'compartment-id': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'compartment-id': 'val1'}, ...]
                  - List of dicts: [{'compartment-id': 'value'}] (recommended)
            oci_region_list: Configure OCI region list.
                Default format: [{'region': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'region': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'region': 'val1'}, ...]
                  - List of dicts: [{'region': 'value'}] (recommended)
            oci_region_type: OCI region type.
            oci_cert: OCI certificate.
            oci_fingerprint: OCI pubkey fingerprint.
            external_ip: Configure GCP external IP.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            route: Configure GCP route.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            gcp_project_list: Configure GCP project list.
                Default format: [{'id': 1}]
                Supported formats:
                  - Single string: "value" → [{'id': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'id': 'val1'}, ...]
                  - List of dicts: [{'id': 1}] (recommended)
            forwarding_rule: Configure GCP forwarding rule.
                Default format: [{'rule-name': 'value', 'target': 'value'}]
                Required format: List of dicts with keys: rule-name, target
                  (String format not allowed due to multiple required fields)
            service_account: GCP service account email.
            private_key: Private key of GCP service account.
            secret_token: Secret token of Kubernetes service account.
            domain: Domain name.
            group_name: Full path group name of computers.
            server_cert: Trust servers that contain this certificate only.
            server_ca_cert: Trust only those servers whose certificate is directly/indirectly signed by this certificate.
            api_key: IBM cloud API key or service ID API key.
            ibm_region: IBM cloud region name.
            par_id: Public address range ID.
            update_interval: Dynamic object update interval (30 - 3600 sec, default = 60, 0 = disabled).
            vdom: Virtual domain name. Use True for global, string for specific VDOM.
            error_mode: Override client-level error_mode. "raise" raises exceptions, "return" returns error dict, "print" prints errors.
            error_format: Override client-level error_format. "detailed" provides full context, "simple" is concise, "code_only" returns just status code.

        Returns:
            FortiObject instance with created object. Use .dict, .json, or .raw to access as dictionary.

        Examples:
            >>> # Create using individual parameters
            >>> result = fgt.api.cmdb.system_sdn_connector.post(
            ...     name="example",
            ...     # ... other required fields
            ... )
            >>> print(f"Created name: {result['results']}")
            
            >>> # Create using payload dict
            >>> payload = SdnConnector.defaults()  # Start with defaults
            >>> payload['name'] = 'my-object'
            >>> result = fgt.api.cmdb.system_sdn_connector.post(payload_dict=payload)

        Note:
            Required fields: {{ ", ".join(SdnConnector.required_fields()) }}
            
            Use SdnConnector.help('field_name') to get field details.

        See Also:
            - get(): Retrieve objects
            - put(): Update existing object
            - set(): Intelligent create or update
        """
        # Apply normalization for table fields (supports flexible input formats)
        if server_list is not None:
            server_list = normalize_table_field(
                server_list,
                mkey="ip",
                required_fields=['ip'],
                field_name="server_list",
                example="[{'ip': '192.168.1.10'}]",
            )
        if external_account_list is not None:
            external_account_list = normalize_table_field(
                external_account_list,
                mkey="role-arn",
                required_fields=['role-arn', 'region-list'],
                field_name="external_account_list",
                example="[{'role-arn': 'value', 'region-list': 'value'}]",
            )
        if nic is not None:
            nic = normalize_table_field(
                nic,
                mkey="name",
                required_fields=['name'],
                field_name="nic",
                example="[{'name': 'value'}]",
            )
        if route_table is not None:
            route_table = normalize_table_field(
                route_table,
                mkey="name",
                required_fields=['name'],
                field_name="route_table",
                example="[{'name': 'value'}]",
            )
        if compartment_list is not None:
            compartment_list = normalize_table_field(
                compartment_list,
                mkey="compartment-id",
                required_fields=['compartment-id'],
                field_name="compartment_list",
                example="[{'compartment-id': 'value'}]",
            )
        if oci_region_list is not None:
            oci_region_list = normalize_table_field(
                oci_region_list,
                mkey="region",
                required_fields=['region'],
                field_name="oci_region_list",
                example="[{'region': 'value'}]",
            )
        if external_ip is not None:
            external_ip = normalize_table_field(
                external_ip,
                mkey="name",
                required_fields=['name'],
                field_name="external_ip",
                example="[{'name': 'value'}]",
            )
        if route is not None:
            route = normalize_table_field(
                route,
                mkey="name",
                required_fields=['name'],
                field_name="route",
                example="[{'name': 'value'}]",
            )
        if gcp_project_list is not None:
            gcp_project_list = normalize_table_field(
                gcp_project_list,
                mkey="id",
                required_fields=['id'],
                field_name="gcp_project_list",
                example="[{'id': 1}]",
            )
        if forwarding_rule is not None:
            forwarding_rule = normalize_table_field(
                forwarding_rule,
                mkey="rule-name",
                required_fields=['rule-name', 'target'],
                field_name="forwarding_rule",
                example="[{'rule-name': 'value', 'target': 'value'}]",
            )
        
        # Build payload using helper function with auto-normalization
        # This automatically converts strings/lists to [{'name': '...'}] format for list fields
        # To disable auto-normalization, use build_cmdb_payload directly
        payload_data = build_api_payload(
            name=name,
            status=status,
            type=type,
            proxy=proxy,
            use_metadata_iam=use_metadata_iam,
            microsoft_365=microsoft_365,
            ha_status=ha_status,
            verify_certificate=verify_certificate,
            server=server,
            server_list=server_list,
            server_port=server_port,
            message_server_port=message_server_port,
            username=username,
            password=password,
            vcenter_server=vcenter_server,
            vcenter_username=vcenter_username,
            vcenter_password=vcenter_password,
            access_key=access_key,
            secret_key=secret_key,
            region=region,
            vpc_id=vpc_id,
            alt_resource_ip=alt_resource_ip,
            external_account_list=external_account_list,
            tenant_id=tenant_id,
            client_id=client_id,
            client_secret=client_secret,
            subscription_id=subscription_id,
            resource_group=resource_group,
            login_endpoint=login_endpoint,
            resource_url=resource_url,
            azure_region=azure_region,
            nic=nic,
            route_table=route_table,
            user_id=user_id,
            compartment_list=compartment_list,
            oci_region_list=oci_region_list,
            oci_region_type=oci_region_type,
            oci_cert=oci_cert,
            oci_fingerprint=oci_fingerprint,
            external_ip=external_ip,
            route=route,
            gcp_project_list=gcp_project_list,
            forwarding_rule=forwarding_rule,
            service_account=service_account,
            private_key=private_key,
            secret_token=secret_token,
            domain=domain,
            group_name=group_name,
            server_cert=server_cert,
            server_ca_cert=server_ca_cert,
            api_key=api_key,
            ibm_region=ibm_region,
            par_id=par_id,
            update_interval=update_interval,
            data=payload_dict,
        )

        # Check for deprecated fields and warn users
        from ._helpers.sdn_connector import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/system/sdn_connector",
            )

        endpoint = "/system/sdn-connector"
        
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
        Delete system/sdn_connector object.

        Configure connection to SDN Connector.

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
            >>> result = fgt.api.cmdb.system_sdn_connector.delete(name=1)
            
            >>> # Check for errors
            >>> if result.get('status') != 'success':
            ...     print(f"Delete failed: {result.get('error')}")

        See Also:
            - exists(): Check if object exists before deleting
            - get(): Retrieve object to verify it exists
        """
        if not name:
            raise ValueError("name is required for DELETE")
        endpoint = "/system/sdn-connector/" + str(name)

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
        Check if system/sdn_connector object exists.

        Verifies whether an object exists by attempting to retrieve it and checking the response status.

        Args:
            name: Primary key identifier
            vdom: Virtual domain name

        Returns:
            True if object exists, False otherwise

        Examples:
            >>> # Check if object exists before operations
            >>> if fgt.api.cmdb.system_sdn_connector.exists(name=1):
            ...     print("Object exists")
            ... else:
            ...     print("Object not found")
            
            >>> # Conditional delete
            >>> if fgt.api.cmdb.system_sdn_connector.exists(name=1):
            ...     fgt.api.cmdb.system_sdn_connector.delete(name=1)

        See Also:
            - get(): Retrieve full object data
            - set(): Create or update automatically based on existence
        """
        # Try to fetch the object - 404 means it doesn't exist
        try:
            result = self.get(
                name=name,
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
        name: str | None = None,
        status: Literal["disable", "enable"] | None = None,
        type: Literal["aci", "alicloud", "aws", "azure", "gcp", "nsx", "nuage", "oci", "openstack", "kubernetes", "vmware", "sepm", "aci-direct", "ibm", "nutanix", "sap"] | None = None,
        proxy: str | None = None,
        use_metadata_iam: Literal["disable", "enable"] | None = None,
        microsoft_365: Literal["disable", "enable"] | None = None,
        ha_status: Literal["disable", "enable"] | None = None,
        verify_certificate: Literal["disable", "enable"] | None = None,
        server: str | None = None,
        server_list: str | list[str] | list[dict[str, Any]] | None = None,
        server_port: int | None = None,
        message_server_port: int | None = None,
        username: str | None = None,
        password: Any | None = None,
        vcenter_server: str | None = None,
        vcenter_username: str | None = None,
        vcenter_password: Any | None = None,
        access_key: str | None = None,
        secret_key: Any | None = None,
        region: str | None = None,
        vpc_id: str | None = None,
        alt_resource_ip: Literal["disable", "enable"] | None = None,
        external_account_list: str | list[str] | list[dict[str, Any]] | None = None,
        tenant_id: str | None = None,
        client_id: str | None = None,
        client_secret: Any | None = None,
        subscription_id: str | None = None,
        resource_group: str | None = None,
        login_endpoint: str | None = None,
        resource_url: str | None = None,
        azure_region: Literal["global", "china", "germany", "usgov", "local"] | None = None,
        nic: str | list[str] | list[dict[str, Any]] | None = None,
        route_table: str | list[str] | list[dict[str, Any]] | None = None,
        user_id: str | None = None,
        compartment_list: str | list[str] | list[dict[str, Any]] | None = None,
        oci_region_list: str | list[str] | list[dict[str, Any]] | None = None,
        oci_region_type: Literal["commercial", "government"] | None = None,
        oci_cert: str | None = None,
        oci_fingerprint: str | None = None,
        external_ip: str | list[str] | list[dict[str, Any]] | None = None,
        route: str | list[str] | list[dict[str, Any]] | None = None,
        gcp_project_list: str | list[str] | list[dict[str, Any]] | None = None,
        forwarding_rule: str | list[str] | list[dict[str, Any]] | None = None,
        service_account: str | None = None,
        private_key: str | None = None,
        secret_token: str | None = None,
        domain: str | None = None,
        group_name: str | None = None,
        server_cert: str | None = None,
        server_ca_cert: str | None = None,
        api_key: Any | None = None,
        ibm_region: Literal["dallas", "washington-dc", "london", "frankfurt", "sydney", "tokyo", "osaka", "toronto", "sao-paulo", "madrid"] | None = None,
        par_id: str | None = None,
        update_interval: int | None = None,
        vdom: str | bool | None = None,
        error_mode: Literal["raise", "return", "print"] | None = None,
        error_format: Literal["detailed", "simple", "code_only"] | None = None,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Create or update system/sdn_connector object (intelligent operation).

        Automatically determines whether to create (POST) or update (PUT) based on
        whether the resource exists. Requires the primary key (name) in the payload.

        Args:
            payload_dict: Resource data including name (primary key)
            name: Field name
            status: Field status
            type: Field type
            proxy: Field proxy
            use_metadata_iam: Field use-metadata-iam
            microsoft_365: Field microsoft-365
            ha_status: Field ha-status
            verify_certificate: Field verify-certificate
            server: Field server
            server_list: Field server-list
            server_port: Field server-port
            message_server_port: Field message-server-port
            username: Field username
            password: Field password
            vcenter_server: Field vcenter-server
            vcenter_username: Field vcenter-username
            vcenter_password: Field vcenter-password
            access_key: Field access-key
            secret_key: Field secret-key
            region: Field region
            vpc_id: Field vpc-id
            alt_resource_ip: Field alt-resource-ip
            external_account_list: Field external-account-list
            tenant_id: Field tenant-id
            client_id: Field client-id
            client_secret: Field client-secret
            subscription_id: Field subscription-id
            resource_group: Field resource-group
            login_endpoint: Field login-endpoint
            resource_url: Field resource-url
            azure_region: Field azure-region
            nic: Field nic
            route_table: Field route-table
            user_id: Field user-id
            compartment_list: Field compartment-list
            oci_region_list: Field oci-region-list
            oci_region_type: Field oci-region-type
            oci_cert: Field oci-cert
            oci_fingerprint: Field oci-fingerprint
            external_ip: Field external-ip
            route: Field route
            gcp_project_list: Field gcp-project-list
            forwarding_rule: Field forwarding-rule
            service_account: Field service-account
            private_key: Field private-key
            secret_token: Field secret-token
            domain: Field domain
            group_name: Field group-name
            server_cert: Field server-cert
            server_ca_cert: Field server-ca-cert
            api_key: Field api-key
            ibm_region: Field ibm-region
            par_id: Field par-id
            update_interval: Field update-interval
            vdom: Virtual domain name
            **kwargs: Additional parameters passed to PUT or POST

        Returns:
            FortiObject instance. Use .dict, .json, or .raw to access as dictionary

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Intelligent create or update using field parameters
            >>> result = fgt.api.cmdb.system_sdn_connector.set(
            ...     name=1,
            ...     # ... other fields
            ... )
            
            >>> # Or using payload dict
            >>> payload = {
            ...     "name": 1,
            ...     "field1": "value1",
            ...     "field2": "value2",
            ... }
            >>> result = fgt.api.cmdb.system_sdn_connector.set(payload_dict=payload)
            >>> # Will POST if object doesn't exist, PUT if it does
            
            >>> # Idempotent configuration
            >>> for obj_data in configuration_list:
            ...     fgt.api.cmdb.system_sdn_connector.set(payload_dict=obj_data)
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
            status=status,
            type=type,
            proxy=proxy,
            use_metadata_iam=use_metadata_iam,
            microsoft_365=microsoft_365,
            ha_status=ha_status,
            verify_certificate=verify_certificate,
            server=server,
            server_list=server_list,
            server_port=server_port,
            message_server_port=message_server_port,
            username=username,
            password=password,
            vcenter_server=vcenter_server,
            vcenter_username=vcenter_username,
            vcenter_password=vcenter_password,
            access_key=access_key,
            secret_key=secret_key,
            region=region,
            vpc_id=vpc_id,
            alt_resource_ip=alt_resource_ip,
            external_account_list=external_account_list,
            tenant_id=tenant_id,
            client_id=client_id,
            client_secret=client_secret,
            subscription_id=subscription_id,
            resource_group=resource_group,
            login_endpoint=login_endpoint,
            resource_url=resource_url,
            azure_region=azure_region,
            nic=nic,
            route_table=route_table,
            user_id=user_id,
            compartment_list=compartment_list,
            oci_region_list=oci_region_list,
            oci_region_type=oci_region_type,
            oci_cert=oci_cert,
            oci_fingerprint=oci_fingerprint,
            external_ip=external_ip,
            route=route,
            gcp_project_list=gcp_project_list,
            forwarding_rule=forwarding_rule,
            service_account=service_account,
            private_key=private_key,
            secret_token=secret_token,
            domain=domain,
            group_name=group_name,
            server_cert=server_cert,
            server_ca_cert=server_ca_cert,
            api_key=api_key,
            ibm_region=ibm_region,
            par_id=par_id,
            update_interval=update_interval,
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
        Move system/sdn_connector object to a new position.
        
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
            >>> fgt.api.cmdb.system_sdn_connector.move(
            ...     name=100,
            ...     action="before",
            ...     reference_name=50
            ... )
        """
        return self._client.request(
            method="PUT",
            path=f"/api/v2/cmdb/system/sdn-connector",
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
        Clone system/sdn_connector object.
        
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
            >>> fgt.api.cmdb.system_sdn_connector.clone(
            ...     name=1,
            ...     new_name=100
            ... )
        """
        return self._client.request(
            method="POST",
            path=f"/api/v2/cmdb/system/sdn-connector",
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
        Check if system/sdn_connector object exists.
        
        Args:
            name: Identifier to check
            vdom: Virtual domain name
            
        Returns:
            True if object exists, False otherwise
            
        Example:
            >>> # Check before creating
            >>> if not fgt.api.cmdb.system_sdn_connector.exists(name=1):
            ...     fgt.api.cmdb.system_sdn_connector.post(payload_dict=data)
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

