"""
FortiOS CMDB - Cmdb System Ike

Configuration endpoint for managing cmdb system ike objects.

API Endpoints:
    GET    /cmdb/system/ike
    PUT    /cmdb/system/ike/{identifier}

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.system.ike.get()
    >>>
    >>> # Get specific item (if supported)
    >>> item = fgt.api.cmdb.system.ike.get(name="item_name")
    >>>
    >>> # Create new item (use POST)
    >>> result = fgt.api.cmdb.system.ike.post(
    ...     name="new_item",
    ...     # ... additional parameters
    ... )
    >>>
    >>> # Update existing item (use PUT)
    >>> result = fgt.api.cmdb.system.ike.put(
    ...     name="existing_item",
    ...     # ... parameters to update
    ... )
    >>>
    >>> # Delete item
    >>> result = fgt.api.cmdb.system.ike.delete(name="item_name")

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


class Ike:
    """
    Ike Operations.

    Provides CRUD operations for FortiOS ike configuration.

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
        Initialize Ike endpoint.

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
        endpoint = "/system/ike"
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
        embryonic_limit: int | None = None,
        dh_multiprocess: str | None = None,
        dh_worker_count: int | None = None,
        dh_mode: str | None = None,
        dh_keypair_cache: str | None = None,
        dh_keypair_count: int | None = None,
        dh_keypair_throttle: str | None = None,
        dh_group_1: list | None = None,
        dh_group_2: list | None = None,
        dh_group_5: list | None = None,
        dh_group_14: list | None = None,
        dh_group_15: list | None = None,
        dh_group_16: list | None = None,
        dh_group_17: list | None = None,
        dh_group_18: list | None = None,
        dh_group_19: list | None = None,
        dh_group_20: list | None = None,
        dh_group_21: list | None = None,
        dh_group_27: list | None = None,
        dh_group_28: list | None = None,
        dh_group_29: list | None = None,
        dh_group_30: list | None = None,
        dh_group_31: list | None = None,
        dh_group_32: list | None = None,
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
            embryonic_limit: Maximum number of IPsec tunnels to negotiate
            simultaneously. (optional)
            dh_multiprocess: Enable/disable multiprocess Diffie-Hellman daemon
            for IKE. (optional)
            dh_worker_count: Number of Diffie-Hellman workers to start.
            (optional)
            dh_mode: Use software (CPU) or hardware (CPX) to perform
            Diffie-Hellman calculations. (optional)
            dh_keypair_cache: Enable/disable Diffie-Hellman key pair cache.
            (optional)
            dh_keypair_count: Number of key pairs to pre-generate for each
            Diffie-Hellman group (per-worker). (optional)
            dh_keypair_throttle: Enable/disable Diffie-Hellman key pair cache
            CPU throttling. (optional)
            dh_group_1: Diffie-Hellman group 1 (MODP-768). (optional)
            dh_group_2: Diffie-Hellman group 2 (MODP-1024). (optional)
            dh_group_5: Diffie-Hellman group 5 (MODP-1536). (optional)
            dh_group_14: Diffie-Hellman group 14 (MODP-2048). (optional)
            dh_group_15: Diffie-Hellman group 15 (MODP-3072). (optional)
            dh_group_16: Diffie-Hellman group 16 (MODP-4096). (optional)
            dh_group_17: Diffie-Hellman group 17 (MODP-6144). (optional)
            dh_group_18: Diffie-Hellman group 18 (MODP-8192). (optional)
            dh_group_19: Diffie-Hellman group 19 (EC-P256). (optional)
            dh_group_20: Diffie-Hellman group 20 (EC-P384). (optional)
            dh_group_21: Diffie-Hellman group 21 (EC-P521). (optional)
            dh_group_27: Diffie-Hellman group 27 (EC-P224BP). (optional)
            dh_group_28: Diffie-Hellman group 28 (EC-P256BP). (optional)
            dh_group_29: Diffie-Hellman group 29 (EC-P384BP). (optional)
            dh_group_30: Diffie-Hellman group 30 (EC-P512BP). (optional)
            dh_group_31: Diffie-Hellman group 31 (EC-X25519). (optional)
            dh_group_32: Diffie-Hellman group 32 (EC-X448). (optional)
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
        endpoint = "/system/ike"
        if before is not None:
            data_payload["before"] = before
        if after is not None:
            data_payload["after"] = after
        if embryonic_limit is not None:
            data_payload["embryonic-limit"] = embryonic_limit
        if dh_multiprocess is not None:
            data_payload["dh-multiprocess"] = dh_multiprocess
        if dh_worker_count is not None:
            data_payload["dh-worker-count"] = dh_worker_count
        if dh_mode is not None:
            data_payload["dh-mode"] = dh_mode
        if dh_keypair_cache is not None:
            data_payload["dh-keypair-cache"] = dh_keypair_cache
        if dh_keypair_count is not None:
            data_payload["dh-keypair-count"] = dh_keypair_count
        if dh_keypair_throttle is not None:
            data_payload["dh-keypair-throttle"] = dh_keypair_throttle
        if dh_group_1 is not None:
            data_payload["dh-group-1"] = dh_group_1
        if dh_group_2 is not None:
            data_payload["dh-group-2"] = dh_group_2
        if dh_group_5 is not None:
            data_payload["dh-group-5"] = dh_group_5
        if dh_group_14 is not None:
            data_payload["dh-group-14"] = dh_group_14
        if dh_group_15 is not None:
            data_payload["dh-group-15"] = dh_group_15
        if dh_group_16 is not None:
            data_payload["dh-group-16"] = dh_group_16
        if dh_group_17 is not None:
            data_payload["dh-group-17"] = dh_group_17
        if dh_group_18 is not None:
            data_payload["dh-group-18"] = dh_group_18
        if dh_group_19 is not None:
            data_payload["dh-group-19"] = dh_group_19
        if dh_group_20 is not None:
            data_payload["dh-group-20"] = dh_group_20
        if dh_group_21 is not None:
            data_payload["dh-group-21"] = dh_group_21
        if dh_group_27 is not None:
            data_payload["dh-group-27"] = dh_group_27
        if dh_group_28 is not None:
            data_payload["dh-group-28"] = dh_group_28
        if dh_group_29 is not None:
            data_payload["dh-group-29"] = dh_group_29
        if dh_group_30 is not None:
            data_payload["dh-group-30"] = dh_group_30
        if dh_group_31 is not None:
            data_payload["dh-group-31"] = dh_group_31
        if dh_group_32 is not None:
            data_payload["dh-group-32"] = dh_group_32
        data_payload.update(kwargs)
        return self._client.put(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )
