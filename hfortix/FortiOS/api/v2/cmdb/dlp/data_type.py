"""
FortiOS CMDB - Cmdb Dlp Data Type

Configuration endpoint for managing cmdb dlp data type objects.

API Endpoints:
    GET    /cmdb/dlp/data_type
    POST   /cmdb/dlp/data_type
    GET    /cmdb/dlp/data_type
    PUT    /cmdb/dlp/data_type/{identifier}
    DELETE /cmdb/dlp/data_type/{identifier}

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.dlp.data_type.get()
    >>>
    >>> # Get specific item (if supported)
    >>> item = fgt.api.cmdb.dlp.data_type.get(name="item_name")
    >>>
    >>> # Create new item (use POST)
    >>> result = fgt.api.cmdb.dlp.data_type.post(
    ...     name="new_item",
    ...     # ... additional parameters
    ... )
    >>>
    >>> # Update existing item (use PUT)
    >>> result = fgt.api.cmdb.dlp.data_type.put(
    ...     name="existing_item",
    ...     # ... parameters to update
    ... )
    >>>
    >>> # Delete item
    >>> result = fgt.api.cmdb.dlp.data_type.delete(name="item_name")

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


class DataType:
    """
    Datatype Operations.

    Provides CRUD operations for FortiOS datatype configuration.

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
        Initialize DataType endpoint.

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
            endpoint = f"/dlp/data-type/{name}"
        else:
            endpoint = "/dlp/data-type"
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
        verify: str | None = None,
        verify2: str | None = None,
        match_around: str | None = None,
        look_back: int | None = None,
        look_ahead: int | None = None,
        match_back: int | None = None,
        match_ahead: int | None = None,
        transform: str | None = None,
        verify_transformed_pattern: str | None = None,
        comment: str | None = None,
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
            name: Name of table containing the data type. (optional)
            verify: Regular expression pattern string used to verify the data
            type. (optional)
            verify2: Extra regular expression pattern string used to verify the
            data type. (optional)
            match_around: Dictionary to check whether it has a match around
            (Only support match-any and basic types, no repeat supported).
            (optional)
            look_back: Number of characters required to save for verification
            (1 - 255, default = 1). (optional)
            look_ahead: Number of characters to obtain in advance for
            verification (1 - 255, default = 1). (optional)
            match_back: Number of characters in front for match-around (1 -
            4096, default = 1). (optional)
            match_ahead: Number of characters behind for match-around (1 -
            4096, default = 1). (optional)
            transform: Template to transform user input to a pattern using
            capture group from 'pattern'. (optional)
            verify_transformed_pattern: Enable/disable verification for
            transformed pattern. (optional)
            comment: Optional comments. (optional)
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
        endpoint = f"/dlp/data-type/{name}"
        if before is not None:
            data_payload["before"] = before
        if after is not None:
            data_payload["after"] = after
        if name is not None:
            data_payload["name"] = name
        if verify is not None:
            data_payload["verify"] = verify
        if verify2 is not None:
            data_payload["verify2"] = verify2
        if match_around is not None:
            data_payload["match-around"] = match_around
        if look_back is not None:
            data_payload["look-back"] = look_back
        if look_ahead is not None:
            data_payload["look-ahead"] = look_ahead
        if match_back is not None:
            data_payload["match-back"] = match_back
        if match_ahead is not None:
            data_payload["match-ahead"] = match_ahead
        if transform is not None:
            data_payload["transform"] = transform
        if verify_transformed_pattern is not None:
            data_payload["verify-transformed-pattern"] = (
                verify_transformed_pattern
            )
        if comment is not None:
            data_payload["comment"] = comment
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
        endpoint = f"/dlp/data-type/{name}"
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
        verify: str | None = None,
        verify2: str | None = None,
        match_around: str | None = None,
        look_back: int | None = None,
        look_ahead: int | None = None,
        match_back: int | None = None,
        match_ahead: int | None = None,
        transform: str | None = None,
        verify_transformed_pattern: str | None = None,
        comment: str | None = None,
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
            name: Name of table containing the data type. (optional)
            verify: Regular expression pattern string used to verify the data
            type. (optional)
            verify2: Extra regular expression pattern string used to verify the
            data type. (optional)
            match_around: Dictionary to check whether it has a match around
            (Only support match-any and basic types, no repeat supported).
            (optional)
            look_back: Number of characters required to save for verification
            (1 - 255, default = 1). (optional)
            look_ahead: Number of characters to obtain in advance for
            verification (1 - 255, default = 1). (optional)
            match_back: Number of characters in front for match-around (1 -
            4096, default = 1). (optional)
            match_ahead: Number of characters behind for match-around (1 -
            4096, default = 1). (optional)
            transform: Template to transform user input to a pattern using
            capture group from 'pattern'. (optional)
            verify_transformed_pattern: Enable/disable verification for
            transformed pattern. (optional)
            comment: Optional comments. (optional)
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
        endpoint = "/dlp/data-type"
        if nkey is not None:
            data_payload["nkey"] = nkey
        if name is not None:
            data_payload["name"] = name
        if verify is not None:
            data_payload["verify"] = verify
        if verify2 is not None:
            data_payload["verify2"] = verify2
        if match_around is not None:
            data_payload["match-around"] = match_around
        if look_back is not None:
            data_payload["look-back"] = look_back
        if look_ahead is not None:
            data_payload["look-ahead"] = look_ahead
        if match_back is not None:
            data_payload["match-back"] = match_back
        if match_ahead is not None:
            data_payload["match-ahead"] = match_ahead
        if transform is not None:
            data_payload["transform"] = transform
        if verify_transformed_pattern is not None:
            data_payload["verify-transformed-pattern"] = (
                verify_transformed_pattern
            )
        if comment is not None:
            data_payload["comment"] = comment
        data_payload.update(kwargs)
        return self._client.post(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )
