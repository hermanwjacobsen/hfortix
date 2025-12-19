"""
FortiOS CMDB - System SnmpCommunity

API Endpoints:
    GET    /system.snmp/community
    POST   /system.snmp/community
    GET    /system.snmp/community/{id}
    PUT    /system.snmp/community/{id}
    DELETE /system.snmp/community/{id}
"""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from ....http_client import HTTPClient


class SnmpCommunity:
    """SnmpCommunity operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize SnmpCommunity endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

    def get(
        self,
        id: str | None = None,
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
            id: Object identifier (optional for list, required for specific)
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
        if id:
            endpoint = f"/system.snmp/community/{id}"
        else:
            endpoint = "/system.snmp/community"
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
        id: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        before: str | None = None,
        after: str | None = None,
        name: str | None = None,
        status: str | None = None,
        hosts: list | None = None,
        hosts6: list | None = None,
        query_v1_status: str | None = None,
        query_v1_port: int | None = None,
        query_v2c_status: str | None = None,
        query_v2c_port: int | None = None,
        trap_v1_status: str | None = None,
        trap_v1_lport: int | None = None,
        trap_v1_rport: int | None = None,
        trap_v2c_status: str | None = None,
        trap_v2c_lport: int | None = None,
        trap_v2c_rport: int | None = None,
        events: str | None = None,
        mib_view: str | None = None,
        vdoms: list | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Update this specific resource.
        
        Args:
            payload_dict: Optional dictionary of all parameters (can be passed as first positional arg)
            id: Object identifier (required)
            before: If *action=move*, use *before* to specify the ID of the resource that this resource will be moved before. (optional)
            after: If *action=move*, use *after* to specify the ID of the resource that this resource will be moved after. (optional)
            id: Community ID. (optional)
            name: Community name. (optional)
            status: Enable/disable this SNMP community. (optional)
            hosts: Configure IPv4 SNMP managers (hosts). (optional)
            hosts6: Configure IPv6 SNMP managers. (optional)
            query_v1_status: Enable/disable SNMP v1 queries. (optional)
            query_v1_port: SNMP v1 query port (default = 161). (optional)
            query_v2c_status: Enable/disable SNMP v2c queries. (optional)
            query_v2c_port: SNMP v2c query port (default = 161). (optional)
            trap_v1_status: Enable/disable SNMP v1 traps. (optional)
            trap_v1_lport: SNMP v1 trap local port (default = 162). (optional)
            trap_v1_rport: SNMP v1 trap remote port (default = 162). (optional)
            trap_v2c_status: Enable/disable SNMP v2c traps. (optional)
            trap_v2c_lport: SNMP v2c trap local port (default = 162). (optional)
            trap_v2c_rport: SNMP v2c trap remote port (default = 162). (optional)
            events: SNMP trap events. (optional)
            mib_view: SNMP access control MIB view. (optional)
            vdoms: SNMP access control VDOMs. (optional)
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
        if not id:
            raise ValueError("id is required for put()")
        endpoint = f"/system.snmp/community/{id}"
        if before is not None:
            data_payload['before'] = before
        if after is not None:
            data_payload['after'] = after
        if id is not None:
            data_payload['id'] = id
        if name is not None:
            data_payload['name'] = name
        if status is not None:
            data_payload['status'] = status
        if hosts is not None:
            data_payload['hosts'] = hosts
        if hosts6 is not None:
            data_payload['hosts6'] = hosts6
        if query_v1_status is not None:
            data_payload['query-v1-status'] = query_v1_status
        if query_v1_port is not None:
            data_payload['query-v1-port'] = query_v1_port
        if query_v2c_status is not None:
            data_payload['query-v2c-status'] = query_v2c_status
        if query_v2c_port is not None:
            data_payload['query-v2c-port'] = query_v2c_port
        if trap_v1_status is not None:
            data_payload['trap-v1-status'] = trap_v1_status
        if trap_v1_lport is not None:
            data_payload['trap-v1-lport'] = trap_v1_lport
        if trap_v1_rport is not None:
            data_payload['trap-v1-rport'] = trap_v1_rport
        if trap_v2c_status is not None:
            data_payload['trap-v2c-status'] = trap_v2c_status
        if trap_v2c_lport is not None:
            data_payload['trap-v2c-lport'] = trap_v2c_lport
        if trap_v2c_rport is not None:
            data_payload['trap-v2c-rport'] = trap_v2c_rport
        if events is not None:
            data_payload['events'] = events
        if mib_view is not None:
            data_payload['mib-view'] = mib_view
        if vdoms is not None:
            data_payload['vdoms'] = vdoms
        data_payload.update(kwargs)
        return self._client.put("cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json)

    def delete(
        self,
        id: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Delete this specific resource.
        
        Args:
            id: Object identifier (required)
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
        if not id:
            raise ValueError("id is required for delete()")
        endpoint = f"/system.snmp/community/{id}"
        params.update(kwargs)
        return self._client.delete("cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json)

    def post(
        self,
        payload_dict: dict[str, Any] | None = None,
        nkey: str | None = None,
        id: int | None = None,
        name: str | None = None,
        status: str | None = None,
        hosts: list | None = None,
        hosts6: list | None = None,
        query_v1_status: str | None = None,
        query_v1_port: int | None = None,
        query_v2c_status: str | None = None,
        query_v2c_port: int | None = None,
        trap_v1_status: str | None = None,
        trap_v1_lport: int | None = None,
        trap_v1_rport: int | None = None,
        trap_v2c_status: str | None = None,
        trap_v2c_lport: int | None = None,
        trap_v2c_rport: int | None = None,
        events: str | None = None,
        mib_view: str | None = None,
        vdoms: list | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Create object(s) in this table.
        
        Args:
            payload_dict: Optional dictionary of all parameters (can be passed as first positional arg)
            nkey: If *action=clone*, use *nkey* to specify the ID for the new resource to be created. (optional)
            id: Community ID. (optional)
            name: Community name. (optional)
            status: Enable/disable this SNMP community. (optional)
            hosts: Configure IPv4 SNMP managers (hosts). (optional)
            hosts6: Configure IPv6 SNMP managers. (optional)
            query_v1_status: Enable/disable SNMP v1 queries. (optional)
            query_v1_port: SNMP v1 query port (default = 161). (optional)
            query_v2c_status: Enable/disable SNMP v2c queries. (optional)
            query_v2c_port: SNMP v2c query port (default = 161). (optional)
            trap_v1_status: Enable/disable SNMP v1 traps. (optional)
            trap_v1_lport: SNMP v1 trap local port (default = 162). (optional)
            trap_v1_rport: SNMP v1 trap remote port (default = 162). (optional)
            trap_v2c_status: Enable/disable SNMP v2c traps. (optional)
            trap_v2c_lport: SNMP v2c trap local port (default = 162). (optional)
            trap_v2c_rport: SNMP v2c trap remote port (default = 162). (optional)
            events: SNMP trap events. (optional)
            mib_view: SNMP access control MIB view. (optional)
            vdoms: SNMP access control VDOMs. (optional)
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
        endpoint = "/system.snmp/community"
        if nkey is not None:
            data_payload['nkey'] = nkey
        if id is not None:
            data_payload['id'] = id
        if name is not None:
            data_payload['name'] = name
        if status is not None:
            data_payload['status'] = status
        if hosts is not None:
            data_payload['hosts'] = hosts
        if hosts6 is not None:
            data_payload['hosts6'] = hosts6
        if query_v1_status is not None:
            data_payload['query-v1-status'] = query_v1_status
        if query_v1_port is not None:
            data_payload['query-v1-port'] = query_v1_port
        if query_v2c_status is not None:
            data_payload['query-v2c-status'] = query_v2c_status
        if query_v2c_port is not None:
            data_payload['query-v2c-port'] = query_v2c_port
        if trap_v1_status is not None:
            data_payload['trap-v1-status'] = trap_v1_status
        if trap_v1_lport is not None:
            data_payload['trap-v1-lport'] = trap_v1_lport
        if trap_v1_rport is not None:
            data_payload['trap-v1-rport'] = trap_v1_rport
        if trap_v2c_status is not None:
            data_payload['trap-v2c-status'] = trap_v2c_status
        if trap_v2c_lport is not None:
            data_payload['trap-v2c-lport'] = trap_v2c_lport
        if trap_v2c_rport is not None:
            data_payload['trap-v2c-rport'] = trap_v2c_rport
        if events is not None:
            data_payload['events'] = events
        if mib_view is not None:
            data_payload['mib-view'] = mib_view
        if vdoms is not None:
            data_payload['vdoms'] = vdoms
        data_payload.update(kwargs)
        return self._client.post("cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json)
