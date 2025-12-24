"""
FortiOS CMDB - Cmdb Firewall Proxy Policy

Configuration endpoint for managing cmdb firewall proxy policy objects.

API Endpoints:
    GET    /cmdb/firewall/proxy_policy
    POST   /cmdb/firewall/proxy_policy
    GET    /cmdb/firewall/proxy_policy
    PUT    /cmdb/firewall/proxy_policy/{identifier}
    DELETE /cmdb/firewall/proxy_policy/{identifier}

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.firewall.proxy_policy.get()
    >>>
    >>> # Get specific item (if supported)
    >>> item = fgt.api.cmdb.firewall.proxy_policy.get(name="item_name")
    >>>
    >>> # Create new item (use POST)
    >>> result = fgt.api.cmdb.firewall.proxy_policy.post(
    ...     name="new_item",
    ...     # ... additional parameters
    ... )
    >>>
    >>> # Update existing item (use PUT)
    >>> result = fgt.api.cmdb.firewall.proxy_policy.put(
    ...     name="existing_item",
    ...     # ... parameters to update
    ... )
    >>>
    >>> # Delete item
    >>> result = fgt.api.cmdb.firewall.proxy_policy.delete(name="item_name")

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


class ProxyPolicy:
    """
    Proxypolicy Operations.

    Provides CRUD operations for FortiOS proxypolicy configuration.

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
        Initialize ProxyPolicy endpoint.

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
            endpoint = f"/firewall/proxy-policy/{policyid}"
        else:
            endpoint = "/firewall/proxy-policy"
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
        proxy: str | None = None,
        access_proxy: list | None = None,
        access_proxy6: list | None = None,
        ztna_proxy: list | None = None,
        srcintf: list | None = None,
        dstintf: list | None = None,
        srcaddr: list | None = None,
        poolname: list | None = None,
        poolname6: list | None = None,
        dstaddr: list | None = None,
        ztna_ems_tag: list | None = None,
        ztna_tags_match_logic: str | None = None,
        device_ownership: str | None = None,
        url_risk: list | None = None,
        internet_service: str | None = None,
        internet_service_negate: str | None = None,
        internet_service_name: list | None = None,
        internet_service_group: list | None = None,
        internet_service_custom: list | None = None,
        internet_service_custom_group: list | None = None,
        internet_service_fortiguard: list | None = None,
        internet_service6: str | None = None,
        internet_service6_negate: str | None = None,
        internet_service6_name: list | None = None,
        internet_service6_group: list | None = None,
        internet_service6_custom: list | None = None,
        internet_service6_custom_group: list | None = None,
        internet_service6_fortiguard: list | None = None,
        service: list | None = None,
        srcaddr_negate: str | None = None,
        dstaddr_negate: str | None = None,
        ztna_ems_tag_negate: str | None = None,
        service_negate: str | None = None,
        status: str | None = None,
        schedule: str | None = None,
        logtraffic: str | None = None,
        session_ttl: int | None = None,
        srcaddr6: list | None = None,
        dstaddr6: list | None = None,
        groups: list | None = None,
        users: list | None = None,
        http_tunnel_auth: str | None = None,
        ssh_policy_redirect: str | None = None,
        webproxy_forward_server: str | None = None,
        isolator_server: str | None = None,
        webproxy_profile: str | None = None,
        transparent: str | None = None,
        disclaimer: str | None = None,
        utm_status: str | None = None,
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
        ips_voip_filter: str | None = None,
        sctp_filter_profile: str | None = None,
        icap_profile: str | None = None,
        videofilter_profile: str | None = None,
        waf_profile: str | None = None,
        ssh_filter_profile: str | None = None,
        casb_profile: str | None = None,
        replacemsg_override_group: str | None = None,
        logtraffic_start: str | None = None,
        log_http_transaction: str | None = None,
        comments: str | None = None,
        block_notification: str | None = None,
        redirect_url: str | None = None,
        https_sub_category: str | None = None,
        decrypted_traffic_mirror: str | None = None,
        detect_https_in_http_request: str | None = None,
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
            proxy: Type of explicit proxy. (optional)
            access_proxy: IPv4 access proxy. (optional)
            access_proxy6: IPv6 access proxy. (optional)
            ztna_proxy: ZTNA proxies. (optional)
            srcintf: Source interface names. (optional)
            dstintf: Destination interface names. (optional)
            srcaddr: Source address objects. (optional)
            poolname: Name of IP pool object. (optional)
            poolname6: Name of IPv6 pool object. (optional)
            dstaddr: Destination address objects. (optional)
            ztna_ems_tag: ZTNA EMS Tag names. (optional)
            ztna_tags_match_logic: ZTNA tag matching logic. (optional)
            device_ownership: When enabled, the ownership enforcement will be
            done at policy level. (optional)
            url_risk: URL risk level name. (optional)
            internet_service: Enable/disable use of Internet Services for this
            policy. If enabled, destination address and service are not used.
            (optional)
            internet_service_negate: When enabled, Internet Services match
            against any internet service EXCEPT the selected Internet Service.
            (optional)
            internet_service_name: Internet Service name. (optional)
            internet_service_group: Internet Service group name. (optional)
            internet_service_custom: Custom Internet Service name. (optional)
            internet_service_custom_group: Custom Internet Service group name.
            (optional)
            internet_service_fortiguard: FortiGuard Internet Service name.
            (optional)
            internet_service6: Enable/disable use of Internet Services IPv6 for
            this policy. If enabled, destination IPv6 address and service are
            not used. (optional)
            internet_service6_negate: When enabled, Internet Services match
            against any internet service IPv6 EXCEPT the selected Internet
            Service IPv6. (optional)
            internet_service6_name: Internet Service IPv6 name. (optional)
            internet_service6_group: Internet Service IPv6 group name.
            (optional)
            internet_service6_custom: Custom Internet Service IPv6 name.
            (optional)
            internet_service6_custom_group: Custom Internet Service IPv6 group
            name. (optional)
            internet_service6_fortiguard: FortiGuard Internet Service IPv6
            name. (optional)
            service: Name of service objects. (optional)
            srcaddr_negate: When enabled, source addresses match against any
            address EXCEPT the specified source addresses. (optional)
            dstaddr_negate: When enabled, destination addresses match against
            any address EXCEPT the specified destination addresses. (optional)
            ztna_ems_tag_negate: When enabled, ZTNA EMS tags match against any
            tag EXCEPT the specified ZTNA EMS tags. (optional)
            service_negate: When enabled, services match against any service
            EXCEPT the specified destination services. (optional)
            status: Enable/disable the active status of the policy. (optional)
            schedule: Name of schedule object. (optional)
            logtraffic: Enable/disable logging traffic through the policy.
            (optional)
            session_ttl: TTL in seconds for sessions accepted by this policy (0
            means use the system default session TTL). (optional)
            srcaddr6: IPv6 source address objects. (optional)
            dstaddr6: IPv6 destination address objects. (optional)
            groups: Names of group objects. (optional)
            users: Names of user objects. (optional)
            http_tunnel_auth: Enable/disable HTTP tunnel authentication.
            (optional)
            ssh_policy_redirect: Redirect SSH traffic to matching transparent
            proxy policy. (optional)
            webproxy_forward_server: Web proxy forward server name. (optional)
            isolator_server: Isolator server name. (optional)
            webproxy_profile: Name of web proxy profile. (optional)
            transparent: Enable to use the IP address of the client to connect
            to the server. (optional)
            disclaimer: Web proxy disclaimer setting: by domain, policy, or
            user. (optional)
            utm_status: Enable the use of UTM profiles/sensors/lists.
            (optional)
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
            ips_voip_filter: Name of an existing VoIP (ips) profile. (optional)
            sctp_filter_profile: Name of an existing SCTP filter profile.
            (optional)
            icap_profile: Name of an existing ICAP profile. (optional)
            videofilter_profile: Name of an existing VideoFilter profile.
            (optional)
            waf_profile: Name of an existing Web application firewall profile.
            (optional)
            ssh_filter_profile: Name of an existing SSH filter profile.
            (optional)
            casb_profile: Name of an existing CASB profile. (optional)
            replacemsg_override_group: Authentication replacement message
            override group. (optional)
            logtraffic_start: Enable/disable policy log traffic start.
            (optional)
            log_http_transaction: Enable/disable HTTP transaction log.
            (optional)
            comments: Optional comments. (optional)
            block_notification: Enable/disable block notification. (optional)
            redirect_url: Redirect URL for further explicit web proxy
            processing. (optional)
            https_sub_category: Enable/disable HTTPS sub-category policy
            matching. (optional)
            decrypted_traffic_mirror: Decrypted traffic mirror. (optional)
            detect_https_in_http_request: Enable/disable detection of HTTPS in
            HTTP request. (optional)
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
        endpoint = f"/firewall/proxy-policy/{policyid}"
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
        if proxy is not None:
            data_payload["proxy"] = proxy
        if access_proxy is not None:
            data_payload["access-proxy"] = access_proxy
        if access_proxy6 is not None:
            data_payload["access-proxy6"] = access_proxy6
        if ztna_proxy is not None:
            data_payload["ztna-proxy"] = ztna_proxy
        if srcintf is not None:
            data_payload["srcint"] = srcintf
        if dstintf is not None:
            data_payload["dstint"] = dstintf
        if srcaddr is not None:
            data_payload["srcaddr"] = srcaddr
        if poolname is not None:
            data_payload["poolname"] = poolname
        if poolname6 is not None:
            data_payload["poolname6"] = poolname6
        if dstaddr is not None:
            data_payload["dstaddr"] = dstaddr
        if ztna_ems_tag is not None:
            data_payload["ztna-ems-tag"] = ztna_ems_tag
        if ztna_tags_match_logic is not None:
            data_payload["ztna-tags-match-logic"] = ztna_tags_match_logic
        if device_ownership is not None:
            data_payload["device-ownership"] = device_ownership
        if url_risk is not None:
            data_payload["url-risk"] = url_risk
        if internet_service is not None:
            data_payload["internet-service"] = internet_service
        if internet_service_negate is not None:
            data_payload["internet-service-negate"] = internet_service_negate
        if internet_service_name is not None:
            data_payload["internet-service-name"] = internet_service_name
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
        if internet_service6 is not None:
            data_payload["internet-service6"] = internet_service6
        if internet_service6_negate is not None:
            data_payload["internet-service6-negate"] = internet_service6_negate
        if internet_service6_name is not None:
            data_payload["internet-service6-name"] = internet_service6_name
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
        if service is not None:
            data_payload["service"] = service
        if srcaddr_negate is not None:
            data_payload["srcaddr-negate"] = srcaddr_negate
        if dstaddr_negate is not None:
            data_payload["dstaddr-negate"] = dstaddr_negate
        if ztna_ems_tag_negate is not None:
            data_payload["ztna-ems-tag-negate"] = ztna_ems_tag_negate
        if service_negate is not None:
            data_payload["service-negate"] = service_negate
        if status is not None:
            data_payload["status"] = status
        if schedule is not None:
            data_payload["schedule"] = schedule
        if logtraffic is not None:
            data_payload["logtraffic"] = logtraffic
        if session_ttl is not None:
            data_payload["session-ttl"] = session_ttl
        if srcaddr6 is not None:
            data_payload["srcaddr6"] = srcaddr6
        if dstaddr6 is not None:
            data_payload["dstaddr6"] = dstaddr6
        if groups is not None:
            data_payload["groups"] = groups
        if users is not None:
            data_payload["users"] = users
        if http_tunnel_auth is not None:
            data_payload["http-tunnel-auth"] = http_tunnel_auth
        if ssh_policy_redirect is not None:
            data_payload["ssh-policy-redirect"] = ssh_policy_redirect
        if webproxy_forward_server is not None:
            data_payload["webproxy-forward-server"] = webproxy_forward_server
        if isolator_server is not None:
            data_payload["isolator-server"] = isolator_server
        if webproxy_profile is not None:
            data_payload["webproxy-profile"] = webproxy_profile
        if transparent is not None:
            data_payload["transparent"] = transparent
        if disclaimer is not None:
            data_payload["disclaimer"] = disclaimer
        if utm_status is not None:
            data_payload["utm-status"] = utm_status
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
        if ips_voip_filter is not None:
            data_payload["ips-voip-filter"] = ips_voip_filter
        if sctp_filter_profile is not None:
            data_payload["sctp-filter-profile"] = sctp_filter_profile
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
        if replacemsg_override_group is not None:
            data_payload["replacemsg-override-group"] = (
                replacemsg_override_group
            )
        if logtraffic_start is not None:
            data_payload["logtraffic-start"] = logtraffic_start
        if log_http_transaction is not None:
            data_payload["log-http-transaction"] = log_http_transaction
        if comments is not None:
            data_payload["comments"] = comments
        if block_notification is not None:
            data_payload["block-notification"] = block_notification
        if redirect_url is not None:
            data_payload["redirect-url"] = redirect_url
        if https_sub_category is not None:
            data_payload["https-sub-category"] = https_sub_category
        if decrypted_traffic_mirror is not None:
            data_payload["decrypted-traffic-mirror"] = decrypted_traffic_mirror
        if detect_https_in_http_request is not None:
            data_payload["detect-https-in-http-request"] = (
                detect_https_in_http_request
            )
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
        endpoint = f"/firewall/proxy-policy/{policyid}"
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
        proxy: str | None = None,
        access_proxy: list | None = None,
        access_proxy6: list | None = None,
        ztna_proxy: list | None = None,
        srcintf: list | None = None,
        dstintf: list | None = None,
        srcaddr: list | None = None,
        poolname: list | None = None,
        poolname6: list | None = None,
        dstaddr: list | None = None,
        ztna_ems_tag: list | None = None,
        ztna_tags_match_logic: str | None = None,
        device_ownership: str | None = None,
        url_risk: list | None = None,
        internet_service: str | None = None,
        internet_service_negate: str | None = None,
        internet_service_name: list | None = None,
        internet_service_group: list | None = None,
        internet_service_custom: list | None = None,
        internet_service_custom_group: list | None = None,
        internet_service_fortiguard: list | None = None,
        internet_service6: str | None = None,
        internet_service6_negate: str | None = None,
        internet_service6_name: list | None = None,
        internet_service6_group: list | None = None,
        internet_service6_custom: list | None = None,
        internet_service6_custom_group: list | None = None,
        internet_service6_fortiguard: list | None = None,
        service: list | None = None,
        srcaddr_negate: str | None = None,
        dstaddr_negate: str | None = None,
        ztna_ems_tag_negate: str | None = None,
        service_negate: str | None = None,
        status: str | None = None,
        schedule: str | None = None,
        logtraffic: str | None = None,
        session_ttl: int | None = None,
        srcaddr6: list | None = None,
        dstaddr6: list | None = None,
        groups: list | None = None,
        users: list | None = None,
        http_tunnel_auth: str | None = None,
        ssh_policy_redirect: str | None = None,
        webproxy_forward_server: str | None = None,
        isolator_server: str | None = None,
        webproxy_profile: str | None = None,
        transparent: str | None = None,
        disclaimer: str | None = None,
        utm_status: str | None = None,
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
        ips_voip_filter: str | None = None,
        sctp_filter_profile: str | None = None,
        icap_profile: str | None = None,
        videofilter_profile: str | None = None,
        waf_profile: str | None = None,
        ssh_filter_profile: str | None = None,
        casb_profile: str | None = None,
        replacemsg_override_group: str | None = None,
        logtraffic_start: str | None = None,
        log_http_transaction: str | None = None,
        comments: str | None = None,
        block_notification: str | None = None,
        redirect_url: str | None = None,
        https_sub_category: str | None = None,
        decrypted_traffic_mirror: str | None = None,
        detect_https_in_http_request: str | None = None,
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
            proxy: Type of explicit proxy. (optional)
            access_proxy: IPv4 access proxy. (optional)
            access_proxy6: IPv6 access proxy. (optional)
            ztna_proxy: ZTNA proxies. (optional)
            srcintf: Source interface names. (optional)
            dstintf: Destination interface names. (optional)
            srcaddr: Source address objects. (optional)
            poolname: Name of IP pool object. (optional)
            poolname6: Name of IPv6 pool object. (optional)
            dstaddr: Destination address objects. (optional)
            ztna_ems_tag: ZTNA EMS Tag names. (optional)
            ztna_tags_match_logic: ZTNA tag matching logic. (optional)
            device_ownership: When enabled, the ownership enforcement will be
            done at policy level. (optional)
            url_risk: URL risk level name. (optional)
            internet_service: Enable/disable use of Internet Services for this
            policy. If enabled, destination address and service are not used.
            (optional)
            internet_service_negate: When enabled, Internet Services match
            against any internet service EXCEPT the selected Internet Service.
            (optional)
            internet_service_name: Internet Service name. (optional)
            internet_service_group: Internet Service group name. (optional)
            internet_service_custom: Custom Internet Service name. (optional)
            internet_service_custom_group: Custom Internet Service group name.
            (optional)
            internet_service_fortiguard: FortiGuard Internet Service name.
            (optional)
            internet_service6: Enable/disable use of Internet Services IPv6 for
            this policy. If enabled, destination IPv6 address and service are
            not used. (optional)
            internet_service6_negate: When enabled, Internet Services match
            against any internet service IPv6 EXCEPT the selected Internet
            Service IPv6. (optional)
            internet_service6_name: Internet Service IPv6 name. (optional)
            internet_service6_group: Internet Service IPv6 group name.
            (optional)
            internet_service6_custom: Custom Internet Service IPv6 name.
            (optional)
            internet_service6_custom_group: Custom Internet Service IPv6 group
            name. (optional)
            internet_service6_fortiguard: FortiGuard Internet Service IPv6
            name. (optional)
            service: Name of service objects. (optional)
            srcaddr_negate: When enabled, source addresses match against any
            address EXCEPT the specified source addresses. (optional)
            dstaddr_negate: When enabled, destination addresses match against
            any address EXCEPT the specified destination addresses. (optional)
            ztna_ems_tag_negate: When enabled, ZTNA EMS tags match against any
            tag EXCEPT the specified ZTNA EMS tags. (optional)
            service_negate: When enabled, services match against any service
            EXCEPT the specified destination services. (optional)
            status: Enable/disable the active status of the policy. (optional)
            schedule: Name of schedule object. (optional)
            logtraffic: Enable/disable logging traffic through the policy.
            (optional)
            session_ttl: TTL in seconds for sessions accepted by this policy (0
            means use the system default session TTL). (optional)
            srcaddr6: IPv6 source address objects. (optional)
            dstaddr6: IPv6 destination address objects. (optional)
            groups: Names of group objects. (optional)
            users: Names of user objects. (optional)
            http_tunnel_auth: Enable/disable HTTP tunnel authentication.
            (optional)
            ssh_policy_redirect: Redirect SSH traffic to matching transparent
            proxy policy. (optional)
            webproxy_forward_server: Web proxy forward server name. (optional)
            isolator_server: Isolator server name. (optional)
            webproxy_profile: Name of web proxy profile. (optional)
            transparent: Enable to use the IP address of the client to connect
            to the server. (optional)
            disclaimer: Web proxy disclaimer setting: by domain, policy, or
            user. (optional)
            utm_status: Enable the use of UTM profiles/sensors/lists.
            (optional)
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
            ips_voip_filter: Name of an existing VoIP (ips) profile. (optional)
            sctp_filter_profile: Name of an existing SCTP filter profile.
            (optional)
            icap_profile: Name of an existing ICAP profile. (optional)
            videofilter_profile: Name of an existing VideoFilter profile.
            (optional)
            waf_profile: Name of an existing Web application firewall profile.
            (optional)
            ssh_filter_profile: Name of an existing SSH filter profile.
            (optional)
            casb_profile: Name of an existing CASB profile. (optional)
            replacemsg_override_group: Authentication replacement message
            override group. (optional)
            logtraffic_start: Enable/disable policy log traffic start.
            (optional)
            log_http_transaction: Enable/disable HTTP transaction log.
            (optional)
            comments: Optional comments. (optional)
            block_notification: Enable/disable block notification. (optional)
            redirect_url: Redirect URL for further explicit web proxy
            processing. (optional)
            https_sub_category: Enable/disable HTTPS sub-category policy
            matching. (optional)
            decrypted_traffic_mirror: Decrypted traffic mirror. (optional)
            detect_https_in_http_request: Enable/disable detection of HTTPS in
            HTTP request. (optional)
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
        endpoint = "/firewall/proxy-policy"
        if nkey is not None:
            data_payload["nkey"] = nkey
        if uuid is not None:
            data_payload["uuid"] = uuid
        if policyid is not None:
            data_payload["policyid"] = policyid
        if name is not None:
            data_payload["name"] = name
        if proxy is not None:
            data_payload["proxy"] = proxy
        if access_proxy is not None:
            data_payload["access-proxy"] = access_proxy
        if access_proxy6 is not None:
            data_payload["access-proxy6"] = access_proxy6
        if ztna_proxy is not None:
            data_payload["ztna-proxy"] = ztna_proxy
        if srcintf is not None:
            data_payload["srcint"] = srcintf
        if dstintf is not None:
            data_payload["dstint"] = dstintf
        if srcaddr is not None:
            data_payload["srcaddr"] = srcaddr
        if poolname is not None:
            data_payload["poolname"] = poolname
        if poolname6 is not None:
            data_payload["poolname6"] = poolname6
        if dstaddr is not None:
            data_payload["dstaddr"] = dstaddr
        if ztna_ems_tag is not None:
            data_payload["ztna-ems-tag"] = ztna_ems_tag
        if ztna_tags_match_logic is not None:
            data_payload["ztna-tags-match-logic"] = ztna_tags_match_logic
        if device_ownership is not None:
            data_payload["device-ownership"] = device_ownership
        if url_risk is not None:
            data_payload["url-risk"] = url_risk
        if internet_service is not None:
            data_payload["internet-service"] = internet_service
        if internet_service_negate is not None:
            data_payload["internet-service-negate"] = internet_service_negate
        if internet_service_name is not None:
            data_payload["internet-service-name"] = internet_service_name
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
        if internet_service6 is not None:
            data_payload["internet-service6"] = internet_service6
        if internet_service6_negate is not None:
            data_payload["internet-service6-negate"] = internet_service6_negate
        if internet_service6_name is not None:
            data_payload["internet-service6-name"] = internet_service6_name
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
        if service is not None:
            data_payload["service"] = service
        if srcaddr_negate is not None:
            data_payload["srcaddr-negate"] = srcaddr_negate
        if dstaddr_negate is not None:
            data_payload["dstaddr-negate"] = dstaddr_negate
        if ztna_ems_tag_negate is not None:
            data_payload["ztna-ems-tag-negate"] = ztna_ems_tag_negate
        if service_negate is not None:
            data_payload["service-negate"] = service_negate
        if status is not None:
            data_payload["status"] = status
        if schedule is not None:
            data_payload["schedule"] = schedule
        if logtraffic is not None:
            data_payload["logtraffic"] = logtraffic
        if session_ttl is not None:
            data_payload["session-ttl"] = session_ttl
        if srcaddr6 is not None:
            data_payload["srcaddr6"] = srcaddr6
        if dstaddr6 is not None:
            data_payload["dstaddr6"] = dstaddr6
        if groups is not None:
            data_payload["groups"] = groups
        if users is not None:
            data_payload["users"] = users
        if http_tunnel_auth is not None:
            data_payload["http-tunnel-auth"] = http_tunnel_auth
        if ssh_policy_redirect is not None:
            data_payload["ssh-policy-redirect"] = ssh_policy_redirect
        if webproxy_forward_server is not None:
            data_payload["webproxy-forward-server"] = webproxy_forward_server
        if isolator_server is not None:
            data_payload["isolator-server"] = isolator_server
        if webproxy_profile is not None:
            data_payload["webproxy-profile"] = webproxy_profile
        if transparent is not None:
            data_payload["transparent"] = transparent
        if disclaimer is not None:
            data_payload["disclaimer"] = disclaimer
        if utm_status is not None:
            data_payload["utm-status"] = utm_status
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
        if ips_voip_filter is not None:
            data_payload["ips-voip-filter"] = ips_voip_filter
        if sctp_filter_profile is not None:
            data_payload["sctp-filter-profile"] = sctp_filter_profile
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
        if replacemsg_override_group is not None:
            data_payload["replacemsg-override-group"] = (
                replacemsg_override_group
            )
        if logtraffic_start is not None:
            data_payload["logtraffic-start"] = logtraffic_start
        if log_http_transaction is not None:
            data_payload["log-http-transaction"] = log_http_transaction
        if comments is not None:
            data_payload["comments"] = comments
        if block_notification is not None:
            data_payload["block-notification"] = block_notification
        if redirect_url is not None:
            data_payload["redirect-url"] = redirect_url
        if https_sub_category is not None:
            data_payload["https-sub-category"] = https_sub_category
        if decrypted_traffic_mirror is not None:
            data_payload["decrypted-traffic-mirror"] = decrypted_traffic_mirror
        if detect_https_in_http_request is not None:
            data_payload["detect-https-in-http-request"] = (
                detect_https_in_http_request
            )
        data_payload.update(kwargs)
        return self._client.post(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )
