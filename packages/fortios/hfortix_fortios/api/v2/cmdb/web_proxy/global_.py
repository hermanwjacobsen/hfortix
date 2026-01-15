"""
FortiOS CMDB - Web_proxy global_

Configuration endpoint for managing cmdb web_proxy/global_ objects.

API Endpoints:
    GET    /cmdb/web_proxy/global_
    POST   /cmdb/web_proxy/global_
    PUT    /cmdb/web_proxy/global_/{identifier}
    DELETE /cmdb/web_proxy/global_/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.web_proxy_global_.get()
    >>>
    >>> # Create with auto-normalization (strings/lists converted automatically)
    >>> result = fgt.api.cmdb.web_proxy_global_.post(
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

class Global(CRUDEndpoint, MetadataMixin):
    """Global Operations."""
    
    # Configure metadata mixin to use this endpoint's helper module
    _helper_module_name = "global_"
    
    # ========================================================================
    # Table Fields Metadata (for normalization)
    # Auto-generated from schema - supports flexible input formats
    # ========================================================================
    _TABLE_FIELDS = {
        "learn_client_ip_srcaddr": {
            "mkey": "name",
            "required_fields": ['name'],
            "example": "[{'name': 'value'}]",
        },
        "learn_client_ip_srcaddr6": {
            "mkey": "name",
            "required_fields": ['name'],
            "example": "[{'name': 'value'}]",
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
        """Initialize Global endpoint."""
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
        Retrieve web_proxy/global_ configuration.

        Configure Web proxy global settings.

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
            >>> # Get all web_proxy/global_ objects
            >>> result = fgt.api.cmdb.web_proxy_global_.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.web_proxy_global_.get(
            ...     filter=["name==test", "status==enable"]
            ... )
            
            >>> # Get with pagination
            >>> result = fgt.api.cmdb.web_proxy_global_.get(
            ...     start=0, count=100
            ... )
            
            >>> # Get schema information  
            >>> schema = fgt.api.cmdb.web_proxy_global_.get_schema()

        See Also:
            - post(): Create new web_proxy/global_ object
            - put(): Update existing web_proxy/global_ object
            - delete(): Remove web_proxy/global_ object
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
            endpoint = f"/web-proxy/global/{name}"
            unwrap_single = True
        else:
            endpoint = "/web-proxy/global"
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
            >>> schema = fgt.api.cmdb.web_proxy_global_.get_schema()
            >>> print(schema['results'])
            
            >>> # Get JSON Schema format (if supported)
            >>> json_schema = fgt.api.cmdb.web_proxy_global_.get_schema(format="json-schema")
        
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
        ssl_cert: str | None = None,
        ssl_ca_cert: str | None = None,
        fast_policy_match: Literal["enable", "disable"] | None = None,
        ldap_user_cache: Literal["enable", "disable"] | None = None,
        proxy_fqdn: str | None = None,
        max_request_length: int | None = None,
        max_message_length: int | None = None,
        http2_client_window_size: int | None = None,
        http2_server_window_size: int | None = None,
        auth_sign_timeout: int | None = None,
        strict_web_check: Literal["enable", "disable"] | None = None,
        forward_proxy_auth: Literal["enable", "disable"] | None = None,
        forward_server_affinity_timeout: int | None = None,
        max_waf_body_cache_length: int | None = None,
        webproxy_profile: str | None = None,
        learn_client_ip: Literal["enable", "disable"] | None = None,
        always_learn_client_ip: Literal["enable", "disable"] | None = None,
        learn_client_ip_from_header: Literal["true-client-ip", "x-real-ip", "x-forwarded-for"] | list[str] | None = None,
        learn_client_ip_srcaddr: str | list[str] | list[dict[str, Any]] | None = None,
        learn_client_ip_srcaddr6: str | list[str] | list[dict[str, Any]] | None = None,
        src_affinity_exempt_addr: str | list[str] | None = None,
        src_affinity_exempt_addr6: str | list[str] | None = None,
        policy_partial_match: Literal["enable", "disable"] | None = None,
        log_policy_pending: Literal["enable", "disable"] | None = None,
        log_forward_server: Literal["enable", "disable"] | None = None,
        log_app_id: Literal["enable", "disable"] | None = None,
        proxy_transparent_cert_inspection: Literal["enable", "disable"] | None = None,
        request_obs_fold: Literal["replace-with-sp", "block", "keep"] | None = None,
        q_action: Literal["move"] | None = None,
        q_before: str | None = None,
        q_after: str | None = None,
        q_scope: str | None = None,
        vdom: str | bool | None = None,
        error_mode: Literal["raise", "return", "print"] | None = None,
        error_format: Literal["detailed", "simple", "code_only"] | None = None,
    ):  # type: ignore[no-untyped-def]
        """
        Update existing web_proxy/global_ object.

        Configure Web proxy global settings.

        Args:
            payload_dict: Object data as dict. Must include name (primary key).
            ssl_cert: SSL certificate for SSL interception.
            ssl_ca_cert: SSL CA certificate for SSL interception.
            fast_policy_match: Enable/disable fast matching algorithm for explicit and transparent proxy policy.
            ldap_user_cache: Enable/disable LDAP user cache for explicit and transparent proxy user.
            proxy_fqdn: Fully Qualified Domain Name of the explicit web proxy (default = default.fqdn) that clients connect to.
            max_request_length: Maximum length of HTTP request line (2 - 64 Kbytes, default = 8).
            max_message_length: Maximum length of HTTP message, not including body (16 - 256 Kbytes, default = 32).
            http2_client_window_size: HTTP/2 client initial window size in bytes (65535 - 2147483647, default = 1048576 (1MB)).
            http2_server_window_size: HTTP/2 server initial window size in bytes (65535 - 2147483647, default = 1048576 (1MB)).
            auth_sign_timeout: Proxy auth query sign timeout in seconds (30 - 3600, default = 120).
            strict_web_check: Enable/disable strict web checking to block web sites that send incorrect headers that don't conform to HTTP.
            forward_proxy_auth: Enable/disable forwarding proxy authentication headers.
            forward_server_affinity_timeout: Period of time before the source IP's traffic is no longer assigned to the forwarding server (6 - 60 min, default = 30).
            max_waf_body_cache_length: Maximum length of HTTP messages processed by Web Application Firewall (WAF) (1 - 1024 Kbytes, default = 1).
            webproxy_profile: Name of the web proxy profile to apply when explicit proxy traffic is allowed by default and traffic is accepted that does not match an explicit proxy policy.
            learn_client_ip: Enable/disable learning the client's IP address from headers.
            always_learn_client_ip: Enable/disable learning the client's IP address from headers for every request.
            learn_client_ip_from_header: Learn client IP address from the specified headers.
            learn_client_ip_srcaddr: Source address name (srcaddr or srcaddr6 must be set).
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            learn_client_ip_srcaddr6: IPv6 Source address name (srcaddr or srcaddr6 must be set).
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            src_affinity_exempt_addr: IPv4 source addresses to exempt proxy affinity.
            src_affinity_exempt_addr6: IPv6 source addresses to exempt proxy affinity.
            policy_partial_match: Enable/disable policy partial matching.
            log_policy_pending: Enable/disable logging sessions that are pending on policy matching.
            log_forward_server: Enable/disable forward server name logging in forward traffic log.
            log_app_id: Enable/disable always log application type in traffic log.
            proxy_transparent_cert_inspection: Enable/disable transparent proxy certificate inspection.
            request_obs_fold: Action when HTTP/1.x request header contains obs-fold (default = keep).
            vdom: Virtual domain name.
            error_mode: Override client-level error_mode. "raise" raises exceptions, "return" returns error dict, "print" prints errors.
            error_format: Override client-level error_format. "detailed" provides full context, "simple" is concise, "code_only" returns just status code.

        Returns:
            FortiObject instance. Use .dict, .json, or .raw to access as dictionary.

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.web_proxy_global_.put(
            ...     name="existing-object",
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "name": "existing-object",
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.web_proxy_global_.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Apply normalization for table fields (supports flexible input formats)
        if learn_client_ip_srcaddr is not None:
            learn_client_ip_srcaddr = normalize_table_field(
                learn_client_ip_srcaddr,
                mkey="name",
                required_fields=['name'],
                field_name="learn_client_ip_srcaddr",
                example="[{'name': 'value'}]",
            )
        if learn_client_ip_srcaddr6 is not None:
            learn_client_ip_srcaddr6 = normalize_table_field(
                learn_client_ip_srcaddr6,
                mkey="name",
                required_fields=['name'],
                field_name="learn_client_ip_srcaddr6",
                example="[{'name': 'value'}]",
            )
        
        # Build payload using helper function with auto-normalization
        # This automatically converts strings/lists to [{'name': '...'}] format for list fields
        # To disable auto-normalization, use build_cmdb_payload directly
        payload_data = build_api_payload(
            ssl_cert=ssl_cert,
            ssl_ca_cert=ssl_ca_cert,
            fast_policy_match=fast_policy_match,
            ldap_user_cache=ldap_user_cache,
            proxy_fqdn=proxy_fqdn,
            max_request_length=max_request_length,
            max_message_length=max_message_length,
            http2_client_window_size=http2_client_window_size,
            http2_server_window_size=http2_server_window_size,
            auth_sign_timeout=auth_sign_timeout,
            strict_web_check=strict_web_check,
            forward_proxy_auth=forward_proxy_auth,
            forward_server_affinity_timeout=forward_server_affinity_timeout,
            max_waf_body_cache_length=max_waf_body_cache_length,
            webproxy_profile=webproxy_profile,
            learn_client_ip=learn_client_ip,
            always_learn_client_ip=always_learn_client_ip,
            learn_client_ip_from_header=learn_client_ip_from_header,
            learn_client_ip_srcaddr=learn_client_ip_srcaddr,
            learn_client_ip_srcaddr6=learn_client_ip_srcaddr6,
            src_affinity_exempt_addr=src_affinity_exempt_addr,
            src_affinity_exempt_addr6=src_affinity_exempt_addr6,
            policy_partial_match=policy_partial_match,
            log_policy_pending=log_policy_pending,
            log_forward_server=log_forward_server,
            log_app_id=log_app_id,
            proxy_transparent_cert_inspection=proxy_transparent_cert_inspection,
            request_obs_fold=request_obs_fold,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.global_ import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/web_proxy/global_",
            )
        
        # Singleton endpoint - no identifier needed
        endpoint = "/web-proxy/global"

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
        Move web_proxy/global_ object to a new position.
        
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
            >>> fgt.api.cmdb.web_proxy_global_.move(
            ...     name="object1",
            ...     action="before",
            ...     reference_name="object2"
            ... )
        """
        return self._client.request(
            method="PUT",
            path=f"/api/v2/cmdb/web-proxy/global",
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
        Clone web_proxy/global_ object.
        
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
            >>> fgt.api.cmdb.web_proxy_global_.clone(
            ...     name="template",
            ...     new_name="new-from-template"
            ... )
        """
        return self._client.request(
            method="POST",
            path=f"/api/v2/cmdb/web-proxy/global",
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
        Check if web_proxy/global_ object exists.
        
        Args:
            name: Name to check
            vdom: Virtual domain name
            
        Returns:
            True if object exists, False otherwise
            
        Example:
            >>> # Check before creating
            >>> if not fgt.api.cmdb.web_proxy_global_.exists(name="myobj"):
            ...     fgt.api.cmdb.web_proxy_global_.post(payload_dict=data)
        """
        # Use direct request with silent error handling to avoid logging 404s
        # This is expected behavior for exists() - 404 just means "doesn't exist"
        endpoint = "/web_proxy/global_"
        endpoint = f"{endpoint}/{quote_path_param(name)}"
        
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

