"""
FortiOS CMDB - Email Filter Profile

Configure Email Filter profiles.

API Endpoints:
    GET    /api/v2/cmdb/emailfilter/profile       - List all email filter profiles
    GET    /api/v2/cmdb/emailfilter/profile/{name} - Get specific email filter profile
    POST   /api/v2/cmdb/emailfilter/profile       - Create email filter profile
    PUT    /api/v2/cmdb/emailfilter/profile/{name} - Update email filter profile
    DELETE /api/v2/cmdb/emailfilter/profile/{name} - Delete email filter profile
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional, Union

if TYPE_CHECKING:
    from ....http_client import HTTPClient


class Profile:
    """Email filter profile endpoint"""

    def __init__(self, client: 'HTTPClient') -> None:
        """
        Initialize Profile endpoint.

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
        Get email filter profile(s).

        Args:
            name (str, optional): Profile name to retrieve. If None, retrieves all profiles
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
            dict: API response containing email filter profile data

        Examples:
            >>> # List all email filter profiles
            >>> profiles = fgt.cmdb.emailfilter.profile.list()

            >>> # Get a specific profile by name
            >>> profile = fgt.cmdb.emailfilter.profile.get('default')

            >>> # Get with filtering
            >>> profiles = fgt.cmdb.emailfilter.profile.get(
            ...     format='name|comment|spam-log',
            ...     count=10
            ... )
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

        path = 'emailfilter/profile'
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
        Get all email filter profiles (convenience method).

        Args:
            Same as get() method, excluding name

        Returns:
            dict: API response containing all email filter profiles

        Examples:
            >>> profiles = fgt.cmdb.emailfilter.profile.list()
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
        name: str,
        # Profile configuration
        comment: Optional[str] = None,
        feature_set: Optional[str] = None,
        replacemsg_group: Optional[str] = None,
        spam_log: Optional[str] = None,
        spam_log_fortiguard_response: Optional[str] = None,
        file_filter: Optional[dict[str, Any]] = None,
        spam_filtering: Optional[str] = None,
        external: Optional[str] = None,
        options: Optional[list[str]] = None,
        imap: Optional[dict[str, Any]] = None,
        pop3: Optional[dict[str, Any]] = None,
        smtp: Optional[dict[str, Any]] = None,
        mapi: Optional[dict[str, Any]] = None,
        msn_hotmail: Optional[dict[str, Any]] = None,
        yahoo_mail: Optional[dict[str, Any]] = None,
        gmail: Optional[dict[str, Any]] = None,
        other_webmails: Optional[dict[str, Any]] = None,
        spam_bword_threshold: Optional[int] = None,
        spam_bword_table: Optional[int] = None,
        spam_bal_table: Optional[int] = None,
        spam_bwl_table: Optional[int] = None,
        spam_mheader_table: Optional[int] = None,
        spam_rbl_table: Optional[int] = None,
        spam_iptrust_table: Optional[int] = None,
        vdom: Optional[Union[str, bool]] = None,
        **kwargs: Any
    ) -> dict[str, Any]:
        """
        Create a new email filter profile.

        Args:
            name (str): Profile name
            comment (str, optional): Optional comment
            feature_set (str, optional): Flow/proxy mode feature set - 'flow' or 'proxy'
            replacemsg_group (str, optional): Replacement message group
            spam_log (str, optional): Enable/disable spam logging - 'enable'/'disable'
            spam_log_fortiguard_response (str, optional): Enable/disable FortiGuard response logging
            file_filter (dict, optional): File filter settings with status, log, scan_archive_contents
            spam_filtering (str, optional): Enable/disable spam filtering - 'enable'/'disable'
            external (str, optional): Enable/disable external Email inspection - 'enable'/'disable'
            options (list, optional): Options list - 'bannedword', 'spambwl', 'spamfsip', etc.
            imap (dict, optional): IMAP protocol options with log, action, tag_type, tag_msg
            pop3 (dict, optional): POP3 protocol options
            smtp (dict, optional): SMTP protocol options
            mapi (dict, optional): MAPI protocol options
            msn_hotmail (dict, optional): MSN Hotmail options
            yahoo_mail (dict, optional): Yahoo Mail options
            gmail (dict, optional): Gmail options
            other_webmails (dict, optional): Other webmail options
            spam_bword_threshold (int, optional): Spam banned word threshold
            spam_bword_table (int, optional): Spam banned word table ID
            spam_bal_table (int, optional): Spam block/allow list table ID
            spam_bwl_table (int, optional): Spam black/white list table ID
            spam_mheader_table (int, optional): Spam MIME header table ID
            spam_rbl_table (int, optional): Spam RBL table ID
            spam_iptrust_table (int, optional): Spam IP trust table ID
            vdom (str, optional): Virtual Domain name
            **kwargs: Additional parameters

        Returns:
            dict: API response

        Examples:
            >>> # Create basic email filter profile
            >>> result = fgt.cmdb.emailfilter.profile.create(
            ...     name='corporate-email',
            ...     comment='Corporate email filtering',
            ...     spam_filtering='enable',
            ...     spam_log='enable',
            ...     options=['bannedword', 'spambwl']
            ... )

            >>> # Create with protocol-specific settings
            >>> result = fgt.cmdb.emailfilter.profile.create(
            ...     name='strict-filter',
            ...     spam_filtering='enable',
            ...     smtp={'log': 'enable', 'action': 'tag', 'tag_type': 'subject'},
            ...     imap={'log': 'enable', 'action': 'discard'}
            ... )
        """
        data = {'name': name}
        
        param_map = {
            'comment': comment,
            'feature_set': feature_set,
            'replacemsg_group': replacemsg_group,
            'spam_log': spam_log,
            'spam_log_fortiguard_response': spam_log_fortiguard_response,
            'spam_filtering': spam_filtering,
            'external': external,
            'spam_bword_threshold': spam_bword_threshold,
            'spam_bword_table': spam_bword_table,
            'spam_bal_table': spam_bal_table,
            'spam_bwl_table': spam_bwl_table,
            'spam_mheader_table': spam_mheader_table,
            'spam_rbl_table': spam_rbl_table,
            'spam_iptrust_table': spam_iptrust_table,
        }

        for key, value in param_map.items():
            if value is not None:
                data[key.replace('_', '-')] = value

        # Handle options list
        if options is not None:
            data['options'] = options

        # Handle nested dictionaries
        for dict_param in ['file_filter', 'imap', 'pop3', 'smtp', 'mapi', 
                          'msn_hotmail', 'yahoo_mail', 'gmail', 'other_webmails']:
            value = locals()[dict_param]
            if value is not None:
                converted = {}
                for k, v in value.items():
                    converted[k.replace('_', '-')] = v
                data[dict_param.replace('_', '-')] = converted

        data.update(kwargs)

        return self._client.post('cmdb', 'emailfilter/profile', data=data, vdom=vdom)

    def update(
        self,
        name: str,
        # Profile configuration
        comment: Optional[str] = None,
        feature_set: Optional[str] = None,
        replacemsg_group: Optional[str] = None,
        spam_log: Optional[str] = None,
        spam_log_fortiguard_response: Optional[str] = None,
        file_filter: Optional[dict[str, Any]] = None,
        spam_filtering: Optional[str] = None,
        external: Optional[str] = None,
        options: Optional[list[str]] = None,
        imap: Optional[dict[str, Any]] = None,
        pop3: Optional[dict[str, Any]] = None,
        smtp: Optional[dict[str, Any]] = None,
        mapi: Optional[dict[str, Any]] = None,
        msn_hotmail: Optional[dict[str, Any]] = None,
        yahoo_mail: Optional[dict[str, Any]] = None,
        gmail: Optional[dict[str, Any]] = None,
        other_webmails: Optional[dict[str, Any]] = None,
        spam_bword_threshold: Optional[int] = None,
        spam_bword_table: Optional[int] = None,
        spam_bal_table: Optional[int] = None,
        spam_bwl_table: Optional[int] = None,
        spam_mheader_table: Optional[int] = None,
        spam_rbl_table: Optional[int] = None,
        spam_iptrust_table: Optional[int] = None,
        # Update parameters
        action: Optional[str] = None,
        before: Optional[str] = None,
        after: Optional[str] = None,
        scope: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        **kwargs: Any
    ) -> dict[str, Any]:
        """
        Update an email filter profile.

        Args:
            name (str): Profile name to update
            comment (str, optional): Optional comment
            feature_set (str, optional): Flow/proxy mode feature set
            replacemsg_group (str, optional): Replacement message group
            spam_log (str, optional): Enable/disable spam logging
            spam_log_fortiguard_response (str, optional): Enable/disable FortiGuard response logging
            file_filter (dict, optional): File filter settings
            spam_filtering (str, optional): Enable/disable spam filtering
            external (str, optional): Enable/disable external Email inspection
            options (list, optional): Options list
            imap (dict, optional): IMAP protocol options
            pop3 (dict, optional): POP3 protocol options
            smtp (dict, optional): SMTP protocol options
            mapi (dict, optional): MAPI protocol options
            msn_hotmail (dict, optional): MSN Hotmail options
            yahoo_mail (dict, optional): Yahoo Mail options
            gmail (dict, optional): Gmail options
            other_webmails (dict, optional): Other webmail options
            spam_bword_threshold (int, optional): Spam banned word threshold
            spam_bword_table (int, optional): Spam banned word table ID
            spam_bal_table (int, optional): Spam block/allow list table ID
            spam_bwl_table (int, optional): Spam black/white list table ID
            spam_mheader_table (int, optional): Spam MIME header table ID
            spam_rbl_table (int, optional): Spam RBL table ID
            spam_iptrust_table (int, optional): Spam IP trust table ID
            action (str, optional): 'add-members', 'replace-members', 'remove-members'
            before (str, optional): Place new object before given object
            after (str, optional): Place new object after given object
            scope (str, optional): Scope level - 'global' or 'vdom'
            vdom (str, optional): Virtual Domain name
            **kwargs: Additional parameters

        Returns:
            dict: API response

        Examples:
            >>> # Update spam filtering settings
            >>> result = fgt.cmdb.emailfilter.profile.update(
            ...     name='corporate-email',
            ...     spam_log='enable',
            ...     spam_bword_threshold=10
            ... )

            >>> # Update SMTP settings
            >>> result = fgt.cmdb.emailfilter.profile.update(
            ...     name='strict-filter',
            ...     smtp={'log': 'enable', 'action': 'discard'}
            ... )
        """
        data = {}
        
        param_map = {
            'comment': comment,
            'feature_set': feature_set,
            'replacemsg_group': replacemsg_group,
            'spam_log': spam_log,
            'spam_log_fortiguard_response': spam_log_fortiguard_response,
            'spam_filtering': spam_filtering,
            'external': external,
            'spam_bword_threshold': spam_bword_threshold,
            'spam_bword_table': spam_bword_table,
            'spam_bal_table': spam_bal_table,
            'spam_bwl_table': spam_bwl_table,
            'spam_mheader_table': spam_mheader_table,
            'spam_rbl_table': spam_rbl_table,
            'spam_iptrust_table': spam_iptrust_table,
            'action': action,
            'before': before,
            'after': after,
            'scope': scope,
        }

        for key, value in param_map.items():
            if value is not None:
                data[key.replace('_', '-')] = value

        # Handle options list
        if options is not None:
            data['options'] = options

        # Handle nested dictionaries
        for dict_param in ['file_filter', 'imap', 'pop3', 'smtp', 'mapi', 
                          'msn_hotmail', 'yahoo_mail', 'gmail', 'other_webmails']:
            value = locals()[dict_param]
            if value is not None:
                converted = {}
                for k, v in value.items():
                    converted[k.replace('_', '-')] = v
                data[dict_param.replace('_', '-')] = converted

        data.update(kwargs)

        return self._client.put('cmdb', f'emailfilter/profile/{name}', data=data, vdom=vdom)

    def delete(
        self,
        name: str,
        scope: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None
    ) -> dict[str, Any]:
        """
        Delete an email filter profile.

        Args:
            name (str): Profile name to delete
            scope (str, optional): Scope level - 'global' or 'vdom'
            vdom (str, optional): Virtual Domain name

        Returns:
            dict: API response

        Examples:
            >>> result = fgt.cmdb.emailfilter.profile.delete('corporate-email')
        """
        params = {}
        if scope is not None:
            params['scope'] = scope

        return self._client.delete('cmdb', f'emailfilter/profile/{name}', 
                                   params=params if params else None, vdom=vdom)
