"""
FortiOS CMDB - Cmdb Ztna Web Portal

Configuration endpoint for managing cmdb ztna web portal objects.

API Endpoints:
    GET    /cmdb/ztna/web_portal
    POST   /cmdb/ztna/web_portal
    GET    /cmdb/ztna/web_portal
    PUT    /cmdb/ztna/web_portal/{identifier}
    DELETE /cmdb/ztna/web_portal/{identifier}

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.ztna.web_portal.get()
    >>>
    >>> # Get specific item (if supported)
    >>> item = fgt.api.cmdb.ztna.web_portal.get(name="item_name")
    >>>
    >>> # Create new item (use POST)
    >>> result = fgt.api.cmdb.ztna.web_portal.post(
    ...     name="new_item",
    ...     # ... additional parameters
    ... )
    >>>
    >>> # Update existing item (use PUT)
    >>> result = fgt.api.cmdb.ztna.web_portal.put(
    ...     name="existing_item",
    ...     # ... parameters to update
    ... )
    >>>
    >>> # Delete item
    >>> result = fgt.api.cmdb.ztna.web_portal.delete(name="item_name")

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


class WebPortal:
    """
    Webportal Operations.

    Provides CRUD operations for FortiOS webportal configuration.

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
        Initialize WebPortal endpoint.

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
            endpoint = f"/ztna/web-portal/{name}"
        else:
            endpoint = "/ztna/web-portal"
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
        vip: str | None = None,
        host: str | None = None,
        decrypted_traffic_mirror: str | None = None,
        log_blocked_traffic: str | None = None,
        auth_portal: str | None = None,
        auth_virtual_host: str | None = None,
        vip6: str | None = None,
        auth_rule: str | None = None,
        display_bookmark: str | None = None,
        focus_bookmark: str | None = None,
        display_status: str | None = None,
        display_history: str | None = None,
        policy_auth_sso: str | None = None,
        heading: str | None = None,
        theme: str | None = None,
        clipboard: str | None = None,
        default_window_width: int | None = None,
        default_window_height: int | None = None,
        cookie_age: int | None = None,
        forticlient_download: str | None = None,
        customize_forticlient_download_url: str | None = None,
        windows_forticlient_download_url: str | None = None,
        macos_forticlient_download_url: str | None = None,
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
            name: ZTNA proxy name. (optional)
            vip: Virtual IP name. (optional)
            host: Virtual or real host name. (optional)
            decrypted_traffic_mirror: Decrypted traffic mirror. (optional)
            log_blocked_traffic: Enable/disable logging of blocked traffic.
            (optional)
            auth_portal: Enable/disable authentication portal. (optional)
            auth_virtual_host: Virtual host for authentication portal.
            (optional)
            vip6: Virtual IPv6 name. (optional)
            auth_rule: Authentication Rule. (optional)
            display_bookmark: Enable to display the web portal bookmark widget.
            (optional)
            focus_bookmark: Enable to prioritize the placement of the bookmark
            section over the quick-connection section in the ztna web-portal.
            (optional)
            display_status: Enable to display the web portal status widget.
            (optional)
            display_history: Enable to display the web portal user login
            history widget. (optional)
            policy_auth_sso: Enable policy sso authentication. (optional)
            heading: Web portal heading message. (optional)
            theme: Web portal color scheme. (optional)
            clipboard: Enable to support RDP/VPC clipboard functionality.
            (optional)
            default_window_width: Screen width (range from 0 - 65535, default =
            1024). (optional)
            default_window_height: Screen height (range from 0 - 65535, default
            = 768). (optional)
            cookie_age: Time in minutes that client web browsers should keep a
            cookie. Default is 60 minutes. 0 = no time limit. (optional)
            forticlient_download: Enable/disable download option for
            FortiClient. (optional)
            customize_forticlient_download_url: Enable support of customized
            download URL for FortiClient. (optional)
            windows_forticlient_download_url: Download URL for Windows
            FortiClient. (optional)
            macos_forticlient_download_url: Download URL for Mac FortiClient.
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
        endpoint = f"/ztna/web-portal/{name}"
        if before is not None:
            data_payload["before"] = before
        if after is not None:
            data_payload["after"] = after
        if name is not None:
            data_payload["name"] = name
        if vip is not None:
            data_payload["vip"] = vip
        if host is not None:
            data_payload["host"] = host
        if decrypted_traffic_mirror is not None:
            data_payload["decrypted-traffic-mirror"] = decrypted_traffic_mirror
        if log_blocked_traffic is not None:
            data_payload["log-blocked-traffic"] = log_blocked_traffic
        if auth_portal is not None:
            data_payload["auth-portal"] = auth_portal
        if auth_virtual_host is not None:
            data_payload["auth-virtual-host"] = auth_virtual_host
        if vip6 is not None:
            data_payload["vip6"] = vip6
        if auth_rule is not None:
            data_payload["auth-rule"] = auth_rule
        if display_bookmark is not None:
            data_payload["display-bookmark"] = display_bookmark
        if focus_bookmark is not None:
            data_payload["focus-bookmark"] = focus_bookmark
        if display_status is not None:
            data_payload["display-status"] = display_status
        if display_history is not None:
            data_payload["display-history"] = display_history
        if policy_auth_sso is not None:
            data_payload["policy-auth-sso"] = policy_auth_sso
        if heading is not None:
            data_payload["heading"] = heading
        if theme is not None:
            data_payload["theme"] = theme
        if clipboard is not None:
            data_payload["clipboard"] = clipboard
        if default_window_width is not None:
            data_payload["default-window-width"] = default_window_width
        if default_window_height is not None:
            data_payload["default-window-height"] = default_window_height
        if cookie_age is not None:
            data_payload["cookie-age"] = cookie_age
        if forticlient_download is not None:
            data_payload["forticlient-download"] = forticlient_download
        if customize_forticlient_download_url is not None:
            data_payload["customize-forticlient-download-url"] = (
                customize_forticlient_download_url
            )
        if windows_forticlient_download_url is not None:
            data_payload["windows-forticlient-download-url"] = (
                windows_forticlient_download_url
            )
        if macos_forticlient_download_url is not None:
            data_payload["macos-forticlient-download-url"] = (
                macos_forticlient_download_url
            )
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
        endpoint = f"/ztna/web-portal/{name}"
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
        vip: str | None = None,
        host: str | None = None,
        decrypted_traffic_mirror: str | None = None,
        log_blocked_traffic: str | None = None,
        auth_portal: str | None = None,
        auth_virtual_host: str | None = None,
        vip6: str | None = None,
        auth_rule: str | None = None,
        display_bookmark: str | None = None,
        focus_bookmark: str | None = None,
        display_status: str | None = None,
        display_history: str | None = None,
        policy_auth_sso: str | None = None,
        heading: str | None = None,
        theme: str | None = None,
        clipboard: str | None = None,
        default_window_width: int | None = None,
        default_window_height: int | None = None,
        cookie_age: int | None = None,
        forticlient_download: str | None = None,
        customize_forticlient_download_url: str | None = None,
        windows_forticlient_download_url: str | None = None,
        macos_forticlient_download_url: str | None = None,
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
            name: ZTNA proxy name. (optional)
            vip: Virtual IP name. (optional)
            host: Virtual or real host name. (optional)
            decrypted_traffic_mirror: Decrypted traffic mirror. (optional)
            log_blocked_traffic: Enable/disable logging of blocked traffic.
            (optional)
            auth_portal: Enable/disable authentication portal. (optional)
            auth_virtual_host: Virtual host for authentication portal.
            (optional)
            vip6: Virtual IPv6 name. (optional)
            auth_rule: Authentication Rule. (optional)
            display_bookmark: Enable to display the web portal bookmark widget.
            (optional)
            focus_bookmark: Enable to prioritize the placement of the bookmark
            section over the quick-connection section in the ztna web-portal.
            (optional)
            display_status: Enable to display the web portal status widget.
            (optional)
            display_history: Enable to display the web portal user login
            history widget. (optional)
            policy_auth_sso: Enable policy sso authentication. (optional)
            heading: Web portal heading message. (optional)
            theme: Web portal color scheme. (optional)
            clipboard: Enable to support RDP/VPC clipboard functionality.
            (optional)
            default_window_width: Screen width (range from 0 - 65535, default =
            1024). (optional)
            default_window_height: Screen height (range from 0 - 65535, default
            = 768). (optional)
            cookie_age: Time in minutes that client web browsers should keep a
            cookie. Default is 60 minutes. 0 = no time limit. (optional)
            forticlient_download: Enable/disable download option for
            FortiClient. (optional)
            customize_forticlient_download_url: Enable support of customized
            download URL for FortiClient. (optional)
            windows_forticlient_download_url: Download URL for Windows
            FortiClient. (optional)
            macos_forticlient_download_url: Download URL for Mac FortiClient.
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
        endpoint = "/ztna/web-portal"
        if nkey is not None:
            data_payload["nkey"] = nkey
        if name is not None:
            data_payload["name"] = name
        if vip is not None:
            data_payload["vip"] = vip
        if host is not None:
            data_payload["host"] = host
        if decrypted_traffic_mirror is not None:
            data_payload["decrypted-traffic-mirror"] = decrypted_traffic_mirror
        if log_blocked_traffic is not None:
            data_payload["log-blocked-traffic"] = log_blocked_traffic
        if auth_portal is not None:
            data_payload["auth-portal"] = auth_portal
        if auth_virtual_host is not None:
            data_payload["auth-virtual-host"] = auth_virtual_host
        if vip6 is not None:
            data_payload["vip6"] = vip6
        if auth_rule is not None:
            data_payload["auth-rule"] = auth_rule
        if display_bookmark is not None:
            data_payload["display-bookmark"] = display_bookmark
        if focus_bookmark is not None:
            data_payload["focus-bookmark"] = focus_bookmark
        if display_status is not None:
            data_payload["display-status"] = display_status
        if display_history is not None:
            data_payload["display-history"] = display_history
        if policy_auth_sso is not None:
            data_payload["policy-auth-sso"] = policy_auth_sso
        if heading is not None:
            data_payload["heading"] = heading
        if theme is not None:
            data_payload["theme"] = theme
        if clipboard is not None:
            data_payload["clipboard"] = clipboard
        if default_window_width is not None:
            data_payload["default-window-width"] = default_window_width
        if default_window_height is not None:
            data_payload["default-window-height"] = default_window_height
        if cookie_age is not None:
            data_payload["cookie-age"] = cookie_age
        if forticlient_download is not None:
            data_payload["forticlient-download"] = forticlient_download
        if customize_forticlient_download_url is not None:
            data_payload["customize-forticlient-download-url"] = (
                customize_forticlient_download_url
            )
        if windows_forticlient_download_url is not None:
            data_payload["windows-forticlient-download-url"] = (
                windows_forticlient_download_url
            )
        if macos_forticlient_download_url is not None:
            data_payload["macos-forticlient-download-url"] = (
                macos_forticlient_download_url
            )
        data_payload.update(kwargs)
        return self._client.post(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )
