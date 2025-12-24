"""
FortiOS CMDB - Cmdb Extension Controller Dataplan

Configuration endpoint for managing cmdb extension controller dataplan objects.

API Endpoints:
    GET    /cmdb/extension-controller/dataplan
    POST   /cmdb/extension-controller/dataplan
    GET    /cmdb/extension-controller/dataplan
    PUT    /cmdb/extension-controller/dataplan/{identifier}
    DELETE /cmdb/extension-controller/dataplan/{identifier}

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.extension_controller.dataplan.get()
    >>>
    >>> # Get specific item (if supported)
    >>> item = fgt.api.cmdb.extension_controller.dataplan.get(name="item_name")
    >>>
    >>> # Create new item (use POST)
    >>> result = fgt.api.cmdb.extension_controller.dataplan.post(
    ...     name="new_item",
    ...     # ... additional parameters
    ... )
    >>>
    >>> # Update existing item (use PUT)
    >>> result = fgt.api.cmdb.extension_controller.dataplan.put(
    ...     name="existing_item",
    ...     # ... parameters to update
    ... )
    >>>
    >>> # Delete item
    >>> result =
    fgt.api.cmdb.extension_controller.dataplan.delete(name="item_name")

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


class Dataplan:
    """
    Dataplan Operations.

    Provides CRUD operations for FortiOS dataplan configuration.

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
        Initialize Dataplan endpoint.

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
            endpoint = f"/extension-controller/dataplan/{name}"
        else:
            endpoint = "/extension-controller/dataplan"
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
        modem_id: str | None = None,
        type: str | None = None,
        slot: str | None = None,
        iccid: str | None = None,
        carrier: str | None = None,
        apn: str | None = None,
        auth_type: str | None = None,
        username: str | None = None,
        password: str | None = None,
        pdn: str | None = None,
        signal_threshold: int | None = None,
        signal_period: int | None = None,
        capacity: int | None = None,
        monthly_fee: int | None = None,
        billing_date: int | None = None,
        overage: str | None = None,
        preferred_subnet: int | None = None,
        private_network: str | None = None,
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
            name: FortiExtender data plan name. (optional)
            modem_id: Dataplan's modem specifics, if any. (optional)
            type: Type preferences configuration. (optional)
            slot: SIM slot configuration. (optional)
            iccid: ICCID configuration. (optional)
            carrier: Carrier configuration. (optional)
            apn: APN configuration. (optional)
            auth_type: Authentication type. (optional)
            username: Username. (optional)
            password: Password. (optional)
            pdn: PDN type. (optional)
            signal_threshold: Signal threshold. Specify the range between 50 -
            100, where 50/100 means -50/-100 dBm. (optional)
            signal_period: Signal period (600 to 18000 seconds). (optional)
            capacity: Capacity in MB (0 - 102400000). (optional)
            monthly_fee: Monthly fee of dataplan (0 - 100000, in local
            currency). (optional)
            billing_date: Billing day of the month (1 - 31). (optional)
            overage: Enable/disable dataplan overage detection. (optional)
            preferred_subnet: Preferred subnet mask (0 - 32). (optional)
            private_network: Enable/disable dataplan private network support.
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
        endpoint = f"/extension-controller/dataplan/{name}"
        if before is not None:
            data_payload["before"] = before
        if after is not None:
            data_payload["after"] = after
        if name is not None:
            data_payload["name"] = name
        if modem_id is not None:
            data_payload["modem-id"] = modem_id
        if type is not None:
            data_payload["type"] = type
        if slot is not None:
            data_payload["slot"] = slot
        if iccid is not None:
            data_payload["iccid"] = iccid
        if carrier is not None:
            data_payload["carrier"] = carrier
        if apn is not None:
            data_payload["apn"] = apn
        if auth_type is not None:
            data_payload["auth-type"] = auth_type
        if username is not None:
            data_payload["username"] = username
        if password is not None:
            data_payload["password"] = password
        if pdn is not None:
            data_payload["pdn"] = pdn
        if signal_threshold is not None:
            data_payload["signal-threshold"] = signal_threshold
        if signal_period is not None:
            data_payload["signal-period"] = signal_period
        if capacity is not None:
            data_payload["capacity"] = capacity
        if monthly_fee is not None:
            data_payload["monthly-fee"] = monthly_fee
        if billing_date is not None:
            data_payload["billing-date"] = billing_date
        if overage is not None:
            data_payload["overage"] = overage
        if preferred_subnet is not None:
            data_payload["preferred-subnet"] = preferred_subnet
        if private_network is not None:
            data_payload["private-network"] = private_network
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
        endpoint = f"/extension-controller/dataplan/{name}"
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
        modem_id: str | None = None,
        type: str | None = None,
        slot: str | None = None,
        iccid: str | None = None,
        carrier: str | None = None,
        apn: str | None = None,
        auth_type: str | None = None,
        username: str | None = None,
        password: str | None = None,
        pdn: str | None = None,
        signal_threshold: int | None = None,
        signal_period: int | None = None,
        capacity: int | None = None,
        monthly_fee: int | None = None,
        billing_date: int | None = None,
        overage: str | None = None,
        preferred_subnet: int | None = None,
        private_network: str | None = None,
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
            name: FortiExtender data plan name. (optional)
            modem_id: Dataplan's modem specifics, if any. (optional)
            type: Type preferences configuration. (optional)
            slot: SIM slot configuration. (optional)
            iccid: ICCID configuration. (optional)
            carrier: Carrier configuration. (optional)
            apn: APN configuration. (optional)
            auth_type: Authentication type. (optional)
            username: Username. (optional)
            password: Password. (optional)
            pdn: PDN type. (optional)
            signal_threshold: Signal threshold. Specify the range between 50 -
            100, where 50/100 means -50/-100 dBm. (optional)
            signal_period: Signal period (600 to 18000 seconds). (optional)
            capacity: Capacity in MB (0 - 102400000). (optional)
            monthly_fee: Monthly fee of dataplan (0 - 100000, in local
            currency). (optional)
            billing_date: Billing day of the month (1 - 31). (optional)
            overage: Enable/disable dataplan overage detection. (optional)
            preferred_subnet: Preferred subnet mask (0 - 32). (optional)
            private_network: Enable/disable dataplan private network support.
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
        endpoint = "/extension-controller/dataplan"
        if nkey is not None:
            data_payload["nkey"] = nkey
        if name is not None:
            data_payload["name"] = name
        if modem_id is not None:
            data_payload["modem-id"] = modem_id
        if type is not None:
            data_payload["type"] = type
        if slot is not None:
            data_payload["slot"] = slot
        if iccid is not None:
            data_payload["iccid"] = iccid
        if carrier is not None:
            data_payload["carrier"] = carrier
        if apn is not None:
            data_payload["apn"] = apn
        if auth_type is not None:
            data_payload["auth-type"] = auth_type
        if username is not None:
            data_payload["username"] = username
        if password is not None:
            data_payload["password"] = password
        if pdn is not None:
            data_payload["pdn"] = pdn
        if signal_threshold is not None:
            data_payload["signal-threshold"] = signal_threshold
        if signal_period is not None:
            data_payload["signal-period"] = signal_period
        if capacity is not None:
            data_payload["capacity"] = capacity
        if monthly_fee is not None:
            data_payload["monthly-fee"] = monthly_fee
        if billing_date is not None:
            data_payload["billing-date"] = billing_date
        if overage is not None:
            data_payload["overage"] = overage
        if preferred_subnet is not None:
            data_payload["preferred-subnet"] = preferred_subnet
        if private_network is not None:
            data_payload["private-network"] = private_network
        data_payload.update(kwargs)
        return self._client.post(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )
