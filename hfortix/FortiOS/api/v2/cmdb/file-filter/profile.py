"""
FortiOS CMDB - Cmdb File Filter Profile

Configuration endpoint for managing cmdb file filter profile objects.

API Endpoints:
    GET    /cmdb/file-filter/profile
    POST   /cmdb/file-filter/profile
    GET    /cmdb/file-filter/profile
    PUT    /cmdb/file-filter/profile/{identifier}
    DELETE /cmdb/file-filter/profile/{identifier}

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>> 
    >>> # List all items
    >>> items = fgt.api.cmdb.file_filter.profile.get()
    >>> 
    >>> # Get specific item (if supported)
    >>> item = fgt.api.cmdb.file_filter.profile.get(name="item_name")
    >>> 
    >>> # Create new item (use POST)
    >>> result = fgt.api.cmdb.file_filter.profile.post(
    ...     name="new_item",
    ...     # ... additional parameters
    ... )
    >>> 
    >>> # Update existing item (use PUT)
    >>> result = fgt.api.cmdb.file_filter.profile.put(
    ...     name="existing_item",
    ...     # ... parameters to update
    ... )
    >>> 
    >>> # Delete item
    >>> result = fgt.api.cmdb.file_filter.profile.delete(name="item_name")

Important:
    - Use **POST** to create new objects (404 error if already exists)
    - Use **PUT** to update existing objects (404 error if doesn't exist)
    - Use **GET** to retrieve configuration (no changes made)
    - Use **DELETE** to remove objects (404 error if doesn't exist)
"""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from ....http_client import HTTPClient


class Profile:
    """
    Profile Operations.
    
    Provides CRUD operations for FortiOS profile configuration.

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

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize Profile endpoint.

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
            endpoint = f"/file-filter/profile/{name}"
        else:
            endpoint = "/file-filter/profile"
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
        feature_set: str | None = None,
        replacemsg_group: str | None = None,
        log: str | None = None,
        extended_log: str | None = None,
        scan_archive_contents: str | None = None,
        rules: list | None = None,
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
            name: Profile name. (optional)
            comment: Comment. (optional)
            feature_set: Flow/proxy feature set. (optional)
            replacemsg_group: Replacement message group. (optional)
            log: Enable/disable file-filter logging. (optional)
            extended_log: Enable/disable file-filter extended logging. (optional)
            scan_archive_contents: Enable/disable archive contents scan. (optional)
            rules: File filter rules. (optional)
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
        endpoint = f"/file-filter/profile/{name}"
        if before is not None:
            data_payload['before'] = before
        if after is not None:
            data_payload['after'] = after
        if name is not None:
            data_payload['name'] = name
        if comment is not None:
            data_payload['comment'] = comment
        if feature_set is not None:
            data_payload['feature-set'] = feature_set
        if replacemsg_group is not None:
            data_payload['replacemsg-group'] = replacemsg_group
        if log is not None:
            data_payload['log'] = log
        if extended_log is not None:
            data_payload['extended-log'] = extended_log
        if scan_archive_contents is not None:
            data_payload['scan-archive-contents'] = scan_archive_contents
        if rules is not None:
            data_payload['rules'] = rules
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
        endpoint = f"/file-filter/profile/{name}"
        params.update(kwargs)
        return self._client.delete("cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json)

    def post(
        self,
        payload_dict: dict[str, Any] | None = None,
        nkey: str | None = None,
        name: str | None = None,
        comment: str | None = None,
        feature_set: str | None = None,
        replacemsg_group: str | None = None,
        log: str | None = None,
        extended_log: str | None = None,
        scan_archive_contents: str | None = None,
        rules: list | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Create object(s) in this table.
        
        Args:
            payload_dict: Optional dictionary of all parameters (can be passed as first positional arg)
            nkey: If *action=clone*, use *nkey* to specify the ID for the new resource to be created. (optional)
            name: Profile name. (optional)
            comment: Comment. (optional)
            feature_set: Flow/proxy feature set. (optional)
            replacemsg_group: Replacement message group. (optional)
            log: Enable/disable file-filter logging. (optional)
            extended_log: Enable/disable file-filter extended logging. (optional)
            scan_archive_contents: Enable/disable archive contents scan. (optional)
            rules: File filter rules. (optional)
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
        endpoint = "/file-filter/profile"
        if nkey is not None:
            data_payload['nkey'] = nkey
        if name is not None:
            data_payload['name'] = name
        if comment is not None:
            data_payload['comment'] = comment
        if feature_set is not None:
            data_payload['feature-set'] = feature_set
        if replacemsg_group is not None:
            data_payload['replacemsg-group'] = replacemsg_group
        if log is not None:
            data_payload['log'] = log
        if extended_log is not None:
            data_payload['extended-log'] = extended_log
        if scan_archive_contents is not None:
            data_payload['scan-archive-contents'] = scan_archive_contents
        if rules is not None:
            data_payload['rules'] = rules
        data_payload.update(kwargs)
        return self._client.post("cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json)
