"""FortiOS CMDB - IPS Decoder

Configure IPS decoder.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional, Union

if TYPE_CHECKING:
    from ...http_client import HTTPClient

from hfortix.FortiOS.http_client import encode_path_component


class Decoder:
    def __init__(self, client: "HTTPClient") -> None:
        self._client = client

    def get(
        self, name: Optional[str] = None, vdom: Optional[Union[str, bool]] = None, **kwargs: Any
    ) -> dict[str, Any]:
        """Get IPS decoder(s) - List all or get specific."""
        path = "ips/decoder"
        if name is not None:
            path = f"{path}/{encode_path_component(name)}"
        return self._client.get(
            "cmdb",
            path,
            params=kwargs if kwargs else None,
            vdom=vdom,
        )

    def post(
        self,
        data_dict: Optional[dict[str, Any]] = None,
        name: Optional[str] = None,
        parameter: Optional[list[dict[str, Any]]] = None,
        status: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Create IPS decoder.

        Args:
            name: Decoder name
            parameter: Decoder parameters (list of parameter objects)
            status: Enable/disable decoder (enable|disable)
        """
        data = data_dict.copy() if data_dict else {}

        param_map = {
            "name": name,
            "parameter": parameter,
            "status": status,
        }

        for key, value in param_map.items():
            if value is not None:
                data[key] = value

        data.update(kwargs)
        return self._client.post("cmdb", "ips/decoder", data=data, vdom=vdom)

    def put(
        self,
        name: str,
        data_dict: Optional[dict[str, Any]] = None,
        parameter: Optional[list[dict[str, Any]]] = None,
        status: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Update IPS decoder.

        Args:
            name: Decoder name to update
            parameter: Decoder parameters (list of parameter objects)
            status: Enable/disable decoder (enable|disable)
        """
        data = data_dict.copy() if data_dict else {}

        param_map = {
            "parameter": parameter,
            "status": status,
        }

        for key, value in param_map.items():
            if value is not None:
                data[key] = value

        data.update(kwargs)
        return self._client.put(
            "cmdb", f"ips/decoder/{encode_path_component(name)}", data=data, vdom=vdom
        )

    def delete(self, name: str, vdom: Optional[Union[str, bool]] = None) -> dict[str, Any]:
        return self._client.delete("cmdb", f"ips/decoder/{encode_path_component(name)}", vdom=vdom)

    def exists(self, name: str, vdom: Optional[Union[str, bool]] = None) -> bool:
        try:
            self.get(name, vdom=vdom)
            return True
        except Exception:
            return False
