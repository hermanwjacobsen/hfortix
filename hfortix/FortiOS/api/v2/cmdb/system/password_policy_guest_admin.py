"""
FortiOS CMDB - Cmdb System Password Policy Guest Admin

Configuration endpoint for managing cmdb system password policy guest admin
objects.

API Endpoints:
    GET    /cmdb/system/password_policy_guest_admin
    PUT    /cmdb/system/password_policy_guest_admin/{identifier}

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.system.password_policy_guest_admin.get()
    >>>
    >>> # Get specific item (if supported)
    >>> item =
    fgt.api.cmdb.system.password_policy_guest_admin.get(name="item_name")
    >>>
    >>> # Create new item (use POST)
    >>> result = fgt.api.cmdb.system.password_policy_guest_admin.post(
    ...     name="new_item",
    ...     # ... additional parameters
    ... )
    >>>
    >>> # Update existing item (use PUT)
    >>> result = fgt.api.cmdb.system.password_policy_guest_admin.put(
    ...     name="existing_item",
    ...     # ... parameters to update
    ... )
    >>>
    >>> # Delete item
    >>> result =
    fgt.api.cmdb.system.password_policy_guest_admin.delete(name="item_name")

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


class PasswordPolicyGuestAdmin:
    """
    Passwordpolicyguestadmin Operations.

    Provides CRUD operations for FortiOS passwordpolicyguestadmin
    configuration.

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
        Initialize PasswordPolicyGuestAdmin endpoint.

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
        params: dict[str, Any] = payload_dict.copy() if payload_dict else {}
        endpoint = "/system/password-policy-guest-admin"
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
        apply_to: str | None = None,
        minimum_length: int | None = None,
        min_lower_case_letter: int | None = None,
        min_upper_case_letter: int | None = None,
        min_non_alphanumeric: int | None = None,
        min_number: int | None = None,
        expire_status: str | None = None,
        expire_day: int | None = None,
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
            before: If *action=move*, use *before* to specify the ID of the
            resource that this resource will be moved before. (optional)
            after: If *action=move*, use *after* to specify the ID of the
            resource that this resource will be moved after. (optional)
            status: Enable/disable setting a password policy for locally
            defined administrator passwords and IPsec VPN pre-shared keys.
            (optional)
            apply_to: Guest administrator to which this password policy
            applies. (optional)
            minimum_length: Minimum password length (12 - 128, default = 12).
            (optional)
            min_lower_case_letter: Minimum number of lowercase characters in
            password (0 - 128, default = 1). (optional)
            min_upper_case_letter: Minimum number of uppercase characters in
            password (0 - 128, default = 1). (optional)
            min_non_alphanumeric: Minimum number of non-alphanumeric characters
            in password (0 - 128, default = 1). (optional)
            min_number: Minimum number of numeric characters in password (0 -
            128, default = 1). (optional)
            expire_status: Enable/disable password expiration. (optional)
            expire_day: Number of days after which passwords expire (1 - 999
            days, default = 90). (optional)
            reuse_password: Enable/disable reuse of password. (optional)
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
        endpoint = "/system/password-policy-guest-admin"
        if before is not None:
            data_payload["before"] = before
        if after is not None:
            data_payload["after"] = after
        if status is not None:
            data_payload["status"] = status
        if apply_to is not None:
            data_payload["apply-to"] = apply_to
        if minimum_length is not None:
            data_payload["minimum-length"] = minimum_length
        if min_lower_case_letter is not None:
            data_payload["min-lower-case-letter"] = min_lower_case_letter
        if min_upper_case_letter is not None:
            data_payload["min-upper-case-letter"] = min_upper_case_letter
        if min_non_alphanumeric is not None:
            data_payload["min-non-alphanumeric"] = min_non_alphanumeric
        if min_number is not None:
            data_payload["min-number"] = min_number
        if expire_status is not None:
            data_payload["expire-status"] = expire_status
        if expire_day is not None:
            data_payload["expire-day"] = expire_day
        if reuse_password is not None:
            data_payload["reuse-password"] = reuse_password
        if reuse_password_limit is not None:
            data_payload["reuse-password-limit"] = reuse_password_limit
        data_payload.update(kwargs)
        return self._client.put(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )
