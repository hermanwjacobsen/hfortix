"""
FortiOS CMDB - Authentication Settings

Configure global authentication settings.

API Endpoints:
    GET    /api/v2/cmdb/authentication/setting       - Get authentication settings
    PUT    /api/v2/cmdb/authentication/setting       - Update authentication settings
"""
from typing import TYPE_CHECKING, Any, Optional, Union

if TYPE_CHECKING:
    from ....client import FortiOS


class Setting:
    """Authentication setting endpoint"""

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
        datasource: Optional[bool] = False,
        with_meta: Optional[bool] = False,
        skip: Optional[bool] = False,
        action: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        **kwargs: Any
    ) -> dict[str, Any]:
        """
        Get authentication settings

        Retrieve global authentication settings.

        Args:
            datasource (bool, optional): Include datasource information
            with_meta (bool, optional): Include meta information
            skip (bool, optional): Enable skip operator
            action (str, optional): Action type - 'default' or 'schema'
            vdom (str, optional): Virtual Domain name
            **kwargs: Additional query parameters

        Returns:
            dict: API response with authentication settings

        Examples:
            >>> # Get authentication settings
            >>> settings = fgt.cmdb.authentication.setting.get()

            >>> # Get with meta information
            >>> settings = fgt.cmdb.authentication.setting.get(with_meta=True)
        """
        params = {}
        param_map = {
            'datasource': datasource,
            'with_meta': with_meta,
            'skip': skip,
            'action': action
        }

        for key, value in param_map.items():
            if value is not None:
                params[key] = value

        params.update(kwargs)

        return self._client.get('cmdb', 'authentication/setting',
                               params=params if params else None, vdom=vdom)

    def update(
        self,
        active_auth_scheme: Optional[str] = None,
        sso_auth_scheme: Optional[str] = None,
        update_time: Optional[str] = None,
        persistent_cookie: Optional[str] = None,
        ip_auth_cookie: Optional[str] = None,
        cookie_max_age: Optional[int] = None,
        cookie_refresh_div: Optional[int] = None,
        captive_portal_type: Optional[str] = None,
        captive_portal_ip: Optional[str] = None,
        captive_portal_ip6: Optional[str] = None,
        captive_portal: Optional[str] = None,
        captive_portal6: Optional[str] = None,
        cert_auth: Optional[str] = None,
        cert_captive_portal: Optional[str] = None,
        cert_captive_portal_ip: Optional[str] = None,
        cert_captive_portal_port: Optional[int] = None,
        captive_portal_port: Optional[int] = None,
        auth_https: Optional[str] = None,
        captive_portal_ssl_port: Optional[int] = None,
        user_cert_ca: Optional[list[Union[str, dict[str, Any]]]] = None,
        dev_range: Optional[list[Union[str, dict[str, Any]]]] = None,
        vdom: Optional[Union[str, bool]] = None,
        **kwargs: Any
    ) -> dict[str, Any]:
        """
        Update authentication settings

        Update global authentication configuration settings.

        Args:
            active_auth_scheme (str, optional): Active authentication method (scheme name, max 35 chars)
            sso_auth_scheme (str, optional): Single-Sign-On authentication method (scheme name, max 35 chars)
            update_time (str, optional): Time of the last update
            persistent_cookie (str, optional): Enable/disable persistent cookie on web portal auth -
                'enable' or 'disable' (default: enable)
            ip_auth_cookie (str, optional): Enable/disable persistent cookie on IP based web portal auth -
                'enable' or 'disable' (default: disable)
            cookie_max_age (int, optional): Persistent web portal cookie max age in minutes
                (30-10080, default: 480)
            cookie_refresh_div (int, optional): Refresh rate divider of persistent cookie
                (2-4, default: 2)
            captive_portal_type (str, optional): Captive portal type - 'fqdn' or 'ip'
            captive_portal_ip (str, optional): Captive portal IPv4 address
            captive_portal_ip6 (str, optional): Captive portal IPv6 address
            captive_portal (str, optional): Captive portal host name (max 255 chars)
            captive_portal6 (str, optional): IPv6 captive portal host name (max 255 chars)
            cert_auth (str, optional): Enable/disable redirecting cert auth to HTTPS portal -
                'enable' or 'disable'
            cert_captive_portal (str, optional): Certificate captive portal host name (max 255 chars)
            cert_captive_portal_ip (str, optional): Certificate captive portal IP address
            cert_captive_portal_port (int, optional): Certificate captive portal port (1-65535, default: 7832)
            captive_portal_port (int, optional): Captive portal port number (1-65535, default: 7830)
            auth_https (str, optional): Enable/disable redirecting HTTP auth to HTTPS -
                'enable' or 'disable'
            captive_portal_ssl_port (int, optional): Captive portal SSL port (1-65535, default: 7831)
            user_cert_ca (list, optional): CA certificates for client cert verification
                (list of strings or dicts with 'name' key)
            dev_range (list, optional): Address range for IP based device query
                (list of strings or dicts with 'name' key)
            vdom (str, optional): Virtual Domain name
            **kwargs: Additional parameters

        Returns:
            dict: API response

        Examples:
            >>> # Enable persistent cookie
            >>> result = fgt.cmdb.authentication.setting.update(
            ...     persistent_cookie='enable',
            ...     cookie_max_age=1440
            ... )

            >>> # Configure captive portal
            >>> result = fgt.cmdb.authentication.setting.update(
            ...     captive_portal_type='fqdn',
            ...     captive_portal='portal.example.com',
            ...     captive_portal_port=8080
            ... )

            >>> # Set authentication schemes
            >>> result = fgt.cmdb.authentication.setting.update(
            ...     active_auth_scheme='form-auth',
            ...     sso_auth_scheme='saml-sso'
            ... )
        """
        # Convert simple lists to FortiOS format
        user_cert_ca = self._format_name_list(user_cert_ca)
        dev_range = self._format_name_list(dev_range)

        param_map = {
            'active_auth_scheme': active_auth_scheme,
            'sso_auth_scheme': sso_auth_scheme,
            'update_time': update_time,
            'persistent_cookie': persistent_cookie,
            'ip_auth_cookie': ip_auth_cookie,
            'cookie_max_age': cookie_max_age,
            'cookie_refresh_div': cookie_refresh_div,
            'captive_portal_type': captive_portal_type,
            'captive_portal_ip': captive_portal_ip,
            'captive_portal_ip6': captive_portal_ip6,
            'captive_portal': captive_portal,
            'captive_portal6': captive_portal6,
            'cert_auth': cert_auth,
            'cert_captive_portal': cert_captive_portal,
            'cert_captive_portal_ip': cert_captive_portal_ip,
            'cert_captive_portal_port': cert_captive_portal_port,
            'captive_portal_port': captive_portal_port,
            'auth_https': auth_https,
            'captive_portal_ssl_port': captive_portal_ssl_port,
            'user_cert_ca': user_cert_ca,
            'dev_range': dev_range
        }

        api_field_map = {
            'active_auth_scheme': 'active-auth-scheme',
            'sso_auth_scheme': 'sso-auth-scheme',
            'update_time': 'update-time',
            'persistent_cookie': 'persistent-cookie',
            'ip_auth_cookie': 'ip-auth-cookie',
            'cookie_max_age': 'cookie-max-age',
            'cookie_refresh_div': 'cookie-refresh-div',
            'captive_portal_type': 'captive-portal-type',
            'captive_portal_ip': 'captive-portal-ip',
            'captive_portal_ip6': 'captive-portal-ip6',
            'captive_portal': 'captive-portal',
            'captive_portal6': 'captive-portal6',
            'cert_auth': 'cert-auth',
            'cert_captive_portal': 'cert-captive-portal',
            'cert_captive_portal_ip': 'cert-captive-portal-ip',
            'cert_captive_portal_port': 'cert-captive-portal-port',
            'captive_portal_port': 'captive-portal-port',
            'auth_https': 'auth-https',
            'captive_portal_ssl_port': 'captive-portal-ssl-port',
            'user_cert_ca': 'user-cert-ca',
            'dev_range': 'dev-range'
        }

        data = {}
        for param_name, value in param_map.items():
            if value is not None:
                api_name = api_field_map[param_name]
                data[api_name] = value

        data.update(kwargs)

        return self._client.put('cmdb', 'authentication/setting', data, vdom=vdom)
