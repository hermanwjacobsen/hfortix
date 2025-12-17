"""
FortiOS CMDB - Firewall IP-MAC Binding Setting

Configure IP to MAC binding settings.

API Endpoints:
    GET  /api/v2/cmdb/firewall.ipmacbinding/setting  - Get configuration
    PUT  /api/v2/cmdb/firewall.ipmacbinding/setting  - Update configuration
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Dict, Optional, Union

if TYPE_CHECKING:
    from ....http_client import HTTPClient


from hfortix.FortiOS.http_client import encode_path_component


class IpmacbindingSetting:
    """Firewall IP-MAC binding setting endpoint"""

    def __init__(self, client: "HTTPClient") -> None:
        """
        Initialize IpmacbindingSetting endpoint

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
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Get IP-MAC binding settings.

        Args:
            datasource: Include datasource information
            with_meta: Include metadata
            skip: Enable CLI skip operator
            format: List of property names to include
            action: Special actions (default, schema)
            vdom: Virtual domain (None=use default, False=skip vdom, or specific vdom)
            **kwargs: Additional query parameters

        Returns:
            API response dict

        Examples:
            >>> # Get IP-MAC binding settings
            >>> result = fgt.cmdb.firewall.ipmacbinding_setting.get()
            >>> print(f"Bind through firewall: {result['results']['bindthroughfw']}")

            >>> # Get with metadata
            >>> result = fgt.cmdb.firewall.ipmacbinding_setting.get(with_meta=True)

            >>> # Get schema
            >>> result = fgt.cmdb.firewall.ipmacbinding_setting.get(action='schema')
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

        path = "firewall.ipmacbinding/setting"
        return self._client.get(
            "cmdb", path, params=params if params else None, vdom=vdom, raw_json=raw_json
        )

    def put(
        self,
        payload_dict: Optional[Dict[str, Any]] = None,
        bindthroughfw: Optional[str] = None,
        bindtofw: Optional[str] = None,
        undefinedhost: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Update IP-MAC binding settings.


        Supports two usage patterns:
        1. Pass data dict: update(payload_dict={'key': 'value'}, vdom='root')
        2. Pass kwargs: update(key='value', vdom='root')
        Args:
            bindthroughfw: Enable/disable IP/MAC binding for packets through firewall
                          ('enable' or 'disable')
            bindtofw: Enable/disable IP/MAC binding for packets to firewall
                     ('enable' or 'disable')
            undefinedhost: Action for packets with IP/MAC not in binding list
                          ('allow' or 'block', default='block')
            vdom: Virtual domain (None=use default, False=skip vdom, or specific vdom)
            **kwargs: Additional parameters

        Returns:
            API response dict

        Examples:
            >>> # Enable IP-MAC binding through firewall
            >>> result = fgt.cmdb.firewall.ipmacbinding_setting.update(
            ...     bindthroughfw='enable'
            ... )

            >>> # Configure all settings
            >>> result = fgt.cmdb.firewall.ipmacbinding_setting.update(
            ...     bindthroughfw='enable',
            ...     bindtofw='enable',
            ...     undefinedhost='block'
            ... )

            >>> # Disable binding and allow undefined hosts
            >>> result = fgt.cmdb.firewall.ipmacbinding_setting.update(
            ...     bindthroughfw='disable',
            ...     bindtofw='disable',
            ...     undefinedhost='allow'
            ... )
        """
        # Pattern 1: data dict provided
        if payload_dict is not None:
            # Use provided data dict
            pass
        # Pattern 2: kwargs pattern - build data dict
        else:
            payload_dict = {}
            if bindthroughfw is not None:
                payload_dict["bindthroughfw"] = bindthroughfw
            if bindtofw is not None:
                payload_dict["bindtofw"] = bindtofw
            if undefinedhost is not None:
                payload_dict["undefinedhost"] = undefinedhost

        payload_dict = {}

        param_map = {
            "bindthroughfw": bindthroughfw,
            "bindtofw": bindtofw,
            "undefinedhost": undefinedhost,
        }

        for key, value in param_map.items():
            if value is not None:
                payload_dict[key] = value

        # Add any additional kwargs
        for key, value in kwargs.items():
            if value is not None:
                payload_dict[key] = value

        path = "firewall.ipmacbinding/setting"
        return self._client.put("cmdb", path, data=payload_dict, vdom=vdom, raw_json=raw_json)
