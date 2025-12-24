"""
FortiOS CMDB - Cmdb User Ldap

Configuration endpoint for managing cmdb user ldap objects.

API Endpoints:
    GET    /cmdb/user/ldap
    POST   /cmdb/user/ldap
    GET    /cmdb/user/ldap
    PUT    /cmdb/user/ldap/{identifier}
    DELETE /cmdb/user/ldap/{identifier}

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.user.ldap.get()
    >>>
    >>> # Get specific item (if supported)
    >>> item = fgt.api.cmdb.user.ldap.get(name="item_name")
    >>>
    >>> # Create new item (use POST)
    >>> result = fgt.api.cmdb.user.ldap.post(
    ...     name="new_item",
    ...     # ... additional parameters
    ... )
    >>>
    >>> # Update existing item (use PUT)
    >>> result = fgt.api.cmdb.user.ldap.put(
    ...     name="existing_item",
    ...     # ... parameters to update
    ... )
    >>>
    >>> # Delete item
    >>> result = fgt.api.cmdb.user.ldap.delete(name="item_name")

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


class Ldap:
    """
    Ldap Operations.

    Provides CRUD operations for FortiOS ldap configuration.

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
        Initialize Ldap endpoint.

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
            endpoint = f"/user/ldap/{name}"
        else:
            endpoint = "/user/ldap"
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
        secondary_server: str | None = None,
        tertiary_server: str | None = None,
        status_ttl: int | None = None,
        server_identity_check: str | None = None,
        source_ip: str | None = None,
        source_ip_interface: str | None = None,
        source_port: int | None = None,
        cnid: str | None = None,
        dn: str | None = None,
        type: str | None = None,
        two_factor: str | None = None,
        two_factor_authentication: str | None = None,
        two_factor_notification: str | None = None,
        two_factor_filter: str | None = None,
        username: str | None = None,
        password: str | None = None,
        group_member_check: str | None = None,
        group_search_base: str | None = None,
        group_object_filter: str | None = None,
        group_filter: str | None = None,
        secure: str | None = None,
        ssl_min_proto_version: str | None = None,
        ca_cert: str | None = None,
        port: int | None = None,
        password_expiry_warning: str | None = None,
        password_renewal: str | None = None,
        member_attr: str | None = None,
        account_key_processing: str | None = None,
        account_key_cert_field: str | None = None,
        account_key_filter: str | None = None,
        search_type: str | None = None,
        client_cert_auth: str | None = None,
        client_cert: str | None = None,
        obtain_user_info: str | None = None,
        user_info_exchange_server: str | None = None,
        interface_select_method: str | None = None,
        interface: str | None = None,
        vrf_select: int | None = None,
        antiphish: str | None = None,
        password_attr: str | None = None,
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
            name: LDAP server entry name. (optional)
            server: LDAP server CN domain name or IP. (optional)
            secondary_server: Secondary LDAP server CN domain name or IP.
            (optional)
            tertiary_server: Tertiary LDAP server CN domain name or IP.
            (optional)
            status_ttl: Time for which server reachability is cached so that
            when a server is unreachable, it will not be retried for at least
            this period of time (0 = cache disabled, default = 300). (optional)
            server_identity_check: Enable/disable LDAP server identity check
            (verify server domain name/IP address against the server
            certificate). (optional)
            source_ip: FortiGate IP address to be used for communication with
            the LDAP server. (optional)
            source_ip_interface: Source interface for communication with the
            LDAP server. (optional)
            source_port: Source port to be used for communication with the LDAP
            server. (optional)
            cnid: Common name identifier for the LDAP server. The common name
            identifier for most LDAP servers is "cn". (optional)
            dn: Distinguished name used to look up entries on the LDAP server.
            (optional)
            type: Authentication type for LDAP searches. (optional)
            two_factor: Enable/disable two-factor authentication. (optional)
            two_factor_authentication: Authentication method by FortiToken
            Cloud. (optional)
            two_factor_notification: Notification method for user activation by
            FortiToken Cloud. (optional)
            two_factor_filter: Filter used to synchronize users to FortiToken
            Cloud. (optional)
            username: Username (full DN) for initial binding. (optional)
            password: Password for initial binding. (optional)
            group_member_check: Group member checking methods. (optional)
            group_search_base: Search base used for group searching. (optional)
            group_object_filter: Filter used for group searching. (optional)
            group_filter: Filter used for group matching. (optional)
            secure: Port to be used for authentication. (optional)
            ssl_min_proto_version: Minimum supported protocol version for
            SSL/TLS connections (default is to follow system global setting).
            (optional)
            ca_cert: CA certificate name. (optional)
            port: Port to be used for communication with the LDAP server
            (default = 389). (optional)
            password_expiry_warning: Enable/disable password expiry warnings.
            (optional)
            password_renewal: Enable/disable online password renewal.
            (optional)
            member_attr: Name of attribute from which to get group membership.
            (optional)
            account_key_processing: Account key processing operation. The
            FortiGate will keep either the whole domain or strip the domain
            from the subject identity. (optional)
            account_key_cert_field: Define subject identity field in
            certificate for user access right checking. (optional)
            account_key_filter: Account key filter, using the UPN as the search
            filter. (optional)
            search_type: Search type. (optional)
            client_cert_auth: Enable/disable using client certificate for TLS
            authentication. (optional)
            client_cert: Client certificate name. (optional)
            obtain_user_info: Enable/disable obtaining of user information.
            (optional)
            user_info_exchange_server: MS Exchange server from which to fetch
            user information. (optional)
            interface_select_method: Specify how to select outgoing interface
            to reach server. (optional)
            interface: Specify outgoing interface to reach server. (optional)
            vrf_select: VRF ID used for connection to server. (optional)
            antiphish: Enable/disable AntiPhishing credential backend.
            (optional)
            password_attr: Name of attribute to get password hash. (optional)
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
        endpoint = f"/user/ldap/{name}"
        if before is not None:
            data_payload["before"] = before
        if after is not None:
            data_payload["after"] = after
        if name is not None:
            data_payload["name"] = name
        if server is not None:
            data_payload["server"] = server
        if secondary_server is not None:
            data_payload["secondary-server"] = secondary_server
        if tertiary_server is not None:
            data_payload["tertiary-server"] = tertiary_server
        if status_ttl is not None:
            data_payload["status-ttl"] = status_ttl
        if server_identity_check is not None:
            data_payload["server-identity-check"] = server_identity_check
        if source_ip is not None:
            data_payload["source-ip"] = source_ip
        if source_ip_interface is not None:
            data_payload["source-ip-interface"] = source_ip_interface
        if source_port is not None:
            data_payload["source-port"] = source_port
        if cnid is not None:
            data_payload["cnid"] = cnid
        if dn is not None:
            data_payload["dn"] = dn
        if type is not None:
            data_payload["type"] = type
        if two_factor is not None:
            data_payload["two-factor"] = two_factor
        if two_factor_authentication is not None:
            data_payload["two-factor-authentication"] = (
                two_factor_authentication
            )
        if two_factor_notification is not None:
            data_payload["two-factor-notification"] = two_factor_notification
        if two_factor_filter is not None:
            data_payload["two-factor-filter"] = two_factor_filter
        if username is not None:
            data_payload["username"] = username
        if password is not None:
            data_payload["password"] = password
        if group_member_check is not None:
            data_payload["group-member-check"] = group_member_check
        if group_search_base is not None:
            data_payload["group-search-base"] = group_search_base
        if group_object_filter is not None:
            data_payload["group-object-filter"] = group_object_filter
        if group_filter is not None:
            data_payload["group-filter"] = group_filter
        if secure is not None:
            data_payload["secure"] = secure
        if ssl_min_proto_version is not None:
            data_payload["ssl-min-proto-version"] = ssl_min_proto_version
        if ca_cert is not None:
            data_payload["ca-cert"] = ca_cert
        if port is not None:
            data_payload["port"] = port
        if password_expiry_warning is not None:
            data_payload["password-expiry-warning"] = password_expiry_warning
        if password_renewal is not None:
            data_payload["password-renewal"] = password_renewal
        if member_attr is not None:
            data_payload["member-attr"] = member_attr
        if account_key_processing is not None:
            data_payload["account-key-processing"] = account_key_processing
        if account_key_cert_field is not None:
            data_payload["account-key-cert-field"] = account_key_cert_field
        if account_key_filter is not None:
            data_payload["account-key-filter"] = account_key_filter
        if search_type is not None:
            data_payload["search-type"] = search_type
        if client_cert_auth is not None:
            data_payload["client-cert-auth"] = client_cert_auth
        if client_cert is not None:
            data_payload["client-cert"] = client_cert
        if obtain_user_info is not None:
            data_payload["obtain-user-info"] = obtain_user_info
        if user_info_exchange_server is not None:
            data_payload["user-info-exchange-server"] = (
                user_info_exchange_server
            )
        if interface_select_method is not None:
            data_payload["interface-select-method"] = interface_select_method
        if interface is not None:
            data_payload["interface"] = interface
        if vrf_select is not None:
            data_payload["vrf-select"] = vrf_select
        if antiphish is not None:
            data_payload["antiphish"] = antiphish
        if password_attr is not None:
            data_payload["password-attr"] = password_attr
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
        endpoint = f"/user/ldap/{name}"
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
        secondary_server: str | None = None,
        tertiary_server: str | None = None,
        status_ttl: int | None = None,
        server_identity_check: str | None = None,
        source_ip: str | None = None,
        source_ip_interface: str | None = None,
        source_port: int | None = None,
        cnid: str | None = None,
        dn: str | None = None,
        type: str | None = None,
        two_factor: str | None = None,
        two_factor_authentication: str | None = None,
        two_factor_notification: str | None = None,
        two_factor_filter: str | None = None,
        username: str | None = None,
        password: str | None = None,
        group_member_check: str | None = None,
        group_search_base: str | None = None,
        group_object_filter: str | None = None,
        group_filter: str | None = None,
        secure: str | None = None,
        ssl_min_proto_version: str | None = None,
        ca_cert: str | None = None,
        port: int | None = None,
        password_expiry_warning: str | None = None,
        password_renewal: str | None = None,
        member_attr: str | None = None,
        account_key_processing: str | None = None,
        account_key_cert_field: str | None = None,
        account_key_filter: str | None = None,
        search_type: str | None = None,
        client_cert_auth: str | None = None,
        client_cert: str | None = None,
        obtain_user_info: str | None = None,
        user_info_exchange_server: str | None = None,
        interface_select_method: str | None = None,
        interface: str | None = None,
        vrf_select: int | None = None,
        antiphish: str | None = None,
        password_attr: str | None = None,
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
            name: LDAP server entry name. (optional)
            server: LDAP server CN domain name or IP. (optional)
            secondary_server: Secondary LDAP server CN domain name or IP.
            (optional)
            tertiary_server: Tertiary LDAP server CN domain name or IP.
            (optional)
            status_ttl: Time for which server reachability is cached so that
            when a server is unreachable, it will not be retried for at least
            this period of time (0 = cache disabled, default = 300). (optional)
            server_identity_check: Enable/disable LDAP server identity check
            (verify server domain name/IP address against the server
            certificate). (optional)
            source_ip: FortiGate IP address to be used for communication with
            the LDAP server. (optional)
            source_ip_interface: Source interface for communication with the
            LDAP server. (optional)
            source_port: Source port to be used for communication with the LDAP
            server. (optional)
            cnid: Common name identifier for the LDAP server. The common name
            identifier for most LDAP servers is "cn". (optional)
            dn: Distinguished name used to look up entries on the LDAP server.
            (optional)
            type: Authentication type for LDAP searches. (optional)
            two_factor: Enable/disable two-factor authentication. (optional)
            two_factor_authentication: Authentication method by FortiToken
            Cloud. (optional)
            two_factor_notification: Notification method for user activation by
            FortiToken Cloud. (optional)
            two_factor_filter: Filter used to synchronize users to FortiToken
            Cloud. (optional)
            username: Username (full DN) for initial binding. (optional)
            password: Password for initial binding. (optional)
            group_member_check: Group member checking methods. (optional)
            group_search_base: Search base used for group searching. (optional)
            group_object_filter: Filter used for group searching. (optional)
            group_filter: Filter used for group matching. (optional)
            secure: Port to be used for authentication. (optional)
            ssl_min_proto_version: Minimum supported protocol version for
            SSL/TLS connections (default is to follow system global setting).
            (optional)
            ca_cert: CA certificate name. (optional)
            port: Port to be used for communication with the LDAP server
            (default = 389). (optional)
            password_expiry_warning: Enable/disable password expiry warnings.
            (optional)
            password_renewal: Enable/disable online password renewal.
            (optional)
            member_attr: Name of attribute from which to get group membership.
            (optional)
            account_key_processing: Account key processing operation. The
            FortiGate will keep either the whole domain or strip the domain
            from the subject identity. (optional)
            account_key_cert_field: Define subject identity field in
            certificate for user access right checking. (optional)
            account_key_filter: Account key filter, using the UPN as the search
            filter. (optional)
            search_type: Search type. (optional)
            client_cert_auth: Enable/disable using client certificate for TLS
            authentication. (optional)
            client_cert: Client certificate name. (optional)
            obtain_user_info: Enable/disable obtaining of user information.
            (optional)
            user_info_exchange_server: MS Exchange server from which to fetch
            user information. (optional)
            interface_select_method: Specify how to select outgoing interface
            to reach server. (optional)
            interface: Specify outgoing interface to reach server. (optional)
            vrf_select: VRF ID used for connection to server. (optional)
            antiphish: Enable/disable AntiPhishing credential backend.
            (optional)
            password_attr: Name of attribute to get password hash. (optional)
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
        endpoint = "/user/ldap"
        if nkey is not None:
            data_payload["nkey"] = nkey
        if name is not None:
            data_payload["name"] = name
        if server is not None:
            data_payload["server"] = server
        if secondary_server is not None:
            data_payload["secondary-server"] = secondary_server
        if tertiary_server is not None:
            data_payload["tertiary-server"] = tertiary_server
        if status_ttl is not None:
            data_payload["status-ttl"] = status_ttl
        if server_identity_check is not None:
            data_payload["server-identity-check"] = server_identity_check
        if source_ip is not None:
            data_payload["source-ip"] = source_ip
        if source_ip_interface is not None:
            data_payload["source-ip-interface"] = source_ip_interface
        if source_port is not None:
            data_payload["source-port"] = source_port
        if cnid is not None:
            data_payload["cnid"] = cnid
        if dn is not None:
            data_payload["dn"] = dn
        if type is not None:
            data_payload["type"] = type
        if two_factor is not None:
            data_payload["two-factor"] = two_factor
        if two_factor_authentication is not None:
            data_payload["two-factor-authentication"] = (
                two_factor_authentication
            )
        if two_factor_notification is not None:
            data_payload["two-factor-notification"] = two_factor_notification
        if two_factor_filter is not None:
            data_payload["two-factor-filter"] = two_factor_filter
        if username is not None:
            data_payload["username"] = username
        if password is not None:
            data_payload["password"] = password
        if group_member_check is not None:
            data_payload["group-member-check"] = group_member_check
        if group_search_base is not None:
            data_payload["group-search-base"] = group_search_base
        if group_object_filter is not None:
            data_payload["group-object-filter"] = group_object_filter
        if group_filter is not None:
            data_payload["group-filter"] = group_filter
        if secure is not None:
            data_payload["secure"] = secure
        if ssl_min_proto_version is not None:
            data_payload["ssl-min-proto-version"] = ssl_min_proto_version
        if ca_cert is not None:
            data_payload["ca-cert"] = ca_cert
        if port is not None:
            data_payload["port"] = port
        if password_expiry_warning is not None:
            data_payload["password-expiry-warning"] = password_expiry_warning
        if password_renewal is not None:
            data_payload["password-renewal"] = password_renewal
        if member_attr is not None:
            data_payload["member-attr"] = member_attr
        if account_key_processing is not None:
            data_payload["account-key-processing"] = account_key_processing
        if account_key_cert_field is not None:
            data_payload["account-key-cert-field"] = account_key_cert_field
        if account_key_filter is not None:
            data_payload["account-key-filter"] = account_key_filter
        if search_type is not None:
            data_payload["search-type"] = search_type
        if client_cert_auth is not None:
            data_payload["client-cert-auth"] = client_cert_auth
        if client_cert is not None:
            data_payload["client-cert"] = client_cert
        if obtain_user_info is not None:
            data_payload["obtain-user-info"] = obtain_user_info
        if user_info_exchange_server is not None:
            data_payload["user-info-exchange-server"] = (
                user_info_exchange_server
            )
        if interface_select_method is not None:
            data_payload["interface-select-method"] = interface_select_method
        if interface is not None:
            data_payload["interface"] = interface
        if vrf_select is not None:
            data_payload["vrf-select"] = vrf_select
        if antiphish is not None:
            data_payload["antiphish"] = antiphish
        if password_attr is not None:
            data_payload["password-attr"] = password_attr
        data_payload.update(kwargs)
        return self._client.post(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )
