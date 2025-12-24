"""
FortiOS CMDB - Cmdb System Automation Trigger

Configuration endpoint for managing cmdb system automation trigger objects.

API Endpoints:
    GET    /cmdb/system/automation_trigger
    POST   /cmdb/system/automation_trigger
    GET    /cmdb/system/automation_trigger
    PUT    /cmdb/system/automation_trigger/{identifier}
    DELETE /cmdb/system/automation_trigger/{identifier}

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.system.automation_trigger.get()
    >>>
    >>> # Get specific item (if supported)
    >>> item = fgt.api.cmdb.system.automation_trigger.get(name="item_name")
    >>>
    >>> # Create new item (use POST)
    >>> result = fgt.api.cmdb.system.automation_trigger.post(
    ...     name="new_item",
    ...     # ... additional parameters
    ... )
    >>>
    >>> # Update existing item (use PUT)
    >>> result = fgt.api.cmdb.system.automation_trigger.put(
    ...     name="existing_item",
    ...     # ... parameters to update
    ... )
    >>>
    >>> # Delete item
    >>> result =
    fgt.api.cmdb.system.automation_trigger.delete(name="item_name")

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


class AutomationTrigger:
    """
    Automationtrigger Operations.

    Provides CRUD operations for FortiOS automationtrigger configuration.

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
        Initialize AutomationTrigger endpoint.

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
            endpoint = f"/system/automation-trigger/{name}"
        else:
            endpoint = "/system/automation-trigger"
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
        description: str | None = None,
        trigger_type: str | None = None,
        event_type: str | None = None,
        license_type: str | None = None,
        report_type: str | None = None,
        stitch_name: str | None = None,
        logid: list | None = None,
        trigger_frequency: str | None = None,
        trigger_weekday: str | None = None,
        trigger_day: int | None = None,
        trigger_hour: int | None = None,
        trigger_minute: int | None = None,
        trigger_datetime: str | None = None,
        fields: list | None = None,
        faz_event_name: str | None = None,
        faz_event_severity: str | None = None,
        faz_event_tags: str | None = None,
        serial: str | None = None,
        fabric_event_name: str | None = None,
        fabric_event_severity: str | None = None,
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
            description: Description. (optional)
            trigger_type: Trigger type. (optional)
            event_type: Event type. (optional)
            license_type: License type. (optional)
            report_type: Security Rating report. (optional)
            stitch_name: Triggering stitch name. (optional)
            logid: Log IDs to trigger event. (optional)
            trigger_frequency: Scheduled trigger frequency (default = daily).
            (optional)
            trigger_weekday: Day of week for trigger. (optional)
            trigger_day: Day within a month to trigger. (optional)
            trigger_hour: Hour of the day on which to trigger (0 - 23, default
            = 1). (optional)
            trigger_minute: Minute of the hour on which to trigger (0 - 59,
            default = 0). (optional)
            trigger_datetime: Trigger date and time (YYYY-MM-DD HH:MM:SS).
            (optional)
            fields: Customized trigger field settings. (optional)
            faz_event_name: FortiAnalyzer event handler name. (optional)
            faz_event_severity: FortiAnalyzer event severity. (optional)
            faz_event_tags: FortiAnalyzer event tags. (optional)
            serial: Fabric connector serial number. (optional)
            fabric_event_name: Fabric connector event handler name. (optional)
            fabric_event_severity: Fabric connector event severity. (optional)
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
        endpoint = f"/system/automation-trigger/{name}"
        if before is not None:
            data_payload["before"] = before
        if after is not None:
            data_payload["after"] = after
        if name is not None:
            data_payload["name"] = name
        if description is not None:
            data_payload["description"] = description
        if trigger_type is not None:
            data_payload["trigger-type"] = trigger_type
        if event_type is not None:
            data_payload["event-type"] = event_type
        if license_type is not None:
            data_payload["license-type"] = license_type
        if report_type is not None:
            data_payload["report-type"] = report_type
        if stitch_name is not None:
            data_payload["stitch-name"] = stitch_name
        if logid is not None:
            data_payload["logid"] = logid
        if trigger_frequency is not None:
            data_payload["trigger-frequency"] = trigger_frequency
        if trigger_weekday is not None:
            data_payload["trigger-weekday"] = trigger_weekday
        if trigger_day is not None:
            data_payload["trigger-day"] = trigger_day
        if trigger_hour is not None:
            data_payload["trigger-hour"] = trigger_hour
        if trigger_minute is not None:
            data_payload["trigger-minute"] = trigger_minute
        if trigger_datetime is not None:
            data_payload["trigger-datetime"] = trigger_datetime
        if fields is not None:
            data_payload["fields"] = fields
        if faz_event_name is not None:
            data_payload["faz-event-name"] = faz_event_name
        if faz_event_severity is not None:
            data_payload["faz-event-severity"] = faz_event_severity
        if faz_event_tags is not None:
            data_payload["faz-event-tags"] = faz_event_tags
        if serial is not None:
            data_payload["serial"] = serial
        if fabric_event_name is not None:
            data_payload["fabric-event-name"] = fabric_event_name
        if fabric_event_severity is not None:
            data_payload["fabric-event-severity"] = fabric_event_severity
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
        endpoint = f"/system/automation-trigger/{name}"
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
        description: str | None = None,
        trigger_type: str | None = None,
        event_type: str | None = None,
        license_type: str | None = None,
        report_type: str | None = None,
        stitch_name: str | None = None,
        logid: list | None = None,
        trigger_frequency: str | None = None,
        trigger_weekday: str | None = None,
        trigger_day: int | None = None,
        trigger_hour: int | None = None,
        trigger_minute: int | None = None,
        trigger_datetime: str | None = None,
        fields: list | None = None,
        faz_event_name: str | None = None,
        faz_event_severity: str | None = None,
        faz_event_tags: str | None = None,
        serial: str | None = None,
        fabric_event_name: str | None = None,
        fabric_event_severity: str | None = None,
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
            description: Description. (optional)
            trigger_type: Trigger type. (optional)
            event_type: Event type. (optional)
            license_type: License type. (optional)
            report_type: Security Rating report. (optional)
            stitch_name: Triggering stitch name. (optional)
            logid: Log IDs to trigger event. (optional)
            trigger_frequency: Scheduled trigger frequency (default = daily).
            (optional)
            trigger_weekday: Day of week for trigger. (optional)
            trigger_day: Day within a month to trigger. (optional)
            trigger_hour: Hour of the day on which to trigger (0 - 23, default
            = 1). (optional)
            trigger_minute: Minute of the hour on which to trigger (0 - 59,
            default = 0). (optional)
            trigger_datetime: Trigger date and time (YYYY-MM-DD HH:MM:SS).
            (optional)
            fields: Customized trigger field settings. (optional)
            faz_event_name: FortiAnalyzer event handler name. (optional)
            faz_event_severity: FortiAnalyzer event severity. (optional)
            faz_event_tags: FortiAnalyzer event tags. (optional)
            serial: Fabric connector serial number. (optional)
            fabric_event_name: Fabric connector event handler name. (optional)
            fabric_event_severity: Fabric connector event severity. (optional)
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
        endpoint = "/system/automation-trigger"
        if nkey is not None:
            data_payload["nkey"] = nkey
        if name is not None:
            data_payload["name"] = name
        if description is not None:
            data_payload["description"] = description
        if trigger_type is not None:
            data_payload["trigger-type"] = trigger_type
        if event_type is not None:
            data_payload["event-type"] = event_type
        if license_type is not None:
            data_payload["license-type"] = license_type
        if report_type is not None:
            data_payload["report-type"] = report_type
        if stitch_name is not None:
            data_payload["stitch-name"] = stitch_name
        if logid is not None:
            data_payload["logid"] = logid
        if trigger_frequency is not None:
            data_payload["trigger-frequency"] = trigger_frequency
        if trigger_weekday is not None:
            data_payload["trigger-weekday"] = trigger_weekday
        if trigger_day is not None:
            data_payload["trigger-day"] = trigger_day
        if trigger_hour is not None:
            data_payload["trigger-hour"] = trigger_hour
        if trigger_minute is not None:
            data_payload["trigger-minute"] = trigger_minute
        if trigger_datetime is not None:
            data_payload["trigger-datetime"] = trigger_datetime
        if fields is not None:
            data_payload["fields"] = fields
        if faz_event_name is not None:
            data_payload["faz-event-name"] = faz_event_name
        if faz_event_severity is not None:
            data_payload["faz-event-severity"] = faz_event_severity
        if faz_event_tags is not None:
            data_payload["faz-event-tags"] = faz_event_tags
        if serial is not None:
            data_payload["serial"] = serial
        if fabric_event_name is not None:
            data_payload["fabric-event-name"] = fabric_event_name
        if fabric_event_severity is not None:
            data_payload["fabric-event-severity"] = fabric_event_severity
        data_payload.update(kwargs)
        return self._client.post(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )
