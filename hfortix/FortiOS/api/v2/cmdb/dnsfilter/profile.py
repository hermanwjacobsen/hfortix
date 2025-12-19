"""
FortiOS CMDB - Dnsfilter Profile

API Endpoints:
    GET    /dnsfilter/profile
    POST   /dnsfilter/profile
    GET    /dnsfilter/profile/{name}
    PUT    /dnsfilter/profile/{name}
    DELETE /dnsfilter/profile/{name}
"""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from ....http_client import HTTPClient


class Profile:
    """Profile operations."""

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
            endpoint = f"/dnsfilter/profile/{name}"
        else:
            endpoint = "/dnsfilter/profile"
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
        domain_filter: list | None = None,
        ftgd_dns: list | None = None,
        log_all_domain: str | None = None,
        sdns_ftgd_err_log: str | None = None,
        sdns_domain_log: str | None = None,
        block_action: str | None = None,
        redirect_portal: str | None = None,
        redirect_portal6: str | None = None,
        block_botnet: str | None = None,
        safe_search: str | None = None,
        youtube_restrict: str | None = None,
        external_ip_blocklist: list | None = None,
        dns_translation: list | None = None,
        transparent_dns_database: list | None = None,
        strip_ech: str | None = None,
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
            domain_filter: Domain filter settings. (optional)
            ftgd_dns: FortiGuard DNS Filter settings. (optional)
            log_all_domain: Enable/disable logging of all domains visited (detailed DNS logging). (optional)
            sdns_ftgd_err_log: Enable/disable FortiGuard SDNS rating error logging. (optional)
            sdns_domain_log: Enable/disable domain filtering and botnet domain logging. (optional)
            block_action: Action to take for blocked domains. (optional)
            redirect_portal: IPv4 address of the SDNS redirect portal. (optional)
            redirect_portal6: IPv6 address of the SDNS redirect portal. (optional)
            block_botnet: Enable/disable blocking botnet C&C DNS lookups. (optional)
            safe_search: Enable/disable Google, Bing, YouTube, Qwant, DuckDuckGo safe search. (optional)
            youtube_restrict: Set safe search for YouTube restriction level. (optional)
            external_ip_blocklist: One or more external IP block lists. (optional)
            dns_translation: DNS translation settings. (optional)
            transparent_dns_database: Transparent DNS database zones. (optional)
            strip_ech: Enable/disable removal of the encrypted client hello service parameter from supporting DNS RRs. (optional)
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
        endpoint = f"/dnsfilter/profile/{name}"
        if before is not None:
            data_payload['before'] = before
        if after is not None:
            data_payload['after'] = after
        if name is not None:
            data_payload['name'] = name
        if comment is not None:
            data_payload['comment'] = comment
        if domain_filter is not None:
            data_payload['domain-filter'] = domain_filter
        if ftgd_dns is not None:
            data_payload['ftgd-dns'] = ftgd_dns
        if log_all_domain is not None:
            data_payload['log-all-domain'] = log_all_domain
        if sdns_ftgd_err_log is not None:
            data_payload['sdns-ftgd-err-log'] = sdns_ftgd_err_log
        if sdns_domain_log is not None:
            data_payload['sdns-domain-log'] = sdns_domain_log
        if block_action is not None:
            data_payload['block-action'] = block_action
        if redirect_portal is not None:
            data_payload['redirect-portal'] = redirect_portal
        if redirect_portal6 is not None:
            data_payload['redirect-portal6'] = redirect_portal6
        if block_botnet is not None:
            data_payload['block-botnet'] = block_botnet
        if safe_search is not None:
            data_payload['safe-search'] = safe_search
        if youtube_restrict is not None:
            data_payload['youtube-restrict'] = youtube_restrict
        if external_ip_blocklist is not None:
            data_payload['external-ip-blocklist'] = external_ip_blocklist
        if dns_translation is not None:
            data_payload['dns-translation'] = dns_translation
        if transparent_dns_database is not None:
            data_payload['transparent-dns-database'] = transparent_dns_database
        if strip_ech is not None:
            data_payload['strip-ech'] = strip_ech
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
        endpoint = f"/dnsfilter/profile/{name}"
        params.update(kwargs)
        return self._client.delete("cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json)

    def post(
        self,
        payload_dict: dict[str, Any] | None = None,
        nkey: str | None = None,
        name: str | None = None,
        comment: str | None = None,
        domain_filter: list | None = None,
        ftgd_dns: list | None = None,
        log_all_domain: str | None = None,
        sdns_ftgd_err_log: str | None = None,
        sdns_domain_log: str | None = None,
        block_action: str | None = None,
        redirect_portal: str | None = None,
        redirect_portal6: str | None = None,
        block_botnet: str | None = None,
        safe_search: str | None = None,
        youtube_restrict: str | None = None,
        external_ip_blocklist: list | None = None,
        dns_translation: list | None = None,
        transparent_dns_database: list | None = None,
        strip_ech: str | None = None,
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
            domain_filter: Domain filter settings. (optional)
            ftgd_dns: FortiGuard DNS Filter settings. (optional)
            log_all_domain: Enable/disable logging of all domains visited (detailed DNS logging). (optional)
            sdns_ftgd_err_log: Enable/disable FortiGuard SDNS rating error logging. (optional)
            sdns_domain_log: Enable/disable domain filtering and botnet domain logging. (optional)
            block_action: Action to take for blocked domains. (optional)
            redirect_portal: IPv4 address of the SDNS redirect portal. (optional)
            redirect_portal6: IPv6 address of the SDNS redirect portal. (optional)
            block_botnet: Enable/disable blocking botnet C&C DNS lookups. (optional)
            safe_search: Enable/disable Google, Bing, YouTube, Qwant, DuckDuckGo safe search. (optional)
            youtube_restrict: Set safe search for YouTube restriction level. (optional)
            external_ip_blocklist: One or more external IP block lists. (optional)
            dns_translation: DNS translation settings. (optional)
            transparent_dns_database: Transparent DNS database zones. (optional)
            strip_ech: Enable/disable removal of the encrypted client hello service parameter from supporting DNS RRs. (optional)
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
        endpoint = "/dnsfilter/profile"
        if nkey is not None:
            data_payload['nkey'] = nkey
        if name is not None:
            data_payload['name'] = name
        if comment is not None:
            data_payload['comment'] = comment
        if domain_filter is not None:
            data_payload['domain-filter'] = domain_filter
        if ftgd_dns is not None:
            data_payload['ftgd-dns'] = ftgd_dns
        if log_all_domain is not None:
            data_payload['log-all-domain'] = log_all_domain
        if sdns_ftgd_err_log is not None:
            data_payload['sdns-ftgd-err-log'] = sdns_ftgd_err_log
        if sdns_domain_log is not None:
            data_payload['sdns-domain-log'] = sdns_domain_log
        if block_action is not None:
            data_payload['block-action'] = block_action
        if redirect_portal is not None:
            data_payload['redirect-portal'] = redirect_portal
        if redirect_portal6 is not None:
            data_payload['redirect-portal6'] = redirect_portal6
        if block_botnet is not None:
            data_payload['block-botnet'] = block_botnet
        if safe_search is not None:
            data_payload['safe-search'] = safe_search
        if youtube_restrict is not None:
            data_payload['youtube-restrict'] = youtube_restrict
        if external_ip_blocklist is not None:
            data_payload['external-ip-blocklist'] = external_ip_blocklist
        if dns_translation is not None:
            data_payload['dns-translation'] = dns_translation
        if transparent_dns_database is not None:
            data_payload['transparent-dns-database'] = transparent_dns_database
        if strip_ech is not None:
            data_payload['strip-ech'] = strip_ech
        data_payload.update(kwargs)
        return self._client.post("cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json)
