"""
FortiOS CMDB - Cmdb System Federated Upgrade

Configuration endpoint for managing cmdb system federated upgrade objects.

API Endpoints:
    GET    /cmdb/system/federated_upgrade
    PUT    /cmdb/system/federated_upgrade/{identifier}

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.system.federated_upgrade.get()
    >>>
    >>> # Get specific item (if supported)
    >>> item = fgt.api.cmdb.system.federated_upgrade.get(name="item_name")
    >>>
    >>> # Create new item (use POST)
    >>> result = fgt.api.cmdb.system.federated_upgrade.post(
    ...     name="new_item",
    ...     # ... additional parameters
    ... )
    >>>
    >>> # Update existing item (use PUT)
    >>> result = fgt.api.cmdb.system.federated_upgrade.put(
    ...     name="existing_item",
    ...     # ... parameters to update
    ... )
    >>>
    >>> # Delete item
    >>> result = fgt.api.cmdb.system.federated_upgrade.delete(name="item_name")

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


class FederatedUpgrade:
    """
    Federatedupgrade Operations.

    Provides CRUD operations for FortiOS federatedupgrade configuration.

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
        Initialize FederatedUpgrade endpoint.

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
        endpoint = "/system/federated-upgrade"
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
        status: str | None = None,
        source: str | None = None,
        failure_reason: str | None = None,
        failure_device: str | None = None,
        upgrade_id: int | None = None,
        next_path_index: int | None = None,
        ignore_signing_errors: str | None = None,
        ha_reboot_controller: str | None = None,
        known_ha_members: list | None = None,
        initial_version: str | None = None,
        starter_admin: str | None = None,
        node_list: list | None = None,
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
            status: Current status of the upgrade. (optional)
            source: Source that set up the federated upgrade config. (optional)
            failure_reason: Reason for upgrade failure. (optional)
            failure_device: Serial number of the node to include. (optional)
            upgrade_id: Unique identifier for this upgrade. (optional)
            next_path_index: The index of the next image to upgrade to.
            (optional)
            ignore_signing_errors: Allow/reject use of FortiGate firmware
            images that are unsigned. (optional)
            ha_reboot_controller: Serial number of the FortiGate unit that will
            control the reboot process for the federated upgrade of the HA
            cluster. (optional)
            known_ha_members: Known members of the HA cluster. If a member is
            missing at upgrade time, the upgrade will be cancelled. (optional)
            initial_version: Firmware version when the upgrade was set up.
            (optional)
            starter_admin: Admin that started the upgrade. (optional)
            node_list: Nodes which will be included in the upgrade. (optional)
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
        endpoint = "/system/federated-upgrade"
        if before is not None:
            data_payload["before"] = before
        if after is not None:
            data_payload["after"] = after
        if status is not None:
            data_payload["status"] = status
        if source is not None:
            data_payload["source"] = source
        if failure_reason is not None:
            data_payload["failure-reason"] = failure_reason
        if failure_device is not None:
            data_payload["failure-device"] = failure_device
        if upgrade_id is not None:
            data_payload["upgrade-id"] = upgrade_id
        if next_path_index is not None:
            data_payload["next-path-index"] = next_path_index
        if ignore_signing_errors is not None:
            data_payload["ignore-signing-errors"] = ignore_signing_errors
        if ha_reboot_controller is not None:
            data_payload["ha-reboot-controller"] = ha_reboot_controller
        if known_ha_members is not None:
            data_payload["known-ha-members"] = known_ha_members
        if initial_version is not None:
            data_payload["initial-version"] = initial_version
        if starter_admin is not None:
            data_payload["starter-admin"] = starter_admin
        if node_list is not None:
            data_payload["node-list"] = node_list
        data_payload.update(kwargs)
        return self._client.put(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )
