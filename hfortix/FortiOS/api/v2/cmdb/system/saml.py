"""
FortiOS CMDB - System Saml

API Endpoints:
    GET    /system/saml
    PUT    /system/saml
"""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from ....http_client import HTTPClient


class Saml:
    """Saml operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize Saml endpoint.

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
        endpoint = "/system/saml"
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
        role: str | None = None,
        default_login_page: str | None = None,
        default_profile: str | None = None,
        cert: str | None = None,
        binding_protocol: str | None = None,
        portal_url: str | None = None,
        entity_id: str | None = None,
        single_sign_on_url: str | None = None,
        single_logout_url: str | None = None,
        idp_entity_id: str | None = None,
        idp_single_sign_on_url: str | None = None,
        idp_single_logout_url: str | None = None,
        idp_cert: str | None = None,
        server_address: str | None = None,
        require_signed_resp_and_asrt: str | None = None,
        tolerance: int | None = None,
        life: int | None = None,
        service_providers: list | None = None,
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
            status: Enable/disable SAML authentication (default = disable). (optional)
            role: SAML role. (optional)
            default_login_page: Choose default login page. (optional)
            default_profile: Default profile for new SSO admin. (optional)
            cert: Certificate to sign SAML messages. (optional)
            binding_protocol: IdP Binding protocol. (optional)
            portal_url: SP portal URL. (optional)
            entity_id: SP entity ID. (optional)
            single_sign_on_url: SP single sign-on URL. (optional)
            single_logout_url: SP single logout URL. (optional)
            idp_entity_id: IDP entity ID. (optional)
            idp_single_sign_on_url: IDP single sign-on URL. (optional)
            idp_single_logout_url: IDP single logout URL. (optional)
            idp_cert: IDP certificate name. (optional)
            server_address: Server address. (optional)
            require_signed_resp_and_asrt: Require both response and assertion from IDP to be signed when FGT acts as SP (default = disable). (optional)
            tolerance: Tolerance to the range of time when the assertion is valid (in minutes). (optional)
            life: Length of the range of time when the assertion is valid (in minutes). (optional)
            service_providers: Authorized service providers. (optional)
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
        endpoint = "/system/saml"
        if before is not None:
            data_payload['before'] = before
        if after is not None:
            data_payload['after'] = after
        if status is not None:
            data_payload['status'] = status
        if role is not None:
            data_payload['role'] = role
        if default_login_page is not None:
            data_payload['default-login-page'] = default_login_page
        if default_profile is not None:
            data_payload['default-profile'] = default_profile
        if cert is not None:
            data_payload['cert'] = cert
        if binding_protocol is not None:
            data_payload['binding-protocol'] = binding_protocol
        if portal_url is not None:
            data_payload['portal-url'] = portal_url
        if entity_id is not None:
            data_payload['entity-id'] = entity_id
        if single_sign_on_url is not None:
            data_payload['single-sign-on-url'] = single_sign_on_url
        if single_logout_url is not None:
            data_payload['single-logout-url'] = single_logout_url
        if idp_entity_id is not None:
            data_payload['idp-entity-id'] = idp_entity_id
        if idp_single_sign_on_url is not None:
            data_payload['idp-single-sign-on-url'] = idp_single_sign_on_url
        if idp_single_logout_url is not None:
            data_payload['idp-single-logout-url'] = idp_single_logout_url
        if idp_cert is not None:
            data_payload['idp-cert'] = idp_cert
        if server_address is not None:
            data_payload['server-address'] = server_address
        if require_signed_resp_and_asrt is not None:
            data_payload['require-signed-resp-and-asrt'] = require_signed_resp_and_asrt
        if tolerance is not None:
            data_payload['tolerance'] = tolerance
        if life is not None:
            data_payload['life'] = life
        if service_providers is not None:
            data_payload['service-providers'] = service_providers
        data_payload.update(kwargs)
        return self._client.put("cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json)
