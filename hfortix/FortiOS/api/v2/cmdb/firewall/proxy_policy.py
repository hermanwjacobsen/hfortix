"""
FortiOS proxy-policy API wrapper.
Provides access to /api/v2/cmdb/firewall/proxy-policy endpoint.
"""

from typing import Any, Dict, List, Optional, Union

from hfortix.FortiOS.http_client import encode_path_component


class ProxyPolicy:
    """
    Wrapper for firewall proxy-policy API endpoint.

    Manages proxy-policy configuration with full Swagger-spec parameter support.
    """

    def __init__(self, http_client: Any):
        """
        Initialize the ProxyPolicy wrapper.

        Args:
            http_client: The HTTP client for API communication
        """
        self._client = http_client
        self.path = "firewall/proxy-policy"

    def list(
        self,
        datasource: Optional[Any] = None,
        start: Optional[Any] = None,
        count: Optional[Any] = None,
        skip_to: Optional[Any] = None,
        with_meta: Optional[Any] = None,
        with_contents_hash: Optional[Any] = None,
        skip: Optional[Any] = None,
        format: Optional[Any] = None,
        filter: Optional[Any] = None,
        key: Optional[Any] = None,
        pattern: Optional[Any] = None,
        scope: Optional[Any] = None,
        exclude_default_values: Optional[Any] = None,
        datasource_format: Optional[Any] = None,
        unfiltered_count: Optional[Any] = None,
        stat_items: Optional[Any] = None,
        primary_keys: Optional[Any] = None,
        action: Optional[Any] = None,
        vdom: Optional[Any] = None,
        raw_json: bool = False,
        **kwargs,
    ) -> Dict[str, Any]:
        """
        Retrieve a list of all proxy-policy entries.

        Args:
            datasource: Enable to include datasource information for each linked object.
            start: Starting entry index.
            count: Maximum number of entries to return.
            skip_to: Skip to Nth CMDB entry.
            with_meta: Enable to include meta information about each object (type id, referen
            with_contents_hash: Enable to include a checksum of each object's contents.
            skip: Enable to call CLI skip operator to hide skipped properties.
            format: List of property names to include in results, separated by | (i.e. pol
            filter: Filtering multiple key/value pairs
            key: If present, objects will be filtered on property with this name.
            pattern: If present, objects will be filtered on property with this value.
            scope: Scope [global|vdom|both*]
            exclude_default_values: Exclude properties/objects with default value
            datasource_format: A map of datasources to a string of attributes, separated by | (ie: po
            unfiltered_count: Maximum number of unfiltered entries to interate through.
            stat_items: Items to count occurrence in entire response (multiple items should be
            primary_keys: The primary key to find indexes for.
            action: default: Return the CLI default values for entire CLI tree.
            vdom: Specify the Virtual Domain(s) from which results are returned or chang
            **kwargs: Additional parameters

        Returns:
            API response dictionary with results list
        """
        params = {}

        if datasource is not None:
            params["datasource"] = datasource
        if start is not None:
            params["start"] = start
        if count is not None:
            params["count"] = count
        if skip_to is not None:
            params["skip_to"] = skip_to
        if with_meta is not None:
            params["with_meta"] = with_meta
        if with_contents_hash is not None:
            params["with_contents_hash"] = with_contents_hash
        if skip is not None:
            params["skip"] = skip
        if format is not None:
            params["format"] = format
        if filter is not None:
            params["filter"] = filter
        if key is not None:
            params["key"] = key
        if pattern is not None:
            params["pattern"] = pattern
        if scope is not None:
            params["scope"] = scope
        if exclude_default_values is not None:
            params["exclude-default-values"] = exclude_default_values
        if datasource_format is not None:
            params["datasource_format"] = datasource_format
        if unfiltered_count is not None:
            params["unfiltered_count"] = unfiltered_count
        if stat_items is not None:
            params["stat-items"] = stat_items
        if primary_keys is not None:
            params["primary_keys"] = primary_keys
        if action is not None:
            params["action"] = action
        if vdom is not None:
            params["vdom"] = vdom

        # Add any additional kwargs
        params.update(kwargs)

        # Extract vdom if present
        vdom = params.pop("vdom", None)

        return self._client.get("cmdb", self.path, params=params, vdom=vdom, raw_json=raw_json)

    def get(
        self,
        mkey: Union[str, int],
        attr: Optional[Any] = None,
        count: Optional[Any] = None,
        skip_to_datasource: Optional[Any] = None,
        acs: Optional[Any] = None,
        search: Optional[Any] = None,
        scope: Optional[Any] = None,
        datasource: Optional[Any] = None,
        with_meta: Optional[Any] = None,
        skip: Optional[Any] = None,
        format: Optional[Any] = None,
        action: Optional[Any] = None,
        vdom: Optional[Any] = None,
        raw_json: bool = False,
        **kwargs,
    ) -> Dict[str, Any]:
        """
        Retrieve a specific proxy-policy entry by its policyid.

        Args:
            mkey: The policyid (primary key)
            attr: Attribute name that references other table
            count: Maximum number of entries to return.
            skip_to_datasource: Skip to provided table's Nth entry. E.g {datasource: 'firewall.address
            acs: If true, returned result are in ascending order.
            search: If present, the objects will be filtered by the search value.
            scope: Scope [global|vdom|both*]
            datasource: Enable to include datasource information for each linked object.
            with_meta: Enable to include meta information about each object (type id, referen
            skip: Enable to call CLI skip operator to hide skipped properties.
            format: List of property names to include in results, separated by | (i.e. pol
            action: datasource: Return all applicable datasource entries for a specific at
            vdom: Specify the Virtual Domain(s) from which results are returned or chang
            **kwargs: Additional parameters

        Returns:
            API response dictionary with entry details
        """
        # Validate mkey
        if mkey is None:
            raise ValueError("mkey cannot be None")

        mkey_str = str(mkey)
        if not mkey_str:
            raise ValueError("mkey cannot be empty")

        params = {}

        if attr is not None:
            params["attr"] = attr
        if count is not None:
            params["count"] = count
        if skip_to_datasource is not None:
            params["skip_to_datasource"] = skip_to_datasource
        if acs is not None:
            params["acs"] = acs
        if search is not None:
            params["search"] = search
        if scope is not None:
            params["scope"] = scope
        if datasource is not None:
            params["datasource"] = datasource
        if with_meta is not None:
            params["with_meta"] = with_meta
        if skip is not None:
            params["skip"] = skip
        if format is not None:
            params["format"] = format
        if action is not None:
            params["action"] = action
        if vdom is not None:
            params["vdom"] = vdom

        # Add any additional kwargs
        params.update(kwargs)

        # Extract vdom if present
        vdom = params.pop("vdom", None)

        return self._client.get(
            "cmdb", f"{self.path}/{mkey_str}", params=params, vdom=vdom, raw_json=raw_json
        )

    def create(
        self,
        payload_dict: Optional[Dict[str, Any]] = None,
        vdom: Optional[Any] = None,
        action: Optional[Any] = None,
        nkey: Optional[Any] = None,
        scope: Optional[Any] = None,
        access_proxy: Optional[list] = None,
        access_proxy6: Optional[list] = None,
        application_list: Optional[str] = None,
        av_profile: Optional[str] = None,
        block_notification: Optional[str] = None,
        casb_profile: Optional[str] = None,
        comments: Optional[str] = None,
        decrypted_traffic_mirror: Optional[str] = None,
        detect_https_in_http_request: Optional[str] = None,
        device_ownership: Optional[str] = None,
        disclaimer: Optional[str] = None,
        dlp_profile: Optional[str] = None,
        dnsfilter_profile: Optional[str] = None,
        dstaddr: Optional[list] = None,
        dstaddr_negate: Optional[str] = None,
        dstaddr6: Optional[list] = None,
        dstintf: Optional[list] = None,
        emailfilter_profile: Optional[str] = None,
        file_filter_profile: Optional[str] = None,
        groups: Optional[list] = None,
        http_tunnel_auth: Optional[str] = None,
        https_sub_category: Optional[str] = None,
        icap_profile: Optional[str] = None,
        internet_service: Optional[str] = None,
        internet_service_custom: Optional[list] = None,
        internet_service_custom_group: Optional[list] = None,
        internet_service_fortiguard: Optional[list] = None,
        internet_service_group: Optional[list] = None,
        internet_service_name: Optional[list] = None,
        internet_service_negate: Optional[str] = None,
        internet_service6: Optional[str] = None,
        internet_service6_custom: Optional[list] = None,
        internet_service6_custom_group: Optional[list] = None,
        internet_service6_fortiguard: Optional[list] = None,
        internet_service6_group: Optional[list] = None,
        internet_service6_name: Optional[list] = None,
        internet_service6_negate: Optional[str] = None,
        ips_sensor: Optional[str] = None,
        ips_voip_filter: Optional[str] = None,
        isolator_server: Optional[str] = None,
        log_http_transaction: Optional[str] = None,
        logtraffic: Optional[str] = None,
        logtraffic_start: Optional[str] = None,
        name: Optional[str] = None,
        policyid: Optional[int] = None,
        poolname: Optional[list] = None,
        poolname6: Optional[list] = None,
        profile_group: Optional[str] = None,
        profile_protocol_options: Optional[str] = None,
        profile_type: Optional[str] = None,
        proxy: Optional[str] = None,
        redirect_url: Optional[str] = None,
        replacemsg_override_group: Optional[str] = None,
        schedule: Optional[str] = None,
        sctp_filter_profile: Optional[str] = None,
        service: Optional[list] = None,
        service_negate: Optional[str] = None,
        session_ttl: Optional[int] = None,
        srcaddr: Optional[list] = None,
        srcaddr_negate: Optional[str] = None,
        srcaddr6: Optional[list] = None,
        srcintf: Optional[list] = None,
        ssh_filter_profile: Optional[str] = None,
        ssh_policy_redirect: Optional[str] = None,
        ssl_ssh_profile: Optional[str] = None,
        status: Optional[str] = None,
        transparent: Optional[str] = None,
        url_risk: Optional[list] = None,
        users: Optional[list] = None,
        utm_status: Optional[str] = None,
        uuid: Optional[str] = None,
        videofilter_profile: Optional[str] = None,
        waf_profile: Optional[str] = None,
        webfilter_profile: Optional[str] = None,
        webproxy_forward_server: Optional[str] = None,
        webproxy_profile: Optional[str] = None,
        ztna_ems_tag: Optional[list] = None,
        ztna_ems_tag_negate: Optional[str] = None,
        ztna_proxy: Optional[list] = None,
        ztna_tags_match_logic: Optional[str] = None,
        raw_json: bool = False,
        **kwargs,
    ) -> Dict[str, Any]:
        """
        Create a new proxy-policy entry.

        Supports two usage patterns:
        1. Pass data dict: create(payload_dict={"key": "value"}, vdom="root")
        2. Pass kwargs: create(key="value", vdom="root")

        Args:
            payload_dict: The configuration data (optional if using kwargs)
            vdom: Specify the Virtual Domain(s) from which results are returned or chang
            action: If supported, an action can be specified.
            nkey: If *action=clone*, use *nkey* to specify the ID for the new resource t
            scope: Specify the Scope from which results are returned or changes are appli
            **kwargs: Additional parameters

        Body schema properties (can pass via data dict or as kwargs):

            access-proxy (list[object]):
                IPv4 access proxy.
            access-proxy6 (list[object]):
                IPv6 access proxy.
            action (string) (enum: ['accept', 'deny', 'redirect']):
                Accept or deny traffic matching the policy parameters.
            application-list (string) (max_len: 47):
                Name of an existing Application list.
            av-profile (string) (max_len: 47):
                Name of an existing Antivirus profile.
            block-notification (string) (enum: ['enable', 'disable']):
                Enable/disable block notification.
            casb-profile (string) (max_len: 47):
                Name of an existing CASB profile.
            comments (string) (max_len: 1023):
                Optional comments.
            decrypted-traffic-mirror (string) (max_len: 35):
                Decrypted traffic mirror.
            detect-https-in-http-request (string) (enum: ['enable', 'disable']):
                Enable/disable detection of HTTPS in HTTP request.
            device-ownership (string) (enum: ['enable', 'disable']):
                When enabled, the ownership enforcement will be done at poli...
            disclaimer (string) (enum: ['disable', 'domain', 'policy']):
                Web proxy disclaimer setting: by domain, policy, or user.
            dlp-profile (string) (max_len: 47):
                Name of an existing DLP profile.
            dnsfilter-profile (string) (max_len: 47):
                Name of an existing DNS filter profile.
            dstaddr (list[object]):
                Destination address objects.
            dstaddr-negate (string) (enum: ['enable', 'disable']):
                When enabled, destination addresses match against any addres...
            dstaddr6 (list[object]):
                IPv6 destination address objects.
            dstintf (list[object]):
                Destination interface names.
            emailfilter-profile (string) (max_len: 47):
                Name of an existing email filter profile.
            file-filter-profile (string) (max_len: 47):
                Name of an existing file-filter profile.
            groups (list[object]):
                Names of group objects.
            http-tunnel-auth (string) (enum: ['enable', 'disable']):
                Enable/disable HTTP tunnel authentication.
            https-sub-category (string) (enum: ['enable', 'disable']):
                Enable/disable HTTPS sub-category policy matching.
            icap-profile (string) (max_len: 47):
                Name of an existing ICAP profile.
            internet-service (string) (enum: ['enable', 'disable']):
                Enable/disable use of Internet Services for this policy. If ...
            internet-service-custom (list[object]):
                Custom Internet Service name.
            internet-service-custom-group (list[object]):
                Custom Internet Service group name.
            internet-service-fortiguard (list[object]):
                FortiGuard Internet Service name.
            internet-service-group (list[object]):
                Internet Service group name.
            internet-service-name (list[object]):
                Internet Service name.
            internet-service-negate (string) (enum: ['enable', 'disable']):
                When enabled, Internet Services match against any internet s...
            internet-service6 (string) (enum: ['enable', 'disable']):
                Enable/disable use of Internet Services IPv6 for this policy...
            internet-service6-custom (list[object]):
                Custom Internet Service IPv6 name.
            internet-service6-custom-group (list[object]):
                Custom Internet Service IPv6 group name.
            internet-service6-fortiguard (list[object]):
                FortiGuard Internet Service IPv6 name.
            internet-service6-group (list[object]):
                Internet Service IPv6 group name.
            internet-service6-name (list[object]):
                Internet Service IPv6 name.
            internet-service6-negate (string) (enum: ['enable', 'disable']):
                When enabled, Internet Services match against any internet s...
            ips-sensor (string) (max_len: 47):
                Name of an existing IPS sensor.
            ips-voip-filter (string) (max_len: 47):
                Name of an existing VoIP (ips) profile.
            isolator-server (string) (max_len: 63):
                Isolator server name.
            log-http-transaction (string) (enum: ['enable', 'disable']):
                Enable/disable HTTP transaction log.
            logtraffic (string) (enum: ['all', 'utm', 'disable']):
                Enable/disable logging traffic through the policy.
            logtraffic-start (string) (enum: ['enable', 'disable']):
                Enable/disable policy log traffic start.
            name (string) (max_len: 35):
                Policy name.
            policyid (integer) (range: 0-4294967295):
                Policy ID.
            poolname (list[object]):
                Name of IP pool object.
            poolname6 (list[object]):
                Name of IPv6 pool object.
            profile-group (string) (max_len: 47):
                Name of profile group.
            profile-protocol-options (string) (max_len: 47):
                Name of an existing Protocol options profile.
            profile-type (string) (enum: ['single', 'group']):
                Determine whether the firewall policy allows security profil...
            proxy (string) (enum: ['explicit-web', 'transparent-web', 'ftp']):
                Type of explicit proxy.
            redirect-url (string) (max_len: 1023):
                Redirect URL for further explicit web proxy processing.
            replacemsg-override-group (string) (max_len: 35):
                Authentication replacement message override group.
            schedule (string) (max_len: 35):
                Name of schedule object.
            sctp-filter-profile (string) (max_len: 47):
                Name of an existing SCTP filter profile.
            service (list[object]):
                Name of service objects.
            service-negate (string) (enum: ['enable', 'disable']):
                When enabled, services match against any service EXCEPT the ...
            session-ttl (integer) (range: 300-2764800):
                TTL in seconds for sessions accepted by this policy (0 means...
            srcaddr (list[object]):
                Source address objects.
            srcaddr-negate (string) (enum: ['enable', 'disable']):
                When enabled, source addresses match against any address EXC...
            srcaddr6 (list[object]):
                IPv6 source address objects.
            srcintf (list[object]):
                Source interface names.
            ssh-filter-profile (string) (max_len: 47):
                Name of an existing SSH filter profile.
            ssh-policy-redirect (string) (enum: ['enable', 'disable']):
                Redirect SSH traffic to matching transparent proxy policy.
            ssl-ssh-profile (string) (max_len: 47):
                Name of an existing SSL SSH profile.
            status (string) (enum: ['enable', 'disable']):
                Enable/disable the active status of the policy.
            transparent (string) (enum: ['enable', 'disable']):
                Enable to use the IP address of the client to connect to the...
            url-risk (list[object]):
                URL risk level name.
            users (list[object]):
                Names of user objects.
            utm-status (string) (enum: ['enable', 'disable']):
                Enable the use of UTM profiles/sensors/lists.
            uuid (string):
                Universally Unique Identifier (UUID; automatically assigned ...
            videofilter-profile (string) (max_len: 47):
                Name of an existing VideoFilter profile.
            waf-profile (string) (max_len: 47):
                Name of an existing Web application firewall profile.
            webfilter-profile (string) (max_len: 47):
                Name of an existing Web filter profile.
            webproxy-forward-server (string) (max_len: 63):
                Web proxy forward server name.
            webproxy-profile (string) (max_len: 63):
                Name of web proxy profile.
            ztna-ems-tag (list[object]):
                ZTNA EMS Tag names.
            ztna-ems-tag-negate (string) (enum: ['enable', 'disable']):
                When enabled, ZTNA EMS tags match against any tag EXCEPT the...
            ztna-proxy (list[object]):
                ZTNA proxies.
            ztna-tags-match-logic (string) (enum: ['or', 'and']):
                ZTNA tag matching logic.

        Returns:
            API response dictionary
        """
        # Build data from kwargs if not provided
        if payload_dict is None:
            payload_dict = {}
        if access_proxy is not None:
            payload_dict["access-proxy"] = access_proxy
        if access_proxy6 is not None:
            payload_dict["access-proxy6"] = access_proxy6
        if action is not None:
            payload_dict["action"] = action
        if application_list is not None:
            payload_dict["application-list"] = application_list
        if av_profile is not None:
            payload_dict["av-profile"] = av_profile
        if block_notification is not None:
            payload_dict["block-notification"] = block_notification
        if casb_profile is not None:
            payload_dict["casb-profile"] = casb_profile
        if comments is not None:
            payload_dict["comments"] = comments
        if decrypted_traffic_mirror is not None:
            payload_dict["decrypted-traffic-mirror"] = decrypted_traffic_mirror
        if detect_https_in_http_request is not None:
            payload_dict["detect-https-in-http-request"] = detect_https_in_http_request
        if device_ownership is not None:
            payload_dict["device-ownership"] = device_ownership
        if disclaimer is not None:
            payload_dict["disclaimer"] = disclaimer
        if dlp_profile is not None:
            payload_dict["dlp-profile"] = dlp_profile
        if dnsfilter_profile is not None:
            payload_dict["dnsfilter-profile"] = dnsfilter_profile
        if dstaddr is not None:
            payload_dict["dstaddr"] = dstaddr
        if dstaddr_negate is not None:
            payload_dict["dstaddr-negate"] = dstaddr_negate
        if dstaddr6 is not None:
            payload_dict["dstaddr6"] = dstaddr6
        if dstintf is not None:
            payload_dict["dstintf"] = dstintf
        if emailfilter_profile is not None:
            payload_dict["emailfilter-profile"] = emailfilter_profile
        if file_filter_profile is not None:
            payload_dict["file-filter-profile"] = file_filter_profile
        if groups is not None:
            payload_dict["groups"] = groups
        if http_tunnel_auth is not None:
            payload_dict["http-tunnel-auth"] = http_tunnel_auth
        if https_sub_category is not None:
            payload_dict["https-sub-category"] = https_sub_category
        if icap_profile is not None:
            payload_dict["icap-profile"] = icap_profile
        if internet_service is not None:
            payload_dict["internet-service"] = internet_service
        if internet_service_custom is not None:
            payload_dict["internet-service-custom"] = internet_service_custom
        if internet_service_custom_group is not None:
            payload_dict["internet-service-custom-group"] = internet_service_custom_group
        if internet_service_fortiguard is not None:
            payload_dict["internet-service-fortiguard"] = internet_service_fortiguard
        if internet_service_group is not None:
            payload_dict["internet-service-group"] = internet_service_group
        if internet_service_name is not None:
            payload_dict["internet-service-name"] = internet_service_name
        if internet_service_negate is not None:
            payload_dict["internet-service-negate"] = internet_service_negate
        if internet_service6 is not None:
            payload_dict["internet-service6"] = internet_service6
        if internet_service6_custom is not None:
            payload_dict["internet-service6-custom"] = internet_service6_custom
        if internet_service6_custom_group is not None:
            payload_dict["internet-service6-custom-group"] = internet_service6_custom_group
        if internet_service6_fortiguard is not None:
            payload_dict["internet-service6-fortiguard"] = internet_service6_fortiguard
        if internet_service6_group is not None:
            payload_dict["internet-service6-group"] = internet_service6_group
        if internet_service6_name is not None:
            payload_dict["internet-service6-name"] = internet_service6_name
        if internet_service6_negate is not None:
            payload_dict["internet-service6-negate"] = internet_service6_negate
        if ips_sensor is not None:
            payload_dict["ips-sensor"] = ips_sensor
        if ips_voip_filter is not None:
            payload_dict["ips-voip-filter"] = ips_voip_filter
        if isolator_server is not None:
            payload_dict["isolator-server"] = isolator_server
        if log_http_transaction is not None:
            payload_dict["log-http-transaction"] = log_http_transaction
        if logtraffic is not None:
            payload_dict["logtraffic"] = logtraffic
        if logtraffic_start is not None:
            payload_dict["logtraffic-start"] = logtraffic_start
        if name is not None:
            payload_dict["name"] = name
        if policyid is not None:
            payload_dict["policyid"] = policyid
        if poolname is not None:
            payload_dict["poolname"] = poolname
        if poolname6 is not None:
            payload_dict["poolname6"] = poolname6
        if profile_group is not None:
            payload_dict["profile-group"] = profile_group
        if profile_protocol_options is not None:
            payload_dict["profile-protocol-options"] = profile_protocol_options
        if profile_type is not None:
            payload_dict["profile-type"] = profile_type
        if proxy is not None:
            payload_dict["proxy"] = proxy
        if redirect_url is not None:
            payload_dict["redirect-url"] = redirect_url
        if replacemsg_override_group is not None:
            payload_dict["replacemsg-override-group"] = replacemsg_override_group
        if schedule is not None:
            payload_dict["schedule"] = schedule
        if sctp_filter_profile is not None:
            payload_dict["sctp-filter-profile"] = sctp_filter_profile
        if service is not None:
            payload_dict["service"] = service
        if service_negate is not None:
            payload_dict["service-negate"] = service_negate
        if session_ttl is not None:
            payload_dict["session-ttl"] = session_ttl
        if srcaddr is not None:
            payload_dict["srcaddr"] = srcaddr
        if srcaddr_negate is not None:
            payload_dict["srcaddr-negate"] = srcaddr_negate
        if srcaddr6 is not None:
            payload_dict["srcaddr6"] = srcaddr6
        if srcintf is not None:
            payload_dict["srcintf"] = srcintf
        if ssh_filter_profile is not None:
            payload_dict["ssh-filter-profile"] = ssh_filter_profile
        if ssh_policy_redirect is not None:
            payload_dict["ssh-policy-redirect"] = ssh_policy_redirect
        if ssl_ssh_profile is not None:
            payload_dict["ssl-ssh-profile"] = ssl_ssh_profile
        if status is not None:
            payload_dict["status"] = status
        if transparent is not None:
            payload_dict["transparent"] = transparent
        if url_risk is not None:
            payload_dict["url-risk"] = url_risk
        if users is not None:
            payload_dict["users"] = users
        if utm_status is not None:
            payload_dict["utm-status"] = utm_status
        if uuid is not None:
            payload_dict["uuid"] = uuid
        if videofilter_profile is not None:
            payload_dict["videofilter-profile"] = videofilter_profile
        if waf_profile is not None:
            payload_dict["waf-profile"] = waf_profile
        if webfilter_profile is not None:
            payload_dict["webfilter-profile"] = webfilter_profile
        if webproxy_forward_server is not None:
            payload_dict["webproxy-forward-server"] = webproxy_forward_server
        if webproxy_profile is not None:
            payload_dict["webproxy-profile"] = webproxy_profile
        if ztna_ems_tag is not None:
            payload_dict["ztna-ems-tag"] = ztna_ems_tag
        if ztna_ems_tag_negate is not None:
            payload_dict["ztna-ems-tag-negate"] = ztna_ems_tag_negate
        if ztna_proxy is not None:
            payload_dict["ztna-proxy"] = ztna_proxy
        if ztna_tags_match_logic is not None:
            payload_dict["ztna-tags-match-logic"] = ztna_tags_match_logic

        params = {}

        if vdom is not None:
            params["vdom"] = vdom
        if action is not None:
            params["action"] = action
        if nkey is not None:
            params["nkey"] = nkey
        if scope is not None:
            params["scope"] = scope

        # Add any additional kwargs
        params.update(kwargs)

        # Extract vdom if present
        vdom = params.pop("vdom", None)

        return self._client.post(
            "cmdb", self.path, data=payload_dict, params=params, vdom=vdom, raw_json=raw_json
        )

    def update(
        self,
        mkey: Union[str, int],
        payload_dict: Optional[Dict[str, Any]] = None,
        vdom: Optional[Any] = None,
        action: Optional[Any] = None,
        before: Optional[Any] = None,
        after: Optional[Any] = None,
        scope: Optional[Any] = None,
        access_proxy: Optional[list] = None,
        access_proxy6: Optional[list] = None,
        application_list: Optional[str] = None,
        av_profile: Optional[str] = None,
        block_notification: Optional[str] = None,
        casb_profile: Optional[str] = None,
        comments: Optional[str] = None,
        decrypted_traffic_mirror: Optional[str] = None,
        detect_https_in_http_request: Optional[str] = None,
        device_ownership: Optional[str] = None,
        disclaimer: Optional[str] = None,
        dlp_profile: Optional[str] = None,
        dnsfilter_profile: Optional[str] = None,
        dstaddr: Optional[list] = None,
        dstaddr_negate: Optional[str] = None,
        dstaddr6: Optional[list] = None,
        dstintf: Optional[list] = None,
        emailfilter_profile: Optional[str] = None,
        file_filter_profile: Optional[str] = None,
        groups: Optional[list] = None,
        http_tunnel_auth: Optional[str] = None,
        https_sub_category: Optional[str] = None,
        icap_profile: Optional[str] = None,
        internet_service: Optional[str] = None,
        internet_service_custom: Optional[list] = None,
        internet_service_custom_group: Optional[list] = None,
        internet_service_fortiguard: Optional[list] = None,
        internet_service_group: Optional[list] = None,
        internet_service_name: Optional[list] = None,
        internet_service_negate: Optional[str] = None,
        internet_service6: Optional[str] = None,
        internet_service6_custom: Optional[list] = None,
        internet_service6_custom_group: Optional[list] = None,
        internet_service6_fortiguard: Optional[list] = None,
        internet_service6_group: Optional[list] = None,
        internet_service6_name: Optional[list] = None,
        internet_service6_negate: Optional[str] = None,
        ips_sensor: Optional[str] = None,
        ips_voip_filter: Optional[str] = None,
        isolator_server: Optional[str] = None,
        log_http_transaction: Optional[str] = None,
        logtraffic: Optional[str] = None,
        logtraffic_start: Optional[str] = None,
        name: Optional[str] = None,
        policyid: Optional[int] = None,
        poolname: Optional[list] = None,
        poolname6: Optional[list] = None,
        profile_group: Optional[str] = None,
        profile_protocol_options: Optional[str] = None,
        profile_type: Optional[str] = None,
        proxy: Optional[str] = None,
        redirect_url: Optional[str] = None,
        replacemsg_override_group: Optional[str] = None,
        schedule: Optional[str] = None,
        sctp_filter_profile: Optional[str] = None,
        service: Optional[list] = None,
        service_negate: Optional[str] = None,
        session_ttl: Optional[int] = None,
        srcaddr: Optional[list] = None,
        srcaddr_negate: Optional[str] = None,
        srcaddr6: Optional[list] = None,
        srcintf: Optional[list] = None,
        ssh_filter_profile: Optional[str] = None,
        ssh_policy_redirect: Optional[str] = None,
        ssl_ssh_profile: Optional[str] = None,
        status: Optional[str] = None,
        transparent: Optional[str] = None,
        url_risk: Optional[list] = None,
        users: Optional[list] = None,
        utm_status: Optional[str] = None,
        uuid: Optional[str] = None,
        videofilter_profile: Optional[str] = None,
        waf_profile: Optional[str] = None,
        webfilter_profile: Optional[str] = None,
        webproxy_forward_server: Optional[str] = None,
        webproxy_profile: Optional[str] = None,
        ztna_ems_tag: Optional[list] = None,
        ztna_ems_tag_negate: Optional[str] = None,
        ztna_proxy: Optional[list] = None,
        ztna_tags_match_logic: Optional[str] = None,
        raw_json: bool = False,
        **kwargs,
    ) -> Dict[str, Any]:
        """
        Update an existing proxy-policy entry.

        Supports two usage patterns:
        1. Pass data dict: update(mkey=123, payload_dict={"key": "value"}, vdom="root")
        2. Pass kwargs: update(mkey=123, key="value", vdom="root")

        Args:
            mkey: The policyid (primary key)
            payload_dict: The updated configuration data (optional if using kwargs)
            vdom: Specify the Virtual Domain(s) from which results are returned or chang
            action: If supported, an action can be specified.
            before: If *action=move*, use *before* to specify the ID of the resource that
            after: If *action=move*, use *after* to specify the ID of the resource that t
            scope: Specify the Scope from which results are returned or changes are appli
            **kwargs: Additional parameters

        Body schema properties (can pass via data dict or as kwargs):

            access-proxy (list[object]):
                IPv4 access proxy.
            access-proxy6 (list[object]):
                IPv6 access proxy.
            action (string) (enum: ['accept', 'deny', 'redirect']):
                Accept or deny traffic matching the policy parameters.
            application-list (string) (max_len: 47):
                Name of an existing Application list.
            av-profile (string) (max_len: 47):
                Name of an existing Antivirus profile.
            block-notification (string) (enum: ['enable', 'disable']):
                Enable/disable block notification.
            casb-profile (string) (max_len: 47):
                Name of an existing CASB profile.
            comments (string) (max_len: 1023):
                Optional comments.
            decrypted-traffic-mirror (string) (max_len: 35):
                Decrypted traffic mirror.
            detect-https-in-http-request (string) (enum: ['enable', 'disable']):
                Enable/disable detection of HTTPS in HTTP request.
            device-ownership (string) (enum: ['enable', 'disable']):
                When enabled, the ownership enforcement will be done at poli...
            disclaimer (string) (enum: ['disable', 'domain', 'policy']):
                Web proxy disclaimer setting: by domain, policy, or user.
            dlp-profile (string) (max_len: 47):
                Name of an existing DLP profile.
            dnsfilter-profile (string) (max_len: 47):
                Name of an existing DNS filter profile.
            dstaddr (list[object]):
                Destination address objects.
            dstaddr-negate (string) (enum: ['enable', 'disable']):
                When enabled, destination addresses match against any addres...
            dstaddr6 (list[object]):
                IPv6 destination address objects.
            dstintf (list[object]):
                Destination interface names.
            emailfilter-profile (string) (max_len: 47):
                Name of an existing email filter profile.
            file-filter-profile (string) (max_len: 47):
                Name of an existing file-filter profile.
            groups (list[object]):
                Names of group objects.
            http-tunnel-auth (string) (enum: ['enable', 'disable']):
                Enable/disable HTTP tunnel authentication.
            https-sub-category (string) (enum: ['enable', 'disable']):
                Enable/disable HTTPS sub-category policy matching.
            icap-profile (string) (max_len: 47):
                Name of an existing ICAP profile.
            internet-service (string) (enum: ['enable', 'disable']):
                Enable/disable use of Internet Services for this policy. If ...
            internet-service-custom (list[object]):
                Custom Internet Service name.
            internet-service-custom-group (list[object]):
                Custom Internet Service group name.
            internet-service-fortiguard (list[object]):
                FortiGuard Internet Service name.
            internet-service-group (list[object]):
                Internet Service group name.
            internet-service-name (list[object]):
                Internet Service name.
            internet-service-negate (string) (enum: ['enable', 'disable']):
                When enabled, Internet Services match against any internet s...
            internet-service6 (string) (enum: ['enable', 'disable']):
                Enable/disable use of Internet Services IPv6 for this policy...
            internet-service6-custom (list[object]):
                Custom Internet Service IPv6 name.
            internet-service6-custom-group (list[object]):
                Custom Internet Service IPv6 group name.
            internet-service6-fortiguard (list[object]):
                FortiGuard Internet Service IPv6 name.
            internet-service6-group (list[object]):
                Internet Service IPv6 group name.
            internet-service6-name (list[object]):
                Internet Service IPv6 name.
            internet-service6-negate (string) (enum: ['enable', 'disable']):
                When enabled, Internet Services match against any internet s...
            ips-sensor (string) (max_len: 47):
                Name of an existing IPS sensor.
            ips-voip-filter (string) (max_len: 47):
                Name of an existing VoIP (ips) profile.
            isolator-server (string) (max_len: 63):
                Isolator server name.
            log-http-transaction (string) (enum: ['enable', 'disable']):
                Enable/disable HTTP transaction log.
            logtraffic (string) (enum: ['all', 'utm', 'disable']):
                Enable/disable logging traffic through the policy.
            logtraffic-start (string) (enum: ['enable', 'disable']):
                Enable/disable policy log traffic start.
            name (string) (max_len: 35):
                Policy name.
            policyid (integer) (range: 0-4294967295):
                Policy ID.
            poolname (list[object]):
                Name of IP pool object.
            poolname6 (list[object]):
                Name of IPv6 pool object.
            profile-group (string) (max_len: 47):
                Name of profile group.
            profile-protocol-options (string) (max_len: 47):
                Name of an existing Protocol options profile.
            profile-type (string) (enum: ['single', 'group']):
                Determine whether the firewall policy allows security profil...
            proxy (string) (enum: ['explicit-web', 'transparent-web', 'ftp']):
                Type of explicit proxy.
            redirect-url (string) (max_len: 1023):
                Redirect URL for further explicit web proxy processing.
            replacemsg-override-group (string) (max_len: 35):
                Authentication replacement message override group.
            schedule (string) (max_len: 35):
                Name of schedule object.
            sctp-filter-profile (string) (max_len: 47):
                Name of an existing SCTP filter profile.
            service (list[object]):
                Name of service objects.
            service-negate (string) (enum: ['enable', 'disable']):
                When enabled, services match against any service EXCEPT the ...
            session-ttl (integer) (range: 300-2764800):
                TTL in seconds for sessions accepted by this policy (0 means...
            srcaddr (list[object]):
                Source address objects.
            srcaddr-negate (string) (enum: ['enable', 'disable']):
                When enabled, source addresses match against any address EXC...
            srcaddr6 (list[object]):
                IPv6 source address objects.
            srcintf (list[object]):
                Source interface names.
            ssh-filter-profile (string) (max_len: 47):
                Name of an existing SSH filter profile.
            ssh-policy-redirect (string) (enum: ['enable', 'disable']):
                Redirect SSH traffic to matching transparent proxy policy.
            ssl-ssh-profile (string) (max_len: 47):
                Name of an existing SSL SSH profile.
            status (string) (enum: ['enable', 'disable']):
                Enable/disable the active status of the policy.
            transparent (string) (enum: ['enable', 'disable']):
                Enable to use the IP address of the client to connect to the...
            url-risk (list[object]):
                URL risk level name.
            users (list[object]):
                Names of user objects.
            utm-status (string) (enum: ['enable', 'disable']):
                Enable the use of UTM profiles/sensors/lists.
            uuid (string):
                Universally Unique Identifier (UUID; automatically assigned ...
            videofilter-profile (string) (max_len: 47):
                Name of an existing VideoFilter profile.
            waf-profile (string) (max_len: 47):
                Name of an existing Web application firewall profile.
            webfilter-profile (string) (max_len: 47):
                Name of an existing Web filter profile.
            webproxy-forward-server (string) (max_len: 63):
                Web proxy forward server name.
            webproxy-profile (string) (max_len: 63):
                Name of web proxy profile.
            ztna-ems-tag (list[object]):
                ZTNA EMS Tag names.
            ztna-ems-tag-negate (string) (enum: ['enable', 'disable']):
                When enabled, ZTNA EMS tags match against any tag EXCEPT the...
            ztna-proxy (list[object]):
                ZTNA proxies.
            ztna-tags-match-logic (string) (enum: ['or', 'and']):
                ZTNA tag matching logic.

        Returns:
            API response dictionary
        """
        # Validate mkey
        if mkey is None:
            raise ValueError("mkey cannot be None")

        mkey_str = str(mkey)
        if not mkey_str:
            raise ValueError("mkey cannot be empty")

        # Build data from kwargs if not provided
        if payload_dict is None:
            payload_dict = {}
        if access_proxy is not None:
            payload_dict["access-proxy"] = access_proxy
        if access_proxy6 is not None:
            payload_dict["access-proxy6"] = access_proxy6
        if action is not None:
            payload_dict["action"] = action
        if application_list is not None:
            payload_dict["application-list"] = application_list
        if av_profile is not None:
            payload_dict["av-profile"] = av_profile
        if block_notification is not None:
            payload_dict["block-notification"] = block_notification
        if casb_profile is not None:
            payload_dict["casb-profile"] = casb_profile
        if comments is not None:
            payload_dict["comments"] = comments
        if decrypted_traffic_mirror is not None:
            payload_dict["decrypted-traffic-mirror"] = decrypted_traffic_mirror
        if detect_https_in_http_request is not None:
            payload_dict["detect-https-in-http-request"] = detect_https_in_http_request
        if device_ownership is not None:
            payload_dict["device-ownership"] = device_ownership
        if disclaimer is not None:
            payload_dict["disclaimer"] = disclaimer
        if dlp_profile is not None:
            payload_dict["dlp-profile"] = dlp_profile
        if dnsfilter_profile is not None:
            payload_dict["dnsfilter-profile"] = dnsfilter_profile
        if dstaddr is not None:
            payload_dict["dstaddr"] = dstaddr
        if dstaddr_negate is not None:
            payload_dict["dstaddr-negate"] = dstaddr_negate
        if dstaddr6 is not None:
            payload_dict["dstaddr6"] = dstaddr6
        if dstintf is not None:
            payload_dict["dstintf"] = dstintf
        if emailfilter_profile is not None:
            payload_dict["emailfilter-profile"] = emailfilter_profile
        if file_filter_profile is not None:
            payload_dict["file-filter-profile"] = file_filter_profile
        if groups is not None:
            payload_dict["groups"] = groups
        if http_tunnel_auth is not None:
            payload_dict["http-tunnel-auth"] = http_tunnel_auth
        if https_sub_category is not None:
            payload_dict["https-sub-category"] = https_sub_category
        if icap_profile is not None:
            payload_dict["icap-profile"] = icap_profile
        if internet_service is not None:
            payload_dict["internet-service"] = internet_service
        if internet_service_custom is not None:
            payload_dict["internet-service-custom"] = internet_service_custom
        if internet_service_custom_group is not None:
            payload_dict["internet-service-custom-group"] = internet_service_custom_group
        if internet_service_fortiguard is not None:
            payload_dict["internet-service-fortiguard"] = internet_service_fortiguard
        if internet_service_group is not None:
            payload_dict["internet-service-group"] = internet_service_group
        if internet_service_name is not None:
            payload_dict["internet-service-name"] = internet_service_name
        if internet_service_negate is not None:
            payload_dict["internet-service-negate"] = internet_service_negate
        if internet_service6 is not None:
            payload_dict["internet-service6"] = internet_service6
        if internet_service6_custom is not None:
            payload_dict["internet-service6-custom"] = internet_service6_custom
        if internet_service6_custom_group is not None:
            payload_dict["internet-service6-custom-group"] = internet_service6_custom_group
        if internet_service6_fortiguard is not None:
            payload_dict["internet-service6-fortiguard"] = internet_service6_fortiguard
        if internet_service6_group is not None:
            payload_dict["internet-service6-group"] = internet_service6_group
        if internet_service6_name is not None:
            payload_dict["internet-service6-name"] = internet_service6_name
        if internet_service6_negate is not None:
            payload_dict["internet-service6-negate"] = internet_service6_negate
        if ips_sensor is not None:
            payload_dict["ips-sensor"] = ips_sensor
        if ips_voip_filter is not None:
            payload_dict["ips-voip-filter"] = ips_voip_filter
        if isolator_server is not None:
            payload_dict["isolator-server"] = isolator_server
        if log_http_transaction is not None:
            payload_dict["log-http-transaction"] = log_http_transaction
        if logtraffic is not None:
            payload_dict["logtraffic"] = logtraffic
        if logtraffic_start is not None:
            payload_dict["logtraffic-start"] = logtraffic_start
        if name is not None:
            payload_dict["name"] = name
        if policyid is not None:
            payload_dict["policyid"] = policyid
        if poolname is not None:
            payload_dict["poolname"] = poolname
        if poolname6 is not None:
            payload_dict["poolname6"] = poolname6
        if profile_group is not None:
            payload_dict["profile-group"] = profile_group
        if profile_protocol_options is not None:
            payload_dict["profile-protocol-options"] = profile_protocol_options
        if profile_type is not None:
            payload_dict["profile-type"] = profile_type
        if proxy is not None:
            payload_dict["proxy"] = proxy
        if redirect_url is not None:
            payload_dict["redirect-url"] = redirect_url
        if replacemsg_override_group is not None:
            payload_dict["replacemsg-override-group"] = replacemsg_override_group
        if schedule is not None:
            payload_dict["schedule"] = schedule
        if sctp_filter_profile is not None:
            payload_dict["sctp-filter-profile"] = sctp_filter_profile
        if service is not None:
            payload_dict["service"] = service
        if service_negate is not None:
            payload_dict["service-negate"] = service_negate
        if session_ttl is not None:
            payload_dict["session-ttl"] = session_ttl
        if srcaddr is not None:
            payload_dict["srcaddr"] = srcaddr
        if srcaddr_negate is not None:
            payload_dict["srcaddr-negate"] = srcaddr_negate
        if srcaddr6 is not None:
            payload_dict["srcaddr6"] = srcaddr6
        if srcintf is not None:
            payload_dict["srcintf"] = srcintf
        if ssh_filter_profile is not None:
            payload_dict["ssh-filter-profile"] = ssh_filter_profile
        if ssh_policy_redirect is not None:
            payload_dict["ssh-policy-redirect"] = ssh_policy_redirect
        if ssl_ssh_profile is not None:
            payload_dict["ssl-ssh-profile"] = ssl_ssh_profile
        if status is not None:
            payload_dict["status"] = status
        if transparent is not None:
            payload_dict["transparent"] = transparent
        if url_risk is not None:
            payload_dict["url-risk"] = url_risk
        if users is not None:
            payload_dict["users"] = users
        if utm_status is not None:
            payload_dict["utm-status"] = utm_status
        if uuid is not None:
            payload_dict["uuid"] = uuid
        if videofilter_profile is not None:
            payload_dict["videofilter-profile"] = videofilter_profile
        if waf_profile is not None:
            payload_dict["waf-profile"] = waf_profile
        if webfilter_profile is not None:
            payload_dict["webfilter-profile"] = webfilter_profile
        if webproxy_forward_server is not None:
            payload_dict["webproxy-forward-server"] = webproxy_forward_server
        if webproxy_profile is not None:
            payload_dict["webproxy-profile"] = webproxy_profile
        if ztna_ems_tag is not None:
            payload_dict["ztna-ems-tag"] = ztna_ems_tag
        if ztna_ems_tag_negate is not None:
            payload_dict["ztna-ems-tag-negate"] = ztna_ems_tag_negate
        if ztna_proxy is not None:
            payload_dict["ztna-proxy"] = ztna_proxy
        if ztna_tags_match_logic is not None:
            payload_dict["ztna-tags-match-logic"] = ztna_tags_match_logic

        params = {}

        if vdom is not None:
            params["vdom"] = vdom
        if action is not None:
            params["action"] = action
        if before is not None:
            params["before"] = before
        if after is not None:
            params["after"] = after
        if scope is not None:
            params["scope"] = scope

        # Add any additional kwargs
        params.update(kwargs)

        # Extract vdom if present
        vdom = params.pop("vdom", None)

        return self._client.put(
            "cmdb",
            f"{self.path}/{mkey_str}",
            data=payload_dict,
            params=params,
            vdom=vdom,
            raw_json=raw_json,
        )

    def delete(
        self,
        mkey: Union[str, int],
        vdom: Optional[Any] = None,
        scope: Optional[Any] = None,
        raw_json: bool = False,
        **kwargs,
    ) -> Dict[str, Any]:
        """
        Delete a proxy-policy entry.

        Args:
            mkey: The policyid (primary key)
            vdom: Specify the Virtual Domain(s) from which results are returned or chang
            scope: Specify the Scope from which results are returned or changes are appli
            **kwargs: Additional parameters

        Returns:
            API response dictionary
        """
        # Validate mkey
        if mkey is None:
            raise ValueError("mkey cannot be None")

        mkey_str = str(mkey)
        if not mkey_str:
            raise ValueError("mkey cannot be empty")

        params = {}

        if vdom is not None:
            params["vdom"] = vdom
        if scope is not None:
            params["scope"] = scope

        # Add any additional kwargs
        params.update(kwargs)

        # Extract vdom if present
        vdom = params.pop("vdom", None)

        return self._client.delete(
            "cmdb", f"{self.path}/{mkey_str}", params=params, vdom=vdom, raw_json=raw_json
        )
