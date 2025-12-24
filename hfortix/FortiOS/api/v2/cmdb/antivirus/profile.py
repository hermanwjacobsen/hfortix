"""
FortiOS CMDB - Cmdb Antivirus Profile

Configuration endpoint for managing cmdb antivirus profile objects.

API Endpoints:
    GET    /cmdb/antivirus/profile
    POST   /cmdb/antivirus/profile
    GET    /cmdb/antivirus/profile
    PUT    /cmdb/antivirus/profile/{identifier}
    DELETE /cmdb/antivirus/profile/{identifier}

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.antivirus.profile.get()
    >>>
    >>> # Get specific item (if supported)
    >>> item = fgt.api.cmdb.antivirus.profile.get(name="item_name")
    >>>
    >>> # Create new item (use POST)
    >>> result = fgt.api.cmdb.antivirus.profile.post(
    ...     name="new_item",
    ...     # ... additional parameters
    ... )
    >>>
    >>> # Update existing item (use PUT)
    >>> result = fgt.api.cmdb.antivirus.profile.put(
    ...     name="existing_item",
    ...     # ... parameters to update
    ... )
    >>>
    >>> # Delete item
    >>> result = fgt.api.cmdb.antivirus.profile.delete(name="item_name")

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
            endpoint = f"/antivirus/profile/{name}"
        else:
            endpoint = "/antivirus/profile"
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
        comment: str | None = None,
        replacemsg_group: str | None = None,
        feature_set: str | None = None,
        fortisandbox_mode: str | None = None,
        fortisandbox_max_upload: int | None = None,
        analytics_ignore_filetype: int | None = None,
        analytics_accept_filetype: int | None = None,
        analytics_db: str | None = None,
        mobile_malware_db: str | None = None,
        http: list | None = None,
        ftp: list | None = None,
        imap: list | None = None,
        pop3: list | None = None,
        smtp: list | None = None,
        mapi: list | None = None,
        nntp: list | None = None,
        cifs: list | None = None,
        ssh: list | None = None,
        nac_quar: list | None = None,
        content_disarm: list | None = None,
        outbreak_prevention_archive_scan: str | None = None,
        external_blocklist_enable_all: str | None = None,
        external_blocklist: list | None = None,
        ems_threat_feed: str | None = None,
        av_virus_log: str | None = None,
        extended_log: str | None = None,
        scan_mode: str | None = None,
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
            name: Profile name. (optional)
            comment: Comment. (optional)
            replacemsg_group: Replacement message group customized for this
            profile. (optional)
            feature_set: Flow/proxy feature set. (optional)
            fortisandbox_mode: FortiSandbox scan modes. (optional)
            fortisandbox_max_upload: Maximum size of files that can be uploaded
            to FortiSandbox in Mbytes. (optional)
            analytics_ignore_filetype: Do not submit files matching this DLP
            file-pattern to FortiSandbox (post-transfer scan only). (optional)
            analytics_accept_filetype: Only submit files matching this DLP
            file-pattern to FortiSandbox (post-transfer scan only). (optional)
            analytics_db: Enable/disable using the FortiSandbox signature
            database to supplement the AV signature databases. (optional)
            mobile_malware_db: Enable/disable using the mobile malware
            signature database. (optional)
            http: Configure HTTP AntiVirus options. (optional)
            ftp: Configure FTP AntiVirus options. (optional)
            imap: Configure IMAP AntiVirus options. (optional)
            pop3: Configure POP3 AntiVirus options. (optional)
            smtp: Configure SMTP AntiVirus options. (optional)
            mapi: Configure MAPI AntiVirus options. (optional)
            nntp: Configure NNTP AntiVirus options. (optional)
            cifs: Configure CIFS AntiVirus options. (optional)
            ssh: Configure SFTP and SCP AntiVirus options. (optional)
            nac_quar: Configure AntiVirus quarantine settings. (optional)
            content_disarm: AV Content Disarm and Reconstruction settings.
            (optional)
            outbreak_prevention_archive_scan: Enable/disable
            outbreak-prevention archive scanning. (optional)
            external_blocklist_enable_all: Enable/disable all external
            blocklists. (optional)
            external_blocklist: One or more external malware block lists.
            (optional)
            ems_threat_feed: Enable/disable use of EMS threat feed when
            performing AntiVirus scan. Analyzes files including the content of
            archives. (optional)
            av_virus_log: Enable/disable AntiVirus logging. (optional)
            extended_log: Enable/disable extended logging for antivirus.
            (optional)
            scan_mode: Configure scan mode (default or legacy). (optional)
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
        endpoint = f"/antivirus/profile/{name}"
        if before is not None:
            data_payload["before"] = before
        if after is not None:
            data_payload["after"] = after
        if name is not None:
            data_payload["name"] = name
        if comment is not None:
            data_payload["comment"] = comment
        if replacemsg_group is not None:
            data_payload["replacemsg-group"] = replacemsg_group
        if feature_set is not None:
            data_payload["feature-set"] = feature_set
        if fortisandbox_mode is not None:
            data_payload["fortisandbox-mode"] = fortisandbox_mode
        if fortisandbox_max_upload is not None:
            data_payload["fortisandbox-max-upload"] = fortisandbox_max_upload
        if analytics_ignore_filetype is not None:
            data_payload["analytics-ignore-filetype"] = (
                analytics_ignore_filetype
            )
        if analytics_accept_filetype is not None:
            data_payload["analytics-accept-filetype"] = (
                analytics_accept_filetype
            )
        if analytics_db is not None:
            data_payload["analytics-db"] = analytics_db
        if mobile_malware_db is not None:
            data_payload["mobile-malware-db"] = mobile_malware_db
        if http is not None:
            data_payload["http"] = http
        if ftp is not None:
            data_payload["ftp"] = ftp
        if imap is not None:
            data_payload["imap"] = imap
        if pop3 is not None:
            data_payload["pop3"] = pop3
        if smtp is not None:
            data_payload["smtp"] = smtp
        if mapi is not None:
            data_payload["mapi"] = mapi
        if nntp is not None:
            data_payload["nntp"] = nntp
        if cifs is not None:
            data_payload["cifs"] = cifs
        if ssh is not None:
            data_payload["ssh"] = ssh
        if nac_quar is not None:
            data_payload["nac-quar"] = nac_quar
        if content_disarm is not None:
            data_payload["content-disarm"] = content_disarm
        if outbreak_prevention_archive_scan is not None:
            data_payload["outbreak-prevention-archive-scan"] = (
                outbreak_prevention_archive_scan
            )
        if external_blocklist_enable_all is not None:
            data_payload["external-blocklist-enable-all"] = (
                external_blocklist_enable_all
            )
        if external_blocklist is not None:
            data_payload["external-blocklist"] = external_blocklist
        if ems_threat_feed is not None:
            data_payload["ems-threat-feed"] = ems_threat_feed
        if av_virus_log is not None:
            data_payload["av-virus-log"] = av_virus_log
        if extended_log is not None:
            data_payload["extended-log"] = extended_log
        if scan_mode is not None:
            data_payload["scan-mode"] = scan_mode
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
        endpoint = f"/antivirus/profile/{name}"
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
        comment: str | None = None,
        replacemsg_group: str | None = None,
        feature_set: str | None = None,
        fortisandbox_mode: str | None = None,
        fortisandbox_max_upload: int | None = None,
        analytics_ignore_filetype: int | None = None,
        analytics_accept_filetype: int | None = None,
        analytics_db: str | None = None,
        mobile_malware_db: str | None = None,
        http: list | None = None,
        ftp: list | None = None,
        imap: list | None = None,
        pop3: list | None = None,
        smtp: list | None = None,
        mapi: list | None = None,
        nntp: list | None = None,
        cifs: list | None = None,
        ssh: list | None = None,
        nac_quar: list | None = None,
        content_disarm: list | None = None,
        outbreak_prevention_archive_scan: str | None = None,
        external_blocklist_enable_all: str | None = None,
        external_blocklist: list | None = None,
        ems_threat_feed: str | None = None,
        av_virus_log: str | None = None,
        extended_log: str | None = None,
        scan_mode: str | None = None,
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
            name: Profile name. (optional)
            comment: Comment. (optional)
            replacemsg_group: Replacement message group customized for this
            profile. (optional)
            feature_set: Flow/proxy feature set. (optional)
            fortisandbox_mode: FortiSandbox scan modes. (optional)
            fortisandbox_max_upload: Maximum size of files that can be uploaded
            to FortiSandbox in Mbytes. (optional)
            analytics_ignore_filetype: Do not submit files matching this DLP
            file-pattern to FortiSandbox (post-transfer scan only). (optional)
            analytics_accept_filetype: Only submit files matching this DLP
            file-pattern to FortiSandbox (post-transfer scan only). (optional)
            analytics_db: Enable/disable using the FortiSandbox signature
            database to supplement the AV signature databases. (optional)
            mobile_malware_db: Enable/disable using the mobile malware
            signature database. (optional)
            http: Configure HTTP AntiVirus options. (optional)
            ftp: Configure FTP AntiVirus options. (optional)
            imap: Configure IMAP AntiVirus options. (optional)
            pop3: Configure POP3 AntiVirus options. (optional)
            smtp: Configure SMTP AntiVirus options. (optional)
            mapi: Configure MAPI AntiVirus options. (optional)
            nntp: Configure NNTP AntiVirus options. (optional)
            cifs: Configure CIFS AntiVirus options. (optional)
            ssh: Configure SFTP and SCP AntiVirus options. (optional)
            nac_quar: Configure AntiVirus quarantine settings. (optional)
            content_disarm: AV Content Disarm and Reconstruction settings.
            (optional)
            outbreak_prevention_archive_scan: Enable/disable
            outbreak-prevention archive scanning. (optional)
            external_blocklist_enable_all: Enable/disable all external
            blocklists. (optional)
            external_blocklist: One or more external malware block lists.
            (optional)
            ems_threat_feed: Enable/disable use of EMS threat feed when
            performing AntiVirus scan. Analyzes files including the content of
            archives. (optional)
            av_virus_log: Enable/disable AntiVirus logging. (optional)
            extended_log: Enable/disable extended logging for antivirus.
            (optional)
            scan_mode: Configure scan mode (default or legacy). (optional)
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
        endpoint = "/antivirus/profile"
        if nkey is not None:
            data_payload["nkey"] = nkey
        if name is not None:
            data_payload["name"] = name
        if comment is not None:
            data_payload["comment"] = comment
        if replacemsg_group is not None:
            data_payload["replacemsg-group"] = replacemsg_group
        if feature_set is not None:
            data_payload["feature-set"] = feature_set
        if fortisandbox_mode is not None:
            data_payload["fortisandbox-mode"] = fortisandbox_mode
        if fortisandbox_max_upload is not None:
            data_payload["fortisandbox-max-upload"] = fortisandbox_max_upload
        if analytics_ignore_filetype is not None:
            data_payload["analytics-ignore-filetype"] = (
                analytics_ignore_filetype
            )
        if analytics_accept_filetype is not None:
            data_payload["analytics-accept-filetype"] = (
                analytics_accept_filetype
            )
        if analytics_db is not None:
            data_payload["analytics-db"] = analytics_db
        if mobile_malware_db is not None:
            data_payload["mobile-malware-db"] = mobile_malware_db
        if http is not None:
            data_payload["http"] = http
        if ftp is not None:
            data_payload["ftp"] = ftp
        if imap is not None:
            data_payload["imap"] = imap
        if pop3 is not None:
            data_payload["pop3"] = pop3
        if smtp is not None:
            data_payload["smtp"] = smtp
        if mapi is not None:
            data_payload["mapi"] = mapi
        if nntp is not None:
            data_payload["nntp"] = nntp
        if cifs is not None:
            data_payload["cifs"] = cifs
        if ssh is not None:
            data_payload["ssh"] = ssh
        if nac_quar is not None:
            data_payload["nac-quar"] = nac_quar
        if content_disarm is not None:
            data_payload["content-disarm"] = content_disarm
        if outbreak_prevention_archive_scan is not None:
            data_payload["outbreak-prevention-archive-scan"] = (
                outbreak_prevention_archive_scan
            )
        if external_blocklist_enable_all is not None:
            data_payload["external-blocklist-enable-all"] = (
                external_blocklist_enable_all
            )
        if external_blocklist is not None:
            data_payload["external-blocklist"] = external_blocklist
        if ems_threat_feed is not None:
            data_payload["ems-threat-feed"] = ems_threat_feed
        if av_virus_log is not None:
            data_payload["av-virus-log"] = av_virus_log
        if extended_log is not None:
            data_payload["extended-log"] = extended_log
        if scan_mode is not None:
            data_payload["scan-mode"] = scan_mode
        data_payload.update(kwargs)
        return self._client.post(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )
