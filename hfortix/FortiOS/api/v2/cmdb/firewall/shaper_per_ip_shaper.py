"""
FortiOS CMDB - Firewall Per-IP Traffic Shaper
Configure per-IP traffic shaper.

API Endpoints:
    GET    /api/v2/cmdb/firewall.shaper/per-ip-shaper           - List all / Get specific
    POST   /api/v2/cmdb/firewall.shaper/per-ip-shaper           - Create
    PUT    /api/v2/cmdb/firewall.shaper/per-ip-shaper/{id}   - Update
    DELETE /api/v2/cmdb/firewall.shaper/per-ip-shaper/{id}   - Delete
"""

from typing import Any, Dict, List, Optional, Union

from hfortix.FortiOS.http_client import encode_path_component

from .....http_client import HTTPResponse


class PerIpShaper:
    """Per-IP traffic shaper endpoint"""

    def __init__(self, client):
        self._client = client

    def get(
        self,
        name: Optional[str] = None,
        filter: Optional[str] = None,
        range: Optional[str] = None,
        sort: Optional[str] = None,
        format: Optional[List[str]] = None,
        vdom: Optional[Union[str, bool]] = None,
        raw_json: bool = False,
        **kwargs,
    ) -> HTTPResponse:
        """
        Get per-IP traffic shaper(s) - List all or get specific.

        Args:
            name: Per-IP shaper name (if retrieving specific shaper)
            filter: Filter results
            range: Range of results
            sort: Sort results
            format: List of fields to include
            vdom: Virtual domain
            **kwargs: Additional parameters

        Returns:
            API response dictionary

        Examples:
            >>> # Get specific per-IP shaper
            >>> result = fgt.cmdb.firewall.shaper.per_ip_shaper.get('high-priority')

            >>> # Get all per-IP shapers
            >>> result = fgt.cmdb.firewall.shaper.per_ip_shaper.get()
        """
        path = "firewall.shaper/per-ip-shaper"
        if name:
            path = f"{path}/{encode_path_component(name)}"

        params = {}
        param_map = {
            "filter": filter,
            "range": range,
            "sort": sort,
            "format": format,
        }
        for key, value in param_map.items():
            if value is not None:
                params[key] = value
        params.update(kwargs)

        return self._client.get(
            "cmdb", path, params=params if params else None, vdom=vdom, raw_json=raw_json
        )

    def post(
        self,
        payload_dict: Optional[Dict[str, Any]] = None,
        name: Optional[str] = None,
        max_bandwidth: Optional[int] = None,
        max_concurrent_session: Optional[int] = None,
        max_concurrent_tcp_session: Optional[int] = None,
        max_concurrent_udp_session: Optional[int] = None,
        comment: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        raw_json: bool = False,
        **kwargs,
    ) -> HTTPResponse:
        """
        Create a per-IP traffic shaper.


        Supports two usage patterns:
        1. Pass data dict: create(payload_dict={'key': 'value'}, vdom='root')
        2. Pass kwargs: create(key='value', vdom='root')
        Args:
            name: Per-IP shaper name (max 35 chars)
            max_bandwidth: Upper bandwidth limit (0-16776000 kbps, 0 = unlimited)
            max_concurrent_session: Maximum concurrent sessions (0-2097000, 0 = unlimited)
            max_concurrent_tcp_session: Maximum concurrent TCP sessions (0-2097000, 0 = unlimited)
            max_concurrent_udp_session: Maximum concurrent UDP sessions (0-2097000, 0 = unlimited)
            comment: Comment (max 1023 chars)
            vdom: Virtual domain
            **kwargs: Additional parameters

        Returns:
            API response dictionary

        Examples:
            >>> # POST - Create per-IP shaper with bandwidth limit
            >>> result = fgt.cmdb.firewall.shaper.per_ip_shaper.create(
            ...     'user-limit',
            ...     max_bandwidth=10240,
            ...     max_concurrent_session=100,
            ...     comment='Per-user bandwidth limit'
            ... )

            >>> # POST - Create per-IP shaper with TCP/UDP session limits
            >>> result = fgt.cmdb.firewall.shaper.per_ip_shaper.create(
            ...     'session-limit',
            ...     max_concurrent_tcp_session=50,
            ...     max_concurrent_udp_session=30
            ... )
        """
        # Pattern 1: data dict provided
        if payload_dict is not None:
            # Use provided data dict
            pass
        # Pattern 2: kwargs pattern - build data dict
        else:
            payload_dict = {}
            if name is not None:
                payload_dict["name"] = name
            if max_bandwidth is not None:
                payload_dict["max-bandwidth"] = max_bandwidth
            if max_concurrent_session is not None:
                payload_dict["max-concurrent-session"] = max_concurrent_session
            if max_concurrent_tcp_session is not None:
                payload_dict["max-concurrent-tcp-session"] = max_concurrent_tcp_session
            if max_concurrent_udp_session is not None:
                payload_dict["max-concurrent-udp-session"] = max_concurrent_udp_session
            if comment is not None:
                payload_dict["comment"] = comment

        return self._client.post(
            "cmdb", "firewall.shaper/per-ip-shaper", payload_dict, vdom=vdom, raw_json=raw_json
        )

    def put(
        self,
        name: str,
        payload_dict: Optional[Dict[str, Any]] = None,
        max_bandwidth: Optional[int] = None,
        max_concurrent_session: Optional[int] = None,
        max_concurrent_tcp_session: Optional[int] = None,
        max_concurrent_udp_session: Optional[int] = None,
        comment: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        raw_json: bool = False,
        **kwargs,
    ) -> HTTPResponse:
        """
        Update a per-IP traffic shaper.


        Supports two usage patterns:
        1. Pass data dict: update(payload_dict={'key': 'value'}, vdom='root')
        2. Pass kwargs: update(key='value', vdom='root')
        Args:
            name: Per-IP shaper name
            max_bandwidth: Upper bandwidth limit (0-16776000 kbps, 0 = unlimited)
            max_concurrent_session: Maximum concurrent sessions (0-2097000, 0 = unlimited)
            max_concurrent_tcp_session: Maximum concurrent TCP sessions (0-2097000, 0 = unlimited)
            max_concurrent_udp_session: Maximum concurrent UDP sessions (0-2097000, 0 = unlimited)
            comment: Comment (max 1023 chars)
            vdom: Virtual domain
            **kwargs: Additional parameters

        Returns:
            API response dictionary

        Examples:
            >>> # PUT - Update bandwidth limit
            >>> result = fgt.cmdb.firewall.shaper.per_ip_shaper.update(
            ...     'user-limit',
            ...     max_bandwidth=20480
            ... )

            >>> # PUT - Update session limits
            >>> result = fgt.cmdb.firewall.shaper.per_ip_shaper.update(
            ...     'session-limit',
            ...     max_concurrent_tcp_session=100,
            ...     max_concurrent_udp_session=50
            ... )
        """
        # Pattern 1: data dict provided
        if payload_dict is not None:
            # Use provided data dict
            pass
        # Pattern 2: kwargs pattern - build data dict
        else:
            payload_dict = {}
            if max_bandwidth is not None:
                payload_dict["max-bandwidth"] = max_bandwidth
            if max_concurrent_session is not None:
                payload_dict["max-concurrent-session"] = max_concurrent_session
            if max_concurrent_tcp_session is not None:
                payload_dict["max-concurrent-tcp-session"] = max_concurrent_tcp_session
            if max_concurrent_udp_session is not None:
                payload_dict["max-concurrent-udp-session"] = max_concurrent_udp_session
            if comment is not None:
                payload_dict["comment"] = comment

        return self._client.put(
            "cmdb",
            f"firewall.shaper/per-ip-shaper/{name}",
            payload_dict,
            vdom=vdom,
            raw_json=raw_json,
        )

    def delete(
        self,
        name: str,
        vdom: Optional[Union[str, bool]] = None,
        raw_json: bool = False,
    ) -> HTTPResponse:
        """
        Delete a per-IP traffic shaper.

        Args:
            name: Per-IP shaper name
            vdom: Virtual domain

        Returns:
            API response dictionary

        Examples:
            >>> # Delete per-IP shaper
            >>> result = fgt.cmdb.firewall.shaper.per_ip_shaper.delete('user-limit')
        """
        return self._client.delete(
            "cmdb", f"firewall.shaper/per-ip-shaper/{name}", vdom=vdom, raw_json=raw_json
        )

    def exists(self, name: str, vdom: Optional[Union[str, bool]] = None) -> bool:
        """
        Check if per-IP shaper exists.

        Args:
            name: Per-IP shaper name
            vdom: Virtual domain

        Returns:
            True if per-IP shaper exists, False otherwise

        Examples:
            >>> if fgt.cmdb.firewall.shaper.per_ip_shaper.exists('user-limit'):
            ...     print("Per-IP shaper exists")
        """
        try:
            result = self.get(name, vdom=vdom, raw_json=True)
            return (
                result.get("status") == "success"
                and result.get("http_status") == 200
                and len(result.get("results", [])) > 0
            )
        except Exception:
            return False
