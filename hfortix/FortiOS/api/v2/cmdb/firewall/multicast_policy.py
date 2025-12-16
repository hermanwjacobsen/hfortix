"""
FortiOS multicast-policy API wrapper.
Provides access to /api/v2/cmdb/firewall/multicast-policy endpoint.
"""

from typing import Any, Dict, List, Optional, Union


class MulticastPolicy:
    """
    Wrapper for firewall multicast-policy API endpoint.
    
    Manages multicast-policy configuration with full Swagger-spec parameter support.
    """
    
    def __init__(self, http_client: Any):
        """
        Initialize the MulticastPolicy wrapper.
        
        Args:
            http_client: The HTTP client for API communication
        """
        self._client = http_client
        self.path = 'firewall/multicast-policy'
    
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
        Retrieve a list of all multicast-policy entries.
        
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
        Retrieve a specific multicast-policy entry by its id.
        
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
        auto_asic_offload: Optional[str] = None,
        comments: Optional[str] = None,
        dnat: Optional[str] = None,
        dstaddr: Optional[list] = None,
        dstintf: Optional[str] = None,
        end_port: Optional[int] = None,
        id: Optional[int] = None,
        ips_sensor: Optional[str] = None,
        logtraffic: Optional[str] = None,
        name: Optional[str] = None,
        protocol: Optional[int] = None,
        snat: Optional[str] = None,
        snat_ip: Optional[str] = None,
        srcaddr: Optional[list] = None,
        srcintf: Optional[str] = None,
        start_port: Optional[int] = None,
        status: Optional[str] = None,
        traffic_shaper: Optional[str] = None,
        utm_status: Optional[str] = None,
        uuid: Optional[str] = None,
        **kwargs
    ) -> Dict[str, Any]:
        """
        Create a new multicast-policy entry.
        
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
                Accept or deny traffic matching the policy.
            auto-asic-offload (string) (enum: ['enable', 'disable']):
                Enable/disable offloading policy traffic for hardware accele...
            comments (string) (max_len: 1023):
                Comment.
            dnat (string):
                IPv4 DNAT address used for multicast destination addresses.
            dstaddr (list[object]):
                Destination address objects.
            dstintf (string) (max_len: 35):
                Destination interface name.
            end-port (integer) (range: 0-65535):
                Integer value for ending TCP/UDP/SCTP destination port in ra...
            id (integer) (range: 0-4294967294):
                Policy ID ((0 - 4294967294).
            ips-sensor (string) (max_len: 47):
                Name of an existing IPS sensor.
            logtraffic (string) (enum: ['all', 'utm', 'disable']):
                Enable or disable logging. Log all sessions or security prof...
            name (string) (max_len: 35):
                Policy name.
            protocol (integer) (range: 0-255):
                Integer value for the protocol type as defined by IANA (0 - ...
            snat (string) (enum: ['enable', 'disable']):
                Enable/disable substitution of the outgoing interface IP add...
            snat-ip (string):
                IPv4 address to be used as the source address for NATed traf...
            srcaddr (list[object]):
                Source address objects.
            srcintf (string) (max_len: 35):
                Source interface name.
            start-port (integer) (range: 0-65535):
                Integer value for starting TCP/UDP/SCTP destination port in ...
            status (string) (enum: ['enable', 'disable']):
                Enable/disable this policy.
            traffic-shaper (string) (max_len: 35):
                Traffic shaper to apply to traffic forwarded by the multicas...
            utm-status (string) (enum: ['enable', 'disable']):
                Enable to add an IPS security profile to the policy.
            uuid (string):
                Universally Unique Identifier (UUID; automatically assigned ...
            
        Returns:
            API response dictionary
        """
        # Build data from kwargs if not provided
        if data is None:
            data = {}
        if action is not None:
            data['action'] = action
        if auto_asic_offload is not None:
            data['auto-asic-offload'] = auto_asic_offload
        if comments is not None:
            data['comments'] = comments
        if dnat is not None:
            data['dnat'] = dnat
        if dstaddr is not None:
            data['dstaddr'] = dstaddr
        if dstintf is not None:
            data['dstintf'] = dstintf
        if end_port is not None:
            data['end-port'] = end_port
        if id is not None:
            data['id'] = id
        if ips_sensor is not None:
            data['ips-sensor'] = ips_sensor
        if logtraffic is not None:
            data['logtraffic'] = logtraffic
        if name is not None:
            data['name'] = name
        if protocol is not None:
            data['protocol'] = protocol
        if snat is not None:
            data['snat'] = snat
        if snat_ip is not None:
            data['snat-ip'] = snat_ip
        if srcaddr is not None:
            data['srcaddr'] = srcaddr
        if srcintf is not None:
            data['srcintf'] = srcintf
        if start_port is not None:
            data['start-port'] = start_port
        if status is not None:
            data['status'] = status
        if traffic_shaper is not None:
            data['traffic-shaper'] = traffic_shaper
        if utm_status is not None:
            data['utm-status'] = utm_status
        if uuid is not None:
            data['uuid'] = uuid
        
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
        auto_asic_offload: Optional[str] = None,
        comments: Optional[str] = None,
        dnat: Optional[str] = None,
        dstaddr: Optional[list] = None,
        dstintf: Optional[str] = None,
        end_port: Optional[int] = None,
        id: Optional[int] = None,
        ips_sensor: Optional[str] = None,
        logtraffic: Optional[str] = None,
        name: Optional[str] = None,
        protocol: Optional[int] = None,
        snat: Optional[str] = None,
        snat_ip: Optional[str] = None,
        srcaddr: Optional[list] = None,
        srcintf: Optional[str] = None,
        start_port: Optional[int] = None,
        status: Optional[str] = None,
        traffic_shaper: Optional[str] = None,
        utm_status: Optional[str] = None,
        uuid: Optional[str] = None,
        **kwargs
    ) -> Dict[str, Any]:
        """
        Update an existing multicast-policy entry.
        
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

            action (string) (enum: ['accept', 'deny']):
                Accept or deny traffic matching the policy.
            auto-asic-offload (string) (enum: ['enable', 'disable']):
                Enable/disable offloading policy traffic for hardware accele...
            comments (string) (max_len: 1023):
                Comment.
            dnat (string):
                IPv4 DNAT address used for multicast destination addresses.
            dstaddr (list[object]):
                Destination address objects.
            dstintf (string) (max_len: 35):
                Destination interface name.
            end-port (integer) (range: 0-65535):
                Integer value for ending TCP/UDP/SCTP destination port in ra...
            id (integer) (range: 0-4294967294):
                Policy ID ((0 - 4294967294).
            ips-sensor (string) (max_len: 47):
                Name of an existing IPS sensor.
            logtraffic (string) (enum: ['all', 'utm', 'disable']):
                Enable or disable logging. Log all sessions or security prof...
            name (string) (max_len: 35):
                Policy name.
            protocol (integer) (range: 0-255):
                Integer value for the protocol type as defined by IANA (0 - ...
            snat (string) (enum: ['enable', 'disable']):
                Enable/disable substitution of the outgoing interface IP add...
            snat-ip (string):
                IPv4 address to be used as the source address for NATed traf...
            srcaddr (list[object]):
                Source address objects.
            srcintf (string) (max_len: 35):
                Source interface name.
            start-port (integer) (range: 0-65535):
                Integer value for starting TCP/UDP/SCTP destination port in ...
            status (string) (enum: ['enable', 'disable']):
                Enable/disable this policy.
            traffic-shaper (string) (max_len: 35):
                Traffic shaper to apply to traffic forwarded by the multicas...
            utm-status (string) (enum: ['enable', 'disable']):
                Enable to add an IPS security profile to the policy.
            uuid (string):
                Universally Unique Identifier (UUID; automatically assigned ...
            
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
        if auto_asic_offload is not None:
            data['auto-asic-offload'] = auto_asic_offload
        if comments is not None:
            data['comments'] = comments
        if dnat is not None:
            data['dnat'] = dnat
        if dstaddr is not None:
            data['dstaddr'] = dstaddr
        if dstintf is not None:
            data['dstintf'] = dstintf
        if end_port is not None:
            data['end-port'] = end_port
        if id is not None:
            data['id'] = id
        if ips_sensor is not None:
            data['ips-sensor'] = ips_sensor
        if logtraffic is not None:
            data['logtraffic'] = logtraffic
        if name is not None:
            data['name'] = name
        if protocol is not None:
            data['protocol'] = protocol
        if snat is not None:
            data['snat'] = snat
        if snat_ip is not None:
            data['snat-ip'] = snat_ip
        if srcaddr is not None:
            data['srcaddr'] = srcaddr
        if srcintf is not None:
            data['srcintf'] = srcintf
        if start_port is not None:
            data['start-port'] = start_port
        if status is not None:
            data['status'] = status
        if traffic_shaper is not None:
            data['traffic-shaper'] = traffic_shaper
        if utm_status is not None:
            data['utm-status'] = utm_status
        if uuid is not None:
            data['uuid'] = uuid
        
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
        Delete a multicast-policy entry.
        
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
