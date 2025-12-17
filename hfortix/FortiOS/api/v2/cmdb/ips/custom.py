"""
FortiOS CMDB - IPS Custom

Configure IPS custom signature.

API Endpoints:
    GET    /api/v2/cmdb/ips/custom        - List all custom signatures
    GET    /api/v2/cmdb/ips/custom/{tag}  - Get specific custom signature
    POST   /api/v2/cmdb/ips/custom        - Create custom signature
    PUT    /api/v2/cmdb/ips/custom/{tag}  - Update custom signature
    DELETE /api/v2/cmdb/ips/custom/{tag}  - Delete custom signature
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional, Union

if TYPE_CHECKING:
    from ...http_client import HTTPClient

from hfortix.FortiOS.http_client import encode_path_component


class Custom:
    """IPS Custom Signature endpoint"""

    def __init__(self, client: "HTTPClient") -> None:
        self._client = client

    def list(self, vdom: Optional[Union[str, bool]] = None, **kwargs: Any) -> dict[str, Any]:
        """
        List all IPS custom signatures.

        Args:
            vdom: Virtual domain name or False for global
            **kwargs: Additional parameters

        Returns:
            Dictionary containing list of custom signatures

        Examples:
            >>> # List all custom signatures
            >>> sigs = fgt.api.cmdb.ips.custom.list()
        """
        path = "ips/custom"
        return self._client.get("cmdb", path, params=kwargs if kwargs else None, vdom=vdom)

    def get(
        self, tag: str, vdom: Optional[Union[str, bool]] = None, **kwargs: Any
    ) -> dict[str, Any]:
        """
        Get specific IPS custom signature.

        Args:
            tag: Signature tag
            vdom: Virtual domain name or False for global
            **kwargs: Additional parameters

        Returns:
            Dictionary containing signature configuration

        Examples:
            >>> sig = fgt.api.cmdb.ips.custom.get('custom-sig-1')
        """
        path = f"ips/custom/{encode_path_component(tag)}"
        return self._client.get("cmdb", path, params=kwargs if kwargs else None, vdom=vdom)

    def create(
        self,
        data_dict: Optional[dict[str, Any]] = None,
        tag: Optional[str] = None,
        signature: Optional[str] = None,
        rule_id: Optional[int] = None,
        severity: Optional[str] = None,
        location: Optional[str] = None,
        os: Optional[str] = None,
        application: Optional[str] = None,
        protocol: Optional[str] = None,
        status: Optional[str] = None,
        log: Optional[str] = None,
        log_packet: Optional[str] = None,
        action: Optional[str] = None,
        comment: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Create IPS custom signature.

        Args:
            data_dict: Complete configuration dictionary
            tag: Signature tag (max 63 chars)
            signature: Custom signature content
            rule_id: Rule ID in IPS database (0-4294967295)
            severity: Signature severity (info|low|medium|high|critical)
            location: Protect client or server traffic
            os: Operating systems to protect
            application: Applications to protect
            protocol: Protocols to examine
            status: Enable/disable signature (disable|enable)
            log: Enable/disable logging (disable|enable)
            log_packet: Enable/disable packet logging (disable|enable)
            action: Action for detected traffic (pass|block|reset)
            comment: Comment (max 255 chars)
            vdom: Virtual domain name or False for global
            **kwargs: Additional parameters

        Returns:
            Dictionary containing creation result

        Examples:
            >>> fgt.api.cmdb.ips.custom.create(
            ...     tag='custom-sig-1',
            ...     signature='F-SBID( --name "custom"; )',
            ...     severity='high',
            ...     action='block'
            ... )
        """
        data = data_dict.copy() if data_dict else {}

        param_map = {
            "tag": tag,
            "signature": signature,
            "rule-id": rule_id,
            "severity": severity,
            "location": location,
            "os": os,
            "application": application,
            "protocol": protocol,
            "status": status,
            "log": log,
            "log-packet": log_packet,
            "action": action,
            "comment": comment,
        }

        for key, value in param_map.items():
            if value is not None:
                data[key] = value

        data.update(kwargs)

        path = "ips/custom"
        return self._client.post("cmdb", path, data=data, vdom=vdom)

    def update(
        self,
        tag: str,
        data_dict: Optional[dict[str, Any]] = None,
        signature: Optional[str] = None,
        rule_id: Optional[int] = None,
        severity: Optional[str] = None,
        location: Optional[str] = None,
        os: Optional[str] = None,
        application: Optional[str] = None,
        protocol: Optional[str] = None,
        status: Optional[str] = None,
        log: Optional[str] = None,
        log_packet: Optional[str] = None,
        action: Optional[str] = None,
        comment: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Update IPS custom signature.

        Args:
            tag: Signature tag to update
            data_dict: Complete configuration dictionary
            signature: Custom signature content
            rule_id: Rule ID in IPS database (0-4294967295)
            severity: Signature severity (info|low|medium|high|critical)
            location: Protect client or server traffic
            os: Operating systems to protect
            application: Applications to protect
            protocol: Protocols to examine
            status: Enable/disable signature (disable|enable)
            log: Enable/disable logging (disable|enable)
            log_packet: Enable/disable packet logging (disable|enable)
            action: Action for detected traffic (pass|block|reset)
            comment: Comment (max 255 chars)
            vdom: Virtual domain name or False for global
            **kwargs: Additional parameters

        Returns:
            Dictionary containing update result

        Examples:
            >>> fgt.api.cmdb.ips.custom.update(
            ...     'custom-sig-1',
            ...     severity='critical',
            ...     action='reset'
            ... )
        """
        data = data_dict.copy() if data_dict else {}

        param_map = {
            "signature": signature,
            "rule-id": rule_id,
            "severity": severity,
            "location": location,
            "os": os,
            "application": application,
            "protocol": protocol,
            "status": status,
            "log": log,
            "log-packet": log_packet,
            "action": action,
            "comment": comment,
        }

        for key, value in param_map.items():
            if value is not None:
                data[key] = value

        data.update(kwargs)

        path = f"ips/custom/{encode_path_component(tag)}"
        return self._client.put("cmdb", path, data=data, vdom=vdom)

    def delete(self, tag: str, vdom: Optional[Union[str, bool]] = None) -> dict[str, Any]:
        """
        Delete IPS custom signature.

        Args:
            tag: Signature tag
            vdom: Virtual domain name or False for global

        Returns:
            Dictionary containing deletion result

        Examples:
            >>> fgt.api.cmdb.ips.custom.delete('custom-sig-1')
        """
        path = f"ips/custom/{encode_path_component(tag)}"
        return self._client.delete("cmdb", path, vdom=vdom)

    def exists(self, tag: str, vdom: Optional[Union[str, bool]] = None) -> bool:
        """
        Check if IPS custom signature exists.

        Args:
            tag: Signature tag
            vdom: Virtual domain name or False for global

        Returns:
            True if signature exists, False otherwise

        Examples:
            >>> if fgt.api.cmdb.ips.custom.exists('custom-sig-1'):
            ...     print("Signature exists")
        """
        try:
            self.get(tag, vdom=vdom)
            return True
        except Exception:
            return False
