"""
FortiOS CMDB - Cmdb Authentication Setting

Configuration endpoint for managing cmdb authentication setting objects.

API Endpoints:
    GET    /cmdb/authentication/setting
    PUT    /cmdb/authentication/setting/{identifier}

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.authentication.setting.get()
    >>>
    >>> # Get specific item (if supported)
    >>> item = fgt.api.cmdb.authentication.setting.get(name="item_name")
    >>>
    >>> # Create new item (use POST)
    >>> result = fgt.api.cmdb.authentication.setting.post(
    ...     name="new_item",
    ...     # ... additional parameters
    ... )
    >>>
    >>> # Update existing item (use PUT)
    >>> result = fgt.api.cmdb.authentication.setting.put(
    ...     name="existing_item",
    ...     # ... parameters to update
    ... )
    >>>
    >>> # Delete item
    >>> result = fgt.api.cmdb.authentication.setting.delete(name="item_name")

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


class Setting:
    """
    Setting Operations.

    Provides CRUD operations for FortiOS setting configuration.

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
        Initialize Setting endpoint.

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
        endpoint = "/authentication/setting"
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
        active_auth_scheme: str | None = None,
        sso_auth_scheme: str | None = None,
        update_time: str | None = None,
        persistent_cookie: str | None = None,
        ip_auth_cookie: str | None = None,
        cookie_max_age: int | None = None,
        cookie_refresh_div: int | None = None,
        captive_portal_type: str | None = None,
        captive_portal_ip: str | None = None,
        captive_portal_ip6: str | None = None,
        captive_portal: str | None = None,
        captive_portal6: str | None = None,
        cert_auth: str | None = None,
        cert_captive_portal: str | None = None,
        cert_captive_portal_ip: str | None = None,
        cert_captive_portal_port: int | None = None,
        captive_portal_port: int | None = None,
        auth_https: str | None = None,
        captive_portal_ssl_port: int | None = None,
        user_cert_ca: list | None = None,
        dev_range: list | None = None,
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
            active_auth_scheme: Active authentication method (scheme name).
            (optional)
            sso_auth_scheme: Single-Sign-On authentication method (scheme
            name). (optional)
            update_time: Time of the last update. (optional)
            persistent_cookie: Enable/disable persistent cookie on web portal
            authentication (default = enable). (optional)
            ip_auth_cookie: Enable/disable persistent cookie on IP based web
            portal authentication (default = disable). (optional)
            cookie_max_age: Persistent web portal cookie maximum age in minutes
            (30 - 10080 (1 week), default = 480 (8 hours)). (optional)
            cookie_refresh_div: Refresh rate divider of persistent web portal
            cookie (default = 2). Refresh value =
            cookie-max-age/cookie-refresh-div. (optional)
            captive_portal_type: Captive portal type. (optional)
            captive_portal_ip: Captive portal IP address. (optional)
            captive_portal_ip6: Captive portal IPv6 address. (optional)
            captive_portal: Captive portal host name. (optional)
            captive_portal6: IPv6 captive portal host name. (optional)
            cert_auth: Enable/disable redirecting certificate authentication to
            HTTPS portal. (optional)
            cert_captive_portal: Certificate captive portal host name.
            (optional)
            cert_captive_portal_ip: Certificate captive portal IP address.
            (optional)
            cert_captive_portal_port: Certificate captive portal port number (1
            - 65535, default = 7832). (optional)
            captive_portal_port: Captive portal port number (1 - 65535, default
            = 7830). (optional)
            auth_https: Enable/disable redirecting HTTP user authentication to
            HTTPS. (optional)
            captive_portal_ssl_port: Captive portal SSL port number (1 - 65535,
            default = 7831). (optional)
            user_cert_ca: CA certificate used for client certificate
            verification. (optional)
            dev_range: Address range for the IP based device query. (optional)
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
        endpoint = "/authentication/setting"
        if before is not None:
            data_payload["before"] = before
        if after is not None:
            data_payload["after"] = after
        if active_auth_scheme is not None:
            data_payload["active-auth-scheme"] = active_auth_scheme
        if sso_auth_scheme is not None:
            data_payload["sso-auth-scheme"] = sso_auth_scheme
        if update_time is not None:
            data_payload["update-time"] = update_time
        if persistent_cookie is not None:
            data_payload["persistent-cookie"] = persistent_cookie
        if ip_auth_cookie is not None:
            data_payload["ip-auth-cookie"] = ip_auth_cookie
        if cookie_max_age is not None:
            data_payload["cookie-max-age"] = cookie_max_age
        if cookie_refresh_div is not None:
            data_payload["cookie-refresh-div"] = cookie_refresh_div
        if captive_portal_type is not None:
            data_payload["captive-portal-type"] = captive_portal_type
        if captive_portal_ip is not None:
            data_payload["captive-portal-ip"] = captive_portal_ip
        if captive_portal_ip6 is not None:
            data_payload["captive-portal-ip6"] = captive_portal_ip6
        if captive_portal is not None:
            data_payload["captive-portal"] = captive_portal
        if captive_portal6 is not None:
            data_payload["captive-portal6"] = captive_portal6
        if cert_auth is not None:
            data_payload["cert-auth"] = cert_auth
        if cert_captive_portal is not None:
            data_payload["cert-captive-portal"] = cert_captive_portal
        if cert_captive_portal_ip is not None:
            data_payload["cert-captive-portal-ip"] = cert_captive_portal_ip
        if cert_captive_portal_port is not None:
            data_payload["cert-captive-portal-port"] = cert_captive_portal_port
        if captive_portal_port is not None:
            data_payload["captive-portal-port"] = captive_portal_port
        if auth_https is not None:
            data_payload["auth-https"] = auth_https
        if captive_portal_ssl_port is not None:
            data_payload["captive-portal-ssl-port"] = captive_portal_ssl_port
        if user_cert_ca is not None:
            data_payload["user-cert-ca"] = user_cert_ca
        if dev_range is not None:
            data_payload["dev-range"] = dev_range
        data_payload.update(kwargs)
        return self._client.put(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )
