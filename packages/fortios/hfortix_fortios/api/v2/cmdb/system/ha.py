"""
FortiOS CMDB - System ha

Configuration endpoint for managing cmdb system/ha objects.

API Endpoints:
    GET    /cmdb/system/ha
    POST   /cmdb/system/ha
    PUT    /cmdb/system/ha/{identifier}
    DELETE /cmdb/system/ha/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.system_ha.get()
    >>>
    >>> # Create with auto-normalization (strings/lists converted automatically)
    >>> result = fgt.api.cmdb.system_ha.post(
    ...     name="example",
    ...     srcintf="port1",  # Auto-converted to [{'name': 'port1'}]
    ...     dstintf=["port2", "port3"],  # Auto-converted to list of dicts
    ... )

Important:
    - Use **POST** to create new objects
    - Use **PUT** to update existing objects
    - Use **GET** to retrieve configuration
    - Use **DELETE** to remove objects
    - **Auto-normalization**: List fields accept strings or lists, automatically
      converted to FortiOS format [{'name': '...'}]
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Union

if TYPE_CHECKING:
    from collections.abc import Coroutine
    from hfortix_core.http.interface import IHTTPClient
    from hfortix_fortios.models import FortiObject

# Import helper functions from central _helpers module
from hfortix_fortios._helpers import (
    build_api_payload,
    build_cmdb_payload,  # Keep for backward compatibility / manual usage
    is_success,
    normalize_table_field,  # For table field normalization
)
# Import metadata mixin for schema introspection
from hfortix_fortios._helpers.metadata_mixin import MetadataMixin

# Import Protocol-based type hints (eliminates need for local @overload decorators)
from hfortix_fortios._protocols import CRUDEndpoint

class Ha(CRUDEndpoint, MetadataMixin):
    """Ha Operations."""
    
    # Configure metadata mixin to use this endpoint's helper module
    _helper_module_name = "ha"
    
    # ========================================================================
    # Table Fields Metadata (for normalization)
    # Auto-generated from schema - supports flexible input formats
    # ========================================================================
    _TABLE_FIELDS = {
        "auto_virtual_mac_interface": {
            "mkey": "interface-name",
            "required_fields": ['interface-name'],
            "example": "[{'interface-name': 'value'}]",
        },
        "backup_hbdev": {
            "mkey": "name",
            "required_fields": ['name'],
            "example": "[{'name': 'value'}]",
        },
        "ha_mgmt_interfaces": {
            "mkey": "id",
            "required_fields": ['interface'],
            "example": "[{'interface': 'value'}]",
        },
        "unicast_peers": {
            "mkey": "id",
            "required_fields": ['id'],
            "example": "[{'id': 1}]",
        },
        "vcluster": {
            "mkey": "vcluster-id",
            "required_fields": ['vcluster-id'],
            "example": "[{'vcluster-id': 1}]",
        },
    }
    
    # ========================================================================
    # Capabilities (from schema metadata)
    # ========================================================================
    SUPPORTS_CREATE = False
    SUPPORTS_READ = True
    SUPPORTS_UPDATE = True
    SUPPORTS_DELETE = False
    SUPPORTS_MOVE = True
    SUPPORTS_CLONE = True
    SUPPORTS_FILTERING = True
    SUPPORTS_PAGINATION = True
    SUPPORTS_SEARCH = False
    SUPPORTS_SORTING = False

    def __init__(self, client: "IHTTPClient"):
        """Initialize Ha endpoint."""
        self._client = client

    # ========================================================================
    # GET Method
    # Type hints provided by CRUDEndpoint protocol (no local @overload needed)
    # ========================================================================
    
    def get(
        self,
        name: str | None = None,
        filter: list[str] | None = None,
        count: int | None = None,
        start: int | None = None,
        q_datasource: bool | None = None,
        q_skip_to: int | None = None,
        q_with_meta: bool | None = None,
        q_with_contents_hash: bool | None = None,
        q_skip: bool | None = None,
        q_format: list[str] | None = None,
        q_key: str | None = None,
        q_pattern: str | None = None,
        q_scope: str | None = None,
        q_exclude_default_values: bool | None = None,
        q_datasource_format: dict[str, Any] | None = None,
        q_unfiltered_count: int | None = None,
        q_stat_items: str | None = None,
        q_primary_keys: str | None = None,
        q_action: Literal["default", "schema"] | None = None,
        payload_dict: dict[str, Any] | None = None,
        vdom: str | bool | None = None,
        error_mode: Literal["raise", "return", "print"] | None = None,
        error_format: Literal["detailed", "simple", "code_only"] | None = None,
    ):  # type: ignore[no-untyped-def]
        """
        Retrieve system/ha configuration.

        Configure HA.

        Args:
            name: Name identifier to retrieve specific object. If None, returns all objects.
            filter: List of filter expressions to limit results.
                Each filter uses format: "field==value" or "field!=value"
                Operators: ==, !=, =@ (contains), !@ (not contains), <=, <, >=, >
                Multiple filters use AND logic. For OR, use comma in single string.
                Example: ["name==test", "status==enable"] or ["name==test,name==prod"]
            count: Maximum number of entries to return (pagination).
            start: Starting entry index for pagination (0-based).
            payload_dict: Additional query parameters for advanced options:
                - datasource (bool): Include datasource information
                - with_meta (bool): Include metadata about each object
                - with_contents_hash (bool): Include checksum of object contents
                - format (list[str]): Property names to include (e.g., ["policyid", "srcintf"])
                - scope (str): Query scope - "global", "vdom", or "both"
                - action (str): Special actions - "schema", "default"
                See FortiOS REST API documentation for complete list.
            vdom: Virtual domain name. Use True for global, string for specific VDOM, None for default.
            error_mode: Override client-level error_mode. "raise" raises exceptions, "return" returns error dict, "print" prints errors.
            error_format: Override client-level error_format. "detailed" provides full context, "simple" is concise, "code_only" returns just status code.

        Returns:
            FortiObject instance or list of FortiObject instances. Returns Coroutine if using async client.
            Use .dict, .json, or .raw properties to access as dictionary.
            
            Response structure:
                - http_method: GET
                - results: Configuration object(s)
                - vdom: Virtual domain
                - path: API path
                - name: Object name (single object queries)
                - status: success/error
                - http_status: HTTP status code
                - build: FortiOS build number

        Examples:
            >>> # Get all system/ha objects
            >>> result = fgt.api.cmdb.system_ha.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.system_ha.get(
            ...     filter=["name==test", "status==enable"]
            ... )
            
            >>> # Get with pagination
            >>> result = fgt.api.cmdb.system_ha.get(
            ...     start=0, count=100
            ... )
            
            >>> # Get schema information  
            >>> schema = fgt.api.cmdb.system_ha.get_schema()

        See Also:
            - post(): Create new system/ha object
            - put(): Update existing system/ha object
            - delete(): Remove system/ha object
            - exists(): Check if object exists
            - get_schema(): Get endpoint schema/metadata
        """
        params = payload_dict.copy() if payload_dict else {}
        
        # Add explicit query parameters
        if filter is not None:
            params["filter"] = filter
        if count is not None:
            params["count"] = count
        if start is not None:
            params["start"] = start
        if q_datasource is not None:
            params["datasource"] = q_datasource
        if q_skip_to is not None:
            params["skip_to"] = q_skip_to
        if q_with_meta is not None:
            params["with_meta"] = q_with_meta
        if q_with_contents_hash is not None:
            params["with_contents_hash"] = q_with_contents_hash
        if q_skip is not None:
            params["skip"] = q_skip
        if q_format is not None:
            params["format"] = q_format
        if q_key is not None:
            params["key"] = q_key
        if q_pattern is not None:
            params["pattern"] = q_pattern
        if q_scope is not None:
            params["scope"] = q_scope
        if q_exclude_default_values is not None:
            params["exclude-default-values"] = q_exclude_default_values
        if q_datasource_format is not None:
            params["datasource_format"] = q_datasource_format
        if q_unfiltered_count is not None:
            params["unfiltered_count"] = q_unfiltered_count
        if q_stat_items is not None:
            params["stat-items"] = q_stat_items
        if q_primary_keys is not None:
            params["primary_keys"] = q_primary_keys
        if q_action is not None:
            params["action"] = q_action
        
        if name:
            endpoint = f"/system/ha/{name}"
            unwrap_single = True
        else:
            endpoint = "/system/ha"
            unwrap_single = False
        
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, unwrap_single=unwrap_single
        )

    def get_schema(
        self,
        vdom: str | None = None,
        format: str = "schema",
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Get schema/metadata for this endpoint.
        
        Returns the FortiOS schema definition including available fields,
        their types, required vs optional properties, enum values, nested
        structures, and default values.
        
        This queries the live firewall for its current schema, which may
        vary between FortiOS versions.
        
        Args:
            vdom: Virtual domain. None uses default VDOM.
            format: Schema format - "schema" (FortiOS native) or "json-schema" (JSON Schema standard).
                Defaults to "schema".
                
        Returns:
            Schema definition as dict. Returns Coroutine if using async client.
            
        Example:
            >>> # Get FortiOS native schema
            >>> schema = fgt.api.cmdb.system_ha.get_schema()
            >>> print(schema['results'])
            
            >>> # Get JSON Schema format (if supported)
            >>> json_schema = fgt.api.cmdb.system_ha.get_schema(format="json-schema")
        
        Note:
            Not all endpoints support all schema formats. The "schema" format
            is most widely supported.
        """
        return self.get(action=format, vdom=vdom)


    # ========================================================================
    # PUT Method
    # Type hints provided by CRUDEndpoint protocol (no local @overload needed)
    # ========================================================================
    
    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        group_id: int | None = None,
        group_name: str | None = None,
        mode: Literal["standalone", "a-a", "a-p"] | None = None,
        sync_packet_balance: Literal["enable", "disable"] | None = None,
        password: Any | None = None,
        key: Any | None = None,
        hbdev: str | list[str] | None = None,
        auto_virtual_mac_interface: str | list[str] | list[dict[str, Any]] | None = None,
        backup_hbdev: str | list[str] | list[dict[str, Any]] | None = None,
        unicast_hb: Literal["enable", "disable"] | None = None,
        unicast_hb_peerip: str | None = None,
        unicast_hb_netmask: str | None = None,
        session_sync_dev: str | list[str] | None = None,
        route_ttl: int | None = None,
        route_wait: int | None = None,
        route_hold: int | None = None,
        multicast_ttl: int | None = None,
        evpn_ttl: int | None = None,
        load_balance_all: Literal["enable", "disable"] | None = None,
        sync_config: Literal["enable", "disable"] | None = None,
        encryption: Literal["enable", "disable"] | None = None,
        authentication: Literal["enable", "disable"] | None = None,
        hb_interval: int | None = None,
        hb_interval_in_milliseconds: Literal["100ms", "10ms"] | None = None,
        hb_lost_threshold: int | None = None,
        hello_holddown: int | None = None,
        gratuitous_arps: Literal["enable", "disable"] | None = None,
        arps: int | None = None,
        arps_interval: int | None = None,
        session_pickup: Literal["enable", "disable"] | None = None,
        session_pickup_connectionless: Literal["enable", "disable"] | None = None,
        session_pickup_expectation: Literal["enable", "disable"] | None = None,
        session_pickup_nat: Literal["enable", "disable"] | None = None,
        session_pickup_delay: Literal["enable", "disable"] | None = None,
        link_failed_signal: Literal["enable", "disable"] | None = None,
        upgrade_mode: Literal["simultaneous", "uninterruptible", "local-only", "secondary-only"] | None = None,
        uninterruptible_primary_wait: int | None = None,
        standalone_mgmt_vdom: Literal["enable", "disable"] | None = None,
        ha_mgmt_status: Literal["enable", "disable"] | None = None,
        ha_mgmt_interfaces: str | list[str] | list[dict[str, Any]] | None = None,
        ha_eth_type: str | None = None,
        hc_eth_type: str | None = None,
        l2ep_eth_type: str | None = None,
        ha_uptime_diff_margin: int | None = None,
        standalone_config_sync: Literal["enable", "disable"] | None = None,
        unicast_status: Literal["enable", "disable"] | None = None,
        unicast_gateway: str | None = None,
        unicast_peers: str | list[str] | list[dict[str, Any]] | None = None,
        schedule: Literal["none", "leastconnection", "round-robin", "weight-round-robin", "random", "ip", "ipport"] | None = None,
        weight: str | None = None,
        cpu_threshold: str | None = None,
        memory_threshold: str | None = None,
        http_proxy_threshold: str | None = None,
        ftp_proxy_threshold: str | None = None,
        imap_proxy_threshold: str | None = None,
        nntp_proxy_threshold: str | None = None,
        pop3_proxy_threshold: str | None = None,
        smtp_proxy_threshold: str | None = None,
        override: Literal["enable", "disable"] | None = None,
        priority: int | None = None,
        override_wait_time: int | None = None,
        monitor: str | list[str] | None = None,
        pingserver_monitor_interface: str | list[str] | None = None,
        pingserver_failover_threshold: int | None = None,
        pingserver_secondary_force_reset: Literal["enable", "disable"] | None = None,
        pingserver_flip_timeout: int | None = None,
        vcluster_status: Literal["enable", "disable"] | None = None,
        vcluster: str | list[str] | list[dict[str, Any]] | None = None,
        ha_direct: Literal["enable", "disable"] | None = None,
        ssd_failover: Literal["enable", "disable"] | None = None,
        memory_compatible_mode: Literal["enable", "disable"] | None = None,
        memory_based_failover: Literal["enable", "disable"] | None = None,
        memory_failover_threshold: int | None = None,
        memory_failover_monitor_period: int | None = None,
        memory_failover_sample_rate: int | None = None,
        memory_failover_flip_timeout: int | None = None,
        failover_hold_time: int | None = None,
        check_secondary_dev_health: Literal["enable", "disable"] | None = None,
        ipsec_phase2_proposal: Literal["aes128-sha1", "aes128-sha256", "aes128-sha384", "aes128-sha512", "aes192-sha1", "aes192-sha256", "aes192-sha384", "aes192-sha512", "aes256-sha1", "aes256-sha256", "aes256-sha384", "aes256-sha512", "aes128gcm", "aes256gcm", "chacha20poly1305"] | list[str] | None = None,
        bounce_intf_upon_failover: Literal["enable", "disable"] | None = None,
        status: Any | None = None,
        q_action: Literal["move"] | None = None,
        q_before: str | None = None,
        q_after: str | None = None,
        q_scope: str | None = None,
        vdom: str | bool | None = None,
        error_mode: Literal["raise", "return", "print"] | None = None,
        error_format: Literal["detailed", "simple", "code_only"] | None = None,
    ):  # type: ignore[no-untyped-def]
        """
        Update existing system/ha object.

        Configure HA.

        Args:
            payload_dict: Object data as dict. Must include name (primary key).
            group_id: HA group ID  (0 - 1023;  or 0 - 7 when there are more than 2 vclusters). Must be the same for all members.
            group_name: Cluster group name. Must be the same for all members.
            mode: HA mode. Must be the same for all members. FGSP requires standalone.
            sync_packet_balance: Enable/disable HA packet distribution to multiple CPUs.
            password: Cluster password. Must be the same for all members.
            key: Key.
            hbdev: Heartbeat interfaces. Must be the same for all members.
            auto_virtual_mac_interface: The physical interface that will be assigned an auto-generated virtual MAC address.
                Default format: [{'interface-name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'interface-name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'interface-name': 'val1'}, ...]
                  - List of dicts: [{'interface-name': 'value'}] (recommended)
            backup_hbdev: Backup heartbeat interfaces. Must be the same for all members.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            unicast_hb: Enable/disable unicast heartbeat.
            unicast_hb_peerip: Unicast heartbeat peer IP.
            unicast_hb_netmask: Unicast heartbeat netmask.
            session_sync_dev: Offload session-sync process to kernel and sync sessions using connected interface(s) directly.
            route_ttl: TTL for primary unit routes (5 - 3600 sec). Increase to maintain active routes during failover.
            route_wait: Time to wait before sending new routes to the cluster (0 - 3600 sec).
            route_hold: Time to wait between routing table updates to the cluster (0 - 3600 sec).
            multicast_ttl: HA multicast TTL on primary (5 - 3600 sec).
            evpn_ttl: HA EVPN FDB TTL on primary box (5 - 3600 sec).
            load_balance_all: Enable to load balance TCP sessions. Disable to load balance proxy sessions only.
            sync_config: Enable/disable configuration synchronization.
            encryption: Enable/disable heartbeat message encryption.
            authentication: Enable/disable heartbeat message authentication.
            hb_interval: Time between sending heartbeat packets (1 - 20). Increase to reduce false positives.
            hb_interval_in_milliseconds: Units of heartbeat interval time between sending heartbeat packets. Default is 100ms.
            hb_lost_threshold: Number of lost heartbeats to signal a failure (1 - 60). Increase to reduce false positives.
            hello_holddown: Time to wait before changing from hello to work state (5 - 300 sec).
            gratuitous_arps: Enable/disable gratuitous ARPs. Disable if link-failed-signal enabled.
            arps: Number of gratuitous ARPs (1 - 60). Lower to reduce traffic. Higher to reduce failover time.
            arps_interval: Time between gratuitous ARPs  (1 - 20 sec). Lower to reduce failover time. Higher to reduce traffic.
            session_pickup: Enable/disable session pickup. Enabling it can reduce session down time when fail over happens.
            session_pickup_connectionless: Enable/disable UDP and ICMP session sync.
            session_pickup_expectation: Enable/disable session helper expectation session sync for FGSP.
            session_pickup_nat: Enable/disable NAT session sync for FGSP.
            session_pickup_delay: Enable to sync sessions longer than 30 sec. Only longer lived sessions need to be synced.
            link_failed_signal: Enable to shut down all interfaces for 1 sec after a failover. Use if gratuitous ARPs do not update network.
            upgrade_mode: The mode to upgrade a cluster.
            uninterruptible_primary_wait: Number of minutes the primary HA unit waits before the secondary HA unit is considered upgraded and the system is started before starting its own upgrade (15 - 300, default = 30).
            standalone_mgmt_vdom: Enable/disable standalone management VDOM.
            ha_mgmt_status: Enable to reserve interfaces to manage individual cluster units.
            ha_mgmt_interfaces: Reserve interfaces to manage individual cluster units.
                Default format: [{'interface': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'id': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'id': 'val1'}, ...]
                  - List of dicts: [{'interface': 'value'}] (recommended)
            ha_eth_type: HA heartbeat packet Ethertype (4-digit hex).
            hc_eth_type: Transparent mode HA heartbeat packet Ethertype (4-digit hex).
            l2ep_eth_type: Telnet session HA heartbeat packet Ethertype (4-digit hex).
            ha_uptime_diff_margin: Normally you would only reduce this value for failover testing.
            standalone_config_sync: Enable/disable FGSP configuration synchronization.
            unicast_status: Enable/disable unicast connection.
            unicast_gateway: Default route gateway for unicast interface.
            unicast_peers: Number of unicast peers.
                Default format: [{'id': 1}]
                Supported formats:
                  - Single string: "value" → [{'id': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'id': 'val1'}, ...]
                  - List of dicts: [{'id': 1}] (recommended)
            schedule: Type of A-A load balancing. Use none if you have external load balancers.
            weight: Weight-round-robin weight for each cluster unit. Syntax <priority> <weight>.
            cpu_threshold: Dynamic weighted load balancing CPU usage weight and high and low thresholds.
            memory_threshold: Dynamic weighted load balancing memory usage weight and high and low thresholds.
            http_proxy_threshold: Dynamic weighted load balancing weight and high and low number of HTTP proxy sessions.
            ftp_proxy_threshold: Dynamic weighted load balancing weight and high and low number of FTP proxy sessions.
            imap_proxy_threshold: Dynamic weighted load balancing weight and high and low number of IMAP proxy sessions.
            nntp_proxy_threshold: Dynamic weighted load balancing weight and high and low number of NNTP proxy sessions.
            pop3_proxy_threshold: Dynamic weighted load balancing weight and high and low number of POP3 proxy sessions.
            smtp_proxy_threshold: Dynamic weighted load balancing weight and high and low number of SMTP proxy sessions.
            override: Enable and increase the priority of the unit that should always be primary (master).
            priority: Increase the priority to select the primary unit (0 - 255).
            override_wait_time: Delay negotiating if override is enabled (0 - 3600 sec). Reduces how often the cluster negotiates.
            monitor: Interfaces to check for port monitoring (or link failure).
            pingserver_monitor_interface: Interfaces to check for remote IP monitoring.
            pingserver_failover_threshold: Remote IP monitoring failover threshold (0 - 50).
            pingserver_secondary_force_reset: Enable to force the cluster to negotiate after a remote IP monitoring failover.
            pingserver_flip_timeout: Time to wait in minutes before renegotiating after a remote IP monitoring failover.
            vcluster_status: Enable/disable virtual cluster for virtual clustering.
            vcluster: Virtual cluster table.
                Default format: [{'vcluster-id': 1}]
                Supported formats:
                  - Single string: "value" → [{'vcluster-id': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'vcluster-id': 'val1'}, ...]
                  - List of dicts: [{'vcluster-id': 1}] (recommended)
            ha_direct: Enable/disable using ha-mgmt interface for syslog, remote authentication (RADIUS), FortiAnalyzer, FortiSandbox, sFlow, and Netflow.
            ssd_failover: Enable/disable automatic HA failover on SSD disk failure.
            memory_compatible_mode: Enable/disable memory compatible mode.
            memory_based_failover: Enable/disable memory based failover.
            memory_failover_threshold: Memory usage threshold to trigger memory based failover (0 means using conserve mode threshold in system.global).
            memory_failover_monitor_period: Duration of high memory usage before memory based failover is triggered in seconds (1 - 300, default = 60).
            memory_failover_sample_rate: Rate at which memory usage is sampled in order to measure memory usage in seconds (1 - 60, default = 1).
            memory_failover_flip_timeout: Time to wait between subsequent memory based failovers in minutes (6 - 2147483647, default = 6).
            failover_hold_time: Time to wait before failover (0 - 300 sec, default = 0), to avoid flip.
            check_secondary_dev_health: Enable/disable secondary dev health check for session load-balance in HA A-A mode.
            ipsec_phase2_proposal: IPsec phase2 proposal.
            bounce_intf_upon_failover: Enable/disable notification of kernel to bring down and up all monitored interfaces. The setting is used during failovers if gratuitous ARPs do not update the network.
            status: list ha status information
            vdom: Virtual domain name.
            error_mode: Override client-level error_mode. "raise" raises exceptions, "return" returns error dict, "print" prints errors.
            error_format: Override client-level error_format. "detailed" provides full context, "simple" is concise, "code_only" returns just status code.

        Returns:
            FortiObject instance. Use .dict, .json, or .raw to access as dictionary.

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.system_ha.put(
            ...     name="existing-object",
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "name": "existing-object",
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.system_ha.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Apply normalization for table fields (supports flexible input formats)
        if auto_virtual_mac_interface is not None:
            auto_virtual_mac_interface = normalize_table_field(
                auto_virtual_mac_interface,
                mkey="interface-name",
                required_fields=['interface-name'],
                field_name="auto_virtual_mac_interface",
                example="[{'interface-name': 'value'}]",
            )
        if backup_hbdev is not None:
            backup_hbdev = normalize_table_field(
                backup_hbdev,
                mkey="name",
                required_fields=['name'],
                field_name="backup_hbdev",
                example="[{'name': 'value'}]",
            )
        if ha_mgmt_interfaces is not None:
            ha_mgmt_interfaces = normalize_table_field(
                ha_mgmt_interfaces,
                mkey="id",
                required_fields=['interface'],
                field_name="ha_mgmt_interfaces",
                example="[{'interface': 'value'}]",
            )
        if unicast_peers is not None:
            unicast_peers = normalize_table_field(
                unicast_peers,
                mkey="id",
                required_fields=['id'],
                field_name="unicast_peers",
                example="[{'id': 1}]",
            )
        if vcluster is not None:
            vcluster = normalize_table_field(
                vcluster,
                mkey="vcluster-id",
                required_fields=['vcluster-id'],
                field_name="vcluster",
                example="[{'vcluster-id': 1}]",
            )
        
        # Build payload using helper function with auto-normalization
        # This automatically converts strings/lists to [{'name': '...'}] format for list fields
        # To disable auto-normalization, use build_cmdb_payload directly
        payload_data = build_api_payload(
            group_id=group_id,
            group_name=group_name,
            mode=mode,
            sync_packet_balance=sync_packet_balance,
            password=password,
            key=key,
            hbdev=hbdev,
            auto_virtual_mac_interface=auto_virtual_mac_interface,
            backup_hbdev=backup_hbdev,
            unicast_hb=unicast_hb,
            unicast_hb_peerip=unicast_hb_peerip,
            unicast_hb_netmask=unicast_hb_netmask,
            session_sync_dev=session_sync_dev,
            route_ttl=route_ttl,
            route_wait=route_wait,
            route_hold=route_hold,
            multicast_ttl=multicast_ttl,
            evpn_ttl=evpn_ttl,
            load_balance_all=load_balance_all,
            sync_config=sync_config,
            encryption=encryption,
            authentication=authentication,
            hb_interval=hb_interval,
            hb_interval_in_milliseconds=hb_interval_in_milliseconds,
            hb_lost_threshold=hb_lost_threshold,
            hello_holddown=hello_holddown,
            gratuitous_arps=gratuitous_arps,
            arps=arps,
            arps_interval=arps_interval,
            session_pickup=session_pickup,
            session_pickup_connectionless=session_pickup_connectionless,
            session_pickup_expectation=session_pickup_expectation,
            session_pickup_nat=session_pickup_nat,
            session_pickup_delay=session_pickup_delay,
            link_failed_signal=link_failed_signal,
            upgrade_mode=upgrade_mode,
            uninterruptible_primary_wait=uninterruptible_primary_wait,
            standalone_mgmt_vdom=standalone_mgmt_vdom,
            ha_mgmt_status=ha_mgmt_status,
            ha_mgmt_interfaces=ha_mgmt_interfaces,
            ha_eth_type=ha_eth_type,
            hc_eth_type=hc_eth_type,
            l2ep_eth_type=l2ep_eth_type,
            ha_uptime_diff_margin=ha_uptime_diff_margin,
            standalone_config_sync=standalone_config_sync,
            unicast_status=unicast_status,
            unicast_gateway=unicast_gateway,
            unicast_peers=unicast_peers,
            schedule=schedule,
            weight=weight,
            cpu_threshold=cpu_threshold,
            memory_threshold=memory_threshold,
            http_proxy_threshold=http_proxy_threshold,
            ftp_proxy_threshold=ftp_proxy_threshold,
            imap_proxy_threshold=imap_proxy_threshold,
            nntp_proxy_threshold=nntp_proxy_threshold,
            pop3_proxy_threshold=pop3_proxy_threshold,
            smtp_proxy_threshold=smtp_proxy_threshold,
            override=override,
            priority=priority,
            override_wait_time=override_wait_time,
            monitor=monitor,
            pingserver_monitor_interface=pingserver_monitor_interface,
            pingserver_failover_threshold=pingserver_failover_threshold,
            pingserver_secondary_force_reset=pingserver_secondary_force_reset,
            pingserver_flip_timeout=pingserver_flip_timeout,
            vcluster_status=vcluster_status,
            vcluster=vcluster,
            ha_direct=ha_direct,
            ssd_failover=ssd_failover,
            memory_compatible_mode=memory_compatible_mode,
            memory_based_failover=memory_based_failover,
            memory_failover_threshold=memory_failover_threshold,
            memory_failover_monitor_period=memory_failover_monitor_period,
            memory_failover_sample_rate=memory_failover_sample_rate,
            memory_failover_flip_timeout=memory_failover_flip_timeout,
            failover_hold_time=failover_hold_time,
            check_secondary_dev_health=check_secondary_dev_health,
            ipsec_phase2_proposal=ipsec_phase2_proposal,
            bounce_intf_upon_failover=bounce_intf_upon_failover,
            status=status,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.ha import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/system/ha",
            )
        
        # Singleton endpoint - no identifier needed
        endpoint = "/system/ha"

        # Add explicit query parameters for PUT
        params: dict[str, Any] = {}
        if q_action is not None:
            params["action"] = q_action
        if q_before is not None:
            params["before"] = q_before
        if q_after is not None:
            params["after"] = q_after
        if q_scope is not None:
            params["scope"] = q_scope
        
        return self._client.put(
            "cmdb", endpoint, data=payload_data, params=params, vdom=vdom
        )





    # ========================================================================
    # Action: Move
    # ========================================================================
    
    def move(
        self,
        name: str,
        action: Literal["before", "after"],
        reference_name: str,
        vdom: str | bool | None = None,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Move system/ha object to a new position.
        
        Reorders objects by moving one before or after another.
        
        Args:
            name: Name of object to move
            action: Move "before" or "after" reference object
            reference_name: Name of reference object
            vdom: Virtual domain name
            **kwargs: Additional parameters
            
        Returns:
            API response dictionary
            
        Example:
            >>> # Move policy 100 before policy 50
            >>> fgt.api.cmdb.system_ha.move(
            ...     name="object1",
            ...     action="before",
            ...     reference_name="object2"
            ... )
        """
        return self._client.request(
            method="PUT",
            path=f"/api/v2/cmdb/system/ha",
            params={
                "name": name,
                "action": "move",
                action: reference_name,
                "vdom": vdom,
                **kwargs,
            },
        )

    # ========================================================================
    # Action: Clone
    # ========================================================================
    
    def clone(
        self,
        name: str,
        new_name: str,
        vdom: str | bool | None = None,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Clone system/ha object.
        
        Creates a copy of an existing object with a new identifier.
        
        Args:
            name: Name of object to clone
            new_name: Name for the cloned object
            vdom: Virtual domain name
            **kwargs: Additional parameters
            
        Returns:
            API response dictionary
            
        Example:
            >>> # Clone an existing object
            >>> fgt.api.cmdb.system_ha.clone(
            ...     name="template",
            ...     new_name="new-from-template"
            ... )
        """
        return self._client.request(
            method="POST",
            path=f"/api/v2/cmdb/system/ha",
            params={
                "name": name,
                "new_name": new_name,
                "action": "clone",
                "vdom": vdom,
                **kwargs,
            },
        )

    # ========================================================================
    # Helper: Check Existence
    # ========================================================================
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = None,
    ) -> bool:
        """
        Check if system/ha object exists.
        
        Args:
            name: Name to check
            vdom: Virtual domain name
            
        Returns:
            True if object exists, False otherwise
            
        Example:
            >>> # Check before creating
            >>> if not fgt.api.cmdb.system_ha.exists(name="myobj"):
            ...     fgt.api.cmdb.system_ha.post(payload_dict=data)
        """
        # Use direct request with silent error handling to avoid logging 404s
        # This is expected behavior for exists() - 404 just means "doesn't exist"
        endpoint = "/system/ha"
        endpoint = f"{endpoint}/{quote_path_param(name)}"
        
        # Make request with silent=True to suppress 404 error logging
        # (404 is expected when checking existence - it just means "doesn't exist")
        # Use _wrapped_client to access the underlying HTTPClient directly
        # (self._client is ResponseProcessingClient, _wrapped_client is HTTPClient)
        try:
            result = self._client._wrapped_client.get(
                "cmdb",
                endpoint,
                params=None,
                vdom=vdom,
                raw_json=True,
                silent=True,
            )
            
            if isinstance(result, dict):
                # Synchronous response - check status
                return result.get("status") == "success"
            else:
                # Asynchronous response
                async def _check() -> bool:
                    r = await result
                    return r.get("status") == "success"
                return _check()
        except Exception:
            # Any error (404, network, etc.) means we can't confirm existence
            return False

