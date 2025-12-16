"""
FortiOS multicast-policy API wrapper.
Provides access to /api/v2/cmdb/firewall/multicast-policy endpoint.
"""

from typing import Any, Dict, List, Optional, Union


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

    def list(
        self,
        # Standard query parameters
        datasource: Optional[str] = None,
        with_meta: Optional[bool] = None,
        skip: Optional[bool] = None,
        format: Optional[str] = None,
        filter: Optional[str] = None,
        vdom: Optional[str] = None,
        # Extended query parameters from Swagger spec
        action: Optional[str] = None,
        count: Optional[int] = None,
        datasource_format: Optional[str] = None,
        exclude_default_values: Optional[bool] = None,
        key: Optional[str] = None,
        pattern: Optional[str] = None,
        primary_keys: Optional[bool] = None,
        scope: Optional[str] = None,
        skip_to: Optional[int] = None,
        start: Optional[int] = None,
        stat_items: Optional[bool] = None,
        unfiltered_count: Optional[bool] = None,
        with_contents_hash: Optional[bool] = None,
        raw_json: bool = False,
        **kwargs,
    ) -> Dict[str, Any]:
        """
        Retrieve a list of all multicast policies.

        Args:
            datasource: Enable to include datasource information
            with_meta: Enable to include meta information
            skip: Enable to call CLI skip operator
            format: List of property names to include in results
            filter: Filter the results
            vdom: Specify the Virtual Domain(s)
            action: Special action (e.g., 'datasource' to return all applicable datasource)
            count: Maximum number of entries to return
            datasource_format: Format for datasource
            exclude_default_values: Exclude default values from results
            key: Specific key to retrieve
            pattern: Pattern for matching
            primary_keys: Return only primary keys
            scope: Scope [global|vdom|both]
            skip_to: Skip to Nth entry
            start: Start index for pagination
            stat_items: Include statistics items
            unfiltered_count: Return unfiltered count
            with_contents_hash: Include contents hash
            **kwargs: Additional parameters

        Returns:
            API response dictionary with results list
        """
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
        if filter is not None:
            params["filter"] = filter
        if action is not None:
            params["action"] = action
        if count is not None:
            params["count"] = count
        if datasource_format is not None:
            params["datasource_format"] = datasource_format
        if exclude_default_values is not None:
            params["exclude-default-values"] = exclude_default_values
        if key is not None:
            params["key"] = key
        if pattern is not None:
            params["pattern"] = pattern
        if primary_keys is not None:
            params["primary_keys"] = primary_keys
        if scope is not None:
            params["scope"] = scope
        if skip_to is not None:
            params["skip_to"] = skip_to
        if start is not None:
            params["start"] = start
        if stat_items is not None:
            params["stat_items"] = stat_items
        if unfiltered_count is not None:
            params["unfiltered_count"] = unfiltered_count
        if with_contents_hash is not None:
            params["with_contents_hash"] = with_contents_hash

        # Add any additional kwargs
        params.update(kwargs)

        return self._client.get("cmdb", self.path, params=params, vdom=vdom, raw_json=raw_json)

    def get(
        self,
        mkey: Union[str, int],
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
            "cmdb", f"{self.path}/{mkey_str}", params=params, vdom=vdom, raw_json=raw_json
        )

    def create(
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
        Create a new multicast policy.

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

    def update(
        self,
        mkey: Union[str, int],
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
        Update an existing multicast policy.

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
            f"{self.path}/{mkey_str}",
            data=data,
            params=params,
            vdom=vdom,
            raw_json=raw_json,
        )

    def delete(
        self,
        mkey: Union[str, int],
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
            "cmdb", f"{self.path}/{mkey_str}", params=params, vdom=vdom, raw_json=raw_json
        )
