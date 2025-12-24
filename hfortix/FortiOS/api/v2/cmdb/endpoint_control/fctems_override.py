"""
FortiOS CMDB - Cmdb Endpoint Control Fctems Override

Configuration endpoint for managing cmdb endpoint control fctems override
objects.

API Endpoints:
    GET    /cmdb/endpoint-control/fctems_override
    POST   /cmdb/endpoint-control/fctems_override
    GET    /cmdb/endpoint-control/fctems_override
    PUT    /cmdb/endpoint-control/fctems_override/{identifier}
    DELETE /cmdb/endpoint-control/fctems_override/{identifier}

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.endpoint_control.fctems_override.get()
    >>>
    >>> # Get specific item (if supported)
    >>> item =
    fgt.api.cmdb.endpoint_control.fctems_override.get(name="item_name")
    >>>
    >>> # Create new item (use POST)
    >>> result = fgt.api.cmdb.endpoint_control.fctems_override.post(
    ...     name="new_item",
    ...     # ... additional parameters
    ... )
    >>>
    >>> # Update existing item (use PUT)
    >>> result = fgt.api.cmdb.endpoint_control.fctems_override.put(
    ...     name="existing_item",
    ...     # ... parameters to update
    ... )
    >>>
    >>> # Delete item
    >>> result =
    fgt.api.cmdb.endpoint_control.fctems_override.delete(name="item_name")

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


class FctemsOverride:
    """
    Fctemsoverride Operations.

    Provides CRUD operations for FortiOS fctemsoverride configuration.

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
        Initialize FctemsOverride endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

    def get(
        self,
        ems_id: str | None = None,
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
            ems_id: Object identifier (optional for list, required for
            specific)
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
        if ems_id:
            endpoint = f"/endpoint-control/fctems-override/{ems_id}"
        else:
            endpoint = "/endpoint-control/fctems-override"
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
        ems_id: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        before: str | None = None,
        after: str | None = None,
        status: str | None = None,
        name: str | None = None,
        dirty_reason: str | None = None,
        fortinetone_cloud_authentication: str | None = None,
        cloud_authentication_access_key: str | None = None,
        server: str | None = None,
        https_port: int | None = None,
        serial_number: str | None = None,
        tenant_id: str | None = None,
        source_ip: str | None = None,
        pull_sysinfo: str | None = None,
        pull_vulnerabilities: str | None = None,
        pull_tags: str | None = None,
        pull_malware_hash: str | None = None,
        capabilities: str | None = None,
        call_timeout: int | None = None,
        out_of_sync_threshold: int | None = None,
        send_tags_to_all_vdoms: str | None = None,
        websocket_override: str | None = None,
        interface_select_method: str | None = None,
        interface: str | None = None,
        trust_ca_cn: str | None = None,
        verifying_ca: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update this specific resource.

        Args:
            payload_dict: Optional dictionary of all parameters (can be passed
            as first positional arg)
            ems_id: Object identifier (required)
            before: If *action=move*, use *before* to specify the ID of the
            resource that this resource will be moved before. (optional)
            after: If *action=move*, use *after* to specify the ID of the
            resource that this resource will be moved after. (optional)
            ems_id: EMS ID in order (1 - 7). (optional)
            status: Enable or disable this EMS configuration. (optional)
            name: FortiClient Enterprise Management Server (EMS) name.
            (optional)
            dirty_reason: Dirty Reason for FortiClient EMS. (optional)
            fortinetone_cloud_authentication: Enable/disable authentication of
            FortiClient EMS Cloud through FortiCloud account. (optional)
            cloud_authentication_access_key: FortiClient EMS Cloud multitenancy
            access key (optional)
            server: FortiClient EMS FQDN or IPv4 address. (optional)
            https_port: FortiClient EMS HTTPS access port number. (1 - 65535,
            default: 443). (optional)
            serial_number: EMS Serial Number. (optional)
            tenant_id: EMS Tenant ID. (optional)
            source_ip: REST API call source IP. (optional)
            pull_sysinfo: Enable/disable pulling SysInfo from EMS. (optional)
            pull_vulnerabilities: Enable/disable pulling vulnerabilities from
            EMS. (optional)
            pull_tags: Enable/disable pulling FortiClient user tags from EMS.
            (optional)
            pull_malware_hash: Enable/disable pulling FortiClient malware hash
            from EMS. (optional)
            capabilities: List of EMS capabilities. (optional)
            call_timeout: FortiClient EMS call timeout in seconds (1 - 180
            seconds, default = 30). (optional)
            out_of_sync_threshold: Outdated resource threshold in seconds (10 -
            3600, default = 180). (optional)
            send_tags_to_all_vdoms: Relax restrictions on tags to send all EMS
            tags to all VDOMs (optional)
            websocket_override: Enable/disable override behavior for how this
            FortiGate unit connects to EMS using a WebSocket connection.
            (optional)
            interface_select_method: Specify how to select outgoing interface
            to reach server. (optional)
            interface: Specify outgoing interface to reach server. (optional)
            trust_ca_cn: Enable/disable trust of the EMS certificate issuer(CA)
            and common name(CN) for certificate auto-renewal. (optional)
            verifying_ca: Lowest CA cert on Fortigate in verified EMS cert
            chain. (optional)
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
        if not ems_id:
            raise ValueError("ems_id is required for put()")
        endpoint = f"/endpoint-control/fctems-override/{ems_id}"
        if before is not None:
            data_payload["before"] = before
        if after is not None:
            data_payload["after"] = after
        if ems_id is not None:
            data_payload["ems-id"] = ems_id
        if status is not None:
            data_payload["status"] = status
        if name is not None:
            data_payload["name"] = name
        if dirty_reason is not None:
            data_payload["dirty-reason"] = dirty_reason
        if fortinetone_cloud_authentication is not None:
            data_payload["fortinetone-cloud-authentication"] = (
                fortinetone_cloud_authentication
            )
        if cloud_authentication_access_key is not None:
            data_payload["cloud-authentication-access-key"] = (
                cloud_authentication_access_key
            )
        if server is not None:
            data_payload["server"] = server
        if https_port is not None:
            data_payload["https-port"] = https_port
        if serial_number is not None:
            data_payload["serial-number"] = serial_number
        if tenant_id is not None:
            data_payload["tenant-id"] = tenant_id
        if source_ip is not None:
            data_payload["source-ip"] = source_ip
        if pull_sysinfo is not None:
            data_payload["pull-sysinfo"] = pull_sysinfo
        if pull_vulnerabilities is not None:
            data_payload["pull-vulnerabilities"] = pull_vulnerabilities
        if pull_tags is not None:
            data_payload["pull-tags"] = pull_tags
        if pull_malware_hash is not None:
            data_payload["pull-malware-hash"] = pull_malware_hash
        if capabilities is not None:
            data_payload["capabilities"] = capabilities
        if call_timeout is not None:
            data_payload["call-timeout"] = call_timeout
        if out_of_sync_threshold is not None:
            data_payload["out-of-sync-threshold"] = out_of_sync_threshold
        if send_tags_to_all_vdoms is not None:
            data_payload["send-tags-to-all-vdoms"] = send_tags_to_all_vdoms
        if websocket_override is not None:
            data_payload["websocket-override"] = websocket_override
        if interface_select_method is not None:
            data_payload["interface-select-method"] = interface_select_method
        if interface is not None:
            data_payload["interface"] = interface
        if trust_ca_cn is not None:
            data_payload["trust-ca-cn"] = trust_ca_cn
        if verifying_ca is not None:
            data_payload["verifying-ca"] = verifying_ca
        data_payload.update(kwargs)
        return self._client.put(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )

    def delete(
        self,
        ems_id: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Delete this specific resource.

        Args:
            ems_id: Object identifier (required)
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
        if not ems_id:
            raise ValueError("ems_id is required for delete()")
        endpoint = f"/endpoint-control/fctems-override/{ems_id}"
        params.update(kwargs)
        return self._client.delete(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )

    def exists(
        self,
        ems_id: str,
        vdom: str | bool | None = None,
    ) -> Union[bool, Coroutine[Any, Any, bool]]:
        """
        Check if an object exists.

        Args:
            ems_id: Object identifier
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
        result = self.get(ems_id=ems_id, vdom=vdom)

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
        ems_id: int | None = None,
        status: str | None = None,
        name: str | None = None,
        dirty_reason: str | None = None,
        fortinetone_cloud_authentication: str | None = None,
        cloud_authentication_access_key: str | None = None,
        server: str | None = None,
        https_port: int | None = None,
        serial_number: str | None = None,
        tenant_id: str | None = None,
        source_ip: str | None = None,
        pull_sysinfo: str | None = None,
        pull_vulnerabilities: str | None = None,
        pull_tags: str | None = None,
        pull_malware_hash: str | None = None,
        capabilities: str | None = None,
        call_timeout: int | None = None,
        out_of_sync_threshold: int | None = None,
        send_tags_to_all_vdoms: str | None = None,
        websocket_override: str | None = None,
        interface_select_method: str | None = None,
        interface: str | None = None,
        trust_ca_cn: str | None = None,
        verifying_ca: str | None = None,
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
            ems_id: EMS ID in order (1 - 7). (optional)
            status: Enable or disable this EMS configuration. (optional)
            name: FortiClient Enterprise Management Server (EMS) name.
            (optional)
            dirty_reason: Dirty Reason for FortiClient EMS. (optional)
            fortinetone_cloud_authentication: Enable/disable authentication of
            FortiClient EMS Cloud through FortiCloud account. (optional)
            cloud_authentication_access_key: FortiClient EMS Cloud multitenancy
            access key (optional)
            server: FortiClient EMS FQDN or IPv4 address. (optional)
            https_port: FortiClient EMS HTTPS access port number. (1 - 65535,
            default: 443). (optional)
            serial_number: EMS Serial Number. (optional)
            tenant_id: EMS Tenant ID. (optional)
            source_ip: REST API call source IP. (optional)
            pull_sysinfo: Enable/disable pulling SysInfo from EMS. (optional)
            pull_vulnerabilities: Enable/disable pulling vulnerabilities from
            EMS. (optional)
            pull_tags: Enable/disable pulling FortiClient user tags from EMS.
            (optional)
            pull_malware_hash: Enable/disable pulling FortiClient malware hash
            from EMS. (optional)
            capabilities: List of EMS capabilities. (optional)
            call_timeout: FortiClient EMS call timeout in seconds (1 - 180
            seconds, default = 30). (optional)
            out_of_sync_threshold: Outdated resource threshold in seconds (10 -
            3600, default = 180). (optional)
            send_tags_to_all_vdoms: Relax restrictions on tags to send all EMS
            tags to all VDOMs (optional)
            websocket_override: Enable/disable override behavior for how this
            FortiGate unit connects to EMS using a WebSocket connection.
            (optional)
            interface_select_method: Specify how to select outgoing interface
            to reach server. (optional)
            interface: Specify outgoing interface to reach server. (optional)
            trust_ca_cn: Enable/disable trust of the EMS certificate issuer(CA)
            and common name(CN) for certificate auto-renewal. (optional)
            verifying_ca: Lowest CA cert on Fortigate in verified EMS cert
            chain. (optional)
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
        endpoint = "/endpoint-control/fctems-override"
        if nkey is not None:
            data_payload["nkey"] = nkey
        if ems_id is not None:
            data_payload["ems-id"] = ems_id
        if status is not None:
            data_payload["status"] = status
        if name is not None:
            data_payload["name"] = name
        if dirty_reason is not None:
            data_payload["dirty-reason"] = dirty_reason
        if fortinetone_cloud_authentication is not None:
            data_payload["fortinetone-cloud-authentication"] = (
                fortinetone_cloud_authentication
            )
        if cloud_authentication_access_key is not None:
            data_payload["cloud-authentication-access-key"] = (
                cloud_authentication_access_key
            )
        if server is not None:
            data_payload["server"] = server
        if https_port is not None:
            data_payload["https-port"] = https_port
        if serial_number is not None:
            data_payload["serial-number"] = serial_number
        if tenant_id is not None:
            data_payload["tenant-id"] = tenant_id
        if source_ip is not None:
            data_payload["source-ip"] = source_ip
        if pull_sysinfo is not None:
            data_payload["pull-sysinfo"] = pull_sysinfo
        if pull_vulnerabilities is not None:
            data_payload["pull-vulnerabilities"] = pull_vulnerabilities
        if pull_tags is not None:
            data_payload["pull-tags"] = pull_tags
        if pull_malware_hash is not None:
            data_payload["pull-malware-hash"] = pull_malware_hash
        if capabilities is not None:
            data_payload["capabilities"] = capabilities
        if call_timeout is not None:
            data_payload["call-timeout"] = call_timeout
        if out_of_sync_threshold is not None:
            data_payload["out-of-sync-threshold"] = out_of_sync_threshold
        if send_tags_to_all_vdoms is not None:
            data_payload["send-tags-to-all-vdoms"] = send_tags_to_all_vdoms
        if websocket_override is not None:
            data_payload["websocket-override"] = websocket_override
        if interface_select_method is not None:
            data_payload["interface-select-method"] = interface_select_method
        if interface is not None:
            data_payload["interface"] = interface
        if trust_ca_cn is not None:
            data_payload["trust-ca-cn"] = trust_ca_cn
        if verifying_ca is not None:
            data_payload["verifying-ca"] = verifying_ca
        data_payload.update(kwargs)
        return self._client.post(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )
