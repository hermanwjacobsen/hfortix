"""
FortiOS CMDB - User ldap

Configuration endpoint for managing cmdb user/ldap objects.

API Endpoints:
    GET    /cmdb/user/ldap
    POST   /cmdb/user/ldap
    PUT    /cmdb/user/ldap/{identifier}
    DELETE /cmdb/user/ldap/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.user_ldap.get()
    >>>
    >>> # Create with auto-normalization (strings/lists converted automatically)
    >>> result = fgt.api.cmdb.user_ldap.post(
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

class Ldap(CRUDEndpoint, MetadataMixin):
    """Ldap Operations."""
    
    # Configure metadata mixin to use this endpoint's helper module
    _helper_module_name = "ldap"
    
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
        """Initialize Ldap endpoint."""
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
        Retrieve user/ldap configuration.

        Configure LDAP server entries.

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
            >>> # Get all user/ldap objects
            >>> result = fgt.api.cmdb.user_ldap.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get specific user/ldap by name
            >>> result = fgt.api.cmdb.user_ldap.get(name=1)
            >>> print(result['results'])
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.user_ldap.get(
            ...     filter=["name==test", "status==enable"]
            ... )
            
            >>> # Get with pagination
            >>> result = fgt.api.cmdb.user_ldap.get(
            ...     start=0, count=100
            ... )
            
            >>> # Get schema information  
            >>> schema = fgt.api.cmdb.user_ldap.get_schema()

        See Also:
            - post(): Create new user/ldap object
            - put(): Update existing user/ldap object
            - delete(): Remove user/ldap object
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
            endpoint = "/user/ldap/" + str(name)
            unwrap_single = True
        else:
            endpoint = "/user/ldap"
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
            >>> schema = fgt.api.cmdb.user_ldap.get_schema()
            >>> print(schema['results'])
            
            >>> # Get JSON Schema format (if supported)
            >>> json_schema = fgt.api.cmdb.user_ldap.get_schema(format="json-schema")
        
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
        server: str | None = None,
        secondary_server: str | None = None,
        tertiary_server: str | None = None,
        status_ttl: int | None = None,
        server_identity_check: Literal["enable", "disable"] | None = None,
        source_ip: str | None = None,
        source_ip_interface: str | None = None,
        source_port: int | None = None,
        cnid: str | None = None,
        dn: str | None = None,
        type: Literal["simple", "anonymous", "regular"] | None = None,
        two_factor: Literal["disable", "fortitoken-cloud"] | None = None,
        two_factor_authentication: Literal["fortitoken", "email", "sms"] | None = None,
        two_factor_notification: Literal["email", "sms"] | None = None,
        two_factor_filter: str | None = None,
        username: str | None = None,
        password: Any | None = None,
        group_member_check: Literal["user-attr", "group-object", "posix-group-object"] | None = None,
        group_search_base: str | None = None,
        group_object_filter: str | None = None,
        group_filter: str | None = None,
        secure: Literal["disable", "starttls", "ldaps"] | None = None,
        ssl_min_proto_version: Literal["default", "SSLv3", "TLSv1", "TLSv1-1", "TLSv1-2", "TLSv1-3"] | None = None,
        ca_cert: str | None = None,
        port: int | None = None,
        password_expiry_warning: Literal["enable", "disable"] | None = None,
        password_renewal: Literal["enable", "disable"] | None = None,
        member_attr: str | None = None,
        account_key_processing: Literal["same", "strip"] | None = None,
        account_key_cert_field: Literal["othername", "rfc822name", "dnsname", "cn"] | None = None,
        account_key_filter: str | None = None,
        search_type: Literal["recursive"] | list[str] | None = None,
        client_cert_auth: Literal["enable", "disable"] | None = None,
        client_cert: str | None = None,
        obtain_user_info: Literal["enable", "disable"] | None = None,
        user_info_exchange_server: str | None = None,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = None,
        interface: str | None = None,
        vrf_select: int | None = None,
        antiphish: Literal["enable", "disable"] | None = None,
        password_attr: str | None = None,
        q_action: Literal["move"] | None = None,
        q_before: str | None = None,
        q_after: str | None = None,
        q_scope: str | None = None,
        vdom: str | bool | None = None,
        error_mode: Literal["raise", "return", "print"] | None = None,
        error_format: Literal["detailed", "simple", "code_only"] | None = None,
    ):  # type: ignore[no-untyped-def]
        """
        Update existing user/ldap object.

        Configure LDAP server entries.

        Args:
            payload_dict: Object data as dict. Must include name (primary key).
            name: LDAP server entry name.
            server: LDAP server CN domain name or IP.
            secondary_server: Secondary LDAP server CN domain name or IP.
            tertiary_server: Tertiary LDAP server CN domain name or IP.
            status_ttl: Time for which server reachability is cached so that when a server is unreachable, it will not be retried for at least this period of time (0 = cache disabled, default = 300).
            server_identity_check: Enable/disable LDAP server identity check (verify server domain name/IP address against the server certificate).
            source_ip: FortiGate IP address to be used for communication with the LDAP server.
            source_ip_interface: Source interface for communication with the LDAP server.
            source_port: Source port to be used for communication with the LDAP server.
            cnid: Common name identifier for the LDAP server. The common name identifier for most LDAP servers is "cn".
            dn: Distinguished name used to look up entries on the LDAP server.
            type: Authentication type for LDAP searches.
            two_factor: Enable/disable two-factor authentication.
            two_factor_authentication: Authentication method by FortiToken Cloud.
            two_factor_notification: Notification method for user activation by FortiToken Cloud.
            two_factor_filter: Filter used to synchronize users to FortiToken Cloud.
            username: Username (full DN) for initial binding.
            password: Password for initial binding.
            group_member_check: Group member checking methods.
            group_search_base: Search base used for group searching.
            group_object_filter: Filter used for group searching.
            group_filter: Filter used for group matching.
            secure: Port to be used for authentication.
            ssl_min_proto_version: Minimum supported protocol version for SSL/TLS connections (default is to follow system global setting).
            ca_cert: CA certificate name.
            port: Port to be used for communication with the LDAP server (default = 389).
            password_expiry_warning: Enable/disable password expiry warnings.
            password_renewal: Enable/disable online password renewal.
            member_attr: Name of attribute from which to get group membership.
            account_key_processing: Account key processing operation. The FortiGate will keep either the whole domain or strip the domain from the subject identity.
            account_key_cert_field: Define subject identity field in certificate for user access right checking.
            account_key_filter: Account key filter, using the UPN as the search filter.
            search_type: Search type.
            client_cert_auth: Enable/disable using client certificate for TLS authentication.
            client_cert: Client certificate name.
            obtain_user_info: Enable/disable obtaining of user information.
            user_info_exchange_server: MS Exchange server from which to fetch user information.
            interface_select_method: Specify how to select outgoing interface to reach server.
            interface: Specify outgoing interface to reach server.
            vrf_select: VRF ID used for connection to server.
            antiphish: Enable/disable AntiPhishing credential backend.
            password_attr: Name of attribute to get password hash.
            vdom: Virtual domain name.
            error_mode: Override client-level error_mode. "raise" raises exceptions, "return" returns error dict, "print" prints errors.
            error_format: Override client-level error_format. "detailed" provides full context, "simple" is concise, "code_only" returns just status code.

        Returns:
            FortiObject instance. Use .dict, .json, or .raw to access as dictionary.

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.user_ldap.put(
            ...     name=1,
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "name": 1,
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.user_ldap.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Build payload using helper function with auto-normalization
        # This automatically converts strings/lists to [{'name': '...'}] format for list fields
        # To disable auto-normalization, use build_cmdb_payload directly
        payload_data = build_api_payload(
            name=name,
            server=server,
            secondary_server=secondary_server,
            tertiary_server=tertiary_server,
            status_ttl=status_ttl,
            server_identity_check=server_identity_check,
            source_ip=source_ip,
            source_ip_interface=source_ip_interface,
            source_port=source_port,
            cnid=cnid,
            dn=dn,
            type=type,
            two_factor=two_factor,
            two_factor_authentication=two_factor_authentication,
            two_factor_notification=two_factor_notification,
            two_factor_filter=two_factor_filter,
            username=username,
            password=password,
            group_member_check=group_member_check,
            group_search_base=group_search_base,
            group_object_filter=group_object_filter,
            group_filter=group_filter,
            secure=secure,
            ssl_min_proto_version=ssl_min_proto_version,
            ca_cert=ca_cert,
            port=port,
            password_expiry_warning=password_expiry_warning,
            password_renewal=password_renewal,
            member_attr=member_attr,
            account_key_processing=account_key_processing,
            account_key_cert_field=account_key_cert_field,
            account_key_filter=account_key_filter,
            search_type=search_type,
            client_cert_auth=client_cert_auth,
            client_cert=client_cert,
            obtain_user_info=obtain_user_info,
            user_info_exchange_server=user_info_exchange_server,
            interface_select_method=interface_select_method,
            interface=interface,
            vrf_select=vrf_select,
            antiphish=antiphish,
            password_attr=password_attr,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.ldap import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/user/ldap",
            )
        
        name_value = payload_data.get("name")
        if not name_value:
            raise ValueError("name is required for PUT")
        endpoint = "/user/ldap/" + str(name_value)

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
        server: str | None = None,
        secondary_server: str | None = None,
        tertiary_server: str | None = None,
        status_ttl: int | None = None,
        server_identity_check: Literal["enable", "disable"] | None = None,
        source_ip: str | None = None,
        source_ip_interface: str | None = None,
        source_port: int | None = None,
        cnid: str | None = None,
        dn: str | None = None,
        type: Literal["simple", "anonymous", "regular"] | None = None,
        two_factor: Literal["disable", "fortitoken-cloud"] | None = None,
        two_factor_authentication: Literal["fortitoken", "email", "sms"] | None = None,
        two_factor_notification: Literal["email", "sms"] | None = None,
        two_factor_filter: str | None = None,
        username: str | None = None,
        password: Any | None = None,
        group_member_check: Literal["user-attr", "group-object", "posix-group-object"] | None = None,
        group_search_base: str | None = None,
        group_object_filter: str | None = None,
        group_filter: str | None = None,
        secure: Literal["disable", "starttls", "ldaps"] | None = None,
        ssl_min_proto_version: Literal["default", "SSLv3", "TLSv1", "TLSv1-1", "TLSv1-2", "TLSv1-3"] | None = None,
        ca_cert: str | None = None,
        port: int | None = None,
        password_expiry_warning: Literal["enable", "disable"] | None = None,
        password_renewal: Literal["enable", "disable"] | None = None,
        member_attr: str | None = None,
        account_key_processing: Literal["same", "strip"] | None = None,
        account_key_cert_field: Literal["othername", "rfc822name", "dnsname", "cn"] | None = None,
        account_key_filter: str | None = None,
        search_type: Literal["recursive"] | list[str] | None = None,
        client_cert_auth: Literal["enable", "disable"] | None = None,
        client_cert: str | None = None,
        obtain_user_info: Literal["enable", "disable"] | None = None,
        user_info_exchange_server: str | None = None,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = None,
        interface: str | None = None,
        vrf_select: int | None = None,
        antiphish: Literal["enable", "disable"] | None = None,
        password_attr: str | None = None,
        q_action: Literal["clone"] | None = None,
        q_nkey: str | None = None,
        q_scope: str | None = None,
        vdom: str | bool | None = None,
        error_mode: Literal["raise", "return", "print"] | None = None,
        error_format: Literal["detailed", "simple", "code_only"] | None = None,
    ):  # type: ignore[no-untyped-def]
        """
        Create new user/ldap object.

        Configure LDAP server entries.

        Args:
            payload_dict: Complete object data as dict. Alternative to individual parameters.
            name: LDAP server entry name.
            server: LDAP server CN domain name or IP.
            secondary_server: Secondary LDAP server CN domain name or IP.
            tertiary_server: Tertiary LDAP server CN domain name or IP.
            status_ttl: Time for which server reachability is cached so that when a server is unreachable, it will not be retried for at least this period of time (0 = cache disabled, default = 300).
            server_identity_check: Enable/disable LDAP server identity check (verify server domain name/IP address against the server certificate).
            source_ip: FortiGate IP address to be used for communication with the LDAP server.
            source_ip_interface: Source interface for communication with the LDAP server.
            source_port: Source port to be used for communication with the LDAP server.
            cnid: Common name identifier for the LDAP server. The common name identifier for most LDAP servers is "cn".
            dn: Distinguished name used to look up entries on the LDAP server.
            type: Authentication type for LDAP searches.
            two_factor: Enable/disable two-factor authentication.
            two_factor_authentication: Authentication method by FortiToken Cloud.
            two_factor_notification: Notification method for user activation by FortiToken Cloud.
            two_factor_filter: Filter used to synchronize users to FortiToken Cloud.
            username: Username (full DN) for initial binding.
            password: Password for initial binding.
            group_member_check: Group member checking methods.
            group_search_base: Search base used for group searching.
            group_object_filter: Filter used for group searching.
            group_filter: Filter used for group matching.
            secure: Port to be used for authentication.
            ssl_min_proto_version: Minimum supported protocol version for SSL/TLS connections (default is to follow system global setting).
            ca_cert: CA certificate name.
            port: Port to be used for communication with the LDAP server (default = 389).
            password_expiry_warning: Enable/disable password expiry warnings.
            password_renewal: Enable/disable online password renewal.
            member_attr: Name of attribute from which to get group membership.
            account_key_processing: Account key processing operation. The FortiGate will keep either the whole domain or strip the domain from the subject identity.
            account_key_cert_field: Define subject identity field in certificate for user access right checking.
            account_key_filter: Account key filter, using the UPN as the search filter.
            search_type: Search type.
            client_cert_auth: Enable/disable using client certificate for TLS authentication.
            client_cert: Client certificate name.
            obtain_user_info: Enable/disable obtaining of user information.
            user_info_exchange_server: MS Exchange server from which to fetch user information.
            interface_select_method: Specify how to select outgoing interface to reach server.
            interface: Specify outgoing interface to reach server.
            vrf_select: VRF ID used for connection to server.
            antiphish: Enable/disable AntiPhishing credential backend.
            password_attr: Name of attribute to get password hash.
            vdom: Virtual domain name. Use True for global, string for specific VDOM.
            error_mode: Override client-level error_mode. "raise" raises exceptions, "return" returns error dict, "print" prints errors.
            error_format: Override client-level error_format. "detailed" provides full context, "simple" is concise, "code_only" returns just status code.

        Returns:
            FortiObject instance with created object. Use .dict, .json, or .raw to access as dictionary.

        Examples:
            >>> # Create using individual parameters
            >>> result = fgt.api.cmdb.user_ldap.post(
            ...     name="example",
            ...     # ... other required fields
            ... )
            >>> print(f"Created name: {result['results']}")
            
            >>> # Create using payload dict
            >>> payload = Ldap.defaults()  # Start with defaults
            >>> payload['name'] = 'my-object'
            >>> result = fgt.api.cmdb.user_ldap.post(payload_dict=payload)

        Note:
            Required fields: {{ ", ".join(Ldap.required_fields()) }}
            
            Use Ldap.help('field_name') to get field details.

        See Also:
            - get(): Retrieve objects
            - put(): Update existing object
            - set(): Intelligent create or update
        """
        # Build payload using helper function with auto-normalization
        # This automatically converts strings/lists to [{'name': '...'}] format for list fields
        # To disable auto-normalization, use build_cmdb_payload directly
        payload_data = build_api_payload(
            name=name,
            server=server,
            secondary_server=secondary_server,
            tertiary_server=tertiary_server,
            status_ttl=status_ttl,
            server_identity_check=server_identity_check,
            source_ip=source_ip,
            source_ip_interface=source_ip_interface,
            source_port=source_port,
            cnid=cnid,
            dn=dn,
            type=type,
            two_factor=two_factor,
            two_factor_authentication=two_factor_authentication,
            two_factor_notification=two_factor_notification,
            two_factor_filter=two_factor_filter,
            username=username,
            password=password,
            group_member_check=group_member_check,
            group_search_base=group_search_base,
            group_object_filter=group_object_filter,
            group_filter=group_filter,
            secure=secure,
            ssl_min_proto_version=ssl_min_proto_version,
            ca_cert=ca_cert,
            port=port,
            password_expiry_warning=password_expiry_warning,
            password_renewal=password_renewal,
            member_attr=member_attr,
            account_key_processing=account_key_processing,
            account_key_cert_field=account_key_cert_field,
            account_key_filter=account_key_filter,
            search_type=search_type,
            client_cert_auth=client_cert_auth,
            client_cert=client_cert,
            obtain_user_info=obtain_user_info,
            user_info_exchange_server=user_info_exchange_server,
            interface_select_method=interface_select_method,
            interface=interface,
            vrf_select=vrf_select,
            antiphish=antiphish,
            password_attr=password_attr,
            data=payload_dict,
        )

        # Check for deprecated fields and warn users
        from ._helpers.ldap import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/user/ldap",
            )

        endpoint = "/user/ldap"
        
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
        Delete user/ldap object.

        Configure LDAP server entries.

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
            >>> result = fgt.api.cmdb.user_ldap.delete(name=1)
            
            >>> # Check for errors
            >>> if result.get('status') != 'success':
            ...     print(f"Delete failed: {result.get('error')}")

        See Also:
            - exists(): Check if object exists before deleting
            - get(): Retrieve object to verify it exists
        """
        if not name:
            raise ValueError("name is required for DELETE")
        endpoint = "/user/ldap/" + str(name)

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
        Check if user/ldap object exists.

        Verifies whether an object exists by attempting to retrieve it and checking the response status.

        Args:
            name: Primary key identifier
            vdom: Virtual domain name

        Returns:
            True if object exists, False otherwise

        Examples:
            >>> # Check if object exists before operations
            >>> if fgt.api.cmdb.user_ldap.exists(name=1):
            ...     print("Object exists")
            ... else:
            ...     print("Object not found")
            
            >>> # Conditional delete
            >>> if fgt.api.cmdb.user_ldap.exists(name=1):
            ...     fgt.api.cmdb.user_ldap.delete(name=1)

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
        server: str | None = None,
        secondary_server: str | None = None,
        tertiary_server: str | None = None,
        status_ttl: int | None = None,
        server_identity_check: Literal["enable", "disable"] | None = None,
        source_ip: str | None = None,
        source_ip_interface: str | None = None,
        source_port: int | None = None,
        cnid: str | None = None,
        dn: str | None = None,
        type: Literal["simple", "anonymous", "regular"] | None = None,
        two_factor: Literal["disable", "fortitoken-cloud"] | None = None,
        two_factor_authentication: Literal["fortitoken", "email", "sms"] | None = None,
        two_factor_notification: Literal["email", "sms"] | None = None,
        two_factor_filter: str | None = None,
        username: str | None = None,
        password: Any | None = None,
        group_member_check: Literal["user-attr", "group-object", "posix-group-object"] | None = None,
        group_search_base: str | None = None,
        group_object_filter: str | None = None,
        group_filter: str | None = None,
        secure: Literal["disable", "starttls", "ldaps"] | None = None,
        ssl_min_proto_version: Literal["default", "SSLv3", "TLSv1", "TLSv1-1", "TLSv1-2", "TLSv1-3"] | None = None,
        ca_cert: str | None = None,
        port: int | None = None,
        password_expiry_warning: Literal["enable", "disable"] | None = None,
        password_renewal: Literal["enable", "disable"] | None = None,
        member_attr: str | None = None,
        account_key_processing: Literal["same", "strip"] | None = None,
        account_key_cert_field: Literal["othername", "rfc822name", "dnsname", "cn"] | None = None,
        account_key_filter: str | None = None,
        search_type: Literal["recursive"] | list[str] | list[dict[str, Any]] | None = None,
        client_cert_auth: Literal["enable", "disable"] | None = None,
        client_cert: str | None = None,
        obtain_user_info: Literal["enable", "disable"] | None = None,
        user_info_exchange_server: str | None = None,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = None,
        interface: str | None = None,
        vrf_select: int | None = None,
        antiphish: Literal["enable", "disable"] | None = None,
        password_attr: str | None = None,
        vdom: str | bool | None = None,
        error_mode: Literal["raise", "return", "print"] | None = None,
        error_format: Literal["detailed", "simple", "code_only"] | None = None,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Create or update user/ldap object (intelligent operation).

        Automatically determines whether to create (POST) or update (PUT) based on
        whether the resource exists. Requires the primary key (name) in the payload.

        Args:
            payload_dict: Resource data including name (primary key)
            name: Field name
            server: Field server
            secondary_server: Field secondary-server
            tertiary_server: Field tertiary-server
            status_ttl: Field status-ttl
            server_identity_check: Field server-identity-check
            source_ip: Field source-ip
            source_ip_interface: Field source-ip-interface
            source_port: Field source-port
            cnid: Field cnid
            dn: Field dn
            type: Field type
            two_factor: Field two-factor
            two_factor_authentication: Field two-factor-authentication
            two_factor_notification: Field two-factor-notification
            two_factor_filter: Field two-factor-filter
            username: Field username
            password: Field password
            group_member_check: Field group-member-check
            group_search_base: Field group-search-base
            group_object_filter: Field group-object-filter
            group_filter: Field group-filter
            secure: Field secure
            ssl_min_proto_version: Field ssl-min-proto-version
            ca_cert: Field ca-cert
            port: Field port
            password_expiry_warning: Field password-expiry-warning
            password_renewal: Field password-renewal
            member_attr: Field member-attr
            account_key_processing: Field account-key-processing
            account_key_cert_field: Field account-key-cert-field
            account_key_filter: Field account-key-filter
            search_type: Field search-type
            client_cert_auth: Field client-cert-auth
            client_cert: Field client-cert
            obtain_user_info: Field obtain-user-info
            user_info_exchange_server: Field user-info-exchange-server
            interface_select_method: Field interface-select-method
            interface: Field interface
            vrf_select: Field vrf-select
            antiphish: Field antiphish
            password_attr: Field password-attr
            vdom: Virtual domain name
            **kwargs: Additional parameters passed to PUT or POST

        Returns:
            FortiObject instance. Use .dict, .json, or .raw to access as dictionary

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Intelligent create or update using field parameters
            >>> result = fgt.api.cmdb.user_ldap.set(
            ...     name=1,
            ...     # ... other fields
            ... )
            
            >>> # Or using payload dict
            >>> payload = {
            ...     "name": 1,
            ...     "field1": "value1",
            ...     "field2": "value2",
            ... }
            >>> result = fgt.api.cmdb.user_ldap.set(payload_dict=payload)
            >>> # Will POST if object doesn't exist, PUT if it does
            
            >>> # Idempotent configuration
            >>> for obj_data in configuration_list:
            ...     fgt.api.cmdb.user_ldap.set(payload_dict=obj_data)
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
            server=server,
            secondary_server=secondary_server,
            tertiary_server=tertiary_server,
            status_ttl=status_ttl,
            server_identity_check=server_identity_check,
            source_ip=source_ip,
            source_ip_interface=source_ip_interface,
            source_port=source_port,
            cnid=cnid,
            dn=dn,
            type=type,
            two_factor=two_factor,
            two_factor_authentication=two_factor_authentication,
            two_factor_notification=two_factor_notification,
            two_factor_filter=two_factor_filter,
            username=username,
            password=password,
            group_member_check=group_member_check,
            group_search_base=group_search_base,
            group_object_filter=group_object_filter,
            group_filter=group_filter,
            secure=secure,
            ssl_min_proto_version=ssl_min_proto_version,
            ca_cert=ca_cert,
            port=port,
            password_expiry_warning=password_expiry_warning,
            password_renewal=password_renewal,
            member_attr=member_attr,
            account_key_processing=account_key_processing,
            account_key_cert_field=account_key_cert_field,
            account_key_filter=account_key_filter,
            search_type=search_type,
            client_cert_auth=client_cert_auth,
            client_cert=client_cert,
            obtain_user_info=obtain_user_info,
            user_info_exchange_server=user_info_exchange_server,
            interface_select_method=interface_select_method,
            interface=interface,
            vrf_select=vrf_select,
            antiphish=antiphish,
            password_attr=password_attr,
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
        Move user/ldap object to a new position.
        
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
            >>> fgt.api.cmdb.user_ldap.move(
            ...     name=100,
            ...     action="before",
            ...     reference_name=50
            ... )
        """
        return self._client.request(
            method="PUT",
            path=f"/api/v2/cmdb/user/ldap",
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
        Clone user/ldap object.
        
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
            >>> fgt.api.cmdb.user_ldap.clone(
            ...     name=1,
            ...     new_name=100
            ... )
        """
        return self._client.request(
            method="POST",
            path=f"/api/v2/cmdb/user/ldap",
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
        Check if user/ldap object exists.
        
        Args:
            name: Identifier to check
            vdom: Virtual domain name
            
        Returns:
            True if object exists, False otherwise
            
        Example:
            >>> # Check before creating
            >>> if not fgt.api.cmdb.user_ldap.exists(name=1):
            ...     fgt.api.cmdb.user_ldap.post(payload_dict=data)
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

