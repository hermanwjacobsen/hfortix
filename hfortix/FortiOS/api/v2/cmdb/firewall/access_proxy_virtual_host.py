"""
FortiOS CMDB - Firewall AccessProxyVirtualHost

API Endpoints:
    GET    /firewall/access-proxy-virtual-host
    POST   /firewall/access-proxy-virtual-host
    GET    /firewall/access-proxy-virtual-host/{name}
    PUT    /firewall/access-proxy-virtual-host/{name}
    DELETE /firewall/access-proxy-virtual-host/{name}
"""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from ....http_client import HTTPClient


class AccessProxyVirtualHost:
    """AccessProxyVirtualHost operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize AccessProxyVirtualHost endpoint.

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
            endpoint = f"/firewall/access-proxy-virtual-host/{name}"
        else:
            endpoint = "/firewall/access-proxy-virtual-host"
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
        ssl_certificate: list | None = None,
        host: str | None = None,
        host_type: str | None = None,
        replacemsg_group: str | None = None,
        empty_cert_action: str | None = None,
        user_agent_detect: str | None = None,
        client_cert: str | None = None,
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
            name: Virtual host name. (optional)
            ssl_certificate: SSL certificates for this host. (optional)
            host: The host name. (optional)
            host_type: Type of host pattern. (optional)
            replacemsg_group: Access-proxy-virtual-host replacement message override group. (optional)
            empty_cert_action: Action for an empty client certificate. (optional)
            user_agent_detect: Enable/disable detecting device type by HTTP user-agent if no client certificate is provided. (optional)
            client_cert: Enable/disable requesting client certificate. (optional)
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
        endpoint = f"/firewall/access-proxy-virtual-host/{name}"
        if before is not None:
            data_payload['before'] = before
        if after is not None:
            data_payload['after'] = after
        if name is not None:
            data_payload['name'] = name
        if ssl_certificate is not None:
            data_payload['ssl-certificate'] = ssl_certificate
        if host is not None:
            data_payload['host'] = host
        if host_type is not None:
            data_payload['host-type'] = host_type
        if replacemsg_group is not None:
            data_payload['replacemsg-group'] = replacemsg_group
        if empty_cert_action is not None:
            data_payload['empty-cert-action'] = empty_cert_action
        if user_agent_detect is not None:
            data_payload['user-agent-detect'] = user_agent_detect
        if client_cert is not None:
            data_payload['client-cert'] = client_cert
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
        endpoint = f"/firewall/access-proxy-virtual-host/{name}"
        params.update(kwargs)
        return self._client.delete("cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json)

    def post(
        self,
        payload_dict: dict[str, Any] | None = None,
        nkey: str | None = None,
        name: str | None = None,
        ssl_certificate: list | None = None,
        host: str | None = None,
        host_type: str | None = None,
        replacemsg_group: str | None = None,
        empty_cert_action: str | None = None,
        user_agent_detect: str | None = None,
        client_cert: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Create object(s) in this table.
        
        Args:
            payload_dict: Optional dictionary of all parameters (can be passed as first positional arg)
            nkey: If *action=clone*, use *nkey* to specify the ID for the new resource to be created. (optional)
            name: Virtual host name. (optional)
            ssl_certificate: SSL certificates for this host. (optional)
            host: The host name. (optional)
            host_type: Type of host pattern. (optional)
            replacemsg_group: Access-proxy-virtual-host replacement message override group. (optional)
            empty_cert_action: Action for an empty client certificate. (optional)
            user_agent_detect: Enable/disable detecting device type by HTTP user-agent if no client certificate is provided. (optional)
            client_cert: Enable/disable requesting client certificate. (optional)
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
        endpoint = "/firewall/access-proxy-virtual-host"
        if nkey is not None:
            data_payload['nkey'] = nkey
        if name is not None:
            data_payload['name'] = name
        if ssl_certificate is not None:
            data_payload['ssl-certificate'] = ssl_certificate
        if host is not None:
            data_payload['host'] = host
        if host_type is not None:
            data_payload['host-type'] = host_type
        if replacemsg_group is not None:
            data_payload['replacemsg-group'] = replacemsg_group
        if empty_cert_action is not None:
            data_payload['empty-cert-action'] = empty_cert_action
        if user_agent_detect is not None:
            data_payload['user-agent-detect'] = user_agent_detect
        if client_cert is not None:
            data_payload['client-cert'] = client_cert
        data_payload.update(kwargs)
        return self._client.post("cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json)
