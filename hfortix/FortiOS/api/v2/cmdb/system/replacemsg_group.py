"""
FortiOS CMDB - Cmdb System Replacemsg Group

Configuration endpoint for managing cmdb system replacemsg group objects.

API Endpoints:
    GET    /cmdb/system/replacemsg_group
    POST   /cmdb/system/replacemsg_group
    GET    /cmdb/system/replacemsg_group
    PUT    /cmdb/system/replacemsg_group/{identifier}
    DELETE /cmdb/system/replacemsg_group/{identifier}

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.system.replacemsg_group.get()
    >>>
    >>> # Get specific item (if supported)
    >>> item = fgt.api.cmdb.system.replacemsg_group.get(name="item_name")
    >>>
    >>> # Create new item (use POST)
    >>> result = fgt.api.cmdb.system.replacemsg_group.post(
    ...     name="new_item",
    ...     # ... additional parameters
    ... )
    >>>
    >>> # Update existing item (use PUT)
    >>> result = fgt.api.cmdb.system.replacemsg_group.put(
    ...     name="existing_item",
    ...     # ... parameters to update
    ... )
    >>>
    >>> # Delete item
    >>> result = fgt.api.cmdb.system.replacemsg_group.delete(name="item_name")

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


class ReplacemsgGroup:
    """
    Replacemsggroup Operations.

    Provides CRUD operations for FortiOS replacemsggroup configuration.

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
        Initialize ReplacemsgGroup endpoint.

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
            endpoint = f"/system/replacemsg-group/{name}"
        else:
            endpoint = "/system/replacemsg-group"
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
        comment: str | None = None,
        group_type: str | None = None,
        mail: list | None = None,
        http: list | None = None,
        fortiguard_wf: list | None = None,
        spam: list | None = None,
        alertmail: list | None = None,
        admin: list | None = None,
        auth: list | None = None,
        sslvpn: list | None = None,
        nac_quar: list | None = None,
        traffic_quota: list | None = None,
        utm: list | None = None,
        custom_message: list | None = None,
        automation: list | None = None,
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
            comment: Comment. (optional)
            group_type: Group type. (optional)
            mail: Replacement message table entries. (optional)
            http: Replacement message table entries. (optional)
            fortiguard_wf: Replacement message table entries. (optional)
            spam: Replacement message table entries. (optional)
            alertmail: Replacement message table entries. (optional)
            admin: Replacement message table entries. (optional)
            auth: Replacement message table entries. (optional)
            sslvpn: Replacement message table entries. (optional)
            nac_quar: Replacement message table entries. (optional)
            traffic_quota: Replacement message table entries. (optional)
            utm: Replacement message table entries. (optional)
            custom_message: Replacement message table entries. (optional)
            automation: Replacement message table entries. (optional)
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
        endpoint = f"/system/replacemsg-group/{name}"
        if before is not None:
            data_payload["before"] = before
        if after is not None:
            data_payload["after"] = after
        if name is not None:
            data_payload["name"] = name
        if comment is not None:
            data_payload["comment"] = comment
        if group_type is not None:
            data_payload["group-type"] = group_type
        if mail is not None:
            data_payload["mail"] = mail
        if http is not None:
            data_payload["http"] = http
        if fortiguard_wf is not None:
            data_payload["fortiguard-w"] = fortiguard_wf
        if spam is not None:
            data_payload["spam"] = spam
        if alertmail is not None:
            data_payload["alertmail"] = alertmail
        if admin is not None:
            data_payload["admin"] = admin
        if auth is not None:
            data_payload["auth"] = auth
        if sslvpn is not None:
            data_payload["sslvpn"] = sslvpn
        if nac_quar is not None:
            data_payload["nac-quar"] = nac_quar
        if traffic_quota is not None:
            data_payload["traffic-quota"] = traffic_quota
        if utm is not None:
            data_payload["utm"] = utm
        if custom_message is not None:
            data_payload["custom-message"] = custom_message
        if automation is not None:
            data_payload["automation"] = automation
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
        endpoint = f"/system/replacemsg-group/{name}"
        params.update(kwargs)
        return self._client.delete(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )

    def post(
        self,
        payload_dict: dict[str, Any] | None = None,
        nkey: str | None = None,
        name: str | None = None,
        comment: str | None = None,
        group_type: str | None = None,
        mail: list | None = None,
        http: list | None = None,
        fortiguard_wf: list | None = None,
        spam: list | None = None,
        alertmail: list | None = None,
        admin: list | None = None,
        auth: list | None = None,
        sslvpn: list | None = None,
        nac_quar: list | None = None,
        traffic_quota: list | None = None,
        utm: list | None = None,
        custom_message: list | None = None,
        automation: list | None = None,
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
            comment: Comment. (optional)
            group_type: Group type. (optional)
            mail: Replacement message table entries. (optional)
            http: Replacement message table entries. (optional)
            fortiguard_wf: Replacement message table entries. (optional)
            spam: Replacement message table entries. (optional)
            alertmail: Replacement message table entries. (optional)
            admin: Replacement message table entries. (optional)
            auth: Replacement message table entries. (optional)
            sslvpn: Replacement message table entries. (optional)
            nac_quar: Replacement message table entries. (optional)
            traffic_quota: Replacement message table entries. (optional)
            utm: Replacement message table entries. (optional)
            custom_message: Replacement message table entries. (optional)
            automation: Replacement message table entries. (optional)
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
        endpoint = "/system/replacemsg-group"
        if nkey is not None:
            data_payload["nkey"] = nkey
        if name is not None:
            data_payload["name"] = name
        if comment is not None:
            data_payload["comment"] = comment
        if group_type is not None:
            data_payload["group-type"] = group_type
        if mail is not None:
            data_payload["mail"] = mail
        if http is not None:
            data_payload["http"] = http
        if fortiguard_wf is not None:
            data_payload["fortiguard-w"] = fortiguard_wf
        if spam is not None:
            data_payload["spam"] = spam
        if alertmail is not None:
            data_payload["alertmail"] = alertmail
        if admin is not None:
            data_payload["admin"] = admin
        if auth is not None:
            data_payload["auth"] = auth
        if sslvpn is not None:
            data_payload["sslvpn"] = sslvpn
        if nac_quar is not None:
            data_payload["nac-quar"] = nac_quar
        if traffic_quota is not None:
            data_payload["traffic-quota"] = traffic_quota
        if utm is not None:
            data_payload["utm"] = utm
        if custom_message is not None:
            data_payload["custom-message"] = custom_message
        if automation is not None:
            data_payload["automation"] = automation
        data_payload.update(kwargs)
        return self._client.post(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )
