"""
FortiOS CMDB - Cmdb Firewall Security Policy

Configuration endpoint for managing cmdb firewall security policy objects.

API Endpoints:
    GET    /cmdb/firewall/security_policy
    POST   /cmdb/firewall/security_policy
    GET    /cmdb/firewall/security_policy
    PUT    /cmdb/firewall/security_policy/{identifier}
    DELETE /cmdb/firewall/security_policy/{identifier}

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.firewall.security_policy.get()
    >>>
    >>> # Get specific item (if supported)
    >>> item = fgt.api.cmdb.firewall.security_policy.get(name="item_name")
    >>>
    >>> # Create new item (use POST)
    >>> result = fgt.api.cmdb.firewall.security_policy.post(
    ...     name="new_item",
    ...     # ... additional parameters
    ... )
    >>>
    >>> # Update existing item (use PUT)
    >>> result = fgt.api.cmdb.firewall.security_policy.put(
    ...     name="existing_item",
    ...     # ... parameters to update
    ... )
    >>>
    >>> # Delete item
    >>> result = fgt.api.cmdb.firewall.security_policy.delete(name="item_name")

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


class SecurityPolicy:
    """
    Securitypolicy Operations.

    Provides CRUD operations for FortiOS securitypolicy configuration.

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
        Initialize SecurityPolicy endpoint.

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
            endpoint = f"/firewall/security-policy/{policyid}"
        else:
            endpoint = "/firewall/security-policy"
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
        name: str | None = None,
        comments: str | None = None,
        srcintf: list | None = None,
        dstintf: list | None = None,
        srcaddr: list | None = None,
        srcaddr_negate: str | None = None,
        dstaddr: list | None = None,
        dstaddr_negate: str | None = None,
        srcaddr6: list | None = None,
        srcaddr6_negate: str | None = None,
        dstaddr6: list | None = None,
        dstaddr6_negate: str | None = None,
        internet_service: str | None = None,
        internet_service_name: list | None = None,
        internet_service_negate: str | None = None,
        internet_service_group: list | None = None,
        internet_service_custom: list | None = None,
        internet_service_custom_group: list | None = None,
        internet_service_fortiguard: list | None = None,
        internet_service_src: str | None = None,
        internet_service_src_name: list | None = None,
        internet_service_src_negate: str | None = None,
        internet_service_src_group: list | None = None,
        internet_service_src_custom: list | None = None,
        internet_service_src_custom_group: list | None = None,
        internet_service_src_fortiguard: list | None = None,
        internet_service6: str | None = None,
        internet_service6_name: list | None = None,
        internet_service6_negate: str | None = None,
        internet_service6_group: list | None = None,
        internet_service6_custom: list | None = None,
        internet_service6_custom_group: list | None = None,
        internet_service6_fortiguard: list | None = None,
        internet_service6_src: str | None = None,
        internet_service6_src_name: list | None = None,
        internet_service6_src_negate: str | None = None,
        internet_service6_src_group: list | None = None,
        internet_service6_src_custom: list | None = None,
        internet_service6_src_custom_group: list | None = None,
        internet_service6_src_fortiguard: list | None = None,
        enforce_default_app_port: str | None = None,
        service: list | None = None,
        service_negate: str | None = None,
        send_deny_packet: str | None = None,
        schedule: str | None = None,
        status: str | None = None,
        logtraffic: str | None = None,
        learning_mode: str | None = None,
        nat46: str | None = None,
        nat64: str | None = None,
        profile_type: str | None = None,
        profile_group: str | None = None,
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
        ssh_filter_profile: str | None = None,
        casb_profile: str | None = None,
        application: list | None = None,
        app_category: list | None = None,
        url_category: str | None = None,
        app_group: list | None = None,
        groups: list | None = None,
        users: list | None = None,
        fsso_groups: list | None = None,
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
            uuid: Universally Unique Identifier (UUID; automatically assigned
            but can be manually reset). (optional)
            policyid: Policy ID. (optional)
            name: Policy name. (optional)
            comments: Comment. (optional)
            srcintf: Incoming (ingress) interface. (optional)
            dstintf: Outgoing (egress) interface. (optional)
            srcaddr: Source IPv4 address name and address group names.
            (optional)
            srcaddr_negate: When enabled srcaddr specifies what the source
            address must NOT be. (optional)
            dstaddr: Destination IPv4 address name and address group names.
            (optional)
            dstaddr_negate: When enabled dstaddr specifies what the destination
            address must NOT be. (optional)
            srcaddr6: Source IPv6 address name and address group names.
            (optional)
            srcaddr6_negate: When enabled srcaddr6 specifies what the source
            address must NOT be. (optional)
            dstaddr6: Destination IPv6 address name and address group names.
            (optional)
            dstaddr6_negate: When enabled dstaddr6 specifies what the
            destination address must NOT be. (optional)
            internet_service: Enable/disable use of Internet Services for this
            policy. If enabled, destination address, service and default
            application port enforcement are not used. (optional)
            internet_service_name: Internet Service name. (optional)
            internet_service_negate: When enabled internet-service specifies
            what the service must NOT be. (optional)
            internet_service_group: Internet Service group name. (optional)
            internet_service_custom: Custom Internet Service name. (optional)
            internet_service_custom_group: Custom Internet Service group name.
            (optional)
            internet_service_fortiguard: FortiGuard Internet Service name.
            (optional)
            internet_service_src: Enable/disable use of Internet Services in
            source for this policy. If enabled, source address is not used.
            (optional)
            internet_service_src_name: Internet Service source name. (optional)
            internet_service_src_negate: When enabled internet-service-src
            specifies what the service must NOT be. (optional)
            internet_service_src_group: Internet Service source group name.
            (optional)
            internet_service_src_custom: Custom Internet Service source name.
            (optional)
            internet_service_src_custom_group: Custom Internet Service source
            group name. (optional)
            internet_service_src_fortiguard: FortiGuard Internet Service source
            name. (optional)
            internet_service6: Enable/disable use of IPv6 Internet Services for
            this policy. If enabled, destination address, service and default
            application port enforcement are not used. (optional)
            internet_service6_name: IPv6 Internet Service name. (optional)
            internet_service6_negate: When enabled internet-service6 specifies
            what the service must NOT be. (optional)
            internet_service6_group: Internet Service group name. (optional)
            internet_service6_custom: Custom IPv6 Internet Service name.
            (optional)
            internet_service6_custom_group: Custom IPv6 Internet Service group
            name. (optional)
            internet_service6_fortiguard: FortiGuard IPv6 Internet Service
            name. (optional)
            internet_service6_src: Enable/disable use of IPv6 Internet Services
            in source for this policy. If enabled, source address is not used.
            (optional)
            internet_service6_src_name: IPv6 Internet Service source name.
            (optional)
            internet_service6_src_negate: When enabled internet-service6-src
            specifies what the service must NOT be. (optional)
            internet_service6_src_group: Internet Service6 source group name.
            (optional)
            internet_service6_src_custom: Custom IPv6 Internet Service source
            name. (optional)
            internet_service6_src_custom_group: Custom Internet Service6 source
            group name. (optional)
            internet_service6_src_fortiguard: FortiGuard IPv6 Internet Service
            source name. (optional)
            enforce_default_app_port: Enable/disable default application port
            enforcement for allowed applications. (optional)
            service: Service and service group names. (optional)
            service_negate: When enabled service specifies what the service
            must NOT be. (optional)
            send_deny_packet: Enable to send a reply when a session is denied
            or blocked by a firewall policy. (optional)
            schedule: Schedule name. (optional)
            status: Enable or disable this policy. (optional)
            logtraffic: Enable or disable logging. Log all sessions or security
            profile sessions. (optional)
            learning_mode: Enable to allow everything, but log all of the
            meaningful data for security information gathering. A learning
            report will be generated. (optional)
            nat46: Enable/disable NAT46. (optional)
            nat64: Enable/disable NAT64. (optional)
            profile_type: Determine whether the firewall policy allows security
            profile groups or single profiles only. (optional)
            profile_group: Name of profile group. (optional)
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
            ssh_filter_profile: Name of an existing SSH filter profile.
            (optional)
            casb_profile: Name of an existing CASB profile. (optional)
            application: Application ID list. (optional)
            app_category: Application category ID list. (optional)
            url_category: URL categories or groups. (optional)
            app_group: Application group names. (optional)
            groups: Names of user groups that can authenticate with this
            policy. (optional)
            users: Names of individual users that can authenticate with this
            policy. (optional)
            fsso_groups: Names of FSSO groups. (optional)
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
        endpoint = f"/firewall/security-policy/{policyid}"
        if before is not None:
            data_payload["before"] = before
        if after is not None:
            data_payload["after"] = after
        if uuid is not None:
            data_payload["uuid"] = uuid
        if policyid is not None:
            data_payload["policyid"] = policyid
        if name is not None:
            data_payload["name"] = name
        if comments is not None:
            data_payload["comments"] = comments
        if srcintf is not None:
            data_payload["srcint"] = srcintf
        if dstintf is not None:
            data_payload["dstint"] = dstintf
        if srcaddr is not None:
            data_payload["srcaddr"] = srcaddr
        if srcaddr_negate is not None:
            data_payload["srcaddr-negate"] = srcaddr_negate
        if dstaddr is not None:
            data_payload["dstaddr"] = dstaddr
        if dstaddr_negate is not None:
            data_payload["dstaddr-negate"] = dstaddr_negate
        if srcaddr6 is not None:
            data_payload["srcaddr6"] = srcaddr6
        if srcaddr6_negate is not None:
            data_payload["srcaddr6-negate"] = srcaddr6_negate
        if dstaddr6 is not None:
            data_payload["dstaddr6"] = dstaddr6
        if dstaddr6_negate is not None:
            data_payload["dstaddr6-negate"] = dstaddr6_negate
        if internet_service is not None:
            data_payload["internet-service"] = internet_service
        if internet_service_name is not None:
            data_payload["internet-service-name"] = internet_service_name
        if internet_service_negate is not None:
            data_payload["internet-service-negate"] = internet_service_negate
        if internet_service_group is not None:
            data_payload["internet-service-group"] = internet_service_group
        if internet_service_custom is not None:
            data_payload["internet-service-custom"] = internet_service_custom
        if internet_service_custom_group is not None:
            data_payload["internet-service-custom-group"] = (
                internet_service_custom_group
            )
        if internet_service_fortiguard is not None:
            data_payload["internet-service-fortiguard"] = (
                internet_service_fortiguard
            )
        if internet_service_src is not None:
            data_payload["internet-service-src"] = internet_service_src
        if internet_service_src_name is not None:
            data_payload["internet-service-src-name"] = (
                internet_service_src_name
            )
        if internet_service_src_negate is not None:
            data_payload["internet-service-src-negate"] = (
                internet_service_src_negate
            )
        if internet_service_src_group is not None:
            data_payload["internet-service-src-group"] = (
                internet_service_src_group
            )
        if internet_service_src_custom is not None:
            data_payload["internet-service-src-custom"] = (
                internet_service_src_custom
            )
        if internet_service_src_custom_group is not None:
            data_payload["internet-service-src-custom-group"] = (
                internet_service_src_custom_group
            )
        if internet_service_src_fortiguard is not None:
            data_payload["internet-service-src-fortiguard"] = (
                internet_service_src_fortiguard
            )
        if internet_service6 is not None:
            data_payload["internet-service6"] = internet_service6
        if internet_service6_name is not None:
            data_payload["internet-service6-name"] = internet_service6_name
        if internet_service6_negate is not None:
            data_payload["internet-service6-negate"] = internet_service6_negate
        if internet_service6_group is not None:
            data_payload["internet-service6-group"] = internet_service6_group
        if internet_service6_custom is not None:
            data_payload["internet-service6-custom"] = internet_service6_custom
        if internet_service6_custom_group is not None:
            data_payload["internet-service6-custom-group"] = (
                internet_service6_custom_group
            )
        if internet_service6_fortiguard is not None:
            data_payload["internet-service6-fortiguard"] = (
                internet_service6_fortiguard
            )
        if internet_service6_src is not None:
            data_payload["internet-service6-src"] = internet_service6_src
        if internet_service6_src_name is not None:
            data_payload["internet-service6-src-name"] = (
                internet_service6_src_name
            )
        if internet_service6_src_negate is not None:
            data_payload["internet-service6-src-negate"] = (
                internet_service6_src_negate
            )
        if internet_service6_src_group is not None:
            data_payload["internet-service6-src-group"] = (
                internet_service6_src_group
            )
        if internet_service6_src_custom is not None:
            data_payload["internet-service6-src-custom"] = (
                internet_service6_src_custom
            )
        if internet_service6_src_custom_group is not None:
            data_payload["internet-service6-src-custom-group"] = (
                internet_service6_src_custom_group
            )
        if internet_service6_src_fortiguard is not None:
            data_payload["internet-service6-src-fortiguard"] = (
                internet_service6_src_fortiguard
            )
        if enforce_default_app_port is not None:
            data_payload["enforce-default-app-port"] = enforce_default_app_port
        if service is not None:
            data_payload["service"] = service
        if service_negate is not None:
            data_payload["service-negate"] = service_negate
        if send_deny_packet is not None:
            data_payload["send-deny-packet"] = send_deny_packet
        if schedule is not None:
            data_payload["schedule"] = schedule
        if status is not None:
            data_payload["status"] = status
        if logtraffic is not None:
            data_payload["logtraffic"] = logtraffic
        if learning_mode is not None:
            data_payload["learning-mode"] = learning_mode
        if nat46 is not None:
            data_payload["nat46"] = nat46
        if nat64 is not None:
            data_payload["nat64"] = nat64
        if profile_type is not None:
            data_payload["profile-type"] = profile_type
        if profile_group is not None:
            data_payload["profile-group"] = profile_group
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
        if ssh_filter_profile is not None:
            data_payload["ssh-filter-profile"] = ssh_filter_profile
        if casb_profile is not None:
            data_payload["casb-profile"] = casb_profile
        if application is not None:
            data_payload["application"] = application
        if app_category is not None:
            data_payload["app-category"] = app_category
        if url_category is not None:
            data_payload["url-category"] = url_category
        if app_group is not None:
            data_payload["app-group"] = app_group
        if groups is not None:
            data_payload["groups"] = groups
        if users is not None:
            data_payload["users"] = users
        if fsso_groups is not None:
            data_payload["fsso-groups"] = fsso_groups
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
        endpoint = f"/firewall/security-policy/{policyid}"
        params.update(kwargs)
        return self._client.delete(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )

    def exists(
        self,
        policyid: str,
        vdom: str | bool | None = None,
    ) -> Union[bool, Coroutine[Any, Any, bool]]:
        """
        Check if an object exists.

        Args:
            policyid: Object identifier
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
        result = self.get(policyid=policyid, vdom=vdom)

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
        uuid: str | None = None,
        policyid: int | None = None,
        name: str | None = None,
        comments: str | None = None,
        srcintf: list | None = None,
        dstintf: list | None = None,
        srcaddr: list | None = None,
        srcaddr_negate: str | None = None,
        dstaddr: list | None = None,
        dstaddr_negate: str | None = None,
        srcaddr6: list | None = None,
        srcaddr6_negate: str | None = None,
        dstaddr6: list | None = None,
        dstaddr6_negate: str | None = None,
        internet_service: str | None = None,
        internet_service_name: list | None = None,
        internet_service_negate: str | None = None,
        internet_service_group: list | None = None,
        internet_service_custom: list | None = None,
        internet_service_custom_group: list | None = None,
        internet_service_fortiguard: list | None = None,
        internet_service_src: str | None = None,
        internet_service_src_name: list | None = None,
        internet_service_src_negate: str | None = None,
        internet_service_src_group: list | None = None,
        internet_service_src_custom: list | None = None,
        internet_service_src_custom_group: list | None = None,
        internet_service_src_fortiguard: list | None = None,
        internet_service6: str | None = None,
        internet_service6_name: list | None = None,
        internet_service6_negate: str | None = None,
        internet_service6_group: list | None = None,
        internet_service6_custom: list | None = None,
        internet_service6_custom_group: list | None = None,
        internet_service6_fortiguard: list | None = None,
        internet_service6_src: str | None = None,
        internet_service6_src_name: list | None = None,
        internet_service6_src_negate: str | None = None,
        internet_service6_src_group: list | None = None,
        internet_service6_src_custom: list | None = None,
        internet_service6_src_custom_group: list | None = None,
        internet_service6_src_fortiguard: list | None = None,
        enforce_default_app_port: str | None = None,
        service: list | None = None,
        service_negate: str | None = None,
        send_deny_packet: str | None = None,
        schedule: str | None = None,
        status: str | None = None,
        logtraffic: str | None = None,
        learning_mode: str | None = None,
        nat46: str | None = None,
        nat64: str | None = None,
        profile_type: str | None = None,
        profile_group: str | None = None,
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
        ssh_filter_profile: str | None = None,
        casb_profile: str | None = None,
        application: list | None = None,
        app_category: list | None = None,
        url_category: str | None = None,
        app_group: list | None = None,
        groups: list | None = None,
        users: list | None = None,
        fsso_groups: list | None = None,
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
            uuid: Universally Unique Identifier (UUID; automatically assigned
            but can be manually reset). (optional)
            policyid: Policy ID. (optional)
            name: Policy name. (optional)
            comments: Comment. (optional)
            srcintf: Incoming (ingress) interface. (optional)
            dstintf: Outgoing (egress) interface. (optional)
            srcaddr: Source IPv4 address name and address group names.
            (optional)
            srcaddr_negate: When enabled srcaddr specifies what the source
            address must NOT be. (optional)
            dstaddr: Destination IPv4 address name and address group names.
            (optional)
            dstaddr_negate: When enabled dstaddr specifies what the destination
            address must NOT be. (optional)
            srcaddr6: Source IPv6 address name and address group names.
            (optional)
            srcaddr6_negate: When enabled srcaddr6 specifies what the source
            address must NOT be. (optional)
            dstaddr6: Destination IPv6 address name and address group names.
            (optional)
            dstaddr6_negate: When enabled dstaddr6 specifies what the
            destination address must NOT be. (optional)
            internet_service: Enable/disable use of Internet Services for this
            policy. If enabled, destination address, service and default
            application port enforcement are not used. (optional)
            internet_service_name: Internet Service name. (optional)
            internet_service_negate: When enabled internet-service specifies
            what the service must NOT be. (optional)
            internet_service_group: Internet Service group name. (optional)
            internet_service_custom: Custom Internet Service name. (optional)
            internet_service_custom_group: Custom Internet Service group name.
            (optional)
            internet_service_fortiguard: FortiGuard Internet Service name.
            (optional)
            internet_service_src: Enable/disable use of Internet Services in
            source for this policy. If enabled, source address is not used.
            (optional)
            internet_service_src_name: Internet Service source name. (optional)
            internet_service_src_negate: When enabled internet-service-src
            specifies what the service must NOT be. (optional)
            internet_service_src_group: Internet Service source group name.
            (optional)
            internet_service_src_custom: Custom Internet Service source name.
            (optional)
            internet_service_src_custom_group: Custom Internet Service source
            group name. (optional)
            internet_service_src_fortiguard: FortiGuard Internet Service source
            name. (optional)
            internet_service6: Enable/disable use of IPv6 Internet Services for
            this policy. If enabled, destination address, service and default
            application port enforcement are not used. (optional)
            internet_service6_name: IPv6 Internet Service name. (optional)
            internet_service6_negate: When enabled internet-service6 specifies
            what the service must NOT be. (optional)
            internet_service6_group: Internet Service group name. (optional)
            internet_service6_custom: Custom IPv6 Internet Service name.
            (optional)
            internet_service6_custom_group: Custom IPv6 Internet Service group
            name. (optional)
            internet_service6_fortiguard: FortiGuard IPv6 Internet Service
            name. (optional)
            internet_service6_src: Enable/disable use of IPv6 Internet Services
            in source for this policy. If enabled, source address is not used.
            (optional)
            internet_service6_src_name: IPv6 Internet Service source name.
            (optional)
            internet_service6_src_negate: When enabled internet-service6-src
            specifies what the service must NOT be. (optional)
            internet_service6_src_group: Internet Service6 source group name.
            (optional)
            internet_service6_src_custom: Custom IPv6 Internet Service source
            name. (optional)
            internet_service6_src_custom_group: Custom Internet Service6 source
            group name. (optional)
            internet_service6_src_fortiguard: FortiGuard IPv6 Internet Service
            source name. (optional)
            enforce_default_app_port: Enable/disable default application port
            enforcement for allowed applications. (optional)
            service: Service and service group names. (optional)
            service_negate: When enabled service specifies what the service
            must NOT be. (optional)
            send_deny_packet: Enable to send a reply when a session is denied
            or blocked by a firewall policy. (optional)
            schedule: Schedule name. (optional)
            status: Enable or disable this policy. (optional)
            logtraffic: Enable or disable logging. Log all sessions or security
            profile sessions. (optional)
            learning_mode: Enable to allow everything, but log all of the
            meaningful data for security information gathering. A learning
            report will be generated. (optional)
            nat46: Enable/disable NAT46. (optional)
            nat64: Enable/disable NAT64. (optional)
            profile_type: Determine whether the firewall policy allows security
            profile groups or single profiles only. (optional)
            profile_group: Name of profile group. (optional)
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
            ssh_filter_profile: Name of an existing SSH filter profile.
            (optional)
            casb_profile: Name of an existing CASB profile. (optional)
            application: Application ID list. (optional)
            app_category: Application category ID list. (optional)
            url_category: URL categories or groups. (optional)
            app_group: Application group names. (optional)
            groups: Names of user groups that can authenticate with this
            policy. (optional)
            users: Names of individual users that can authenticate with this
            policy. (optional)
            fsso_groups: Names of FSSO groups. (optional)
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
        endpoint = "/firewall/security-policy"
        if nkey is not None:
            data_payload["nkey"] = nkey
        if uuid is not None:
            data_payload["uuid"] = uuid
        if policyid is not None:
            data_payload["policyid"] = policyid
        if name is not None:
            data_payload["name"] = name
        if comments is not None:
            data_payload["comments"] = comments
        if srcintf is not None:
            data_payload["srcint"] = srcintf
        if dstintf is not None:
            data_payload["dstint"] = dstintf
        if srcaddr is not None:
            data_payload["srcaddr"] = srcaddr
        if srcaddr_negate is not None:
            data_payload["srcaddr-negate"] = srcaddr_negate
        if dstaddr is not None:
            data_payload["dstaddr"] = dstaddr
        if dstaddr_negate is not None:
            data_payload["dstaddr-negate"] = dstaddr_negate
        if srcaddr6 is not None:
            data_payload["srcaddr6"] = srcaddr6
        if srcaddr6_negate is not None:
            data_payload["srcaddr6-negate"] = srcaddr6_negate
        if dstaddr6 is not None:
            data_payload["dstaddr6"] = dstaddr6
        if dstaddr6_negate is not None:
            data_payload["dstaddr6-negate"] = dstaddr6_negate
        if internet_service is not None:
            data_payload["internet-service"] = internet_service
        if internet_service_name is not None:
            data_payload["internet-service-name"] = internet_service_name
        if internet_service_negate is not None:
            data_payload["internet-service-negate"] = internet_service_negate
        if internet_service_group is not None:
            data_payload["internet-service-group"] = internet_service_group
        if internet_service_custom is not None:
            data_payload["internet-service-custom"] = internet_service_custom
        if internet_service_custom_group is not None:
            data_payload["internet-service-custom-group"] = (
                internet_service_custom_group
            )
        if internet_service_fortiguard is not None:
            data_payload["internet-service-fortiguard"] = (
                internet_service_fortiguard
            )
        if internet_service_src is not None:
            data_payload["internet-service-src"] = internet_service_src
        if internet_service_src_name is not None:
            data_payload["internet-service-src-name"] = (
                internet_service_src_name
            )
        if internet_service_src_negate is not None:
            data_payload["internet-service-src-negate"] = (
                internet_service_src_negate
            )
        if internet_service_src_group is not None:
            data_payload["internet-service-src-group"] = (
                internet_service_src_group
            )
        if internet_service_src_custom is not None:
            data_payload["internet-service-src-custom"] = (
                internet_service_src_custom
            )
        if internet_service_src_custom_group is not None:
            data_payload["internet-service-src-custom-group"] = (
                internet_service_src_custom_group
            )
        if internet_service_src_fortiguard is not None:
            data_payload["internet-service-src-fortiguard"] = (
                internet_service_src_fortiguard
            )
        if internet_service6 is not None:
            data_payload["internet-service6"] = internet_service6
        if internet_service6_name is not None:
            data_payload["internet-service6-name"] = internet_service6_name
        if internet_service6_negate is not None:
            data_payload["internet-service6-negate"] = internet_service6_negate
        if internet_service6_group is not None:
            data_payload["internet-service6-group"] = internet_service6_group
        if internet_service6_custom is not None:
            data_payload["internet-service6-custom"] = internet_service6_custom
        if internet_service6_custom_group is not None:
            data_payload["internet-service6-custom-group"] = (
                internet_service6_custom_group
            )
        if internet_service6_fortiguard is not None:
            data_payload["internet-service6-fortiguard"] = (
                internet_service6_fortiguard
            )
        if internet_service6_src is not None:
            data_payload["internet-service6-src"] = internet_service6_src
        if internet_service6_src_name is not None:
            data_payload["internet-service6-src-name"] = (
                internet_service6_src_name
            )
        if internet_service6_src_negate is not None:
            data_payload["internet-service6-src-negate"] = (
                internet_service6_src_negate
            )
        if internet_service6_src_group is not None:
            data_payload["internet-service6-src-group"] = (
                internet_service6_src_group
            )
        if internet_service6_src_custom is not None:
            data_payload["internet-service6-src-custom"] = (
                internet_service6_src_custom
            )
        if internet_service6_src_custom_group is not None:
            data_payload["internet-service6-src-custom-group"] = (
                internet_service6_src_custom_group
            )
        if internet_service6_src_fortiguard is not None:
            data_payload["internet-service6-src-fortiguard"] = (
                internet_service6_src_fortiguard
            )
        if enforce_default_app_port is not None:
            data_payload["enforce-default-app-port"] = enforce_default_app_port
        if service is not None:
            data_payload["service"] = service
        if service_negate is not None:
            data_payload["service-negate"] = service_negate
        if send_deny_packet is not None:
            data_payload["send-deny-packet"] = send_deny_packet
        if schedule is not None:
            data_payload["schedule"] = schedule
        if status is not None:
            data_payload["status"] = status
        if logtraffic is not None:
            data_payload["logtraffic"] = logtraffic
        if learning_mode is not None:
            data_payload["learning-mode"] = learning_mode
        if nat46 is not None:
            data_payload["nat46"] = nat46
        if nat64 is not None:
            data_payload["nat64"] = nat64
        if profile_type is not None:
            data_payload["profile-type"] = profile_type
        if profile_group is not None:
            data_payload["profile-group"] = profile_group
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
        if ssh_filter_profile is not None:
            data_payload["ssh-filter-profile"] = ssh_filter_profile
        if casb_profile is not None:
            data_payload["casb-profile"] = casb_profile
        if application is not None:
            data_payload["application"] = application
        if app_category is not None:
            data_payload["app-category"] = app_category
        if url_category is not None:
            data_payload["url-category"] = url_category
        if app_group is not None:
            data_payload["app-group"] = app_group
        if groups is not None:
            data_payload["groups"] = groups
        if users is not None:
            data_payload["users"] = users
        if fsso_groups is not None:
            data_payload["fsso-groups"] = fsso_groups
        data_payload.update(kwargs)
        return self._client.post(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )
