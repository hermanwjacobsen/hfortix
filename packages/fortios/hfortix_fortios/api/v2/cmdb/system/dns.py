"""
FortiOS CMDB - System dns

Configuration endpoint for managing cmdb system/dns objects.

API Endpoints:
    GET    /cmdb/system/dns
    POST   /cmdb/system/dns
    PUT    /cmdb/system/dns/{identifier}
    DELETE /cmdb/system/dns/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.system_dns.get()
    >>>
    >>> # Create with auto-normalization (strings/lists converted automatically)
    >>> result = fgt.api.cmdb.system_dns.post(
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

class Dns(CRUDEndpoint, MetadataMixin):
    """Dns Operations."""
    
    # Configure metadata mixin to use this endpoint's helper module
    _helper_module_name = "dns"
    
    # ========================================================================
    # Table Fields Metadata (for normalization)
    # Auto-generated from schema - supports flexible input formats
    # ========================================================================
    _TABLE_FIELDS = {
        "server_hostname": {
            "mkey": "hostname",
            "required_fields": ['hostname'],
            "example": "[{'hostname': 'value'}]",
        },
        "domain": {
            "mkey": "domain",
            "required_fields": ['domain'],
            "example": "[{'domain': 'value'}]",
        },
    }
    
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
        """Initialize Dns endpoint."""
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
        Retrieve system/dns configuration.

        Configure DNS.

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
            >>> # Get all system/dns objects
            >>> result = fgt.api.cmdb.system_dns.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.system_dns.get(
            ...     filter=["name==test", "status==enable"]
            ... )
            
            >>> # Get with pagination
            >>> result = fgt.api.cmdb.system_dns.get(
            ...     start=0, count=100
            ... )
            
            >>> # Get schema information  
            >>> schema = fgt.api.cmdb.system_dns.get_schema()

        See Also:
            - post(): Create new system/dns object
            - put(): Update existing system/dns object
            - delete(): Remove system/dns object
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
            endpoint = f"/system/dns/{name}"
            unwrap_single = True
        else:
            endpoint = "/system/dns"
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
            >>> schema = fgt.api.cmdb.system_dns.get_schema()
            >>> print(schema['results'])
            
            >>> # Get JSON Schema format (if supported)
            >>> json_schema = fgt.api.cmdb.system_dns.get_schema(format="json-schema")
        
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
        primary: str | None = None,
        secondary: str | None = None,
        protocol: Literal["cleartext", "dot", "doh"] | list[str] | None = None,
        ssl_certificate: str | None = None,
        server_hostname: str | list[str] | list[dict[str, Any]] | None = None,
        domain: str | list[str] | list[dict[str, Any]] | None = None,
        ip6_primary: str | None = None,
        ip6_secondary: str | None = None,
        timeout: int | None = None,
        retry: int | None = None,
        dns_cache_limit: int | None = None,
        dns_cache_ttl: int | None = None,
        cache_notfound_responses: Literal["disable", "enable"] | None = None,
        source_ip: str | None = None,
        source_ip_interface: str | None = None,
        root_servers: str | list[str] | None = None,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = None,
        interface: str | None = None,
        vrf_select: int | None = None,
        server_select_method: Literal["least-rtt", "failover"] | None = None,
        alt_primary: str | None = None,
        alt_secondary: str | None = None,
        log: Literal["disable", "error", "all"] | None = None,
        fqdn_cache_ttl: int | None = None,
        fqdn_max_refresh: int | None = None,
        fqdn_min_refresh: int | None = None,
        hostname_ttl: int | None = None,
        hostname_limit: int | None = None,
        q_action: Literal["move"] | None = None,
        q_before: str | None = None,
        q_after: str | None = None,
        q_scope: str | None = None,
        vdom: str | bool | None = None,
        error_mode: Literal["raise", "return", "print"] | None = None,
        error_format: Literal["detailed", "simple", "code_only"] | None = None,
    ):  # type: ignore[no-untyped-def]
        """
        Update existing system/dns object.

        Configure DNS.

        Args:
            payload_dict: Object data as dict. Must include name (primary key).
            primary: Primary DNS server IP address.
            secondary: Secondary DNS server IP address.
            protocol: DNS transport protocols.
            ssl_certificate: Name of local certificate for SSL connections.
            server_hostname: DNS server host name list.
                Default format: [{'hostname': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'hostname': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'hostname': 'val1'}, ...]
                  - List of dicts: [{'hostname': 'value'}] (recommended)
            domain: Search suffix list for hostname lookup.
                Default format: [{'domain': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'domain': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'domain': 'val1'}, ...]
                  - List of dicts: [{'domain': 'value'}] (recommended)
            ip6_primary: Primary DNS server IPv6 address.
            ip6_secondary: Secondary DNS server IPv6 address.
            timeout: DNS query timeout interval in seconds (1 - 10).
            retry: Number of times to retry (0 - 5).
            dns_cache_limit: Maximum number of records in the DNS cache.
            dns_cache_ttl: Duration in seconds that the DNS cache retains information.
            cache_notfound_responses: Enable/disable response from the DNS server when a record is not in cache.
            source_ip: IP address used by the DNS server as its source IP.
            source_ip_interface: IP address of the specified interface as the source IP address.
            root_servers: Configure up to two preferred servers that serve the DNS root zone (default uses all 13 root servers).
            interface_select_method: Specify how to select outgoing interface to reach server.
            interface: Specify outgoing interface to reach server.
            vrf_select: VRF ID used for connection to server.
            server_select_method: Specify how configured servers are prioritized.
            alt_primary: Alternate primary DNS server. This is not used as a failover DNS server.
            alt_secondary: Alternate secondary DNS server. This is not used as a failover DNS server.
            log: Local DNS log setting.
            fqdn_cache_ttl: FQDN cache time to live in seconds (0 - 86400, default = 0).
            fqdn_max_refresh: FQDN cache maximum refresh time in seconds (3600 - 86400, default = 3600).
            fqdn_min_refresh: FQDN cache minimum refresh time in seconds (10 - 3600, default = 60).
            hostname_ttl: TTL of hostname table entries (60 - 86400).
            hostname_limit: Limit of the number of hostname table entries (0 - 50000).
            vdom: Virtual domain name.
            error_mode: Override client-level error_mode. "raise" raises exceptions, "return" returns error dict, "print" prints errors.
            error_format: Override client-level error_format. "detailed" provides full context, "simple" is concise, "code_only" returns just status code.

        Returns:
            FortiObject instance. Use .dict, .json, or .raw to access as dictionary.

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.system_dns.put(
            ...     name="existing-object",
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "name": "existing-object",
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.system_dns.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Apply normalization for table fields (supports flexible input formats)
        if server_hostname is not None:
            server_hostname = normalize_table_field(
                server_hostname,
                mkey="hostname",
                required_fields=['hostname'],
                field_name="server_hostname",
                example="[{'hostname': 'value'}]",
            )
        if domain is not None:
            domain = normalize_table_field(
                domain,
                mkey="domain",
                required_fields=['domain'],
                field_name="domain",
                example="[{'domain': 'value'}]",
            )
        
        # Build payload using helper function with auto-normalization
        # This automatically converts strings/lists to [{'name': '...'}] format for list fields
        # To disable auto-normalization, use build_cmdb_payload directly
        payload_data = build_api_payload(
            primary=primary,
            secondary=secondary,
            protocol=protocol,
            ssl_certificate=ssl_certificate,
            server_hostname=server_hostname,
            domain=domain,
            ip6_primary=ip6_primary,
            ip6_secondary=ip6_secondary,
            timeout=timeout,
            retry=retry,
            dns_cache_limit=dns_cache_limit,
            dns_cache_ttl=dns_cache_ttl,
            cache_notfound_responses=cache_notfound_responses,
            source_ip=source_ip,
            source_ip_interface=source_ip_interface,
            root_servers=root_servers,
            interface_select_method=interface_select_method,
            interface=interface,
            vrf_select=vrf_select,
            server_select_method=server_select_method,
            alt_primary=alt_primary,
            alt_secondary=alt_secondary,
            log=log,
            fqdn_cache_ttl=fqdn_cache_ttl,
            fqdn_max_refresh=fqdn_max_refresh,
            fqdn_min_refresh=fqdn_min_refresh,
            hostname_ttl=hostname_ttl,
            hostname_limit=hostname_limit,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.dns import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/system/dns",
            )
        
        # Singleton endpoint - no identifier needed
        endpoint = "/system/dns"

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
        Move system/dns object to a new position.
        
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
            >>> fgt.api.cmdb.system_dns.move(
            ...     name="object1",
            ...     action="before",
            ...     reference_name="object2"
            ... )
        """
        return self._client.request(
            method="PUT",
            path=f"/api/v2/cmdb/system/dns",
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
        Clone system/dns object.
        
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
            >>> fgt.api.cmdb.system_dns.clone(
            ...     name="template",
            ...     new_name="new-from-template"
            ... )
        """
        return self._client.request(
            method="POST",
            path=f"/api/v2/cmdb/system/dns",
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
        Check if system/dns object exists.
        
        Args:
            name: Name to check
            vdom: Virtual domain name
            
        Returns:
            True if object exists, False otherwise
            
        Example:
            >>> # Check before creating
            >>> if not fgt.api.cmdb.system_dns.exists(name="myobj"):
            ...     fgt.api.cmdb.system_dns.post(payload_dict=data)
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

