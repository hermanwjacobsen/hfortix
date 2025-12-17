"""
FortiOS ldb-monitor API wrapper.
Provides access to /api/v2/cmdb/firewall/ldb-monitor endpoint.
"""

from typing import Any, Dict, List, Optional, Union

from hfortix.FortiOS.http_client import encode_path_component


class LdbMonitor:
    """
    Wrapper for firewall ldb-monitor API endpoint.

    Manages ldb-monitor configuration with full Swagger-spec parameter support.
    """

    def __init__(self, http_client: Any):
        """
        Initialize the LdbMonitor wrapper.

        Args:
            http_client: The HTTP client for API communication
        """
        self._client = http_client
        self.path = "firewall/ldb-monitor"

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
        Retrieve a list of all ldb-monitor entries.

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
        Retrieve a specific ldb-monitor entry by its name.

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
        dns_match_ip: Optional[str] = None,
        dns_protocol: Optional[str] = None,
        dns_request_domain: Optional[str] = None,
        http_get: Optional[str] = None,
        http_match: Optional[str] = None,
        http_max_redirects: Optional[int] = None,
        interval: Optional[int] = None,
        name: Optional[str] = None,
        port: Optional[int] = None,
        retry: Optional[int] = None,
        src_ip: Optional[str] = None,
        timeout: Optional[int] = None,
        type: Optional[str] = None,
        raw_json: bool = False,
        **kwargs,
    ) -> Dict[str, Any]:
        """
        Create a new ldb-monitor entry.

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

            dns-match-ip (string):
                Response IP expected from DNS server.
            dns-protocol (string) (enum: ['udp', 'tcp']):
                Select the protocol used by the DNS health check monitor to ...
            dns-request-domain (string) (max_len: 255):
                Fully qualified domain name to resolve for the DNS probe.
            http-get (string) (max_len: 255):
                Request URI used to send a GET request to check the health o...
            http-match (string) (max_len: 255):
                String to match the value expected in response to an HTTP-GE...
            http-max-redirects (integer) (range: 0-5):
                The maximum number of HTTP redirects to be allowed (0 - 5, d...
            interval (integer) (range: 5-65535):
                Time between health checks (5 - 65535 sec, default = 10).
            name (string) (max_len: 35):
                Monitor name.
            port (integer) (range: 0-65535):
                Service port used to perform the health check. If 0, health ...
            retry (integer) (range: 1-255):
                Number health check attempts before the server is considered...
            src-ip (string):
                Source IP for ldb-monitor.
            timeout (integer) (range: 1-255):
                Time to wait to receive response to a health check from a se...
            type (string) (enum: ['ping', 'tcp', 'http']):
                Select the Monitor type used by the health check monitor to ...

        Returns:
            API response dictionary
        """
        # Build data from kwargs if not provided
        if payload_dict is None:
            payload_dict = {}
        if dns_match_ip is not None:
            payload_dict["dns-match-ip"] = dns_match_ip
        if dns_protocol is not None:
            payload_dict["dns-protocol"] = dns_protocol
        if dns_request_domain is not None:
            payload_dict["dns-request-domain"] = dns_request_domain
        if http_get is not None:
            payload_dict["http-get"] = http_get
        if http_match is not None:
            payload_dict["http-match"] = http_match
        if http_max_redirects is not None:
            payload_dict["http-max-redirects"] = http_max_redirects
        if interval is not None:
            payload_dict["interval"] = interval
        if name is not None:
            payload_dict["name"] = name
        if port is not None:
            payload_dict["port"] = port
        if retry is not None:
            payload_dict["retry"] = retry
        if src_ip is not None:
            payload_dict["src-ip"] = src_ip
        if timeout is not None:
            payload_dict["timeout"] = timeout
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

    def update(
        self,
        mkey: Union[str, int],
        payload_dict: Optional[Dict[str, Any]] = None,
        vdom: Optional[Any] = None,
        action: Optional[Any] = None,
        before: Optional[Any] = None,
        after: Optional[Any] = None,
        scope: Optional[Any] = None,
        dns_match_ip: Optional[str] = None,
        dns_protocol: Optional[str] = None,
        dns_request_domain: Optional[str] = None,
        http_get: Optional[str] = None,
        http_match: Optional[str] = None,
        http_max_redirects: Optional[int] = None,
        interval: Optional[int] = None,
        name: Optional[str] = None,
        port: Optional[int] = None,
        retry: Optional[int] = None,
        src_ip: Optional[str] = None,
        timeout: Optional[int] = None,
        type: Optional[str] = None,
        raw_json: bool = False,
        **kwargs,
    ) -> Dict[str, Any]:
        """
        Update an existing ldb-monitor entry.

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

            dns-match-ip (string):
                Response IP expected from DNS server.
            dns-protocol (string) (enum: ['udp', 'tcp']):
                Select the protocol used by the DNS health check monitor to ...
            dns-request-domain (string) (max_len: 255):
                Fully qualified domain name to resolve for the DNS probe.
            http-get (string) (max_len: 255):
                Request URI used to send a GET request to check the health o...
            http-match (string) (max_len: 255):
                String to match the value expected in response to an HTTP-GE...
            http-max-redirects (integer) (range: 0-5):
                The maximum number of HTTP redirects to be allowed (0 - 5, d...
            interval (integer) (range: 5-65535):
                Time between health checks (5 - 65535 sec, default = 10).
            name (string) (max_len: 35):
                Monitor name.
            port (integer) (range: 0-65535):
                Service port used to perform the health check. If 0, health ...
            retry (integer) (range: 1-255):
                Number health check attempts before the server is considered...
            src-ip (string):
                Source IP for ldb-monitor.
            timeout (integer) (range: 1-255):
                Time to wait to receive response to a health check from a se...
            type (string) (enum: ['ping', 'tcp', 'http']):
                Select the Monitor type used by the health check monitor to ...

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
        if dns_match_ip is not None:
            payload_dict["dns-match-ip"] = dns_match_ip
        if dns_protocol is not None:
            payload_dict["dns-protocol"] = dns_protocol
        if dns_request_domain is not None:
            payload_dict["dns-request-domain"] = dns_request_domain
        if http_get is not None:
            payload_dict["http-get"] = http_get
        if http_match is not None:
            payload_dict["http-match"] = http_match
        if http_max_redirects is not None:
            payload_dict["http-max-redirects"] = http_max_redirects
        if interval is not None:
            payload_dict["interval"] = interval
        if name is not None:
            payload_dict["name"] = name
        if port is not None:
            payload_dict["port"] = port
        if retry is not None:
            payload_dict["retry"] = retry
        if src_ip is not None:
            payload_dict["src-ip"] = src_ip
        if timeout is not None:
            payload_dict["timeout"] = timeout
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
        Delete a ldb-monitor entry.

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
