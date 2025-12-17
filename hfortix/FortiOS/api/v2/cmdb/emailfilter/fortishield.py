"""
FortiOS CMDB - Email Filter FortiGuard

Configure FortiGuard AntiSpam settings.

This is a singleton endpoint - only GET and PUT operations are supported.

API Endpoints:
    GET  /api/v2/cmdb/emailfilter/fortishield  - Get configuration
    PUT  /api/v2/cmdb/emailfilter/fortishield  - Update configuration
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Dict, Optional, Union

if TYPE_CHECKING:
    from ....http_client import HTTPClient


from hfortix.FortiOS.http_client import encode_path_component


class Fortishield:
    """Email filter FortiGuard AntiSpam settings endpoint"""

    def __init__(self, client: "HTTPClient") -> None:
        """
        Initialize Fortishield endpoint.

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
        Get FortiGuard AntiSpam settings.

        Args:
            datasource (bool, optional): Include datasource information
            with_meta (bool, optional): Include meta information
            skip (bool, optional): Enable CLI skip operator
            format (str, optional): List of property names to include, separated by |
            action (str, optional): Special action - 'default', 'schema', 'revision'
            vdom (str, optional): Virtual Domain name
            **kwargs: Additional query parameters

        Returns:
            dict: API response containing FortiGuard AntiSpam settings

        Examples:
            >>> # Get FortiGuard AntiSpam settings
            >>> settings = fgt.cmdb.emailfilter.fortishield.get()

            >>> # Get with meta information
            >>> settings = fgt.cmdb.emailfilter.fortishield.get(with_meta=True)
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
            "emailfilter/fortishield",
            params=params if params else None,
            vdom=vdom,
            raw_json=raw_json,
        )

    def put(
        self,
        payload_dict: Optional[Dict[str, Any]] = None,
        # FortiGuard configuration
        spam_submit_srv: Optional[str] = None,
        spam_submit_force: Optional[str] = None,
        spam_submit_txt2htm: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Update FortiGuard AntiSpam settings.

        Args:
            spam_submit_srv (str, optional): Hostname of spam submission server
            spam_submit_force (str, optional): Enable to submit all email to FortiGuard - 'enable'/'disable'
            spam_submit_txt2htm (str, optional): Submit text email to FortiGuard - 'enable'/'disable'
            vdom (str, optional): Virtual Domain name
            **kwargs: Additional parameters

        Returns:
            dict: API response

        Examples:
            >>> # PUT - Update FortiGuard settings
            >>> result = fgt.cmdb.emailfilter.fortishield.update(
            ...     spam_submit_srv='spam-submit.fortinet.com',
            ...     spam_submit_force='disable',
            ...     spam_submit_txt2htm='enable'
            ... )
        """
        data = {}

        param_map = {
            "spam_submit_srv": spam_submit_srv,
            "spam_submit_force": spam_submit_force,
            "spam_submit_txt2htm": spam_submit_txt2htm,
        }

        for key, value in param_map.items():
            if value is not None:
                data[key.replace("_", "-")] = value

        data.update(kwargs)

        return self._client.put(
            "cmdb", "emailfilter/fortishield", data=data, vdom=vdom, raw_json=raw_json
        )
