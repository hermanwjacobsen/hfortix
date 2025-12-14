"""
FortiOS CMDB - Authentication Rules

Configure authentication rules for controlling user authentication requirements.

API Endpoints:
    GET    /api/v2/cmdb/authentication/rule       - Get all authentication rules
    GET    /api/v2/cmdb/authentication/rule/{name} - Get specific authentication rule
    POST   /api/v2/cmdb/authentication/rule       - Create authentication rule
    PUT    /api/v2/cmdb/authentication/rule/{name} - Update authentication rule
    DELETE /api/v2/cmdb/authentication/rule/{name} - Delete authentication rule
"""
from typing import TYPE_CHECKING, Any, Optional, Union

if TYPE_CHECKING:
    from ....client import FortiOS


class Rule:
    """Authentication rule endpoint"""

    def __init__(self, client: 'FortiOS') -> None:
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
        Get authentication rule(s)

        Retrieve authentication rules with filtering and query options.

        Args:
            name (str, optional): Rule name. If provided, get specific rule.
            attr (str, optional): Attribute name that references other table
            datasource (bool, optional): Include datasource information
            with_meta (bool, optional): Include meta information
            skip (bool, optional): Enable skip operator
            count (int, optional): Maximum number of entries to return
            skip_to_datasource (str, optional): Skip to datasource entry
            acs (bool, optional): If true, return in ascending order
            search (str, optional): Filter by search value
            scope (str, optional): Scope level - 'global', 'vdom', or 'both'
            format (str, optional): Return specific fields (e.g., 'name|status')
            action (str, optional): Action type - 'default', 'schema', or 'revision'
            vdom (str, optional): Virtual Domain name
            **kwargs: Additional query parameters

        Returns:
            dict: API response with rule data

        Examples:
            >>> # Get all authentication rules
            >>> rules = fgt.cmdb.authentication.rule.list()

            >>> # Get specific rule by name
            >>> rule = fgt.cmdb.authentication.rule.get('rule1')

            >>> # Get with filtering
            >>> filtered = fgt.cmdb.authentication.rule.get(
            ...     format='name|status',
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
        path = 'authentication/rule'
        if name is not None:
            path = f'{path}/{name}'

        return self._client.get('cmdb', path, params=params if params else None, vdom=vdom)

    def list(self, **kwargs: Any) -> dict[str, Any]:
        """
        Get all authentication rules (convenience method)

        Args:
            **kwargs: All parameters from get() method

        Returns:
            dict: API response with all rules

        Examples:
            >>> # Get all authentication rules
            >>> all_rules = fgt.cmdb.authentication.rule.list()
        """
        return self.get(**kwargs)

    def create(
        self,
        name: str,
        status: Optional[str] = None,
        protocol: Optional[str] = None,
        srcintf: Optional[list[Union[str, dict[str, Any]]]] = None,
        srcaddr: Optional[list[Union[str, dict[str, Any]]]] = None,
        srcaddr6: Optional[list[Union[str, dict[str, Any]]]] = None,
        dstaddr: Optional[list[Union[str, dict[str, Any]]]] = None,
        dstaddr6: Optional[list[Union[str, dict[str, Any]]]] = None,
        ip_based: Optional[str] = None,
        active_auth_method: Optional[str] = None,
        sso_auth_method: Optional[str] = None,
        web_auth_cookie: Optional[str] = None,
        web_portal: Optional[str] = None,
        cert_auth_cookie: Optional[str] = None,
        transaction_based: Optional[str] = None,
        cors_stateful: Optional[str] = None,
        cors_depth: Optional[int] = None,
        comments: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        **kwargs: Any
    ) -> dict[str, Any]:
        """
        Create authentication rule

        Create a new authentication rule to control user authentication requirements.
        Note: Either srcaddr or srcaddr6 is required by FortiOS.

        Args:
            name (str, required): Authentication rule name
            status (str, optional): Enable/disable rule - 'enable' or 'disable'
            protocol (str, optional): Protocol - 'http', 'ftp', 'socks', 'ssh', 'ztna-portal'
            srcintf (list, optional): List of source interface names or dicts with 'name' key
            srcaddr (list, required): List of IPv4 source addresses (strings or dicts with 'name' key)
            srcaddr6 (list, optional): List of IPv6 source addresses (strings or dicts with 'name' key)
            dstaddr (list, optional): List of IPv4 destination addresses (strings or dicts with 'name' key)
            dstaddr6 (list, optional): List of IPv6 destination addresses (strings or dicts with 'name' key)
            ip_based (str, optional): Enable/disable IP-based auth - 'enable' or 'disable'
            active_auth_method (str, optional): Active authentication method (scheme name)
            sso_auth_method (str, optional): SSO authentication method (scheme name)
            web_auth_cookie (str, optional): Enable/disable web auth cookies - 'enable' or 'disable'
            web_portal (str, optional): Enable/disable web portal - 'enable' or 'disable'
            cert_auth_cookie (str, optional): Enable/disable cert auth cookie - 'enable' or 'disable'
            transaction_based (str, optional): Enable/disable transaction-based auth - 'enable' or 'disable'
            cors_stateful (str, optional): Enable/disable CORS access - 'enable' or 'disable'
            cors_depth (int, optional): CORS depth (default: 3)
            comments (str, optional): Comment
            vdom (str, optional): Virtual Domain name
            **kwargs: Additional parameters

        Returns:
            dict: API response

        Examples:
            >>> # Create basic authentication rule (simple format)
            >>> result = fgt.cmdb.authentication.rule.create(
            ...     name='web-auth-rule',
            ...     status='enable',
            ...     protocol='http',
            ...     srcaddr=['all'],  # Simple string format
            ...     active_auth_method='form-based'
            ... )

            >>> # Create rule with source addresses (dict format also works)
            >>> result = fgt.cmdb.authentication.rule.create(
            ...     name='lan-auth-rule',
            ...     status='enable',
            ...     srcintf=['port2'],
            ...     srcaddr=[{'name': 'LAN-subnet'}],  # Dict format
            ...     active_auth_method='basic-auth'
            ... )
        """
        # Convert simple lists to FortiOS format
        srcintf = self._format_name_list(srcintf)
        srcaddr = self._format_name_list(srcaddr)
        srcaddr6 = self._format_name_list(srcaddr6)
        dstaddr = self._format_name_list(dstaddr)
        dstaddr6 = self._format_name_list(dstaddr6)

        param_map = {
            'name': name,
            'status': status,
            'protocol': protocol,
            'srcintf': srcintf,
            'srcaddr': srcaddr,
            'srcaddr6': srcaddr6,
            'dstaddr': dstaddr,
            'dstaddr6': dstaddr6,
            'ip_based': ip_based,
            'active_auth_method': active_auth_method,
            'sso_auth_method': sso_auth_method,
            'web_auth_cookie': web_auth_cookie,
            'web_portal': web_portal,
            'cert_auth_cookie': cert_auth_cookie,
            'transaction_based': transaction_based,
            'cors_stateful': cors_stateful,
            'cors_depth': cors_depth,
            'comments': comments
        }

        api_field_map = {
            'name': 'name',
            'status': 'status',
            'protocol': 'protocol',
            'srcintf': 'srcintf',
            'srcaddr': 'srcaddr',
            'srcaddr6': 'srcaddr6',
            'dstaddr': 'dstaddr',
            'dstaddr6': 'dstaddr6',
            'ip_based': 'ip-based',
            'active_auth_method': 'active-auth-method',
            'sso_auth_method': 'sso-auth-method',
            'web_auth_cookie': 'web-auth-cookie',
            'web_portal': 'web-portal',
            'cert_auth_cookie': 'cert-auth-cookie',
            'transaction_based': 'transaction-based',
            'cors_stateful': 'cors-stateful',
            'cors_depth': 'cors-depth',
            'comments': 'comments'
        }

        data = {}
        for param_name, value in param_map.items():
            if value is not None:
                api_name = api_field_map[param_name]
                data[api_name] = value

        data.update(kwargs)

        return self._client.post('cmdb', 'authentication/rule', data, vdom=vdom)

    def update(
        self,
        name: str,
        status: Optional[str] = None,
        protocol: Optional[str] = None,
        srcintf: Optional[list[Union[str, dict[str, Any]]]] = None,
        srcaddr: Optional[list[Union[str, dict[str, Any]]]] = None,
        srcaddr6: Optional[list[Union[str, dict[str, Any]]]] = None,
        dstaddr: Optional[list[Union[str, dict[str, Any]]]] = None,
        dstaddr6: Optional[list[Union[str, dict[str, Any]]]] = None,
        ip_based: Optional[str] = None,
        active_auth_method: Optional[str] = None,
        sso_auth_method: Optional[str] = None,
        web_auth_cookie: Optional[str] = None,
        web_portal: Optional[str] = None,
        cert_auth_cookie: Optional[str] = None,
        transaction_based: Optional[str] = None,
        cors_stateful: Optional[str] = None,
        cors_depth: Optional[int] = None,
        comments: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        **kwargs: Any
    ) -> dict[str, Any]:
        """
        Update authentication rule

        Update an existing authentication rule configuration.

        Args:
            name (str, required): Authentication rule name
            status (str, optional): Enable/disable rule - 'enable' or 'disable'
            protocol (str, optional): Protocol - 'http', 'ftp', 'socks', 'ssh', 'ztna-portal'
            srcintf (list, optional): List of source interface names
            srcaddr (list, optional): List of IPv4 source addresses
            srcaddr6 (list, optional): List of IPv6 source addresses
            dstaddr (list, optional): List of IPv4 destination addresses
            dstaddr6 (list, optional): List of IPv6 destination addresses
            ip_based (str, optional): Enable/disable IP-based auth - 'enable' or 'disable'
            active_auth_method (str, optional): Active authentication method
            sso_auth_method (str, optional): SSO authentication method
            web_auth_cookie (str, optional): Enable/disable web auth cookies - 'enable' or 'disable'
            web_portal (str, optional): Enable/disable web portal - 'enable' or 'disable'
            cert_auth_cookie (str, optional): Enable/disable cert auth cookie - 'enable' or 'disable'
            transaction_based (str, optional): Enable/disable transaction-based auth - 'enable' or 'disable'
            cors_stateful (str, optional): Enable/disable CORS access - 'enable' or 'disable'
            cors_depth (int, optional): CORS depth
            comments (str, optional): Comment
            vdom (str, optional): Virtual Domain name
            **kwargs: Additional parameters

        Returns:
            dict: API response

        Examples:
            >>> # Update rule status
            >>> result = fgt.cmdb.authentication.rule.update(
            ...     name='web-auth-rule',
            ...     status='disable'
            ... )

            >>> # Update authentication method
            >>> result = fgt.cmdb.authentication.rule.update(
            ...     name='web-auth-rule',
            ...     active_auth_method='ldap-auth'
            ... )
        """
        # Convert simple lists to FortiOS format
        srcintf = self._format_name_list(srcintf)
        srcaddr = self._format_name_list(srcaddr)
        srcaddr6 = self._format_name_list(srcaddr6)
        dstaddr = self._format_name_list(dstaddr)
        dstaddr6 = self._format_name_list(dstaddr6)

        param_map = {
            'status': status,
            'protocol': protocol,
            'srcintf': srcintf,
            'srcaddr': srcaddr,
            'srcaddr6': srcaddr6,
            'dstaddr': dstaddr,
            'dstaddr6': dstaddr6,
            'ip_based': ip_based,
            'active_auth_method': active_auth_method,
            'sso_auth_method': sso_auth_method,
            'web_auth_cookie': web_auth_cookie,
            'web_portal': web_portal,
            'cert_auth_cookie': cert_auth_cookie,
            'transaction_based': transaction_based,
            'cors_stateful': cors_stateful,
            'cors_depth': cors_depth,
            'comments': comments
        }

        api_field_map = {
            'status': 'status',
            'protocol': 'protocol',
            'srcintf': 'srcintf',
            'srcaddr': 'srcaddr',
            'srcaddr6': 'srcaddr6',
            'dstaddr': 'dstaddr',
            'dstaddr6': 'dstaddr6',
            'ip_based': 'ip-based',
            'active_auth_method': 'active-auth-method',
            'sso_auth_method': 'sso-auth-method',
            'web_auth_cookie': 'web-auth-cookie',
            'web_portal': 'web-portal',
            'cert_auth_cookie': 'cert-auth-cookie',
            'transaction_based': 'transaction-based',
            'cors_stateful': 'cors-stateful',
            'cors_depth': 'cors-depth',
            'comments': 'comments'
        }

        data = {}
        for param_name, value in param_map.items():
            if value is not None:
                api_name = api_field_map[param_name]
                data[api_name] = value

        data.update(kwargs)

        return self._client.put('cmdb', f'authentication/rule/{name}', data, vdom=vdom)

    def delete(
        self,
        name: str,
        vdom: Optional[Union[str, bool]] = None
    ) -> dict[str, Any]:
        """
        Delete authentication rule

        Args:
            name (str, required): Authentication rule name
            vdom (str, optional): Virtual Domain name

        Returns:
            dict: API response

        Examples:
            >>> # Delete authentication rule
            >>> result = fgt.cmdb.authentication.rule.delete('web-auth-rule')
        """
        return self._client.delete('cmdb', f'authentication/rule/{name}', vdom=vdom)
