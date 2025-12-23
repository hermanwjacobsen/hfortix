"""
FortiOS CMDB - Cmdb Webfilter Fortiguard

Configuration endpoint for managing cmdb webfilter fortiguard objects.

API Endpoints:
    GET    /cmdb/webfilter/fortiguard
    PUT    /cmdb/webfilter/fortiguard/{identifier}

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.webfilter.fortiguard.get()
    >>>
    >>> # Get specific item (if supported)
    >>> item = fgt.api.cmdb.webfilter.fortiguard.get(name="item_name")
    >>>
    >>> # Create new item (use POST)
    >>> result = fgt.api.cmdb.webfilter.fortiguard.post(
    ...     name="new_item",
    ...     # ... additional parameters
    ... )
    >>>
    >>> # Update existing item (use PUT)
    >>> result = fgt.api.cmdb.webfilter.fortiguard.put(
    ...     name="existing_item",
    ...     # ... parameters to update
    ... )
    >>>
    >>> # Delete item
    >>> result = fgt.api.cmdb.webfilter.fortiguard.delete(name="item_name")

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


class Fortiguard:
    """
    Fortiguard Operations.

    Provides CRUD operations for FortiOS fortiguard configuration.

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
        Initialize Fortiguard endpoint.

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
        endpoint = "/webfilter/fortiguard"
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
        cache_mode: str | None = None,
        cache_prefix_match: str | None = None,
        cache_mem_permille: int | None = None,
        ovrd_auth_port_http: int | None = None,
        ovrd_auth_port_https: int | None = None,
        ovrd_auth_port_https_flow: int | None = None,
        ovrd_auth_port_warning: int | None = None,
        ovrd_auth_https: str | None = None,
        warn_auth_https: str | None = None,
        close_ports: str | None = None,
        request_packet_size_limit: int | None = None,
        embed_image: str | None = None,
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
            cache_mode: Cache entry expiration mode. (optional)
            cache_prefix_match: Enable/disable prefix matching in the cache.
            (optional)
            cache_mem_permille: Maximum permille of available memory allocated
            to caching (1 - 150). (optional)
            ovrd_auth_port_http: Port to use for FortiGuard Web Filter HTTP
            override authentication. (optional)
            ovrd_auth_port_https: Port to use for FortiGuard Web Filter HTTPS
            override authentication in proxy mode. (optional)
            ovrd_auth_port_https_flow: Port to use for FortiGuard Web Filter
            HTTPS override authentication in flow mode. (optional)
            ovrd_auth_port_warning: Port to use for FortiGuard Web Filter
            Warning override authentication. (optional)
            ovrd_auth_https: Enable/disable use of HTTPS for override
            authentication. (optional)
            warn_auth_https: Enable/disable use of HTTPS for warning and
            authentication. (optional)
            close_ports: Close ports used for HTTP/HTTPS override
            authentication and disable user overrides. (optional)
            request_packet_size_limit: Limit size of URL request packets sent
            to FortiGuard server (0 for default). (optional)
            embed_image: Enable/disable embedding images into replacement
            messages (default = enable). (optional)
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
        endpoint = "/webfilter/fortiguard"
        if before is not None:
            data_payload["before"] = before
        if after is not None:
            data_payload["after"] = after
        if cache_mode is not None:
            data_payload["cache-mode"] = cache_mode
        if cache_prefix_match is not None:
            data_payload["cache-prefix-match"] = cache_prefix_match
        if cache_mem_permille is not None:
            data_payload["cache-mem-permille"] = cache_mem_permille
        if ovrd_auth_port_http is not None:
            data_payload["ovrd-auth-port-http"] = ovrd_auth_port_http
        if ovrd_auth_port_https is not None:
            data_payload["ovrd-auth-port-https"] = ovrd_auth_port_https
        if ovrd_auth_port_https_flow is not None:
            data_payload["ovrd-auth-port-https-flow"] = (
                ovrd_auth_port_https_flow
            )
        if ovrd_auth_port_warning is not None:
            data_payload["ovrd-auth-port-warning"] = ovrd_auth_port_warning
        if ovrd_auth_https is not None:
            data_payload["ovrd-auth-https"] = ovrd_auth_https
        if warn_auth_https is not None:
            data_payload["warn-auth-https"] = warn_auth_https
        if close_ports is not None:
            data_payload["close-ports"] = close_ports
        if request_packet_size_limit is not None:
            data_payload["request-packet-size-limit"] = (
                request_packet_size_limit
            )
        if embed_image is not None:
            data_payload["embed-image"] = embed_image
        data_payload.update(kwargs)
        return self._client.put(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )
