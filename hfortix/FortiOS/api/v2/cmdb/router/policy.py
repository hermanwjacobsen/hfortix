"""
FortiOS CMDB - Cmdb Router Policy

Configuration endpoint for managing cmdb router policy objects.

API Endpoints:
    GET    /cmdb/router/policy
    POST   /cmdb/router/policy
    GET    /cmdb/router/policy
    PUT    /cmdb/router/policy/{identifier}
    DELETE /cmdb/router/policy/{identifier}

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.router.policy.get()
    >>>
    >>> # Get specific item (if supported)
    >>> item = fgt.api.cmdb.router.policy.get(name="item_name")
    >>>
    >>> # Create new item (use POST)
    >>> result = fgt.api.cmdb.router.policy.post(
    ...     name="new_item",
    ...     # ... additional parameters
    ... )
    >>>
    >>> # Update existing item (use PUT)
    >>> result = fgt.api.cmdb.router.policy.put(
    ...     name="existing_item",
    ...     # ... parameters to update
    ... )
    >>>
    >>> # Delete item
    >>> result = fgt.api.cmdb.router.policy.delete(name="item_name")

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


class Policy:
    """
    Policy Operations.

    Provides CRUD operations for FortiOS policy configuration.

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
        Initialize Policy endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

    def get(
        self,
        seq_num: str | None = None,
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
            seq_num: Object identifier (optional for list, required for
            specific)
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
        if seq_num:
            endpoint = f"/router/policy/{seq_num}"
        else:
            endpoint = "/router/policy"
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
        seq_num: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        before: str | None = None,
        after: str | None = None,
        input_device: list | None = None,
        input_device_negate: str | None = None,
        src: list | None = None,
        srcaddr: list | None = None,
        src_negate: str | None = None,
        dst: list | None = None,
        dstaddr: list | None = None,
        dst_negate: str | None = None,
        protocol: int | None = None,
        start_port: int | None = None,
        end_port: int | None = None,
        start_source_port: int | None = None,
        end_source_port: int | None = None,
        gateway: str | None = None,
        output_device: str | None = None,
        tos: str | None = None,
        tos_mask: str | None = None,
        status: str | None = None,
        comments: str | None = None,
        internet_service_id: list | None = None,
        internet_service_custom: list | None = None,
        internet_service_fortiguard: list | None = None,
        users: list | None = None,
        groups: list | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update this specific resource.

        Args:
            payload_dict: Optional dictionary of all parameters (can be passed
            as first positional arg)
            seq_num: Object identifier (required)
            before: If *action=move*, use *before* to specify the ID of the
            resource that this resource will be moved before. (optional)
            after: If *action=move*, use *after* to specify the ID of the
            resource that this resource will be moved after. (optional)
            seq_num: Sequence number(1-65535). (optional)
            input_device: Incoming interface name. (optional)
            input_device_negate: Enable/disable negation of input device match.
            (optional)
            src: Source IP and mask (x.x.x.x/x). (optional)
            srcaddr: Source address name. (optional)
            src_negate: Enable/disable negating source address match.
            (optional)
            dst: Destination IP and mask (x.x.x.x/x). (optional)
            dstaddr: Destination address name. (optional)
            dst_negate: Enable/disable negating destination address match.
            (optional)
            protocol: Protocol number (0 - 255). (optional)
            start_port: Start destination port number (0 - 65535). (optional)
            end_port: End destination port number (0 - 65535). (optional)
            start_source_port: Start source port number (0 - 65535). (optional)
            end_source_port: End source port number (0 - 65535). (optional)
            gateway: IP address of the gateway. (optional)
            output_device: Outgoing interface name. (optional)
            tos: Type of service bit pattern. (optional)
            tos_mask: Type of service evaluated bits. (optional)
            status: Enable/disable this policy route. (optional)
            comments: Optional comments. (optional)
            internet_service_id: Destination Internet Service ID. (optional)
            internet_service_custom: Custom Destination Internet Service name.
            (optional)
            internet_service_fortiguard: FortiGuard Destination Internet
            Service name. (optional)
            users: List of users. (optional)
            groups: List of user groups. (optional)
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
        if not seq_num:
            raise ValueError("seq_num is required for put()")
        endpoint = f"/router/policy/{seq_num}"
        if before is not None:
            data_payload["before"] = before
        if after is not None:
            data_payload["after"] = after
        if seq_num is not None:
            data_payload["seq-num"] = seq_num
        if input_device is not None:
            data_payload["input-device"] = input_device
        if input_device_negate is not None:
            data_payload["input-device-negate"] = input_device_negate
        if src is not None:
            data_payload["src"] = src
        if srcaddr is not None:
            data_payload["srcaddr"] = srcaddr
        if src_negate is not None:
            data_payload["src-negate"] = src_negate
        if dst is not None:
            data_payload["dst"] = dst
        if dstaddr is not None:
            data_payload["dstaddr"] = dstaddr
        if dst_negate is not None:
            data_payload["dst-negate"] = dst_negate
        if protocol is not None:
            data_payload["protocol"] = protocol
        if start_port is not None:
            data_payload["start-port"] = start_port
        if end_port is not None:
            data_payload["end-port"] = end_port
        if start_source_port is not None:
            data_payload["start-source-port"] = start_source_port
        if end_source_port is not None:
            data_payload["end-source-port"] = end_source_port
        if gateway is not None:
            data_payload["gateway"] = gateway
        if output_device is not None:
            data_payload["output-device"] = output_device
        if tos is not None:
            data_payload["tos"] = tos
        if tos_mask is not None:
            data_payload["tos-mask"] = tos_mask
        if status is not None:
            data_payload["status"] = status
        if comments is not None:
            data_payload["comments"] = comments
        if internet_service_id is not None:
            data_payload["internet-service-id"] = internet_service_id
        if internet_service_custom is not None:
            data_payload["internet-service-custom"] = internet_service_custom
        if internet_service_fortiguard is not None:
            data_payload["internet-service-fortiguard"] = (
                internet_service_fortiguard
            )
        if users is not None:
            data_payload["users"] = users
        if groups is not None:
            data_payload["groups"] = groups
        data_payload.update(kwargs)
        return self._client.put(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )

    def delete(
        self,
        seq_num: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Delete this specific resource.

        Args:
            seq_num: Object identifier (required)
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
        if not seq_num:
            raise ValueError("seq_num is required for delete()")
        endpoint = f"/router/policy/{seq_num}"
        params.update(kwargs)
        return self._client.delete(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )

    def exists(
        self,
        seq_num: str,
        vdom: str | bool | None = None,
    ) -> Union[bool, Coroutine[Any, Any, bool]]:
        """
        Check if an object exists.

        Args:
            seq_num: Object identifier
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
        result = self.get(seq_num=seq_num, vdom=vdom)

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
        seq_num: int | None = None,
        input_device: list | None = None,
        input_device_negate: str | None = None,
        src: list | None = None,
        srcaddr: list | None = None,
        src_negate: str | None = None,
        dst: list | None = None,
        dstaddr: list | None = None,
        dst_negate: str | None = None,
        protocol: int | None = None,
        start_port: int | None = None,
        end_port: int | None = None,
        start_source_port: int | None = None,
        end_source_port: int | None = None,
        gateway: str | None = None,
        output_device: str | None = None,
        tos: str | None = None,
        tos_mask: str | None = None,
        status: str | None = None,
        comments: str | None = None,
        internet_service_id: list | None = None,
        internet_service_custom: list | None = None,
        internet_service_fortiguard: list | None = None,
        users: list | None = None,
        groups: list | None = None,
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
            seq_num: Sequence number(1-65535). (optional)
            input_device: Incoming interface name. (optional)
            input_device_negate: Enable/disable negation of input device match.
            (optional)
            src: Source IP and mask (x.x.x.x/x). (optional)
            srcaddr: Source address name. (optional)
            src_negate: Enable/disable negating source address match.
            (optional)
            dst: Destination IP and mask (x.x.x.x/x). (optional)
            dstaddr: Destination address name. (optional)
            dst_negate: Enable/disable negating destination address match.
            (optional)
            protocol: Protocol number (0 - 255). (optional)
            start_port: Start destination port number (0 - 65535). (optional)
            end_port: End destination port number (0 - 65535). (optional)
            start_source_port: Start source port number (0 - 65535). (optional)
            end_source_port: End source port number (0 - 65535). (optional)
            gateway: IP address of the gateway. (optional)
            output_device: Outgoing interface name. (optional)
            tos: Type of service bit pattern. (optional)
            tos_mask: Type of service evaluated bits. (optional)
            status: Enable/disable this policy route. (optional)
            comments: Optional comments. (optional)
            internet_service_id: Destination Internet Service ID. (optional)
            internet_service_custom: Custom Destination Internet Service name.
            (optional)
            internet_service_fortiguard: FortiGuard Destination Internet
            Service name. (optional)
            users: List of users. (optional)
            groups: List of user groups. (optional)
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
        endpoint = "/router/policy"
        if nkey is not None:
            data_payload["nkey"] = nkey
        if seq_num is not None:
            data_payload["seq-num"] = seq_num
        if input_device is not None:
            data_payload["input-device"] = input_device
        if input_device_negate is not None:
            data_payload["input-device-negate"] = input_device_negate
        if src is not None:
            data_payload["src"] = src
        if srcaddr is not None:
            data_payload["srcaddr"] = srcaddr
        if src_negate is not None:
            data_payload["src-negate"] = src_negate
        if dst is not None:
            data_payload["dst"] = dst
        if dstaddr is not None:
            data_payload["dstaddr"] = dstaddr
        if dst_negate is not None:
            data_payload["dst-negate"] = dst_negate
        if protocol is not None:
            data_payload["protocol"] = protocol
        if start_port is not None:
            data_payload["start-port"] = start_port
        if end_port is not None:
            data_payload["end-port"] = end_port
        if start_source_port is not None:
            data_payload["start-source-port"] = start_source_port
        if end_source_port is not None:
            data_payload["end-source-port"] = end_source_port
        if gateway is not None:
            data_payload["gateway"] = gateway
        if output_device is not None:
            data_payload["output-device"] = output_device
        if tos is not None:
            data_payload["tos"] = tos
        if tos_mask is not None:
            data_payload["tos-mask"] = tos_mask
        if status is not None:
            data_payload["status"] = status
        if comments is not None:
            data_payload["comments"] = comments
        if internet_service_id is not None:
            data_payload["internet-service-id"] = internet_service_id
        if internet_service_custom is not None:
            data_payload["internet-service-custom"] = internet_service_custom
        if internet_service_fortiguard is not None:
            data_payload["internet-service-fortiguard"] = (
                internet_service_fortiguard
            )
        if users is not None:
            data_payload["users"] = users
        if groups is not None:
            data_payload["groups"] = groups
        data_payload.update(kwargs)
        return self._client.post(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )
