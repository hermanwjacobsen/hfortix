"""
FortiOS CMDB - Cmdb User Saml

Configuration endpoint for managing cmdb user saml objects.

API Endpoints:
    GET    /cmdb/user/saml
    POST   /cmdb/user/saml
    GET    /cmdb/user/saml
    PUT    /cmdb/user/saml/{identifier}
    DELETE /cmdb/user/saml/{identifier}

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.user.saml.get()
    >>>
    >>> # Get specific item (if supported)
    >>> item = fgt.api.cmdb.user.saml.get(name="item_name")
    >>>
    >>> # Create new item (use POST)
    >>> result = fgt.api.cmdb.user.saml.post(
    ...     name="new_item",
    ...     # ... additional parameters
    ... )
    >>>
    >>> # Update existing item (use PUT)
    >>> result = fgt.api.cmdb.user.saml.put(
    ...     name="existing_item",
    ...     # ... parameters to update
    ... )
    >>>
    >>> # Delete item
    >>> result = fgt.api.cmdb.user.saml.delete(name="item_name")

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


class Saml:
    """
    Saml Operations.

    Provides CRUD operations for FortiOS saml configuration.

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
        Initialize Saml endpoint.

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
            endpoint = f"/user/saml/{name}"
        else:
            endpoint = "/user/saml"
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
        cert: str | None = None,
        entity_id: str | None = None,
        single_sign_on_url: str | None = None,
        single_logout_url: str | None = None,
        idp_entity_id: str | None = None,
        idp_single_sign_on_url: str | None = None,
        idp_single_logout_url: str | None = None,
        idp_cert: str | None = None,
        scim_client: str | None = None,
        scim_user_attr_type: str | None = None,
        scim_group_attr_type: str | None = None,
        user_name: str | None = None,
        group_name: str | None = None,
        digest_method: str | None = None,
        require_signed_resp_and_asrt: str | None = None,
        limit_relaystate: str | None = None,
        clock_tolerance: int | None = None,
        adfs_claim: str | None = None,
        user_claim_type: str | None = None,
        group_claim_type: str | None = None,
        reauth: str | None = None,
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
            name: SAML server entry name. (optional)
            cert: Certificate to sign SAML messages. (optional)
            entity_id: SP entity ID. (optional)
            single_sign_on_url: SP single sign-on URL. (optional)
            single_logout_url: SP single logout URL. (optional)
            idp_entity_id: IDP entity ID. (optional)
            idp_single_sign_on_url: IDP single sign-on URL. (optional)
            idp_single_logout_url: IDP single logout url. (optional)
            idp_cert: IDP Certificate name. (optional)
            scim_client: SCIM client name. (optional)
            scim_user_attr_type: User attribute type used to match SCIM users
            (default = user-name). (optional)
            scim_group_attr_type: Group attribute type used to match SCIM
            groups (default = display-name). (optional)
            user_name: User name in assertion statement. (optional)
            group_name: Group name in assertion statement. (optional)
            digest_method: Digest method algorithm. (optional)
            require_signed_resp_and_asrt: Require both response and assertion
            from IDP to be signed when FGT acts as SP (default = disable).
            (optional)
            limit_relaystate: Enable/disable limiting of relay-state parameter
            when it exceeds SAML 2.0 specification limits (80 bytes).
            (optional)
            clock_tolerance: Clock skew tolerance in seconds (0 - 300, default
            = 15, 0 = no tolerance). (optional)
            adfs_claim: Enable/disable ADFS Claim for user/group attribute in
            assertion statement (default = disable). (optional)
            user_claim_type: User name claim in assertion statement. (optional)
            group_claim_type: Group claim in assertion statement. (optional)
            reauth: Enable/disable signalling of IDP to force user
            re-authentication (default = disable). (optional)
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
        endpoint = f"/user/saml/{name}"
        if before is not None:
            data_payload["before"] = before
        if after is not None:
            data_payload["after"] = after
        if name is not None:
            data_payload["name"] = name
        if cert is not None:
            data_payload["cert"] = cert
        if entity_id is not None:
            data_payload["entity-id"] = entity_id
        if single_sign_on_url is not None:
            data_payload["single-sign-on-url"] = single_sign_on_url
        if single_logout_url is not None:
            data_payload["single-logout-url"] = single_logout_url
        if idp_entity_id is not None:
            data_payload["idp-entity-id"] = idp_entity_id
        if idp_single_sign_on_url is not None:
            data_payload["idp-single-sign-on-url"] = idp_single_sign_on_url
        if idp_single_logout_url is not None:
            data_payload["idp-single-logout-url"] = idp_single_logout_url
        if idp_cert is not None:
            data_payload["idp-cert"] = idp_cert
        if scim_client is not None:
            data_payload["scim-client"] = scim_client
        if scim_user_attr_type is not None:
            data_payload["scim-user-attr-type"] = scim_user_attr_type
        if scim_group_attr_type is not None:
            data_payload["scim-group-attr-type"] = scim_group_attr_type
        if user_name is not None:
            data_payload["user-name"] = user_name
        if group_name is not None:
            data_payload["group-name"] = group_name
        if digest_method is not None:
            data_payload["digest-method"] = digest_method
        if require_signed_resp_and_asrt is not None:
            data_payload["require-signed-resp-and-asrt"] = (
                require_signed_resp_and_asrt
            )
        if limit_relaystate is not None:
            data_payload["limit-relaystate"] = limit_relaystate
        if clock_tolerance is not None:
            data_payload["clock-tolerance"] = clock_tolerance
        if adfs_claim is not None:
            data_payload["adfs-claim"] = adfs_claim
        if user_claim_type is not None:
            data_payload["user-claim-type"] = user_claim_type
        if group_claim_type is not None:
            data_payload["group-claim-type"] = group_claim_type
        if reauth is not None:
            data_payload["reauth"] = reauth
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
        endpoint = f"/user/saml/{name}"
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
        cert: str | None = None,
        entity_id: str | None = None,
        single_sign_on_url: str | None = None,
        single_logout_url: str | None = None,
        idp_entity_id: str | None = None,
        idp_single_sign_on_url: str | None = None,
        idp_single_logout_url: str | None = None,
        idp_cert: str | None = None,
        scim_client: str | None = None,
        scim_user_attr_type: str | None = None,
        scim_group_attr_type: str | None = None,
        user_name: str | None = None,
        group_name: str | None = None,
        digest_method: str | None = None,
        require_signed_resp_and_asrt: str | None = None,
        limit_relaystate: str | None = None,
        clock_tolerance: int | None = None,
        adfs_claim: str | None = None,
        user_claim_type: str | None = None,
        group_claim_type: str | None = None,
        reauth: str | None = None,
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
            name: SAML server entry name. (optional)
            cert: Certificate to sign SAML messages. (optional)
            entity_id: SP entity ID. (optional)
            single_sign_on_url: SP single sign-on URL. (optional)
            single_logout_url: SP single logout URL. (optional)
            idp_entity_id: IDP entity ID. (optional)
            idp_single_sign_on_url: IDP single sign-on URL. (optional)
            idp_single_logout_url: IDP single logout url. (optional)
            idp_cert: IDP Certificate name. (optional)
            scim_client: SCIM client name. (optional)
            scim_user_attr_type: User attribute type used to match SCIM users
            (default = user-name). (optional)
            scim_group_attr_type: Group attribute type used to match SCIM
            groups (default = display-name). (optional)
            user_name: User name in assertion statement. (optional)
            group_name: Group name in assertion statement. (optional)
            digest_method: Digest method algorithm. (optional)
            require_signed_resp_and_asrt: Require both response and assertion
            from IDP to be signed when FGT acts as SP (default = disable).
            (optional)
            limit_relaystate: Enable/disable limiting of relay-state parameter
            when it exceeds SAML 2.0 specification limits (80 bytes).
            (optional)
            clock_tolerance: Clock skew tolerance in seconds (0 - 300, default
            = 15, 0 = no tolerance). (optional)
            adfs_claim: Enable/disable ADFS Claim for user/group attribute in
            assertion statement (default = disable). (optional)
            user_claim_type: User name claim in assertion statement. (optional)
            group_claim_type: Group claim in assertion statement. (optional)
            reauth: Enable/disable signalling of IDP to force user
            re-authentication (default = disable). (optional)
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
        endpoint = "/user/saml"
        if nkey is not None:
            data_payload["nkey"] = nkey
        if name is not None:
            data_payload["name"] = name
        if cert is not None:
            data_payload["cert"] = cert
        if entity_id is not None:
            data_payload["entity-id"] = entity_id
        if single_sign_on_url is not None:
            data_payload["single-sign-on-url"] = single_sign_on_url
        if single_logout_url is not None:
            data_payload["single-logout-url"] = single_logout_url
        if idp_entity_id is not None:
            data_payload["idp-entity-id"] = idp_entity_id
        if idp_single_sign_on_url is not None:
            data_payload["idp-single-sign-on-url"] = idp_single_sign_on_url
        if idp_single_logout_url is not None:
            data_payload["idp-single-logout-url"] = idp_single_logout_url
        if idp_cert is not None:
            data_payload["idp-cert"] = idp_cert
        if scim_client is not None:
            data_payload["scim-client"] = scim_client
        if scim_user_attr_type is not None:
            data_payload["scim-user-attr-type"] = scim_user_attr_type
        if scim_group_attr_type is not None:
            data_payload["scim-group-attr-type"] = scim_group_attr_type
        if user_name is not None:
            data_payload["user-name"] = user_name
        if group_name is not None:
            data_payload["group-name"] = group_name
        if digest_method is not None:
            data_payload["digest-method"] = digest_method
        if require_signed_resp_and_asrt is not None:
            data_payload["require-signed-resp-and-asrt"] = (
                require_signed_resp_and_asrt
            )
        if limit_relaystate is not None:
            data_payload["limit-relaystate"] = limit_relaystate
        if clock_tolerance is not None:
            data_payload["clock-tolerance"] = clock_tolerance
        if adfs_claim is not None:
            data_payload["adfs-claim"] = adfs_claim
        if user_claim_type is not None:
            data_payload["user-claim-type"] = user_claim_type
        if group_claim_type is not None:
            data_payload["group-claim-type"] = group_claim_type
        if reauth is not None:
            data_payload["reauth"] = reauth
        data_payload.update(kwargs)
        return self._client.post(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )
