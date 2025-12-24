"""
FortiOS CMDB - Cmdb Web Proxy Profile

Configuration endpoint for managing cmdb web proxy profile objects.

API Endpoints:
    GET    /cmdb/web-proxy/profile
    POST   /cmdb/web-proxy/profile
    GET    /cmdb/web-proxy/profile
    PUT    /cmdb/web-proxy/profile/{identifier}
    DELETE /cmdb/web-proxy/profile/{identifier}

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.web_proxy.profile.get()
    >>>
    >>> # Get specific item (if supported)
    >>> item = fgt.api.cmdb.web_proxy.profile.get(name="item_name")
    >>>
    >>> # Create new item (use POST)
    >>> result = fgt.api.cmdb.web_proxy.profile.post(
    ...     name="new_item",
    ...     # ... additional parameters
    ... )
    >>>
    >>> # Update existing item (use PUT)
    >>> result = fgt.api.cmdb.web_proxy.profile.put(
    ...     name="existing_item",
    ...     # ... parameters to update
    ... )
    >>>
    >>> # Delete item
    >>> result = fgt.api.cmdb.web_proxy.profile.delete(name="item_name")

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


class Profile:
    """
    Profile Operations.

    Provides CRUD operations for FortiOS profile configuration.

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
        Initialize Profile endpoint.

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
            endpoint = f"/web-proxy/profile/{name}"
        else:
            endpoint = "/web-proxy/profile"
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
        header_client_ip: str | None = None,
        header_via_request: str | None = None,
        header_via_response: str | None = None,
        header_client_cert: str | None = None,
        header_x_forwarded_for: str | None = None,
        header_x_forwarded_client_cert: str | None = None,
        header_front_end_https: str | None = None,
        header_x_authenticated_user: str | None = None,
        header_x_authenticated_groups: str | None = None,
        strip_encoding: str | None = None,
        log_header_change: str | None = None,
        headers: list | None = None,
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
            header_client_ip: Action to take on the HTTP client-IP header in
            forwarded requests: forwards (pass), adds, or removes the HTTP
            header. (optional)
            header_via_request: Action to take on the HTTP via header in
            forwarded requests: forwards (pass), adds, or removes the HTTP
            header. (optional)
            header_via_response: Action to take on the HTTP via header in
            forwarded responses: forwards (pass), adds, or removes the HTTP
            header. (optional)
            header_client_cert: Action to take on the HTTP
            Client-Cert/Client-Cert-Chain headers in forwarded responses:
            forwards (pass), adds, or removes the HTTP header. (optional)
            header_x_forwarded_for: Action to take on the HTTP x-forwarded-for
            header in forwarded requests: forwards (pass), adds, or removes the
            HTTP header. (optional)
            header_x_forwarded_client_cert: Action to take on the HTTP
            x-forwarded-client-cert header in forwarded requests: forwards
            (pass), adds, or removes the HTTP header. (optional)
            header_front_end_https: Action to take on the HTTP front-end-HTTPS
            header in forwarded requests: forwards (pass), adds, or removes the
            HTTP header. (optional)
            header_x_authenticated_user: Action to take on the HTTP
            x-authenticated-user header in forwarded requests: forwards (pass),
            adds, or removes the HTTP header. (optional)
            header_x_authenticated_groups: Action to take on the HTTP
            x-authenticated-groups header in forwarded requests: forwards
            (pass), adds, or removes the HTTP header. (optional)
            strip_encoding: Enable/disable stripping unsupported encoding from
            the request header. (optional)
            log_header_change: Enable/disable logging HTTP header changes.
            (optional)
            headers: Configure HTTP forwarded requests headers. (optional)
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
        endpoint = f"/web-proxy/profile/{name}"
        if before is not None:
            data_payload["before"] = before
        if after is not None:
            data_payload["after"] = after
        if name is not None:
            data_payload["name"] = name
        if header_client_ip is not None:
            data_payload["header-client-ip"] = header_client_ip
        if header_via_request is not None:
            data_payload["header-via-request"] = header_via_request
        if header_via_response is not None:
            data_payload["header-via-response"] = header_via_response
        if header_client_cert is not None:
            data_payload["header-client-cert"] = header_client_cert
        if header_x_forwarded_for is not None:
            data_payload["header-x-forwarded-for"] = header_x_forwarded_for
        if header_x_forwarded_client_cert is not None:
            data_payload["header-x-forwarded-client-cert"] = (
                header_x_forwarded_client_cert
            )
        if header_front_end_https is not None:
            data_payload["header-front-end-https"] = header_front_end_https
        if header_x_authenticated_user is not None:
            data_payload["header-x-authenticated-user"] = (
                header_x_authenticated_user
            )
        if header_x_authenticated_groups is not None:
            data_payload["header-x-authenticated-groups"] = (
                header_x_authenticated_groups
            )
        if strip_encoding is not None:
            data_payload["strip-encoding"] = strip_encoding
        if log_header_change is not None:
            data_payload["log-header-change"] = log_header_change
        if headers is not None:
            data_payload["headers"] = headers
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
        endpoint = f"/web-proxy/profile/{name}"
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
        header_client_ip: str | None = None,
        header_via_request: str | None = None,
        header_via_response: str | None = None,
        header_client_cert: str | None = None,
        header_x_forwarded_for: str | None = None,
        header_x_forwarded_client_cert: str | None = None,
        header_front_end_https: str | None = None,
        header_x_authenticated_user: str | None = None,
        header_x_authenticated_groups: str | None = None,
        strip_encoding: str | None = None,
        log_header_change: str | None = None,
        headers: list | None = None,
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
            header_client_ip: Action to take on the HTTP client-IP header in
            forwarded requests: forwards (pass), adds, or removes the HTTP
            header. (optional)
            header_via_request: Action to take on the HTTP via header in
            forwarded requests: forwards (pass), adds, or removes the HTTP
            header. (optional)
            header_via_response: Action to take on the HTTP via header in
            forwarded responses: forwards (pass), adds, or removes the HTTP
            header. (optional)
            header_client_cert: Action to take on the HTTP
            Client-Cert/Client-Cert-Chain headers in forwarded responses:
            forwards (pass), adds, or removes the HTTP header. (optional)
            header_x_forwarded_for: Action to take on the HTTP x-forwarded-for
            header in forwarded requests: forwards (pass), adds, or removes the
            HTTP header. (optional)
            header_x_forwarded_client_cert: Action to take on the HTTP
            x-forwarded-client-cert header in forwarded requests: forwards
            (pass), adds, or removes the HTTP header. (optional)
            header_front_end_https: Action to take on the HTTP front-end-HTTPS
            header in forwarded requests: forwards (pass), adds, or removes the
            HTTP header. (optional)
            header_x_authenticated_user: Action to take on the HTTP
            x-authenticated-user header in forwarded requests: forwards (pass),
            adds, or removes the HTTP header. (optional)
            header_x_authenticated_groups: Action to take on the HTTP
            x-authenticated-groups header in forwarded requests: forwards
            (pass), adds, or removes the HTTP header. (optional)
            strip_encoding: Enable/disable stripping unsupported encoding from
            the request header. (optional)
            log_header_change: Enable/disable logging HTTP header changes.
            (optional)
            headers: Configure HTTP forwarded requests headers. (optional)
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
        endpoint = "/web-proxy/profile"
        if nkey is not None:
            data_payload["nkey"] = nkey
        if name is not None:
            data_payload["name"] = name
        if header_client_ip is not None:
            data_payload["header-client-ip"] = header_client_ip
        if header_via_request is not None:
            data_payload["header-via-request"] = header_via_request
        if header_via_response is not None:
            data_payload["header-via-response"] = header_via_response
        if header_client_cert is not None:
            data_payload["header-client-cert"] = header_client_cert
        if header_x_forwarded_for is not None:
            data_payload["header-x-forwarded-for"] = header_x_forwarded_for
        if header_x_forwarded_client_cert is not None:
            data_payload["header-x-forwarded-client-cert"] = (
                header_x_forwarded_client_cert
            )
        if header_front_end_https is not None:
            data_payload["header-front-end-https"] = header_front_end_https
        if header_x_authenticated_user is not None:
            data_payload["header-x-authenticated-user"] = (
                header_x_authenticated_user
            )
        if header_x_authenticated_groups is not None:
            data_payload["header-x-authenticated-groups"] = (
                header_x_authenticated_groups
            )
        if strip_encoding is not None:
            data_payload["strip-encoding"] = strip_encoding
        if log_header_change is not None:
            data_payload["log-header-change"] = log_header_change
        if headers is not None:
            data_payload["headers"] = headers
        data_payload.update(kwargs)
        return self._client.post(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )
