"""
from __future__ import annotations
from typing import TYPE_CHECKING, Any, Optional, Union

if TYPE_CHECKING:
    from ....http_client import HTTPClient

FortiOS CMDB - DLP Profile

Configure DLP profiles.

API Endpoints:
    GET    /dlp/profile       - List all profiles
    GET    /dlp/profile/{name} - Get specific profile
    POST   /dlp/profile       - Create new profile
    PUT    /dlp/profile/{name} - Update profile
    DELETE /dlp/profile/{name} - Delete profile
"""

from __future__ import annotations
from typing import Any


class Profile:
    """DLP profile endpoint"""
    
    def __init__(self, client: 'HTTPClient') -> None:
        self._client = client
    
    def get(
        self,
        name: str | None = None,
        # Query parameters
        attr: str | None = None,
        count: int | None = None,
        skip_to_datasource: dict[str, Any] | None = None,
        acs: int | None = None,
        search: str | None = None,
        scope: str | None = None,
        datasource: bool | None = None,
        with_meta: bool | None = None,
        skip: bool | None = None,
        format: str | None = None,
        action: str | None = None,
        vdom: str | None = None,
        **kwargs
    ) -> dict[str, Any]:
        """
        Get DLP profile(s).
        
        Args:
            name: Name of specific profile to retrieve
            attr: Attribute name that references other table
            count: Maximum number of entries to return
            skip_to_datasource: Skip to provided table's Nth entry
            acs: If true, returned results are in ascending order
            search: Filter objects by search value
            scope: Scope - 'global', 'vdom', or 'both'
            datasource: Include datasource information for each linked object
            with_meta: Include meta information (type id, references, etc)
            skip: Enable CLI skip operator to hide skipped properties
            format: List of property names to include (pipe-separated)
            action: Special actions - 'default', 'schema', 'revision'
            vdom: Virtual Domain(s). Use 'root' for single VDOM, or '*' for all
            **kwargs: Additional query parameters
        
        Returns:
            API response dictionary with profile configuration(s)
        
        Examples:
            >>> # Get all profiles
            >>> result = fgt.cmdb.dlp.profile.get()
            >>> print(f"Total profiles: {len(result['results'])}")
            
            >>> # Get specific profile
            >>> result = fgt.cmdb.dlp.profile.get('email-dlp')
            >>> print(f"Feature set: {result['results']['feature-set']}")
        """
        # Build path
        path = 'dlp/profile'
        if name:
            path = f'dlp/profile/{name}'
        
        # Build query parameters
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
        
        return self._client.get('cmdb', path, params=params if params else None, vdom=vdom)
    
    def list(
        self,
        vdom: str | None = None,
        **kwargs
    ) -> dict[str, Any]:
        """
        List all DLP profiles (convenience method).
        
        Args:
            vdom: Virtual Domain(s)
            **kwargs: Additional query parameters
        
        Returns:
            API response dictionary with all profiles
        
        Examples:
            >>> # List all profiles
            >>> result = fgt.cmdb.dlp.profile.list()
            >>> for prof in result['results']:
            ...     print(f"{prof['name']}: {prof.get('comment', 'N/A')}")
        """
        return self.get(vdom=vdom, **kwargs)
    
    def create(
        self,
        name: str,
        # Profile configuration
        comment: str | None = None,
        feature_set: str | None = None,
        replacemsg_group: str | None = None,
        rule: list[dict[str, Any]] | None = None,
        dlp_log: str | None = None,
        extended_log: str | None = None,
        nac_quar_log: str | None = None,
        full_archive_proto: str | None = None,
        summary_proto: str | None = None,
        fortidata_error_action: str | None = None,
        vdom: str | None = None,
        **kwargs
    ) -> dict[str, Any]:
        """
        Create a new DLP profile.
        
        Args:
            name: Name of the DLP profile (max 47 chars)
            comment: Comment (max 255 chars)
            feature_set: Flow/proxy feature set - 'flow' or 'proxy'
            replacemsg_group: Replacement message group name (max 35 chars)
            rule: List of DLP rules. Each rule is a dict with:
                - id (int): Rule ID
                - name (str): Filter name (max 35 chars)
                - severity (str): Severity - 'info', 'low', 'medium', 'high', 'critical'
                - type (str): Rule type - 'file' or 'message'
                - proto (str): Protocol - 'smtp', 'pop3', 'imap', 'http-get', 'http-post', 'ftp', 'nntp', 'mapi', 'ssh', 'cifs'
                - filter_by (str): Filter by - 'sensor', 'label', 'encrypted', 'none'
                - file_size (int): Match files >= this size in KB (0-197632)
                - file_type (int): DLP file pattern table number
                - sensor (list): List of DLP sensors (list of dicts with 'name')
                - label (str): DLP label name (max 35 chars)
                - archive (str): Enable archiving - 'enable' or 'disable'
                - action (str): Action - 'allow', 'log-only', 'block', 'quarantine-ip'
                - expiry (str): Quarantine duration format dddhhmm
            dlp_log: Enable DLP logging - 'enable' or 'disable'
            extended_log: Enable extended logging - 'enable' or 'disable'
            nac_quar_log: Enable NAC quarantine logging - 'enable' or 'disable'
            full_archive_proto: Protocols to always content archive (same as proto)
            summary_proto: Protocols to always log summary (same as proto)
            fortidata_error_action: Action if FortiData query fails - 'log-only', 'block', 'ignore'
            vdom: Virtual Domain(s)
            **kwargs: Additional data parameters
        
        Returns:
            API response dictionary
        
        Examples:
            >>> # Create simple DLP profile
            >>> result = fgt.cmdb.dlp.profile.create(
            ...     name='email-protection',
            ...     comment='DLP for email',
            ...     feature_set='proxy',
            ...     dlp_log='enable'
            ... )
            
            >>> # Create profile with rules
            >>> result = fgt.cmdb.dlp.profile.create(
            ...     name='file-dlp',
            ...     comment='Block sensitive files',
            ...     feature_set='proxy',
            ...     rule=[
            ...         {
            ...             'id': 1,
            ...             'name': 'Block SSN',
            ...             'severity': 'high',
            ...             'type': 'file',
            ...             'proto': 'http-post',
            ...             'filter_by': 'sensor',
            ...             'sensor': [{'name': 'ssn-sensor'}],
            ...             'action': 'block'
            ...         }
            ...     ],
            ...     dlp_log='enable'
            ... )
        """
        data = {}
        param_map = {
            'name': name,
            'comment': comment,
            'feature_set': feature_set,
            'replacemsg_group': replacemsg_group,
            'rule': rule,
            'dlp_log': dlp_log,
            'extended_log': extended_log,
            'nac_quar_log': nac_quar_log,
            'full_archive_proto': full_archive_proto,
            'summary_proto': summary_proto,
            'fortidata_error_action': fortidata_error_action,
        }
        
        # Map to API field names
        api_field_map = {
            'name': 'name',
            'comment': 'comment',
            'feature_set': 'feature-set',
            'replacemsg_group': 'replacemsg-group',
            'rule': 'rule',
            'dlp_log': 'dlp-log',
            'extended_log': 'extended-log',
            'nac_quar_log': 'nac-quar-log',
            'full_archive_proto': 'full-archive-proto',
            'summary_proto': 'summary-proto',
            'fortidata_error_action': 'fortidata-error-action',
        }
        
        for param_name, value in param_map.items():
            if value is not None:
                api_name = api_field_map[param_name]
                # Handle rule list - convert snake_case keys to hyphen-case
                if param_name == 'rule' and isinstance(value, list):
                    converted_rules = []
                    for rule_item in value:
                        converted_rule = {}
                        for k, v in rule_item.items():
                            # Convert snake_case to hyphen-case
                            api_key = k.replace('_', '-')
                            converted_rule[api_key] = v
                        converted_rules.append(converted_rule)
                    data[api_name] = converted_rules
                else:
                    data[api_name] = value
        
        data.update(kwargs)
        
        return self._client.post('cmdb', 'dlp/profile', data, vdom=vdom)
    
    def update(
        self,
        name: str,
        # Profile configuration
        comment: str | None = None,
        feature_set: str | None = None,
        replacemsg_group: str | None = None,
        rule: list[dict[str, Any]] | None = None,
        dlp_log: str | None = None,
        extended_log: str | None = None,
        nac_quar_log: str | None = None,
        full_archive_proto: str | None = None,
        summary_proto: str | None = None,
        fortidata_error_action: str | None = None,
        vdom: str | None = None,
        **kwargs
    ) -> dict[str, Any]:
        """
        Update an existing DLP profile.
        
        Args:
            name: Name of the DLP profile to update
            comment: Comment (max 255 chars)
            feature_set: Flow/proxy feature set - 'flow' or 'proxy'
            replacemsg_group: Replacement message group name (max 35 chars)
            rule: List of DLP rules (see create() for structure)
            dlp_log: Enable DLP logging - 'enable' or 'disable'
            extended_log: Enable extended logging - 'enable' or 'disable'
            nac_quar_log: Enable NAC quarantine logging - 'enable' or 'disable'
            full_archive_proto: Protocols to always content archive
            summary_proto: Protocols to always log summary
            fortidata_error_action: Action if FortiData query fails - 'log-only', 'block', 'ignore'
            vdom: Virtual Domain(s)
            **kwargs: Additional data parameters
        
        Returns:
            API response dictionary
        
        Examples:
            >>> # Update comment
            >>> result = fgt.cmdb.dlp.profile.update(
            ...     name='email-protection',
            ...     comment='Updated email DLP'
            ... )
            
            >>> # Add a rule
            >>> result = fgt.cmdb.dlp.profile.update(
            ...     name='email-protection',
            ...     rule=[
            ...         {
            ...             'id': 1,
            ...             'name': 'Block Credit Cards',
            ...             'severity': 'critical',
            ...             'type': 'message',
            ...             'proto': 'smtp',
            ...             'filter_by': 'sensor',
            ...             'sensor': [{'name': 'cc-sensor'}],
            ...             'action': 'block'
            ...         }
            ...     ]
            ... )
        """
        data = {}
        param_map = {
            'comment': comment,
            'feature_set': feature_set,
            'replacemsg_group': replacemsg_group,
            'rule': rule,
            'dlp_log': dlp_log,
            'extended_log': extended_log,
            'nac_quar_log': nac_quar_log,
            'full_archive_proto': full_archive_proto,
            'summary_proto': summary_proto,
            'fortidata_error_action': fortidata_error_action,
        }
        
        # Map to API field names
        api_field_map = {
            'comment': 'comment',
            'feature_set': 'feature-set',
            'replacemsg_group': 'replacemsg-group',
            'rule': 'rule',
            'dlp_log': 'dlp-log',
            'extended_log': 'extended-log',
            'nac_quar_log': 'nac-quar-log',
            'full_archive_proto': 'full-archive-proto',
            'summary_proto': 'summary-proto',
            'fortidata_error_action': 'fortidata-error-action',
        }
        
        for param_name, value in param_map.items():
            if value is not None:
                api_name = api_field_map[param_name]
                # Handle rule list - convert snake_case keys to hyphen-case
                if param_name == 'rule' and isinstance(value, list):
                    converted_rules = []
                    for rule_item in value:
                        converted_rule = {}
                        for k, v in rule_item.items():
                            # Convert snake_case to hyphen-case
                            api_key = k.replace('_', '-')
                            converted_rule[api_key] = v
                        converted_rules.append(converted_rule)
                    data[api_name] = converted_rules
                else:
                    data[api_name] = value
        
        data.update(kwargs)
        
        return self._client.put('cmdb', f'dlp/profile/{name}', data, vdom=vdom)
    
    def delete(
        self,
        name: str,
        vdom: str | None = None
    ) -> dict[str, Any]:
        """
        Delete a DLP profile.
        
        Args:
            name: Name of the profile to delete
            vdom: Virtual Domain(s)
        
        Returns:
            API response dictionary
        
        Examples:
            >>> # Delete a profile
            >>> result = fgt.cmdb.dlp.profile.delete('email-protection')
            >>> print(f"Status: {result['status']}")
        """
        return self._client.delete('cmdb', f'dlp/profile/{name}', vdom=vdom)
