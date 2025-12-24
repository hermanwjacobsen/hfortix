"""
FortiOS CMDB - Cmdb Firewall Interface Policy6

Configuration endpoint for managing cmdb firewall interface policy6 objects.

API Endpoints:
    GET    /cmdb/firewall/interface_policy6
    POST   /cmdb/firewall/interface_policy6
    GET    /cmdb/firewall/interface_policy6
    PUT    /cmdb/firewall/interface_policy6/{identifier}
    DELETE /cmdb/firewall/interface_policy6/{identifier}

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.firewall.interface_policy6.get()
    >>>
    >>> # Get specific item (if supported)
    >>> item = fgt.api.cmdb.firewall.interface_policy6.get(name="item_name")
    >>>
    >>> # Create new item (use POST)
    >>> result = fgt.api.cmdb.firewall.interface_policy6.post(
    ...     name="new_item",
    ...     # ... additional parameters
    ... )
    >>>
    >>> # Update existing item (use PUT)
    >>> result = fgt.api.cmdb.firewall.interface_policy6.put(
    ...     name="existing_item",
    ...     # ... parameters to update
    ... )
    >>>
    >>> # Delete item
    >>> result =
    fgt.api.cmdb.firewall.interface_policy6.delete(name="item_name")

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


class InterfacePolicy6:
    """
    Interfacepolicy6 Operations.

    Provides CRUD operations for FortiOS interfacepolicy6 configuration.

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
        Initialize InterfacePolicy6 endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

    def get(
        self,
        policyid: str | None = None,
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
            policyid: Object identifier (optional for list, required for
            specific)
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
        if policyid:
            endpoint = f"/firewall/interface-policy6/{policyid}"
        else:
            endpoint = "/firewall/interface-policy6"
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
        policyid: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        before: str | None = None,
        after: str | None = None,
        uuid: str | None = None,
        status: str | None = None,
        comments: str | None = None,
        logtraffic: str | None = None,
        interface: str | None = None,
        srcaddr6: list | None = None,
        dstaddr6: list | None = None,
        service6: list | None = None,
        application_list_status: str | None = None,
        application_list: str | None = None,
        ips_sensor_status: str | None = None,
        ips_sensor: str | None = None,
        dsri: str | None = None,
        av_profile_status: str | None = None,
        av_profile: str | None = None,
        webfilter_profile_status: str | None = None,
        webfilter_profile: str | None = None,
        casb_profile_status: str | None = None,
        casb_profile: str | None = None,
        emailfilter_profile_status: str | None = None,
        emailfilter_profile: str | None = None,
        dlp_profile_status: str | None = None,
        dlp_profile: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update this specific resource.

        Args:
            payload_dict: Optional dictionary of all parameters (can be passed
            as first positional arg)
            policyid: Object identifier (required)
            before: If *action=move*, use *before* to specify the ID of the
            resource that this resource will be moved before. (optional)
            after: If *action=move*, use *after* to specify the ID of the
            resource that this resource will be moved after. (optional)
            policyid: Policy ID (0 - 4294967295). (optional)
            uuid: Universally Unique Identifier (UUID; automatically assigned
            but can be manually reset). (optional)
            status: Enable/disable this policy. (optional)
            comments: Comments. (optional)
            logtraffic: Logging type to be used in this policy (Options: all |
            utm | disable, Default: utm). (optional)
            interface: Monitored interface name from available interfaces.
            (optional)
            srcaddr6: IPv6 address object to limit traffic monitoring to
            network traffic sent from the specified address or range.
            (optional)
            dstaddr6: IPv6 address object to limit traffic monitoring to
            network traffic sent to the specified address or range. (optional)
            service6: Service name. (optional)
            application_list_status: Enable/disable application control.
            (optional)
            application_list: Application list name. (optional)
            ips_sensor_status: Enable/disable IPS. (optional)
            ips_sensor: IPS sensor name. (optional)
            dsri: Enable/disable DSRI. (optional)
            av_profile_status: Enable/disable antivirus. (optional)
            av_profile: Antivirus profile. (optional)
            webfilter_profile_status: Enable/disable web filtering. (optional)
            webfilter_profile: Web filter profile. (optional)
            casb_profile_status: Enable/disable CASB. (optional)
            casb_profile: CASB profile. (optional)
            emailfilter_profile_status: Enable/disable email filter. (optional)
            emailfilter_profile: Email filter profile. (optional)
            dlp_profile_status: Enable/disable DLP. (optional)
            dlp_profile: DLP profile name. (optional)
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
        if not policyid:
            raise ValueError("policyid is required for put()")
        endpoint = f"/firewall/interface-policy6/{policyid}"
        if before is not None:
            data_payload["before"] = before
        if after is not None:
            data_payload["after"] = after
        if policyid is not None:
            data_payload["policyid"] = policyid
        if uuid is not None:
            data_payload["uuid"] = uuid
        if status is not None:
            data_payload["status"] = status
        if comments is not None:
            data_payload["comments"] = comments
        if logtraffic is not None:
            data_payload["logtraffic"] = logtraffic
        if interface is not None:
            data_payload["interface"] = interface
        if srcaddr6 is not None:
            data_payload["srcaddr6"] = srcaddr6
        if dstaddr6 is not None:
            data_payload["dstaddr6"] = dstaddr6
        if service6 is not None:
            data_payload["service6"] = service6
        if application_list_status is not None:
            data_payload["application-list-status"] = application_list_status
        if application_list is not None:
            data_payload["application-list"] = application_list
        if ips_sensor_status is not None:
            data_payload["ips-sensor-status"] = ips_sensor_status
        if ips_sensor is not None:
            data_payload["ips-sensor"] = ips_sensor
        if dsri is not None:
            data_payload["dsri"] = dsri
        if av_profile_status is not None:
            data_payload["av-profile-status"] = av_profile_status
        if av_profile is not None:
            data_payload["av-profile"] = av_profile
        if webfilter_profile_status is not None:
            data_payload["webfilter-profile-status"] = webfilter_profile_status
        if webfilter_profile is not None:
            data_payload["webfilter-profile"] = webfilter_profile
        if casb_profile_status is not None:
            data_payload["casb-profile-status"] = casb_profile_status
        if casb_profile is not None:
            data_payload["casb-profile"] = casb_profile
        if emailfilter_profile_status is not None:
            data_payload["emailfilter-profile-status"] = (
                emailfilter_profile_status
            )
        if emailfilter_profile is not None:
            data_payload["emailfilter-profile"] = emailfilter_profile
        if dlp_profile_status is not None:
            data_payload["dlp-profile-status"] = dlp_profile_status
        if dlp_profile is not None:
            data_payload["dlp-profile"] = dlp_profile
        data_payload.update(kwargs)
        return self._client.put(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )

    def delete(
        self,
        policyid: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Delete this specific resource.

        Args:
            policyid: Object identifier (required)
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
        if not policyid:
            raise ValueError("policyid is required for delete()")
        endpoint = f"/firewall/interface-policy6/{policyid}"
        params.update(kwargs)
        return self._client.delete(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )

    def post(
        self,
        payload_dict: dict[str, Any] | None = None,
        nkey: str | None = None,
        policyid: int | None = None,
        uuid: str | None = None,
        status: str | None = None,
        comments: str | None = None,
        logtraffic: str | None = None,
        interface: str | None = None,
        srcaddr6: list | None = None,
        dstaddr6: list | None = None,
        service6: list | None = None,
        application_list_status: str | None = None,
        application_list: str | None = None,
        ips_sensor_status: str | None = None,
        ips_sensor: str | None = None,
        dsri: str | None = None,
        av_profile_status: str | None = None,
        av_profile: str | None = None,
        webfilter_profile_status: str | None = None,
        webfilter_profile: str | None = None,
        casb_profile_status: str | None = None,
        casb_profile: str | None = None,
        emailfilter_profile_status: str | None = None,
        emailfilter_profile: str | None = None,
        dlp_profile_status: str | None = None,
        dlp_profile: str | None = None,
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
            policyid: Policy ID (0 - 4294967295). (optional)
            uuid: Universally Unique Identifier (UUID; automatically assigned
            but can be manually reset). (optional)
            status: Enable/disable this policy. (optional)
            comments: Comments. (optional)
            logtraffic: Logging type to be used in this policy (Options: all |
            utm | disable, Default: utm). (optional)
            interface: Monitored interface name from available interfaces.
            (optional)
            srcaddr6: IPv6 address object to limit traffic monitoring to
            network traffic sent from the specified address or range.
            (optional)
            dstaddr6: IPv6 address object to limit traffic monitoring to
            network traffic sent to the specified address or range. (optional)
            service6: Service name. (optional)
            application_list_status: Enable/disable application control.
            (optional)
            application_list: Application list name. (optional)
            ips_sensor_status: Enable/disable IPS. (optional)
            ips_sensor: IPS sensor name. (optional)
            dsri: Enable/disable DSRI. (optional)
            av_profile_status: Enable/disable antivirus. (optional)
            av_profile: Antivirus profile. (optional)
            webfilter_profile_status: Enable/disable web filtering. (optional)
            webfilter_profile: Web filter profile. (optional)
            casb_profile_status: Enable/disable CASB. (optional)
            casb_profile: CASB profile. (optional)
            emailfilter_profile_status: Enable/disable email filter. (optional)
            emailfilter_profile: Email filter profile. (optional)
            dlp_profile_status: Enable/disable DLP. (optional)
            dlp_profile: DLP profile name. (optional)
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
        endpoint = "/firewall/interface-policy6"
        if nkey is not None:
            data_payload["nkey"] = nkey
        if policyid is not None:
            data_payload["policyid"] = policyid
        if uuid is not None:
            data_payload["uuid"] = uuid
        if status is not None:
            data_payload["status"] = status
        if comments is not None:
            data_payload["comments"] = comments
        if logtraffic is not None:
            data_payload["logtraffic"] = logtraffic
        if interface is not None:
            data_payload["interface"] = interface
        if srcaddr6 is not None:
            data_payload["srcaddr6"] = srcaddr6
        if dstaddr6 is not None:
            data_payload["dstaddr6"] = dstaddr6
        if service6 is not None:
            data_payload["service6"] = service6
        if application_list_status is not None:
            data_payload["application-list-status"] = application_list_status
        if application_list is not None:
            data_payload["application-list"] = application_list
        if ips_sensor_status is not None:
            data_payload["ips-sensor-status"] = ips_sensor_status
        if ips_sensor is not None:
            data_payload["ips-sensor"] = ips_sensor
        if dsri is not None:
            data_payload["dsri"] = dsri
        if av_profile_status is not None:
            data_payload["av-profile-status"] = av_profile_status
        if av_profile is not None:
            data_payload["av-profile"] = av_profile
        if webfilter_profile_status is not None:
            data_payload["webfilter-profile-status"] = webfilter_profile_status
        if webfilter_profile is not None:
            data_payload["webfilter-profile"] = webfilter_profile
        if casb_profile_status is not None:
            data_payload["casb-profile-status"] = casb_profile_status
        if casb_profile is not None:
            data_payload["casb-profile"] = casb_profile
        if emailfilter_profile_status is not None:
            data_payload["emailfilter-profile-status"] = (
                emailfilter_profile_status
            )
        if emailfilter_profile is not None:
            data_payload["emailfilter-profile"] = emailfilter_profile
        if dlp_profile_status is not None:
            data_payload["dlp-profile-status"] = dlp_profile_status
        if dlp_profile is not None:
            data_payload["dlp-profile"] = dlp_profile
        data_payload.update(kwargs)
        return self._client.post(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )
