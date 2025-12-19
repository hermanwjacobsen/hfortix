"""
FortiOS CMDB - Authentication Scheme

API Endpoints:
    GET    /authentication/scheme
    POST   /authentication/scheme
    GET    /authentication/scheme/{name}
    PUT    /authentication/scheme/{name}
    DELETE /authentication/scheme/{name}
"""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from ....http_client import HTTPClient


class Scheme:
    """Scheme operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize Scheme endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

    def get(
        self,
        name: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        attr: str | None = None,
        skip_to_datasource: dict | None = None,
        acs: int | None = None,
        search: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Select a specific entry from a CLI table.
        
        Args:
            name: Object identifier (optional for list, required for specific)
            attr: Attribute name that references other table (optional)
            skip_to_datasource: Skip to provided table's Nth entry. E.g {datasource: 'firewall.address', pos: 10, global_entry: false} (optional)
            acs: If true, returned result are in ascending order. (optional)
            search: If present, the objects will be filtered by the search value. (optional)
            vdom: Virtual domain name, or False to skip. Handled by HTTPClient.
            raw_json: If True, return full API response with metadata. If False, return only results.
            **kwargs: Additional query parameters (filter, sort, start, count, format, etc.)
        
        Common Query Parameters (via **kwargs):
            filter: Filter results (e.g., filter='name==value')
            sort: Sort results (e.g., sort='name,asc')
            start: Starting entry index for paging
            count: Maximum number of entries to return
            format: Fields to return (e.g., format='name|type')
            See FortiOS REST API documentation for full list of query parameters
        
        Returns:
            Dictionary containing API response
        """
        params = payload_dict.copy() if payload_dict else {}
        
        # Build endpoint path
        if name:
            endpoint = f"/authentication/scheme/{name}"
        else:
            endpoint = "/authentication/scheme"
        if attr is not None:
            params['attr'] = attr
        if skip_to_datasource is not None:
            params['skip_to_datasource'] = skip_to_datasource
        if acs is not None:
            params['acs'] = acs
        if search is not None:
            params['search'] = search
        params.update(kwargs)
        return self._client.get("cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json)

    def put(
        self,
        name: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        before: str | None = None,
        after: str | None = None,
        method: str | None = None,
        negotiate_ntlm: str | None = None,
        kerberos_keytab: str | None = None,
        domain_controller: str | None = None,
        saml_server: str | None = None,
        saml_timeout: int | None = None,
        fsso_agent_for_ntlm: str | None = None,
        require_tfa: str | None = None,
        fsso_guest: str | None = None,
        user_cert: str | None = None,
        cert_http_header: str | None = None,
        user_database: list | None = None,
        ssh_ca: str | None = None,
        external_idp: str | None = None,
        group_attr_type: str | None = None,
        digest_algo: str | None = None,
        digest_rfc2069: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Update this specific resource.
        
        Args:
            payload_dict: Optional dictionary of all parameters (can be passed as first positional arg)
            name: Object identifier (required)
            before: If *action=move*, use *before* to specify the ID of the resource that this resource will be moved before. (optional)
            after: If *action=move*, use *after* to specify the ID of the resource that this resource will be moved after. (optional)
            name: Authentication scheme name. (optional)
            method: Authentication methods (default = basic). (optional)
            negotiate_ntlm: Enable/disable negotiate authentication for NTLM (default = disable). (optional)
            kerberos_keytab: Kerberos keytab setting. (optional)
            domain_controller: Domain controller setting. (optional)
            saml_server: SAML configuration. (optional)
            saml_timeout: SAML authentication timeout in seconds. (optional)
            fsso_agent_for_ntlm: FSSO agent to use for NTLM authentication. (optional)
            require_tfa: Enable/disable two-factor authentication (default = disable). (optional)
            fsso_guest: Enable/disable user fsso-guest authentication (default = disable). (optional)
            user_cert: Enable/disable authentication with user certificate (default = disable). (optional)
            cert_http_header: Enable/disable authentication with user certificate in Client-Cert HTTP header (default = disable). (optional)
            user_database: Authentication server to contain user information; "local-user-db" (default) or "123" (for LDAP). (optional)
            ssh_ca: SSH CA name. (optional)
            external_idp: External identity provider configuration. (optional)
            group_attr_type: Group attribute type used to match SCIM groups (default = display-name). (optional)
            digest_algo: Digest Authentication Algorithms. (optional)
            digest_rfc2069: Enable/disable support for the deprecated RFC2069 Digest Client (no cnonce field, default = disable). (optional)
            vdom: Virtual domain name, or False to skip. Handled by HTTPClient.
            raw_json: If True, return full API response with metadata. If False, return only results.
            **kwargs: Additional query parameters (filter, sort, start, count, format, etc.)
        
        Common Query Parameters (via **kwargs):
            filter: Filter results (e.g., filter='name==value')
            sort: Sort results (e.g., sort='name,asc')
            start: Starting entry index for paging
            count: Maximum number of entries to return
            format: Fields to return (e.g., format='name|type')
            See FortiOS REST API documentation for full list of query parameters
        
        Returns:
            Dictionary containing API response
        """
        data_payload = payload_dict.copy() if payload_dict else {}
        params = {}
        
        # Build endpoint path
        if not name:
            raise ValueError("name is required for put()")
        endpoint = f"/authentication/scheme/{name}"
        if before is not None:
            data_payload['before'] = before
        if after is not None:
            data_payload['after'] = after
        if name is not None:
            data_payload['name'] = name
        if method is not None:
            data_payload['method'] = method
        if negotiate_ntlm is not None:
            data_payload['negotiate-ntlm'] = negotiate_ntlm
        if kerberos_keytab is not None:
            data_payload['kerberos-keytab'] = kerberos_keytab
        if domain_controller is not None:
            data_payload['domain-controller'] = domain_controller
        if saml_server is not None:
            data_payload['saml-server'] = saml_server
        if saml_timeout is not None:
            data_payload['saml-timeout'] = saml_timeout
        if fsso_agent_for_ntlm is not None:
            data_payload['fsso-agent-for-ntlm'] = fsso_agent_for_ntlm
        if require_tfa is not None:
            data_payload['require-tfa'] = require_tfa
        if fsso_guest is not None:
            data_payload['fsso-guest'] = fsso_guest
        if user_cert is not None:
            data_payload['user-cert'] = user_cert
        if cert_http_header is not None:
            data_payload['cert-http-header'] = cert_http_header
        if user_database is not None:
            data_payload['user-database'] = user_database
        if ssh_ca is not None:
            data_payload['ssh-ca'] = ssh_ca
        if external_idp is not None:
            data_payload['external-idp'] = external_idp
        if group_attr_type is not None:
            data_payload['group-attr-type'] = group_attr_type
        if digest_algo is not None:
            data_payload['digest-algo'] = digest_algo
        if digest_rfc2069 is not None:
            data_payload['digest-rfc2069'] = digest_rfc2069
        data_payload.update(kwargs)
        return self._client.put("cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json)

    def delete(
        self,
        name: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Delete this specific resource.
        
        Args:
            name: Object identifier (required)
            vdom: Virtual domain name, or False to skip. Handled by HTTPClient.
            raw_json: If True, return full API response with metadata. If False, return only results.
            **kwargs: Additional query parameters (filter, sort, start, count, format, etc.)
        
        Common Query Parameters (via **kwargs):
            filter: Filter results (e.g., filter='name==value')
            sort: Sort results (e.g., sort='name,asc')
            start: Starting entry index for paging
            count: Maximum number of entries to return
            format: Fields to return (e.g., format='name|type')
            See FortiOS REST API documentation for full list of query parameters
        
        Returns:
            Dictionary containing API response
        """
        params = payload_dict.copy() if payload_dict else {}
        
        # Build endpoint path
        if not name:
            raise ValueError("name is required for delete()")
        endpoint = f"/authentication/scheme/{name}"
        params.update(kwargs)
        return self._client.delete("cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json)

    def post(
        self,
        payload_dict: dict[str, Any] | None = None,
        nkey: str | None = None,
        name: str | None = None,
        method: str | None = None,
        negotiate_ntlm: str | None = None,
        kerberos_keytab: str | None = None,
        domain_controller: str | None = None,
        saml_server: str | None = None,
        saml_timeout: int | None = None,
        fsso_agent_for_ntlm: str | None = None,
        require_tfa: str | None = None,
        fsso_guest: str | None = None,
        user_cert: str | None = None,
        cert_http_header: str | None = None,
        user_database: list | None = None,
        ssh_ca: str | None = None,
        external_idp: str | None = None,
        group_attr_type: str | None = None,
        digest_algo: str | None = None,
        digest_rfc2069: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Create object(s) in this table.
        
        Args:
            payload_dict: Optional dictionary of all parameters (can be passed as first positional arg)
            nkey: If *action=clone*, use *nkey* to specify the ID for the new resource to be created. (optional)
            name: Authentication scheme name. (optional)
            method: Authentication methods (default = basic). (optional)
            negotiate_ntlm: Enable/disable negotiate authentication for NTLM (default = disable). (optional)
            kerberos_keytab: Kerberos keytab setting. (optional)
            domain_controller: Domain controller setting. (optional)
            saml_server: SAML configuration. (optional)
            saml_timeout: SAML authentication timeout in seconds. (optional)
            fsso_agent_for_ntlm: FSSO agent to use for NTLM authentication. (optional)
            require_tfa: Enable/disable two-factor authentication (default = disable). (optional)
            fsso_guest: Enable/disable user fsso-guest authentication (default = disable). (optional)
            user_cert: Enable/disable authentication with user certificate (default = disable). (optional)
            cert_http_header: Enable/disable authentication with user certificate in Client-Cert HTTP header (default = disable). (optional)
            user_database: Authentication server to contain user information; "local-user-db" (default) or "123" (for LDAP). (optional)
            ssh_ca: SSH CA name. (optional)
            external_idp: External identity provider configuration. (optional)
            group_attr_type: Group attribute type used to match SCIM groups (default = display-name). (optional)
            digest_algo: Digest Authentication Algorithms. (optional)
            digest_rfc2069: Enable/disable support for the deprecated RFC2069 Digest Client (no cnonce field, default = disable). (optional)
            vdom: Virtual domain name, or False to skip. Handled by HTTPClient.
            raw_json: If True, return full API response with metadata. If False, return only results.
            **kwargs: Additional query parameters (filter, sort, start, count, format, etc.)
        
        Common Query Parameters (via **kwargs):
            filter: Filter results (e.g., filter='name==value')
            sort: Sort results (e.g., sort='name,asc')
            start: Starting entry index for paging
            count: Maximum number of entries to return
            format: Fields to return (e.g., format='name|type')
            See FortiOS REST API documentation for full list of query parameters
        
        Returns:
            Dictionary containing API response
        """
        data_payload = payload_dict.copy() if payload_dict else {}
        params = {}
        endpoint = "/authentication/scheme"
        if nkey is not None:
            data_payload['nkey'] = nkey
        if name is not None:
            data_payload['name'] = name
        if method is not None:
            data_payload['method'] = method
        if negotiate_ntlm is not None:
            data_payload['negotiate-ntlm'] = negotiate_ntlm
        if kerberos_keytab is not None:
            data_payload['kerberos-keytab'] = kerberos_keytab
        if domain_controller is not None:
            data_payload['domain-controller'] = domain_controller
        if saml_server is not None:
            data_payload['saml-server'] = saml_server
        if saml_timeout is not None:
            data_payload['saml-timeout'] = saml_timeout
        if fsso_agent_for_ntlm is not None:
            data_payload['fsso-agent-for-ntlm'] = fsso_agent_for_ntlm
        if require_tfa is not None:
            data_payload['require-tfa'] = require_tfa
        if fsso_guest is not None:
            data_payload['fsso-guest'] = fsso_guest
        if user_cert is not None:
            data_payload['user-cert'] = user_cert
        if cert_http_header is not None:
            data_payload['cert-http-header'] = cert_http_header
        if user_database is not None:
            data_payload['user-database'] = user_database
        if ssh_ca is not None:
            data_payload['ssh-ca'] = ssh_ca
        if external_idp is not None:
            data_payload['external-idp'] = external_idp
        if group_attr_type is not None:
            data_payload['group-attr-type'] = group_attr_type
        if digest_algo is not None:
            data_payload['digest-algo'] = digest_algo
        if digest_rfc2069 is not None:
            data_payload['digest-rfc2069'] = digest_rfc2069
        data_payload.update(kwargs)
        return self._client.post("cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json)
