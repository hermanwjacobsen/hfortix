"""
FortiOS ippool6 API wrapper.
Provides access to /api/v2/cmdb/firewall/ippool6 endpoint.
"""

from typing import Any, Dict, List, Optional, Union

from hfortix.FortiOS.http_client import encode_path_component


class Ippool6:
    """
    Wrapper for firewall ippool6 API endpoint.

    Manages ippool6 configuration with full Swagger-spec parameter support.
    """

    def __init__(self, http_client: Any):
        """
        Initialize the Ippool6 wrapper.

        Args:
            http_client: The HTTP client for API communication
        """
        self._client = http_client
        self.path = "firewall/ippool6"


    def get(
        self,
        mkey: Optional[Union[str, int]] = None,
        attr: Optional[Any] = None,
        count: Optional[Any] = None,
        skip_to_datasource: Optional[Any] = None,
        acs: Optional[Any] = None,
        search: Optional[Any] = None,
        scope: Optional[Any] = None,
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
        Retrieve a specific ippool6 entry by its name.

        Args:
            mkey: The name (primary key)
            attr: Attribute name that references other table
            count: Maximum number of entries to return.
            skip_to_datasource: Skip to provided table's Nth entry. E.g {datasource: 'firewall.address
            acs: If true, returned result are in ascending order.
            search: If present, the objects will be filtered by the search value.
            scope: Scope [global|vdom|both*]
            datasource: Enable to include datasource information for each linked object.
            with_meta: Enable to include meta information about each object (type id, referen
            skip: Enable to call CLI skip operator to hide skipped properties.
            format: List of property names to include in results, separated by | (i.e. pol
            action: datasource: Return all applicable datasource entries for a specific at
            vdom: Specify the Virtual Domain(s) from which results are returned or chang
            **kwargs: Additional parameters

        Returns:
            API response dictionary with entry details
        """
        # Validate mkey
        if mkey is None:
            raise ValueError("mkey cannot be None")

        mkey_str = str(mkey)
        if not mkey_str:
            raise ValueError("mkey cannot be empty")

        params = {}

        if attr is not None:
            params["attr"] = attr
        if count is not None:
            params["count"] = count
        if skip_to_datasource is not None:
            params["skip_to_datasource"] = skip_to_datasource
        if acs is not None:
            params["acs"] = acs
        if search is not None:
            params["search"] = search
        if scope is not None:
            params["scope"] = scope
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
        if vdom is not None:
            params["vdom"] = vdom

        # Add any additional kwargs
        params.update(kwargs)

        # Extract vdom if present
        vdom = params.pop("vdom", None)

        return self._client.get(
            "cmdb", f"{self.path}/{encode_path_component(mkey)}" if mkey is not None else self.path, params=params, vdom=vdom, raw_json=raw_json
        )

    def post(
        self,
        payload_dict: Optional[Dict[str, Any]] = None,
        vdom: Optional[Any] = None,
        action: Optional[Any] = None,
        nkey: Optional[Any] = None,
        scope: Optional[Any] = None,
        add_nat46_route: Optional[str] = None,
        comments: Optional[str] = None,
        endip: Optional[str] = None,
        external_prefix: Optional[str] = None,
        internal_prefix: Optional[str] = None,
        name: Optional[str] = None,
        nat46: Optional[str] = None,
        startip: Optional[str] = None,
        type: Optional[str] = None,
        raw_json: bool = False,
        **kwargs,
    ) -> Dict[str, Any]:
        """
        Create ippool6 entry.

        Supports two usage patterns:
        1. Pass data dict: create(payload_dict={"key": "value"}, vdom="root")
        2. Pass kwargs: create(key="value", vdom="root")

        Args:
            payload_dict: The configuration data (optional if using kwargs)
            vdom: Specify the Virtual Domain(s) from which results are returned or chang
            action: If supported, an action can be specified.
            nkey: If *action=clone*, use *nkey* to specify the ID for the new resource t
            scope: Specify the Scope from which results are returned or changes are appli
            **kwargs: Additional parameters

        Body schema properties (can pass via data dict or as kwargs):

            add-nat46-route (string) (enum: ['disable', 'enable']):
                Enable/disable adding NAT46 route.
            comments (string) (max_len: 255):
                Comment.
            endip (string):
                Final IPv6 address (inclusive) in the range for the address ...
            external-prefix (string):
                External NPTv6 prefix length (32 - 64).
            internal-prefix (string):
                Internal NPTv6 prefix length (32 - 64).
            name (string) (max_len: 79):
                IPv6 IP pool name.
            nat46 (string) (enum: ['disable', 'enable']):
                Enable/disable NAT46.
            startip (string):
                First IPv6 address (inclusive) in the range for the address ...
            type (string) (enum: ['overload', 'nptv6']):
                Configure IPv6 pool type (overload or NPTv6).

        Returns:
            API response dictionary
        """
        # Build data from kwargs if not provided
        if payload_dict is None:
            payload_dict = {}
        if add_nat46_route is not None:
            payload_dict["add-nat46-route"] = add_nat46_route
        if comments is not None:
            payload_dict["comments"] = comments
        if endip is not None:
            payload_dict["endip"] = endip
        if external_prefix is not None:
            payload_dict["external-prefix"] = external_prefix
        if internal_prefix is not None:
            payload_dict["internal-prefix"] = internal_prefix
        if name is not None:
            payload_dict["name"] = name
        if nat46 is not None:
            payload_dict["nat46"] = nat46
        if startip is not None:
            payload_dict["startip"] = startip
        if type is not None:
            payload_dict["type"] = type

        params = {}

        if vdom is not None:
            params["vdom"] = vdom
        if action is not None:
            params["action"] = action
        if nkey is not None:
            params["nkey"] = nkey
        if scope is not None:
            params["scope"] = scope

        # Add any additional kwargs
        params.update(kwargs)

        # Extract vdom if present
        vdom = params.pop("vdom", None)

        return self._client.post(
            "cmdb", self.path, data=payload_dict, params=params, vdom=vdom, raw_json=raw_json
        )

    def put(
        self,
        mkey: Optional[Union[str, int]] = None,
        payload_dict: Optional[Dict[str, Any]] = None,
        vdom: Optional[Any] = None,
        action: Optional[Any] = None,
        before: Optional[Any] = None,
        after: Optional[Any] = None,
        scope: Optional[Any] = None,
        add_nat46_route: Optional[str] = None,
        comments: Optional[str] = None,
        endip: Optional[str] = None,
        external_prefix: Optional[str] = None,
        internal_prefix: Optional[str] = None,
        name: Optional[str] = None,
        nat46: Optional[str] = None,
        startip: Optional[str] = None,
        type: Optional[str] = None,
        raw_json: bool = False,
        **kwargs,
    ) -> Dict[str, Any]:
        """
        Update ippool6 entry.

        Supports two usage patterns:
        1. Pass data dict: update(mkey=123, payload_dict={"key": "value"}, vdom="root")
        2. Pass kwargs: update(mkey=123, key="value", vdom="root")

        Args:
            mkey: The name (primary key)
            payload_dict: The updated configuration data (optional if using kwargs)
            vdom: Specify the Virtual Domain(s) from which results are returned or chang
            action: If supported, an action can be specified.
            before: If *action=move*, use *before* to specify the ID of the resource that
            after: If *action=move*, use *after* to specify the ID of the resource that t
            scope: Specify the Scope from which results are returned or changes are appli
            **kwargs: Additional parameters

        Body schema properties (can pass via data dict or as kwargs):

            add-nat46-route (string) (enum: ['disable', 'enable']):
                Enable/disable adding NAT46 route.
            comments (string) (max_len: 255):
                Comment.
            endip (string):
                Final IPv6 address (inclusive) in the range for the address ...
            external-prefix (string):
                External NPTv6 prefix length (32 - 64).
            internal-prefix (string):
                Internal NPTv6 prefix length (32 - 64).
            name (string) (max_len: 79):
                IPv6 IP pool name.
            nat46 (string) (enum: ['disable', 'enable']):
                Enable/disable NAT46.
            startip (string):
                First IPv6 address (inclusive) in the range for the address ...
            type (string) (enum: ['overload', 'nptv6']):
                Configure IPv6 pool type (overload or NPTv6).

        Returns:
            API response dictionary
        """
        # Validate mkey
        if mkey is None:
            raise ValueError("mkey cannot be None")

        mkey_str = str(mkey)
        if not mkey_str:
            raise ValueError("mkey cannot be empty")

        # Build data from kwargs if not provided
        if payload_dict is None:
            payload_dict = {}
        if add_nat46_route is not None:
            payload_dict["add-nat46-route"] = add_nat46_route
        if comments is not None:
            payload_dict["comments"] = comments
        if endip is not None:
            payload_dict["endip"] = endip
        if external_prefix is not None:
            payload_dict["external-prefix"] = external_prefix
        if internal_prefix is not None:
            payload_dict["internal-prefix"] = internal_prefix
        if name is not None:
            payload_dict["name"] = name
        if nat46 is not None:
            payload_dict["nat46"] = nat46
        if startip is not None:
            payload_dict["startip"] = startip
        if type is not None:
            payload_dict["type"] = type

        params = {}

        if vdom is not None:
            params["vdom"] = vdom
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

        # Extract vdom if present
        vdom = params.pop("vdom", None)

        return self._client.put(
            "cmdb",
            f"{self.path}/{encode_path_component(mkey)}" if mkey is not None else self.path,
            data=payload_dict,
            params=params,
            vdom=vdom,
            raw_json=raw_json,
        )

    def delete(
        self,
        mkey: Optional[Union[str, int]] = None,
        vdom: Optional[Any] = None,
        scope: Optional[Any] = None,
        raw_json: bool = False,
        **kwargs,
    ) -> Dict[str, Any]:
        """
        Delete a ippool6 entry.

        Args:
            mkey: The name (primary key)
            vdom: Specify the Virtual Domain(s) from which results are returned or chang
            scope: Specify the Scope from which results are returned or changes are appli
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

        if vdom is not None:
            params["vdom"] = vdom
        if scope is not None:
            params["scope"] = scope

        # Add any additional kwargs
        params.update(kwargs)

        # Extract vdom if present
        vdom = params.pop("vdom", None)

        return self._client.delete(
            "cmdb", f"{self.path}/{encode_path_component(mkey)}" if mkey is not None else self.path, params=params, vdom=vdom, raw_json=raw_json
        )
