"""
FortiOS CMDB - Cmdb System Csf

Configuration endpoint for managing cmdb system csf objects.

API Endpoints:
    GET    /cmdb/system/csf
    PUT    /cmdb/system/csf/{identifier}

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.system.csf.get()
    >>>
    >>> # Get specific item (if supported)
    >>> item = fgt.api.cmdb.system.csf.get(name="item_name")
    >>>
    >>> # Create new item (use POST)
    >>> result = fgt.api.cmdb.system.csf.post(
    ...     name="new_item",
    ...     # ... additional parameters
    ... )
    >>>
    >>> # Update existing item (use PUT)
    >>> result = fgt.api.cmdb.system.csf.put(
    ...     name="existing_item",
    ...     # ... parameters to update
    ... )
    >>>
    >>> # Delete item
    >>> result = fgt.api.cmdb.system.csf.delete(name="item_name")

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


class Csf:
    """
    Csf Operations.

    Provides CRUD operations for FortiOS csf configuration.

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
        Initialize Csf endpoint.

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
        endpoint = "/system/cs"
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
        uid: str | None = None,
        upstream: str | None = None,
        source_ip: str | None = None,
        upstream_interface_select_method: str | None = None,
        upstream_interface: str | None = None,
        upstream_port: int | None = None,
        group_name: str | None = None,
        group_password: str | None = None,
        accept_auth_by_cert: str | None = None,
        log_unification: str | None = None,
        authorization_request_type: str | None = None,
        certificate: str | None = None,
        fabric_workers: int | None = None,
        downstream_access: str | None = None,
        legacy_authentication: str | None = None,
        downstream_accprofile: str | None = None,
        configuration_sync: str | None = None,
        fabric_object_unification: str | None = None,
        saml_configuration_sync: str | None = None,
        trusted_list: list | None = None,
        fabric_connector: list | None = None,
        forticloud_account_enforcement: str | None = None,
        file_mgmt: str | None = None,
        file_quota: int | None = None,
        file_quota_warning: int | None = None,
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
            status: Enable/disable Security Fabric. (optional)
            uid: Unique ID of the current CSF node (optional)
            upstream: IP/FQDN of the FortiGate upstream from this FortiGate in
            the Security Fabric. (optional)
            source_ip: Source IP address for communication with the upstream
            FortiGate. (optional)
            upstream_interface_select_method: Specify how to select outgoing
            interface to reach server. (optional)
            upstream_interface: Specify outgoing interface to reach server.
            (optional)
            upstream_port: The port number to use to communicate with the
            FortiGate upstream from this FortiGate in the Security Fabric
            (default = 8013). (optional)
            group_name: Security Fabric group name. All FortiGates in a
            Security Fabric must have the same group name. (optional)
            group_password: Security Fabric group password. For legacy
            authentication, fabric members must have the same group password.
            (optional)
            accept_auth_by_cert: Accept connections with unknown certificates
            and ask admin for approval. (optional)
            log_unification: Enable/disable broadcast of discovery messages for
            log unification. (optional)
            authorization_request_type: Authorization request type. (optional)
            certificate: Certificate. (optional)
            fabric_workers: Number of worker processes for Security Fabric
            daemon. (optional)
            downstream_access: Enable/disable downstream device access to this
            device's configuration and data. (optional)
            legacy_authentication: Enable/disable legacy authentication.
            (optional)
            downstream_accprofile: Default access profile for requests from
            downstream devices. (optional)
            configuration_sync: Configuration sync mode. (optional)
            fabric_object_unification: Fabric CMDB Object Unification.
            (optional)
            saml_configuration_sync: SAML setting configuration
            synchronization. (optional)
            trusted_list: Pre-authorized and blocked security fabric nodes.
            (optional)
            fabric_connector: Fabric connector configuration. (optional)
            forticloud_account_enforcement: Fabric FortiCloud account
            unification. (optional)
            file_mgmt: Enable/disable Security Fabric daemon file management.
            (optional)
            file_quota: Maximum amount of memory that can be used by the daemon
            files (in bytes). (optional)
            file_quota_warning: Warn when the set percentage of quota has been
            used. (optional)
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
        endpoint = "/system/cs"
        if before is not None:
            data_payload["before"] = before
        if after is not None:
            data_payload["after"] = after
        if status is not None:
            data_payload["status"] = status
        if uid is not None:
            data_payload["uid"] = uid
        if upstream is not None:
            data_payload["upstream"] = upstream
        if source_ip is not None:
            data_payload["source-ip"] = source_ip
        if upstream_interface_select_method is not None:
            data_payload["upstream-interface-select-method"] = (
                upstream_interface_select_method
            )
        if upstream_interface is not None:
            data_payload["upstream-interface"] = upstream_interface
        if upstream_port is not None:
            data_payload["upstream-port"] = upstream_port
        if group_name is not None:
            data_payload["group-name"] = group_name
        if group_password is not None:
            data_payload["group-password"] = group_password
        if accept_auth_by_cert is not None:
            data_payload["accept-auth-by-cert"] = accept_auth_by_cert
        if log_unification is not None:
            data_payload["log-unification"] = log_unification
        if authorization_request_type is not None:
            data_payload["authorization-request-type"] = (
                authorization_request_type
            )
        if certificate is not None:
            data_payload["certificate"] = certificate
        if fabric_workers is not None:
            data_payload["fabric-workers"] = fabric_workers
        if downstream_access is not None:
            data_payload["downstream-access"] = downstream_access
        if legacy_authentication is not None:
            data_payload["legacy-authentication"] = legacy_authentication
        if downstream_accprofile is not None:
            data_payload["downstream-accprofile"] = downstream_accprofile
        if configuration_sync is not None:
            data_payload["configuration-sync"] = configuration_sync
        if fabric_object_unification is not None:
            data_payload["fabric-object-unification"] = (
                fabric_object_unification
            )
        if saml_configuration_sync is not None:
            data_payload["saml-configuration-sync"] = saml_configuration_sync
        if trusted_list is not None:
            data_payload["trusted-list"] = trusted_list
        if fabric_connector is not None:
            data_payload["fabric-connector"] = fabric_connector
        if forticloud_account_enforcement is not None:
            data_payload["forticloud-account-enforcement"] = (
                forticloud_account_enforcement
            )
        if file_mgmt is not None:
            data_payload["file-mgmt"] = file_mgmt
        if file_quota is not None:
            data_payload["file-quota"] = file_quota
        if file_quota_warning is not None:
            data_payload["file-quota-warning"] = file_quota_warning
        data_payload.update(kwargs)
        return self._client.put(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )
