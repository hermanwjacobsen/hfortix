"""
FortiOS CMDB - System ProbeResponse

Configure system probe response.

API Endpoints:
    GET  /system/probe-response  - Get configuration
    PUT  /system/probe-response  - Update configuration
"""
from __future__ import annotations

from typing import TYPE_CHECKING, Any, Dict, Optional, Union

if TYPE_CHECKING:
    from ....http_client import HTTPClient


class ProbeResponse:
    """probe-response settings endpoint (singleton)"""

    def __init__(self, client: "HTTPClient") -> None:
        """
        Initialize ProbeResponse endpoint

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
        Get probe-response settings

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
            >>> settings = fgt.api.cmdb.system.probe_response.get()
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
        
        return self._client.get("cmdb", "system/probe-response", params=params if params else None, vdom=vdom)

    def put(
        self,
        payload_dict: Optional[Dict[str, Any]] = None,
        vdom: Optional[Union[str, bool]] = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Update probe-response settings

        Args:
            payload_dict (dict, optional): Complete configuration as dictionary
            vdom (str/bool, optional): Virtual domain, False to skip
            **kwargs: Additional parameters to update

        Returns:
            dict: API response

        Examples:
            >>> # PUT - Update with dictionary
            >>> result = fgt.api.cmdb.system.probe_response.update(
            ...     payload_dict={'setting1': 'value1'}
            ... )
            
            >>> # PUT - Update with parameters
            >>> result = fgt.api.cmdb.system.probe_response.update(
            ...     setting1='value1',
            ...     setting2='value2'
            ... )
        """
        data = payload_dict.copy() if payload_dict else {}
        
        for key, value in kwargs.items():
            if value is not None:
                api_key = key.replace("_", "-")
                data[api_key] = value
        
        return self._client.put("cmdb", "system/probe-response", data=data, vdom=vdom)
