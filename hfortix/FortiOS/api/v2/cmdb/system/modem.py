"""
FortiOS CMDB - Cmdb System Modem

Configuration endpoint for managing cmdb system modem objects.

API Endpoints:
    GET    /cmdb/system/modem
    PUT    /cmdb/system/modem/{identifier}

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.system.modem.get()
    >>>
    >>> # Get specific item (if supported)
    >>> item = fgt.api.cmdb.system.modem.get(name="item_name")
    >>>
    >>> # Create new item (use POST)
    >>> result = fgt.api.cmdb.system.modem.post(
    ...     name="new_item",
    ...     # ... additional parameters
    ... )
    >>>
    >>> # Update existing item (use PUT)
    >>> result = fgt.api.cmdb.system.modem.put(
    ...     name="existing_item",
    ...     # ... parameters to update
    ... )
    >>>
    >>> # Delete item
    >>> result = fgt.api.cmdb.system.modem.delete(name="item_name")

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


class Modem:
    """
    Modem Operations.

    Provides CRUD operations for FortiOS modem configuration.

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
        Initialize Modem endpoint.

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
        endpoint = "/system/modem"
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
        pin_init: str | None = None,
        network_init: str | None = None,
        lockdown_lac: str | None = None,
        mode: str | None = None,
        auto_dial: str | None = None,
        dial_on_demand: str | None = None,
        idle_timer: int | None = None,
        redial: str | None = None,
        reset: int | None = None,
        holddown_timer: int | None = None,
        connect_timeout: int | None = None,
        interface: str | None = None,
        wireless_port: int | None = None,
        dont_send_CR1: str | None = None,
        phone1: str | None = None,
        dial_cmd1: str | None = None,
        username1: str | None = None,
        passwd1: str | None = None,
        extra_init1: str | None = None,
        peer_modem1: str | None = None,
        ppp_echo_request1: str | None = None,
        authtype1: str | None = None,
        dont_send_CR2: str | None = None,
        phone2: str | None = None,
        dial_cmd2: str | None = None,
        username2: str | None = None,
        passwd2: str | None = None,
        extra_init2: str | None = None,
        peer_modem2: str | None = None,
        ppp_echo_request2: str | None = None,
        authtype2: str | None = None,
        dont_send_CR3: str | None = None,
        phone3: str | None = None,
        dial_cmd3: str | None = None,
        username3: str | None = None,
        passwd3: str | None = None,
        extra_init3: str | None = None,
        peer_modem3: str | None = None,
        ppp_echo_request3: str | None = None,
        altmode: str | None = None,
        authtype3: str | None = None,
        traffic_check: str | None = None,
        distance: int | None = None,
        priority: int | None = None,
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
            status: Enable/disable Modem support (equivalent to bringing an
            interface up or down). (optional)
            pin_init: AT command to set the PIN (AT+PIN=<pin>). (optional)
            network_init: AT command to set the Network name/type
            (AT+COPS=<mode>,[<format>,<oper>[,<AcT>]]). (optional)
            lockdown_lac: Allow connection only to the specified Location Area
            Code (LAC). (optional)
            mode: Set MODEM operation mode to redundant or standalone.
            (optional)
            auto_dial: Enable/disable auto-dial after a reboot or
            disconnection. (optional)
            dial_on_demand: Enable/disable to dial the modem when packets are
            routed to the modem interface. (optional)
            idle_timer: MODEM connection idle time (1 - 9999 min, default = 5).
            (optional)
            redial: Redial limit (1 - 10 attempts, none = redial forever).
            (optional)
            reset: Number of dial attempts before resetting modem (0 = never
            reset). (optional)
            holddown_timer: Hold down timer in seconds (1 - 60 sec). (optional)
            connect_timeout: Connection completion timeout (30 - 255 sec,
            default = 90). (optional)
            interface: Name of redundant interface. (optional)
            wireless_port: Enter wireless port number: 0 for default, 1 for
            first port, and so on (0 - 4294967295). (optional)
            dont_send_CR1: Do not send CR when connected (ISP1). (optional)
            phone1: Phone number to connect to the dialup account (must not
            contain spaces, and should include standard special characters).
            (optional)
            dial_cmd1: Dial command (this is often an ATD or ATDT command).
            (optional)
            username1: User name to access the specified dialup account.
            (optional)
            passwd1: Password to access the specified dialup account.
            (optional)
            extra_init1: Extra initialization string to ISP 1. (optional)
            peer_modem1: Specify peer MODEM type for phone1. (optional)
            ppp_echo_request1: Enable/disable PPP echo-request to ISP 1.
            (optional)
            authtype1: Allowed authentication types for ISP 1. (optional)
            dont_send_CR2: Do not send CR when connected (ISP2). (optional)
            phone2: Phone number to connect to the dialup account (must not
            contain spaces, and should include standard special characters).
            (optional)
            dial_cmd2: Dial command (this is often an ATD or ATDT command).
            (optional)
            username2: User name to access the specified dialup account.
            (optional)
            passwd2: Password to access the specified dialup account.
            (optional)
            extra_init2: Extra initialization string to ISP 2. (optional)
            peer_modem2: Specify peer MODEM type for phone2. (optional)
            ppp_echo_request2: Enable/disable PPP echo-request to ISP 2.
            (optional)
            authtype2: Allowed authentication types for ISP 2. (optional)
            dont_send_CR3: Do not send CR when connected (ISP3). (optional)
            phone3: Phone number to connect to the dialup account (must not
            contain spaces, and should include standard special characters).
            (optional)
            dial_cmd3: Dial command (this is often an ATD or ATDT command).
            (optional)
            username3: User name to access the specified dialup account.
            (optional)
            passwd3: Password to access the specified dialup account.
            (optional)
            extra_init3: Extra initialization string to ISP 3. (optional)
            peer_modem3: Specify peer MODEM type for phone3. (optional)
            ppp_echo_request3: Enable/disable PPP echo-request to ISP 3.
            (optional)
            altmode: Enable/disable altmode for installations using PPP in
            China. (optional)
            authtype3: Allowed authentication types for ISP 3. (optional)
            traffic_check: Enable/disable traffic-check. (optional)
            distance: Distance of learned routes (1 - 255, default = 1).
            (optional)
            priority: Priority of learned routes (1 - 65535, default = 1).
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
        endpoint = "/system/modem"
        if before is not None:
            data_payload["before"] = before
        if after is not None:
            data_payload["after"] = after
        if status is not None:
            data_payload["status"] = status
        if pin_init is not None:
            data_payload["pin-init"] = pin_init
        if network_init is not None:
            data_payload["network-init"] = network_init
        if lockdown_lac is not None:
            data_payload["lockdown-lac"] = lockdown_lac
        if mode is not None:
            data_payload["mode"] = mode
        if auto_dial is not None:
            data_payload["auto-dial"] = auto_dial
        if dial_on_demand is not None:
            data_payload["dial-on-demand"] = dial_on_demand
        if idle_timer is not None:
            data_payload["idle-timer"] = idle_timer
        if redial is not None:
            data_payload["redial"] = redial
        if reset is not None:
            data_payload["reset"] = reset
        if holddown_timer is not None:
            data_payload["holddown-timer"] = holddown_timer
        if connect_timeout is not None:
            data_payload["connect-timeout"] = connect_timeout
        if interface is not None:
            data_payload["interface"] = interface
        if wireless_port is not None:
            data_payload["wireless-port"] = wireless_port
        if dont_send_CR1 is not None:
            data_payload["dont-send-CR1"] = dont_send_CR1
        if phone1 is not None:
            data_payload["phone1"] = phone1
        if dial_cmd1 is not None:
            data_payload["dial-cmd1"] = dial_cmd1
        if username1 is not None:
            data_payload["username1"] = username1
        if passwd1 is not None:
            data_payload["passwd1"] = passwd1
        if extra_init1 is not None:
            data_payload["extra-init1"] = extra_init1
        if peer_modem1 is not None:
            data_payload["peer-modem1"] = peer_modem1
        if ppp_echo_request1 is not None:
            data_payload["ppp-echo-request1"] = ppp_echo_request1
        if authtype1 is not None:
            data_payload["authtype1"] = authtype1
        if dont_send_CR2 is not None:
            data_payload["dont-send-CR2"] = dont_send_CR2
        if phone2 is not None:
            data_payload["phone2"] = phone2
        if dial_cmd2 is not None:
            data_payload["dial-cmd2"] = dial_cmd2
        if username2 is not None:
            data_payload["username2"] = username2
        if passwd2 is not None:
            data_payload["passwd2"] = passwd2
        if extra_init2 is not None:
            data_payload["extra-init2"] = extra_init2
        if peer_modem2 is not None:
            data_payload["peer-modem2"] = peer_modem2
        if ppp_echo_request2 is not None:
            data_payload["ppp-echo-request2"] = ppp_echo_request2
        if authtype2 is not None:
            data_payload["authtype2"] = authtype2
        if dont_send_CR3 is not None:
            data_payload["dont-send-CR3"] = dont_send_CR3
        if phone3 is not None:
            data_payload["phone3"] = phone3
        if dial_cmd3 is not None:
            data_payload["dial-cmd3"] = dial_cmd3
        if username3 is not None:
            data_payload["username3"] = username3
        if passwd3 is not None:
            data_payload["passwd3"] = passwd3
        if extra_init3 is not None:
            data_payload["extra-init3"] = extra_init3
        if peer_modem3 is not None:
            data_payload["peer-modem3"] = peer_modem3
        if ppp_echo_request3 is not None:
            data_payload["ppp-echo-request3"] = ppp_echo_request3
        if altmode is not None:
            data_payload["altmode"] = altmode
        if authtype3 is not None:
            data_payload["authtype3"] = authtype3
        if traffic_check is not None:
            data_payload["traffic-check"] = traffic_check
        if distance is not None:
            data_payload["distance"] = distance
        if priority is not None:
            data_payload["priority"] = priority
        data_payload.update(kwargs)
        return self._client.put(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )
