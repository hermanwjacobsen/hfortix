"""
FortiOS CMDB - Antivirus Profile
Configure AntiVirus profiles

API Endpoints:
    GET    /antivirus/profile       - Get all antivirus profiles
    GET    /antivirus/profile/{name} - Get specific antivirus profile
    POST   /antivirus/profile       - Create antivirus profile
    PUT    /antivirus/profile/{name} - Update antivirus profile
    DELETE /antivirus/profile/{name} - Delete antivirus profile
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Dict, Optional, Union

if TYPE_CHECKING:
    from ....http_client import HTTPClient


from hfortix.FortiOS.http_client import encode_path_component


class Profile:
    """Antivirus Profile endpoint"""

    def __init__(self, client: "HTTPClient") -> None:
        self._client = client

    def get(
        self,
        name: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
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
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        GET /antivirus/profile or /antivirus/profile/{name}
        Get antivirus profiles

        Args:
            name: Profile name (if None, returns all profiles)
            vdom: Virtual domain (optional)

            Query parameters (all optional):
            attr: Attribute name that references other table
            count: Maximum number of entries to return
            skip_to_datasource: Skip to provided table's Nth entry
            acs: If true, returned result are in ascending order
            search: Filter objects by search value
            scope: Scope (global|vdom|both)
            datasource: Include datasource information for each linked object
            with_meta: Include meta information about each object (type id, references, etc)
            skip: Enable CLI skip operator to hide skipped properties
            format: List of property names to include (e.g., 'name|comment|scan-mode')
            action: Special actions (default, schema, revision)
            **kwargs: Any additional parameters

        Returns:
            Antivirus profile or list of profiles

        Examples:
            >>> # Get all profiles
            >>> profiles = fgt.cmdb.antivirus.profile.get()

            >>> # Get specific profile
            >>> profile = fgt.cmdb.antivirus.profile.get('default')

            >>> # Get with meta information
            >>> profiles = fgt.cmdb.antivirus.profile.get(with_meta=True)

            >>> # Get with filters and format
            >>> profiles = fgt.cmdb.antivirus.profile.get(
            ...     format='name|comment|scan-mode',
            ...     search='corporate',
            ...     count=10
            ... )
        """
        # Build params dict from provided parameters
        params = {}

        # Map parameters
        param_map = {
            "attr": attr,
            "count": count,
            "skip_to_datasource": skip_to_datasource,
            "acs": acs,
            "search": search,
            "scope": scope,
            "datasource": datasource,
            "with_meta": with_meta,
            "skip": skip,
            "format": format,
            "action": action,
        }

        # Add non-None parameters
        for key, value in param_map.items():
            if value is not None:
                params[key] = value

        # Add any extra kwargs
        params.update(kwargs)

        path = f"antivirus/profile/{encode_path_component(name)}" if name else "antivirus/profile"
        return self._client.get(
            "cmdb", path, params=params if params else None, vdom=vdom, raw_json=raw_json
        )

    def post(
        self,
        payload_dict: Optional[Dict[str, Any]] = None,
        name: Optional[str] = None,
        comment: Optional[str] = None,
        replacemsg_group: Optional[str] = None,
        scan_mode: Optional[str] = None,
        mobile_malware_db: Optional[str] = None,
        analytics_max_upload: Optional[int] = None,
        analytics_ignore_filetype: Optional[int] = None,
        analytics_accept_filetype: Optional[int] = None,
        analytics_wl_filetype: Optional[int] = None,
        analytics_bl_filetype: Optional[int] = None,
        analytics_db: Optional[str] = None,
        feature_set: Optional[str] = None,
        fortindr_error_action: Optional[str] = None,
        fortindr_timeout_action: Optional[str] = None,
        fortisandbox_mode: Optional[str] = None,
        fortisandbox_max_upload: Optional[int] = None,
        fortisandbox_error_action: Optional[str] = None,
        fortisandbox_timeout_action: Optional[str] = None,
        outbreak_prevention_mode: Optional[str] = None,
        outbreak_prevention_archive_scan: Optional[str] = None,
        external_blocklist_enable_all: Optional[str] = None,
        external_blocklist_archive_scan: Optional[str] = None,
        ems_threat_feed: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        POST /antivirus/profile
        Create antivirus profile

        Args:
            name: Profile name (required, max 35 chars)
            comment: Comment (max 255 chars)
            replacemsg_group: Replacement message group
            scan_mode: Scan mode - 'quick', 'full', 'legacy', 'default'
            mobile_malware_db: Enable/disable mobile malware database - 'disable' or 'enable'
            analytics_max_upload: Maximum size of files uploaded to FortiSandbox (1-395 MB)
            analytics_ignore_filetype: File types to ignore for FortiSandbox inspection
            analytics_accept_filetype: File types to submit for FortiSandbox inspection
            analytics_wl_filetype: Whitelist file types
            analytics_bl_filetype: Blacklist file types
            analytics_db: Enable/disable using FortiSandbox signature database - 'disable' or 'enable'
            feature_set: Flow/proxy feature set - 'flow' or 'proxy'
            fortindr_error_action: Action on FortiNDR error - 'pass' or 'block'
            fortindr_timeout_action: Action on FortiNDR timeout - 'pass' or 'block'
            fortisandbox_mode: FortiSandbox inline mode - 'inline' or 'analytics-suspicious'
            fortisandbox_max_upload: Maximum size for FortiSandbox upload (1-395 MB)
            fortisandbox_error_action: Action on FortiSandbox error - 'pass' or 'block'
            fortisandbox_timeout_action: Action on FortiSandbox timeout - 'pass' or 'block'
            outbreak_prevention_mode: Outbreak prevention mode - 'disabled', 'files', 'full-archive', 'pass', 'block'
            outbreak_prevention_archive_scan: Archive scan setting - 'disable' or 'enable'
            external_blocklist_enable_all: Enable/disable all external blocklists - 'disable' or 'enable'
            external_blocklist_archive_scan: External blocklist archive scan - 'disable' or 'enable'
            ems_threat_feed: Enable/disable EMS threat feed - 'disable' or 'enable'
            vdom: Virtual domain (optional)
            **kwargs: Any additional parameters (http, ftp, imap, pop3, smtp, mapi, nntp, cifs, ssh)

        Returns:
            Response dict with status

        Examples:
            >>> # POST - Create basic profile
            >>> fgt.cmdb.antivirus.profile.create(
            ...     name='corporate_av',
            ...     comment='Corporate antivirus policy',
            ...     scan_mode='full',
            ...     analytics_db='enable'
            ... )

            >>> # POST - Create with FortiSandbox
            >>> fgt.cmdb.antivirus.profile.create(
            ...     name='strict_av',
            ...     scan_mode='full',
            ...     fortisandbox_mode='inline',
            ...     fortisandbox_max_upload=50,
            ...     fortisandbox_error_action='block'
            ... )
        """
        # Build data dict from provided parameters
        payload_dict = {"name": name}

        # Map Python parameter names to API field names
        param_map = {
            "comment": comment,
            "replacemsg_group": replacemsg_group,
            "scan_mode": scan_mode,
            "mobile_malware_db": mobile_malware_db,
            "analytics_max_upload": analytics_max_upload,
            "analytics_ignore_filetype": analytics_ignore_filetype,
            "analytics_accept_filetype": analytics_accept_filetype,
            "analytics_wl_filetype": analytics_wl_filetype,
            "analytics_bl_filetype": analytics_bl_filetype,
            "analytics_db": analytics_db,
            "feature_set": feature_set,
            "fortindr_error_action": fortindr_error_action,
            "fortindr_timeout_action": fortindr_timeout_action,
            "fortisandbox_mode": fortisandbox_mode,
            "fortisandbox_max_upload": fortisandbox_max_upload,
            "fortisandbox_error_action": fortisandbox_error_action,
            "fortisandbox_timeout_action": fortisandbox_timeout_action,
            "outbreak_prevention_mode": outbreak_prevention_mode,
            "outbreak_prevention_archive_scan": outbreak_prevention_archive_scan,
            "external_blocklist_enable_all": external_blocklist_enable_all,
            "external_blocklist_archive_scan": external_blocklist_archive_scan,
            "ems_threat_feed": ems_threat_feed,
        }

        # API field name mapping
        api_field_map = {
            "comment": "comment",
            "replacemsg_group": "replacemsg-group",
            "scan_mode": "scan-mode",
            "mobile_malware_db": "mobile-malware-db",
            "analytics_max_upload": "analytics-max-upload",
            "analytics_ignore_filetype": "analytics-ignore-filetype",
            "analytics_accept_filetype": "analytics-accept-filetype",
            "analytics_wl_filetype": "analytics-wl-filetype",
            "analytics_bl_filetype": "analytics-bl-filetype",
            "analytics_db": "analytics-db",
            "feature_set": "feature-set",
            "fortindr_error_action": "fortindr-error-action",
            "fortindr_timeout_action": "fortindr-timeout-action",
            "fortisandbox_mode": "fortisandbox-mode",
            "fortisandbox_max_upload": "fortisandbox-max-upload",
            "fortisandbox_error_action": "fortisandbox-error-action",
            "fortisandbox_timeout_action": "fortisandbox-timeout-action",
            "outbreak_prevention_mode": "outbreak-prevention-mode",
            "outbreak_prevention_archive_scan": "outbreak-prevention-archive-scan",
            "external_blocklist_enable_all": "external-blocklist-enable-all",
            "external_blocklist_archive_scan": "external-blocklist-archive-scan",
            "ems_threat_feed": "ems-threat-feed",
        }

        # Add non-None parameters
        for param_name, value in param_map.items():
            if value is not None:
                api_name = api_field_map[param_name]
                payload_dict[api_name] = value

        # Add any extra kwargs (protocol settings like http, ftp, etc.)
        payload_dict.update(kwargs)

        return self._client.post(
            "cmdb", "antivirus/profile", payload_dict, vdom=vdom, raw_json=raw_json
        )

    def put(
        self,
        payload_dict: Optional[Dict[str, Any]] = None,
        name: Optional[str] = None,
        comment: Optional[str] = None,
        replacemsg_group: Optional[str] = None,
        scan_mode: Optional[str] = None,
        mobile_malware_db: Optional[str] = None,
        analytics_max_upload: Optional[int] = None,
        analytics_ignore_filetype: Optional[int] = None,
        analytics_accept_filetype: Optional[int] = None,
        analytics_wl_filetype: Optional[int] = None,
        analytics_bl_filetype: Optional[int] = None,
        analytics_db: Optional[str] = None,
        feature_set: Optional[str] = None,
        fortindr_error_action: Optional[str] = None,
        fortindr_timeout_action: Optional[str] = None,
        fortisandbox_mode: Optional[str] = None,
        fortisandbox_max_upload: Optional[int] = None,
        fortisandbox_error_action: Optional[str] = None,
        fortisandbox_timeout_action: Optional[str] = None,
        outbreak_prevention_mode: Optional[str] = None,
        outbreak_prevention_archive_scan: Optional[str] = None,
        external_blocklist_enable_all: Optional[str] = None,
        external_blocklist_archive_scan: Optional[str] = None,
        ems_threat_feed: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        # Query parameters for actions
        action: Optional[str] = None,
        before: Optional[str] = None,
        after: Optional[str] = None,
        scope: Optional[str] = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        PUT /antivirus/profile/{name}
        Update antivirus profile

        Args:
            name: Profile name (required)
            comment: Comment (max 255 chars)
            replacemsg_group: Replacement message group
            scan_mode: Scan mode - 'quick', 'full', 'legacy', 'default'
            mobile_malware_db: Enable/disable mobile malware database - 'disable' or 'enable'
            analytics_max_upload: Maximum size of files uploaded to FortiSandbox (1-395 MB)
            analytics_ignore_filetype: File types to ignore for FortiSandbox inspection
            analytics_accept_filetype: File types to submit for FortiSandbox inspection
            analytics_wl_filetype: Whitelist file types
            analytics_bl_filetype: Blacklist file types
            analytics_db: Enable/disable using FortiSandbox signature database - 'disable' or 'enable'
            feature_set: Flow/proxy feature set - 'flow' or 'proxy'
            fortindr_error_action: Action on FortiNDR error - 'pass' or 'block'
            fortindr_timeout_action: Action on FortiNDR timeout - 'pass' or 'block'
            fortisandbox_mode: FortiSandbox inline mode - 'inline' or 'analytics-suspicious'
            fortisandbox_max_upload: Maximum size for FortiSandbox upload (1-395 MB)
            fortisandbox_error_action: Action on FortiSandbox error - 'pass' or 'block'
            fortisandbox_timeout_action: Action on FortiSandbox timeout - 'pass' or 'block'
            outbreak_prevention_mode: Outbreak prevention mode - 'disabled', 'files', 'full-archive', 'pass', 'block'
            outbreak_prevention_archive_scan: Archive scan setting - 'disable' or 'enable'
            external_blocklist_enable_all: Enable/disable all external blocklists - 'disable' or 'enable'
            external_blocklist_archive_scan: External blocklist archive scan - 'disable' or 'enable'
            ems_threat_feed: Enable/disable EMS threat feed - 'disable' or 'enable'
            vdom: Virtual domain (optional)

            Action parameters (optional):
            action: Action to perform - 'move' to reorder entries
            before: If action=move, move before this entry ID
            after: If action=move, move after this entry ID
            scope: Scope (vdom)
            **kwargs: Any additional parameters (http, ftp, imap, pop3, smtp, mapi, nntp, cifs, ssh)

        Returns:
            Response dict with status

        Examples:
            >>> # PUT - Update scan mode
            >>> fgt.cmdb.antivirus.profile.update(
            ...     name='default',
            ...     scan_mode='full'
            ... )

            >>> # PUT - Update FortiSandbox settings
            >>> fgt.cmdb.antivirus.profile.update(
            ...     name='corporate_av',
            ...     fortisandbox_mode='inline',
            ...     fortisandbox_error_action='block',
            ...     comment='Updated FortiSandbox settings'
            ... )

            >>> # Enable outbreak prevention
            >>> fgt.cmdb.antivirus.profile.update(
            ...     name='strict_av',
            ...     outbreak_prevention_mode='full-archive',
            ...     outbreak_prevention_archive_scan='enable'
            ... )
        """
        # Build data dict from provided parameters
        payload_dict = {}

        # Map data parameters
        data_param_map = {
            "comment": comment,
            "replacemsg_group": replacemsg_group,
            "scan_mode": scan_mode,
            "mobile_malware_db": mobile_malware_db,
            "analytics_max_upload": analytics_max_upload,
            "analytics_ignore_filetype": analytics_ignore_filetype,
            "analytics_accept_filetype": analytics_accept_filetype,
            "analytics_wl_filetype": analytics_wl_filetype,
            "analytics_bl_filetype": analytics_bl_filetype,
            "analytics_db": analytics_db,
            "feature_set": feature_set,
            "fortindr_error_action": fortindr_error_action,
            "fortindr_timeout_action": fortindr_timeout_action,
            "fortisandbox_mode": fortisandbox_mode,
            "fortisandbox_max_upload": fortisandbox_max_upload,
            "fortisandbox_error_action": fortisandbox_error_action,
            "fortisandbox_timeout_action": fortisandbox_timeout_action,
            "outbreak_prevention_mode": outbreak_prevention_mode,
            "outbreak_prevention_archive_scan": outbreak_prevention_archive_scan,
            "external_blocklist_enable_all": external_blocklist_enable_all,
            "external_blocklist_archive_scan": external_blocklist_archive_scan,
            "ems_threat_feed": ems_threat_feed,
        }

        # API field name mapping for data
        api_field_map = {
            "comment": "comment",
            "replacemsg_group": "replacemsg-group",
            "scan_mode": "scan-mode",
            "mobile_malware_db": "mobile-malware-db",
            "analytics_max_upload": "analytics-max-upload",
            "analytics_ignore_filetype": "analytics-ignore-filetype",
            "analytics_accept_filetype": "analytics-accept-filetype",
            "analytics_wl_filetype": "analytics-wl-filetype",
            "analytics_bl_filetype": "analytics-bl-filetype",
            "analytics_db": "analytics-db",
            "feature_set": "feature-set",
            "fortindr_error_action": "fortindr-error-action",
            "fortindr_timeout_action": "fortindr-timeout-action",
            "fortisandbox_mode": "fortisandbox-mode",
            "fortisandbox_max_upload": "fortisandbox-max-upload",
            "fortisandbox_error_action": "fortisandbox-error-action",
            "fortisandbox_timeout_action": "fortisandbox-timeout-action",
            "outbreak_prevention_mode": "outbreak-prevention-mode",
            "outbreak_prevention_archive_scan": "outbreak-prevention-archive-scan",
            "external_blocklist_enable_all": "external-blocklist-enable-all",
            "external_blocklist_archive_scan": "external-blocklist-archive-scan",
            "ems_threat_feed": "ems-threat-feed",
        }

        # Add non-None data parameters
        for param_name, value in data_param_map.items():
            if value is not None:
                api_name = api_field_map[param_name]
                payload_dict[api_name] = value

        # Add any extra data kwargs
        for key, value in kwargs.items():
            if key not in ["action", "before", "after", "scope"]:
                payload_dict[key] = value

        # Build query params dict
        params = {}

        # Map query parameters
        query_param_map = {
            "action": action,
            "before": before,
            "after": after,
            "scope": scope,
        }

        # Add non-None query parameters
        for param_name, value in query_param_map.items():
            if value is not None:
                params[param_name] = value

        return self._client.put(
            "cmdb",
            f"antivirus/profile/{name}",
            payload_dict,
            params=params if params else None,
            vdom=vdom,
            raw_json=raw_json,
        )

    def delete(
        self,
        name: str,
        vdom: Optional[Union[str, bool]] = None,
        # Action parameters
        mkey: Optional[str] = None,
        scope: Optional[str] = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        DELETE /antivirus/profile/{name}
        Delete antivirus profile

        Args:
            name: Profile name (required) - the MKEY identifier
            vdom: Virtual domain (optional)

            Action parameters (optional):
            mkey: Filter matching mkey attribute value (if different from name)
            scope: Scope (vdom)
            **kwargs: Any additional parameters

        Returns:
            Response dict with status

        Examples:
            >>> # Simple delete
            >>> fgt.cmdb.antivirus.profile.delete('old_profile')

            >>> # Delete with specific vdom
            >>> fgt.cmdb.antivirus.profile.delete(
            ...     name='old_profile',
            ...     vdom='root'
            ... )
        """
        # Build params dict
        params = {}

        # Map parameters
        param_map = {
            "mkey": mkey,
            "scope": scope,
        }

        # Add non-None parameters
        for key, value in param_map.items():
            if value is not None:
                params[key] = value

        # Add any extra kwargs
        params.update(kwargs)

        return self._client.delete(
            "cmdb",
            f"antivirus/profile/{name}",
            params=params if params else None,
            vdom=vdom,
            raw_json=raw_json,
        )
