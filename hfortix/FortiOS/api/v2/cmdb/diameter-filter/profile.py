"""
FortiOS CMDB - Cmdb Diameter Filter Profile

Configuration endpoint for managing cmdb diameter filter profile objects.

API Endpoints:
    GET    /cmdb/diameter-filter/profile
    POST   /cmdb/diameter-filter/profile
    GET    /cmdb/diameter-filter/profile
    PUT    /cmdb/diameter-filter/profile/{identifier}
    DELETE /cmdb/diameter-filter/profile/{identifier}

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.diameter_filter.profile.get()
    >>>
    >>> # Get specific item (if supported)
    >>> item = fgt.api.cmdb.diameter_filter.profile.get(name="item_name")
    >>>
    >>> # Create new item (use POST)
    >>> result = fgt.api.cmdb.diameter_filter.profile.post(
    ...     name="new_item",
    ...     # ... additional parameters
    ... )
    >>>
    >>> # Update existing item (use PUT)
    >>> result = fgt.api.cmdb.diameter_filter.profile.put(
    ...     name="existing_item",
    ...     # ... parameters to update
    ... )
    >>>
    >>> # Delete item
    >>> result = fgt.api.cmdb.diameter_filter.profile.delete(name="item_name")

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
            endpoint = f"/diameter-filter/profile/{name}"
        else:
            endpoint = "/diameter-filter/profile"
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
        monitor_all_messages: str | None = None,
        log_packet: str | None = None,
        track_requests_answers: str | None = None,
        missing_request_action: str | None = None,
        protocol_version_invalid: str | None = None,
        message_length_invalid: str | None = None,
        request_error_flag_set: str | None = None,
        cmd_flags_reserve_set: str | None = None,
        command_code_invalid: str | None = None,
        command_code_range: str | None = None,
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
            monitor_all_messages: Enable/disable logging for all User Name and
            Result Code AVP messages. (optional)
            log_packet: Enable/disable packet log for triggered diameter
            settings. (optional)
            track_requests_answers: Enable/disable validation that each answer
            has a corresponding request. (optional)
            missing_request_action: Action to be taken for answers without
            corresponding request. (optional)
            protocol_version_invalid: Action to be taken for invalid protocol
            version. (optional)
            message_length_invalid: Action to be taken for invalid message
            length. (optional)
            request_error_flag_set: Action to be taken for request messages
            with error flag set. (optional)
            cmd_flags_reserve_set: Action to be taken for messages with cmd
            flag reserve bits set. (optional)
            command_code_invalid: Action to be taken for messages with invalid
            command code. (optional)
            command_code_range: Valid range for command codes (0-16777215).
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
        endpoint = f"/diameter-filter/profile/{name}"
        if before is not None:
            data_payload["before"] = before
        if after is not None:
            data_payload["after"] = after
        if name is not None:
            data_payload["name"] = name
        if comment is not None:
            data_payload["comment"] = comment
        if monitor_all_messages is not None:
            data_payload["monitor-all-messages"] = monitor_all_messages
        if log_packet is not None:
            data_payload["log-packet"] = log_packet
        if track_requests_answers is not None:
            data_payload["track-requests-answers"] = track_requests_answers
        if missing_request_action is not None:
            data_payload["missing-request-action"] = missing_request_action
        if protocol_version_invalid is not None:
            data_payload["protocol-version-invalid"] = protocol_version_invalid
        if message_length_invalid is not None:
            data_payload["message-length-invalid"] = message_length_invalid
        if request_error_flag_set is not None:
            data_payload["request-error-flag-set"] = request_error_flag_set
        if cmd_flags_reserve_set is not None:
            data_payload["cmd-flags-reserve-set"] = cmd_flags_reserve_set
        if command_code_invalid is not None:
            data_payload["command-code-invalid"] = command_code_invalid
        if command_code_range is not None:
            data_payload["command-code-range"] = command_code_range
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
        endpoint = f"/diameter-filter/profile/{name}"
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
        monitor_all_messages: str | None = None,
        log_packet: str | None = None,
        track_requests_answers: str | None = None,
        missing_request_action: str | None = None,
        protocol_version_invalid: str | None = None,
        message_length_invalid: str | None = None,
        request_error_flag_set: str | None = None,
        cmd_flags_reserve_set: str | None = None,
        command_code_invalid: str | None = None,
        command_code_range: str | None = None,
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
            monitor_all_messages: Enable/disable logging for all User Name and
            Result Code AVP messages. (optional)
            log_packet: Enable/disable packet log for triggered diameter
            settings. (optional)
            track_requests_answers: Enable/disable validation that each answer
            has a corresponding request. (optional)
            missing_request_action: Action to be taken for answers without
            corresponding request. (optional)
            protocol_version_invalid: Action to be taken for invalid protocol
            version. (optional)
            message_length_invalid: Action to be taken for invalid message
            length. (optional)
            request_error_flag_set: Action to be taken for request messages
            with error flag set. (optional)
            cmd_flags_reserve_set: Action to be taken for messages with cmd
            flag reserve bits set. (optional)
            command_code_invalid: Action to be taken for messages with invalid
            command code. (optional)
            command_code_range: Valid range for command codes (0-16777215).
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
        endpoint = "/diameter-filter/profile"
        if nkey is not None:
            data_payload["nkey"] = nkey
        if name is not None:
            data_payload["name"] = name
        if comment is not None:
            data_payload["comment"] = comment
        if monitor_all_messages is not None:
            data_payload["monitor-all-messages"] = monitor_all_messages
        if log_packet is not None:
            data_payload["log-packet"] = log_packet
        if track_requests_answers is not None:
            data_payload["track-requests-answers"] = track_requests_answers
        if missing_request_action is not None:
            data_payload["missing-request-action"] = missing_request_action
        if protocol_version_invalid is not None:
            data_payload["protocol-version-invalid"] = protocol_version_invalid
        if message_length_invalid is not None:
            data_payload["message-length-invalid"] = message_length_invalid
        if request_error_flag_set is not None:
            data_payload["request-error-flag-set"] = request_error_flag_set
        if cmd_flags_reserve_set is not None:
            data_payload["cmd-flags-reserve-set"] = cmd_flags_reserve_set
        if command_code_invalid is not None:
            data_payload["command-code-invalid"] = command_code_invalid
        if command_code_range is not None:
            data_payload["command-code-range"] = command_code_range
        data_payload.update(kwargs)
        return self._client.post(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )
