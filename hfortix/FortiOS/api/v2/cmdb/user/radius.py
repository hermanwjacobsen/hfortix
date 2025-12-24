"""
FortiOS CMDB - Cmdb User Radius

Configuration endpoint for managing cmdb user radius objects.

API Endpoints:
    GET    /cmdb/user/radius
    POST   /cmdb/user/radius
    GET    /cmdb/user/radius
    PUT    /cmdb/user/radius/{identifier}
    DELETE /cmdb/user/radius/{identifier}

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.user.radius.get()
    >>>
    >>> # Get specific item (if supported)
    >>> item = fgt.api.cmdb.user.radius.get(name="item_name")
    >>>
    >>> # Create new item (use POST)
    >>> result = fgt.api.cmdb.user.radius.post(
    ...     name="new_item",
    ...     # ... additional parameters
    ... )
    >>>
    >>> # Update existing item (use PUT)
    >>> result = fgt.api.cmdb.user.radius.put(
    ...     name="existing_item",
    ...     # ... parameters to update
    ... )
    >>>
    >>> # Delete item
    >>> result = fgt.api.cmdb.user.radius.delete(name="item_name")

Important:
    - Use **POST** to create new objects (404 error if already exists)
    - Use **PUT** to update existing objects (404 error if doesn't exist)
    - Use **GET** to retrieve configuration (no changes made)
    - Use **DELETE** to remove objects (404 error if doesn't exist)
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Union, cast

if TYPE_CHECKING:
    from collections.abc import Coroutine

    from hfortix.FortiOS.http_client_interface import IHTTPClient


class Radius:
    """
    Radius Operations.

    Provides CRUD operations for FortiOS radius configuration.

    Methods:
        get(): Retrieve configuration objects
        post(): Create new configuration objects
        put(): Update existing configuration objects
        delete(): Remove configuration objects

    Important:
        - POST creates new objects (404 if name already exists)
        - PUT updates existing objects (404 if name doesn't exist)
        - GET retrieves objects without making changes
        - DELETE removes objects (404 if name doesn't exist)
    """

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Radius endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

    def get(
        self,
        name: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        attr: str | None = None,
        skip_to_datasource: dict | None = None,
        acs: int | None = None,
        search: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Select a specific entry from a CLI table.

        Args:
            name: Object identifier (optional for list, required for specific)
            attr: Attribute name that references other table (optional)
            skip_to_datasource: Skip to provided table's Nth entry. E.g
            {datasource: 'firewall.address', pos: 10, global_entry: false}
            (optional)
            acs: If true, returned result are in ascending order. (optional)
            search: If present, the objects will be filtered by the search
            value. (optional)
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

        # Build endpoint path
        if name:
            endpoint = f"/user/radius/{name}"
        else:
            endpoint = "/user/radius"
        if attr is not None:
            params["attr"] = attr
        if skip_to_datasource is not None:
            params["skip_to_datasource"] = skip_to_datasource
        if acs is not None:
            params["acs"] = acs
        if search is not None:
            params["search"] = search
        params.update(kwargs)
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )

    def put(
        self,
        name: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        before: str | None = None,
        after: str | None = None,
        server: str | None = None,
        secret: str | None = None,
        secondary_server: str | None = None,
        secondary_secret: str | None = None,
        tertiary_server: str | None = None,
        tertiary_secret: str | None = None,
        timeout: int | None = None,
        status_ttl: int | None = None,
        all_usergroup: str | None = None,
        use_management_vdom: str | None = None,
        switch_controller_nas_ip_dynamic: str | None = None,
        nas_ip: str | None = None,
        nas_id_type: str | None = None,
        call_station_id_type: str | None = None,
        nas_id: str | None = None,
        acct_interim_interval: int | None = None,
        radius_coa: str | None = None,
        radius_port: int | None = None,
        h3c_compatibility: str | None = None,
        auth_type: str | None = None,
        source_ip: str | None = None,
        source_ip_interface: str | None = None,
        username_case_sensitive: str | None = None,
        group_override_attr_type: str | None = None,
        class_: list | None = None,
        password_renewal: str | None = None,
        require_message_authenticator: str | None = None,
        password_encoding: str | None = None,
        mac_username_delimiter: str | None = None,
        mac_password_delimiter: str | None = None,
        mac_case: str | None = None,
        acct_all_servers: str | None = None,
        switch_controller_acct_fast_framedip_detect: int | None = None,
        interface_select_method: str | None = None,
        interface: str | None = None,
        vrf_select: int | None = None,
        switch_controller_service_type: str | None = None,
        transport_protocol: str | None = None,
        tls_min_proto_version: str | None = None,
        ca_cert: str | None = None,
        client_cert: str | None = None,
        server_identity_check: str | None = None,
        account_key_processing: str | None = None,
        account_key_cert_field: str | None = None,
        rsso: str | None = None,
        rsso_radius_server_port: int | None = None,
        rsso_radius_response: str | None = None,
        rsso_validate_request_secret: str | None = None,
        rsso_secret: str | None = None,
        rsso_endpoint_attribute: str | None = None,
        rsso_endpoint_block_attribute: str | None = None,
        sso_attribute: str | None = None,
        sso_attribute_key: str | None = None,
        sso_attribute_value_override: str | None = None,
        rsso_context_timeout: int | None = None,
        rsso_log_period: int | None = None,
        rsso_log_flags: str | None = None,
        rsso_flush_ip_session: str | None = None,
        rsso_ep_one_ip_only: str | None = None,
        delimiter: str | None = None,
        accounting_server: list | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update this specific resource.

        Args:
            payload_dict: Optional dictionary of all parameters (can be passed
            as first positional arg)
            name: Object identifier (required)
            before: If *action=move*, use *before* to specify the ID of the
            resource that this resource will be moved before. (optional)
            after: If *action=move*, use *after* to specify the ID of the
            resource that this resource will be moved after. (optional)
            name: RADIUS server entry name. (optional)
            server: Primary RADIUS server CN domain name or IP address.
            (optional)
            secret: Pre-shared secret key used to access the primary RADIUS
            server. (optional)
            secondary_server: Secondary RADIUS CN domain name or IP address.
            (optional)
            secondary_secret: Secret key to access the secondary server.
            (optional)
            tertiary_server: Tertiary RADIUS CN domain name or IP address.
            (optional)
            tertiary_secret: Secret key to access the tertiary server.
            (optional)
            timeout: Time in seconds to retry connecting server. (optional)
            status_ttl: Time for which server reachability is cached so that
            when a server is unreachable, it will not be retried for at least
            this period of time (0 = cache disabled, default = 300). (optional)
            all_usergroup: Enable/disable automatically including this RADIUS
            server in all user groups. (optional)
            use_management_vdom: Enable/disable using management VDOM to send
            requests. (optional)
            switch_controller_nas_ip_dynamic: Enable/Disable switch-controller
            nas-ip dynamic to dynamically set nas-ip. (optional)
            nas_ip: IP address used to communicate with the RADIUS server and
            used as NAS-IP-Address and Called-Station-ID attributes. (optional)
            nas_id_type: NAS identifier type configuration (default = legacy).
            (optional)
            call_station_id_type: Calling & Called station identifier type
            configuration (default = legacy), this option is not available for
            802.1x authentication. (optional)
            nas_id: Custom NAS identifier. (optional)
            acct_interim_interval: Time in seconds between each accounting
            interim update message. (optional)
            radius_coa: Enable to allow a mechanism to change the attributes of
            an authentication, authorization, and accounting session after it
            is authenticated. (optional)
            radius_port: RADIUS service port number. (optional)
            h3c_compatibility: Enable/disable compatibility with the H3C, a
            mechanism that performs security checking for authentication.
            (optional)
            auth_type: Authentication methods/protocols permitted for this
            RADIUS server. (optional)
            source_ip: Source IP address for communications to the RADIUS
            server. (optional)
            source_ip_interface: Source interface for communication with the
            RADIUS server. (optional)
            username_case_sensitive: Enable/disable case sensitive user names.
            (optional)
            group_override_attr_type: RADIUS attribute type to override user
            group information. (optional)
            class_: Class attribute name(s). (optional)
            password_renewal: Enable/disable password renewal. (optional)
            require_message_authenticator: Require message authenticator in
            authentication response. (optional)
            password_encoding: Password encoding. (optional)
            mac_username_delimiter: MAC authentication username delimiter
            (default = hyphen). (optional)
            mac_password_delimiter: MAC authentication password delimiter
            (default = hyphen). (optional)
            mac_case: MAC authentication case (default = lowercase). (optional)
            acct_all_servers: Enable/disable sending of accounting messages to
            all configured servers (default = disable). (optional)
            switch_controller_acct_fast_framedip_detect: Switch controller
            accounting message Framed-IP detection from DHCP snooping (seconds,
            default=2). (optional)
            interface_select_method: Specify how to select outgoing interface
            to reach server. (optional)
            interface: Specify outgoing interface to reach server. (optional)
            vrf_select: VRF ID used for connection to server. (optional)
            switch_controller_service_type: RADIUS service type. (optional)
            transport_protocol: Transport protocol to be used (default = udp).
            (optional)
            tls_min_proto_version: Minimum supported protocol version for TLS
            connections (default is to follow system global setting).
            (optional)
            ca_cert: CA of server to trust under TLS. (optional)
            client_cert: Client certificate to use under TLS. (optional)
            server_identity_check: Enable/disable RADIUS server identity check
            (verify server domain name/IP address against the server
            certificate). (optional)
            account_key_processing: Account key processing operation. The
            FortiGate will keep either the whole domain or strip the domain
            from the subject identity. (optional)
            account_key_cert_field: Define subject identity field in
            certificate for user access right checking. (optional)
            rsso: Enable/disable RADIUS based single sign on feature.
            (optional)
            rsso_radius_server_port: UDP port to listen on for RADIUS Start and
            Stop records. (optional)
            rsso_radius_response: Enable/disable sending RADIUS response
            packets after receiving Start and Stop records. (optional)
            rsso_validate_request_secret: Enable/disable validating the RADIUS
            request shared secret in the Start or End record. (optional)
            rsso_secret: RADIUS secret used by the RADIUS accounting server.
            (optional)
            rsso_endpoint_attribute: RADIUS attributes used to extract the user
            end point identifier from the RADIUS Start record. (optional)
            rsso_endpoint_block_attribute: RADIUS attributes used to block a
            user. (optional)
            sso_attribute: RADIUS attribute that contains the profile group
            name to be extracted from the RADIUS Start record. (optional)
            sso_attribute_key: Key prefix for SSO group value in the SSO
            attribute. (optional)
            sso_attribute_value_override: Enable/disable override old attribute
            value with new value for the same endpoint. (optional)
            rsso_context_timeout: Time in seconds before the logged out user is
            removed from the "user context list" of logged on users. (optional)
            rsso_log_period: Time interval in seconds that group event log
            messages will be generated for dynamic profile events. (optional)
            rsso_log_flags: Events to log. (optional)
            rsso_flush_ip_session: Enable/disable flushing user IP sessions on
            RADIUS accounting Stop messages. (optional)
            rsso_ep_one_ip_only: Enable/disable the replacement of old IP
            addresses with new ones for the same endpoint on RADIUS accounting
            Start messages. (optional)
            delimiter: Configure delimiter to be used for separating profile
            group names in the SSO attribute (default = plus character "+").
            (optional)
            accounting_server: Additional accounting servers. (optional)
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

        # Build endpoint path
        if not name:
            raise ValueError("name is required for put()")
        endpoint = f"/user/radius/{name}"
        if before is not None:
            data_payload["before"] = before
        if after is not None:
            data_payload["after"] = after
        if name is not None:
            data_payload["name"] = name
        if server is not None:
            data_payload["server"] = server
        if secret is not None:
            data_payload["secret"] = secret
        if secondary_server is not None:
            data_payload["secondary-server"] = secondary_server
        if secondary_secret is not None:
            data_payload["secondary-secret"] = secondary_secret
        if tertiary_server is not None:
            data_payload["tertiary-server"] = tertiary_server
        if tertiary_secret is not None:
            data_payload["tertiary-secret"] = tertiary_secret
        if timeout is not None:
            data_payload["timeout"] = timeout
        if status_ttl is not None:
            data_payload["status-ttl"] = status_ttl
        if all_usergroup is not None:
            data_payload["all-usergroup"] = all_usergroup
        if use_management_vdom is not None:
            data_payload["use-management-vdom"] = use_management_vdom
        if switch_controller_nas_ip_dynamic is not None:
            data_payload["switch-controller-nas-ip-dynamic"] = (
                switch_controller_nas_ip_dynamic
            )
        if nas_ip is not None:
            data_payload["nas-ip"] = nas_ip
        if nas_id_type is not None:
            data_payload["nas-id-type"] = nas_id_type
        if call_station_id_type is not None:
            data_payload["call-station-id-type"] = call_station_id_type
        if nas_id is not None:
            data_payload["nas-id"] = nas_id
        if acct_interim_interval is not None:
            data_payload["acct-interim-interval"] = acct_interim_interval
        if radius_coa is not None:
            data_payload["radius-coa"] = radius_coa
        if radius_port is not None:
            data_payload["radius-port"] = radius_port
        if h3c_compatibility is not None:
            data_payload["h3c-compatibility"] = h3c_compatibility
        if auth_type is not None:
            data_payload["auth-type"] = auth_type
        if source_ip is not None:
            data_payload["source-ip"] = source_ip
        if source_ip_interface is not None:
            data_payload["source-ip-interface"] = source_ip_interface
        if username_case_sensitive is not None:
            data_payload["username-case-sensitive"] = username_case_sensitive
        if group_override_attr_type is not None:
            data_payload["group-override-attr-type"] = group_override_attr_type
        if class_ is not None:
            data_payload["class"] = class_
        if password_renewal is not None:
            data_payload["password-renewal"] = password_renewal
        if require_message_authenticator is not None:
            data_payload["require-message-authenticator"] = (
                require_message_authenticator
            )
        if password_encoding is not None:
            data_payload["password-encoding"] = password_encoding
        if mac_username_delimiter is not None:
            data_payload["mac-username-delimiter"] = mac_username_delimiter
        if mac_password_delimiter is not None:
            data_payload["mac-password-delimiter"] = mac_password_delimiter
        if mac_case is not None:
            data_payload["mac-case"] = mac_case
        if acct_all_servers is not None:
            data_payload["acct-all-servers"] = acct_all_servers
        if switch_controller_acct_fast_framedip_detect is not None:
            data_payload["switch-controller-acct-fast-framedip-detect"] = (
                switch_controller_acct_fast_framedip_detect
            )
        if interface_select_method is not None:
            data_payload["interface-select-method"] = interface_select_method
        if interface is not None:
            data_payload["interface"] = interface
        if vrf_select is not None:
            data_payload["vrf-select"] = vrf_select
        if switch_controller_service_type is not None:
            data_payload["switch-controller-service-type"] = (
                switch_controller_service_type
            )
        if transport_protocol is not None:
            data_payload["transport-protocol"] = transport_protocol
        if tls_min_proto_version is not None:
            data_payload["tls-min-proto-version"] = tls_min_proto_version
        if ca_cert is not None:
            data_payload["ca-cert"] = ca_cert
        if client_cert is not None:
            data_payload["client-cert"] = client_cert
        if server_identity_check is not None:
            data_payload["server-identity-check"] = server_identity_check
        if account_key_processing is not None:
            data_payload["account-key-processing"] = account_key_processing
        if account_key_cert_field is not None:
            data_payload["account-key-cert-field"] = account_key_cert_field
        if rsso is not None:
            data_payload["rsso"] = rsso
        if rsso_radius_server_port is not None:
            data_payload["rsso-radius-server-port"] = rsso_radius_server_port
        if rsso_radius_response is not None:
            data_payload["rsso-radius-response"] = rsso_radius_response
        if rsso_validate_request_secret is not None:
            data_payload["rsso-validate-request-secret"] = (
                rsso_validate_request_secret
            )
        if rsso_secret is not None:
            data_payload["rsso-secret"] = rsso_secret
        if rsso_endpoint_attribute is not None:
            data_payload["rsso-endpoint-attribute"] = rsso_endpoint_attribute
        if rsso_endpoint_block_attribute is not None:
            data_payload["rsso-endpoint-block-attribute"] = (
                rsso_endpoint_block_attribute
            )
        if sso_attribute is not None:
            data_payload["sso-attribute"] = sso_attribute
        if sso_attribute_key is not None:
            data_payload["sso-attribute-key"] = sso_attribute_key
        if sso_attribute_value_override is not None:
            data_payload["sso-attribute-value-override"] = (
                sso_attribute_value_override
            )
        if rsso_context_timeout is not None:
            data_payload["rsso-context-timeout"] = rsso_context_timeout
        if rsso_log_period is not None:
            data_payload["rsso-log-period"] = rsso_log_period
        if rsso_log_flags is not None:
            data_payload["rsso-log-flags"] = rsso_log_flags
        if rsso_flush_ip_session is not None:
            data_payload["rsso-flush-ip-session"] = rsso_flush_ip_session
        if rsso_ep_one_ip_only is not None:
            data_payload["rsso-ep-one-ip-only"] = rsso_ep_one_ip_only
        if delimiter is not None:
            data_payload["delimiter"] = delimiter
        if accounting_server is not None:
            data_payload["accounting-server"] = accounting_server
        data_payload.update(kwargs)
        return self._client.put(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )

    def delete(
        self,
        name: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Delete this specific resource.

        Args:
            name: Object identifier (required)
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

        # Build endpoint path
        if not name:
            raise ValueError("name is required for delete()")
        endpoint = f"/user/radius/{name}"
        params.update(kwargs)
        return self._client.delete(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )

    def exists(
        self,
        name: str,
        vdom: str | bool | None = None,
    ) -> Union[bool, Coroutine[Any, Any, bool]]:
        """
        Check if an object exists.

        Args:
            name: Object identifier
            vdom: Virtual domain name, or False to skip. Handled by HTTPClient.

        Returns:
            True if object exists, False otherwise

        Example:
            >>> if fgt.api.cmdb.firewall.address.exists("server1"):
            ...     print("Address exists")
        """
        import inspect

        from hfortix.FortiOS.exceptions_forti import ResourceNotFoundError

        # Call get() - returns dict (sync) or coroutine (async)
        result = self.get(name=name, vdom=vdom)

        # Check if async mode
        if inspect.iscoroutine(result):

            async def _async():
                try:
                    # Runtime check confirms result is a coroutine, cast for
                    # mypy
                    await cast(Coroutine[Any, Any, dict[str, Any]], result)
                    return True
                except ResourceNotFoundError:
                    return False

            # Type ignore justified: mypy can't verify Union return type
            # narrowing

            return _async()
        # Sync mode - get() already executed, no exception means it exists
        return True

    def post(
        self,
        payload_dict: dict[str, Any] | None = None,
        nkey: str | None = None,
        name: str | None = None,
        server: str | None = None,
        secret: str | None = None,
        secondary_server: str | None = None,
        secondary_secret: str | None = None,
        tertiary_server: str | None = None,
        tertiary_secret: str | None = None,
        timeout: int | None = None,
        status_ttl: int | None = None,
        all_usergroup: str | None = None,
        use_management_vdom: str | None = None,
        switch_controller_nas_ip_dynamic: str | None = None,
        nas_ip: str | None = None,
        nas_id_type: str | None = None,
        call_station_id_type: str | None = None,
        nas_id: str | None = None,
        acct_interim_interval: int | None = None,
        radius_coa: str | None = None,
        radius_port: int | None = None,
        h3c_compatibility: str | None = None,
        auth_type: str | None = None,
        source_ip: str | None = None,
        source_ip_interface: str | None = None,
        username_case_sensitive: str | None = None,
        group_override_attr_type: str | None = None,
        class_: list | None = None,
        password_renewal: str | None = None,
        require_message_authenticator: str | None = None,
        password_encoding: str | None = None,
        mac_username_delimiter: str | None = None,
        mac_password_delimiter: str | None = None,
        mac_case: str | None = None,
        acct_all_servers: str | None = None,
        switch_controller_acct_fast_framedip_detect: int | None = None,
        interface_select_method: str | None = None,
        interface: str | None = None,
        vrf_select: int | None = None,
        switch_controller_service_type: str | None = None,
        transport_protocol: str | None = None,
        tls_min_proto_version: str | None = None,
        ca_cert: str | None = None,
        client_cert: str | None = None,
        server_identity_check: str | None = None,
        account_key_processing: str | None = None,
        account_key_cert_field: str | None = None,
        rsso: str | None = None,
        rsso_radius_server_port: int | None = None,
        rsso_radius_response: str | None = None,
        rsso_validate_request_secret: str | None = None,
        rsso_secret: str | None = None,
        rsso_endpoint_attribute: str | None = None,
        rsso_endpoint_block_attribute: str | None = None,
        sso_attribute: str | None = None,
        sso_attribute_key: str | None = None,
        sso_attribute_value_override: str | None = None,
        rsso_context_timeout: int | None = None,
        rsso_log_period: int | None = None,
        rsso_log_flags: str | None = None,
        rsso_flush_ip_session: str | None = None,
        rsso_ep_one_ip_only: str | None = None,
        delimiter: str | None = None,
        accounting_server: list | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Create object(s) in this table.

        Args:
            payload_dict: Optional dictionary of all parameters (can be passed
            as first positional arg)
            nkey: If *action=clone*, use *nkey* to specify the ID for the new
            resource to be created. (optional)
            name: RADIUS server entry name. (optional)
            server: Primary RADIUS server CN domain name or IP address.
            (optional)
            secret: Pre-shared secret key used to access the primary RADIUS
            server. (optional)
            secondary_server: Secondary RADIUS CN domain name or IP address.
            (optional)
            secondary_secret: Secret key to access the secondary server.
            (optional)
            tertiary_server: Tertiary RADIUS CN domain name or IP address.
            (optional)
            tertiary_secret: Secret key to access the tertiary server.
            (optional)
            timeout: Time in seconds to retry connecting server. (optional)
            status_ttl: Time for which server reachability is cached so that
            when a server is unreachable, it will not be retried for at least
            this period of time (0 = cache disabled, default = 300). (optional)
            all_usergroup: Enable/disable automatically including this RADIUS
            server in all user groups. (optional)
            use_management_vdom: Enable/disable using management VDOM to send
            requests. (optional)
            switch_controller_nas_ip_dynamic: Enable/Disable switch-controller
            nas-ip dynamic to dynamically set nas-ip. (optional)
            nas_ip: IP address used to communicate with the RADIUS server and
            used as NAS-IP-Address and Called-Station-ID attributes. (optional)
            nas_id_type: NAS identifier type configuration (default = legacy).
            (optional)
            call_station_id_type: Calling & Called station identifier type
            configuration (default = legacy), this option is not available for
            802.1x authentication. (optional)
            nas_id: Custom NAS identifier. (optional)
            acct_interim_interval: Time in seconds between each accounting
            interim update message. (optional)
            radius_coa: Enable to allow a mechanism to change the attributes of
            an authentication, authorization, and accounting session after it
            is authenticated. (optional)
            radius_port: RADIUS service port number. (optional)
            h3c_compatibility: Enable/disable compatibility with the H3C, a
            mechanism that performs security checking for authentication.
            (optional)
            auth_type: Authentication methods/protocols permitted for this
            RADIUS server. (optional)
            source_ip: Source IP address for communications to the RADIUS
            server. (optional)
            source_ip_interface: Source interface for communication with the
            RADIUS server. (optional)
            username_case_sensitive: Enable/disable case sensitive user names.
            (optional)
            group_override_attr_type: RADIUS attribute type to override user
            group information. (optional)
            class_: Class attribute name(s). (optional)
            password_renewal: Enable/disable password renewal. (optional)
            require_message_authenticator: Require message authenticator in
            authentication response. (optional)
            password_encoding: Password encoding. (optional)
            mac_username_delimiter: MAC authentication username delimiter
            (default = hyphen). (optional)
            mac_password_delimiter: MAC authentication password delimiter
            (default = hyphen). (optional)
            mac_case: MAC authentication case (default = lowercase). (optional)
            acct_all_servers: Enable/disable sending of accounting messages to
            all configured servers (default = disable). (optional)
            switch_controller_acct_fast_framedip_detect: Switch controller
            accounting message Framed-IP detection from DHCP snooping (seconds,
            default=2). (optional)
            interface_select_method: Specify how to select outgoing interface
            to reach server. (optional)
            interface: Specify outgoing interface to reach server. (optional)
            vrf_select: VRF ID used for connection to server. (optional)
            switch_controller_service_type: RADIUS service type. (optional)
            transport_protocol: Transport protocol to be used (default = udp).
            (optional)
            tls_min_proto_version: Minimum supported protocol version for TLS
            connections (default is to follow system global setting).
            (optional)
            ca_cert: CA of server to trust under TLS. (optional)
            client_cert: Client certificate to use under TLS. (optional)
            server_identity_check: Enable/disable RADIUS server identity check
            (verify server domain name/IP address against the server
            certificate). (optional)
            account_key_processing: Account key processing operation. The
            FortiGate will keep either the whole domain or strip the domain
            from the subject identity. (optional)
            account_key_cert_field: Define subject identity field in
            certificate for user access right checking. (optional)
            rsso: Enable/disable RADIUS based single sign on feature.
            (optional)
            rsso_radius_server_port: UDP port to listen on for RADIUS Start and
            Stop records. (optional)
            rsso_radius_response: Enable/disable sending RADIUS response
            packets after receiving Start and Stop records. (optional)
            rsso_validate_request_secret: Enable/disable validating the RADIUS
            request shared secret in the Start or End record. (optional)
            rsso_secret: RADIUS secret used by the RADIUS accounting server.
            (optional)
            rsso_endpoint_attribute: RADIUS attributes used to extract the user
            end point identifier from the RADIUS Start record. (optional)
            rsso_endpoint_block_attribute: RADIUS attributes used to block a
            user. (optional)
            sso_attribute: RADIUS attribute that contains the profile group
            name to be extracted from the RADIUS Start record. (optional)
            sso_attribute_key: Key prefix for SSO group value in the SSO
            attribute. (optional)
            sso_attribute_value_override: Enable/disable override old attribute
            value with new value for the same endpoint. (optional)
            rsso_context_timeout: Time in seconds before the logged out user is
            removed from the "user context list" of logged on users. (optional)
            rsso_log_period: Time interval in seconds that group event log
            messages will be generated for dynamic profile events. (optional)
            rsso_log_flags: Events to log. (optional)
            rsso_flush_ip_session: Enable/disable flushing user IP sessions on
            RADIUS accounting Stop messages. (optional)
            rsso_ep_one_ip_only: Enable/disable the replacement of old IP
            addresses with new ones for the same endpoint on RADIUS accounting
            Start messages. (optional)
            delimiter: Configure delimiter to be used for separating profile
            group names in the SSO attribute (default = plus character "+").
            (optional)
            accounting_server: Additional accounting servers. (optional)
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
        endpoint = "/user/radius"
        if nkey is not None:
            data_payload["nkey"] = nkey
        if name is not None:
            data_payload["name"] = name
        if server is not None:
            data_payload["server"] = server
        if secret is not None:
            data_payload["secret"] = secret
        if secondary_server is not None:
            data_payload["secondary-server"] = secondary_server
        if secondary_secret is not None:
            data_payload["secondary-secret"] = secondary_secret
        if tertiary_server is not None:
            data_payload["tertiary-server"] = tertiary_server
        if tertiary_secret is not None:
            data_payload["tertiary-secret"] = tertiary_secret
        if timeout is not None:
            data_payload["timeout"] = timeout
        if status_ttl is not None:
            data_payload["status-ttl"] = status_ttl
        if all_usergroup is not None:
            data_payload["all-usergroup"] = all_usergroup
        if use_management_vdom is not None:
            data_payload["use-management-vdom"] = use_management_vdom
        if switch_controller_nas_ip_dynamic is not None:
            data_payload["switch-controller-nas-ip-dynamic"] = (
                switch_controller_nas_ip_dynamic
            )
        if nas_ip is not None:
            data_payload["nas-ip"] = nas_ip
        if nas_id_type is not None:
            data_payload["nas-id-type"] = nas_id_type
        if call_station_id_type is not None:
            data_payload["call-station-id-type"] = call_station_id_type
        if nas_id is not None:
            data_payload["nas-id"] = nas_id
        if acct_interim_interval is not None:
            data_payload["acct-interim-interval"] = acct_interim_interval
        if radius_coa is not None:
            data_payload["radius-coa"] = radius_coa
        if radius_port is not None:
            data_payload["radius-port"] = radius_port
        if h3c_compatibility is not None:
            data_payload["h3c-compatibility"] = h3c_compatibility
        if auth_type is not None:
            data_payload["auth-type"] = auth_type
        if source_ip is not None:
            data_payload["source-ip"] = source_ip
        if source_ip_interface is not None:
            data_payload["source-ip-interface"] = source_ip_interface
        if username_case_sensitive is not None:
            data_payload["username-case-sensitive"] = username_case_sensitive
        if group_override_attr_type is not None:
            data_payload["group-override-attr-type"] = group_override_attr_type
        if class_ is not None:
            data_payload["class"] = class_
        if password_renewal is not None:
            data_payload["password-renewal"] = password_renewal
        if require_message_authenticator is not None:
            data_payload["require-message-authenticator"] = (
                require_message_authenticator
            )
        if password_encoding is not None:
            data_payload["password-encoding"] = password_encoding
        if mac_username_delimiter is not None:
            data_payload["mac-username-delimiter"] = mac_username_delimiter
        if mac_password_delimiter is not None:
            data_payload["mac-password-delimiter"] = mac_password_delimiter
        if mac_case is not None:
            data_payload["mac-case"] = mac_case
        if acct_all_servers is not None:
            data_payload["acct-all-servers"] = acct_all_servers
        if switch_controller_acct_fast_framedip_detect is not None:
            data_payload["switch-controller-acct-fast-framedip-detect"] = (
                switch_controller_acct_fast_framedip_detect
            )
        if interface_select_method is not None:
            data_payload["interface-select-method"] = interface_select_method
        if interface is not None:
            data_payload["interface"] = interface
        if vrf_select is not None:
            data_payload["vrf-select"] = vrf_select
        if switch_controller_service_type is not None:
            data_payload["switch-controller-service-type"] = (
                switch_controller_service_type
            )
        if transport_protocol is not None:
            data_payload["transport-protocol"] = transport_protocol
        if tls_min_proto_version is not None:
            data_payload["tls-min-proto-version"] = tls_min_proto_version
        if ca_cert is not None:
            data_payload["ca-cert"] = ca_cert
        if client_cert is not None:
            data_payload["client-cert"] = client_cert
        if server_identity_check is not None:
            data_payload["server-identity-check"] = server_identity_check
        if account_key_processing is not None:
            data_payload["account-key-processing"] = account_key_processing
        if account_key_cert_field is not None:
            data_payload["account-key-cert-field"] = account_key_cert_field
        if rsso is not None:
            data_payload["rsso"] = rsso
        if rsso_radius_server_port is not None:
            data_payload["rsso-radius-server-port"] = rsso_radius_server_port
        if rsso_radius_response is not None:
            data_payload["rsso-radius-response"] = rsso_radius_response
        if rsso_validate_request_secret is not None:
            data_payload["rsso-validate-request-secret"] = (
                rsso_validate_request_secret
            )
        if rsso_secret is not None:
            data_payload["rsso-secret"] = rsso_secret
        if rsso_endpoint_attribute is not None:
            data_payload["rsso-endpoint-attribute"] = rsso_endpoint_attribute
        if rsso_endpoint_block_attribute is not None:
            data_payload["rsso-endpoint-block-attribute"] = (
                rsso_endpoint_block_attribute
            )
        if sso_attribute is not None:
            data_payload["sso-attribute"] = sso_attribute
        if sso_attribute_key is not None:
            data_payload["sso-attribute-key"] = sso_attribute_key
        if sso_attribute_value_override is not None:
            data_payload["sso-attribute-value-override"] = (
                sso_attribute_value_override
            )
        if rsso_context_timeout is not None:
            data_payload["rsso-context-timeout"] = rsso_context_timeout
        if rsso_log_period is not None:
            data_payload["rsso-log-period"] = rsso_log_period
        if rsso_log_flags is not None:
            data_payload["rsso-log-flags"] = rsso_log_flags
        if rsso_flush_ip_session is not None:
            data_payload["rsso-flush-ip-session"] = rsso_flush_ip_session
        if rsso_ep_one_ip_only is not None:
            data_payload["rsso-ep-one-ip-only"] = rsso_ep_one_ip_only
        if delimiter is not None:
            data_payload["delimiter"] = delimiter
        if accounting_server is not None:
            data_payload["accounting-server"] = accounting_server
        data_payload.update(kwargs)
        return self._client.post(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )
