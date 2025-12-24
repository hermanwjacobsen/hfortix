"""
FortiOS CMDB - Cmdb System External Resource

Configuration endpoint for managing cmdb system external resource objects.

API Endpoints:
    GET    /cmdb/system/external_resource
    POST   /cmdb/system/external_resource
    GET    /cmdb/system/external_resource
    PUT    /cmdb/system/external_resource/{identifier}
    DELETE /cmdb/system/external_resource/{identifier}

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.system.external_resource.get()
    >>>
    >>> # Get specific item (if supported)
    >>> item = fgt.api.cmdb.system.external_resource.get(name="item_name")
    >>>
    >>> # Create new item (use POST)
    >>> result = fgt.api.cmdb.system.external_resource.post(
    ...     name="new_item",
    ...     # ... additional parameters
    ... )
    >>>
    >>> # Update existing item (use PUT)
    >>> result = fgt.api.cmdb.system.external_resource.put(
    ...     name="existing_item",
    ...     # ... parameters to update
    ... )
    >>>
    >>> # Delete item
    >>> result = fgt.api.cmdb.system.external_resource.delete(name="item_name")

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


class ExternalResource:
    """
    Externalresource Operations.

    Provides CRUD operations for FortiOS externalresource configuration.

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
        Initialize ExternalResource endpoint.

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
            endpoint = f"/system/external-resource/{name}"
        else:
            endpoint = "/system/external-resource"
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
        uuid: str | None = None,
        status: str | None = None,
        type: str | None = None,
        namespace: str | None = None,
        object_array_path: str | None = None,
        address_name_field: str | None = None,
        address_data_field: str | None = None,
        address_comment_field: str | None = None,
        update_method: str | None = None,
        category: int | None = None,
        username: str | None = None,
        password: str | None = None,
        client_cert_auth: str | None = None,
        client_cert: str | None = None,
        comments: str | None = None,
        resource: str | None = None,
        user_agent: str | None = None,
        server_identity_check: str | None = None,
        refresh_rate: int | None = None,
        source_ip: str | None = None,
        source_ip_interface: str | None = None,
        interface_select_method: str | None = None,
        interface: str | None = None,
        vrf_select: int | None = None,
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
            name: External resource name. (optional)
            uuid: Universally Unique Identifier (UUID; automatically assigned
            but can be manually reset). (optional)
            status: Enable/disable user resource. (optional)
            type: User resource type. (optional)
            namespace: Generic external connector address namespace. (optional)
            object_array_path: JSON Path to array of generic addresses in
            resource. (optional)
            address_name_field: JSON Path to address name in generic address
            entry. (optional)
            address_data_field: JSON Path to address data in generic address
            entry. (optional)
            address_comment_field: JSON Path to address description in generic
            address entry. (optional)
            update_method: External resource update method. (optional)
            category: User resource category. (optional)
            username: HTTP basic authentication user name. (optional)
            password: HTTP basic authentication password. (optional)
            client_cert_auth: Enable/disable using client certificate for TLS
            authentication. (optional)
            client_cert: Client certificate name. (optional)
            comments: Comment. (optional)
            resource: URL of external resource. (optional)
            user_agent: HTTP User-Agent header (default = 'curl/7.58.0').
            (optional)
            server_identity_check: Certificate verification option. (optional)
            refresh_rate: Time interval to refresh external resource (1 - 43200
            min, default = 5 min). (optional)
            source_ip: Source IPv4 address used to communicate with server.
            (optional)
            source_ip_interface: IPv4 Source interface for communication with
            the server. (optional)
            interface_select_method: Specify how to select outgoing interface
            to reach server. (optional)
            interface: Specify outgoing interface to reach server. (optional)
            vrf_select: VRF ID used for connection to server. (optional)
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
        endpoint = f"/system/external-resource/{name}"
        if before is not None:
            data_payload["before"] = before
        if after is not None:
            data_payload["after"] = after
        if name is not None:
            data_payload["name"] = name
        if uuid is not None:
            data_payload["uuid"] = uuid
        if status is not None:
            data_payload["status"] = status
        if type is not None:
            data_payload["type"] = type
        if namespace is not None:
            data_payload["namespace"] = namespace
        if object_array_path is not None:
            data_payload["object-array-path"] = object_array_path
        if address_name_field is not None:
            data_payload["address-name-field"] = address_name_field
        if address_data_field is not None:
            data_payload["address-data-field"] = address_data_field
        if address_comment_field is not None:
            data_payload["address-comment-field"] = address_comment_field
        if update_method is not None:
            data_payload["update-method"] = update_method
        if category is not None:
            data_payload["category"] = category
        if username is not None:
            data_payload["username"] = username
        if password is not None:
            data_payload["password"] = password
        if client_cert_auth is not None:
            data_payload["client-cert-auth"] = client_cert_auth
        if client_cert is not None:
            data_payload["client-cert"] = client_cert
        if comments is not None:
            data_payload["comments"] = comments
        if resource is not None:
            data_payload["resource"] = resource
        if user_agent is not None:
            data_payload["user-agent"] = user_agent
        if server_identity_check is not None:
            data_payload["server-identity-check"] = server_identity_check
        if refresh_rate is not None:
            data_payload["refresh-rate"] = refresh_rate
        if source_ip is not None:
            data_payload["source-ip"] = source_ip
        if source_ip_interface is not None:
            data_payload["source-ip-interface"] = source_ip_interface
        if interface_select_method is not None:
            data_payload["interface-select-method"] = interface_select_method
        if interface is not None:
            data_payload["interface"] = interface
        if vrf_select is not None:
            data_payload["vrf-select"] = vrf_select
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
        endpoint = f"/system/external-resource/{name}"
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
        uuid: str | None = None,
        status: str | None = None,
        type: str | None = None,
        namespace: str | None = None,
        object_array_path: str | None = None,
        address_name_field: str | None = None,
        address_data_field: str | None = None,
        address_comment_field: str | None = None,
        update_method: str | None = None,
        category: int | None = None,
        username: str | None = None,
        password: str | None = None,
        client_cert_auth: str | None = None,
        client_cert: str | None = None,
        comments: str | None = None,
        resource: str | None = None,
        user_agent: str | None = None,
        server_identity_check: str | None = None,
        refresh_rate: int | None = None,
        source_ip: str | None = None,
        source_ip_interface: str | None = None,
        interface_select_method: str | None = None,
        interface: str | None = None,
        vrf_select: int | None = None,
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
            name: External resource name. (optional)
            uuid: Universally Unique Identifier (UUID; automatically assigned
            but can be manually reset). (optional)
            status: Enable/disable user resource. (optional)
            type: User resource type. (optional)
            namespace: Generic external connector address namespace. (optional)
            object_array_path: JSON Path to array of generic addresses in
            resource. (optional)
            address_name_field: JSON Path to address name in generic address
            entry. (optional)
            address_data_field: JSON Path to address data in generic address
            entry. (optional)
            address_comment_field: JSON Path to address description in generic
            address entry. (optional)
            update_method: External resource update method. (optional)
            category: User resource category. (optional)
            username: HTTP basic authentication user name. (optional)
            password: HTTP basic authentication password. (optional)
            client_cert_auth: Enable/disable using client certificate for TLS
            authentication. (optional)
            client_cert: Client certificate name. (optional)
            comments: Comment. (optional)
            resource: URL of external resource. (optional)
            user_agent: HTTP User-Agent header (default = 'curl/7.58.0').
            (optional)
            server_identity_check: Certificate verification option. (optional)
            refresh_rate: Time interval to refresh external resource (1 - 43200
            min, default = 5 min). (optional)
            source_ip: Source IPv4 address used to communicate with server.
            (optional)
            source_ip_interface: IPv4 Source interface for communication with
            the server. (optional)
            interface_select_method: Specify how to select outgoing interface
            to reach server. (optional)
            interface: Specify outgoing interface to reach server. (optional)
            vrf_select: VRF ID used for connection to server. (optional)
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
        endpoint = "/system/external-resource"
        if nkey is not None:
            data_payload["nkey"] = nkey
        if name is not None:
            data_payload["name"] = name
        if uuid is not None:
            data_payload["uuid"] = uuid
        if status is not None:
            data_payload["status"] = status
        if type is not None:
            data_payload["type"] = type
        if namespace is not None:
            data_payload["namespace"] = namespace
        if object_array_path is not None:
            data_payload["object-array-path"] = object_array_path
        if address_name_field is not None:
            data_payload["address-name-field"] = address_name_field
        if address_data_field is not None:
            data_payload["address-data-field"] = address_data_field
        if address_comment_field is not None:
            data_payload["address-comment-field"] = address_comment_field
        if update_method is not None:
            data_payload["update-method"] = update_method
        if category is not None:
            data_payload["category"] = category
        if username is not None:
            data_payload["username"] = username
        if password is not None:
            data_payload["password"] = password
        if client_cert_auth is not None:
            data_payload["client-cert-auth"] = client_cert_auth
        if client_cert is not None:
            data_payload["client-cert"] = client_cert
        if comments is not None:
            data_payload["comments"] = comments
        if resource is not None:
            data_payload["resource"] = resource
        if user_agent is not None:
            data_payload["user-agent"] = user_agent
        if server_identity_check is not None:
            data_payload["server-identity-check"] = server_identity_check
        if refresh_rate is not None:
            data_payload["refresh-rate"] = refresh_rate
        if source_ip is not None:
            data_payload["source-ip"] = source_ip
        if source_ip_interface is not None:
            data_payload["source-ip-interface"] = source_ip_interface
        if interface_select_method is not None:
            data_payload["interface-select-method"] = interface_select_method
        if interface is not None:
            data_payload["interface"] = interface
        if vrf_select is not None:
            data_payload["vrf-select"] = vrf_select
        data_payload.update(kwargs)
        return self._client.post(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )
