"""
FortiOS CMDB - System SshConfig

Configure SSH config.

API Endpoints:
    GET  /system/ssh-config  - Get configuration
    PUT  /system/ssh-config  - Update configuration
"""
from __future__ import annotations

from typing import TYPE_CHECKING, Any, Dict, Optional, Union

if TYPE_CHECKING:
    from ....http_client import HTTPClient


class SshConfig:
    """ssh-config settings endpoint (singleton)"""

    def __init__(self, client: "HTTPClient") -> None:
        """
        Initialize SshConfig endpoint

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def get(
        self,
        datasource: Optional[bool] = None,
        with_meta: Optional[bool] = None,
        skip: Optional[bool] = None,
        action: Optional[str] = None,
        format: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Get ssh-config settings

        Args:
            datasource (bool, optional): Include datasource information
            with_meta (bool, optional): Include metadata
            skip (bool, optional): Enable CLI skip operator
            action (str, optional): Special actions
            format (str, optional): Field list to return
            vdom (str/bool, optional): Virtual domain, False to skip
            **kwargs: Additional query parameters

        Returns:
            dict: API response with settings

        Examples:
            >>> # Get current settings
            >>> settings = fgt.api.cmdb.system.ssh_config.get()
            >>> print(settings)
        """
        params = {}
        
        param_map = {
            "datasource": datasource,
            "with_meta": with_meta,
            "skip": skip,
            "action": action,
            "format": format,
        }
        
        for key, value in param_map.items():
            if value is not None:
                params[key] = value
        
        params.update(kwargs)
        
        return self._client.get("cmdb", "system/ssh-config", params=params if params else None, vdom=vdom)

    def put(
        self,
        payload_dict: Optional[Dict[str, Any]] = None,
        vdom: Optional[Union[str, bool]] = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Update ssh-config settings

        Args:
            payload_dict (dict, optional): Complete configuration as dictionary
            vdom (str/bool, optional): Virtual domain, False to skip
            **kwargs: Additional parameters to update

        Returns:
            dict: API response

        Examples:
            >>> # PUT - Update with dictionary
            >>> result = fgt.api.cmdb.system.ssh_config.update(
            ...     payload_dict={'setting1': 'value1'}
            ... )
            
            >>> # PUT - Update with parameters
            >>> result = fgt.api.cmdb.system.ssh_config.update(
            ...     setting1='value1',
            ...     setting2='value2'
            ... )
        """
        data = payload_dict.copy() if payload_dict else {}
        
        for key, value in kwargs.items():
            if value is not None:
                api_key = key.replace("_", "-")
                data[api_key] = value
        
        return self._client.put("cmdb", "system/ssh-config", data=data, vdom=vdom)
