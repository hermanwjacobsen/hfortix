"""
FortiOS CMDB - Firewall Authentication Portal

Configure firewall authentication portals.

API Endpoints:
    GET /api/v2/cmdb/firewall/auth-portal - Get authentication portal configuration
    PUT /api/v2/cmdb/firewall/auth-portal - Update authentication portal configuration

Reference (FortiOS 7.6.5):
    - groups: Firewall user groups permitted to authenticate through this portal
    - portal-addr: Address (or FQDN) of the authentication portal
    - portal-addr6: IPv6 address (or FQDN) of authentication portal
    - identity-based-route: Name of the identity-based route that applies to this portal
    - proxy-auth: Enable/disable authentication by proxy daemon
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Dict, Optional, Union

if TYPE_CHECKING:
    from ....http_client import HTTPClient


from hfortix.FortiOS.http_client import encode_path_component


class AuthPortal:
    """Firewall auth-portal singleton endpoint."""

    # Fortinet-documented endpoint identifiers
    name = "auth-portal"
    path = "firewall/auth-portal"

    def __init__(self, client: "HTTPClient") -> None:
        """Initialize AuthPortal endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def get(
        self,
        datasource: Optional[bool] = None,
        with_meta: Optional[bool] = None,
        skip: Optional[bool] = None,
        format: Optional[list] = None,
        action: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Get authentication portal configuration.

        This is a singleton-ish CMDB endpoint (no name/key in the path).

        Args:
            datasource: Include datasource information
            with_meta: Include metadata
            skip: Enable CLI skip operator
            format: List of property names to include
            action: Special actions (default, schema)
            vdom: Virtual domain (None=use default, False=skip vdom, or specific vdom)
            **kwargs: Additional query parameters

        Returns:
            API response dict

        Examples:
            >>> result = fgt.api.cmdb.firewall.auth_portal.get()
            >>> result = fgt.api.cmdb.firewall.auth_portal.get(action='schema')
        """
        params: dict[str, Any] = {}
        param_map = {
            "datasource": datasource,
            "with_meta": with_meta,
            "skip": skip,
            "format": format,
            "action": action,
        }

        for key, value in param_map.items():
            if value is not None:
                params[key] = value

        params.update(kwargs)

        return self._client.get(
            "cmdb", self.path, params=params if params else None, vdom=vdom, raw_json=raw_json
        )

    def put(
        self,
        payload_dict: Optional[Dict[str, Any]] = None,
        groups: Optional[list[dict[str, Any]]] = None,
        portal_addr: Optional[str] = None,
        portal_addr6: Optional[str] = None,
        identity_based_route: Optional[str] = None,
        proxy_auth: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        action: Optional[str] = None,
        before: Optional[str] = None,
        after: Optional[str] = None,
        scope: Optional[str] = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Update authentication portal configuration.

        Note: The API uses hyphenated field names; this method accepts snake_case
        and maps to FortiOS fields.

        Args:
            groups: List of group objects, e.g. [{"name": "grp1"}, {"name": "grp2"}]
            portal_addr: Portal address/FQDN (maps to "portal-addr")
            portal_addr6: Portal IPv6 address/FQDN (maps to "portal-addr6")
            identity_based_route: Identity-based route name (maps to "identity-based-route")
            proxy_auth: 'enable' or 'disable' (maps to "proxy-auth")
            vdom: Virtual domain (None=use default, False=skip vdom, or specific vdom)
            action: If supported, can be 'move'
            before: If action=move, move before specified ID
            after: If action=move, move after specified ID
            scope: Scope (e.g. 'vdom')
            **kwargs: Additional parameters to include in the request body

        Returns:
            API response dict

        Examples:
            >>> result = fgt.api.cmdb.firewall.auth_portal.update(
            ...     portal_addr='auth.example.com',
            ...     proxy_auth='enable',
            ... )
        """
        # Support both patterns: data dict or individual kwargs
        if payload_dict is not None:
            # Pattern 1: data dict provided
            payload = payload_dict.copy()
        else:
            # Pattern 2: build from kwargs
            payload: Dict[str, Any] = {}

            field_map = {
                "groups": groups,
                "portal-addr": portal_addr,
                "portal-addr6": portal_addr6,
                "identity-based-route": identity_based_route,
                "proxy-auth": proxy_auth,
            }

            for key, value in field_map.items():
                if value is not None:
                    payload[key] = value

            # Add any additional kwargs as-is
            for key, value in kwargs.items():
                if value is not None:
                    payload[key] = value

        params: dict[str, Any] = {}
        param_map = {
            "action": action,
            "before": before,
            "after": after,
            "scope": scope,
        }
        for key, value in param_map.items():
            if value is not None:
                params[key] = value

        return self._client.put(
            "cmdb",
            self.path,
            data=payload,
            params=params if params else None,
            vdom=vdom,
            raw_json=raw_json,
        )
