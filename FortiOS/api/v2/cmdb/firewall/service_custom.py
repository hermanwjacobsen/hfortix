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

from typing import TYPE_CHECKING, Any, Optional, Union

if TYPE_CHECKING:
    from ....client import FortiOS


class ServiceCustom:
    """Firewall custom service endpoint"""

    def __init__(self, client: 'FortiOS') -> None:
        """
        Initialize ServiceCustom endpoint

        Args:
            client: FortiOS client instance
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
        name: str,
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
        data = {}
        param_map = {
            'name': name,
            'protocol': protocol,
            'tcp_portrange': tcp_portrange,
            'udp_portrange': udp_portrange,
            'sctp_portrange': sctp_portrange,
            'icmptype': icmptype,
            'icmpcode': icmpcode,
            'protocol_number': protocol_number,
            'category': category,
            'comment': comment,
            'visibility': visibility,
            'color': color,
            'app_service_type': app_service_type,
            'app_category': app_category,
            'application': application,
            'fabric_object': fabric_object,
        }
        
        api_field_map = {
            'name': 'name',
            'protocol': 'protocol',
            'tcp_portrange': 'tcp-portrange',
            'udp_portrange': 'udp-portrange',
            'sctp_portrange': 'sctp-portrange',
            'icmptype': 'icmptype',
            'icmpcode': 'icmpcode',
            'protocol_number': 'protocol-number',
            'category': 'category',
            'comment': 'comment',
            'visibility': 'visibility',
            'color': 'color',
            'app_service_type': 'app-service-type',
            'app_category': 'app-category',
            'application': 'application',
            'fabric_object': 'fabric-object',
        }
        
        for param_name, value in param_map.items():
            if value is not None:
                api_name = api_field_map[param_name]
                data[api_name] = value
        
        data.update(kwargs)
        
        return self._client.post('cmdb', 'firewall.service/custom', data, vdom=vdom)

    def update(
        self,
        name: str,
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
        data = {}
        param_map = {
            'protocol': protocol,
            'tcp_portrange': tcp_portrange,
            'udp_portrange': udp_portrange,
            'sctp_portrange': sctp_portrange,
            'icmptype': icmptype,
            'icmpcode': icmpcode,
            'protocol_number': protocol_number,
            'category': category,
            'comment': comment,
            'visibility': visibility,
            'color': color,
            'app_service_type': app_service_type,
            'app_category': app_category,
            'application': application,
            'fabric_object': fabric_object,
        }
        
        api_field_map = {
            'protocol': 'protocol',
            'tcp_portrange': 'tcp-portrange',
            'udp_portrange': 'udp-portrange',
            'sctp_portrange': 'sctp-portrange',
            'icmptype': 'icmptype',
            'icmpcode': 'icmpcode',
            'protocol_number': 'protocol-number',
            'category': 'category',
            'comment': 'comment',
            'visibility': 'visibility',
            'color': 'color',
            'app_service_type': 'app-service-type',
            'app_category': 'app-category',
            'application': 'application',
            'fabric_object': 'fabric-object',
        }
        
        for param_name, value in param_map.items():
            if value is not None:
                api_name = api_field_map[param_name]
                data[api_name] = value
        
        data.update(kwargs)
        
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
