"""
FortiOS multicast-policy API wrapper.
Provides access to /api/v2/cmdb/firewall/multicast-policy endpoint.
"""

from typing import Any, Dict, List, Optional, Union

from hfortix.FortiOS.http_client import encode_path_component


class MulticastPolicy:
    """
    Wrapper for firewall multicast-policy API endpoint.

    Manages multicast policy configuration with full Swagger-spec parameter support.
    """

    def __init__(self, http_client: Any):
        """
        Initialize the MulticastPolicy wrapper.

        Args:
            http_client: The HTTP client for API communication
        """
        self._client = http_client
        self.path = "firewall/multicast-policy"


    def get(
        self,
        mkey: Optional[Union[str, int]] = None,
        # Standard query parameters
        datasource: Optional[str] = None,
        with_meta: Optional[bool] = None,
        skip: Optional[bool] = None,
        format: Optional[str] = None,
        vdom: Optional[str] = None,
        # Extended query parameters from Swagger spec
        acs: Optional[bool] = None,
        action: Optional[str] = None,
        attr: Optional[str] = None,
        count: Optional[int] = None,
        scope: Optional[str] = None,
        search: Optional[str] = None,
        skip_to_datasource: Optional[str] = None,
        raw_json: bool = False,
        **kwargs,
    ) -> Dict[str, Any]:
        """
        Retrieve a specific multicast policy by its ID.

        Args:
            mkey: The policy ID (primary key)
            datasource: Enable to include datasource information
            with_meta: Enable to include meta information
            skip: Enable to call CLI skip operator
            format: List of property names to include in results
            vdom: Specify the Virtual Domain(s)
            acs: If true, returned result are in ascending order
            action: Special action (e.g., 'datasource')
            attr: Attribute name that references other table
            count: Maximum number of entries to return
            scope: Scope [global|vdom|both]
            search: Search/filter the results
            skip_to_datasource: Skip to provided table's Nth entry
            **kwargs: Additional parameters

        Returns:
            API response dictionary with policy details
        """
        # Validate mkey
        if mkey is None:
            raise ValueError("mkey cannot be None")

        mkey_str = str(mkey)
        if not mkey_str:
            raise ValueError("mkey cannot be empty")

        params = {}

        # Build params dict from provided arguments
        if datasource is not None:
            params["datasource"] = datasource
        if with_meta is not None:
            params["with_meta"] = with_meta
        if skip is not None:
            params["skip"] = skip
        if format is not None:
            params["format"] = format
        if acs is not None:
            params["acs"] = acs
        if action is not None:
            params["action"] = action
        if attr is not None:
            params["attr"] = attr
        if count is not None:
            params["count"] = count
        if scope is not None:
            params["scope"] = scope
        if search is not None:
            params["search"] = search
        if skip_to_datasource is not None:
            params["skip_to_datasource"] = skip_to_datasource

        # Add any additional kwargs
        params.update(kwargs)

        return self._client.get(
            "cmdb", f"{self.path}/{encode_path_component(mkey)}" if mkey is not None else self.path, params=params, vdom=vdom, raw_json=raw_json
        )

    def post(
        self,
        data: Dict[str, Any],
        vdom: Optional[str] = None,
        # Extended query parameters from Swagger spec
        action: Optional[str] = None,
        nkey: Optional[str] = None,
        scope: Optional[str] = None,
        raw_json: bool = False,
        **kwargs,
    ) -> Dict[str, Any]:
        """
        Create multicast policy.

        Args:
            data: The policy configuration data
            vdom: Specify the Virtual Domain(s)
            action: Special action (e.g., 'move' with before/after for positioning)
            nkey: New key value for creation
            scope: Scope [global|vdom|both]
            **kwargs: Additional parameters

        Returns:
            API response dictionary
        """
        params = {}

        # Build params dict from provided arguments
        if action is not None:
            params["action"] = action
        if nkey is not None:
            params["nkey"] = nkey
        if scope is not None:
            params["scope"] = scope

        # Add any additional kwargs
        params.update(kwargs)

        return self._client.post(
            "cmdb", self.path, data=data, params=params, vdom=vdom, raw_json=raw_json
        )

    def put(
        self,
        mkey: Optional[Union[str, int]] = None,
        data: Dict[str, Any],
        vdom: Optional[str] = None,
        # Extended query parameters from Swagger spec
        action: Optional[str] = None,
        before: Optional[Union[str, int]] = None,
        after: Optional[Union[str, int]] = None,
        scope: Optional[str] = None,
        raw_json: bool = False,
        **kwargs,
    ) -> Dict[str, Any]:
        """
        Update multicast policy.

        Args:
            mkey: The policy ID (primary key)
            data: The updated policy configuration data
            vdom: Specify the Virtual Domain(s)
            action: Special action (e.g., 'move' to reposition policy)
            before: If action=move, specify ID to move before
            after: If action=move, specify ID to move after
            scope: Scope [global|vdom|both]
            **kwargs: Additional parameters

        Returns:
            API response dictionary
        """
        # Validate mkey
        if mkey is None:
            raise ValueError("mkey cannot be None")

        mkey_str = str(mkey)
        if not mkey_str:
            raise ValueError("mkey cannot be empty")

        params = {}

        # Build params dict from provided arguments
        if action is not None:
            params["action"] = action
        if before is not None:
            params["before"] = before
        if after is not None:
            params["after"] = after
        if scope is not None:
            params["scope"] = scope

        # Add any additional kwargs
        params.update(kwargs)

        return self._client.put(
            "cmdb",
            f"{self.path}/{encode_path_component(mkey)}" if mkey is not None else self.path,
            data=data,
            params=params,
            vdom=vdom,
            raw_json=raw_json,
        )

    def delete(
        self,
        mkey: Optional[Union[str, int]] = None,
        vdom: Optional[str] = None,
        # Extended query parameters from Swagger spec
        scope: Optional[str] = None,
        raw_json: bool = False,
        **kwargs,
    ) -> Dict[str, Any]:
        """
        Delete a multicast policy.

        Args:
            mkey: The policy ID (primary key)
            vdom: Specify the Virtual Domain(s)
            scope: Scope [global|vdom|both]
            **kwargs: Additional parameters

        Returns:
            API response dictionary
        """
        # Validate mkey
        if mkey is None:
            raise ValueError("mkey cannot be None")

        mkey_str = str(mkey)
        if not mkey_str:
            raise ValueError("mkey cannot be empty")

        params = {}

        # Build params dict from provided arguments
        if scope is not None:
            params["scope"] = scope

        # Add any additional kwargs
        params.update(kwargs)

        return self._client.delete(
            "cmdb", f"{self.path}/{encode_path_component(mkey)}" if mkey is not None else self.path, params=params, vdom=vdom, raw_json=raw_json
        )
