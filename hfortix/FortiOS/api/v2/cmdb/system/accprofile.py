"""
FortiOS CMDB - Cmdb System Accprofile

Configuration endpoint for managing cmdb system accprofile objects.

API Endpoints:
    GET    /cmdb/system/accprofile
    POST   /cmdb/system/accprofile
    GET    /cmdb/system/accprofile
    PUT    /cmdb/system/accprofile/{identifier}
    DELETE /cmdb/system/accprofile/{identifier}

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.system.accprofile.get()
    >>>
    >>> # Get specific item (if supported)
    >>> item = fgt.api.cmdb.system.accprofile.get(name="item_name")
    >>>
    >>> # Create new item (use POST)
    >>> result = fgt.api.cmdb.system.accprofile.post(
    ...     name="new_item",
    ...     # ... additional parameters
    ... )
    >>>
    >>> # Update existing item (use PUT)
    >>> result = fgt.api.cmdb.system.accprofile.put(
    ...     name="existing_item",
    ...     # ... parameters to update
    ... )
    >>>
    >>> # Delete item
    >>> result = fgt.api.cmdb.system.accprofile.delete(name="item_name")

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


class Accprofile:
    """
    Accprofile Operations.

    Provides CRUD operations for FortiOS accprofile configuration.

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
        Initialize Accprofile endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

    def get(
        self,
        name: str | None = None,
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
            name: Object identifier (optional for list, required for specific)
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
        if name:
            endpoint = f"/system/accprofile/{name}"
        else:
            endpoint = "/system/accprofile"
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
        name: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        before: str | None = None,
        after: str | None = None,
        comments: str | None = None,
        secfabgrp: str | None = None,
        ftviewgrp: str | None = None,
        authgrp: str | None = None,
        sysgrp: str | None = None,
        netgrp: str | None = None,
        loggrp: str | None = None,
        fwgrp: str | None = None,
        vpngrp: str | None = None,
        utmgrp: str | None = None,
        wifi: str | None = None,
        netgrp_permission: list | None = None,
        sysgrp_permission: list | None = None,
        fwgrp_permission: list | None = None,
        loggrp_permission: list | None = None,
        utmgrp_permission: list | None = None,
        secfabgrp_permission: list | None = None,
        admintimeout_override: str | None = None,
        admintimeout: int | None = None,
        cli_diagnose: str | None = None,
        cli_get: str | None = None,
        cli_show: str | None = None,
        cli_exec: str | None = None,
        cli_config: str | None = None,
        system_execute_ssh: str | None = None,
        system_execute_telnet: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update this specific resource.

        Args:
            payload_dict: Optional dictionary of all parameters (can be passed
            as first positional arg)
            name: Object identifier (required)
            before: If *action=move*, use *before* to specify the ID of the
            resource that this resource will be moved before. (optional)
            after: If *action=move*, use *after* to specify the ID of the
            resource that this resource will be moved after. (optional)
            name: Profile name. (optional)
            comments: Comment. (optional)
            secfabgrp: Security Fabric. (optional)
            ftviewgrp: FortiView. (optional)
            authgrp: Administrator access to Users and Devices. (optional)
            sysgrp: System Configuration. (optional)
            netgrp: Network Configuration. (optional)
            loggrp: Administrator access to Logging and Reporting including
            viewing log messages. (optional)
            fwgrp: Administrator access to the Firewall configuration.
            (optional)
            vpngrp: Administrator access to IPsec, SSL, PPTP, and L2TP VPN.
            (optional)
            utmgrp: Administrator access to Security Profiles. (optional)
            wifi: Administrator access to the WiFi controller and Switch
            controller. (optional)
            netgrp_permission: Custom network permission. (optional)
            sysgrp_permission: Custom system permission. (optional)
            fwgrp_permission: Custom firewall permission. (optional)
            loggrp_permission: Custom Log & Report permission. (optional)
            utmgrp_permission: Custom Security Profile permissions. (optional)
            secfabgrp_permission: Custom Security Fabric permissions.
            (optional)
            admintimeout_override: Enable/disable overriding the global
            administrator idle timeout. (optional)
            admintimeout: Administrator timeout for this access profile (0 -
            480 min, default = 10, 0 means never timeout). (optional)
            cli_diagnose: Enable/disable permission to run diagnostic commands.
            (optional)
            cli_get: Enable/disable permission to run get commands. (optional)
            cli_show: Enable/disable permission to run show commands.
            (optional)
            cli_exec: Enable/disable permission to run execute commands.
            (optional)
            cli_config: Enable/disable permission to run config commands.
            (optional)
            system_execute_ssh: Enable/disable permission to execute SSH
            commands. (optional)
            system_execute_telnet: Enable/disable permission to execute TELNET
            commands. (optional)
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
        if not name:
            raise ValueError("name is required for put()")
        endpoint = f"/system/accprofile/{name}"
        if before is not None:
            data_payload["before"] = before
        if after is not None:
            data_payload["after"] = after
        if name is not None:
            data_payload["name"] = name
        if comments is not None:
            data_payload["comments"] = comments
        if secfabgrp is not None:
            data_payload["secfabgrp"] = secfabgrp
        if ftviewgrp is not None:
            data_payload["ftviewgrp"] = ftviewgrp
        if authgrp is not None:
            data_payload["authgrp"] = authgrp
        if sysgrp is not None:
            data_payload["sysgrp"] = sysgrp
        if netgrp is not None:
            data_payload["netgrp"] = netgrp
        if loggrp is not None:
            data_payload["loggrp"] = loggrp
        if fwgrp is not None:
            data_payload["fwgrp"] = fwgrp
        if vpngrp is not None:
            data_payload["vpngrp"] = vpngrp
        if utmgrp is not None:
            data_payload["utmgrp"] = utmgrp
        if wifi is not None:
            data_payload["wifi"] = wifi
        if netgrp_permission is not None:
            data_payload["netgrp-permission"] = netgrp_permission
        if sysgrp_permission is not None:
            data_payload["sysgrp-permission"] = sysgrp_permission
        if fwgrp_permission is not None:
            data_payload["fwgrp-permission"] = fwgrp_permission
        if loggrp_permission is not None:
            data_payload["loggrp-permission"] = loggrp_permission
        if utmgrp_permission is not None:
            data_payload["utmgrp-permission"] = utmgrp_permission
        if secfabgrp_permission is not None:
            data_payload["secfabgrp-permission"] = secfabgrp_permission
        if admintimeout_override is not None:
            data_payload["admintimeout-override"] = admintimeout_override
        if admintimeout is not None:
            data_payload["admintimeout"] = admintimeout
        if cli_diagnose is not None:
            data_payload["cli-diagnose"] = cli_diagnose
        if cli_get is not None:
            data_payload["cli-get"] = cli_get
        if cli_show is not None:
            data_payload["cli-show"] = cli_show
        if cli_exec is not None:
            data_payload["cli-exec"] = cli_exec
        if cli_config is not None:
            data_payload["cli-config"] = cli_config
        if system_execute_ssh is not None:
            data_payload["system-execute-ssh"] = system_execute_ssh
        if system_execute_telnet is not None:
            data_payload["system-execute-telnet"] = system_execute_telnet
        data_payload.update(kwargs)
        return self._client.put(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )

    def delete(
        self,
        name: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Delete this specific resource.

        Args:
            name: Object identifier (required)
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
        if not name:
            raise ValueError("name is required for delete()")
        endpoint = f"/system/accprofile/{name}"
        params.update(kwargs)
        return self._client.delete(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )

    def exists(
        self,
        name: str,
        vdom: str | bool | None = None,
    ) -> Union[bool, Coroutine[Any, Any, bool]]:
        """
        Check if an object exists.

        Args:
            name: Object identifier
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
        result = self.get(name=name, vdom=vdom)

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
        name: str | None = None,
        comments: str | None = None,
        secfabgrp: str | None = None,
        ftviewgrp: str | None = None,
        authgrp: str | None = None,
        sysgrp: str | None = None,
        netgrp: str | None = None,
        loggrp: str | None = None,
        fwgrp: str | None = None,
        vpngrp: str | None = None,
        utmgrp: str | None = None,
        wifi: str | None = None,
        netgrp_permission: list | None = None,
        sysgrp_permission: list | None = None,
        fwgrp_permission: list | None = None,
        loggrp_permission: list | None = None,
        utmgrp_permission: list | None = None,
        secfabgrp_permission: list | None = None,
        admintimeout_override: str | None = None,
        admintimeout: int | None = None,
        cli_diagnose: str | None = None,
        cli_get: str | None = None,
        cli_show: str | None = None,
        cli_exec: str | None = None,
        cli_config: str | None = None,
        system_execute_ssh: str | None = None,
        system_execute_telnet: str | None = None,
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
            name: Profile name. (optional)
            comments: Comment. (optional)
            secfabgrp: Security Fabric. (optional)
            ftviewgrp: FortiView. (optional)
            authgrp: Administrator access to Users and Devices. (optional)
            sysgrp: System Configuration. (optional)
            netgrp: Network Configuration. (optional)
            loggrp: Administrator access to Logging and Reporting including
            viewing log messages. (optional)
            fwgrp: Administrator access to the Firewall configuration.
            (optional)
            vpngrp: Administrator access to IPsec, SSL, PPTP, and L2TP VPN.
            (optional)
            utmgrp: Administrator access to Security Profiles. (optional)
            wifi: Administrator access to the WiFi controller and Switch
            controller. (optional)
            netgrp_permission: Custom network permission. (optional)
            sysgrp_permission: Custom system permission. (optional)
            fwgrp_permission: Custom firewall permission. (optional)
            loggrp_permission: Custom Log & Report permission. (optional)
            utmgrp_permission: Custom Security Profile permissions. (optional)
            secfabgrp_permission: Custom Security Fabric permissions.
            (optional)
            admintimeout_override: Enable/disable overriding the global
            administrator idle timeout. (optional)
            admintimeout: Administrator timeout for this access profile (0 -
            480 min, default = 10, 0 means never timeout). (optional)
            cli_diagnose: Enable/disable permission to run diagnostic commands.
            (optional)
            cli_get: Enable/disable permission to run get commands. (optional)
            cli_show: Enable/disable permission to run show commands.
            (optional)
            cli_exec: Enable/disable permission to run execute commands.
            (optional)
            cli_config: Enable/disable permission to run config commands.
            (optional)
            system_execute_ssh: Enable/disable permission to execute SSH
            commands. (optional)
            system_execute_telnet: Enable/disable permission to execute TELNET
            commands. (optional)
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
        endpoint = "/system/accprofile"
        if nkey is not None:
            data_payload["nkey"] = nkey
        if name is not None:
            data_payload["name"] = name
        if comments is not None:
            data_payload["comments"] = comments
        if secfabgrp is not None:
            data_payload["secfabgrp"] = secfabgrp
        if ftviewgrp is not None:
            data_payload["ftviewgrp"] = ftviewgrp
        if authgrp is not None:
            data_payload["authgrp"] = authgrp
        if sysgrp is not None:
            data_payload["sysgrp"] = sysgrp
        if netgrp is not None:
            data_payload["netgrp"] = netgrp
        if loggrp is not None:
            data_payload["loggrp"] = loggrp
        if fwgrp is not None:
            data_payload["fwgrp"] = fwgrp
        if vpngrp is not None:
            data_payload["vpngrp"] = vpngrp
        if utmgrp is not None:
            data_payload["utmgrp"] = utmgrp
        if wifi is not None:
            data_payload["wifi"] = wifi
        if netgrp_permission is not None:
            data_payload["netgrp-permission"] = netgrp_permission
        if sysgrp_permission is not None:
            data_payload["sysgrp-permission"] = sysgrp_permission
        if fwgrp_permission is not None:
            data_payload["fwgrp-permission"] = fwgrp_permission
        if loggrp_permission is not None:
            data_payload["loggrp-permission"] = loggrp_permission
        if utmgrp_permission is not None:
            data_payload["utmgrp-permission"] = utmgrp_permission
        if secfabgrp_permission is not None:
            data_payload["secfabgrp-permission"] = secfabgrp_permission
        if admintimeout_override is not None:
            data_payload["admintimeout-override"] = admintimeout_override
        if admintimeout is not None:
            data_payload["admintimeout"] = admintimeout
        if cli_diagnose is not None:
            data_payload["cli-diagnose"] = cli_diagnose
        if cli_get is not None:
            data_payload["cli-get"] = cli_get
        if cli_show is not None:
            data_payload["cli-show"] = cli_show
        if cli_exec is not None:
            data_payload["cli-exec"] = cli_exec
        if cli_config is not None:
            data_payload["cli-config"] = cli_config
        if system_execute_ssh is not None:
            data_payload["system-execute-ssh"] = system_execute_ssh
        if system_execute_telnet is not None:
            data_payload["system-execute-telnet"] = system_execute_telnet
        data_payload.update(kwargs)
        return self._client.post(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )
