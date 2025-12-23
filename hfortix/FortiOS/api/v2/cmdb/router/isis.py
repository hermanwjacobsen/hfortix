"""
FortiOS CMDB - Cmdb Router Isis

Configuration endpoint for managing cmdb router isis objects.

API Endpoints:
    GET    /cmdb/router/isis
    PUT    /cmdb/router/isis/{identifier}

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.router.isis.get()
    >>>
    >>> # Get specific item (if supported)
    >>> item = fgt.api.cmdb.router.isis.get(name="item_name")
    >>>
    >>> # Create new item (use POST)
    >>> result = fgt.api.cmdb.router.isis.post(
    ...     name="new_item",
    ...     # ... additional parameters
    ... )
    >>>
    >>> # Update existing item (use PUT)
    >>> result = fgt.api.cmdb.router.isis.put(
    ...     name="existing_item",
    ...     # ... parameters to update
    ... )
    >>>
    >>> # Delete item
    >>> result = fgt.api.cmdb.router.isis.delete(name="item_name")

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


class Isis:
    """
    Isis Operations.

    Provides CRUD operations for FortiOS isis configuration.

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
        Initialize Isis endpoint.

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
        endpoint = "/router/isis"
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
        is_type: str | None = None,
        adv_passive_only: str | None = None,
        adv_passive_only6: str | None = None,
        auth_mode_l1: str | None = None,
        auth_mode_l2: str | None = None,
        auth_password_l1: str | None = None,
        auth_password_l2: str | None = None,
        auth_keychain_l1: str | None = None,
        auth_keychain_l2: str | None = None,
        auth_sendonly_l1: str | None = None,
        auth_sendonly_l2: str | None = None,
        ignore_lsp_errors: str | None = None,
        lsp_gen_interval_l1: int | None = None,
        lsp_gen_interval_l2: int | None = None,
        lsp_refresh_interval: int | None = None,
        max_lsp_lifetime: int | None = None,
        spf_interval_exp_l1: str | None = None,
        spf_interval_exp_l2: str | None = None,
        dynamic_hostname: str | None = None,
        adjacency_check: str | None = None,
        adjacency_check6: str | None = None,
        overload_bit: str | None = None,
        overload_bit_suppress: str | None = None,
        overload_bit_on_startup: int | None = None,
        default_originate: str | None = None,
        default_originate6: str | None = None,
        metric_style: str | None = None,
        redistribute_l1: str | None = None,
        redistribute_l1_list: str | None = None,
        redistribute_l2: str | None = None,
        redistribute_l2_list: str | None = None,
        redistribute6_l1: str | None = None,
        redistribute6_l1_list: str | None = None,
        redistribute6_l2: str | None = None,
        redistribute6_l2_list: str | None = None,
        isis_net: list | None = None,
        isis_interface: list | None = None,
        summary_address: list | None = None,
        summary_address6: list | None = None,
        redistribute: list | None = None,
        redistribute6: list | None = None,
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
            is_type: IS type. (optional)
            adv_passive_only: Enable/disable IS-IS advertisement of passive
            interfaces only. (optional)
            adv_passive_only6: Enable/disable IPv6 IS-IS advertisement of
            passive interfaces only. (optional)
            auth_mode_l1: Level 1 authentication mode. (optional)
            auth_mode_l2: Level 2 authentication mode. (optional)
            auth_password_l1: Authentication password for level 1 PDUs.
            (optional)
            auth_password_l2: Authentication password for level 2 PDUs.
            (optional)
            auth_keychain_l1: Authentication key-chain for level 1 PDUs.
            (optional)
            auth_keychain_l2: Authentication key-chain for level 2 PDUs.
            (optional)
            auth_sendonly_l1: Enable/disable level 1 authentication send-only.
            (optional)
            auth_sendonly_l2: Enable/disable level 2 authentication send-only.
            (optional)
            ignore_lsp_errors: Enable/disable ignoring of LSP errors with bad
            checksums. (optional)
            lsp_gen_interval_l1: Minimum interval for level 1 LSP regenerating.
            (optional)
            lsp_gen_interval_l2: Minimum interval for level 2 LSP regenerating.
            (optional)
            lsp_refresh_interval: LSP refresh time in seconds. (optional)
            max_lsp_lifetime: Maximum LSP lifetime in seconds. (optional)
            spf_interval_exp_l1: Level 1 SPF calculation delay. (optional)
            spf_interval_exp_l2: Level 2 SPF calculation delay. (optional)
            dynamic_hostname: Enable/disable dynamic hostname. (optional)
            adjacency_check: Enable/disable adjacency check. (optional)
            adjacency_check6: Enable/disable IPv6 adjacency check. (optional)
            overload_bit: Enable/disable signal other routers not to use us in
            SPF. (optional)
            overload_bit_suppress: Suppress overload-bit for the specific
            prefixes. (optional)
            overload_bit_on_startup: Overload-bit only temporarily after
            reboot. (optional)
            default_originate: Enable/disable distribution of default route
            information. (optional)
            default_originate6: Enable/disable distribution of default IPv6
            route information. (optional)
            metric_style: Use old-style (ISO 10589) or new-style packet
            formats. (optional)
            redistribute_l1: Enable/disable redistribution of level 1 routes
            into level 2. (optional)
            redistribute_l1_list: Access-list for route redistribution from l1
            to l2. (optional)
            redistribute_l2: Enable/disable redistribution of level 2 routes
            into level 1. (optional)
            redistribute_l2_list: Access-list for route redistribution from l2
            to l1. (optional)
            redistribute6_l1: Enable/disable redistribution of level 1 IPv6
            routes into level 2. (optional)
            redistribute6_l1_list: Access-list for IPv6 route redistribution
            from l1 to l2. (optional)
            redistribute6_l2: Enable/disable redistribution of level 2 IPv6
            routes into level 1. (optional)
            redistribute6_l2_list: Access-list for IPv6 route redistribution
            from l2 to l1. (optional)
            isis_net: IS-IS net configuration. (optional)
            isis_interface: IS-IS interface configuration. (optional)
            summary_address: IS-IS summary addresses. (optional)
            summary_address6: IS-IS IPv6 summary address. (optional)
            redistribute: IS-IS redistribute protocols. (optional)
            redistribute6: IS-IS IPv6 redistribution for routing protocols.
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
        endpoint = "/router/isis"
        if before is not None:
            data_payload["before"] = before
        if after is not None:
            data_payload["after"] = after
        if is_type is not None:
            data_payload["is-type"] = is_type
        if adv_passive_only is not None:
            data_payload["adv-passive-only"] = adv_passive_only
        if adv_passive_only6 is not None:
            data_payload["adv-passive-only6"] = adv_passive_only6
        if auth_mode_l1 is not None:
            data_payload["auth-mode-l1"] = auth_mode_l1
        if auth_mode_l2 is not None:
            data_payload["auth-mode-l2"] = auth_mode_l2
        if auth_password_l1 is not None:
            data_payload["auth-password-l1"] = auth_password_l1
        if auth_password_l2 is not None:
            data_payload["auth-password-l2"] = auth_password_l2
        if auth_keychain_l1 is not None:
            data_payload["auth-keychain-l1"] = auth_keychain_l1
        if auth_keychain_l2 is not None:
            data_payload["auth-keychain-l2"] = auth_keychain_l2
        if auth_sendonly_l1 is not None:
            data_payload["auth-sendonly-l1"] = auth_sendonly_l1
        if auth_sendonly_l2 is not None:
            data_payload["auth-sendonly-l2"] = auth_sendonly_l2
        if ignore_lsp_errors is not None:
            data_payload["ignore-lsp-errors"] = ignore_lsp_errors
        if lsp_gen_interval_l1 is not None:
            data_payload["lsp-gen-interval-l1"] = lsp_gen_interval_l1
        if lsp_gen_interval_l2 is not None:
            data_payload["lsp-gen-interval-l2"] = lsp_gen_interval_l2
        if lsp_refresh_interval is not None:
            data_payload["lsp-refresh-interval"] = lsp_refresh_interval
        if max_lsp_lifetime is not None:
            data_payload["max-lsp-lifetime"] = max_lsp_lifetime
        if spf_interval_exp_l1 is not None:
            data_payload["spf-interval-exp-l1"] = spf_interval_exp_l1
        if spf_interval_exp_l2 is not None:
            data_payload["spf-interval-exp-l2"] = spf_interval_exp_l2
        if dynamic_hostname is not None:
            data_payload["dynamic-hostname"] = dynamic_hostname
        if adjacency_check is not None:
            data_payload["adjacency-check"] = adjacency_check
        if adjacency_check6 is not None:
            data_payload["adjacency-check6"] = adjacency_check6
        if overload_bit is not None:
            data_payload["overload-bit"] = overload_bit
        if overload_bit_suppress is not None:
            data_payload["overload-bit-suppress"] = overload_bit_suppress
        if overload_bit_on_startup is not None:
            data_payload["overload-bit-on-startup"] = overload_bit_on_startup
        if default_originate is not None:
            data_payload["default-originate"] = default_originate
        if default_originate6 is not None:
            data_payload["default-originate6"] = default_originate6
        if metric_style is not None:
            data_payload["metric-style"] = metric_style
        if redistribute_l1 is not None:
            data_payload["redistribute-l1"] = redistribute_l1
        if redistribute_l1_list is not None:
            data_payload["redistribute-l1-list"] = redistribute_l1_list
        if redistribute_l2 is not None:
            data_payload["redistribute-l2"] = redistribute_l2
        if redistribute_l2_list is not None:
            data_payload["redistribute-l2-list"] = redistribute_l2_list
        if redistribute6_l1 is not None:
            data_payload["redistribute6-l1"] = redistribute6_l1
        if redistribute6_l1_list is not None:
            data_payload["redistribute6-l1-list"] = redistribute6_l1_list
        if redistribute6_l2 is not None:
            data_payload["redistribute6-l2"] = redistribute6_l2
        if redistribute6_l2_list is not None:
            data_payload["redistribute6-l2-list"] = redistribute6_l2_list
        if isis_net is not None:
            data_payload["isis-net"] = isis_net
        if isis_interface is not None:
            data_payload["isis-interface"] = isis_interface
        if summary_address is not None:
            data_payload["summary-address"] = summary_address
        if summary_address6 is not None:
            data_payload["summary-address6"] = summary_address6
        if redistribute is not None:
            data_payload["redistribute"] = redistribute
        if redistribute6 is not None:
            data_payload["redistribute6"] = redistribute6
        data_payload.update(kwargs)
        return self._client.put(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )
