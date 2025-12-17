"""
FortiOS proxy-address API wrapper.
Provides access to /api/v2/cmdb/firewall/proxy-address endpoint.
"""

from typing import Any, Dict, List, Optional, Union

from hfortix.FortiOS.http_client import encode_path_component


class ProxyAddress:
    """
    Wrapper for firewall proxy-address API endpoint.

    Manages proxy-address configuration with full Swagger-spec parameter support.
    """

    def __init__(self, http_client: Any):
        """
        Initialize the ProxyAddress wrapper.

        Args:
            http_client: The HTTP client for API communication
        """
        self._client = http_client
        self.path = "firewall/proxy-address"


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
        Retrieve a specific proxy-address entry by its name.

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
        application: Optional[list] = None,
        case_sensitivity: Optional[str] = None,
        category: Optional[list] = None,
        color: Optional[int] = None,
        comment: Optional[str] = None,
        header: Optional[str] = None,
        header_group: Optional[list] = None,
        header_name: Optional[str] = None,
        host: Optional[str] = None,
        host_regex: Optional[str] = None,
        method: Optional[str] = None,
        name: Optional[str] = None,
        path: Optional[str] = None,
        query: Optional[str] = None,
        referrer: Optional[str] = None,
        tagging: Optional[list] = None,
        type: Optional[str] = None,
        ua: Optional[str] = None,
        ua_max_ver: Optional[str] = None,
        ua_min_ver: Optional[str] = None,
        uuid: Optional[str] = None,
        raw_json: bool = False,
        **kwargs,
    ) -> Dict[str, Any]:
        """
        Create proxy-address entry.

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

            application (list[object]):
                SaaS application.
            case-sensitivity (string) (enum: ['disable', 'enable']):
                Enable to make the pattern case sensitive.
            category (list[object]):
                FortiGuard category ID.
            color (integer) (range: 0-32):
                Integer value to determine the color of the icon in the GUI ...
            comment (string) (max_len: 255):
                Optional comments.
            header (string) (max_len: 255):
                HTTP header name as a regular expression.
            header-group (list[object]):
                HTTP header group.
            header-name (string) (max_len: 79):
                Name of HTTP header.
            host (string) (max_len: 79):
                Address object for the host.
            host-regex (string) (max_len: 255):
                Host name as a regular expression.
            method (string) (enum: ['get', 'post', 'put']):
                HTTP request methods to be used.
            name (string) (max_len: 79):
                Address name.
            path (string) (max_len: 255):
                URL path as a regular expression.
            query (string) (max_len: 255):
                Match the query part of the URL as a regular expression.
            referrer (string) (enum: ['enable', 'disable']):
                Enable/disable use of referrer field in the HTTP header to m...
            tagging (list[object]):
                Config object tagging.
            type (string) (enum: ['host-regex', 'url', 'category']):
                Proxy address type.
            ua (string) (enum: ['chrome', 'ms', 'firefox']):
                Names of browsers to be used as user agent.
            ua-max-ver (string) (max_len: 63):
                Maximum version of the user agent specified in dotted notati...
            ua-min-ver (string) (max_len: 63):
                Minimum version of the user agent specified in dotted notati...
            uuid (string):
                Universally Unique Identifier (UUID; automatically assigned ...

        Returns:
            API response dictionary
        """
        # Build data from kwargs if not provided
        if payload_dict is None:
            payload_dict = {}
        if application is not None:
            payload_dict["application"] = application
        if case_sensitivity is not None:
            payload_dict["case-sensitivity"] = case_sensitivity
        if category is not None:
            payload_dict["category"] = category
        if color is not None:
            payload_dict["color"] = color
        if comment is not None:
            payload_dict["comment"] = comment
        if header is not None:
            payload_dict["header"] = header
        if header_group is not None:
            payload_dict["header-group"] = header_group
        if header_name is not None:
            payload_dict["header-name"] = header_name
        if host is not None:
            payload_dict["host"] = host
        if host_regex is not None:
            payload_dict["host-regex"] = host_regex
        if method is not None:
            payload_dict["method"] = method
        if name is not None:
            payload_dict["name"] = name
        if path is not None:
            payload_dict["path"] = path
        if query is not None:
            payload_dict["query"] = query
        if referrer is not None:
            payload_dict["referrer"] = referrer
        if tagging is not None:
            payload_dict["tagging"] = tagging
        if type is not None:
            payload_dict["type"] = type
        if ua is not None:
            payload_dict["ua"] = ua
        if ua_max_ver is not None:
            payload_dict["ua-max-ver"] = ua_max_ver
        if ua_min_ver is not None:
            payload_dict["ua-min-ver"] = ua_min_ver
        if uuid is not None:
            payload_dict["uuid"] = uuid

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
        application: Optional[list] = None,
        case_sensitivity: Optional[str] = None,
        category: Optional[list] = None,
        color: Optional[int] = None,
        comment: Optional[str] = None,
        header: Optional[str] = None,
        header_group: Optional[list] = None,
        header_name: Optional[str] = None,
        host: Optional[str] = None,
        host_regex: Optional[str] = None,
        method: Optional[str] = None,
        name: Optional[str] = None,
        path: Optional[str] = None,
        query: Optional[str] = None,
        referrer: Optional[str] = None,
        tagging: Optional[list] = None,
        type: Optional[str] = None,
        ua: Optional[str] = None,
        ua_max_ver: Optional[str] = None,
        ua_min_ver: Optional[str] = None,
        uuid: Optional[str] = None,
        raw_json: bool = False,
        **kwargs,
    ) -> Dict[str, Any]:
        """
        Update proxy-address entry.

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

            application (list[object]):
                SaaS application.
            case-sensitivity (string) (enum: ['disable', 'enable']):
                Enable to make the pattern case sensitive.
            category (list[object]):
                FortiGuard category ID.
            color (integer) (range: 0-32):
                Integer value to determine the color of the icon in the GUI ...
            comment (string) (max_len: 255):
                Optional comments.
            header (string) (max_len: 255):
                HTTP header name as a regular expression.
            header-group (list[object]):
                HTTP header group.
            header-name (string) (max_len: 79):
                Name of HTTP header.
            host (string) (max_len: 79):
                Address object for the host.
            host-regex (string) (max_len: 255):
                Host name as a regular expression.
            method (string) (enum: ['get', 'post', 'put']):
                HTTP request methods to be used.
            name (string) (max_len: 79):
                Address name.
            path (string) (max_len: 255):
                URL path as a regular expression.
            query (string) (max_len: 255):
                Match the query part of the URL as a regular expression.
            referrer (string) (enum: ['enable', 'disable']):
                Enable/disable use of referrer field in the HTTP header to m...
            tagging (list[object]):
                Config object tagging.
            type (string) (enum: ['host-regex', 'url', 'category']):
                Proxy address type.
            ua (string) (enum: ['chrome', 'ms', 'firefox']):
                Names of browsers to be used as user agent.
            ua-max-ver (string) (max_len: 63):
                Maximum version of the user agent specified in dotted notati...
            ua-min-ver (string) (max_len: 63):
                Minimum version of the user agent specified in dotted notati...
            uuid (string):
                Universally Unique Identifier (UUID; automatically assigned ...

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
        if application is not None:
            payload_dict["application"] = application
        if case_sensitivity is not None:
            payload_dict["case-sensitivity"] = case_sensitivity
        if category is not None:
            payload_dict["category"] = category
        if color is not None:
            payload_dict["color"] = color
        if comment is not None:
            payload_dict["comment"] = comment
        if header is not None:
            payload_dict["header"] = header
        if header_group is not None:
            payload_dict["header-group"] = header_group
        if header_name is not None:
            payload_dict["header-name"] = header_name
        if host is not None:
            payload_dict["host"] = host
        if host_regex is not None:
            payload_dict["host-regex"] = host_regex
        if method is not None:
            payload_dict["method"] = method
        if name is not None:
            payload_dict["name"] = name
        if path is not None:
            payload_dict["path"] = path
        if query is not None:
            payload_dict["query"] = query
        if referrer is not None:
            payload_dict["referrer"] = referrer
        if tagging is not None:
            payload_dict["tagging"] = tagging
        if type is not None:
            payload_dict["type"] = type
        if ua is not None:
            payload_dict["ua"] = ua
        if ua_max_ver is not None:
            payload_dict["ua-max-ver"] = ua_max_ver
        if ua_min_ver is not None:
            payload_dict["ua-min-ver"] = ua_min_ver
        if uuid is not None:
            payload_dict["uuid"] = uuid

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
        Delete a proxy-address entry.

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
