"""
FortiOS CMDB - Cmdb Antivirus Quarantine

Configuration endpoint for managing cmdb antivirus quarantine objects.

API Endpoints:
    GET    /cmdb/antivirus/quarantine
    PUT    /cmdb/antivirus/quarantine/{identifier}

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.antivirus.quarantine.get()
    >>>
    >>> # Get specific item (if supported)
    >>> item = fgt.api.cmdb.antivirus.quarantine.get(name="item_name")
    >>>
    >>> # Create new item (use POST)
    >>> result = fgt.api.cmdb.antivirus.quarantine.post(
    ...     name="new_item",
    ...     # ... additional parameters
    ... )
    >>>
    >>> # Update existing item (use PUT)
    >>> result = fgt.api.cmdb.antivirus.quarantine.put(
    ...     name="existing_item",
    ...     # ... parameters to update
    ... )
    >>>
    >>> # Delete item
    >>> result = fgt.api.cmdb.antivirus.quarantine.delete(name="item_name")

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


class Quarantine:
    """
    Quarantine Operations.

    Provides CRUD operations for FortiOS quarantine configuration.

    Methods:
        get(): Retrieve configuration objects
        put(): Update existing configuration objects

    Important:
        - POST creates new objects (404 if name already exists)
        - PUT updates existing objects (404 if name doesn't exist)
        - GET retrieves objects without making changes
        - DELETE removes objects (404 if name doesn't exist)
    """

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Quarantine endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

    def get(
        self,
        payload_dict: dict[str, Any] | None = None,
        exclude_default_values: bool | None = None,
        stat_items: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Select all entries in a CLI table.

        Args:
            exclude_default_values: Exclude properties/objects with default
            value (optional)
            stat_items: Items to count occurrence in entire response (multiple
            items should be separated by '|'). (optional)
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
        endpoint = "/antivirus/quarantine"
        if exclude_default_values is not None:
            params["exclude-default-values"] = exclude_default_values
        if stat_items is not None:
            params["stat-items"] = stat_items
        params.update(kwargs)
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )

    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        before: str | None = None,
        after: str | None = None,
        agelimit: int | None = None,
        maxfilesize: int | None = None,
        quarantine_quota: int | None = None,
        drop_infected: str | None = None,
        store_infected: str | None = None,
        drop_machine_learning: str | None = None,
        store_machine_learning: str | None = None,
        lowspace: str | None = None,
        destination: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update this specific resource.

        Args:
            payload_dict: Optional dictionary of all parameters (can be passed
            as first positional arg)
            before: If *action=move*, use *before* to specify the ID of the
            resource that this resource will be moved before. (optional)
            after: If *action=move*, use *after* to specify the ID of the
            resource that this resource will be moved after. (optional)
            agelimit: Age limit for quarantined files (0 - 479 hours, 0 means
            forever). (optional)
            maxfilesize: Maximum file size to quarantine (0 - 500 Mbytes, 0
            means unlimited). (optional)
            quarantine_quota: The amount of disk space to reserve for
            quarantining files (0 - 4294967295 Mbytes, 0 means unlimited and
            depends on disk space). (optional)
            drop_infected: Do not quarantine infected files found in sessions
            using the selected protocols. Dropped files are deleted instead of
            being quarantined. (optional)
            store_infected: Quarantine infected files found in sessions using
            the selected protocols. (optional)
            drop_machine_learning: Do not quarantine files detected by machine
            learning found in sessions using the selected protocols. Dropped
            files are deleted instead of being quarantined. (optional)
            store_machine_learning: Quarantine files detected by machine
            learning found in sessions using the selected protocols. (optional)
            lowspace: Select the method for handling additional files when
            running low on disk space. (optional)
            destination: Choose whether to quarantine files to the FortiGate
            disk or to FortiAnalyzer or to delete them instead of quarantining
            them. (optional)
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
        endpoint = "/antivirus/quarantine"
        if before is not None:
            data_payload["before"] = before
        if after is not None:
            data_payload["after"] = after
        if agelimit is not None:
            data_payload["agelimit"] = agelimit
        if maxfilesize is not None:
            data_payload["maxfilesize"] = maxfilesize
        if quarantine_quota is not None:
            data_payload["quarantine-quota"] = quarantine_quota
        if drop_infected is not None:
            data_payload["drop-infected"] = drop_infected
        if store_infected is not None:
            data_payload["store-infected"] = store_infected
        if drop_machine_learning is not None:
            data_payload["drop-machine-learning"] = drop_machine_learning
        if store_machine_learning is not None:
            data_payload["store-machine-learning"] = store_machine_learning
        if lowspace is not None:
            data_payload["lowspace"] = lowspace
        if destination is not None:
            data_payload["destination"] = destination
        data_payload.update(kwargs)
        return self._client.put(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )
