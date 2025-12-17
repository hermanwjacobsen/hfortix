"""
FortiOS CMDB - Log Memory Setting

Settings for memory buffer.

API Endpoints:
    GET  /api/v2/cmdb/log.memory/setting  - Get configuration
    PUT  /api/v2/cmdb/log.memory/setting  - Update configuration
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional, Union

if TYPE_CHECKING:
    from ...http_client import HTTPClient


class MemorySetting:
    """Log Memory Setting endpoint (singleton)"""

    def __init__(self, client: "HTTPClient") -> None:
        self._client = client

    def get(
        self,
        datasource: Optional[bool] = None,
        with_meta: Optional[bool] = None,
        skip: Optional[bool] = None,
        action: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Get memory buffer settings.

        Args:
            datasource: Include datasource information
            with_meta: Include metadata
            skip: Enable CLI skip operator
            action: Special actions (default, schema, revision)
            vdom: Virtual domain
            **kwargs: Additional query parameters

        Returns:
            Memory buffer settings configuration

        Examples:
            >>> # Get memory buffer settings
            >>> result = fgt.api.cmdb.log.memory.setting.get()

            >>> # Get with metadata
            >>> result = fgt.api.cmdb.log.memory.setting.get(with_meta=True)
        """
        params = {}
        param_map = {
            "datasource": datasource,
            "with_meta": with_meta,
            "skip": skip,
            "action": action,
        }

        for key, value in param_map.items():
            if value is not None:
                params[key] = value

        params.update(kwargs)

        path = "log.memory/setting"
        return self._client.get("cmdb", path, params=params if params else None, vdom=vdom)

    def put(
        self,
        data_dict: Optional[dict[str, Any]] = None,
        status: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Update memory buffer settings.

        Supports three usage patterns:
        1. Dictionary: update(data_dict={'status': 'enable'})
        2. Keywords: update(status='enable')
        3. Mixed: update(data_dict={...}, status='enable')

        Args:
            data_dict: Complete configuration dictionary
            status: Enable/disable memory buffer logging
            vdom: Virtual domain
            **kwargs: Additional parameters

        Returns:
            Update result

        Examples:
            >>> # Enable memory buffer logging
            >>> fgt.api.cmdb.log.memory.setting.update(status='enable')

            >>> # Disable memory buffer logging
            >>> fgt.api.cmdb.log.memory.setting.update(
            ...     data_dict={'status': 'disable'}
            ... )
        """
        data = data_dict.copy() if data_dict else {}

        if status is not None:
            data["status"] = status

        data.update(kwargs)

        path = "log.memory/setting"
        return self._client.put("cmdb", path, data=data, vdom=vdom)
