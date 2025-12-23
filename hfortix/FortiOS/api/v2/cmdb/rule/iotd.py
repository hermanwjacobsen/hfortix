"""
FortiOS CMDB - Cmdb Rule Iotd

Configuration endpoint for managing cmdb rule iotd objects.

API Endpoints:
    GET    /cmdb/rule/iotd
    POST   /cmdb/rule/iotd
    GET    /cmdb/rule/iotd
    PUT    /cmdb/rule/iotd/{identifier}
    DELETE /cmdb/rule/iotd/{identifier}

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.rule.iotd.get()
    >>>
    >>> # Get specific item (if supported)
    >>> item = fgt.api.cmdb.rule.iotd.get(name="item_name")
    >>>
    >>> # Create new item (use POST)
    >>> result = fgt.api.cmdb.rule.iotd.post(
    ...     name="new_item",
    ...     # ... additional parameters
    ... )
    >>>
    >>> # Update existing item (use PUT)
    >>> result = fgt.api.cmdb.rule.iotd.put(
    ...     name="existing_item",
    ...     # ... parameters to update
    ... )
    >>>
    >>> # Delete item
    >>> result = fgt.api.cmdb.rule.iotd.delete(name="item_name")

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


class Iotd:
    """
    Iotd Operations.

    Provides CRUD operations for FortiOS iotd configuration.

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
        Initialize Iotd endpoint.

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
            endpoint = f"/rule/iotd/{name}"
        else:
            endpoint = "/rule/iotd"
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
        id: int | None = None,
        category: int | None = None,
        popularity: int | None = None,
        risk: int | None = None,
        weight: int | None = None,
        protocol: str | None = None,
        technology: str | None = None,
        behavior: str | None = None,
        vendor: str | None = None,
        parameters: list | None = None,
        metadata: list | None = None,
        status: str | None = None,
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
            name: Application name. (optional)
            id: Application ID. (optional)
            category: Application category ID. (optional)
            popularity: Application popularity. (optional)
            risk: Application risk. (optional)
            weight: Application weight. (optional)
            protocol: Application protocol. (optional)
            technology: Application technology. (optional)
            behavior: Application behavior. (optional)
            vendor: Application vendor. (optional)
            parameters: Application parameters. (optional)
            metadata: Meta data. (optional)
            status: Print all IOT detection rules information. (optional)
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
        endpoint = f"/rule/iotd/{name}"
        if before is not None:
            data_payload["before"] = before
        if after is not None:
            data_payload["after"] = after
        if name is not None:
            data_payload["name"] = name
        if id is not None:
            data_payload["id"] = id
        if category is not None:
            data_payload["category"] = category
        if popularity is not None:
            data_payload["popularity"] = popularity
        if risk is not None:
            data_payload["risk"] = risk
        if weight is not None:
            data_payload["weight"] = weight
        if protocol is not None:
            data_payload["protocol"] = protocol
        if technology is not None:
            data_payload["technology"] = technology
        if behavior is not None:
            data_payload["behavior"] = behavior
        if vendor is not None:
            data_payload["vendor"] = vendor
        if parameters is not None:
            data_payload["parameters"] = parameters
        if metadata is not None:
            data_payload["metadata"] = metadata
        if status is not None:
            data_payload["status"] = status
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
        endpoint = f"/rule/iotd/{name}"
        params.update(kwargs)
        return self._client.delete(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )

    def post(
        self,
        payload_dict: dict[str, Any] | None = None,
        nkey: str | None = None,
        name: str | None = None,
        id: int | None = None,
        category: int | None = None,
        popularity: int | None = None,
        risk: int | None = None,
        weight: int | None = None,
        protocol: str | None = None,
        technology: str | None = None,
        behavior: str | None = None,
        vendor: str | None = None,
        parameters: list | None = None,
        metadata: list | None = None,
        status: str | None = None,
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
            name: Application name. (optional)
            id: Application ID. (optional)
            category: Application category ID. (optional)
            popularity: Application popularity. (optional)
            risk: Application risk. (optional)
            weight: Application weight. (optional)
            protocol: Application protocol. (optional)
            technology: Application technology. (optional)
            behavior: Application behavior. (optional)
            vendor: Application vendor. (optional)
            parameters: Application parameters. (optional)
            metadata: Meta data. (optional)
            status: Print all IOT detection rules information. (optional)
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
        endpoint = "/rule/iotd"
        if nkey is not None:
            data_payload["nkey"] = nkey
        if name is not None:
            data_payload["name"] = name
        if id is not None:
            data_payload["id"] = id
        if category is not None:
            data_payload["category"] = category
        if popularity is not None:
            data_payload["popularity"] = popularity
        if risk is not None:
            data_payload["risk"] = risk
        if weight is not None:
            data_payload["weight"] = weight
        if protocol is not None:
            data_payload["protocol"] = protocol
        if technology is not None:
            data_payload["technology"] = technology
        if behavior is not None:
            data_payload["behavior"] = behavior
        if vendor is not None:
            data_payload["vendor"] = vendor
        if parameters is not None:
            data_payload["parameters"] = parameters
        if metadata is not None:
            data_payload["metadata"] = metadata
        if status is not None:
            data_payload["status"] = status
        data_payload.update(kwargs)
        return self._client.post(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )
