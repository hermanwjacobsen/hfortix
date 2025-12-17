"""
FortiOS CMDB - Router Setting

Configure router settings.

API Endpoints:
    GET  /api/v2/cmdb/router/setting  - Get configuration
    PUT  /api/v2/cmdb/router/setting  - Update configuration
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional, Union

if TYPE_CHECKING:
    from ....http_client import HTTPClient


class Setting:
    """Router setting endpoint"""

    def __init__(self, client: "HTTPClient") -> None:
        """
        Initialize Router Setting endpoint

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def get(
        self,
        datasource: Optional[bool] = None,
        with_meta: Optional[bool] = None,
        skip: Optional[bool] = None,
        format: Optional[list] = None,
        action: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Get router settings.

        Args:
            datasource: Enable to include datasource information
            with_meta: Enable to include meta information
            skip: Enable to call CLI skip operator
            format: List of property names to include in results
            action: Special action (default, schema, etc.)
            vdom: Virtual domain (None=use default, False=skip vdom, or specific vdom)
            **kwargs: Additional query parameters

        Returns:
            API response dict with router settings

        Examples:
            >>> # Get router settings
            >>> result = fgt.api.cmdb.router.setting.get()
            >>> print(f"Hostname: {result['results'].get('hostname', 'N/A')}")

            >>> # Get with metadata
            >>> result = fgt.api.cmdb.router.setting.get(with_meta=True)

            >>> # Get schema
            >>> schema = fgt.api.cmdb.router.setting.get(action='schema')
        """
        params = {}
        param_map = {
            "datasource": datasource,
            "with_meta": with_meta,
            "skip": skip,
            "format": format,
            "action": action,
        }

        for key, value in param_map.items():
            if value is not None:
                params[key] = value

        params.update(kwargs)

        return self._client.get(
            "cmdb", "router/setting", params=params if params else None, vdom=vdom
        )

    def put(
        self,
        data_dict: Optional[dict[str, Any]] = None,
        show_filter: Optional[str] = None,
        hostname: Optional[str] = None,
        kernel_route_distance: Optional[int] = None,
        vdom: Optional[Union[str, bool]] = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Update router settings.

        Supports three usage patterns:
        1. Dictionary: update(data_dict={'hostname': 'router1', 'show-filter': 'my-list'})
        2. Keywords: update(hostname='router1', show_filter='my-list')
        3. Mixed: update(data_dict={...}, hostname='override')

        Args:
            data_dict: Complete settings dictionary (Python snake_case keys)
            show_filter: Prefix-list as filter for showing routes (max 35 chars)
            hostname: Hostname for this virtual domain router (max 14 chars)
            kernel_route_distance: Administrative distance for routes learned from kernel (0-255)
            vdom: Virtual domain (None=use default, False=skip vdom, or specific vdom)
            **kwargs: Additional parameters

        Returns:
            API response dict

        Examples:
            >>> # PUT - Update hostname
            >>> result = fgt.api.cmdb.router.setting.update(
            ...     hostname='core-router'
            ... )

            >>> # PUT - Update kernel route distance
            >>> result = fgt.api.cmdb.router.setting.update(
            ...     kernel_route_distance=150
            ... )

            >>> # Use dictionary
            >>> config = {
            ...     'hostname': 'edge-router',
            ...     'show_filter': 'default-filter',
            ...     'kernel_route_distance': 200
            ... }
            >>> result = fgt.api.cmdb.router.setting.update(data_dict=config)
        """
        # Start with data_dict or empty dict
        data = data_dict.copy() if data_dict else {}

        # Map Python parameter names to API field names
        param_map = {
            "show_filter": "show-filter",
            "kernel_route_distance": "kernel-route-distance",
        }

        # Apply individual parameters (override data_dict if provided)
        if show_filter is not None:
            data[param_map["show_filter"]] = show_filter
        if hostname is not None:
            data["hostname"] = hostname
        if kernel_route_distance is not None:
            data[param_map["kernel_route_distance"]] = kernel_route_distance

        # Add any additional kwargs
        data.update(kwargs)

        return self._client.put("cmdb", "router/setting", data=data, vdom=vdom)
