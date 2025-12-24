"""
FortiOS CMDB - Cmdb Switch Controller Global

Configuration endpoint for managing cmdb switch controller global objects.

API Endpoints:
    GET    /cmdb/switch-controller/global_
    PUT    /cmdb/switch-controller/global_/{identifier}

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.switch_controller.global_.get()
    >>>
    >>> # Get specific item (if supported)
    >>> item = fgt.api.cmdb.switch_controller.global_.get(name="item_name")
    >>>
    >>> # Create new item (use POST)
    >>> result = fgt.api.cmdb.switch_controller.global_.post(
    ...     name="new_item",
    ...     # ... additional parameters
    ... )
    >>>
    >>> # Update existing item (use PUT)
    >>> result = fgt.api.cmdb.switch_controller.global_.put(
    ...     name="existing_item",
    ...     # ... parameters to update
    ... )
    >>>
    >>> # Delete item
    >>> result =
    fgt.api.cmdb.switch_controller.global_.delete(name="item_name")

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


class Global:
    """
    Global Operations.

    Provides CRUD operations for FortiOS global configuration.

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
        Initialize Global endpoint.

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
        endpoint = "/switch-controller/global"
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
        mac_aging_interval: int | None = None,
        https_image_push: str | None = None,
        vlan_all_mode: str | None = None,
        vlan_optimization: str | None = None,
        vlan_identity: str | None = None,
        disable_discovery: list | None = None,
        mac_retention_period: int | None = None,
        default_virtual_switch_vlan: str | None = None,
        dhcp_server_access_list: str | None = None,
        dhcp_option82_format: str | None = None,
        dhcp_option82_circuit_id: str | None = None,
        dhcp_option82_remote_id: str | None = None,
        dhcp_snoop_client_req: str | None = None,
        dhcp_snoop_client_db_exp: int | None = None,
        dhcp_snoop_db_per_port_learn_limit: int | None = None,
        log_mac_limit_violations: str | None = None,
        mac_violation_timer: int | None = None,
        sn_dns_resolution: str | None = None,
        mac_event_logging: str | None = None,
        bounce_quarantined_link: str | None = None,
        quarantine_mode: str | None = None,
        update_user_device: str | None = None,
        custom_command: list | None = None,
        fips_enforce: str | None = None,
        firmware_provision_on_authorization: str | None = None,
        switch_on_deauth: str | None = None,
        firewall_auth_user_hold_period: int | None = None,
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
            mac_aging_interval: Time after which an inactive MAC is aged out
            (10 - 1000000 sec, default = 300, 0 = disable). (optional)
            https_image_push: Enable/disable image push to FortiSwitch using
            HTTPS. (optional)
            vlan_all_mode: VLAN configuration mode, user-defined-vlans or
            all-possible-vlans. (optional)
            vlan_optimization: FortiLink VLAN optimization. (optional)
            vlan_identity: Identity of the VLAN. Commonly used for RADIUS
            Tunnel-Private-Group-Id. (optional)
            disable_discovery: Prevent this FortiSwitch from discovering.
            (optional)
            mac_retention_period: Time in hours after which an inactive MAC is
            removed from client DB (0 = aged out based on mac-aging-interval).
            (optional)
            default_virtual_switch_vlan: Default VLAN for ports when added to
            the virtual-switch. (optional)
            dhcp_server_access_list: Enable/disable DHCP snooping server access
            list. (optional)
            dhcp_option82_format: DHCP option-82 format string. (optional)
            dhcp_option82_circuit_id: List the parameters to be included to
            inform about client identification. (optional)
            dhcp_option82_remote_id: List the parameters to be included to
            inform about client identification. (optional)
            dhcp_snoop_client_req: Client DHCP packet broadcast mode.
            (optional)
            dhcp_snoop_client_db_exp: Expiry time for DHCP snooping server
            database entries (300 - 259200 sec, default = 86400 sec).
            (optional)
            dhcp_snoop_db_per_port_learn_limit: Per Interface dhcp-server
            entries learn limit (0 - 1024, default = 64). (optional)
            log_mac_limit_violations: Enable/disable logs for Learning Limit
            Violations. (optional)
            mac_violation_timer: Set timeout for Learning Limit Violations (0 =
            disabled). (optional)
            sn_dns_resolution: Enable/disable DNS resolution of the FortiSwitch
            unit's IP address with switch name. (optional)
            mac_event_logging: Enable/disable MAC address event logging.
            (optional)
            bounce_quarantined_link: Enable/disable bouncing (administratively
            bring the link down, up) of a switch port where a quarantined
            device was seen last. Helps to re-initiate the DHCP process for a
            device. (optional)
            quarantine_mode: Quarantine mode. (optional)
            update_user_device: Control which sources update the device user
            list. (optional)
            custom_command: List of custom commands to be pushed to all
            FortiSwitches in the VDOM. (optional)
            fips_enforce: Enable/disable enforcement of FIPS on managed
            FortiSwitch devices. (optional)
            firmware_provision_on_authorization: Enable/disable automatic
            provisioning of latest firmware on authorization. (optional)
            switch_on_deauth: No-operation/Factory-reset the managed
            FortiSwitch on deauthorization. (optional)
            firewall_auth_user_hold_period: Time period in minutes to hold
            firewall authenticated MAC users (5 - 1440, default = 5, disable =
            0). (optional)
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
        endpoint = "/switch-controller/global"
        if before is not None:
            data_payload["before"] = before
        if after is not None:
            data_payload["after"] = after
        if mac_aging_interval is not None:
            data_payload["mac-aging-interval"] = mac_aging_interval
        if https_image_push is not None:
            data_payload["https-image-push"] = https_image_push
        if vlan_all_mode is not None:
            data_payload["vlan-all-mode"] = vlan_all_mode
        if vlan_optimization is not None:
            data_payload["vlan-optimization"] = vlan_optimization
        if vlan_identity is not None:
            data_payload["vlan-identity"] = vlan_identity
        if disable_discovery is not None:
            data_payload["disable-discovery"] = disable_discovery
        if mac_retention_period is not None:
            data_payload["mac-retention-period"] = mac_retention_period
        if default_virtual_switch_vlan is not None:
            data_payload["default-virtual-switch-vlan"] = (
                default_virtual_switch_vlan
            )
        if dhcp_server_access_list is not None:
            data_payload["dhcp-server-access-list"] = dhcp_server_access_list
        if dhcp_option82_format is not None:
            data_payload["dhcp-option82-format"] = dhcp_option82_format
        if dhcp_option82_circuit_id is not None:
            data_payload["dhcp-option82-circuit-id"] = dhcp_option82_circuit_id
        if dhcp_option82_remote_id is not None:
            data_payload["dhcp-option82-remote-id"] = dhcp_option82_remote_id
        if dhcp_snoop_client_req is not None:
            data_payload["dhcp-snoop-client-req"] = dhcp_snoop_client_req
        if dhcp_snoop_client_db_exp is not None:
            data_payload["dhcp-snoop-client-db-exp"] = dhcp_snoop_client_db_exp
        if dhcp_snoop_db_per_port_learn_limit is not None:
            data_payload["dhcp-snoop-db-per-port-learn-limit"] = (
                dhcp_snoop_db_per_port_learn_limit
            )
        if log_mac_limit_violations is not None:
            data_payload["log-mac-limit-violations"] = log_mac_limit_violations
        if mac_violation_timer is not None:
            data_payload["mac-violation-timer"] = mac_violation_timer
        if sn_dns_resolution is not None:
            data_payload["sn-dns-resolution"] = sn_dns_resolution
        if mac_event_logging is not None:
            data_payload["mac-event-logging"] = mac_event_logging
        if bounce_quarantined_link is not None:
            data_payload["bounce-quarantined-link"] = bounce_quarantined_link
        if quarantine_mode is not None:
            data_payload["quarantine-mode"] = quarantine_mode
        if update_user_device is not None:
            data_payload["update-user-device"] = update_user_device
        if custom_command is not None:
            data_payload["custom-command"] = custom_command
        if fips_enforce is not None:
            data_payload["fips-enforce"] = fips_enforce
        if firmware_provision_on_authorization is not None:
            data_payload["firmware-provision-on-authorization"] = (
                firmware_provision_on_authorization
            )
        if switch_on_deauth is not None:
            data_payload["switch-on-deauth"] = switch_on_deauth
        if firewall_auth_user_hold_period is not None:
            data_payload["firewall-auth-user-hold-period"] = (
                firewall_auth_user_hold_period
            )
        data_payload.update(kwargs)
        return self._client.put(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )
