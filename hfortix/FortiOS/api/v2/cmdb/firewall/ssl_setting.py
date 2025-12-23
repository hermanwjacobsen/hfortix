"""
FortiOS CMDB - Cmdb Firewall Ssl Setting

Configuration endpoint for managing cmdb firewall ssl setting objects.

API Endpoints:
    GET    /cmdb/firewall/ssl_setting
    PUT    /cmdb/firewall/ssl_setting/{identifier}

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.firewall.ssl_setting.get()
    >>>
    >>> # Get specific item (if supported)
    >>> item = fgt.api.cmdb.firewall.ssl_setting.get(name="item_name")
    >>>
    >>> # Create new item (use POST)
    >>> result = fgt.api.cmdb.firewall.ssl_setting.post(
    ...     name="new_item",
    ...     # ... additional parameters
    ... )
    >>>
    >>> # Update existing item (use PUT)
    >>> result = fgt.api.cmdb.firewall.ssl_setting.put(
    ...     name="existing_item",
    ...     # ... parameters to update
    ... )
    >>>
    >>> # Delete item
    >>> result = fgt.api.cmdb.firewall.ssl_setting.delete(name="item_name")

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


class SslSetting:
    """
    Sslsetting Operations.

    Provides CRUD operations for FortiOS sslsetting configuration.

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
        Initialize SslSetting endpoint.

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
        endpoint = "/firewall.ssl/setting"
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
        proxy_connect_timeout: int | None = None,
        ssl_dh_bits: str | None = None,
        ssl_send_empty_frags: str | None = None,
        no_matching_cipher_action: str | None = None,
        cert_manager_cache_timeout: int | None = None,
        resigned_short_lived_certificate: str | None = None,
        cert_cache_capacity: int | None = None,
        cert_cache_timeout: int | None = None,
        session_cache_capacity: int | None = None,
        session_cache_timeout: int | None = None,
        kxp_queue_threshold: int | None = None,
        ssl_queue_threshold: int | None = None,
        abbreviate_handshake: str | None = None,
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
            proxy_connect_timeout: Time limit to make an internal connection to
            the appropriate proxy process (1 - 60 sec, default = 30).
            (optional)
            ssl_dh_bits: Bit-size of Diffie-Hellman (DH) prime used in DHE-RSA
            negotiation (default = 2048). (optional)
            ssl_send_empty_frags: Enable/disable sending empty fragments to
            avoid attack on CBC IV (for SSL 3.0 and TLS 1.0 only). (optional)
            no_matching_cipher_action: Bypass or drop the connection when no
            matching cipher is found. (optional)
            cert_manager_cache_timeout: Time limit for certificate manager to
            keep FortiGate re-signed server certificate (24 - 720 hours,
            default = 72). (optional)
            resigned_short_lived_certificate: Enable/disable short-lived
            certificate. (optional)
            cert_cache_capacity: Maximum capacity of the host certificate cache
            (0 - 500, default = 200). (optional)
            cert_cache_timeout: Time limit to keep certificate cache (1 - 120
            min, default = 10). (optional)
            session_cache_capacity: Capacity of the SSL session cache
            (--Obsolete--) (1 - 1000, default = 500). (optional)
            session_cache_timeout: Time limit to keep SSL session state (1 - 60
            min, default = 20). (optional)
            kxp_queue_threshold: Maximum length of the CP KXP queue. When the
            queue becomes full, the proxy switches cipher functions to the main
            CPU (0 - 512, default = 16). (optional)
            ssl_queue_threshold: Maximum length of the CP SSL queue. When the
            queue becomes full, the proxy switches cipher functions to the main
            CPU (0 - 512, default = 32). (optional)
            abbreviate_handshake: Enable/disable use of SSL abbreviated
            handshake. (optional)
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
        endpoint = "/firewall.ssl/setting"
        if before is not None:
            data_payload["before"] = before
        if after is not None:
            data_payload["after"] = after
        if proxy_connect_timeout is not None:
            data_payload["proxy-connect-timeout"] = proxy_connect_timeout
        if ssl_dh_bits is not None:
            data_payload["ssl-dh-bits"] = ssl_dh_bits
        if ssl_send_empty_frags is not None:
            data_payload["ssl-send-empty-frags"] = ssl_send_empty_frags
        if no_matching_cipher_action is not None:
            data_payload["no-matching-cipher-action"] = (
                no_matching_cipher_action
            )
        if cert_manager_cache_timeout is not None:
            data_payload["cert-manager-cache-timeout"] = (
                cert_manager_cache_timeout
            )
        if resigned_short_lived_certificate is not None:
            data_payload["resigned-short-lived-certificate"] = (
                resigned_short_lived_certificate
            )
        if cert_cache_capacity is not None:
            data_payload["cert-cache-capacity"] = cert_cache_capacity
        if cert_cache_timeout is not None:
            data_payload["cert-cache-timeout"] = cert_cache_timeout
        if session_cache_capacity is not None:
            data_payload["session-cache-capacity"] = session_cache_capacity
        if session_cache_timeout is not None:
            data_payload["session-cache-timeout"] = session_cache_timeout
        if kxp_queue_threshold is not None:
            data_payload["kxp-queue-threshold"] = kxp_queue_threshold
        if ssl_queue_threshold is not None:
            data_payload["ssl-queue-threshold"] = ssl_queue_threshold
        if abbreviate_handshake is not None:
            data_payload["abbreviate-handshake"] = abbreviate_handshake
        data_payload.update(kwargs)
        return self._client.put(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )
