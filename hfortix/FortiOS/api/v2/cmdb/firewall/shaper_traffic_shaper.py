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

from typing import Dict, Optional, Union, List, Any

from .....http_client import HTTPResponse


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
    ) -> HTTPResponse:
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
    ) -> HTTPResponse:
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
        data: Optional[Dict[str, Any]] = None,
        name: Optional[str] = None,
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
    ) -> HTTPResponse:
        """
        Create a shared traffic shaper.
        
        
        Supports two usage patterns:
        1. Pass data dict: create(data={'key': 'value'}, vdom='root')
        2. Pass kwargs: create(key='value', vdom='root')
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
        # Pattern 1: data dict provided
        if data is not None:
            # Use provided data dict
            pass
        # Pattern 2: kwargs pattern - build data dict
        else:
            data = {}
            if name is not None:
                data['name'] = name
            if guaranteed_bandwidth is not None:
                data['guaranteed-bandwidth'] = guaranteed_bandwidth
            if maximum_bandwidth is not None:
                data['maximum-bandwidth'] = maximum_bandwidth
            if bandwidth_unit is not None:
                data['bandwidth-unit'] = bandwidth_unit
            if priority is not None:
                data['priority'] = priority
            if per_policy is not None:
                data['per-policy'] = per_policy
            if diffserv is not None:
                data['diffserv'] = diffserv
            if diffservcode is not None:
                data['diffservcode'] = diffservcode
            if dscp_marking_method is not None:
                data['dscp-marking-method'] = dscp_marking_method
            if exceed_bandwidth is not None:
                data['exceed-bandwidth'] = exceed_bandwidth
            if exceed_dscp is not None:
                data['exceed-dscp'] = exceed_dscp
            if maximum_dscp is not None:
                data['maximum-dscp'] = maximum_dscp
            if overhead is not None:
                data['overhead'] = overhead
            if exceed_class_id is not None:
                data['exceed-class-id'] = exceed_class_id
            if comment is not None:
                data['comment'] = comment
        
        return self._client.post('cmdb', 'firewall.shaper/traffic-shaper', data, vdom=vdom)
    def update(
        self,
        name: str,
        data: Optional[Dict[str, Any]] = None,
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
    ) -> HTTPResponse:
        """
        Update a shared traffic shaper.
        
        
        Supports two usage patterns:
        1. Pass data dict: update(data={'key': 'value'}, vdom='root')
        2. Pass kwargs: update(key='value', vdom='root')
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
        # Pattern 1: data dict provided
        if data is not None:
            # Use provided data dict
            pass
        # Pattern 2: kwargs pattern - build data dict
        else:
            data = {}
            if guaranteed_bandwidth is not None:
                data['guaranteed-bandwidth'] = guaranteed_bandwidth
            if maximum_bandwidth is not None:
                data['maximum-bandwidth'] = maximum_bandwidth
            if bandwidth_unit is not None:
                data['bandwidth-unit'] = bandwidth_unit
            if priority is not None:
                data['priority'] = priority
            if per_policy is not None:
                data['per-policy'] = per_policy
            if diffserv is not None:
                data['diffserv'] = diffserv
            if diffservcode is not None:
                data['diffservcode'] = diffservcode
            if dscp_marking_method is not None:
                data['dscp-marking-method'] = dscp_marking_method
            if exceed_bandwidth is not None:
                data['exceed-bandwidth'] = exceed_bandwidth
            if exceed_dscp is not None:
                data['exceed-dscp'] = exceed_dscp
            if maximum_dscp is not None:
                data['maximum-dscp'] = maximum_dscp
            if overhead is not None:
                data['overhead'] = overhead
            if exceed_class_id is not None:
                data['exceed-class-id'] = exceed_class_id
            if comment is not None:
                data['comment'] = comment
        
        return self._client.put('cmdb', f'firewall.shaper/traffic-shaper/{name}', data, vdom=vdom)
    
    def delete(
        self,
        name: str,
        vdom: Optional[Union[str, bool]] = None
    ) -> HTTPResponse:
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
