"""
FortiOS CMDB - Cmdb System Fortisandbox

Configuration endpoint for managing cmdb system fortisandbox objects.

API Endpoints:
    GET    /cmdb/system/fortisandbox
    PUT    /cmdb/system/fortisandbox/{identifier}

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.system.fortisandbox.get()
    >>>
    >>> # Get specific item (if supported)
    >>> item = fgt.api.cmdb.system.fortisandbox.get(name="item_name")
    >>>
    >>> # Create new item (use POST)
    >>> result = fgt.api.cmdb.system.fortisandbox.post(
    ...     name="new_item",
    ...     # ... additional parameters
    ... )
    >>>
    >>> # Update existing item (use PUT)
    >>> result = fgt.api.cmdb.system.fortisandbox.put(
    ...     name="existing_item",
    ...     # ... parameters to update
    ... )
    >>>
    >>> # Delete item
    >>> result = fgt.api.cmdb.system.fortisandbox.delete(name="item_name")

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


class Fortisandbox:
    """
    Fortisandbox Operations.

    Provides CRUD operations for FortiOS fortisandbox configuration.

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
        Initialize Fortisandbox endpoint.

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
        endpoint = "/system/fortisandbox"
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
        status: str | None = None,
        forticloud: str | None = None,
        server: str | None = None,
        source_ip: str | None = None,
        interface_select_method: str | None = None,
        interface: str | None = None,
        vrf_select: int | None = None,
        enc_algorithm: str | None = None,
        ssl_min_proto_version: str | None = None,
        email: str | None = None,
        ca: str | None = None,
        cn: str | None = None,
        certificate_verification: str | None = None,
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
            status: Enable/disable FortiSandbox. (optional)
            forticloud: Enable/disable FortiSandbox Cloud. (optional)
            server: Server IP address or FQDN of the remote FortiSandbox.
            (optional)
            source_ip: Source IP address for communications to FortiSandbox.
            (optional)
            interface_select_method: Specify how to select outgoing interface
            to reach server. (optional)
            interface: Specify outgoing interface to reach server. (optional)
            vrf_select: VRF ID used for connection to server. (optional)
            enc_algorithm: Configure the level of SSL protection for secure
            communication with FortiSandbox. (optional)
            ssl_min_proto_version: Minimum supported protocol version for
            SSL/TLS connections (default is to follow system global setting).
            (optional)
            email: Notifier email address. (optional)
            ca: The CA that signs remote FortiSandbox certificate, empty for no
            check. (optional)
            cn: The CN of remote server certificate, case sensitive, empty for
            no check. (optional)
            certificate_verification: Enable/disable identity verification of
            FortiSandbox by use of certificate. (optional)
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
        endpoint = "/system/fortisandbox"
        if before is not None:
            data_payload["before"] = before
        if after is not None:
            data_payload["after"] = after
        if status is not None:
            data_payload["status"] = status
        if forticloud is not None:
            data_payload["forticloud"] = forticloud
        if server is not None:
            data_payload["server"] = server
        if source_ip is not None:
            data_payload["source-ip"] = source_ip
        if interface_select_method is not None:
            data_payload["interface-select-method"] = interface_select_method
        if interface is not None:
            data_payload["interface"] = interface
        if vrf_select is not None:
            data_payload["vrf-select"] = vrf_select
        if enc_algorithm is not None:
            data_payload["enc-algorithm"] = enc_algorithm
        if ssl_min_proto_version is not None:
            data_payload["ssl-min-proto-version"] = ssl_min_proto_version
        if email is not None:
            data_payload["email"] = email
        if ca is not None:
            data_payload["ca"] = ca
        if cn is not None:
            data_payload["cn"] = cn
        if certificate_verification is not None:
            data_payload["certificate-verification"] = certificate_verification
        data_payload.update(kwargs)
        return self._client.put(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )
