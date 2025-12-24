"""
FortiOS CMDB - Cmdb Switch Controller Lldp Profile

Configuration endpoint for managing cmdb switch controller lldp profile
objects.

API Endpoints:
    GET    /cmdb/switch-controller/lldp_profile
    POST   /cmdb/switch-controller/lldp_profile
    GET    /cmdb/switch-controller/lldp_profile
    PUT    /cmdb/switch-controller/lldp_profile/{identifier}
    DELETE /cmdb/switch-controller/lldp_profile/{identifier}

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.switch_controller.lldp_profile.get()
    >>>
    >>> # Get specific item (if supported)
    >>> item =
    fgt.api.cmdb.switch_controller.lldp_profile.get(name="item_name")
    >>>
    >>> # Create new item (use POST)
    >>> result = fgt.api.cmdb.switch_controller.lldp_profile.post(
    ...     name="new_item",
    ...     # ... additional parameters
    ... )
    >>>
    >>> # Update existing item (use PUT)
    >>> result = fgt.api.cmdb.switch_controller.lldp_profile.put(
    ...     name="existing_item",
    ...     # ... parameters to update
    ... )
    >>>
    >>> # Delete item
    >>> result =
    fgt.api.cmdb.switch_controller.lldp_profile.delete(name="item_name")

Important:
    - Use **POST** to create new objects (404 error if already exists)
    - Use **PUT** to update existing objects (404 error if doesn't exist)
    - Use **GET** to retrieve configuration (no changes made)
    - Use **DELETE** to remove objects (404 error if doesn't exist)
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Union, cast

if TYPE_CHECKING:
    from collections.abc import Coroutine

    from hfortix.FortiOS.http_client_interface import IHTTPClient


class LldpProfile:
    """
    Lldpprofile Operations.

    Provides CRUD operations for FortiOS lldpprofile configuration.

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
        Initialize LldpProfile endpoint.

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
            endpoint = f"/switch-controller/lldp-profile/{name}"
        else:
            endpoint = "/switch-controller/lldp-profile"
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
        med_tlvs: str | None = None,
        _802_1_tlvs: str | None = None,
        _802_3_tlvs: str | None = None,
        auto_isl: str | None = None,
        auto_isl_hello_timer: int | None = None,
        auto_isl_receive_timeout: int | None = None,
        auto_isl_port_group: int | None = None,
        auto_mclag_icl: str | None = None,
        auto_isl_auth: str | None = None,
        auto_isl_auth_user: str | None = None,
        auto_isl_auth_identity: str | None = None,
        auto_isl_auth_reauth: int | None = None,
        auto_isl_auth_encrypt: str | None = None,
        auto_isl_auth_macsec_profile: str | None = None,
        med_network_policy: list | None = None,
        med_location_service: list | None = None,
        custom_tlvs: list | None = None,
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
            name: Profile name. (optional)
            med_tlvs: Transmitted LLDP-MED TLVs (type-length-value
            descriptions). (optional)
            _802_1_tlvs: Transmitted IEEE 802.1 TLVs. (optional)
            _802_3_tlvs: Transmitted IEEE 802.3 TLVs. (optional)
            auto_isl: Enable/disable auto inter-switch LAG. (optional)
            auto_isl_hello_timer: Auto inter-switch LAG hello timer duration (1
            - 30 sec, default = 3). (optional)
            auto_isl_receive_timeout: Auto inter-switch LAG timeout if no
            response is received (3 - 90 sec, default = 9). (optional)
            auto_isl_port_group: Auto inter-switch LAG port group ID (0 - 9).
            (optional)
            auto_mclag_icl: Enable/disable MCLAG inter chassis link. (optional)
            auto_isl_auth: Auto inter-switch LAG authentication mode.
            (optional)
            auto_isl_auth_user: Auto inter-switch LAG authentication user
            certificate. (optional)
            auto_isl_auth_identity: Auto inter-switch LAG authentication
            identity. (optional)
            auto_isl_auth_reauth: Auto inter-switch LAG authentication reauth
            period in seconds(10 - 3600, default = 3600). (optional)
            auto_isl_auth_encrypt: Auto inter-switch LAG encryption mode.
            (optional)
            auto_isl_auth_macsec_profile: Auto inter-switch LAG macsec profile
            for encryption. (optional)
            med_network_policy: Configuration method to edit Media Endpoint
            Discovery (MED) network policy type-length-value (TLV) categories.
            (optional)
            med_location_service: Configuration method to edit Media Endpoint
            Discovery (MED) location service type-length-value (TLV)
            categories. (optional)
            custom_tlvs: Configuration method to edit custom TLV entries.
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
        endpoint = f"/switch-controller/lldp-profile/{name}"
        if before is not None:
            data_payload["before"] = before
        if after is not None:
            data_payload["after"] = after
        if name is not None:
            data_payload["name"] = name
        if med_tlvs is not None:
            data_payload["med-tlvs"] = med_tlvs
        if _802_1_tlvs is not None:
            data_payload["802.1-tlvs"] = _802_1_tlvs
        if _802_3_tlvs is not None:
            data_payload["802.3-tlvs"] = _802_3_tlvs
        if auto_isl is not None:
            data_payload["auto-isl"] = auto_isl
        if auto_isl_hello_timer is not None:
            data_payload["auto-isl-hello-timer"] = auto_isl_hello_timer
        if auto_isl_receive_timeout is not None:
            data_payload["auto-isl-receive-timeout"] = auto_isl_receive_timeout
        if auto_isl_port_group is not None:
            data_payload["auto-isl-port-group"] = auto_isl_port_group
        if auto_mclag_icl is not None:
            data_payload["auto-mclag-icl"] = auto_mclag_icl
        if auto_isl_auth is not None:
            data_payload["auto-isl-auth"] = auto_isl_auth
        if auto_isl_auth_user is not None:
            data_payload["auto-isl-auth-user"] = auto_isl_auth_user
        if auto_isl_auth_identity is not None:
            data_payload["auto-isl-auth-identity"] = auto_isl_auth_identity
        if auto_isl_auth_reauth is not None:
            data_payload["auto-isl-auth-reauth"] = auto_isl_auth_reauth
        if auto_isl_auth_encrypt is not None:
            data_payload["auto-isl-auth-encrypt"] = auto_isl_auth_encrypt
        if auto_isl_auth_macsec_profile is not None:
            data_payload["auto-isl-auth-macsec-profile"] = (
                auto_isl_auth_macsec_profile
            )
        if med_network_policy is not None:
            data_payload["med-network-policy"] = med_network_policy
        if med_location_service is not None:
            data_payload["med-location-service"] = med_location_service
        if custom_tlvs is not None:
            data_payload["custom-tlvs"] = custom_tlvs
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
        endpoint = f"/switch-controller/lldp-profile/{name}"
        params.update(kwargs)
        return self._client.delete(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )

    def exists(
        self,
        name: str,
        vdom: str | bool | None = None,
    ) -> Union[bool, Coroutine[Any, Any, bool]]:
        """
        Check if an object exists.

        Args:
            name: Object identifier
            vdom: Virtual domain name, or False to skip. Handled by HTTPClient.

        Returns:
            True if object exists, False otherwise

        Example:
            >>> if fgt.api.cmdb.firewall.address.exists("server1"):
            ...     print("Address exists")
        """
        import inspect

        from hfortix.FortiOS.exceptions_forti import ResourceNotFoundError

        # Call get() - returns dict (sync) or coroutine (async)
        result = self.get(name=name, vdom=vdom)

        # Check if async mode
        if inspect.iscoroutine(result):

            async def _async():
                try:
                    # Runtime check confirms result is a coroutine, cast for
                    # mypy
                    await cast(Coroutine[Any, Any, dict[str, Any]], result)
                    return True
                except ResourceNotFoundError:
                    return False

            # Type ignore justified: mypy can't verify Union return type
            # narrowing

            return _async()
        # Sync mode - get() already executed, no exception means it exists
        return True

    def post(
        self,
        payload_dict: dict[str, Any] | None = None,
        nkey: str | None = None,
        name: str | None = None,
        med_tlvs: str | None = None,
        _802_1_tlvs: str | None = None,
        _802_3_tlvs: str | None = None,
        auto_isl: str | None = None,
        auto_isl_hello_timer: int | None = None,
        auto_isl_receive_timeout: int | None = None,
        auto_isl_port_group: int | None = None,
        auto_mclag_icl: str | None = None,
        auto_isl_auth: str | None = None,
        auto_isl_auth_user: str | None = None,
        auto_isl_auth_identity: str | None = None,
        auto_isl_auth_reauth: int | None = None,
        auto_isl_auth_encrypt: str | None = None,
        auto_isl_auth_macsec_profile: str | None = None,
        med_network_policy: list | None = None,
        med_location_service: list | None = None,
        custom_tlvs: list | None = None,
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
            name: Profile name. (optional)
            med_tlvs: Transmitted LLDP-MED TLVs (type-length-value
            descriptions). (optional)
            _802_1_tlvs: Transmitted IEEE 802.1 TLVs. (optional)
            _802_3_tlvs: Transmitted IEEE 802.3 TLVs. (optional)
            auto_isl: Enable/disable auto inter-switch LAG. (optional)
            auto_isl_hello_timer: Auto inter-switch LAG hello timer duration (1
            - 30 sec, default = 3). (optional)
            auto_isl_receive_timeout: Auto inter-switch LAG timeout if no
            response is received (3 - 90 sec, default = 9). (optional)
            auto_isl_port_group: Auto inter-switch LAG port group ID (0 - 9).
            (optional)
            auto_mclag_icl: Enable/disable MCLAG inter chassis link. (optional)
            auto_isl_auth: Auto inter-switch LAG authentication mode.
            (optional)
            auto_isl_auth_user: Auto inter-switch LAG authentication user
            certificate. (optional)
            auto_isl_auth_identity: Auto inter-switch LAG authentication
            identity. (optional)
            auto_isl_auth_reauth: Auto inter-switch LAG authentication reauth
            period in seconds(10 - 3600, default = 3600). (optional)
            auto_isl_auth_encrypt: Auto inter-switch LAG encryption mode.
            (optional)
            auto_isl_auth_macsec_profile: Auto inter-switch LAG macsec profile
            for encryption. (optional)
            med_network_policy: Configuration method to edit Media Endpoint
            Discovery (MED) network policy type-length-value (TLV) categories.
            (optional)
            med_location_service: Configuration method to edit Media Endpoint
            Discovery (MED) location service type-length-value (TLV)
            categories. (optional)
            custom_tlvs: Configuration method to edit custom TLV entries.
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
        endpoint = "/switch-controller/lldp-profile"
        if nkey is not None:
            data_payload["nkey"] = nkey
        if name is not None:
            data_payload["name"] = name
        if med_tlvs is not None:
            data_payload["med-tlvs"] = med_tlvs
        if _802_1_tlvs is not None:
            data_payload["802.1-tlvs"] = _802_1_tlvs
        if _802_3_tlvs is not None:
            data_payload["802.3-tlvs"] = _802_3_tlvs
        if auto_isl is not None:
            data_payload["auto-isl"] = auto_isl
        if auto_isl_hello_timer is not None:
            data_payload["auto-isl-hello-timer"] = auto_isl_hello_timer
        if auto_isl_receive_timeout is not None:
            data_payload["auto-isl-receive-timeout"] = auto_isl_receive_timeout
        if auto_isl_port_group is not None:
            data_payload["auto-isl-port-group"] = auto_isl_port_group
        if auto_mclag_icl is not None:
            data_payload["auto-mclag-icl"] = auto_mclag_icl
        if auto_isl_auth is not None:
            data_payload["auto-isl-auth"] = auto_isl_auth
        if auto_isl_auth_user is not None:
            data_payload["auto-isl-auth-user"] = auto_isl_auth_user
        if auto_isl_auth_identity is not None:
            data_payload["auto-isl-auth-identity"] = auto_isl_auth_identity
        if auto_isl_auth_reauth is not None:
            data_payload["auto-isl-auth-reauth"] = auto_isl_auth_reauth
        if auto_isl_auth_encrypt is not None:
            data_payload["auto-isl-auth-encrypt"] = auto_isl_auth_encrypt
        if auto_isl_auth_macsec_profile is not None:
            data_payload["auto-isl-auth-macsec-profile"] = (
                auto_isl_auth_macsec_profile
            )
        if med_network_policy is not None:
            data_payload["med-network-policy"] = med_network_policy
        if med_location_service is not None:
            data_payload["med-location-service"] = med_location_service
        if custom_tlvs is not None:
            data_payload["custom-tlvs"] = custom_tlvs
        data_payload.update(kwargs)
        return self._client.post(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )
