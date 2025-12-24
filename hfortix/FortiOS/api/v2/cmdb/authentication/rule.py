"""
FortiOS CMDB - Cmdb Authentication Rule

Configuration endpoint for managing cmdb authentication rule objects.

API Endpoints:
    GET    /cmdb/authentication/rule
    POST   /cmdb/authentication/rule
    GET    /cmdb/authentication/rule
    PUT    /cmdb/authentication/rule/{identifier}
    DELETE /cmdb/authentication/rule/{identifier}

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.authentication.rule.get()
    >>>
    >>> # Get specific item (if supported)
    >>> item = fgt.api.cmdb.authentication.rule.get(name="item_name")
    >>>
    >>> # Create new item (use POST)
    >>> result = fgt.api.cmdb.authentication.rule.post(
    ...     name="new_item",
    ...     # ... additional parameters
    ... )
    >>>
    >>> # Update existing item (use PUT)
    >>> result = fgt.api.cmdb.authentication.rule.put(
    ...     name="existing_item",
    ...     # ... parameters to update
    ... )
    >>>
    >>> # Delete item
    >>> result = fgt.api.cmdb.authentication.rule.delete(name="item_name")

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


class Rule:
    """
    Rule Operations.

    Provides CRUD operations for FortiOS rule configuration.

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
        Initialize Rule endpoint.

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
            endpoint = f"/authentication/rule/{name}"
        else:
            endpoint = "/authentication/rule"
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
        status: str | None = None,
        protocol: str | None = None,
        srcintf: list | None = None,
        srcaddr: list | None = None,
        dstaddr: list | None = None,
        srcaddr6: list | None = None,
        dstaddr6: list | None = None,
        ip_based: str | None = None,
        active_auth_method: str | None = None,
        sso_auth_method: str | None = None,
        web_auth_cookie: str | None = None,
        cors_stateful: str | None = None,
        cors_depth: int | None = None,
        cert_auth_cookie: str | None = None,
        transaction_based: str | None = None,
        web_portal: str | None = None,
        comments: str | None = None,
        session_logout: str | None = None,
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
            name: Authentication rule name. (optional)
            status: Enable/disable this authentication rule. (optional)
            protocol: Authentication is required for the selected protocol
            (default = HTTP). (optional)
            srcintf: Incoming (ingress) interface. (optional)
            srcaddr: Authentication is required for the selected IPv4 source
            address. (optional)
            dstaddr: Select an IPv4 destination address from available options.
            Required for web proxy authentication. (optional)
            srcaddr6: Authentication is required for the selected IPv6 source
            address. (optional)
            dstaddr6: Select an IPv6 destination address from available
            options. Required for web proxy authentication. (optional)
            ip_based: Enable/disable IP-based authentication. When enabled,
            previously authenticated users from the same IP address will be
            exempted. (optional)
            active_auth_method: Select an active authentication method.
            (optional)
            sso_auth_method: Select a single-sign on (SSO) authentication
            method. (optional)
            web_auth_cookie: Enable/disable Web authentication cookies (default
            = disable). (optional)
            cors_stateful: Enable/disable allowance of CORS access (default =
            disable). (optional)
            cors_depth: Depth to allow CORS access (default = 3). (optional)
            cert_auth_cookie: Enable/disable to use device certificate as
            authentication cookie (default = enable). (optional)
            transaction_based: Enable/disable transaction based authentication
            (default = disable). (optional)
            web_portal: Enable/disable web portal for proxy transparent policy
            (default = enable). (optional)
            comments: Comment. (optional)
            session_logout: Enable/disable logout of a user from the current
            session. (optional)
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
        endpoint = f"/authentication/rule/{name}"
        if before is not None:
            data_payload["before"] = before
        if after is not None:
            data_payload["after"] = after
        if name is not None:
            data_payload["name"] = name
        if status is not None:
            data_payload["status"] = status
        if protocol is not None:
            data_payload["protocol"] = protocol
        if srcintf is not None:
            data_payload["srcint"] = srcintf
        if srcaddr is not None:
            data_payload["srcaddr"] = srcaddr
        if dstaddr is not None:
            data_payload["dstaddr"] = dstaddr
        if srcaddr6 is not None:
            data_payload["srcaddr6"] = srcaddr6
        if dstaddr6 is not None:
            data_payload["dstaddr6"] = dstaddr6
        if ip_based is not None:
            data_payload["ip-based"] = ip_based
        if active_auth_method is not None:
            data_payload["active-auth-method"] = active_auth_method
        if sso_auth_method is not None:
            data_payload["sso-auth-method"] = sso_auth_method
        if web_auth_cookie is not None:
            data_payload["web-auth-cookie"] = web_auth_cookie
        if cors_stateful is not None:
            data_payload["cors-stateful"] = cors_stateful
        if cors_depth is not None:
            data_payload["cors-depth"] = cors_depth
        if cert_auth_cookie is not None:
            data_payload["cert-auth-cookie"] = cert_auth_cookie
        if transaction_based is not None:
            data_payload["transaction-based"] = transaction_based
        if web_portal is not None:
            data_payload["web-portal"] = web_portal
        if comments is not None:
            data_payload["comments"] = comments
        if session_logout is not None:
            data_payload["session-logout"] = session_logout
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
        endpoint = f"/authentication/rule/{name}"
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
        status: str | None = None,
        protocol: str | None = None,
        srcintf: list | None = None,
        srcaddr: list | None = None,
        dstaddr: list | None = None,
        srcaddr6: list | None = None,
        dstaddr6: list | None = None,
        ip_based: str | None = None,
        active_auth_method: str | None = None,
        sso_auth_method: str | None = None,
        web_auth_cookie: str | None = None,
        cors_stateful: str | None = None,
        cors_depth: int | None = None,
        cert_auth_cookie: str | None = None,
        transaction_based: str | None = None,
        web_portal: str | None = None,
        comments: str | None = None,
        session_logout: str | None = None,
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
            name: Authentication rule name. (optional)
            status: Enable/disable this authentication rule. (optional)
            protocol: Authentication is required for the selected protocol
            (default = HTTP). (optional)
            srcintf: Incoming (ingress) interface. (optional)
            srcaddr: Authentication is required for the selected IPv4 source
            address. (optional)
            dstaddr: Select an IPv4 destination address from available options.
            Required for web proxy authentication. (optional)
            srcaddr6: Authentication is required for the selected IPv6 source
            address. (optional)
            dstaddr6: Select an IPv6 destination address from available
            options. Required for web proxy authentication. (optional)
            ip_based: Enable/disable IP-based authentication. When enabled,
            previously authenticated users from the same IP address will be
            exempted. (optional)
            active_auth_method: Select an active authentication method.
            (optional)
            sso_auth_method: Select a single-sign on (SSO) authentication
            method. (optional)
            web_auth_cookie: Enable/disable Web authentication cookies (default
            = disable). (optional)
            cors_stateful: Enable/disable allowance of CORS access (default =
            disable). (optional)
            cors_depth: Depth to allow CORS access (default = 3). (optional)
            cert_auth_cookie: Enable/disable to use device certificate as
            authentication cookie (default = enable). (optional)
            transaction_based: Enable/disable transaction based authentication
            (default = disable). (optional)
            web_portal: Enable/disable web portal for proxy transparent policy
            (default = enable). (optional)
            comments: Comment. (optional)
            session_logout: Enable/disable logout of a user from the current
            session. (optional)
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
        endpoint = "/authentication/rule"
        if nkey is not None:
            data_payload["nkey"] = nkey
        if name is not None:
            data_payload["name"] = name
        if status is not None:
            data_payload["status"] = status
        if protocol is not None:
            data_payload["protocol"] = protocol
        if srcintf is not None:
            data_payload["srcint"] = srcintf
        if srcaddr is not None:
            data_payload["srcaddr"] = srcaddr
        if dstaddr is not None:
            data_payload["dstaddr"] = dstaddr
        if srcaddr6 is not None:
            data_payload["srcaddr6"] = srcaddr6
        if dstaddr6 is not None:
            data_payload["dstaddr6"] = dstaddr6
        if ip_based is not None:
            data_payload["ip-based"] = ip_based
        if active_auth_method is not None:
            data_payload["active-auth-method"] = active_auth_method
        if sso_auth_method is not None:
            data_payload["sso-auth-method"] = sso_auth_method
        if web_auth_cookie is not None:
            data_payload["web-auth-cookie"] = web_auth_cookie
        if cors_stateful is not None:
            data_payload["cors-stateful"] = cors_stateful
        if cors_depth is not None:
            data_payload["cors-depth"] = cors_depth
        if cert_auth_cookie is not None:
            data_payload["cert-auth-cookie"] = cert_auth_cookie
        if transaction_based is not None:
            data_payload["transaction-based"] = transaction_based
        if web_portal is not None:
            data_payload["web-portal"] = web_portal
        if comments is not None:
            data_payload["comments"] = comments
        if session_logout is not None:
            data_payload["session-logout"] = session_logout
        data_payload.update(kwargs)
        return self._client.post(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )
