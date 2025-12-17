"""
FortiOS CMDB - Endpoint Control FortiClient EMS Override

Configure FortiClient Enterprise Management Server (EMS) override entries for granular control.

API Endpoints:
    GET    /api/v2/cmdb/endpoint-control/fctems-override           - List all / Get specific
    POST   /api/v2/cmdb/endpoint-control/fctems-override           - Create
    PUT    /api/v2/cmdb/endpoint-control/fctems-override/{ems-id}   - Update
    DELETE /api/v2/cmdb/endpoint-control/fctems-override/{ems-id}   - Delete
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Dict, Optional, Union

if TYPE_CHECKING:
    from ....http_client import HTTPClient


from hfortix.FortiOS.http_client import encode_path_component


class FctemsOverride:
    """FortiClient EMS Override endpoint"""

    def __init__(self, client: "HTTPClient") -> None:
        """
        Initialize FctemsOverride endpoint.

        Args:
            client: FortiOS API client instance
        """
        self._client = client

    def get(
        self,
        ems_id: Optional[str] = None,
        # Query parameters
        attr: Optional[str] = None,
        count: Optional[int] = None,
        skip_to_datasource: Optional[int] = None,
        acs: Optional[bool] = None,
        search: Optional[str] = None,
        scope: Optional[str] = None,
        datasource: Optional[bool] = None,
        with_meta: Optional[bool] = None,
        skip: Optional[bool] = None,
        format: Optional[str] = None,
        action: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Get FortiClient EMS override entry(ies).

        Args:
            ems_id (str, optional): EMS ID to retrieve. If None, retrieves all entries
            attr (str, optional): Attribute name that references other table
            count (int, optional): Maximum number of entries to return
            skip_to_datasource (int, optional): Skip to provided table's Nth entry
            acs (bool, optional): If true, returned results are in ascending order
            search (str, optional): Filter objects by search value
            scope (str, optional): Scope level - 'global', 'vdom', or 'both'
            datasource (bool, optional): Include datasource information
            with_meta (bool, optional): Include meta information
            skip (bool, optional): Enable CLI skip operator
            format (str, optional): List of property names to include, separated by |
            action (str, optional): Special action - 'default', 'schema', 'revision'
            vdom (str, optional): Virtual Domain name
            **kwargs: Additional query parameters

        Returns:
            dict: API response containing EMS override entry data

        Examples:
            >>> # List all EMS override entries
            >>> entries = fgt.cmdb.endpoint_control.fctems_override.list()

            >>> # Get a specific EMS override entry
            >>> entry = fgt.cmdb.endpoint_control.fctems_override.get('EMS1')

            >>> # Get with filtering
            >>> entries = fgt.cmdb.endpoint_control.fctems_override.get(
            ...     format='ems-id|status',
            ...     count=10
            ... )
        """
        params = {}
        param_map = {
            "attr": attr,
            "count": count,
            "skip_to_datasource": skip_to_datasource,
            "acs": acs,
            "search": search,
            "scope": scope,
            "datasource": datasource,
            "with_meta": with_meta,
            "skip": skip,
            "format": format,
            "action": action,
        }

        for key, value in param_map.items():
            if value is not None:
                params[key] = value

        params.update(kwargs)

        path = "endpoint-control/fctems-override"
        if ems_id:
            path = f"{path}/{ems_id}"

        return self._client.get(
            "cmdb", path, params=params if params else None, vdom=vdom, raw_json=raw_json
        )

    def post(
        self,
        payload_dict: Optional[Dict[str, Any]] = None,
        ems_id: Optional[str] = None,
        # Override configuration
        status: Optional[str] = None,
        name: Optional[str] = None,
        dirty_reason: Optional[str] = None,
        fortinetone_cloud_authentication: Optional[str] = None,
        server: Optional[str] = None,
        https_port: Optional[int] = None,
        serial_number: Optional[str] = None,
        tenant_id: Optional[str] = None,
        source_ip: Optional[str] = None,
        pull_sysinfo: Optional[str] = None,
        pull_vulnerabilities: Optional[str] = None,
        pull_avatars: Optional[str] = None,
        pull_tags: Optional[str] = None,
        pull_malware_hash: Optional[str] = None,
        cloud_server_type: Optional[str] = None,
        capabilities: Optional[list[str]] = None,
        call_timeout: Optional[int] = None,
        out_of_sync_threshold: Optional[int] = None,
        send_tags_to_all_vdoms: Optional[str] = None,
        websocket_override: Optional[str] = None,
        preserve_ssl_session: Optional[str] = None,
        interface_select_method: Optional[str] = None,
        interface: Optional[str] = None,
        trust_ca_cn: Optional[str] = None,
        verifying_ca: Optional[str] = None,
        status_check_interval: Optional[int] = None,
        vdom: Optional[Union[str, bool]] = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Create FortiClient EMS override entry.

        Args:
            ems_id (str): EMS ID (primary identifier)
            status (str, optional): Enable/disable override - 'enable'/'disable'
            name (str, optional): FortiClient EMS name
            dirty_reason (str, optional): Dirty reason - 'none'/'mismatched-ems-sn'
            fortinetone_cloud_authentication (str, optional): FortiCloud auth - 'enable'/'disable'
            server (str, optional): FortiClient EMS FQDN or IPv4 address
            https_port (int, optional): FortiClient EMS HTTPS access port (1-65535)
            serial_number (str, optional): FortiClient EMS Serial Number
            tenant_id (str, optional): EMS Tenant ID
            source_ip (str, optional): REST API call source IP
            pull_sysinfo (str, optional): Pull system info - 'enable'/'disable'
            pull_vulnerabilities (str, optional): Pull vulnerabilities - 'enable'/'disable'
            pull_avatars (str, optional): Pull avatars - 'enable'/'disable'
            pull_tags (str, optional): Pull endpoint tags - 'enable'/'disable'
            pull_malware_hash (str, optional): Pull malware hash - 'enable'/'disable'
            cloud_server_type (str, optional): Cloud server type - 'production'/'alpha'/'beta'
            capabilities (list, optional): List of EMS capabilities
            call_timeout (int, optional): FortiClient EMS call timeout in seconds (1-180)
            out_of_sync_threshold (int, optional): Outdated resource threshold (10-3600 seconds)
            send_tags_to_all_vdoms (str, optional): Send tags to all VDOMs - 'enable'/'disable'
            websocket_override (str, optional): WebSocket override - 'disable'/'enable'
            preserve_ssl_session (str, optional): Preserve SSL session - 'enable'/'disable'
            interface_select_method (str, optional): Interface selection - 'auto'/'sdwan'/'specify'
            interface (str, optional): Specify outgoing interface
            trust_ca_cn (str, optional): Trust CA CN - 'enable'/'disable'
            verifying_ca (str, optional): Lowest CA cert in chain for SSL verification
            status_check_interval (int, optional): Status check interval (0-120 seconds)
            vdom (str, optional): Virtual Domain name
            **kwargs: Additional parameters

        Returns:
            dict: API response

        Examples:
            >>> # POST - Create EMS override entry
            >>> result = fgt.cmdb.endpoint_control.fctems_override.create(
            ...     ems_id='EMS1',
            ...     status='enable',
            ...     server='ems-override.example.com',
            ...     https_port=8443
            ... )
        """
        data = {"ems-id": ems_id}

        param_map = {
            "status": status,
            "name": name,
            "dirty_reason": dirty_reason,
            "fortinetone_cloud_authentication": fortinetone_cloud_authentication,
            "server": server,
            "https_port": https_port,
            "serial_number": serial_number,
            "tenant_id": tenant_id,
            "source_ip": source_ip,
            "pull_sysinfo": pull_sysinfo,
            "pull_vulnerabilities": pull_vulnerabilities,
            "pull_avatars": pull_avatars,
            "pull_tags": pull_tags,
            "pull_malware_hash": pull_malware_hash,
            "cloud_server_type": cloud_server_type,
            "call_timeout": call_timeout,
            "out_of_sync_threshold": out_of_sync_threshold,
            "send_tags_to_all_vdoms": send_tags_to_all_vdoms,
            "websocket_override": websocket_override,
            "preserve_ssl_session": preserve_ssl_session,
            "interface_select_method": interface_select_method,
            "interface": interface,
            "trust_ca_cn": trust_ca_cn,
            "verifying_ca": verifying_ca,
            "status_check_interval": status_check_interval,
        }

        for key, value in param_map.items():
            if value is not None:
                data[key.replace("_", "-")] = value

        if capabilities is not None:
            data["capabilities"] = capabilities

        data.update(kwargs)

        return self._client.post(
            "cmdb", "endpoint-control/fctems-override", data=data, vdom=vdom, raw_json=raw_json
        )

    def put(
        self,
        payload_dict: Optional[Dict[str, Any]] = None,
        ems_id: Optional[str] = None,
        # Override configuration
        status: Optional[str] = None,
        name: Optional[str] = None,
        dirty_reason: Optional[str] = None,
        fortinetone_cloud_authentication: Optional[str] = None,
        server: Optional[str] = None,
        https_port: Optional[int] = None,
        serial_number: Optional[str] = None,
        tenant_id: Optional[str] = None,
        source_ip: Optional[str] = None,
        pull_sysinfo: Optional[str] = None,
        pull_vulnerabilities: Optional[str] = None,
        pull_avatars: Optional[str] = None,
        pull_tags: Optional[str] = None,
        pull_malware_hash: Optional[str] = None,
        cloud_server_type: Optional[str] = None,
        capabilities: Optional[list[str]] = None,
        call_timeout: Optional[int] = None,
        out_of_sync_threshold: Optional[int] = None,
        send_tags_to_all_vdoms: Optional[str] = None,
        websocket_override: Optional[str] = None,
        preserve_ssl_session: Optional[str] = None,
        interface_select_method: Optional[str] = None,
        interface: Optional[str] = None,
        trust_ca_cn: Optional[str] = None,
        verifying_ca: Optional[str] = None,
        status_check_interval: Optional[int] = None,
        # PUT - Update parameters
        action: Optional[str] = None,
        before: Optional[str] = None,
        after: Optional[str] = None,
        scope: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Update a FortiClient EMS override entry.

        Args:
            ems_id (str): EMS ID to update
            (Other parameters same as create method)
            action (str, optional): 'add-members', 'replace-members', 'remove-members'
            before (str, optional): Place new object before given object
            after (str, optional): Place new object after given object
            scope (str, optional): Scope level - 'global' or 'vdom'
            vdom (str, optional): Virtual Domain name
            **kwargs: Additional parameters

        Returns:
            dict: API response

        Examples:
            >>> # PUT - Update EMS override entry
            >>> result = fgt.cmdb.endpoint_control.fctems_override.update(
            ...     ems_id='EMS1',
            ...     status='disable',
            ...     https_port=9443
            ... )
        """
        data = {}

        param_map = {
            "status": status,
            "name": name,
            "dirty_reason": dirty_reason,
            "fortinetone_cloud_authentication": fortinetone_cloud_authentication,
            "server": server,
            "https_port": https_port,
            "serial_number": serial_number,
            "tenant_id": tenant_id,
            "source_ip": source_ip,
            "pull_sysinfo": pull_sysinfo,
            "pull_vulnerabilities": pull_vulnerabilities,
            "pull_avatars": pull_avatars,
            "pull_tags": pull_tags,
            "pull_malware_hash": pull_malware_hash,
            "cloud_server_type": cloud_server_type,
            "call_timeout": call_timeout,
            "out_of_sync_threshold": out_of_sync_threshold,
            "send_tags_to_all_vdoms": send_tags_to_all_vdoms,
            "websocket_override": websocket_override,
            "preserve_ssl_session": preserve_ssl_session,
            "interface_select_method": interface_select_method,
            "interface": interface,
            "trust_ca_cn": trust_ca_cn,
            "verifying_ca": verifying_ca,
            "status_check_interval": status_check_interval,
            "action": action,
            "before": before,
            "after": after,
            "scope": scope,
        }

        for key, value in param_map.items():
            if value is not None:
                data[key.replace("_", "-")] = value

        if capabilities is not None:
            data["capabilities"] = capabilities

        data.update(kwargs)

        return self._client.put(
            "cmdb",
            f"endpoint-control/fctems-override/{ems_id}",
            data=data,
            vdom=vdom,
            raw_json=raw_json,
        )

    def delete(
        self,
        ems_id: str,
        scope: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        raw_json: bool = False,
    ) -> dict[str, Any]:
        """
        Delete a FortiClient EMS override entry.

        Args:
            ems_id (str): EMS ID to delete
            scope (str, optional): Scope level - 'global' or 'vdom'
            vdom (str, optional): Virtual Domain name

        Returns:
            dict: API response

        Examples:
            >>> result = fgt.cmdb.endpoint_control.fctems_override.delete('EMS1')
        """
        params = {}
        if scope is not None:
            params["scope"] = scope

        return self._client.delete(
            "cmdb",
            f"endpoint-control/fctems-override/{ems_id}",
            params=params if params else None,
            vdom=vdom,
            raw_json=raw_json,
        )
