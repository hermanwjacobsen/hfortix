"""
FortiOS CMDB - Cmdb Icap Profile

Configuration endpoint for managing cmdb icap profile objects.

API Endpoints:
    GET    /cmdb/icap/profile
    POST   /cmdb/icap/profile
    GET    /cmdb/icap/profile
    PUT    /cmdb/icap/profile/{identifier}
    DELETE /cmdb/icap/profile/{identifier}

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.icap.profile.get()
    >>>
    >>> # Get specific item (if supported)
    >>> item = fgt.api.cmdb.icap.profile.get(name="item_name")
    >>>
    >>> # Create new item (use POST)
    >>> result = fgt.api.cmdb.icap.profile.post(
    ...     name="new_item",
    ...     # ... additional parameters
    ... )
    >>>
    >>> # Update existing item (use PUT)
    >>> result = fgt.api.cmdb.icap.profile.put(
    ...     name="existing_item",
    ...     # ... parameters to update
    ... )
    >>>
    >>> # Delete item
    >>> result = fgt.api.cmdb.icap.profile.delete(name="item_name")

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

    def __init__(self, client: "IHTTPClient"):
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
            endpoint = f"/icap/profile/{name}"
        else:
            endpoint = "/icap/profile"
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
        replacemsg_group: str | None = None,
        comment: str | None = None,
        request: str | None = None,
        response: str | None = None,
        file_transfer: str | None = None,
        streaming_content_bypass: str | None = None,
        ocr_only: str | None = None,
        _204_size_limit: int | None = None,
        _204_response: str | None = None,
        preview: str | None = None,
        preview_data_length: int | None = None,
        request_server: str | None = None,
        response_server: str | None = None,
        file_transfer_server: str | None = None,
        request_failure: str | None = None,
        response_failure: str | None = None,
        file_transfer_failure: str | None = None,
        request_path: str | None = None,
        response_path: str | None = None,
        file_transfer_path: str | None = None,
        methods: str | None = None,
        response_req_hdr: str | None = None,
        respmod_default_action: str | None = None,
        icap_block_log: str | None = None,
        chunk_encap: str | None = None,
        extension_feature: str | None = None,
        scan_progress_interval: int | None = None,
        timeout: int | None = None,
        icap_headers: list | None = None,
        respmod_forward_rules: list | None = None,
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
            replacemsg_group: Replacement message group. (optional)
            name: ICAP profile name. (optional)
            comment: Comment. (optional)
            request: Enable/disable whether an HTTP request is passed to an
            ICAP server. (optional)
            response: Enable/disable whether an HTTP response is passed to an
            ICAP server. (optional)
            file_transfer: Configure the file transfer protocols to pass
            transferred files to an ICAP server as REQMOD. (optional)
            streaming_content_bypass: Enable/disable bypassing of ICAP server
            for streaming content. (optional)
            ocr_only: Enable/disable this FortiGate unit to submit only OCR
            interested content to the ICAP server. (optional)
            _204_size_limit: 204 response size limit to be saved by ICAP client
            in megabytes (1 - 10, default = 1 MB). (optional)
            _204_response: Enable/disable allowance of 204 response from ICAP
            server. (optional)
            preview: Enable/disable preview of data to ICAP server. (optional)
            preview_data_length: Preview data length to be sent to ICAP server.
            (optional)
            request_server: ICAP server to use for an HTTP request. (optional)
            response_server: ICAP server to use for an HTTP response.
            (optional)
            file_transfer_server: ICAP server to use for a file transfer.
            (optional)
            request_failure: Action to take if the ICAP server cannot be
            contacted when processing an HTTP request. (optional)
            response_failure: Action to take if the ICAP server cannot be
            contacted when processing an HTTP response. (optional)
            file_transfer_failure: Action to take if the ICAP server cannot be
            contacted when processing a file transfer. (optional)
            request_path: Path component of the ICAP URI that identifies the
            HTTP request processing service. (optional)
            response_path: Path component of the ICAP URI that identifies the
            HTTP response processing service. (optional)
            file_transfer_path: Path component of the ICAP URI that identifies
            the file transfer processing service. (optional)
            methods: The allowed HTTP methods that will be sent to ICAP server
            for further processing. (optional)
            response_req_hdr: Enable/disable addition of req-hdr for ICAP
            response modification (respmod) processing. (optional)
            respmod_default_action: Default action to ICAP response
            modification (respmod) processing. (optional)
            icap_block_log: Enable/disable UTM log when infection found
            (default = disable). (optional)
            chunk_encap: Enable/disable chunked encapsulation (default =
            disable). (optional)
            extension_feature: Enable/disable ICAP extension features.
            (optional)
            scan_progress_interval: Scan progress interval value. (optional)
            timeout: Time (in seconds) that ICAP client waits for the response
            from ICAP server. (optional)
            icap_headers: Configure ICAP forwarded request headers. (optional)
            respmod_forward_rules: ICAP response mode forward rules. (optional)
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
        endpoint = f"/icap/profile/{name}"
        if before is not None:
            data_payload["before"] = before
        if after is not None:
            data_payload["after"] = after
        if replacemsg_group is not None:
            data_payload["replacemsg-group"] = replacemsg_group
        if name is not None:
            data_payload["name"] = name
        if comment is not None:
            data_payload["comment"] = comment
        if request is not None:
            data_payload["request"] = request
        if response is not None:
            data_payload["response"] = response
        if file_transfer is not None:
            data_payload["file-transfer"] = file_transfer
        if streaming_content_bypass is not None:
            data_payload["streaming-content-bypass"] = streaming_content_bypass
        if ocr_only is not None:
            data_payload["ocr-only"] = ocr_only
        if _204_size_limit is not None:
            data_payload["204-size-limit"] = _204_size_limit
        if _204_response is not None:
            data_payload["204-response"] = _204_response
        if preview is not None:
            data_payload["preview"] = preview
        if preview_data_length is not None:
            data_payload["preview-data-length"] = preview_data_length
        if request_server is not None:
            data_payload["request-server"] = request_server
        if response_server is not None:
            data_payload["response-server"] = response_server
        if file_transfer_server is not None:
            data_payload["file-transfer-server"] = file_transfer_server
        if request_failure is not None:
            data_payload["request-failure"] = request_failure
        if response_failure is not None:
            data_payload["response-failure"] = response_failure
        if file_transfer_failure is not None:
            data_payload["file-transfer-failure"] = file_transfer_failure
        if request_path is not None:
            data_payload["request-path"] = request_path
        if response_path is not None:
            data_payload["response-path"] = response_path
        if file_transfer_path is not None:
            data_payload["file-transfer-path"] = file_transfer_path
        if methods is not None:
            data_payload["methods"] = methods
        if response_req_hdr is not None:
            data_payload["response-req-hdr"] = response_req_hdr
        if respmod_default_action is not None:
            data_payload["respmod-default-action"] = respmod_default_action
        if icap_block_log is not None:
            data_payload["icap-block-log"] = icap_block_log
        if chunk_encap is not None:
            data_payload["chunk-encap"] = chunk_encap
        if extension_feature is not None:
            data_payload["extension-feature"] = extension_feature
        if scan_progress_interval is not None:
            data_payload["scan-progress-interval"] = scan_progress_interval
        if timeout is not None:
            data_payload["timeout"] = timeout
        if icap_headers is not None:
            data_payload["icap-headers"] = icap_headers
        if respmod_forward_rules is not None:
            data_payload["respmod-forward-rules"] = respmod_forward_rules
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
        endpoint = f"/icap/profile/{name}"
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
        replacemsg_group: str | None = None,
        name: str | None = None,
        comment: str | None = None,
        request: str | None = None,
        response: str | None = None,
        file_transfer: str | None = None,
        streaming_content_bypass: str | None = None,
        ocr_only: str | None = None,
        _204_size_limit: int | None = None,
        _204_response: str | None = None,
        preview: str | None = None,
        preview_data_length: int | None = None,
        request_server: str | None = None,
        response_server: str | None = None,
        file_transfer_server: str | None = None,
        request_failure: str | None = None,
        response_failure: str | None = None,
        file_transfer_failure: str | None = None,
        request_path: str | None = None,
        response_path: str | None = None,
        file_transfer_path: str | None = None,
        methods: str | None = None,
        response_req_hdr: str | None = None,
        respmod_default_action: str | None = None,
        icap_block_log: str | None = None,
        chunk_encap: str | None = None,
        extension_feature: str | None = None,
        scan_progress_interval: int | None = None,
        timeout: int | None = None,
        icap_headers: list | None = None,
        respmod_forward_rules: list | None = None,
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
            replacemsg_group: Replacement message group. (optional)
            name: ICAP profile name. (optional)
            comment: Comment. (optional)
            request: Enable/disable whether an HTTP request is passed to an
            ICAP server. (optional)
            response: Enable/disable whether an HTTP response is passed to an
            ICAP server. (optional)
            file_transfer: Configure the file transfer protocols to pass
            transferred files to an ICAP server as REQMOD. (optional)
            streaming_content_bypass: Enable/disable bypassing of ICAP server
            for streaming content. (optional)
            ocr_only: Enable/disable this FortiGate unit to submit only OCR
            interested content to the ICAP server. (optional)
            _204_size_limit: 204 response size limit to be saved by ICAP client
            in megabytes (1 - 10, default = 1 MB). (optional)
            _204_response: Enable/disable allowance of 204 response from ICAP
            server. (optional)
            preview: Enable/disable preview of data to ICAP server. (optional)
            preview_data_length: Preview data length to be sent to ICAP server.
            (optional)
            request_server: ICAP server to use for an HTTP request. (optional)
            response_server: ICAP server to use for an HTTP response.
            (optional)
            file_transfer_server: ICAP server to use for a file transfer.
            (optional)
            request_failure: Action to take if the ICAP server cannot be
            contacted when processing an HTTP request. (optional)
            response_failure: Action to take if the ICAP server cannot be
            contacted when processing an HTTP response. (optional)
            file_transfer_failure: Action to take if the ICAP server cannot be
            contacted when processing a file transfer. (optional)
            request_path: Path component of the ICAP URI that identifies the
            HTTP request processing service. (optional)
            response_path: Path component of the ICAP URI that identifies the
            HTTP response processing service. (optional)
            file_transfer_path: Path component of the ICAP URI that identifies
            the file transfer processing service. (optional)
            methods: The allowed HTTP methods that will be sent to ICAP server
            for further processing. (optional)
            response_req_hdr: Enable/disable addition of req-hdr for ICAP
            response modification (respmod) processing. (optional)
            respmod_default_action: Default action to ICAP response
            modification (respmod) processing. (optional)
            icap_block_log: Enable/disable UTM log when infection found
            (default = disable). (optional)
            chunk_encap: Enable/disable chunked encapsulation (default =
            disable). (optional)
            extension_feature: Enable/disable ICAP extension features.
            (optional)
            scan_progress_interval: Scan progress interval value. (optional)
            timeout: Time (in seconds) that ICAP client waits for the response
            from ICAP server. (optional)
            icap_headers: Configure ICAP forwarded request headers. (optional)
            respmod_forward_rules: ICAP response mode forward rules. (optional)
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
        endpoint = "/icap/profile"
        if nkey is not None:
            data_payload["nkey"] = nkey
        if replacemsg_group is not None:
            data_payload["replacemsg-group"] = replacemsg_group
        if name is not None:
            data_payload["name"] = name
        if comment is not None:
            data_payload["comment"] = comment
        if request is not None:
            data_payload["request"] = request
        if response is not None:
            data_payload["response"] = response
        if file_transfer is not None:
            data_payload["file-transfer"] = file_transfer
        if streaming_content_bypass is not None:
            data_payload["streaming-content-bypass"] = streaming_content_bypass
        if ocr_only is not None:
            data_payload["ocr-only"] = ocr_only
        if _204_size_limit is not None:
            data_payload["204-size-limit"] = _204_size_limit
        if _204_response is not None:
            data_payload["204-response"] = _204_response
        if preview is not None:
            data_payload["preview"] = preview
        if preview_data_length is not None:
            data_payload["preview-data-length"] = preview_data_length
        if request_server is not None:
            data_payload["request-server"] = request_server
        if response_server is not None:
            data_payload["response-server"] = response_server
        if file_transfer_server is not None:
            data_payload["file-transfer-server"] = file_transfer_server
        if request_failure is not None:
            data_payload["request-failure"] = request_failure
        if response_failure is not None:
            data_payload["response-failure"] = response_failure
        if file_transfer_failure is not None:
            data_payload["file-transfer-failure"] = file_transfer_failure
        if request_path is not None:
            data_payload["request-path"] = request_path
        if response_path is not None:
            data_payload["response-path"] = response_path
        if file_transfer_path is not None:
            data_payload["file-transfer-path"] = file_transfer_path
        if methods is not None:
            data_payload["methods"] = methods
        if response_req_hdr is not None:
            data_payload["response-req-hdr"] = response_req_hdr
        if respmod_default_action is not None:
            data_payload["respmod-default-action"] = respmod_default_action
        if icap_block_log is not None:
            data_payload["icap-block-log"] = icap_block_log
        if chunk_encap is not None:
            data_payload["chunk-encap"] = chunk_encap
        if extension_feature is not None:
            data_payload["extension-feature"] = extension_feature
        if scan_progress_interval is not None:
            data_payload["scan-progress-interval"] = scan_progress_interval
        if timeout is not None:
            data_payload["timeout"] = timeout
        if icap_headers is not None:
            data_payload["icap-headers"] = icap_headers
        if respmod_forward_rules is not None:
            data_payload["respmod-forward-rules"] = respmod_forward_rules
        data_payload.update(kwargs)
        return self._client.post(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )
