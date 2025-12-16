"""
FortiOS CMDB - Endpoint Control Settings

Configure endpoint control settings.

API Endpoints:
    GET /api/v2/cmdb/endpoint-control/settings - Get endpoint control settings
    PUT /api/v2/cmdb/endpoint-control/settings - Update endpoint control settings
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Dict, Optional, Union

if TYPE_CHECKING:
    from ....http_client import HTTPClient


class Settings:
    """Endpoint Control Settings endpoint (singleton)"""

    def __init__(self, client: "HTTPClient") -> None:
        """
        Initialize Settings endpoint.

        Args:
            client: FortiOS API client instance
        """
        self._client = client

    def get(
        self,
        # Query parameters
        datasource: Optional[bool] = None,
        with_meta: Optional[bool] = None,
        skip: Optional[bool] = None,
        format: Optional[str] = None,
        action: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Get endpoint control settings.

        Args:
            datasource (bool, optional): Include datasource information
            with_meta (bool, optional): Include meta information
            skip (bool, optional): Enable CLI skip operator
            format (str, optional): List of property names to include, separated by |
            action (str, optional): Special action - 'default', 'schema', 'revision'
            vdom (str, optional): Virtual Domain name
            **kwargs: Additional query parameters

        Returns:
            dict: API response containing settings

        Examples:
            >>> # Get endpoint control settings
            >>> settings = fgt.cmdb.endpoint_control.settings.get()

            >>> # Get with specific fields
            >>> settings = fgt.cmdb.endpoint_control.settings.get(
            ...     format='forticlient-keepalive-interval|forticlient-sys-update-interval'
            ... )
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
            "cmdb",
            "endpoint-control/settings",
            params=params if params else None,
            vdom=vdom,
            raw_json=raw_json,
        )

    def update(
        self,
        payload_dict: Optional[Dict[str, Any]] = None,
        # FortiClient settings
        forticlient_reg_key_enforce: Optional[str] = None,
        forticlient_reg_key: Optional[str] = None,
        forticlient_reg_timeout: Optional[int] = None,
        download_custom_link: Optional[str] = None,
        download_location: Optional[str] = None,
        forticlient_offline_grace: Optional[str] = None,
        forticlient_offline_grace_interval: Optional[int] = None,
        forticlient_keepalive_interval: Optional[int] = None,
        forticlient_sys_update_interval: Optional[int] = None,
        forticlient_avdb_update_interval: Optional[int] = None,
        forticlient_warning_interval: Optional[int] = None,
        forticlient_user_avatar: Optional[str] = None,
        forticlient_disconnect_unsupported_client: Optional[str] = None,
        forticlient_dereg_unsupported_client: Optional[str] = None,
        forticlient_ems_rest_api_call_timeout: Optional[int] = None,
        # Update parameters
        action: Optional[str] = None,
        scope: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Update endpoint control settings.

        Args:
            forticlient_reg_key_enforce (str, optional): Enforce FortiClient registration keys
                'enable'/'disable'
            forticlient_reg_key (str, optional): FortiClient registration key
            forticlient_reg_timeout (int, optional): FortiClient registration license timeout
                (0-180 days, 0 = disabled)
            download_custom_link (str, optional): Customized URL for downloading FortiClient
            download_location (str, optional): FortiClient download location
                'fortiguard'/'any'
            forticlient_offline_grace (str, optional): Grace period for offline registered clients
                'enable'/'disable'
            forticlient_offline_grace_interval (int, optional): Grace period interval (60-600 seconds)
            forticlient_keepalive_interval (int, optional): Keepalive interval (20-300 seconds,
                default 60)
            forticlient_sys_update_interval (int, optional): System update interval (30-1440 minutes,
                default 720)
            forticlient_avdb_update_interval (int, optional): Antivirus database update interval
                (0-24 hours, default 8)
            forticlient_warning_interval (int, optional): Warning interval (0-30 days, default 1)
            forticlient_user_avatar (str, optional): Enable/disable user avatars - 'enable'/'disable'
            forticlient_disconnect_unsupported_client (str, optional): Disconnect unsupported clients
                'enable'/'disable'
            forticlient_dereg_unsupported_client (str, optional): Deregister unsupported clients
                'enable'/'disable'
            forticlient_ems_rest_api_call_timeout (int, optional): FortiClient EMS REST API call
                timeout (500-30000 ms, default 5000)
            action (str, optional): 'add-members', 'replace-members', 'remove-members'
            scope (str, optional): Scope level - 'global' or 'vdom'
            vdom (str, optional): Virtual Domain name
            **kwargs: Additional parameters

        Returns:
            dict: API response

        Examples:
            >>> # Update FortiClient keepalive interval
            >>> result = fgt.cmdb.endpoint_control.settings.update(
            ...     forticlient_keepalive_interval=120
            ... )

            >>> # Update multiple settings
            >>> result = fgt.cmdb.endpoint_control.settings.update(
            ...     forticlient_keepalive_interval=90,
            ...     forticlient_sys_update_interval=480,
            ...     forticlient_user_avatar='enable'
            ... )
        """
        data = {}

        param_map = {
            "forticlient_reg_key_enforce": forticlient_reg_key_enforce,
            "forticlient_reg_key": forticlient_reg_key,
            "forticlient_reg_timeout": forticlient_reg_timeout,
            "download_custom_link": download_custom_link,
            "download_location": download_location,
            "forticlient_offline_grace": forticlient_offline_grace,
            "forticlient_offline_grace_interval": forticlient_offline_grace_interval,
            "forticlient_keepalive_interval": forticlient_keepalive_interval,
            "forticlient_sys_update_interval": forticlient_sys_update_interval,
            "forticlient_avdb_update_interval": forticlient_avdb_update_interval,
            "forticlient_warning_interval": forticlient_warning_interval,
            "forticlient_user_avatar": forticlient_user_avatar,
            "forticlient_disconnect_unsupported_client": forticlient_disconnect_unsupported_client,
            "forticlient_dereg_unsupported_client": forticlient_dereg_unsupported_client,
            "forticlient_ems_rest_api_call_timeout": forticlient_ems_rest_api_call_timeout,
            "action": action,
            "scope": scope,
        }

        for key, value in param_map.items():
            if value is not None:
                data[key.replace("_", "-")] = value

        data.update(kwargs)

        return self._client.put(
            "cmdb", "endpoint-control/settings", data=data, vdom=vdom, raw_json=raw_json
        )
