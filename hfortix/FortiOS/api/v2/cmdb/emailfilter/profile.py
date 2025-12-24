"""
FortiOS CMDB - Cmdb Emailfilter Profile

Configuration endpoint for managing cmdb emailfilter profile objects.

API Endpoints:
    GET    /cmdb/emailfilter/profile
    POST   /cmdb/emailfilter/profile
    GET    /cmdb/emailfilter/profile
    PUT    /cmdb/emailfilter/profile/{identifier}
    DELETE /cmdb/emailfilter/profile/{identifier}

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.emailfilter.profile.get()
    >>>
    >>> # Get specific item (if supported)
    >>> item = fgt.api.cmdb.emailfilter.profile.get(name="item_name")
    >>>
    >>> # Create new item (use POST)
    >>> result = fgt.api.cmdb.emailfilter.profile.post(
    ...     name="new_item",
    ...     # ... additional parameters
    ... )
    >>>
    >>> # Update existing item (use PUT)
    >>> result = fgt.api.cmdb.emailfilter.profile.put(
    ...     name="existing_item",
    ...     # ... parameters to update
    ... )
    >>>
    >>> # Delete item
    >>> result = fgt.api.cmdb.emailfilter.profile.delete(name="item_name")

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
            endpoint = f"/emailfilter/profile/{name}"
        else:
            endpoint = "/emailfilter/profile"
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
        spam_log: str | None = None,
        spam_log_fortiguard_response: str | None = None,
        spam_filtering: str | None = None,
        external: str | None = None,
        options: str | None = None,
        imap: list | None = None,
        pop3: list | None = None,
        smtp: list | None = None,
        other_webmails: list | None = None,
        spam_bword_threshold: int | None = None,
        spam_bword_table: int | None = None,
        spam_bal_table: int | None = None,
        spam_mheader_table: int | None = None,
        spam_rbl_table: int | None = None,
        spam_iptrust_table: int | None = None,
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
            comment: Comment. (optional)
            feature_set: Flow/proxy feature set. (optional)
            replacemsg_group: Replacement message group. (optional)
            spam_log: Enable/disable spam logging for email filtering.
            (optional)
            spam_log_fortiguard_response: Enable/disable logging FortiGuard
            spam response. (optional)
            spam_filtering: Enable/disable spam filtering. (optional)
            external: Enable/disable external Email inspection. (optional)
            options: Options. (optional)
            imap: IMAP. (optional)
            pop3: POP3. (optional)
            smtp: SMTP. (optional)
            other_webmails: Other supported webmails. (optional)
            spam_bword_threshold: Spam banned word threshold. (optional)
            spam_bword_table: Anti-spam banned word table ID. (optional)
            spam_bal_table: Anti-spam block/allow list table ID. (optional)
            spam_mheader_table: Anti-spam MIME header table ID. (optional)
            spam_rbl_table: Anti-spam DNSBL table ID. (optional)
            spam_iptrust_table: Anti-spam IP trust table ID. (optional)
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
        endpoint = f"/emailfilter/profile/{name}"
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
        if spam_log is not None:
            data_payload["spam-log"] = spam_log
        if spam_log_fortiguard_response is not None:
            data_payload["spam-log-fortiguard-response"] = (
                spam_log_fortiguard_response
            )
        if spam_filtering is not None:
            data_payload["spam-filtering"] = spam_filtering
        if external is not None:
            data_payload["external"] = external
        if options is not None:
            data_payload["options"] = options
        if imap is not None:
            data_payload["imap"] = imap
        if pop3 is not None:
            data_payload["pop3"] = pop3
        if smtp is not None:
            data_payload["smtp"] = smtp
        if other_webmails is not None:
            data_payload["other-webmails"] = other_webmails
        if spam_bword_threshold is not None:
            data_payload["spam-bword-threshold"] = spam_bword_threshold
        if spam_bword_table is not None:
            data_payload["spam-bword-table"] = spam_bword_table
        if spam_bal_table is not None:
            data_payload["spam-bal-table"] = spam_bal_table
        if spam_mheader_table is not None:
            data_payload["spam-mheader-table"] = spam_mheader_table
        if spam_rbl_table is not None:
            data_payload["spam-rbl-table"] = spam_rbl_table
        if spam_iptrust_table is not None:
            data_payload["spam-iptrust-table"] = spam_iptrust_table
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
        endpoint = f"/emailfilter/profile/{name}"
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
        spam_log: str | None = None,
        spam_log_fortiguard_response: str | None = None,
        spam_filtering: str | None = None,
        external: str | None = None,
        options: str | None = None,
        imap: list | None = None,
        pop3: list | None = None,
        smtp: list | None = None,
        other_webmails: list | None = None,
        spam_bword_threshold: int | None = None,
        spam_bword_table: int | None = None,
        spam_bal_table: int | None = None,
        spam_mheader_table: int | None = None,
        spam_rbl_table: int | None = None,
        spam_iptrust_table: int | None = None,
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
            comment: Comment. (optional)
            feature_set: Flow/proxy feature set. (optional)
            replacemsg_group: Replacement message group. (optional)
            spam_log: Enable/disable spam logging for email filtering.
            (optional)
            spam_log_fortiguard_response: Enable/disable logging FortiGuard
            spam response. (optional)
            spam_filtering: Enable/disable spam filtering. (optional)
            external: Enable/disable external Email inspection. (optional)
            options: Options. (optional)
            imap: IMAP. (optional)
            pop3: POP3. (optional)
            smtp: SMTP. (optional)
            other_webmails: Other supported webmails. (optional)
            spam_bword_threshold: Spam banned word threshold. (optional)
            spam_bword_table: Anti-spam banned word table ID. (optional)
            spam_bal_table: Anti-spam block/allow list table ID. (optional)
            spam_mheader_table: Anti-spam MIME header table ID. (optional)
            spam_rbl_table: Anti-spam DNSBL table ID. (optional)
            spam_iptrust_table: Anti-spam IP trust table ID. (optional)
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
        endpoint = "/emailfilter/profile"
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
        if spam_log is not None:
            data_payload["spam-log"] = spam_log
        if spam_log_fortiguard_response is not None:
            data_payload["spam-log-fortiguard-response"] = (
                spam_log_fortiguard_response
            )
        if spam_filtering is not None:
            data_payload["spam-filtering"] = spam_filtering
        if external is not None:
            data_payload["external"] = external
        if options is not None:
            data_payload["options"] = options
        if imap is not None:
            data_payload["imap"] = imap
        if pop3 is not None:
            data_payload["pop3"] = pop3
        if smtp is not None:
            data_payload["smtp"] = smtp
        if other_webmails is not None:
            data_payload["other-webmails"] = other_webmails
        if spam_bword_threshold is not None:
            data_payload["spam-bword-threshold"] = spam_bword_threshold
        if spam_bword_table is not None:
            data_payload["spam-bword-table"] = spam_bword_table
        if spam_bal_table is not None:
            data_payload["spam-bal-table"] = spam_bal_table
        if spam_mheader_table is not None:
            data_payload["spam-mheader-table"] = spam_mheader_table
        if spam_rbl_table is not None:
            data_payload["spam-rbl-table"] = spam_rbl_table
        if spam_iptrust_table is not None:
            data_payload["spam-iptrust-table"] = spam_iptrust_table
        data_payload.update(kwargs)
        return self._client.post(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )
