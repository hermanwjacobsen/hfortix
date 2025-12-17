"""
FortiOS CMDB - IPS Sensor

Configure IPS sensor profiles.

API Endpoints:
    GET    /api/v2/cmdb/ips/sensor           - List all / Get specific
    POST   /api/v2/cmdb/ips/sensor           - Create
    PUT    /api/v2/cmdb/ips/sensor/{name}   - Update
    DELETE /api/v2/cmdb/ips/sensor/{name}   - Delete
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional, Union

if TYPE_CHECKING:
    from ...http_client import HTTPClient

from hfortix.FortiOS.http_client import encode_path_component


class Sensor:
    """IPS Sensor endpoint"""

    def __init__(self, client: "HTTPClient") -> None:
        self._client = client

    def list(self, vdom: Optional[Union[str, bool]] = None, **kwargs: Any) -> dict[str, Any]:
        """List all IPS sensors."""
        path = "ips/sensor"
        return self._client.get("cmdb", path, params=kwargs if kwargs else None, vdom=vdom)

    def get(
        self, name: str, vdom: Optional[Union[str, bool]] = None, **kwargs: Any
    ) -> dict[str, Any]:
        """Get specific IPS sensor."""
        path = f"ips/sensor/{encode_path_component(name)}"
        return self._client.get("cmdb", path, params=kwargs if kwargs else None, vdom=vdom)

    def post(
        self,
        data_dict: Optional[dict[str, Any]] = None,
        name: Optional[str] = None,
        comment: Optional[str] = None,
        replacemsg_group: Optional[str] = None,
        block_malicious_url: Optional[str] = None,
        scan_botnet_connections: Optional[str] = None,
        extended_log: Optional[str] = None,
        entries: Optional[list[dict[str, Any]]] = None,
        vdom: Optional[Union[str, bool]] = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Create IPS sensor.

        Args:
            name: Sensor name (max 47 chars)
            comment: Comment (max 255 chars)
            replacemsg_group: Replacement message group (max 35 chars)
            block_malicious_url: Enable/disable malicious URL blocking (disable|enable)
            scan_botnet_connections: Block/monitor connections to Botnet servers (disable|block|monitor)
            extended_log: Enable/disable extended logging (enable|disable)
            entries: IPS sensor filter entries (list of filter objects)
        """
        data = data_dict.copy() if data_dict else {}

        param_map = {
            "name": name,
            "comment": comment,
            "replacemsg-group": replacemsg_group,
            "block-malicious-url": block_malicious_url,
            "scan-botnet-connections": scan_botnet_connections,
            "extended-log": extended_log,
            "entries": entries,
        }

        for key, value in param_map.items():
            if value is not None:
                data[key] = value

        data.update(kwargs)

        path = "ips/sensor"
        return self._client.post("cmdb", path, data=data, vdom=vdom)

    def put(
        self,
        name: str,
        data_dict: Optional[dict[str, Any]] = None,
        comment: Optional[str] = None,
        replacemsg_group: Optional[str] = None,
        block_malicious_url: Optional[str] = None,
        scan_botnet_connections: Optional[str] = None,
        extended_log: Optional[str] = None,
        entries: Optional[list[dict[str, Any]]] = None,
        vdom: Optional[Union[str, bool]] = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Update IPS sensor.

        Args:
            name: Sensor name to update
            comment: Comment (max 255 chars)
            replacemsg_group: Replacement message group (max 35 chars)
            block_malicious_url: Enable/disable malicious URL blocking (disable|enable)
            scan_botnet_connections: Block/monitor connections to Botnet servers (disable|block|monitor)
            extended_log: Enable/disable extended logging (enable|disable)
            entries: IPS sensor filter entries (list of filter objects)
        """
        data = data_dict.copy() if data_dict else {}

        param_map = {
            "comment": comment,
            "replacemsg-group": replacemsg_group,
            "block-malicious-url": block_malicious_url,
            "scan-botnet-connections": scan_botnet_connections,
            "extended-log": extended_log,
            "entries": entries,
        }

        for key, value in param_map.items():
            if value is not None:
                data[key] = value

        data.update(kwargs)

        path = f"ips/sensor/{encode_path_component(name)}"
        return self._client.put("cmdb", path, data=data, vdom=vdom)

    def delete(self, name: str, vdom: Optional[Union[str, bool]] = None) -> dict[str, Any]:
        """Delete IPS sensor."""
        path = f"ips/sensor/{encode_path_component(name)}"
        return self._client.delete("cmdb", path, vdom=vdom)

    def exists(self, name: str, vdom: Optional[Union[str, bool]] = None) -> bool:
        """Check if IPS sensor exists."""
        try:
            self.get(name, vdom=vdom)
            return True
        except Exception:
            return False
