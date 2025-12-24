"""
FortiOS CMDB - Cmdb User Fsso Polling

Configuration endpoint for managing cmdb user fsso polling objects.

API Endpoints:
    GET    /cmdb/user/fsso_polling
    POST   /cmdb/user/fsso_polling
    GET    /cmdb/user/fsso_polling
    PUT    /cmdb/user/fsso_polling/{identifier}
    DELETE /cmdb/user/fsso_polling/{identifier}

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.user.fsso_polling.get()
    >>>
    >>> # Get specific item (if supported)
    >>> item = fgt.api.cmdb.user.fsso_polling.get(name="item_name")
    >>>
    >>> # Create new item (use POST)
    >>> result = fgt.api.cmdb.user.fsso_polling.post(
    ...     name="new_item",
    ...     # ... additional parameters
    ... )
    >>>
    >>> # Update existing item (use PUT)
    >>> result = fgt.api.cmdb.user.fsso_polling.put(
    ...     name="existing_item",
    ...     # ... parameters to update
    ... )
    >>>
    >>> # Delete item
    >>> result = fgt.api.cmdb.user.fsso_polling.delete(name="item_name")

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


class FssoPolling:
    """
    Fssopolling Operations.

    Provides CRUD operations for FortiOS fssopolling configuration.

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
        Initialize FssoPolling endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

    def get(
        self,
        id: str | None = None,
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
            id: Object identifier (optional for list, required for specific)
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
        if id:
            endpoint = f"/user/fsso-polling/{id}"
        else:
            endpoint = "/user/fsso-polling"
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
        id: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        before: str | None = None,
        after: str | None = None,
        status: str | None = None,
        server: str | None = None,
        default_domain: str | None = None,
        port: int | None = None,
        user: str | None = None,
        password: str | None = None,
        ldap_server: str | None = None,
        logon_history: int | None = None,
        polling_frequency: int | None = None,
        adgrp: list | None = None,
        smbv1: str | None = None,
        smb_ntlmv1_auth: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update this specific resource.

        Args:
            payload_dict: Optional dictionary of all parameters (can be passed
            as first positional arg)
            id: Object identifier (required)
            before: If *action=move*, use *before* to specify the ID of the
            resource that this resource will be moved before. (optional)
            after: If *action=move*, use *after* to specify the ID of the
            resource that this resource will be moved after. (optional)
            id: Active Directory server ID. (optional)
            status: Enable/disable polling for the status of this Active
            Directory server. (optional)
            server: Host name or IP address of the Active Directory server.
            (optional)
            default_domain: Default domain managed by this Active Directory
            server. (optional)
            port: Port to communicate with this Active Directory server.
            (optional)
            user: User name required to log into this Active Directory server.
            (optional)
            password: Password required to log into this Active Directory
            server. (optional)
            ldap_server: LDAP server name used in LDAP connection strings.
            (optional)
            logon_history: Number of hours of logon history to keep, 0 means
            keep all history. (optional)
            polling_frequency: Polling frequency (every 1 to 30 seconds).
            (optional)
            adgrp: LDAP Group Info. (optional)
            smbv1: Enable/disable support of SMBv1 for Samba. (optional)
            smb_ntlmv1_auth: Enable/disable support of NTLMv1 for Samba
            authentication. (optional)
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
        if not id:
            raise ValueError("id is required for put()")
        endpoint = f"/user/fsso-polling/{id}"
        if before is not None:
            data_payload["before"] = before
        if after is not None:
            data_payload["after"] = after
        if id is not None:
            data_payload["id"] = id
        if status is not None:
            data_payload["status"] = status
        if server is not None:
            data_payload["server"] = server
        if default_domain is not None:
            data_payload["default-domain"] = default_domain
        if port is not None:
            data_payload["port"] = port
        if user is not None:
            data_payload["user"] = user
        if password is not None:
            data_payload["password"] = password
        if ldap_server is not None:
            data_payload["ldap-server"] = ldap_server
        if logon_history is not None:
            data_payload["logon-history"] = logon_history
        if polling_frequency is not None:
            data_payload["polling-frequency"] = polling_frequency
        if adgrp is not None:
            data_payload["adgrp"] = adgrp
        if smbv1 is not None:
            data_payload["smbv1"] = smbv1
        if smb_ntlmv1_auth is not None:
            data_payload["smb-ntlmv1-auth"] = smb_ntlmv1_auth
        data_payload.update(kwargs)
        return self._client.put(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )

    def delete(
        self,
        id: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Delete this specific resource.

        Args:
            id: Object identifier (required)
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
        if not id:
            raise ValueError("id is required for delete()")
        endpoint = f"/user/fsso-polling/{id}"
        params.update(kwargs)
        return self._client.delete(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )

    def exists(
        self,
        id: str,
        vdom: str | bool | None = None,
    ) -> Union[bool, Coroutine[Any, Any, bool]]:
        """
        Check if an object exists.

        Args:
            id: Object identifier
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
        result = self.get(id=id, vdom=vdom)

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
        id: int | None = None,
        status: str | None = None,
        server: str | None = None,
        default_domain: str | None = None,
        port: int | None = None,
        user: str | None = None,
        password: str | None = None,
        ldap_server: str | None = None,
        logon_history: int | None = None,
        polling_frequency: int | None = None,
        adgrp: list | None = None,
        smbv1: str | None = None,
        smb_ntlmv1_auth: str | None = None,
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
            id: Active Directory server ID. (optional)
            status: Enable/disable polling for the status of this Active
            Directory server. (optional)
            server: Host name or IP address of the Active Directory server.
            (optional)
            default_domain: Default domain managed by this Active Directory
            server. (optional)
            port: Port to communicate with this Active Directory server.
            (optional)
            user: User name required to log into this Active Directory server.
            (optional)
            password: Password required to log into this Active Directory
            server. (optional)
            ldap_server: LDAP server name used in LDAP connection strings.
            (optional)
            logon_history: Number of hours of logon history to keep, 0 means
            keep all history. (optional)
            polling_frequency: Polling frequency (every 1 to 30 seconds).
            (optional)
            adgrp: LDAP Group Info. (optional)
            smbv1: Enable/disable support of SMBv1 for Samba. (optional)
            smb_ntlmv1_auth: Enable/disable support of NTLMv1 for Samba
            authentication. (optional)
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
        endpoint = "/user/fsso-polling"
        if nkey is not None:
            data_payload["nkey"] = nkey
        if id is not None:
            data_payload["id"] = id
        if status is not None:
            data_payload["status"] = status
        if server is not None:
            data_payload["server"] = server
        if default_domain is not None:
            data_payload["default-domain"] = default_domain
        if port is not None:
            data_payload["port"] = port
        if user is not None:
            data_payload["user"] = user
        if password is not None:
            data_payload["password"] = password
        if ldap_server is not None:
            data_payload["ldap-server"] = ldap_server
        if logon_history is not None:
            data_payload["logon-history"] = logon_history
        if polling_frequency is not None:
            data_payload["polling-frequency"] = polling_frequency
        if adgrp is not None:
            data_payload["adgrp"] = adgrp
        if smbv1 is not None:
            data_payload["smbv1"] = smbv1
        if smb_ntlmv1_auth is not None:
            data_payload["smb-ntlmv1-auth"] = smb_ntlmv1_auth
        data_payload.update(kwargs)
        return self._client.post(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )
