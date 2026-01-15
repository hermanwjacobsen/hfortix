"""
FortiOS CMDB - User fsso

Configuration endpoint for managing cmdb user/fsso objects.

API Endpoints:
    GET    /cmdb/user/fsso
    POST   /cmdb/user/fsso
    PUT    /cmdb/user/fsso/{identifier}
    DELETE /cmdb/user/fsso/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.user_fsso.get()
    >>>
    >>> # Create with auto-normalization (strings/lists converted automatically)
    >>> result = fgt.api.cmdb.user_fsso.post(
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

class Fsso(CRUDEndpoint, MetadataMixin):
    """Fsso Operations."""
    
    # Configure metadata mixin to use this endpoint's helper module
    _helper_module_name = "fsso"
    
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
        """Initialize Fsso endpoint."""
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
        Retrieve user/fsso configuration.

        Configure Fortinet Single Sign On (FSSO) agents.

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
            >>> # Get all user/fsso objects
            >>> result = fgt.api.cmdb.user_fsso.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get specific user/fsso by name
            >>> result = fgt.api.cmdb.user_fsso.get(name=1)
            >>> print(result['results'])
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.user_fsso.get(
            ...     filter=["name==test", "status==enable"]
            ... )
            
            >>> # Get with pagination
            >>> result = fgt.api.cmdb.user_fsso.get(
            ...     start=0, count=100
            ... )
            
            >>> # Get schema information  
            >>> schema = fgt.api.cmdb.user_fsso.get_schema()

        See Also:
            - post(): Create new user/fsso object
            - put(): Update existing user/fsso object
            - delete(): Remove user/fsso object
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
            endpoint = "/user/fsso/" + str(name)
            unwrap_single = True
        else:
            endpoint = "/user/fsso"
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
            >>> schema = fgt.api.cmdb.user_fsso.get_schema()
            >>> print(schema['results'])
            
            >>> # Get JSON Schema format (if supported)
            >>> json_schema = fgt.api.cmdb.user_fsso.get_schema(format="json-schema")
        
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
        type: Literal["default", "fortinac"] | None = None,
        server: str | None = None,
        port: int | None = None,
        password: Any | None = None,
        server2: str | None = None,
        port2: int | None = None,
        password2: Any | None = None,
        server3: str | None = None,
        port3: int | None = None,
        password3: Any | None = None,
        server4: str | None = None,
        port4: int | None = None,
        password4: Any | None = None,
        server5: str | None = None,
        port5: int | None = None,
        password5: Any | None = None,
        logon_timeout: int | None = None,
        ldap_server: str | None = None,
        group_poll_interval: int | None = None,
        ldap_poll: Literal["enable", "disable"] | None = None,
        ldap_poll_interval: int | None = None,
        ldap_poll_filter: str | None = None,
        user_info_server: str | None = None,
        ssl: Literal["enable", "disable"] | None = None,
        sni: str | None = None,
        ssl_server_host_ip_check: Literal["enable", "disable"] | None = None,
        ssl_trusted_cert: str | None = None,
        source_ip: str | None = None,
        source_ip6: str | None = None,
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
        Update existing user/fsso object.

        Configure Fortinet Single Sign On (FSSO) agents.

        Args:
            payload_dict: Object data as dict. Must include name (primary key).
            name: Name.
            type: Server type.
            server: Domain name or IP address of the first FSSO collector agent.
            port: Port of the first FSSO collector agent.
            password: Password of the first FSSO collector agent.
            server2: Domain name or IP address of the second FSSO collector agent.
            port2: Port of the second FSSO collector agent.
            password2: Password of the second FSSO collector agent.
            server3: Domain name or IP address of the third FSSO collector agent.
            port3: Port of the third FSSO collector agent.
            password3: Password of the third FSSO collector agent.
            server4: Domain name or IP address of the fourth FSSO collector agent.
            port4: Port of the fourth FSSO collector agent.
            password4: Password of the fourth FSSO collector agent.
            server5: Domain name or IP address of the fifth FSSO collector agent.
            port5: Port of the fifth FSSO collector agent.
            password5: Password of the fifth FSSO collector agent.
            logon_timeout: Interval in minutes to keep logons after FSSO server down.
            ldap_server: LDAP server to get group information.
            group_poll_interval: Interval in minutes within to fetch groups from FSSO server, or unset to disable.
            ldap_poll: Enable/disable automatic fetching of groups from LDAP server.
            ldap_poll_interval: Interval in minutes within to fetch groups from LDAP server.
            ldap_poll_filter: Filter used to fetch groups.
            user_info_server: LDAP server to get user information.
            ssl: Enable/disable use of SSL.
            sni: Server Name Indication.
            ssl_server_host_ip_check: Enable/disable server host/IP verification.
            ssl_trusted_cert: Trusted server certificate or CA certificate.
            source_ip: Source IP for communications to FSSO agent.
            source_ip6: IPv6 source for communications to FSSO agent.
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
            >>> result = fgt.api.cmdb.user_fsso.put(
            ...     name=1,
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "name": 1,
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.user_fsso.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Build payload using helper function with auto-normalization
        # This automatically converts strings/lists to [{'name': '...'}] format for list fields
        # To disable auto-normalization, use build_cmdb_payload directly
        payload_data = build_api_payload(
            name=name,
            type=type,
            server=server,
            port=port,
            password=password,
            server2=server2,
            port2=port2,
            password2=password2,
            server3=server3,
            port3=port3,
            password3=password3,
            server4=server4,
            port4=port4,
            password4=password4,
            server5=server5,
            port5=port5,
            password5=password5,
            logon_timeout=logon_timeout,
            ldap_server=ldap_server,
            group_poll_interval=group_poll_interval,
            ldap_poll=ldap_poll,
            ldap_poll_interval=ldap_poll_interval,
            ldap_poll_filter=ldap_poll_filter,
            user_info_server=user_info_server,
            ssl=ssl,
            sni=sni,
            ssl_server_host_ip_check=ssl_server_host_ip_check,
            ssl_trusted_cert=ssl_trusted_cert,
            source_ip=source_ip,
            source_ip6=source_ip6,
            interface_select_method=interface_select_method,
            interface=interface,
            vrf_select=vrf_select,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.fsso import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/user/fsso",
            )
        
        name_value = payload_data.get("name")
        if not name_value:
            raise ValueError("name is required for PUT")
        endpoint = "/user/fsso/" + str(name_value)

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
        type: Literal["default", "fortinac"] | None = None,
        server: str | None = None,
        port: int | None = None,
        password: Any | None = None,
        server2: str | None = None,
        port2: int | None = None,
        password2: Any | None = None,
        server3: str | None = None,
        port3: int | None = None,
        password3: Any | None = None,
        server4: str | None = None,
        port4: int | None = None,
        password4: Any | None = None,
        server5: str | None = None,
        port5: int | None = None,
        password5: Any | None = None,
        logon_timeout: int | None = None,
        ldap_server: str | None = None,
        group_poll_interval: int | None = None,
        ldap_poll: Literal["enable", "disable"] | None = None,
        ldap_poll_interval: int | None = None,
        ldap_poll_filter: str | None = None,
        user_info_server: str | None = None,
        ssl: Literal["enable", "disable"] | None = None,
        sni: str | None = None,
        ssl_server_host_ip_check: Literal["enable", "disable"] | None = None,
        ssl_trusted_cert: str | None = None,
        source_ip: str | None = None,
        source_ip6: str | None = None,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = None,
        interface: str | None = None,
        vrf_select: int | None = None,
        q_action: Literal["clone"] | None = None,
        q_nkey: str | None = None,
        q_scope: str | None = None,
        vdom: str | bool | None = None,
        error_mode: Literal["raise", "return", "print"] | None = None,
        error_format: Literal["detailed", "simple", "code_only"] | None = None,
    ):  # type: ignore[no-untyped-def]
        """
        Create new user/fsso object.

        Configure Fortinet Single Sign On (FSSO) agents.

        Args:
            payload_dict: Complete object data as dict. Alternative to individual parameters.
            name: Name.
            type: Server type.
            server: Domain name or IP address of the first FSSO collector agent.
            port: Port of the first FSSO collector agent.
            password: Password of the first FSSO collector agent.
            server2: Domain name or IP address of the second FSSO collector agent.
            port2: Port of the second FSSO collector agent.
            password2: Password of the second FSSO collector agent.
            server3: Domain name or IP address of the third FSSO collector agent.
            port3: Port of the third FSSO collector agent.
            password3: Password of the third FSSO collector agent.
            server4: Domain name or IP address of the fourth FSSO collector agent.
            port4: Port of the fourth FSSO collector agent.
            password4: Password of the fourth FSSO collector agent.
            server5: Domain name or IP address of the fifth FSSO collector agent.
            port5: Port of the fifth FSSO collector agent.
            password5: Password of the fifth FSSO collector agent.
            logon_timeout: Interval in minutes to keep logons after FSSO server down.
            ldap_server: LDAP server to get group information.
            group_poll_interval: Interval in minutes within to fetch groups from FSSO server, or unset to disable.
            ldap_poll: Enable/disable automatic fetching of groups from LDAP server.
            ldap_poll_interval: Interval in minutes within to fetch groups from LDAP server.
            ldap_poll_filter: Filter used to fetch groups.
            user_info_server: LDAP server to get user information.
            ssl: Enable/disable use of SSL.
            sni: Server Name Indication.
            ssl_server_host_ip_check: Enable/disable server host/IP verification.
            ssl_trusted_cert: Trusted server certificate or CA certificate.
            source_ip: Source IP for communications to FSSO agent.
            source_ip6: IPv6 source for communications to FSSO agent.
            interface_select_method: Specify how to select outgoing interface to reach server.
            interface: Specify outgoing interface to reach server.
            vrf_select: VRF ID used for connection to server.
            vdom: Virtual domain name. Use True for global, string for specific VDOM.
            error_mode: Override client-level error_mode. "raise" raises exceptions, "return" returns error dict, "print" prints errors.
            error_format: Override client-level error_format. "detailed" provides full context, "simple" is concise, "code_only" returns just status code.

        Returns:
            FortiObject instance with created object. Use .dict, .json, or .raw to access as dictionary.

        Examples:
            >>> # Create using individual parameters
            >>> result = fgt.api.cmdb.user_fsso.post(
            ...     name="example",
            ...     # ... other required fields
            ... )
            >>> print(f"Created name: {result['results']}")
            
            >>> # Create using payload dict
            >>> payload = Fsso.defaults()  # Start with defaults
            >>> payload['name'] = 'my-object'
            >>> result = fgt.api.cmdb.user_fsso.post(payload_dict=payload)

        Note:
            Required fields: {{ ", ".join(Fsso.required_fields()) }}
            
            Use Fsso.help('field_name') to get field details.

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
            type=type,
            server=server,
            port=port,
            password=password,
            server2=server2,
            port2=port2,
            password2=password2,
            server3=server3,
            port3=port3,
            password3=password3,
            server4=server4,
            port4=port4,
            password4=password4,
            server5=server5,
            port5=port5,
            password5=password5,
            logon_timeout=logon_timeout,
            ldap_server=ldap_server,
            group_poll_interval=group_poll_interval,
            ldap_poll=ldap_poll,
            ldap_poll_interval=ldap_poll_interval,
            ldap_poll_filter=ldap_poll_filter,
            user_info_server=user_info_server,
            ssl=ssl,
            sni=sni,
            ssl_server_host_ip_check=ssl_server_host_ip_check,
            ssl_trusted_cert=ssl_trusted_cert,
            source_ip=source_ip,
            source_ip6=source_ip6,
            interface_select_method=interface_select_method,
            interface=interface,
            vrf_select=vrf_select,
            data=payload_dict,
        )

        # Check for deprecated fields and warn users
        from ._helpers.fsso import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/user/fsso",
            )

        endpoint = "/user/fsso"
        
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
        Delete user/fsso object.

        Configure Fortinet Single Sign On (FSSO) agents.

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
            >>> result = fgt.api.cmdb.user_fsso.delete(name=1)
            
            >>> # Check for errors
            >>> if result.get('status') != 'success':
            ...     print(f"Delete failed: {result.get('error')}")

        See Also:
            - exists(): Check if object exists before deleting
            - get(): Retrieve object to verify it exists
        """
        if not name:
            raise ValueError("name is required for DELETE")
        endpoint = "/user/fsso/" + str(name)

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
        Check if user/fsso object exists.

        Verifies whether an object exists by attempting to retrieve it and checking the response status.

        Args:
            name: Primary key identifier
            vdom: Virtual domain name

        Returns:
            True if object exists, False otherwise

        Examples:
            >>> # Check if object exists before operations
            >>> if fgt.api.cmdb.user_fsso.exists(name=1):
            ...     print("Object exists")
            ... else:
            ...     print("Object not found")
            
            >>> # Conditional delete
            >>> if fgt.api.cmdb.user_fsso.exists(name=1):
            ...     fgt.api.cmdb.user_fsso.delete(name=1)

        See Also:
            - get(): Retrieve full object data
            - set(): Create or update automatically based on existence
        """
        # Use direct request with silent error handling to avoid logging 404s
        # This is expected behavior for exists() - 404 just means "doesn't exist"
        endpoint = "/user/fsso"
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
        type: Literal["default", "fortinac"] | None = None,
        server: str | None = None,
        port: int | None = None,
        password: Any | None = None,
        server2: str | None = None,
        port2: int | None = None,
        password2: Any | None = None,
        server3: str | None = None,
        port3: int | None = None,
        password3: Any | None = None,
        server4: str | None = None,
        port4: int | None = None,
        password4: Any | None = None,
        server5: str | None = None,
        port5: int | None = None,
        password5: Any | None = None,
        logon_timeout: int | None = None,
        ldap_server: str | None = None,
        group_poll_interval: int | None = None,
        ldap_poll: Literal["enable", "disable"] | None = None,
        ldap_poll_interval: int | None = None,
        ldap_poll_filter: str | None = None,
        user_info_server: str | None = None,
        ssl: Literal["enable", "disable"] | None = None,
        sni: str | None = None,
        ssl_server_host_ip_check: Literal["enable", "disable"] | None = None,
        ssl_trusted_cert: str | None = None,
        source_ip: str | None = None,
        source_ip6: str | None = None,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = None,
        interface: str | None = None,
        vrf_select: int | None = None,
        vdom: str | bool | None = None,
        error_mode: Literal["raise", "return", "print"] | None = None,
        error_format: Literal["detailed", "simple", "code_only"] | None = None,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Create or update user/fsso object (intelligent operation).

        Automatically determines whether to create (POST) or update (PUT) based on
        whether the resource exists. Requires the primary key (name) in the payload.

        Args:
            payload_dict: Resource data including name (primary key)
            name: Field name
            type: Field type
            server: Field server
            port: Field port
            password: Field password
            server2: Field server2
            port2: Field port2
            password2: Field password2
            server3: Field server3
            port3: Field port3
            password3: Field password3
            server4: Field server4
            port4: Field port4
            password4: Field password4
            server5: Field server5
            port5: Field port5
            password5: Field password5
            logon_timeout: Field logon-timeout
            ldap_server: Field ldap-server
            group_poll_interval: Field group-poll-interval
            ldap_poll: Field ldap-poll
            ldap_poll_interval: Field ldap-poll-interval
            ldap_poll_filter: Field ldap-poll-filter
            user_info_server: Field user-info-server
            ssl: Field ssl
            sni: Field sni
            ssl_server_host_ip_check: Field ssl-server-host-ip-check
            ssl_trusted_cert: Field ssl-trusted-cert
            source_ip: Field source-ip
            source_ip6: Field source-ip6
            interface_select_method: Field interface-select-method
            interface: Field interface
            vrf_select: Field vrf-select
            vdom: Virtual domain name
            **kwargs: Additional parameters passed to PUT or POST

        Returns:
            FortiObject instance. Use .dict, .json, or .raw to access as dictionary

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Intelligent create or update using field parameters
            >>> result = fgt.api.cmdb.user_fsso.set(
            ...     name=1,
            ...     # ... other fields
            ... )
            
            >>> # Or using payload dict
            >>> payload = {
            ...     "name": 1,
            ...     "field1": "value1",
            ...     "field2": "value2",
            ... }
            >>> result = fgt.api.cmdb.user_fsso.set(payload_dict=payload)
            >>> # Will POST if object doesn't exist, PUT if it does
            
            >>> # Idempotent configuration
            >>> for obj_data in configuration_list:
            ...     fgt.api.cmdb.user_fsso.set(payload_dict=obj_data)
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
            type=type,
            server=server,
            port=port,
            password=password,
            server2=server2,
            port2=port2,
            password2=password2,
            server3=server3,
            port3=port3,
            password3=password3,
            server4=server4,
            port4=port4,
            password4=password4,
            server5=server5,
            port5=port5,
            password5=password5,
            logon_timeout=logon_timeout,
            ldap_server=ldap_server,
            group_poll_interval=group_poll_interval,
            ldap_poll=ldap_poll,
            ldap_poll_interval=ldap_poll_interval,
            ldap_poll_filter=ldap_poll_filter,
            user_info_server=user_info_server,
            ssl=ssl,
            sni=sni,
            ssl_server_host_ip_check=ssl_server_host_ip_check,
            ssl_trusted_cert=ssl_trusted_cert,
            source_ip=source_ip,
            source_ip6=source_ip6,
            interface_select_method=interface_select_method,
            interface=interface,
            vrf_select=vrf_select,
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
        Move user/fsso object to a new position.
        
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
            >>> fgt.api.cmdb.user_fsso.move(
            ...     name=100,
            ...     action="before",
            ...     reference_name=50
            ... )
        """
        return self._client.request(
            method="PUT",
            path=f"/api/v2/cmdb/user/fsso",
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
        Clone user/fsso object.
        
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
            >>> fgt.api.cmdb.user_fsso.clone(
            ...     name=1,
            ...     new_name=100
            ... )
        """
        return self._client.request(
            method="POST",
            path=f"/api/v2/cmdb/user/fsso",
            params={
                "name": name,
                "new_name": new_name,
                "action": "clone",
                "vdom": vdom,
                **kwargs,
            },
        )


