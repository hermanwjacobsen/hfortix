"""
FortiOS multicast-policy6 API wrapper.
Provides access to /api/v2/cmdb/firewall/multicast-policy6 endpoint.
"""

from typing import Any, Dict, List, Optional, Union

from hfortix.FortiOS.http_client import encode_path_component


class MulticastPolicy6:
    """
    Wrapper for firewall multicast-policy6 API endpoint.

    Manages multicast-policy6 configuration with full Swagger-spec parameter support.
    """

    def __init__(self, http_client: Any):
        """
        Initialize the MulticastPolicy6 wrapper.

        Args:
            http_client: The HTTP client for API communication
        """
        self._client = http_client
        self.path = "firewall/multicast-policy6"


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
        Retrieve a specific multicast-policy6 entry by its id.

        Args:
            mkey: The id (primary key)
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
        auto_asic_offload: Optional[str] = None,
        comments: Optional[str] = None,
        dstaddr: Optional[list] = None,
        dstintf: Optional[str] = None,
        end_port: Optional[int] = None,
        id: Optional[int] = None,
        ips_sensor: Optional[str] = None,
        logtraffic: Optional[str] = None,
        name: Optional[str] = None,
        protocol: Optional[int] = None,
        srcaddr: Optional[list] = None,
        srcintf: Optional[str] = None,
        start_port: Optional[int] = None,
        status: Optional[str] = None,
        utm_status: Optional[str] = None,
        uuid: Optional[str] = None,
        raw_json: bool = False,
        **kwargs,
    ) -> Dict[str, Any]:
        """
        Create multicast-policy6 entry.

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
                Accept or deny traffic matching the policy.
            auto-asic-offload (string) (enum: ['enable', 'disable']):
                Enable/disable offloading policy traffic for hardware accele...
            comments (string) (max_len: 1023):
                Comment.
            dstaddr (list[object]):
                IPv6 destination address name.
            dstintf (string) (max_len: 35):
                IPv6 destination interface name.
            end-port (integer) (range: 0-65535):
                Integer value for ending TCP/UDP/SCTP destination port in ra...
            id (integer) (range: 0-4294967294):
                Policy ID (0 - 4294967294).
            ips-sensor (string) (max_len: 47):
                Name of an existing IPS sensor.
            logtraffic (string) (enum: ['all', 'utm', 'disable']):
                Enable or disable logging. Log all sessions or security prof...
            name (string) (max_len: 35):
                Policy name.
            protocol (integer) (range: 0-255):
                Integer value for the protocol type as defined by IANA (0 - ...
            srcaddr (list[object]):
                IPv6 source address name.
            srcintf (string) (max_len: 35):
                IPv6 source interface name.
            start-port (integer) (range: 0-65535):
                Integer value for starting TCP/UDP/SCTP destination port in ...
            status (string) (enum: ['enable', 'disable']):
                Enable/disable this policy.
            utm-status (string) (enum: ['enable', 'disable']):
                Enable to add an IPS security profile to the policy.
            uuid (string):
                Universally Unique Identifier (UUID; automatically assigned ...

        Returns:
            API response dictionary
        """
        # Build data from kwargs if not provided
        if payload_dict is None:
            payload_dict = {}
        if action is not None:
            payload_dict["action"] = action
        if auto_asic_offload is not None:
            payload_dict["auto-asic-offload"] = auto_asic_offload
        if comments is not None:
            payload_dict["comments"] = comments
        if dstaddr is not None:
            payload_dict["dstaddr"] = dstaddr
        if dstintf is not None:
            payload_dict["dstintf"] = dstintf
        if end_port is not None:
            payload_dict["end-port"] = end_port
        if id is not None:
            payload_dict["id"] = id
        if ips_sensor is not None:
            payload_dict["ips-sensor"] = ips_sensor
        if logtraffic is not None:
            payload_dict["logtraffic"] = logtraffic
        if name is not None:
            payload_dict["name"] = name
        if protocol is not None:
            payload_dict["protocol"] = protocol
        if srcaddr is not None:
            payload_dict["srcaddr"] = srcaddr
        if srcintf is not None:
            payload_dict["srcintf"] = srcintf
        if start_port is not None:
            payload_dict["start-port"] = start_port
        if status is not None:
            payload_dict["status"] = status
        if utm_status is not None:
            payload_dict["utm-status"] = utm_status
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
        auto_asic_offload: Optional[str] = None,
        comments: Optional[str] = None,
        dstaddr: Optional[list] = None,
        dstintf: Optional[str] = None,
        end_port: Optional[int] = None,
        id: Optional[int] = None,
        ips_sensor: Optional[str] = None,
        logtraffic: Optional[str] = None,
        name: Optional[str] = None,
        protocol: Optional[int] = None,
        srcaddr: Optional[list] = None,
        srcintf: Optional[str] = None,
        start_port: Optional[int] = None,
        status: Optional[str] = None,
        utm_status: Optional[str] = None,
        uuid: Optional[str] = None,
        raw_json: bool = False,
        **kwargs,
    ) -> Dict[str, Any]:
        """
        Update multicast-policy6 entry.

        Supports two usage patterns:
        1. Pass data dict: update(mkey=123, payload_dict={"key": "value"}, vdom="root")
        2. Pass kwargs: update(mkey=123, key="value", vdom="root")

        Args:
            mkey: The id (primary key)
            payload_dict: The updated configuration data (optional if using kwargs)
            vdom: Specify the Virtual Domain(s) from which results are returned or chang
            action: If supported, an action can be specified.
            before: If *action=move*, use *before* to specify the ID of the resource that
            after: If *action=move*, use *after* to specify the ID of the resource that t
            scope: Specify the Scope from which results are returned or changes are appli
            **kwargs: Additional parameters

        Body schema properties (can pass via data dict or as kwargs):

            action (string) (enum: ['accept', 'deny']):
                Accept or deny traffic matching the policy.
            auto-asic-offload (string) (enum: ['enable', 'disable']):
                Enable/disable offloading policy traffic for hardware accele...
            comments (string) (max_len: 1023):
                Comment.
            dstaddr (list[object]):
                IPv6 destination address name.
            dstintf (string) (max_len: 35):
                IPv6 destination interface name.
            end-port (integer) (range: 0-65535):
                Integer value for ending TCP/UDP/SCTP destination port in ra...
            id (integer) (range: 0-4294967294):
                Policy ID (0 - 4294967294).
            ips-sensor (string) (max_len: 47):
                Name of an existing IPS sensor.
            logtraffic (string) (enum: ['all', 'utm', 'disable']):
                Enable or disable logging. Log all sessions or security prof...
            name (string) (max_len: 35):
                Policy name.
            protocol (integer) (range: 0-255):
                Integer value for the protocol type as defined by IANA (0 - ...
            srcaddr (list[object]):
                IPv6 source address name.
            srcintf (string) (max_len: 35):
                IPv6 source interface name.
            start-port (integer) (range: 0-65535):
                Integer value for starting TCP/UDP/SCTP destination port in ...
            status (string) (enum: ['enable', 'disable']):
                Enable/disable this policy.
            utm-status (string) (enum: ['enable', 'disable']):
                Enable to add an IPS security profile to the policy.
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
        if action is not None:
            payload_dict["action"] = action
        if auto_asic_offload is not None:
            payload_dict["auto-asic-offload"] = auto_asic_offload
        if comments is not None:
            payload_dict["comments"] = comments
        if dstaddr is not None:
            payload_dict["dstaddr"] = dstaddr
        if dstintf is not None:
            payload_dict["dstintf"] = dstintf
        if end_port is not None:
            payload_dict["end-port"] = end_port
        if id is not None:
            payload_dict["id"] = id
        if ips_sensor is not None:
            payload_dict["ips-sensor"] = ips_sensor
        if logtraffic is not None:
            payload_dict["logtraffic"] = logtraffic
        if name is not None:
            payload_dict["name"] = name
        if protocol is not None:
            payload_dict["protocol"] = protocol
        if srcaddr is not None:
            payload_dict["srcaddr"] = srcaddr
        if srcintf is not None:
            payload_dict["srcintf"] = srcintf
        if start_port is not None:
            payload_dict["start-port"] = start_port
        if status is not None:
            payload_dict["status"] = status
        if utm_status is not None:
            payload_dict["utm-status"] = utm_status
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
        Delete a multicast-policy6 entry.

        Args:
            mkey: The id (primary key)
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
