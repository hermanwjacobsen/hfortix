"""
FortiOS CMDB - Cmdb System Automation Action

Configuration endpoint for managing cmdb system automation action objects.

API Endpoints:
    GET    /cmdb/system/automation_action
    POST   /cmdb/system/automation_action
    GET    /cmdb/system/automation_action
    PUT    /cmdb/system/automation_action/{identifier}
    DELETE /cmdb/system/automation_action/{identifier}

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.system.automation_action.get()
    >>>
    >>> # Get specific item (if supported)
    >>> item = fgt.api.cmdb.system.automation_action.get(name="item_name")
    >>>
    >>> # Create new item (use POST)
    >>> result = fgt.api.cmdb.system.automation_action.post(
    ...     name="new_item",
    ...     # ... additional parameters
    ... )
    >>>
    >>> # Update existing item (use PUT)
    >>> result = fgt.api.cmdb.system.automation_action.put(
    ...     name="existing_item",
    ...     # ... parameters to update
    ... )
    >>>
    >>> # Delete item
    >>> result = fgt.api.cmdb.system.automation_action.delete(name="item_name")

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


class AutomationAction:
    """
    Automationaction Operations.

    Provides CRUD operations for FortiOS automationaction configuration.

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
        Initialize AutomationAction endpoint.

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
            endpoint = f"/system/automation-action/{name}"
        else:
            endpoint = "/system/automation-action"
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
        description: str | None = None,
        action_type: str | None = None,
        system_action: str | None = None,
        tls_certificate: str | None = None,
        forticare_email: str | None = None,
        email_to: list | None = None,
        email_from: str | None = None,
        email_subject: str | None = None,
        minimum_interval: int | None = None,
        aws_api_key: str | None = None,
        azure_function_authorization: str | None = None,
        azure_api_key: str | None = None,
        alicloud_function_authorization: str | None = None,
        alicloud_access_key_id: str | None = None,
        alicloud_access_key_secret: str | None = None,
        message_type: str | None = None,
        message: str | None = None,
        replacement_message: str | None = None,
        replacemsg_group: str | None = None,
        protocol: str | None = None,
        method: str | None = None,
        uri: str | None = None,
        http_body: str | None = None,
        port: int | None = None,
        http_headers: list | None = None,
        form_data: list | None = None,
        verify_host_cert: str | None = None,
        script: str | None = None,
        output_size: int | None = None,
        timeout: int | None = None,
        duration: int | None = None,
        output_interval: int | None = None,
        file_only: str | None = None,
        execute_security_fabric: str | None = None,
        accprofile: str | None = None,
        regular_expression: str | None = None,
        log_debug_print: str | None = None,
        security_tag: str | None = None,
        sdn_connector: list | None = None,
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
            name: Name. (optional)
            description: Description. (optional)
            action_type: Action type. (optional)
            system_action: System action type. (optional)
            tls_certificate: Custom TLS certificate for API request. (optional)
            forticare_email: Enable/disable use of your FortiCare email address
            as the email-to address. (optional)
            email_to: Email addresses. (optional)
            email_from: Email sender name. (optional)
            email_subject: Email subject. (optional)
            minimum_interval: Limit execution to no more than once in this
            interval (in seconds). (optional)
            aws_api_key: AWS API Gateway API key. (optional)
            azure_function_authorization: Azure function authorization level.
            (optional)
            azure_api_key: Azure function API key. (optional)
            alicloud_function_authorization: AliCloud function authorization
            type. (optional)
            alicloud_access_key_id: AliCloud AccessKey ID. (optional)
            alicloud_access_key_secret: AliCloud AccessKey secret. (optional)
            message_type: Message type. (optional)
            message: Message content. (optional)
            replacement_message: Enable/disable replacement message. (optional)
            replacemsg_group: Replacement message group. (optional)
            protocol: Request protocol. (optional)
            method: Request method (POST, PUT, GET, PATCH or DELETE).
            (optional)
            uri: Request API URI. (optional)
            http_body: Request body (if necessary). Should be serialized json
            string. (optional)
            port: Protocol port. (optional)
            http_headers: Request headers. (optional)
            form_data: Form data parts for content type multipart/form-data.
            (optional)
            verify_host_cert: Enable/disable verification of the remote host
            certificate. (optional)
            script: CLI script. (optional)
            output_size: Number of megabytes to limit script output to (1 -
            1024, default = 10). (optional)
            timeout: Maximum running time for this script in seconds (0 = no
            timeout). (optional)
            duration: Maximum running time for this script in seconds.
            (optional)
            output_interval: Collect the outputs for each output-interval in
            seconds (0 = no intermediate output). (optional)
            file_only: Enable/disable the output in files only. (optional)
            execute_security_fabric: Enable/disable execution of CLI script on
            all or only one FortiGate unit in the Security Fabric. (optional)
            accprofile: Access profile for CLI script action to access
            FortiGate features. (optional)
            regular_expression: Regular expression string. (optional)
            log_debug_print: Enable/disable logging debug print output from
            diagnose action. (optional)
            security_tag: NSX security tag. (optional)
            sdn_connector: NSX SDN connector names. (optional)
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
        endpoint = f"/system/automation-action/{name}"
        if before is not None:
            data_payload["before"] = before
        if after is not None:
            data_payload["after"] = after
        if name is not None:
            data_payload["name"] = name
        if description is not None:
            data_payload["description"] = description
        if action_type is not None:
            data_payload["action-type"] = action_type
        if system_action is not None:
            data_payload["system-action"] = system_action
        if tls_certificate is not None:
            data_payload["tls-certificate"] = tls_certificate
        if forticare_email is not None:
            data_payload["forticare-email"] = forticare_email
        if email_to is not None:
            data_payload["email-to"] = email_to
        if email_from is not None:
            data_payload["email-from"] = email_from
        if email_subject is not None:
            data_payload["email-subject"] = email_subject
        if minimum_interval is not None:
            data_payload["minimum-interval"] = minimum_interval
        if aws_api_key is not None:
            data_payload["aws-api-key"] = aws_api_key
        if azure_function_authorization is not None:
            data_payload["azure-function-authorization"] = (
                azure_function_authorization
            )
        if azure_api_key is not None:
            data_payload["azure-api-key"] = azure_api_key
        if alicloud_function_authorization is not None:
            data_payload["alicloud-function-authorization"] = (
                alicloud_function_authorization
            )
        if alicloud_access_key_id is not None:
            data_payload["alicloud-access-key-id"] = alicloud_access_key_id
        if alicloud_access_key_secret is not None:
            data_payload["alicloud-access-key-secret"] = (
                alicloud_access_key_secret
            )
        if message_type is not None:
            data_payload["message-type"] = message_type
        if message is not None:
            data_payload["message"] = message
        if replacement_message is not None:
            data_payload["replacement-message"] = replacement_message
        if replacemsg_group is not None:
            data_payload["replacemsg-group"] = replacemsg_group
        if protocol is not None:
            data_payload["protocol"] = protocol
        if method is not None:
            data_payload["method"] = method
        if uri is not None:
            data_payload["uri"] = uri
        if http_body is not None:
            data_payload["http-body"] = http_body
        if port is not None:
            data_payload["port"] = port
        if http_headers is not None:
            data_payload["http-headers"] = http_headers
        if form_data is not None:
            data_payload["form-data"] = form_data
        if verify_host_cert is not None:
            data_payload["verify-host-cert"] = verify_host_cert
        if script is not None:
            data_payload["script"] = script
        if output_size is not None:
            data_payload["output-size"] = output_size
        if timeout is not None:
            data_payload["timeout"] = timeout
        if duration is not None:
            data_payload["duration"] = duration
        if output_interval is not None:
            data_payload["output-interval"] = output_interval
        if file_only is not None:
            data_payload["file-only"] = file_only
        if execute_security_fabric is not None:
            data_payload["execute-security-fabric"] = execute_security_fabric
        if accprofile is not None:
            data_payload["accprofile"] = accprofile
        if regular_expression is not None:
            data_payload["regular-expression"] = regular_expression
        if log_debug_print is not None:
            data_payload["log-debug-print"] = log_debug_print
        if security_tag is not None:
            data_payload["security-tag"] = security_tag
        if sdn_connector is not None:
            data_payload["sdn-connector"] = sdn_connector
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
        endpoint = f"/system/automation-action/{name}"
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
        description: str | None = None,
        action_type: str | None = None,
        system_action: str | None = None,
        tls_certificate: str | None = None,
        forticare_email: str | None = None,
        email_to: list | None = None,
        email_from: str | None = None,
        email_subject: str | None = None,
        minimum_interval: int | None = None,
        aws_api_key: str | None = None,
        azure_function_authorization: str | None = None,
        azure_api_key: str | None = None,
        alicloud_function_authorization: str | None = None,
        alicloud_access_key_id: str | None = None,
        alicloud_access_key_secret: str | None = None,
        message_type: str | None = None,
        message: str | None = None,
        replacement_message: str | None = None,
        replacemsg_group: str | None = None,
        protocol: str | None = None,
        method: str | None = None,
        uri: str | None = None,
        http_body: str | None = None,
        port: int | None = None,
        http_headers: list | None = None,
        form_data: list | None = None,
        verify_host_cert: str | None = None,
        script: str | None = None,
        output_size: int | None = None,
        timeout: int | None = None,
        duration: int | None = None,
        output_interval: int | None = None,
        file_only: str | None = None,
        execute_security_fabric: str | None = None,
        accprofile: str | None = None,
        regular_expression: str | None = None,
        log_debug_print: str | None = None,
        security_tag: str | None = None,
        sdn_connector: list | None = None,
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
            name: Name. (optional)
            description: Description. (optional)
            action_type: Action type. (optional)
            system_action: System action type. (optional)
            tls_certificate: Custom TLS certificate for API request. (optional)
            forticare_email: Enable/disable use of your FortiCare email address
            as the email-to address. (optional)
            email_to: Email addresses. (optional)
            email_from: Email sender name. (optional)
            email_subject: Email subject. (optional)
            minimum_interval: Limit execution to no more than once in this
            interval (in seconds). (optional)
            aws_api_key: AWS API Gateway API key. (optional)
            azure_function_authorization: Azure function authorization level.
            (optional)
            azure_api_key: Azure function API key. (optional)
            alicloud_function_authorization: AliCloud function authorization
            type. (optional)
            alicloud_access_key_id: AliCloud AccessKey ID. (optional)
            alicloud_access_key_secret: AliCloud AccessKey secret. (optional)
            message_type: Message type. (optional)
            message: Message content. (optional)
            replacement_message: Enable/disable replacement message. (optional)
            replacemsg_group: Replacement message group. (optional)
            protocol: Request protocol. (optional)
            method: Request method (POST, PUT, GET, PATCH or DELETE).
            (optional)
            uri: Request API URI. (optional)
            http_body: Request body (if necessary). Should be serialized json
            string. (optional)
            port: Protocol port. (optional)
            http_headers: Request headers. (optional)
            form_data: Form data parts for content type multipart/form-data.
            (optional)
            verify_host_cert: Enable/disable verification of the remote host
            certificate. (optional)
            script: CLI script. (optional)
            output_size: Number of megabytes to limit script output to (1 -
            1024, default = 10). (optional)
            timeout: Maximum running time for this script in seconds (0 = no
            timeout). (optional)
            duration: Maximum running time for this script in seconds.
            (optional)
            output_interval: Collect the outputs for each output-interval in
            seconds (0 = no intermediate output). (optional)
            file_only: Enable/disable the output in files only. (optional)
            execute_security_fabric: Enable/disable execution of CLI script on
            all or only one FortiGate unit in the Security Fabric. (optional)
            accprofile: Access profile for CLI script action to access
            FortiGate features. (optional)
            regular_expression: Regular expression string. (optional)
            log_debug_print: Enable/disable logging debug print output from
            diagnose action. (optional)
            security_tag: NSX security tag. (optional)
            sdn_connector: NSX SDN connector names. (optional)
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
        endpoint = "/system/automation-action"
        if nkey is not None:
            data_payload["nkey"] = nkey
        if name is not None:
            data_payload["name"] = name
        if description is not None:
            data_payload["description"] = description
        if action_type is not None:
            data_payload["action-type"] = action_type
        if system_action is not None:
            data_payload["system-action"] = system_action
        if tls_certificate is not None:
            data_payload["tls-certificate"] = tls_certificate
        if forticare_email is not None:
            data_payload["forticare-email"] = forticare_email
        if email_to is not None:
            data_payload["email-to"] = email_to
        if email_from is not None:
            data_payload["email-from"] = email_from
        if email_subject is not None:
            data_payload["email-subject"] = email_subject
        if minimum_interval is not None:
            data_payload["minimum-interval"] = minimum_interval
        if aws_api_key is not None:
            data_payload["aws-api-key"] = aws_api_key
        if azure_function_authorization is not None:
            data_payload["azure-function-authorization"] = (
                azure_function_authorization
            )
        if azure_api_key is not None:
            data_payload["azure-api-key"] = azure_api_key
        if alicloud_function_authorization is not None:
            data_payload["alicloud-function-authorization"] = (
                alicloud_function_authorization
            )
        if alicloud_access_key_id is not None:
            data_payload["alicloud-access-key-id"] = alicloud_access_key_id
        if alicloud_access_key_secret is not None:
            data_payload["alicloud-access-key-secret"] = (
                alicloud_access_key_secret
            )
        if message_type is not None:
            data_payload["message-type"] = message_type
        if message is not None:
            data_payload["message"] = message
        if replacement_message is not None:
            data_payload["replacement-message"] = replacement_message
        if replacemsg_group is not None:
            data_payload["replacemsg-group"] = replacemsg_group
        if protocol is not None:
            data_payload["protocol"] = protocol
        if method is not None:
            data_payload["method"] = method
        if uri is not None:
            data_payload["uri"] = uri
        if http_body is not None:
            data_payload["http-body"] = http_body
        if port is not None:
            data_payload["port"] = port
        if http_headers is not None:
            data_payload["http-headers"] = http_headers
        if form_data is not None:
            data_payload["form-data"] = form_data
        if verify_host_cert is not None:
            data_payload["verify-host-cert"] = verify_host_cert
        if script is not None:
            data_payload["script"] = script
        if output_size is not None:
            data_payload["output-size"] = output_size
        if timeout is not None:
            data_payload["timeout"] = timeout
        if duration is not None:
            data_payload["duration"] = duration
        if output_interval is not None:
            data_payload["output-interval"] = output_interval
        if file_only is not None:
            data_payload["file-only"] = file_only
        if execute_security_fabric is not None:
            data_payload["execute-security-fabric"] = execute_security_fabric
        if accprofile is not None:
            data_payload["accprofile"] = accprofile
        if regular_expression is not None:
            data_payload["regular-expression"] = regular_expression
        if log_debug_print is not None:
            data_payload["log-debug-print"] = log_debug_print
        if security_tag is not None:
            data_payload["security-tag"] = security_tag
        if sdn_connector is not None:
            data_payload["sdn-connector"] = sdn_connector
        data_payload.update(kwargs)
        return self._client.post(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )
