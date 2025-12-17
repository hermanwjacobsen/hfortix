"""
FortiOS CMDB - System Npu

Configure NPU attributes.

API Endpoints:
    GET  /system/npu  - Get configuration
    PUT  /system/npu  - Update configuration
"""
from __future__ import annotations

from typing import TYPE_CHECKING, Any, Dict, Optional, Union

if TYPE_CHECKING:
    from ....http_client import HTTPClient


class Npu:
    """npu settings endpoint (singleton)"""

    def __init__(self, client: "HTTPClient") -> None:
        """
        Initialize Npu endpoint

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
        Get npu settings

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
            >>> settings = fgt.api.cmdb.system.npu.get()
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
        
        return self._client.get("cmdb", "system/npu", params=params if params else None, vdom=vdom)

    def put(
        self,
        payload_dict: Optional[Dict[str, Any]] = None,
        vdom: Optional[Union[str, bool]] = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Update npu settings

        Args:
            payload_dict (dict, optional): Complete configuration as dictionary
            vdom (str/bool, optional): Virtual domain, False to skip
            **kwargs: Additional parameters to update

        Returns:
            dict: API response

        Examples:
            >>> # PUT - Update with dictionary
            >>> result = fgt.api.cmdb.system.npu.update(
            ...     payload_dict={'setting1': 'value1'}
            ... )
            
            >>> # PUT - Update with parameters
            >>> result = fgt.api.cmdb.system.npu.update(
            ...     setting1='value1',
            ...     setting2='value2'
            ... )
        """
        data = payload_dict.copy() if payload_dict else {}
        
        for key, value in kwargs.items():
            if value is not None:
                api_key = key.replace("_", "-")
                data[api_key] = value
        
        return self._client.put("cmdb", "system/npu", data=data, vdom=vdom)
