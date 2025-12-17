"""
FTP Proxy Explicit endpoint.

This module provides the FtpProxyExplicit class for managing explicit FTP proxy settings.
"""

from typing import TYPE_CHECKING, Any, Optional

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client import HTTPClient


class FtpProxyExplicit:
    """
    Configure explicit FTP proxy settings.

    This class provides methods to manage explicit FTP proxy configuration.
    """

    def __init__(self, client: "HTTPClient"):
        """
        Initialize FTP Proxy Explicit endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client
        self._api_type = "cmdb"
        self._path = "ftp-proxy/explicit"

    def get(
        self,
        vdom: Optional[str] = None,
        raw_json: bool = False,
        data_dict: Optional[dict[str, Any]] = None,
        **kwargs: Any,
    ) -> dict[str, Any] | list[dict[str, Any]]:
        """
        Get explicit FTP proxy settings.

        Args:
            vdom: Virtual domain name. If not specified, uses management VDOM
            raw_json: Include metadata in response
            data_dict: Dictionary of additional parameters
            **kwargs: Additional parameters (merged with data_dict)

        Returns:
            Explicit FTP proxy configuration

        Raises:
            APIError: If the API request fails

        Example:
            >>> # Get explicit FTP proxy settings
            >>> config = fgt.api.cmdb.ftp_proxy.explicit.get()
            >>> print(config['status'])
            'disable'
            >>>
            >>> # Get with full response
            >>> response = fgt.api.cmdb.ftp_proxy.explicit.get(raw_json=True)
            >>> print(response['http_status'])
            200
        """
        params = data_dict.copy() if data_dict else {}
        params.update(kwargs)

        return self._client.get(
            self._api_type, self._path, params=params, vdom=vdom, raw_json=raw_json
        )

    def update(
        self,
        status: Optional[str] = None,
        incoming_port: Optional[str] = None,
        incoming_ip: Optional[str] = None,
        outgoing_ip: Optional[str] = None,
        sec_default_action: Optional[str] = None,
        server_data_mode: Optional[str] = None,
        ssl: Optional[str] = None,
        ssl_cert: Optional[list[dict[str, Any]]] = None,
        ssl_dh_bits: Optional[str] = None,
        ssl_algorithm: Optional[str] = None,
        vdom: Optional[str] = None,
        raw_json: bool = False,
        data_dict: Optional[dict[str, Any]] = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Update explicit FTP proxy settings.

        Args:
            status: Enable/disable the explicit FTP proxy ('enable' or 'disable')
            incoming_port: Accept incoming FTP requests on one or more ports
            incoming_ip: Accept incoming FTP requests from this IP address
            outgoing_ip: Outgoing FTP requests will leave from this IP address
            sec_default_action: Accept or deny sessions when no policy exists ('accept' or 'deny')
            server_data_mode: Mode of data session on FTP server side ('client' or 'passive')
            ssl: Enable/disable the explicit FTPS proxy ('enable' or 'disable')
            ssl_cert: List of certificate names to use for SSL connections
            ssl_dh_bits: Bit-size of DH prime ('768', '1024', '1536', '2048')
            ssl_algorithm: Encryption algorithms strength ('high', 'medium', 'low')
            vdom: Virtual domain name. If not specified, uses management VDOM
            raw_json: Include metadata in response
            data_dict: Dictionary of parameters to send (overridden by explicit params)
            **kwargs: Additional parameters (merged with data_dict, overridden by explicit params)

        Returns:
            API response message

        Raises:
            APIError: If the API request fails

        Example:
            >>> # Enable explicit FTP proxy
            >>> fgt.api.cmdb.ftp_proxy.explicit.update(
            ...     status='enable',
            ...     incoming_port='21',
            ...     incoming_ip='192.168.1.99',
            ...     outgoing_ip='192.168.1.99',
            ...     sec_default_action='deny'
            ... )
            >>>
            >>> # Enable FTPS with SSL settings
            >>> fgt.api.cmdb.ftp_proxy.explicit.update(
            ...     ssl='enable',
            ...     ssl_cert=[{'name': 'Fortinet_Factory'}],
            ...     ssl_dh_bits='2048',
            ...     ssl_algorithm='high'
            ... )
            >>>
            >>> # Using data_dict pattern
            >>> config = {
            ...     'status': 'enable',
            ...     'incoming-port': '21',
            ...     'server-data-mode': 'passive'
            ... }
            >>> fgt.api.cmdb.ftp_proxy.explicit.update(data_dict=config)
        """
        payload_dict = data_dict.copy() if data_dict else {}
        payload_dict.update(kwargs)

        # Map Python-friendly names to API names
        param_map = {
            "status": "status",
            "incoming_port": "incoming-port",
            "incoming_ip": "incoming-ip",
            "outgoing_ip": "outgoing-ip",
            "sec_default_action": "sec-default-action",
            "server_data_mode": "server-data-mode",
            "ssl": "ssl",
            "ssl_cert": "ssl-cert",
            "ssl_dh_bits": "ssl-dh-bits",
            "ssl_algorithm": "ssl-algorithm",
        }

        params: dict[str, Any] = {}
        if vdom:
            params["vdom"] = vdom

        # Build payload from explicit parameters
        for py_name, api_name in param_map.items():
            value = locals().get(py_name)
            if value is not None:
                payload_dict[api_name] = value

        return self._client.put(
            self._api_type,
            self._path,
            data=payload_dict,
            params=params,
            vdom=vdom,
            raw_json=raw_json,
        )
