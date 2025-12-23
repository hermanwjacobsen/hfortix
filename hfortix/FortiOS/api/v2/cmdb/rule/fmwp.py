"""
FortiOS CMDB - Cmdb Rule Fmwp

Configuration endpoint for managing cmdb rule fmwp objects.

API Endpoints:
    GET    /cmdb/rule/fmwp
    POST   /cmdb/rule/fmwp
    GET    /cmdb/rule/fmwp
    PUT    /cmdb/rule/fmwp/{identifier}
    DELETE /cmdb/rule/fmwp/{identifier}

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.rule.fmwp.get()
    >>>
    >>> # Get specific item (if supported)
    >>> item = fgt.api.cmdb.rule.fmwp.get(name="item_name")
    >>>
    >>> # Create new item (use POST)
    >>> result = fgt.api.cmdb.rule.fmwp.post(
    ...     name="new_item",
    ...     # ... additional parameters
    ... )
    >>>
    >>> # Update existing item (use PUT)
    >>> result = fgt.api.cmdb.rule.fmwp.put(
    ...     name="existing_item",
    ...     # ... parameters to update
    ... )
    >>>
    >>> # Delete item
    >>> result = fgt.api.cmdb.rule.fmwp.delete(name="item_name")

Important:
    - Use **POST** to create new objects (404 error if already exists)
    - Use **PUT** to update existing objects (404 error if doesn't exist)
    - Use **GET** to retrieve configuration (no changes made)
    - Use **DELETE** to remove objects (404 error if doesn't exist)
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Union

if TYPE_CHECKING:
    from collections.abc import Coroutine

    from hfortix.FortiOS.http_client_interface import IHTTPClient


class Fmwp:
    """
    Fmwp Operations.

    Provides CRUD operations for FortiOS fmwp configuration.

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
        Initialize Fmwp endpoint.

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
            endpoint = f"/rule/fmwp/{name}"
        else:
            endpoint = "/rule/fmwp"
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
        log: str | None = None,
        log_packet: str | None = None,
        group: str | None = None,
        severity: str | None = None,
        location: str | None = None,
        os: str | None = None,
        application: str | None = None,
        service: str | None = None,
        rule_id: int | None = None,
        rev: int | None = None,
        date: int | None = None,
        metadata: list | None = None,
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
            name: Rule name. (optional)
            status: Print all FMWP rules information. (optional)
            log: Enable/disable logging. (optional)
            log_packet: Enable/disable packet logging. (optional)
            group: Group. (optional)
            severity: Severity. (optional)
            location: Vulnerable location. (optional)
            os: Vulnerable operation systems. (optional)
            application: Vulnerable applications. (optional)
            service: Vulnerable service. (optional)
            rule_id: Rule ID. (optional)
            rev: Revision. (optional)
            date: Date. (optional)
            metadata: Meta data. (optional)
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
        endpoint = f"/rule/fmwp/{name}"
        if before is not None:
            data_payload["before"] = before
        if after is not None:
            data_payload["after"] = after
        if name is not None:
            data_payload["name"] = name
        if status is not None:
            data_payload["status"] = status
        if log is not None:
            data_payload["log"] = log
        if log_packet is not None:
            data_payload["log-packet"] = log_packet
        if group is not None:
            data_payload["group"] = group
        if severity is not None:
            data_payload["severity"] = severity
        if location is not None:
            data_payload["location"] = location
        if os is not None:
            data_payload["os"] = os
        if application is not None:
            data_payload["application"] = application
        if service is not None:
            data_payload["service"] = service
        if rule_id is not None:
            data_payload["rule-id"] = rule_id
        if rev is not None:
            data_payload["rev"] = rev
        if date is not None:
            data_payload["date"] = date
        if metadata is not None:
            data_payload["metadata"] = metadata
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
        endpoint = f"/rule/fmwp/{name}"
        params.update(kwargs)
        return self._client.delete(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )

    def post(
        self,
        payload_dict: dict[str, Any] | None = None,
        nkey: str | None = None,
        name: str | None = None,
        status: str | None = None,
        log: str | None = None,
        log_packet: str | None = None,
        group: str | None = None,
        severity: str | None = None,
        location: str | None = None,
        os: str | None = None,
        application: str | None = None,
        service: str | None = None,
        rule_id: int | None = None,
        rev: int | None = None,
        date: int | None = None,
        metadata: list | None = None,
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
            name: Rule name. (optional)
            status: Print all FMWP rules information. (optional)
            log: Enable/disable logging. (optional)
            log_packet: Enable/disable packet logging. (optional)
            group: Group. (optional)
            severity: Severity. (optional)
            location: Vulnerable location. (optional)
            os: Vulnerable operation systems. (optional)
            application: Vulnerable applications. (optional)
            service: Vulnerable service. (optional)
            rule_id: Rule ID. (optional)
            rev: Revision. (optional)
            date: Date. (optional)
            metadata: Meta data. (optional)
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
        endpoint = "/rule/fmwp"
        if nkey is not None:
            data_payload["nkey"] = nkey
        if name is not None:
            data_payload["name"] = name
        if status is not None:
            data_payload["status"] = status
        if log is not None:
            data_payload["log"] = log
        if log_packet is not None:
            data_payload["log-packet"] = log_packet
        if group is not None:
            data_payload["group"] = group
        if severity is not None:
            data_payload["severity"] = severity
        if location is not None:
            data_payload["location"] = location
        if os is not None:
            data_payload["os"] = os
        if application is not None:
            data_payload["application"] = application
        if service is not None:
            data_payload["service"] = service
        if rule_id is not None:
            data_payload["rule-id"] = rule_id
        if rev is not None:
            data_payload["rev"] = rev
        if date is not None:
            data_payload["date"] = date
        if metadata is not None:
            data_payload["metadata"] = metadata
        data_payload.update(kwargs)
        return self._client.post(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )
