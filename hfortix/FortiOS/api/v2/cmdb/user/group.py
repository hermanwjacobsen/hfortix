"""
FortiOS CMDB - Cmdb User Group

Configuration endpoint for managing cmdb user group objects.

API Endpoints:
    GET    /cmdb/user/group
    POST   /cmdb/user/group
    GET    /cmdb/user/group
    PUT    /cmdb/user/group/{identifier}
    DELETE /cmdb/user/group/{identifier}

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.user.group.get()
    >>>
    >>> # Get specific item (if supported)
    >>> item = fgt.api.cmdb.user.group.get(name="item_name")
    >>>
    >>> # Create new item (use POST)
    >>> result = fgt.api.cmdb.user.group.post(
    ...     name="new_item",
    ...     # ... additional parameters
    ... )
    >>>
    >>> # Update existing item (use PUT)
    >>> result = fgt.api.cmdb.user.group.put(
    ...     name="existing_item",
    ...     # ... parameters to update
    ... )
    >>>
    >>> # Delete item
    >>> result = fgt.api.cmdb.user.group.delete(name="item_name")

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


class Group:
    """
    Group Operations.

    Provides CRUD operations for FortiOS group configuration.

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
        Initialize Group endpoint.

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
            endpoint = f"/user/group/{name}"
        else:
            endpoint = "/user/group"
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
        group_type: str | None = None,
        authtimeout: int | None = None,
        auth_concurrent_override: str | None = None,
        auth_concurrent_value: int | None = None,
        http_digest_realm: str | None = None,
        sso_attribute_value: str | None = None,
        member: list | None = None,
        match: list | None = None,
        user_id: str | None = None,
        password: str | None = None,
        user_name: str | None = None,
        sponsor: str | None = None,
        company: str | None = None,
        email: str | None = None,
        mobile_phone: str | None = None,
        sms_server: str | None = None,
        sms_custom_server: str | None = None,
        expire_type: str | None = None,
        expire: int | None = None,
        max_accounts: int | None = None,
        multiple_guest_add: str | None = None,
        guest: list | None = None,
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
            name: Group name. (optional)
            id: Group ID. (optional)
            group_type: Set the group to be for firewall authentication, FSSO,
            RSSO, or guest users. (optional)
            authtimeout: Authentication timeout in minutes for this user group.
            0 to use the global user setting auth-timeout. (optional)
            auth_concurrent_override: Enable/disable overriding the global
            number of concurrent authentication sessions for this user group.
            (optional)
            auth_concurrent_value: Maximum number of concurrent authenticated
            connections per user (0 - 100). (optional)
            http_digest_realm: Realm attribute for MD5-digest authentication.
            (optional)
            sso_attribute_value: RADIUS attribute value. (optional)
            member: Names of users, peers, LDAP severs, RADIUS servers or
            external idp servers to add to the user group. (optional)
            match: Group matches. (optional)
            user_id: Guest user ID type. (optional)
            password: Guest user password type. (optional)
            user_name: Enable/disable the guest user name entry. (optional)
            sponsor: Set the action for the sponsor guest user field.
            (optional)
            company: Set the action for the company guest user field.
            (optional)
            email: Enable/disable the guest user email address field.
            (optional)
            mobile_phone: Enable/disable the guest user mobile phone number
            field. (optional)
            sms_server: Send SMS through FortiGuard or other external server.
            (optional)
            sms_custom_server: SMS server. (optional)
            expire_type: Determine when the expiration countdown begins.
            (optional)
            expire: Time in seconds before guest user accounts expire (1 -
            31536000). (optional)
            max_accounts: Maximum number of guest accounts that can be created
            for this group (0 means unlimited). (optional)
            multiple_guest_add: Enable/disable addition of multiple guests.
            (optional)
            guest: Guest User. (optional)
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
        endpoint = f"/user/group/{name}"
        if before is not None:
            data_payload["before"] = before
        if after is not None:
            data_payload["after"] = after
        if name is not None:
            data_payload["name"] = name
        if id is not None:
            data_payload["id"] = id
        if group_type is not None:
            data_payload["group-type"] = group_type
        if authtimeout is not None:
            data_payload["authtimeout"] = authtimeout
        if auth_concurrent_override is not None:
            data_payload["auth-concurrent-override"] = auth_concurrent_override
        if auth_concurrent_value is not None:
            data_payload["auth-concurrent-value"] = auth_concurrent_value
        if http_digest_realm is not None:
            data_payload["http-digest-realm"] = http_digest_realm
        if sso_attribute_value is not None:
            data_payload["sso-attribute-value"] = sso_attribute_value
        if member is not None:
            data_payload["member"] = member
        if match is not None:
            data_payload["match"] = match
        if user_id is not None:
            data_payload["user-id"] = user_id
        if password is not None:
            data_payload["password"] = password
        if user_name is not None:
            data_payload["user-name"] = user_name
        if sponsor is not None:
            data_payload["sponsor"] = sponsor
        if company is not None:
            data_payload["company"] = company
        if email is not None:
            data_payload["email"] = email
        if mobile_phone is not None:
            data_payload["mobile-phone"] = mobile_phone
        if sms_server is not None:
            data_payload["sms-server"] = sms_server
        if sms_custom_server is not None:
            data_payload["sms-custom-server"] = sms_custom_server
        if expire_type is not None:
            data_payload["expire-type"] = expire_type
        if expire is not None:
            data_payload["expire"] = expire
        if max_accounts is not None:
            data_payload["max-accounts"] = max_accounts
        if multiple_guest_add is not None:
            data_payload["multiple-guest-add"] = multiple_guest_add
        if guest is not None:
            data_payload["guest"] = guest
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
        endpoint = f"/user/group/{name}"
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
        group_type: str | None = None,
        authtimeout: int | None = None,
        auth_concurrent_override: str | None = None,
        auth_concurrent_value: int | None = None,
        http_digest_realm: str | None = None,
        sso_attribute_value: str | None = None,
        member: list | None = None,
        match: list | None = None,
        user_id: str | None = None,
        password: str | None = None,
        user_name: str | None = None,
        sponsor: str | None = None,
        company: str | None = None,
        email: str | None = None,
        mobile_phone: str | None = None,
        sms_server: str | None = None,
        sms_custom_server: str | None = None,
        expire_type: str | None = None,
        expire: int | None = None,
        max_accounts: int | None = None,
        multiple_guest_add: str | None = None,
        guest: list | None = None,
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
            name: Group name. (optional)
            id: Group ID. (optional)
            group_type: Set the group to be for firewall authentication, FSSO,
            RSSO, or guest users. (optional)
            authtimeout: Authentication timeout in minutes for this user group.
            0 to use the global user setting auth-timeout. (optional)
            auth_concurrent_override: Enable/disable overriding the global
            number of concurrent authentication sessions for this user group.
            (optional)
            auth_concurrent_value: Maximum number of concurrent authenticated
            connections per user (0 - 100). (optional)
            http_digest_realm: Realm attribute for MD5-digest authentication.
            (optional)
            sso_attribute_value: RADIUS attribute value. (optional)
            member: Names of users, peers, LDAP severs, RADIUS servers or
            external idp servers to add to the user group. (optional)
            match: Group matches. (optional)
            user_id: Guest user ID type. (optional)
            password: Guest user password type. (optional)
            user_name: Enable/disable the guest user name entry. (optional)
            sponsor: Set the action for the sponsor guest user field.
            (optional)
            company: Set the action for the company guest user field.
            (optional)
            email: Enable/disable the guest user email address field.
            (optional)
            mobile_phone: Enable/disable the guest user mobile phone number
            field. (optional)
            sms_server: Send SMS through FortiGuard or other external server.
            (optional)
            sms_custom_server: SMS server. (optional)
            expire_type: Determine when the expiration countdown begins.
            (optional)
            expire: Time in seconds before guest user accounts expire (1 -
            31536000). (optional)
            max_accounts: Maximum number of guest accounts that can be created
            for this group (0 means unlimited). (optional)
            multiple_guest_add: Enable/disable addition of multiple guests.
            (optional)
            guest: Guest User. (optional)
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
        endpoint = "/user/group"
        if nkey is not None:
            data_payload["nkey"] = nkey
        if name is not None:
            data_payload["name"] = name
        if id is not None:
            data_payload["id"] = id
        if group_type is not None:
            data_payload["group-type"] = group_type
        if authtimeout is not None:
            data_payload["authtimeout"] = authtimeout
        if auth_concurrent_override is not None:
            data_payload["auth-concurrent-override"] = auth_concurrent_override
        if auth_concurrent_value is not None:
            data_payload["auth-concurrent-value"] = auth_concurrent_value
        if http_digest_realm is not None:
            data_payload["http-digest-realm"] = http_digest_realm
        if sso_attribute_value is not None:
            data_payload["sso-attribute-value"] = sso_attribute_value
        if member is not None:
            data_payload["member"] = member
        if match is not None:
            data_payload["match"] = match
        if user_id is not None:
            data_payload["user-id"] = user_id
        if password is not None:
            data_payload["password"] = password
        if user_name is not None:
            data_payload["user-name"] = user_name
        if sponsor is not None:
            data_payload["sponsor"] = sponsor
        if company is not None:
            data_payload["company"] = company
        if email is not None:
            data_payload["email"] = email
        if mobile_phone is not None:
            data_payload["mobile-phone"] = mobile_phone
        if sms_server is not None:
            data_payload["sms-server"] = sms_server
        if sms_custom_server is not None:
            data_payload["sms-custom-server"] = sms_custom_server
        if expire_type is not None:
            data_payload["expire-type"] = expire_type
        if expire is not None:
            data_payload["expire"] = expire
        if max_accounts is not None:
            data_payload["max-accounts"] = max_accounts
        if multiple_guest_add is not None:
            data_payload["multiple-guest-add"] = multiple_guest_add
        if guest is not None:
            data_payload["guest"] = guest
        data_payload.update(kwargs)
        return self._client.post(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )
