"""
FortiOS CMDB - Cmdb User Local

Configuration endpoint for managing cmdb user local objects.

API Endpoints:
    GET    /cmdb/user/local
    POST   /cmdb/user/local
    GET    /cmdb/user/local
    PUT    /cmdb/user/local/{identifier}
    DELETE /cmdb/user/local/{identifier}

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.user.local.get()
    >>>
    >>> # Get specific item (if supported)
    >>> item = fgt.api.cmdb.user.local.get(name="item_name")
    >>>
    >>> # Create new item (use POST)
    >>> result = fgt.api.cmdb.user.local.post(
    ...     name="new_item",
    ...     # ... additional parameters
    ... )
    >>>
    >>> # Update existing item (use PUT)
    >>> result = fgt.api.cmdb.user.local.put(
    ...     name="existing_item",
    ...     # ... parameters to update
    ... )
    >>>
    >>> # Delete item
    >>> result = fgt.api.cmdb.user.local.delete(name="item_name")

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


class Local:
    """
    Local Operations.

    Provides CRUD operations for FortiOS local configuration.

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
        Initialize Local endpoint.

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
            endpoint = f"/user/local/{name}"
        else:
            endpoint = "/user/local"
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
        id: int | None = None,
        status: str | None = None,
        type: str | None = None,
        passwd: str | None = None,
        ldap_server: str | None = None,
        radius_server: str | None = None,
        tacacs_plus__server: str | None = None,
        saml_server: str | None = None,
        two_factor: str | None = None,
        two_factor_authentication: str | None = None,
        two_factor_notification: str | None = None,
        fortitoken: str | None = None,
        email_to: str | None = None,
        sms_server: str | None = None,
        sms_custom_server: str | None = None,
        sms_phone: str | None = None,
        passwd_policy: str | None = None,
        passwd_time: str | None = None,
        authtimeout: int | None = None,
        workstation: str | None = None,
        auth_concurrent_override: str | None = None,
        auth_concurrent_value: int | None = None,
        ppk_secret: str | None = None,
        ppk_identity: str | None = None,
        qkd_profile: str | None = None,
        username_sensitivity: str | None = None,
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
            name: Local user name. (optional)
            id: User ID. (optional)
            status: Enable/disable allowing the local user to authenticate with
            the FortiGate unit. (optional)
            type: Authentication method. (optional)
            passwd: User's password. (optional)
            ldap_server: Name of LDAP server with which the user must
            authenticate. (optional)
            radius_server: Name of RADIUS server with which the user must
            authenticate. (optional)
            tacacs_plus__server: Name of TACACS+ server with which the user
            must authenticate. (optional)
            saml_server: Name of SAML server with which the user must
            authenticate. (optional)
            two_factor: Enable/disable two-factor authentication. (optional)
            two_factor_authentication: Authentication method by FortiToken
            Cloud. (optional)
            two_factor_notification: Notification method for user activation by
            FortiToken Cloud. (optional)
            fortitoken: Two-factor recipient's FortiToken serial number.
            (optional)
            email_to: Two-factor recipient's email address. (optional)
            sms_server: Send SMS through FortiGuard or other external server.
            (optional)
            sms_custom_server: Two-factor recipient's SMS server. (optional)
            sms_phone: Two-factor recipient's mobile phone number. (optional)
            passwd_policy: Password policy to apply to this user, as defined in
            config user password-policy. (optional)
            passwd_time: Time of the last password update. (optional)
            authtimeout: Time in minutes before the authentication timeout for
            a user is reached. (optional)
            workstation: Name of the remote user workstation, if you want to
            limit the user to authenticate only from a particular workstation.
            (optional)
            auth_concurrent_override: Enable/disable overriding the
            policy-auth-concurrent under config system global. (optional)
            auth_concurrent_value: Maximum number of concurrent logins
            permitted from the same user. (optional)
            ppk_secret: IKEv2 Postquantum Preshared Key (ASCII string or
            hexadecimal encoded with a leading 0x). (optional)
            ppk_identity: IKEv2 Postquantum Preshared Key Identity. (optional)
            qkd_profile: Quantum Key Distribution (QKD) profile. (optional)
            username_sensitivity: Enable/disable case and accent sensitivity
            when performing username matching (accents are stripped and case is
            ignored when disabled). (optional)
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
        endpoint = f"/user/local/{name}"
        if before is not None:
            data_payload["before"] = before
        if after is not None:
            data_payload["after"] = after
        if name is not None:
            data_payload["name"] = name
        if id is not None:
            data_payload["id"] = id
        if status is not None:
            data_payload["status"] = status
        if type is not None:
            data_payload["type"] = type
        if passwd is not None:
            data_payload["passwd"] = passwd
        if ldap_server is not None:
            data_payload["ldap-server"] = ldap_server
        if radius_server is not None:
            data_payload["radius-server"] = radius_server
        if tacacs_plus__server is not None:
            data_payload["tacacs+-server"] = tacacs_plus__server
        if saml_server is not None:
            data_payload["saml-server"] = saml_server
        if two_factor is not None:
            data_payload["two-factor"] = two_factor
        if two_factor_authentication is not None:
            data_payload["two-factor-authentication"] = (
                two_factor_authentication
            )
        if two_factor_notification is not None:
            data_payload["two-factor-notification"] = two_factor_notification
        if fortitoken is not None:
            data_payload["fortitoken"] = fortitoken
        if email_to is not None:
            data_payload["email-to"] = email_to
        if sms_server is not None:
            data_payload["sms-server"] = sms_server
        if sms_custom_server is not None:
            data_payload["sms-custom-server"] = sms_custom_server
        if sms_phone is not None:
            data_payload["sms-phone"] = sms_phone
        if passwd_policy is not None:
            data_payload["passwd-policy"] = passwd_policy
        if passwd_time is not None:
            data_payload["passwd-time"] = passwd_time
        if authtimeout is not None:
            data_payload["authtimeout"] = authtimeout
        if workstation is not None:
            data_payload["workstation"] = workstation
        if auth_concurrent_override is not None:
            data_payload["auth-concurrent-override"] = auth_concurrent_override
        if auth_concurrent_value is not None:
            data_payload["auth-concurrent-value"] = auth_concurrent_value
        if ppk_secret is not None:
            data_payload["ppk-secret"] = ppk_secret
        if ppk_identity is not None:
            data_payload["ppk-identity"] = ppk_identity
        if qkd_profile is not None:
            data_payload["qkd-profile"] = qkd_profile
        if username_sensitivity is not None:
            data_payload["username-sensitivity"] = username_sensitivity
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
        endpoint = f"/user/local/{name}"
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
        id: int | None = None,
        status: str | None = None,
        type: str | None = None,
        passwd: str | None = None,
        ldap_server: str | None = None,
        radius_server: str | None = None,
        tacacs_plus__server: str | None = None,
        saml_server: str | None = None,
        two_factor: str | None = None,
        two_factor_authentication: str | None = None,
        two_factor_notification: str | None = None,
        fortitoken: str | None = None,
        email_to: str | None = None,
        sms_server: str | None = None,
        sms_custom_server: str | None = None,
        sms_phone: str | None = None,
        passwd_policy: str | None = None,
        passwd_time: str | None = None,
        authtimeout: int | None = None,
        workstation: str | None = None,
        auth_concurrent_override: str | None = None,
        auth_concurrent_value: int | None = None,
        ppk_secret: str | None = None,
        ppk_identity: str | None = None,
        qkd_profile: str | None = None,
        username_sensitivity: str | None = None,
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
            name: Local user name. (optional)
            id: User ID. (optional)
            status: Enable/disable allowing the local user to authenticate with
            the FortiGate unit. (optional)
            type: Authentication method. (optional)
            passwd: User's password. (optional)
            ldap_server: Name of LDAP server with which the user must
            authenticate. (optional)
            radius_server: Name of RADIUS server with which the user must
            authenticate. (optional)
            tacacs_plus__server: Name of TACACS+ server with which the user
            must authenticate. (optional)
            saml_server: Name of SAML server with which the user must
            authenticate. (optional)
            two_factor: Enable/disable two-factor authentication. (optional)
            two_factor_authentication: Authentication method by FortiToken
            Cloud. (optional)
            two_factor_notification: Notification method for user activation by
            FortiToken Cloud. (optional)
            fortitoken: Two-factor recipient's FortiToken serial number.
            (optional)
            email_to: Two-factor recipient's email address. (optional)
            sms_server: Send SMS through FortiGuard or other external server.
            (optional)
            sms_custom_server: Two-factor recipient's SMS server. (optional)
            sms_phone: Two-factor recipient's mobile phone number. (optional)
            passwd_policy: Password policy to apply to this user, as defined in
            config user password-policy. (optional)
            passwd_time: Time of the last password update. (optional)
            authtimeout: Time in minutes before the authentication timeout for
            a user is reached. (optional)
            workstation: Name of the remote user workstation, if you want to
            limit the user to authenticate only from a particular workstation.
            (optional)
            auth_concurrent_override: Enable/disable overriding the
            policy-auth-concurrent under config system global. (optional)
            auth_concurrent_value: Maximum number of concurrent logins
            permitted from the same user. (optional)
            ppk_secret: IKEv2 Postquantum Preshared Key (ASCII string or
            hexadecimal encoded with a leading 0x). (optional)
            ppk_identity: IKEv2 Postquantum Preshared Key Identity. (optional)
            qkd_profile: Quantum Key Distribution (QKD) profile. (optional)
            username_sensitivity: Enable/disable case and accent sensitivity
            when performing username matching (accents are stripped and case is
            ignored when disabled). (optional)
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
        endpoint = "/user/local"
        if nkey is not None:
            data_payload["nkey"] = nkey
        if name is not None:
            data_payload["name"] = name
        if id is not None:
            data_payload["id"] = id
        if status is not None:
            data_payload["status"] = status
        if type is not None:
            data_payload["type"] = type
        if passwd is not None:
            data_payload["passwd"] = passwd
        if ldap_server is not None:
            data_payload["ldap-server"] = ldap_server
        if radius_server is not None:
            data_payload["radius-server"] = radius_server
        if tacacs_plus__server is not None:
            data_payload["tacacs+-server"] = tacacs_plus__server
        if saml_server is not None:
            data_payload["saml-server"] = saml_server
        if two_factor is not None:
            data_payload["two-factor"] = two_factor
        if two_factor_authentication is not None:
            data_payload["two-factor-authentication"] = (
                two_factor_authentication
            )
        if two_factor_notification is not None:
            data_payload["two-factor-notification"] = two_factor_notification
        if fortitoken is not None:
            data_payload["fortitoken"] = fortitoken
        if email_to is not None:
            data_payload["email-to"] = email_to
        if sms_server is not None:
            data_payload["sms-server"] = sms_server
        if sms_custom_server is not None:
            data_payload["sms-custom-server"] = sms_custom_server
        if sms_phone is not None:
            data_payload["sms-phone"] = sms_phone
        if passwd_policy is not None:
            data_payload["passwd-policy"] = passwd_policy
        if passwd_time is not None:
            data_payload["passwd-time"] = passwd_time
        if authtimeout is not None:
            data_payload["authtimeout"] = authtimeout
        if workstation is not None:
            data_payload["workstation"] = workstation
        if auth_concurrent_override is not None:
            data_payload["auth-concurrent-override"] = auth_concurrent_override
        if auth_concurrent_value is not None:
            data_payload["auth-concurrent-value"] = auth_concurrent_value
        if ppk_secret is not None:
            data_payload["ppk-secret"] = ppk_secret
        if ppk_identity is not None:
            data_payload["ppk-identity"] = ppk_identity
        if qkd_profile is not None:
            data_payload["qkd-profile"] = qkd_profile
        if username_sensitivity is not None:
            data_payload["username-sensitivity"] = username_sensitivity
        data_payload.update(kwargs)
        return self._client.post(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )
