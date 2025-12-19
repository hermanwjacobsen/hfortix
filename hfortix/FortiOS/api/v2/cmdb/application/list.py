"""
FortiOS CMDB - Application List

API Endpoints:
    GET    /application/list
    POST   /application/list
    GET    /application/list/{name}
    PUT    /application/list/{name}
    DELETE /application/list/{name}
"""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from ....http_client import HTTPClient


class List:
    """List operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize List endpoint.

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
    ) -> dict[str, Any]:
        """
        Select a specific entry from a CLI table.
        
        Args:
            name: Object identifier (optional for list, required for specific)
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
        if name:
            endpoint = f"/application/list/{name}"
        else:
            endpoint = "/application/list"
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
        name: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        before: str | None = None,
        after: str | None = None,
        comment: str | None = None,
        replacemsg_group: str | None = None,
        extended_log: str | None = None,
        other_application_action: str | None = None,
        app_replacemsg: str | None = None,
        other_application_log: str | None = None,
        enforce_default_app_port: str | None = None,
        force_inclusion_ssl_di_sigs: str | None = None,
        unknown_application_action: str | None = None,
        unknown_application_log: str | None = None,
        p2p_block_list: str | None = None,
        deep_app_inspection: str | None = None,
        options: str | None = None,
        entries: list | None = None,
        control_default_network_services: str | None = None,
        default_network_services: list | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Update this specific resource.
        
        Args:
            payload_dict: Optional dictionary of all parameters (can be passed as first positional arg)
            name: Object identifier (required)
            before: If *action=move*, use *before* to specify the ID of the resource that this resource will be moved before. (optional)
            after: If *action=move*, use *after* to specify the ID of the resource that this resource will be moved after. (optional)
            name: List name. (optional)
            comment: Comments. (optional)
            replacemsg_group: Replacement message group. (optional)
            extended_log: Enable/disable extended logging. (optional)
            other_application_action: Action for other applications. (optional)
            app_replacemsg: Enable/disable replacement messages for blocked applications. (optional)
            other_application_log: Enable/disable logging for other applications. (optional)
            enforce_default_app_port: Enable/disable default application port enforcement for allowed applications. (optional)
            force_inclusion_ssl_di_sigs: Enable/disable forced inclusion of SSL deep inspection signatures. (optional)
            unknown_application_action: Pass or block traffic from unknown applications. (optional)
            unknown_application_log: Enable/disable logging for unknown applications. (optional)
            p2p_block_list: P2P applications to be block listed. (optional)
            deep_app_inspection: Enable/disable deep application inspection. (optional)
            options: Basic application protocol signatures allowed by default. (optional)
            entries: Application list entries. (optional)
            control_default_network_services: Enable/disable enforcement of protocols over selected ports. (optional)
            default_network_services: Default network service entries. (optional)
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
        if not name:
            raise ValueError("name is required for put()")
        endpoint = f"/application/list/{name}"
        if before is not None:
            data_payload['before'] = before
        if after is not None:
            data_payload['after'] = after
        if name is not None:
            data_payload['name'] = name
        if comment is not None:
            data_payload['comment'] = comment
        if replacemsg_group is not None:
            data_payload['replacemsg-group'] = replacemsg_group
        if extended_log is not None:
            data_payload['extended-log'] = extended_log
        if other_application_action is not None:
            data_payload['other-application-action'] = other_application_action
        if app_replacemsg is not None:
            data_payload['app-replacemsg'] = app_replacemsg
        if other_application_log is not None:
            data_payload['other-application-log'] = other_application_log
        if enforce_default_app_port is not None:
            data_payload['enforce-default-app-port'] = enforce_default_app_port
        if force_inclusion_ssl_di_sigs is not None:
            data_payload['force-inclusion-ssl-di-sigs'] = force_inclusion_ssl_di_sigs
        if unknown_application_action is not None:
            data_payload['unknown-application-action'] = unknown_application_action
        if unknown_application_log is not None:
            data_payload['unknown-application-log'] = unknown_application_log
        if p2p_block_list is not None:
            data_payload['p2p-block-list'] = p2p_block_list
        if deep_app_inspection is not None:
            data_payload['deep-app-inspection'] = deep_app_inspection
        if options is not None:
            data_payload['options'] = options
        if entries is not None:
            data_payload['entries'] = entries
        if control_default_network_services is not None:
            data_payload['control-default-network-services'] = control_default_network_services
        if default_network_services is not None:
            data_payload['default-network-services'] = default_network_services
        data_payload.update(kwargs)
        return self._client.put("cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json)

    def delete(
        self,
        name: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Delete this specific resource.
        
        Args:
            name: Object identifier (required)
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
        if not name:
            raise ValueError("name is required for delete()")
        endpoint = f"/application/list/{name}"
        params.update(kwargs)
        return self._client.delete("cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json)

    def post(
        self,
        payload_dict: dict[str, Any] | None = None,
        nkey: str | None = None,
        name: str | None = None,
        comment: str | None = None,
        replacemsg_group: str | None = None,
        extended_log: str | None = None,
        other_application_action: str | None = None,
        app_replacemsg: str | None = None,
        other_application_log: str | None = None,
        enforce_default_app_port: str | None = None,
        force_inclusion_ssl_di_sigs: str | None = None,
        unknown_application_action: str | None = None,
        unknown_application_log: str | None = None,
        p2p_block_list: str | None = None,
        deep_app_inspection: str | None = None,
        options: str | None = None,
        entries: list | None = None,
        control_default_network_services: str | None = None,
        default_network_services: list | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Create object(s) in this table.
        
        Args:
            payload_dict: Optional dictionary of all parameters (can be passed as first positional arg)
            nkey: If *action=clone*, use *nkey* to specify the ID for the new resource to be created. (optional)
            name: List name. (optional)
            comment: Comments. (optional)
            replacemsg_group: Replacement message group. (optional)
            extended_log: Enable/disable extended logging. (optional)
            other_application_action: Action for other applications. (optional)
            app_replacemsg: Enable/disable replacement messages for blocked applications. (optional)
            other_application_log: Enable/disable logging for other applications. (optional)
            enforce_default_app_port: Enable/disable default application port enforcement for allowed applications. (optional)
            force_inclusion_ssl_di_sigs: Enable/disable forced inclusion of SSL deep inspection signatures. (optional)
            unknown_application_action: Pass or block traffic from unknown applications. (optional)
            unknown_application_log: Enable/disable logging for unknown applications. (optional)
            p2p_block_list: P2P applications to be block listed. (optional)
            deep_app_inspection: Enable/disable deep application inspection. (optional)
            options: Basic application protocol signatures allowed by default. (optional)
            entries: Application list entries. (optional)
            control_default_network_services: Enable/disable enforcement of protocols over selected ports. (optional)
            default_network_services: Default network service entries. (optional)
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
        endpoint = "/application/list"
        if nkey is not None:
            data_payload['nkey'] = nkey
        if name is not None:
            data_payload['name'] = name
        if comment is not None:
            data_payload['comment'] = comment
        if replacemsg_group is not None:
            data_payload['replacemsg-group'] = replacemsg_group
        if extended_log is not None:
            data_payload['extended-log'] = extended_log
        if other_application_action is not None:
            data_payload['other-application-action'] = other_application_action
        if app_replacemsg is not None:
            data_payload['app-replacemsg'] = app_replacemsg
        if other_application_log is not None:
            data_payload['other-application-log'] = other_application_log
        if enforce_default_app_port is not None:
            data_payload['enforce-default-app-port'] = enforce_default_app_port
        if force_inclusion_ssl_di_sigs is not None:
            data_payload['force-inclusion-ssl-di-sigs'] = force_inclusion_ssl_di_sigs
        if unknown_application_action is not None:
            data_payload['unknown-application-action'] = unknown_application_action
        if unknown_application_log is not None:
            data_payload['unknown-application-log'] = unknown_application_log
        if p2p_block_list is not None:
            data_payload['p2p-block-list'] = p2p_block_list
        if deep_app_inspection is not None:
            data_payload['deep-app-inspection'] = deep_app_inspection
        if options is not None:
            data_payload['options'] = options
        if entries is not None:
            data_payload['entries'] = entries
        if control_default_network_services is not None:
            data_payload['control-default-network-services'] = control_default_network_services
        if default_network_services is not None:
            data_payload['default-network-services'] = default_network_services
        data_payload.update(kwargs)
        return self._client.post("cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json)
