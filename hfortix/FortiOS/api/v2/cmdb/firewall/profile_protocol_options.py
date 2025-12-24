"""
FortiOS CMDB - Cmdb Firewall Profile Protocol Options

Configuration endpoint for managing cmdb firewall profile protocol options
objects.

API Endpoints:
    GET    /cmdb/firewall/profile_protocol_options
    POST   /cmdb/firewall/profile_protocol_options
    GET    /cmdb/firewall/profile_protocol_options
    PUT    /cmdb/firewall/profile_protocol_options/{identifier}
    DELETE /cmdb/firewall/profile_protocol_options/{identifier}

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.firewall.profile_protocol_options.get()
    >>>
    >>> # Get specific item (if supported)
    >>> item =
    fgt.api.cmdb.firewall.profile_protocol_options.get(name="item_name")
    >>>
    >>> # Create new item (use POST)
    >>> result = fgt.api.cmdb.firewall.profile_protocol_options.post(
    ...     name="new_item",
    ...     # ... additional parameters
    ... )
    >>>
    >>> # Update existing item (use PUT)
    >>> result = fgt.api.cmdb.firewall.profile_protocol_options.put(
    ...     name="existing_item",
    ...     # ... parameters to update
    ... )
    >>>
    >>> # Delete item
    >>> result =
    fgt.api.cmdb.firewall.profile_protocol_options.delete(name="item_name")

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


class ProfileProtocolOptions:
    """
    Profileprotocoloptions Operations.

    Provides CRUD operations for FortiOS profileprotocoloptions configuration.

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
        Initialize ProfileProtocolOptions endpoint.

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
            endpoint = f"/firewall/profile-protocol-options/{name}"
        else:
            endpoint = "/firewall/profile-protocol-options"
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
        comment: str | None = None,
        replacemsg_group: str | None = None,
        oversize_log: str | None = None,
        switching_protocols_log: str | None = None,
        http: list | None = None,
        ftp: list | None = None,
        imap: list | None = None,
        mapi: list | None = None,
        pop3: list | None = None,
        smtp: list | None = None,
        nntp: list | None = None,
        ssh: list | None = None,
        dns: list | None = None,
        cifs: list | None = None,
        mail_signature: list | None = None,
        rpc_over_http: str | None = None,
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
            name: Name. (optional)
            comment: Optional comments. (optional)
            replacemsg_group: Name of the replacement message group to be used.
            (optional)
            oversize_log: Enable/disable logging for antivirus oversize file
            blocking. (optional)
            switching_protocols_log: Enable/disable logging for HTTP/HTTPS
            switching protocols. (optional)
            http: Configure HTTP protocol options. (optional)
            ftp: Configure FTP protocol options. (optional)
            imap: Configure IMAP protocol options. (optional)
            mapi: Configure MAPI protocol options. (optional)
            pop3: Configure POP3 protocol options. (optional)
            smtp: Configure SMTP protocol options. (optional)
            nntp: Configure NNTP protocol options. (optional)
            ssh: Configure SFTP and SCP protocol options. (optional)
            dns: Configure DNS protocol options. (optional)
            cifs: Configure CIFS protocol options. (optional)
            mail_signature: Configure Mail signature. (optional)
            rpc_over_http: Enable/disable inspection of RPC over HTTP.
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
        endpoint = f"/firewall/profile-protocol-options/{name}"
        if before is not None:
            data_payload["before"] = before
        if after is not None:
            data_payload["after"] = after
        if name is not None:
            data_payload["name"] = name
        if comment is not None:
            data_payload["comment"] = comment
        if replacemsg_group is not None:
            data_payload["replacemsg-group"] = replacemsg_group
        if oversize_log is not None:
            data_payload["oversize-log"] = oversize_log
        if switching_protocols_log is not None:
            data_payload["switching-protocols-log"] = switching_protocols_log
        if http is not None:
            data_payload["http"] = http
        if ftp is not None:
            data_payload["ftp"] = ftp
        if imap is not None:
            data_payload["imap"] = imap
        if mapi is not None:
            data_payload["mapi"] = mapi
        if pop3 is not None:
            data_payload["pop3"] = pop3
        if smtp is not None:
            data_payload["smtp"] = smtp
        if nntp is not None:
            data_payload["nntp"] = nntp
        if ssh is not None:
            data_payload["ssh"] = ssh
        if dns is not None:
            data_payload["dns"] = dns
        if cifs is not None:
            data_payload["cifs"] = cifs
        if mail_signature is not None:
            data_payload["mail-signature"] = mail_signature
        if rpc_over_http is not None:
            data_payload["rpc-over-http"] = rpc_over_http
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
        endpoint = f"/firewall/profile-protocol-options/{name}"
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
        comment: str | None = None,
        replacemsg_group: str | None = None,
        oversize_log: str | None = None,
        switching_protocols_log: str | None = None,
        http: list | None = None,
        ftp: list | None = None,
        imap: list | None = None,
        mapi: list | None = None,
        pop3: list | None = None,
        smtp: list | None = None,
        nntp: list | None = None,
        ssh: list | None = None,
        dns: list | None = None,
        cifs: list | None = None,
        mail_signature: list | None = None,
        rpc_over_http: str | None = None,
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
            name: Name. (optional)
            comment: Optional comments. (optional)
            replacemsg_group: Name of the replacement message group to be used.
            (optional)
            oversize_log: Enable/disable logging for antivirus oversize file
            blocking. (optional)
            switching_protocols_log: Enable/disable logging for HTTP/HTTPS
            switching protocols. (optional)
            http: Configure HTTP protocol options. (optional)
            ftp: Configure FTP protocol options. (optional)
            imap: Configure IMAP protocol options. (optional)
            mapi: Configure MAPI protocol options. (optional)
            pop3: Configure POP3 protocol options. (optional)
            smtp: Configure SMTP protocol options. (optional)
            nntp: Configure NNTP protocol options. (optional)
            ssh: Configure SFTP and SCP protocol options. (optional)
            dns: Configure DNS protocol options. (optional)
            cifs: Configure CIFS protocol options. (optional)
            mail_signature: Configure Mail signature. (optional)
            rpc_over_http: Enable/disable inspection of RPC over HTTP.
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
        endpoint = "/firewall/profile-protocol-options"
        if nkey is not None:
            data_payload["nkey"] = nkey
        if name is not None:
            data_payload["name"] = name
        if comment is not None:
            data_payload["comment"] = comment
        if replacemsg_group is not None:
            data_payload["replacemsg-group"] = replacemsg_group
        if oversize_log is not None:
            data_payload["oversize-log"] = oversize_log
        if switching_protocols_log is not None:
            data_payload["switching-protocols-log"] = switching_protocols_log
        if http is not None:
            data_payload["http"] = http
        if ftp is not None:
            data_payload["ftp"] = ftp
        if imap is not None:
            data_payload["imap"] = imap
        if mapi is not None:
            data_payload["mapi"] = mapi
        if pop3 is not None:
            data_payload["pop3"] = pop3
        if smtp is not None:
            data_payload["smtp"] = smtp
        if nntp is not None:
            data_payload["nntp"] = nntp
        if ssh is not None:
            data_payload["ssh"] = ssh
        if dns is not None:
            data_payload["dns"] = dns
        if cifs is not None:
            data_payload["cifs"] = cifs
        if mail_signature is not None:
            data_payload["mail-signature"] = mail_signature
        if rpc_over_http is not None:
            data_payload["rpc-over-http"] = rpc_over_http
        data_payload.update(kwargs)
        return self._client.post(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )
