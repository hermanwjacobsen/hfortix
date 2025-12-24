"""
FortiOS CMDB - Cmdb Vpn Ipsec Phase2 Interface

Configuration endpoint for managing cmdb vpn ipsec phase2 interface objects.

API Endpoints:
    GET    /cmdb/vpn/ipsec_phase2_interface
    POST   /cmdb/vpn/ipsec_phase2_interface
    GET    /cmdb/vpn/ipsec_phase2_interface
    PUT    /cmdb/vpn/ipsec_phase2_interface/{identifier}
    DELETE /cmdb/vpn/ipsec_phase2_interface/{identifier}

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.vpn.ipsec_phase2_interface.get()
    >>>
    >>> # Get specific item (if supported)
    >>> item = fgt.api.cmdb.vpn.ipsec_phase2_interface.get(name="item_name")
    >>>
    >>> # Create new item (use POST)
    >>> result = fgt.api.cmdb.vpn.ipsec_phase2_interface.post(
    ...     name="new_item",
    ...     # ... additional parameters
    ... )
    >>>
    >>> # Update existing item (use PUT)
    >>> result = fgt.api.cmdb.vpn.ipsec_phase2_interface.put(
    ...     name="existing_item",
    ...     # ... parameters to update
    ... )
    >>>
    >>> # Delete item
    >>> result =
    fgt.api.cmdb.vpn.ipsec_phase2_interface.delete(name="item_name")

Important:
    - Use **POST** to create new objects (404 error if already exists)
    - Use **PUT** to update existing objects (404 error if doesn't exist)
    - Use **GET** to retrieve configuration (no changes made)
    - Use **DELETE** to remove objects (404 error if doesn't exist)
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Union, cast

if TYPE_CHECKING:
    from collections.abc import Coroutine

    from hfortix.FortiOS.http_client_interface import IHTTPClient


class IpsecPhase2Interface:
    """
    Ipsecphase2Interface Operations.

    Provides CRUD operations for FortiOS ipsecphase2interface configuration.

    Methods:
        get(): Retrieve configuration objects
        post(): Create new configuration objects
        put(): Update existing configuration objects
        delete(): Remove configuration objects

    Important:
        - POST creates new objects (404 if name already exists)
        - PUT updates existing objects (404 if name doesn't exist)
        - GET retrieves objects without making changes
        - DELETE removes objects (404 if name doesn't exist)
    """

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize IpsecPhase2Interface endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

    def get(
        self,
        name: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        attr: str | None = None,
        skip_to_datasource: dict | None = None,
        acs: int | None = None,
        search: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Select a specific entry from a CLI table.

        Args:
            name: Object identifier (optional for list, required for specific)
            attr: Attribute name that references other table (optional)
            skip_to_datasource: Skip to provided table's Nth entry. E.g
            {datasource: 'firewall.address', pos: 10, global_entry: false}
            (optional)
            acs: If true, returned result are in ascending order. (optional)
            search: If present, the objects will be filtered by the search
            value. (optional)
            vdom: Virtual domain name, or False to skip. Handled by HTTPClient.
            raw_json: If True, return full API response with metadata. If
            False, return only results.
            **kwargs: Additional query parameters (filter, sort, start, count,
            format, etc.)

        Common Query Parameters (via **kwargs):
            filter: Filter results (e.g., filter='name==value')
            sort: Sort results (e.g., sort='name,asc')
            start: Starting entry index for paging
            count: Maximum number of entries to return
            format: Fields to return (e.g., format='name|type')
            See FortiOS REST API documentation for full list of query
            parameters

        Returns:
            Dictionary containing API response
        """
        params = payload_dict.copy() if payload_dict else {}

        # Build endpoint path
        if name:
            endpoint = f"/vpn.ipsec/phase2-interface/{name}"
        else:
            endpoint = "/vpn.ipsec/phase2-interface"
        if attr is not None:
            params["attr"] = attr
        if skip_to_datasource is not None:
            params["skip_to_datasource"] = skip_to_datasource
        if acs is not None:
            params["acs"] = acs
        if search is not None:
            params["search"] = search
        params.update(kwargs)
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )

    def put(
        self,
        name: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        before: str | None = None,
        after: str | None = None,
        phase1name: str | None = None,
        dhcp_ipsec: str | None = None,
        proposal: str | None = None,
        pfs: str | None = None,
        dhgrp: str | None = None,
        addke1: str | None = None,
        addke2: str | None = None,
        addke3: str | None = None,
        addke4: str | None = None,
        addke5: str | None = None,
        addke6: str | None = None,
        addke7: str | None = None,
        replay: str | None = None,
        keepalive: str | None = None,
        auto_negotiate: str | None = None,
        add_route: str | None = None,
        inbound_dscp_copy: str | None = None,
        auto_discovery_sender: str | None = None,
        auto_discovery_forwarder: str | None = None,
        keylifeseconds: int | None = None,
        keylifekbs: int | None = None,
        keylife_type: str | None = None,
        single_source: str | None = None,
        route_overlap: str | None = None,
        encapsulation: str | None = None,
        l2tp: str | None = None,
        comments: str | None = None,
        initiator_ts_narrow: str | None = None,
        diffserv: str | None = None,
        diffservcode: str | None = None,
        protocol: int | None = None,
        src_name: str | None = None,
        src_name6: str | None = None,
        src_addr_type: str | None = None,
        src_start_ip: str | None = None,
        src_start_ip6: str | None = None,
        src_end_ip: str | None = None,
        src_end_ip6: str | None = None,
        src_subnet: str | None = None,
        src_subnet6: str | None = None,
        src_port: int | None = None,
        dst_name: str | None = None,
        dst_name6: str | None = None,
        dst_addr_type: str | None = None,
        dst_start_ip: str | None = None,
        dst_start_ip6: str | None = None,
        dst_end_ip: str | None = None,
        dst_end_ip6: str | None = None,
        dst_subnet: str | None = None,
        dst_subnet6: str | None = None,
        dst_port: int | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update this specific resource.

        Args:
            payload_dict: Optional dictionary of all parameters (can be passed
            as first positional arg)
            name: Object identifier (required)
            before: If *action=move*, use *before* to specify the ID of the
            resource that this resource will be moved before. (optional)
            after: If *action=move*, use *after* to specify the ID of the
            resource that this resource will be moved after. (optional)
            name: IPsec tunnel name. (optional)
            phase1name: Phase 1 determines the options required for phase 2.
            (optional)
            dhcp_ipsec: Enable/disable DHCP-IPsec. (optional)
            proposal: Phase2 proposal. (optional)
            pfs: Enable/disable PFS feature. (optional)
            dhgrp: Phase2 DH group. (optional)
            addke1: phase2 ADDKE1 group. (optional)
            addke2: phase2 ADDKE2 group. (optional)
            addke3: phase2 ADDKE3 group. (optional)
            addke4: phase2 ADDKE4 group. (optional)
            addke5: phase2 ADDKE5 group. (optional)
            addke6: phase2 ADDKE6 group. (optional)
            addke7: phase2 ADDKE7 group. (optional)
            replay: Enable/disable replay detection. (optional)
            keepalive: Enable/disable keep alive. (optional)
            auto_negotiate: Enable/disable IPsec SA auto-negotiation.
            (optional)
            add_route: Enable/disable automatic route addition. (optional)
            inbound_dscp_copy: Enable/disable copying of the DSCP in the ESP
            header to the inner IP header. (optional)
            auto_discovery_sender: Enable/disable sending short-cut messages.
            (optional)
            auto_discovery_forwarder: Enable/disable forwarding short-cut
            messages. (optional)
            keylifeseconds: Phase2 key life in time in seconds (120 - 172800).
            (optional)
            keylifekbs: Phase2 key life in number of kilobytes of traffic (5120
            - 4294967295). (optional)
            keylife_type: Keylife type. (optional)
            single_source: Enable/disable single source IP restriction.
            (optional)
            route_overlap: Action for overlapping routes. (optional)
            encapsulation: ESP encapsulation mode. (optional)
            l2tp: Enable/disable L2TP over IPsec. (optional)
            comments: Comment. (optional)
            initiator_ts_narrow: Enable/disable traffic selector narrowing for
            IKEv2 initiator. (optional)
            diffserv: Enable/disable applying DSCP value to the IPsec tunnel
            outer IP header. (optional)
            diffservcode: DSCP value to be applied to the IPsec tunnel outer IP
            header. (optional)
            protocol: Quick mode protocol selector (1 - 255 or 0 for all).
            (optional)
            src_name: Local proxy ID name. (optional)
            src_name6: Local proxy ID name. (optional)
            src_addr_type: Local proxy ID type. (optional)
            src_start_ip: Local proxy ID start. (optional)
            src_start_ip6: Local proxy ID IPv6 start. (optional)
            src_end_ip: Local proxy ID end. (optional)
            src_end_ip6: Local proxy ID IPv6 end. (optional)
            src_subnet: Local proxy ID subnet. (optional)
            src_subnet6: Local proxy ID IPv6 subnet. (optional)
            src_port: Quick mode source port (1 - 65535 or 0 for all).
            (optional)
            dst_name: Remote proxy ID name. (optional)
            dst_name6: Remote proxy ID name. (optional)
            dst_addr_type: Remote proxy ID type. (optional)
            dst_start_ip: Remote proxy ID IPv4 start. (optional)
            dst_start_ip6: Remote proxy ID IPv6 start. (optional)
            dst_end_ip: Remote proxy ID IPv4 end. (optional)
            dst_end_ip6: Remote proxy ID IPv6 end. (optional)
            dst_subnet: Remote proxy ID IPv4 subnet. (optional)
            dst_subnet6: Remote proxy ID IPv6 subnet. (optional)
            dst_port: Quick mode destination port (1 - 65535 or 0 for all).
            (optional)
            vdom: Virtual domain name, or False to skip. Handled by HTTPClient.
            raw_json: If True, return full API response with metadata. If
            False, return only results.
            **kwargs: Additional query parameters (filter, sort, start, count,
            format, etc.)

        Common Query Parameters (via **kwargs):
            filter: Filter results (e.g., filter='name==value')
            sort: Sort results (e.g., sort='name,asc')
            start: Starting entry index for paging
            count: Maximum number of entries to return
            format: Fields to return (e.g., format='name|type')
            See FortiOS REST API documentation for full list of query
            parameters

        Returns:
            Dictionary containing API response
        """
        data_payload = payload_dict.copy() if payload_dict else {}

        # Build endpoint path
        if not name:
            raise ValueError("name is required for put()")
        endpoint = f"/vpn.ipsec/phase2-interface/{name}"
        if before is not None:
            data_payload["before"] = before
        if after is not None:
            data_payload["after"] = after
        if name is not None:
            data_payload["name"] = name
        if phase1name is not None:
            data_payload["phase1name"] = phase1name
        if dhcp_ipsec is not None:
            data_payload["dhcp-ipsec"] = dhcp_ipsec
        if proposal is not None:
            data_payload["proposal"] = proposal
        if pfs is not None:
            data_payload["pfs"] = pfs
        if dhgrp is not None:
            data_payload["dhgrp"] = dhgrp
        if addke1 is not None:
            data_payload["addke1"] = addke1
        if addke2 is not None:
            data_payload["addke2"] = addke2
        if addke3 is not None:
            data_payload["addke3"] = addke3
        if addke4 is not None:
            data_payload["addke4"] = addke4
        if addke5 is not None:
            data_payload["addke5"] = addke5
        if addke6 is not None:
            data_payload["addke6"] = addke6
        if addke7 is not None:
            data_payload["addke7"] = addke7
        if replay is not None:
            data_payload["replay"] = replay
        if keepalive is not None:
            data_payload["keepalive"] = keepalive
        if auto_negotiate is not None:
            data_payload["auto-negotiate"] = auto_negotiate
        if add_route is not None:
            data_payload["add-route"] = add_route
        if inbound_dscp_copy is not None:
            data_payload["inbound-dscp-copy"] = inbound_dscp_copy
        if auto_discovery_sender is not None:
            data_payload["auto-discovery-sender"] = auto_discovery_sender
        if auto_discovery_forwarder is not None:
            data_payload["auto-discovery-forwarder"] = auto_discovery_forwarder
        if keylifeseconds is not None:
            data_payload["keylifeseconds"] = keylifeseconds
        if keylifekbs is not None:
            data_payload["keylifekbs"] = keylifekbs
        if keylife_type is not None:
            data_payload["keylife-type"] = keylife_type
        if single_source is not None:
            data_payload["single-source"] = single_source
        if route_overlap is not None:
            data_payload["route-overlap"] = route_overlap
        if encapsulation is not None:
            data_payload["encapsulation"] = encapsulation
        if l2tp is not None:
            data_payload["l2tp"] = l2tp
        if comments is not None:
            data_payload["comments"] = comments
        if initiator_ts_narrow is not None:
            data_payload["initiator-ts-narrow"] = initiator_ts_narrow
        if diffserv is not None:
            data_payload["diffserv"] = diffserv
        if diffservcode is not None:
            data_payload["diffservcode"] = diffservcode
        if protocol is not None:
            data_payload["protocol"] = protocol
        if src_name is not None:
            data_payload["src-name"] = src_name
        if src_name6 is not None:
            data_payload["src-name6"] = src_name6
        if src_addr_type is not None:
            data_payload["src-addr-type"] = src_addr_type
        if src_start_ip is not None:
            data_payload["src-start-ip"] = src_start_ip
        if src_start_ip6 is not None:
            data_payload["src-start-ip6"] = src_start_ip6
        if src_end_ip is not None:
            data_payload["src-end-ip"] = src_end_ip
        if src_end_ip6 is not None:
            data_payload["src-end-ip6"] = src_end_ip6
        if src_subnet is not None:
            data_payload["src-subnet"] = src_subnet
        if src_subnet6 is not None:
            data_payload["src-subnet6"] = src_subnet6
        if src_port is not None:
            data_payload["src-port"] = src_port
        if dst_name is not None:
            data_payload["dst-name"] = dst_name
        if dst_name6 is not None:
            data_payload["dst-name6"] = dst_name6
        if dst_addr_type is not None:
            data_payload["dst-addr-type"] = dst_addr_type
        if dst_start_ip is not None:
            data_payload["dst-start-ip"] = dst_start_ip
        if dst_start_ip6 is not None:
            data_payload["dst-start-ip6"] = dst_start_ip6
        if dst_end_ip is not None:
            data_payload["dst-end-ip"] = dst_end_ip
        if dst_end_ip6 is not None:
            data_payload["dst-end-ip6"] = dst_end_ip6
        if dst_subnet is not None:
            data_payload["dst-subnet"] = dst_subnet
        if dst_subnet6 is not None:
            data_payload["dst-subnet6"] = dst_subnet6
        if dst_port is not None:
            data_payload["dst-port"] = dst_port
        data_payload.update(kwargs)
        return self._client.put(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )

    def delete(
        self,
        name: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Delete this specific resource.

        Args:
            name: Object identifier (required)
            vdom: Virtual domain name, or False to skip. Handled by HTTPClient.
            raw_json: If True, return full API response with metadata. If
            False, return only results.
            **kwargs: Additional query parameters (filter, sort, start, count,
            format, etc.)

        Common Query Parameters (via **kwargs):
            filter: Filter results (e.g., filter='name==value')
            sort: Sort results (e.g., sort='name,asc')
            start: Starting entry index for paging
            count: Maximum number of entries to return
            format: Fields to return (e.g., format='name|type')
            See FortiOS REST API documentation for full list of query
            parameters

        Returns:
            Dictionary containing API response
        """
        params = payload_dict.copy() if payload_dict else {}

        # Build endpoint path
        if not name:
            raise ValueError("name is required for delete()")
        endpoint = f"/vpn.ipsec/phase2-interface/{name}"
        params.update(kwargs)
        return self._client.delete(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )

    def exists(
        self,
        name: str,
        vdom: str | bool | None = None,
    ) -> Union[bool, Coroutine[Any, Any, bool]]:
        """
        Check if an object exists.

        Args:
            name: Object identifier
            vdom: Virtual domain name, or False to skip. Handled by HTTPClient.

        Returns:
            True if object exists, False otherwise

        Example:
            >>> if fgt.api.cmdb.firewall.address.exists("server1"):
            ...     print("Address exists")
        """
        import inspect

        from hfortix.FortiOS.exceptions_forti import ResourceNotFoundError

        # Call get() - returns dict (sync) or coroutine (async)
        result = self.get(name=name, vdom=vdom)

        # Check if async mode
        if inspect.iscoroutine(result):

            async def _async():
                try:
                    # Runtime check confirms result is a coroutine, cast for
                    # mypy
                    await cast(Coroutine[Any, Any, dict[str, Any]], result)
                    return True
                except ResourceNotFoundError:
                    return False

            # Type ignore justified: mypy can't verify Union return type
            # narrowing

            return _async()
        # Sync mode - get() already executed, no exception means it exists
        return True

    def post(
        self,
        payload_dict: dict[str, Any] | None = None,
        nkey: str | None = None,
        name: str | None = None,
        phase1name: str | None = None,
        dhcp_ipsec: str | None = None,
        proposal: str | None = None,
        pfs: str | None = None,
        dhgrp: str | None = None,
        addke1: str | None = None,
        addke2: str | None = None,
        addke3: str | None = None,
        addke4: str | None = None,
        addke5: str | None = None,
        addke6: str | None = None,
        addke7: str | None = None,
        replay: str | None = None,
        keepalive: str | None = None,
        auto_negotiate: str | None = None,
        add_route: str | None = None,
        inbound_dscp_copy: str | None = None,
        auto_discovery_sender: str | None = None,
        auto_discovery_forwarder: str | None = None,
        keylifeseconds: int | None = None,
        keylifekbs: int | None = None,
        keylife_type: str | None = None,
        single_source: str | None = None,
        route_overlap: str | None = None,
        encapsulation: str | None = None,
        l2tp: str | None = None,
        comments: str | None = None,
        initiator_ts_narrow: str | None = None,
        diffserv: str | None = None,
        diffservcode: str | None = None,
        protocol: int | None = None,
        src_name: str | None = None,
        src_name6: str | None = None,
        src_addr_type: str | None = None,
        src_start_ip: str | None = None,
        src_start_ip6: str | None = None,
        src_end_ip: str | None = None,
        src_end_ip6: str | None = None,
        src_subnet: str | None = None,
        src_subnet6: str | None = None,
        src_port: int | None = None,
        dst_name: str | None = None,
        dst_name6: str | None = None,
        dst_addr_type: str | None = None,
        dst_start_ip: str | None = None,
        dst_start_ip6: str | None = None,
        dst_end_ip: str | None = None,
        dst_end_ip6: str | None = None,
        dst_subnet: str | None = None,
        dst_subnet6: str | None = None,
        dst_port: int | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Create object(s) in this table.

        Args:
            payload_dict: Optional dictionary of all parameters (can be passed
            as first positional arg)
            nkey: If *action=clone*, use *nkey* to specify the ID for the new
            resource to be created. (optional)
            name: IPsec tunnel name. (optional)
            phase1name: Phase 1 determines the options required for phase 2.
            (optional)
            dhcp_ipsec: Enable/disable DHCP-IPsec. (optional)
            proposal: Phase2 proposal. (optional)
            pfs: Enable/disable PFS feature. (optional)
            dhgrp: Phase2 DH group. (optional)
            addke1: phase2 ADDKE1 group. (optional)
            addke2: phase2 ADDKE2 group. (optional)
            addke3: phase2 ADDKE3 group. (optional)
            addke4: phase2 ADDKE4 group. (optional)
            addke5: phase2 ADDKE5 group. (optional)
            addke6: phase2 ADDKE6 group. (optional)
            addke7: phase2 ADDKE7 group. (optional)
            replay: Enable/disable replay detection. (optional)
            keepalive: Enable/disable keep alive. (optional)
            auto_negotiate: Enable/disable IPsec SA auto-negotiation.
            (optional)
            add_route: Enable/disable automatic route addition. (optional)
            inbound_dscp_copy: Enable/disable copying of the DSCP in the ESP
            header to the inner IP header. (optional)
            auto_discovery_sender: Enable/disable sending short-cut messages.
            (optional)
            auto_discovery_forwarder: Enable/disable forwarding short-cut
            messages. (optional)
            keylifeseconds: Phase2 key life in time in seconds (120 - 172800).
            (optional)
            keylifekbs: Phase2 key life in number of kilobytes of traffic (5120
            - 4294967295). (optional)
            keylife_type: Keylife type. (optional)
            single_source: Enable/disable single source IP restriction.
            (optional)
            route_overlap: Action for overlapping routes. (optional)
            encapsulation: ESP encapsulation mode. (optional)
            l2tp: Enable/disable L2TP over IPsec. (optional)
            comments: Comment. (optional)
            initiator_ts_narrow: Enable/disable traffic selector narrowing for
            IKEv2 initiator. (optional)
            diffserv: Enable/disable applying DSCP value to the IPsec tunnel
            outer IP header. (optional)
            diffservcode: DSCP value to be applied to the IPsec tunnel outer IP
            header. (optional)
            protocol: Quick mode protocol selector (1 - 255 or 0 for all).
            (optional)
            src_name: Local proxy ID name. (optional)
            src_name6: Local proxy ID name. (optional)
            src_addr_type: Local proxy ID type. (optional)
            src_start_ip: Local proxy ID start. (optional)
            src_start_ip6: Local proxy ID IPv6 start. (optional)
            src_end_ip: Local proxy ID end. (optional)
            src_end_ip6: Local proxy ID IPv6 end. (optional)
            src_subnet: Local proxy ID subnet. (optional)
            src_subnet6: Local proxy ID IPv6 subnet. (optional)
            src_port: Quick mode source port (1 - 65535 or 0 for all).
            (optional)
            dst_name: Remote proxy ID name. (optional)
            dst_name6: Remote proxy ID name. (optional)
            dst_addr_type: Remote proxy ID type. (optional)
            dst_start_ip: Remote proxy ID IPv4 start. (optional)
            dst_start_ip6: Remote proxy ID IPv6 start. (optional)
            dst_end_ip: Remote proxy ID IPv4 end. (optional)
            dst_end_ip6: Remote proxy ID IPv6 end. (optional)
            dst_subnet: Remote proxy ID IPv4 subnet. (optional)
            dst_subnet6: Remote proxy ID IPv6 subnet. (optional)
            dst_port: Quick mode destination port (1 - 65535 or 0 for all).
            (optional)
            vdom: Virtual domain name, or False to skip. Handled by HTTPClient.
            raw_json: If True, return full API response with metadata. If
            False, return only results.
            **kwargs: Additional query parameters (filter, sort, start, count,
            format, etc.)

        Common Query Parameters (via **kwargs):
            filter: Filter results (e.g., filter='name==value')
            sort: Sort results (e.g., sort='name,asc')
            start: Starting entry index for paging
            count: Maximum number of entries to return
            format: Fields to return (e.g., format='name|type')
            See FortiOS REST API documentation for full list of query
            parameters

        Returns:
            Dictionary containing API response
        """
        data_payload = payload_dict.copy() if payload_dict else {}
        endpoint = "/vpn.ipsec/phase2-interface"
        if nkey is not None:
            data_payload["nkey"] = nkey
        if name is not None:
            data_payload["name"] = name
        if phase1name is not None:
            data_payload["phase1name"] = phase1name
        if dhcp_ipsec is not None:
            data_payload["dhcp-ipsec"] = dhcp_ipsec
        if proposal is not None:
            data_payload["proposal"] = proposal
        if pfs is not None:
            data_payload["pfs"] = pfs
        if dhgrp is not None:
            data_payload["dhgrp"] = dhgrp
        if addke1 is not None:
            data_payload["addke1"] = addke1
        if addke2 is not None:
            data_payload["addke2"] = addke2
        if addke3 is not None:
            data_payload["addke3"] = addke3
        if addke4 is not None:
            data_payload["addke4"] = addke4
        if addke5 is not None:
            data_payload["addke5"] = addke5
        if addke6 is not None:
            data_payload["addke6"] = addke6
        if addke7 is not None:
            data_payload["addke7"] = addke7
        if replay is not None:
            data_payload["replay"] = replay
        if keepalive is not None:
            data_payload["keepalive"] = keepalive
        if auto_negotiate is not None:
            data_payload["auto-negotiate"] = auto_negotiate
        if add_route is not None:
            data_payload["add-route"] = add_route
        if inbound_dscp_copy is not None:
            data_payload["inbound-dscp-copy"] = inbound_dscp_copy
        if auto_discovery_sender is not None:
            data_payload["auto-discovery-sender"] = auto_discovery_sender
        if auto_discovery_forwarder is not None:
            data_payload["auto-discovery-forwarder"] = auto_discovery_forwarder
        if keylifeseconds is not None:
            data_payload["keylifeseconds"] = keylifeseconds
        if keylifekbs is not None:
            data_payload["keylifekbs"] = keylifekbs
        if keylife_type is not None:
            data_payload["keylife-type"] = keylife_type
        if single_source is not None:
            data_payload["single-source"] = single_source
        if route_overlap is not None:
            data_payload["route-overlap"] = route_overlap
        if encapsulation is not None:
            data_payload["encapsulation"] = encapsulation
        if l2tp is not None:
            data_payload["l2tp"] = l2tp
        if comments is not None:
            data_payload["comments"] = comments
        if initiator_ts_narrow is not None:
            data_payload["initiator-ts-narrow"] = initiator_ts_narrow
        if diffserv is not None:
            data_payload["diffserv"] = diffserv
        if diffservcode is not None:
            data_payload["diffservcode"] = diffservcode
        if protocol is not None:
            data_payload["protocol"] = protocol
        if src_name is not None:
            data_payload["src-name"] = src_name
        if src_name6 is not None:
            data_payload["src-name6"] = src_name6
        if src_addr_type is not None:
            data_payload["src-addr-type"] = src_addr_type
        if src_start_ip is not None:
            data_payload["src-start-ip"] = src_start_ip
        if src_start_ip6 is not None:
            data_payload["src-start-ip6"] = src_start_ip6
        if src_end_ip is not None:
            data_payload["src-end-ip"] = src_end_ip
        if src_end_ip6 is not None:
            data_payload["src-end-ip6"] = src_end_ip6
        if src_subnet is not None:
            data_payload["src-subnet"] = src_subnet
        if src_subnet6 is not None:
            data_payload["src-subnet6"] = src_subnet6
        if src_port is not None:
            data_payload["src-port"] = src_port
        if dst_name is not None:
            data_payload["dst-name"] = dst_name
        if dst_name6 is not None:
            data_payload["dst-name6"] = dst_name6
        if dst_addr_type is not None:
            data_payload["dst-addr-type"] = dst_addr_type
        if dst_start_ip is not None:
            data_payload["dst-start-ip"] = dst_start_ip
        if dst_start_ip6 is not None:
            data_payload["dst-start-ip6"] = dst_start_ip6
        if dst_end_ip is not None:
            data_payload["dst-end-ip"] = dst_end_ip
        if dst_end_ip6 is not None:
            data_payload["dst-end-ip6"] = dst_end_ip6
        if dst_subnet is not None:
            data_payload["dst-subnet"] = dst_subnet
        if dst_subnet6 is not None:
            data_payload["dst-subnet6"] = dst_subnet6
        if dst_port is not None:
            data_payload["dst-port"] = dst_port
        data_payload.update(kwargs)
        return self._client.post(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )
