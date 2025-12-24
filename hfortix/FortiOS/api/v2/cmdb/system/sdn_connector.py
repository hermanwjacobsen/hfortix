"""
FortiOS CMDB - Cmdb System Sdn Connector

Configuration endpoint for managing cmdb system sdn connector objects.

API Endpoints:
    GET    /cmdb/system/sdn_connector
    POST   /cmdb/system/sdn_connector
    GET    /cmdb/system/sdn_connector
    PUT    /cmdb/system/sdn_connector/{identifier}
    DELETE /cmdb/system/sdn_connector/{identifier}

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.system.sdn_connector.get()
    >>>
    >>> # Get specific item (if supported)
    >>> item = fgt.api.cmdb.system.sdn_connector.get(name="item_name")
    >>>
    >>> # Create new item (use POST)
    >>> result = fgt.api.cmdb.system.sdn_connector.post(
    ...     name="new_item",
    ...     # ... additional parameters
    ... )
    >>>
    >>> # Update existing item (use PUT)
    >>> result = fgt.api.cmdb.system.sdn_connector.put(
    ...     name="existing_item",
    ...     # ... parameters to update
    ... )
    >>>
    >>> # Delete item
    >>> result = fgt.api.cmdb.system.sdn_connector.delete(name="item_name")

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


class SdnConnector:
    """
    Sdnconnector Operations.

    Provides CRUD operations for FortiOS sdnconnector configuration.

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
        Initialize SdnConnector endpoint.

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
            endpoint = f"/system/sdn-connector/{name}"
        else:
            endpoint = "/system/sdn-connector"
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
        status: str | None = None,
        type: str | None = None,
        proxy: str | None = None,
        use_metadata_iam: str | None = None,
        microsoft_365: str | None = None,
        ha_status: str | None = None,
        verify_certificate: str | None = None,
        server: str | None = None,
        server_list: list | None = None,
        server_port: int | None = None,
        message_server_port: int | None = None,
        username: str | None = None,
        password: str | None = None,
        vcenter_server: str | None = None,
        vcenter_username: str | None = None,
        vcenter_password: str | None = None,
        access_key: str | None = None,
        secret_key: str | None = None,
        region: str | None = None,
        vpc_id: str | None = None,
        alt_resource_ip: str | None = None,
        external_account_list: list | None = None,
        tenant_id: str | None = None,
        client_id: str | None = None,
        client_secret: str | None = None,
        subscription_id: str | None = None,
        resource_group: str | None = None,
        login_endpoint: str | None = None,
        resource_url: str | None = None,
        azure_region: str | None = None,
        nic: list | None = None,
        route_table: list | None = None,
        user_id: str | None = None,
        compartment_list: list | None = None,
        oci_region_list: list | None = None,
        oci_region_type: str | None = None,
        oci_cert: str | None = None,
        oci_fingerprint: str | None = None,
        external_ip: list | None = None,
        route: list | None = None,
        gcp_project_list: list | None = None,
        forwarding_rule: list | None = None,
        service_account: str | None = None,
        private_key: str | None = None,
        secret_token: str | None = None,
        domain: str | None = None,
        group_name: str | None = None,
        server_cert: str | None = None,
        server_ca_cert: str | None = None,
        api_key: str | None = None,
        ibm_region: str | None = None,
        par_id: str | None = None,
        update_interval: int | None = None,
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
            name: SDN connector name. (optional)
            status: Enable/disable connection to the remote SDN connector.
            (optional)
            type: Type of SDN connector. (optional)
            proxy: SDN proxy. (optional)
            use_metadata_iam: Enable/disable use of IAM role from metadata to
            call API. (optional)
            microsoft_365: Enable to use as Microsoft 365 connector. (optional)
            ha_status: Enable/disable use for FortiGate HA service. (optional)
            verify_certificate: Enable/disable server certificate verification.
            (optional)
            server: Server address of the remote SDN connector. (optional)
            server_list: Server address list of the remote SDN connector.
            (optional)
            server_port: Port number of the remote SDN connector. (optional)
            message_server_port: HTTP port number of the SAP message server.
            (optional)
            username: Username of the remote SDN connector as login
            credentials. (optional)
            password: Password of the remote SDN connector as login
            credentials. (optional)
            vcenter_server: vCenter server address for NSX quarantine.
            (optional)
            vcenter_username: vCenter server username for NSX quarantine.
            (optional)
            vcenter_password: vCenter server password for NSX quarantine.
            (optional)
            access_key: AWS / ACS access key ID. (optional)
            secret_key: AWS / ACS secret access key. (optional)
            region: AWS / ACS region name. (optional)
            vpc_id: AWS VPC ID. (optional)
            alt_resource_ip: Enable/disable AWS alternative resource IP.
            (optional)
            external_account_list: Configure AWS external account list.
            (optional)
            tenant_id: Tenant ID (directory ID). (optional)
            client_id: Azure client ID (application ID). (optional)
            client_secret: Azure client secret (application key). (optional)
            subscription_id: Azure subscription ID. (optional)
            resource_group: Azure resource group. (optional)
            login_endpoint: Azure Stack login endpoint. (optional)
            resource_url: Azure Stack resource URL. (optional)
            azure_region: Azure server region. (optional)
            nic: Configure Azure network interface. (optional)
            route_table: Configure Azure route table. (optional)
            user_id: User ID. (optional)
            compartment_list: Configure OCI compartment list. (optional)
            oci_region_list: Configure OCI region list. (optional)
            oci_region_type: OCI region type. (optional)
            oci_cert: OCI certificate. (optional)
            oci_fingerprint: OCI pubkey fingerprint. (optional)
            external_ip: Configure GCP external IP. (optional)
            route: Configure GCP route. (optional)
            gcp_project_list: Configure GCP project list. (optional)
            forwarding_rule: Configure GCP forwarding rule. (optional)
            service_account: GCP service account email. (optional)
            private_key: Private key of GCP service account. (optional)
            secret_token: Secret token of Kubernetes service account.
            (optional)
            domain: Domain name. (optional)
            group_name: Full path group name of computers. (optional)
            server_cert: Trust servers that contain this certificate only.
            (optional)
            server_ca_cert: Trust only those servers whose certificate is
            directly/indirectly signed by this certificate. (optional)
            api_key: IBM cloud API key or service ID API key. (optional)
            ibm_region: IBM cloud region name. (optional)
            par_id: Public address range ID. (optional)
            update_interval: Dynamic object update interval (30 - 3600 sec,
            default = 60, 0 = disabled). (optional)
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
        endpoint = f"/system/sdn-connector/{name}"
        if before is not None:
            data_payload["before"] = before
        if after is not None:
            data_payload["after"] = after
        if name is not None:
            data_payload["name"] = name
        if status is not None:
            data_payload["status"] = status
        if type is not None:
            data_payload["type"] = type
        if proxy is not None:
            data_payload["proxy"] = proxy
        if use_metadata_iam is not None:
            data_payload["use-metadata-iam"] = use_metadata_iam
        if microsoft_365 is not None:
            data_payload["microsoft-365"] = microsoft_365
        if ha_status is not None:
            data_payload["ha-status"] = ha_status
        if verify_certificate is not None:
            data_payload["verify-certificate"] = verify_certificate
        if server is not None:
            data_payload["server"] = server
        if server_list is not None:
            data_payload["server-list"] = server_list
        if server_port is not None:
            data_payload["server-port"] = server_port
        if message_server_port is not None:
            data_payload["message-server-port"] = message_server_port
        if username is not None:
            data_payload["username"] = username
        if password is not None:
            data_payload["password"] = password
        if vcenter_server is not None:
            data_payload["vcenter-server"] = vcenter_server
        if vcenter_username is not None:
            data_payload["vcenter-username"] = vcenter_username
        if vcenter_password is not None:
            data_payload["vcenter-password"] = vcenter_password
        if access_key is not None:
            data_payload["access-key"] = access_key
        if secret_key is not None:
            data_payload["secret-key"] = secret_key
        if region is not None:
            data_payload["region"] = region
        if vpc_id is not None:
            data_payload["vpc-id"] = vpc_id
        if alt_resource_ip is not None:
            data_payload["alt-resource-ip"] = alt_resource_ip
        if external_account_list is not None:
            data_payload["external-account-list"] = external_account_list
        if tenant_id is not None:
            data_payload["tenant-id"] = tenant_id
        if client_id is not None:
            data_payload["client-id"] = client_id
        if client_secret is not None:
            data_payload["client-secret"] = client_secret
        if subscription_id is not None:
            data_payload["subscription-id"] = subscription_id
        if resource_group is not None:
            data_payload["resource-group"] = resource_group
        if login_endpoint is not None:
            data_payload["login-endpoint"] = login_endpoint
        if resource_url is not None:
            data_payload["resource-url"] = resource_url
        if azure_region is not None:
            data_payload["azure-region"] = azure_region
        if nic is not None:
            data_payload["nic"] = nic
        if route_table is not None:
            data_payload["route-table"] = route_table
        if user_id is not None:
            data_payload["user-id"] = user_id
        if compartment_list is not None:
            data_payload["compartment-list"] = compartment_list
        if oci_region_list is not None:
            data_payload["oci-region-list"] = oci_region_list
        if oci_region_type is not None:
            data_payload["oci-region-type"] = oci_region_type
        if oci_cert is not None:
            data_payload["oci-cert"] = oci_cert
        if oci_fingerprint is not None:
            data_payload["oci-fingerprint"] = oci_fingerprint
        if external_ip is not None:
            data_payload["external-ip"] = external_ip
        if route is not None:
            data_payload["route"] = route
        if gcp_project_list is not None:
            data_payload["gcp-project-list"] = gcp_project_list
        if forwarding_rule is not None:
            data_payload["forwarding-rule"] = forwarding_rule
        if service_account is not None:
            data_payload["service-account"] = service_account
        if private_key is not None:
            data_payload["private-key"] = private_key
        if secret_token is not None:
            data_payload["secret-token"] = secret_token
        if domain is not None:
            data_payload["domain"] = domain
        if group_name is not None:
            data_payload["group-name"] = group_name
        if server_cert is not None:
            data_payload["server-cert"] = server_cert
        if server_ca_cert is not None:
            data_payload["server-ca-cert"] = server_ca_cert
        if api_key is not None:
            data_payload["api-key"] = api_key
        if ibm_region is not None:
            data_payload["ibm-region"] = ibm_region
        if par_id is not None:
            data_payload["par-id"] = par_id
        if update_interval is not None:
            data_payload["update-interval"] = update_interval
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
        endpoint = f"/system/sdn-connector/{name}"
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
        status: str | None = None,
        type: str | None = None,
        proxy: str | None = None,
        use_metadata_iam: str | None = None,
        microsoft_365: str | None = None,
        ha_status: str | None = None,
        verify_certificate: str | None = None,
        server: str | None = None,
        server_list: list | None = None,
        server_port: int | None = None,
        message_server_port: int | None = None,
        username: str | None = None,
        password: str | None = None,
        vcenter_server: str | None = None,
        vcenter_username: str | None = None,
        vcenter_password: str | None = None,
        access_key: str | None = None,
        secret_key: str | None = None,
        region: str | None = None,
        vpc_id: str | None = None,
        alt_resource_ip: str | None = None,
        external_account_list: list | None = None,
        tenant_id: str | None = None,
        client_id: str | None = None,
        client_secret: str | None = None,
        subscription_id: str | None = None,
        resource_group: str | None = None,
        login_endpoint: str | None = None,
        resource_url: str | None = None,
        azure_region: str | None = None,
        nic: list | None = None,
        route_table: list | None = None,
        user_id: str | None = None,
        compartment_list: list | None = None,
        oci_region_list: list | None = None,
        oci_region_type: str | None = None,
        oci_cert: str | None = None,
        oci_fingerprint: str | None = None,
        external_ip: list | None = None,
        route: list | None = None,
        gcp_project_list: list | None = None,
        forwarding_rule: list | None = None,
        service_account: str | None = None,
        private_key: str | None = None,
        secret_token: str | None = None,
        domain: str | None = None,
        group_name: str | None = None,
        server_cert: str | None = None,
        server_ca_cert: str | None = None,
        api_key: str | None = None,
        ibm_region: str | None = None,
        par_id: str | None = None,
        update_interval: int | None = None,
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
            name: SDN connector name. (optional)
            status: Enable/disable connection to the remote SDN connector.
            (optional)
            type: Type of SDN connector. (optional)
            proxy: SDN proxy. (optional)
            use_metadata_iam: Enable/disable use of IAM role from metadata to
            call API. (optional)
            microsoft_365: Enable to use as Microsoft 365 connector. (optional)
            ha_status: Enable/disable use for FortiGate HA service. (optional)
            verify_certificate: Enable/disable server certificate verification.
            (optional)
            server: Server address of the remote SDN connector. (optional)
            server_list: Server address list of the remote SDN connector.
            (optional)
            server_port: Port number of the remote SDN connector. (optional)
            message_server_port: HTTP port number of the SAP message server.
            (optional)
            username: Username of the remote SDN connector as login
            credentials. (optional)
            password: Password of the remote SDN connector as login
            credentials. (optional)
            vcenter_server: vCenter server address for NSX quarantine.
            (optional)
            vcenter_username: vCenter server username for NSX quarantine.
            (optional)
            vcenter_password: vCenter server password for NSX quarantine.
            (optional)
            access_key: AWS / ACS access key ID. (optional)
            secret_key: AWS / ACS secret access key. (optional)
            region: AWS / ACS region name. (optional)
            vpc_id: AWS VPC ID. (optional)
            alt_resource_ip: Enable/disable AWS alternative resource IP.
            (optional)
            external_account_list: Configure AWS external account list.
            (optional)
            tenant_id: Tenant ID (directory ID). (optional)
            client_id: Azure client ID (application ID). (optional)
            client_secret: Azure client secret (application key). (optional)
            subscription_id: Azure subscription ID. (optional)
            resource_group: Azure resource group. (optional)
            login_endpoint: Azure Stack login endpoint. (optional)
            resource_url: Azure Stack resource URL. (optional)
            azure_region: Azure server region. (optional)
            nic: Configure Azure network interface. (optional)
            route_table: Configure Azure route table. (optional)
            user_id: User ID. (optional)
            compartment_list: Configure OCI compartment list. (optional)
            oci_region_list: Configure OCI region list. (optional)
            oci_region_type: OCI region type. (optional)
            oci_cert: OCI certificate. (optional)
            oci_fingerprint: OCI pubkey fingerprint. (optional)
            external_ip: Configure GCP external IP. (optional)
            route: Configure GCP route. (optional)
            gcp_project_list: Configure GCP project list. (optional)
            forwarding_rule: Configure GCP forwarding rule. (optional)
            service_account: GCP service account email. (optional)
            private_key: Private key of GCP service account. (optional)
            secret_token: Secret token of Kubernetes service account.
            (optional)
            domain: Domain name. (optional)
            group_name: Full path group name of computers. (optional)
            server_cert: Trust servers that contain this certificate only.
            (optional)
            server_ca_cert: Trust only those servers whose certificate is
            directly/indirectly signed by this certificate. (optional)
            api_key: IBM cloud API key or service ID API key. (optional)
            ibm_region: IBM cloud region name. (optional)
            par_id: Public address range ID. (optional)
            update_interval: Dynamic object update interval (30 - 3600 sec,
            default = 60, 0 = disabled). (optional)
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
        endpoint = "/system/sdn-connector"
        if nkey is not None:
            data_payload["nkey"] = nkey
        if name is not None:
            data_payload["name"] = name
        if status is not None:
            data_payload["status"] = status
        if type is not None:
            data_payload["type"] = type
        if proxy is not None:
            data_payload["proxy"] = proxy
        if use_metadata_iam is not None:
            data_payload["use-metadata-iam"] = use_metadata_iam
        if microsoft_365 is not None:
            data_payload["microsoft-365"] = microsoft_365
        if ha_status is not None:
            data_payload["ha-status"] = ha_status
        if verify_certificate is not None:
            data_payload["verify-certificate"] = verify_certificate
        if server is not None:
            data_payload["server"] = server
        if server_list is not None:
            data_payload["server-list"] = server_list
        if server_port is not None:
            data_payload["server-port"] = server_port
        if message_server_port is not None:
            data_payload["message-server-port"] = message_server_port
        if username is not None:
            data_payload["username"] = username
        if password is not None:
            data_payload["password"] = password
        if vcenter_server is not None:
            data_payload["vcenter-server"] = vcenter_server
        if vcenter_username is not None:
            data_payload["vcenter-username"] = vcenter_username
        if vcenter_password is not None:
            data_payload["vcenter-password"] = vcenter_password
        if access_key is not None:
            data_payload["access-key"] = access_key
        if secret_key is not None:
            data_payload["secret-key"] = secret_key
        if region is not None:
            data_payload["region"] = region
        if vpc_id is not None:
            data_payload["vpc-id"] = vpc_id
        if alt_resource_ip is not None:
            data_payload["alt-resource-ip"] = alt_resource_ip
        if external_account_list is not None:
            data_payload["external-account-list"] = external_account_list
        if tenant_id is not None:
            data_payload["tenant-id"] = tenant_id
        if client_id is not None:
            data_payload["client-id"] = client_id
        if client_secret is not None:
            data_payload["client-secret"] = client_secret
        if subscription_id is not None:
            data_payload["subscription-id"] = subscription_id
        if resource_group is not None:
            data_payload["resource-group"] = resource_group
        if login_endpoint is not None:
            data_payload["login-endpoint"] = login_endpoint
        if resource_url is not None:
            data_payload["resource-url"] = resource_url
        if azure_region is not None:
            data_payload["azure-region"] = azure_region
        if nic is not None:
            data_payload["nic"] = nic
        if route_table is not None:
            data_payload["route-table"] = route_table
        if user_id is not None:
            data_payload["user-id"] = user_id
        if compartment_list is not None:
            data_payload["compartment-list"] = compartment_list
        if oci_region_list is not None:
            data_payload["oci-region-list"] = oci_region_list
        if oci_region_type is not None:
            data_payload["oci-region-type"] = oci_region_type
        if oci_cert is not None:
            data_payload["oci-cert"] = oci_cert
        if oci_fingerprint is not None:
            data_payload["oci-fingerprint"] = oci_fingerprint
        if external_ip is not None:
            data_payload["external-ip"] = external_ip
        if route is not None:
            data_payload["route"] = route
        if gcp_project_list is not None:
            data_payload["gcp-project-list"] = gcp_project_list
        if forwarding_rule is not None:
            data_payload["forwarding-rule"] = forwarding_rule
        if service_account is not None:
            data_payload["service-account"] = service_account
        if private_key is not None:
            data_payload["private-key"] = private_key
        if secret_token is not None:
            data_payload["secret-token"] = secret_token
        if domain is not None:
            data_payload["domain"] = domain
        if group_name is not None:
            data_payload["group-name"] = group_name
        if server_cert is not None:
            data_payload["server-cert"] = server_cert
        if server_ca_cert is not None:
            data_payload["server-ca-cert"] = server_ca_cert
        if api_key is not None:
            data_payload["api-key"] = api_key
        if ibm_region is not None:
            data_payload["ibm-region"] = ibm_region
        if par_id is not None:
            data_payload["par-id"] = par_id
        if update_interval is not None:
            data_payload["update-interval"] = update_interval
        data_payload.update(kwargs)
        return self._client.post(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )
