"""
FortiOS CMDB - Authentication Schemes

Configure authentication schemes for controlling authentication methods.

API Endpoints:
    GET    /api/v2/cmdb/authentication/scheme       - Get all authentication schemes
    GET    /api/v2/cmdb/authentication/scheme/{name} - Get specific authentication scheme
    POST   /api/v2/cmdb/authentication/scheme       - Create authentication scheme
    PUT    /api/v2/cmdb/authentication/scheme/{name} - Update authentication scheme
    DELETE /api/v2/cmdb/authentication/scheme/{name} - Delete authentication scheme
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Dict, Any, Optional, Union

if TYPE_CHECKING:
    from ....http_client import HTTPClient


class Scheme:
    """Authentication scheme endpoint"""

    def __init__(self, client: 'HTTPClient') -> None:
        self._client = client

    @staticmethod
    def _format_name_list(items: Optional[list[Union[str, dict[str, Any]]]]) -> Optional[list[dict[str, Any]]]:
        """
        Convert simple list of strings to FortiOS format [{'name': 'item'}]

        Args:
            items: List of strings or dicts or None

        Returns:
            List of dicts with 'name' key, or None if input is None
        """
        if items is None:
            return None

        formatted = []
        for item in items:
            if isinstance(item, str):
                formatted.append({'name': item})
            elif isinstance(item, dict):
                formatted.append(item)
            else:
                formatted.append({'name': str(item)})

        return formatted

    def get(
        self,
        name: Optional[str] = None,
        attr: Optional[str] = None,
        datasource: Optional[bool] = False,
        with_meta: Optional[bool] = False,
        skip: Optional[bool] = False,
        count: Optional[int] = None,
        skip_to_datasource: Optional[str] = None,
        acs: Optional[bool] = None,
        search: Optional[str] = None,
        scope: Optional[str] = None,
        format: Optional[str] = None,
        action: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        **kwargs: Any
    ) -> dict[str, Any]:
        """
        Get authentication scheme(s)

        Retrieve authentication schemes with filtering and query options.

        Args:
            name (str, optional): Scheme name. If provided, get specific scheme.
            attr (str, optional): Attribute name that references other table
            datasource (bool, optional): Include datasource information
            with_meta (bool, optional): Include meta information
            skip (bool, optional): Enable skip operator
            count (int, optional): Maximum number of entries to return
            skip_to_datasource (str, optional): Skip to datasource entry
            acs (bool, optional): If true, return in ascending order
            search (str, optional): Filter by search value
            scope (str, optional): Scope level - 'global', 'vdom', or 'both'
            format (str, optional): Return specific fields (e.g., 'name|method')
            action (str, optional): Action type - 'default', 'schema', or 'revision'
            vdom (str, optional): Virtual Domain name
            **kwargs: Additional query parameters

        Returns:
            dict: API response with scheme data

        Examples:
            >>> # Get all authentication schemes
            >>> schemes = fgt.cmdb.authentication.scheme.list()

            >>> # Get specific scheme by name
            >>> scheme = fgt.cmdb.authentication.scheme.get('basic-auth')

            >>> # Get with filtering
            >>> filtered = fgt.cmdb.authentication.scheme.get(
            ...     format='name|method',
            ...     count=10
            ... )
        """
        params = {}
        param_map = {
            'attr': attr,
            'datasource': datasource,
            'with_meta': with_meta,
            'skip': skip,
            'count': count,
            'skip_to_datasource': skip_to_datasource,
            'acs': acs,
            'search': search,
            'scope': scope,
            'format': format,
            'action': action
        }

        for key, value in param_map.items():
            if value is not None:
                params[key] = value

        params.update(kwargs)

        # Build path
        path = 'authentication/scheme'
        if name is not None:
            path = f'{path}/{name}'

        return self._client.get('cmdb', path, params=params if params else None, vdom=vdom)

    def list(self, **kwargs: Any) -> dict[str, Any]:
        """
        Get all authentication schemes (convenience method)

        Args:
            **kwargs: All parameters from get() method

        Returns:
            dict: API response with all schemes

        Examples:
            >>> # Get all authentication schemes
            >>> all_schemes = fgt.cmdb.authentication.scheme.list()
        """
        return self.get(**kwargs)

    def create(
        self,
        data_dict: Optional[Dict[str, Any]] = None,
        name: Optional[str] = None,
        method: Optional[str] = None,
        negotiate_ntlm: Optional[str] = None,
        kerberos_keytab: Optional[str] = None,
        domain_controller: Optional[str] = None,
        saml_server: Optional[str] = None,
        saml_timeout: Optional[int] = None,
        fsso_agent_for_ntlm: Optional[str] = None,
        require_tfa: Optional[str] = None,
        fsso_guest: Optional[str] = None,
        user_cert: Optional[str] = None,
        cert_http_header: Optional[str] = None,
        user_database: Optional[list[Union[str, dict[str, Any]]]] = None,
        ssh_ca: Optional[str] = None,
        external_idp: Optional[str] = None,
        group_attr_type: Optional[str] = None,
        digest_algo: Optional[str] = None,
        digest_rfc2069: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        **kwargs: Any
    ) -> dict[str, Any]:
        """
        Create authentication scheme

        Create a new authentication scheme to define authentication methods.

        Args:
            name (str, required): Authentication scheme name (max 35 chars)
            method (str, optional): Authentication method - 'ntlm', 'basic', 'digest',
                'form', 'negotiate', 'fsso', 'rsso', 'ssh-publickey', 'cert', 'saml',
                'entra-sso' (default: 'basic')
            negotiate_ntlm (str, optional): Enable/disable negotiate auth for NTLM -
                'enable' or 'disable'
            kerberos_keytab (str, optional): Kerberos keytab setting (max 35 chars)
            domain_controller (str, optional): Domain controller setting (max 35 chars)
            saml_server (str, optional): SAML configuration (max 35 chars)
            saml_timeout (int, optional): SAML authentication timeout in seconds (30-1200)
            fsso_agent_for_ntlm (str, optional): FSSO agent to use for NTLM auth (max 35 chars)
            require_tfa (str, optional): Enable/disable two-factor auth - 'enable' or 'disable'
            fsso_guest (str, optional): Enable/disable fsso-guest auth - 'enable' or 'disable'
            user_cert (str, optional): Enable/disable user certificate auth - 'enable' or 'disable'
            cert_http_header (str, optional): Enable/disable cert auth with HTTP header -
                'enable' or 'disable'
            user_database (list, optional): List of authentication server names (strings or
                dicts with 'name' key)
            ssh_ca (str, optional): SSH CA name (max 35 chars)
            external_idp (str, optional): External identity provider configuration (max 35 chars)
            group_attr_type (str, optional): Group attribute type - 'display-name' or 'external-id'
            digest_algo (str, optional): Digest auth algorithm - 'md5' or 'sha-256'
            digest_rfc2069 (str, optional): Enable/disable RFC2069 Digest Client -
                'enable' or 'disable'
            vdom (str, optional): Virtual Domain name
            **kwargs: Additional parameters

        Returns:
            dict: API response

        Examples:
            >>> # Create basic HTTP authentication scheme
            >>> result = fgt.cmdb.authentication.scheme.create(
            ...     name='basic-http-auth',
            ...     method='basic',
            ...     user_database=['local-user-db']
            ... )

            >>> # Create LDAP authentication scheme
            >>> result = fgt.cmdb.authentication.scheme.create(
            ...     name='ldap-auth',
            ...     method='form',
            ...     user_database=['LDAP-Server'],
            ...     require_tfa='enable'
            ... )

            >>> # Create SAML authentication scheme
            >>> result = fgt.cmdb.authentication.scheme.create(
            ...     name='saml-sso',
            ...     method='saml',
            ...     saml_server='Azure-SAML',
            ...     saml_timeout=300
            ... )
        """
        # Convert simple lists to FortiOS format
        user_database = self._format_name_list(user_database)

        param_map = {
            'name': name,
            'method': method,
            'negotiate_ntlm': negotiate_ntlm,
            'kerberos_keytab': kerberos_keytab,
            'domain_controller': domain_controller,
            'saml_server': saml_server,
            'saml_timeout': saml_timeout,
            'fsso_agent_for_ntlm': fsso_agent_for_ntlm,
            'require_tfa': require_tfa,
            'fsso_guest': fsso_guest,
            'user_cert': user_cert,
            'cert_http_header': cert_http_header,
            'user_database': user_database,
            'ssh_ca': ssh_ca,
            'external_idp': external_idp,
            'group_attr_type': group_attr_type,
            'digest_algo': digest_algo,
            'digest_rfc2069': digest_rfc2069
        }

        api_field_map = {
            'name': 'name',
            'method': 'method',
            'negotiate_ntlm': 'negotiate-ntlm',
            'kerberos_keytab': 'kerberos-keytab',
            'domain_controller': 'domain-controller',
            'saml_server': 'saml-server',
            'saml_timeout': 'saml-timeout',
            'fsso_agent_for_ntlm': 'fsso-agent-for-ntlm',
            'require_tfa': 'require-tfa',
            'fsso_guest': 'fsso-guest',
            'user_cert': 'user-cert',
            'cert_http_header': 'cert-http-header',
            'user_database': 'user-database',
            'ssh_ca': 'ssh-ca',
            'external_idp': 'external-idp',
            'group_attr_type': 'group-attr-type',
            'digest_algo': 'digest-algo',
            'digest_rfc2069': 'digest-rfc2069'
        }

        data = {}
        for param_name, value in param_map.items():
            if value is not None:
                api_name = api_field_map[param_name]
                data[api_name] = value

        data.update(kwargs)

        return self._client.post('cmdb', 'authentication/scheme', data, vdom=vdom)

    def update(
        self,
        data_dict: Optional[Dict[str, Any]] = None,
        name: Optional[str] = None,
        method: Optional[str] = None,
        negotiate_ntlm: Optional[str] = None,
        kerberos_keytab: Optional[str] = None,
        domain_controller: Optional[str] = None,
        saml_server: Optional[str] = None,
        saml_timeout: Optional[int] = None,
        fsso_agent_for_ntlm: Optional[str] = None,
        require_tfa: Optional[str] = None,
        fsso_guest: Optional[str] = None,
        user_cert: Optional[str] = None,
        cert_http_header: Optional[str] = None,
        user_database: Optional[list[Union[str, dict[str, Any]]]] = None,
        ssh_ca: Optional[str] = None,
        external_idp: Optional[str] = None,
        group_attr_type: Optional[str] = None,
        digest_algo: Optional[str] = None,
        digest_rfc2069: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        **kwargs: Any
    ) -> dict[str, Any]:
        """
        Update authentication scheme

        Update an existing authentication scheme configuration.

        Args:
            name (str, required): Authentication scheme name
            method (str, optional): Authentication method - 'ntlm', 'basic', 'digest',
                'form', 'negotiate', 'fsso', 'rsso', 'ssh-publickey', 'cert', 'saml',
                'entra-sso'
            negotiate_ntlm (str, optional): Enable/disable negotiate auth for NTLM -
                'enable' or 'disable'
            kerberos_keytab (str, optional): Kerberos keytab setting
            domain_controller (str, optional): Domain controller setting
            saml_server (str, optional): SAML configuration
            saml_timeout (int, optional): SAML authentication timeout in seconds (30-1200)
            fsso_agent_for_ntlm (str, optional): FSSO agent to use for NTLM auth
            require_tfa (str, optional): Enable/disable two-factor auth - 'enable' or 'disable'
            fsso_guest (str, optional): Enable/disable fsso-guest auth - 'enable' or 'disable'
            user_cert (str, optional): Enable/disable user certificate auth - 'enable' or 'disable'
            cert_http_header (str, optional): Enable/disable cert auth with HTTP header -
                'enable' or 'disable'
            user_database (list, optional): List of authentication server names
            ssh_ca (str, optional): SSH CA name
            external_idp (str, optional): External identity provider configuration
            group_attr_type (str, optional): Group attribute type - 'display-name' or 'external-id'
            digest_algo (str, optional): Digest auth algorithm - 'md5' or 'sha-256'
            digest_rfc2069 (str, optional): Enable/disable RFC2069 Digest Client -
                'enable' or 'disable'
            vdom (str, optional): Virtual Domain name
            **kwargs: Additional parameters

        Returns:
            dict: API response

        Examples:
            >>> # Update scheme to require two-factor authentication
            >>> result = fgt.cmdb.authentication.scheme.update(
            ...     name='basic-http-auth',
            ...     require_tfa='enable'
            ... )

            >>> # Update authentication method
            >>> result = fgt.cmdb.authentication.scheme.update(
            ...     name='web-auth',
            ...     method='form',
            ...     user_database=['LDAP-Server', 'RADIUS-Server']
            ... )
        """
        # Convert simple lists to FortiOS format
        user_database = self._format_name_list(user_database)

        param_map = {
            'method': method,
            'negotiate_ntlm': negotiate_ntlm,
            'kerberos_keytab': kerberos_keytab,
            'domain_controller': domain_controller,
            'saml_server': saml_server,
            'saml_timeout': saml_timeout,
            'fsso_agent_for_ntlm': fsso_agent_for_ntlm,
            'require_tfa': require_tfa,
            'fsso_guest': fsso_guest,
            'user_cert': user_cert,
            'cert_http_header': cert_http_header,
            'user_database': user_database,
            'ssh_ca': ssh_ca,
            'external_idp': external_idp,
            'group_attr_type': group_attr_type,
            'digest_algo': digest_algo,
            'digest_rfc2069': digest_rfc2069
        }

        api_field_map = {
            'method': 'method',
            'negotiate_ntlm': 'negotiate-ntlm',
            'kerberos_keytab': 'kerberos-keytab',
            'domain_controller': 'domain-controller',
            'saml_server': 'saml-server',
            'saml_timeout': 'saml-timeout',
            'fsso_agent_for_ntlm': 'fsso-agent-for-ntlm',
            'require_tfa': 'require-tfa',
            'fsso_guest': 'fsso-guest',
            'user_cert': 'user-cert',
            'cert_http_header': 'cert-http-header',
            'user_database': 'user-database',
            'ssh_ca': 'ssh-ca',
            'external_idp': 'external-idp',
            'group_attr_type': 'group-attr-type',
            'digest_algo': 'digest-algo',
            'digest_rfc2069': 'digest-rfc2069'
        }

        data = {}
        for param_name, value in param_map.items():
            if value is not None:
                api_name = api_field_map[param_name]
                data[api_name] = value

        data.update(kwargs)

        return self._client.put('cmdb', f'authentication/scheme/{name}', data, vdom=vdom)

    def delete(
        self,
        name: str,
        vdom: Optional[Union[str, bool]] = None
    ) -> dict[str, Any]:
        """
        Delete authentication scheme

        Args:
            name (str, required): Authentication scheme name
            vdom (str, optional): Virtual Domain name

        Returns:
            dict: API response

        Examples:
            >>> # Delete authentication scheme
            >>> result = fgt.cmdb.authentication.scheme.delete('basic-http-auth')
        """
        return self._client.delete('cmdb', f'authentication/scheme/{name}', vdom=vdom)
