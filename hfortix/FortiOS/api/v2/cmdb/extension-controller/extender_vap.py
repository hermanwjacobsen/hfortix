"""
FortiOS CMDB - Cmdb Extension Controller Extender Vap

Configuration endpoint for managing cmdb extension controller extender vap
objects.

API Endpoints:
    GET    /cmdb/extension-controller/extender_vap
    POST   /cmdb/extension-controller/extender_vap
    GET    /cmdb/extension-controller/extender_vap
    PUT    /cmdb/extension-controller/extender_vap/{identifier}
    DELETE /cmdb/extension-controller/extender_vap/{identifier}

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.extension_controller.extender_vap.get()
    >>>
    >>> # Get specific item (if supported)
    >>> item =
    fgt.api.cmdb.extension_controller.extender_vap.get(name="item_name")
    >>>
    >>> # Create new item (use POST)
    >>> result = fgt.api.cmdb.extension_controller.extender_vap.post(
    ...     name="new_item",
    ...     # ... additional parameters
    ... )
    >>>
    >>> # Update existing item (use PUT)
    >>> result = fgt.api.cmdb.extension_controller.extender_vap.put(
    ...     name="existing_item",
    ...     # ... parameters to update
    ... )
    >>>
    >>> # Delete item
    >>> result =
    fgt.api.cmdb.extension_controller.extender_vap.delete(name="item_name")

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


class ExtenderVap:
    """
    Extendervap Operations.

    Provides CRUD operations for FortiOS extendervap configuration.

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
        Initialize ExtenderVap endpoint.

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
            endpoint = f"/extension-controller/extender-vap/{name}"
        else:
            endpoint = "/extension-controller/extender-vap"
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
        type: str | None = None,
        ssid: str | None = None,
        max_clients: int | None = None,
        broadcast_ssid: str | None = None,
        security: str | None = None,
        dtim: int | None = None,
        rts_threshold: int | None = None,
        pmf: str | None = None,
        target_wake_time: str | None = None,
        bss_color_partial: str | None = None,
        mu_mimo: str | None = None,
        passphrase: str | None = None,
        sae_password: str | None = None,
        auth_server_address: str | None = None,
        auth_server_port: int | None = None,
        auth_server_secret: str | None = None,
        ip_address: str | None = None,
        start_ip: str | None = None,
        end_ip: str | None = None,
        allowaccess: str | None = None,
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
            name: Wi-Fi VAP name. (optional)
            type: Wi-Fi VAP type local-vap / lan-extension-vap. (optional)
            ssid: Wi-Fi SSID. (optional)
            max_clients: Wi-Fi max clients (0 - 512), default = 0 (no limit)
            (optional)
            broadcast_ssid: Wi-Fi broadcast SSID enable / disable. (optional)
            security: Wi-Fi security. (optional)
            dtim: Wi-Fi DTIM (1 - 255) default = 1. (optional)
            rts_threshold: Wi-Fi RTS Threshold (256 - 2347), default = 2347
            (RTS/CTS disabled). (optional)
            pmf: Wi-Fi pmf enable/disable, default = disable. (optional)
            target_wake_time: Wi-Fi 802.11AX target wake time enable / disable,
            default = enable. (optional)
            bss_color_partial: Wi-Fi 802.11AX bss color partial enable /
            disable, default = enable. (optional)
            mu_mimo: Wi-Fi multi-user MIMO enable / disable, default = enable.
            (optional)
            passphrase: Wi-Fi passphrase. (optional)
            sae_password: Wi-Fi SAE Password. (optional)
            auth_server_address: Wi-Fi Authentication Server Address (IPv4
            format). (optional)
            auth_server_port: Wi-Fi Authentication Server Port. (optional)
            auth_server_secret: Wi-Fi Authentication Server Secret. (optional)
            ip_address: Extender ip address. (optional)
            start_ip: Start ip address. (optional)
            end_ip: End ip address. (optional)
            allowaccess: Control management access to the managed extender.
            Separate entries with a space. (optional)
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
        endpoint = f"/extension-controller/extender-vap/{name}"
        if before is not None:
            data_payload["before"] = before
        if after is not None:
            data_payload["after"] = after
        if name is not None:
            data_payload["name"] = name
        if type is not None:
            data_payload["type"] = type
        if ssid is not None:
            data_payload["ssid"] = ssid
        if max_clients is not None:
            data_payload["max-clients"] = max_clients
        if broadcast_ssid is not None:
            data_payload["broadcast-ssid"] = broadcast_ssid
        if security is not None:
            data_payload["security"] = security
        if dtim is not None:
            data_payload["dtim"] = dtim
        if rts_threshold is not None:
            data_payload["rts-threshold"] = rts_threshold
        if pmf is not None:
            data_payload["pm"] = pmf
        if target_wake_time is not None:
            data_payload["target-wake-time"] = target_wake_time
        if bss_color_partial is not None:
            data_payload["bss-color-partial"] = bss_color_partial
        if mu_mimo is not None:
            data_payload["mu-mimo"] = mu_mimo
        if passphrase is not None:
            data_payload["passphrase"] = passphrase
        if sae_password is not None:
            data_payload["sae-password"] = sae_password
        if auth_server_address is not None:
            data_payload["auth-server-address"] = auth_server_address
        if auth_server_port is not None:
            data_payload["auth-server-port"] = auth_server_port
        if auth_server_secret is not None:
            data_payload["auth-server-secret"] = auth_server_secret
        if ip_address is not None:
            data_payload["ip-address"] = ip_address
        if start_ip is not None:
            data_payload["start-ip"] = start_ip
        if end_ip is not None:
            data_payload["end-ip"] = end_ip
        if allowaccess is not None:
            data_payload["allowaccess"] = allowaccess
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
        endpoint = f"/extension-controller/extender-vap/{name}"
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
        type: str | None = None,
        ssid: str | None = None,
        max_clients: int | None = None,
        broadcast_ssid: str | None = None,
        security: str | None = None,
        dtim: int | None = None,
        rts_threshold: int | None = None,
        pmf: str | None = None,
        target_wake_time: str | None = None,
        bss_color_partial: str | None = None,
        mu_mimo: str | None = None,
        passphrase: str | None = None,
        sae_password: str | None = None,
        auth_server_address: str | None = None,
        auth_server_port: int | None = None,
        auth_server_secret: str | None = None,
        ip_address: str | None = None,
        start_ip: str | None = None,
        end_ip: str | None = None,
        allowaccess: str | None = None,
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
            name: Wi-Fi VAP name. (optional)
            type: Wi-Fi VAP type local-vap / lan-extension-vap. (optional)
            ssid: Wi-Fi SSID. (optional)
            max_clients: Wi-Fi max clients (0 - 512), default = 0 (no limit)
            (optional)
            broadcast_ssid: Wi-Fi broadcast SSID enable / disable. (optional)
            security: Wi-Fi security. (optional)
            dtim: Wi-Fi DTIM (1 - 255) default = 1. (optional)
            rts_threshold: Wi-Fi RTS Threshold (256 - 2347), default = 2347
            (RTS/CTS disabled). (optional)
            pmf: Wi-Fi pmf enable/disable, default = disable. (optional)
            target_wake_time: Wi-Fi 802.11AX target wake time enable / disable,
            default = enable. (optional)
            bss_color_partial: Wi-Fi 802.11AX bss color partial enable /
            disable, default = enable. (optional)
            mu_mimo: Wi-Fi multi-user MIMO enable / disable, default = enable.
            (optional)
            passphrase: Wi-Fi passphrase. (optional)
            sae_password: Wi-Fi SAE Password. (optional)
            auth_server_address: Wi-Fi Authentication Server Address (IPv4
            format). (optional)
            auth_server_port: Wi-Fi Authentication Server Port. (optional)
            auth_server_secret: Wi-Fi Authentication Server Secret. (optional)
            ip_address: Extender ip address. (optional)
            start_ip: Start ip address. (optional)
            end_ip: End ip address. (optional)
            allowaccess: Control management access to the managed extender.
            Separate entries with a space. (optional)
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
        endpoint = "/extension-controller/extender-vap"
        if nkey is not None:
            data_payload["nkey"] = nkey
        if name is not None:
            data_payload["name"] = name
        if type is not None:
            data_payload["type"] = type
        if ssid is not None:
            data_payload["ssid"] = ssid
        if max_clients is not None:
            data_payload["max-clients"] = max_clients
        if broadcast_ssid is not None:
            data_payload["broadcast-ssid"] = broadcast_ssid
        if security is not None:
            data_payload["security"] = security
        if dtim is not None:
            data_payload["dtim"] = dtim
        if rts_threshold is not None:
            data_payload["rts-threshold"] = rts_threshold
        if pmf is not None:
            data_payload["pm"] = pmf
        if target_wake_time is not None:
            data_payload["target-wake-time"] = target_wake_time
        if bss_color_partial is not None:
            data_payload["bss-color-partial"] = bss_color_partial
        if mu_mimo is not None:
            data_payload["mu-mimo"] = mu_mimo
        if passphrase is not None:
            data_payload["passphrase"] = passphrase
        if sae_password is not None:
            data_payload["sae-password"] = sae_password
        if auth_server_address is not None:
            data_payload["auth-server-address"] = auth_server_address
        if auth_server_port is not None:
            data_payload["auth-server-port"] = auth_server_port
        if auth_server_secret is not None:
            data_payload["auth-server-secret"] = auth_server_secret
        if ip_address is not None:
            data_payload["ip-address"] = ip_address
        if start_ip is not None:
            data_payload["start-ip"] = start_ip
        if end_ip is not None:
            data_payload["end-ip"] = end_ip
        if allowaccess is not None:
            data_payload["allowaccess"] = allowaccess
        data_payload.update(kwargs)
        return self._client.post(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )
