"""
FortiOS CMDB - Extension Controller Dataplan

Configure FortiExtender dataplan settings.

API Endpoints:
    GET    /api/v2/cmdb/extension-controller/dataplan        - List all dataplans
    GET    /api/v2/cmdb/extension-controller/dataplan/{name} - Get specific dataplan
    POST   /api/v2/cmdb/extension-controller/dataplan        - Create dataplan
    PUT    /api/v2/cmdb/extension-controller/dataplan/{name} - Update dataplan
    DELETE /api/v2/cmdb/extension-controller/dataplan/{name} - Delete dataplan
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Dict, Any, Optional, Union

if TYPE_CHECKING:
    from ....http_client import HTTPClient


class Dataplan:
    """FortiExtender dataplan endpoint"""

    def __init__(self, client: 'HTTPClient') -> None:
        """
        Initialize Dataplan endpoint.

        Args:
            client: FortiOS API client instance
        """
        self._client = client

    def get(
        self,
        name: Optional[str] = None,
        # Query parameters
        attr: Optional[str] = None,
        count: Optional[int] = None,
        skip_to_datasource: Optional[int] = None,
        acs: Optional[bool] = None,
        search: Optional[str] = None,
        scope: Optional[str] = None,
        datasource: Optional[bool] = None,
        with_meta: Optional[bool] = None,
        skip: Optional[bool] = None,
        format: Optional[str] = None,
        action: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        **kwargs: Any
    ) -> dict[str, Any]:
        """
        Get FortiExtender dataplan(s).

        Args:
            name (str, optional): Dataplan name. If None, retrieves all dataplans
            attr (str, optional): Attribute name that references other table
            count (int, optional): Maximum number of entries to return
            skip_to_datasource (int, optional): Skip to provided table's Nth entry
            acs (bool, optional): If true, returned results are in ascending order
            search (str, optional): Filter objects by search value
            scope (str, optional): Scope level - 'global', 'vdom', or 'both'
            datasource (bool, optional): Include datasource information
            with_meta (bool, optional): Include meta information
            skip (bool, optional): Enable CLI skip operator
            format (str, optional): List of property names to include, separated by |
            action (str, optional): Special action - 'default', 'schema', 'revision'
            vdom (str, optional): Virtual Domain name
            **kwargs: Additional query parameters

        Returns:
            dict: API response containing dataplan data

        Examples:
            >>> # List all dataplans
            >>> plans = fgt.cmdb.extension_controller.dataplan.list()

            >>> # Get a specific dataplan
            >>> plan = fgt.cmdb.extension_controller.dataplan.get('plan1')
        """
        params = {}
        param_map = {
            'attr': attr,
            'count': count,
            'skip_to_datasource': skip_to_datasource,
            'acs': acs,
            'search': search,
            'scope': scope,
            'datasource': datasource,
            'with_meta': with_meta,
            'skip': skip,
            'format': format,
            'action': action,
        }

        for key, value in param_map.items():
            if value is not None:
                params[key] = value

        params.update(kwargs)

        path = 'extension-controller/dataplan'
        if name:
            path = f'{path}/{name}'

        return self._client.get('cmdb', path, params=params if params else None, vdom=vdom)

    def list(
        self,
        attr: Optional[str] = None,
        count: Optional[int] = None,
        skip_to_datasource: Optional[int] = None,
        acs: Optional[bool] = None,
        search: Optional[str] = None,
        scope: Optional[str] = None,
        datasource: Optional[bool] = None,
        with_meta: Optional[bool] = None,
        skip: Optional[bool] = None,
        format: Optional[str] = None,
        action: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        **kwargs: Any
    ) -> dict[str, Any]:
        """
        Get all FortiExtender dataplans (convenience method).

        Args:
            Same as get() method, excluding name

        Returns:
            dict: API response containing all dataplans

        Examples:
            >>> plans = fgt.cmdb.extension_controller.dataplan.list()
        """
        return self.get(
            name=None,
            attr=attr,
            count=count,
            skip_to_datasource=skip_to_datasource,
            acs=acs,
            search=search,
            scope=scope,
            datasource=datasource,
            with_meta=with_meta,
            skip=skip,
            format=format,
            action=action,
            vdom=vdom,
            **kwargs
        )

    def create(
        self,
        data_dict: Optional[Dict[str, Any]] = None,
        name: Optional[str] = None,
        # Dataplan configuration
        modem_id: Optional[str] = None,
        type: Optional[str] = None,
        slot: Optional[str] = None,
        iccid: Optional[str] = None,
        carrier: Optional[str] = None,
        apn: Optional[str] = None,
        auth_type: Optional[str] = None,
        username: Optional[str] = None,
        password: Optional[str] = None,
        pdn: Optional[str] = None,
        signal_threshold: Optional[int] = None,
        signal_period: Optional[int] = None,
        capacity: Optional[int] = None,
        monthly_fee: Optional[int] = None,
        billing_date: Optional[int] = None,
        overage: Optional[str] = None,
        preferred_subnet: Optional[int] = None,
        private_network: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        **kwargs: Any
    ) -> dict[str, Any]:
        """
        Create a new FortiExtender dataplan.

        Args:
            name (str): Dataplan name
            modem_id (str, optional): Modem ID - 'modem1'/'modem2'/'all'
            type (str, optional): Type - 'carrier'/'slot'/'iccid'/'generic'
            slot (str, optional): SIM slot - 'sim1'/'sim2'
            iccid (str, optional): ICCID
            carrier (str, optional): Carrier name
            apn (str, optional): Access Point Name
            auth_type (str, optional): Authentication type - 'none'/'pap'/'chap'
            username (str, optional): Username for authentication
            password (str, optional): Password for authentication
            pdn (str, optional): PDN type - 'ipv4-only'/'ipv6-only'/'ipv4-ipv6'
            signal_threshold (int, optional): Signal threshold (50-100)
            signal_period (int, optional): Signal period (600-18000 seconds)
            capacity (int, optional): Capacity in MB (0-102400)
            monthly_fee (int, optional): Monthly fee (0-100000)
            billing_date (int, optional): Billing day of month (1-31)
            overage (str, optional): Overage - 'enable'/'disable'
            preferred_subnet (int, optional): Preferred subnet bits (0-32)
            private_network (str, optional): Private network - 'enable'/'disable'
            vdom (str, optional): Virtual Domain name
            **kwargs: Additional parameters

        Returns:
            dict: API response

        Examples:
            >>> result = fgt.cmdb.extension_controller.dataplan.create(
            ...     name='MyDataplan',
            ...     modem_id='modem1',
            ...     type='carrier',
            ...     apn='internet'
            ... )
        """
        data = {'name': name}
        
        param_map = {
            'modem_id': modem_id,
            'type': type,
            'slot': slot,
            'iccid': iccid,
            'carrier': carrier,
            'apn': apn,
            'auth_type': auth_type,
            'username': username,
            'password': password,
            'pdn': pdn,
            'signal_threshold': signal_threshold,
            'signal_period': signal_period,
            'capacity': capacity,
            'monthly_fee': monthly_fee,
            'billing_date': billing_date,
            'overage': overage,
            'preferred_subnet': preferred_subnet,
            'private_network': private_network,
        }

        for key, value in param_map.items():
            if value is not None:
                data[key.replace('_', '-')] = value

        data.update(kwargs)

        return self._client.post('cmdb', 'extension-controller/dataplan', data=data, vdom=vdom)

    def update(
        self,
        data_dict: Optional[Dict[str, Any]] = None,
        name: Optional[str] = None,
        # Dataplan configuration
        modem_id: Optional[str] = None,
        type: Optional[str] = None,
        slot: Optional[str] = None,
        iccid: Optional[str] = None,
        carrier: Optional[str] = None,
        apn: Optional[str] = None,
        auth_type: Optional[str] = None,
        username: Optional[str] = None,
        password: Optional[str] = None,
        pdn: Optional[str] = None,
        signal_threshold: Optional[int] = None,
        signal_period: Optional[int] = None,
        capacity: Optional[int] = None,
        monthly_fee: Optional[int] = None,
        billing_date: Optional[int] = None,
        overage: Optional[str] = None,
        preferred_subnet: Optional[int] = None,
        private_network: Optional[str] = None,
        # Update parameters
        action: Optional[str] = None,
        before: Optional[str] = None,
        after: Optional[str] = None,
        scope: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        **kwargs: Any
    ) -> dict[str, Any]:
        """
        Update a FortiExtender dataplan.

        Args:
            name (str): Dataplan name to update
            (Other parameters same as create method)
            action (str, optional): 'add-members', 'replace-members', 'remove-members'
            before (str, optional): Place new object before given object
            after (str, optional): Place new object after given object
            scope (str, optional): Scope level - 'global' or 'vdom'
            vdom (str, optional): Virtual Domain name
            **kwargs: Additional parameters

        Returns:
            dict: API response

        Examples:
            >>> result = fgt.cmdb.extension_controller.dataplan.update(
            ...     name='MyDataplan',
            ...     apn='new-apn',
            ...     capacity=10240
            ... )
        """
        data = {}
        
        param_map = {
            'modem_id': modem_id,
            'type': type,
            'slot': slot,
            'iccid': iccid,
            'carrier': carrier,
            'apn': apn,
            'auth_type': auth_type,
            'username': username,
            'password': password,
            'pdn': pdn,
            'signal_threshold': signal_threshold,
            'signal_period': signal_period,
            'capacity': capacity,
            'monthly_fee': monthly_fee,
            'billing_date': billing_date,
            'overage': overage,
            'preferred_subnet': preferred_subnet,
            'private_network': private_network,
            'action': action,
            'before': before,
            'after': after,
            'scope': scope,
        }

        for key, value in param_map.items():
            if value is not None:
                data[key.replace('_', '-')] = value

        data.update(kwargs)

        return self._client.put('cmdb', f'extension-controller/dataplan/{name}', data=data, vdom=vdom)

    def delete(
        self,
        name: str,
        scope: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None
    ) -> dict[str, Any]:
        """
        Delete a FortiExtender dataplan.

        Args:
            name (str): Dataplan name to delete
            scope (str, optional): Scope level - 'global' or 'vdom'
            vdom (str, optional): Virtual Domain name

        Returns:
            dict: API response

        Examples:
            >>> result = fgt.cmdb.extension_controller.dataplan.delete('MyDataplan')
        """
        params = {}
        if scope is not None:
            params['scope'] = scope

        return self._client.delete('cmdb', f'extension-controller/dataplan/{name}', 
                                   params=params if params else None, vdom=vdom)
