"""
FortiOS ippool API wrapper.
Provides access to /api/v2/cmdb/firewall/ippool endpoint.
"""

from typing import Any, Dict, List, Optional, Union

from hfortix.FortiOS.http_client import encode_path_component


class Ippool:
    """
    Wrapper for firewall ippool API endpoint.

    Manages ippool configuration with full Swagger-spec parameter support.
    """

    def __init__(self, http_client: Any):
        """
        Initialize the Ippool wrapper.

        Args:
            http_client: The HTTP client for API communication
        """
        self._client = http_client
        self.path = "firewall/ippool"

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
        Retrieve a list of all ippool entries.

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
        Retrieve a specific ippool entry by its name.

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
            "cmdb", f"{self.path}/{mkey_str}", params=params, vdom=vdom, raw_json=raw_json
        )

    def create(
        self,
        payload_dict: Optional[Dict[str, Any]] = None,
        vdom: Optional[Any] = None,
        action: Optional[Any] = None,
        nkey: Optional[Any] = None,
        scope: Optional[Any] = None,
        add_nat64_route: Optional[str] = None,
        arp_intf: Optional[str] = None,
        arp_reply: Optional[str] = None,
        associated_interface: Optional[str] = None,
        block_size: Optional[int] = None,
        client_prefix_length: Optional[int] = None,
        comments: Optional[str] = None,
        endip: Optional[str] = None,
        endport: Optional[int] = None,
        icmp_session_quota: Optional[int] = None,
        name: Optional[str] = None,
        nat64: Optional[str] = None,
        num_blocks_per_user: Optional[int] = None,
        pba_interim_log: Optional[int] = None,
        pba_timeout: Optional[int] = None,
        permit_any_host: Optional[str] = None,
        port_per_user: Optional[int] = None,
        privileged_port_use_pba: Optional[str] = None,
        source_endip: Optional[str] = None,
        source_prefix6: Optional[str] = None,
        source_startip: Optional[str] = None,
        startip: Optional[str] = None,
        startport: Optional[int] = None,
        subnet_broadcast_in_ippool: Optional[str] = None,
        tcp_session_quota: Optional[int] = None,
        type: Optional[str] = None,
        udp_session_quota: Optional[int] = None,
        raw_json: bool = False,
        **kwargs,
    ) -> Dict[str, Any]:
        """
        Create a new ippool entry.

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

            add-nat64-route (string) (enum: ['disable', 'enable']):
                Enable/disable adding NAT64 route.
            arp-intf (string) (max_len: 15):
                Select an interface from available options that will reply t...
            arp-reply (string) (enum: ['disable', 'enable']):
                Enable/disable replying to ARP requests when an IP Pool is a...
            associated-interface (string) (max_len: 15):
                Associated interface name.
            block-size (integer) (range: 64-4096):
                Number of addresses in a block (64 - 4096, default = 128).
            client-prefix-length (integer) (range: 1-128):
                Subnet length of a single deterministic NAT64 client (1 - 12...
            comments (string) (max_len: 255):
                Comment.
            endip (string):
                Final IPv4 address (inclusive) in the range for the address ...
            endport (integer) (range: 1024-65535):
                Final port number (inclusive) in the range for the address p...
            icmp-session-quota (integer) (range: 0-2097000):
                Maximum number of concurrent ICMP sessions allowed per clien...
            name (string) (max_len: 79):
                IP pool name.
            nat64 (string) (enum: ['disable', 'enable']):
                Enable/disable NAT64.
            num-blocks-per-user (integer) (range: 1-128):
                Number of addresses blocks that can be used by a user (1 to ...
            pba-interim-log (integer) (range: 600-86400):
                Port block allocation interim logging interval (600 - 86400 ...
            pba-timeout (integer) (range: 3-86400):
                Port block allocation timeout (seconds).
            permit-any-host (string) (enum: ['disable', 'enable']):
                Enable/disable fullcone NAT. Accept UDP packets from any hos...
            port-per-user (integer) (range: 32-60417):
                Number of port for each user (32 - 60416, default = 0, which...
            privileged-port-use-pba (string) (enum: ['disable', 'enable']):
                Enable/disable selection of the external port from the port ...
            source-endip (string):
                Final IPv4 address (inclusive) in the range of the source ad...
            source-prefix6 (string):
                Source IPv6 network to be translated (format = xxxx:xxxx:xxx...
            source-startip (string):
                First IPv4 address (inclusive) in the range of the source ad...
            startip (string):
                First IPv4 address (inclusive) in the range for the address ...
            startport (integer) (range: 1024-65535):
                First port number (inclusive) in the range for the address p...
            subnet-broadcast-in-ippool (string) (enum: ['disable']):
                Enable/disable inclusion of the subnetwork address and broad...
            tcp-session-quota (integer) (range: 0-2097000):
                Maximum number of concurrent TCP sessions allowed per client...
            type (string) (enum: ['overload', 'one-to-one', 'fixed-port-range']):
                IP pool type: overload, one-to-one, fixed-port-range, port-b...
            udp-session-quota (integer) (range: 0-2097000):
                Maximum number of concurrent UDP sessions allowed per client...

        Returns:
            API response dictionary
        """
        # Build data from kwargs if not provided
        if payload_dict is None:
            payload_dict = {}
        if add_nat64_route is not None:
            payload_dict["add-nat64-route"] = add_nat64_route
        if arp_intf is not None:
            payload_dict["arp-intf"] = arp_intf
        if arp_reply is not None:
            payload_dict["arp-reply"] = arp_reply
        if associated_interface is not None:
            payload_dict["associated-interface"] = associated_interface
        if block_size is not None:
            payload_dict["block-size"] = block_size
        if client_prefix_length is not None:
            payload_dict["client-prefix-length"] = client_prefix_length
        if comments is not None:
            payload_dict["comments"] = comments
        if endip is not None:
            payload_dict["endip"] = endip
        if endport is not None:
            payload_dict["endport"] = endport
        if icmp_session_quota is not None:
            payload_dict["icmp-session-quota"] = icmp_session_quota
        if name is not None:
            payload_dict["name"] = name
        if nat64 is not None:
            payload_dict["nat64"] = nat64
        if num_blocks_per_user is not None:
            payload_dict["num-blocks-per-user"] = num_blocks_per_user
        if pba_interim_log is not None:
            payload_dict["pba-interim-log"] = pba_interim_log
        if pba_timeout is not None:
            payload_dict["pba-timeout"] = pba_timeout
        if permit_any_host is not None:
            payload_dict["permit-any-host"] = permit_any_host
        if port_per_user is not None:
            payload_dict["port-per-user"] = port_per_user
        if privileged_port_use_pba is not None:
            payload_dict["privileged-port-use-pba"] = privileged_port_use_pba
        if source_endip is not None:
            payload_dict["source-endip"] = source_endip
        if source_prefix6 is not None:
            payload_dict["source-prefix6"] = source_prefix6
        if source_startip is not None:
            payload_dict["source-startip"] = source_startip
        if startip is not None:
            payload_dict["startip"] = startip
        if startport is not None:
            payload_dict["startport"] = startport
        if subnet_broadcast_in_ippool is not None:
            payload_dict["subnet-broadcast-in-ippool"] = subnet_broadcast_in_ippool
        if tcp_session_quota is not None:
            payload_dict["tcp-session-quota"] = tcp_session_quota
        if type is not None:
            payload_dict["type"] = type
        if udp_session_quota is not None:
            payload_dict["udp-session-quota"] = udp_session_quota

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

    def update(
        self,
        mkey: Union[str, int],
        payload_dict: Optional[Dict[str, Any]] = None,
        vdom: Optional[Any] = None,
        action: Optional[Any] = None,
        before: Optional[Any] = None,
        after: Optional[Any] = None,
        scope: Optional[Any] = None,
        add_nat64_route: Optional[str] = None,
        arp_intf: Optional[str] = None,
        arp_reply: Optional[str] = None,
        associated_interface: Optional[str] = None,
        block_size: Optional[int] = None,
        client_prefix_length: Optional[int] = None,
        comments: Optional[str] = None,
        endip: Optional[str] = None,
        endport: Optional[int] = None,
        icmp_session_quota: Optional[int] = None,
        name: Optional[str] = None,
        nat64: Optional[str] = None,
        num_blocks_per_user: Optional[int] = None,
        pba_interim_log: Optional[int] = None,
        pba_timeout: Optional[int] = None,
        permit_any_host: Optional[str] = None,
        port_per_user: Optional[int] = None,
        privileged_port_use_pba: Optional[str] = None,
        source_endip: Optional[str] = None,
        source_prefix6: Optional[str] = None,
        source_startip: Optional[str] = None,
        startip: Optional[str] = None,
        startport: Optional[int] = None,
        subnet_broadcast_in_ippool: Optional[str] = None,
        tcp_session_quota: Optional[int] = None,
        type: Optional[str] = None,
        udp_session_quota: Optional[int] = None,
        raw_json: bool = False,
        **kwargs,
    ) -> Dict[str, Any]:
        """
        Update an existing ippool entry.

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

            add-nat64-route (string) (enum: ['disable', 'enable']):
                Enable/disable adding NAT64 route.
            arp-intf (string) (max_len: 15):
                Select an interface from available options that will reply t...
            arp-reply (string) (enum: ['disable', 'enable']):
                Enable/disable replying to ARP requests when an IP Pool is a...
            associated-interface (string) (max_len: 15):
                Associated interface name.
            block-size (integer) (range: 64-4096):
                Number of addresses in a block (64 - 4096, default = 128).
            client-prefix-length (integer) (range: 1-128):
                Subnet length of a single deterministic NAT64 client (1 - 12...
            comments (string) (max_len: 255):
                Comment.
            endip (string):
                Final IPv4 address (inclusive) in the range for the address ...
            endport (integer) (range: 1024-65535):
                Final port number (inclusive) in the range for the address p...
            icmp-session-quota (integer) (range: 0-2097000):
                Maximum number of concurrent ICMP sessions allowed per clien...
            name (string) (max_len: 79):
                IP pool name.
            nat64 (string) (enum: ['disable', 'enable']):
                Enable/disable NAT64.
            num-blocks-per-user (integer) (range: 1-128):
                Number of addresses blocks that can be used by a user (1 to ...
            pba-interim-log (integer) (range: 600-86400):
                Port block allocation interim logging interval (600 - 86400 ...
            pba-timeout (integer) (range: 3-86400):
                Port block allocation timeout (seconds).
            permit-any-host (string) (enum: ['disable', 'enable']):
                Enable/disable fullcone NAT. Accept UDP packets from any hos...
            port-per-user (integer) (range: 32-60417):
                Number of port for each user (32 - 60416, default = 0, which...
            privileged-port-use-pba (string) (enum: ['disable', 'enable']):
                Enable/disable selection of the external port from the port ...
            source-endip (string):
                Final IPv4 address (inclusive) in the range of the source ad...
            source-prefix6 (string):
                Source IPv6 network to be translated (format = xxxx:xxxx:xxx...
            source-startip (string):
                First IPv4 address (inclusive) in the range of the source ad...
            startip (string):
                First IPv4 address (inclusive) in the range for the address ...
            startport (integer) (range: 1024-65535):
                First port number (inclusive) in the range for the address p...
            subnet-broadcast-in-ippool (string) (enum: ['disable']):
                Enable/disable inclusion of the subnetwork address and broad...
            tcp-session-quota (integer) (range: 0-2097000):
                Maximum number of concurrent TCP sessions allowed per client...
            type (string) (enum: ['overload', 'one-to-one', 'fixed-port-range']):
                IP pool type: overload, one-to-one, fixed-port-range, port-b...
            udp-session-quota (integer) (range: 0-2097000):
                Maximum number of concurrent UDP sessions allowed per client...

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
        if add_nat64_route is not None:
            payload_dict["add-nat64-route"] = add_nat64_route
        if arp_intf is not None:
            payload_dict["arp-intf"] = arp_intf
        if arp_reply is not None:
            payload_dict["arp-reply"] = arp_reply
        if associated_interface is not None:
            payload_dict["associated-interface"] = associated_interface
        if block_size is not None:
            payload_dict["block-size"] = block_size
        if client_prefix_length is not None:
            payload_dict["client-prefix-length"] = client_prefix_length
        if comments is not None:
            payload_dict["comments"] = comments
        if endip is not None:
            payload_dict["endip"] = endip
        if endport is not None:
            payload_dict["endport"] = endport
        if icmp_session_quota is not None:
            payload_dict["icmp-session-quota"] = icmp_session_quota
        if name is not None:
            payload_dict["name"] = name
        if nat64 is not None:
            payload_dict["nat64"] = nat64
        if num_blocks_per_user is not None:
            payload_dict["num-blocks-per-user"] = num_blocks_per_user
        if pba_interim_log is not None:
            payload_dict["pba-interim-log"] = pba_interim_log
        if pba_timeout is not None:
            payload_dict["pba-timeout"] = pba_timeout
        if permit_any_host is not None:
            payload_dict["permit-any-host"] = permit_any_host
        if port_per_user is not None:
            payload_dict["port-per-user"] = port_per_user
        if privileged_port_use_pba is not None:
            payload_dict["privileged-port-use-pba"] = privileged_port_use_pba
        if source_endip is not None:
            payload_dict["source-endip"] = source_endip
        if source_prefix6 is not None:
            payload_dict["source-prefix6"] = source_prefix6
        if source_startip is not None:
            payload_dict["source-startip"] = source_startip
        if startip is not None:
            payload_dict["startip"] = startip
        if startport is not None:
            payload_dict["startport"] = startport
        if subnet_broadcast_in_ippool is not None:
            payload_dict["subnet-broadcast-in-ippool"] = subnet_broadcast_in_ippool
        if tcp_session_quota is not None:
            payload_dict["tcp-session-quota"] = tcp_session_quota
        if type is not None:
            payload_dict["type"] = type
        if udp_session_quota is not None:
            payload_dict["udp-session-quota"] = udp_session_quota

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
        Delete a ippool entry.

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
            "cmdb", f"{self.path}/{mkey_str}", params=params, vdom=vdom, raw_json=raw_json
        )
