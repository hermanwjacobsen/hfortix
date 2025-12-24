"""
FortiOS CMDB - Cmdb Switch Controller 802 1x Settings

Configuration endpoint for managing cmdb switch controller 802 1x settings
objects.

API Endpoints:
    GET    /cmdb/switch-controller/_802_1X_settings
    PUT    /cmdb/switch-controller/_802_1X_settings/{identifier}

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.switch_controller._802_1X_settings.get()
    >>>
    >>> # Get specific item (if supported)
    >>> item =
    fgt.api.cmdb.switch_controller._802_1X_settings.get(name="item_name")
    >>>
    >>> # Create new item (use POST)
    >>> result = fgt.api.cmdb.switch_controller._802_1X_settings.post(
    ...     name="new_item",
    ...     # ... additional parameters
    ... )
    >>>
    >>> # Update existing item (use PUT)
    >>> result = fgt.api.cmdb.switch_controller._802_1X_settings.put(
    ...     name="existing_item",
    ...     # ... parameters to update
    ... )
    >>>
    >>> # Delete item
    >>> result =
    fgt.api.cmdb.switch_controller._802_1X_settings.delete(name="item_name")

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


class Eight02OneXSettings:
    """
    Eight02Onexsettings Operations.

    Provides CRUD operations for FortiOS eight02onexsettings configuration.

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
        Initialize Eight02OneXSettings endpoint.

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
        endpoint = "/switch-controller/802-1X-settings"
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
        link_down_auth: str | None = None,
        reauth_period: int | None = None,
        max_reauth_attempt: int | None = None,
        tx_period: int | None = None,
        mab_reauth: str | None = None,
        mac_username_delimiter: str | None = None,
        mac_password_delimiter: str | None = None,
        mac_calling_station_delimiter: str | None = None,
        mac_called_station_delimiter: str | None = None,
        mac_case: str | None = None,
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
            link_down_auth: Interface-reauthentication state to set if a link
            is down. (optional)
            reauth_period: Period of time to allow for reauthentication (1 -
            1440 sec, default = 60, 0 = disable reauthentication). (optional)
            max_reauth_attempt: Maximum number of authentication attempts (0 -
            15, default = 3). (optional)
            tx_period: 802.1X Tx period (seconds, default=30). (optional)
            mab_reauth: Enable/disable MAB re-authentication. (optional)
            mac_username_delimiter: MAC authentication username delimiter
            (default = hyphen). (optional)
            mac_password_delimiter: MAC authentication password delimiter
            (default = hyphen). (optional)
            mac_calling_station_delimiter: MAC calling station delimiter
            (default = hyphen). (optional)
            mac_called_station_delimiter: MAC called station delimiter (default
            = hyphen). (optional)
            mac_case: MAC case (default = lowercase). (optional)
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
        endpoint = "/switch-controller/802-1X-settings"
        if before is not None:
            data_payload["before"] = before
        if after is not None:
            data_payload["after"] = after
        if link_down_auth is not None:
            data_payload["link-down-auth"] = link_down_auth
        if reauth_period is not None:
            data_payload["reauth-period"] = reauth_period
        if max_reauth_attempt is not None:
            data_payload["max-reauth-attempt"] = max_reauth_attempt
        if tx_period is not None:
            data_payload["tx-period"] = tx_period
        if mab_reauth is not None:
            data_payload["mab-reauth"] = mab_reauth
        if mac_username_delimiter is not None:
            data_payload["mac-username-delimiter"] = mac_username_delimiter
        if mac_password_delimiter is not None:
            data_payload["mac-password-delimiter"] = mac_password_delimiter
        if mac_calling_station_delimiter is not None:
            data_payload["mac-calling-station-delimiter"] = (
                mac_calling_station_delimiter
            )
        if mac_called_station_delimiter is not None:
            data_payload["mac-called-station-delimiter"] = (
                mac_called_station_delimiter
            )
        if mac_case is not None:
            data_payload["mac-case"] = mac_case
        data_payload.update(kwargs)
        return self._client.put(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )
