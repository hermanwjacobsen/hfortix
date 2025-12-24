"""
FortiOS CMDB - Cmdb System Fortiguard

Configuration endpoint for managing cmdb system fortiguard objects.

API Endpoints:
    GET    /cmdb/system/fortiguard
    PUT    /cmdb/system/fortiguard/{identifier}

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.system.fortiguard.get()
    >>>
    >>> # Get specific item (if supported)
    >>> item = fgt.api.cmdb.system.fortiguard.get(name="item_name")
    >>>
    >>> # Create new item (use POST)
    >>> result = fgt.api.cmdb.system.fortiguard.post(
    ...     name="new_item",
    ...     # ... additional parameters
    ... )
    >>>
    >>> # Update existing item (use PUT)
    >>> result = fgt.api.cmdb.system.fortiguard.put(
    ...     name="existing_item",
    ...     # ... parameters to update
    ... )
    >>>
    >>> # Delete item
    >>> result = fgt.api.cmdb.system.fortiguard.delete(name="item_name")

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


class Fortiguard:
    """
    Fortiguard Operations.

    Provides CRUD operations for FortiOS fortiguard configuration.

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
        Initialize Fortiguard endpoint.

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
        endpoint = "/system/fortiguard"
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
        fortiguard_anycast: str | None = None,
        fortiguard_anycast_source: str | None = None,
        protocol: str | None = None,
        port: str | None = None,
        service_account_id: str | None = None,
        load_balance_servers: int | None = None,
        auto_join_forticloud: str | None = None,
        update_server_location: str | None = None,
        sandbox_region: str | None = None,
        update_ffdb: str | None = None,
        update_uwdb: str | None = None,
        update_dldb: str | None = None,
        update_extdb: str | None = None,
        update_build_proxy: str | None = None,
        persistent_connection: str | None = None,
        auto_firmware_upgrade: str | None = None,
        auto_firmware_upgrade_day: str | None = None,
        auto_firmware_upgrade_delay: int | None = None,
        auto_firmware_upgrade_start_hour: int | None = None,
        auto_firmware_upgrade_end_hour: int | None = None,
        FDS_license_expiring_days: int | None = None,
        subscribe_update_notification: str | None = None,
        antispam_force_off: str | None = None,
        antispam_cache: str | None = None,
        antispam_cache_ttl: int | None = None,
        antispam_cache_mpermille: int | None = None,
        antispam_license: int | None = None,
        antispam_expiration: int | None = None,
        antispam_timeout: int | None = None,
        outbreak_prevention_force_off: str | None = None,
        outbreak_prevention_cache: str | None = None,
        outbreak_prevention_cache_ttl: int | None = None,
        outbreak_prevention_cache_mpermille: int | None = None,
        outbreak_prevention_license: int | None = None,
        outbreak_prevention_expiration: int | None = None,
        outbreak_prevention_timeout: int | None = None,
        webfilter_force_off: str | None = None,
        webfilter_cache: str | None = None,
        webfilter_cache_ttl: int | None = None,
        webfilter_license: int | None = None,
        webfilter_expiration: int | None = None,
        webfilter_timeout: int | None = None,
        sdns_server_ip: str | None = None,
        sdns_server_port: int | None = None,
        anycast_sdns_server_ip: str | None = None,
        anycast_sdns_server_port: int | None = None,
        sdns_options: str | None = None,
        source_ip: str | None = None,
        source_ip6: str | None = None,
        proxy_server_ip: str | None = None,
        proxy_server_port: int | None = None,
        proxy_username: str | None = None,
        proxy_password: str | None = None,
        ddns_server_ip: str | None = None,
        ddns_server_ip6: str | None = None,
        ddns_server_port: int | None = None,
        interface_select_method: str | None = None,
        interface: str | None = None,
        vrf_select: int | None = None,
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
            fortiguard_anycast: Enable/disable use of FortiGuard's Anycast
            network. (optional)
            fortiguard_anycast_source: Configure which of Fortinet's servers to
            provide FortiGuard services in FortiGuard's anycast network.
            Default is Fortinet. (optional)
            protocol: Protocol used to communicate with the FortiGuard servers.
            (optional)
            port: Port used to communicate with the FortiGuard servers.
            (optional)
            service_account_id: Service account ID. (optional)
            load_balance_servers: Number of servers to alternate between as
            first FortiGuard option. (optional)
            auto_join_forticloud: Automatically connect to and login to
            FortiCloud. (optional)
            update_server_location: Location from which to receive FortiGuard
            updates. (optional)
            sandbox_region: FortiCloud Sandbox region. (optional)
            update_ffdb: Enable/disable Internet Service Database update.
            (optional)
            update_uwdb: Enable/disable allowlist update. (optional)
            update_dldb: Enable/disable DLP signature update. (optional)
            update_extdb: Enable/disable external resource update. (optional)
            update_build_proxy: Enable/disable proxy dictionary rebuild.
            (optional)
            persistent_connection: Enable/disable use of persistent connection
            to receive update notification from FortiGuard. (optional)
            auto_firmware_upgrade: Enable/disable automatic patch-level
            firmware upgrade from FortiGuard. The FortiGate unit searches for
            new patches only in the same major and minor version. (optional)
            auto_firmware_upgrade_day: Allowed day(s) of the week to install an
            automatic patch-level firmware upgrade from FortiGuard (default is
            none). Disallow any day of the week to use
            auto-firmware-upgrade-delay instead, which waits for designated
            days before installing an automatic patch-level firmware upgrade.
            (optional)
            auto_firmware_upgrade_delay: Delay of day(s) before installing an
            automatic patch-level firmware upgrade from FortiGuard (default =
            3). Set it 0 to use auto-firmware-upgrade-day instead, which
            selects allowed day(s) of the week for installing an automatic
            patch-level firmware upgrade. (optional)
            auto_firmware_upgrade_start_hour: Start time in the designated time
            window for automatic patch-level firmware upgrade from FortiGuard
            in 24 hour time (0 ~ 23, default = 2). The actual upgrade time is
            selected randomly within the time window. (optional)
            auto_firmware_upgrade_end_hour: End time in the designated time
            window for automatic patch-level firmware upgrade from FortiGuard
            in 24 hour time (0 ~ 23, default = 4). When the end time is smaller
            than the start time, the end time is interpreted as the next day.
            The actual upgrade time is selected randomly within the time
            window. (optional)
            FDS_license_expiring_days: Threshold for number of days before
            FortiGuard license expiration to generate license expiring event
            log (1 - 100 days, default = 15). (optional)
            subscribe_update_notification: Enable/disable subscription to
            receive update notification from FortiGuard. (optional)
            antispam_force_off: Enable/disable turning off the FortiGuard
            antispam service. (optional)
            antispam_cache: Enable/disable FortiGuard antispam request caching.
            Uses a small amount of memory but improves performance. (optional)
            antispam_cache_ttl: Time-to-live for antispam cache entries in
            seconds (300 - 86400). Lower times reduce the cache size. Higher
            times may improve performance since the cache will have more
            entries. (optional)
            antispam_cache_mpermille: Maximum permille of FortiGate memory the
            antispam cache is allowed to use (1 - 150). (optional)
            antispam_license: Interval of time between license checks for the
            FortiGuard antispam contract. (optional)
            antispam_expiration: Expiration date of the FortiGuard antispam
            contract. (optional)
            antispam_timeout: Antispam query time out (1 - 30 sec, default =
            7). (optional)
            outbreak_prevention_force_off: Turn off FortiGuard Virus Outbreak
            Prevention service. (optional)
            outbreak_prevention_cache: Enable/disable FortiGuard Virus Outbreak
            Prevention cache. (optional)
            outbreak_prevention_cache_ttl: Time-to-live for FortiGuard Virus
            Outbreak Prevention cache entries (300 - 86400 sec, default = 300).
            (optional)
            outbreak_prevention_cache_mpermille: Maximum permille of memory
            FortiGuard Virus Outbreak Prevention cache can use (1 - 150
            permille, default = 1). (optional)
            outbreak_prevention_license: Interval of time between license
            checks for FortiGuard Virus Outbreak Prevention contract.
            (optional)
            outbreak_prevention_expiration: Expiration date of FortiGuard Virus
            Outbreak Prevention contract. (optional)
            outbreak_prevention_timeout: FortiGuard Virus Outbreak Prevention
            time out (1 - 30 sec, default = 7). (optional)
            webfilter_force_off: Enable/disable turning off the FortiGuard web
            filtering service. (optional)
            webfilter_cache: Enable/disable FortiGuard web filter caching.
            (optional)
            webfilter_cache_ttl: Time-to-live for web filter cache entries in
            seconds (300 - 86400). (optional)
            webfilter_license: Interval of time between license checks for the
            FortiGuard web filter contract. (optional)
            webfilter_expiration: Expiration date of the FortiGuard web filter
            contract. (optional)
            webfilter_timeout: Web filter query time out (1 - 30 sec, default =
            15). (optional)
            sdns_server_ip: IP address of the FortiGuard DNS rating server.
            (optional)
            sdns_server_port: Port to connect to on the FortiGuard DNS rating
            server. (optional)
            anycast_sdns_server_ip: IP address of the FortiGuard anycast DNS
            rating server. (optional)
            anycast_sdns_server_port: Port to connect to on the FortiGuard
            anycast DNS rating server. (optional)
            sdns_options: Customization options for the FortiGuard DNS service.
            (optional)
            source_ip: Source IPv4 address used to communicate with FortiGuard.
            (optional)
            source_ip6: Source IPv6 address used to communicate with
            FortiGuard. (optional)
            proxy_server_ip: Hostname or IPv4 address of the proxy server.
            (optional)
            proxy_server_port: Port used to communicate with the proxy server.
            (optional)
            proxy_username: Proxy user name. (optional)
            proxy_password: Proxy user password. (optional)
            ddns_server_ip: IP address of the FortiDDNS server. (optional)
            ddns_server_ip6: IPv6 address of the FortiDDNS server. (optional)
            ddns_server_port: Port used to communicate with FortiDDNS servers.
            (optional)
            interface_select_method: Specify how to select outgoing interface
            to reach server. (optional)
            interface: Specify outgoing interface to reach server. (optional)
            vrf_select: VRF ID used for connection to server. (optional)
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
        endpoint = "/system/fortiguard"
        if before is not None:
            data_payload["before"] = before
        if after is not None:
            data_payload["after"] = after
        if fortiguard_anycast is not None:
            data_payload["fortiguard-anycast"] = fortiguard_anycast
        if fortiguard_anycast_source is not None:
            data_payload["fortiguard-anycast-source"] = (
                fortiguard_anycast_source
            )
        if protocol is not None:
            data_payload["protocol"] = protocol
        if port is not None:
            data_payload["port"] = port
        if service_account_id is not None:
            data_payload["service-account-id"] = service_account_id
        if load_balance_servers is not None:
            data_payload["load-balance-servers"] = load_balance_servers
        if auto_join_forticloud is not None:
            data_payload["auto-join-forticloud"] = auto_join_forticloud
        if update_server_location is not None:
            data_payload["update-server-location"] = update_server_location
        if sandbox_region is not None:
            data_payload["sandbox-region"] = sandbox_region
        if update_ffdb is not None:
            data_payload["update-ffdb"] = update_ffdb
        if update_uwdb is not None:
            data_payload["update-uwdb"] = update_uwdb
        if update_dldb is not None:
            data_payload["update-dldb"] = update_dldb
        if update_extdb is not None:
            data_payload["update-extdb"] = update_extdb
        if update_build_proxy is not None:
            data_payload["update-build-proxy"] = update_build_proxy
        if persistent_connection is not None:
            data_payload["persistent-connection"] = persistent_connection
        if auto_firmware_upgrade is not None:
            data_payload["auto-firmware-upgrade"] = auto_firmware_upgrade
        if auto_firmware_upgrade_day is not None:
            data_payload["auto-firmware-upgrade-day"] = (
                auto_firmware_upgrade_day
            )
        if auto_firmware_upgrade_delay is not None:
            data_payload["auto-firmware-upgrade-delay"] = (
                auto_firmware_upgrade_delay
            )
        if auto_firmware_upgrade_start_hour is not None:
            data_payload["auto-firmware-upgrade-start-hour"] = (
                auto_firmware_upgrade_start_hour
            )
        if auto_firmware_upgrade_end_hour is not None:
            data_payload["auto-firmware-upgrade-end-hour"] = (
                auto_firmware_upgrade_end_hour
            )
        if FDS_license_expiring_days is not None:
            data_payload["FDS-license-expiring-days"] = (
                FDS_license_expiring_days
            )
        if subscribe_update_notification is not None:
            data_payload["subscribe-update-notification"] = (
                subscribe_update_notification
            )
        if antispam_force_off is not None:
            data_payload["antispam-force-of"] = antispam_force_off
        if antispam_cache is not None:
            data_payload["antispam-cache"] = antispam_cache
        if antispam_cache_ttl is not None:
            data_payload["antispam-cache-ttl"] = antispam_cache_ttl
        if antispam_cache_mpermille is not None:
            data_payload["antispam-cache-mpermille"] = antispam_cache_mpermille
        if antispam_license is not None:
            data_payload["antispam-license"] = antispam_license
        if antispam_expiration is not None:
            data_payload["antispam-expiration"] = antispam_expiration
        if antispam_timeout is not None:
            data_payload["antispam-timeout"] = antispam_timeout
        if outbreak_prevention_force_off is not None:
            data_payload["outbreak-prevention-force-of"] = (
                outbreak_prevention_force_off
            )
        if outbreak_prevention_cache is not None:
            data_payload["outbreak-prevention-cache"] = (
                outbreak_prevention_cache
            )
        if outbreak_prevention_cache_ttl is not None:
            data_payload["outbreak-prevention-cache-ttl"] = (
                outbreak_prevention_cache_ttl
            )
        if outbreak_prevention_cache_mpermille is not None:
            data_payload["outbreak-prevention-cache-mpermille"] = (
                outbreak_prevention_cache_mpermille
            )
        if outbreak_prevention_license is not None:
            data_payload["outbreak-prevention-license"] = (
                outbreak_prevention_license
            )
        if outbreak_prevention_expiration is not None:
            data_payload["outbreak-prevention-expiration"] = (
                outbreak_prevention_expiration
            )
        if outbreak_prevention_timeout is not None:
            data_payload["outbreak-prevention-timeout"] = (
                outbreak_prevention_timeout
            )
        if webfilter_force_off is not None:
            data_payload["webfilter-force-of"] = webfilter_force_off
        if webfilter_cache is not None:
            data_payload["webfilter-cache"] = webfilter_cache
        if webfilter_cache_ttl is not None:
            data_payload["webfilter-cache-ttl"] = webfilter_cache_ttl
        if webfilter_license is not None:
            data_payload["webfilter-license"] = webfilter_license
        if webfilter_expiration is not None:
            data_payload["webfilter-expiration"] = webfilter_expiration
        if webfilter_timeout is not None:
            data_payload["webfilter-timeout"] = webfilter_timeout
        if sdns_server_ip is not None:
            data_payload["sdns-server-ip"] = sdns_server_ip
        if sdns_server_port is not None:
            data_payload["sdns-server-port"] = sdns_server_port
        if anycast_sdns_server_ip is not None:
            data_payload["anycast-sdns-server-ip"] = anycast_sdns_server_ip
        if anycast_sdns_server_port is not None:
            data_payload["anycast-sdns-server-port"] = anycast_sdns_server_port
        if sdns_options is not None:
            data_payload["sdns-options"] = sdns_options
        if source_ip is not None:
            data_payload["source-ip"] = source_ip
        if source_ip6 is not None:
            data_payload["source-ip6"] = source_ip6
        if proxy_server_ip is not None:
            data_payload["proxy-server-ip"] = proxy_server_ip
        if proxy_server_port is not None:
            data_payload["proxy-server-port"] = proxy_server_port
        if proxy_username is not None:
            data_payload["proxy-username"] = proxy_username
        if proxy_password is not None:
            data_payload["proxy-password"] = proxy_password
        if ddns_server_ip is not None:
            data_payload["ddns-server-ip"] = ddns_server_ip
        if ddns_server_ip6 is not None:
            data_payload["ddns-server-ip6"] = ddns_server_ip6
        if ddns_server_port is not None:
            data_payload["ddns-server-port"] = ddns_server_port
        if interface_select_method is not None:
            data_payload["interface-select-method"] = interface_select_method
        if interface is not None:
            data_payload["interface"] = interface
        if vrf_select is not None:
            data_payload["vrf-select"] = vrf_select
        data_payload.update(kwargs)
        return self._client.put(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )
