"""Firewall IP/MAC Binding Table Convenience Wrapper."""

from typing import TYPE_CHECKING, Any, Dict, Optional, Union

from ._helpers import (
    validate_ip_address,
    validate_mac_address,
    validate_seq_num,
    validate_status,
)

if TYPE_CHECKING:
    from collections.abc import Coroutine

    from ..fortios import FortiOS


class IPMACBindingTable:
    """Convenience wrapper for firewall IP/MAC binding table."""

    def __init__(self, fortios_instance: "FortiOS") -> None:
        """Initialize the IPMACBindingTable wrapper."""
        self._fgt = fortios_instance
        self._api = fortios_instance.api.cmdb.firewall.ipmacbinding_table

    def get(
        self,
        seq_num: Optional[Union[str, int]] = None,
        vdom: Optional[str] = None,
        **kwargs: Any,
    ) -> Union[Dict[str, Any], "Coroutine[Any, Any, Dict[str, Any]]"]:
        """Get IP/MAC binding table entries."""
        api_params: dict[str, Any] = {}
        if vdom:
            api_params["vdom"] = vdom
        api_params.update(kwargs)

        if seq_num is not None:
            return self._api.get(str(seq_num), **api_params)
        return self._api.get(**api_params)

    def create(
        self,
        seq_num: Union[str, int],
        ip: str,
        mac: str,
        name: Optional[str] = None,
        status: str = "enable",
        vdom: Optional[str] = None,
        **kwargs: Any,
    ) -> Union[Dict[str, Any], "Coroutine[Any, Any, Dict[str, Any]]"]:
        """Create a new IP/MAC binding entry."""
        validate_seq_num(seq_num, "create")
        validate_ip_address(ip, allow_wildcard=True)
        validate_mac_address(mac, allow_wildcard=True)
        validate_status(status)

        data: dict[str, Any] = {
            "seq-num": int(seq_num),
            "ip": ip,
            "mac": mac,
            "status": status,
        }

        if name:
            if len(name) > 35:
                raise ValueError(
                    f"Name must be 35 characters or less, got {len(name)}"
                )
            data["name"] = name

        api_params: dict[str, Any] = {}
        if vdom:
            api_params["vdom"] = vdom
        api_params.update(kwargs)

        return self._api.post(data, **api_params)

    def update(
        self,
        seq_num: Union[str, int],
        ip: Optional[str] = None,
        mac: Optional[str] = None,
        name: Optional[str] = None,
        status: Optional[str] = None,
        vdom: Optional[str] = None,
        **kwargs: Any,
    ) -> Union[Dict[str, Any], "Coroutine[Any, Any, Dict[str, Any]]"]:
        """Update an existing IP/MAC binding entry."""
        validate_seq_num(seq_num, "update")

        if ip is not None:
            validate_ip_address(ip, allow_wildcard=True)
        if mac is not None:
            validate_mac_address(mac, allow_wildcard=True)
        if status is not None:
            validate_status(status)

        data: dict[str, Any] = {}
        if ip is not None:
            data["ip"] = ip
        if mac is not None:
            data["mac"] = mac
        if name is not None:
            if len(name) > 35:
                raise ValueError(
                    f"Name must be 35 characters or less, got {len(name)}"
                )
            data["name"] = name
        if status is not None:
            data["status"] = status

        api_params: dict[str, Any] = {}
        if vdom:
            api_params["vdom"] = vdom
        api_params.update(kwargs)

        return self._api.put(str(seq_num), data, **api_params)

    def delete(
        self,
        seq_num: Union[str, int],
        vdom: Optional[str] = None,
        **kwargs: Any,
    ) -> Union[Dict[str, Any], "Coroutine[Any, Any, Dict[str, Any]]"]:
        """Delete an IP/MAC binding entry."""
        validate_seq_num(seq_num, "delete")

        api_params: dict[str, Any] = {}
        if vdom:
            api_params["vdom"] = vdom
        api_params.update(kwargs)

        return self._api.delete(str(seq_num), **api_params)

    def exists(
        self, seq_num: Union[str, int], vdom: Optional[str] = None
    ) -> bool:
        """Check if an IP/MAC binding entry exists."""
        try:
            result = self.get(seq_num=seq_num, vdom=vdom)
            return (
                isinstance(result, dict)
                and result.get("http_status") == 200
                and result.get("results") is not None
            )
        except Exception:
            return False

    def enable(
        self, seq_num: Union[str, int], vdom: Optional[str] = None
    ) -> Union[Dict[str, Any], "Coroutine[Any, Any, Dict[str, Any]]"]:
        """Enable an IP/MAC binding entry."""
        return self.update(seq_num=seq_num, status="enable", vdom=vdom)

    def disable(
        self, seq_num: Union[str, int], vdom: Optional[str] = None
    ) -> Union[Dict[str, Any], "Coroutine[Any, Any, Dict[str, Any]]"]:
        """Disable an IP/MAC binding entry."""
        return self.update(seq_num=seq_num, status="disable", vdom=vdom)
