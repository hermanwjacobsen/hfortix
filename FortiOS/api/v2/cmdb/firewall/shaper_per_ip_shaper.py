"""
FortiOS CMDB - Firewall Per-IP Traffic Shaper
Configure per-IP traffic shaper.

API Endpoints:
    GET    /api/v2/cmdb/firewall.shaper/per-ip-shaper       - List all per-IP shapers
    GET    /api/v2/cmdb/firewall.shaper/per-ip-shaper/{id}  - Get specific per-IP shaper
    POST   /api/v2/cmdb/firewall.shaper/per-ip-shaper       - Create per-IP shaper
    PUT    /api/v2/cmdb/firewall.shaper/per-ip-shaper/{id}  - Update per-IP shaper
    DELETE /api/v2/cmdb/firewall.shaper/per-ip-shaper/{id}  - Delete per-IP shaper
"""

from typing import Optional, Union, List


class PerIpShaper:
    """Per-IP traffic shaper endpoint"""
    
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
        List all per-IP traffic shapers.
        
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
            >>> # List all per-IP shapers
            >>> result = fgt.cmdb.firewall.shaper.per_ip_shaper.list()
            
            >>> # List with specific fields
            >>> result = fgt.cmdb.firewall.shaper.per_ip_shaper.list(
            ...     format=['name', 'max-bandwidth', 'max-concurrent-session']
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
        Get per-IP traffic shaper(s).
        
        Args:
            name: Per-IP shaper name (if retrieving specific shaper)
            filter: Filter results
            range: Range of results
            sort: Sort results
            format: List of fields to include
            vdom: Virtual domain
            **kwargs: Additional parameters
        
        Returns:
            API response dictionary
        
        Examples:
            >>> # Get specific per-IP shaper
            >>> result = fgt.cmdb.firewall.shaper.per_ip_shaper.get('high-priority')
            
            >>> # Get all per-IP shapers
            >>> result = fgt.cmdb.firewall.shaper.per_ip_shaper.get()
        """
        path = 'firewall.shaper/per-ip-shaper'
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
        max_bandwidth: Optional[int] = None,
        max_concurrent_session: Optional[int] = None,
        max_concurrent_tcp_session: Optional[int] = None,
        max_concurrent_udp_session: Optional[int] = None,
        comment: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        **kwargs
    ) -> HTTPResponse:
        """
        Create a per-IP traffic shaper.
        
        Args:
            name: Per-IP shaper name (max 35 chars)
            max_bandwidth: Upper bandwidth limit (0-16776000 kbps, 0 = unlimited)
            max_concurrent_session: Maximum concurrent sessions (0-2097000, 0 = unlimited)
            max_concurrent_tcp_session: Maximum concurrent TCP sessions (0-2097000, 0 = unlimited)
            max_concurrent_udp_session: Maximum concurrent UDP sessions (0-2097000, 0 = unlimited)
            comment: Comment (max 1023 chars)
            vdom: Virtual domain
            **kwargs: Additional parameters
        
        Returns:
            API response dictionary
        
        Examples:
            >>> # Create per-IP shaper with bandwidth limit
            >>> result = fgt.cmdb.firewall.shaper.per_ip_shaper.create(
            ...     'user-limit',
            ...     max_bandwidth=10240,
            ...     max_concurrent_session=100,
            ...     comment='Per-user bandwidth limit'
            ... )
            
            >>> # Create per-IP shaper with TCP/UDP session limits
            >>> result = fgt.cmdb.firewall.shaper.per_ip_shaper.create(
            ...     'session-limit',
            ...     max_concurrent_tcp_session=50,
            ...     max_concurrent_udp_session=30
            ... )
        """
        data = {'name': name}
        
        param_map = {
            'max_bandwidth': max_bandwidth,
            'max_concurrent_session': max_concurrent_session,
            'max_concurrent_tcp_session': max_concurrent_tcp_session,
            'max_concurrent_udp_session': max_concurrent_udp_session,
            'comment': comment,
        }
        
        api_field_map = {
            'max_bandwidth': 'max-bandwidth',
            'max_concurrent_session': 'max-concurrent-session',
            'max_concurrent_tcp_session': 'max-concurrent-tcp-session',
            'max_concurrent_udp_session': 'max-concurrent-udp-session',
            'comment': 'comment',
        }
        
        for param_name, value in param_map.items():
            if value is not None:
                api_name = api_field_map[param_name]
                data[api_name] = value
        data.update(kwargs)
        
        return self._client.post('cmdb', 'firewall.shaper/per-ip-shaper', data, vdom=vdom)
    
    def update(
        self,
        name: str,
        max_bandwidth: Optional[int] = None,
        max_concurrent_session: Optional[int] = None,
        max_concurrent_tcp_session: Optional[int] = None,
        max_concurrent_udp_session: Optional[int] = None,
        comment: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        **kwargs
    ) -> HTTPResponse:
        """
        Update a per-IP traffic shaper.
        
        Args:
            name: Per-IP shaper name
            max_bandwidth: Upper bandwidth limit (0-16776000 kbps, 0 = unlimited)
            max_concurrent_session: Maximum concurrent sessions (0-2097000, 0 = unlimited)
            max_concurrent_tcp_session: Maximum concurrent TCP sessions (0-2097000, 0 = unlimited)
            max_concurrent_udp_session: Maximum concurrent UDP sessions (0-2097000, 0 = unlimited)
            comment: Comment (max 1023 chars)
            vdom: Virtual domain
            **kwargs: Additional parameters
        
        Returns:
            API response dictionary
        
        Examples:
            >>> # Update bandwidth limit
            >>> result = fgt.cmdb.firewall.shaper.per_ip_shaper.update(
            ...     'user-limit',
            ...     max_bandwidth=20480
            ... )
            
            >>> # Update session limits
            >>> result = fgt.cmdb.firewall.shaper.per_ip_shaper.update(
            ...     'session-limit',
            ...     max_concurrent_tcp_session=100,
            ...     max_concurrent_udp_session=50
            ... )
        """
        data = {}
        
        param_map = {
            'max_bandwidth': max_bandwidth,
            'max_concurrent_session': max_concurrent_session,
            'max_concurrent_tcp_session': max_concurrent_tcp_session,
            'max_concurrent_udp_session': max_concurrent_udp_session,
            'comment': comment,
        }
        
        api_field_map = {
            'max_bandwidth': 'max-bandwidth',
            'max_concurrent_session': 'max-concurrent-session',
            'max_concurrent_tcp_session': 'max-concurrent-tcp-session',
            'max_concurrent_udp_session': 'max-concurrent-udp-session',
            'comment': 'comment',
        }
        
        for param_name, value in param_map.items():
            if value is not None:
                api_name = api_field_map[param_name]
                data[api_name] = value
        data.update(kwargs)
        
        return self._client.put('cmdb', f'firewall.shaper/per-ip-shaper/{name}', data, vdom=vdom)
    
    def delete(
        self,
        name: str,
        vdom: Optional[Union[str, bool]] = None
    ) -> HTTPResponse:
        """
        Delete a per-IP traffic shaper.
        
        Args:
            name: Per-IP shaper name
            vdom: Virtual domain
        
        Returns:
            API response dictionary
        
        Examples:
            >>> # Delete per-IP shaper
            >>> result = fgt.cmdb.firewall.shaper.per_ip_shaper.delete('user-limit')
        """
        return self._client.delete('cmdb', f'firewall.shaper/per-ip-shaper/{name}', vdom=vdom)
    
    def exists(
        self,
        name: str,
        vdom: Optional[Union[str, bool]] = None
    ) -> bool:
        """
        Check if per-IP shaper exists.
        
        Args:
            name: Per-IP shaper name
            vdom: Virtual domain
        
        Returns:
            True if per-IP shaper exists, False otherwise
        
        Examples:
            >>> if fgt.cmdb.firewall.shaper.per_ip_shaper.exists('user-limit'):
            ...     print("Per-IP shaper exists")
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
