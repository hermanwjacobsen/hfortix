"""
FortiOS CMDB - Cmdb Firewall Access Proxy Ssh Client Cert

Configuration endpoint for managing cmdb firewall access proxy ssh client cert
objects.

API Endpoints:
    GET    /cmdb/firewall/access_proxy_ssh_client_cert
    POST   /cmdb/firewall/access_proxy_ssh_client_cert
    GET    /cmdb/firewall/access_proxy_ssh_client_cert
    PUT    /cmdb/firewall/access_proxy_ssh_client_cert/{identifier}
    DELETE /cmdb/firewall/access_proxy_ssh_client_cert/{identifier}

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.firewall.access_proxy_ssh_client_cert.get()
    >>>
    >>> # Get specific item (if supported)
    >>> item =
    fgt.api.cmdb.firewall.access_proxy_ssh_client_cert.get(name="item_name")
    >>>
    >>> # Create new item (use POST)
    >>> result = fgt.api.cmdb.firewall.access_proxy_ssh_client_cert.post(
    ...     name="new_item",
    ...     # ... additional parameters
    ... )
    >>>
    >>> # Update existing item (use PUT)
    >>> result = fgt.api.cmdb.firewall.access_proxy_ssh_client_cert.put(
    ...     name="existing_item",
    ...     # ... parameters to update
    ... )
    >>>
    >>> # Delete item
    >>> result =
    fgt.api.cmdb.firewall.access_proxy_ssh_client_cert.delete(name="item_name")

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


class AccessProxySshClientCert:
    """
    Accessproxysshclientcert Operations.

    Provides CRUD operations for FortiOS accessproxysshclientcert
    configuration.

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
        Initialize AccessProxySshClientCert endpoint.

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
            endpoint = f"/firewall/access-proxy-ssh-client-cert/{name}"
        else:
            endpoint = "/firewall/access-proxy-ssh-client-cert"
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
        source_address: str | None = None,
        permit_x11_forwarding: str | None = None,
        permit_agent_forwarding: str | None = None,
        permit_port_forwarding: str | None = None,
        permit_pty: str | None = None,
        permit_user_rc: str | None = None,
        cert_extension: list | None = None,
        auth_ca: str | None = None,
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
            name: SSH client certificate name. (optional)
            source_address: Enable/disable appending source-address certificate
            critical option. This option ensure certificate only accepted from
            FortiGate source address. (optional)
            permit_x11_forwarding: Enable/disable appending
            permit-x11-forwarding certificate extension. (optional)
            permit_agent_forwarding: Enable/disable appending
            permit-agent-forwarding certificate extension. (optional)
            permit_port_forwarding: Enable/disable appending
            permit-port-forwarding certificate extension. (optional)
            permit_pty: Enable/disable appending permit-pty certificate
            extension. (optional)
            permit_user_rc: Enable/disable appending permit-user-rc certificate
            extension. (optional)
            cert_extension: Configure certificate extension for user
            certificate. (optional)
            auth_ca: Name of the SSH server public key authentication CA.
            (optional)
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
        endpoint = f"/firewall/access-proxy-ssh-client-cert/{name}"
        if before is not None:
            data_payload["before"] = before
        if after is not None:
            data_payload["after"] = after
        if name is not None:
            data_payload["name"] = name
        if source_address is not None:
            data_payload["source-address"] = source_address
        if permit_x11_forwarding is not None:
            data_payload["permit-x11-forwarding"] = permit_x11_forwarding
        if permit_agent_forwarding is not None:
            data_payload["permit-agent-forwarding"] = permit_agent_forwarding
        if permit_port_forwarding is not None:
            data_payload["permit-port-forwarding"] = permit_port_forwarding
        if permit_pty is not None:
            data_payload["permit-pty"] = permit_pty
        if permit_user_rc is not None:
            data_payload["permit-user-rc"] = permit_user_rc
        if cert_extension is not None:
            data_payload["cert-extension"] = cert_extension
        if auth_ca is not None:
            data_payload["auth-ca"] = auth_ca
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
        endpoint = f"/firewall/access-proxy-ssh-client-cert/{name}"
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
        source_address: str | None = None,
        permit_x11_forwarding: str | None = None,
        permit_agent_forwarding: str | None = None,
        permit_port_forwarding: str | None = None,
        permit_pty: str | None = None,
        permit_user_rc: str | None = None,
        cert_extension: list | None = None,
        auth_ca: str | None = None,
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
            name: SSH client certificate name. (optional)
            source_address: Enable/disable appending source-address certificate
            critical option. This option ensure certificate only accepted from
            FortiGate source address. (optional)
            permit_x11_forwarding: Enable/disable appending
            permit-x11-forwarding certificate extension. (optional)
            permit_agent_forwarding: Enable/disable appending
            permit-agent-forwarding certificate extension. (optional)
            permit_port_forwarding: Enable/disable appending
            permit-port-forwarding certificate extension. (optional)
            permit_pty: Enable/disable appending permit-pty certificate
            extension. (optional)
            permit_user_rc: Enable/disable appending permit-user-rc certificate
            extension. (optional)
            cert_extension: Configure certificate extension for user
            certificate. (optional)
            auth_ca: Name of the SSH server public key authentication CA.
            (optional)
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
        endpoint = "/firewall/access-proxy-ssh-client-cert"
        if nkey is not None:
            data_payload["nkey"] = nkey
        if name is not None:
            data_payload["name"] = name
        if source_address is not None:
            data_payload["source-address"] = source_address
        if permit_x11_forwarding is not None:
            data_payload["permit-x11-forwarding"] = permit_x11_forwarding
        if permit_agent_forwarding is not None:
            data_payload["permit-agent-forwarding"] = permit_agent_forwarding
        if permit_port_forwarding is not None:
            data_payload["permit-port-forwarding"] = permit_port_forwarding
        if permit_pty is not None:
            data_payload["permit-pty"] = permit_pty
        if permit_user_rc is not None:
            data_payload["permit-user-rc"] = permit_user_rc
        if cert_extension is not None:
            data_payload["cert-extension"] = cert_extension
        if auth_ca is not None:
            data_payload["auth-ca"] = auth_ca
        data_payload.update(kwargs)
        return self._client.post(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )
