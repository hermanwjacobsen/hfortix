"""
FortiOS CMDB - Wireless_controller timers

Configuration endpoint for managing cmdb wireless_controller/timers objects.

API Endpoints:
    GET    /cmdb/wireless_controller/timers
    POST   /cmdb/wireless_controller/timers
    PUT    /cmdb/wireless_controller/timers/{identifier}
    DELETE /cmdb/wireless_controller/timers/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.wireless_controller_timers.get()
    >>>
    >>> # Create with auto-normalization (strings/lists converted automatically)
    >>> result = fgt.api.cmdb.wireless_controller_timers.post(
    ...     name="example",
    ...     srcintf="port1",  # Auto-converted to [{'name': 'port1'}]
    ...     dstintf=["port2", "port3"],  # Auto-converted to list of dicts
    ... )

Important:
    - Use **POST** to create new objects
    - Use **PUT** to update existing objects
    - Use **GET** to retrieve configuration
    - Use **DELETE** to remove objects
    - **Auto-normalization**: List fields accept strings or lists, automatically
      converted to FortiOS format [{'name': '...'}]
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Union

if TYPE_CHECKING:
    from collections.abc import Coroutine
    from hfortix_core.http.interface import IHTTPClient
    from hfortix_fortios.models import FortiObject

# Import helper functions from central _helpers module
from hfortix_fortios._helpers import (
    build_api_payload,
    build_cmdb_payload,  # Keep for backward compatibility / manual usage
    is_success,
)
# Import metadata mixin for schema introspection
from hfortix_fortios._helpers.metadata_mixin import MetadataMixin

# Import Protocol-based type hints (eliminates need for local @overload decorators)
from hfortix_fortios._protocols import CRUDEndpoint

class Timers(CRUDEndpoint, MetadataMixin):
    """Timers Operations."""
    
    # Configure metadata mixin to use this endpoint's helper module
    _helper_module_name = "timers"
    
    # ========================================================================
    # Capabilities (from schema metadata)
    # ========================================================================
    SUPPORTS_CREATE = False
    SUPPORTS_READ = True
    SUPPORTS_UPDATE = True
    SUPPORTS_DELETE = False
    SUPPORTS_MOVE = True
    SUPPORTS_CLONE = True
    SUPPORTS_FILTERING = True
    SUPPORTS_PAGINATION = True
    SUPPORTS_SEARCH = False
    SUPPORTS_SORTING = False

    def __init__(self, client: "IHTTPClient"):
        """Initialize Timers endpoint."""
        self._client = client

    # ========================================================================
    # GET Method
    # Type hints provided by CRUDEndpoint protocol (no local @overload needed)
    # ========================================================================
    
    def get(
        self,
        name: str | None = None,
        filter: list[str] | None = None,
        count: int | None = None,
        start: int | None = None,
        q_datasource: bool | None = None,
        q_skip_to: int | None = None,
        q_with_meta: bool | None = None,
        q_with_contents_hash: bool | None = None,
        q_skip: bool | None = None,
        q_format: list[str] | None = None,
        q_key: str | None = None,
        q_pattern: str | None = None,
        q_scope: str | None = None,
        q_exclude_default_values: bool | None = None,
        q_datasource_format: dict[str, Any] | None = None,
        q_unfiltered_count: int | None = None,
        q_stat_items: str | None = None,
        q_primary_keys: str | None = None,
        q_action: Literal["default", "schema"] | None = None,
        payload_dict: dict[str, Any] | None = None,
        vdom: str | bool | None = None,
        error_mode: Literal["raise", "return", "print"] | None = None,
        error_format: Literal["detailed", "simple", "code_only"] | None = None,
    ):  # type: ignore[no-untyped-def]
        """
        Retrieve wireless_controller/timers configuration.

        Configure CAPWAP timers.

        Args:
            name: Name identifier to retrieve specific object. If None, returns all objects.
            filter: List of filter expressions to limit results.
                Each filter uses format: "field==value" or "field!=value"
                Operators: ==, !=, =@ (contains), !@ (not contains), <=, <, >=, >
                Multiple filters use AND logic. For OR, use comma in single string.
                Example: ["name==test", "status==enable"] or ["name==test,name==prod"]
            count: Maximum number of entries to return (pagination).
            start: Starting entry index for pagination (0-based).
            payload_dict: Additional query parameters for advanced options:
                - datasource (bool): Include datasource information
                - with_meta (bool): Include metadata about each object
                - with_contents_hash (bool): Include checksum of object contents
                - format (list[str]): Property names to include (e.g., ["policyid", "srcintf"])
                - scope (str): Query scope - "global", "vdom", or "both"
                - action (str): Special actions - "schema", "default"
                See FortiOS REST API documentation for complete list.
            vdom: Virtual domain name. Use True for global, string for specific VDOM, None for default.
            error_mode: Override client-level error_mode. "raise" raises exceptions, "return" returns error dict, "print" prints errors.
            error_format: Override client-level error_format. "detailed" provides full context, "simple" is concise, "code_only" returns just status code.

        Returns:
            FortiObject instance or list of FortiObject instances. Returns Coroutine if using async client.
            Use .dict, .json, or .raw properties to access as dictionary.
            
            Response structure:
                - http_method: GET
                - results: Configuration object(s)
                - vdom: Virtual domain
                - path: API path
                - name: Object name (single object queries)
                - status: success/error
                - http_status: HTTP status code
                - build: FortiOS build number

        Examples:
            >>> # Get all wireless_controller/timers objects
            >>> result = fgt.api.cmdb.wireless_controller_timers.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.wireless_controller_timers.get(
            ...     filter=["name==test", "status==enable"]
            ... )
            
            >>> # Get with pagination
            >>> result = fgt.api.cmdb.wireless_controller_timers.get(
            ...     start=0, count=100
            ... )
            
            >>> # Get schema information  
            >>> schema = fgt.api.cmdb.wireless_controller_timers.get_schema()

        See Also:
            - post(): Create new wireless_controller/timers object
            - put(): Update existing wireless_controller/timers object
            - delete(): Remove wireless_controller/timers object
            - exists(): Check if object exists
            - get_schema(): Get endpoint schema/metadata
        """
        params = payload_dict.copy() if payload_dict else {}
        
        # Add explicit query parameters
        if filter is not None:
            params["filter"] = filter
        if count is not None:
            params["count"] = count
        if start is not None:
            params["start"] = start
        if q_datasource is not None:
            params["datasource"] = q_datasource
        if q_skip_to is not None:
            params["skip_to"] = q_skip_to
        if q_with_meta is not None:
            params["with_meta"] = q_with_meta
        if q_with_contents_hash is not None:
            params["with_contents_hash"] = q_with_contents_hash
        if q_skip is not None:
            params["skip"] = q_skip
        if q_format is not None:
            params["format"] = q_format
        if q_key is not None:
            params["key"] = q_key
        if q_pattern is not None:
            params["pattern"] = q_pattern
        if q_scope is not None:
            params["scope"] = q_scope
        if q_exclude_default_values is not None:
            params["exclude-default-values"] = q_exclude_default_values
        if q_datasource_format is not None:
            params["datasource_format"] = q_datasource_format
        if q_unfiltered_count is not None:
            params["unfiltered_count"] = q_unfiltered_count
        if q_stat_items is not None:
            params["stat-items"] = q_stat_items
        if q_primary_keys is not None:
            params["primary_keys"] = q_primary_keys
        if q_action is not None:
            params["action"] = q_action
        
        if name:
            endpoint = f"/wireless-controller/timers/{name}"
            unwrap_single = True
        else:
            endpoint = "/wireless-controller/timers"
            unwrap_single = False
        
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, unwrap_single=unwrap_single
        )

    def get_schema(
        self,
        vdom: str | None = None,
        format: str = "schema",
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Get schema/metadata for this endpoint.
        
        Returns the FortiOS schema definition including available fields,
        their types, required vs optional properties, enum values, nested
        structures, and default values.
        
        This queries the live firewall for its current schema, which may
        vary between FortiOS versions.
        
        Args:
            vdom: Virtual domain. None uses default VDOM.
            format: Schema format - "schema" (FortiOS native) or "json-schema" (JSON Schema standard).
                Defaults to "schema".
                
        Returns:
            Schema definition as dict. Returns Coroutine if using async client.
            
        Example:
            >>> # Get FortiOS native schema
            >>> schema = fgt.api.cmdb.wireless_controller_timers.get_schema()
            >>> print(schema['results'])
            
            >>> # Get JSON Schema format (if supported)
            >>> json_schema = fgt.api.cmdb.wireless_controller_timers.get_schema(format="json-schema")
        
        Note:
            Not all endpoints support all schema formats. The "schema" format
            is most widely supported.
        """
        return self.get(action=format, vdom=vdom)


    # ========================================================================
    # PUT Method
    # Type hints provided by CRUDEndpoint protocol (no local @overload needed)
    # ========================================================================
    
    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        echo_interval: int | None = None,
        nat_session_keep_alive: int | None = None,
        discovery_interval: int | None = None,
        client_idle_timeout: int | None = None,
        client_idle_rehome_timeout: int | None = None,
        auth_timeout: int | None = None,
        rogue_ap_log: int | None = None,
        fake_ap_log: int | None = None,
        sta_offline_cleanup: int | None = None,
        sta_offline_ip2mac_cleanup: int | None = None,
        sta_cap_cleanup: int | None = None,
        rogue_ap_cleanup: int | None = None,
        rogue_sta_cleanup: int | None = None,
        wids_entry_cleanup: int | None = None,
        ble_device_cleanup: int | None = None,
        sta_stats_interval: int | None = None,
        vap_stats_interval: int | None = None,
        radio_stats_interval: int | None = None,
        sta_capability_interval: int | None = None,
        sta_locate_timer: int | None = None,
        ipsec_intf_cleanup: int | None = None,
        ble_scan_report_intv: int | None = None,
        drma_interval: int | None = None,
        ap_reboot_wait_interval1: int | None = None,
        ap_reboot_wait_time: str | None = None,
        ap_reboot_wait_interval2: int | None = None,
        q_action: Literal["move"] | None = None,
        q_before: str | None = None,
        q_after: str | None = None,
        q_scope: str | None = None,
        vdom: str | bool | None = None,
        error_mode: Literal["raise", "return", "print"] | None = None,
        error_format: Literal["detailed", "simple", "code_only"] | None = None,
    ):  # type: ignore[no-untyped-def]
        """
        Update existing wireless_controller/timers object.

        Configure CAPWAP timers.

        Args:
            payload_dict: Object data as dict. Must include name (primary key).
            echo_interval: Time between echo requests sent by the managed WTP, AP, or FortiAP (1 - 255 sec, default = 30).
            nat_session_keep_alive: Maximal time in seconds between control requests sent by the managed WTP, AP, or FortiAP (0 - 255 sec, default = 0).
            discovery_interval: Time between discovery requests (2 - 180 sec, default = 5).
            client_idle_timeout: Time after which a client is considered idle and times out (20 - 3600 sec, default = 300, 0 for no timeout).
            client_idle_rehome_timeout: Time after which a client is considered idle and disconnected from the home controller (2 - 3600 sec, default = 20, 0 for no timeout).
            auth_timeout: Time after which a client is considered failed in RADIUS authentication and times out (5 - 30 sec, default = 5).
            rogue_ap_log: Time between logging rogue AP messages if periodic rogue AP logging is configured (0 - 1440 min, default = 0).
            fake_ap_log: Time between recording logs about fake APs if periodic fake AP logging is configured (1 - 1440 min, default = 1).
            sta_offline_cleanup: Time period in seconds to keep station offline data after it is gone (default = 300).
            sta_offline_ip2mac_cleanup: Time period in seconds to keep station offline Ip2mac data after it is gone (default = 300).
            sta_cap_cleanup: Time period in minutes to keep station capability data after it is gone (default = 0).
            rogue_ap_cleanup: Time period in minutes to keep rogue AP after it is gone (default = 0).
            rogue_sta_cleanup: Time period in minutes to keep rogue station after it is gone (default = 0).
            wids_entry_cleanup: Time period in minutes to keep wids entry after it is gone (default = 0).
            ble_device_cleanup: Time period in minutes to keep BLE device after it is gone (default = 60).
            sta_stats_interval: Time between running client (station) reports (1 - 255 sec, default = 10).
            vap_stats_interval: Time between running Virtual Access Point (VAP) reports (1 - 255 sec, default = 15).
            radio_stats_interval: Time between running radio reports (1 - 255 sec, default = 15).
            sta_capability_interval: Time between running station capability reports (1 - 255 sec, default = 30).
            sta_locate_timer: Time between running client presence flushes to remove clients that are listed but no longer present (0 - 86400 sec, default = 1800).
            ipsec_intf_cleanup: Time period to keep IPsec VPN interfaces up after WTP sessions are disconnected (30 - 3600 sec, default = 120).
            ble_scan_report_intv: Time between running Bluetooth Low Energy (BLE) reports (10 - 3600 sec, default = 30).
            drma_interval: Dynamic radio mode assignment (DRMA) schedule interval in minutes (1 - 1440, default = 60).
            ap_reboot_wait_interval1: Time in minutes to wait before AP reboots when there is no controller detected (5 - 65535, default = 0, 0 for no reboot).
            ap_reboot_wait_time: Time to reboot the AP when there is no controller detected and standalone SSIDs are pushed to the AP in the previous session, format hh:mm.
            ap_reboot_wait_interval2: Time in minutes to wait before AP reboots when there is no controller detected and standalone SSIDs are pushed to the AP in the previous session (5 - 65535, default = 0, 0 for no reboot).
            vdom: Virtual domain name.
            error_mode: Override client-level error_mode. "raise" raises exceptions, "return" returns error dict, "print" prints errors.
            error_format: Override client-level error_format. "detailed" provides full context, "simple" is concise, "code_only" returns just status code.

        Returns:
            FortiObject instance. Use .dict, .json, or .raw to access as dictionary.

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.wireless_controller_timers.put(
            ...     name="existing-object",
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "name": "existing-object",
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.wireless_controller_timers.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Build payload using helper function with auto-normalization
        # This automatically converts strings/lists to [{'name': '...'}] format for list fields
        # To disable auto-normalization, use build_cmdb_payload directly
        payload_data = build_api_payload(
            echo_interval=echo_interval,
            nat_session_keep_alive=nat_session_keep_alive,
            discovery_interval=discovery_interval,
            client_idle_timeout=client_idle_timeout,
            client_idle_rehome_timeout=client_idle_rehome_timeout,
            auth_timeout=auth_timeout,
            rogue_ap_log=rogue_ap_log,
            fake_ap_log=fake_ap_log,
            sta_offline_cleanup=sta_offline_cleanup,
            sta_offline_ip2mac_cleanup=sta_offline_ip2mac_cleanup,
            sta_cap_cleanup=sta_cap_cleanup,
            rogue_ap_cleanup=rogue_ap_cleanup,
            rogue_sta_cleanup=rogue_sta_cleanup,
            wids_entry_cleanup=wids_entry_cleanup,
            ble_device_cleanup=ble_device_cleanup,
            sta_stats_interval=sta_stats_interval,
            vap_stats_interval=vap_stats_interval,
            radio_stats_interval=radio_stats_interval,
            sta_capability_interval=sta_capability_interval,
            sta_locate_timer=sta_locate_timer,
            ipsec_intf_cleanup=ipsec_intf_cleanup,
            ble_scan_report_intv=ble_scan_report_intv,
            drma_interval=drma_interval,
            ap_reboot_wait_interval1=ap_reboot_wait_interval1,
            ap_reboot_wait_time=ap_reboot_wait_time,
            ap_reboot_wait_interval2=ap_reboot_wait_interval2,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.timers import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/wireless_controller/timers",
            )
        
        # Singleton endpoint - no identifier needed
        endpoint = "/wireless-controller/timers"

        # Add explicit query parameters for PUT
        params: dict[str, Any] = {}
        if q_action is not None:
            params["action"] = q_action
        if q_before is not None:
            params["before"] = q_before
        if q_after is not None:
            params["after"] = q_after
        if q_scope is not None:
            params["scope"] = q_scope
        
        return self._client.put(
            "cmdb", endpoint, data=payload_data, params=params, vdom=vdom
        )





    # ========================================================================
    # Action: Move
    # ========================================================================
    
    def move(
        self,
        name: str,
        action: Literal["before", "after"],
        reference_name: str,
        vdom: str | bool | None = None,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Move wireless_controller/timers object to a new position.
        
        Reorders objects by moving one before or after another.
        
        Args:
            name: Name of object to move
            action: Move "before" or "after" reference object
            reference_name: Name of reference object
            vdom: Virtual domain name
            **kwargs: Additional parameters
            
        Returns:
            API response dictionary
            
        Example:
            >>> # Move policy 100 before policy 50
            >>> fgt.api.cmdb.wireless_controller_timers.move(
            ...     name="object1",
            ...     action="before",
            ...     reference_name="object2"
            ... )
        """
        return self._client.request(
            method="PUT",
            path=f"/api/v2/cmdb/wireless-controller/timers",
            params={
                "name": name,
                "action": "move",
                action: reference_name,
                "vdom": vdom,
                **kwargs,
            },
        )

    # ========================================================================
    # Action: Clone
    # ========================================================================
    
    def clone(
        self,
        name: str,
        new_name: str,
        vdom: str | bool | None = None,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Clone wireless_controller/timers object.
        
        Creates a copy of an existing object with a new identifier.
        
        Args:
            name: Name of object to clone
            new_name: Name for the cloned object
            vdom: Virtual domain name
            **kwargs: Additional parameters
            
        Returns:
            API response dictionary
            
        Example:
            >>> # Clone an existing object
            >>> fgt.api.cmdb.wireless_controller_timers.clone(
            ...     name="template",
            ...     new_name="new-from-template"
            ... )
        """
        return self._client.request(
            method="POST",
            path=f"/api/v2/cmdb/wireless-controller/timers",
            params={
                "name": name,
                "new_name": new_name,
                "action": "clone",
                "vdom": vdom,
                **kwargs,
            },
        )

    # ========================================================================
    # Helper: Check Existence
    # ========================================================================
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = None,
    ) -> bool:
        """
        Check if wireless_controller/timers object exists.
        
        Args:
            name: Name to check
            vdom: Virtual domain name
            
        Returns:
            True if object exists, False otherwise
            
        Example:
            >>> # Check before creating
            >>> if not fgt.api.cmdb.wireless_controller_timers.exists(name="myobj"):
            ...     fgt.api.cmdb.wireless_controller_timers.post(payload_dict=data)
        """
        # Try to fetch the object - 404 means it doesn't exist
        try:
            result = self.get(
                name=name,
                vdom=vdom
            )
            response = result.raw if hasattr(result, 'raw') else result
            # Check if response indicates success
            return is_success(response)
        except Exception as e:
            # 404 means object doesn't exist - return False
            # Any other error should be re-raised
            error_str = str(e)
            if '404' in error_str or 'Not Found' in error_str or 'ResourceNotFoundError' in str(type(e)):
                return False
            raise

