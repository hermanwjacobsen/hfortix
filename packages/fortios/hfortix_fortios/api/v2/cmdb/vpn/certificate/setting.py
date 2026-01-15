"""
FortiOS CMDB - Vpn certificate setting

Configuration endpoint for managing cmdb vpn/certificate/setting objects.

API Endpoints:
    GET    /cmdb/vpn/certificate/setting
    POST   /cmdb/vpn/certificate/setting
    PUT    /cmdb/vpn/certificate/setting/{identifier}
    DELETE /cmdb/vpn/certificate/setting/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.vpn_certificate_setting.get()
    >>>
    >>> # Create with auto-normalization (strings/lists converted automatically)
    >>> result = fgt.api.cmdb.vpn_certificate_setting.post(
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
        Retrieve vpn/certificate/setting configuration.

        VPN certificate setting.

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
            >>> # Get all vpn/certificate/setting objects
            >>> result = fgt.api.cmdb.vpn_certificate_setting.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.vpn_certificate_setting.get(
            ...     filter=["name==test", "status==enable"]
            ... )
            
            >>> # Get with pagination
            >>> result = fgt.api.cmdb.vpn_certificate_setting.get(
            ...     start=0, count=100
            ... )
            
            >>> # Get schema information  
            >>> schema = fgt.api.cmdb.vpn_certificate_setting.get_schema()

        See Also:
            - post(): Create new vpn/certificate/setting object
            - put(): Update existing vpn/certificate/setting object
            - delete(): Remove vpn/certificate/setting object
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
            endpoint = f"/vpn.certificate/setting/{name}"
            unwrap_single = True
        else:
            endpoint = "/vpn.certificate/setting"
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
            >>> schema = fgt.api.cmdb.vpn_certificate_setting.get_schema()
            >>> print(schema['results'])
            
            >>> # Get JSON Schema format (if supported)
            >>> json_schema = fgt.api.cmdb.vpn_certificate_setting.get_schema(format="json-schema")
        
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
        ocsp_status: Literal["enable", "mandatory", "disable"] | None = None,
        ocsp_option: Literal["certificate", "server"] | None = None,
        proxy: str | None = None,
        proxy_port: int | None = None,
        proxy_username: str | None = None,
        proxy_password: Any | None = None,
        source_ip: str | None = None,
        ocsp_default_server: str | None = None,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = None,
        interface: str | None = None,
        vrf_select: int | None = None,
        check_ca_cert: Literal["enable", "disable"] | None = None,
        check_ca_chain: Literal["enable", "disable"] | None = None,
        subject_match: Literal["substring", "value"] | None = None,
        subject_set: Literal["subset", "superset"] | None = None,
        cn_match: Literal["substring", "value"] | None = None,
        cn_allow_multi: Literal["disable", "enable"] | None = None,
        crl_verification: str | None = None,
        strict_ocsp_check: Literal["enable", "disable"] | None = None,
        ssl_min_proto_version: Literal["default", "SSLv3", "TLSv1", "TLSv1-1", "TLSv1-2", "TLSv1-3"] | None = None,
        cmp_save_extra_certs: Literal["enable", "disable"] | None = None,
        cmp_key_usage_checking: Literal["enable", "disable"] | None = None,
        cert_expire_warning: int | None = None,
        certname_rsa1024: str | None = None,
        certname_rsa2048: str | None = None,
        certname_rsa4096: str | None = None,
        certname_dsa1024: str | None = None,
        certname_dsa2048: str | None = None,
        certname_ecdsa256: str | None = None,
        certname_ecdsa384: str | None = None,
        certname_ecdsa521: str | None = None,
        certname_ed25519: str | None = None,
        certname_ed448: str | None = None,
        q_action: Literal["move"] | None = None,
        q_before: str | None = None,
        q_after: str | None = None,
        q_scope: str | None = None,
        vdom: str | bool | None = None,
        error_mode: Literal["raise", "return", "print"] | None = None,
        error_format: Literal["detailed", "simple", "code_only"] | None = None,
    ):  # type: ignore[no-untyped-def]
        """
        Update existing vpn/certificate/setting object.

        VPN certificate setting.

        Args:
            payload_dict: Object data as dict. Must include name (primary key).
            ocsp_status: Enable/disable receiving certificates using the OCSP.
            ocsp_option: Specify whether the OCSP URL is from certificate or configured OCSP server.
            proxy: Proxy server FQDN or IP for OCSP/CA queries during certificate verification.
            proxy_port: Proxy server port (1 - 65535, default = 8080).
            proxy_username: Proxy server user name.
            proxy_password: Proxy server password.
            source_ip: Source IP address for dynamic AIA and OCSP queries.
            ocsp_default_server: Default OCSP server.
            interface_select_method: Specify how to select outgoing interface to reach server.
            interface: Specify outgoing interface to reach server.
            vrf_select: VRF ID used for connection to server.
            check_ca_cert: Enable/disable verification of the user certificate and pass authentication if any CA in the chain is trusted (default = enable).
            check_ca_chain: Enable/disable verification of the entire certificate chain and pass authentication only if the chain is complete and all of the CAs in the chain are trusted (default = disable).
            subject_match: When searching for a matching certificate, control how to do RDN value matching with certificate subject name (default = substring).
            subject_set: When searching for a matching certificate, control how to do RDN set matching with certificate subject name (default = subset).
            cn_match: When searching for a matching certificate, control how to do CN value matching with certificate subject name (default = substring).
            cn_allow_multi: When searching for a matching certificate, allow multiple CN fields in certificate subject name (default = enable).
            crl_verification: CRL verification options.
            strict_ocsp_check: Enable/disable strict mode OCSP checking.
            ssl_min_proto_version: Minimum supported protocol version for SSL/TLS connections (default is to follow system global setting).
            cmp_save_extra_certs: Enable/disable saving extra certificates in CMP mode (default = disable).
            cmp_key_usage_checking: Enable/disable server certificate key usage checking in CMP mode (default = enable).
            cert_expire_warning: Number of days before a certificate expires to send a warning. Set to 0 to disable sending of the warning (0 - 100, default = 14).
            certname_rsa1024: 1024 bit RSA key certificate for re-signing server certificates for SSL inspection.
            certname_rsa2048: 2048 bit RSA key certificate for re-signing server certificates for SSL inspection.
            certname_rsa4096: 4096 bit RSA key certificate for re-signing server certificates for SSL inspection.
            certname_dsa1024: 1024 bit DSA key certificate for re-signing server certificates for SSL inspection.
            certname_dsa2048: 2048 bit DSA key certificate for re-signing server certificates for SSL inspection.
            certname_ecdsa256: 256 bit ECDSA key certificate for re-signing server certificates for SSL inspection.
            certname_ecdsa384: 384 bit ECDSA key certificate for re-signing server certificates for SSL inspection.
            certname_ecdsa521: 521 bit ECDSA key certificate for re-signing server certificates for SSL inspection.
            certname_ed25519: 253 bit EdDSA key certificate for re-signing server certificates for SSL inspection.
            certname_ed448: 456 bit EdDSA key certificate for re-signing server certificates for SSL inspection.
            vdom: Virtual domain name.
            error_mode: Override client-level error_mode. "raise" raises exceptions, "return" returns error dict, "print" prints errors.
            error_format: Override client-level error_format. "detailed" provides full context, "simple" is concise, "code_only" returns just status code.

        Returns:
            FortiObject instance. Use .dict, .json, or .raw to access as dictionary.

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.vpn_certificate_setting.put(
            ...     name="existing-object",
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "name": "existing-object",
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.vpn_certificate_setting.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Build payload using helper function with auto-normalization
        # This automatically converts strings/lists to [{'name': '...'}] format for list fields
        # To disable auto-normalization, use build_cmdb_payload directly
        payload_data = build_api_payload(
            ocsp_status=ocsp_status,
            ocsp_option=ocsp_option,
            proxy=proxy,
            proxy_port=proxy_port,
            proxy_username=proxy_username,
            proxy_password=proxy_password,
            source_ip=source_ip,
            ocsp_default_server=ocsp_default_server,
            interface_select_method=interface_select_method,
            interface=interface,
            vrf_select=vrf_select,
            check_ca_cert=check_ca_cert,
            check_ca_chain=check_ca_chain,
            subject_match=subject_match,
            subject_set=subject_set,
            cn_match=cn_match,
            cn_allow_multi=cn_allow_multi,
            crl_verification=crl_verification,
            strict_ocsp_check=strict_ocsp_check,
            ssl_min_proto_version=ssl_min_proto_version,
            cmp_save_extra_certs=cmp_save_extra_certs,
            cmp_key_usage_checking=cmp_key_usage_checking,
            cert_expire_warning=cert_expire_warning,
            certname_rsa1024=certname_rsa1024,
            certname_rsa2048=certname_rsa2048,
            certname_rsa4096=certname_rsa4096,
            certname_dsa1024=certname_dsa1024,
            certname_dsa2048=certname_dsa2048,
            certname_ecdsa256=certname_ecdsa256,
            certname_ecdsa384=certname_ecdsa384,
            certname_ecdsa521=certname_ecdsa521,
            certname_ed25519=certname_ed25519,
            certname_ed448=certname_ed448,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.setting import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/vpn/certificate/setting",
            )
        
        # Singleton endpoint - no identifier needed
        endpoint = "/vpn.certificate/setting"

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
        Move vpn/certificate/setting object to a new position.
        
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
            >>> fgt.api.cmdb.vpn_certificate_setting.move(
            ...     name="object1",
            ...     action="before",
            ...     reference_name="object2"
            ... )
        """
        return self._client.request(
            method="PUT",
            path=f"/api/v2/cmdb/vpn.certificate/setting",
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
        Clone vpn/certificate/setting object.
        
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
            >>> fgt.api.cmdb.vpn_certificate_setting.clone(
            ...     name="template",
            ...     new_name="new-from-template"
            ... )
        """
        return self._client.request(
            method="POST",
            path=f"/api/v2/cmdb/vpn.certificate/setting",
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
        Check if vpn/certificate/setting object exists.
        
        Args:
            name: Name to check
            vdom: Virtual domain name
            
        Returns:
            True if object exists, False otherwise
            
        Example:
            >>> # Check before creating
            >>> if not fgt.api.cmdb.vpn_certificate_setting.exists(name="myobj"):
            ...     fgt.api.cmdb.vpn_certificate_setting.post(payload_dict=data)
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

