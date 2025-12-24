"""
FortiOS CMDB - Cmdb Firewall Local In Policy6

Configuration endpoint for managing cmdb firewall local in policy6 objects.

API Endpoints:
    GET    /cmdb/firewall/local_in_policy6
    POST   /cmdb/firewall/local_in_policy6
    GET    /cmdb/firewall/local_in_policy6
    PUT    /cmdb/firewall/local_in_policy6/{identifier}
    DELETE /cmdb/firewall/local_in_policy6/{identifier}

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.firewall.local_in_policy6.get()
    >>>
    >>> # Get specific item (if supported)
    >>> item = fgt.api.cmdb.firewall.local_in_policy6.get(name="item_name")
    >>>
    >>> # Create new item (use POST)
    >>> result = fgt.api.cmdb.firewall.local_in_policy6.post(
    ...     name="new_item",
    ...     # ... additional parameters
    ... )
    >>>
    >>> # Update existing item (use PUT)
    >>> result = fgt.api.cmdb.firewall.local_in_policy6.put(
    ...     name="existing_item",
    ...     # ... parameters to update
    ... )
    >>>
    >>> # Delete item
    >>> result =
    fgt.api.cmdb.firewall.local_in_policy6.delete(name="item_name")

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


class LocalInPolicy6:
    """
    Localinpolicy6 Operations.

    Provides CRUD operations for FortiOS localinpolicy6 configuration.

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
        Initialize LocalInPolicy6 endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

    def get(
        self,
        policyid: str | None = None,
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
            policyid: Object identifier (optional for list, required for
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
        if policyid:
            endpoint = f"/firewall/local-in-policy6/{policyid}"
        else:
            endpoint = "/firewall/local-in-policy6"
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
        policyid: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        before: str | None = None,
        after: str | None = None,
        uuid: str | None = None,
        intf: list | None = None,
        srcaddr: list | None = None,
        srcaddr_negate: str | None = None,
        dstaddr: list | None = None,
        internet_service6_src: str | None = None,
        internet_service6_src_name: list | None = None,
        internet_service6_src_group: list | None = None,
        internet_service6_src_custom: list | None = None,
        internet_service6_src_custom_group: list | None = None,
        internet_service6_src_fortiguard: list | None = None,
        dstaddr_negate: str | None = None,
        service: list | None = None,
        service_negate: str | None = None,
        internet_service6_src_negate: str | None = None,
        schedule: str | None = None,
        status: str | None = None,
        virtual_patch: str | None = None,
        logtraffic: str | None = None,
        comments: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update this specific resource.

        Args:
            payload_dict: Optional dictionary of all parameters (can be passed
            as first positional arg)
            policyid: Object identifier (required)
            before: If *action=move*, use *before* to specify the ID of the
            resource that this resource will be moved before. (optional)
            after: If *action=move*, use *after* to specify the ID of the
            resource that this resource will be moved after. (optional)
            policyid: User defined local in policy ID. (optional)
            uuid: Universally Unique Identifier (UUID; automatically assigned
            but can be manually reset). (optional)
            intf: Incoming interface name from available options. (optional)
            srcaddr: Source address object from available options. (optional)
            srcaddr_negate: When enabled srcaddr specifies what the source
            address must NOT be. (optional)
            dstaddr: Destination address object from available options.
            (optional)
            internet_service6_src: Enable/disable use of IPv6 Internet Services
            in source for this local-in policy.If enabled, source address is
            not used. (optional)
            internet_service6_src_name: IPv6 Internet Service source name.
            (optional)
            internet_service6_src_group: Internet Service6 source group name.
            (optional)
            internet_service6_src_custom: Custom IPv6 Internet Service source
            name. (optional)
            internet_service6_src_custom_group: Custom Internet Service6 source
            group name. (optional)
            internet_service6_src_fortiguard: FortiGuard IPv6 Internet Service
            source name. (optional)
            dstaddr_negate: When enabled dstaddr specifies what the destination
            address must NOT be. (optional)
            service: Service object from available options. Separate names with
            a space. (optional)
            service_negate: When enabled service specifies what the service
            must NOT be. (optional)
            internet_service6_src_negate: When enabled internet-service6-src
            specifies what the service must NOT be. (optional)
            schedule: Schedule object from available options. (optional)
            status: Enable/disable this local-in policy. (optional)
            virtual_patch: Enable/disable the virtual patching feature.
            (optional)
            logtraffic: Enable/disable local-in traffic logging. (optional)
            comments: Comment. (optional)
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
        if not policyid:
            raise ValueError("policyid is required for put()")
        endpoint = f"/firewall/local-in-policy6/{policyid}"
        if before is not None:
            data_payload["before"] = before
        if after is not None:
            data_payload["after"] = after
        if policyid is not None:
            data_payload["policyid"] = policyid
        if uuid is not None:
            data_payload["uuid"] = uuid
        if intf is not None:
            data_payload["int"] = intf
        if srcaddr is not None:
            data_payload["srcaddr"] = srcaddr
        if srcaddr_negate is not None:
            data_payload["srcaddr-negate"] = srcaddr_negate
        if dstaddr is not None:
            data_payload["dstaddr"] = dstaddr
        if internet_service6_src is not None:
            data_payload["internet-service6-src"] = internet_service6_src
        if internet_service6_src_name is not None:
            data_payload["internet-service6-src-name"] = (
                internet_service6_src_name
            )
        if internet_service6_src_group is not None:
            data_payload["internet-service6-src-group"] = (
                internet_service6_src_group
            )
        if internet_service6_src_custom is not None:
            data_payload["internet-service6-src-custom"] = (
                internet_service6_src_custom
            )
        if internet_service6_src_custom_group is not None:
            data_payload["internet-service6-src-custom-group"] = (
                internet_service6_src_custom_group
            )
        if internet_service6_src_fortiguard is not None:
            data_payload["internet-service6-src-fortiguard"] = (
                internet_service6_src_fortiguard
            )
        if dstaddr_negate is not None:
            data_payload["dstaddr-negate"] = dstaddr_negate
        if service is not None:
            data_payload["service"] = service
        if service_negate is not None:
            data_payload["service-negate"] = service_negate
        if internet_service6_src_negate is not None:
            data_payload["internet-service6-src-negate"] = (
                internet_service6_src_negate
            )
        if schedule is not None:
            data_payload["schedule"] = schedule
        if status is not None:
            data_payload["status"] = status
        if virtual_patch is not None:
            data_payload["virtual-patch"] = virtual_patch
        if logtraffic is not None:
            data_payload["logtraffic"] = logtraffic
        if comments is not None:
            data_payload["comments"] = comments
        data_payload.update(kwargs)
        return self._client.put(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )

    def delete(
        self,
        policyid: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Delete this specific resource.

        Args:
            policyid: Object identifier (required)
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
        if not policyid:
            raise ValueError("policyid is required for delete()")
        endpoint = f"/firewall/local-in-policy6/{policyid}"
        params.update(kwargs)
        return self._client.delete(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )

    def exists(
        self,
        policyid: str,
        vdom: str | bool | None = None,
    ) -> Union[bool, Coroutine[Any, Any, bool]]:
        """
        Check if an object exists.

        Args:
            policyid: Object identifier
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
        result = self.get(policyid=policyid, vdom=vdom)

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
        policyid: int | None = None,
        uuid: str | None = None,
        intf: list | None = None,
        srcaddr: list | None = None,
        srcaddr_negate: str | None = None,
        dstaddr: list | None = None,
        internet_service6_src: str | None = None,
        internet_service6_src_name: list | None = None,
        internet_service6_src_group: list | None = None,
        internet_service6_src_custom: list | None = None,
        internet_service6_src_custom_group: list | None = None,
        internet_service6_src_fortiguard: list | None = None,
        dstaddr_negate: str | None = None,
        service: list | None = None,
        service_negate: str | None = None,
        internet_service6_src_negate: str | None = None,
        schedule: str | None = None,
        status: str | None = None,
        virtual_patch: str | None = None,
        logtraffic: str | None = None,
        comments: str | None = None,
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
            policyid: User defined local in policy ID. (optional)
            uuid: Universally Unique Identifier (UUID; automatically assigned
            but can be manually reset). (optional)
            intf: Incoming interface name from available options. (optional)
            srcaddr: Source address object from available options. (optional)
            srcaddr_negate: When enabled srcaddr specifies what the source
            address must NOT be. (optional)
            dstaddr: Destination address object from available options.
            (optional)
            internet_service6_src: Enable/disable use of IPv6 Internet Services
            in source for this local-in policy.If enabled, source address is
            not used. (optional)
            internet_service6_src_name: IPv6 Internet Service source name.
            (optional)
            internet_service6_src_group: Internet Service6 source group name.
            (optional)
            internet_service6_src_custom: Custom IPv6 Internet Service source
            name. (optional)
            internet_service6_src_custom_group: Custom Internet Service6 source
            group name. (optional)
            internet_service6_src_fortiguard: FortiGuard IPv6 Internet Service
            source name. (optional)
            dstaddr_negate: When enabled dstaddr specifies what the destination
            address must NOT be. (optional)
            service: Service object from available options. Separate names with
            a space. (optional)
            service_negate: When enabled service specifies what the service
            must NOT be. (optional)
            internet_service6_src_negate: When enabled internet-service6-src
            specifies what the service must NOT be. (optional)
            schedule: Schedule object from available options. (optional)
            status: Enable/disable this local-in policy. (optional)
            virtual_patch: Enable/disable the virtual patching feature.
            (optional)
            logtraffic: Enable/disable local-in traffic logging. (optional)
            comments: Comment. (optional)
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
        endpoint = "/firewall/local-in-policy6"
        if nkey is not None:
            data_payload["nkey"] = nkey
        if policyid is not None:
            data_payload["policyid"] = policyid
        if uuid is not None:
            data_payload["uuid"] = uuid
        if intf is not None:
            data_payload["int"] = intf
        if srcaddr is not None:
            data_payload["srcaddr"] = srcaddr
        if srcaddr_negate is not None:
            data_payload["srcaddr-negate"] = srcaddr_negate
        if dstaddr is not None:
            data_payload["dstaddr"] = dstaddr
        if internet_service6_src is not None:
            data_payload["internet-service6-src"] = internet_service6_src
        if internet_service6_src_name is not None:
            data_payload["internet-service6-src-name"] = (
                internet_service6_src_name
            )
        if internet_service6_src_group is not None:
            data_payload["internet-service6-src-group"] = (
                internet_service6_src_group
            )
        if internet_service6_src_custom is not None:
            data_payload["internet-service6-src-custom"] = (
                internet_service6_src_custom
            )
        if internet_service6_src_custom_group is not None:
            data_payload["internet-service6-src-custom-group"] = (
                internet_service6_src_custom_group
            )
        if internet_service6_src_fortiguard is not None:
            data_payload["internet-service6-src-fortiguard"] = (
                internet_service6_src_fortiguard
            )
        if dstaddr_negate is not None:
            data_payload["dstaddr-negate"] = dstaddr_negate
        if service is not None:
            data_payload["service"] = service
        if service_negate is not None:
            data_payload["service-negate"] = service_negate
        if internet_service6_src_negate is not None:
            data_payload["internet-service6-src-negate"] = (
                internet_service6_src_negate
            )
        if schedule is not None:
            data_payload["schedule"] = schedule
        if status is not None:
            data_payload["status"] = status
        if virtual_patch is not None:
            data_payload["virtual-patch"] = virtual_patch
        if logtraffic is not None:
            data_payload["logtraffic"] = logtraffic
        if comments is not None:
            data_payload["comments"] = comments
        data_payload.update(kwargs)
        return self._client.post(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )
