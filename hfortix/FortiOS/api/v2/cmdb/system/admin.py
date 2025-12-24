"""
FortiOS CMDB - Cmdb System Admin

Configuration endpoint for managing cmdb system admin objects.

API Endpoints:
    GET    /cmdb/system/admin
    POST   /cmdb/system/admin
    GET    /cmdb/system/admin
    PUT    /cmdb/system/admin/{identifier}
    DELETE /cmdb/system/admin/{identifier}

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.system.admin.get()
    >>>
    >>> # Get specific item (if supported)
    >>> item = fgt.api.cmdb.system.admin.get(name="item_name")
    >>>
    >>> # Create new item (use POST)
    >>> result = fgt.api.cmdb.system.admin.post(
    ...     name="new_item",
    ...     # ... additional parameters
    ... )
    >>>
    >>> # Update existing item (use PUT)
    >>> result = fgt.api.cmdb.system.admin.put(
    ...     name="existing_item",
    ...     # ... parameters to update
    ... )
    >>>
    >>> # Delete item
    >>> result = fgt.api.cmdb.system.admin.delete(name="item_name")

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


class Admin:
    """
    Admin Operations.

    Provides CRUD operations for FortiOS admin configuration.

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
        Initialize Admin endpoint.

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
            endpoint = f"/system/admin/{name}"
        else:
            endpoint = "/system/admin"
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
        remote_auth: str | None = None,
        remote_group: str | None = None,
        wildcard: str | None = None,
        password: str | None = None,
        peer_auth: str | None = None,
        peer_group: str | None = None,
        trusthost1: str | None = None,
        trusthost2: str | None = None,
        trusthost3: str | None = None,
        trusthost4: str | None = None,
        trusthost5: str | None = None,
        trusthost6: str | None = None,
        trusthost7: str | None = None,
        trusthost8: str | None = None,
        trusthost9: str | None = None,
        trusthost10: str | None = None,
        ip6_trusthost1: str | None = None,
        ip6_trusthost2: str | None = None,
        ip6_trusthost3: str | None = None,
        ip6_trusthost4: str | None = None,
        ip6_trusthost5: str | None = None,
        ip6_trusthost6: str | None = None,
        ip6_trusthost7: str | None = None,
        ip6_trusthost8: str | None = None,
        ip6_trusthost9: str | None = None,
        ip6_trusthost10: str | None = None,
        accprofile: str | None = None,
        allow_remove_admin_session: str | None = None,
        comments: str | None = None,
        ssh_public_key1: str | None = None,
        ssh_public_key2: str | None = None,
        ssh_public_key3: str | None = None,
        ssh_certificate: str | None = None,
        schedule: str | None = None,
        accprofile_override: str | None = None,
        vdom_override: str | None = None,
        password_expire: str | None = None,
        force_password_change: str | None = None,
        two_factor: str | None = None,
        two_factor_authentication: str | None = None,
        two_factor_notification: str | None = None,
        fortitoken: str | None = None,
        email_to: str | None = None,
        sms_server: str | None = None,
        sms_custom_server: str | None = None,
        sms_phone: str | None = None,
        guest_auth: str | None = None,
        guest_usergroups: list | None = None,
        guest_lang: str | None = None,
        status: str | None = None,
        list: str | None = None,
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
            name: User name. (optional)
            remote_auth: Enable/disable authentication using a remote RADIUS,
            LDAP, or TACACS+ server. (optional)
            remote_group: User group name used for remote auth. (optional)
            wildcard: Enable/disable wildcard RADIUS authentication. (optional)
            password: Admin user password. (optional)
            peer_auth: Set to enable peer certificate authentication (for HTTPS
            admin access). (optional)
            peer_group: Name of peer group defined under config user group
            which has PKI members. Used for peer certificate authentication
            (for HTTPS admin access). (optional)
            trusthost1: Any IPv4 address or subnet address and netmask from
            which the administrator can connect to the FortiGate unit. Default
            allows access from any IPv4 address. (optional)
            trusthost2: Any IPv4 address or subnet address and netmask from
            which the administrator can connect to the FortiGate unit. Default
            allows access from any IPv4 address. (optional)
            trusthost3: Any IPv4 address or subnet address and netmask from
            which the administrator can connect to the FortiGate unit. Default
            allows access from any IPv4 address. (optional)
            trusthost4: Any IPv4 address or subnet address and netmask from
            which the administrator can connect to the FortiGate unit. Default
            allows access from any IPv4 address. (optional)
            trusthost5: Any IPv4 address or subnet address and netmask from
            which the administrator can connect to the FortiGate unit. Default
            allows access from any IPv4 address. (optional)
            trusthost6: Any IPv4 address or subnet address and netmask from
            which the administrator can connect to the FortiGate unit. Default
            allows access from any IPv4 address. (optional)
            trusthost7: Any IPv4 address or subnet address and netmask from
            which the administrator can connect to the FortiGate unit. Default
            allows access from any IPv4 address. (optional)
            trusthost8: Any IPv4 address or subnet address and netmask from
            which the administrator can connect to the FortiGate unit. Default
            allows access from any IPv4 address. (optional)
            trusthost9: Any IPv4 address or subnet address and netmask from
            which the administrator can connect to the FortiGate unit. Default
            allows access from any IPv4 address. (optional)
            trusthost10: Any IPv4 address or subnet address and netmask from
            which the administrator can connect to the FortiGate unit. Default
            allows access from any IPv4 address. (optional)
            ip6_trusthost1: Any IPv6 address from which the administrator can
            connect to the FortiGate unit. Default allows access from any IPv6
            address. (optional)
            ip6_trusthost2: Any IPv6 address from which the administrator can
            connect to the FortiGate unit. Default allows access from any IPv6
            address. (optional)
            ip6_trusthost3: Any IPv6 address from which the administrator can
            connect to the FortiGate unit. Default allows access from any IPv6
            address. (optional)
            ip6_trusthost4: Any IPv6 address from which the administrator can
            connect to the FortiGate unit. Default allows access from any IPv6
            address. (optional)
            ip6_trusthost5: Any IPv6 address from which the administrator can
            connect to the FortiGate unit. Default allows access from any IPv6
            address. (optional)
            ip6_trusthost6: Any IPv6 address from which the administrator can
            connect to the FortiGate unit. Default allows access from any IPv6
            address. (optional)
            ip6_trusthost7: Any IPv6 address from which the administrator can
            connect to the FortiGate unit. Default allows access from any IPv6
            address. (optional)
            ip6_trusthost8: Any IPv6 address from which the administrator can
            connect to the FortiGate unit. Default allows access from any IPv6
            address. (optional)
            ip6_trusthost9: Any IPv6 address from which the administrator can
            connect to the FortiGate unit. Default allows access from any IPv6
            address. (optional)
            ip6_trusthost10: Any IPv6 address from which the administrator can
            connect to the FortiGate unit. Default allows access from any IPv6
            address. (optional)
            accprofile: Access profile for this administrator. Access profiles
            control administrator access to FortiGate features. (optional)
            allow_remove_admin_session: Enable/disable allow admin session to
            be removed by privileged admin users. (optional)
            comments: Comment. (optional)
            ssh_public_key1: Public key of an SSH client. The client is
            authenticated without being asked for credentials. Create the
            public-private key pair in the SSH client application. (optional)
            ssh_public_key2: Public key of an SSH client. The client is
            authenticated without being asked for credentials. Create the
            public-private key pair in the SSH client application. (optional)
            ssh_public_key3: Public key of an SSH client. The client is
            authenticated without being asked for credentials. Create the
            public-private key pair in the SSH client application. (optional)
            ssh_certificate: Select the certificate to be used by the FortiGate
            for authentication with an SSH client. (optional)
            schedule: Firewall schedule used to restrict when the administrator
            can log in. No schedule means no restrictions. (optional)
            accprofile_override: Enable to use the name of an access profile
            provided by the remote authentication server to control the
            FortiGate features that this administrator can access. (optional)
            vdom_override: Enable to use the names of VDOMs provided by the
            remote authentication server to control the VDOMs that this
            administrator can access. (optional)
            password_expire: Password expire time. (optional)
            force_password_change: Enable/disable force password change on next
            login. (optional)
            two_factor: Enable/disable two-factor authentication. (optional)
            two_factor_authentication: Authentication method by FortiToken
            Cloud. (optional)
            two_factor_notification: Notification method for user activation by
            FortiToken Cloud. (optional)
            fortitoken: This administrator's FortiToken serial number.
            (optional)
            email_to: This administrator's email address. (optional)
            sms_server: Send SMS messages using the FortiGuard SMS server or a
            custom server. (optional)
            sms_custom_server: Custom SMS server to send SMS messages to.
            (optional)
            sms_phone: Phone number on which the administrator receives SMS
            messages. (optional)
            guest_auth: Enable/disable guest authentication. (optional)
            guest_usergroups: Select guest user groups. (optional)
            guest_lang: Guest management portal language. (optional)
            status: print admin status information (optional)
            list: print admin list information (optional)
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
        endpoint = f"/system/admin/{name}"
        if before is not None:
            data_payload["before"] = before
        if after is not None:
            data_payload["after"] = after
        if name is not None:
            data_payload["name"] = name
        if remote_auth is not None:
            data_payload["remote-auth"] = remote_auth
        if remote_group is not None:
            data_payload["remote-group"] = remote_group
        if wildcard is not None:
            data_payload["wildcard"] = wildcard
        if password is not None:
            data_payload["password"] = password
        if peer_auth is not None:
            data_payload["peer-auth"] = peer_auth
        if peer_group is not None:
            data_payload["peer-group"] = peer_group
        if trusthost1 is not None:
            data_payload["trusthost1"] = trusthost1
        if trusthost2 is not None:
            data_payload["trusthost2"] = trusthost2
        if trusthost3 is not None:
            data_payload["trusthost3"] = trusthost3
        if trusthost4 is not None:
            data_payload["trusthost4"] = trusthost4
        if trusthost5 is not None:
            data_payload["trusthost5"] = trusthost5
        if trusthost6 is not None:
            data_payload["trusthost6"] = trusthost6
        if trusthost7 is not None:
            data_payload["trusthost7"] = trusthost7
        if trusthost8 is not None:
            data_payload["trusthost8"] = trusthost8
        if trusthost9 is not None:
            data_payload["trusthost9"] = trusthost9
        if trusthost10 is not None:
            data_payload["trusthost10"] = trusthost10
        if ip6_trusthost1 is not None:
            data_payload["ip6-trusthost1"] = ip6_trusthost1
        if ip6_trusthost2 is not None:
            data_payload["ip6-trusthost2"] = ip6_trusthost2
        if ip6_trusthost3 is not None:
            data_payload["ip6-trusthost3"] = ip6_trusthost3
        if ip6_trusthost4 is not None:
            data_payload["ip6-trusthost4"] = ip6_trusthost4
        if ip6_trusthost5 is not None:
            data_payload["ip6-trusthost5"] = ip6_trusthost5
        if ip6_trusthost6 is not None:
            data_payload["ip6-trusthost6"] = ip6_trusthost6
        if ip6_trusthost7 is not None:
            data_payload["ip6-trusthost7"] = ip6_trusthost7
        if ip6_trusthost8 is not None:
            data_payload["ip6-trusthost8"] = ip6_trusthost8
        if ip6_trusthost9 is not None:
            data_payload["ip6-trusthost9"] = ip6_trusthost9
        if ip6_trusthost10 is not None:
            data_payload["ip6-trusthost10"] = ip6_trusthost10
        if accprofile is not None:
            data_payload["accprofile"] = accprofile
        if allow_remove_admin_session is not None:
            data_payload["allow-remove-admin-session"] = (
                allow_remove_admin_session
            )
        if comments is not None:
            data_payload["comments"] = comments
        if ssh_public_key1 is not None:
            data_payload["ssh-public-key1"] = ssh_public_key1
        if ssh_public_key2 is not None:
            data_payload["ssh-public-key2"] = ssh_public_key2
        if ssh_public_key3 is not None:
            data_payload["ssh-public-key3"] = ssh_public_key3
        if ssh_certificate is not None:
            data_payload["ssh-certificate"] = ssh_certificate
        if schedule is not None:
            data_payload["schedule"] = schedule
        if accprofile_override is not None:
            data_payload["accprofile-override"] = accprofile_override
        if vdom_override is not None:
            data_payload["vdom-override"] = vdom_override
        if password_expire is not None:
            data_payload["password-expire"] = password_expire
        if force_password_change is not None:
            data_payload["force-password-change"] = force_password_change
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
        if guest_auth is not None:
            data_payload["guest-auth"] = guest_auth
        if guest_usergroups is not None:
            data_payload["guest-usergroups"] = guest_usergroups
        if guest_lang is not None:
            data_payload["guest-lang"] = guest_lang
        if status is not None:
            data_payload["status"] = status
        if list is not None:
            data_payload["list"] = list
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
        endpoint = f"/system/admin/{name}"
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
        remote_auth: str | None = None,
        remote_group: str | None = None,
        wildcard: str | None = None,
        password: str | None = None,
        peer_auth: str | None = None,
        peer_group: str | None = None,
        trusthost1: str | None = None,
        trusthost2: str | None = None,
        trusthost3: str | None = None,
        trusthost4: str | None = None,
        trusthost5: str | None = None,
        trusthost6: str | None = None,
        trusthost7: str | None = None,
        trusthost8: str | None = None,
        trusthost9: str | None = None,
        trusthost10: str | None = None,
        ip6_trusthost1: str | None = None,
        ip6_trusthost2: str | None = None,
        ip6_trusthost3: str | None = None,
        ip6_trusthost4: str | None = None,
        ip6_trusthost5: str | None = None,
        ip6_trusthost6: str | None = None,
        ip6_trusthost7: str | None = None,
        ip6_trusthost8: str | None = None,
        ip6_trusthost9: str | None = None,
        ip6_trusthost10: str | None = None,
        accprofile: str | None = None,
        allow_remove_admin_session: str | None = None,
        comments: str | None = None,
        ssh_public_key1: str | None = None,
        ssh_public_key2: str | None = None,
        ssh_public_key3: str | None = None,
        ssh_certificate: str | None = None,
        schedule: str | None = None,
        accprofile_override: str | None = None,
        vdom_override: str | None = None,
        password_expire: str | None = None,
        force_password_change: str | None = None,
        two_factor: str | None = None,
        two_factor_authentication: str | None = None,
        two_factor_notification: str | None = None,
        fortitoken: str | None = None,
        email_to: str | None = None,
        sms_server: str | None = None,
        sms_custom_server: str | None = None,
        sms_phone: str | None = None,
        guest_auth: str | None = None,
        guest_usergroups: list | None = None,
        guest_lang: str | None = None,
        status: str | None = None,
        list: str | None = None,
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
            name: User name. (optional)
            remote_auth: Enable/disable authentication using a remote RADIUS,
            LDAP, or TACACS+ server. (optional)
            remote_group: User group name used for remote auth. (optional)
            wildcard: Enable/disable wildcard RADIUS authentication. (optional)
            password: Admin user password. (optional)
            peer_auth: Set to enable peer certificate authentication (for HTTPS
            admin access). (optional)
            peer_group: Name of peer group defined under config user group
            which has PKI members. Used for peer certificate authentication
            (for HTTPS admin access). (optional)
            trusthost1: Any IPv4 address or subnet address and netmask from
            which the administrator can connect to the FortiGate unit. Default
            allows access from any IPv4 address. (optional)
            trusthost2: Any IPv4 address or subnet address and netmask from
            which the administrator can connect to the FortiGate unit. Default
            allows access from any IPv4 address. (optional)
            trusthost3: Any IPv4 address or subnet address and netmask from
            which the administrator can connect to the FortiGate unit. Default
            allows access from any IPv4 address. (optional)
            trusthost4: Any IPv4 address or subnet address and netmask from
            which the administrator can connect to the FortiGate unit. Default
            allows access from any IPv4 address. (optional)
            trusthost5: Any IPv4 address or subnet address and netmask from
            which the administrator can connect to the FortiGate unit. Default
            allows access from any IPv4 address. (optional)
            trusthost6: Any IPv4 address or subnet address and netmask from
            which the administrator can connect to the FortiGate unit. Default
            allows access from any IPv4 address. (optional)
            trusthost7: Any IPv4 address or subnet address and netmask from
            which the administrator can connect to the FortiGate unit. Default
            allows access from any IPv4 address. (optional)
            trusthost8: Any IPv4 address or subnet address and netmask from
            which the administrator can connect to the FortiGate unit. Default
            allows access from any IPv4 address. (optional)
            trusthost9: Any IPv4 address or subnet address and netmask from
            which the administrator can connect to the FortiGate unit. Default
            allows access from any IPv4 address. (optional)
            trusthost10: Any IPv4 address or subnet address and netmask from
            which the administrator can connect to the FortiGate unit. Default
            allows access from any IPv4 address. (optional)
            ip6_trusthost1: Any IPv6 address from which the administrator can
            connect to the FortiGate unit. Default allows access from any IPv6
            address. (optional)
            ip6_trusthost2: Any IPv6 address from which the administrator can
            connect to the FortiGate unit. Default allows access from any IPv6
            address. (optional)
            ip6_trusthost3: Any IPv6 address from which the administrator can
            connect to the FortiGate unit. Default allows access from any IPv6
            address. (optional)
            ip6_trusthost4: Any IPv6 address from which the administrator can
            connect to the FortiGate unit. Default allows access from any IPv6
            address. (optional)
            ip6_trusthost5: Any IPv6 address from which the administrator can
            connect to the FortiGate unit. Default allows access from any IPv6
            address. (optional)
            ip6_trusthost6: Any IPv6 address from which the administrator can
            connect to the FortiGate unit. Default allows access from any IPv6
            address. (optional)
            ip6_trusthost7: Any IPv6 address from which the administrator can
            connect to the FortiGate unit. Default allows access from any IPv6
            address. (optional)
            ip6_trusthost8: Any IPv6 address from which the administrator can
            connect to the FortiGate unit. Default allows access from any IPv6
            address. (optional)
            ip6_trusthost9: Any IPv6 address from which the administrator can
            connect to the FortiGate unit. Default allows access from any IPv6
            address. (optional)
            ip6_trusthost10: Any IPv6 address from which the administrator can
            connect to the FortiGate unit. Default allows access from any IPv6
            address. (optional)
            accprofile: Access profile for this administrator. Access profiles
            control administrator access to FortiGate features. (optional)
            allow_remove_admin_session: Enable/disable allow admin session to
            be removed by privileged admin users. (optional)
            comments: Comment. (optional)
            ssh_public_key1: Public key of an SSH client. The client is
            authenticated without being asked for credentials. Create the
            public-private key pair in the SSH client application. (optional)
            ssh_public_key2: Public key of an SSH client. The client is
            authenticated without being asked for credentials. Create the
            public-private key pair in the SSH client application. (optional)
            ssh_public_key3: Public key of an SSH client. The client is
            authenticated without being asked for credentials. Create the
            public-private key pair in the SSH client application. (optional)
            ssh_certificate: Select the certificate to be used by the FortiGate
            for authentication with an SSH client. (optional)
            schedule: Firewall schedule used to restrict when the administrator
            can log in. No schedule means no restrictions. (optional)
            accprofile_override: Enable to use the name of an access profile
            provided by the remote authentication server to control the
            FortiGate features that this administrator can access. (optional)
            vdom_override: Enable to use the names of VDOMs provided by the
            remote authentication server to control the VDOMs that this
            administrator can access. (optional)
            password_expire: Password expire time. (optional)
            force_password_change: Enable/disable force password change on next
            login. (optional)
            two_factor: Enable/disable two-factor authentication. (optional)
            two_factor_authentication: Authentication method by FortiToken
            Cloud. (optional)
            two_factor_notification: Notification method for user activation by
            FortiToken Cloud. (optional)
            fortitoken: This administrator's FortiToken serial number.
            (optional)
            email_to: This administrator's email address. (optional)
            sms_server: Send SMS messages using the FortiGuard SMS server or a
            custom server. (optional)
            sms_custom_server: Custom SMS server to send SMS messages to.
            (optional)
            sms_phone: Phone number on which the administrator receives SMS
            messages. (optional)
            guest_auth: Enable/disable guest authentication. (optional)
            guest_usergroups: Select guest user groups. (optional)
            guest_lang: Guest management portal language. (optional)
            status: print admin status information (optional)
            list: print admin list information (optional)
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
        endpoint = "/system/admin"
        if nkey is not None:
            data_payload["nkey"] = nkey
        if name is not None:
            data_payload["name"] = name
        if remote_auth is not None:
            data_payload["remote-auth"] = remote_auth
        if remote_group is not None:
            data_payload["remote-group"] = remote_group
        if wildcard is not None:
            data_payload["wildcard"] = wildcard
        if password is not None:
            data_payload["password"] = password
        if peer_auth is not None:
            data_payload["peer-auth"] = peer_auth
        if peer_group is not None:
            data_payload["peer-group"] = peer_group
        if trusthost1 is not None:
            data_payload["trusthost1"] = trusthost1
        if trusthost2 is not None:
            data_payload["trusthost2"] = trusthost2
        if trusthost3 is not None:
            data_payload["trusthost3"] = trusthost3
        if trusthost4 is not None:
            data_payload["trusthost4"] = trusthost4
        if trusthost5 is not None:
            data_payload["trusthost5"] = trusthost5
        if trusthost6 is not None:
            data_payload["trusthost6"] = trusthost6
        if trusthost7 is not None:
            data_payload["trusthost7"] = trusthost7
        if trusthost8 is not None:
            data_payload["trusthost8"] = trusthost8
        if trusthost9 is not None:
            data_payload["trusthost9"] = trusthost9
        if trusthost10 is not None:
            data_payload["trusthost10"] = trusthost10
        if ip6_trusthost1 is not None:
            data_payload["ip6-trusthost1"] = ip6_trusthost1
        if ip6_trusthost2 is not None:
            data_payload["ip6-trusthost2"] = ip6_trusthost2
        if ip6_trusthost3 is not None:
            data_payload["ip6-trusthost3"] = ip6_trusthost3
        if ip6_trusthost4 is not None:
            data_payload["ip6-trusthost4"] = ip6_trusthost4
        if ip6_trusthost5 is not None:
            data_payload["ip6-trusthost5"] = ip6_trusthost5
        if ip6_trusthost6 is not None:
            data_payload["ip6-trusthost6"] = ip6_trusthost6
        if ip6_trusthost7 is not None:
            data_payload["ip6-trusthost7"] = ip6_trusthost7
        if ip6_trusthost8 is not None:
            data_payload["ip6-trusthost8"] = ip6_trusthost8
        if ip6_trusthost9 is not None:
            data_payload["ip6-trusthost9"] = ip6_trusthost9
        if ip6_trusthost10 is not None:
            data_payload["ip6-trusthost10"] = ip6_trusthost10
        if accprofile is not None:
            data_payload["accprofile"] = accprofile
        if allow_remove_admin_session is not None:
            data_payload["allow-remove-admin-session"] = (
                allow_remove_admin_session
            )
        if comments is not None:
            data_payload["comments"] = comments
        if ssh_public_key1 is not None:
            data_payload["ssh-public-key1"] = ssh_public_key1
        if ssh_public_key2 is not None:
            data_payload["ssh-public-key2"] = ssh_public_key2
        if ssh_public_key3 is not None:
            data_payload["ssh-public-key3"] = ssh_public_key3
        if ssh_certificate is not None:
            data_payload["ssh-certificate"] = ssh_certificate
        if schedule is not None:
            data_payload["schedule"] = schedule
        if accprofile_override is not None:
            data_payload["accprofile-override"] = accprofile_override
        if vdom_override is not None:
            data_payload["vdom-override"] = vdom_override
        if password_expire is not None:
            data_payload["password-expire"] = password_expire
        if force_password_change is not None:
            data_payload["force-password-change"] = force_password_change
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
        if guest_auth is not None:
            data_payload["guest-auth"] = guest_auth
        if guest_usergroups is not None:
            data_payload["guest-usergroups"] = guest_usergroups
        if guest_lang is not None:
            data_payload["guest-lang"] = guest_lang
        if status is not None:
            data_payload["status"] = status
        if list is not None:
            data_payload["list"] = list
        data_payload.update(kwargs)
        return self._client.post(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )
