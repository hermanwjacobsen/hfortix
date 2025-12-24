"""
FortiOS CMDB - Cmdb User Nac Policy

Configuration endpoint for managing cmdb user nac policy objects.

API Endpoints:
    GET    /cmdb/user/nac_policy
    POST   /cmdb/user/nac_policy
    GET    /cmdb/user/nac_policy
    PUT    /cmdb/user/nac_policy/{identifier}
    DELETE /cmdb/user/nac_policy/{identifier}

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.user.nac_policy.get()
    >>>
    >>> # Get specific item (if supported)
    >>> item = fgt.api.cmdb.user.nac_policy.get(name="item_name")
    >>>
    >>> # Create new item (use POST)
    >>> result = fgt.api.cmdb.user.nac_policy.post(
    ...     name="new_item",
    ...     # ... additional parameters
    ... )
    >>>
    >>> # Update existing item (use PUT)
    >>> result = fgt.api.cmdb.user.nac_policy.put(
    ...     name="existing_item",
    ...     # ... parameters to update
    ... )
    >>>
    >>> # Delete item
    >>> result = fgt.api.cmdb.user.nac_policy.delete(name="item_name")

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


class NacPolicy:
    """
    Nacpolicy Operations.

    Provides CRUD operations for FortiOS nacpolicy configuration.

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
        Initialize NacPolicy endpoint.

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
            endpoint = f"/user/nac-policy/{name}"
        else:
            endpoint = "/user/nac-policy"
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
        description: str | None = None,
        category: str | None = None,
        status: str | None = None,
        match_type: str | None = None,
        match_period: int | None = None,
        match_remove: str | None = None,
        mac: str | None = None,
        hw_vendor: str | None = None,
        type: str | None = None,
        family: str | None = None,
        os: str | None = None,
        hw_version: str | None = None,
        sw_version: str | None = None,
        host: str | None = None,
        user: str | None = None,
        src: str | None = None,
        user_group: str | None = None,
        ems_tag: str | None = None,
        fortivoice_tag: str | None = None,
        severity: list | None = None,
        switch_fortilink: str | None = None,
        switch_group: list | None = None,
        switch_mac_policy: str | None = None,
        firewall_address: str | None = None,
        ssid_policy: str | None = None,
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
            name: NAC policy name. (optional)
            description: Description for the NAC policy matching pattern.
            (optional)
            category: Category of NAC policy. (optional)
            status: Enable/disable NAC policy. (optional)
            match_type: Match and retain the devices based on the type.
            (optional)
            match_period: Number of days the matched devices will be retained
            (0 - always retain) (optional)
            match_remove: Options to remove the matched override devices.
            (optional)
            mac: NAC policy matching MAC address. (optional)
            hw_vendor: NAC policy matching hardware vendor. (optional)
            type: NAC policy matching type. (optional)
            family: NAC policy matching family. (optional)
            os: NAC policy matching operating system. (optional)
            hw_version: NAC policy matching hardware version. (optional)
            sw_version: NAC policy matching software version. (optional)
            host: NAC policy matching host. (optional)
            user: NAC policy matching user. (optional)
            src: NAC policy matching source. (optional)
            user_group: NAC policy matching user group. (optional)
            ems_tag: NAC policy matching EMS tag. (optional)
            fortivoice_tag: NAC policy matching FortiVoice tag. (optional)
            severity: NAC policy matching devices vulnerability severity lists.
            (optional)
            switch_fortilink: FortiLink interface for which this NAC policy
            belongs to. (optional)
            switch_group: List of managed FortiSwitch groups on which NAC
            policy can be applied. (optional)
            switch_mac_policy: Switch MAC policy action to be applied on the
            matched NAC policy. (optional)
            firewall_address: Dynamic firewall address to associate MAC which
            match this policy. (optional)
            ssid_policy: SSID policy to be applied on the matched NAC policy.
            (optional)
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
        endpoint = f"/user/nac-policy/{name}"
        if before is not None:
            data_payload["before"] = before
        if after is not None:
            data_payload["after"] = after
        if name is not None:
            data_payload["name"] = name
        if description is not None:
            data_payload["description"] = description
        if category is not None:
            data_payload["category"] = category
        if status is not None:
            data_payload["status"] = status
        if match_type is not None:
            data_payload["match-type"] = match_type
        if match_period is not None:
            data_payload["match-period"] = match_period
        if match_remove is not None:
            data_payload["match-remove"] = match_remove
        if mac is not None:
            data_payload["mac"] = mac
        if hw_vendor is not None:
            data_payload["hw-vendor"] = hw_vendor
        if type is not None:
            data_payload["type"] = type
        if family is not None:
            data_payload["family"] = family
        if os is not None:
            data_payload["os"] = os
        if hw_version is not None:
            data_payload["hw-version"] = hw_version
        if sw_version is not None:
            data_payload["sw-version"] = sw_version
        if host is not None:
            data_payload["host"] = host
        if user is not None:
            data_payload["user"] = user
        if src is not None:
            data_payload["src"] = src
        if user_group is not None:
            data_payload["user-group"] = user_group
        if ems_tag is not None:
            data_payload["ems-tag"] = ems_tag
        if fortivoice_tag is not None:
            data_payload["fortivoice-tag"] = fortivoice_tag
        if severity is not None:
            data_payload["severity"] = severity
        if switch_fortilink is not None:
            data_payload["switch-fortilink"] = switch_fortilink
        if switch_group is not None:
            data_payload["switch-group"] = switch_group
        if switch_mac_policy is not None:
            data_payload["switch-mac-policy"] = switch_mac_policy
        if firewall_address is not None:
            data_payload["firewall-address"] = firewall_address
        if ssid_policy is not None:
            data_payload["ssid-policy"] = ssid_policy
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
        endpoint = f"/user/nac-policy/{name}"
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
        description: str | None = None,
        category: str | None = None,
        status: str | None = None,
        match_type: str | None = None,
        match_period: int | None = None,
        match_remove: str | None = None,
        mac: str | None = None,
        hw_vendor: str | None = None,
        type: str | None = None,
        family: str | None = None,
        os: str | None = None,
        hw_version: str | None = None,
        sw_version: str | None = None,
        host: str | None = None,
        user: str | None = None,
        src: str | None = None,
        user_group: str | None = None,
        ems_tag: str | None = None,
        fortivoice_tag: str | None = None,
        severity: list | None = None,
        switch_fortilink: str | None = None,
        switch_group: list | None = None,
        switch_mac_policy: str | None = None,
        firewall_address: str | None = None,
        ssid_policy: str | None = None,
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
            name: NAC policy name. (optional)
            description: Description for the NAC policy matching pattern.
            (optional)
            category: Category of NAC policy. (optional)
            status: Enable/disable NAC policy. (optional)
            match_type: Match and retain the devices based on the type.
            (optional)
            match_period: Number of days the matched devices will be retained
            (0 - always retain) (optional)
            match_remove: Options to remove the matched override devices.
            (optional)
            mac: NAC policy matching MAC address. (optional)
            hw_vendor: NAC policy matching hardware vendor. (optional)
            type: NAC policy matching type. (optional)
            family: NAC policy matching family. (optional)
            os: NAC policy matching operating system. (optional)
            hw_version: NAC policy matching hardware version. (optional)
            sw_version: NAC policy matching software version. (optional)
            host: NAC policy matching host. (optional)
            user: NAC policy matching user. (optional)
            src: NAC policy matching source. (optional)
            user_group: NAC policy matching user group. (optional)
            ems_tag: NAC policy matching EMS tag. (optional)
            fortivoice_tag: NAC policy matching FortiVoice tag. (optional)
            severity: NAC policy matching devices vulnerability severity lists.
            (optional)
            switch_fortilink: FortiLink interface for which this NAC policy
            belongs to. (optional)
            switch_group: List of managed FortiSwitch groups on which NAC
            policy can be applied. (optional)
            switch_mac_policy: Switch MAC policy action to be applied on the
            matched NAC policy. (optional)
            firewall_address: Dynamic firewall address to associate MAC which
            match this policy. (optional)
            ssid_policy: SSID policy to be applied on the matched NAC policy.
            (optional)
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
        endpoint = "/user/nac-policy"
        if nkey is not None:
            data_payload["nkey"] = nkey
        if name is not None:
            data_payload["name"] = name
        if description is not None:
            data_payload["description"] = description
        if category is not None:
            data_payload["category"] = category
        if status is not None:
            data_payload["status"] = status
        if match_type is not None:
            data_payload["match-type"] = match_type
        if match_period is not None:
            data_payload["match-period"] = match_period
        if match_remove is not None:
            data_payload["match-remove"] = match_remove
        if mac is not None:
            data_payload["mac"] = mac
        if hw_vendor is not None:
            data_payload["hw-vendor"] = hw_vendor
        if type is not None:
            data_payload["type"] = type
        if family is not None:
            data_payload["family"] = family
        if os is not None:
            data_payload["os"] = os
        if hw_version is not None:
            data_payload["hw-version"] = hw_version
        if sw_version is not None:
            data_payload["sw-version"] = sw_version
        if host is not None:
            data_payload["host"] = host
        if user is not None:
            data_payload["user"] = user
        if src is not None:
            data_payload["src"] = src
        if user_group is not None:
            data_payload["user-group"] = user_group
        if ems_tag is not None:
            data_payload["ems-tag"] = ems_tag
        if fortivoice_tag is not None:
            data_payload["fortivoice-tag"] = fortivoice_tag
        if severity is not None:
            data_payload["severity"] = severity
        if switch_fortilink is not None:
            data_payload["switch-fortilink"] = switch_fortilink
        if switch_group is not None:
            data_payload["switch-group"] = switch_group
        if switch_mac_policy is not None:
            data_payload["switch-mac-policy"] = switch_mac_policy
        if firewall_address is not None:
            data_payload["firewall-address"] = firewall_address
        if ssid_policy is not None:
            data_payload["ssid-policy"] = ssid_policy
        data_payload.update(kwargs)
        return self._client.post(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )
