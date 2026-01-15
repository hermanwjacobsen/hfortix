"""
FortiOS MONITOR - Firewall sessions

Configuration endpoint for managing monitor firewall/sessions objects.

API Endpoints:
    GET    /monitor/firewall/sessions
    POST   /monitor/firewall/sessions
    PUT    /monitor/firewall/sessions/{identifier}
    DELETE /monitor/firewall/sessions/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.monitor.firewall_sessions.get()
    >>>
    >>> # Create with auto-normalization (strings/lists converted automatically)
    >>> result = fgt.api.monitor.firewall_sessions.post(
    ...     name="example",
    ...     srcintf="port1",  # Auto-converted to [{'name': 'port1'}]
    ...     dstintf=["port2", "port3"],  # Auto-converted to list of dicts
    ... )

Important:
    - Use **POST** to create new objects
    - Use **PUT** to update existing objects
    - Use **GET** to retrieve configuration
    - Use **DELETE** to remove objects
    - **Auto-normalization**: List fields accept strings or lists, automatically
      converted to FortiOS format [{'name': '...'}]
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Union

if TYPE_CHECKING:
    from collections.abc import Coroutine
    from hfortix_core.http.interface import IHTTPClient
    from hfortix_fortios.models import FortiObject

# Import helper functions from central _helpers module
from hfortix_fortios._helpers import (
    build_api_payload,
    build_cmdb_payload,  # Keep for backward compatibility / manual usage
    is_success,
)
# Import metadata mixin for schema introspection
from hfortix_fortios._helpers.metadata_mixin import MetadataMixin

# Import Protocol-based type hints (eliminates need for local @overload decorators)
from hfortix_fortios._protocols import CRUDEndpoint

class Sessions(CRUDEndpoint, MetadataMixin):
    """Sessions Operations."""
    
    # Configure metadata mixin to use this endpoint's helper module
    _helper_module_name = "sessions"
    
    # ========================================================================
    # Capabilities (from schema metadata)
    # ========================================================================
    SUPPORTS_CREATE = False
    SUPPORTS_READ = True
    SUPPORTS_UPDATE = True
    SUPPORTS_DELETE = False
    SUPPORTS_MOVE = False
    SUPPORTS_CLONE = False
    SUPPORTS_FILTERING = False
    SUPPORTS_PAGINATION = True
    SUPPORTS_SEARCH = False
    SUPPORTS_SORTING = False

    def __init__(self, client: "IHTTPClient"):
        """Initialize Sessions endpoint."""
        self._client = client

    # ========================================================================
    # GET Method
    # Type hints provided by CRUDEndpoint protocol (no local @overload needed)
    # ========================================================================
    
    def get(
        self,
        name: str | None = None,
        filter: list[str] | None = None,
        count: int | None = None,
        start: int | None = None,
        q_ip_version: str | None = None,
        q_summary: bool | None = None,
        q_srcport: str | None = None,
        q_policyid: str | None = None,
        q_security_policyid: str | None = None,
        q_application: str | None = None,
        q_protocol: str | None = None,
        q_dstport: str | None = None,
        q_srcintf: str | None = None,
        q_dstintf: str | None = None,
        q_srcintfrole: list[str] | None = None,
        q_dstintfrole: list[str] | None = None,
        q_srcaddr: str | None = None,
        q_srcaddr6: str | None = None,
        q_srcuuid: str | None = None,
        q_dstaddr: str | None = None,
        q_dstaddr6: str | None = None,
        q_dstuuid: str | None = None,
        q_username: str | None = None,
        q_shaper: str | None = None,
        q_country: str | None = None,
        q_owner: str | None = None,
        q_natsourceaddress: str | None = None,
        q_natsourceport: str | None = None,
        q_since: str | None = None,
        q_seconds: str | None = None,
        q_fortiasic: str | None = None,
        q_nturbo: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        vdom: str | bool | None = None,
        error_mode: Literal["raise", "return", "print"] | None = None,
        error_format: Literal["detailed", "simple", "code_only"] | None = None,
    ):  # type: ignore[no-untyped-def]
        """
        Retrieve firewall/sessions configuration.

        List all active firewall sessions (optionally filtered).

        Args:
            name: Name identifier to retrieve specific object. If None, returns all objects.
            filter: List of filter expressions to limit results.
                Each filter uses format: "field==value" or "field!=value"
                Operators: ==, !=, =@ (contains), !@ (not contains), <=, <, >=, >
                Multiple filters use AND logic. For OR, use comma in single string.
                Example: ["name==test", "status==enable"] or ["name==test,name==prod"]
            count: Maximum number of entries to return (pagination).
            start: Starting entry index for pagination (0-based).
            payload_dict: Additional query parameters for advanced options:
                - datasource (bool): Include datasource information
                - with_meta (bool): Include metadata about each object
                - with_contents_hash (bool): Include checksum of object contents
                - format (list[str]): Property names to include (e.g., ["policyid", "srcintf"])
                - scope (str): Query scope - "global", "vdom", or "both"
                - action (str): Special actions - "schema", "default"
                See FortiOS REST API documentation for complete list.
            vdom: Virtual domain name. Use True for global, string for specific VDOM, None for default.
            error_mode: Override client-level error_mode. "raise" raises exceptions, "return" returns error dict, "print" prints errors.
            error_format: Override client-level error_format. "detailed" provides full context, "simple" is concise, "code_only" returns just status code.

        Returns:
            FortiObject instance or list of FortiObject instances. Returns Coroutine if using async client.
            Use .dict, .json, or .raw properties to access as dictionary.
            
            Response structure:
                - http_method: GET
                - results: Configuration object(s)
                - vdom: Virtual domain
                - path: API path
                - name: Object name (single object queries)
                - status: success/error
                - http_status: HTTP status code
                - build: FortiOS build number

        Examples:
            >>> # Get all firewall/sessions objects
            >>> result = fgt.api.monitor.firewall_sessions.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get with filter
            >>> result = fgt.api.monitor.firewall_sessions.get(
            ...     filter=["name==test", "status==enable"]
            ... )
            
            >>> # Get with pagination
            >>> result = fgt.api.monitor.firewall_sessions.get(
            ...     start=0, count=100
            ... )
            
            >>> # Get schema information  
            >>> schema = fgt.api.monitor.firewall_sessions.get_schema()

        See Also:
            - post(): Create new firewall/sessions object
            - put(): Update existing firewall/sessions object
            - delete(): Remove firewall/sessions object
            - exists(): Check if object exists
        """
        params = payload_dict.copy() if payload_dict else {}
        
        # Add explicit query parameters
        if filter is not None:
            params["filter"] = filter
        if count is not None:
            params["count"] = count
        if start is not None:
            params["start"] = start
        if q_ip_version is not None:
            params["ip_version"] = q_ip_version
        if q_summary is not None:
            params["summary"] = q_summary
        if q_srcport is not None:
            params["srcport"] = q_srcport
        if q_policyid is not None:
            params["policyid"] = q_policyid
        if q_security_policyid is not None:
            params["security-policyid"] = q_security_policyid
        if q_application is not None:
            params["application"] = q_application
        if q_protocol is not None:
            params["protocol"] = q_protocol
        if q_dstport is not None:
            params["dstport"] = q_dstport
        if q_srcintf is not None:
            params["srcintf"] = q_srcintf
        if q_dstintf is not None:
            params["dstintf"] = q_dstintf
        if q_srcintfrole is not None:
            params["srcintfrole"] = q_srcintfrole
        if q_dstintfrole is not None:
            params["dstintfrole"] = q_dstintfrole
        if q_srcaddr is not None:
            params["srcaddr"] = q_srcaddr
        if q_srcaddr6 is not None:
            params["srcaddr6"] = q_srcaddr6
        if q_srcuuid is not None:
            params["srcuuid"] = q_srcuuid
        if q_dstaddr is not None:
            params["dstaddr"] = q_dstaddr
        if q_dstaddr6 is not None:
            params["dstaddr6"] = q_dstaddr6
        if q_dstuuid is not None:
            params["dstuuid"] = q_dstuuid
        if q_username is not None:
            params["username"] = q_username
        if q_shaper is not None:
            params["shaper"] = q_shaper
        if q_country is not None:
            params["country"] = q_country
        if q_owner is not None:
            params["owner"] = q_owner
        if q_natsourceaddress is not None:
            params["natsourceaddress"] = q_natsourceaddress
        if q_natsourceport is not None:
            params["natsourceport"] = q_natsourceport
        if q_since is not None:
            params["since"] = q_since
        if q_seconds is not None:
            params["seconds"] = q_seconds
        if q_fortiasic is not None:
            params["fortiasic"] = q_fortiasic
        if q_nturbo is not None:
            params["nturbo"] = q_nturbo
        
        if name:
            endpoint = f"/firewall/sessions/{name}"
            unwrap_single = True
        else:
            endpoint = "/firewall/sessions"
            unwrap_single = False
        
        return self._client.get(
            "monitor", endpoint, params=params, vdom=vdom, unwrap_single=unwrap_single
        )









    # ========================================================================
    # Helper: Check Existence
    # ========================================================================
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = None,
    ) -> bool:
        """
        Check if firewall/sessions object exists.
        
        Args:
            name: Name to check
            vdom: Virtual domain name
            
        Returns:
            True if object exists, False otherwise
            
        Example:
            >>> # Check before creating
            >>> if not fgt.api.monitor.firewall_sessions.exists(name="myobj"):
            ...     fgt.api.monitor.firewall_sessions.post(payload_dict=data)
        """
        # Use direct request with silent error handling to avoid logging 404s
        # This is expected behavior for exists() - 404 just means "doesn't exist"
        endpoint = "/firewall/sessions"
        endpoint = f"{endpoint}/{quote_path_param(name)}"
        
        # Make request with silent=True to suppress 404 error logging
        # (404 is expected when checking existence - it just means "doesn't exist")
        # Use _wrapped_client to access the underlying HTTPClient directly
        # (self._client is ResponseProcessingClient, _wrapped_client is HTTPClient)
        try:
            result = self._client._wrapped_client.get(
                "monitor",
                endpoint,
                params=None,
                vdom=vdom,
                raw_json=True,
                silent=True,
            )
            
            if isinstance(result, dict):
                # Synchronous response - check status
                return result.get("status") == "success"
            else:
                # Asynchronous response
                async def _check() -> bool:
                    r = await result
                    return r.get("status") == "success"
                return _check()
        except Exception:
            # Any error (404, network, etc.) means we can't confirm existence
            return False

