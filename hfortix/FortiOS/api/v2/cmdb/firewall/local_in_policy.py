"""
FortiOS local-in-policy API wrapper.
Provides access to /api/v2/cmdb/firewall/local-in-policy endpoint.
"""

from typing import Any, Dict, List, Optional, Union


class LocalInPolicy:
    """
    Wrapper for firewall local-in-policy API endpoint.
    
    Manages local-in-policy configuration with full Swagger-spec parameter support.
    """
    
    def __init__(self, http_client: Any):
        """
        Initialize the LocalInPolicy wrapper.
        
        Args:
            http_client: The HTTP client for API communication
        """
        self._client = http_client
        self.path = 'firewall/local-in-policy'
    
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
        Retrieve a list of all local-in-policy entries.
        
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
        Retrieve a specific local-in-policy entry by its policyid.
        
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
        comments: Optional[str] = None,
        dstaddr: Optional[list] = None,
        dstaddr_negate: Optional[str] = None,
        ha_mgmt_intf_only: Optional[str] = None,
        internet_service_src: Optional[str] = None,
        internet_service_src_custom: Optional[list] = None,
        internet_service_src_custom_group: Optional[list] = None,
        internet_service_src_fortiguard: Optional[list] = None,
        internet_service_src_group: Optional[list] = None,
        internet_service_src_name: Optional[list] = None,
        internet_service_src_negate: Optional[str] = None,
        intf: Optional[list] = None,
        logtraffic: Optional[str] = None,
        policyid: Optional[int] = None,
        schedule: Optional[str] = None,
        service: Optional[list] = None,
        service_negate: Optional[str] = None,
        srcaddr: Optional[list] = None,
        srcaddr_negate: Optional[str] = None,
        status: Optional[str] = None,
        uuid: Optional[str] = None,
        virtual_patch: Optional[str] = None,
        **kwargs
    ) -> Dict[str, Any]:
        """
        Create a new local-in-policy entry.
        
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
                Action performed on traffic matching the policy (default = d...
            comments (string) (max_len: 1023):
                Comment.
            dstaddr (list[object]):
                Destination address object from available options.
            dstaddr-negate (string) (enum: ['enable', 'disable']):
                When enabled dstaddr specifies what the destination address ...
            ha-mgmt-intf-only (string) (enum: ['enable', 'disable']):
                Enable/disable dedicating the HA management interface only f...
            internet-service-src (string) (enum: ['enable', 'disable']):
                Enable/disable use of Internet Services in source for this l...
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
            intf (list[object]):
                Incoming interface name from available options.
            logtraffic (string) (enum: ['enable', 'disable']):
                Enable/disable local-in traffic logging.
            policyid (integer) (range: 0-4294967295):
                User defined local in policy ID.
            schedule (string) (max_len: 35):
                Schedule object from available options.
            service (list[object]):
                Service object from available options.
            service-negate (string) (enum: ['enable', 'disable']):
                When enabled service specifies what the service must NOT be.
            srcaddr (list[object]):
                Source address object from available options.
            srcaddr-negate (string) (enum: ['enable', 'disable']):
                When enabled srcaddr specifies what the source address must ...
            status (string) (enum: ['enable', 'disable']):
                Enable/disable this local-in policy.
            uuid (string):
                Universally Unique Identifier (UUID; automatically assigned ...
            virtual-patch (string) (enum: ['enable', 'disable']):
                Enable/disable virtual patching.
            
        Returns:
            API response dictionary
        """
        # Build data from kwargs if not provided
        if data is None:
            data = {}
        if action is not None:
            data['action'] = action
        if comments is not None:
            data['comments'] = comments
        if dstaddr is not None:
            data['dstaddr'] = dstaddr
        if dstaddr_negate is not None:
            data['dstaddr-negate'] = dstaddr_negate
        if ha_mgmt_intf_only is not None:
            data['ha-mgmt-intf-only'] = ha_mgmt_intf_only
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
        if intf is not None:
            data['intf'] = intf
        if logtraffic is not None:
            data['logtraffic'] = logtraffic
        if policyid is not None:
            data['policyid'] = policyid
        if schedule is not None:
            data['schedule'] = schedule
        if service is not None:
            data['service'] = service
        if service_negate is not None:
            data['service-negate'] = service_negate
        if srcaddr is not None:
            data['srcaddr'] = srcaddr
        if srcaddr_negate is not None:
            data['srcaddr-negate'] = srcaddr_negate
        if status is not None:
            data['status'] = status
        if uuid is not None:
            data['uuid'] = uuid
        if virtual_patch is not None:
            data['virtual-patch'] = virtual_patch
        
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
        comments: Optional[str] = None,
        dstaddr: Optional[list] = None,
        dstaddr_negate: Optional[str] = None,
        ha_mgmt_intf_only: Optional[str] = None,
        internet_service_src: Optional[str] = None,
        internet_service_src_custom: Optional[list] = None,
        internet_service_src_custom_group: Optional[list] = None,
        internet_service_src_fortiguard: Optional[list] = None,
        internet_service_src_group: Optional[list] = None,
        internet_service_src_name: Optional[list] = None,
        internet_service_src_negate: Optional[str] = None,
        intf: Optional[list] = None,
        logtraffic: Optional[str] = None,
        policyid: Optional[int] = None,
        schedule: Optional[str] = None,
        service: Optional[list] = None,
        service_negate: Optional[str] = None,
        srcaddr: Optional[list] = None,
        srcaddr_negate: Optional[str] = None,
        status: Optional[str] = None,
        uuid: Optional[str] = None,
        virtual_patch: Optional[str] = None,
        **kwargs
    ) -> Dict[str, Any]:
        """
        Update an existing local-in-policy entry.
        
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
                Action performed on traffic matching the policy (default = d...
            comments (string) (max_len: 1023):
                Comment.
            dstaddr (list[object]):
                Destination address object from available options.
            dstaddr-negate (string) (enum: ['enable', 'disable']):
                When enabled dstaddr specifies what the destination address ...
            ha-mgmt-intf-only (string) (enum: ['enable', 'disable']):
                Enable/disable dedicating the HA management interface only f...
            internet-service-src (string) (enum: ['enable', 'disable']):
                Enable/disable use of Internet Services in source for this l...
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
            intf (list[object]):
                Incoming interface name from available options.
            logtraffic (string) (enum: ['enable', 'disable']):
                Enable/disable local-in traffic logging.
            policyid (integer) (range: 0-4294967295):
                User defined local in policy ID.
            schedule (string) (max_len: 35):
                Schedule object from available options.
            service (list[object]):
                Service object from available options.
            service-negate (string) (enum: ['enable', 'disable']):
                When enabled service specifies what the service must NOT be.
            srcaddr (list[object]):
                Source address object from available options.
            srcaddr-negate (string) (enum: ['enable', 'disable']):
                When enabled srcaddr specifies what the source address must ...
            status (string) (enum: ['enable', 'disable']):
                Enable/disable this local-in policy.
            uuid (string):
                Universally Unique Identifier (UUID; automatically assigned ...
            virtual-patch (string) (enum: ['enable', 'disable']):
                Enable/disable virtual patching.
            
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
        if comments is not None:
            data['comments'] = comments
        if dstaddr is not None:
            data['dstaddr'] = dstaddr
        if dstaddr_negate is not None:
            data['dstaddr-negate'] = dstaddr_negate
        if ha_mgmt_intf_only is not None:
            data['ha-mgmt-intf-only'] = ha_mgmt_intf_only
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
        if intf is not None:
            data['intf'] = intf
        if logtraffic is not None:
            data['logtraffic'] = logtraffic
        if policyid is not None:
            data['policyid'] = policyid
        if schedule is not None:
            data['schedule'] = schedule
        if service is not None:
            data['service'] = service
        if service_negate is not None:
            data['service-negate'] = service_negate
        if srcaddr is not None:
            data['srcaddr'] = srcaddr
        if srcaddr_negate is not None:
            data['srcaddr-negate'] = srcaddr_negate
        if status is not None:
            data['status'] = status
        if uuid is not None:
            data['uuid'] = uuid
        if virtual_patch is not None:
            data['virtual-patch'] = virtual_patch
        
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
        Delete a local-in-policy entry.
        
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
