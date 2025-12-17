"""
TACACS+ accounting3 filter endpoint module.

This module provides access to the log.tacacs+accounting3/filter endpoint
for configuring which TACACS+ accounting events to log.

API Path: log.tacacs+accounting3/filter
"""

from typing import TYPE_CHECKING, Any, Dict, Optional

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client import HTTPClient


class TacacsAccounting3Filter:
    """
    Interface for configuring TACACS+ accounting3 filter settings.

    This class provides methods to manage TACACS+ accounting3 filter configuration,
    controlling which accounting events are sent to TACACS+ servers.

    Supports three types of parameters:
    - data_dict: Standard dictionary format matching API structure
    - keyword arguments: Python snake_case parameters
    - mixed: Both data_dict and keyword arguments combined

    Example usage:
        # Using keyword arguments (snake_case)
        fgt.api.cmdb.log.tacacs_accounting3.filter.update(
            login_audit='enable',
            config_change_audit='enable'
        )

        # Using data_dict (hyphenated)
        fgt.api.cmdb.log.tacacs_accounting3.filter.update(
            data_dict={
                'login-audit': 'enable',
                'config-change-audit': 'enable'
            }
        )
    """

    def __init__(self, client: "HTTPClient") -> None:
        """
        Initialize the TacacsAccounting3Filter instance.

        Args:
            client: The HTTP client used to communicate with the FortiOS device
        """
        self._client = client
        self._endpoint = "log.tacacs+accounting3/filter"

    def get(self) -> Dict[str, Any]:
        """
        Retrieve current TACACS+ accounting3 filter configuration.

        Returns:
            Dictionary containing TACACS+ accounting3 filter settings

        Example:
            >>> result = fgt.api.cmdb.log.tacacs_accounting3.filter.get()
            >>> print(result['login-audit'])
            'enable'
        """
        path = "log.tacacs+accounting3/filter"
        return self._client.get("cmdb", path)

    def update(
        self,
        data_dict: Optional[Dict[str, Any]] = None,
        cli_cmd_audit: Optional[str] = None,
        config_change_audit: Optional[str] = None,
        login_audit: Optional[str] = None,
        **kwargs: Any,
    ) -> Dict[str, Any]:
        """
        Update TACACS+ accounting3 filter configuration.

        Accepts parameters in multiple formats for flexibility:
        1. data_dict with API format (hyphenated keys)
        2. Python snake_case keyword arguments
        3. Both data_dict and kwargs combined

        Args:
            data_dict: Dictionary with API format parameters (hyphenated)
            cli_cmd_audit: Enable/disable TACACS+ accounting for CLI command audit
                         (enable | disable)
            config_change_audit: Enable/disable TACACS+ accounting for config changes
                               (enable | disable)
            login_audit: Enable/disable TACACS+ accounting for login events
                        (enable | disable)
            **kwargs: Additional parameters in API format (hyphenated)

        Returns:
            Dictionary containing API response

        Example:
            >>> # Using keyword arguments
            >>> fgt.api.cmdb.log.tacacs_accounting3.filter.update(
            ...     login_audit='enable',
            ...     config_change_audit='enable'
            ... )

            >>> # Using data_dict
            >>> fgt.api.cmdb.log.tacacs_accounting3.filter.update(
            ...     data_dict={'login-audit': 'enable'}
            ... )
        """
        # Start with data_dict if provided, otherwise empty dict
        payload = dict(data_dict) if data_dict else {}

        # Map Python parameter names to API format and add to payload
        param_map = {
            "cli_cmd_audit": "cli-cmd-audit",
            "config_change_audit": "config-change-audit",
            "login_audit": "login-audit",
        }

        # Add mapped parameters
        for py_name, api_name in param_map.items():
            value = locals().get(py_name)
            if value is not None:
                payload[api_name] = value

        # Add any additional kwargs
        payload.update(kwargs)

        path = "log.tacacs+accounting3/filter"
        return self._client.put("cmdb", path, data=payload)
