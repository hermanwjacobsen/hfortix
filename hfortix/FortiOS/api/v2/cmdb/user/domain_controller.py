"""
FortiOS CMDB - User DomainController

API Endpoints:
    GET    /user/domain-controller
    POST   /user/domain-controller
    GET    /user/domain-controller/{name}
    PUT    /user/domain-controller/{name}
    DELETE /user/domain-controller/{name}
"""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from ....http_client import HTTPClient


class DomainController:
    """DomainController operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize DomainController endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

    def get(
        self,
        name: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        attr: str | None = None,
        skip_to_datasource: dict | None = None,
        acs: int | None = None,
        search: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Select a specific entry from a CLI table.
        
        Args:
            name: Object identifier (optional for list, required for specific)
            attr: Attribute name that references other table (optional)
            skip_to_datasource: Skip to provided table's Nth entry. E.g {datasource: 'firewall.address', pos: 10, global_entry: false} (optional)
            acs: If true, returned result are in ascending order. (optional)
            search: If present, the objects will be filtered by the search value. (optional)
            vdom: Virtual domain name, or False to skip. Handled by HTTPClient.
            raw_json: If True, return full API response with metadata. If False, return only results.
            **kwargs: Additional query parameters (filter, sort, start, count, format, etc.)
        
        Common Query Parameters (via **kwargs):
            filter: Filter results (e.g., filter='name==value')
            sort: Sort results (e.g., sort='name,asc')
            start: Starting entry index for paging
            count: Maximum number of entries to return
            format: Fields to return (e.g., format='name|type')
            See FortiOS REST API documentation for full list of query parameters
        
        Returns:
            Dictionary containing API response
        """
        params = payload_dict.copy() if payload_dict else {}
        
        # Build endpoint path
        if name:
            endpoint = f"/user/domain-controller/{name}"
        else:
            endpoint = "/user/domain-controller"
        if attr is not None:
            params['attr'] = attr
        if skip_to_datasource is not None:
            params['skip_to_datasource'] = skip_to_datasource
        if acs is not None:
            params['acs'] = acs
        if search is not None:
            params['search'] = search
        params.update(kwargs)
        return self._client.get("cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json)

    def put(
        self,
        name: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        before: str | None = None,
        after: str | None = None,
        ad_mode: str | None = None,
        hostname: str | None = None,
        username: str | None = None,
        password: str | None = None,
        ip_address: str | None = None,
        ip6: str | None = None,
        port: int | None = None,
        source_ip_address: str | None = None,
        source_ip6: str | None = None,
        source_port: int | None = None,
        interface_select_method: str | None = None,
        interface: str | None = None,
        extra_server: list | None = None,
        domain_name: str | None = None,
        replication_port: int | None = None,
        ldap_server: list | None = None,
        change_detection: str | None = None,
        change_detection_period: int | None = None,
        dns_srv_lookup: str | None = None,
        adlds_dn: str | None = None,
        adlds_ip_address: str | None = None,
        adlds_ip6: str | None = None,
        adlds_port: int | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Update this specific resource.
        
        Args:
            payload_dict: Optional dictionary of all parameters (can be passed as first positional arg)
            name: Object identifier (required)
            before: If *action=move*, use *before* to specify the ID of the resource that this resource will be moved before. (optional)
            after: If *action=move*, use *after* to specify the ID of the resource that this resource will be moved after. (optional)
            name: Domain controller entry name. (optional)
            ad_mode: Set Active Directory mode. (optional)
            hostname: Hostname of the server to connect to. (optional)
            username: User name to sign in with. Must have proper permissions for service. (optional)
            password: Password for specified username. (optional)
            ip_address: Domain controller IPv4 address. (optional)
            ip6: Domain controller IPv6 address. (optional)
            port: Port to be used for communication with the domain controller (default = 445). (optional)
            source_ip_address: FortiGate IPv4 address to be used for communication with the domain controller. (optional)
            source_ip6: FortiGate IPv6 address to be used for communication with the domain controller. (optional)
            source_port: Source port to be used for communication with the domain controller. (optional)
            interface_select_method: Specify how to select outgoing interface to reach server. (optional)
            interface: Specify outgoing interface to reach server. (optional)
            extra_server: Extra servers. (optional)
            domain_name: Domain DNS name. (optional)
            replication_port: Port to be used for communication with the domain controller for replication service. Port number 0 indicates automatic discovery. (optional)
            ldap_server: LDAP server name(s). (optional)
            change_detection: Enable/disable detection of a configuration change in the Active Directory server. (optional)
            change_detection_period: Minutes to detect a configuration change in the Active Directory server (5 - 10080 minutes (7 days), default = 60). (optional)
            dns_srv_lookup: Enable/disable DNS service lookup. (optional)
            adlds_dn: AD LDS distinguished name. (optional)
            adlds_ip_address: AD LDS IPv4 address. (optional)
            adlds_ip6: AD LDS IPv6 address. (optional)
            adlds_port: Port number of AD LDS service (default = 389). (optional)
            vdom: Virtual domain name, or False to skip. Handled by HTTPClient.
            raw_json: If True, return full API response with metadata. If False, return only results.
            **kwargs: Additional query parameters (filter, sort, start, count, format, etc.)
        
        Common Query Parameters (via **kwargs):
            filter: Filter results (e.g., filter='name==value')
            sort: Sort results (e.g., sort='name,asc')
            start: Starting entry index for paging
            count: Maximum number of entries to return
            format: Fields to return (e.g., format='name|type')
            See FortiOS REST API documentation for full list of query parameters
        
        Returns:
            Dictionary containing API response
        """
        data_payload = payload_dict.copy() if payload_dict else {}
        params = {}
        
        # Build endpoint path
        if not name:
            raise ValueError("name is required for put()")
        endpoint = f"/user/domain-controller/{name}"
        if before is not None:
            data_payload['before'] = before
        if after is not None:
            data_payload['after'] = after
        if name is not None:
            data_payload['name'] = name
        if ad_mode is not None:
            data_payload['ad-mode'] = ad_mode
        if hostname is not None:
            data_payload['hostname'] = hostname
        if username is not None:
            data_payload['username'] = username
        if password is not None:
            data_payload['password'] = password
        if ip_address is not None:
            data_payload['ip-address'] = ip_address
        if ip6 is not None:
            data_payload['ip6'] = ip6
        if port is not None:
            data_payload['port'] = port
        if source_ip_address is not None:
            data_payload['source-ip-address'] = source_ip_address
        if source_ip6 is not None:
            data_payload['source-ip6'] = source_ip6
        if source_port is not None:
            data_payload['source-port'] = source_port
        if interface_select_method is not None:
            data_payload['interface-select-method'] = interface_select_method
        if interface is not None:
            data_payload['interface'] = interface
        if extra_server is not None:
            data_payload['extra-server'] = extra_server
        if domain_name is not None:
            data_payload['domain-name'] = domain_name
        if replication_port is not None:
            data_payload['replication-port'] = replication_port
        if ldap_server is not None:
            data_payload['ldap-server'] = ldap_server
        if change_detection is not None:
            data_payload['change-detection'] = change_detection
        if change_detection_period is not None:
            data_payload['change-detection-period'] = change_detection_period
        if dns_srv_lookup is not None:
            data_payload['dns-srv-lookup'] = dns_srv_lookup
        if adlds_dn is not None:
            data_payload['adlds-dn'] = adlds_dn
        if adlds_ip_address is not None:
            data_payload['adlds-ip-address'] = adlds_ip_address
        if adlds_ip6 is not None:
            data_payload['adlds-ip6'] = adlds_ip6
        if adlds_port is not None:
            data_payload['adlds-port'] = adlds_port
        data_payload.update(kwargs)
        return self._client.put("cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json)

    def delete(
        self,
        name: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Delete this specific resource.
        
        Args:
            name: Object identifier (required)
            vdom: Virtual domain name, or False to skip. Handled by HTTPClient.
            raw_json: If True, return full API response with metadata. If False, return only results.
            **kwargs: Additional query parameters (filter, sort, start, count, format, etc.)
        
        Common Query Parameters (via **kwargs):
            filter: Filter results (e.g., filter='name==value')
            sort: Sort results (e.g., sort='name,asc')
            start: Starting entry index for paging
            count: Maximum number of entries to return
            format: Fields to return (e.g., format='name|type')
            See FortiOS REST API documentation for full list of query parameters
        
        Returns:
            Dictionary containing API response
        """
        params = payload_dict.copy() if payload_dict else {}
        
        # Build endpoint path
        if not name:
            raise ValueError("name is required for delete()")
        endpoint = f"/user/domain-controller/{name}"
        params.update(kwargs)
        return self._client.delete("cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json)

    def post(
        self,
        payload_dict: dict[str, Any] | None = None,
        nkey: str | None = None,
        name: str | None = None,
        ad_mode: str | None = None,
        hostname: str | None = None,
        username: str | None = None,
        password: str | None = None,
        ip_address: str | None = None,
        ip6: str | None = None,
        port: int | None = None,
        source_ip_address: str | None = None,
        source_ip6: str | None = None,
        source_port: int | None = None,
        interface_select_method: str | None = None,
        interface: str | None = None,
        extra_server: list | None = None,
        domain_name: str | None = None,
        replication_port: int | None = None,
        ldap_server: list | None = None,
        change_detection: str | None = None,
        change_detection_period: int | None = None,
        dns_srv_lookup: str | None = None,
        adlds_dn: str | None = None,
        adlds_ip_address: str | None = None,
        adlds_ip6: str | None = None,
        adlds_port: int | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Create object(s) in this table.
        
        Args:
            payload_dict: Optional dictionary of all parameters (can be passed as first positional arg)
            nkey: If *action=clone*, use *nkey* to specify the ID for the new resource to be created. (optional)
            name: Domain controller entry name. (optional)
            ad_mode: Set Active Directory mode. (optional)
            hostname: Hostname of the server to connect to. (optional)
            username: User name to sign in with. Must have proper permissions for service. (optional)
            password: Password for specified username. (optional)
            ip_address: Domain controller IPv4 address. (optional)
            ip6: Domain controller IPv6 address. (optional)
            port: Port to be used for communication with the domain controller (default = 445). (optional)
            source_ip_address: FortiGate IPv4 address to be used for communication with the domain controller. (optional)
            source_ip6: FortiGate IPv6 address to be used for communication with the domain controller. (optional)
            source_port: Source port to be used for communication with the domain controller. (optional)
            interface_select_method: Specify how to select outgoing interface to reach server. (optional)
            interface: Specify outgoing interface to reach server. (optional)
            extra_server: Extra servers. (optional)
            domain_name: Domain DNS name. (optional)
            replication_port: Port to be used for communication with the domain controller for replication service. Port number 0 indicates automatic discovery. (optional)
            ldap_server: LDAP server name(s). (optional)
            change_detection: Enable/disable detection of a configuration change in the Active Directory server. (optional)
            change_detection_period: Minutes to detect a configuration change in the Active Directory server (5 - 10080 minutes (7 days), default = 60). (optional)
            dns_srv_lookup: Enable/disable DNS service lookup. (optional)
            adlds_dn: AD LDS distinguished name. (optional)
            adlds_ip_address: AD LDS IPv4 address. (optional)
            adlds_ip6: AD LDS IPv6 address. (optional)
            adlds_port: Port number of AD LDS service (default = 389). (optional)
            vdom: Virtual domain name, or False to skip. Handled by HTTPClient.
            raw_json: If True, return full API response with metadata. If False, return only results.
            **kwargs: Additional query parameters (filter, sort, start, count, format, etc.)
        
        Common Query Parameters (via **kwargs):
            filter: Filter results (e.g., filter='name==value')
            sort: Sort results (e.g., sort='name,asc')
            start: Starting entry index for paging
            count: Maximum number of entries to return
            format: Fields to return (e.g., format='name|type')
            See FortiOS REST API documentation for full list of query parameters
        
        Returns:
            Dictionary containing API response
        """
        data_payload = payload_dict.copy() if payload_dict else {}
        params = {}
        endpoint = "/user/domain-controller"
        if nkey is not None:
            data_payload['nkey'] = nkey
        if name is not None:
            data_payload['name'] = name
        if ad_mode is not None:
            data_payload['ad-mode'] = ad_mode
        if hostname is not None:
            data_payload['hostname'] = hostname
        if username is not None:
            data_payload['username'] = username
        if password is not None:
            data_payload['password'] = password
        if ip_address is not None:
            data_payload['ip-address'] = ip_address
        if ip6 is not None:
            data_payload['ip6'] = ip6
        if port is not None:
            data_payload['port'] = port
        if source_ip_address is not None:
            data_payload['source-ip-address'] = source_ip_address
        if source_ip6 is not None:
            data_payload['source-ip6'] = source_ip6
        if source_port is not None:
            data_payload['source-port'] = source_port
        if interface_select_method is not None:
            data_payload['interface-select-method'] = interface_select_method
        if interface is not None:
            data_payload['interface'] = interface
        if extra_server is not None:
            data_payload['extra-server'] = extra_server
        if domain_name is not None:
            data_payload['domain-name'] = domain_name
        if replication_port is not None:
            data_payload['replication-port'] = replication_port
        if ldap_server is not None:
            data_payload['ldap-server'] = ldap_server
        if change_detection is not None:
            data_payload['change-detection'] = change_detection
        if change_detection_period is not None:
            data_payload['change-detection-period'] = change_detection_period
        if dns_srv_lookup is not None:
            data_payload['dns-srv-lookup'] = dns_srv_lookup
        if adlds_dn is not None:
            data_payload['adlds-dn'] = adlds_dn
        if adlds_ip_address is not None:
            data_payload['adlds-ip-address'] = adlds_ip_address
        if adlds_ip6 is not None:
            data_payload['adlds-ip6'] = adlds_ip6
        if adlds_port is not None:
            data_payload['adlds-port'] = adlds_port
        data_payload.update(kwargs)
        return self._client.post("cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json)
