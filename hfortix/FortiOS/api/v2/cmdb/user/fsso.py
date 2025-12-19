"""
FortiOS CMDB - User Fsso

API Endpoints:
    GET    /user/fsso
    POST   /user/fsso
    GET    /user/fsso/{name}
    PUT    /user/fsso/{name}
    DELETE /user/fsso/{name}
"""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from ....http_client import HTTPClient


class Fsso:
    """Fsso operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize Fsso endpoint.

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
            endpoint = f"/user/fsso/{name}"
        else:
            endpoint = "/user/fsso"
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
        type: str | None = None,
        server: str | None = None,
        port: int | None = None,
        password: str | None = None,
        server2: str | None = None,
        port2: int | None = None,
        password2: str | None = None,
        server3: str | None = None,
        port3: int | None = None,
        password3: str | None = None,
        server4: str | None = None,
        port4: int | None = None,
        password4: str | None = None,
        server5: str | None = None,
        port5: int | None = None,
        password5: str | None = None,
        logon_timeout: int | None = None,
        ldap_server: str | None = None,
        group_poll_interval: int | None = None,
        ldap_poll: str | None = None,
        ldap_poll_interval: int | None = None,
        ldap_poll_filter: str | None = None,
        user_info_server: str | None = None,
        ssl: str | None = None,
        sni: str | None = None,
        ssl_server_host_ip_check: str | None = None,
        ssl_trusted_cert: str | None = None,
        source_ip: str | None = None,
        source_ip6: str | None = None,
        interface_select_method: str | None = None,
        interface: str | None = None,
        vrf_select: int | None = None,
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
            name: Name. (optional)
            type: Server type. (optional)
            server: Domain name or IP address of the first FSSO collector agent. (optional)
            port: Port of the first FSSO collector agent. (optional)
            password: Password of the first FSSO collector agent. (optional)
            server2: Domain name or IP address of the second FSSO collector agent. (optional)
            port2: Port of the second FSSO collector agent. (optional)
            password2: Password of the second FSSO collector agent. (optional)
            server3: Domain name or IP address of the third FSSO collector agent. (optional)
            port3: Port of the third FSSO collector agent. (optional)
            password3: Password of the third FSSO collector agent. (optional)
            server4: Domain name or IP address of the fourth FSSO collector agent. (optional)
            port4: Port of the fourth FSSO collector agent. (optional)
            password4: Password of the fourth FSSO collector agent. (optional)
            server5: Domain name or IP address of the fifth FSSO collector agent. (optional)
            port5: Port of the fifth FSSO collector agent. (optional)
            password5: Password of the fifth FSSO collector agent. (optional)
            logon_timeout: Interval in minutes to keep logons after FSSO server down. (optional)
            ldap_server: LDAP server to get group information. (optional)
            group_poll_interval: Interval in minutes within to fetch groups from FSSO server, or unset to disable. (optional)
            ldap_poll: Enable/disable automatic fetching of groups from LDAP server. (optional)
            ldap_poll_interval: Interval in minutes within to fetch groups from LDAP server. (optional)
            ldap_poll_filter: Filter used to fetch groups. (optional)
            user_info_server: LDAP server to get user information. (optional)
            ssl: Enable/disable use of SSL. (optional)
            sni: Server Name Indication. (optional)
            ssl_server_host_ip_check: Enable/disable server host/IP verification. (optional)
            ssl_trusted_cert: Trusted server certificate or CA certificate. (optional)
            source_ip: Source IP for communications to FSSO agent. (optional)
            source_ip6: IPv6 source for communications to FSSO agent. (optional)
            interface_select_method: Specify how to select outgoing interface to reach server. (optional)
            interface: Specify outgoing interface to reach server. (optional)
            vrf_select: VRF ID used for connection to server. (optional)
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
        endpoint = f"/user/fsso/{name}"
        if before is not None:
            data_payload['before'] = before
        if after is not None:
            data_payload['after'] = after
        if name is not None:
            data_payload['name'] = name
        if type is not None:
            data_payload['type'] = type
        if server is not None:
            data_payload['server'] = server
        if port is not None:
            data_payload['port'] = port
        if password is not None:
            data_payload['password'] = password
        if server2 is not None:
            data_payload['server2'] = server2
        if port2 is not None:
            data_payload['port2'] = port2
        if password2 is not None:
            data_payload['password2'] = password2
        if server3 is not None:
            data_payload['server3'] = server3
        if port3 is not None:
            data_payload['port3'] = port3
        if password3 is not None:
            data_payload['password3'] = password3
        if server4 is not None:
            data_payload['server4'] = server4
        if port4 is not None:
            data_payload['port4'] = port4
        if password4 is not None:
            data_payload['password4'] = password4
        if server5 is not None:
            data_payload['server5'] = server5
        if port5 is not None:
            data_payload['port5'] = port5
        if password5 is not None:
            data_payload['password5'] = password5
        if logon_timeout is not None:
            data_payload['logon-timeout'] = logon_timeout
        if ldap_server is not None:
            data_payload['ldap-server'] = ldap_server
        if group_poll_interval is not None:
            data_payload['group-poll-interval'] = group_poll_interval
        if ldap_poll is not None:
            data_payload['ldap-poll'] = ldap_poll
        if ldap_poll_interval is not None:
            data_payload['ldap-poll-interval'] = ldap_poll_interval
        if ldap_poll_filter is not None:
            data_payload['ldap-poll-filter'] = ldap_poll_filter
        if user_info_server is not None:
            data_payload['user-info-server'] = user_info_server
        if ssl is not None:
            data_payload['ssl'] = ssl
        if sni is not None:
            data_payload['sni'] = sni
        if ssl_server_host_ip_check is not None:
            data_payload['ssl-server-host-ip-check'] = ssl_server_host_ip_check
        if ssl_trusted_cert is not None:
            data_payload['ssl-trusted-cert'] = ssl_trusted_cert
        if source_ip is not None:
            data_payload['source-ip'] = source_ip
        if source_ip6 is not None:
            data_payload['source-ip6'] = source_ip6
        if interface_select_method is not None:
            data_payload['interface-select-method'] = interface_select_method
        if interface is not None:
            data_payload['interface'] = interface
        if vrf_select is not None:
            data_payload['vrf-select'] = vrf_select
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
        endpoint = f"/user/fsso/{name}"
        params.update(kwargs)
        return self._client.delete("cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json)

    def post(
        self,
        payload_dict: dict[str, Any] | None = None,
        nkey: str | None = None,
        name: str | None = None,
        type: str | None = None,
        server: str | None = None,
        port: int | None = None,
        password: str | None = None,
        server2: str | None = None,
        port2: int | None = None,
        password2: str | None = None,
        server3: str | None = None,
        port3: int | None = None,
        password3: str | None = None,
        server4: str | None = None,
        port4: int | None = None,
        password4: str | None = None,
        server5: str | None = None,
        port5: int | None = None,
        password5: str | None = None,
        logon_timeout: int | None = None,
        ldap_server: str | None = None,
        group_poll_interval: int | None = None,
        ldap_poll: str | None = None,
        ldap_poll_interval: int | None = None,
        ldap_poll_filter: str | None = None,
        user_info_server: str | None = None,
        ssl: str | None = None,
        sni: str | None = None,
        ssl_server_host_ip_check: str | None = None,
        ssl_trusted_cert: str | None = None,
        source_ip: str | None = None,
        source_ip6: str | None = None,
        interface_select_method: str | None = None,
        interface: str | None = None,
        vrf_select: int | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Create object(s) in this table.
        
        Args:
            payload_dict: Optional dictionary of all parameters (can be passed as first positional arg)
            nkey: If *action=clone*, use *nkey* to specify the ID for the new resource to be created. (optional)
            name: Name. (optional)
            type: Server type. (optional)
            server: Domain name or IP address of the first FSSO collector agent. (optional)
            port: Port of the first FSSO collector agent. (optional)
            password: Password of the first FSSO collector agent. (optional)
            server2: Domain name or IP address of the second FSSO collector agent. (optional)
            port2: Port of the second FSSO collector agent. (optional)
            password2: Password of the second FSSO collector agent. (optional)
            server3: Domain name or IP address of the third FSSO collector agent. (optional)
            port3: Port of the third FSSO collector agent. (optional)
            password3: Password of the third FSSO collector agent. (optional)
            server4: Domain name or IP address of the fourth FSSO collector agent. (optional)
            port4: Port of the fourth FSSO collector agent. (optional)
            password4: Password of the fourth FSSO collector agent. (optional)
            server5: Domain name or IP address of the fifth FSSO collector agent. (optional)
            port5: Port of the fifth FSSO collector agent. (optional)
            password5: Password of the fifth FSSO collector agent. (optional)
            logon_timeout: Interval in minutes to keep logons after FSSO server down. (optional)
            ldap_server: LDAP server to get group information. (optional)
            group_poll_interval: Interval in minutes within to fetch groups from FSSO server, or unset to disable. (optional)
            ldap_poll: Enable/disable automatic fetching of groups from LDAP server. (optional)
            ldap_poll_interval: Interval in minutes within to fetch groups from LDAP server. (optional)
            ldap_poll_filter: Filter used to fetch groups. (optional)
            user_info_server: LDAP server to get user information. (optional)
            ssl: Enable/disable use of SSL. (optional)
            sni: Server Name Indication. (optional)
            ssl_server_host_ip_check: Enable/disable server host/IP verification. (optional)
            ssl_trusted_cert: Trusted server certificate or CA certificate. (optional)
            source_ip: Source IP for communications to FSSO agent. (optional)
            source_ip6: IPv6 source for communications to FSSO agent. (optional)
            interface_select_method: Specify how to select outgoing interface to reach server. (optional)
            interface: Specify outgoing interface to reach server. (optional)
            vrf_select: VRF ID used for connection to server. (optional)
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
        endpoint = "/user/fsso"
        if nkey is not None:
            data_payload['nkey'] = nkey
        if name is not None:
            data_payload['name'] = name
        if type is not None:
            data_payload['type'] = type
        if server is not None:
            data_payload['server'] = server
        if port is not None:
            data_payload['port'] = port
        if password is not None:
            data_payload['password'] = password
        if server2 is not None:
            data_payload['server2'] = server2
        if port2 is not None:
            data_payload['port2'] = port2
        if password2 is not None:
            data_payload['password2'] = password2
        if server3 is not None:
            data_payload['server3'] = server3
        if port3 is not None:
            data_payload['port3'] = port3
        if password3 is not None:
            data_payload['password3'] = password3
        if server4 is not None:
            data_payload['server4'] = server4
        if port4 is not None:
            data_payload['port4'] = port4
        if password4 is not None:
            data_payload['password4'] = password4
        if server5 is not None:
            data_payload['server5'] = server5
        if port5 is not None:
            data_payload['port5'] = port5
        if password5 is not None:
            data_payload['password5'] = password5
        if logon_timeout is not None:
            data_payload['logon-timeout'] = logon_timeout
        if ldap_server is not None:
            data_payload['ldap-server'] = ldap_server
        if group_poll_interval is not None:
            data_payload['group-poll-interval'] = group_poll_interval
        if ldap_poll is not None:
            data_payload['ldap-poll'] = ldap_poll
        if ldap_poll_interval is not None:
            data_payload['ldap-poll-interval'] = ldap_poll_interval
        if ldap_poll_filter is not None:
            data_payload['ldap-poll-filter'] = ldap_poll_filter
        if user_info_server is not None:
            data_payload['user-info-server'] = user_info_server
        if ssl is not None:
            data_payload['ssl'] = ssl
        if sni is not None:
            data_payload['sni'] = sni
        if ssl_server_host_ip_check is not None:
            data_payload['ssl-server-host-ip-check'] = ssl_server_host_ip_check
        if ssl_trusted_cert is not None:
            data_payload['ssl-trusted-cert'] = ssl_trusted_cert
        if source_ip is not None:
            data_payload['source-ip'] = source_ip
        if source_ip6 is not None:
            data_payload['source-ip6'] = source_ip6
        if interface_select_method is not None:
            data_payload['interface-select-method'] = interface_select_method
        if interface is not None:
            data_payload['interface'] = interface
        if vrf_select is not None:
            data_payload['vrf-select'] = vrf_select
        data_payload.update(kwargs)
        return self._client.post("cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json)
