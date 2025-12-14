"""
FortiOS CMDB - Firewall Shared Traffic Shaper
Configure shared traffic shaper.

API Endpoints:
    GET    /api/v2/cmdb/firewall.shaper/traffic-shaper       - List all traffic shapers
    GET    /api/v2/cmdb/firewall.shaper/traffic-shaper/{id}  - Get specific traffic shaper
    POST   /api/v2/cmdb/firewall.shaper/traffic-shaper       - Create traffic shaper
    PUT    /api/v2/cmdb/firewall.shaper/traffic-shaper/{id}  - Update traffic shaper
    DELETE /api/v2/cmdb/firewall.shaper/traffic-shaper/{id}  - Delete traffic shaper
"""

from typing import Optional, Union, List


class TrafficShaper:
    """Shared traffic shaper endpoint"""
    
    def __init__(self, client):
        self._client = client
    
    def list(
        self,
        filter: Optional[str] = None,
        range: Optional[str] = None,
        sort: Optional[str] = None,
        format: Optional[List[str]] = None,
        vdom: Optional[Union[str, bool]] = None,
        **kwargs
    ):
        """
        List all shared traffic shapers.
        
        Args:
            filter: Filter results
            range: Range of results (e.g., '0-50')
            sort: Sort results
            format: List of fields to include in response
            vdom: Virtual domain
            **kwargs: Additional parameters
        
        Returns:
            API response dictionary
        
        Examples:
            >>> # List all traffic shapers
            >>> result = fgt.cmdb.firewall.shaper.traffic_shaper.list()
            
            >>> # List with specific fields
            >>> result = fgt.cmdb.firewall.shaper.traffic_shaper.list(
            ...     format=['name', 'guaranteed-bandwidth', 'maximum-bandwidth']
            ... )
        """
        return self.get(
            filter=filter,
            range=range,
            sort=sort,
            format=format,
            vdom=vdom,
            **kwargs
        )
    
    def get(
        self,
        name: Optional[str] = None,
        filter: Optional[str] = None,
        range: Optional[str] = None,
        sort: Optional[str] = None,
        format: Optional[List[str]] = None,
        vdom: Optional[Union[str, bool]] = None,
        **kwargs
    ):
        """
        Get shared traffic shaper(s).
        
        Args:
            name: Traffic shaper name (if retrieving specific shaper)
            filter: Filter results
            range: Range of results
            sort: Sort results
            format: List of fields to include
            vdom: Virtual domain
            **kwargs: Additional parameters
        
        Returns:
            API response dictionary
        
        Examples:
            >>> # Get specific traffic shaper
            >>> result = fgt.cmdb.firewall.shaper.traffic_shaper.get('high-priority')
            
            >>> # Get all traffic shapers
            >>> result = fgt.cmdb.firewall.shaper.traffic_shaper.get()
        """
        path = 'firewall.shaper/traffic-shaper'
        if name:
            path = f'{path}/{name}'
        
        params = {}
        param_map = {
            'filter': filter,
            'range': range,
            'sort': sort,
            'format': format,
        }
        for key, value in param_map.items():
            if value is not None:
                params[key] = value
        params.update(kwargs)
        
        return self._client.get('cmdb', path, params=params if params else None, vdom=vdom)
    
    def create(
        self,
        name: str,
        guaranteed_bandwidth: Optional[int] = None,
        maximum_bandwidth: Optional[int] = None,
        bandwidth_unit: Optional[str] = None,
        priority: Optional[str] = None,
        per_policy: Optional[str] = None,
        diffserv: Optional[str] = None,
        diffservcode: Optional[str] = None,
        dscp_marking_method: Optional[str] = None,
        exceed_bandwidth: Optional[int] = None,
        exceed_dscp: Optional[str] = None,
        maximum_dscp: Optional[str] = None,
        overhead: Optional[int] = None,
        exceed_class_id: Optional[int] = None,
        comment: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        **kwargs
    ):
        """
        Create a shared traffic shaper.
        
        Args:
            name: Traffic shaper name (max 35 chars)
            guaranteed_bandwidth: Guaranteed bandwidth (0-16776000)
            maximum_bandwidth: Maximum bandwidth (0-16776000)
            bandwidth_unit: Bandwidth unit - 'kbps' or 'mbps'
            priority: Priority - 'low', 'medium', 'high', 'top'
            per_policy: Apply per-policy shaper - 'disable' or 'enable'
            diffserv: Enable/disable DSCP marking - 'disable' or 'enable'
            diffservcode: DSCP code point (000000-111111)
            dscp_marking_method: DSCP marking method - 'multi-stage', 'static'
            exceed_bandwidth: Exceed bandwidth (0-16776000)
            exceed_dscp: Exceed DSCP (000000-111111)
            maximum_dscp: Maximum DSCP (000000-111111)
            overhead: Per-packet overhead (0-100 bytes)
            exceed_class_id: Exceed class ID (0-31)
            comment: Comment (max 1023 chars)
            vdom: Virtual domain
            **kwargs: Additional parameters
        
        Returns:
            API response dictionary
        
        Examples:
            >>> # Create basic traffic shaper
            >>> result = fgt.cmdb.firewall.shaper.traffic_shaper.create(
            ...     'web-traffic',
            ...     guaranteed_bandwidth=5120,
            ...     maximum_bandwidth=10240,
            ...     bandwidth_unit='kbps',
            ...     priority='high',
            ...     comment='Web traffic shaper'
            ... )
            
            >>> # Create traffic shaper with DSCP marking
            >>> result = fgt.cmdb.firewall.shaper.traffic_shaper.create(
            ...     'voip-traffic',
            ...     guaranteed_bandwidth=2048,
            ...     maximum_bandwidth=4096,
            ...     bandwidth_unit='kbps',
            ...     priority='top',
            ...     diffserv='enable',
            ...     diffservcode='101110'
            ... )
        """
        data = {'name': name}
        
        param_map = {
            'guaranteed_bandwidth': guaranteed_bandwidth,
            'maximum_bandwidth': maximum_bandwidth,
            'bandwidth_unit': bandwidth_unit,
            'priority': priority,
            'per_policy': per_policy,
            'diffserv': diffserv,
            'diffservcode': diffservcode,
            'dscp_marking_method': dscp_marking_method,
            'exceed_bandwidth': exceed_bandwidth,
            'exceed_dscp': exceed_dscp,
            'maximum_dscp': maximum_dscp,
            'overhead': overhead,
            'exceed_class_id': exceed_class_id,
            'comment': comment,
        }
        
        api_field_map = {
            'guaranteed_bandwidth': 'guaranteed-bandwidth',
            'maximum_bandwidth': 'maximum-bandwidth',
            'bandwidth_unit': 'bandwidth-unit',
            'priority': 'priority',
            'per_policy': 'per-policy',
            'diffserv': 'diffserv',
            'diffservcode': 'diffservcode',
            'dscp_marking_method': 'dscp-marking-method',
            'exceed_bandwidth': 'exceed-bandwidth',
            'exceed_dscp': 'exceed-dscp',
            'maximum_dscp': 'maximum-dscp',
            'overhead': 'overhead',
            'exceed_class_id': 'exceed-class-id',
            'comment': 'comment',
        }
        
        for param_name, value in param_map.items():
            if value is not None:
                api_name = api_field_map[param_name]
                data[api_name] = value
        data.update(kwargs)
        
        return self._client.post('cmdb', 'firewall.shaper/traffic-shaper', data, vdom=vdom)
    
    def update(
        self,
        name: str,
        guaranteed_bandwidth: Optional[int] = None,
        maximum_bandwidth: Optional[int] = None,
        bandwidth_unit: Optional[str] = None,
        priority: Optional[str] = None,
        per_policy: Optional[str] = None,
        diffserv: Optional[str] = None,
        diffservcode: Optional[str] = None,
        dscp_marking_method: Optional[str] = None,
        exceed_bandwidth: Optional[int] = None,
        exceed_dscp: Optional[str] = None,
        maximum_dscp: Optional[str] = None,
        overhead: Optional[int] = None,
        exceed_class_id: Optional[int] = None,
        comment: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        **kwargs
    ):
        """
        Update a shared traffic shaper.
        
        Args:
            name: Traffic shaper name
            guaranteed_bandwidth: Guaranteed bandwidth (0-16776000)
            maximum_bandwidth: Maximum bandwidth (0-16776000)
            bandwidth_unit: Bandwidth unit - 'kbps' or 'mbps'
            priority: Priority - 'low', 'medium', 'high', 'top'
            per_policy: Apply per-policy shaper - 'disable' or 'enable'
            diffserv: Enable/disable DSCP marking - 'disable' or 'enable'
            diffservcode: DSCP code point (000000-111111)
            dscp_marking_method: DSCP marking method - 'multi-stage', 'static'
            exceed_bandwidth: Exceed bandwidth (0-16776000)
            exceed_dscp: Exceed DSCP (000000-111111)
            maximum_dscp: Maximum DSCP (000000-111111)
            overhead: Per-packet overhead (0-100 bytes)
            overhead: Per-packet overhead (0-100 bytes)
            exceed_class_id: Exceed class ID (0-31)
            comment: Comment (max 1023 chars)
            vdom: Virtual domain
            **kwargs: Additional parameters
        
        Returns:
            API response dictionary
        
        Examples:
            >>> # Update bandwidth limits
            >>> result = fgt.cmdb.firewall.shaper.traffic_shaper.update(
            ...     'web-traffic',
            ...     guaranteed_bandwidth=10240,
            ...     maximum_bandwidth=20480
            ... )
            
            >>> # Update priority
            >>> result = fgt.cmdb.firewall.shaper.traffic_shaper.update(
            ...     'voip-traffic',
            ...     priority='top'
            ... )
        """
        data = {}
        
        param_map = {
            'guaranteed_bandwidth': guaranteed_bandwidth,
            'maximum_bandwidth': maximum_bandwidth,
            'bandwidth_unit': bandwidth_unit,
            'priority': priority,
            'per_policy': per_policy,
            'diffserv': diffserv,
            'diffservcode': diffservcode,
            'dscp_marking_method': dscp_marking_method,
            'exceed_bandwidth': exceed_bandwidth,
            'exceed_dscp': exceed_dscp,
            'maximum_dscp': maximum_dscp,
            'overhead': overhead,
            'exceed_class_id': exceed_class_id,
            'comment': comment,
        }
        
        api_field_map = {
            'guaranteed_bandwidth': 'guaranteed-bandwidth',
            'maximum_bandwidth': 'maximum-bandwidth',
            'bandwidth_unit': 'bandwidth-unit',
            'priority': 'priority',
            'per_policy': 'per-policy',
            'diffserv': 'diffserv',
            'diffservcode': 'diffservcode',
            'dscp_marking_method': 'dscp-marking-method',
            'exceed_bandwidth': 'exceed-bandwidth',
            'exceed_dscp': 'exceed-dscp',
            'maximum_dscp': 'maximum-dscp',
            'overhead': 'overhead',
            'exceed_class_id': 'exceed-class-id',
            'comment': 'comment',
        }
        
        for param_name, value in param_map.items():
            if value is not None:
                api_name = api_field_map[param_name]
                data[api_name] = value
        data.update(kwargs)
        
        return self._client.put('cmdb', f'firewall.shaper/traffic-shaper/{name}', data, vdom=vdom)
    
    def delete(
        self,
        name: str,
        vdom: Optional[Union[str, bool]] = None
    ):
        """
        Delete a shared traffic shaper.
        
        Args:
            name: Traffic shaper name
            vdom: Virtual domain
        
        Returns:
            API response dictionary
        
        Examples:
            >>> # Delete traffic shaper
            >>> result = fgt.cmdb.firewall.shaper.traffic_shaper.delete('web-traffic')
        """
        return self._client.delete('cmdb', f'firewall.shaper/traffic-shaper/{name}', vdom=vdom)
    
    def exists(
        self,
        name: str,
        vdom: Optional[Union[str, bool]] = None
    ) -> bool:
        """
        Check if traffic shaper exists.
        
        Args:
            name: Traffic shaper name
            vdom: Virtual domain
        
        Returns:
            True if traffic shaper exists, False otherwise
        
        Examples:
            >>> if fgt.cmdb.firewall.shaper.traffic_shaper.exists('web-traffic'):
            ...     print("Traffic shaper exists")
        """
        try:
            result = self.get(name, vdom=vdom)
            return (
                result.get('status') == 'success' and
                result.get('http_status') == 200 and
                len(result.get('results', [])) > 0
            )
        except Exception:
            return False
