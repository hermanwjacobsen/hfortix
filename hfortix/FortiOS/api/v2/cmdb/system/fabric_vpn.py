"""
FortiOS CMDB - System FabricVpn

API Endpoints:
    GET    /system/fabric-vpn
    PUT    /system/fabric-vpn
"""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from ....http_client import HTTPClient


class FabricVpn:
    """FabricVpn operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize FabricVpn endpoint.

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
        endpoint = "/system/fabric-vpn"
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
        sync_mode: str | None = None,
        branch_name: str | None = None,
        policy_rule: str | None = None,
        vpn_role: str | None = None,
        overlays: list | None = None,
        advertised_subnets: list | None = None,
        loopback_address_block: str | None = None,
        loopback_interface: str | None = None,
        loopback_advertised_subnet: int | None = None,
        psksecret: str | None = None,
        bgp_as: str | None = None,
        sdwan_zone: str | None = None,
        health_checks: str | None = None,
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
            status: Enable/disable Fabric VPN. (optional)
            sync_mode: Setting synchronized by fabric or manual. (optional)
            branch_name: Branch name. (optional)
            policy_rule: Policy creation rule. (optional)
            vpn_role: Fabric VPN role. (optional)
            overlays: Local overlay interfaces table. (optional)
            advertised_subnets: Local advertised subnets. (optional)
            loopback_address_block: IPv4 address and subnet mask for hub's loopback address, syntax: X.X.X.X/24. (optional)
            loopback_interface: Loopback interface. (optional)
            loopback_advertised_subnet: Loopback advertised subnet reference. (optional)
            psksecret: Pre-shared secret for ADVPN. (optional)
            bgp_as: BGP Router AS number, asplain/asdot/asdot+ format. (optional)
            sdwan_zone: Reference to created SD-WAN zone. (optional)
            health_checks: Underlying health checks. (optional)
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
        endpoint = "/system/fabric-vpn"
        if before is not None:
            data_payload['before'] = before
        if after is not None:
            data_payload['after'] = after
        if status is not None:
            data_payload['status'] = status
        if sync_mode is not None:
            data_payload['sync-mode'] = sync_mode
        if branch_name is not None:
            data_payload['branch-name'] = branch_name
        if policy_rule is not None:
            data_payload['policy-rule'] = policy_rule
        if vpn_role is not None:
            data_payload['vpn-role'] = vpn_role
        if overlays is not None:
            data_payload['overlays'] = overlays
        if advertised_subnets is not None:
            data_payload['advertised-subnets'] = advertised_subnets
        if loopback_address_block is not None:
            data_payload['loopback-address-block'] = loopback_address_block
        if loopback_interface is not None:
            data_payload['loopback-interface'] = loopback_interface
        if loopback_advertised_subnet is not None:
            data_payload['loopback-advertised-subnet'] = loopback_advertised_subnet
        if psksecret is not None:
            data_payload['psksecret'] = psksecret
        if bgp_as is not None:
            data_payload['bgp-as'] = bgp_as
        if sdwan_zone is not None:
            data_payload['sdwan-zone'] = sdwan_zone
        if health_checks is not None:
            data_payload['health-checks'] = health_checks
        data_payload.update(kwargs)
        return self._client.put("cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json)
