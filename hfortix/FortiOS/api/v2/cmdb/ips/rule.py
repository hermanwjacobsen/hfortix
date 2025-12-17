"""FortiOS CMDB - IPS Rule"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional, Union

if TYPE_CHECKING:
    from ...http_client import HTTPClient

from hfortix.FortiOS.http_client import encode_path_component


class Rule:
    def __init__(self, client: "HTTPClient") -> None:
        self._client = client

    def list(self, vdom: Optional[Union[str, bool]] = None, **kwargs: Any) -> dict[str, Any]:
        return self._client.get("cmdb", "ips/rule", params=kwargs if kwargs else None, vdom=vdom)

    def get(
        self, name: str, vdom: Optional[Union[str, bool]] = None, **kwargs: Any
    ) -> dict[str, Any]:
        return self._client.get(
            "cmdb",
            f"ips/rule/{encode_path_component(name)}",
            params=kwargs if kwargs else None,
            vdom=vdom,
        )

    def create(
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
        metadata: Optional[list[dict[str, Any]]] = None,
        vdom: Optional[Union[str, bool]] = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Create IPS rule.

        Args:
            name: Rule name
            status: Enable/disable rule (enable|disable)
            log: Enable/disable logging (enable|disable)
            log_packet: Enable/disable packet logging (enable|disable)
            action: Action for detected traffic (pass|block|reset|default)
            group: Rule group
            severity: Rule severity
            location: Location (server|client)
            os: Operating systems
            application: Applications
            service: Services
            rule_id: Rule ID
            rev: Revision
            date: Date
            metadata: Metadata (list of metadata objects)
        """
        data = data_dict.copy() if data_dict else {}

        param_map = {
            "name": name,
            "status": status,
            "log": log,
            "log-packet": log_packet,
            "action": action,
            "group": group,
            "severity": severity,
            "location": location,
            "os": os,
            "application": application,
            "service": service,
            "rule-id": rule_id,
            "rev": rev,
            "date": date,
            "metadata": metadata,
        }

        for key, value in param_map.items():
            if value is not None:
                data[key] = value

        data.update(kwargs)
        return self._client.post("cmdb", "ips/rule", data=data, vdom=vdom)

    def update(
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
        metadata: Optional[list[dict[str, Any]]] = None,
        vdom: Optional[Union[str, bool]] = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Update IPS rule.

        Args:
            name: Rule name to update
            status: Enable/disable rule (enable|disable)
            log: Enable/disable logging (enable|disable)
            log_packet: Enable/disable packet logging (enable|disable)
            action: Action for detected traffic (pass|block|reset|default)
            group: Rule group
            severity: Rule severity
            location: Location (server|client)
            os: Operating systems
            application: Applications
            service: Services
            rule_id: Rule ID
            rev: Revision
            date: Date
            metadata: Metadata (list of metadata objects)
        """
        data = data_dict.copy() if data_dict else {}

        param_map = {
            "status": status,
            "log": log,
            "log-packet": log_packet,
            "action": action,
            "group": group,
            "severity": severity,
            "location": location,
            "os": os,
            "application": application,
            "service": service,
            "rule-id": rule_id,
            "rev": rev,
            "date": date,
            "metadata": metadata,
        }

        for key, value in param_map.items():
            if value is not None:
                data[key] = value

        data.update(kwargs)
        return self._client.put(
            "cmdb", f"ips/rule/{encode_path_component(name)}", data=data, vdom=vdom
        )

    def delete(self, name: str, vdom: Optional[Union[str, bool]] = None) -> dict[str, Any]:
        return self._client.delete("cmdb", f"ips/rule/{encode_path_component(name)}", vdom=vdom)

    def exists(self, name: str, vdom: Optional[Union[str, bool]] = None) -> bool:
        try:
            self.get(name, vdom=vdom)
            return True
        except Exception:
            return False
