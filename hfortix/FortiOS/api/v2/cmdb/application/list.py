"""
FortiOS CMDB - Application Control Lists

Configure application control lists to control applications and application categories.

API Endpoints:
    GET    /api/v2/cmdb/application/list       - Get all application control lists
    GET    /api/v2/cmdb/application/list/{name} - Get specific application control list
    POST   /api/v2/cmdb/application/list       - Create application control list
    PUT    /api/v2/cmdb/application/list/{name} - Update application control list
    DELETE /api/v2/cmdb/application/list/{name} - Delete application control list
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Dict, Optional, Union

if TYPE_CHECKING:
    from ....http_client import HTTPClient


from hfortix.FortiOS.http_client import encode_path_component


class List:
    """Application control list endpoint"""

    def __init__(self, client: "HTTPClient") -> None:
        self._client = client

    def get(
        self,
        name: Optional[str] = None,
        attr: Optional[str] = None,
        datasource: Optional[bool] = False,
        with_meta: Optional[bool] = False,
        skip: Optional[bool] = False,
        count: Optional[int] = None,
        skip_to_datasource: Optional[str] = None,
        acs: Optional[bool] = None,
        search: Optional[str] = None,
        scope: Optional[str] = None,
        format: Optional[str] = None,
        action: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Get application control list(s)

        Retrieve application control lists with filtering and query options.

        Args:
            name (str, optional): List name. If provided, get specific list.
            attr (str, optional): Attribute name that references other table
            datasource (bool, optional): Include datasource information
            with_meta (bool, optional): Include meta information
            skip (bool, optional): Enable skip operator
            count (int, optional): Maximum number of entries to return
            skip_to_datasource (str, optional): Skip to datasource entry
            acs (bool, optional): If true, return in ascending order
            search (str, optional): Filter by search value
            scope (str, optional): Scope level - 'global', 'vdom', or 'both'
            format (str, optional): Return specific fields (e.g., 'name|comment')
            action (str, optional): Action type - 'default', 'schema', or 'revision'
            vdom (str, optional): Virtual Domain name
            **kwargs: Additional query parameters

        Returns:
            dict: API response with list data

        Examples:
            >>> # Get all application control lists
            >>> lists = fgt.cmdb.application.list.list()

            >>> # Get specific list by name
            >>> app_list = fgt.cmdb.application.list.get('default')

            >>> # Get with filtering and meta information
            >>> filtered = fgt.cmdb.application.list.get(
            ...     format='name|comment|default-network-services',
            ...     count=10,
            ...     with_meta=True
            ... )
        """
        params = {}
        param_map = {
            "attr": attr,
            "datasource": datasource,
            "with_meta": with_meta,
            "skip": skip,
            "count": count,
            "skip_to_datasource": skip_to_datasource,
            "acs": acs,
            "search": search,
            "scope": scope,
            "format": format,
            "action": action,
        }

        for key, value in param_map.items():
            if value is not None:
                params[key] = value

        params.update(kwargs)

        # Build path
        path = "application/list"
        if name:
            path = f"{path}/{encode_path_component(name)}"

        return self._client.get(
            "cmdb", path, params=params if params else None, vdom=vdom, raw_json=raw_json
        )

    def list(self, **kwargs: Any) -> dict[str, Any]:
        """
        Get all application control lists (convenience method)

        Args:
            **kwargs: All parameters from get() method

        Returns:
            dict: API response with all lists

        Examples:
            >>> # Get all lists
            >>> all_lists = fgt.cmdb.application.list.list()
        """
        return self.get(**kwargs)

    def create(
        self,
        payload_dict: Optional[Dict[str, Any]] = None,
        name: Optional[str] = None,
        comment: Optional[str] = None,
        app_replacemsg: Optional[str] = None,
        control_default_network_services: Optional[str] = None,
        deep_app_inspection: Optional[str] = None,
        default_network_services: Optional[list[dict[str, Any]]] = None,
        enforce_default_app_port: Optional[str] = None,
        extended_log: Optional[str] = None,
        force_inclusion_ssl_di_sigs: Optional[str] = None,
        options: Optional[list[str]] = None,
        other_application_action: Optional[str] = None,
        other_application_log: Optional[str] = None,
        p2p_black_list: Optional[list[str]] = None,
        p2p_block_list: Optional[list[str]] = None,
        replacemsg_group: Optional[str] = None,
        unknown_application_action: Optional[str] = None,
        unknown_application_log: Optional[str] = None,
        entries: Optional[list[dict[str, Any]]] = None,
        vdom: Optional[Union[str, bool]] = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Create application control list

        Create a new application control list with specified settings.

        Args:
            name (str, required): Application list name (max 35 chars)
            comment (str, optional): Comment (max 1023 chars)
            app_replacemsg (str, optional): Enable/disable replacement messages - 'disable' or 'enable'
            control_default_network_services (str, optional): Enable/disable default network service control - 'disable' or 'enable'
            deep_app_inspection (str, optional): Enable/disable deep application inspection - 'disable' or 'enable'
            default_network_services (list, optional): Default network service filters (e.g., [{'id': 1}])
            enforce_default_app_port (str, optional): Enable/disable default app port enforcement - 'disable' or 'enable'
            extended_log (str, optional): Enable/disable extended logging - 'disable' or 'enable'
            force_inclusion_ssl_di_sigs (str, optional): Enable/disable SSL deep inspection - 'disable' or 'enable'
            options (list, optional): Basic application protocol signatures allowed (e.g., ['allow-dns', 'allow-icmp'])
            other_application_action (str, optional): Action for other applications - 'pass' or 'block'
            other_application_log (str, optional): Enable/disable logging - 'disable' or 'enable'
            p2p_black_list (list, optional): Deprecated - use p2p_block_list
            p2p_block_list (list, optional): P2P applications to block (e.g., ['skype', 'edonkey'])
            replacemsg_group (str, optional): Replacement message group name
            unknown_application_action (str, optional): Action for unknown apps - 'pass' or 'block'
            unknown_application_log (str, optional): Enable/disable logging - 'disable' or 'enable'
            entries (list, optional): Application list entries (list of dicts with id, action, log, etc.)
            vdom (str, optional): Virtual Domain name
            **kwargs: Additional parameters

        Returns:
            dict: API response

        Examples:
            >>> # Create simple application list
            >>> result = fgt.cmdb.application.list.create(
            ...     name='web-filter',
            ...     comment='Block P2P and unknown apps',
            ...     unknown_application_action='block',
            ...     unknown_application_log='enable'
            ... )

            >>> # Create list with P2P blocking
            >>> result = fgt.cmdb.application.list.create(
            ...     name='security-policy',
            ...     comment='Enhanced security controls',
            ...     p2p_block_list=['skype', 'edonkey', 'bittorrent'],
            ...     deep_app_inspection='enable',
            ...     extended_log='enable'
            ... )

            >>> # Create list with entries
            >>> result = fgt.cmdb.application.list.create(
            ...     name='business-apps',
            ...     entries=[
            ...         {'id': 1, 'action': 'block', 'log': 'enable', 'application': [{'id': 16072}]},
            ...         {'id': 2, 'action': 'pass', 'category': [{'id': 2}]}
            ...     ]
            ... )
        """
        payload_dict = {}
        param_map = {
            "name": name,
            "comment": comment,
            "app_replacemsg": app_replacemsg,
            "control_default_network_services": control_default_network_services,
            "deep_app_inspection": deep_app_inspection,
            "default_network_services": default_network_services,
            "enforce_default_app_port": enforce_default_app_port,
            "extended_log": extended_log,
            "force_inclusion_ssl_di_sigs": force_inclusion_ssl_di_sigs,
            "options": options,
            "other_application_action": other_application_action,
            "other_application_log": other_application_log,
            "p2p_black_list": p2p_black_list,
            "p2p_block_list": p2p_block_list,
            "replacemsg_group": replacemsg_group,
            "unknown_application_action": unknown_application_action,
            "unknown_application_log": unknown_application_log,
            "entries": entries,
        }

        api_field_map = {
            "name": "name",
            "comment": "comment",
            "app_replacemsg": "app-replacemsg",
            "control_default_network_services": "control-default-network-services",
            "deep_app_inspection": "deep-app-inspection",
            "default_network_services": "default-network-services",
            "enforce_default_app_port": "enforce-default-app-port",
            "extended_log": "extended-log",
            "force_inclusion_ssl_di_sigs": "force-inclusion-ssl-di-sigs",
            "options": "options",
            "other_application_action": "other-application-action",
            "other_application_log": "other-application-log",
            "p2p_black_list": "p2p-black-list",
            "p2p_block_list": "p2p-block-list",
            "replacemsg_group": "replacemsg-group",
            "unknown_application_action": "unknown-application-action",
            "unknown_application_log": "unknown-application-log",
            "entries": "entries",
        }

        for param_name, value in param_map.items():
            if value is not None:
                api_name = api_field_map[param_name]
                payload_dict[api_name] = value

        payload_dict.update(kwargs)

        return self._client.post("cmdb", "application/list", data, vdom=vdom, raw_json=raw_json)

    def update(
        self,
        payload_dict: Optional[Dict[str, Any]] = None,
        name: Optional[str] = None,
        comment: Optional[str] = None,
        app_replacemsg: Optional[str] = None,
        control_default_network_services: Optional[str] = None,
        deep_app_inspection: Optional[str] = None,
        default_network_services: Optional[list[dict[str, Any]]] = None,
        enforce_default_app_port: Optional[str] = None,
        extended_log: Optional[str] = None,
        force_inclusion_ssl_di_sigs: Optional[str] = None,
        options: Optional[list[str]] = None,
        other_application_action: Optional[str] = None,
        other_application_log: Optional[str] = None,
        p2p_black_list: Optional[list[str]] = None,
        p2p_block_list: Optional[list[str]] = None,
        replacemsg_group: Optional[str] = None,
        unknown_application_action: Optional[str] = None,
        unknown_application_log: Optional[str] = None,
        entries: Optional[list[dict[str, Any]]] = None,
        vdom: Optional[Union[str, bool]] = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Update application control list

        Update an existing application control list.

        Args:
            name (str, required): Application list name
            comment (str, optional): Comment (max 1023 chars)
            app_replacemsg (str, optional): Enable/disable replacement messages - 'disable' or 'enable'
            control_default_network_services (str, optional): Enable/disable default network service control - 'disable' or 'enable'
            deep_app_inspection (str, optional): Enable/disable deep application inspection - 'disable' or 'enable'
            default_network_services (list, optional): Default network service filters (e.g., [{'id': 1}])
            enforce_default_app_port (str, optional): Enable/disable default app port enforcement - 'disable' or 'enable'
            extended_log (str, optional): Enable/disable extended logging - 'disable' or 'enable'
            force_inclusion_ssl_di_sigs (str, optional): Enable/disable SSL deep inspection - 'disable' or 'enable'
            options (list, optional): Basic application protocol signatures allowed (e.g., ['allow-dns', 'allow-icmp'])
            other_application_action (str, optional): Action for other applications - 'pass' or 'block'
            other_application_log (str, optional): Enable/disable logging - 'disable' or 'enable'
            p2p_black_list (list, optional): Deprecated - use p2p_block_list
            p2p_block_list (list, optional): P2P applications to block (e.g., ['skype', 'edonkey'])
            replacemsg_group (str, optional): Replacement message group name
            unknown_application_action (str, optional): Action for unknown apps - 'pass' or 'block'
            unknown_application_log (str, optional): Enable/disable logging - 'disable' or 'enable'
            entries (list, optional): Application list entries (list of dicts)
            vdom (str, optional): Virtual Domain name
            **kwargs: Additional parameters

        Returns:
            dict: API response

        Examples:
            >>> # Enable deep inspection
            >>> result = fgt.cmdb.application.list.update(
            ...     name='web-filter',
            ...     deep_app_inspection='enable',
            ...     extended_log='enable'
            ... )

            >>> # Update P2P block list
            >>> result = fgt.cmdb.application.list.update(
            ...     name='security-policy',
            ...     p2p_block_list=['skype', 'edonkey', 'bittorrent', 'ares']
            ... )
        """
        payload_dict = {}
        param_map = {
            "comment": comment,
            "app_replacemsg": app_replacemsg,
            "control_default_network_services": control_default_network_services,
            "deep_app_inspection": deep_app_inspection,
            "default_network_services": default_network_services,
            "enforce_default_app_port": enforce_default_app_port,
            "extended_log": extended_log,
            "force_inclusion_ssl_di_sigs": force_inclusion_ssl_di_sigs,
            "options": options,
            "other_application_action": other_application_action,
            "other_application_log": other_application_log,
            "p2p_black_list": p2p_black_list,
            "p2p_block_list": p2p_block_list,
            "replacemsg_group": replacemsg_group,
            "unknown_application_action": unknown_application_action,
            "unknown_application_log": unknown_application_log,
            "entries": entries,
        }

        api_field_map = {
            "comment": "comment",
            "app_replacemsg": "app-replacemsg",
            "control_default_network_services": "control-default-network-services",
            "deep_app_inspection": "deep-app-inspection",
            "default_network_services": "default-network-services",
            "enforce_default_app_port": "enforce-default-app-port",
            "extended_log": "extended-log",
            "force_inclusion_ssl_di_sigs": "force-inclusion-ssl-di-sigs",
            "options": "options",
            "other_application_action": "other-application-action",
            "other_application_log": "other-application-log",
            "p2p_black_list": "p2p-black-list",
            "p2p_block_list": "p2p-block-list",
            "replacemsg_group": "replacemsg-group",
            "unknown_application_action": "unknown-application-action",
            "unknown_application_log": "unknown-application-log",
            "entries": "entries",
        }

        for param_name, value in param_map.items():
            if value is not None:
                api_name = api_field_map[param_name]
                payload_dict[api_name] = value

        payload_dict.update(kwargs)

        return self._client.put(
            "cmdb", f"application/list/{name}", data, vdom=vdom, raw_json=raw_json
        )

    def delete(
        self,
        name: str,
        vdom: Optional[Union[str, bool]] = None,
        raw_json: bool = False,
    ) -> dict[str, Any]:
        """
        Delete application control list

        Args:
            name (str, required): Application list name
            vdom (str, optional): Virtual Domain name

        Returns:
            dict: API response

        Examples:
            >>> # Delete application list
            >>> result = fgt.cmdb.application.list.delete('web-filter')
        """
        return self._client.delete("cmdb", f"application/list/{name}", vdom=vdom, raw_json=raw_json)
