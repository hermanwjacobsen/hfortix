"""FortiOS CMDB DNS Filter Profile API module.

This module provides methods for managing DNS filter profiles.
"""

from typing import Any, Optional


class Profile:
    """Manage DNS filter profile objects.
    
    This class provides methods to create, read, update, and delete DNS filter profiles
    that configure DNS filtering policies.
    """
    
    def __init__(self, client: Any) -> None:
        """Initialize Profile API module.
        
        Args:
            client: The FortiOS API client instance.
        """
        self._client = client
    
    def get(
        self,
        name: Optional[str] = None,
        vdom: Optional[str] = None,
        **kwargs: Any
    ) -> dict[str, Any]:
        """Retrieve DNS filter profile configuration.
        
        Args:
            name (str, optional): Profile name. If provided, retrieves specific profile.
                If not provided, retrieves all profiles.
            vdom (str, optional): Virtual domain name. Defaults to 'root' if not specified.
            **kwargs: Additional parameters to pass to the API:
                - datasource (bool): Include datasource information
                - with_meta (bool): Include meta information
                - skip (bool): Enable skip operator
                - format (list): List of property names to include
                - filter (str): Filter expression
                - count (int): Maximum number of entries to return
                - start (int): Starting entry index
        
        Returns:
            dict: API response containing DNS filter profile configuration.
        
        Example:
            >>> # Get all profiles
            >>> profiles = client.cmdb.dnsfilter.profile.list()
            
            >>> # Get specific profile
            >>> profile = client.cmdb.dnsfilter.profile.get(name='default')
        """
        if name is not None:
            path = f'dnsfilter/profile/{name}'
        else:
            path = 'dnsfilter/profile'
        
        params = {}
        if kwargs:
            params.update(kwargs)
        
        return self._client.get('cmdb', path, params=params if params else None, vdom=vdom)
    
    def list(self, vdom: Optional[str] = None, **kwargs: Any) -> dict[str, Any]:
        """List all DNS filter profiles.
        
        Convenience method that calls get() without a name.
        
        Args:
            vdom (str, optional): Virtual domain name.
            **kwargs: Additional query parameters.
        
        Returns:
            dict: API response containing list of all profiles.
        
        Example:
            >>> profiles = client.cmdb.dnsfilter.profile.list()
            >>> for p in profiles['results']:
            ...     print(p['name'], p.get('comment', ''))
        """
        return self.get(vdom=vdom, **kwargs)
    
    def create(
        self,
        name: str,
        comment: Optional[str] = None,
        domain_filter: Optional[list[dict[str, Any]]] = None,
        ftgd_dns: Optional[list[dict[str, Any]]] = None,
        log_all_domain: Optional[str] = None,
        sdns_ftgd_err_log: Optional[str] = None,
        sdns_domain_log: Optional[str] = None,
        block_action: Optional[str] = None,
        redirect_portal: Optional[str] = None,
        redirect_portal6: Optional[str] = None,
        block_botnet: Optional[str] = None,
        safe_search: Optional[str] = None,
        youtube_restrict: Optional[str] = None,
        external_ip_blocklist: Optional[list[dict[str, Any]]] = None,
        dns_translation: Optional[list[dict[str, Any]]] = None,
        transparent_dns_database: Optional[list[dict[str, Any]]] = None,
        strip_ech: Optional[str] = None,
        vdom: Optional[str] = None,
        **kwargs: Any
    ) -> dict[str, Any]:
        """Create a new DNS filter profile.
        
        Args:
            name (str): Profile name (max 47 chars, required).
            comment (str, optional): Comment (max 255 chars).
            domain_filter (list, optional): List of domain filter settings. Each is a dict with:
                - domain_filter_table (int): DNS domain filter table ID
            ftgd_dns (list, optional): FortiGuard DNS Filter settings. Each is a dict with:
                - options (str): 'error-allow' or 'ftgd-disable'
                - filters (list): List of FortiGuard DNS domain filters with:
                    - id (int): ID number (0-255)
                    - category (int): Category number (0-255)
                    - action (str): 'block' or 'monitor'
                    - log (str): 'enable' or 'disable'
            log_all_domain (str, optional): Enable/disable logging all domains - 'enable' or 'disable'.
            sdns_ftgd_err_log (str, optional): Enable/disable FortiGuard SDNS rating error logging.
            sdns_domain_log (str, optional): Enable/disable domain filtering and botnet domain logging.
            block_action (str, optional): Action for blocked domains - 'block', 'redirect', 'block-sevrfail'.
            redirect_portal (str, optional): IPv4 address of SDNS redirect portal.
            redirect_portal6 (str, optional): IPv6 address of SDNS redirect portal.
            block_botnet (str, optional): Enable/disable blocking botnet C&C DNS lookups.
            safe_search (str, optional): Enable/disable Google, Bing, YouTube safe search.
            youtube_restrict (str, optional): YouTube restriction level - 'strict', 'moderate', 'none'.
            external_ip_blocklist (list, optional): External IP block lists. Each is a dict with:
                - name (str): External domain block list name
            dns_translation (list, optional): DNS translation settings. Each is a dict with:
                - id (int): ID
                - addr_type (str): 'ipv4' or 'ipv6'
                - src (str): IPv4 source address/subnet
                - dst (str): IPv4 destination address/subnet
                - netmask (str): Netmask for src and dst
                - status (str): 'enable' or 'disable'
                - src6 (str): IPv6 source address/subnet
                - dst6 (str): IPv6 destination address/subnet
                - prefix (int): Prefix for src6/dst6 (1-128)
            transparent_dns_database (list, optional): Transparent DNS database zones. Each is a dict with:
                - name (str): DNS database zone name
            strip_ech (str, optional): Enable/disable removal of encrypted client hello parameter.
            vdom (str, optional): Virtual domain name.
            **kwargs: Additional parameters.
        
        Returns:
            dict: API response containing operation results.
        
        Example:
            >>> # Create profile with domain filter
            >>> client.cmdb.dnsfilter.profile.create(
            ...     name='corporate-filter',
            ...     comment='Corporate DNS filtering policy',
            ...     domain_filter=[
            ...         {'domain_filter_table': 10}
            ...     ],
            ...     block_action='redirect',
            ...     safe_search='enable'
            ... )
        """
        data = {'name': name}
        
        param_map = {
            'comment': comment,
            'domain_filter': domain_filter,
            'ftgd_dns': ftgd_dns,
            'log_all_domain': log_all_domain,
            'sdns_ftgd_err_log': sdns_ftgd_err_log,
            'sdns_domain_log': sdns_domain_log,
            'block_action': block_action,
            'redirect_portal': redirect_portal,
            'redirect_portal6': redirect_portal6,
            'block_botnet': block_botnet,
            'safe_search': safe_search,
            'youtube_restrict': youtube_restrict,
            'external_ip_blocklist': external_ip_blocklist,
            'dns_translation': dns_translation,
            'transparent_dns_database': transparent_dns_database,
            'strip_ech': strip_ech
        }
        
        api_field_map = {
            'comment': 'comment',
            'domain_filter': 'domain-filter',
            'ftgd_dns': 'ftgd-dns',
            'log_all_domain': 'log-all-domain',
            'sdns_ftgd_err_log': 'sdns-ftgd-err-log',
            'sdns_domain_log': 'sdns-domain-log',
            'block_action': 'block-action',
            'redirect_portal': 'redirect-portal',
            'redirect_portal6': 'redirect-portal6',
            'block_botnet': 'block-botnet',
            'safe_search': 'safe-search',
            'youtube_restrict': 'youtube-restrict',
            'external_ip_blocklist': 'external-ip-blocklist',
            'dns_translation': 'dns-translation',
            'transparent_dns_database': 'transparent-dns-database',
            'strip_ech': 'strip-ech'
        }
        
        for param_name, value in param_map.items():
            if value is not None:
                api_name = api_field_map[param_name]
                # Handle nested objects with snake_case conversion
                if isinstance(value, list):
                    converted_list = []
                    for item in value:
                        if isinstance(item, dict):
                            converted_item = {}
                            for k, v in item.items():
                                # Convert snake_case to hyphen-case
                                api_key = k.replace('_', '-')
                                converted_item[api_key] = v
                            converted_list.append(converted_item)
                        else:
                            converted_list.append(item)
                    data[api_name] = converted_list
                else:
                    data[api_name] = value
        
        if kwargs:
            data.update(kwargs)
        
        return self._client.post('cmdb', 'dnsfilter/profile', data, vdom=vdom)
    
    def update(
        self,
        name: str,
        comment: Optional[str] = None,
        domain_filter: Optional[list[dict[str, Any]]] = None,
        ftgd_dns: Optional[list[dict[str, Any]]] = None,
        log_all_domain: Optional[str] = None,
        sdns_ftgd_err_log: Optional[str] = None,
        sdns_domain_log: Optional[str] = None,
        block_action: Optional[str] = None,
        redirect_portal: Optional[str] = None,
        redirect_portal6: Optional[str] = None,
        block_botnet: Optional[str] = None,
        safe_search: Optional[str] = None,
        youtube_restrict: Optional[str] = None,
        external_ip_blocklist: Optional[list[dict[str, Any]]] = None,
        dns_translation: Optional[list[dict[str, Any]]] = None,
        transparent_dns_database: Optional[list[dict[str, Any]]] = None,
        strip_ech: Optional[str] = None,
        vdom: Optional[str] = None,
        **kwargs: Any
    ) -> dict[str, Any]:
        """Update an existing DNS filter profile.
        
        Args:
            name (str): Profile name to update.
            comment (str, optional): Updated comment.
            domain_filter (list, optional): Updated domain filter settings.
            ftgd_dns (list, optional): Updated FortiGuard DNS Filter settings.
            log_all_domain (str, optional): Updated logging setting.
            sdns_ftgd_err_log (str, optional): Updated SDNS error logging.
            sdns_domain_log (str, optional): Updated domain logging.
            block_action (str, optional): Updated block action.
            redirect_portal (str, optional): Updated IPv4 redirect portal.
            redirect_portal6 (str, optional): Updated IPv6 redirect portal.
            block_botnet (str, optional): Updated botnet blocking.
            safe_search (str, optional): Updated safe search.
            youtube_restrict (str, optional): Updated YouTube restriction.
            external_ip_blocklist (list, optional): Updated external IP blocklists.
            dns_translation (list, optional): Updated DNS translation settings.
            transparent_dns_database (list, optional): Updated transparent DNS database zones.
            strip_ech (str, optional): Updated ECH stripping setting.
            vdom (str, optional): Virtual domain name.
            **kwargs: Additional parameters.
        
        Returns:
            dict: API response containing operation results.
        
        Example:
            >>> # Update profile to enable safe search
            >>> client.cmdb.dnsfilter.profile.update(
            ...     name='corporate-filter',
            ...     safe_search='enable',
            ...     youtube_restrict='strict'
            ... )
        """
        data = {}
        
        param_map = {
            'comment': comment,
            'domain_filter': domain_filter,
            'ftgd_dns': ftgd_dns,
            'log_all_domain': log_all_domain,
            'sdns_ftgd_err_log': sdns_ftgd_err_log,
            'sdns_domain_log': sdns_domain_log,
            'block_action': block_action,
            'redirect_portal': redirect_portal,
            'redirect_portal6': redirect_portal6,
            'block_botnet': block_botnet,
            'safe_search': safe_search,
            'youtube_restrict': youtube_restrict,
            'external_ip_blocklist': external_ip_blocklist,
            'dns_translation': dns_translation,
            'transparent_dns_database': transparent_dns_database,
            'strip_ech': strip_ech
        }
        
        api_field_map = {
            'comment': 'comment',
            'domain_filter': 'domain-filter',
            'ftgd_dns': 'ftgd-dns',
            'log_all_domain': 'log-all-domain',
            'sdns_ftgd_err_log': 'sdns-ftgd-err-log',
            'sdns_domain_log': 'sdns-domain-log',
            'block_action': 'block-action',
            'redirect_portal': 'redirect-portal',
            'redirect_portal6': 'redirect-portal6',
            'block_botnet': 'block-botnet',
            'safe_search': 'safe-search',
            'youtube_restrict': 'youtube-restrict',
            'external_ip_blocklist': 'external-ip-blocklist',
            'dns_translation': 'dns-translation',
            'transparent_dns_database': 'transparent-dns-database',
            'strip_ech': 'strip-ech'
        }
        
        for param_name, value in param_map.items():
            if value is not None:
                api_name = api_field_map[param_name]
                # Handle nested objects with snake_case conversion
                if isinstance(value, list):
                    converted_list = []
                    for item in value:
                        if isinstance(item, dict):
                            converted_item = {}
                            for k, v in item.items():
                                # Convert snake_case to hyphen-case
                                api_key = k.replace('_', '-')
                                converted_item[api_key] = v
                            converted_list.append(converted_item)
                        else:
                            converted_list.append(item)
                    data[api_name] = converted_list
                else:
                    data[api_name] = value
        
        if kwargs:
            data.update(kwargs)
        
        return self._client.put('cmdb', f'dnsfilter/profile/{name}', data, vdom=vdom)
    
    def delete(self, name: str, vdom: Optional[str] = None) -> dict[str, Any]:
        """Delete a DNS filter profile.
        
        Args:
            name (str): Profile name to delete.
            vdom (str, optional): Virtual domain name.
        
        Returns:
            dict: API response containing operation results.
        
        Example:
            >>> client.cmdb.dnsfilter.profile.delete(name='corporate-filter')
        """
        return self._client.delete('cmdb', f'dnsfilter/profile/{name}', vdom=vdom)
