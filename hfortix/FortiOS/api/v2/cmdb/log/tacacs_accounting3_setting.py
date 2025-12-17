"""
TACACS+ accounting setting endpoint module.

This module provides access to the log.tacacs+accounting3/setting endpoint
for configuring TACACS+ accounting3 server settings.

API Path: log.tacacs+accounting3/setting
"""

from typing import TYPE_CHECKING, Any, Dict, Optional

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client import HTTPClient


class TacacsAccounting3Setting:
    """
    Interface for configuring TACACS+ accounting3 server settings.

    This class provides methods to manage TACACS+ accounting3 server configuration,
    including server details, authentication, and connection settings.

    Supports three types of parameters:
    - data_dict: Standard dictionary format matching API structure
    - keyword arguments: Python snake_case parameters
    - mixed: Both data_dict and keyword arguments combined

    Example usage:
        # Using keyword arguments (snake_case)
        fgt.api.cmdb.log.tacacs_accounting3.setting.update(
            status='enable',
            server='192.168.1.100',
            server_key='mysecretkey'
        )

        # Using data_dict (hyphenated)
        fgt.api.cmdb.log.tacacs_accounting3.setting.update(
            data_dict={
                'status': 'enable',
                'server': '192.168.1.100',
                'server-key': 'mysecretkey'
            }
        )
    """

    def __init__(self, client: "HTTPClient") -> None:
        """
        Initialize the TacacsAccounting3Setting instance.

        Args:
            client: The HTTP client used to communicate with the FortiOS device
        """
        self._client = client
        self._endpoint = "log.tacacs+accounting3/setting"

    def get(self) -> Dict[str, Any]:
        """
        Retrieve current TACACS+ accounting3 server settings.

        Returns:
            Dictionary containing TACACS+ accounting3 server configuration

        Example:
            >>> result = fgt.api.cmdb.log.tacacs_accounting3.setting.get()
            >>> print(result['status'])
            'enable'
        """
        path = "log.tacacs+accounting3/setting"
        return self._client.get("cmdb", path)

    def put(
        self,
        data_dict: Optional[Dict[str, Any]] = None,
        interface: Optional[str] = None,
        interface_select_method: Optional[str] = None,
        server: Optional[str] = None,
        server_key: Optional[str] = None,
        source_ip: Optional[str] = None,
        status: Optional[str] = None,
        vrf_select: Optional[str] = None,
        **kwargs: Any,
    ) -> Dict[str, Any]:
        """
        Update TACACS+ accounting3 server settings.

        Accepts parameters in multiple formats for flexibility:
        1. data_dict with API format (hyphenated keys)
        2. Python snake_case keyword arguments
        3. Both data_dict and kwargs combined

        Args:
            data_dict: Dictionary with API format parameters (hyphenated)
            interface: Specify outgoing interface to reach server
            interface_select_method: Specify how to select outgoing interface
                                   (auto | sdwan | specify)
            server: Address of TACACS+ server
            server_key: Key to access TACACS+ server
            source_ip: Source IP address for communication to TACACS+ server
            status: Enable/disable TACACS+ accounting (enable | disable)
            vrf_select: VRF select
            **kwargs: Additional parameters in API format (hyphenated)

        Returns:
            Dictionary containing API response

        Example:
            >>> # Using keyword arguments
            >>> fgt.api.cmdb.log.tacacs_accounting3.setting.update(
            ...     status='enable',
            ...     server='192.168.1.100',
            ...     server_key='mysecretkey'
            ... )

            >>> # Using data_dict
            >>> fgt.api.cmdb.log.tacacs_accounting3.setting.update(
            ...     data_dict={
            ...         'status': 'enable',
            ...         'server': '192.168.1.100'
            ...     }
            ... )
        """
        # Start with data_dict if provided, otherwise empty dict
        payload = dict(data_dict) if data_dict else {}

        # Map Python parameter names to API format and add to payload
        param_map = {
            "interface": "interface",
            "interface_select_method": "interface-select-method",
            "server": "server",
            "server_key": "server-key",
            "source_ip": "source-ip",
            "status": "status",
            "vrf_select": "vrf-select",
        }

        # Add mapped parameters
        for py_name, api_name in param_map.items():
            value = locals().get(py_name)
            if value is not None:
                payload[api_name] = value

        # Add any additional kwargs
        payload.update(kwargs)

        path = "log.tacacs+accounting3/setting"
        return self._client.put("cmdb", path, data=payload)
