"""
FortiOS CMDB - Cmdb Firewall Profile Group

Configuration endpoint for managing cmdb firewall profile group objects.

API Endpoints:
    GET    /cmdb/firewall/profile_group
    POST   /cmdb/firewall/profile_group
    GET    /cmdb/firewall/profile_group
    PUT    /cmdb/firewall/profile_group/{identifier}
    DELETE /cmdb/firewall/profile_group/{identifier}

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.firewall.profile_group.get()
    >>>
    >>> # Get specific item (if supported)
    >>> item = fgt.api.cmdb.firewall.profile_group.get(name="item_name")
    >>>
    >>> # Create new item (use POST)
    >>> result = fgt.api.cmdb.firewall.profile_group.post(
    ...     name="new_item",
    ...     # ... additional parameters
    ... )
    >>>
    >>> # Update existing item (use PUT)
    >>> result = fgt.api.cmdb.firewall.profile_group.put(
    ...     name="existing_item",
    ...     # ... parameters to update
    ... )
    >>>
    >>> # Delete item
    >>> result = fgt.api.cmdb.firewall.profile_group.delete(name="item_name")

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


class ProfileGroup:
    """
    Profilegroup Operations.

    Provides CRUD operations for FortiOS profilegroup configuration.

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
        Initialize ProfileGroup endpoint.

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
            endpoint = f"/firewall/profile-group/{name}"
        else:
            endpoint = "/firewall/profile-group"
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
        profile_protocol_options: str | None = None,
        ssl_ssh_profile: str | None = None,
        av_profile: str | None = None,
        webfilter_profile: str | None = None,
        dnsfilter_profile: str | None = None,
        emailfilter_profile: str | None = None,
        dlp_profile: str | None = None,
        file_filter_profile: str | None = None,
        ips_sensor: str | None = None,
        application_list: str | None = None,
        voip_profile: str | None = None,
        ips_voip_filter: str | None = None,
        sctp_filter_profile: str | None = None,
        diameter_filter_profile: str | None = None,
        virtual_patch_profile: str | None = None,
        icap_profile: str | None = None,
        videofilter_profile: str | None = None,
        waf_profile: str | None = None,
        ssh_filter_profile: str | None = None,
        casb_profile: str | None = None,
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
            name: Profile group name. (optional)
            profile_protocol_options: Name of an existing Protocol options
            profile. (optional)
            ssl_ssh_profile: Name of an existing SSL SSH profile. (optional)
            av_profile: Name of an existing Antivirus profile. (optional)
            webfilter_profile: Name of an existing Web filter profile.
            (optional)
            dnsfilter_profile: Name of an existing DNS filter profile.
            (optional)
            emailfilter_profile: Name of an existing email filter profile.
            (optional)
            dlp_profile: Name of an existing DLP profile. (optional)
            file_filter_profile: Name of an existing file-filter profile.
            (optional)
            ips_sensor: Name of an existing IPS sensor. (optional)
            application_list: Name of an existing Application list. (optional)
            voip_profile: Name of an existing VoIP (voipd) profile. (optional)
            ips_voip_filter: Name of an existing VoIP (ips) profile. (optional)
            sctp_filter_profile: Name of an existing SCTP filter profile.
            (optional)
            diameter_filter_profile: Name of an existing Diameter filter
            profile. (optional)
            virtual_patch_profile: Name of an existing virtual-patch profile.
            (optional)
            icap_profile: Name of an existing ICAP profile. (optional)
            videofilter_profile: Name of an existing VideoFilter profile.
            (optional)
            waf_profile: Name of an existing Web application firewall profile.
            (optional)
            ssh_filter_profile: Name of an existing SSH filter profile.
            (optional)
            casb_profile: Name of an existing CASB profile. (optional)
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
        endpoint = f"/firewall/profile-group/{name}"
        if before is not None:
            data_payload["before"] = before
        if after is not None:
            data_payload["after"] = after
        if name is not None:
            data_payload["name"] = name
        if profile_protocol_options is not None:
            data_payload["profile-protocol-options"] = profile_protocol_options
        if ssl_ssh_profile is not None:
            data_payload["ssl-ssh-profile"] = ssl_ssh_profile
        if av_profile is not None:
            data_payload["av-profile"] = av_profile
        if webfilter_profile is not None:
            data_payload["webfilter-profile"] = webfilter_profile
        if dnsfilter_profile is not None:
            data_payload["dnsfilter-profile"] = dnsfilter_profile
        if emailfilter_profile is not None:
            data_payload["emailfilter-profile"] = emailfilter_profile
        if dlp_profile is not None:
            data_payload["dlp-profile"] = dlp_profile
        if file_filter_profile is not None:
            data_payload["file-filter-profile"] = file_filter_profile
        if ips_sensor is not None:
            data_payload["ips-sensor"] = ips_sensor
        if application_list is not None:
            data_payload["application-list"] = application_list
        if voip_profile is not None:
            data_payload["voip-profile"] = voip_profile
        if ips_voip_filter is not None:
            data_payload["ips-voip-filter"] = ips_voip_filter
        if sctp_filter_profile is not None:
            data_payload["sctp-filter-profile"] = sctp_filter_profile
        if diameter_filter_profile is not None:
            data_payload["diameter-filter-profile"] = diameter_filter_profile
        if virtual_patch_profile is not None:
            data_payload["virtual-patch-profile"] = virtual_patch_profile
        if icap_profile is not None:
            data_payload["icap-profile"] = icap_profile
        if videofilter_profile is not None:
            data_payload["videofilter-profile"] = videofilter_profile
        if waf_profile is not None:
            data_payload["waf-profile"] = waf_profile
        if ssh_filter_profile is not None:
            data_payload["ssh-filter-profile"] = ssh_filter_profile
        if casb_profile is not None:
            data_payload["casb-profile"] = casb_profile
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
        endpoint = f"/firewall/profile-group/{name}"
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
        profile_protocol_options: str | None = None,
        ssl_ssh_profile: str | None = None,
        av_profile: str | None = None,
        webfilter_profile: str | None = None,
        dnsfilter_profile: str | None = None,
        emailfilter_profile: str | None = None,
        dlp_profile: str | None = None,
        file_filter_profile: str | None = None,
        ips_sensor: str | None = None,
        application_list: str | None = None,
        voip_profile: str | None = None,
        ips_voip_filter: str | None = None,
        sctp_filter_profile: str | None = None,
        diameter_filter_profile: str | None = None,
        virtual_patch_profile: str | None = None,
        icap_profile: str | None = None,
        videofilter_profile: str | None = None,
        waf_profile: str | None = None,
        ssh_filter_profile: str | None = None,
        casb_profile: str | None = None,
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
            name: Profile group name. (optional)
            profile_protocol_options: Name of an existing Protocol options
            profile. (optional)
            ssl_ssh_profile: Name of an existing SSL SSH profile. (optional)
            av_profile: Name of an existing Antivirus profile. (optional)
            webfilter_profile: Name of an existing Web filter profile.
            (optional)
            dnsfilter_profile: Name of an existing DNS filter profile.
            (optional)
            emailfilter_profile: Name of an existing email filter profile.
            (optional)
            dlp_profile: Name of an existing DLP profile. (optional)
            file_filter_profile: Name of an existing file-filter profile.
            (optional)
            ips_sensor: Name of an existing IPS sensor. (optional)
            application_list: Name of an existing Application list. (optional)
            voip_profile: Name of an existing VoIP (voipd) profile. (optional)
            ips_voip_filter: Name of an existing VoIP (ips) profile. (optional)
            sctp_filter_profile: Name of an existing SCTP filter profile.
            (optional)
            diameter_filter_profile: Name of an existing Diameter filter
            profile. (optional)
            virtual_patch_profile: Name of an existing virtual-patch profile.
            (optional)
            icap_profile: Name of an existing ICAP profile. (optional)
            videofilter_profile: Name of an existing VideoFilter profile.
            (optional)
            waf_profile: Name of an existing Web application firewall profile.
            (optional)
            ssh_filter_profile: Name of an existing SSH filter profile.
            (optional)
            casb_profile: Name of an existing CASB profile. (optional)
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
        endpoint = "/firewall/profile-group"
        if nkey is not None:
            data_payload["nkey"] = nkey
        if name is not None:
            data_payload["name"] = name
        if profile_protocol_options is not None:
            data_payload["profile-protocol-options"] = profile_protocol_options
        if ssl_ssh_profile is not None:
            data_payload["ssl-ssh-profile"] = ssl_ssh_profile
        if av_profile is not None:
            data_payload["av-profile"] = av_profile
        if webfilter_profile is not None:
            data_payload["webfilter-profile"] = webfilter_profile
        if dnsfilter_profile is not None:
            data_payload["dnsfilter-profile"] = dnsfilter_profile
        if emailfilter_profile is not None:
            data_payload["emailfilter-profile"] = emailfilter_profile
        if dlp_profile is not None:
            data_payload["dlp-profile"] = dlp_profile
        if file_filter_profile is not None:
            data_payload["file-filter-profile"] = file_filter_profile
        if ips_sensor is not None:
            data_payload["ips-sensor"] = ips_sensor
        if application_list is not None:
            data_payload["application-list"] = application_list
        if voip_profile is not None:
            data_payload["voip-profile"] = voip_profile
        if ips_voip_filter is not None:
            data_payload["ips-voip-filter"] = ips_voip_filter
        if sctp_filter_profile is not None:
            data_payload["sctp-filter-profile"] = sctp_filter_profile
        if diameter_filter_profile is not None:
            data_payload["diameter-filter-profile"] = diameter_filter_profile
        if virtual_patch_profile is not None:
            data_payload["virtual-patch-profile"] = virtual_patch_profile
        if icap_profile is not None:
            data_payload["icap-profile"] = icap_profile
        if videofilter_profile is not None:
            data_payload["videofilter-profile"] = videofilter_profile
        if waf_profile is not None:
            data_payload["waf-profile"] = waf_profile
        if ssh_filter_profile is not None:
            data_payload["ssh-filter-profile"] = ssh_filter_profile
        if casb_profile is not None:
            data_payload["casb-profile"] = casb_profile
        data_payload.update(kwargs)
        return self._client.post(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )
