"""
FortiOS CMDB - Cmdb Web Proxy Global

Configuration endpoint for managing cmdb web proxy global objects.

API Endpoints:
    GET    /cmdb/web-proxy/global_
    PUT    /cmdb/web-proxy/global_/{identifier}

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.web_proxy.global_.get()
    >>>
    >>> # Get specific item (if supported)
    >>> item = fgt.api.cmdb.web_proxy.global_.get(name="item_name")
    >>>
    >>> # Create new item (use POST)
    >>> result = fgt.api.cmdb.web_proxy.global_.post(
    ...     name="new_item",
    ...     # ... additional parameters
    ... )
    >>>
    >>> # Update existing item (use PUT)
    >>> result = fgt.api.cmdb.web_proxy.global_.put(
    ...     name="existing_item",
    ...     # ... parameters to update
    ... )
    >>>
    >>> # Delete item
    >>> result = fgt.api.cmdb.web_proxy.global_.delete(name="item_name")

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


class Global:
    """
    Global Operations.

    Provides CRUD operations for FortiOS global configuration.

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
        Initialize Global endpoint.

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
        endpoint = "/web-proxy/global"
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
        ssl_cert: str | None = None,
        ssl_ca_cert: str | None = None,
        fast_policy_match: str | None = None,
        ldap_user_cache: str | None = None,
        proxy_fqdn: str | None = None,
        max_request_length: int | None = None,
        max_message_length: int | None = None,
        http2_client_window_size: int | None = None,
        http2_server_window_size: int | None = None,
        auth_sign_timeout: int | None = None,
        strict_web_check: str | None = None,
        forward_proxy_auth: str | None = None,
        forward_server_affinity_timeout: int | None = None,
        max_waf_body_cache_length: int | None = None,
        webproxy_profile: str | None = None,
        learn_client_ip: str | None = None,
        always_learn_client_ip: str | None = None,
        learn_client_ip_from_header: str | None = None,
        learn_client_ip_srcaddr: list | None = None,
        learn_client_ip_srcaddr6: list | None = None,
        src_affinity_exempt_addr: str | None = None,
        src_affinity_exempt_addr6: str | None = None,
        policy_partial_match: str | None = None,
        log_policy_pending: str | None = None,
        log_forward_server: str | None = None,
        log_app_id: str | None = None,
        proxy_transparent_cert_inspection: str | None = None,
        request_obs_fold: str | None = None,
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
            ssl_cert: SSL certificate for SSL interception. (optional)
            ssl_ca_cert: SSL CA certificate for SSL interception. (optional)
            fast_policy_match: Enable/disable fast matching algorithm for
            explicit and transparent proxy policy. (optional)
            ldap_user_cache: Enable/disable LDAP user cache for explicit and
            transparent proxy user. (optional)
            proxy_fqdn: Fully Qualified Domain Name of the explicit web proxy
            (default = default.fqdn) that clients connect to. (optional)
            max_request_length: Maximum length of HTTP request line (2 - 64
            Kbytes, default = 8). (optional)
            max_message_length: Maximum length of HTTP message, not including
            body (16 - 256 Kbytes, default = 32). (optional)
            http2_client_window_size: HTTP/2 client initial window size in
            bytes (65535 - 2147483647, default = 1048576 (1MB)). (optional)
            http2_server_window_size: HTTP/2 server initial window size in
            bytes (65535 - 2147483647, default = 1048576 (1MB)). (optional)
            auth_sign_timeout: Proxy auth query sign timeout in seconds (30 -
            3600, default = 120). (optional)
            strict_web_check: Enable/disable strict web checking to block web
            sites that send incorrect headers that don't conform to HTTP.
            (optional)
            forward_proxy_auth: Enable/disable forwarding proxy authentication
            headers. (optional)
            forward_server_affinity_timeout: Period of time before the source
            IP's traffic is no longer assigned to the forwarding server (6 - 60
            min, default = 30). (optional)
            max_waf_body_cache_length: Maximum length of HTTP messages
            processed by Web Application Firewall (WAF) (1 - 1024 Kbytes,
            default = 1). (optional)
            webproxy_profile: Name of the web proxy profile to apply when
            explicit proxy traffic is allowed by default and traffic is
            accepted that does not match an explicit proxy policy. (optional)
            learn_client_ip: Enable/disable learning the client's IP address
            from headers. (optional)
            always_learn_client_ip: Enable/disable learning the client's IP
            address from headers for every request. (optional)
            learn_client_ip_from_header: Learn client IP address from the
            specified headers. (optional)
            learn_client_ip_srcaddr: Source address name (srcaddr or srcaddr6
            must be set). (optional)
            learn_client_ip_srcaddr6: IPv6 Source address name (srcaddr or
            srcaddr6 must be set). (optional)
            src_affinity_exempt_addr: IPv4 source addresses to exempt proxy
            affinity. (optional)
            src_affinity_exempt_addr6: IPv6 source addresses to exempt proxy
            affinity. (optional)
            policy_partial_match: Enable/disable policy partial matching.
            (optional)
            log_policy_pending: Enable/disable logging sessions that are
            pending on policy matching. (optional)
            log_forward_server: Enable/disable forward server name logging in
            forward traffic log. (optional)
            log_app_id: Enable/disable always log application type in traffic
            log. (optional)
            proxy_transparent_cert_inspection: Enable/disable transparent proxy
            certificate inspection. (optional)
            request_obs_fold: Action when HTTP/1.x request header contains
            obs-fold (default = keep). (optional)
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
        endpoint = "/web-proxy/global"
        if before is not None:
            data_payload["before"] = before
        if after is not None:
            data_payload["after"] = after
        if ssl_cert is not None:
            data_payload["ssl-cert"] = ssl_cert
        if ssl_ca_cert is not None:
            data_payload["ssl-ca-cert"] = ssl_ca_cert
        if fast_policy_match is not None:
            data_payload["fast-policy-match"] = fast_policy_match
        if ldap_user_cache is not None:
            data_payload["ldap-user-cache"] = ldap_user_cache
        if proxy_fqdn is not None:
            data_payload["proxy-fqdn"] = proxy_fqdn
        if max_request_length is not None:
            data_payload["max-request-length"] = max_request_length
        if max_message_length is not None:
            data_payload["max-message-length"] = max_message_length
        if http2_client_window_size is not None:
            data_payload["http2-client-window-size"] = http2_client_window_size
        if http2_server_window_size is not None:
            data_payload["http2-server-window-size"] = http2_server_window_size
        if auth_sign_timeout is not None:
            data_payload["auth-sign-timeout"] = auth_sign_timeout
        if strict_web_check is not None:
            data_payload["strict-web-check"] = strict_web_check
        if forward_proxy_auth is not None:
            data_payload["forward-proxy-auth"] = forward_proxy_auth
        if forward_server_affinity_timeout is not None:
            data_payload["forward-server-affinity-timeout"] = (
                forward_server_affinity_timeout
            )
        if max_waf_body_cache_length is not None:
            data_payload["max-waf-body-cache-length"] = (
                max_waf_body_cache_length
            )
        if webproxy_profile is not None:
            data_payload["webproxy-profile"] = webproxy_profile
        if learn_client_ip is not None:
            data_payload["learn-client-ip"] = learn_client_ip
        if always_learn_client_ip is not None:
            data_payload["always-learn-client-ip"] = always_learn_client_ip
        if learn_client_ip_from_header is not None:
            data_payload["learn-client-ip-from-header"] = (
                learn_client_ip_from_header
            )
        if learn_client_ip_srcaddr is not None:
            data_payload["learn-client-ip-srcaddr"] = learn_client_ip_srcaddr
        if learn_client_ip_srcaddr6 is not None:
            data_payload["learn-client-ip-srcaddr6"] = learn_client_ip_srcaddr6
        if src_affinity_exempt_addr is not None:
            data_payload["src-affinity-exempt-addr"] = src_affinity_exempt_addr
        if src_affinity_exempt_addr6 is not None:
            data_payload["src-affinity-exempt-addr6"] = (
                src_affinity_exempt_addr6
            )
        if policy_partial_match is not None:
            data_payload["policy-partial-match"] = policy_partial_match
        if log_policy_pending is not None:
            data_payload["log-policy-pending"] = log_policy_pending
        if log_forward_server is not None:
            data_payload["log-forward-server"] = log_forward_server
        if log_app_id is not None:
            data_payload["log-app-id"] = log_app_id
        if proxy_transparent_cert_inspection is not None:
            data_payload["proxy-transparent-cert-inspection"] = (
                proxy_transparent_cert_inspection
            )
        if request_obs_fold is not None:
            data_payload["request-obs-fold"] = request_obs_fold
        data_payload.update(kwargs)
        return self._client.put(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )
