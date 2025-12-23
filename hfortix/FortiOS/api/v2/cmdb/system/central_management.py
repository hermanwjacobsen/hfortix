"""
FortiOS CMDB - Cmdb System Central Management

Configuration endpoint for managing cmdb system central management objects.

API Endpoints:
    GET    /cmdb/system/central_management
    PUT    /cmdb/system/central_management/{identifier}

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.system.central_management.get()
    >>>
    >>> # Get specific item (if supported)
    >>> item = fgt.api.cmdb.system.central_management.get(name="item_name")
    >>>
    >>> # Create new item (use POST)
    >>> result = fgt.api.cmdb.system.central_management.post(
    ...     name="new_item",
    ...     # ... additional parameters
    ... )
    >>>
    >>> # Update existing item (use PUT)
    >>> result = fgt.api.cmdb.system.central_management.put(
    ...     name="existing_item",
    ...     # ... parameters to update
    ... )
    >>>
    >>> # Delete item
    >>> result =
    fgt.api.cmdb.system.central_management.delete(name="item_name")

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


class CentralManagement:
    """
    Centralmanagement Operations.

    Provides CRUD operations for FortiOS centralmanagement configuration.

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
        Initialize CentralManagement endpoint.

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
        endpoint = "/system/central-management"
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
        mode: str | None = None,
        type: str | None = None,
        fortigate_cloud_sso_default_profile: str | None = None,
        schedule_config_restore: str | None = None,
        schedule_script_restore: str | None = None,
        allow_push_configuration: str | None = None,
        allow_push_firmware: str | None = None,
        allow_remote_firmware_upgrade: str | None = None,
        allow_monitor: str | None = None,
        serial_number: str | None = None,
        fmg: str | None = None,
        fmg_source_ip: str | None = None,
        fmg_source_ip6: str | None = None,
        local_cert: str | None = None,
        ca_cert: str | None = None,
        server_list: list | None = None,
        fmg_update_port: str | None = None,
        fmg_update_http_header: str | None = None,
        include_default_servers: str | None = None,
        enc_algorithm: str | None = None,
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
            mode: Central management mode. (optional)
            type: Central management type. (optional)
            fortigate_cloud_sso_default_profile: Override access profile.
            Permission is set to read-only without a FortiGate Cloud Central
            Management license. (optional)
            schedule_config_restore: Enable/disable allowing the central
            management server to restore the configuration of this FortiGate.
            (optional)
            schedule_script_restore: Enable/disable allowing the central
            management server to restore the scripts stored on this FortiGate.
            (optional)
            allow_push_configuration: Enable/disable allowing the central
            management server to push configuration changes to this FortiGate.
            (optional)
            allow_push_firmware: Enable/disable allowing the central management
            server to push firmware updates to this FortiGate. (optional)
            allow_remote_firmware_upgrade: Enable/disable remotely upgrading
            the firmware on this FortiGate from the central management server.
            (optional)
            allow_monitor: Enable/disable allowing the central management
            server to remotely monitor this FortiGate unit. (optional)
            serial_number: Serial number. (optional)
            fmg: IP address or FQDN of the FortiManager. (optional)
            fmg_source_ip: IPv4 source address that this FortiGate uses when
            communicating with FortiManager. (optional)
            fmg_source_ip6: IPv6 source address that this FortiGate uses when
            communicating with FortiManager. (optional)
            local_cert: Certificate to be used by FGFM protocol. (optional)
            ca_cert: CA certificate to be used by FGFM protocol. (optional)
            server_list: Additional severs that the FortiGate can use for
            updates (for AV, IPS, updates) and ratings (for web filter and
            antispam ratings) servers. (optional)
            fmg_update_port: Port used to communicate with FortiManager that is
            acting as a FortiGuard update server. (optional)
            fmg_update_http_header: Enable/disable inclusion of HTTP header in
            update request. (optional)
            include_default_servers: Enable/disable inclusion of public
            FortiGuard servers in the override server list. (optional)
            enc_algorithm: Encryption strength for communications between the
            FortiGate and central management. (optional)
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
        endpoint = "/system/central-management"
        if before is not None:
            data_payload["before"] = before
        if after is not None:
            data_payload["after"] = after
        if mode is not None:
            data_payload["mode"] = mode
        if type is not None:
            data_payload["type"] = type
        if fortigate_cloud_sso_default_profile is not None:
            data_payload["fortigate-cloud-sso-default-profile"] = (
                fortigate_cloud_sso_default_profile
            )
        if schedule_config_restore is not None:
            data_payload["schedule-config-restore"] = schedule_config_restore
        if schedule_script_restore is not None:
            data_payload["schedule-script-restore"] = schedule_script_restore
        if allow_push_configuration is not None:
            data_payload["allow-push-configuration"] = allow_push_configuration
        if allow_push_firmware is not None:
            data_payload["allow-push-firmware"] = allow_push_firmware
        if allow_remote_firmware_upgrade is not None:
            data_payload["allow-remote-firmware-upgrade"] = (
                allow_remote_firmware_upgrade
            )
        if allow_monitor is not None:
            data_payload["allow-monitor"] = allow_monitor
        if serial_number is not None:
            data_payload["serial-number"] = serial_number
        if fmg is not None:
            data_payload["fmg"] = fmg
        if fmg_source_ip is not None:
            data_payload["fmg-source-ip"] = fmg_source_ip
        if fmg_source_ip6 is not None:
            data_payload["fmg-source-ip6"] = fmg_source_ip6
        if local_cert is not None:
            data_payload["local-cert"] = local_cert
        if ca_cert is not None:
            data_payload["ca-cert"] = ca_cert
        if server_list is not None:
            data_payload["server-list"] = server_list
        if fmg_update_port is not None:
            data_payload["fmg-update-port"] = fmg_update_port
        if fmg_update_http_header is not None:
            data_payload["fmg-update-http-header"] = fmg_update_http_header
        if include_default_servers is not None:
            data_payload["include-default-servers"] = include_default_servers
        if enc_algorithm is not None:
            data_payload["enc-algorithm"] = enc_algorithm
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
