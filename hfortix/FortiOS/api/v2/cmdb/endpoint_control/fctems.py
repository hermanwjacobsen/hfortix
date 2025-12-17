"""
FortiOS CMDB - Endpoint Control FortiClient EMS

Configure FortiClient Enterprise Management Server (EMS) entries.

API Endpoints:
    GET    /api/v2/cmdb/endpoint-control/fctems           - List all EMS entries
    GET    /api/v2/cmdb/endpoint-control/fctems/{ems-id}  - Get specific EMS entry
    POST   /api/v2/cmdb/endpoint-control/fctems           - Create EMS entry
    PUT    /api/v2/cmdb/endpoint-control/fctems/{ems-id}  - Update EMS entry
    DELETE /api/v2/cmdb/endpoint-control/fctems/{ems-id}  - Delete EMS entry
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Dict, Optional, Union

if TYPE_CHECKING:
    from ....http_client import HTTPClient


from hfortix.FortiOS.http_client import encode_path_component


class Fctems:
    """FortiClient EMS endpoint"""

    def __init__(self, client: "HTTPClient") -> None:
        """
        Initialize Fctems endpoint.

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
        Get FortiClient EMS entry(ies).

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
            dict: API response containing EMS entry data

        Examples:
            >>> # List all EMS entries
            >>> entries = fgt.cmdb.endpoint_control.fctems.list()

            >>> # Get a specific EMS entry
            >>> entry = fgt.cmdb.endpoint_control.fctems.get('EMS1')

            >>> # Get with filtering
            >>> entries = fgt.cmdb.endpoint_control.fctems.get(
            ...     format='ems-id|name|server',
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

        path = "endpoint-control/fctems"
        if ems_id:
            path = f"{path}/{ems_id}"

        return self._client.get(
            "cmdb", path, params=params if params else None, vdom=vdom, raw_json=raw_json
        )

    def list(
        self,
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
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Get all FortiClient EMS entries (convenience method).

        Args:
            Same as get() method, excluding ems_id

        Returns:
            dict: API response containing all EMS entries

        Examples:
            >>> entries = fgt.cmdb.endpoint_control.fctems.list()
        """
        return self.get(
            ems_id=None,
            attr=attr,
            count=count,
            skip_to_datasource=skip_to_datasource,
            acs=acs,
            search=search,
            scope=scope,
            datasource=datasource,
            with_meta=with_meta,
            skip=skip,
            format=format,
            action=action,
            vdom=vdom,
            **kwargs,
        )

    def create(
        self,
        payload_dict: Optional[Dict[str, Any]] = None,
        name: Optional[str] = None,
        # EMS configuration
        ems_id: Optional[str] = None,
        status: Optional[str] = None,
        address: Optional[str] = None,
        serial_number: Optional[str] = None,
        fortinetone_cloud_authentication: Optional[str] = None,
        server: Optional[str] = None,
        https_port: Optional[int] = None,
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
        certificate_fingerprint: Optional[str] = None,
        admin_username: Optional[str] = None,
        admin_password: Optional[str] = None,
        admin_type: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Create a new FortiClient EMS entry.

        Args:
            name (str): EMS entry name
            ems_id (str, optional): EMS ID
            status (str, optional): Enable/disable - 'enable'/'disable'
            address (str, optional): EMS IP address or FQDN
            serial_number (str, optional): EMS serial number
            fortinetone_cloud_authentication (str, optional): FortiCloud auth - 'enable'/'disable'
            server (str, optional): EMS server address
            https_port (int, optional): HTTPS port (1-65535)
            source_ip (str, optional): Source IP for communication
            pull_sysinfo (str, optional): Pull system info - 'enable'/'disable'
            pull_vulnerabilities (str, optional): Pull vulnerabilities - 'enable'/'disable'
            pull_avatars (str, optional): Pull avatars - 'enable'/'disable'
            pull_tags (str, optional): Pull tags - 'enable'/'disable'
            pull_malware_hash (str, optional): Pull malware hash - 'enable'/'disable'
            cloud_server_type (str, optional): Cloud server type - 'production'/'alpha'/'beta'
            capabilities (list, optional): EMS capabilities list
            call_timeout (int, optional): Call timeout in seconds
            out_of_sync_threshold (int, optional): Out of sync threshold
            send_tags_to_all_vdoms (str, optional): Send tags to all VDOMs - 'enable'/'disable'
            websocket_override (str, optional): WebSocket override - 'disable'/'enable'
            preserve_ssl_session (str, optional): Preserve SSL session - 'enable'/'disable'
            interface_select_method (str, optional): Interface select method - 'auto'/'sdwan'/'specify'
            interface (str, optional): Interface name
            trust_ca_cn (str, optional): Trust CA CN - 'enable'/'disable'
            verifying_ca (str, optional): Verifying CA certificate
            status_check_interval (int, optional): Status check interval in seconds
            certificate_fingerprint (str, optional): Certificate fingerprint
            admin_username (str, optional): Admin username
            admin_password (str, optional): Admin password
            admin_type (str, optional): Admin type - 'Windows'/'LDAP'
            vdom (str, optional): Virtual Domain name
            **kwargs: Additional parameters

        Returns:
            dict: API response

        Examples:
            >>> # Create EMS entry
            >>> result = fgt.cmdb.endpoint_control.fctems.create(
            ...     name='EMS1',
            ...     server='ems.example.com',
            ...     https_port=443,
            ...     status='enable'
            ... )
        """
        data = {"name": name}

        param_map = {
            "ems_id": ems_id,
            "status": status,
            "address": address,
            "serial_number": serial_number,
            "fortinetone_cloud_authentication": fortinetone_cloud_authentication,
            "server": server,
            "https_port": https_port,
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
            "certificate_fingerprint": certificate_fingerprint,
            "admin_username": admin_username,
            "admin_password": admin_password,
            "admin_type": admin_type,
        }

        for key, value in param_map.items():
            if value is not None:
                data[key.replace("_", "-")] = value

        if capabilities is not None:
            data["capabilities"] = capabilities

        data.update(kwargs)

        return self._client.post(
            "cmdb", "endpoint-control/fctems", data=data, vdom=vdom, raw_json=raw_json
        )

    def update(
        self,
        payload_dict: Optional[Dict[str, Any]] = None,
        ems_id: Optional[str] = None,
        # EMS configuration
        name: Optional[str] = None,
        status: Optional[str] = None,
        address: Optional[str] = None,
        serial_number: Optional[str] = None,
        fortinetone_cloud_authentication: Optional[str] = None,
        server: Optional[str] = None,
        https_port: Optional[int] = None,
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
        certificate_fingerprint: Optional[str] = None,
        admin_username: Optional[str] = None,
        admin_password: Optional[str] = None,
        admin_type: Optional[str] = None,
        # Update parameters
        action: Optional[str] = None,
        before: Optional[str] = None,
        after: Optional[str] = None,
        scope: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Update a FortiClient EMS entry.

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
            >>> # Update EMS entry
            >>> result = fgt.cmdb.endpoint_control.fctems.update(
            ...     ems_id='EMS1',
            ...     status='enable',
            ...     https_port=8443
            ... )
        """
        data = {}

        param_map = {
            "name": name,
            "status": status,
            "address": address,
            "serial_number": serial_number,
            "fortinetone_cloud_authentication": fortinetone_cloud_authentication,
            "server": server,
            "https_port": https_port,
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
            "certificate_fingerprint": certificate_fingerprint,
            "admin_username": admin_username,
            "admin_password": admin_password,
            "admin_type": admin_type,
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
            "cmdb", f"endpoint-control/fctems/{ems_id}", data=data, vdom=vdom, raw_json=raw_json
        )

    def delete(
        self,
        ems_id: str,
        scope: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        raw_json: bool = False,
    ) -> dict[str, Any]:
        """
        Delete a FortiClient EMS entry.

        Args:
            ems_id (str): EMS ID to delete
            scope (str, optional): Scope level - 'global' or 'vdom'
            vdom (str, optional): Virtual Domain name

        Returns:
            dict: API response

        Examples:
            >>> result = fgt.cmdb.endpoint_control.fctems.delete('EMS1')
        """
        params = {}
        if scope is not None:
            params["scope"] = scope

        return self._client.delete(
            "cmdb",
            f"endpoint-control/fctems/{ems_id}",
            params=params if params else None,
            vdom=vdom,
            raw_json=raw_json,
        )
