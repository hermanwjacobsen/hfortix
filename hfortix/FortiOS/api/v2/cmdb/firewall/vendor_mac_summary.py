"""
FortiOS vendor-mac-summary API wrapper.
Provides access to /api/v2/cmdb/firewall/vendor-mac-summary endpoint.
"""

from typing import Any, Dict, List, Optional, Union

from hfortix.FortiOS.http_client import encode_path_component


class VendorMacSummary:
    """
    Wrapper for firewall vendor-mac-summary API endpoint.

    Manages vendor-mac-summary configuration with full Swagger-spec parameter support.
    """

    def __init__(self, http_client: Any):
        """
        Initialize the VendorMacSummary wrapper.

        Args:
            http_client: The HTTP client for API communication
        """
        self._client = http_client
        self.path = "firewall/vendor-mac-summary"

    def get(
        self,
        datasource: Optional[Any] = None,
        with_meta: Optional[Any] = None,
        skip: Optional[Any] = None,
        format: Optional[Any] = None,
        action: Optional[Any] = None,
        vdom: Optional[Any] = None,
        raw_json: bool = False,
        **kwargs,
    ) -> Dict[str, Any]:
        """
        Retrieve vendor-mac-summary configuration (singleton).

        Args:
            datasource: Enable to include datasource information for each linked object.
            with_meta: Enable to include meta information about each object.
            skip: Enable to call CLI skip operator to hide skipped properties.
            format: List of property names to include in results, separated by |.
            action: default: Return the CLI default values for entire CLI tree.
            vdom: Specify the Virtual Domain(s) from which results are returned.
            **kwargs: Additional parameters

        Returns:
            API response dictionary with results
        """
        params = {}

        if datasource is not None:
            params["datasource"] = datasource
        if with_meta is not None:
            params["with_meta"] = with_meta
        if skip is not None:
            params["skip"] = skip
        if format is not None:
            params["format"] = format
        if action is not None:
            params["action"] = action

        params.update(kwargs)
        return self._client.get(
            "cmdb", self.path, params=params if params else None, vdom=vdom, raw_json=raw_json
        )
