"""
FortiOS policy API wrapper.
Provides access to /api/v2/cmdb/firewall/policy endpoint.
"""

from typing import Any, Dict, List, Optional, Union

from hfortix.FortiOS.http_client import encode_path_component


class Policy:
    """
    Wrapper for firewall policy API endpoint.

    Manages policy configuration with full Swagger-spec parameter support.
    """

    def __init__(self, http_client: Any):
        """
        Initialize the Policy wrapper.

        Args:
            http_client: The HTTP client for API communication
        """
        self._client = http_client
        self.path = "firewall/policy"

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
        Retrieve a list of all policy entries.

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
        Retrieve a specific policy entry by its policyid.

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
        anti_replay: Optional[str] = None,
        app_monitor: Optional[str] = None,
        application_list: Optional[str] = None,
        auth_cert: Optional[str] = None,
        auth_path: Optional[str] = None,
        auth_redirect_addr: Optional[str] = None,
        auto_asic_offload: Optional[str] = None,
        av_profile: Optional[str] = None,
        block_notification: Optional[str] = None,
        captive_portal_exempt: Optional[str] = None,
        capture_packet: Optional[str] = None,
        casb_profile: Optional[str] = None,
        comments: Optional[str] = None,
        custom_log_fields: Optional[list] = None,
        decrypted_traffic_mirror: Optional[str] = None,
        delay_tcp_npu_session: Optional[str] = None,
        diameter_filter_profile: Optional[str] = None,
        diffserv_copy: Optional[str] = None,
        diffserv_forward: Optional[str] = None,
        diffserv_reverse: Optional[str] = None,
        diffservcode_forward: Optional[str] = None,
        diffservcode_rev: Optional[str] = None,
        disclaimer: Optional[str] = None,
        dlp_profile: Optional[str] = None,
        dnsfilter_profile: Optional[str] = None,
        dsri: Optional[str] = None,
        dstaddr: Optional[list] = None,
        dstaddr_negate: Optional[str] = None,
        dstaddr6: Optional[list] = None,
        dstaddr6_negate: Optional[str] = None,
        dstintf: Optional[list] = None,
        dynamic_shaping: Optional[str] = None,
        email_collect: Optional[str] = None,
        emailfilter_profile: Optional[str] = None,
        fec: Optional[str] = None,
        file_filter_profile: Optional[str] = None,
        firewall_session_dirty: Optional[str] = None,
        fixedport: Optional[str] = None,
        fsso_agent_for_ntlm: Optional[str] = None,
        fsso_groups: Optional[list] = None,
        geoip_anycast: Optional[str] = None,
        geoip_match: Optional[str] = None,
        groups: Optional[list] = None,
        http_policy_redirect: Optional[str] = None,
        icap_profile: Optional[str] = None,
        identity_based_route: Optional[str] = None,
        inbound: Optional[str] = None,
        inspection_mode: Optional[str] = None,
        internet_service: Optional[str] = None,
        internet_service_custom: Optional[list] = None,
        internet_service_custom_group: Optional[list] = None,
        internet_service_fortiguard: Optional[list] = None,
        internet_service_group: Optional[list] = None,
        internet_service_name: Optional[list] = None,
        internet_service_negate: Optional[str] = None,
        internet_service_src: Optional[str] = None,
        internet_service_src_custom: Optional[list] = None,
        internet_service_src_custom_group: Optional[list] = None,
        internet_service_src_fortiguard: Optional[list] = None,
        internet_service_src_group: Optional[list] = None,
        internet_service_src_name: Optional[list] = None,
        internet_service_src_negate: Optional[str] = None,
        internet_service6: Optional[str] = None,
        internet_service6_custom: Optional[list] = None,
        internet_service6_custom_group: Optional[list] = None,
        internet_service6_fortiguard: Optional[list] = None,
        internet_service6_group: Optional[list] = None,
        internet_service6_name: Optional[list] = None,
        internet_service6_negate: Optional[str] = None,
        internet_service6_src: Optional[str] = None,
        internet_service6_src_custom: Optional[list] = None,
        internet_service6_src_custom_group: Optional[list] = None,
        internet_service6_src_fortiguard: Optional[list] = None,
        internet_service6_src_group: Optional[list] = None,
        internet_service6_src_name: Optional[list] = None,
        internet_service6_src_negate: Optional[str] = None,
        ippool: Optional[str] = None,
        ips_sensor: Optional[str] = None,
        ips_voip_filter: Optional[str] = None,
        log_http_transaction: Optional[str] = None,
        logtraffic: Optional[str] = None,
        logtraffic_start: Optional[str] = None,
        match_vip: Optional[str] = None,
        match_vip_only: Optional[str] = None,
        name: Optional[str] = None,
        nat: Optional[str] = None,
        nat46: Optional[str] = None,
        nat64: Optional[str] = None,
        natinbound: Optional[str] = None,
        natip: Optional[str] = None,
        natoutbound: Optional[str] = None,
        network_service_dynamic: Optional[list] = None,
        network_service_src_dynamic: Optional[list] = None,
        np_acceleration: Optional[str] = None,
        ntlm: Optional[str] = None,
        ntlm_enabled_browsers: Optional[list] = None,
        ntlm_guest: Optional[str] = None,
        outbound: Optional[str] = None,
        passive_wan_health_measurement: Optional[str] = None,
        pcp_inbound: Optional[str] = None,
        pcp_outbound: Optional[str] = None,
        pcp_poolname: Optional[list] = None,
        per_ip_shaper: Optional[str] = None,
        permit_any_host: Optional[str] = None,
        permit_stun_host: Optional[str] = None,
        policy_expiry: Optional[str] = None,
        policy_expiry_date: Optional[str] = None,
        policy_expiry_date_utc: Optional[str] = None,
        policyid: Optional[int] = None,
        poolname: Optional[list] = None,
        poolname6: Optional[list] = None,
        port_preserve: Optional[str] = None,
        port_random: Optional[str] = None,
        profile_group: Optional[str] = None,
        profile_protocol_options: Optional[str] = None,
        profile_type: Optional[str] = None,
        radius_ip_auth_bypass: Optional[str] = None,
        radius_mac_auth_bypass: Optional[str] = None,
        redirect_url: Optional[str] = None,
        replacemsg_override_group: Optional[str] = None,
        reputation_direction: Optional[str] = None,
        reputation_direction6: Optional[str] = None,
        reputation_minimum: Optional[int] = None,
        reputation_minimum6: Optional[int] = None,
        rtp_addr: Optional[list] = None,
        rtp_nat: Optional[str] = None,
        schedule: Optional[str] = None,
        schedule_timeout: Optional[str] = None,
        sctp_filter_profile: Optional[str] = None,
        send_deny_packet: Optional[str] = None,
        service: Optional[list] = None,
        service_negate: Optional[str] = None,
        session_ttl: Optional[str] = None,
        sgt: Optional[list] = None,
        sgt_check: Optional[str] = None,
        src_vendor_mac: Optional[list] = None,
        srcaddr: Optional[list] = None,
        srcaddr_negate: Optional[str] = None,
        srcaddr6: Optional[list] = None,
        srcaddr6_negate: Optional[str] = None,
        srcintf: Optional[list] = None,
        ssh_filter_profile: Optional[str] = None,
        ssh_policy_redirect: Optional[str] = None,
        ssl_ssh_profile: Optional[str] = None,
        status: Optional[str] = None,
        tcp_mss_receiver: Optional[int] = None,
        tcp_mss_sender: Optional[int] = None,
        tcp_session_without_syn: Optional[str] = None,
        timeout_send_rst: Optional[str] = None,
        tos: Optional[str] = None,
        tos_mask: Optional[str] = None,
        tos_negate: Optional[str] = None,
        traffic_shaper: Optional[str] = None,
        traffic_shaper_reverse: Optional[str] = None,
        users: Optional[list] = None,
        utm_status: Optional[str] = None,
        uuid: Optional[str] = None,
        videofilter_profile: Optional[str] = None,
        virtual_patch_profile: Optional[str] = None,
        vlan_cos_fwd: Optional[int] = None,
        vlan_cos_rev: Optional[int] = None,
        vlan_filter: Optional[str] = None,
        voip_profile: Optional[str] = None,
        vpntunnel: Optional[str] = None,
        waf_profile: Optional[str] = None,
        wccp: Optional[str] = None,
        webfilter_profile: Optional[str] = None,
        webproxy_forward_server: Optional[str] = None,
        webproxy_profile: Optional[str] = None,
        ztna_device_ownership: Optional[str] = None,
        ztna_ems_tag: Optional[list] = None,
        ztna_ems_tag_negate: Optional[str] = None,
        ztna_ems_tag_secondary: Optional[list] = None,
        ztna_geo_tag: Optional[list] = None,
        ztna_policy_redirect: Optional[str] = None,
        ztna_status: Optional[str] = None,
        ztna_tags_match_logic: Optional[str] = None,
        raw_json: bool = False,
        **kwargs,
    ) -> Dict[str, Any]:
        """
        Create a new policy entry.

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

            action (string) (enum: ['accept', 'deny', 'ipsec']):
                Policy action (accept/deny/ipsec).
            anti-replay (string) (enum: ['enable', 'disable']):
                Enable/disable anti-replay check.
            app-monitor (string) (enum: ['enable', 'disable']):
                Enable/disable application TCP metrics in session logs.When ...
            application-list (string) (max_len: 47):
                Name of an existing Application list.
            auth-cert (string) (max_len: 35):
                HTTPS server certificate for policy authentication.
            auth-path (string) (enum: ['enable', 'disable']):
                Enable/disable authentication-based routing.
            auth-redirect-addr (string) (max_len: 63):
                HTTP-to-HTTPS redirect address for firewall authentication.
            auto-asic-offload (string) (enum: ['enable', 'disable']):
                Enable/disable policy traffic ASIC offloading.
            av-profile (string) (max_len: 47):
                Name of an existing Antivirus profile.
            block-notification (string) (enum: ['enable', 'disable']):
                Enable/disable block notification.
            captive-portal-exempt (string) (enum: ['enable', 'disable']):
                Enable to exempt some users from the captive portal.
            capture-packet (string) (enum: ['enable', 'disable']):
                Enable/disable capture packets.
            casb-profile (string) (max_len: 47):
                Name of an existing CASB profile.
            comments (string) (max_len: 1023):
                Comment.
            custom-log-fields (list[object]):
                Custom fields to append to log messages for this policy.
            decrypted-traffic-mirror (string) (max_len: 35):
                Decrypted traffic mirror.
            delay-tcp-npu-session (string) (enum: ['enable', 'disable']):
                Enable TCP NPU session delay to guarantee packet order of 3-...
            diameter-filter-profile (string) (max_len: 47):
                Name of an existing Diameter filter profile.
            diffserv-copy (string) (enum: ['enable', 'disable']):
                Enable to copy packet's DiffServ values from session's origi...
            diffserv-forward (string) (enum: ['enable', 'disable']):
                Enable to change packet's DiffServ values to the specified d...
            diffserv-reverse (string) (enum: ['enable', 'disable']):
                Enable to change packet's reverse (reply) DiffServ values to...
            diffservcode-forward (string):
                Change packet's DiffServ to this value.
            diffservcode-rev (string):
                Change packet's reverse (reply) DiffServ to this value.
            disclaimer (string) (enum: ['enable', 'disable']):
                Enable/disable user authentication disclaimer.
            dlp-profile (string) (max_len: 47):
                Name of an existing DLP profile.
            dnsfilter-profile (string) (max_len: 47):
                Name of an existing DNS filter profile.
            dsri (string) (enum: ['enable', 'disable']):
                Enable DSRI to ignore HTTP server responses.
            dstaddr (list[object]):
                Destination IPv4 address and address group names.
            dstaddr-negate (string) (enum: ['enable', 'disable']):
                When enabled dstaddr specifies what the destination address ...
            dstaddr6 (list[object]):
                Destination IPv6 address name and address group names.
            dstaddr6-negate (string) (enum: ['enable', 'disable']):
                When enabled dstaddr6 specifies what the destination address...
            dstintf (list[object]):
                Outgoing (egress) interface.
            dynamic-shaping (string) (enum: ['enable', 'disable']):
                Enable/disable dynamic RADIUS defined traffic shaping.
            email-collect (string) (enum: ['enable', 'disable']):
                Enable/disable email collection.
            emailfilter-profile (string) (max_len: 47):
                Name of an existing email filter profile.
            fec (string) (enum: ['enable', 'disable']):
                Enable/disable Forward Error Correction on traffic matching ...
            file-filter-profile (string) (max_len: 47):
                Name of an existing file-filter profile.
            firewall-session-dirty (string) (enum: ['check-all', 'check-new']):
                How to handle sessions if the configuration of this firewall...
            fixedport (string) (enum: ['enable', 'disable']):
                Enable to prevent source NAT from changing a session's sourc...
            fsso-agent-for-ntlm (string) (max_len: 35):
                FSSO agent to use for NTLM authentication.
            fsso-groups (list[object]):
                Names of FSSO groups.
            geoip-anycast (string) (enum: ['enable', 'disable']):
                Enable/disable recognition of anycast IP addresses using the...
            geoip-match (string) (enum: ['physical-location', 'registered-location']):
                Match geography address based either on its physical locatio...
            groups (list[object]):
                Names of user groups that can authenticate with this policy.
            http-policy-redirect (string) (enum: ['enable', 'disable', 'legacy']):
                Redirect HTTP(S) traffic to matching transparent web proxy p...
            icap-profile (string) (max_len: 47):
                Name of an existing ICAP profile.
            identity-based-route (string) (max_len: 35):
                Name of identity-based routing rule.
            inbound (string) (enum: ['enable', 'disable']):
                Policy-based IPsec VPN: only traffic from the remote network...
            inspection-mode (string) (enum: ['proxy', 'flow']):
                Policy inspection mode (Flow/proxy). Default is Flow mode.
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
                When enabled internet-service specifies what the service mus...
            internet-service-src (string) (enum: ['enable', 'disable']):
                Enable/disable use of Internet Services in source for this p...
            internet-service-src-custom (list[object]):
                Custom Internet Service source name.
            internet-service-src-custom-group (list[object]):
                Custom Internet Service source group name.
            internet-service-src-fortiguard (list[object]):
                FortiGuard Internet Service source name.
            internet-service-src-group (list[object]):
                Internet Service source group name.
            internet-service-src-name (list[object]):
                Internet Service source name.
            internet-service-src-negate (string) (enum: ['enable', 'disable']):
                When enabled internet-service-src specifies what the service...
            internet-service6 (string) (enum: ['enable', 'disable']):
                Enable/disable use of IPv6 Internet Services for this policy...
            internet-service6-custom (list[object]):
                Custom IPv6 Internet Service name.
            internet-service6-custom-group (list[object]):
                Custom Internet Service6 group name.
            internet-service6-fortiguard (list[object]):
                FortiGuard IPv6 Internet Service name.
            internet-service6-group (list[object]):
                Internet Service group name.
            internet-service6-name (list[object]):
                IPv6 Internet Service name.
            internet-service6-negate (string) (enum: ['enable', 'disable']):
                When enabled internet-service6 specifies what the service mu...
            internet-service6-src (string) (enum: ['enable', 'disable']):
                Enable/disable use of IPv6 Internet Services in source for t...
            internet-service6-src-custom (list[object]):
                Custom IPv6 Internet Service source name.
            internet-service6-src-custom-group (list[object]):
                Custom Internet Service6 source group name.
            internet-service6-src-fortiguard (list[object]):
                FortiGuard IPv6 Internet Service source name.
            internet-service6-src-group (list[object]):
                Internet Service6 source group name.
            internet-service6-src-name (list[object]):
                IPv6 Internet Service source name.
            internet-service6-src-negate (string) (enum: ['enable', 'disable']):
                When enabled internet-service6-src specifies what the servic...
            ippool (string) (enum: ['enable', 'disable']):
                Enable to use IP Pools for source NAT.
            ips-sensor (string) (max_len: 47):
                Name of an existing IPS sensor.
            ips-voip-filter (string) (max_len: 47):
                Name of an existing VoIP (ips) profile.
            log-http-transaction (string) (enum: ['enable', 'disable']):
                Enable/disable HTTP transaction log.
            logtraffic (string) (enum: ['all', 'utm', 'disable']):
                Enable or disable logging. Log all sessions or security prof...
            logtraffic-start (string) (enum: ['enable', 'disable']):
                Record logs when a session starts.
            match-vip (string) (enum: ['enable', 'disable']):
                Enable to match packets that have had their destination addr...
            match-vip-only (string) (enum: ['enable', 'disable']):
                Enable/disable matching of only those packets that have had ...
            name (string) (max_len: 35):
                Policy name.
            nat (string) (enum: ['enable', 'disable']):
                Enable/disable source NAT.
            nat46 (string) (enum: ['enable', 'disable']):
                Enable/disable NAT46.
            nat64 (string) (enum: ['enable', 'disable']):
                Enable/disable NAT64.
            natinbound (string) (enum: ['enable', 'disable']):
                Policy-based IPsec VPN: apply destination NAT to inbound tra...
            natip (string):
                Policy-based IPsec VPN: source NAT IP address for outgoing t...
            natoutbound (string) (enum: ['enable', 'disable']):
                Policy-based IPsec VPN: apply source NAT to outbound traffic...
            network-service-dynamic (list[object]):
                Dynamic Network Service name.
            network-service-src-dynamic (list[object]):
                Dynamic Network Service source name.
            np-acceleration (string) (enum: ['enable', 'disable']):
                Enable/disable UTM Network Processor acceleration.
            ntlm (string) (enum: ['enable', 'disable']):
                Enable/disable NTLM authentication.
            ntlm-enabled-browsers (list[object]):
                HTTP-User-Agent value of supported browsers.
            ntlm-guest (string) (enum: ['enable', 'disable']):
                Enable/disable NTLM guest user access.
            outbound (string) (enum: ['enable', 'disable']):
                Policy-based IPsec VPN: only traffic from the internal netwo...
            passive-wan-health-measurement (string) (enum: ['enable', 'disable']):
                Enable/disable passive WAN health measurement. When enabled,...
            pcp-inbound (string) (enum: ['enable', 'disable']):
                Enable/disable PCP inbound DNAT.
            pcp-outbound (string) (enum: ['enable', 'disable']):
                Enable/disable PCP outbound SNAT.
            pcp-poolname (list[object]):
                PCP pool names.
            per-ip-shaper (string) (max_len: 35):
                Per-IP traffic shaper.
            permit-any-host (string) (enum: ['enable', 'disable']):
                Enable/disable fullcone NAT. Accept UDP packets from any hos...
            permit-stun-host (string) (enum: ['enable', 'disable']):
                Accept UDP packets from any Session Traversal Utilities for ...
            policy-expiry (string) (enum: ['enable', 'disable']):
                Enable/disable policy expiry.
            policy-expiry-date (string):
                Policy expiry date (YYYY-MM-DD HH:MM:SS).
            policy-expiry-date-utc (string):
                Policy expiry date and time, in epoch format.
            policyid (integer) (range: 0-4294967294):
                Policy ID (0 - 4294967294).
            poolname (list[object]):
                IP Pool names.
            poolname6 (list[object]):
                IPv6 pool names.
            port-preserve (string) (enum: ['enable', 'disable']):
                Enable/disable preservation of the original source port from...
            port-random (string) (enum: ['enable', 'disable']):
                Enable/disable random source port selection for source NAT.
            profile-group (string) (max_len: 47):
                Name of profile group.
            profile-protocol-options (string) (max_len: 47):
                Name of an existing Protocol options profile.
            profile-type (string) (enum: ['single', 'group']):
                Determine whether the firewall policy allows security profil...
            radius-ip-auth-bypass (string) (enum: ['enable', 'disable']):
                Enable IP authentication bypass. The bypassed IP address mus...
            radius-mac-auth-bypass (string) (enum: ['enable', 'disable']):
                Enable MAC authentication bypass. The bypassed MAC address m...
            redirect-url (string) (max_len: 1023):
                URL users are directed to after seeing and accepting the dis...
            replacemsg-override-group (string) (max_len: 35):
                Override the default replacement message group for this poli...
            reputation-direction (string) (enum: ['source', 'destination']):
                Direction of the initial traffic for reputation to take effe...
            reputation-direction6 (string) (enum: ['source', 'destination']):
                Direction of the initial traffic for IPv6 reputation to take...
            reputation-minimum (integer) (range: 0-4294967295):
                Minimum Reputation to take action.
            reputation-minimum6 (integer) (range: 0-4294967295):
                IPv6 Minimum Reputation to take action.
            rtp-addr (list[object]):
                Address names if this is an RTP NAT policy.
            rtp-nat (string) (enum: ['disable', 'enable']):
                Enable Real Time Protocol (RTP) NAT.
            schedule (string) (max_len: 35):
                Schedule name.
            schedule-timeout (string) (enum: ['enable', 'disable']):
                Enable to force current sessions to end when the schedule ob...
            sctp-filter-profile (string) (max_len: 47):
                Name of an existing SCTP filter profile.
            send-deny-packet (string) (enum: ['disable', 'enable']):
                Enable to send a reply when a session is denied or blocked b...
            service (list[object]):
                Service and service group names.
            service-negate (string) (enum: ['enable', 'disable']):
                When enabled service specifies what the service must NOT be.
            session-ttl (string):
                TTL in seconds for sessions accepted by this policy (0 means...
            sgt (list[object]):
                Security group tags.
            sgt-check (string) (enum: ['enable', 'disable']):
                Enable/disable security group tags (SGT) check.
            src-vendor-mac (list[object]):
                Vendor MAC source ID.
            srcaddr (list[object]):
                Source IPv4 address and address group names.
            srcaddr-negate (string) (enum: ['enable', 'disable']):
                When enabled srcaddr specifies what the source address must ...
            srcaddr6 (list[object]):
                Source IPv6 address name and address group names.
            srcaddr6-negate (string) (enum: ['enable', 'disable']):
                When enabled srcaddr6 specifies what the source address must...
            srcintf (list[object]):
                Incoming (ingress) interface.
            ssh-filter-profile (string) (max_len: 47):
                Name of an existing SSH filter profile.
            ssh-policy-redirect (string) (enum: ['enable', 'disable']):
                Redirect SSH traffic to matching transparent proxy policy.
            ssl-ssh-profile (string) (max_len: 47):
                Name of an existing SSL SSH profile.
            status (string) (enum: ['enable', 'disable']):
                Enable or disable this policy.
            tcp-mss-receiver (integer) (range: 0-65535):
                Receiver TCP maximum segment size (MSS).
            tcp-mss-sender (integer) (range: 0-65535):
                Sender TCP maximum segment size (MSS).
            tcp-session-without-syn (string) (enum: ['all', 'data-only', 'disable']):
                Enable/disable creation of TCP session without SYN flag.
            timeout-send-rst (string) (enum: ['enable', 'disable']):
                Enable/disable sending RST packets when TCP sessions expire.
            tos (string):
                ToS (Type of Service) value used for comparison.
            tos-mask (string):
                Non-zero bit positions are used for comparison while zero bi...
            tos-negate (string) (enum: ['enable', 'disable']):
                Enable negated TOS match.
            traffic-shaper (string) (max_len: 35):
                Traffic shaper.
            traffic-shaper-reverse (string) (max_len: 35):
                Reverse traffic shaper.
            users (list[object]):
                Names of individual users that can authenticate with this po...
            utm-status (string) (enum: ['enable', 'disable']):
                Enable to add one or more security profiles (AV, IPS, etc.) ...
            uuid (string):
                Universally Unique Identifier (UUID; automatically assigned ...
            videofilter-profile (string) (max_len: 47):
                Name of an existing VideoFilter profile.
            virtual-patch-profile (string) (max_len: 47):
                Name of an existing virtual-patch profile.
            vlan-cos-fwd (integer) (range: 0-7):
                VLAN forward direction user priority: 255 passthrough, 0 low...
            vlan-cos-rev (integer) (range: 0-7):
                VLAN reverse direction user priority: 255 passthrough, 0 low...
            vlan-filter (string):
                VLAN ranges to allow
            voip-profile (string) (max_len: 47):
                Name of an existing VoIP (voipd) profile.
            vpntunnel (string) (max_len: 35):
                Policy-based IPsec VPN: name of the IPsec VPN Phase 1.
            waf-profile (string) (max_len: 47):
                Name of an existing Web application firewall profile.
            wccp (string) (enum: ['enable', 'disable']):
                Enable/disable forwarding traffic matching this policy to a ...
            webfilter-profile (string) (max_len: 47):
                Name of an existing Web filter profile.
            webproxy-forward-server (string) (max_len: 63):
                Webproxy forward server name.
            webproxy-profile (string) (max_len: 63):
                Webproxy profile name.
            ztna-device-ownership (string) (enum: ['enable', 'disable']):
                Enable/disable zero trust device ownership.
            ztna-ems-tag (list[object]):
                Source ztna-ems-tag names.
            ztna-ems-tag-negate (string) (enum: ['enable', 'disable']):
                When enabled ztna-ems-tag specifies what the tags must NOT b...
            ztna-ems-tag-secondary (list[object]):
                Source ztna-ems-tag-secondary names.
            ztna-geo-tag (list[object]):
                Source ztna-geo-tag names.
            ztna-policy-redirect (string) (enum: ['enable', 'disable']):
                Redirect ZTNA traffic to matching Access-Proxy proxy-policy.
            ztna-status (string) (enum: ['enable', 'disable']):
                Enable/disable zero trust access.
            ztna-tags-match-logic (string) (enum: ['or', 'and']):
                ZTNA tag matching logic.

        Returns:
            API response dictionary
        """
        # Build data from kwargs if not provided
        if payload_dict is None:
            payload_dict = {}
        if action is not None:
            payload_dict["action"] = action
        if anti_replay is not None:
            payload_dict["anti-replay"] = anti_replay
        if app_monitor is not None:
            payload_dict["app-monitor"] = app_monitor
        if application_list is not None:
            payload_dict["application-list"] = application_list
        if auth_cert is not None:
            payload_dict["auth-cert"] = auth_cert
        if auth_path is not None:
            payload_dict["auth-path"] = auth_path
        if auth_redirect_addr is not None:
            payload_dict["auth-redirect-addr"] = auth_redirect_addr
        if auto_asic_offload is not None:
            payload_dict["auto-asic-offload"] = auto_asic_offload
        if av_profile is not None:
            payload_dict["av-profile"] = av_profile
        if block_notification is not None:
            payload_dict["block-notification"] = block_notification
        if captive_portal_exempt is not None:
            payload_dict["captive-portal-exempt"] = captive_portal_exempt
        if capture_packet is not None:
            payload_dict["capture-packet"] = capture_packet
        if casb_profile is not None:
            payload_dict["casb-profile"] = casb_profile
        if comments is not None:
            payload_dict["comments"] = comments
        if custom_log_fields is not None:
            payload_dict["custom-log-fields"] = custom_log_fields
        if decrypted_traffic_mirror is not None:
            payload_dict["decrypted-traffic-mirror"] = decrypted_traffic_mirror
        if delay_tcp_npu_session is not None:
            payload_dict["delay-tcp-npu-session"] = delay_tcp_npu_session
        if diameter_filter_profile is not None:
            payload_dict["diameter-filter-profile"] = diameter_filter_profile
        if diffserv_copy is not None:
            payload_dict["diffserv-copy"] = diffserv_copy
        if diffserv_forward is not None:
            payload_dict["diffserv-forward"] = diffserv_forward
        if diffserv_reverse is not None:
            payload_dict["diffserv-reverse"] = diffserv_reverse
        if diffservcode_forward is not None:
            payload_dict["diffservcode-forward"] = diffservcode_forward
        if diffservcode_rev is not None:
            payload_dict["diffservcode-rev"] = diffservcode_rev
        if disclaimer is not None:
            payload_dict["disclaimer"] = disclaimer
        if dlp_profile is not None:
            payload_dict["dlp-profile"] = dlp_profile
        if dnsfilter_profile is not None:
            payload_dict["dnsfilter-profile"] = dnsfilter_profile
        if dsri is not None:
            payload_dict["dsri"] = dsri
        if dstaddr is not None:
            payload_dict["dstaddr"] = dstaddr
        if dstaddr_negate is not None:
            payload_dict["dstaddr-negate"] = dstaddr_negate
        if dstaddr6 is not None:
            payload_dict["dstaddr6"] = dstaddr6
        if dstaddr6_negate is not None:
            payload_dict["dstaddr6-negate"] = dstaddr6_negate
        if dstintf is not None:
            payload_dict["dstintf"] = dstintf
        if dynamic_shaping is not None:
            payload_dict["dynamic-shaping"] = dynamic_shaping
        if email_collect is not None:
            payload_dict["email-collect"] = email_collect
        if emailfilter_profile is not None:
            payload_dict["emailfilter-profile"] = emailfilter_profile
        if fec is not None:
            payload_dict["fec"] = fec
        if file_filter_profile is not None:
            payload_dict["file-filter-profile"] = file_filter_profile
        if firewall_session_dirty is not None:
            payload_dict["firewall-session-dirty"] = firewall_session_dirty
        if fixedport is not None:
            payload_dict["fixedport"] = fixedport
        if fsso_agent_for_ntlm is not None:
            payload_dict["fsso-agent-for-ntlm"] = fsso_agent_for_ntlm
        if fsso_groups is not None:
            payload_dict["fsso-groups"] = fsso_groups
        if geoip_anycast is not None:
            payload_dict["geoip-anycast"] = geoip_anycast
        if geoip_match is not None:
            payload_dict["geoip-match"] = geoip_match
        if groups is not None:
            payload_dict["groups"] = groups
        if http_policy_redirect is not None:
            payload_dict["http-policy-redirect"] = http_policy_redirect
        if icap_profile is not None:
            payload_dict["icap-profile"] = icap_profile
        if identity_based_route is not None:
            payload_dict["identity-based-route"] = identity_based_route
        if inbound is not None:
            payload_dict["inbound"] = inbound
        if inspection_mode is not None:
            payload_dict["inspection-mode"] = inspection_mode
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
        if internet_service_src is not None:
            payload_dict["internet-service-src"] = internet_service_src
        if internet_service_src_custom is not None:
            payload_dict["internet-service-src-custom"] = internet_service_src_custom
        if internet_service_src_custom_group is not None:
            payload_dict["internet-service-src-custom-group"] = internet_service_src_custom_group
        if internet_service_src_fortiguard is not None:
            payload_dict["internet-service-src-fortiguard"] = internet_service_src_fortiguard
        if internet_service_src_group is not None:
            payload_dict["internet-service-src-group"] = internet_service_src_group
        if internet_service_src_name is not None:
            payload_dict["internet-service-src-name"] = internet_service_src_name
        if internet_service_src_negate is not None:
            payload_dict["internet-service-src-negate"] = internet_service_src_negate
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
        if internet_service6_src is not None:
            payload_dict["internet-service6-src"] = internet_service6_src
        if internet_service6_src_custom is not None:
            payload_dict["internet-service6-src-custom"] = internet_service6_src_custom
        if internet_service6_src_custom_group is not None:
            payload_dict["internet-service6-src-custom-group"] = internet_service6_src_custom_group
        if internet_service6_src_fortiguard is not None:
            payload_dict["internet-service6-src-fortiguard"] = internet_service6_src_fortiguard
        if internet_service6_src_group is not None:
            payload_dict["internet-service6-src-group"] = internet_service6_src_group
        if internet_service6_src_name is not None:
            payload_dict["internet-service6-src-name"] = internet_service6_src_name
        if internet_service6_src_negate is not None:
            payload_dict["internet-service6-src-negate"] = internet_service6_src_negate
        if ippool is not None:
            payload_dict["ippool"] = ippool
        if ips_sensor is not None:
            payload_dict["ips-sensor"] = ips_sensor
        if ips_voip_filter is not None:
            payload_dict["ips-voip-filter"] = ips_voip_filter
        if log_http_transaction is not None:
            payload_dict["log-http-transaction"] = log_http_transaction
        if logtraffic is not None:
            payload_dict["logtraffic"] = logtraffic
        if logtraffic_start is not None:
            payload_dict["logtraffic-start"] = logtraffic_start
        if match_vip is not None:
            payload_dict["match-vip"] = match_vip
        if match_vip_only is not None:
            payload_dict["match-vip-only"] = match_vip_only
        if name is not None:
            payload_dict["name"] = name
        if nat is not None:
            payload_dict["nat"] = nat
        if nat46 is not None:
            payload_dict["nat46"] = nat46
        if nat64 is not None:
            payload_dict["nat64"] = nat64
        if natinbound is not None:
            payload_dict["natinbound"] = natinbound
        if natip is not None:
            payload_dict["natip"] = natip
        if natoutbound is not None:
            payload_dict["natoutbound"] = natoutbound
        if network_service_dynamic is not None:
            payload_dict["network-service-dynamic"] = network_service_dynamic
        if network_service_src_dynamic is not None:
            payload_dict["network-service-src-dynamic"] = network_service_src_dynamic
        if np_acceleration is not None:
            payload_dict["np-acceleration"] = np_acceleration
        if ntlm is not None:
            payload_dict["ntlm"] = ntlm
        if ntlm_enabled_browsers is not None:
            payload_dict["ntlm-enabled-browsers"] = ntlm_enabled_browsers
        if ntlm_guest is not None:
            payload_dict["ntlm-guest"] = ntlm_guest
        if outbound is not None:
            payload_dict["outbound"] = outbound
        if passive_wan_health_measurement is not None:
            payload_dict["passive-wan-health-measurement"] = passive_wan_health_measurement
        if pcp_inbound is not None:
            payload_dict["pcp-inbound"] = pcp_inbound
        if pcp_outbound is not None:
            payload_dict["pcp-outbound"] = pcp_outbound
        if pcp_poolname is not None:
            payload_dict["pcp-poolname"] = pcp_poolname
        if per_ip_shaper is not None:
            payload_dict["per-ip-shaper"] = per_ip_shaper
        if permit_any_host is not None:
            payload_dict["permit-any-host"] = permit_any_host
        if permit_stun_host is not None:
            payload_dict["permit-stun-host"] = permit_stun_host
        if policy_expiry is not None:
            payload_dict["policy-expiry"] = policy_expiry
        if policy_expiry_date is not None:
            payload_dict["policy-expiry-date"] = policy_expiry_date
        if policy_expiry_date_utc is not None:
            payload_dict["policy-expiry-date-utc"] = policy_expiry_date_utc
        if policyid is not None:
            payload_dict["policyid"] = policyid
        if poolname is not None:
            payload_dict["poolname"] = poolname
        if poolname6 is not None:
            payload_dict["poolname6"] = poolname6
        if port_preserve is not None:
            payload_dict["port-preserve"] = port_preserve
        if port_random is not None:
            payload_dict["port-random"] = port_random
        if profile_group is not None:
            payload_dict["profile-group"] = profile_group
        if profile_protocol_options is not None:
            payload_dict["profile-protocol-options"] = profile_protocol_options
        if profile_type is not None:
            payload_dict["profile-type"] = profile_type
        if radius_ip_auth_bypass is not None:
            payload_dict["radius-ip-auth-bypass"] = radius_ip_auth_bypass
        if radius_mac_auth_bypass is not None:
            payload_dict["radius-mac-auth-bypass"] = radius_mac_auth_bypass
        if redirect_url is not None:
            payload_dict["redirect-url"] = redirect_url
        if replacemsg_override_group is not None:
            payload_dict["replacemsg-override-group"] = replacemsg_override_group
        if reputation_direction is not None:
            payload_dict["reputation-direction"] = reputation_direction
        if reputation_direction6 is not None:
            payload_dict["reputation-direction6"] = reputation_direction6
        if reputation_minimum is not None:
            payload_dict["reputation-minimum"] = reputation_minimum
        if reputation_minimum6 is not None:
            payload_dict["reputation-minimum6"] = reputation_minimum6
        if rtp_addr is not None:
            payload_dict["rtp-addr"] = rtp_addr
        if rtp_nat is not None:
            payload_dict["rtp-nat"] = rtp_nat
        if schedule is not None:
            payload_dict["schedule"] = schedule
        if schedule_timeout is not None:
            payload_dict["schedule-timeout"] = schedule_timeout
        if sctp_filter_profile is not None:
            payload_dict["sctp-filter-profile"] = sctp_filter_profile
        if send_deny_packet is not None:
            payload_dict["send-deny-packet"] = send_deny_packet
        if service is not None:
            payload_dict["service"] = service
        if service_negate is not None:
            payload_dict["service-negate"] = service_negate
        if session_ttl is not None:
            payload_dict["session-ttl"] = session_ttl
        if sgt is not None:
            payload_dict["sgt"] = sgt
        if sgt_check is not None:
            payload_dict["sgt-check"] = sgt_check
        if src_vendor_mac is not None:
            payload_dict["src-vendor-mac"] = src_vendor_mac
        if srcaddr is not None:
            payload_dict["srcaddr"] = srcaddr
        if srcaddr_negate is not None:
            payload_dict["srcaddr-negate"] = srcaddr_negate
        if srcaddr6 is not None:
            payload_dict["srcaddr6"] = srcaddr6
        if srcaddr6_negate is not None:
            payload_dict["srcaddr6-negate"] = srcaddr6_negate
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
        if tcp_mss_receiver is not None:
            payload_dict["tcp-mss-receiver"] = tcp_mss_receiver
        if tcp_mss_sender is not None:
            payload_dict["tcp-mss-sender"] = tcp_mss_sender
        if tcp_session_without_syn is not None:
            payload_dict["tcp-session-without-syn"] = tcp_session_without_syn
        if timeout_send_rst is not None:
            payload_dict["timeout-send-rst"] = timeout_send_rst
        if tos is not None:
            payload_dict["tos"] = tos
        if tos_mask is not None:
            payload_dict["tos-mask"] = tos_mask
        if tos_negate is not None:
            payload_dict["tos-negate"] = tos_negate
        if traffic_shaper is not None:
            payload_dict["traffic-shaper"] = traffic_shaper
        if traffic_shaper_reverse is not None:
            payload_dict["traffic-shaper-reverse"] = traffic_shaper_reverse
        if users is not None:
            payload_dict["users"] = users
        if utm_status is not None:
            payload_dict["utm-status"] = utm_status
        if uuid is not None:
            payload_dict["uuid"] = uuid
        if videofilter_profile is not None:
            payload_dict["videofilter-profile"] = videofilter_profile
        if virtual_patch_profile is not None:
            payload_dict["virtual-patch-profile"] = virtual_patch_profile
        if vlan_cos_fwd is not None:
            payload_dict["vlan-cos-fwd"] = vlan_cos_fwd
        if vlan_cos_rev is not None:
            payload_dict["vlan-cos-rev"] = vlan_cos_rev
        if vlan_filter is not None:
            payload_dict["vlan-filter"] = vlan_filter
        if voip_profile is not None:
            payload_dict["voip-profile"] = voip_profile
        if vpntunnel is not None:
            payload_dict["vpntunnel"] = vpntunnel
        if waf_profile is not None:
            payload_dict["waf-profile"] = waf_profile
        if wccp is not None:
            payload_dict["wccp"] = wccp
        if webfilter_profile is not None:
            payload_dict["webfilter-profile"] = webfilter_profile
        if webproxy_forward_server is not None:
            payload_dict["webproxy-forward-server"] = webproxy_forward_server
        if webproxy_profile is not None:
            payload_dict["webproxy-profile"] = webproxy_profile
        if ztna_device_ownership is not None:
            payload_dict["ztna-device-ownership"] = ztna_device_ownership
        if ztna_ems_tag is not None:
            payload_dict["ztna-ems-tag"] = ztna_ems_tag
        if ztna_ems_tag_negate is not None:
            payload_dict["ztna-ems-tag-negate"] = ztna_ems_tag_negate
        if ztna_ems_tag_secondary is not None:
            payload_dict["ztna-ems-tag-secondary"] = ztna_ems_tag_secondary
        if ztna_geo_tag is not None:
            payload_dict["ztna-geo-tag"] = ztna_geo_tag
        if ztna_policy_redirect is not None:
            payload_dict["ztna-policy-redirect"] = ztna_policy_redirect
        if ztna_status is not None:
            payload_dict["ztna-status"] = ztna_status
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
        anti_replay: Optional[str] = None,
        app_monitor: Optional[str] = None,
        application_list: Optional[str] = None,
        auth_cert: Optional[str] = None,
        auth_path: Optional[str] = None,
        auth_redirect_addr: Optional[str] = None,
        auto_asic_offload: Optional[str] = None,
        av_profile: Optional[str] = None,
        block_notification: Optional[str] = None,
        captive_portal_exempt: Optional[str] = None,
        capture_packet: Optional[str] = None,
        casb_profile: Optional[str] = None,
        comments: Optional[str] = None,
        custom_log_fields: Optional[list] = None,
        decrypted_traffic_mirror: Optional[str] = None,
        delay_tcp_npu_session: Optional[str] = None,
        diameter_filter_profile: Optional[str] = None,
        diffserv_copy: Optional[str] = None,
        diffserv_forward: Optional[str] = None,
        diffserv_reverse: Optional[str] = None,
        diffservcode_forward: Optional[str] = None,
        diffservcode_rev: Optional[str] = None,
        disclaimer: Optional[str] = None,
        dlp_profile: Optional[str] = None,
        dnsfilter_profile: Optional[str] = None,
        dsri: Optional[str] = None,
        dstaddr: Optional[list] = None,
        dstaddr_negate: Optional[str] = None,
        dstaddr6: Optional[list] = None,
        dstaddr6_negate: Optional[str] = None,
        dstintf: Optional[list] = None,
        dynamic_shaping: Optional[str] = None,
        email_collect: Optional[str] = None,
        emailfilter_profile: Optional[str] = None,
        fec: Optional[str] = None,
        file_filter_profile: Optional[str] = None,
        firewall_session_dirty: Optional[str] = None,
        fixedport: Optional[str] = None,
        fsso_agent_for_ntlm: Optional[str] = None,
        fsso_groups: Optional[list] = None,
        geoip_anycast: Optional[str] = None,
        geoip_match: Optional[str] = None,
        groups: Optional[list] = None,
        http_policy_redirect: Optional[str] = None,
        icap_profile: Optional[str] = None,
        identity_based_route: Optional[str] = None,
        inbound: Optional[str] = None,
        inspection_mode: Optional[str] = None,
        internet_service: Optional[str] = None,
        internet_service_custom: Optional[list] = None,
        internet_service_custom_group: Optional[list] = None,
        internet_service_fortiguard: Optional[list] = None,
        internet_service_group: Optional[list] = None,
        internet_service_name: Optional[list] = None,
        internet_service_negate: Optional[str] = None,
        internet_service_src: Optional[str] = None,
        internet_service_src_custom: Optional[list] = None,
        internet_service_src_custom_group: Optional[list] = None,
        internet_service_src_fortiguard: Optional[list] = None,
        internet_service_src_group: Optional[list] = None,
        internet_service_src_name: Optional[list] = None,
        internet_service_src_negate: Optional[str] = None,
        internet_service6: Optional[str] = None,
        internet_service6_custom: Optional[list] = None,
        internet_service6_custom_group: Optional[list] = None,
        internet_service6_fortiguard: Optional[list] = None,
        internet_service6_group: Optional[list] = None,
        internet_service6_name: Optional[list] = None,
        internet_service6_negate: Optional[str] = None,
        internet_service6_src: Optional[str] = None,
        internet_service6_src_custom: Optional[list] = None,
        internet_service6_src_custom_group: Optional[list] = None,
        internet_service6_src_fortiguard: Optional[list] = None,
        internet_service6_src_group: Optional[list] = None,
        internet_service6_src_name: Optional[list] = None,
        internet_service6_src_negate: Optional[str] = None,
        ippool: Optional[str] = None,
        ips_sensor: Optional[str] = None,
        ips_voip_filter: Optional[str] = None,
        log_http_transaction: Optional[str] = None,
        logtraffic: Optional[str] = None,
        logtraffic_start: Optional[str] = None,
        match_vip: Optional[str] = None,
        match_vip_only: Optional[str] = None,
        name: Optional[str] = None,
        nat: Optional[str] = None,
        nat46: Optional[str] = None,
        nat64: Optional[str] = None,
        natinbound: Optional[str] = None,
        natip: Optional[str] = None,
        natoutbound: Optional[str] = None,
        network_service_dynamic: Optional[list] = None,
        network_service_src_dynamic: Optional[list] = None,
        np_acceleration: Optional[str] = None,
        ntlm: Optional[str] = None,
        ntlm_enabled_browsers: Optional[list] = None,
        ntlm_guest: Optional[str] = None,
        outbound: Optional[str] = None,
        passive_wan_health_measurement: Optional[str] = None,
        pcp_inbound: Optional[str] = None,
        pcp_outbound: Optional[str] = None,
        pcp_poolname: Optional[list] = None,
        per_ip_shaper: Optional[str] = None,
        permit_any_host: Optional[str] = None,
        permit_stun_host: Optional[str] = None,
        policy_expiry: Optional[str] = None,
        policy_expiry_date: Optional[str] = None,
        policy_expiry_date_utc: Optional[str] = None,
        policyid: Optional[int] = None,
        poolname: Optional[list] = None,
        poolname6: Optional[list] = None,
        port_preserve: Optional[str] = None,
        port_random: Optional[str] = None,
        profile_group: Optional[str] = None,
        profile_protocol_options: Optional[str] = None,
        profile_type: Optional[str] = None,
        radius_ip_auth_bypass: Optional[str] = None,
        radius_mac_auth_bypass: Optional[str] = None,
        redirect_url: Optional[str] = None,
        replacemsg_override_group: Optional[str] = None,
        reputation_direction: Optional[str] = None,
        reputation_direction6: Optional[str] = None,
        reputation_minimum: Optional[int] = None,
        reputation_minimum6: Optional[int] = None,
        rtp_addr: Optional[list] = None,
        rtp_nat: Optional[str] = None,
        schedule: Optional[str] = None,
        schedule_timeout: Optional[str] = None,
        sctp_filter_profile: Optional[str] = None,
        send_deny_packet: Optional[str] = None,
        service: Optional[list] = None,
        service_negate: Optional[str] = None,
        session_ttl: Optional[str] = None,
        sgt: Optional[list] = None,
        sgt_check: Optional[str] = None,
        src_vendor_mac: Optional[list] = None,
        srcaddr: Optional[list] = None,
        srcaddr_negate: Optional[str] = None,
        srcaddr6: Optional[list] = None,
        srcaddr6_negate: Optional[str] = None,
        srcintf: Optional[list] = None,
        ssh_filter_profile: Optional[str] = None,
        ssh_policy_redirect: Optional[str] = None,
        ssl_ssh_profile: Optional[str] = None,
        status: Optional[str] = None,
        tcp_mss_receiver: Optional[int] = None,
        tcp_mss_sender: Optional[int] = None,
        tcp_session_without_syn: Optional[str] = None,
        timeout_send_rst: Optional[str] = None,
        tos: Optional[str] = None,
        tos_mask: Optional[str] = None,
        tos_negate: Optional[str] = None,
        traffic_shaper: Optional[str] = None,
        traffic_shaper_reverse: Optional[str] = None,
        users: Optional[list] = None,
        utm_status: Optional[str] = None,
        uuid: Optional[str] = None,
        videofilter_profile: Optional[str] = None,
        virtual_patch_profile: Optional[str] = None,
        vlan_cos_fwd: Optional[int] = None,
        vlan_cos_rev: Optional[int] = None,
        vlan_filter: Optional[str] = None,
        voip_profile: Optional[str] = None,
        vpntunnel: Optional[str] = None,
        waf_profile: Optional[str] = None,
        wccp: Optional[str] = None,
        webfilter_profile: Optional[str] = None,
        webproxy_forward_server: Optional[str] = None,
        webproxy_profile: Optional[str] = None,
        ztna_device_ownership: Optional[str] = None,
        ztna_ems_tag: Optional[list] = None,
        ztna_ems_tag_negate: Optional[str] = None,
        ztna_ems_tag_secondary: Optional[list] = None,
        ztna_geo_tag: Optional[list] = None,
        ztna_policy_redirect: Optional[str] = None,
        ztna_status: Optional[str] = None,
        ztna_tags_match_logic: Optional[str] = None,
        raw_json: bool = False,
        **kwargs,
    ) -> Dict[str, Any]:
        """
        Update an existing policy entry.

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

            action (string) (enum: ['accept', 'deny', 'ipsec']):
                Policy action (accept/deny/ipsec).
            anti-replay (string) (enum: ['enable', 'disable']):
                Enable/disable anti-replay check.
            app-monitor (string) (enum: ['enable', 'disable']):
                Enable/disable application TCP metrics in session logs.When ...
            application-list (string) (max_len: 47):
                Name of an existing Application list.
            auth-cert (string) (max_len: 35):
                HTTPS server certificate for policy authentication.
            auth-path (string) (enum: ['enable', 'disable']):
                Enable/disable authentication-based routing.
            auth-redirect-addr (string) (max_len: 63):
                HTTP-to-HTTPS redirect address for firewall authentication.
            auto-asic-offload (string) (enum: ['enable', 'disable']):
                Enable/disable policy traffic ASIC offloading.
            av-profile (string) (max_len: 47):
                Name of an existing Antivirus profile.
            block-notification (string) (enum: ['enable', 'disable']):
                Enable/disable block notification.
            captive-portal-exempt (string) (enum: ['enable', 'disable']):
                Enable to exempt some users from the captive portal.
            capture-packet (string) (enum: ['enable', 'disable']):
                Enable/disable capture packets.
            casb-profile (string) (max_len: 47):
                Name of an existing CASB profile.
            comments (string) (max_len: 1023):
                Comment.
            custom-log-fields (list[object]):
                Custom fields to append to log messages for this policy.
            decrypted-traffic-mirror (string) (max_len: 35):
                Decrypted traffic mirror.
            delay-tcp-npu-session (string) (enum: ['enable', 'disable']):
                Enable TCP NPU session delay to guarantee packet order of 3-...
            diameter-filter-profile (string) (max_len: 47):
                Name of an existing Diameter filter profile.
            diffserv-copy (string) (enum: ['enable', 'disable']):
                Enable to copy packet's DiffServ values from session's origi...
            diffserv-forward (string) (enum: ['enable', 'disable']):
                Enable to change packet's DiffServ values to the specified d...
            diffserv-reverse (string) (enum: ['enable', 'disable']):
                Enable to change packet's reverse (reply) DiffServ values to...
            diffservcode-forward (string):
                Change packet's DiffServ to this value.
            diffservcode-rev (string):
                Change packet's reverse (reply) DiffServ to this value.
            disclaimer (string) (enum: ['enable', 'disable']):
                Enable/disable user authentication disclaimer.
            dlp-profile (string) (max_len: 47):
                Name of an existing DLP profile.
            dnsfilter-profile (string) (max_len: 47):
                Name of an existing DNS filter profile.
            dsri (string) (enum: ['enable', 'disable']):
                Enable DSRI to ignore HTTP server responses.
            dstaddr (list[object]):
                Destination IPv4 address and address group names.
            dstaddr-negate (string) (enum: ['enable', 'disable']):
                When enabled dstaddr specifies what the destination address ...
            dstaddr6 (list[object]):
                Destination IPv6 address name and address group names.
            dstaddr6-negate (string) (enum: ['enable', 'disable']):
                When enabled dstaddr6 specifies what the destination address...
            dstintf (list[object]):
                Outgoing (egress) interface.
            dynamic-shaping (string) (enum: ['enable', 'disable']):
                Enable/disable dynamic RADIUS defined traffic shaping.
            email-collect (string) (enum: ['enable', 'disable']):
                Enable/disable email collection.
            emailfilter-profile (string) (max_len: 47):
                Name of an existing email filter profile.
            fec (string) (enum: ['enable', 'disable']):
                Enable/disable Forward Error Correction on traffic matching ...
            file-filter-profile (string) (max_len: 47):
                Name of an existing file-filter profile.
            firewall-session-dirty (string) (enum: ['check-all', 'check-new']):
                How to handle sessions if the configuration of this firewall...
            fixedport (string) (enum: ['enable', 'disable']):
                Enable to prevent source NAT from changing a session's sourc...
            fsso-agent-for-ntlm (string) (max_len: 35):
                FSSO agent to use for NTLM authentication.
            fsso-groups (list[object]):
                Names of FSSO groups.
            geoip-anycast (string) (enum: ['enable', 'disable']):
                Enable/disable recognition of anycast IP addresses using the...
            geoip-match (string) (enum: ['physical-location', 'registered-location']):
                Match geography address based either on its physical locatio...
            groups (list[object]):
                Names of user groups that can authenticate with this policy.
            http-policy-redirect (string) (enum: ['enable', 'disable', 'legacy']):
                Redirect HTTP(S) traffic to matching transparent web proxy p...
            icap-profile (string) (max_len: 47):
                Name of an existing ICAP profile.
            identity-based-route (string) (max_len: 35):
                Name of identity-based routing rule.
            inbound (string) (enum: ['enable', 'disable']):
                Policy-based IPsec VPN: only traffic from the remote network...
            inspection-mode (string) (enum: ['proxy', 'flow']):
                Policy inspection mode (Flow/proxy). Default is Flow mode.
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
                When enabled internet-service specifies what the service mus...
            internet-service-src (string) (enum: ['enable', 'disable']):
                Enable/disable use of Internet Services in source for this p...
            internet-service-src-custom (list[object]):
                Custom Internet Service source name.
            internet-service-src-custom-group (list[object]):
                Custom Internet Service source group name.
            internet-service-src-fortiguard (list[object]):
                FortiGuard Internet Service source name.
            internet-service-src-group (list[object]):
                Internet Service source group name.
            internet-service-src-name (list[object]):
                Internet Service source name.
            internet-service-src-negate (string) (enum: ['enable', 'disable']):
                When enabled internet-service-src specifies what the service...
            internet-service6 (string) (enum: ['enable', 'disable']):
                Enable/disable use of IPv6 Internet Services for this policy...
            internet-service6-custom (list[object]):
                Custom IPv6 Internet Service name.
            internet-service6-custom-group (list[object]):
                Custom Internet Service6 group name.
            internet-service6-fortiguard (list[object]):
                FortiGuard IPv6 Internet Service name.
            internet-service6-group (list[object]):
                Internet Service group name.
            internet-service6-name (list[object]):
                IPv6 Internet Service name.
            internet-service6-negate (string) (enum: ['enable', 'disable']):
                When enabled internet-service6 specifies what the service mu...
            internet-service6-src (string) (enum: ['enable', 'disable']):
                Enable/disable use of IPv6 Internet Services in source for t...
            internet-service6-src-custom (list[object]):
                Custom IPv6 Internet Service source name.
            internet-service6-src-custom-group (list[object]):
                Custom Internet Service6 source group name.
            internet-service6-src-fortiguard (list[object]):
                FortiGuard IPv6 Internet Service source name.
            internet-service6-src-group (list[object]):
                Internet Service6 source group name.
            internet-service6-src-name (list[object]):
                IPv6 Internet Service source name.
            internet-service6-src-negate (string) (enum: ['enable', 'disable']):
                When enabled internet-service6-src specifies what the servic...
            ippool (string) (enum: ['enable', 'disable']):
                Enable to use IP Pools for source NAT.
            ips-sensor (string) (max_len: 47):
                Name of an existing IPS sensor.
            ips-voip-filter (string) (max_len: 47):
                Name of an existing VoIP (ips) profile.
            log-http-transaction (string) (enum: ['enable', 'disable']):
                Enable/disable HTTP transaction log.
            logtraffic (string) (enum: ['all', 'utm', 'disable']):
                Enable or disable logging. Log all sessions or security prof...
            logtraffic-start (string) (enum: ['enable', 'disable']):
                Record logs when a session starts.
            match-vip (string) (enum: ['enable', 'disable']):
                Enable to match packets that have had their destination addr...
            match-vip-only (string) (enum: ['enable', 'disable']):
                Enable/disable matching of only those packets that have had ...
            name (string) (max_len: 35):
                Policy name.
            nat (string) (enum: ['enable', 'disable']):
                Enable/disable source NAT.
            nat46 (string) (enum: ['enable', 'disable']):
                Enable/disable NAT46.
            nat64 (string) (enum: ['enable', 'disable']):
                Enable/disable NAT64.
            natinbound (string) (enum: ['enable', 'disable']):
                Policy-based IPsec VPN: apply destination NAT to inbound tra...
            natip (string):
                Policy-based IPsec VPN: source NAT IP address for outgoing t...
            natoutbound (string) (enum: ['enable', 'disable']):
                Policy-based IPsec VPN: apply source NAT to outbound traffic...
            network-service-dynamic (list[object]):
                Dynamic Network Service name.
            network-service-src-dynamic (list[object]):
                Dynamic Network Service source name.
            np-acceleration (string) (enum: ['enable', 'disable']):
                Enable/disable UTM Network Processor acceleration.
            ntlm (string) (enum: ['enable', 'disable']):
                Enable/disable NTLM authentication.
            ntlm-enabled-browsers (list[object]):
                HTTP-User-Agent value of supported browsers.
            ntlm-guest (string) (enum: ['enable', 'disable']):
                Enable/disable NTLM guest user access.
            outbound (string) (enum: ['enable', 'disable']):
                Policy-based IPsec VPN: only traffic from the internal netwo...
            passive-wan-health-measurement (string) (enum: ['enable', 'disable']):
                Enable/disable passive WAN health measurement. When enabled,...
            pcp-inbound (string) (enum: ['enable', 'disable']):
                Enable/disable PCP inbound DNAT.
            pcp-outbound (string) (enum: ['enable', 'disable']):
                Enable/disable PCP outbound SNAT.
            pcp-poolname (list[object]):
                PCP pool names.
            per-ip-shaper (string) (max_len: 35):
                Per-IP traffic shaper.
            permit-any-host (string) (enum: ['enable', 'disable']):
                Enable/disable fullcone NAT. Accept UDP packets from any hos...
            permit-stun-host (string) (enum: ['enable', 'disable']):
                Accept UDP packets from any Session Traversal Utilities for ...
            policy-expiry (string) (enum: ['enable', 'disable']):
                Enable/disable policy expiry.
            policy-expiry-date (string):
                Policy expiry date (YYYY-MM-DD HH:MM:SS).
            policy-expiry-date-utc (string):
                Policy expiry date and time, in epoch format.
            policyid (integer) (range: 0-4294967294):
                Policy ID (0 - 4294967294).
            poolname (list[object]):
                IP Pool names.
            poolname6 (list[object]):
                IPv6 pool names.
            port-preserve (string) (enum: ['enable', 'disable']):
                Enable/disable preservation of the original source port from...
            port-random (string) (enum: ['enable', 'disable']):
                Enable/disable random source port selection for source NAT.
            profile-group (string) (max_len: 47):
                Name of profile group.
            profile-protocol-options (string) (max_len: 47):
                Name of an existing Protocol options profile.
            profile-type (string) (enum: ['single', 'group']):
                Determine whether the firewall policy allows security profil...
            radius-ip-auth-bypass (string) (enum: ['enable', 'disable']):
                Enable IP authentication bypass. The bypassed IP address mus...
            radius-mac-auth-bypass (string) (enum: ['enable', 'disable']):
                Enable MAC authentication bypass. The bypassed MAC address m...
            redirect-url (string) (max_len: 1023):
                URL users are directed to after seeing and accepting the dis...
            replacemsg-override-group (string) (max_len: 35):
                Override the default replacement message group for this poli...
            reputation-direction (string) (enum: ['source', 'destination']):
                Direction of the initial traffic for reputation to take effe...
            reputation-direction6 (string) (enum: ['source', 'destination']):
                Direction of the initial traffic for IPv6 reputation to take...
            reputation-minimum (integer) (range: 0-4294967295):
                Minimum Reputation to take action.
            reputation-minimum6 (integer) (range: 0-4294967295):
                IPv6 Minimum Reputation to take action.
            rtp-addr (list[object]):
                Address names if this is an RTP NAT policy.
            rtp-nat (string) (enum: ['disable', 'enable']):
                Enable Real Time Protocol (RTP) NAT.
            schedule (string) (max_len: 35):
                Schedule name.
            schedule-timeout (string) (enum: ['enable', 'disable']):
                Enable to force current sessions to end when the schedule ob...
            sctp-filter-profile (string) (max_len: 47):
                Name of an existing SCTP filter profile.
            send-deny-packet (string) (enum: ['disable', 'enable']):
                Enable to send a reply when a session is denied or blocked b...
            service (list[object]):
                Service and service group names.
            service-negate (string) (enum: ['enable', 'disable']):
                When enabled service specifies what the service must NOT be.
            session-ttl (string):
                TTL in seconds for sessions accepted by this policy (0 means...
            sgt (list[object]):
                Security group tags.
            sgt-check (string) (enum: ['enable', 'disable']):
                Enable/disable security group tags (SGT) check.
            src-vendor-mac (list[object]):
                Vendor MAC source ID.
            srcaddr (list[object]):
                Source IPv4 address and address group names.
            srcaddr-negate (string) (enum: ['enable', 'disable']):
                When enabled srcaddr specifies what the source address must ...
            srcaddr6 (list[object]):
                Source IPv6 address name and address group names.
            srcaddr6-negate (string) (enum: ['enable', 'disable']):
                When enabled srcaddr6 specifies what the source address must...
            srcintf (list[object]):
                Incoming (ingress) interface.
            ssh-filter-profile (string) (max_len: 47):
                Name of an existing SSH filter profile.
            ssh-policy-redirect (string) (enum: ['enable', 'disable']):
                Redirect SSH traffic to matching transparent proxy policy.
            ssl-ssh-profile (string) (max_len: 47):
                Name of an existing SSL SSH profile.
            status (string) (enum: ['enable', 'disable']):
                Enable or disable this policy.
            tcp-mss-receiver (integer) (range: 0-65535):
                Receiver TCP maximum segment size (MSS).
            tcp-mss-sender (integer) (range: 0-65535):
                Sender TCP maximum segment size (MSS).
            tcp-session-without-syn (string) (enum: ['all', 'data-only', 'disable']):
                Enable/disable creation of TCP session without SYN flag.
            timeout-send-rst (string) (enum: ['enable', 'disable']):
                Enable/disable sending RST packets when TCP sessions expire.
            tos (string):
                ToS (Type of Service) value used for comparison.
            tos-mask (string):
                Non-zero bit positions are used for comparison while zero bi...
            tos-negate (string) (enum: ['enable', 'disable']):
                Enable negated TOS match.
            traffic-shaper (string) (max_len: 35):
                Traffic shaper.
            traffic-shaper-reverse (string) (max_len: 35):
                Reverse traffic shaper.
            users (list[object]):
                Names of individual users that can authenticate with this po...
            utm-status (string) (enum: ['enable', 'disable']):
                Enable to add one or more security profiles (AV, IPS, etc.) ...
            uuid (string):
                Universally Unique Identifier (UUID; automatically assigned ...
            videofilter-profile (string) (max_len: 47):
                Name of an existing VideoFilter profile.
            virtual-patch-profile (string) (max_len: 47):
                Name of an existing virtual-patch profile.
            vlan-cos-fwd (integer) (range: 0-7):
                VLAN forward direction user priority: 255 passthrough, 0 low...
            vlan-cos-rev (integer) (range: 0-7):
                VLAN reverse direction user priority: 255 passthrough, 0 low...
            vlan-filter (string):
                VLAN ranges to allow
            voip-profile (string) (max_len: 47):
                Name of an existing VoIP (voipd) profile.
            vpntunnel (string) (max_len: 35):
                Policy-based IPsec VPN: name of the IPsec VPN Phase 1.
            waf-profile (string) (max_len: 47):
                Name of an existing Web application firewall profile.
            wccp (string) (enum: ['enable', 'disable']):
                Enable/disable forwarding traffic matching this policy to a ...
            webfilter-profile (string) (max_len: 47):
                Name of an existing Web filter profile.
            webproxy-forward-server (string) (max_len: 63):
                Webproxy forward server name.
            webproxy-profile (string) (max_len: 63):
                Webproxy profile name.
            ztna-device-ownership (string) (enum: ['enable', 'disable']):
                Enable/disable zero trust device ownership.
            ztna-ems-tag (list[object]):
                Source ztna-ems-tag names.
            ztna-ems-tag-negate (string) (enum: ['enable', 'disable']):
                When enabled ztna-ems-tag specifies what the tags must NOT b...
            ztna-ems-tag-secondary (list[object]):
                Source ztna-ems-tag-secondary names.
            ztna-geo-tag (list[object]):
                Source ztna-geo-tag names.
            ztna-policy-redirect (string) (enum: ['enable', 'disable']):
                Redirect ZTNA traffic to matching Access-Proxy proxy-policy.
            ztna-status (string) (enum: ['enable', 'disable']):
                Enable/disable zero trust access.
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
        if action is not None:
            payload_dict["action"] = action
        if anti_replay is not None:
            payload_dict["anti-replay"] = anti_replay
        if app_monitor is not None:
            payload_dict["app-monitor"] = app_monitor
        if application_list is not None:
            payload_dict["application-list"] = application_list
        if auth_cert is not None:
            payload_dict["auth-cert"] = auth_cert
        if auth_path is not None:
            payload_dict["auth-path"] = auth_path
        if auth_redirect_addr is not None:
            payload_dict["auth-redirect-addr"] = auth_redirect_addr
        if auto_asic_offload is not None:
            payload_dict["auto-asic-offload"] = auto_asic_offload
        if av_profile is not None:
            payload_dict["av-profile"] = av_profile
        if block_notification is not None:
            payload_dict["block-notification"] = block_notification
        if captive_portal_exempt is not None:
            payload_dict["captive-portal-exempt"] = captive_portal_exempt
        if capture_packet is not None:
            payload_dict["capture-packet"] = capture_packet
        if casb_profile is not None:
            payload_dict["casb-profile"] = casb_profile
        if comments is not None:
            payload_dict["comments"] = comments
        if custom_log_fields is not None:
            payload_dict["custom-log-fields"] = custom_log_fields
        if decrypted_traffic_mirror is not None:
            payload_dict["decrypted-traffic-mirror"] = decrypted_traffic_mirror
        if delay_tcp_npu_session is not None:
            payload_dict["delay-tcp-npu-session"] = delay_tcp_npu_session
        if diameter_filter_profile is not None:
            payload_dict["diameter-filter-profile"] = diameter_filter_profile
        if diffserv_copy is not None:
            payload_dict["diffserv-copy"] = diffserv_copy
        if diffserv_forward is not None:
            payload_dict["diffserv-forward"] = diffserv_forward
        if diffserv_reverse is not None:
            payload_dict["diffserv-reverse"] = diffserv_reverse
        if diffservcode_forward is not None:
            payload_dict["diffservcode-forward"] = diffservcode_forward
        if diffservcode_rev is not None:
            payload_dict["diffservcode-rev"] = diffservcode_rev
        if disclaimer is not None:
            payload_dict["disclaimer"] = disclaimer
        if dlp_profile is not None:
            payload_dict["dlp-profile"] = dlp_profile
        if dnsfilter_profile is not None:
            payload_dict["dnsfilter-profile"] = dnsfilter_profile
        if dsri is not None:
            payload_dict["dsri"] = dsri
        if dstaddr is not None:
            payload_dict["dstaddr"] = dstaddr
        if dstaddr_negate is not None:
            payload_dict["dstaddr-negate"] = dstaddr_negate
        if dstaddr6 is not None:
            payload_dict["dstaddr6"] = dstaddr6
        if dstaddr6_negate is not None:
            payload_dict["dstaddr6-negate"] = dstaddr6_negate
        if dstintf is not None:
            payload_dict["dstintf"] = dstintf
        if dynamic_shaping is not None:
            payload_dict["dynamic-shaping"] = dynamic_shaping
        if email_collect is not None:
            payload_dict["email-collect"] = email_collect
        if emailfilter_profile is not None:
            payload_dict["emailfilter-profile"] = emailfilter_profile
        if fec is not None:
            payload_dict["fec"] = fec
        if file_filter_profile is not None:
            payload_dict["file-filter-profile"] = file_filter_profile
        if firewall_session_dirty is not None:
            payload_dict["firewall-session-dirty"] = firewall_session_dirty
        if fixedport is not None:
            payload_dict["fixedport"] = fixedport
        if fsso_agent_for_ntlm is not None:
            payload_dict["fsso-agent-for-ntlm"] = fsso_agent_for_ntlm
        if fsso_groups is not None:
            payload_dict["fsso-groups"] = fsso_groups
        if geoip_anycast is not None:
            payload_dict["geoip-anycast"] = geoip_anycast
        if geoip_match is not None:
            payload_dict["geoip-match"] = geoip_match
        if groups is not None:
            payload_dict["groups"] = groups
        if http_policy_redirect is not None:
            payload_dict["http-policy-redirect"] = http_policy_redirect
        if icap_profile is not None:
            payload_dict["icap-profile"] = icap_profile
        if identity_based_route is not None:
            payload_dict["identity-based-route"] = identity_based_route
        if inbound is not None:
            payload_dict["inbound"] = inbound
        if inspection_mode is not None:
            payload_dict["inspection-mode"] = inspection_mode
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
        if internet_service_src is not None:
            payload_dict["internet-service-src"] = internet_service_src
        if internet_service_src_custom is not None:
            payload_dict["internet-service-src-custom"] = internet_service_src_custom
        if internet_service_src_custom_group is not None:
            payload_dict["internet-service-src-custom-group"] = internet_service_src_custom_group
        if internet_service_src_fortiguard is not None:
            payload_dict["internet-service-src-fortiguard"] = internet_service_src_fortiguard
        if internet_service_src_group is not None:
            payload_dict["internet-service-src-group"] = internet_service_src_group
        if internet_service_src_name is not None:
            payload_dict["internet-service-src-name"] = internet_service_src_name
        if internet_service_src_negate is not None:
            payload_dict["internet-service-src-negate"] = internet_service_src_negate
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
        if internet_service6_src is not None:
            payload_dict["internet-service6-src"] = internet_service6_src
        if internet_service6_src_custom is not None:
            payload_dict["internet-service6-src-custom"] = internet_service6_src_custom
        if internet_service6_src_custom_group is not None:
            payload_dict["internet-service6-src-custom-group"] = internet_service6_src_custom_group
        if internet_service6_src_fortiguard is not None:
            payload_dict["internet-service6-src-fortiguard"] = internet_service6_src_fortiguard
        if internet_service6_src_group is not None:
            payload_dict["internet-service6-src-group"] = internet_service6_src_group
        if internet_service6_src_name is not None:
            payload_dict["internet-service6-src-name"] = internet_service6_src_name
        if internet_service6_src_negate is not None:
            payload_dict["internet-service6-src-negate"] = internet_service6_src_negate
        if ippool is not None:
            payload_dict["ippool"] = ippool
        if ips_sensor is not None:
            payload_dict["ips-sensor"] = ips_sensor
        if ips_voip_filter is not None:
            payload_dict["ips-voip-filter"] = ips_voip_filter
        if log_http_transaction is not None:
            payload_dict["log-http-transaction"] = log_http_transaction
        if logtraffic is not None:
            payload_dict["logtraffic"] = logtraffic
        if logtraffic_start is not None:
            payload_dict["logtraffic-start"] = logtraffic_start
        if match_vip is not None:
            payload_dict["match-vip"] = match_vip
        if match_vip_only is not None:
            payload_dict["match-vip-only"] = match_vip_only
        if name is not None:
            payload_dict["name"] = name
        if nat is not None:
            payload_dict["nat"] = nat
        if nat46 is not None:
            payload_dict["nat46"] = nat46
        if nat64 is not None:
            payload_dict["nat64"] = nat64
        if natinbound is not None:
            payload_dict["natinbound"] = natinbound
        if natip is not None:
            payload_dict["natip"] = natip
        if natoutbound is not None:
            payload_dict["natoutbound"] = natoutbound
        if network_service_dynamic is not None:
            payload_dict["network-service-dynamic"] = network_service_dynamic
        if network_service_src_dynamic is not None:
            payload_dict["network-service-src-dynamic"] = network_service_src_dynamic
        if np_acceleration is not None:
            payload_dict["np-acceleration"] = np_acceleration
        if ntlm is not None:
            payload_dict["ntlm"] = ntlm
        if ntlm_enabled_browsers is not None:
            payload_dict["ntlm-enabled-browsers"] = ntlm_enabled_browsers
        if ntlm_guest is not None:
            payload_dict["ntlm-guest"] = ntlm_guest
        if outbound is not None:
            payload_dict["outbound"] = outbound
        if passive_wan_health_measurement is not None:
            payload_dict["passive-wan-health-measurement"] = passive_wan_health_measurement
        if pcp_inbound is not None:
            payload_dict["pcp-inbound"] = pcp_inbound
        if pcp_outbound is not None:
            payload_dict["pcp-outbound"] = pcp_outbound
        if pcp_poolname is not None:
            payload_dict["pcp-poolname"] = pcp_poolname
        if per_ip_shaper is not None:
            payload_dict["per-ip-shaper"] = per_ip_shaper
        if permit_any_host is not None:
            payload_dict["permit-any-host"] = permit_any_host
        if permit_stun_host is not None:
            payload_dict["permit-stun-host"] = permit_stun_host
        if policy_expiry is not None:
            payload_dict["policy-expiry"] = policy_expiry
        if policy_expiry_date is not None:
            payload_dict["policy-expiry-date"] = policy_expiry_date
        if policy_expiry_date_utc is not None:
            payload_dict["policy-expiry-date-utc"] = policy_expiry_date_utc
        if policyid is not None:
            payload_dict["policyid"] = policyid
        if poolname is not None:
            payload_dict["poolname"] = poolname
        if poolname6 is not None:
            payload_dict["poolname6"] = poolname6
        if port_preserve is not None:
            payload_dict["port-preserve"] = port_preserve
        if port_random is not None:
            payload_dict["port-random"] = port_random
        if profile_group is not None:
            payload_dict["profile-group"] = profile_group
        if profile_protocol_options is not None:
            payload_dict["profile-protocol-options"] = profile_protocol_options
        if profile_type is not None:
            payload_dict["profile-type"] = profile_type
        if radius_ip_auth_bypass is not None:
            payload_dict["radius-ip-auth-bypass"] = radius_ip_auth_bypass
        if radius_mac_auth_bypass is not None:
            payload_dict["radius-mac-auth-bypass"] = radius_mac_auth_bypass
        if redirect_url is not None:
            payload_dict["redirect-url"] = redirect_url
        if replacemsg_override_group is not None:
            payload_dict["replacemsg-override-group"] = replacemsg_override_group
        if reputation_direction is not None:
            payload_dict["reputation-direction"] = reputation_direction
        if reputation_direction6 is not None:
            payload_dict["reputation-direction6"] = reputation_direction6
        if reputation_minimum is not None:
            payload_dict["reputation-minimum"] = reputation_minimum
        if reputation_minimum6 is not None:
            payload_dict["reputation-minimum6"] = reputation_minimum6
        if rtp_addr is not None:
            payload_dict["rtp-addr"] = rtp_addr
        if rtp_nat is not None:
            payload_dict["rtp-nat"] = rtp_nat
        if schedule is not None:
            payload_dict["schedule"] = schedule
        if schedule_timeout is not None:
            payload_dict["schedule-timeout"] = schedule_timeout
        if sctp_filter_profile is not None:
            payload_dict["sctp-filter-profile"] = sctp_filter_profile
        if send_deny_packet is not None:
            payload_dict["send-deny-packet"] = send_deny_packet
        if service is not None:
            payload_dict["service"] = service
        if service_negate is not None:
            payload_dict["service-negate"] = service_negate
        if session_ttl is not None:
            payload_dict["session-ttl"] = session_ttl
        if sgt is not None:
            payload_dict["sgt"] = sgt
        if sgt_check is not None:
            payload_dict["sgt-check"] = sgt_check
        if src_vendor_mac is not None:
            payload_dict["src-vendor-mac"] = src_vendor_mac
        if srcaddr is not None:
            payload_dict["srcaddr"] = srcaddr
        if srcaddr_negate is not None:
            payload_dict["srcaddr-negate"] = srcaddr_negate
        if srcaddr6 is not None:
            payload_dict["srcaddr6"] = srcaddr6
        if srcaddr6_negate is not None:
            payload_dict["srcaddr6-negate"] = srcaddr6_negate
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
        if tcp_mss_receiver is not None:
            payload_dict["tcp-mss-receiver"] = tcp_mss_receiver
        if tcp_mss_sender is not None:
            payload_dict["tcp-mss-sender"] = tcp_mss_sender
        if tcp_session_without_syn is not None:
            payload_dict["tcp-session-without-syn"] = tcp_session_without_syn
        if timeout_send_rst is not None:
            payload_dict["timeout-send-rst"] = timeout_send_rst
        if tos is not None:
            payload_dict["tos"] = tos
        if tos_mask is not None:
            payload_dict["tos-mask"] = tos_mask
        if tos_negate is not None:
            payload_dict["tos-negate"] = tos_negate
        if traffic_shaper is not None:
            payload_dict["traffic-shaper"] = traffic_shaper
        if traffic_shaper_reverse is not None:
            payload_dict["traffic-shaper-reverse"] = traffic_shaper_reverse
        if users is not None:
            payload_dict["users"] = users
        if utm_status is not None:
            payload_dict["utm-status"] = utm_status
        if uuid is not None:
            payload_dict["uuid"] = uuid
        if videofilter_profile is not None:
            payload_dict["videofilter-profile"] = videofilter_profile
        if virtual_patch_profile is not None:
            payload_dict["virtual-patch-profile"] = virtual_patch_profile
        if vlan_cos_fwd is not None:
            payload_dict["vlan-cos-fwd"] = vlan_cos_fwd
        if vlan_cos_rev is not None:
            payload_dict["vlan-cos-rev"] = vlan_cos_rev
        if vlan_filter is not None:
            payload_dict["vlan-filter"] = vlan_filter
        if voip_profile is not None:
            payload_dict["voip-profile"] = voip_profile
        if vpntunnel is not None:
            payload_dict["vpntunnel"] = vpntunnel
        if waf_profile is not None:
            payload_dict["waf-profile"] = waf_profile
        if wccp is not None:
            payload_dict["wccp"] = wccp
        if webfilter_profile is not None:
            payload_dict["webfilter-profile"] = webfilter_profile
        if webproxy_forward_server is not None:
            payload_dict["webproxy-forward-server"] = webproxy_forward_server
        if webproxy_profile is not None:
            payload_dict["webproxy-profile"] = webproxy_profile
        if ztna_device_ownership is not None:
            payload_dict["ztna-device-ownership"] = ztna_device_ownership
        if ztna_ems_tag is not None:
            payload_dict["ztna-ems-tag"] = ztna_ems_tag
        if ztna_ems_tag_negate is not None:
            payload_dict["ztna-ems-tag-negate"] = ztna_ems_tag_negate
        if ztna_ems_tag_secondary is not None:
            payload_dict["ztna-ems-tag-secondary"] = ztna_ems_tag_secondary
        if ztna_geo_tag is not None:
            payload_dict["ztna-geo-tag"] = ztna_geo_tag
        if ztna_policy_redirect is not None:
            payload_dict["ztna-policy-redirect"] = ztna_policy_redirect
        if ztna_status is not None:
            payload_dict["ztna-status"] = ztna_status
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
        Delete a policy entry.

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
