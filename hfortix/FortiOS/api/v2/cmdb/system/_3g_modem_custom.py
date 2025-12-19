"""
FortiOS CMDB - System ThreeGModemCustom

API Endpoints:
    GET    /system.3g-modem/custom
    POST   /system.3g-modem/custom
    GET    /system.3g-modem/custom/{id}
    PUT    /system.3g-modem/custom/{id}
    DELETE /system.3g-modem/custom/{id}
"""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from ....http_client import HTTPClient


class ThreeGModemCustom:
    """ThreeGModemCustom operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize ThreeGModemCustom endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

    def get(
        self,
        id: str | None = None,
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
            id: Object identifier (optional for list, required for specific)
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
        if id:
            endpoint = f"/system.3g-modem/custom/{id}"
        else:
            endpoint = "/system.3g-modem/custom"
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
        id: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        before: str | None = None,
        after: str | None = None,
        vendor: str | None = None,
        model: str | None = None,
        vendor_id: str | None = None,
        product_id: str | None = None,
        class_id: str | None = None,
        init_string: str | None = None,
        modeswitch_string: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Update this specific resource.
        
        Args:
            payload_dict: Optional dictionary of all parameters (can be passed as first positional arg)
            id: Object identifier (required)
            before: If *action=move*, use *before* to specify the ID of the resource that this resource will be moved before. (optional)
            after: If *action=move*, use *after* to specify the ID of the resource that this resource will be moved after. (optional)
            id: ID. (optional)
            vendor: MODEM vendor name. (optional)
            model: MODEM model name. (optional)
            vendor_id: USB vendor ID in hexadecimal format (0000-ffff). (optional)
            product_id: USB product ID in hexadecimal format (0000-ffff). (optional)
            class_id: USB interface class in hexadecimal format (00-ff). (optional)
            init_string: Init string in hexadecimal format (even length). (optional)
            modeswitch_string: USB modeswitch arguments. For example: '-v 1410 -p 9030 -V 1410 -P 9032 -u 3'. (optional)
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
        if not id:
            raise ValueError("id is required for put()")
        endpoint = f"/system.3g-modem/custom/{id}"
        if before is not None:
            data_payload['before'] = before
        if after is not None:
            data_payload['after'] = after
        if id is not None:
            data_payload['id'] = id
        if vendor is not None:
            data_payload['vendor'] = vendor
        if model is not None:
            data_payload['model'] = model
        if vendor_id is not None:
            data_payload['vendor-id'] = vendor_id
        if product_id is not None:
            data_payload['product-id'] = product_id
        if class_id is not None:
            data_payload['class-id'] = class_id
        if init_string is not None:
            data_payload['init-string'] = init_string
        if modeswitch_string is not None:
            data_payload['modeswitch-string'] = modeswitch_string
        data_payload.update(kwargs)
        return self._client.put("cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json)

    def delete(
        self,
        id: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Delete this specific resource.
        
        Args:
            id: Object identifier (required)
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
        if not id:
            raise ValueError("id is required for delete()")
        endpoint = f"/system.3g-modem/custom/{id}"
        params.update(kwargs)
        return self._client.delete("cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json)

    def post(
        self,
        payload_dict: dict[str, Any] | None = None,
        nkey: str | None = None,
        id: int | None = None,
        vendor: str | None = None,
        model: str | None = None,
        vendor_id: str | None = None,
        product_id: str | None = None,
        class_id: str | None = None,
        init_string: str | None = None,
        modeswitch_string: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Create object(s) in this table.
        
        Args:
            payload_dict: Optional dictionary of all parameters (can be passed as first positional arg)
            nkey: If *action=clone*, use *nkey* to specify the ID for the new resource to be created. (optional)
            id: ID. (optional)
            vendor: MODEM vendor name. (optional)
            model: MODEM model name. (optional)
            vendor_id: USB vendor ID in hexadecimal format (0000-ffff). (optional)
            product_id: USB product ID in hexadecimal format (0000-ffff). (optional)
            class_id: USB interface class in hexadecimal format (00-ff). (optional)
            init_string: Init string in hexadecimal format (even length). (optional)
            modeswitch_string: USB modeswitch arguments. For example: '-v 1410 -p 9030 -V 1410 -P 9032 -u 3'. (optional)
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
        endpoint = "/system.3g-modem/custom"
        if nkey is not None:
            data_payload['nkey'] = nkey
        if id is not None:
            data_payload['id'] = id
        if vendor is not None:
            data_payload['vendor'] = vendor
        if model is not None:
            data_payload['model'] = model
        if vendor_id is not None:
            data_payload['vendor-id'] = vendor_id
        if product_id is not None:
            data_payload['product-id'] = product_id
        if class_id is not None:
            data_payload['class-id'] = class_id
        if init_string is not None:
            data_payload['init-string'] = init_string
        if modeswitch_string is not None:
            data_payload['modeswitch-string'] = modeswitch_string
        data_payload.update(kwargs)
        return self._client.post("cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json)
