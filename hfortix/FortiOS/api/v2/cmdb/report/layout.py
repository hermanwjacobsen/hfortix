"""
FortiOS CMDB - Cmdb Report Layout

Configuration endpoint for managing cmdb report layout objects.

API Endpoints:
    GET    /cmdb/report/layout
    POST   /cmdb/report/layout
    GET    /cmdb/report/layout
    PUT    /cmdb/report/layout/{identifier}
    DELETE /cmdb/report/layout/{identifier}

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.report.layout.get()
    >>>
    >>> # Get specific item (if supported)
    >>> item = fgt.api.cmdb.report.layout.get(name="item_name")
    >>>
    >>> # Create new item (use POST)
    >>> result = fgt.api.cmdb.report.layout.post(
    ...     name="new_item",
    ...     # ... additional parameters
    ... )
    >>>
    >>> # Update existing item (use PUT)
    >>> result = fgt.api.cmdb.report.layout.put(
    ...     name="existing_item",
    ...     # ... parameters to update
    ... )
    >>>
    >>> # Delete item
    >>> result = fgt.api.cmdb.report.layout.delete(name="item_name")

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


class Layout:
    """
    Layout Operations.

    Provides CRUD operations for FortiOS layout configuration.

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
        Initialize Layout endpoint.

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
            endpoint = f"/report/layout/{name}"
        else:
            endpoint = "/report/layout"
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
        title: str | None = None,
        subtitle: str | None = None,
        description: str | None = None,
        style_theme: str | None = None,
        options: str | None = None,
        schedule_type: str | None = None,
        day: str | None = None,
        time: str | None = None,
        cutoff_option: str | None = None,
        cutoff_time: str | None = None,
        email_send: str | None = None,
        email_recipients: str | None = None,
        max_pdf_report: int | None = None,
        page: list | None = None,
        body_item: list | None = None,
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
            name: Report layout name. (optional)
            title: Report title. (optional)
            subtitle: Report subtitle. (optional)
            description: Description. (optional)
            style_theme: Report style theme. (optional)
            options: Report layout options. (optional)
            schedule_type: Report schedule type. (optional)
            day: Schedule days of week to generate report. (optional)
            time: Schedule time to generate report (format = hh:mm). (optional)
            cutoff_option: Cutoff-option is either run-time or custom.
            (optional)
            cutoff_time: Custom cutoff time to generate report (format =
            hh:mm). (optional)
            email_send: Enable/disable sending emails after reports are
            generated. (optional)
            email_recipients: Email recipients for generated reports.
            (optional)
            max_pdf_report: Maximum number of PDF reports to keep at one time
            (oldest report is overwritten). (optional)
            page: Configure report page. (optional)
            body_item: Configure report body item. (optional)
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
        endpoint = f"/report/layout/{name}"
        if before is not None:
            data_payload["before"] = before
        if after is not None:
            data_payload["after"] = after
        if name is not None:
            data_payload["name"] = name
        if title is not None:
            data_payload["title"] = title
        if subtitle is not None:
            data_payload["subtitle"] = subtitle
        if description is not None:
            data_payload["description"] = description
        if style_theme is not None:
            data_payload["style-theme"] = style_theme
        if options is not None:
            data_payload["options"] = options
        if schedule_type is not None:
            data_payload["schedule-type"] = schedule_type
        if day is not None:
            data_payload["day"] = day
        if time is not None:
            data_payload["time"] = time
        if cutoff_option is not None:
            data_payload["cutoff-option"] = cutoff_option
        if cutoff_time is not None:
            data_payload["cutoff-time"] = cutoff_time
        if email_send is not None:
            data_payload["email-send"] = email_send
        if email_recipients is not None:
            data_payload["email-recipients"] = email_recipients
        if max_pdf_report is not None:
            data_payload["max-pdf-report"] = max_pdf_report
        if page is not None:
            data_payload["page"] = page
        if body_item is not None:
            data_payload["body-item"] = body_item
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
        endpoint = f"/report/layout/{name}"
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
        title: str | None = None,
        subtitle: str | None = None,
        description: str | None = None,
        style_theme: str | None = None,
        options: str | None = None,
        schedule_type: str | None = None,
        day: str | None = None,
        time: str | None = None,
        cutoff_option: str | None = None,
        cutoff_time: str | None = None,
        email_send: str | None = None,
        email_recipients: str | None = None,
        max_pdf_report: int | None = None,
        page: list | None = None,
        body_item: list | None = None,
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
            name: Report layout name. (optional)
            title: Report title. (optional)
            subtitle: Report subtitle. (optional)
            description: Description. (optional)
            style_theme: Report style theme. (optional)
            options: Report layout options. (optional)
            schedule_type: Report schedule type. (optional)
            day: Schedule days of week to generate report. (optional)
            time: Schedule time to generate report (format = hh:mm). (optional)
            cutoff_option: Cutoff-option is either run-time or custom.
            (optional)
            cutoff_time: Custom cutoff time to generate report (format =
            hh:mm). (optional)
            email_send: Enable/disable sending emails after reports are
            generated. (optional)
            email_recipients: Email recipients for generated reports.
            (optional)
            max_pdf_report: Maximum number of PDF reports to keep at one time
            (oldest report is overwritten). (optional)
            page: Configure report page. (optional)
            body_item: Configure report body item. (optional)
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
        endpoint = "/report/layout"
        if nkey is not None:
            data_payload["nkey"] = nkey
        if name is not None:
            data_payload["name"] = name
        if title is not None:
            data_payload["title"] = title
        if subtitle is not None:
            data_payload["subtitle"] = subtitle
        if description is not None:
            data_payload["description"] = description
        if style_theme is not None:
            data_payload["style-theme"] = style_theme
        if options is not None:
            data_payload["options"] = options
        if schedule_type is not None:
            data_payload["schedule-type"] = schedule_type
        if day is not None:
            data_payload["day"] = day
        if time is not None:
            data_payload["time"] = time
        if cutoff_option is not None:
            data_payload["cutoff-option"] = cutoff_option
        if cutoff_time is not None:
            data_payload["cutoff-time"] = cutoff_time
        if email_send is not None:
            data_payload["email-send"] = email_send
        if email_recipients is not None:
            data_payload["email-recipients"] = email_recipients
        if max_pdf_report is not None:
            data_payload["max-pdf-report"] = max_pdf_report
        if page is not None:
            data_payload["page"] = page
        if body_item is not None:
            data_payload["body-item"] = body_item
        data_payload.update(kwargs)
        return self._client.post(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )
