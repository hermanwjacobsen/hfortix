"""
FortiOS CMDB - Rule OTDT

Show OT (Operational Technology) detection signatures.

API Endpoints:
    GET    /api/v2/cmdb/rule/otdt           - List all / Get specific
    POST   /api/v2/cmdb/rule/otdt           - Create
    PUT    /api/v2/cmdb/rule/otdt/{name}   - Update
    DELETE /api/v2/cmdb/rule/otdt/{name}   - Delete
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional, Union

from hfortix.FortiOS.http_client import encode_path_component

if TYPE_CHECKING:
    from ....http_client import HTTPClient


class Otdt:
    """Rule OTDT endpoint"""

    def __init__(self, client: "HTTPClient") -> None:
        """
        Initialize Rule OTDT endpoint

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def get(
        self,
        name: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Get OT detection signature(s) - List all or get specific.

        Args:
            name: Signature name (if specified, gets single signature)
            vdom: Virtual domain (None=use default, False=skip vdom, or specific vdom)
            **kwargs: Additional query parameters

        Returns:
            API response dict

        Examples:
            >>> result = fgt.api.cmdb.rule.otdt.get()
            >>> result = fgt.api.cmdb.rule.otdt.get(name='signature1')
        """
        path = "rule/otdt"
        if name:
            path = f"{path}/{encode_path_component(name)}"
        return self._client.get("cmdb", path, params=kwargs if kwargs else None, vdom=vdom)

    # NOTE: OT detection signatures are READ-ONLY (managed by FortiGuard Services)
    # The create/update/delete methods are included for API completeness but will
    # return HTTP 500 errors as these signatures cannot be manually created/modified.
    
    def post(
        self,
        data_dict: Optional[dict[str, Any]] = None,
        name: Optional[str] = None,
        status: Optional[str] = None,
        log: Optional[str] = None,
        log_packet: Optional[str] = None,
        action: Optional[str] = None,
        severity: Optional[str] = None,
        location: Optional[str] = None,
        os: Optional[str] = None,
        application: Optional[str] = None,
        service: Optional[str] = None,
        rule_id: Optional[int] = None,
        rev: Optional[int] = None,
        date: Optional[int] = None,
        metadata: Optional[list] = None,
        vdom: Optional[Union[str, bool]] = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Create OT detection signature.
        
        NOTE: This operation is not supported. OT detection signatures are read-only and 
        managed by FortiGuard Services. This method will return an error.

        Args:
            data_dict: Complete signature configuration dictionary
            name: Rule name (max 63 chars)
            status: Enable/disable rule. Options: 'disable', 'enable'
            log: Enable/disable logging. Options: 'disable', 'enable'
            log_packet: Enable/disable packet logging. Options: 'disable', 'enable'
            action: Action for matching traffic. Options: 'pass', 'block'
            severity: Severity level
            location: Vulnerable location
            os: Vulnerable operating systems
            application: Vulnerable applications
            service: Vulnerable service
            rule_id: Rule ID (0-4294967295)
            rev: Revision number (0-4294967295)
            date: Date (0-4294967295)
            metadata: List of metadata dicts
            vdom: Virtual domain (None=use default, False=skip vdom, or specific vdom)
            **kwargs: Additional parameters

        Returns:
            API response dict

        Examples:
            >>> # Using data_dict
            >>> data = {
            ...     'name': 'ot-sig1',
            ...     'status': 'enable',
            ...     'action': 'block',
            ...     'log': 'enable'
            ... }
            >>> result = fgt.api.cmdb.rule.otdt.create(data_dict=data)
            >>> 
            >>> # Using explicit parameters
            >>> result = fgt.api.cmdb.rule.otdt.create(
            ...     name='ot-sig1',
            ...     status='enable',
            ...     action='block',
            ...     severity='critical'
            ... )
        """
        data = data_dict.copy() if data_dict else {}
        
        if name is not None:
            data["name"] = name
        if status is not None:
            data["status"] = status
        if log is not None:
            data["log"] = log
        if log_packet is not None:
            data["log-packet"] = log_packet
        if action is not None:
            data["action"] = action
        if severity is not None:
            data["severity"] = severity
        if location is not None:
            data["location"] = location
        if os is not None:
            data["os"] = os
        if application is not None:
            data["application"] = application
        if service is not None:
            data["service"] = service
        if rule_id is not None:
            data["rule-id"] = rule_id
        if rev is not None:
            data["rev"] = rev
        if date is not None:
            data["date"] = date
        if metadata is not None:
            data["metadata"] = metadata
            
        data.update(kwargs)
        return self._client.post("cmdb", "rule/otdt", data=data, vdom=vdom)

    def put(
        self,
        name: str,
        data_dict: Optional[dict[str, Any]] = None,
        status: Optional[str] = None,
        log: Optional[str] = None,
        log_packet: Optional[str] = None,
        action: Optional[str] = None,
        severity: Optional[str] = None,
        location: Optional[str] = None,
        os: Optional[str] = None,
        application: Optional[str] = None,
        service: Optional[str] = None,
        rule_id: Optional[int] = None,
        rev: Optional[int] = None,
        date: Optional[int] = None,
        metadata: Optional[list] = None,
        vdom: Optional[Union[str, bool]] = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Update OT detection signature.
        
        NOTE: This operation is not supported. OT detection signatures are read-only and 
        managed by FortiGuard Services. This method will return an error.

        Args:
            name: Signature name (required)
            data_dict: Complete signature configuration dictionary
            status: Enable/disable rule. Options: 'disable', 'enable'
            log: Enable/disable logging. Options: 'disable', 'enable'
            log_packet: Enable/disable packet logging. Options: 'disable', 'enable'
            action: Action for matching traffic. Options: 'pass', 'block'
            severity: Severity level
            location: Vulnerable location
            os: Vulnerable operating systems
            application: Vulnerable applications
            service: Vulnerable service
            rule_id: Rule ID (0-4294967295)
            rev: Revision number (0-4294967295)
            date: Date (0-4294967295)
            metadata: List of metadata dicts
            vdom: Virtual domain (None=use default, False=skip vdom, or specific vdom)
            **kwargs: Additional parameters to update

        Returns:
            API response dict

        Examples:
            >>> # Using data_dict
            >>> data = {'status': 'disable'}
            >>> result = fgt.api.cmdb.rule.otdt.update(name='ot-sig1', data_dict=data)
            >>> 
            >>> # Using explicit parameters
            >>> result = fgt.api.cmdb.rule.otdt.update(
            ...     name='ot-sig1',
            ...     status='enable',
            ...     action='pass'
            ... )
        """
        data = data_dict.copy() if data_dict else {}
        
        if status is not None:
            data["status"] = status
        if log is not None:
            data["log"] = log
        if log_packet is not None:
            data["log-packet"] = log_packet
        if action is not None:
            data["action"] = action
        if severity is not None:
            data["severity"] = severity
        if location is not None:
            data["location"] = location
        if os is not None:
            data["os"] = os
        if application is not None:
            data["application"] = application
        if service is not None:
            data["service"] = service
        if rule_id is not None:
            data["rule-id"] = rule_id
        if rev is not None:
            data["rev"] = rev
        if date is not None:
            data["date"] = date
        if metadata is not None:
            data["metadata"] = metadata
            
        data.update(kwargs)
        path = f"rule/otdt/{encode_path_component(name)}"
        return self._client.put("cmdb", path, data=data, vdom=vdom)

    def delete(self, name: str, vdom: Optional[Union[str, bool]] = None) -> dict[str, Any]:
        """
        Delete OT detection signature.
        
        NOTE: This operation is not supported. OT detection signatures are read-only and 
        managed by FortiGuard Services. This method will return an error.

        Args:
            name: Signature name
            vdom: Virtual domain (None=use default, False=skip vdom, or specific vdom)

        Returns:
            API response dict

        Examples:
            >>> result = fgt.api.cmdb.rule.otdt.delete(name='ot-sig1')
        """
        path = f"rule/otdt/{encode_path_component(name)}"
        return self._client.delete("cmdb", path, vdom=vdom)

    def exists(self, name: str, vdom: Optional[Union[str, bool]] = None) -> bool:
        """
        Check if OT detection signature exists.

        Args:
            name: Signature name
            vdom: Virtual domain (None=use default, False=skip vdom, or specific vdom)

        Returns:
            True if signature exists, False otherwise

        Examples:
            >>> if fgt.api.cmdb.rule.otdt.exists(name='ot-sig1'):
            ...     print("Signature exists")
        """
        try:
            self.get(name=name, vdom=vdom)
            return True
        except Exception:
            return False
