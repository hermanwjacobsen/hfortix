"""
FortiOS CMDB - Cmdb System Npu

Configuration endpoint for managing cmdb system npu objects.

API Endpoints:
    GET    /cmdb/system/npu
    PUT    /cmdb/system/npu/{identifier}

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.system.npu.get()
    >>>
    >>> # Get specific item (if supported)
    >>> item = fgt.api.cmdb.system.npu.get(name="item_name")
    >>>
    >>> # Create new item (use POST)
    >>> result = fgt.api.cmdb.system.npu.post(
    ...     name="new_item",
    ...     # ... additional parameters
    ... )
    >>>
    >>> # Update existing item (use PUT)
    >>> result = fgt.api.cmdb.system.npu.put(
    ...     name="existing_item",
    ...     # ... parameters to update
    ... )
    >>>
    >>> # Delete item
    >>> result = fgt.api.cmdb.system.npu.delete(name="item_name")

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


class Npu:
    """
    Npu Operations.

    Provides CRUD operations for FortiOS npu configuration.

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
        Initialize Npu endpoint.

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
        endpoint = "/system/npu"
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
        dedicated_management_cpu: str | None = None,
        dedicated_management_affinity: str | None = None,
        capwap_offload: str | None = None,
        ipsec_mtu_override: str | None = None,
        ipsec_ordering: str | None = None,
        ipsec_enc_subengine_mask: str | None = None,
        ipsec_dec_subengine_mask: str | None = None,
        priority_protocol: list | None = None,
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
            dedicated_management_cpu: Enable to dedicate one CPU for GUI and
            CLI connections when NPs are busy. (optional)
            dedicated_management_affinity: Affinity setting for management
            daemons (hexadecimal value up to 256 bits in the format of
            xxxxxxxxxxxxxxxx). (optional)
            capwap_offload: Enable/disable offloading managed FortiAP and
            FortiLink CAPWAP sessions. (optional)
            ipsec_mtu_override: Enable/disable NP6 IPsec MTU override.
            (optional)
            ipsec_ordering: Enable/disable IPsec ordering. (optional)
            ipsec_enc_subengine_mask: IPsec encryption subengine mask (0x1 -
            0x0f, default 0x0f). (optional)
            ipsec_dec_subengine_mask: IPsec decryption subengine mask (0x1 -
            0x0f, default 0x0f). (optional)
            priority_protocol: Configure NPU priority protocol. (optional)
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
        endpoint = "/system/npu"
        if before is not None:
            data_payload["before"] = before
        if after is not None:
            data_payload["after"] = after
        if dedicated_management_cpu is not None:
            data_payload["dedicated-management-cpu"] = dedicated_management_cpu
        if dedicated_management_affinity is not None:
            data_payload["dedicated-management-affinity"] = (
                dedicated_management_affinity
            )
        if capwap_offload is not None:
            data_payload["capwap-offload"] = capwap_offload
        if ipsec_mtu_override is not None:
            data_payload["ipsec-mtu-override"] = ipsec_mtu_override
        if ipsec_ordering is not None:
            data_payload["ipsec-ordering"] = ipsec_ordering
        if ipsec_enc_subengine_mask is not None:
            data_payload["ipsec-enc-subengine-mask"] = ipsec_enc_subengine_mask
        if ipsec_dec_subengine_mask is not None:
            data_payload["ipsec-dec-subengine-mask"] = ipsec_dec_subengine_mask
        if priority_protocol is not None:
            data_payload["priority-protocol"] = priority_protocol
        data_payload.update(kwargs)
        return self._client.put(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )
