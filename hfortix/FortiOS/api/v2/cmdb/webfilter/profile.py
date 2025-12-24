"""
FortiOS CMDB - Cmdb Webfilter Profile

Configuration endpoint for managing cmdb webfilter profile objects.

API Endpoints:
    GET    /cmdb/webfilter/profile
    POST   /cmdb/webfilter/profile
    GET    /cmdb/webfilter/profile
    PUT    /cmdb/webfilter/profile/{identifier}
    DELETE /cmdb/webfilter/profile/{identifier}

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.webfilter.profile.get()
    >>>
    >>> # Get specific item (if supported)
    >>> item = fgt.api.cmdb.webfilter.profile.get(name="item_name")
    >>>
    >>> # Create new item (use POST)
    >>> result = fgt.api.cmdb.webfilter.profile.post(
    ...     name="new_item",
    ...     # ... additional parameters
    ... )
    >>>
    >>> # Update existing item (use PUT)
    >>> result = fgt.api.cmdb.webfilter.profile.put(
    ...     name="existing_item",
    ...     # ... parameters to update
    ... )
    >>>
    >>> # Delete item
    >>> result = fgt.api.cmdb.webfilter.profile.delete(name="item_name")

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
            endpoint = f"/webfilter/profile/{name}"
        else:
            endpoint = "/webfilter/profile"
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
        feature_set: str | None = None,
        replacemsg_group: str | None = None,
        options: str | None = None,
        https_replacemsg: str | None = None,
        web_flow_log_encoding: str | None = None,
        ovrd_perm: str | None = None,
        post_action: str | None = None,
        override: list | None = None,
        web: list | None = None,
        ftgd_wf: list | None = None,
        antiphish: list | None = None,
        wisp: str | None = None,
        wisp_servers: list | None = None,
        wisp_algorithm: str | None = None,
        log_all_url: str | None = None,
        web_content_log: str | None = None,
        web_filter_activex_log: str | None = None,
        web_filter_command_block_log: str | None = None,
        web_filter_cookie_log: str | None = None,
        web_filter_applet_log: str | None = None,
        web_filter_jscript_log: str | None = None,
        web_filter_js_log: str | None = None,
        web_filter_vbs_log: str | None = None,
        web_filter_unknown_log: str | None = None,
        web_filter_referer_log: str | None = None,
        web_filter_cookie_removal_log: str | None = None,
        web_url_log: str | None = None,
        web_invalid_domain_log: str | None = None,
        web_ftgd_err_log: str | None = None,
        web_ftgd_quota_usage: str | None = None,
        extended_log: str | None = None,
        web_extended_all_action_log: str | None = None,
        web_antiphishing_log: str | None = None,
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
            comment: Optional comments. (optional)
            feature_set: Flow/proxy feature set. (optional)
            replacemsg_group: Replacement message group. (optional)
            options: Options. (optional)
            https_replacemsg: Enable replacement messages for HTTPS. (optional)
            web_flow_log_encoding: Log encoding in flow mode. (optional)
            ovrd_perm: Permitted override types. (optional)
            post_action: Action taken for HTTP POST traffic. (optional)
            override: Web Filter override settings. (optional)
            web: Web content filtering settings. (optional)
            ftgd_wf: FortiGuard Web Filter settings. (optional)
            antiphish: AntiPhishing profile. (optional)
            wisp: Enable/disable web proxy WISP. (optional)
            wisp_servers: WISP servers. (optional)
            wisp_algorithm: WISP server selection algorithm. (optional)
            log_all_url: Enable/disable logging all URLs visited. (optional)
            web_content_log: Enable/disable logging logging blocked web
            content. (optional)
            web_filter_activex_log: Enable/disable logging ActiveX. (optional)
            web_filter_command_block_log: Enable/disable logging blocked
            commands. (optional)
            web_filter_cookie_log: Enable/disable logging cookie filtering.
            (optional)
            web_filter_applet_log: Enable/disable logging Java applets.
            (optional)
            web_filter_jscript_log: Enable/disable logging JScripts. (optional)
            web_filter_js_log: Enable/disable logging Java scripts. (optional)
            web_filter_vbs_log: Enable/disable logging VBS scripts. (optional)
            web_filter_unknown_log: Enable/disable logging unknown scripts.
            (optional)
            web_filter_referer_log: Enable/disable logging referrers.
            (optional)
            web_filter_cookie_removal_log: Enable/disable logging blocked
            cookies. (optional)
            web_url_log: Enable/disable logging URL filtering. (optional)
            web_invalid_domain_log: Enable/disable logging invalid domain
            names. (optional)
            web_ftgd_err_log: Enable/disable logging rating errors. (optional)
            web_ftgd_quota_usage: Enable/disable logging daily quota usage.
            (optional)
            extended_log: Enable/disable extended logging for web filtering.
            (optional)
            web_extended_all_action_log: Enable/disable extended any filter
            action logging for web filtering. (optional)
            web_antiphishing_log: Enable/disable logging of AntiPhishing
            checks. (optional)
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
        endpoint = f"/webfilter/profile/{name}"
        if before is not None:
            data_payload["before"] = before
        if after is not None:
            data_payload["after"] = after
        if name is not None:
            data_payload["name"] = name
        if comment is not None:
            data_payload["comment"] = comment
        if feature_set is not None:
            data_payload["feature-set"] = feature_set
        if replacemsg_group is not None:
            data_payload["replacemsg-group"] = replacemsg_group
        if options is not None:
            data_payload["options"] = options
        if https_replacemsg is not None:
            data_payload["https-replacemsg"] = https_replacemsg
        if web_flow_log_encoding is not None:
            data_payload["web-flow-log-encoding"] = web_flow_log_encoding
        if ovrd_perm is not None:
            data_payload["ovrd-perm"] = ovrd_perm
        if post_action is not None:
            data_payload["post-action"] = post_action
        if override is not None:
            data_payload["override"] = override
        if web is not None:
            data_payload["web"] = web
        if ftgd_wf is not None:
            data_payload["ftgd-w"] = ftgd_wf
        if antiphish is not None:
            data_payload["antiphish"] = antiphish
        if wisp is not None:
            data_payload["wisp"] = wisp
        if wisp_servers is not None:
            data_payload["wisp-servers"] = wisp_servers
        if wisp_algorithm is not None:
            data_payload["wisp-algorithm"] = wisp_algorithm
        if log_all_url is not None:
            data_payload["log-all-url"] = log_all_url
        if web_content_log is not None:
            data_payload["web-content-log"] = web_content_log
        if web_filter_activex_log is not None:
            data_payload["web-filter-activex-log"] = web_filter_activex_log
        if web_filter_command_block_log is not None:
            data_payload["web-filter-command-block-log"] = (
                web_filter_command_block_log
            )
        if web_filter_cookie_log is not None:
            data_payload["web-filter-cookie-log"] = web_filter_cookie_log
        if web_filter_applet_log is not None:
            data_payload["web-filter-applet-log"] = web_filter_applet_log
        if web_filter_jscript_log is not None:
            data_payload["web-filter-jscript-log"] = web_filter_jscript_log
        if web_filter_js_log is not None:
            data_payload["web-filter-js-log"] = web_filter_js_log
        if web_filter_vbs_log is not None:
            data_payload["web-filter-vbs-log"] = web_filter_vbs_log
        if web_filter_unknown_log is not None:
            data_payload["web-filter-unknown-log"] = web_filter_unknown_log
        if web_filter_referer_log is not None:
            data_payload["web-filter-referer-log"] = web_filter_referer_log
        if web_filter_cookie_removal_log is not None:
            data_payload["web-filter-cookie-removal-log"] = (
                web_filter_cookie_removal_log
            )
        if web_url_log is not None:
            data_payload["web-url-log"] = web_url_log
        if web_invalid_domain_log is not None:
            data_payload["web-invalid-domain-log"] = web_invalid_domain_log
        if web_ftgd_err_log is not None:
            data_payload["web-ftgd-err-log"] = web_ftgd_err_log
        if web_ftgd_quota_usage is not None:
            data_payload["web-ftgd-quota-usage"] = web_ftgd_quota_usage
        if extended_log is not None:
            data_payload["extended-log"] = extended_log
        if web_extended_all_action_log is not None:
            data_payload["web-extended-all-action-log"] = (
                web_extended_all_action_log
            )
        if web_antiphishing_log is not None:
            data_payload["web-antiphishing-log"] = web_antiphishing_log
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
        endpoint = f"/webfilter/profile/{name}"
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
        feature_set: str | None = None,
        replacemsg_group: str | None = None,
        options: str | None = None,
        https_replacemsg: str | None = None,
        web_flow_log_encoding: str | None = None,
        ovrd_perm: str | None = None,
        post_action: str | None = None,
        override: list | None = None,
        web: list | None = None,
        ftgd_wf: list | None = None,
        antiphish: list | None = None,
        wisp: str | None = None,
        wisp_servers: list | None = None,
        wisp_algorithm: str | None = None,
        log_all_url: str | None = None,
        web_content_log: str | None = None,
        web_filter_activex_log: str | None = None,
        web_filter_command_block_log: str | None = None,
        web_filter_cookie_log: str | None = None,
        web_filter_applet_log: str | None = None,
        web_filter_jscript_log: str | None = None,
        web_filter_js_log: str | None = None,
        web_filter_vbs_log: str | None = None,
        web_filter_unknown_log: str | None = None,
        web_filter_referer_log: str | None = None,
        web_filter_cookie_removal_log: str | None = None,
        web_url_log: str | None = None,
        web_invalid_domain_log: str | None = None,
        web_ftgd_err_log: str | None = None,
        web_ftgd_quota_usage: str | None = None,
        extended_log: str | None = None,
        web_extended_all_action_log: str | None = None,
        web_antiphishing_log: str | None = None,
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
            comment: Optional comments. (optional)
            feature_set: Flow/proxy feature set. (optional)
            replacemsg_group: Replacement message group. (optional)
            options: Options. (optional)
            https_replacemsg: Enable replacement messages for HTTPS. (optional)
            web_flow_log_encoding: Log encoding in flow mode. (optional)
            ovrd_perm: Permitted override types. (optional)
            post_action: Action taken for HTTP POST traffic. (optional)
            override: Web Filter override settings. (optional)
            web: Web content filtering settings. (optional)
            ftgd_wf: FortiGuard Web Filter settings. (optional)
            antiphish: AntiPhishing profile. (optional)
            wisp: Enable/disable web proxy WISP. (optional)
            wisp_servers: WISP servers. (optional)
            wisp_algorithm: WISP server selection algorithm. (optional)
            log_all_url: Enable/disable logging all URLs visited. (optional)
            web_content_log: Enable/disable logging logging blocked web
            content. (optional)
            web_filter_activex_log: Enable/disable logging ActiveX. (optional)
            web_filter_command_block_log: Enable/disable logging blocked
            commands. (optional)
            web_filter_cookie_log: Enable/disable logging cookie filtering.
            (optional)
            web_filter_applet_log: Enable/disable logging Java applets.
            (optional)
            web_filter_jscript_log: Enable/disable logging JScripts. (optional)
            web_filter_js_log: Enable/disable logging Java scripts. (optional)
            web_filter_vbs_log: Enable/disable logging VBS scripts. (optional)
            web_filter_unknown_log: Enable/disable logging unknown scripts.
            (optional)
            web_filter_referer_log: Enable/disable logging referrers.
            (optional)
            web_filter_cookie_removal_log: Enable/disable logging blocked
            cookies. (optional)
            web_url_log: Enable/disable logging URL filtering. (optional)
            web_invalid_domain_log: Enable/disable logging invalid domain
            names. (optional)
            web_ftgd_err_log: Enable/disable logging rating errors. (optional)
            web_ftgd_quota_usage: Enable/disable logging daily quota usage.
            (optional)
            extended_log: Enable/disable extended logging for web filtering.
            (optional)
            web_extended_all_action_log: Enable/disable extended any filter
            action logging for web filtering. (optional)
            web_antiphishing_log: Enable/disable logging of AntiPhishing
            checks. (optional)
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
        endpoint = "/webfilter/profile"
        if nkey is not None:
            data_payload["nkey"] = nkey
        if name is not None:
            data_payload["name"] = name
        if comment is not None:
            data_payload["comment"] = comment
        if feature_set is not None:
            data_payload["feature-set"] = feature_set
        if replacemsg_group is not None:
            data_payload["replacemsg-group"] = replacemsg_group
        if options is not None:
            data_payload["options"] = options
        if https_replacemsg is not None:
            data_payload["https-replacemsg"] = https_replacemsg
        if web_flow_log_encoding is not None:
            data_payload["web-flow-log-encoding"] = web_flow_log_encoding
        if ovrd_perm is not None:
            data_payload["ovrd-perm"] = ovrd_perm
        if post_action is not None:
            data_payload["post-action"] = post_action
        if override is not None:
            data_payload["override"] = override
        if web is not None:
            data_payload["web"] = web
        if ftgd_wf is not None:
            data_payload["ftgd-w"] = ftgd_wf
        if antiphish is not None:
            data_payload["antiphish"] = antiphish
        if wisp is not None:
            data_payload["wisp"] = wisp
        if wisp_servers is not None:
            data_payload["wisp-servers"] = wisp_servers
        if wisp_algorithm is not None:
            data_payload["wisp-algorithm"] = wisp_algorithm
        if log_all_url is not None:
            data_payload["log-all-url"] = log_all_url
        if web_content_log is not None:
            data_payload["web-content-log"] = web_content_log
        if web_filter_activex_log is not None:
            data_payload["web-filter-activex-log"] = web_filter_activex_log
        if web_filter_command_block_log is not None:
            data_payload["web-filter-command-block-log"] = (
                web_filter_command_block_log
            )
        if web_filter_cookie_log is not None:
            data_payload["web-filter-cookie-log"] = web_filter_cookie_log
        if web_filter_applet_log is not None:
            data_payload["web-filter-applet-log"] = web_filter_applet_log
        if web_filter_jscript_log is not None:
            data_payload["web-filter-jscript-log"] = web_filter_jscript_log
        if web_filter_js_log is not None:
            data_payload["web-filter-js-log"] = web_filter_js_log
        if web_filter_vbs_log is not None:
            data_payload["web-filter-vbs-log"] = web_filter_vbs_log
        if web_filter_unknown_log is not None:
            data_payload["web-filter-unknown-log"] = web_filter_unknown_log
        if web_filter_referer_log is not None:
            data_payload["web-filter-referer-log"] = web_filter_referer_log
        if web_filter_cookie_removal_log is not None:
            data_payload["web-filter-cookie-removal-log"] = (
                web_filter_cookie_removal_log
            )
        if web_url_log is not None:
            data_payload["web-url-log"] = web_url_log
        if web_invalid_domain_log is not None:
            data_payload["web-invalid-domain-log"] = web_invalid_domain_log
        if web_ftgd_err_log is not None:
            data_payload["web-ftgd-err-log"] = web_ftgd_err_log
        if web_ftgd_quota_usage is not None:
            data_payload["web-ftgd-quota-usage"] = web_ftgd_quota_usage
        if extended_log is not None:
            data_payload["extended-log"] = extended_log
        if web_extended_all_action_log is not None:
            data_payload["web-extended-all-action-log"] = (
                web_extended_all_action_log
            )
        if web_antiphishing_log is not None:
            data_payload["web-antiphishing-log"] = web_antiphishing_log
        data_payload.update(kwargs)
        return self._client.post(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )
