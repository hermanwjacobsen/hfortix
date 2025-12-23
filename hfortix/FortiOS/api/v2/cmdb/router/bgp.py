"""
FortiOS CMDB - Cmdb Router Bgp

Configuration endpoint for managing cmdb router bgp objects.

API Endpoints:
    GET    /cmdb/router/bgp
    PUT    /cmdb/router/bgp/{identifier}

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.router.bgp.get()
    >>>
    >>> # Get specific item (if supported)
    >>> item = fgt.api.cmdb.router.bgp.get(name="item_name")
    >>>
    >>> # Create new item (use POST)
    >>> result = fgt.api.cmdb.router.bgp.post(
    ...     name="new_item",
    ...     # ... additional parameters
    ... )
    >>>
    >>> # Update existing item (use PUT)
    >>> result = fgt.api.cmdb.router.bgp.put(
    ...     name="existing_item",
    ...     # ... parameters to update
    ... )
    >>>
    >>> # Delete item
    >>> result = fgt.api.cmdb.router.bgp.delete(name="item_name")

Important:
    - Use **POST** to create new objects (404 error if already exists)
    - Use **PUT** to update existing objects (404 error if doesn't exist)
    - Use **GET** to retrieve configuration (no changes made)
    - Use **DELETE** to remove objects (404 error if doesn't exist)
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Union

if TYPE_CHECKING:
    from collections.abc import Coroutine

    from hfortix.FortiOS.http_client_interface import IHTTPClient


class Bgp:
    """
    Bgp Operations.

    Provides CRUD operations for FortiOS bgp configuration.

    Methods:
        get(): Retrieve configuration objects
        put(): Update existing configuration objects

    Important:
        - POST creates new objects (404 if name already exists)
        - PUT updates existing objects (404 if name doesn't exist)
        - GET retrieves objects without making changes
        - DELETE removes objects (404 if name doesn't exist)
    """

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Bgp endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

    def get(
        self,
        payload_dict: dict[str, Any] | None = None,
        exclude_default_values: bool | None = None,
        stat_items: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Select all entries in a CLI table.

        Args:
            exclude_default_values: Exclude properties/objects with default
            value (optional)
            stat_items: Items to count occurrence in entire response (multiple
            items should be separated by '|'). (optional)
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
        endpoint = "/router/bgp"
        if exclude_default_values is not None:
            params["exclude-default-values"] = exclude_default_values
        if stat_items is not None:
            params["stat-items"] = stat_items
        params.update(kwargs)
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )

    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        before: str | None = None,
        after: str | None = None,
        as_: str | None = None,
        router_id: str | None = None,
        keepalive_timer: int | None = None,
        holdtime_timer: int | None = None,
        always_compare_med: str | None = None,
        bestpath_as_path_ignore: str | None = None,
        bestpath_cmp_confed_aspath: str | None = None,
        bestpath_cmp_routerid: str | None = None,
        bestpath_med_confed: str | None = None,
        bestpath_med_missing_as_worst: str | None = None,
        client_to_client_reflection: str | None = None,
        dampening: str | None = None,
        deterministic_med: str | None = None,
        ebgp_multipath: str | None = None,
        ibgp_multipath: str | None = None,
        enforce_first_as: str | None = None,
        fast_external_failover: str | None = None,
        log_neighbour_changes: str | None = None,
        network_import_check: str | None = None,
        ignore_optional_capability: str | None = None,
        additional_path: str | None = None,
        additional_path6: str | None = None,
        additional_path_vpnv4: str | None = None,
        additional_path_vpnv6: str | None = None,
        multipath_recursive_distance: str | None = None,
        recursive_next_hop: str | None = None,
        recursive_inherit_priority: str | None = None,
        tag_resolve_mode: str | None = None,
        cluster_id: str | None = None,
        confederation_identifier: int | None = None,
        confederation_peers: list | None = None,
        dampening_route_map: str | None = None,
        dampening_reachability_half_life: int | None = None,
        dampening_reuse: int | None = None,
        dampening_suppress: int | None = None,
        dampening_max_suppress_time: int | None = None,
        dampening_unreachability_half_life: int | None = None,
        default_local_preference: int | None = None,
        scan_time: int | None = None,
        distance_external: int | None = None,
        distance_internal: int | None = None,
        distance_local: int | None = None,
        synchronization: str | None = None,
        graceful_restart: str | None = None,
        graceful_restart_time: int | None = None,
        graceful_stalepath_time: int | None = None,
        graceful_update_delay: int | None = None,
        graceful_end_on_timer: str | None = None,
        additional_path_select: int | None = None,
        additional_path_select6: int | None = None,
        additional_path_select_vpnv4: int | None = None,
        additional_path_select_vpnv6: int | None = None,
        cross_family_conditional_adv: str | None = None,
        aggregate_address: list | None = None,
        aggregate_address6: list | None = None,
        neighbor: list | None = None,
        neighbor_group: list | None = None,
        neighbor_range: list | None = None,
        neighbor_range6: list | None = None,
        network: list | None = None,
        network6: list | None = None,
        redistribute: list | None = None,
        redistribute6: list | None = None,
        admin_distance: list | None = None,
        vrf: list | None = None,
        vrf6: list | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update this specific resource.

        Args:
            payload_dict: Optional dictionary of all parameters (can be passed
            as first positional arg)
            before: If *action=move*, use *before* to specify the ID of the
            resource that this resource will be moved before. (optional)
            after: If *action=move*, use *after* to specify the ID of the
            resource that this resource will be moved after. (optional)
            as_: Router AS number, asplain/asdot/asdot+ format, 0 to disable
            BGP. (optional)
            router_id: Router ID. (optional)
            keepalive_timer: Frequency to send keep alive requests. (optional)
            holdtime_timer: Number of seconds to mark peer as dead. (optional)
            always_compare_med: Enable/disable always compare MED. (optional)
            bestpath_as_path_ignore: Enable/disable ignore AS path. (optional)
            bestpath_cmp_confed_aspath: Enable/disable compare federation AS
            path length. (optional)
            bestpath_cmp_routerid: Enable/disable compare router ID for
            identical EBGP paths. (optional)
            bestpath_med_confed: Enable/disable compare MED among confederation
            paths. (optional)
            bestpath_med_missing_as_worst: Enable/disable treat missing MED as
            least preferred. (optional)
            client_to_client_reflection: Enable/disable client-to-client route
            reflection. (optional)
            dampening: Enable/disable route-flap dampening. (optional)
            deterministic_med: Enable/disable enforce deterministic comparison
            of MED. (optional)
            ebgp_multipath: Enable/disable EBGP multi-path. (optional)
            ibgp_multipath: Enable/disable IBGP multi-path. (optional)
            enforce_first_as: Enable/disable enforce first AS for EBGP routes.
            (optional)
            fast_external_failover: Enable/disable reset peer BGP session if
            link goes down. (optional)
            log_neighbour_changes: Log BGP neighbor changes. (optional)
            network_import_check: Enable/disable ensure BGP network route
            exists in IGP. (optional)
            ignore_optional_capability: Do not send unknown optional capability
            notification message. (optional)
            additional_path: Enable/disable selection of BGP IPv4 additional
            paths. (optional)
            additional_path6: Enable/disable selection of BGP IPv6 additional
            paths. (optional)
            additional_path_vpnv4: Enable/disable selection of BGP VPNv4
            additional paths. (optional)
            additional_path_vpnv6: Enable/disable selection of BGP VPNv6
            additional paths. (optional)
            multipath_recursive_distance: Enable/disable use of recursive
            distance to select multipath. (optional)
            recursive_next_hop: Enable/disable recursive resolution of next-hop
            using BGP route. (optional)
            recursive_inherit_priority: Enable/disable priority inheritance for
            recursive resolution. (optional)
            tag_resolve_mode: Configure tag-match mode. Resolves BGP routes
            with other routes containing the same tag. (optional)
            cluster_id: Route reflector cluster ID. (optional)
            confederation_identifier: Confederation identifier. (optional)
            confederation_peers: Confederation peers. (optional)
            dampening_route_map: Criteria for dampening. (optional)
            dampening_reachability_half_life: Reachability half-life time for
            penalty (min). (optional)
            dampening_reuse: Threshold to reuse routes. (optional)
            dampening_suppress: Threshold to suppress routes. (optional)
            dampening_max_suppress_time: Maximum minutes a route can be
            suppressed. (optional)
            dampening_unreachability_half_life: Unreachability half-life time
            for penalty (min). (optional)
            default_local_preference: Default local preference. (optional)
            scan_time: Background scanner interval (sec), 0 to disable it.
            (optional)
            distance_external: Distance for routes external to the AS.
            (optional)
            distance_internal: Distance for routes internal to the AS.
            (optional)
            distance_local: Distance for routes local to the AS. (optional)
            synchronization: Enable/disable only advertise routes from iBGP if
            routes present in an IGP. (optional)
            graceful_restart: Enable/disable BGP graceful restart capabilities.
            (optional)
            graceful_restart_time: Time needed for neighbors to restart (sec).
            (optional)
            graceful_stalepath_time: Time to hold stale paths of restarting
            neighbor (sec). (optional)
            graceful_update_delay: Route advertisement/selection delay after
            restart (sec). (optional)
            graceful_end_on_timer: Enable/disable to exit graceful restart on
            timer only. (optional)
            additional_path_select: Number of additional paths to be selected
            for each IPv4 NLRI. (optional)
            additional_path_select6: Number of additional paths to be selected
            for each IPv6 NLRI. (optional)
            additional_path_select_vpnv4: Number of additional paths to be
            selected for each VPNv4 NLRI. (optional)
            additional_path_select_vpnv6: Number of additional paths to be
            selected for each VPNv6 NLRI. (optional)
            cross_family_conditional_adv: Enable/disable cross address family
            conditional advertisement. (optional)
            aggregate_address: BGP aggregate address table. (optional)
            aggregate_address6: BGP IPv6 aggregate address table. (optional)
            neighbor: BGP neighbor table. (optional)
            neighbor_group: BGP neighbor group table. (optional)
            neighbor_range: BGP neighbor range table. (optional)
            neighbor_range6: BGP IPv6 neighbor range table. (optional)
            network: BGP network table. (optional)
            network6: BGP IPv6 network table. (optional)
            redistribute: BGP IPv4 redistribute table. (optional)
            redistribute6: BGP IPv6 redistribute table. (optional)
            admin_distance: Administrative distance modifications. (optional)
            vrf: BGP VRF leaking table. (optional)
            vrf6: BGP IPv6 VRF leaking table. (optional)
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
        endpoint = "/router/bgp"
        if before is not None:
            data_payload["before"] = before
        if after is not None:
            data_payload["after"] = after
        if as_ is not None:
            data_payload["as"] = as_
        if router_id is not None:
            data_payload["router-id"] = router_id
        if keepalive_timer is not None:
            data_payload["keepalive-timer"] = keepalive_timer
        if holdtime_timer is not None:
            data_payload["holdtime-timer"] = holdtime_timer
        if always_compare_med is not None:
            data_payload["always-compare-med"] = always_compare_med
        if bestpath_as_path_ignore is not None:
            data_payload["bestpath-as-path-ignore"] = bestpath_as_path_ignore
        if bestpath_cmp_confed_aspath is not None:
            data_payload["bestpath-cmp-confed-aspath"] = (
                bestpath_cmp_confed_aspath
            )
        if bestpath_cmp_routerid is not None:
            data_payload["bestpath-cmp-routerid"] = bestpath_cmp_routerid
        if bestpath_med_confed is not None:
            data_payload["bestpath-med-confed"] = bestpath_med_confed
        if bestpath_med_missing_as_worst is not None:
            data_payload["bestpath-med-missing-as-worst"] = (
                bestpath_med_missing_as_worst
            )
        if client_to_client_reflection is not None:
            data_payload["client-to-client-reflection"] = (
                client_to_client_reflection
            )
        if dampening is not None:
            data_payload["dampening"] = dampening
        if deterministic_med is not None:
            data_payload["deterministic-med"] = deterministic_med
        if ebgp_multipath is not None:
            data_payload["ebgp-multipath"] = ebgp_multipath
        if ibgp_multipath is not None:
            data_payload["ibgp-multipath"] = ibgp_multipath
        if enforce_first_as is not None:
            data_payload["enforce-first-as"] = enforce_first_as
        if fast_external_failover is not None:
            data_payload["fast-external-failover"] = fast_external_failover
        if log_neighbour_changes is not None:
            data_payload["log-neighbour-changes"] = log_neighbour_changes
        if network_import_check is not None:
            data_payload["network-import-check"] = network_import_check
        if ignore_optional_capability is not None:
            data_payload["ignore-optional-capability"] = (
                ignore_optional_capability
            )
        if additional_path is not None:
            data_payload["additional-path"] = additional_path
        if additional_path6 is not None:
            data_payload["additional-path6"] = additional_path6
        if additional_path_vpnv4 is not None:
            data_payload["additional-path-vpnv4"] = additional_path_vpnv4
        if additional_path_vpnv6 is not None:
            data_payload["additional-path-vpnv6"] = additional_path_vpnv6
        if multipath_recursive_distance is not None:
            data_payload["multipath-recursive-distance"] = (
                multipath_recursive_distance
            )
        if recursive_next_hop is not None:
            data_payload["recursive-next-hop"] = recursive_next_hop
        if recursive_inherit_priority is not None:
            data_payload["recursive-inherit-priority"] = (
                recursive_inherit_priority
            )
        if tag_resolve_mode is not None:
            data_payload["tag-resolve-mode"] = tag_resolve_mode
        if cluster_id is not None:
            data_payload["cluster-id"] = cluster_id
        if confederation_identifier is not None:
            data_payload["confederation-identifier"] = confederation_identifier
        if confederation_peers is not None:
            data_payload["confederation-peers"] = confederation_peers
        if dampening_route_map is not None:
            data_payload["dampening-route-map"] = dampening_route_map
        if dampening_reachability_half_life is not None:
            data_payload["dampening-reachability-half-life"] = (
                dampening_reachability_half_life
            )
        if dampening_reuse is not None:
            data_payload["dampening-reuse"] = dampening_reuse
        if dampening_suppress is not None:
            data_payload["dampening-suppress"] = dampening_suppress
        if dampening_max_suppress_time is not None:
            data_payload["dampening-max-suppress-time"] = (
                dampening_max_suppress_time
            )
        if dampening_unreachability_half_life is not None:
            data_payload["dampening-unreachability-half-life"] = (
                dampening_unreachability_half_life
            )
        if default_local_preference is not None:
            data_payload["default-local-preference"] = default_local_preference
        if scan_time is not None:
            data_payload["scan-time"] = scan_time
        if distance_external is not None:
            data_payload["distance-external"] = distance_external
        if distance_internal is not None:
            data_payload["distance-internal"] = distance_internal
        if distance_local is not None:
            data_payload["distance-local"] = distance_local
        if synchronization is not None:
            data_payload["synchronization"] = synchronization
        if graceful_restart is not None:
            data_payload["graceful-restart"] = graceful_restart
        if graceful_restart_time is not None:
            data_payload["graceful-restart-time"] = graceful_restart_time
        if graceful_stalepath_time is not None:
            data_payload["graceful-stalepath-time"] = graceful_stalepath_time
        if graceful_update_delay is not None:
            data_payload["graceful-update-delay"] = graceful_update_delay
        if graceful_end_on_timer is not None:
            data_payload["graceful-end-on-timer"] = graceful_end_on_timer
        if additional_path_select is not None:
            data_payload["additional-path-select"] = additional_path_select
        if additional_path_select6 is not None:
            data_payload["additional-path-select6"] = additional_path_select6
        if additional_path_select_vpnv4 is not None:
            data_payload["additional-path-select-vpnv4"] = (
                additional_path_select_vpnv4
            )
        if additional_path_select_vpnv6 is not None:
            data_payload["additional-path-select-vpnv6"] = (
                additional_path_select_vpnv6
            )
        if cross_family_conditional_adv is not None:
            data_payload["cross-family-conditional-adv"] = (
                cross_family_conditional_adv
            )
        if aggregate_address is not None:
            data_payload["aggregate-address"] = aggregate_address
        if aggregate_address6 is not None:
            data_payload["aggregate-address6"] = aggregate_address6
        if neighbor is not None:
            data_payload["neighbor"] = neighbor
        if neighbor_group is not None:
            data_payload["neighbor-group"] = neighbor_group
        if neighbor_range is not None:
            data_payload["neighbor-range"] = neighbor_range
        if neighbor_range6 is not None:
            data_payload["neighbor-range6"] = neighbor_range6
        if network is not None:
            data_payload["network"] = network
        if network6 is not None:
            data_payload["network6"] = network6
        if redistribute is not None:
            data_payload["redistribute"] = redistribute
        if redistribute6 is not None:
            data_payload["redistribute6"] = redistribute6
        if admin_distance is not None:
            data_payload["admin-distance"] = admin_distance
        if vrf is not None:
            data_payload["vr"] = vrf
        if vrf6 is not None:
            data_payload["vrf6"] = vrf6
        data_payload.update(kwargs)
        return self._client.put(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )
