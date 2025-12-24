"""
FortiOS CMDB - Cmdb Ftp Proxy Explicit

Configuration endpoint for managing cmdb ftp proxy explicit objects.

API Endpoints:
    GET    /cmdb/ftp-proxy/explicit
    PUT    /cmdb/ftp-proxy/explicit/{identifier}

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.ftp_proxy.explicit.get()
    >>>
    >>> # Get specific item (if supported)
    >>> item = fgt.api.cmdb.ftp_proxy.explicit.get(name="item_name")
    >>>
    >>> # Create new item (use POST)
    >>> result = fgt.api.cmdb.ftp_proxy.explicit.post(
    ...     name="new_item",
    ...     # ... additional parameters
    ... )
    >>>
    >>> # Update existing item (use PUT)
    >>> result = fgt.api.cmdb.ftp_proxy.explicit.put(
    ...     name="existing_item",
    ...     # ... parameters to update
    ... )
    >>>
    >>> # Delete item
    >>> result = fgt.api.cmdb.ftp_proxy.explicit.delete(name="item_name")

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


class Explicit:
    """
    Explicit Operations.

    Provides CRUD operations for FortiOS explicit configuration.

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
        Initialize Explicit endpoint.

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
        endpoint = "/ftp-proxy/explicit"
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
        incoming_port: str | None = None,
        incoming_ip: str | None = None,
        outgoing_ip: str | None = None,
        sec_default_action: str | None = None,
        server_data_mode: str | None = None,
        ssl: str | None = None,
        ssl_cert: list | None = None,
        ssl_dh_bits: str | None = None,
        ssl_algorithm: str | None = None,
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
            status: Enable/disable the explicit FTP proxy. (optional)
            incoming_port: Accept incoming FTP requests on one or more ports.
            (optional)
            incoming_ip: Accept incoming FTP requests from this IP address. An
            interface must have this IP address. (optional)
            outgoing_ip: Outgoing FTP requests will leave from this IP address.
            An interface must have this IP address. (optional)
            sec_default_action: Accept or deny explicit FTP proxy sessions when
            no FTP proxy firewall policy exists. (optional)
            server_data_mode: Determine mode of data session on FTP server
            side. (optional)
            ssl: Enable/disable the explicit FTPS proxy. (optional)
            ssl_cert: List of certificate names to use for SSL connections to
            this server. (optional)
            ssl_dh_bits: Bit-size of Diffie-Hellman (DH) prime used in DHE-RSA
            negotiation (default = 2048). (optional)
            ssl_algorithm: Relative strength of encryption algorithms accepted
            in negotiation. (optional)
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
        endpoint = "/ftp-proxy/explicit"
        if before is not None:
            data_payload["before"] = before
        if after is not None:
            data_payload["after"] = after
        if status is not None:
            data_payload["status"] = status
        if incoming_port is not None:
            data_payload["incoming-port"] = incoming_port
        if incoming_ip is not None:
            data_payload["incoming-ip"] = incoming_ip
        if outgoing_ip is not None:
            data_payload["outgoing-ip"] = outgoing_ip
        if sec_default_action is not None:
            data_payload["sec-default-action"] = sec_default_action
        if server_data_mode is not None:
            data_payload["server-data-mode"] = server_data_mode
        if ssl is not None:
            data_payload["ssl"] = ssl
        if ssl_cert is not None:
            data_payload["ssl-cert"] = ssl_cert
        if ssl_dh_bits is not None:
            data_payload["ssl-dh-bits"] = ssl_dh_bits
        if ssl_algorithm is not None:
            data_payload["ssl-algorithm"] = ssl_algorithm
        data_payload.update(kwargs)
        return self._client.put(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )
