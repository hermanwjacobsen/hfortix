"""
FortiOS CMDB - Rule FMWP

Show FMWP (FortiManager Wireless Protection) signatures.

API Endpoints:
    GET    /api/v2/cmdb/rule/fmwp           - List all / Get specific
    POST   /api/v2/cmdb/rule/fmwp           - Create
    PUT    /api/v2/cmdb/rule/fmwp/{name}   - Update
    DELETE /api/v2/cmdb/rule/fmwp/{name}   - Delete
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional, Union

from hfortix.FortiOS.http_client import encode_path_component

if TYPE_CHECKING:
    from ....http_client import HTTPClient


class Fmwp:
    """Rule FMWP endpoint"""

    def __init__(self, client: "HTTPClient") -> None:
        """
        Initialize Rule FMWP endpoint

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
        Get FMWP signature(s) - List all or get specific.

        Args:
            name: Signature name (if specified, gets single signature)
            vdom: Virtual domain (None=use default, False=skip vdom, or specific vdom)
            **kwargs: Additional query parameters

        Returns:
            API response dict

        Examples:
            >>> result = fgt.api.cmdb.rule.fmwp.get()
            >>> result = fgt.api.cmdb.rule.fmwp.get(name='signature1')
        """
        path = "rule/fmwp"
        if name:
            path = f"{path}/{encode_path_component(name)}"
        return self._client.get("cmdb", path, params=kwargs if kwargs else None, vdom=vdom)

    # NOTE: FMWP signatures are READ-ONLY (managed by FortiGuard Services)
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
        group: Optional[str] = None,
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
        Create FMWP signature.
        
        NOTE: This operation is not supported. FMWP signatures are read-only and 
        managed by FortiGuard Services. This method will return an error.

        Args:
            data_dict: Complete signature configuration dictionary
            name: Rule name (max 63 chars)
            status: Enable/disable rule. Options: 'disable', 'enable'
            log: Enable/disable logging. Options: 'disable', 'enable'
            log_packet: Enable/disable packet logging. Options: 'disable', 'enable'
            action: Action for matching traffic. Options: 'pass', 'block'
            group: Rule group (max 63 chars)
            severity: Severity level
            location: Vulnerable location
            os: Vulnerable operating systems
            application: Vulnerable applications
            service: Vulnerable service
            rule_id: Rule ID (0-4294967295)
            rev: Revision number (0-4294967295)
            date: Date (0-4294967295)
            metadata: List of metadata dicts with id, metaid, valueid
            vdom: Virtual domain (None=use default, False=skip vdom, or specific vdom)
            **kwargs: Additional parameters

        Returns:
            API response dict

        Examples:
            >>> # Using data_dict
            >>> data = {
            ...     'name': 'sig1',
            ...     'status': 'enable',
            ...     'action': 'block',
            ...     'log': 'enable'
            ... }
            >>> result = fgt.api.cmdb.rule.fmwp.create(data_dict=data)
            >>> 
            >>> # Using explicit parameters
            >>> result = fgt.api.cmdb.rule.fmwp.create(
            ...     name='sig1',
            ...     status='enable',
            ...     action='block',
            ...     log='enable',
            ...     severity='high'
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
        if group is not None:
            data["group"] = group
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
        return self._client.post("cmdb", "rule/fmwp", data=data, vdom=vdom)

    def put(
        self,
        name: str,
        data_dict: Optional[dict[str, Any]] = None,
        status: Optional[str] = None,
        log: Optional[str] = None,
        log_packet: Optional[str] = None,
        action: Optional[str] = None,
        group: Optional[str] = None,
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
        Update FMWP signature.
        
        NOTE: This operation is not supported. FMWP signatures are read-only and 
        managed by FortiGuard Services. This method will return an error.

        Args:
            name: Signature name (required)
            data_dict: Complete signature configuration dictionary
            status: Enable/disable rule. Options: 'disable', 'enable'
            log: Enable/disable logging. Options: 'disable', 'enable'
            log_packet: Enable/disable packet logging. Options: 'disable', 'enable'
            action: Action for matching traffic. Options: 'pass', 'block'
            group: Rule group (max 63 chars)
            severity: Severity level
            location: Vulnerable location
            os: Vulnerable operating systems
            application: Vulnerable applications
            service: Vulnerable service
            rule_id: Rule ID (0-4294967295)
            rev: Revision number (0-4294967295)
            date: Date (0-4294967295)
            metadata: List of metadata dicts with id, metaid, valueid
            vdom: Virtual domain (None=use default, False=skip vdom, or specific vdom)
            **kwargs: Additional parameters to update

        Returns:
            API response dict

        Examples:
            >>> # Using data_dict
            >>> data = {'status': 'disable', 'log': 'disable'}
            >>> result = fgt.api.cmdb.rule.fmwp.update(name='sig1', data_dict=data)
            >>> 
            >>> # Using explicit parameters
            >>> result = fgt.api.cmdb.rule.fmwp.update(
            ...     name='sig1',
            ...     status='disable',
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
        if group is not None:
            data["group"] = group
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
        path = f"rule/fmwp/{encode_path_component(name)}"
        return self._client.put("cmdb", path, data=data, vdom=vdom)

    def delete(self, name: str, vdom: Optional[Union[str, bool]] = None) -> dict[str, Any]:
        """
        Delete FMWP signature.
        
        NOTE: This operation is not supported. FMWP signatures are read-only and 
        managed by FortiGuard Services. This method will return an error.

        Args:
            name: Signature name
            vdom: Virtual domain (None=use default, False=skip vdom, or specific vdom)

        Returns:
            API response dict

        Examples:
            >>> result = fgt.api.cmdb.rule.fmwp.delete(name='sig1')
        """
        path = f"rule/fmwp/{encode_path_component(name)}"
        return self._client.delete("cmdb", path, vdom=vdom)

    def exists(self, name: str, vdom: Optional[Union[str, bool]] = None) -> bool:
        """
        Check if FMWP signature exists.

        Args:
            name: Signature name
            vdom: Virtual domain (None=use default, False=skip vdom, or specific vdom)

        Returns:
            True if signature exists, False otherwise

        Examples:
            >>> if fgt.api.cmdb.rule.fmwp.exists(name='sig1'):
            ...     print("Signature exists")
        """
        try:
            self.get(name=name, vdom=vdom)
            return True
        except Exception:
            return False
