"""
FortiOS CMDB - System SnmpSysinfo

API Endpoints:
    GET    /system.snmp/sysinfo
    PUT    /system.snmp/sysinfo
"""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from ....http_client import HTTPClient


class SnmpSysinfo:
    """SnmpSysinfo operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize SnmpSysinfo endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

    def get(
        self,
        payload_dict: dict[str, Any] | None = None,
        exclude_default_values: bool | None = None,
        stat_items: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Select all entries in a CLI table.
        
        Args:
            exclude_default_values: Exclude properties/objects with default value (optional)
            stat_items: Items to count occurrence in entire response (multiple items should be separated by '|'). (optional)
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
        endpoint = "/system.snmp/sysinfo"
        if exclude_default_values is not None:
            params['exclude-default-values'] = exclude_default_values
        if stat_items is not None:
            params['stat-items'] = stat_items
        params.update(kwargs)
        return self._client.get("cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json)

    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        before: str | None = None,
        after: str | None = None,
        status: str | None = None,
        engine_id_type: str | None = None,
        engine_id: str | None = None,
        description: str | None = None,
        contact_info: str | None = None,
        location: str | None = None,
        trap_high_cpu_threshold: int | None = None,
        trap_low_memory_threshold: int | None = None,
        trap_log_full_threshold: int | None = None,
        trap_free_memory_threshold: int | None = None,
        trap_freeable_memory_threshold: int | None = None,
        append_index: str | None = None,
        non_mgmt_vdom_query: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Update this specific resource.
        
        Args:
            payload_dict: Optional dictionary of all parameters (can be passed as first positional arg)
            before: If *action=move*, use *before* to specify the ID of the resource that this resource will be moved before. (optional)
            after: If *action=move*, use *after* to specify the ID of the resource that this resource will be moved after. (optional)
            status: Enable/disable SNMP. (optional)
            engine_id_type: Local SNMP engineID type (text/hex/mac). (optional)
            engine_id: Local SNMP engineID string (maximum 27 characters). (optional)
            description: System description. (optional)
            contact_info: Contact information. (optional)
            location: System location. (optional)
            trap_high_cpu_threshold: CPU usage when trap is sent. (optional)
            trap_low_memory_threshold: Memory usage when trap is sent. (optional)
            trap_log_full_threshold: Log disk usage when trap is sent. (optional)
            trap_free_memory_threshold: Free memory usage when trap is sent. (optional)
            trap_freeable_memory_threshold: Freeable memory usage when trap is sent. (optional)
            append_index: Enable/disable allowance of appending vdom or interface index in some RFC tables. (optional)
            non_mgmt_vdom_query: Enable/disable allowance of SNMPv3 query from non-management vdoms. (optional)
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
        endpoint = "/system.snmp/sysinfo"
        if before is not None:
            data_payload['before'] = before
        if after is not None:
            data_payload['after'] = after
        if status is not None:
            data_payload['status'] = status
        if engine_id_type is not None:
            data_payload['engine-id-type'] = engine_id_type
        if engine_id is not None:
            data_payload['engine-id'] = engine_id
        if description is not None:
            data_payload['description'] = description
        if contact_info is not None:
            data_payload['contact-info'] = contact_info
        if location is not None:
            data_payload['location'] = location
        if trap_high_cpu_threshold is not None:
            data_payload['trap-high-cpu-threshold'] = trap_high_cpu_threshold
        if trap_low_memory_threshold is not None:
            data_payload['trap-low-memory-threshold'] = trap_low_memory_threshold
        if trap_log_full_threshold is not None:
            data_payload['trap-log-full-threshold'] = trap_log_full_threshold
        if trap_free_memory_threshold is not None:
            data_payload['trap-free-memory-threshold'] = trap_free_memory_threshold
        if trap_freeable_memory_threshold is not None:
            data_payload['trap-freeable-memory-threshold'] = trap_freeable_memory_threshold
        if append_index is not None:
            data_payload['append-index'] = append_index
        if non_mgmt_vdom_query is not None:
            data_payload['non-mgmt-vdom-query'] = non_mgmt_vdom_query
        data_payload.update(kwargs)
        return self._client.put("cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json)
