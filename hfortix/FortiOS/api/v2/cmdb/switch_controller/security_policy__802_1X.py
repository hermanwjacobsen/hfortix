"""
FortiOS CMDB - Cmdb Switch Controller Security Policy 802 1x

Configuration endpoint for managing cmdb switch controller security policy 802
1x objects.

API Endpoints:
    GET    /cmdb/switch-controller/security_policy__802_1X
    POST   /cmdb/switch-controller/security_policy__802_1X
    GET    /cmdb/switch-controller/security_policy__802_1X
    PUT    /cmdb/switch-controller/security_policy__802_1X/{identifier}
    DELETE /cmdb/switch-controller/security_policy__802_1X/{identifier}

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.switch_controller.security_policy__802_1X.get()
    >>>
    >>> # Get specific item (if supported)
    >>> item =
    fgt.api.cmdb.switch_controller.security_policy__802_1X.get(name="item_name")
    >>>
    >>> # Create new item (use POST)
    >>> result = fgt.api.cmdb.switch_controller.security_policy__802_1X.post(
    ...     name="new_item",
    ...     # ... additional parameters
    ... )
    >>>
    >>> # Update existing item (use PUT)
    >>> result = fgt.api.cmdb.switch_controller.security_policy__802_1X.put(
    ...     name="existing_item",
    ...     # ... parameters to update
    ... )
    >>>
    >>> # Delete item
    >>> result =
    fgt.api.cmdb.switch_controller.security_policy__802_1X.delete(name="item_name")

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


class SecurityPolicyEight02OneX:
    """
    Securitypolicyeight02Onex Operations.

    Provides CRUD operations for FortiOS securitypolicyeight02onex
    configuration.

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
        Initialize SecurityPolicyEight02OneX endpoint.

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
            endpoint = f"/switch-controller.security-policy/802-1X/{name}"
        else:
            endpoint = "/switch-controller.security-policy/802-1X"
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
        security_mode: str | None = None,
        user_group: list | None = None,
        mac_auth_bypass: str | None = None,
        auth_order: str | None = None,
        auth_priority: str | None = None,
        open_auth: str | None = None,
        eap_passthru: str | None = None,
        eap_auto_untagged_vlans: str | None = None,
        guest_vlan: str | None = None,
        guest_vlan_id: str | None = None,
        guest_auth_delay: int | None = None,
        auth_fail_vlan: str | None = None,
        auth_fail_vlan_id: str | None = None,
        framevid_apply: str | None = None,
        radius_timeout_overwrite: str | None = None,
        policy_type: str | None = None,
        authserver_timeout_period: int | None = None,
        authserver_timeout_vlan: str | None = None,
        authserver_timeout_vlanid: str | None = None,
        authserver_timeout_tagged: str | None = None,
        authserver_timeout_tagged_vlanid: str | None = None,
        dacl: str | None = None,
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
            name: Policy name. (optional)
            security_mode: Port or MAC based 802.1X security mode. (optional)
            user_group: Name of user-group to assign to this MAC Authentication
            Bypass (MAB) policy. (optional)
            mac_auth_bypass: Enable/disable MAB for this policy. (optional)
            auth_order: Configure authentication order. (optional)
            auth_priority: Configure authentication priority. (optional)
            open_auth: Enable/disable open authentication for this policy.
            (optional)
            eap_passthru: Enable/disable EAP pass-through mode, allowing
            protocols (such as LLDP) to pass through ports for more flexible
            authentication. (optional)
            eap_auto_untagged_vlans: Enable/disable automatic inclusion of
            untagged VLANs. (optional)
            guest_vlan: Enable the guest VLAN feature to allow limited access
            to non-802.1X-compliant clients. (optional)
            guest_vlan_id: Guest VLAN name. (optional)
            guest_auth_delay: Guest authentication delay (1 - 900 sec, default
            = 30). (optional)
            auth_fail_vlan: Enable to allow limited access to clients that
            cannot authenticate. (optional)
            auth_fail_vlan_id: VLAN ID on which authentication failed.
            (optional)
            framevid_apply: Enable/disable the capability to apply the EAP/MAB
            frame VLAN to the port native VLAN. (optional)
            radius_timeout_overwrite: Enable to override the global RADIUS
            session timeout. (optional)
            policy_type: Policy type. (optional)
            authserver_timeout_period: Authentication server timeout period (3
            - 15 sec, default = 3). (optional)
            authserver_timeout_vlan: Enable/disable the authentication server
            timeout VLAN to allow limited access when RADIUS is unavailable.
            (optional)
            authserver_timeout_vlanid: Authentication server timeout VLAN name.
            (optional)
            authserver_timeout_tagged: Configure timeout option for the tagged
            VLAN which allows limited access when the authentication server is
            unavailable. (optional)
            authserver_timeout_tagged_vlanid: Tagged VLAN name for which the
            timeout option is applied to (only one VLAN ID). (optional)
            dacl: Enable/disable dynamic access control list on this interface.
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
        endpoint = f"/switch-controller.security-policy/802-1X/{name}"
        if before is not None:
            data_payload["before"] = before
        if after is not None:
            data_payload["after"] = after
        if name is not None:
            data_payload["name"] = name
        if security_mode is not None:
            data_payload["security-mode"] = security_mode
        if user_group is not None:
            data_payload["user-group"] = user_group
        if mac_auth_bypass is not None:
            data_payload["mac-auth-bypass"] = mac_auth_bypass
        if auth_order is not None:
            data_payload["auth-order"] = auth_order
        if auth_priority is not None:
            data_payload["auth-priority"] = auth_priority
        if open_auth is not None:
            data_payload["open-auth"] = open_auth
        if eap_passthru is not None:
            data_payload["eap-passthru"] = eap_passthru
        if eap_auto_untagged_vlans is not None:
            data_payload["eap-auto-untagged-vlans"] = eap_auto_untagged_vlans
        if guest_vlan is not None:
            data_payload["guest-vlan"] = guest_vlan
        if guest_vlan_id is not None:
            data_payload["guest-vlan-id"] = guest_vlan_id
        if guest_auth_delay is not None:
            data_payload["guest-auth-delay"] = guest_auth_delay
        if auth_fail_vlan is not None:
            data_payload["auth-fail-vlan"] = auth_fail_vlan
        if auth_fail_vlan_id is not None:
            data_payload["auth-fail-vlan-id"] = auth_fail_vlan_id
        if framevid_apply is not None:
            data_payload["framevid-apply"] = framevid_apply
        if radius_timeout_overwrite is not None:
            data_payload["radius-timeout-overwrite"] = radius_timeout_overwrite
        if policy_type is not None:
            data_payload["policy-type"] = policy_type
        if authserver_timeout_period is not None:
            data_payload["authserver-timeout-period"] = (
                authserver_timeout_period
            )
        if authserver_timeout_vlan is not None:
            data_payload["authserver-timeout-vlan"] = authserver_timeout_vlan
        if authserver_timeout_vlanid is not None:
            data_payload["authserver-timeout-vlanid"] = (
                authserver_timeout_vlanid
            )
        if authserver_timeout_tagged is not None:
            data_payload["authserver-timeout-tagged"] = (
                authserver_timeout_tagged
            )
        if authserver_timeout_tagged_vlanid is not None:
            data_payload["authserver-timeout-tagged-vlanid"] = (
                authserver_timeout_tagged_vlanid
            )
        if dacl is not None:
            data_payload["dacl"] = dacl
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
        endpoint = f"/switch-controller.security-policy/802-1X/{name}"
        params.update(kwargs)
        return self._client.delete(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )

    def post(
        self,
        payload_dict: dict[str, Any] | None = None,
        nkey: str | None = None,
        name: str | None = None,
        security_mode: str | None = None,
        user_group: list | None = None,
        mac_auth_bypass: str | None = None,
        auth_order: str | None = None,
        auth_priority: str | None = None,
        open_auth: str | None = None,
        eap_passthru: str | None = None,
        eap_auto_untagged_vlans: str | None = None,
        guest_vlan: str | None = None,
        guest_vlan_id: str | None = None,
        guest_auth_delay: int | None = None,
        auth_fail_vlan: str | None = None,
        auth_fail_vlan_id: str | None = None,
        framevid_apply: str | None = None,
        radius_timeout_overwrite: str | None = None,
        policy_type: str | None = None,
        authserver_timeout_period: int | None = None,
        authserver_timeout_vlan: str | None = None,
        authserver_timeout_vlanid: str | None = None,
        authserver_timeout_tagged: str | None = None,
        authserver_timeout_tagged_vlanid: str | None = None,
        dacl: str | None = None,
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
            name: Policy name. (optional)
            security_mode: Port or MAC based 802.1X security mode. (optional)
            user_group: Name of user-group to assign to this MAC Authentication
            Bypass (MAB) policy. (optional)
            mac_auth_bypass: Enable/disable MAB for this policy. (optional)
            auth_order: Configure authentication order. (optional)
            auth_priority: Configure authentication priority. (optional)
            open_auth: Enable/disable open authentication for this policy.
            (optional)
            eap_passthru: Enable/disable EAP pass-through mode, allowing
            protocols (such as LLDP) to pass through ports for more flexible
            authentication. (optional)
            eap_auto_untagged_vlans: Enable/disable automatic inclusion of
            untagged VLANs. (optional)
            guest_vlan: Enable the guest VLAN feature to allow limited access
            to non-802.1X-compliant clients. (optional)
            guest_vlan_id: Guest VLAN name. (optional)
            guest_auth_delay: Guest authentication delay (1 - 900 sec, default
            = 30). (optional)
            auth_fail_vlan: Enable to allow limited access to clients that
            cannot authenticate. (optional)
            auth_fail_vlan_id: VLAN ID on which authentication failed.
            (optional)
            framevid_apply: Enable/disable the capability to apply the EAP/MAB
            frame VLAN to the port native VLAN. (optional)
            radius_timeout_overwrite: Enable to override the global RADIUS
            session timeout. (optional)
            policy_type: Policy type. (optional)
            authserver_timeout_period: Authentication server timeout period (3
            - 15 sec, default = 3). (optional)
            authserver_timeout_vlan: Enable/disable the authentication server
            timeout VLAN to allow limited access when RADIUS is unavailable.
            (optional)
            authserver_timeout_vlanid: Authentication server timeout VLAN name.
            (optional)
            authserver_timeout_tagged: Configure timeout option for the tagged
            VLAN which allows limited access when the authentication server is
            unavailable. (optional)
            authserver_timeout_tagged_vlanid: Tagged VLAN name for which the
            timeout option is applied to (only one VLAN ID). (optional)
            dacl: Enable/disable dynamic access control list on this interface.
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
        endpoint = "/switch-controller.security-policy/802-1X"
        if nkey is not None:
            data_payload["nkey"] = nkey
        if name is not None:
            data_payload["name"] = name
        if security_mode is not None:
            data_payload["security-mode"] = security_mode
        if user_group is not None:
            data_payload["user-group"] = user_group
        if mac_auth_bypass is not None:
            data_payload["mac-auth-bypass"] = mac_auth_bypass
        if auth_order is not None:
            data_payload["auth-order"] = auth_order
        if auth_priority is not None:
            data_payload["auth-priority"] = auth_priority
        if open_auth is not None:
            data_payload["open-auth"] = open_auth
        if eap_passthru is not None:
            data_payload["eap-passthru"] = eap_passthru
        if eap_auto_untagged_vlans is not None:
            data_payload["eap-auto-untagged-vlans"] = eap_auto_untagged_vlans
        if guest_vlan is not None:
            data_payload["guest-vlan"] = guest_vlan
        if guest_vlan_id is not None:
            data_payload["guest-vlan-id"] = guest_vlan_id
        if guest_auth_delay is not None:
            data_payload["guest-auth-delay"] = guest_auth_delay
        if auth_fail_vlan is not None:
            data_payload["auth-fail-vlan"] = auth_fail_vlan
        if auth_fail_vlan_id is not None:
            data_payload["auth-fail-vlan-id"] = auth_fail_vlan_id
        if framevid_apply is not None:
            data_payload["framevid-apply"] = framevid_apply
        if radius_timeout_overwrite is not None:
            data_payload["radius-timeout-overwrite"] = radius_timeout_overwrite
        if policy_type is not None:
            data_payload["policy-type"] = policy_type
        if authserver_timeout_period is not None:
            data_payload["authserver-timeout-period"] = (
                authserver_timeout_period
            )
        if authserver_timeout_vlan is not None:
            data_payload["authserver-timeout-vlan"] = authserver_timeout_vlan
        if authserver_timeout_vlanid is not None:
            data_payload["authserver-timeout-vlanid"] = (
                authserver_timeout_vlanid
            )
        if authserver_timeout_tagged is not None:
            data_payload["authserver-timeout-tagged"] = (
                authserver_timeout_tagged
            )
        if authserver_timeout_tagged_vlanid is not None:
            data_payload["authserver-timeout-tagged-vlanid"] = (
                authserver_timeout_tagged_vlanid
            )
        if dacl is not None:
            data_payload["dacl"] = dacl
        data_payload.update(kwargs)
        return self._client.post(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )
