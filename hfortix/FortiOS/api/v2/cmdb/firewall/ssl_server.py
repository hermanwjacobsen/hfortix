"""
FortiOS ssl-server API wrapper.
Provides access to /api/v2/cmdb/firewall/ssl-server endpoint.
"""

from typing import Any, Dict, List, Optional, Union


class SslServer:
    """
    Wrapper for firewall ssl-server API endpoint.

    Manages ssl-server configuration with full Swagger-spec parameter support.
    """

    def __init__(self, http_client: Any):
        """
        Initialize the SslServer wrapper.

        Args:
            http_client: The HTTP client for API communication
        """
        self._client = http_client
        self.path = "firewall/ssl-server"

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
        Retrieve a list of all ssl-server entries.

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
        Retrieve a specific ssl-server entry by its name.

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
        add_header_x_forwarded_proto: Optional[str] = None,
        ip: Optional[str] = None,
        mapped_port: Optional[int] = None,
        name: Optional[str] = None,
        port: Optional[int] = None,
        ssl_algorithm: Optional[str] = None,
        ssl_cert: Optional[list] = None,
        ssl_client_renegotiation: Optional[str] = None,
        ssl_dh_bits: Optional[str] = None,
        ssl_max_version: Optional[str] = None,
        ssl_min_version: Optional[str] = None,
        ssl_mode: Optional[str] = None,
        ssl_send_empty_frags: Optional[str] = None,
        url_rewrite: Optional[str] = None,
        raw_json: bool = False,
        **kwargs,
    ) -> Dict[str, Any]:
        """
        Create a new ssl-server entry.

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

            add-header-x-forwarded-proto (string) (enum: ['enable', 'disable']):
                Enable/disable adding an X-Forwarded-Proto header to forward...
            ip (string):
                IPv4 address of the SSL server.
            mapped-port (integer) (range: 1-65535):
                Mapped server service port (1 - 65535, default = 80).
            name (string) (max_len: 35):
                Server name.
            port (integer) (range: 1-65535):
                Server service port (1 - 65535, default = 443).
            ssl-algorithm (string) (enum: ['high', 'medium', 'low']):
                Relative strength of encryption algorithms accepted in negot...
            ssl-cert (list[object]):
                List of certificate names to use for SSL connections to this...
            ssl-client-renegotiation (string) (enum: ['allow', 'deny', 'secure']):
                Allow or block client renegotiation by server.
            ssl-dh-bits (string) (enum: ['768', '1024', '1536']):
                Bit-size of Diffie-Hellman (DH) prime used in DHE-RSA negoti...
            ssl-max-version (string) (enum: ['tls-1.0', 'tls-1.1', 'tls-1.2']):
                Highest SSL/TLS version to negotiate.
            ssl-min-version (string) (enum: ['tls-1.0', 'tls-1.1', 'tls-1.2']):
                Lowest SSL/TLS version to negotiate.
            ssl-mode (string) (enum: ['half', 'full']):
                SSL/TLS mode for encryption and decryption of traffic.
            ssl-send-empty-frags (string) (enum: ['enable', 'disable']):
                Enable/disable sending empty fragments to avoid attack on CB...
            url-rewrite (string) (enum: ['enable', 'disable']):
                Enable/disable rewriting the URL.

        Returns:
            API response dictionary
        """
        # Build data from kwargs if not provided
        if payload_dict is None:
            payload_dict = {}
        if add_header_x_forwarded_proto is not None:
            payload_dict["add-header-x-forwarded-proto"] = add_header_x_forwarded_proto
        if ip is not None:
            payload_dict["ip"] = ip
        if mapped_port is not None:
            payload_dict["mapped-port"] = mapped_port
        if name is not None:
            payload_dict["name"] = name
        if port is not None:
            payload_dict["port"] = port
        if ssl_algorithm is not None:
            payload_dict["ssl-algorithm"] = ssl_algorithm
        if ssl_cert is not None:
            payload_dict["ssl-cert"] = ssl_cert
        if ssl_client_renegotiation is not None:
            payload_dict["ssl-client-renegotiation"] = ssl_client_renegotiation
        if ssl_dh_bits is not None:
            payload_dict["ssl-dh-bits"] = ssl_dh_bits
        if ssl_max_version is not None:
            payload_dict["ssl-max-version"] = ssl_max_version
        if ssl_min_version is not None:
            payload_dict["ssl-min-version"] = ssl_min_version
        if ssl_mode is not None:
            payload_dict["ssl-mode"] = ssl_mode
        if ssl_send_empty_frags is not None:
            payload_dict["ssl-send-empty-frags"] = ssl_send_empty_frags
        if url_rewrite is not None:
            payload_dict["url-rewrite"] = url_rewrite

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
        add_header_x_forwarded_proto: Optional[str] = None,
        ip: Optional[str] = None,
        mapped_port: Optional[int] = None,
        name: Optional[str] = None,
        port: Optional[int] = None,
        ssl_algorithm: Optional[str] = None,
        ssl_cert: Optional[list] = None,
        ssl_client_renegotiation: Optional[str] = None,
        ssl_dh_bits: Optional[str] = None,
        ssl_max_version: Optional[str] = None,
        ssl_min_version: Optional[str] = None,
        ssl_mode: Optional[str] = None,
        ssl_send_empty_frags: Optional[str] = None,
        url_rewrite: Optional[str] = None,
        raw_json: bool = False,
        **kwargs,
    ) -> Dict[str, Any]:
        """
        Update an existing ssl-server entry.

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

            add-header-x-forwarded-proto (string) (enum: ['enable', 'disable']):
                Enable/disable adding an X-Forwarded-Proto header to forward...
            ip (string):
                IPv4 address of the SSL server.
            mapped-port (integer) (range: 1-65535):
                Mapped server service port (1 - 65535, default = 80).
            name (string) (max_len: 35):
                Server name.
            port (integer) (range: 1-65535):
                Server service port (1 - 65535, default = 443).
            ssl-algorithm (string) (enum: ['high', 'medium', 'low']):
                Relative strength of encryption algorithms accepted in negot...
            ssl-cert (list[object]):
                List of certificate names to use for SSL connections to this...
            ssl-client-renegotiation (string) (enum: ['allow', 'deny', 'secure']):
                Allow or block client renegotiation by server.
            ssl-dh-bits (string) (enum: ['768', '1024', '1536']):
                Bit-size of Diffie-Hellman (DH) prime used in DHE-RSA negoti...
            ssl-max-version (string) (enum: ['tls-1.0', 'tls-1.1', 'tls-1.2']):
                Highest SSL/TLS version to negotiate.
            ssl-min-version (string) (enum: ['tls-1.0', 'tls-1.1', 'tls-1.2']):
                Lowest SSL/TLS version to negotiate.
            ssl-mode (string) (enum: ['half', 'full']):
                SSL/TLS mode for encryption and decryption of traffic.
            ssl-send-empty-frags (string) (enum: ['enable', 'disable']):
                Enable/disable sending empty fragments to avoid attack on CB...
            url-rewrite (string) (enum: ['enable', 'disable']):
                Enable/disable rewriting the URL.

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
        if add_header_x_forwarded_proto is not None:
            payload_dict["add-header-x-forwarded-proto"] = add_header_x_forwarded_proto
        if ip is not None:
            payload_dict["ip"] = ip
        if mapped_port is not None:
            payload_dict["mapped-port"] = mapped_port
        if name is not None:
            payload_dict["name"] = name
        if port is not None:
            payload_dict["port"] = port
        if ssl_algorithm is not None:
            payload_dict["ssl-algorithm"] = ssl_algorithm
        if ssl_cert is not None:
            payload_dict["ssl-cert"] = ssl_cert
        if ssl_client_renegotiation is not None:
            payload_dict["ssl-client-renegotiation"] = ssl_client_renegotiation
        if ssl_dh_bits is not None:
            payload_dict["ssl-dh-bits"] = ssl_dh_bits
        if ssl_max_version is not None:
            payload_dict["ssl-max-version"] = ssl_max_version
        if ssl_min_version is not None:
            payload_dict["ssl-min-version"] = ssl_min_version
        if ssl_mode is not None:
            payload_dict["ssl-mode"] = ssl_mode
        if ssl_send_empty_frags is not None:
            payload_dict["ssl-send-empty-frags"] = ssl_send_empty_frags
        if url_rewrite is not None:
            payload_dict["url-rewrite"] = url_rewrite

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
        Delete a ssl-server entry.

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
