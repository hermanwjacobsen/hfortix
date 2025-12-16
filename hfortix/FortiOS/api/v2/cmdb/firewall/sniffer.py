"""
FortiOS sniffer API wrapper.
Provides access to /api/v2/cmdb/firewall/sniffer endpoint.
"""

from typing import Any, Dict, List, Optional, Union


class Sniffer:
    """
    Wrapper for firewall sniffer API endpoint.
    
    Manages sniffer configuration with full Swagger-spec parameter support.
    """
    
    def __init__(self, http_client: Any):
        """
        Initialize the Sniffer wrapper.
        
        Args:
            http_client: The HTTP client for API communication
        """
        self._client = http_client
        self.path = 'firewall/sniffer'
    
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
        Retrieve a list of all sniffer entries.
        
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
        Retrieve a specific sniffer entry by its id.
        
        Args:
            mkey: The id (primary key)
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
        anomaly: Optional[list] = None,
        application_list: Optional[str] = None,
        application_list_status: Optional[str] = None,
        av_profile: Optional[str] = None,
        av_profile_status: Optional[str] = None,
        dlp_profile: Optional[str] = None,
        dlp_profile_status: Optional[str] = None,
        dsri: Optional[str] = None,
        emailfilter_profile: Optional[str] = None,
        emailfilter_profile_status: Optional[str] = None,
        file_filter_profile: Optional[str] = None,
        file_filter_profile_status: Optional[str] = None,
        host: Optional[str] = None,
        id: Optional[int] = None,
        interface: Optional[str] = None,
        ip_threatfeed: Optional[list] = None,
        ip_threatfeed_status: Optional[str] = None,
        ips_dos_status: Optional[str] = None,
        ips_sensor: Optional[str] = None,
        ips_sensor_status: Optional[str] = None,
        ipv6: Optional[str] = None,
        logtraffic: Optional[str] = None,
        non_ip: Optional[str] = None,
        port: Optional[str] = None,
        protocol: Optional[str] = None,
        status: Optional[str] = None,
        uuid: Optional[str] = None,
        vlan: Optional[str] = None,
        webfilter_profile: Optional[str] = None,
        webfilter_profile_status: Optional[str] = None,
        **kwargs
    ) -> Dict[str, Any]:
        """
        Create a new sniffer entry.
        
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

            anomaly (list[object]):
                Configuration method to edit Denial of Service (DoS) anomaly...
            application-list (string) (max_len: 47):
                Name of an existing application list.
            application-list-status (string) (enum: ['enable', 'disable']):
                Enable/disable application control profile.
            av-profile (string) (max_len: 47):
                Name of an existing antivirus profile.
            av-profile-status (string) (enum: ['enable', 'disable']):
                Enable/disable antivirus profile.
            dlp-profile (string) (max_len: 47):
                Name of an existing DLP profile.
            dlp-profile-status (string) (enum: ['enable', 'disable']):
                Enable/disable DLP profile.
            dsri (string) (enum: ['enable', 'disable']):
                Enable/disable DSRI.
            emailfilter-profile (string) (max_len: 47):
                Name of an existing email filter profile.
            emailfilter-profile-status (string) (enum: ['enable', 'disable']):
                Enable/disable emailfilter.
            file-filter-profile (string) (max_len: 47):
                Name of an existing file-filter profile.
            file-filter-profile-status (string) (enum: ['enable', 'disable']):
                Enable/disable file filter.
            host (string) (max_len: 63):
                Hosts to filter for in sniffer traffic (Format examples: 1.1...
            id (integer) (range: 0-9999):
                Sniffer ID (0 - 9999).
            interface (string) (max_len: 35):
                Interface name that traffic sniffing will take place on.
            ip-threatfeed (list[object]):
                Name of an existing IP threat feed.
            ip-threatfeed-status (string) (enum: ['enable', 'disable']):
                Enable/disable IP threat feed.
            ips-dos-status (string) (enum: ['enable', 'disable']):
                Enable/disable IPS DoS anomaly detection.
            ips-sensor (string) (max_len: 47):
                Name of an existing IPS sensor.
            ips-sensor-status (string) (enum: ['enable', 'disable']):
                Enable/disable IPS sensor.
            ipv6 (string) (enum: ['enable', 'disable']):
                Enable/disable sniffing IPv6 packets.
            logtraffic (string) (enum: ['all', 'utm', 'disable']):
                Either log all sessions, only sessions that have a security ...
            non-ip (string) (enum: ['enable', 'disable']):
                Enable/disable sniffing non-IP packets.
            port (string) (max_len: 63):
                Ports to sniff (Format examples: 10, :20, 30:40, 50-, 100-20...
            protocol (string) (max_len: 63):
                Integer value for the protocol type as defined by IANA (0 - ...
            status (string) (enum: ['enable', 'disable']):
                Enable/disable the active status of the sniffer.
            uuid (string):
                Universally Unique Identifier (UUID; automatically assigned ...
            vlan (string) (max_len: 63):
                List of VLANs to sniff.
            webfilter-profile (string) (max_len: 47):
                Name of an existing web filter profile.
            webfilter-profile-status (string) (enum: ['enable', 'disable']):
                Enable/disable web filter profile.
            
        Returns:
            API response dictionary
        """
        # Build data from kwargs if not provided
        if data is None:
            data = {}
        if anomaly is not None:
            data['anomaly'] = anomaly
        if application_list is not None:
            data['application-list'] = application_list
        if application_list_status is not None:
            data['application-list-status'] = application_list_status
        if av_profile is not None:
            data['av-profile'] = av_profile
        if av_profile_status is not None:
            data['av-profile-status'] = av_profile_status
        if dlp_profile is not None:
            data['dlp-profile'] = dlp_profile
        if dlp_profile_status is not None:
            data['dlp-profile-status'] = dlp_profile_status
        if dsri is not None:
            data['dsri'] = dsri
        if emailfilter_profile is not None:
            data['emailfilter-profile'] = emailfilter_profile
        if emailfilter_profile_status is not None:
            data['emailfilter-profile-status'] = emailfilter_profile_status
        if file_filter_profile is not None:
            data['file-filter-profile'] = file_filter_profile
        if file_filter_profile_status is not None:
            data['file-filter-profile-status'] = file_filter_profile_status
        if host is not None:
            data['host'] = host
        if id is not None:
            data['id'] = id
        if interface is not None:
            data['interface'] = interface
        if ip_threatfeed is not None:
            data['ip-threatfeed'] = ip_threatfeed
        if ip_threatfeed_status is not None:
            data['ip-threatfeed-status'] = ip_threatfeed_status
        if ips_dos_status is not None:
            data['ips-dos-status'] = ips_dos_status
        if ips_sensor is not None:
            data['ips-sensor'] = ips_sensor
        if ips_sensor_status is not None:
            data['ips-sensor-status'] = ips_sensor_status
        if ipv6 is not None:
            data['ipv6'] = ipv6
        if logtraffic is not None:
            data['logtraffic'] = logtraffic
        if non_ip is not None:
            data['non-ip'] = non_ip
        if port is not None:
            data['port'] = port
        if protocol is not None:
            data['protocol'] = protocol
        if status is not None:
            data['status'] = status
        if uuid is not None:
            data['uuid'] = uuid
        if vlan is not None:
            data['vlan'] = vlan
        if webfilter_profile is not None:
            data['webfilter-profile'] = webfilter_profile
        if webfilter_profile_status is not None:
            data['webfilter-profile-status'] = webfilter_profile_status
        
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
        anomaly: Optional[list] = None,
        application_list: Optional[str] = None,
        application_list_status: Optional[str] = None,
        av_profile: Optional[str] = None,
        av_profile_status: Optional[str] = None,
        dlp_profile: Optional[str] = None,
        dlp_profile_status: Optional[str] = None,
        dsri: Optional[str] = None,
        emailfilter_profile: Optional[str] = None,
        emailfilter_profile_status: Optional[str] = None,
        file_filter_profile: Optional[str] = None,
        file_filter_profile_status: Optional[str] = None,
        host: Optional[str] = None,
        id: Optional[int] = None,
        interface: Optional[str] = None,
        ip_threatfeed: Optional[list] = None,
        ip_threatfeed_status: Optional[str] = None,
        ips_dos_status: Optional[str] = None,
        ips_sensor: Optional[str] = None,
        ips_sensor_status: Optional[str] = None,
        ipv6: Optional[str] = None,
        logtraffic: Optional[str] = None,
        non_ip: Optional[str] = None,
        port: Optional[str] = None,
        protocol: Optional[str] = None,
        status: Optional[str] = None,
        uuid: Optional[str] = None,
        vlan: Optional[str] = None,
        webfilter_profile: Optional[str] = None,
        webfilter_profile_status: Optional[str] = None,
        **kwargs
    ) -> Dict[str, Any]:
        """
        Update an existing sniffer entry.
        
        Supports two usage patterns:
        1. Pass data dict: update(mkey=123, data={"key": "value"}, vdom="root")
        2. Pass kwargs: update(mkey=123, key="value", vdom="root")
        
        Args:
            mkey: The id (primary key)
            data: The updated configuration data (optional if using kwargs)
            vdom: Specify the Virtual Domain(s) from which results are returned or chang
            action: If supported, an action can be specified.
            before: If *action=move*, use *before* to specify the ID of the resource that 
            after: If *action=move*, use *after* to specify the ID of the resource that t
            scope: Specify the Scope from which results are returned or changes are appli
            **kwargs: Additional parameters

        Body schema properties (can pass via data dict or as kwargs):

            anomaly (list[object]):
                Configuration method to edit Denial of Service (DoS) anomaly...
            application-list (string) (max_len: 47):
                Name of an existing application list.
            application-list-status (string) (enum: ['enable', 'disable']):
                Enable/disable application control profile.
            av-profile (string) (max_len: 47):
                Name of an existing antivirus profile.
            av-profile-status (string) (enum: ['enable', 'disable']):
                Enable/disable antivirus profile.
            dlp-profile (string) (max_len: 47):
                Name of an existing DLP profile.
            dlp-profile-status (string) (enum: ['enable', 'disable']):
                Enable/disable DLP profile.
            dsri (string) (enum: ['enable', 'disable']):
                Enable/disable DSRI.
            emailfilter-profile (string) (max_len: 47):
                Name of an existing email filter profile.
            emailfilter-profile-status (string) (enum: ['enable', 'disable']):
                Enable/disable emailfilter.
            file-filter-profile (string) (max_len: 47):
                Name of an existing file-filter profile.
            file-filter-profile-status (string) (enum: ['enable', 'disable']):
                Enable/disable file filter.
            host (string) (max_len: 63):
                Hosts to filter for in sniffer traffic (Format examples: 1.1...
            id (integer) (range: 0-9999):
                Sniffer ID (0 - 9999).
            interface (string) (max_len: 35):
                Interface name that traffic sniffing will take place on.
            ip-threatfeed (list[object]):
                Name of an existing IP threat feed.
            ip-threatfeed-status (string) (enum: ['enable', 'disable']):
                Enable/disable IP threat feed.
            ips-dos-status (string) (enum: ['enable', 'disable']):
                Enable/disable IPS DoS anomaly detection.
            ips-sensor (string) (max_len: 47):
                Name of an existing IPS sensor.
            ips-sensor-status (string) (enum: ['enable', 'disable']):
                Enable/disable IPS sensor.
            ipv6 (string) (enum: ['enable', 'disable']):
                Enable/disable sniffing IPv6 packets.
            logtraffic (string) (enum: ['all', 'utm', 'disable']):
                Either log all sessions, only sessions that have a security ...
            non-ip (string) (enum: ['enable', 'disable']):
                Enable/disable sniffing non-IP packets.
            port (string) (max_len: 63):
                Ports to sniff (Format examples: 10, :20, 30:40, 50-, 100-20...
            protocol (string) (max_len: 63):
                Integer value for the protocol type as defined by IANA (0 - ...
            status (string) (enum: ['enable', 'disable']):
                Enable/disable the active status of the sniffer.
            uuid (string):
                Universally Unique Identifier (UUID; automatically assigned ...
            vlan (string) (max_len: 63):
                List of VLANs to sniff.
            webfilter-profile (string) (max_len: 47):
                Name of an existing web filter profile.
            webfilter-profile-status (string) (enum: ['enable', 'disable']):
                Enable/disable web filter profile.
            
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
        if anomaly is not None:
            data['anomaly'] = anomaly
        if application_list is not None:
            data['application-list'] = application_list
        if application_list_status is not None:
            data['application-list-status'] = application_list_status
        if av_profile is not None:
            data['av-profile'] = av_profile
        if av_profile_status is not None:
            data['av-profile-status'] = av_profile_status
        if dlp_profile is not None:
            data['dlp-profile'] = dlp_profile
        if dlp_profile_status is not None:
            data['dlp-profile-status'] = dlp_profile_status
        if dsri is not None:
            data['dsri'] = dsri
        if emailfilter_profile is not None:
            data['emailfilter-profile'] = emailfilter_profile
        if emailfilter_profile_status is not None:
            data['emailfilter-profile-status'] = emailfilter_profile_status
        if file_filter_profile is not None:
            data['file-filter-profile'] = file_filter_profile
        if file_filter_profile_status is not None:
            data['file-filter-profile-status'] = file_filter_profile_status
        if host is not None:
            data['host'] = host
        if id is not None:
            data['id'] = id
        if interface is not None:
            data['interface'] = interface
        if ip_threatfeed is not None:
            data['ip-threatfeed'] = ip_threatfeed
        if ip_threatfeed_status is not None:
            data['ip-threatfeed-status'] = ip_threatfeed_status
        if ips_dos_status is not None:
            data['ips-dos-status'] = ips_dos_status
        if ips_sensor is not None:
            data['ips-sensor'] = ips_sensor
        if ips_sensor_status is not None:
            data['ips-sensor-status'] = ips_sensor_status
        if ipv6 is not None:
            data['ipv6'] = ipv6
        if logtraffic is not None:
            data['logtraffic'] = logtraffic
        if non_ip is not None:
            data['non-ip'] = non_ip
        if port is not None:
            data['port'] = port
        if protocol is not None:
            data['protocol'] = protocol
        if status is not None:
            data['status'] = status
        if uuid is not None:
            data['uuid'] = uuid
        if vlan is not None:
            data['vlan'] = vlan
        if webfilter_profile is not None:
            data['webfilter-profile'] = webfilter_profile
        if webfilter_profile_status is not None:
            data['webfilter-profile-status'] = webfilter_profile_status
        
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
        Delete a sniffer entry.
        
        Args:
            mkey: The id (primary key)
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
