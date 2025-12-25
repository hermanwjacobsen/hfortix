"""
FortiOS CMDB - Cmdb User Password Policy

Configuration endpoint for managing cmdb user password policy objects.

API Endpoints:
    GET    /cmdb/user/password_policy
    POST   /cmdb/user/password_policy
    GET    /cmdb/user/password_policy
    PUT    /cmdb/user/password_policy/{identifier}
    DELETE /cmdb/user/password_policy/{identifier}

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.user.password_policy.get()
    >>>
    >>> # Get specific item (if supported)
    >>> item = fgt.api.cmdb.user.password_policy.get(name="item_name")
    >>>
    >>> # Create new item (use POST)
    >>> result = fgt.api.cmdb.user.password_policy.post(
    ...     name="new_item",
    ...     # ... additional parameters
    ... )
    >>>
    >>> # Update existing item (use PUT)
    >>> result = fgt.api.cmdb.user.password_policy.put(
    ...     name="existing_item",
    ...     # ... parameters to update
    ... )
    >>>
    >>> # Delete item
    >>> result = fgt.api.cmdb.user.password_policy.delete(name="item_name")

Important:
    - Use **POST** to create new objects (404 error if already exists)
    - Use **PUT** to update existing objects (404 error if doesn't exist)
    - Use **GET** to retrieve configuration (no changes made)
    - Use **DELETE** to remove objects (404 error if doesn't exist)
"""

from __future__ import annotations

from typing import Any, TYPE_CHECKING, Union, cast

if TYPE_CHECKING:
    from collections.abc import Coroutine
    from hfortix.FortiOS.http_client_interface import IHTTPClient


