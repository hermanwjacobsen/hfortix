"""
FortiOS security-policy API wrapper.
Provides access to /api/v2/cmdb/firewall/security-policy endpoint.
"""

from typing import Any, Dict, List, Optional, Union


class SecurityPolicy:
    """
    Wrapper for firewall security-policy API endpoint.
    
    Manages security-policy configuration with full Swagger-spec parameter support.
    """
    
    def __init__(self, http_client: Any):
        """
        Initialize the SecurityPolicy wrapper.
        
        Args:
            http_client: The HTTP client for API communication
        """
        self._client = http_client
        self.path = 'firewall/security-policy'
    
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
        **kwargs
    ) -> Dict[str, Any]:
        """
        Retrieve a list of all security-policy entries.
        
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
            params['datasource'] = datasource
        if start is not None:
            params['start'] = start
        if count is not None:
            params['count'] = count
        if skip_to is not None:
            params['skip_to'] = skip_to
        if with_meta is not None:
            params['with_meta'] = with_meta
        if with_contents_hash is not None:
            params['with_contents_hash'] = with_contents_hash
        if skip is not None:
            params['skip'] = skip
        if format is not None:
            params['format'] = format
        if filter is not None:
            params['filter'] = filter
        if key is not None:
            params['key'] = key
        if pattern is not None:
            params['pattern'] = pattern
        if scope is not None:
            params['scope'] = scope
        if exclude_default_values is not None:
            params['exclude-default-values'] = exclude_default_values
        if datasource_format is not None:
            params['datasource_format'] = datasource_format
        if unfiltered_count is not None:
            params['unfiltered_count'] = unfiltered_count
        if stat_items is not None:
            params['stat-items'] = stat_items
        if primary_keys is not None:
            params['primary_keys'] = primary_keys
        if action is not None:
            params['action'] = action
        if vdom is not None:
            params['vdom'] = vdom
        
        # Add any additional kwargs
        params.update(kwargs)
        
        # Extract vdom if present
        vdom = params.pop('vdom', None)
        
        return self._client.get('cmdb', self.path, params=params, vdom=vdom)

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
        **kwargs
    ) -> Dict[str, Any]:
        """
        Retrieve a specific security-policy entry by its policyid.
        
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
            params['attr'] = attr
        if count is not None:
            params['count'] = count
        if skip_to_datasource is not None:
            params['skip_to_datasource'] = skip_to_datasource
        if acs is not None:
            params['acs'] = acs
        if search is not None:
            params['search'] = search
        if scope is not None:
            params['scope'] = scope
        if datasource is not None:
            params['datasource'] = datasource
        if with_meta is not None:
            params['with_meta'] = with_meta
        if skip is not None:
            params['skip'] = skip
        if format is not None:
            params['format'] = format
        if action is not None:
            params['action'] = action
        if vdom is not None:
            params['vdom'] = vdom
        
        # Add any additional kwargs
        params.update(kwargs)
        
        # Extract vdom if present
        vdom = params.pop('vdom', None)
        
        return self._client.get('cmdb', f'{self.path}/{mkey_str}', params=params, vdom=vdom)

    def create(
        self,
        data: Optional[Dict[str, Any]] = None,
        vdom: Optional[Any] = None,
        action: Optional[Any] = None,
        nkey: Optional[Any] = None,
        scope: Optional[Any] = None,
        app_category: Optional[list] = None,
        app_group: Optional[list] = None,
        application: Optional[list] = None,
        application_list: Optional[str] = None,
        av_profile: Optional[str] = None,
        casb_profile: Optional[str] = None,
        comments: Optional[str] = None,
        diameter_filter_profile: Optional[str] = None,
        dlp_profile: Optional[str] = None,
        dnsfilter_profile: Optional[str] = None,
        dstaddr: Optional[list] = None,
        dstaddr_negate: Optional[str] = None,
        dstaddr6: Optional[list] = None,
        dstaddr6_negate: Optional[str] = None,
        dstintf: Optional[list] = None,
        emailfilter_profile: Optional[str] = None,
        enforce_default_app_port: Optional[str] = None,
        file_filter_profile: Optional[str] = None,
        fsso_groups: Optional[list] = None,
        groups: Optional[list] = None,
        icap_profile: Optional[str] = None,
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
        ips_sensor: Optional[str] = None,
        ips_voip_filter: Optional[str] = None,
        learning_mode: Optional[str] = None,
        logtraffic: Optional[str] = None,
        name: Optional[str] = None,
        nat46: Optional[str] = None,
        nat64: Optional[str] = None,
        policyid: Optional[int] = None,
        profile_group: Optional[str] = None,
        profile_protocol_options: Optional[str] = None,
        profile_type: Optional[str] = None,
        schedule: Optional[str] = None,
        sctp_filter_profile: Optional[str] = None,
        send_deny_packet: Optional[str] = None,
        service: Optional[list] = None,
        service_negate: Optional[str] = None,
        srcaddr: Optional[list] = None,
        srcaddr_negate: Optional[str] = None,
        srcaddr6: Optional[list] = None,
        srcaddr6_negate: Optional[str] = None,
        srcintf: Optional[list] = None,
        ssh_filter_profile: Optional[str] = None,
        ssl_ssh_profile: Optional[str] = None,
        status: Optional[str] = None,
        url_category: Optional[str] = None,
        users: Optional[list] = None,
        uuid: Optional[str] = None,
        videofilter_profile: Optional[str] = None,
        virtual_patch_profile: Optional[str] = None,
        voip_profile: Optional[str] = None,
        webfilter_profile: Optional[str] = None,
        **kwargs
    ) -> Dict[str, Any]:
        """
        Create a new security-policy entry.
        
        Supports two usage patterns:
        1. Pass data dict: create(data={"key": "value"}, vdom="root")
        2. Pass kwargs: create(key="value", vdom="root")
        
        Args:
            data: The configuration data (optional if using kwargs)
            vdom: Specify the Virtual Domain(s) from which results are returned or chang
            action: If supported, an action can be specified.
            nkey: If *action=clone*, use *nkey* to specify the ID for the new resource t
            scope: Specify the Scope from which results are returned or changes are appli
            **kwargs: Additional parameters

        Body schema properties (can pass via data dict or as kwargs):

            action (string) (enum: ['accept', 'deny']):
                Policy action (accept/deny).
            app-category (list[object]):
                Application category ID list.
            app-group (list[object]):
                Application group names.
            application (list[object]):
                Application ID list.
            application-list (string) (max_len: 47):
                Name of an existing Application list.
            av-profile (string) (max_len: 47):
                Name of an existing Antivirus profile.
            casb-profile (string) (max_len: 47):
                Name of an existing CASB profile.
            comments (string) (max_len: 1023):
                Comment.
            diameter-filter-profile (string) (max_len: 47):
                Name of an existing Diameter filter profile.
            dlp-profile (string) (max_len: 47):
                Name of an existing DLP profile.
            dnsfilter-profile (string) (max_len: 47):
                Name of an existing DNS filter profile.
            dstaddr (list[object]):
                Destination IPv4 address name and address group names.
            dstaddr-negate (string) (enum: ['enable', 'disable']):
                When enabled dstaddr specifies what the destination address ...
            dstaddr6 (list[object]):
                Destination IPv6 address name and address group names.
            dstaddr6-negate (string) (enum: ['enable', 'disable']):
                When enabled dstaddr6 specifies what the destination address...
            dstintf (list[object]):
                Outgoing (egress) interface.
            emailfilter-profile (string) (max_len: 47):
                Name of an existing email filter profile.
            enforce-default-app-port (string) (enum: ['enable', 'disable']):
                Enable/disable default application port enforcement for allo...
            file-filter-profile (string) (max_len: 47):
                Name of an existing file-filter profile.
            fsso-groups (list[object]):
                Names of FSSO groups.
            groups (list[object]):
                Names of user groups that can authenticate with this policy.
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
                Custom IPv6 Internet Service group name.
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
            ips-sensor (string) (max_len: 47):
                Name of an existing IPS sensor.
            ips-voip-filter (string) (max_len: 47):
                Name of an existing VoIP (ips) profile.
            learning-mode (string) (enum: ['enable', 'disable']):
                Enable to allow everything, but log all of the meaningful da...
            logtraffic (string) (enum: ['all', 'utm', 'disable']):
                Enable or disable logging. Log all sessions or security prof...
            name (string) (max_len: 35):
                Policy name.
            nat46 (string) (enum: ['enable', 'disable']):
                Enable/disable NAT46.
            nat64 (string) (enum: ['enable', 'disable']):
                Enable/disable NAT64.
            policyid (integer) (range: 0-4294967294):
                Policy ID.
            profile-group (string) (max_len: 47):
                Name of profile group.
            profile-protocol-options (string) (max_len: 47):
                Name of an existing Protocol options profile.
            profile-type (string) (enum: ['single', 'group']):
                Determine whether the firewall policy allows security profil...
            schedule (string) (max_len: 35):
                Schedule name.
            sctp-filter-profile (string) (max_len: 47):
                Name of an existing SCTP filter profile.
            send-deny-packet (string) (enum: ['disable', 'enable']):
                Enable to send a reply when a session is denied or blocked b...
            service (list[object]):
                Service and service group names.
            service-negate (string) (enum: ['enable', 'disable']):
                When enabled service specifies what the service must NOT be.
            srcaddr (list[object]):
                Source IPv4 address name and address group names.
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
            ssl-ssh-profile (string) (max_len: 47):
                Name of an existing SSL SSH profile.
            status (string) (enum: ['enable', 'disable']):
                Enable or disable this policy.
            url-category (string):
                URL categories or groups.
            users (list[object]):
                Names of individual users that can authenticate with this po...
            uuid (string):
                Universally Unique Identifier (UUID; automatically assigned ...
            videofilter-profile (string) (max_len: 47):
                Name of an existing VideoFilter profile.
            virtual-patch-profile (string) (max_len: 47):
                Name of an existing virtual-patch profile.
            voip-profile (string) (max_len: 47):
                Name of an existing VoIP (voipd) profile.
            webfilter-profile (string) (max_len: 47):
                Name of an existing Web filter profile.
            
        Returns:
            API response dictionary
        """
        # Build data from kwargs if not provided
        if data is None:
            data = {}
        if action is not None:
            data['action'] = action
        if app_category is not None:
            data['app-category'] = app_category
        if app_group is not None:
            data['app-group'] = app_group
        if application is not None:
            data['application'] = application
        if application_list is not None:
            data['application-list'] = application_list
        if av_profile is not None:
            data['av-profile'] = av_profile
        if casb_profile is not None:
            data['casb-profile'] = casb_profile
        if comments is not None:
            data['comments'] = comments
        if diameter_filter_profile is not None:
            data['diameter-filter-profile'] = diameter_filter_profile
        if dlp_profile is not None:
            data['dlp-profile'] = dlp_profile
        if dnsfilter_profile is not None:
            data['dnsfilter-profile'] = dnsfilter_profile
        if dstaddr is not None:
            data['dstaddr'] = dstaddr
        if dstaddr_negate is not None:
            data['dstaddr-negate'] = dstaddr_negate
        if dstaddr6 is not None:
            data['dstaddr6'] = dstaddr6
        if dstaddr6_negate is not None:
            data['dstaddr6-negate'] = dstaddr6_negate
        if dstintf is not None:
            data['dstintf'] = dstintf
        if emailfilter_profile is not None:
            data['emailfilter-profile'] = emailfilter_profile
        if enforce_default_app_port is not None:
            data['enforce-default-app-port'] = enforce_default_app_port
        if file_filter_profile is not None:
            data['file-filter-profile'] = file_filter_profile
        if fsso_groups is not None:
            data['fsso-groups'] = fsso_groups
        if groups is not None:
            data['groups'] = groups
        if icap_profile is not None:
            data['icap-profile'] = icap_profile
        if internet_service is not None:
            data['internet-service'] = internet_service
        if internet_service_custom is not None:
            data['internet-service-custom'] = internet_service_custom
        if internet_service_custom_group is not None:
            data['internet-service-custom-group'] = internet_service_custom_group
        if internet_service_fortiguard is not None:
            data['internet-service-fortiguard'] = internet_service_fortiguard
        if internet_service_group is not None:
            data['internet-service-group'] = internet_service_group
        if internet_service_name is not None:
            data['internet-service-name'] = internet_service_name
        if internet_service_negate is not None:
            data['internet-service-negate'] = internet_service_negate
        if internet_service_src is not None:
            data['internet-service-src'] = internet_service_src
        if internet_service_src_custom is not None:
            data['internet-service-src-custom'] = internet_service_src_custom
        if internet_service_src_custom_group is not None:
            data['internet-service-src-custom-group'] = internet_service_src_custom_group
        if internet_service_src_fortiguard is not None:
            data['internet-service-src-fortiguard'] = internet_service_src_fortiguard
        if internet_service_src_group is not None:
            data['internet-service-src-group'] = internet_service_src_group
        if internet_service_src_name is not None:
            data['internet-service-src-name'] = internet_service_src_name
        if internet_service_src_negate is not None:
            data['internet-service-src-negate'] = internet_service_src_negate
        if internet_service6 is not None:
            data['internet-service6'] = internet_service6
        if internet_service6_custom is not None:
            data['internet-service6-custom'] = internet_service6_custom
        if internet_service6_custom_group is not None:
            data['internet-service6-custom-group'] = internet_service6_custom_group
        if internet_service6_fortiguard is not None:
            data['internet-service6-fortiguard'] = internet_service6_fortiguard
        if internet_service6_group is not None:
            data['internet-service6-group'] = internet_service6_group
        if internet_service6_name is not None:
            data['internet-service6-name'] = internet_service6_name
        if internet_service6_negate is not None:
            data['internet-service6-negate'] = internet_service6_negate
        if internet_service6_src is not None:
            data['internet-service6-src'] = internet_service6_src
        if internet_service6_src_custom is not None:
            data['internet-service6-src-custom'] = internet_service6_src_custom
        if internet_service6_src_custom_group is not None:
            data['internet-service6-src-custom-group'] = internet_service6_src_custom_group
        if internet_service6_src_fortiguard is not None:
            data['internet-service6-src-fortiguard'] = internet_service6_src_fortiguard
        if internet_service6_src_group is not None:
            data['internet-service6-src-group'] = internet_service6_src_group
        if internet_service6_src_name is not None:
            data['internet-service6-src-name'] = internet_service6_src_name
        if internet_service6_src_negate is not None:
            data['internet-service6-src-negate'] = internet_service6_src_negate
        if ips_sensor is not None:
            data['ips-sensor'] = ips_sensor
        if ips_voip_filter is not None:
            data['ips-voip-filter'] = ips_voip_filter
        if learning_mode is not None:
            data['learning-mode'] = learning_mode
        if logtraffic is not None:
            data['logtraffic'] = logtraffic
        if name is not None:
            data['name'] = name
        if nat46 is not None:
            data['nat46'] = nat46
        if nat64 is not None:
            data['nat64'] = nat64
        if policyid is not None:
            data['policyid'] = policyid
        if profile_group is not None:
            data['profile-group'] = profile_group
        if profile_protocol_options is not None:
            data['profile-protocol-options'] = profile_protocol_options
        if profile_type is not None:
            data['profile-type'] = profile_type
        if schedule is not None:
            data['schedule'] = schedule
        if sctp_filter_profile is not None:
            data['sctp-filter-profile'] = sctp_filter_profile
        if send_deny_packet is not None:
            data['send-deny-packet'] = send_deny_packet
        if service is not None:
            data['service'] = service
        if service_negate is not None:
            data['service-negate'] = service_negate
        if srcaddr is not None:
            data['srcaddr'] = srcaddr
        if srcaddr_negate is not None:
            data['srcaddr-negate'] = srcaddr_negate
        if srcaddr6 is not None:
            data['srcaddr6'] = srcaddr6
        if srcaddr6_negate is not None:
            data['srcaddr6-negate'] = srcaddr6_negate
        if srcintf is not None:
            data['srcintf'] = srcintf
        if ssh_filter_profile is not None:
            data['ssh-filter-profile'] = ssh_filter_profile
        if ssl_ssh_profile is not None:
            data['ssl-ssh-profile'] = ssl_ssh_profile
        if status is not None:
            data['status'] = status
        if url_category is not None:
            data['url-category'] = url_category
        if users is not None:
            data['users'] = users
        if uuid is not None:
            data['uuid'] = uuid
        if videofilter_profile is not None:
            data['videofilter-profile'] = videofilter_profile
        if virtual_patch_profile is not None:
            data['virtual-patch-profile'] = virtual_patch_profile
        if voip_profile is not None:
            data['voip-profile'] = voip_profile
        if webfilter_profile is not None:
            data['webfilter-profile'] = webfilter_profile
        
        params = {}
        
        if vdom is not None:
            params['vdom'] = vdom
        if action is not None:
            params['action'] = action
        if nkey is not None:
            params['nkey'] = nkey
        if scope is not None:
            params['scope'] = scope
        
        # Add any additional kwargs
        params.update(kwargs)
        
        # Extract vdom if present
        vdom = params.pop('vdom', None)
        
        return self._client.post('cmdb', self.path, data=data, params=params, vdom=vdom)

    def update(
        self,
        mkey: Union[str, int],
        data: Optional[Dict[str, Any]] = None,
        vdom: Optional[Any] = None,
        action: Optional[Any] = None,
        before: Optional[Any] = None,
        after: Optional[Any] = None,
        scope: Optional[Any] = None,
        app_category: Optional[list] = None,
        app_group: Optional[list] = None,
        application: Optional[list] = None,
        application_list: Optional[str] = None,
        av_profile: Optional[str] = None,
        casb_profile: Optional[str] = None,
        comments: Optional[str] = None,
        diameter_filter_profile: Optional[str] = None,
        dlp_profile: Optional[str] = None,
        dnsfilter_profile: Optional[str] = None,
        dstaddr: Optional[list] = None,
        dstaddr_negate: Optional[str] = None,
        dstaddr6: Optional[list] = None,
        dstaddr6_negate: Optional[str] = None,
        dstintf: Optional[list] = None,
        emailfilter_profile: Optional[str] = None,
        enforce_default_app_port: Optional[str] = None,
        file_filter_profile: Optional[str] = None,
        fsso_groups: Optional[list] = None,
        groups: Optional[list] = None,
        icap_profile: Optional[str] = None,
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
        ips_sensor: Optional[str] = None,
        ips_voip_filter: Optional[str] = None,
        learning_mode: Optional[str] = None,
        logtraffic: Optional[str] = None,
        name: Optional[str] = None,
        nat46: Optional[str] = None,
        nat64: Optional[str] = None,
        policyid: Optional[int] = None,
        profile_group: Optional[str] = None,
        profile_protocol_options: Optional[str] = None,
        profile_type: Optional[str] = None,
        schedule: Optional[str] = None,
        sctp_filter_profile: Optional[str] = None,
        send_deny_packet: Optional[str] = None,
        service: Optional[list] = None,
        service_negate: Optional[str] = None,
        srcaddr: Optional[list] = None,
        srcaddr_negate: Optional[str] = None,
        srcaddr6: Optional[list] = None,
        srcaddr6_negate: Optional[str] = None,
        srcintf: Optional[list] = None,
        ssh_filter_profile: Optional[str] = None,
        ssl_ssh_profile: Optional[str] = None,
        status: Optional[str] = None,
        url_category: Optional[str] = None,
        users: Optional[list] = None,
        uuid: Optional[str] = None,
        videofilter_profile: Optional[str] = None,
        virtual_patch_profile: Optional[str] = None,
        voip_profile: Optional[str] = None,
        webfilter_profile: Optional[str] = None,
        **kwargs
    ) -> Dict[str, Any]:
        """
        Update an existing security-policy entry.
        
        Supports two usage patterns:
        1. Pass data dict: update(mkey=123, data={"key": "value"}, vdom="root")
        2. Pass kwargs: update(mkey=123, key="value", vdom="root")
        
        Args:
            mkey: The policyid (primary key)
            data: The updated configuration data (optional if using kwargs)
            vdom: Specify the Virtual Domain(s) from which results are returned or chang
            action: If supported, an action can be specified.
            before: If *action=move*, use *before* to specify the ID of the resource that 
            after: If *action=move*, use *after* to specify the ID of the resource that t
            scope: Specify the Scope from which results are returned or changes are appli
            **kwargs: Additional parameters

        Body schema properties (can pass via data dict or as kwargs):

            action (string) (enum: ['accept', 'deny']):
                Policy action (accept/deny).
            app-category (list[object]):
                Application category ID list.
            app-group (list[object]):
                Application group names.
            application (list[object]):
                Application ID list.
            application-list (string) (max_len: 47):
                Name of an existing Application list.
            av-profile (string) (max_len: 47):
                Name of an existing Antivirus profile.
            casb-profile (string) (max_len: 47):
                Name of an existing CASB profile.
            comments (string) (max_len: 1023):
                Comment.
            diameter-filter-profile (string) (max_len: 47):
                Name of an existing Diameter filter profile.
            dlp-profile (string) (max_len: 47):
                Name of an existing DLP profile.
            dnsfilter-profile (string) (max_len: 47):
                Name of an existing DNS filter profile.
            dstaddr (list[object]):
                Destination IPv4 address name and address group names.
            dstaddr-negate (string) (enum: ['enable', 'disable']):
                When enabled dstaddr specifies what the destination address ...
            dstaddr6 (list[object]):
                Destination IPv6 address name and address group names.
            dstaddr6-negate (string) (enum: ['enable', 'disable']):
                When enabled dstaddr6 specifies what the destination address...
            dstintf (list[object]):
                Outgoing (egress) interface.
            emailfilter-profile (string) (max_len: 47):
                Name of an existing email filter profile.
            enforce-default-app-port (string) (enum: ['enable', 'disable']):
                Enable/disable default application port enforcement for allo...
            file-filter-profile (string) (max_len: 47):
                Name of an existing file-filter profile.
            fsso-groups (list[object]):
                Names of FSSO groups.
            groups (list[object]):
                Names of user groups that can authenticate with this policy.
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
                Custom IPv6 Internet Service group name.
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
            ips-sensor (string) (max_len: 47):
                Name of an existing IPS sensor.
            ips-voip-filter (string) (max_len: 47):
                Name of an existing VoIP (ips) profile.
            learning-mode (string) (enum: ['enable', 'disable']):
                Enable to allow everything, but log all of the meaningful da...
            logtraffic (string) (enum: ['all', 'utm', 'disable']):
                Enable or disable logging. Log all sessions or security prof...
            name (string) (max_len: 35):
                Policy name.
            nat46 (string) (enum: ['enable', 'disable']):
                Enable/disable NAT46.
            nat64 (string) (enum: ['enable', 'disable']):
                Enable/disable NAT64.
            policyid (integer) (range: 0-4294967294):
                Policy ID.
            profile-group (string) (max_len: 47):
                Name of profile group.
            profile-protocol-options (string) (max_len: 47):
                Name of an existing Protocol options profile.
            profile-type (string) (enum: ['single', 'group']):
                Determine whether the firewall policy allows security profil...
            schedule (string) (max_len: 35):
                Schedule name.
            sctp-filter-profile (string) (max_len: 47):
                Name of an existing SCTP filter profile.
            send-deny-packet (string) (enum: ['disable', 'enable']):
                Enable to send a reply when a session is denied or blocked b...
            service (list[object]):
                Service and service group names.
            service-negate (string) (enum: ['enable', 'disable']):
                When enabled service specifies what the service must NOT be.
            srcaddr (list[object]):
                Source IPv4 address name and address group names.
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
            ssl-ssh-profile (string) (max_len: 47):
                Name of an existing SSL SSH profile.
            status (string) (enum: ['enable', 'disable']):
                Enable or disable this policy.
            url-category (string):
                URL categories or groups.
            users (list[object]):
                Names of individual users that can authenticate with this po...
            uuid (string):
                Universally Unique Identifier (UUID; automatically assigned ...
            videofilter-profile (string) (max_len: 47):
                Name of an existing VideoFilter profile.
            virtual-patch-profile (string) (max_len: 47):
                Name of an existing virtual-patch profile.
            voip-profile (string) (max_len: 47):
                Name of an existing VoIP (voipd) profile.
            webfilter-profile (string) (max_len: 47):
                Name of an existing Web filter profile.
            
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
        if data is None:
            data = {}
        if action is not None:
            data['action'] = action
        if app_category is not None:
            data['app-category'] = app_category
        if app_group is not None:
            data['app-group'] = app_group
        if application is not None:
            data['application'] = application
        if application_list is not None:
            data['application-list'] = application_list
        if av_profile is not None:
            data['av-profile'] = av_profile
        if casb_profile is not None:
            data['casb-profile'] = casb_profile
        if comments is not None:
            data['comments'] = comments
        if diameter_filter_profile is not None:
            data['diameter-filter-profile'] = diameter_filter_profile
        if dlp_profile is not None:
            data['dlp-profile'] = dlp_profile
        if dnsfilter_profile is not None:
            data['dnsfilter-profile'] = dnsfilter_profile
        if dstaddr is not None:
            data['dstaddr'] = dstaddr
        if dstaddr_negate is not None:
            data['dstaddr-negate'] = dstaddr_negate
        if dstaddr6 is not None:
            data['dstaddr6'] = dstaddr6
        if dstaddr6_negate is not None:
            data['dstaddr6-negate'] = dstaddr6_negate
        if dstintf is not None:
            data['dstintf'] = dstintf
        if emailfilter_profile is not None:
            data['emailfilter-profile'] = emailfilter_profile
        if enforce_default_app_port is not None:
            data['enforce-default-app-port'] = enforce_default_app_port
        if file_filter_profile is not None:
            data['file-filter-profile'] = file_filter_profile
        if fsso_groups is not None:
            data['fsso-groups'] = fsso_groups
        if groups is not None:
            data['groups'] = groups
        if icap_profile is not None:
            data['icap-profile'] = icap_profile
        if internet_service is not None:
            data['internet-service'] = internet_service
        if internet_service_custom is not None:
            data['internet-service-custom'] = internet_service_custom
        if internet_service_custom_group is not None:
            data['internet-service-custom-group'] = internet_service_custom_group
        if internet_service_fortiguard is not None:
            data['internet-service-fortiguard'] = internet_service_fortiguard
        if internet_service_group is not None:
            data['internet-service-group'] = internet_service_group
        if internet_service_name is not None:
            data['internet-service-name'] = internet_service_name
        if internet_service_negate is not None:
            data['internet-service-negate'] = internet_service_negate
        if internet_service_src is not None:
            data['internet-service-src'] = internet_service_src
        if internet_service_src_custom is not None:
            data['internet-service-src-custom'] = internet_service_src_custom
        if internet_service_src_custom_group is not None:
            data['internet-service-src-custom-group'] = internet_service_src_custom_group
        if internet_service_src_fortiguard is not None:
            data['internet-service-src-fortiguard'] = internet_service_src_fortiguard
        if internet_service_src_group is not None:
            data['internet-service-src-group'] = internet_service_src_group
        if internet_service_src_name is not None:
            data['internet-service-src-name'] = internet_service_src_name
        if internet_service_src_negate is not None:
            data['internet-service-src-negate'] = internet_service_src_negate
        if internet_service6 is not None:
            data['internet-service6'] = internet_service6
        if internet_service6_custom is not None:
            data['internet-service6-custom'] = internet_service6_custom
        if internet_service6_custom_group is not None:
            data['internet-service6-custom-group'] = internet_service6_custom_group
        if internet_service6_fortiguard is not None:
            data['internet-service6-fortiguard'] = internet_service6_fortiguard
        if internet_service6_group is not None:
            data['internet-service6-group'] = internet_service6_group
        if internet_service6_name is not None:
            data['internet-service6-name'] = internet_service6_name
        if internet_service6_negate is not None:
            data['internet-service6-negate'] = internet_service6_negate
        if internet_service6_src is not None:
            data['internet-service6-src'] = internet_service6_src
        if internet_service6_src_custom is not None:
            data['internet-service6-src-custom'] = internet_service6_src_custom
        if internet_service6_src_custom_group is not None:
            data['internet-service6-src-custom-group'] = internet_service6_src_custom_group
        if internet_service6_src_fortiguard is not None:
            data['internet-service6-src-fortiguard'] = internet_service6_src_fortiguard
        if internet_service6_src_group is not None:
            data['internet-service6-src-group'] = internet_service6_src_group
        if internet_service6_src_name is not None:
            data['internet-service6-src-name'] = internet_service6_src_name
        if internet_service6_src_negate is not None:
            data['internet-service6-src-negate'] = internet_service6_src_negate
        if ips_sensor is not None:
            data['ips-sensor'] = ips_sensor
        if ips_voip_filter is not None:
            data['ips-voip-filter'] = ips_voip_filter
        if learning_mode is not None:
            data['learning-mode'] = learning_mode
        if logtraffic is not None:
            data['logtraffic'] = logtraffic
        if name is not None:
            data['name'] = name
        if nat46 is not None:
            data['nat46'] = nat46
        if nat64 is not None:
            data['nat64'] = nat64
        if policyid is not None:
            data['policyid'] = policyid
        if profile_group is not None:
            data['profile-group'] = profile_group
        if profile_protocol_options is not None:
            data['profile-protocol-options'] = profile_protocol_options
        if profile_type is not None:
            data['profile-type'] = profile_type
        if schedule is not None:
            data['schedule'] = schedule
        if sctp_filter_profile is not None:
            data['sctp-filter-profile'] = sctp_filter_profile
        if send_deny_packet is not None:
            data['send-deny-packet'] = send_deny_packet
        if service is not None:
            data['service'] = service
        if service_negate is not None:
            data['service-negate'] = service_negate
        if srcaddr is not None:
            data['srcaddr'] = srcaddr
        if srcaddr_negate is not None:
            data['srcaddr-negate'] = srcaddr_negate
        if srcaddr6 is not None:
            data['srcaddr6'] = srcaddr6
        if srcaddr6_negate is not None:
            data['srcaddr6-negate'] = srcaddr6_negate
        if srcintf is not None:
            data['srcintf'] = srcintf
        if ssh_filter_profile is not None:
            data['ssh-filter-profile'] = ssh_filter_profile
        if ssl_ssh_profile is not None:
            data['ssl-ssh-profile'] = ssl_ssh_profile
        if status is not None:
            data['status'] = status
        if url_category is not None:
            data['url-category'] = url_category
        if users is not None:
            data['users'] = users
        if uuid is not None:
            data['uuid'] = uuid
        if videofilter_profile is not None:
            data['videofilter-profile'] = videofilter_profile
        if virtual_patch_profile is not None:
            data['virtual-patch-profile'] = virtual_patch_profile
        if voip_profile is not None:
            data['voip-profile'] = voip_profile
        if webfilter_profile is not None:
            data['webfilter-profile'] = webfilter_profile
        
        params = {}
        
        if vdom is not None:
            params['vdom'] = vdom
        if action is not None:
            params['action'] = action
        if before is not None:
            params['before'] = before
        if after is not None:
            params['after'] = after
        if scope is not None:
            params['scope'] = scope
        
        # Add any additional kwargs
        params.update(kwargs)
        
        # Extract vdom if present
        vdom = params.pop('vdom', None)
        
        return self._client.put('cmdb', f'{self.path}/{mkey_str}', data=data, params=params, vdom=vdom)

    def delete(
        self,
        mkey: Union[str, int],
        vdom: Optional[Any] = None,
        scope: Optional[Any] = None,
        **kwargs
    ) -> Dict[str, Any]:
        """
        Delete a security-policy entry.
        
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
            params['vdom'] = vdom
        if scope is not None:
            params['scope'] = scope
        
        # Add any additional kwargs
        params.update(kwargs)
        
        # Extract vdom if present
        vdom = params.pop('vdom', None)
        
        return self._client.delete('cmdb', f'{self.path}/{mkey_str}', params=params, vdom=vdom)
