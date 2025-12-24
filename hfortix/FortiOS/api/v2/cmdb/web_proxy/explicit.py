"""
FortiOS CMDB - Cmdb Web Proxy Explicit

Configuration endpoint for managing cmdb web proxy explicit objects.

API Endpoints:
    GET    /cmdb/web-proxy/explicit
    PUT    /cmdb/web-proxy/explicit/{identifier}

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.web_proxy.explicit.get()
    >>>
    >>> # Get specific item (if supported)
    >>> item = fgt.api.cmdb.web_proxy.explicit.get(name="item_name")
    >>>
    >>> # Create new item (use POST)
    >>> result = fgt.api.cmdb.web_proxy.explicit.post(
    ...     name="new_item",
    ...     # ... additional parameters
    ... )
    >>>
    >>> # Update existing item (use PUT)
    >>> result = fgt.api.cmdb.web_proxy.explicit.put(
    ...     name="existing_item",
    ...     # ... parameters to update
    ... )
    >>>
    >>> # Delete item
    >>> result = fgt.api.cmdb.web_proxy.explicit.delete(name="item_name")

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
        endpoint = "/web-proxy/explicit"
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
        secure_web_proxy: str | None = None,
        ftp_over_http: str | None = None,
        socks: str | None = None,
        http_incoming_port: str | None = None,
        http_connection_mode: str | None = None,
        https_incoming_port: str | None = None,
        secure_web_proxy_cert: list | None = None,
        client_cert: str | None = None,
        user_agent_detect: str | None = None,
        empty_cert_action: str | None = None,
        ssl_dh_bits: str | None = None,
        ftp_incoming_port: str | None = None,
        socks_incoming_port: str | None = None,
        incoming_ip: str | None = None,
        outgoing_ip: str | None = None,
        interface_select_method: str | None = None,
        interface: str | None = None,
        vrf_select: int | None = None,
        ipv6_status: str | None = None,
        incoming_ip6: str | None = None,
        outgoing_ip6: str | None = None,
        strict_guest: str | None = None,
        pref_dns_result: str | None = None,
        unknown_http_version: str | None = None,
        realm: str | None = None,
        sec_default_action: str | None = None,
        https_replacement_message: str | None = None,
        message_upon_server_error: str | None = None,
        pac_file_server_status: str | None = None,
        pac_file_url: str | None = None,
        pac_file_server_port: str | None = None,
        pac_file_through_https: str | None = None,
        pac_file_name: str | None = None,
        pac_file_data: str | None = None,
        pac_policy: list | None = None,
        ssl_algorithm: str | None = None,
        trace_auth_no_rsp: str | None = None,
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
            status: Enable/disable the explicit Web proxy for HTTP and HTTPS
            session. (optional)
            secure_web_proxy: Enable/disable/require the secure web proxy for
            HTTP and HTTPS session. (optional)
            ftp_over_http: Enable to proxy FTP-over-HTTP sessions sent from a
            web browser. (optional)
            socks: Enable/disable the SOCKS proxy. (optional)
            http_incoming_port: Accept incoming HTTP requests on one or more
            ports (0 - 65535, default = 8080). (optional)
            http_connection_mode: HTTP connection mode (default = static).
            (optional)
            https_incoming_port: Accept incoming HTTPS requests on one or more
            ports (0 - 65535, default = 0, use the same as HTTP). (optional)
            secure_web_proxy_cert: Name of certificates for secure web proxy.
            (optional)
            client_cert: Enable/disable to request client certificate.
            (optional)
            user_agent_detect: Enable/disable to detect device type by HTTP
            user-agent if no client certificate provided. (optional)
            empty_cert_action: Action of an empty client certificate.
            (optional)
            ssl_dh_bits: Bit-size of Diffie-Hellman (DH) prime used in DHE-RSA
            negotiation (default = 2048). (optional)
            ftp_incoming_port: Accept incoming FTP-over-HTTP requests on one or
            more ports (0 - 65535, default = 0; use the same as HTTP).
            (optional)
            socks_incoming_port: Accept incoming SOCKS proxy requests on one or
            more ports (0 - 65535, default = 0; use the same as HTTP).
            (optional)
            incoming_ip: Restrict the explicit HTTP proxy to only accept
            sessions from this IP address. An interface must have this IP
            address. (optional)
            outgoing_ip: Outgoing HTTP requests will have this IP address as
            their source address. An interface must have this IP address.
            (optional)
            interface_select_method: Specify how to select outgoing interface
            to reach server. (optional)
            interface: Specify outgoing interface to reach server. (optional)
            vrf_select: VRF ID used for connection to server. (optional)
            ipv6_status: Enable/disable allowing an IPv6 web proxy destination
            in policies and all IPv6 related entries in this command.
            (optional)
            incoming_ip6: Restrict the explicit web proxy to only accept
            sessions from this IPv6 address. An interface must have this IPv6
            address. (optional)
            outgoing_ip6: Outgoing HTTP requests will leave this IPv6. Multiple
            interfaces can be specified. Interfaces must have these IPv6
            addresses. (optional)
            strict_guest: Enable/disable strict guest user checking by the
            explicit web proxy. (optional)
            pref_dns_result: Prefer resolving addresses using the configured
            IPv4 or IPv6 DNS server (default = ipv4). (optional)
            unknown_http_version: How to handle HTTP sessions that do not
            comply with HTTP 0.9, 1.0, or 1.1. (optional)
            realm: Authentication realm used to identify the explicit web proxy
            (maximum of 63 characters). (optional)
            sec_default_action: Accept or deny explicit web proxy sessions when
            no web proxy firewall policy exists. (optional)
            https_replacement_message: Enable/disable sending the client a
            replacement message for HTTPS requests. (optional)
            message_upon_server_error: Enable/disable displaying a replacement
            message when a server error is detected. (optional)
            pac_file_server_status: Enable/disable Proxy Auto-Configuration
            (PAC) for users of this explicit proxy profile. (optional)
            pac_file_url: PAC file access URL. (optional)
            pac_file_server_port: Port number that PAC traffic from client web
            browsers uses to connect to the explicit web proxy (0 - 65535,
            default = 0; use the same as HTTP). (optional)
            pac_file_through_https: Enable/disable to get Proxy
            Auto-Configuration (PAC) through HTTPS. (optional)
            pac_file_name: Pac file name. (optional)
            pac_file_data: PAC file contents enclosed in quotes (maximum of
            256K bytes). (optional)
            pac_policy: PAC policies. (optional)
            ssl_algorithm: Relative strength of encryption algorithms accepted
            in HTTPS deep scan: high, medium, or low. (optional)
            trace_auth_no_rsp: Enable/disable logging timed-out authentication
            requests. (optional)
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
        endpoint = "/web-proxy/explicit"
        if before is not None:
            data_payload["before"] = before
        if after is not None:
            data_payload["after"] = after
        if status is not None:
            data_payload["status"] = status
        if secure_web_proxy is not None:
            data_payload["secure-web-proxy"] = secure_web_proxy
        if ftp_over_http is not None:
            data_payload["ftp-over-http"] = ftp_over_http
        if socks is not None:
            data_payload["socks"] = socks
        if http_incoming_port is not None:
            data_payload["http-incoming-port"] = http_incoming_port
        if http_connection_mode is not None:
            data_payload["http-connection-mode"] = http_connection_mode
        if https_incoming_port is not None:
            data_payload["https-incoming-port"] = https_incoming_port
        if secure_web_proxy_cert is not None:
            data_payload["secure-web-proxy-cert"] = secure_web_proxy_cert
        if client_cert is not None:
            data_payload["client-cert"] = client_cert
        if user_agent_detect is not None:
            data_payload["user-agent-detect"] = user_agent_detect
        if empty_cert_action is not None:
            data_payload["empty-cert-action"] = empty_cert_action
        if ssl_dh_bits is not None:
            data_payload["ssl-dh-bits"] = ssl_dh_bits
        if ftp_incoming_port is not None:
            data_payload["ftp-incoming-port"] = ftp_incoming_port
        if socks_incoming_port is not None:
            data_payload["socks-incoming-port"] = socks_incoming_port
        if incoming_ip is not None:
            data_payload["incoming-ip"] = incoming_ip
        if outgoing_ip is not None:
            data_payload["outgoing-ip"] = outgoing_ip
        if interface_select_method is not None:
            data_payload["interface-select-method"] = interface_select_method
        if interface is not None:
            data_payload["interface"] = interface
        if vrf_select is not None:
            data_payload["vrf-select"] = vrf_select
        if ipv6_status is not None:
            data_payload["ipv6-status"] = ipv6_status
        if incoming_ip6 is not None:
            data_payload["incoming-ip6"] = incoming_ip6
        if outgoing_ip6 is not None:
            data_payload["outgoing-ip6"] = outgoing_ip6
        if strict_guest is not None:
            data_payload["strict-guest"] = strict_guest
        if pref_dns_result is not None:
            data_payload["pref-dns-result"] = pref_dns_result
        if unknown_http_version is not None:
            data_payload["unknown-http-version"] = unknown_http_version
        if realm is not None:
            data_payload["realm"] = realm
        if sec_default_action is not None:
            data_payload["sec-default-action"] = sec_default_action
        if https_replacement_message is not None:
            data_payload["https-replacement-message"] = (
                https_replacement_message
            )
        if message_upon_server_error is not None:
            data_payload["message-upon-server-error"] = (
                message_upon_server_error
            )
        if pac_file_server_status is not None:
            data_payload["pac-file-server-status"] = pac_file_server_status
        if pac_file_url is not None:
            data_payload["pac-file-url"] = pac_file_url
        if pac_file_server_port is not None:
            data_payload["pac-file-server-port"] = pac_file_server_port
        if pac_file_through_https is not None:
            data_payload["pac-file-through-https"] = pac_file_through_https
        if pac_file_name is not None:
            data_payload["pac-file-name"] = pac_file_name
        if pac_file_data is not None:
            data_payload["pac-file-data"] = pac_file_data
        if pac_policy is not None:
            data_payload["pac-policy"] = pac_policy
        if ssl_algorithm is not None:
            data_payload["ssl-algorithm"] = ssl_algorithm
        if trace_auth_no_rsp is not None:
            data_payload["trace-auth-no-rsp"] = trace_auth_no_rsp
        data_payload.update(kwargs)
        return self._client.put(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )
