"""
FortiOS CMDB - Certificate local

Configuration endpoint for managing cmdb certificate/local objects.

API Endpoints:
    GET    /cmdb/certificate/local
    POST   /cmdb/certificate/local
    PUT    /cmdb/certificate/local/{identifier}
    DELETE /cmdb/certificate/local/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.certificate_local.get()
    >>>
    >>> # Create with auto-normalization (strings/lists converted automatically)
    >>> result = fgt.api.cmdb.certificate_local.post(
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

class Local(CRUDEndpoint, MetadataMixin):
    """Local Operations."""
    
    # Configure metadata mixin to use this endpoint's helper module
    _helper_module_name = "local"
    
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
        """Initialize Local endpoint."""
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
        Retrieve certificate/local configuration.

        Local keys and certificates.

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
            >>> # Get all certificate/local objects
            >>> result = fgt.api.cmdb.certificate_local.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get specific certificate/local by name
            >>> result = fgt.api.cmdb.certificate_local.get(name=1)
            >>> print(result['results'])
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.certificate_local.get(
            ...     filter=["name==test", "status==enable"]
            ... )
            
            >>> # Get with pagination
            >>> result = fgt.api.cmdb.certificate_local.get(
            ...     start=0, count=100
            ... )
            
            >>> # Get schema information  
            >>> schema = fgt.api.cmdb.certificate_local.get_schema()

        See Also:
            - post(): Create new certificate/local object
            - put(): Update existing certificate/local object
            - delete(): Remove certificate/local object
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
            endpoint = "/certificate/local/" + str(name)
            unwrap_single = True
        else:
            endpoint = "/certificate/local"
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
            >>> schema = fgt.api.cmdb.certificate_local.get_schema()
            >>> print(schema['results'])
            
            >>> # Get JSON Schema format (if supported)
            >>> json_schema = fgt.api.cmdb.certificate_local.get_schema(format="json-schema")
        
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
        password: Any | None = None,
        comments: str | None = None,
        private_key: str | None = None,
        certificate: str | None = None,
        csr: str | None = None,
        state: str | None = None,
        scep_url: str | None = None,
        range: Literal["global", "vdom"] | None = None,
        source: Literal["factory", "user", "bundle"] | None = None,
        auto_regenerate_days: int | None = None,
        auto_regenerate_days_warning: int | None = None,
        scep_password: Any | None = None,
        ca_identifier: str | None = None,
        name_encoding: Literal["printable", "utf8"] | None = None,
        source_ip: str | None = None,
        ike_localid: str | None = None,
        ike_localid_type: Literal["asn1dn", "fqdn"] | None = None,
        enroll_protocol: Literal["none", "scep", "cmpv2", "acme2", "est"] | None = None,
        private_key_retain: Literal["enable", "disable"] | None = None,
        cmp_server: str | None = None,
        cmp_path: str | None = None,
        cmp_server_cert: str | None = None,
        cmp_regeneration_method: Literal["keyupate", "renewal"] | None = None,
        acme_ca_url: str | None = None,
        acme_domain: str | None = None,
        acme_email: str | None = None,
        acme_eab_key_id: str | None = None,
        acme_eab_key_hmac: Any | None = None,
        acme_rsa_key_size: int | None = None,
        acme_renew_window: int | None = None,
        est_server: str | None = None,
        est_ca_id: str | None = None,
        est_http_username: str | None = None,
        est_http_password: Any | None = None,
        est_client_cert: str | None = None,
        est_server_cert: str | None = None,
        est_srp_username: str | None = None,
        est_srp_password: Any | None = None,
        est_regeneration_method: Literal["create-new-key", "use-existing-key"] | None = None,
        details: Any | None = None,
        vdom: str | bool | None = None,
        error_mode: Literal["raise", "return", "print"] | None = None,
        error_format: Literal["detailed", "simple", "code_only"] | None = None,
    ):  # type: ignore[no-untyped-def]
        """
        Update existing certificate/local object.

        Local keys and certificates.

        Args:
            payload_dict: Object data as dict. Must include name (primary key).
            name: Name.
            password: Password as a PEM file.
            comments: Comment.
            private_key: PEM format key encrypted with a password.
            certificate: PEM format certificate.
            csr: Certificate Signing Request.
            state: Certificate Signing Request State.
            scep_url: SCEP server URL.
            range: Either a global or VDOM IP address range for the certificate.
            source: Certificate source type.
            auto_regenerate_days: Number of days to wait before expiry of an updated local certificate is requested (0 = disabled).
            auto_regenerate_days_warning: Number of days to wait before an expiry warning message is generated (0 = disabled).
            scep_password: SCEP server challenge password for auto-regeneration.
            ca_identifier: CA identifier of the CA server for signing via SCEP.
            name_encoding: Name encoding method for auto-regeneration.
            source_ip: Source IP address for communications to the SCEP server.
            ike_localid: Local ID the FortiGate uses for authentication as a VPN client.
            ike_localid_type: IKE local ID type.
            enroll_protocol: Certificate enrollment protocol.
            private_key_retain: Enable/disable retention of private key during SCEP renewal (default = disable).
            cmp_server: Address and port for CMP server (format = address:port).
            cmp_path: Path location inside CMP server.
            cmp_server_cert: CMP server certificate.
            cmp_regeneration_method: CMP auto-regeneration method.
            acme_ca_url: The URL for the ACME CA server (Let's Encrypt is the default provider).
            acme_domain: A valid domain that resolves to this FortiGate unit.
            acme_email: Contact email address that is required by some CAs like LetsEncrypt.
            acme_eab_key_id: External Account Binding Key ID (optional setting).
            acme_eab_key_hmac: External Account Binding HMAC Key (URL-encoded base64).
            acme_rsa_key_size: Length of the RSA private key of the generated cert (Minimum 2048 bits).
            acme_renew_window: Beginning of the renewal window (in days before certificate expiration, 30 by default).
            est_server: Address and port for EST server (e.g. https://example.com:1234).
            est_ca_id: CA identifier of the CA server for signing via EST.
            est_http_username: HTTP Authentication username for signing via EST.
            est_http_password: HTTP Authentication password for signing via EST.
            est_client_cert: Certificate used to authenticate this FortiGate to EST server.
            est_server_cert: EST server's certificate must be verifiable by this certificate to be authenticated.
            est_srp_username: EST SRP authentication username.
            est_srp_password: EST SRP authentication password.
            est_regeneration_method: EST behavioral options during re-enrollment.
            details: Print local certificate detailed information.
            vdom: Virtual domain name.
            error_mode: Override client-level error_mode. "raise" raises exceptions, "return" returns error dict, "print" prints errors.
            error_format: Override client-level error_format. "detailed" provides full context, "simple" is concise, "code_only" returns just status code.

        Returns:
            FortiObject instance. Use .dict, .json, or .raw to access as dictionary.

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.certificate_local.put(
            ...     name=1,
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "name": 1,
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.certificate_local.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Build payload using helper function with auto-normalization
        # This automatically converts strings/lists to [{'name': '...'}] format for list fields
        # To disable auto-normalization, use build_cmdb_payload directly
        payload_data = build_api_payload(
            name=name,
            password=password,
            comments=comments,
            private_key=private_key,
            certificate=certificate,
            csr=csr,
            state=state,
            scep_url=scep_url,
            range=range,
            source=source,
            auto_regenerate_days=auto_regenerate_days,
            auto_regenerate_days_warning=auto_regenerate_days_warning,
            scep_password=scep_password,
            ca_identifier=ca_identifier,
            name_encoding=name_encoding,
            source_ip=source_ip,
            ike_localid=ike_localid,
            ike_localid_type=ike_localid_type,
            enroll_protocol=enroll_protocol,
            private_key_retain=private_key_retain,
            cmp_server=cmp_server,
            cmp_path=cmp_path,
            cmp_server_cert=cmp_server_cert,
            cmp_regeneration_method=cmp_regeneration_method,
            acme_ca_url=acme_ca_url,
            acme_domain=acme_domain,
            acme_email=acme_email,
            acme_eab_key_id=acme_eab_key_id,
            acme_eab_key_hmac=acme_eab_key_hmac,
            acme_rsa_key_size=acme_rsa_key_size,
            acme_renew_window=acme_renew_window,
            est_server=est_server,
            est_ca_id=est_ca_id,
            est_http_username=est_http_username,
            est_http_password=est_http_password,
            est_client_cert=est_client_cert,
            est_server_cert=est_server_cert,
            est_srp_username=est_srp_username,
            est_srp_password=est_srp_password,
            est_regeneration_method=est_regeneration_method,
            details=details,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.local import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/certificate/local",
            )
        
        name_value = payload_data.get("name")
        if not name_value:
            raise ValueError("name is required for PUT")
        endpoint = "/certificate/local/" + str(name_value)

        return self._client.put(
            "cmdb", endpoint, data=payload_data, vdom=vdom
        )

    # ========================================================================
    # POST Method
    # Type hints provided by CRUDEndpoint protocol (no local @overload needed)
    # ========================================================================
    
    def post(
        self,
        payload_dict: dict[str, Any] | None = None,
        name: str | None = None,
        password: Any | None = None,
        comments: str | None = None,
        private_key: str | None = None,
        certificate: str | None = None,
        csr: str | None = None,
        state: str | None = None,
        scep_url: str | None = None,
        range: Literal["global", "vdom"] | None = None,
        source: Literal["factory", "user", "bundle"] | None = None,
        auto_regenerate_days: int | None = None,
        auto_regenerate_days_warning: int | None = None,
        scep_password: Any | None = None,
        ca_identifier: str | None = None,
        name_encoding: Literal["printable", "utf8"] | None = None,
        source_ip: str | None = None,
        ike_localid: str | None = None,
        ike_localid_type: Literal["asn1dn", "fqdn"] | None = None,
        enroll_protocol: Literal["none", "scep", "cmpv2", "acme2", "est"] | None = None,
        private_key_retain: Literal["enable", "disable"] | None = None,
        cmp_server: str | None = None,
        cmp_path: str | None = None,
        cmp_server_cert: str | None = None,
        cmp_regeneration_method: Literal["keyupate", "renewal"] | None = None,
        acme_ca_url: str | None = None,
        acme_domain: str | None = None,
        acme_email: str | None = None,
        acme_eab_key_id: str | None = None,
        acme_eab_key_hmac: Any | None = None,
        acme_rsa_key_size: int | None = None,
        acme_renew_window: int | None = None,
        est_server: str | None = None,
        est_ca_id: str | None = None,
        est_http_username: str | None = None,
        est_http_password: Any | None = None,
        est_client_cert: str | None = None,
        est_server_cert: str | None = None,
        est_srp_username: str | None = None,
        est_srp_password: Any | None = None,
        est_regeneration_method: Literal["create-new-key", "use-existing-key"] | None = None,
        details: Any | None = None,
        vdom: str | bool | None = None,
        error_mode: Literal["raise", "return", "print"] | None = None,
        error_format: Literal["detailed", "simple", "code_only"] | None = None,
    ):  # type: ignore[no-untyped-def]
        """
        Create new certificate/local object.

        Local keys and certificates.

        Args:
            payload_dict: Complete object data as dict. Alternative to individual parameters.
            name: Name.
            password: Password as a PEM file.
            comments: Comment.
            private_key: PEM format key encrypted with a password.
            certificate: PEM format certificate.
            csr: Certificate Signing Request.
            state: Certificate Signing Request State.
            scep_url: SCEP server URL.
            range: Either a global or VDOM IP address range for the certificate.
            source: Certificate source type.
            auto_regenerate_days: Number of days to wait before expiry of an updated local certificate is requested (0 = disabled).
            auto_regenerate_days_warning: Number of days to wait before an expiry warning message is generated (0 = disabled).
            scep_password: SCEP server challenge password for auto-regeneration.
            ca_identifier: CA identifier of the CA server for signing via SCEP.
            name_encoding: Name encoding method for auto-regeneration.
            source_ip: Source IP address for communications to the SCEP server.
            ike_localid: Local ID the FortiGate uses for authentication as a VPN client.
            ike_localid_type: IKE local ID type.
            enroll_protocol: Certificate enrollment protocol.
            private_key_retain: Enable/disable retention of private key during SCEP renewal (default = disable).
            cmp_server: Address and port for CMP server (format = address:port).
            cmp_path: Path location inside CMP server.
            cmp_server_cert: CMP server certificate.
            cmp_regeneration_method: CMP auto-regeneration method.
            acme_ca_url: The URL for the ACME CA server (Let's Encrypt is the default provider).
            acme_domain: A valid domain that resolves to this FortiGate unit.
            acme_email: Contact email address that is required by some CAs like LetsEncrypt.
            acme_eab_key_id: External Account Binding Key ID (optional setting).
            acme_eab_key_hmac: External Account Binding HMAC Key (URL-encoded base64).
            acme_rsa_key_size: Length of the RSA private key of the generated cert (Minimum 2048 bits).
            acme_renew_window: Beginning of the renewal window (in days before certificate expiration, 30 by default).
            est_server: Address and port for EST server (e.g. https://example.com:1234).
            est_ca_id: CA identifier of the CA server for signing via EST.
            est_http_username: HTTP Authentication username for signing via EST.
            est_http_password: HTTP Authentication password for signing via EST.
            est_client_cert: Certificate used to authenticate this FortiGate to EST server.
            est_server_cert: EST server's certificate must be verifiable by this certificate to be authenticated.
            est_srp_username: EST SRP authentication username.
            est_srp_password: EST SRP authentication password.
            est_regeneration_method: EST behavioral options during re-enrollment.
            details: Print local certificate detailed information.
            vdom: Virtual domain name. Use True for global, string for specific VDOM.
            error_mode: Override client-level error_mode. "raise" raises exceptions, "return" returns error dict, "print" prints errors.
            error_format: Override client-level error_format. "detailed" provides full context, "simple" is concise, "code_only" returns just status code.

        Returns:
            FortiObject instance with created object. Use .dict, .json, or .raw to access as dictionary.

        Examples:
            >>> # Create using individual parameters
            >>> result = fgt.api.cmdb.certificate_local.post(
            ...     name="example",
            ...     # ... other required fields
            ... )
            >>> print(f"Created name: {result['results']}")
            
            >>> # Create using payload dict
            >>> payload = Local.defaults()  # Start with defaults
            >>> payload['name'] = 'my-object'
            >>> result = fgt.api.cmdb.certificate_local.post(payload_dict=payload)

        Note:
            Required fields: {{ ", ".join(Local.required_fields()) }}
            
            Use Local.help('field_name') to get field details.

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
            password=password,
            comments=comments,
            private_key=private_key,
            certificate=certificate,
            csr=csr,
            state=state,
            scep_url=scep_url,
            range=range,
            source=source,
            auto_regenerate_days=auto_regenerate_days,
            auto_regenerate_days_warning=auto_regenerate_days_warning,
            scep_password=scep_password,
            ca_identifier=ca_identifier,
            name_encoding=name_encoding,
            source_ip=source_ip,
            ike_localid=ike_localid,
            ike_localid_type=ike_localid_type,
            enroll_protocol=enroll_protocol,
            private_key_retain=private_key_retain,
            cmp_server=cmp_server,
            cmp_path=cmp_path,
            cmp_server_cert=cmp_server_cert,
            cmp_regeneration_method=cmp_regeneration_method,
            acme_ca_url=acme_ca_url,
            acme_domain=acme_domain,
            acme_email=acme_email,
            acme_eab_key_id=acme_eab_key_id,
            acme_eab_key_hmac=acme_eab_key_hmac,
            acme_rsa_key_size=acme_rsa_key_size,
            acme_renew_window=acme_renew_window,
            est_server=est_server,
            est_ca_id=est_ca_id,
            est_http_username=est_http_username,
            est_http_password=est_http_password,
            est_client_cert=est_client_cert,
            est_server_cert=est_server_cert,
            est_srp_username=est_srp_username,
            est_srp_password=est_srp_password,
            est_regeneration_method=est_regeneration_method,
            details=details,
            data=payload_dict,
        )

        # Check for deprecated fields and warn users
        from ._helpers.local import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/certificate/local",
            )

        endpoint = "/certificate/local"
        return self._client.post(
            "cmdb", endpoint, data=payload_data, vdom=vdom
        )

    # ========================================================================
    # DELETE Method
    # Type hints provided by CRUDEndpoint protocol (no local @overload needed)
    # ========================================================================
    
    def delete(
        self,
        name: str | None = None,
        vdom: str | bool | None = None,
        error_mode: Literal["raise", "return", "print"] | None = None,
        error_format: Literal["detailed", "simple", "code_only"] | None = None,
    ):  # type: ignore[no-untyped-def]
        """
        Delete certificate/local object.

        Local keys and certificates.

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
            >>> result = fgt.api.cmdb.certificate_local.delete(name=1)
            
            >>> # Check for errors
            >>> if result.get('status') != 'success':
            ...     print(f"Delete failed: {result.get('error')}")

        See Also:
            - exists(): Check if object exists before deleting
            - get(): Retrieve object to verify it exists
        """
        if not name:
            raise ValueError("name is required for DELETE")
        endpoint = "/certificate/local/" + str(name)

        return self._client.delete(
            "cmdb", endpoint, vdom=vdom
        )

    def exists(
        self,
        name: str,
        vdom: str | bool | None = None,
    ) -> Union[bool, Coroutine[Any, Any, bool]]:
        """
        Check if certificate/local object exists.

        Verifies whether an object exists by attempting to retrieve it and checking the response status.

        Args:
            name: Primary key identifier
            vdom: Virtual domain name

        Returns:
            True if object exists, False otherwise

        Examples:
            >>> # Check if object exists before operations
            >>> if fgt.api.cmdb.certificate_local.exists(name=1):
            ...     print("Object exists")
            ... else:
            ...     print("Object not found")
            
            >>> # Conditional delete
            >>> if fgt.api.cmdb.certificate_local.exists(name=1):
            ...     fgt.api.cmdb.certificate_local.delete(name=1)

        See Also:
            - get(): Retrieve full object data
            - set(): Create or update automatically based on existence
        """
        # Use direct request with silent error handling to avoid logging 404s
        # This is expected behavior for exists() - 404 just means "doesn't exist"
        endpoint = "/certificate/local"
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
        password: Any | None = None,
        comments: str | None = None,
        private_key: str | None = None,
        certificate: str | None = None,
        csr: str | None = None,
        state: str | None = None,
        scep_url: str | None = None,
        range: Literal["global", "vdom"] | None = None,
        source: Literal["factory", "user", "bundle"] | None = None,
        auto_regenerate_days: int | None = None,
        auto_regenerate_days_warning: int | None = None,
        scep_password: Any | None = None,
        ca_identifier: str | None = None,
        name_encoding: Literal["printable", "utf8"] | None = None,
        source_ip: str | None = None,
        ike_localid: str | None = None,
        ike_localid_type: Literal["asn1dn", "fqdn"] | None = None,
        enroll_protocol: Literal["none", "scep", "cmpv2", "acme2", "est"] | None = None,
        private_key_retain: Literal["enable", "disable"] | None = None,
        cmp_server: str | None = None,
        cmp_path: str | None = None,
        cmp_server_cert: str | None = None,
        cmp_regeneration_method: Literal["keyupate", "renewal"] | None = None,
        acme_ca_url: str | None = None,
        acme_domain: str | None = None,
        acme_email: str | None = None,
        acme_eab_key_id: str | None = None,
        acme_eab_key_hmac: Any | None = None,
        acme_rsa_key_size: int | None = None,
        acme_renew_window: int | None = None,
        est_server: str | None = None,
        est_ca_id: str | None = None,
        est_http_username: str | None = None,
        est_http_password: Any | None = None,
        est_client_cert: str | None = None,
        est_server_cert: str | None = None,
        est_srp_username: str | None = None,
        est_srp_password: Any | None = None,
        est_regeneration_method: Literal["create-new-key", "use-existing-key"] | None = None,
        details: Any | None = None,
        vdom: str | bool | None = None,
        error_mode: Literal["raise", "return", "print"] | None = None,
        error_format: Literal["detailed", "simple", "code_only"] | None = None,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Create or update certificate/local object (intelligent operation).

        Automatically determines whether to create (POST) or update (PUT) based on
        whether the resource exists. Requires the primary key (name) in the payload.

        Args:
            payload_dict: Resource data including name (primary key)
            name: Field name
            password: Field password
            comments: Field comments
            private_key: Field private-key
            certificate: Field certificate
            csr: Field csr
            state: Field state
            scep_url: Field scep-url
            range: Field range
            source: Field source
            auto_regenerate_days: Field auto-regenerate-days
            auto_regenerate_days_warning: Field auto-regenerate-days-warning
            scep_password: Field scep-password
            ca_identifier: Field ca-identifier
            name_encoding: Field name-encoding
            source_ip: Field source-ip
            ike_localid: Field ike-localid
            ike_localid_type: Field ike-localid-type
            enroll_protocol: Field enroll-protocol
            private_key_retain: Field private-key-retain
            cmp_server: Field cmp-server
            cmp_path: Field cmp-path
            cmp_server_cert: Field cmp-server-cert
            cmp_regeneration_method: Field cmp-regeneration-method
            acme_ca_url: Field acme-ca-url
            acme_domain: Field acme-domain
            acme_email: Field acme-email
            acme_eab_key_id: Field acme-eab-key-id
            acme_eab_key_hmac: Field acme-eab-key-hmac
            acme_rsa_key_size: Field acme-rsa-key-size
            acme_renew_window: Field acme-renew-window
            est_server: Field est-server
            est_ca_id: Field est-ca-id
            est_http_username: Field est-http-username
            est_http_password: Field est-http-password
            est_client_cert: Field est-client-cert
            est_server_cert: Field est-server-cert
            est_srp_username: Field est-srp-username
            est_srp_password: Field est-srp-password
            est_regeneration_method: Field est-regeneration-method
            details: Field details
            vdom: Virtual domain name
            **kwargs: Additional parameters passed to PUT or POST

        Returns:
            FortiObject instance. Use .dict, .json, or .raw to access as dictionary

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Intelligent create or update using field parameters
            >>> result = fgt.api.cmdb.certificate_local.set(
            ...     name=1,
            ...     # ... other fields
            ... )
            
            >>> # Or using payload dict
            >>> payload = {
            ...     "name": 1,
            ...     "field1": "value1",
            ...     "field2": "value2",
            ... }
            >>> result = fgt.api.cmdb.certificate_local.set(payload_dict=payload)
            >>> # Will POST if object doesn't exist, PUT if it does
            
            >>> # Idempotent configuration
            >>> for obj_data in configuration_list:
            ...     fgt.api.cmdb.certificate_local.set(payload_dict=obj_data)
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
            password=password,
            comments=comments,
            private_key=private_key,
            certificate=certificate,
            csr=csr,
            state=state,
            scep_url=scep_url,
            range=range,
            source=source,
            auto_regenerate_days=auto_regenerate_days,
            auto_regenerate_days_warning=auto_regenerate_days_warning,
            scep_password=scep_password,
            ca_identifier=ca_identifier,
            name_encoding=name_encoding,
            source_ip=source_ip,
            ike_localid=ike_localid,
            ike_localid_type=ike_localid_type,
            enroll_protocol=enroll_protocol,
            private_key_retain=private_key_retain,
            cmp_server=cmp_server,
            cmp_path=cmp_path,
            cmp_server_cert=cmp_server_cert,
            cmp_regeneration_method=cmp_regeneration_method,
            acme_ca_url=acme_ca_url,
            acme_domain=acme_domain,
            acme_email=acme_email,
            acme_eab_key_id=acme_eab_key_id,
            acme_eab_key_hmac=acme_eab_key_hmac,
            acme_rsa_key_size=acme_rsa_key_size,
            acme_renew_window=acme_renew_window,
            est_server=est_server,
            est_ca_id=est_ca_id,
            est_http_username=est_http_username,
            est_http_password=est_http_password,
            est_client_cert=est_client_cert,
            est_server_cert=est_server_cert,
            est_srp_username=est_srp_username,
            est_srp_password=est_srp_password,
            est_regeneration_method=est_regeneration_method,
            details=details,
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
        Move certificate/local object to a new position.
        
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
            >>> fgt.api.cmdb.certificate_local.move(
            ...     name=100,
            ...     action="before",
            ...     reference_name=50
            ... )
        """
        return self._client.request(
            method="PUT",
            path=f"/api/v2/cmdb/certificate/local",
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
        Clone certificate/local object.
        
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
            >>> fgt.api.cmdb.certificate_local.clone(
            ...     name=1,
            ...     new_name=100
            ... )
        """
        return self._client.request(
            method="POST",
            path=f"/api/v2/cmdb/certificate/local",
            params={
                "name": name,
                "new_name": new_name,
                "action": "clone",
                "vdom": vdom,
                **kwargs,
            },
        )


