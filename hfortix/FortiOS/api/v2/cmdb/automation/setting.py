"""
FortiOS CMDB - Automation Settings

Automation stitch configuration settings.

API Endpoints:
    GET    /automation/setting       - Get automation settings
    PUT    /automation/setting       - Update automation settings
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Dict, Optional, Union

if TYPE_CHECKING:
    from ....http_client import HTTPClient


from hfortix.FortiOS.http_client import encode_path_component


class Setting:
    """Automation setting endpoint"""

    def __init__(self, client: "HTTPClient") -> None:
        """
        Initialize Automation Setting endpoint

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
        vdom: Optional[Union[str, bool]] = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Get automation settings

        Args:
            datasource (bool, optional): Include datasource information
            with_meta (bool, optional): Include metadata
            skip (bool, optional): Enable CLI skip operator
            action (str, optional): Special actions (default, schema, revision)
            vdom (str/bool, optional): Virtual domain, False to skip
            **kwargs: Additional query parameters

        Returns:
            dict: API response with automation settings

        Examples:
            >>> # Get automation settings
            >>> settings = fgt.cmdb.automation.setting.get()
            >>> print(f"Status: {settings['http_status']}")

            >>> # Get with metadata
            >>> settings = fgt.cmdb.automation.setting.get(with_meta=True)
        """
        # Build query parameters
        params = {}

        if datasource is not None:
            params["datasource"] = datasource
        if with_meta is not None:
            params["with_meta"] = with_meta
        if skip is not None:
            params["skip"] = skip
        if action is not None:
            params["action"] = action

        # Add any additional parameters
        params.update(kwargs)

        return self._client.get(
            "cmdb", "automation/setting", params=params, vdom=vdom, raw_json=raw_json
        )

    def update(
        self,
        payload_dict: Optional[Dict[str, Any]] = None,
        max_concurrent_stitches: Optional[int] = None,
        fabric_sync: Optional[str] = None,
        secure_mode: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Update automation settings

        Args:
            max_concurrent_stitches (int, optional): Maximum number of concurrent automation stitches (32-1024, default: 512)
            fabric_sync (str, optional): Enable/disable sync with security fabric - 'enable' or 'disable' (default: 'enable')
            secure_mode (str, optional): Enable/disable secure running mode - 'enable' or 'disable' (default: 'disable')
            vdom (str/bool, optional): Virtual domain, False to skip
            **kwargs: Additional parameters

        Returns:
            dict: API response

        Examples:
            >>> # Update max concurrent stitches
            >>> result = fgt.cmdb.automation.setting.update(
            ...     max_concurrent_stitches=100
            ... )
            >>> print(f"Status: {result['status']}")

            >>> # Enable fabric sync and secure mode
            >>> result = fgt.cmdb.automation.setting.update(
            ...     fabric_sync='enable',
            ...     secure_mode='enable'
            ... )
        """
        # Build data dictionary
        data = {}

        # Map parameters (Python snake_case to API hyphenated-case)
        param_map = {
            "max_concurrent_stitches": "max-concurrent-stitches",
            "fabric_sync": "fabric-sync",
            "secure_mode": "secure-mode",
        }

        # Add parameters to data
        if max_concurrent_stitches is not None:
            data[param_map["max_concurrent_stitches"]] = max_concurrent_stitches
        if fabric_sync is not None:
            data[param_map["fabric_sync"]] = fabric_sync
        if secure_mode is not None:
            data[param_map["secure_mode"]] = secure_mode

        # Add any additional parameters
        data.update(kwargs)

        return self._client.put(
            "cmdb", "automation/setting", data=data, vdom=vdom, raw_json=raw_json
        )
