"""
FortiOS MONITOR - Firewall policy_lookup

Configuration endpoint for managing monitor firewall/policy_lookup objects.

API Endpoints:
    GET    /monitor/firewall/policy_lookup
    POST   /monitor/firewall/policy_lookup
    PUT    /monitor/firewall/policy_lookup/{identifier}
    DELETE /monitor/firewall/policy_lookup/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.monitor.firewall_policy_lookup.get()
    >>>
    >>> # Create with auto-normalization (strings/lists converted automatically)
    >>> result = fgt.api.monitor.firewall_policy_lookup.post(
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

class PolicyLookup(CRUDEndpoint, MetadataMixin):
    """PolicyLookup Operations."""
    
    # Configure metadata mixin to use this endpoint's helper module
    _helper_module_name = "policy_lookup"
    
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
    SUPPORTS_PAGINATION = False
    SUPPORTS_SEARCH = False
    SUPPORTS_SORTING = False

    def __init__(self, client: "IHTTPClient"):
        """Initialize PolicyLookup endpoint."""
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
        q_ipv6: bool | None = None,
        q_srcintf: str | None = None,
        q_sourceport: int | None = None,
        q_sourceip: str | None = None,
        q_protocol: str | None = None,
        q_dest: str | None = None,
        q_destport: int | None = None,
        q_icmptype: int | None = None,
        q_icmpcode: int | None = None,
        q_policy_type: str | None = None,
        q_auth_type: str | None = None,
        q_user_group: list[str] | None = None,
        q_server_name: str | None = None,
        q_user_db: str | None = None,
        q_group_attr_type: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        vdom: str | bool | None = None,
        error_mode: Literal["raise", "return", "print"] | None = None,
        error_format: Literal["detailed", "simple", "code_only"] | None = None,
    ):  # type: ignore[no-untyped-def]
        """
        Retrieve firewall/policy_lookup configuration.

        Performs a policy lookup by creating a dummy packet and asking the kernel which policy would be hit.

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
            >>> # Get all firewall/policy_lookup objects
            >>> result = fgt.api.monitor.firewall_policy_lookup.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get with filter
            >>> result = fgt.api.monitor.firewall_policy_lookup.get(
            ...     filter=["name==test", "status==enable"]
            ... )
            
            >>> # Get with pagination
            >>> result = fgt.api.monitor.firewall_policy_lookup.get(
            ...     start=0, count=100
            ... )
            
            >>> # Get schema information  
            >>> schema = fgt.api.monitor.firewall_policy_lookup.get_schema()

        See Also:
            - post(): Create new firewall/policy_lookup object
            - put(): Update existing firewall/policy_lookup object
            - delete(): Remove firewall/policy_lookup object
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
        if q_ipv6 is not None:
            params["ipv6"] = q_ipv6
        if q_srcintf is not None:
            params["srcintf"] = q_srcintf
        if q_sourceport is not None:
            params["sourceport"] = q_sourceport
        if q_sourceip is not None:
            params["sourceip"] = q_sourceip
        if q_protocol is not None:
            params["protocol"] = q_protocol
        if q_dest is not None:
            params["dest"] = q_dest
        if q_destport is not None:
            params["destport"] = q_destport
        if q_icmptype is not None:
            params["icmptype"] = q_icmptype
        if q_icmpcode is not None:
            params["icmpcode"] = q_icmpcode
        if q_policy_type is not None:
            params["policy_type"] = q_policy_type
        if q_auth_type is not None:
            params["auth_type"] = q_auth_type
        if q_user_group is not None:
            params["user_group"] = q_user_group
        if q_server_name is not None:
            params["server_name"] = q_server_name
        if q_user_db is not None:
            params["user_db"] = q_user_db
        if q_group_attr_type is not None:
            params["group_attr_type"] = q_group_attr_type
        
        if name:
            endpoint = f"/firewall/policy-lookup/{name}"
            unwrap_single = True
        else:
            endpoint = "/firewall/policy-lookup"
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
        Check if firewall/policy_lookup object exists.
        
        Args:
            name: Name to check
            vdom: Virtual domain name
            
        Returns:
            True if object exists, False otherwise
            
        Example:
            >>> # Check before creating
            >>> if not fgt.api.monitor.firewall_policy_lookup.exists(name="myobj"):
            ...     fgt.api.monitor.firewall_policy_lookup.post(payload_dict=data)
        """
        # Try to fetch the object - 404 means it doesn't exist
        try:
            result = self.get(
                name=name,
                vdom=vdom
            )
            response = result.raw if hasattr(result, 'raw') else result
            # Check if response indicates success
            return is_success(response)
        except Exception as e:
            # 404 means object doesn't exist - return False
            # Any other error should be re-raised
            error_str = str(e)
            if '404' in error_str or 'Not Found' in error_str or 'ResourceNotFoundError' in str(type(e)):
                return False
            raise

