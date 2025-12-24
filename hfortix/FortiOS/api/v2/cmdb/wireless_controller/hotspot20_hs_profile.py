"""
FortiOS CMDB - Cmdb Wireless Controller Hotspot20 Hs Profile

Configuration endpoint for managing cmdb wireless controller hotspot20 hs
profile objects.

API Endpoints:
    GET    /cmdb/wireless-controller/hotspot20_hs_profile
    POST   /cmdb/wireless-controller/hotspot20_hs_profile
    GET    /cmdb/wireless-controller/hotspot20_hs_profile
    PUT    /cmdb/wireless-controller/hotspot20_hs_profile/{identifier}
    DELETE /cmdb/wireless-controller/hotspot20_hs_profile/{identifier}

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.wireless_controller.hotspot20_hs_profile.get()
    >>>
    >>> # Get specific item (if supported)
    >>> item =
    fgt.api.cmdb.wireless_controller.hotspot20_hs_profile.get(name="item_name")
    >>>
    >>> # Create new item (use POST)
    >>> result = fgt.api.cmdb.wireless_controller.hotspot20_hs_profile.post(
    ...     name="new_item",
    ...     # ... additional parameters
    ... )
    >>>
    >>> # Update existing item (use PUT)
    >>> result = fgt.api.cmdb.wireless_controller.hotspot20_hs_profile.put(
    ...     name="existing_item",
    ...     # ... parameters to update
    ... )
    >>>
    >>> # Delete item
    >>> result =
    fgt.api.cmdb.wireless_controller.hotspot20_hs_profile.delete(name="item_name")

Important:
    - Use **POST** to create new objects (404 error if already exists)
    - Use **PUT** to update existing objects (404 error if doesn't exist)
    - Use **GET** to retrieve configuration (no changes made)
    - Use **DELETE** to remove objects (404 error if doesn't exist)
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Union

if TYPE_CHECKING:
    from collections.abc import Coroutine

    from hfortix.FortiOS.http_client_interface import IHTTPClient


class Hotspot20HsProfile:
    """
    Hotspot20Hsprofile Operations.

    Provides CRUD operations for FortiOS hotspot20hsprofile configuration.

    Methods:
        get(): Retrieve configuration objects
        post(): Create new configuration objects
        put(): Update existing configuration objects
        delete(): Remove configuration objects

    Important:
        - POST creates new objects (404 if name already exists)
        - PUT updates existing objects (404 if name doesn't exist)
        - GET retrieves objects without making changes
        - DELETE removes objects (404 if name doesn't exist)
    """

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Hotspot20HsProfile endpoint.

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
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Select a specific entry from a CLI table.

        Args:
            name: Object identifier (optional for list, required for specific)
            attr: Attribute name that references other table (optional)
            skip_to_datasource: Skip to provided table's Nth entry. E.g
            {datasource: 'firewall.address', pos: 10, global_entry: false}
            (optional)
            acs: If true, returned result are in ascending order. (optional)
            search: If present, the objects will be filtered by the search
            value. (optional)
            vdom: Virtual domain name, or False to skip. Handled by HTTPClient.
            raw_json: If True, return full API response with metadata. If
            False, return only results.
            **kwargs: Additional query parameters (filter, sort, start, count,
            format, etc.)

        Common Query Parameters (via **kwargs):
            filter: Filter results (e.g., filter='name==value')
            sort: Sort results (e.g., sort='name,asc')
            start: Starting entry index for paging
            count: Maximum number of entries to return
            format: Fields to return (e.g., format='name|type')
            See FortiOS REST API documentation for full list of query
            parameters

        Returns:
            Dictionary containing API response
        """
        params = payload_dict.copy() if payload_dict else {}

        # Build endpoint path
        if name:
            endpoint = f"/wireless-controller.hotspot20/hs-profile/{name}"
        else:
            endpoint = "/wireless-controller.hotspot20/hs-profile"
        if attr is not None:
            params["attr"] = attr
        if skip_to_datasource is not None:
            params["skip_to_datasource"] = skip_to_datasource
        if acs is not None:
            params["acs"] = acs
        if search is not None:
            params["search"] = search
        params.update(kwargs)
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )

    def put(
        self,
        name: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        before: str | None = None,
        after: str | None = None,
        release: int | None = None,
        access_network_type: str | None = None,
        access_network_internet: str | None = None,
        access_network_asra: str | None = None,
        access_network_esr: str | None = None,
        access_network_uesa: str | None = None,
        venue_group: str | None = None,
        venue_type: str | None = None,
        hessid: str | None = None,
        proxy_arp: str | None = None,
        l2tif: str | None = None,
        pame_bi: str | None = None,
        anqp_domain_id: int | None = None,
        domain_name: str | None = None,
        osu_ssid: str | None = None,
        gas_comeback_delay: int | None = None,
        gas_fragmentation_limit: int | None = None,
        dgaf: str | None = None,
        deauth_request_timeout: int | None = None,
        wnm_sleep_mode: str | None = None,
        bss_transition: str | None = None,
        venue_name: str | None = None,
        venue_url: str | None = None,
        roaming_consortium: str | None = None,
        nai_realm: str | None = None,
        oper_friendly_name: str | None = None,
        oper_icon: str | None = None,
        advice_of_charge: str | None = None,
        osu_provider_nai: str | None = None,
        terms_and_conditions: str | None = None,
        osu_provider: list | None = None,
        wan_metrics: str | None = None,
        network_auth: str | None = None,
        _3gpp_plmn: str | None = None,
        conn_cap: str | None = None,
        qos_map: str | None = None,
        ip_addr_type: str | None = None,
        wba_open_roaming: str | None = None,
        wba_financial_clearing_provider: str | None = None,
        wba_data_clearing_provider: str | None = None,
        wba_charging_currency: str | None = None,
        wba_charging_rate: int | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update this specific resource.

        Args:
            payload_dict: Optional dictionary of all parameters (can be passed
            as first positional arg)
            name: Object identifier (required)
            before: If *action=move*, use *before* to specify the ID of the
            resource that this resource will be moved before. (optional)
            after: If *action=move*, use *after* to specify the ID of the
            resource that this resource will be moved after. (optional)
            name: Hotspot profile name. (optional)
            release: Hotspot 2.0 Release number (1, 2, 3, default = 2).
            (optional)
            access_network_type: Access network type. (optional)
            access_network_internet: Enable/disable connectivity to the
            Internet. (optional)
            access_network_asra: Enable/disable additional step required for
            access (ASRA). (optional)
            access_network_esr: Enable/disable emergency services reachable
            (ESR). (optional)
            access_network_uesa: Enable/disable unauthenticated emergency
            service accessible (UESA). (optional)
            venue_group: Venue group. (optional)
            venue_type: Venue type. (optional)
            hessid: Homogeneous extended service set identifier (HESSID).
            (optional)
            proxy_arp: Enable/disable Proxy ARP. (optional)
            l2tif: Enable/disable Layer 2 traffic inspection and filtering.
            (optional)
            pame_bi: Enable/disable Pre-Association Message Exchange BSSID
            Independent (PAME-BI). (optional)
            anqp_domain_id: ANQP Domain ID (0-65535). (optional)
            domain_name: Domain name. (optional)
            osu_ssid: Online sign up (OSU) SSID. (optional)
            gas_comeback_delay: GAS comeback delay (0 or 100 - 10000
            milliseconds, default = 500). (optional)
            gas_fragmentation_limit: GAS fragmentation limit (512 - 4096,
            default = 1024). (optional)
            dgaf: Enable/disable downstream group-addressed forwarding (DGAF).
            (optional)
            deauth_request_timeout: Deauthentication request timeout (in
            seconds). (optional)
            wnm_sleep_mode: Enable/disable wireless network management (WNM)
            sleep mode. (optional)
            bss_transition: Enable/disable basic service set (BSS) transition
            Support. (optional)
            venue_name: Venue name. (optional)
            venue_url: Venue name. (optional)
            roaming_consortium: Roaming consortium list name. (optional)
            nai_realm: NAI realm list name. (optional)
            oper_friendly_name: Operator friendly name. (optional)
            oper_icon: Operator icon. (optional)
            advice_of_charge: Advice of charge. (optional)
            osu_provider_nai: OSU Provider NAI. (optional)
            terms_and_conditions: Terms and conditions. (optional)
            osu_provider: Manually selected list of OSU provider(s). (optional)
            wan_metrics: WAN metric name. (optional)
            network_auth: Network authentication name. (optional)
            _3gpp_plmn: 3GPP PLMN name. (optional)
            conn_cap: Connection capability name. (optional)
            qos_map: QoS MAP set ID. (optional)
            ip_addr_type: IP address type name. (optional)
            wba_open_roaming: Enable/disable WBA open roaming support.
            (optional)
            wba_financial_clearing_provider: WBA ID of financial clearing
            provider. (optional)
            wba_data_clearing_provider: WBA ID of data clearing provider.
            (optional)
            wba_charging_currency: Three letter currency code. (optional)
            wba_charging_rate: Number of currency units per kilobyte.
            (optional)
            vdom: Virtual domain name, or False to skip. Handled by HTTPClient.
            raw_json: If True, return full API response with metadata. If
            False, return only results.
            **kwargs: Additional query parameters (filter, sort, start, count,
            format, etc.)

        Common Query Parameters (via **kwargs):
            filter: Filter results (e.g., filter='name==value')
            sort: Sort results (e.g., sort='name,asc')
            start: Starting entry index for paging
            count: Maximum number of entries to return
            format: Fields to return (e.g., format='name|type')
            See FortiOS REST API documentation for full list of query
            parameters

        Returns:
            Dictionary containing API response
        """
        data_payload = payload_dict.copy() if payload_dict else {}

        # Build endpoint path
        if not name:
            raise ValueError("name is required for put()")
        endpoint = f"/wireless-controller.hotspot20/hs-profile/{name}"
        if before is not None:
            data_payload["before"] = before
        if after is not None:
            data_payload["after"] = after
        if name is not None:
            data_payload["name"] = name
        if release is not None:
            data_payload["release"] = release
        if access_network_type is not None:
            data_payload["access-network-type"] = access_network_type
        if access_network_internet is not None:
            data_payload["access-network-internet"] = access_network_internet
        if access_network_asra is not None:
            data_payload["access-network-asra"] = access_network_asra
        if access_network_esr is not None:
            data_payload["access-network-esr"] = access_network_esr
        if access_network_uesa is not None:
            data_payload["access-network-uesa"] = access_network_uesa
        if venue_group is not None:
            data_payload["venue-group"] = venue_group
        if venue_type is not None:
            data_payload["venue-type"] = venue_type
        if hessid is not None:
            data_payload["hessid"] = hessid
        if proxy_arp is not None:
            data_payload["proxy-arp"] = proxy_arp
        if l2tif is not None:
            data_payload["l2ti"] = l2tif
        if pame_bi is not None:
            data_payload["pame-bi"] = pame_bi
        if anqp_domain_id is not None:
            data_payload["anqp-domain-id"] = anqp_domain_id
        if domain_name is not None:
            data_payload["domain-name"] = domain_name
        if osu_ssid is not None:
            data_payload["osu-ssid"] = osu_ssid
        if gas_comeback_delay is not None:
            data_payload["gas-comeback-delay"] = gas_comeback_delay
        if gas_fragmentation_limit is not None:
            data_payload["gas-fragmentation-limit"] = gas_fragmentation_limit
        if dgaf is not None:
            data_payload["dga"] = dgaf
        if deauth_request_timeout is not None:
            data_payload["deauth-request-timeout"] = deauth_request_timeout
        if wnm_sleep_mode is not None:
            data_payload["wnm-sleep-mode"] = wnm_sleep_mode
        if bss_transition is not None:
            data_payload["bss-transition"] = bss_transition
        if venue_name is not None:
            data_payload["venue-name"] = venue_name
        if venue_url is not None:
            data_payload["venue-url"] = venue_url
        if roaming_consortium is not None:
            data_payload["roaming-consortium"] = roaming_consortium
        if nai_realm is not None:
            data_payload["nai-realm"] = nai_realm
        if oper_friendly_name is not None:
            data_payload["oper-friendly-name"] = oper_friendly_name
        if oper_icon is not None:
            data_payload["oper-icon"] = oper_icon
        if advice_of_charge is not None:
            data_payload["advice-of-charge"] = advice_of_charge
        if osu_provider_nai is not None:
            data_payload["osu-provider-nai"] = osu_provider_nai
        if terms_and_conditions is not None:
            data_payload["terms-and-conditions"] = terms_and_conditions
        if osu_provider is not None:
            data_payload["osu-provider"] = osu_provider
        if wan_metrics is not None:
            data_payload["wan-metrics"] = wan_metrics
        if network_auth is not None:
            data_payload["network-auth"] = network_auth
        if _3gpp_plmn is not None:
            data_payload["3gpp-plmn"] = _3gpp_plmn
        if conn_cap is not None:
            data_payload["conn-cap"] = conn_cap
        if qos_map is not None:
            data_payload["qos-map"] = qos_map
        if ip_addr_type is not None:
            data_payload["ip-addr-type"] = ip_addr_type
        if wba_open_roaming is not None:
            data_payload["wba-open-roaming"] = wba_open_roaming
        if wba_financial_clearing_provider is not None:
            data_payload["wba-financial-clearing-provider"] = (
                wba_financial_clearing_provider
            )
        if wba_data_clearing_provider is not None:
            data_payload["wba-data-clearing-provider"] = (
                wba_data_clearing_provider
            )
        if wba_charging_currency is not None:
            data_payload["wba-charging-currency"] = wba_charging_currency
        if wba_charging_rate is not None:
            data_payload["wba-charging-rate"] = wba_charging_rate
        data_payload.update(kwargs)
        return self._client.put(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )

    def delete(
        self,
        name: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Delete this specific resource.

        Args:
            name: Object identifier (required)
            vdom: Virtual domain name, or False to skip. Handled by HTTPClient.
            raw_json: If True, return full API response with metadata. If
            False, return only results.
            **kwargs: Additional query parameters (filter, sort, start, count,
            format, etc.)

        Common Query Parameters (via **kwargs):
            filter: Filter results (e.g., filter='name==value')
            sort: Sort results (e.g., sort='name,asc')
            start: Starting entry index for paging
            count: Maximum number of entries to return
            format: Fields to return (e.g., format='name|type')
            See FortiOS REST API documentation for full list of query
            parameters

        Returns:
            Dictionary containing API response
        """
        params = payload_dict.copy() if payload_dict else {}

        # Build endpoint path
        if not name:
            raise ValueError("name is required for delete()")
        endpoint = f"/wireless-controller.hotspot20/hs-profile/{name}"
        params.update(kwargs)
        return self._client.delete(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )

    def post(
        self,
        payload_dict: dict[str, Any] | None = None,
        nkey: str | None = None,
        name: str | None = None,
        release: int | None = None,
        access_network_type: str | None = None,
        access_network_internet: str | None = None,
        access_network_asra: str | None = None,
        access_network_esr: str | None = None,
        access_network_uesa: str | None = None,
        venue_group: str | None = None,
        venue_type: str | None = None,
        hessid: str | None = None,
        proxy_arp: str | None = None,
        l2tif: str | None = None,
        pame_bi: str | None = None,
        anqp_domain_id: int | None = None,
        domain_name: str | None = None,
        osu_ssid: str | None = None,
        gas_comeback_delay: int | None = None,
        gas_fragmentation_limit: int | None = None,
        dgaf: str | None = None,
        deauth_request_timeout: int | None = None,
        wnm_sleep_mode: str | None = None,
        bss_transition: str | None = None,
        venue_name: str | None = None,
        venue_url: str | None = None,
        roaming_consortium: str | None = None,
        nai_realm: str | None = None,
        oper_friendly_name: str | None = None,
        oper_icon: str | None = None,
        advice_of_charge: str | None = None,
        osu_provider_nai: str | None = None,
        terms_and_conditions: str | None = None,
        osu_provider: list | None = None,
        wan_metrics: str | None = None,
        network_auth: str | None = None,
        _3gpp_plmn: str | None = None,
        conn_cap: str | None = None,
        qos_map: str | None = None,
        ip_addr_type: str | None = None,
        wba_open_roaming: str | None = None,
        wba_financial_clearing_provider: str | None = None,
        wba_data_clearing_provider: str | None = None,
        wba_charging_currency: str | None = None,
        wba_charging_rate: int | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Create object(s) in this table.

        Args:
            payload_dict: Optional dictionary of all parameters (can be passed
            as first positional arg)
            nkey: If *action=clone*, use *nkey* to specify the ID for the new
            resource to be created. (optional)
            name: Hotspot profile name. (optional)
            release: Hotspot 2.0 Release number (1, 2, 3, default = 2).
            (optional)
            access_network_type: Access network type. (optional)
            access_network_internet: Enable/disable connectivity to the
            Internet. (optional)
            access_network_asra: Enable/disable additional step required for
            access (ASRA). (optional)
            access_network_esr: Enable/disable emergency services reachable
            (ESR). (optional)
            access_network_uesa: Enable/disable unauthenticated emergency
            service accessible (UESA). (optional)
            venue_group: Venue group. (optional)
            venue_type: Venue type. (optional)
            hessid: Homogeneous extended service set identifier (HESSID).
            (optional)
            proxy_arp: Enable/disable Proxy ARP. (optional)
            l2tif: Enable/disable Layer 2 traffic inspection and filtering.
            (optional)
            pame_bi: Enable/disable Pre-Association Message Exchange BSSID
            Independent (PAME-BI). (optional)
            anqp_domain_id: ANQP Domain ID (0-65535). (optional)
            domain_name: Domain name. (optional)
            osu_ssid: Online sign up (OSU) SSID. (optional)
            gas_comeback_delay: GAS comeback delay (0 or 100 - 10000
            milliseconds, default = 500). (optional)
            gas_fragmentation_limit: GAS fragmentation limit (512 - 4096,
            default = 1024). (optional)
            dgaf: Enable/disable downstream group-addressed forwarding (DGAF).
            (optional)
            deauth_request_timeout: Deauthentication request timeout (in
            seconds). (optional)
            wnm_sleep_mode: Enable/disable wireless network management (WNM)
            sleep mode. (optional)
            bss_transition: Enable/disable basic service set (BSS) transition
            Support. (optional)
            venue_name: Venue name. (optional)
            venue_url: Venue name. (optional)
            roaming_consortium: Roaming consortium list name. (optional)
            nai_realm: NAI realm list name. (optional)
            oper_friendly_name: Operator friendly name. (optional)
            oper_icon: Operator icon. (optional)
            advice_of_charge: Advice of charge. (optional)
            osu_provider_nai: OSU Provider NAI. (optional)
            terms_and_conditions: Terms and conditions. (optional)
            osu_provider: Manually selected list of OSU provider(s). (optional)
            wan_metrics: WAN metric name. (optional)
            network_auth: Network authentication name. (optional)
            _3gpp_plmn: 3GPP PLMN name. (optional)
            conn_cap: Connection capability name. (optional)
            qos_map: QoS MAP set ID. (optional)
            ip_addr_type: IP address type name. (optional)
            wba_open_roaming: Enable/disable WBA open roaming support.
            (optional)
            wba_financial_clearing_provider: WBA ID of financial clearing
            provider. (optional)
            wba_data_clearing_provider: WBA ID of data clearing provider.
            (optional)
            wba_charging_currency: Three letter currency code. (optional)
            wba_charging_rate: Number of currency units per kilobyte.
            (optional)
            vdom: Virtual domain name, or False to skip. Handled by HTTPClient.
            raw_json: If True, return full API response with metadata. If
            False, return only results.
            **kwargs: Additional query parameters (filter, sort, start, count,
            format, etc.)

        Common Query Parameters (via **kwargs):
            filter: Filter results (e.g., filter='name==value')
            sort: Sort results (e.g., sort='name,asc')
            start: Starting entry index for paging
            count: Maximum number of entries to return
            format: Fields to return (e.g., format='name|type')
            See FortiOS REST API documentation for full list of query
            parameters

        Returns:
            Dictionary containing API response
        """
        data_payload = payload_dict.copy() if payload_dict else {}
        endpoint = "/wireless-controller.hotspot20/hs-profile"
        if nkey is not None:
            data_payload["nkey"] = nkey
        if name is not None:
            data_payload["name"] = name
        if release is not None:
            data_payload["release"] = release
        if access_network_type is not None:
            data_payload["access-network-type"] = access_network_type
        if access_network_internet is not None:
            data_payload["access-network-internet"] = access_network_internet
        if access_network_asra is not None:
            data_payload["access-network-asra"] = access_network_asra
        if access_network_esr is not None:
            data_payload["access-network-esr"] = access_network_esr
        if access_network_uesa is not None:
            data_payload["access-network-uesa"] = access_network_uesa
        if venue_group is not None:
            data_payload["venue-group"] = venue_group
        if venue_type is not None:
            data_payload["venue-type"] = venue_type
        if hessid is not None:
            data_payload["hessid"] = hessid
        if proxy_arp is not None:
            data_payload["proxy-arp"] = proxy_arp
        if l2tif is not None:
            data_payload["l2ti"] = l2tif
        if pame_bi is not None:
            data_payload["pame-bi"] = pame_bi
        if anqp_domain_id is not None:
            data_payload["anqp-domain-id"] = anqp_domain_id
        if domain_name is not None:
            data_payload["domain-name"] = domain_name
        if osu_ssid is not None:
            data_payload["osu-ssid"] = osu_ssid
        if gas_comeback_delay is not None:
            data_payload["gas-comeback-delay"] = gas_comeback_delay
        if gas_fragmentation_limit is not None:
            data_payload["gas-fragmentation-limit"] = gas_fragmentation_limit
        if dgaf is not None:
            data_payload["dga"] = dgaf
        if deauth_request_timeout is not None:
            data_payload["deauth-request-timeout"] = deauth_request_timeout
        if wnm_sleep_mode is not None:
            data_payload["wnm-sleep-mode"] = wnm_sleep_mode
        if bss_transition is not None:
            data_payload["bss-transition"] = bss_transition
        if venue_name is not None:
            data_payload["venue-name"] = venue_name
        if venue_url is not None:
            data_payload["venue-url"] = venue_url
        if roaming_consortium is not None:
            data_payload["roaming-consortium"] = roaming_consortium
        if nai_realm is not None:
            data_payload["nai-realm"] = nai_realm
        if oper_friendly_name is not None:
            data_payload["oper-friendly-name"] = oper_friendly_name
        if oper_icon is not None:
            data_payload["oper-icon"] = oper_icon
        if advice_of_charge is not None:
            data_payload["advice-of-charge"] = advice_of_charge
        if osu_provider_nai is not None:
            data_payload["osu-provider-nai"] = osu_provider_nai
        if terms_and_conditions is not None:
            data_payload["terms-and-conditions"] = terms_and_conditions
        if osu_provider is not None:
            data_payload["osu-provider"] = osu_provider
        if wan_metrics is not None:
            data_payload["wan-metrics"] = wan_metrics
        if network_auth is not None:
            data_payload["network-auth"] = network_auth
        if _3gpp_plmn is not None:
            data_payload["3gpp-plmn"] = _3gpp_plmn
        if conn_cap is not None:
            data_payload["conn-cap"] = conn_cap
        if qos_map is not None:
            data_payload["qos-map"] = qos_map
        if ip_addr_type is not None:
            data_payload["ip-addr-type"] = ip_addr_type
        if wba_open_roaming is not None:
            data_payload["wba-open-roaming"] = wba_open_roaming
        if wba_financial_clearing_provider is not None:
            data_payload["wba-financial-clearing-provider"] = (
                wba_financial_clearing_provider
            )
        if wba_data_clearing_provider is not None:
            data_payload["wba-data-clearing-provider"] = (
                wba_data_clearing_provider
            )
        if wba_charging_currency is not None:
            data_payload["wba-charging-currency"] = wba_charging_currency
        if wba_charging_rate is not None:
            data_payload["wba-charging-rate"] = wba_charging_rate
        data_payload.update(kwargs)
        return self._client.post(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )
