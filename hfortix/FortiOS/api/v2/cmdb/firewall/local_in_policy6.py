"""
FortiOS local-in-policy6 API wrapper.
Provides access to /api/v2/cmdb/firewall/local-in-policy6 endpoint.
"""

from typing import Any, Dict, List, Optional, Union

from hfortix.FortiOS.http_client import encode_path_component


class LocalInPolicy6:
    """
    Wrapper for firewall local-in-policy6 API endpoint.

    Manages local-in-policy6 configuration with full Swagger-spec parameter support.
    """

    def __init__(self, http_client: Any):
        """
        Initialize the LocalInPolicy6 wrapper.

        Args:
            http_client: The HTTP client for API communication
        """
        self._client = http_client
        self.path = "firewall/local-in-policy6"

    def list(
        self,
        datasource: Optional[Any] = None,
        start: Optional[Any] = None,
        count: Optional[Any] = None,
        skip_to: Optional[Any] = None,
        with_meta: Optional[Any] = None,
        with_contents_hash: Optional[Any] = None,
        skip: Optional[Any] = None,
        format: Optional[Any] = None,
        filter: Optional[Any] = None,
        key: Optional[Any] = None,
        pattern: Optional[Any] = None,
        scope: Optional[Any] = None,
        exclude_default_values: Optional[Any] = None,
        datasource_format: Optional[Any] = None,
        unfiltered_count: Optional[Any] = None,
        stat_items: Optional[Any] = None,
        primary_keys: Optional[Any] = None,
        action: Optional[Any] = None,
        vdom: Optional[Any] = None,
        raw_json: bool = False,
        **kwargs,
    ) -> Dict[str, Any]:
        """
        Retrieve a list of all local-in-policy6 entries.

        Args:
            datasource: Enable to include datasource information for each linked object.
            start: Starting entry index.
            count: Maximum number of entries to return.
            skip_to: Skip to Nth CMDB entry.
            with_meta: Enable to include meta information about each object (type id, referen
            with_contents_hash: Enable to include a checksum of each object's contents.
            skip: Enable to call CLI skip operator to hide skipped properties.
            format: List of property names to include in results, separated by | (i.e. pol
            filter: Filtering multiple key/value pairs
            key: If present, objects will be filtered on property with this name.
            pattern: If present, objects will be filtered on property with this value.
            scope: Scope [global|vdom|both*]
            exclude_default_values: Exclude properties/objects with default value
            datasource_format: A map of datasources to a string of attributes, separated by | (ie: po
            unfiltered_count: Maximum number of unfiltered entries to interate through.
            stat_items: Items to count occurrence in entire response (multiple items should be
            primary_keys: The primary key to find indexes for.
            action: default: Return the CLI default values for entire CLI tree.
            vdom: Specify the Virtual Domain(s) from which results are returned or chang
            **kwargs: Additional parameters

        Returns:
            API response dictionary with results list
        """
        params = {}

        if datasource is not None:
            params["datasource"] = datasource
        if start is not None:
            params["start"] = start
        if count is not None:
            params["count"] = count
        if skip_to is not None:
            params["skip_to"] = skip_to
        if with_meta is not None:
            params["with_meta"] = with_meta
        if with_contents_hash is not None:
            params["with_contents_hash"] = with_contents_hash
        if skip is not None:
            params["skip"] = skip
        if format is not None:
            params["format"] = format
        if filter is not None:
            params["filter"] = filter
        if key is not None:
            params["key"] = key
        if pattern is not None:
            params["pattern"] = pattern
        if scope is not None:
            params["scope"] = scope
        if exclude_default_values is not None:
            params["exclude-default-values"] = exclude_default_values
        if datasource_format is not None:
            params["datasource_format"] = datasource_format
        if unfiltered_count is not None:
            params["unfiltered_count"] = unfiltered_count
        if stat_items is not None:
            params["stat-items"] = stat_items
        if primary_keys is not None:
            params["primary_keys"] = primary_keys
        if action is not None:
            params["action"] = action
        if vdom is not None:
            params["vdom"] = vdom

        # Add any additional kwargs
        params.update(kwargs)

        # Extract vdom if present
        vdom = params.pop("vdom", None)

        return self._client.get("cmdb", self.path, params=params, vdom=vdom, raw_json=raw_json)

    def get(
        self,
        mkey: Union[str, int],
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
        Retrieve a specific local-in-policy6 entry by its policyid.

        Args:
            mkey: The policyid (primary key)
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
            "cmdb", f"{self.path}/{mkey_str}", params=params, vdom=vdom, raw_json=raw_json
        )

    def post(
        self,
        payload_dict: Optional[Dict[str, Any]] = None,
        vdom: Optional[Any] = None,
        action: Optional[Any] = None,
        nkey: Optional[Any] = None,
        scope: Optional[Any] = None,
        comments: Optional[str] = None,
        dstaddr: Optional[list] = None,
        dstaddr_negate: Optional[str] = None,
        internet_service6_src: Optional[str] = None,
        internet_service6_src_custom: Optional[list] = None,
        internet_service6_src_custom_group: Optional[list] = None,
        internet_service6_src_fortiguard: Optional[list] = None,
        internet_service6_src_group: Optional[list] = None,
        internet_service6_src_name: Optional[list] = None,
        internet_service6_src_negate: Optional[str] = None,
        intf: Optional[list] = None,
        logtraffic: Optional[str] = None,
        policyid: Optional[int] = None,
        schedule: Optional[str] = None,
        service: Optional[list] = None,
        service_negate: Optional[str] = None,
        srcaddr: Optional[list] = None,
        srcaddr_negate: Optional[str] = None,
        status: Optional[str] = None,
        uuid: Optional[str] = None,
        virtual_patch: Optional[str] = None,
        raw_json: bool = False,
        **kwargs,
    ) -> Dict[str, Any]:
        """
        Create local-in-policy6 entry.

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

            action (string) (enum: ['accept', 'deny']):
                Action performed on traffic matching the policy (default = d...
            comments (string) (max_len: 1023):
                Comment.
            dstaddr (list[object]):
                Destination address object from available options.
            dstaddr-negate (string) (enum: ['enable', 'disable']):
                When enabled dstaddr specifies what the destination address ...
            internet-service6-src (string) (enum: ['enable', 'disable']):
                Enable/disable use of IPv6 Internet Services in source for t...
            internet-service6-src-custom (list[object]):
                Custom IPv6 Internet Service source name.
            internet-service6-src-custom-group (list[object]):
                Custom Internet Service6 source group name.
            internet-service6-src-fortiguard (list[object]):
                FortiGuard IPv6 Internet Service source name.
            internet-service6-src-group (list[object]):
                Internet Service6 source group name.
            internet-service6-src-name (list[object]):
                IPv6 Internet Service source name.
            internet-service6-src-negate (string) (enum: ['enable', 'disable']):
                When enabled internet-service6-src specifies what the servic...
            intf (list[object]):
                Incoming interface name from available options.
            logtraffic (string) (enum: ['enable', 'disable']):
                Enable/disable local-in traffic logging.
            policyid (integer) (range: 0-4294967295):
                User defined local in policy ID.
            schedule (string) (max_len: 35):
                Schedule object from available options.
            service (list[object]):
                Service object from available options. Separate names with a...
            service-negate (string) (enum: ['enable', 'disable']):
                When enabled service specifies what the service must NOT be.
            srcaddr (list[object]):
                Source address object from available options.
            srcaddr-negate (string) (enum: ['enable', 'disable']):
                When enabled srcaddr specifies what the source address must ...
            status (string) (enum: ['enable', 'disable']):
                Enable/disable this local-in policy.
            uuid (string):
                Universally Unique Identifier (UUID; automatically assigned ...
            virtual-patch (string) (enum: ['enable', 'disable']):
                Enable/disable the virtual patching feature.

        Returns:
            API response dictionary
        """
        # Build data from kwargs if not provided
        if payload_dict is None:
            payload_dict = {}
        if action is not None:
            payload_dict["action"] = action
        if comments is not None:
            payload_dict["comments"] = comments
        if dstaddr is not None:
            payload_dict["dstaddr"] = dstaddr
        if dstaddr_negate is not None:
            payload_dict["dstaddr-negate"] = dstaddr_negate
        if internet_service6_src is not None:
            payload_dict["internet-service6-src"] = internet_service6_src
        if internet_service6_src_custom is not None:
            payload_dict["internet-service6-src-custom"] = internet_service6_src_custom
        if internet_service6_src_custom_group is not None:
            payload_dict["internet-service6-src-custom-group"] = internet_service6_src_custom_group
        if internet_service6_src_fortiguard is not None:
            payload_dict["internet-service6-src-fortiguard"] = internet_service6_src_fortiguard
        if internet_service6_src_group is not None:
            payload_dict["internet-service6-src-group"] = internet_service6_src_group
        if internet_service6_src_name is not None:
            payload_dict["internet-service6-src-name"] = internet_service6_src_name
        if internet_service6_src_negate is not None:
            payload_dict["internet-service6-src-negate"] = internet_service6_src_negate
        if intf is not None:
            payload_dict["intf"] = intf
        if logtraffic is not None:
            payload_dict["logtraffic"] = logtraffic
        if policyid is not None:
            payload_dict["policyid"] = policyid
        if schedule is not None:
            payload_dict["schedule"] = schedule
        if service is not None:
            payload_dict["service"] = service
        if service_negate is not None:
            payload_dict["service-negate"] = service_negate
        if srcaddr is not None:
            payload_dict["srcaddr"] = srcaddr
        if srcaddr_negate is not None:
            payload_dict["srcaddr-negate"] = srcaddr_negate
        if status is not None:
            payload_dict["status"] = status
        if uuid is not None:
            payload_dict["uuid"] = uuid
        if virtual_patch is not None:
            payload_dict["virtual-patch"] = virtual_patch

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
        mkey: Union[str, int],
        payload_dict: Optional[Dict[str, Any]] = None,
        vdom: Optional[Any] = None,
        action: Optional[Any] = None,
        before: Optional[Any] = None,
        after: Optional[Any] = None,
        scope: Optional[Any] = None,
        comments: Optional[str] = None,
        dstaddr: Optional[list] = None,
        dstaddr_negate: Optional[str] = None,
        internet_service6_src: Optional[str] = None,
        internet_service6_src_custom: Optional[list] = None,
        internet_service6_src_custom_group: Optional[list] = None,
        internet_service6_src_fortiguard: Optional[list] = None,
        internet_service6_src_group: Optional[list] = None,
        internet_service6_src_name: Optional[list] = None,
        internet_service6_src_negate: Optional[str] = None,
        intf: Optional[list] = None,
        logtraffic: Optional[str] = None,
        policyid: Optional[int] = None,
        schedule: Optional[str] = None,
        service: Optional[list] = None,
        service_negate: Optional[str] = None,
        srcaddr: Optional[list] = None,
        srcaddr_negate: Optional[str] = None,
        status: Optional[str] = None,
        uuid: Optional[str] = None,
        virtual_patch: Optional[str] = None,
        raw_json: bool = False,
        **kwargs,
    ) -> Dict[str, Any]:
        """
        Update local-in-policy6 entry.

        Supports two usage patterns:
        1. Pass data dict: update(mkey=123, payload_dict={"key": "value"}, vdom="root")
        2. Pass kwargs: update(mkey=123, key="value", vdom="root")

        Args:
            mkey: The policyid (primary key)
            payload_dict: The updated configuration data (optional if using kwargs)
            vdom: Specify the Virtual Domain(s) from which results are returned or chang
            action: If supported, an action can be specified.
            before: If *action=move*, use *before* to specify the ID of the resource that
            after: If *action=move*, use *after* to specify the ID of the resource that t
            scope: Specify the Scope from which results are returned or changes are appli
            **kwargs: Additional parameters

        Body schema properties (can pass via data dict or as kwargs):

            action (string) (enum: ['accept', 'deny']):
                Action performed on traffic matching the policy (default = d...
            comments (string) (max_len: 1023):
                Comment.
            dstaddr (list[object]):
                Destination address object from available options.
            dstaddr-negate (string) (enum: ['enable', 'disable']):
                When enabled dstaddr specifies what the destination address ...
            internet-service6-src (string) (enum: ['enable', 'disable']):
                Enable/disable use of IPv6 Internet Services in source for t...
            internet-service6-src-custom (list[object]):
                Custom IPv6 Internet Service source name.
            internet-service6-src-custom-group (list[object]):
                Custom Internet Service6 source group name.
            internet-service6-src-fortiguard (list[object]):
                FortiGuard IPv6 Internet Service source name.
            internet-service6-src-group (list[object]):
                Internet Service6 source group name.
            internet-service6-src-name (list[object]):
                IPv6 Internet Service source name.
            internet-service6-src-negate (string) (enum: ['enable', 'disable']):
                When enabled internet-service6-src specifies what the servic...
            intf (list[object]):
                Incoming interface name from available options.
            logtraffic (string) (enum: ['enable', 'disable']):
                Enable/disable local-in traffic logging.
            policyid (integer) (range: 0-4294967295):
                User defined local in policy ID.
            schedule (string) (max_len: 35):
                Schedule object from available options.
            service (list[object]):
                Service object from available options. Separate names with a...
            service-negate (string) (enum: ['enable', 'disable']):
                When enabled service specifies what the service must NOT be.
            srcaddr (list[object]):
                Source address object from available options.
            srcaddr-negate (string) (enum: ['enable', 'disable']):
                When enabled srcaddr specifies what the source address must ...
            status (string) (enum: ['enable', 'disable']):
                Enable/disable this local-in policy.
            uuid (string):
                Universally Unique Identifier (UUID; automatically assigned ...
            virtual-patch (string) (enum: ['enable', 'disable']):
                Enable/disable the virtual patching feature.

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
        if action is not None:
            payload_dict["action"] = action
        if comments is not None:
            payload_dict["comments"] = comments
        if dstaddr is not None:
            payload_dict["dstaddr"] = dstaddr
        if dstaddr_negate is not None:
            payload_dict["dstaddr-negate"] = dstaddr_negate
        if internet_service6_src is not None:
            payload_dict["internet-service6-src"] = internet_service6_src
        if internet_service6_src_custom is not None:
            payload_dict["internet-service6-src-custom"] = internet_service6_src_custom
        if internet_service6_src_custom_group is not None:
            payload_dict["internet-service6-src-custom-group"] = internet_service6_src_custom_group
        if internet_service6_src_fortiguard is not None:
            payload_dict["internet-service6-src-fortiguard"] = internet_service6_src_fortiguard
        if internet_service6_src_group is not None:
            payload_dict["internet-service6-src-group"] = internet_service6_src_group
        if internet_service6_src_name is not None:
            payload_dict["internet-service6-src-name"] = internet_service6_src_name
        if internet_service6_src_negate is not None:
            payload_dict["internet-service6-src-negate"] = internet_service6_src_negate
        if intf is not None:
            payload_dict["intf"] = intf
        if logtraffic is not None:
            payload_dict["logtraffic"] = logtraffic
        if policyid is not None:
            payload_dict["policyid"] = policyid
        if schedule is not None:
            payload_dict["schedule"] = schedule
        if service is not None:
            payload_dict["service"] = service
        if service_negate is not None:
            payload_dict["service-negate"] = service_negate
        if srcaddr is not None:
            payload_dict["srcaddr"] = srcaddr
        if srcaddr_negate is not None:
            payload_dict["srcaddr-negate"] = srcaddr_negate
        if status is not None:
            payload_dict["status"] = status
        if uuid is not None:
            payload_dict["uuid"] = uuid
        if virtual_patch is not None:
            payload_dict["virtual-patch"] = virtual_patch

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
            f"{self.path}/{mkey_str}",
            data=payload_dict,
            params=params,
            vdom=vdom,
            raw_json=raw_json,
        )

    def delete(
        self,
        mkey: Union[str, int],
        vdom: Optional[Any] = None,
        scope: Optional[Any] = None,
        raw_json: bool = False,
        **kwargs,
    ) -> Dict[str, Any]:
        """
        Delete a local-in-policy6 entry.

        Args:
            mkey: The policyid (primary key)
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
            "cmdb", f"{self.path}/{mkey_str}", params=params, vdom=vdom, raw_json=raw_json
        )
