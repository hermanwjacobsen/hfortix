"""
FortiOS CMDB - Firewall Service Custom

Configure custom services.

API Endpoints:
    GET    /api/v2/cmdb/firewall.service/custom        - List all custom services
    GET    /api/v2/cmdb/firewall.service/custom/{name} - Get specific custom service
    POST   /api/v2/cmdb/firewall.service/custom        - Create new custom service
    PUT    /api/v2/cmdb/firewall.service/custom/{name} - Update custom service
    DELETE /api/v2/cmdb/firewall.service/custom/{name} - Delete custom service
"""

from __future__ import annotations

from typing import Dict, TYPE_CHECKING, Any, Optional, Union

if TYPE_CHECKING:
    from ....http_client import HTTPClient


class ServiceCustom:
    """Firewall custom service endpoint"""

    def __init__(self, client: 'HTTPClient') -> None:
        """
        Initialize ServiceCustom endpoint

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def list(
        self,
        filter: Optional[str] = None,
        start: Optional[int] = None,
        count: Optional[int] = None,
        with_meta: Optional[bool] = None,
        datasource: Optional[bool] = None,
        format: Optional[list] = None,
        vdom: Optional[Union[str, bool]] = None,
        **kwargs: Any
    ) -> dict[str, Any]:
        """
        List all custom services.

        Args:
            filter: Filter results
            start: Starting entry index
            count: Maximum number of entries to return
            with_meta: Include metadata
            datasource: Include datasource information
            format: List of fields to return
            vdom: Virtual domain
            **kwargs: Additional parameters

        Returns:
            API response dictionary

        Examples:
            >>> # List all custom services
            >>> result = fgt.cmdb.firewall.service.custom.list()
            
            >>> # List with specific fields
            >>> result = fgt.cmdb.firewall.service.custom.list(
            ...     format=['name', 'protocol', 'tcp-portrange']
            ... )
        """
        return self.get(
            name=None,
            filter=filter,
            start=start,
            count=count,
            with_meta=with_meta,
            datasource=datasource,
            format=format,
            vdom=vdom,
            **kwargs
        )

    def get(
        self,
        name: Optional[str] = None,
        filter: Optional[str] = None,
        start: Optional[int] = None,
        count: Optional[int] = None,
        with_meta: Optional[bool] = None,
        datasource: Optional[bool] = None,
        format: Optional[list] = None,
        vdom: Optional[Union[str, bool]] = None,
        **kwargs: Any
    ) -> dict[str, Any]:
        """
        Get custom service configuration.

        Args:
            name: Service name (if None, returns all)
            filter: Filter results
            start: Starting entry index
            count: Maximum number of entries to return
            with_meta: Include metadata
            datasource: Include datasource information
            format: List of fields to return
            vdom: Virtual domain
            **kwargs: Additional parameters

        Returns:
            API response dictionary

        Examples:
            >>> # Get all custom services
            >>> result = fgt.cmdb.firewall.service.custom.get()
            
            >>> # Get specific service
            >>> result = fgt.cmdb.firewall.service.custom.get('HTTPS-8443')
            
            >>> # Get with metadata
            >>> result = fgt.cmdb.firewall.service.custom.get(
            ...     'HTTPS-8443',
            ...     with_meta=True
            ... )
        """
        params = {}
        param_map = {
            'filter': filter,
            'start': start,
            'count': count,
            'with_meta': with_meta,
            'datasource': datasource,
            'format': format,
        }
        
        for key, value in param_map.items():
            if value is not None:
                params[key] = value
        
        params.update(kwargs)
        
        path = 'firewall.service/custom'
        if name:
            path = f'{path}/{name}'
        
        return self._client.get('cmdb', path, params=params if params else None, vdom=vdom)
    def create(
        self,
        data: Optional[Dict[str, Any]] = None,
        name: Optional[str] = None,
        protocol: Optional[str] = None,
        tcp_portrange: Optional[str] = None,
        udp_portrange: Optional[str] = None,
        sctp_portrange: Optional[str] = None,
        icmptype: Optional[int] = None,
        icmpcode: Optional[int] = None,
        protocol_number: Optional[int] = None,
        category: Optional[str] = None,
        comment: Optional[str] = None,
        visibility: Optional[str] = None,
        color: Optional[int] = None,
        app_service_type: Optional[str] = None,
        app_category: Optional[list] = None,
        application: Optional[list] = None,
        fabric_object: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        **kwargs: Any
    ) -> dict[str, Any]:
        """
        Create a new custom service.

        
        Supports two usage patterns:
        1. Pass data dict: create(data={'key': 'value'}, vdom='root')
        2. Pass kwargs: create(key='value', vdom='root')
        Args:
            name: Service name (required)
            protocol: Protocol type - 'TCP/UDP/SCTP', 'ICMP', 'ICMP6', 'IP', 'HTTP', 'FTP', 'CONNECT', 'SOCKS-TCP', 'SOCKS-UDP', 'ALL'
            tcp_portrange: TCP port range (e.g., '80', '8000-8080', '80 443 8080')
            udp_portrange: UDP port range (e.g., '53', '5000-5100')
            sctp_portrange: SCTP port range
            icmptype: ICMP type (0-255)
            icmpcode: ICMP code (0-255)
            protocol_number: IP protocol number (0-255)
            category: Service category name
            comment: Comment text (max 255 chars)
            visibility: Enable/disable visibility - 'enable' or 'disable'
            color: Color value (0-32)
            app_service_type: Application service type - 'disable', 'app-id', 'app-category'
            app_category: Application category list
            application: Application list
            fabric_object: Security Fabric global object setting - 'enable' or 'disable'
            vdom: Virtual domain
            **kwargs: Additional parameters

        Returns:
            API response dictionary

        Examples:
            >>> # Create TCP service
            >>> result = fgt.cmdb.firewall.service.custom.create(
            ...     name='HTTPS-8443',
            ...     protocol='TCP/UDP/SCTP',
            ...     tcp_portrange='8443',
            ...     comment='HTTPS on port 8443'
            ... )
            
            >>> # Create UDP service with multiple ports
            >>> result = fgt.cmdb.firewall.service.custom.create(
            ...     name='Custom-DNS',
            ...     protocol='TCP/UDP/SCTP',
            ...     udp_portrange='53 5353',
            ...     category='Network Services'
            ... )
            
            >>> # Create ICMP service
            >>> result = fgt.cmdb.firewall.service.custom.create(
            ...     name='ICMP-Echo',
            ...     protocol='ICMP',
            ...     icmptype=8,
            ...     icmpcode=0
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
            if protocol is not None:
                data['protocol'] = protocol
            if tcp_portrange is not None:
                data['tcp-portrange'] = tcp_portrange
            if udp_portrange is not None:
                data['udp-portrange'] = udp_portrange
            if sctp_portrange is not None:
                data['sctp-portrange'] = sctp_portrange
            if icmptype is not None:
                data['icmptype'] = icmptype
            if icmpcode is not None:
                data['icmpcode'] = icmpcode
            if protocol_number is not None:
                data['protocol-number'] = protocol_number
            if category is not None:
                data['category'] = category
            if comment is not None:
                data['comment'] = comment
            if visibility is not None:
                data['visibility'] = visibility
            if color is not None:
                data['color'] = color
            if app_service_type is not None:
                data['app-service-type'] = app_service_type
            if app_category is not None:
                data['app-category'] = app_category
            if application is not None:
                data['application'] = application
            if fabric_object is not None:
                data['fabric-object'] = fabric_object
        
        return self._client.post('cmdb', 'firewall.service/custom', data, vdom=vdom)
    def update(
        self,
        name: str,
        data: Optional[Dict[str, Any]] = None,
        protocol: Optional[str] = None,
        tcp_portrange: Optional[str] = None,
        udp_portrange: Optional[str] = None,
        sctp_portrange: Optional[str] = None,
        icmptype: Optional[int] = None,
        icmpcode: Optional[int] = None,
        protocol_number: Optional[int] = None,
        category: Optional[str] = None,
        comment: Optional[str] = None,
        visibility: Optional[str] = None,
        color: Optional[int] = None,
        app_service_type: Optional[str] = None,
        app_category: Optional[list] = None,
        application: Optional[list] = None,
        fabric_object: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        **kwargs: Any
    ) -> dict[str, Any]:
        """
        Update an existing custom service.

        
        Supports two usage patterns:
        1. Pass data dict: update(data={'key': 'value'}, vdom='root')
        2. Pass kwargs: update(key='value', vdom='root')
        Args:
            name: Service name (required)
            protocol: Protocol type - 'TCP/UDP/SCTP', 'ICMP', 'ICMP6', 'IP', 'HTTP', 'FTP', 'CONNECT', 'SOCKS-TCP', 'SOCKS-UDP', 'ALL'
            tcp_portrange: TCP port range (e.g., '80', '8000-8080', '80 443 8080')
            udp_portrange: UDP port range (e.g., '53', '5000-5100')
            sctp_portrange: SCTP port range
            icmptype: ICMP type (0-255)
            icmpcode: ICMP code (0-255)
            protocol_number: IP protocol number (0-255)
            category: Service category name
            comment: Comment text (max 255 chars)
            visibility: Enable/disable visibility - 'enable' or 'disable'
            color: Color value (0-32)
            app_service_type: Application service type - 'disable', 'app-id', 'app-category'
            app_category: Application category list
            application: Application list
            fabric_object: Security Fabric global object setting - 'enable' or 'disable'
            vdom: Virtual domain
            **kwargs: Additional parameters

        Returns:
            API response dictionary

        Examples:
            >>> # Update port range
            >>> result = fgt.cmdb.firewall.service.custom.update(
            ...     name='HTTPS-8443',
            ...     tcp_portrange='8443 8444'
            ... )
            
            >>> # Update category and comment
            >>> result = fgt.cmdb.firewall.service.custom.update(
            ...     name='HTTPS-8443',
            ...     category='Web Access',
            ...     comment='HTTPS on alternate ports'
            ... )
        """
        # Pattern 1: data dict provided
        if data is not None:
            # Use provided data dict
            pass
        # Pattern 2: kwargs pattern - build data dict
        else:
            data = {}
            if protocol is not None:
                data['protocol'] = protocol
            if tcp_portrange is not None:
                data['tcp-portrange'] = tcp_portrange
            if udp_portrange is not None:
                data['udp-portrange'] = udp_portrange
            if sctp_portrange is not None:
                data['sctp-portrange'] = sctp_portrange
            if icmptype is not None:
                data['icmptype'] = icmptype
            if icmpcode is not None:
                data['icmpcode'] = icmpcode
            if protocol_number is not None:
                data['protocol-number'] = protocol_number
            if category is not None:
                data['category'] = category
            if comment is not None:
                data['comment'] = comment
            if visibility is not None:
                data['visibility'] = visibility
            if color is not None:
                data['color'] = color
            if app_service_type is not None:
                data['app-service-type'] = app_service_type
            if app_category is not None:
                data['app-category'] = app_category
            if application is not None:
                data['application'] = application
            if fabric_object is not None:
                data['fabric-object'] = fabric_object
        
        return self._client.put('cmdb', f'firewall.service/custom/{name}', data, vdom=vdom)

    def delete(
        self,
        name: str,
        vdom: Optional[Union[str, bool]] = None
    ) -> dict[str, Any]:
        """
        Delete a custom service.

        Args:
            name: Service name
            vdom: Virtual domain

        Returns:
            API response dictionary

        Examples:
            >>> # Delete service
            >>> result = fgt.cmdb.firewall.service.custom.delete('HTTPS-8443')
        """
        return self._client.delete('cmdb', f'firewall.service/custom/{name}', vdom=vdom)

    def exists(
        self,
        name: str,
        vdom: Optional[Union[str, bool]] = None
    ) -> bool:
        """
        Check if a custom service exists.

        Args:
            name: Service name
            vdom: Virtual domain

        Returns:
            True if service exists, False otherwise

        Examples:
            >>> if fgt.cmdb.firewall.service.custom.exists('HTTPS-8443'):
            ...     print("Service exists")
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