class PasswordPolicy:
    """
    Passwordpolicy Operations.

    Provides CRUD operations for FortiOS passwordpolicy configuration.

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

    def __init__(self, client: 'IHTTPClient'):
        """
        Initialize PasswordPolicy endpoint.

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
            endpoint = f"/user/password-policy/{name}"
        else:
            endpoint = "/user/password-policy"
        if attr is not None:
            params['attr'] = attr
        if skip_to_datasource is not None:
            params['skip_to_datasource'] = skip_to_datasource
        if acs is not None:
            params['acs'] = acs
        if search is not None:
            params['search'] = search
        params.update(kwargs)
        return self._client.get(
            "cmdb",
            endpoint,
            params=params,
            vdom=vdom,
            raw_json=raw_json
        )

    def put(
        self,
        name: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        before: str | None = None,
        after: str | None = None,
        expire_status: str | None = None,
        expire_days: int | None = None,
        warn_days: int | None = None,
        expired_password_renewal: str | None = None,
        minimum_length: int | None = None,
        min_lower_case_letter: int | None = None,
        min_upper_case_letter: int | None = None,
        min_non_alphanumeric: int | None = None,
        min_number: int | None = None,
        min_change_characters: int | None = None,
        reuse_password: str | None = None,
        reuse_password_limit: int | None = None,
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
            name: Password policy name. (optional)
            expire_status: Enable/disable password expiration. (optional)
            expire_days: Time in days before the user's password expires.
            (optional)
            warn_days: Time in days before a password expiration warning
            message is displayed to the user upon login. (optional)
            expired_password_renewal: Enable/disable renewal of a password that
            already is expired. (optional)
            minimum_length: Minimum password length (8 - 128, default = 8).
            (optional)
            min_lower_case_letter: Minimum number of lowercase characters in
            password (0 - 128, default = 0). (optional)
            min_upper_case_letter: Minimum number of uppercase characters in
            password (0 - 128, default = 0). (optional)
            min_non_alphanumeric: Minimum number of non-alphanumeric characters
            in password (0 - 128, default = 0). (optional)
            min_number: Minimum number of numeric characters in password (0 -
            128, default = 0). (optional)
            min_change_characters: Minimum number of unique characters in new
            password which do not exist in old password (0 - 128, default = 0.
            This attribute overrides reuse-password if both are enabled).
            (optional)
            reuse_password: Enable/disable reuse of password. If both
            reuse-password and min-change-characters are enabled,
            min-change-characters overrides. (optional)
            reuse_password_limit: Number of times passwords can be reused (0 -
            20, default = 0. If set to 0, can reuse password an unlimited
            number of times.). (optional)
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
        endpoint = f"/user/password-policy/{name}"
        if before is not None:
            data_payload['before'] = before
        if after is not None:
            data_payload['after'] = after
        if name is not None:
            data_payload['name'] = name
        if expire_status is not None:
            data_payload['expire-status'] = expire_status
        if expire_days is not None:
            data_payload['expire-days'] = expire_days
        if warn_days is not None:
            data_payload['warn-days'] = warn_days
        if expired_password_renewal is not None:
            data_payload['expired-password-renewal'] = expired_password_renewal
        if minimum_length is not None:
            data_payload['minimum-length'] = minimum_length
        if min_lower_case_letter is not None:
            data_payload['min-lower-case-letter'] = min_lower_case_letter
        if min_upper_case_letter is not None:
            data_payload['min-upper-case-letter'] = min_upper_case_letter
        if min_non_alphanumeric is not None:
            data_payload['min-non-alphanumeric'] = min_non_alphanumeric
        if min_number is not None:
            data_payload['min-number'] = min_number
        if min_change_characters is not None:
            data_payload['min-change-characters'] = min_change_characters
        if reuse_password is not None:
            data_payload['reuse-password'] = reuse_password
        if reuse_password_limit is not None:
            data_payload['reuse-password-limit'] = reuse_password_limit
        data_payload.update(kwargs)
        return self._client.put(
            "cmdb",
            endpoint,
            data=data_payload,
            vdom=vdom,
            raw_json=raw_json
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
        endpoint = f"/user/password-policy/{name}"
        params.update(kwargs)
        return self._client.delete(
            "cmdb",
            endpoint,
            params=params,
            vdom=vdom,
            raw_json=raw_json
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
        expire_status: str | None = None,
        expire_days: int | None = None,
        warn_days: int | None = None,
        expired_password_renewal: str | None = None,
        minimum_length: int | None = None,
        min_lower_case_letter: int | None = None,
        min_upper_case_letter: int | None = None,
        min_non_alphanumeric: int | None = None,
        min_number: int | None = None,
        min_change_characters: int | None = None,
        reuse_password: str | None = None,
        reuse_password_limit: int | None = None,
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
            name: Password policy name. (optional)
            expire_status: Enable/disable password expiration. (optional)
            expire_days: Time in days before the user's password expires.
            (optional)
            warn_days: Time in days before a password expiration warning
            message is displayed to the user upon login. (optional)
            expired_password_renewal: Enable/disable renewal of a password that
            already is expired. (optional)
            minimum_length: Minimum password length (8 - 128, default = 8).
            (optional)
            min_lower_case_letter: Minimum number of lowercase characters in
            password (0 - 128, default = 0). (optional)
            min_upper_case_letter: Minimum number of uppercase characters in
            password (0 - 128, default = 0). (optional)
            min_non_alphanumeric: Minimum number of non-alphanumeric characters
            in password (0 - 128, default = 0). (optional)
            min_number: Minimum number of numeric characters in password (0 -
            128, default = 0). (optional)
            min_change_characters: Minimum number of unique characters in new
            password which do not exist in old password (0 - 128, default = 0.
            This attribute overrides reuse-password if both are enabled).
            (optional)
            reuse_password: Enable/disable reuse of password. If both
            reuse-password and min-change-characters are enabled,
            min-change-characters overrides. (optional)
            reuse_password_limit: Number of times passwords can be reused (0 -
            20, default = 0. If set to 0, can reuse password an unlimited
            number of times.). (optional)
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
        endpoint = "/user/password-policy"
        if nkey is not None:
            data_payload['nkey'] = nkey
        if name is not None:
            data_payload['name'] = name
        if expire_status is not None:
            data_payload['expire-status'] = expire_status
        if expire_days is not None:
            data_payload['expire-days'] = expire_days
        if warn_days is not None:
            data_payload['warn-days'] = warn_days
        if expired_password_renewal is not None:
            data_payload['expired-password-renewal'] = expired_password_renewal
        if minimum_length is not None:
            data_payload['minimum-length'] = minimum_length
        if min_lower_case_letter is not None:
            data_payload['min-lower-case-letter'] = min_lower_case_letter
        if min_upper_case_letter is not None:
            data_payload['min-upper-case-letter'] = min_upper_case_letter
        if min_non_alphanumeric is not None:
            data_payload['min-non-alphanumeric'] = min_non_alphanumeric
        if min_number is not None:
            data_payload['min-number'] = min_number
        if min_change_characters is not None:
            data_payload['min-change-characters'] = min_change_characters
        if reuse_password is not None:
            data_payload['reuse-password'] = reuse_password
        if reuse_password_limit is not None:
            data_payload['reuse-password-limit'] = reuse_password_limit
        data_payload.update(kwargs)
        return self._client.post(
            "cmdb",
            endpoint,
            data=data_payload,
            vdom=vdom,
            raw_json=raw_json
        )
