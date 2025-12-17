"""
FortiOS CMDB - Email Filter Options

Configure AntiSpam options.

This is a singleton endpoint - only GET and PUT operations are supported.

API Endpoints:
    GET /api/v2/cmdb/emailfilter/options - Get AntiSpam options
    PUT /api/v2/cmdb/emailfilter/options - Update AntiSpam options
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Dict, Optional, Union

if TYPE_CHECKING:
    from ....http_client import HTTPClient


from hfortix.FortiOS.http_client import encode_path_component


class Options:
    """Email filter options endpoint"""

    def __init__(self, client: "HTTPClient") -> None:
        """
        Initialize Options endpoint.

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
        Get AntiSpam options.

        Args:
            datasource (bool, optional): Include datasource information
            with_meta (bool, optional): Include meta information
            skip (bool, optional): Enable CLI skip operator
            format (str, optional): List of property names to include, separated by |
            action (str, optional): Special action - 'default', 'schema', 'revision'
            vdom (str, optional): Virtual Domain name
            **kwargs: Additional query parameters

        Returns:
            dict: API response containing AntiSpam options

        Examples:
            >>> # Get AntiSpam options
            >>> options = fgt.cmdb.emailfilter.options.get()

            >>> # Get with meta information
            >>> options = fgt.cmdb.emailfilter.options.get(with_meta=True)
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
            "emailfilter/options",
            params=params if params else None,
            vdom=vdom,
            raw_json=raw_json,
        )

    def put(
        self,
        payload_dict: Optional[Dict[str, Any]] = None,
        # AntiSpam options
        dns_timeout: Optional[int] = None,
        vdom: Optional[Union[str, bool]] = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Update AntiSpam options.

        Args:
            dns_timeout (int, optional): DNS query timeout in seconds (1-30)
            vdom (str, optional): Virtual Domain name
            **kwargs: Additional parameters

        Returns:
            dict: API response

        Examples:
            >>> # PUT - Update DNS timeout
            >>> result = fgt.cmdb.emailfilter.options.update(
            ...     dns_timeout=10
            ... )
        """
        data = {}

        if dns_timeout is not None:
            data["dns-timeout"] = dns_timeout

        data.update(kwargs)

        return self._client.put(
            "cmdb", "emailfilter/options", data=data, vdom=vdom, raw_json=raw_json
        )
