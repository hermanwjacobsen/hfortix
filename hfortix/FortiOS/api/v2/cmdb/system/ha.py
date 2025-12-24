"""
FortiOS CMDB - Cmdb System Ha

Configuration endpoint for managing cmdb system ha objects.

API Endpoints:
    GET    /cmdb/system/ha
    PUT    /cmdb/system/ha/{identifier}

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.system.ha.get()
    >>>
    >>> # Get specific item (if supported)
    >>> item = fgt.api.cmdb.system.ha.get(name="item_name")
    >>>
    >>> # Create new item (use POST)
    >>> result = fgt.api.cmdb.system.ha.post(
    ...     name="new_item",
    ...     # ... additional parameters
    ... )
    >>>
    >>> # Update existing item (use PUT)
    >>> result = fgt.api.cmdb.system.ha.put(
    ...     name="existing_item",
    ...     # ... parameters to update
    ... )
    >>>
    >>> # Delete item
    >>> result = fgt.api.cmdb.system.ha.delete(name="item_name")

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


class Ha:
    """
    Ha Operations.

    Provides CRUD operations for FortiOS ha configuration.

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
        Initialize Ha endpoint.

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
        endpoint = "/system/ha"
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
        group_id: int | None = None,
        group_name: str | None = None,
        mode: str | None = None,
        sync_packet_balance: str | None = None,
        password: str | None = None,
        hbdev: str | None = None,
        auto_virtual_mac_interface: list | None = None,
        backup_hbdev: list | None = None,
        session_sync_dev: str | None = None,
        route_ttl: int | None = None,
        route_wait: int | None = None,
        route_hold: int | None = None,
        multicast_ttl: int | None = None,
        evpn_ttl: int | None = None,
        load_balance_all: str | None = None,
        sync_config: str | None = None,
        encryption: str | None = None,
        authentication: str | None = None,
        hb_interval: int | None = None,
        hb_interval_in_milliseconds: str | None = None,
        hb_lost_threshold: int | None = None,
        hello_holddown: int | None = None,
        gratuitous_arps: str | None = None,
        arps: int | None = None,
        arps_interval: int | None = None,
        session_pickup: str | None = None,
        session_pickup_connectionless: str | None = None,
        session_pickup_expectation: str | None = None,
        session_pickup_nat: str | None = None,
        session_pickup_delay: str | None = None,
        link_failed_signal: str | None = None,
        upgrade_mode: str | None = None,
        uninterruptible_primary_wait: int | None = None,
        standalone_mgmt_vdom: str | None = None,
        ha_mgmt_status: str | None = None,
        ha_mgmt_interfaces: list | None = None,
        ha_eth_type: str | None = None,
        hc_eth_type: str | None = None,
        l2ep_eth_type: str | None = None,
        ha_uptime_diff_margin: int | None = None,
        standalone_config_sync: str | None = None,
        logical_sn: str | None = None,
        schedule: str | None = None,
        weight: str | None = None,
        cpu_threshold: str | None = None,
        memory_threshold: str | None = None,
        http_proxy_threshold: str | None = None,
        ftp_proxy_threshold: str | None = None,
        imap_proxy_threshold: str | None = None,
        nntp_proxy_threshold: str | None = None,
        pop3_proxy_threshold: str | None = None,
        smtp_proxy_threshold: str | None = None,
        override: str | None = None,
        priority: int | None = None,
        override_wait_time: int | None = None,
        monitor: str | None = None,
        pingserver_monitor_interface: str | None = None,
        pingserver_failover_threshold: int | None = None,
        pingserver_secondary_force_reset: str | None = None,
        pingserver_flip_timeout: int | None = None,
        vcluster_status: str | None = None,
        vcluster: list | None = None,
        ha_direct: str | None = None,
        ssd_failover: str | None = None,
        memory_compatible_mode: str | None = None,
        memory_based_failover: str | None = None,
        memory_failover_threshold: int | None = None,
        memory_failover_monitor_period: int | None = None,
        memory_failover_sample_rate: int | None = None,
        memory_failover_flip_timeout: int | None = None,
        failover_hold_time: int | None = None,
        check_secondary_dev_health: str | None = None,
        ipsec_phase2_proposal: str | None = None,
        bounce_intf_upon_failover: str | None = None,
        status: str | None = None,
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
            group_id: HA group ID (0 - 1023; or 0 - 7 when there are more than
            2 vclusters). Must be the same for all members. (optional)
            group_name: Cluster group name. Must be the same for all members.
            (optional)
            mode: HA mode. Must be the same for all members. FGSP requires
            standalone. (optional)
            sync_packet_balance: Enable/disable HA packet distribution to
            multiple CPUs. (optional)
            password: Cluster password. Must be the same for all members.
            (optional)
            hbdev: Heartbeat interfaces. Must be the same for all members.
            (optional)
            auto_virtual_mac_interface: The physical interface that will be
            assigned an auto-generated virtual MAC address. (optional)
            backup_hbdev: Backup heartbeat interfaces. Must be the same for all
            members. (optional)
            session_sync_dev: Offload session-sync process to kernel and sync
            sessions using connected interface(s) directly. (optional)
            route_ttl: TTL for primary unit routes (5 - 3600 sec). Increase to
            maintain active routes during failover. (optional)
            route_wait: Time to wait before sending new routes to the cluster
            (0 - 3600 sec). (optional)
            route_hold: Time to wait between routing table updates to the
            cluster (0 - 3600 sec). (optional)
            multicast_ttl: HA multicast TTL on primary (5 - 3600 sec).
            (optional)
            evpn_ttl: HA EVPN FDB TTL on primary box (5 - 3600 sec). (optional)
            load_balance_all: Enable to load balance TCP sessions. Disable to
            load balance proxy sessions only. (optional)
            sync_config: Enable/disable configuration synchronization.
            (optional)
            encryption: Enable/disable heartbeat message encryption. (optional)
            authentication: Enable/disable heartbeat message authentication.
            (optional)
            hb_interval: Time between sending heartbeat packets (1 - 20).
            Increase to reduce false positives. (optional)
            hb_interval_in_milliseconds: Units of heartbeat interval time
            between sending heartbeat packets. Default is 100ms. (optional)
            hb_lost_threshold: Number of lost heartbeats to signal a failure (1
            - 60). Increase to reduce false positives. (optional)
            hello_holddown: Time to wait before changing from hello to work
            state (5 - 300 sec). (optional)
            gratuitous_arps: Enable/disable gratuitous ARPs. Disable if
            link-failed-signal enabled. (optional)
            arps: Number of gratuitous ARPs (1 - 60). Lower to reduce traffic.
            Higher to reduce failover time. (optional)
            arps_interval: Time between gratuitous ARPs (1 - 20 sec). Lower to
            reduce failover time. Higher to reduce traffic. (optional)
            session_pickup: Enable/disable session pickup. Enabling it can
            reduce session down time when fail over happens. (optional)
            session_pickup_connectionless: Enable/disable UDP and ICMP session
            sync. (optional)
            session_pickup_expectation: Enable/disable session helper
            expectation session sync for FGSP. (optional)
            session_pickup_nat: Enable/disable NAT session sync for FGSP.
            (optional)
            session_pickup_delay: Enable to sync sessions longer than 30 sec.
            Only longer lived sessions need to be synced. (optional)
            link_failed_signal: Enable to shut down all interfaces for 1 sec
            after a failover. Use if gratuitous ARPs do not update network.
            (optional)
            upgrade_mode: The mode to upgrade a cluster. (optional)
            uninterruptible_primary_wait: Number of minutes the primary HA unit
            waits before the secondary HA unit is considered upgraded and the
            system is started before starting its own upgrade (15 - 300,
            default = 30). (optional)
            standalone_mgmt_vdom: Enable/disable standalone management VDOM.
            (optional)
            ha_mgmt_status: Enable to reserve interfaces to manage individual
            cluster units. (optional)
            ha_mgmt_interfaces: Reserve interfaces to manage individual cluster
            units. (optional)
            ha_eth_type: HA heartbeat packet Ethertype (4-digit hex).
            (optional)
            hc_eth_type: Transparent mode HA heartbeat packet Ethertype
            (4-digit hex). (optional)
            l2ep_eth_type: Telnet session HA heartbeat packet Ethertype
            (4-digit hex). (optional)
            ha_uptime_diff_margin: Normally you would only reduce this value
            for failover testing. (optional)
            standalone_config_sync: Enable/disable FGSP configuration
            synchronization. (optional)
            logical_sn: Enable/disable usage of the logical serial number.
            (optional)
            schedule: Type of A-A load balancing. Use none if you have external
            load balancers. (optional)
            weight: Weight-round-robin weight for each cluster unit. Syntax
            <priority> <weight>. (optional)
            cpu_threshold: Dynamic weighted load balancing CPU usage weight and
            high and low thresholds. (optional)
            memory_threshold: Dynamic weighted load balancing memory usage
            weight and high and low thresholds. (optional)
            http_proxy_threshold: Dynamic weighted load balancing weight and
            high and low number of HTTP proxy sessions. (optional)
            ftp_proxy_threshold: Dynamic weighted load balancing weight and
            high and low number of FTP proxy sessions. (optional)
            imap_proxy_threshold: Dynamic weighted load balancing weight and
            high and low number of IMAP proxy sessions. (optional)
            nntp_proxy_threshold: Dynamic weighted load balancing weight and
            high and low number of NNTP proxy sessions. (optional)
            pop3_proxy_threshold: Dynamic weighted load balancing weight and
            high and low number of POP3 proxy sessions. (optional)
            smtp_proxy_threshold: Dynamic weighted load balancing weight and
            high and low number of SMTP proxy sessions. (optional)
            override: Enable and increase the priority of the unit that should
            always be primary (master). (optional)
            priority: Increase the priority to select the primary unit (0 -
            255). (optional)
            override_wait_time: Delay negotiating if override is enabled (0 -
            3600 sec). Reduces how often the cluster negotiates. (optional)
            monitor: Interfaces to check for port monitoring (or link failure).
            (optional)
            pingserver_monitor_interface: Interfaces to check for remote IP
            monitoring. (optional)
            pingserver_failover_threshold: Remote IP monitoring failover
            threshold (0 - 50). (optional)
            pingserver_secondary_force_reset: Enable to force the cluster to
            negotiate after a remote IP monitoring failover. (optional)
            pingserver_flip_timeout: Time to wait in minutes before
            renegotiating after a remote IP monitoring failover. (optional)
            vcluster_status: Enable/disable virtual cluster for virtual
            clustering. (optional)
            vcluster: Virtual cluster table. (optional)
            ha_direct: Enable/disable using ha-mgmt interface for syslog,
            remote authentication (RADIUS), FortiAnalyzer, FortiSandbox, sFlow,
            and Netflow. (optional)
            ssd_failover: Enable/disable automatic HA failover on SSD disk
            failure. (optional)
            memory_compatible_mode: Enable/disable memory compatible mode.
            (optional)
            memory_based_failover: Enable/disable memory based failover.
            (optional)
            memory_failover_threshold: Memory usage threshold to trigger memory
            based failover (0 means using conserve mode threshold in
            system.global). (optional)
            memory_failover_monitor_period: Duration of high memory usage
            before memory based failover is triggered in seconds (1 - 300,
            default = 60). (optional)
            memory_failover_sample_rate: Rate at which memory usage is sampled
            in order to measure memory usage in seconds (1 - 60, default = 1).
            (optional)
            memory_failover_flip_timeout: Time to wait between subsequent
            memory based failovers in minutes (6 - 2147483647, default = 6).
            (optional)
            failover_hold_time: Time to wait before failover (0 - 300 sec,
            default = 0), to avoid flip. (optional)
            check_secondary_dev_health: Enable/disable secondary dev health
            check for session load-balance in HA A-A mode. (optional)
            ipsec_phase2_proposal: IPsec phase2 proposal. (optional)
            bounce_intf_upon_failover: Enable/disable notification of kernel to
            bring down and up all monitored interfaces. The setting is used
            during failovers if gratuitous ARPs do not update the network.
            (optional)
            status: list ha status information (optional)
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
        endpoint = "/system/ha"
        if before is not None:
            data_payload["before"] = before
        if after is not None:
            data_payload["after"] = after
        if group_id is not None:
            data_payload["group-id"] = group_id
        if group_name is not None:
            data_payload["group-name"] = group_name
        if mode is not None:
            data_payload["mode"] = mode
        if sync_packet_balance is not None:
            data_payload["sync-packet-balance"] = sync_packet_balance
        if password is not None:
            data_payload["password"] = password
        if hbdev is not None:
            data_payload["hbdev"] = hbdev
        if auto_virtual_mac_interface is not None:
            data_payload["auto-virtual-mac-interface"] = (
                auto_virtual_mac_interface
            )
        if backup_hbdev is not None:
            data_payload["backup-hbdev"] = backup_hbdev
        if session_sync_dev is not None:
            data_payload["session-sync-dev"] = session_sync_dev
        if route_ttl is not None:
            data_payload["route-ttl"] = route_ttl
        if route_wait is not None:
            data_payload["route-wait"] = route_wait
        if route_hold is not None:
            data_payload["route-hold"] = route_hold
        if multicast_ttl is not None:
            data_payload["multicast-ttl"] = multicast_ttl
        if evpn_ttl is not None:
            data_payload["evpn-ttl"] = evpn_ttl
        if load_balance_all is not None:
            data_payload["load-balance-all"] = load_balance_all
        if sync_config is not None:
            data_payload["sync-config"] = sync_config
        if encryption is not None:
            data_payload["encryption"] = encryption
        if authentication is not None:
            data_payload["authentication"] = authentication
        if hb_interval is not None:
            data_payload["hb-interval"] = hb_interval
        if hb_interval_in_milliseconds is not None:
            data_payload["hb-interval-in-milliseconds"] = (
                hb_interval_in_milliseconds
            )
        if hb_lost_threshold is not None:
            data_payload["hb-lost-threshold"] = hb_lost_threshold
        if hello_holddown is not None:
            data_payload["hello-holddown"] = hello_holddown
        if gratuitous_arps is not None:
            data_payload["gratuitous-arps"] = gratuitous_arps
        if arps is not None:
            data_payload["arps"] = arps
        if arps_interval is not None:
            data_payload["arps-interval"] = arps_interval
        if session_pickup is not None:
            data_payload["session-pickup"] = session_pickup
        if session_pickup_connectionless is not None:
            data_payload["session-pickup-connectionless"] = (
                session_pickup_connectionless
            )
        if session_pickup_expectation is not None:
            data_payload["session-pickup-expectation"] = (
                session_pickup_expectation
            )
        if session_pickup_nat is not None:
            data_payload["session-pickup-nat"] = session_pickup_nat
        if session_pickup_delay is not None:
            data_payload["session-pickup-delay"] = session_pickup_delay
        if link_failed_signal is not None:
            data_payload["link-failed-signal"] = link_failed_signal
        if upgrade_mode is not None:
            data_payload["upgrade-mode"] = upgrade_mode
        if uninterruptible_primary_wait is not None:
            data_payload["uninterruptible-primary-wait"] = (
                uninterruptible_primary_wait
            )
        if standalone_mgmt_vdom is not None:
            data_payload["standalone-mgmt-vdom"] = standalone_mgmt_vdom
        if ha_mgmt_status is not None:
            data_payload["ha-mgmt-status"] = ha_mgmt_status
        if ha_mgmt_interfaces is not None:
            data_payload["ha-mgmt-interfaces"] = ha_mgmt_interfaces
        if ha_eth_type is not None:
            data_payload["ha-eth-type"] = ha_eth_type
        if hc_eth_type is not None:
            data_payload["hc-eth-type"] = hc_eth_type
        if l2ep_eth_type is not None:
            data_payload["l2ep-eth-type"] = l2ep_eth_type
        if ha_uptime_diff_margin is not None:
            data_payload["ha-uptime-diff-margin"] = ha_uptime_diff_margin
        if standalone_config_sync is not None:
            data_payload["standalone-config-sync"] = standalone_config_sync
        if logical_sn is not None:
            data_payload["logical-sn"] = logical_sn
        if schedule is not None:
            data_payload["schedule"] = schedule
        if weight is not None:
            data_payload["weight"] = weight
        if cpu_threshold is not None:
            data_payload["cpu-threshold"] = cpu_threshold
        if memory_threshold is not None:
            data_payload["memory-threshold"] = memory_threshold
        if http_proxy_threshold is not None:
            data_payload["http-proxy-threshold"] = http_proxy_threshold
        if ftp_proxy_threshold is not None:
            data_payload["ftp-proxy-threshold"] = ftp_proxy_threshold
        if imap_proxy_threshold is not None:
            data_payload["imap-proxy-threshold"] = imap_proxy_threshold
        if nntp_proxy_threshold is not None:
            data_payload["nntp-proxy-threshold"] = nntp_proxy_threshold
        if pop3_proxy_threshold is not None:
            data_payload["pop3-proxy-threshold"] = pop3_proxy_threshold
        if smtp_proxy_threshold is not None:
            data_payload["smtp-proxy-threshold"] = smtp_proxy_threshold
        if override is not None:
            data_payload["override"] = override
        if priority is not None:
            data_payload["priority"] = priority
        if override_wait_time is not None:
            data_payload["override-wait-time"] = override_wait_time
        if monitor is not None:
            data_payload["monitor"] = monitor
        if pingserver_monitor_interface is not None:
            data_payload["pingserver-monitor-interface"] = (
                pingserver_monitor_interface
            )
        if pingserver_failover_threshold is not None:
            data_payload["pingserver-failover-threshold"] = (
                pingserver_failover_threshold
            )
        if pingserver_secondary_force_reset is not None:
            data_payload["pingserver-secondary-force-reset"] = (
                pingserver_secondary_force_reset
            )
        if pingserver_flip_timeout is not None:
            data_payload["pingserver-flip-timeout"] = pingserver_flip_timeout
        if vcluster_status is not None:
            data_payload["vcluster-status"] = vcluster_status
        if vcluster is not None:
            data_payload["vcluster"] = vcluster
        if ha_direct is not None:
            data_payload["ha-direct"] = ha_direct
        if ssd_failover is not None:
            data_payload["ssd-failover"] = ssd_failover
        if memory_compatible_mode is not None:
            data_payload["memory-compatible-mode"] = memory_compatible_mode
        if memory_based_failover is not None:
            data_payload["memory-based-failover"] = memory_based_failover
        if memory_failover_threshold is not None:
            data_payload["memory-failover-threshold"] = (
                memory_failover_threshold
            )
        if memory_failover_monitor_period is not None:
            data_payload["memory-failover-monitor-period"] = (
                memory_failover_monitor_period
            )
        if memory_failover_sample_rate is not None:
            data_payload["memory-failover-sample-rate"] = (
                memory_failover_sample_rate
            )
        if memory_failover_flip_timeout is not None:
            data_payload["memory-failover-flip-timeout"] = (
                memory_failover_flip_timeout
            )
        if failover_hold_time is not None:
            data_payload["failover-hold-time"] = failover_hold_time
        if check_secondary_dev_health is not None:
            data_payload["check-secondary-dev-health"] = (
                check_secondary_dev_health
            )
        if ipsec_phase2_proposal is not None:
            data_payload["ipsec-phase2-proposal"] = ipsec_phase2_proposal
        if bounce_intf_upon_failover is not None:
            data_payload["bounce-intf-upon-failover"] = (
                bounce_intf_upon_failover
            )
        if status is not None:
            data_payload["status"] = status
        data_payload.update(kwargs)
        return self._client.put(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )
