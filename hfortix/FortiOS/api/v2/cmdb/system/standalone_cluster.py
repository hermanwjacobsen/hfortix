"""
FortiOS CMDB - System StandaloneCluster

API Endpoints:
    GET    /system/standalone-cluster
    PUT    /system/standalone-cluster
"""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from ....http_client import HTTPClient


class StandaloneCluster:
    """StandaloneCluster operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize StandaloneCluster endpoint.

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
        endpoint = "/system/standalone-cluster"
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
        standalone_group_id: int | None = None,
        group_member_id: int | None = None,
        layer2_connection: str | None = None,
        session_sync_dev: str | None = None,
        encryption: str | None = None,
        psksecret: str | None = None,
        asymmetric_traffic_control: str | None = None,
        cluster_peer: list | None = None,
        monitor_interface: list | None = None,
        pingsvr_monitor_interface: list | None = None,
        monitor_prefix: list | None = None,
        helper_traffic_bounce: str | None = None,
        utm_traffic_bounce: str | None = None,
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
            standalone_group_id: Cluster group ID (0 - 255). Must be the same for all members. (optional)
            group_member_id: Cluster member ID (0 - 15). (optional)
            layer2_connection: Indicate whether layer 2 connections are present among FGSP members. (optional)
            session_sync_dev: Offload session-sync process to kernel and sync sessions using connected interface(s) directly. (optional)
            encryption: Enable/disable encryption when synchronizing sessions. (optional)
            psksecret: Pre-shared secret for session synchronization (ASCII string or hexadecimal encoded with a leading 0x). (optional)
            asymmetric_traffic_control: Asymmetric traffic control mode. (optional)
            cluster_peer: Configure FortiGate Session Life Support Protocol (FGSP) session synchronization. (optional)
            monitor_interface: Configure a list of interfaces on which to monitor itself. Monitoring is performed on the status of the interface. (optional)
            pingsvr_monitor_interface: List of pingsvr monitor interface to check for remote IP monitoring. (optional)
            monitor_prefix: Configure a list of routing prefixes to monitor. (optional)
            helper_traffic_bounce: Enable/disable helper related traffic bounce. (optional)
            utm_traffic_bounce: Enable/disable UTM related traffic bounce. (optional)
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
        endpoint = "/system/standalone-cluster"
        if before is not None:
            data_payload['before'] = before
        if after is not None:
            data_payload['after'] = after
        if standalone_group_id is not None:
            data_payload['standalone-group-id'] = standalone_group_id
        if group_member_id is not None:
            data_payload['group-member-id'] = group_member_id
        if layer2_connection is not None:
            data_payload['layer2-connection'] = layer2_connection
        if session_sync_dev is not None:
            data_payload['session-sync-dev'] = session_sync_dev
        if encryption is not None:
            data_payload['encryption'] = encryption
        if psksecret is not None:
            data_payload['psksecret'] = psksecret
        if asymmetric_traffic_control is not None:
            data_payload['asymmetric-traffic-control'] = asymmetric_traffic_control
        if cluster_peer is not None:
            data_payload['cluster-peer'] = cluster_peer
        if monitor_interface is not None:
            data_payload['monitor-interface'] = monitor_interface
        if pingsvr_monitor_interface is not None:
            data_payload['pingsvr-monitor-interface'] = pingsvr_monitor_interface
        if monitor_prefix is not None:
            data_payload['monitor-prefix'] = monitor_prefix
        if helper_traffic_bounce is not None:
            data_payload['helper-traffic-bounce'] = helper_traffic_bounce
        if utm_traffic_bounce is not None:
            data_payload['utm-traffic-bounce'] = utm_traffic_bounce
        data_payload.update(kwargs)
        return self._client.put("cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json)
