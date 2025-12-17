"""
FortiOS CMDB - Log Memory Global Setting

Global settings for memory logging.

API Endpoints:
    GET /api/v2/cmdb/log.memory/global-setting - Get memory global settings
    PUT /api/v2/cmdb/log.memory/global-setting - Update memory global settings
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional, Union

if TYPE_CHECKING:
    from ...http_client import HTTPClient


class MemoryGlobalSetting:
    """Log Memory Global Setting endpoint (singleton)"""

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
        Get memory global settings.

        Args:
            datasource: Include datasource information
            with_meta: Include metadata
            skip: Enable CLI skip operator
            action: Special actions (default, schema, revision)
            vdom: Virtual domain
            **kwargs: Additional query parameters

        Returns:
            Memory global settings configuration

        Examples:
            >>> # Get memory global settings
            >>> result = fgt.api.cmdb.log.memory.global_setting.get()

            >>> # Get with metadata
            >>> result = fgt.api.cmdb.log.memory.global_setting.get(with_meta=True)
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

        path = "log.memory/global-setting"
        return self._client.get("cmdb", path, params=params if params else None, vdom=vdom)

    def update(
        self,
        data_dict: Optional[dict[str, Any]] = None,
        max_size: Optional[int] = None,
        full_first_warning_threshold: Optional[int] = None,
        full_second_warning_threshold: Optional[int] = None,
        full_final_warning_threshold: Optional[int] = None,
        vdom: Optional[Union[str, bool]] = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Update memory global settings.

        Supports three usage patterns:
        1. Dictionary: update(data_dict={'max-size': 163840})
        2. Keywords: update(max_size=163840)
        3. Mixed: update(data_dict={...}, max_size=163840)

        Args:
            data_dict: Complete configuration dictionary
            max_size: Maximum memory size in KB
            full_first_warning_threshold: First warning threshold percentage
            full_second_warning_threshold: Second warning threshold percentage
            full_final_warning_threshold: Final warning threshold percentage
            vdom: Virtual domain
            **kwargs: Additional parameters

        Returns:
            Update result

        Examples:
            >>> # Update with dictionary
            >>> fgt.api.cmdb.log.memory.global_setting.update(
            ...     data_dict={'max-size': 163840}
            ... )

            >>> # Update with keywords
            >>> fgt.api.cmdb.log.memory.global_setting.update(
            ...     max_size=163840,
            ...     full_first_warning_threshold=75
            ... )

            >>> # Update with mixed
            >>> config = {'max-size': 163840}
            >>> fgt.api.cmdb.log.memory.global_setting.update(
            ...     data_dict=config,
            ...     full_first_warning_threshold=75
            ... )
        """
        data = data_dict.copy() if data_dict else {}

        param_map = {
            "max_size": max_size,
            "full_first_warning_threshold": full_first_warning_threshold,
            "full_second_warning_threshold": full_second_warning_threshold,
            "full_final_warning_threshold": full_final_warning_threshold,
        }

        api_field_map = {
            "max_size": "max-size",
            "full_first_warning_threshold": "full-first-warning-threshold",
            "full_second_warning_threshold": "full-second-warning-threshold",
            "full_final_warning_threshold": "full-final-warning-threshold",
        }

        for python_key, value in param_map.items():
            if value is not None:
                api_key = api_field_map[python_key]
                data[api_key] = value

        data.update(kwargs)

        path = "log.memory/global-setting"
        return self._client.put("cmdb", path, data=data, vdom=vdom)
